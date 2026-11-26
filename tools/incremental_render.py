"""Incremental Quarto site renderer for StatWiki.

Compares the freshly generated ``.qmd`` inputs, ``_quarto.yml``, HTML/SCSS
template includes, post-render scripts, and static resources against the cached
manifest in ``_build/incremental-manifest.json`` alongside a warm ``_site/``
and ``.quarto/`` directory.

- When global chrome, sidebar navigation, theme SCSS, template includes, Quarto
  version, or post-render scripts change (or no valid warm cache exists), wipes
  ``_site/`` and ``.quarto/`` and runs a clean full ``quarto render``.
- When only ``1 .. max_incremental_files`` ``.qmd`` pages change, prunes any
  deleted pages/aliases/resources, resets collision-prefixed search descriptions
  so ``search_meta.py`` stays idempotent, renders ``f_1 .. f_{k-1}`` without
  repeating ``post-render``, and renders ``f_k`` with the full ``_quarto.yml``
  so all post-render passes execute once.
- When zero ``.qmd`` pages change and only static resources change (for example
  ``styles.css``, ``labs/*.js``, or ``ask/widget/dist/*``), renders ``404.qmd``
  so Quarto syncs project resources and runs ``post-render`` in a few seconds.
- When nothing renderable changed at all, skips ``quarto render`` and refreshes
  ``_site/wiki.json``'s modification time so ``wait-for-wiki.sh`` accepts the
  deployed ``wiki.json``.
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import html
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import time
from collections.abc import Iterable
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1
DEFAULT_MAX_INCREMENTAL_FILES = 250

SKIP_TOP_DIRS = frozenset(
    {
        "_build",
        ".quarto",
        "_publish",
        "sources",
        ".git",
        ".github",
        ".claude",
        "ask",
        "webr",
        "node_modules",
        "__pycache__",
    }
)

# Optional post-render companion files that are not listed directly in
# _quarto.yml's post-render array (or may be added by upcoming PRs such as
# accessible tables and build-time KaTeX rendering). Recording whether each
# exists and its SHA-256 ensures that adding, editing, or removing one
# invalidates the warm cache automatically.
POST_RENDER_COMPANIONS = (
    "table_a11y.py",
    "page_a11y.py",
    "tools/prerender_math.mjs",
    "katex_macros.json",
    "katex/katex.min.js",
    "katex/katex.min.css",
)

INCLUDE_SHORTCODE_RE = re.compile(r"\{\{<\s*include\s+([^\s>]+)\s*>\}\}")
LOCAL_FIGURE_REF_RE = re.compile(r'(?:\]\(|src=["\'])((?:\.\./|\./)*figures/[^)"\'?#\s]+)')
FRONTMATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?\r?\n)---[ \t]*(?:\r?\n|\Z)", re.S)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path, cache: dict[Path, str] | None = None) -> str:
    resolved = path.resolve()
    if cache is not None and resolved in cache:
        return cache[resolved]
    digest = sha256_bytes(resolved.read_bytes())
    if cache is not None:
        cache[resolved] = digest
    return digest


def _unquote_yaml_scalar(raw: str) -> str:
    val = raw.strip()
    if not val:
        return ""
    if val[0] == '"' and val.endswith('"') and len(val) >= 2:
        try:
            return json.loads(val)
        except json.JSONDecodeError:
            return val[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    if val[0] == "'" and val.endswith("'") and len(val) >= 2:
        return val[1:-1].replace("''", "'")
    # Strip inline comment when unquoted.
    comment = re.search(r"\s+#", val)
    if comment:
        val = val[: comment.start()].rstrip()
    return val


def parse_quarto_config(quarto_yml_text: str) -> dict[str, Any]:
    """Extract the fields needed for dependency tracking from ``_quarto.yml``
    using pure standard-library parsing (CI's build job does not install PyYAML).
    """
    lines = quarto_yml_text.splitlines()
    output_dir = "_site"
    site_url = "https://www.statwiki.io"
    site_description = ""
    favicon = ""
    css_files: list[str] = []
    post_render: list[str] = []
    resources: list[str] = []
    includes: list[str] = []
    scss_files: list[str] = []
    sidebar_qmds: list[str] = []

    stack: list[tuple[int, str]] = []

    def current_path() -> tuple[str, ...]:
        return tuple(name for _indent, name in stack)

    for raw_line in lines:
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))

        while stack and stack[-1][0] >= indent and not stripped.startswith("- "):
            stack.pop()
        while stack and stack[-1][0] > indent and stripped.startswith("- "):
            stack.pop()

        path = current_path()

        if stripped.startswith("- "):
            item_body = stripped[2:].strip()
            if path == ("project", "post-render"):
                val = _unquote_yaml_scalar(item_body)
                if val:
                    post_render.append(val)
            elif path == ("project", "resources"):
                val = _unquote_yaml_scalar(item_body)
                if val:
                    resources.append(val)
            elif path in (
                ("format", "html", "include-in-header"),
                ("format", "html", "include-before-body"),
                ("format", "html", "include-after-body"),
            ):
                val = _unquote_yaml_scalar(item_body)
                if val:
                    includes.append(val)
            elif path == ("format", "html", "css"):
                val = _unquote_yaml_scalar(item_body)
                if val:
                    css_files.append(val)
            elif len(path) >= 2 and path[:2] == ("website", "sidebar"):
                if item_body.startswith("href:"):
                    href = _unquote_yaml_scalar(item_body.split(":", 1)[1])
                    if href.endswith(".qmd"):
                        sidebar_qmds.append(href)
                elif ":" not in item_body:
                    href = _unquote_yaml_scalar(item_body)
                    if href.endswith(".qmd"):
                        sidebar_qmds.append(href)
            continue

        if ":" in stripped:
            key, rest = stripped.split(":", 1)
            key = key.strip()
            rest_clean = rest.strip()
            # Inline bracket list such as `light: [cosmo, theme.scss]`
            if rest_clean.startswith("[") and rest_clean.endswith("]"):
                inner = rest_clean[1:-1]
                items = [_unquote_yaml_scalar(part) for part in inner.split(",") if part.strip()]
                full_key = (*path, key)
                if len(full_key) >= 3 and full_key[:3] == ("format", "html", "theme"):
                    for item in items:
                        if item.endswith(".scss") and item not in scss_files:
                            scss_files.append(item)
                continue

            if not rest_clean or rest_clean.startswith("#"):
                stack.append((indent, key))
                continue

            scalar = _unquote_yaml_scalar(rest_clean)
            full_key = (*path, key)
            if full_key == ("project", "output-dir"):
                output_dir = scalar or "_site"
            elif full_key == ("website", "site-url"):
                site_url = scalar.rstrip("/")
            elif full_key == ("website", "description"):
                site_description = scalar
            elif full_key == ("website", "favicon"):
                if scalar:
                    favicon = scalar
            elif full_key == ("format", "html", "css"):
                if scalar:
                    css_files.append(scalar)
            elif full_key in (
                ("format", "html", "include-in-header"),
                ("format", "html", "include-before-body"),
                ("format", "html", "include-after-body"),
            ):
                if scalar:
                    includes.append(scalar)
            elif full_key == ("format", "html", "theme"):
                if scalar.endswith(".scss") and scalar not in scss_files:
                    scss_files.append(scalar)
            elif len(path) >= 2 and path[:2] == ("website", "sidebar") and key == "href":
                if scalar.endswith(".qmd"):
                    sidebar_qmds.append(scalar)

    return {
        "output_dir": output_dir,
        "site_url": site_url,
        "site_description": site_description,
        "favicon": favicon,
        "css_files": css_files,
        "post_render": post_render,
        "resources": resources,
        "includes": includes,
        "scss_files": scss_files,
        "sidebar_qmds": sidebar_qmds,
    }


def strip_post_render_block(quarto_yml_text: str) -> str:
    """Return ``_quarto.yml`` without ``project.post-render`` so multi-file
    incremental batches run post-render once on the final file.
    """
    lines = quarto_yml_text.splitlines(keepends=True)
    out: list[str] = []
    in_project = False
    project_indent = 0
    skipping_post_render = False
    post_render_indent = 0

    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))

        if skipping_post_render:
            if (
                not stripped
                or stripped.startswith("#")
                or indent > post_render_indent
                or (indent == post_render_indent and stripped.startswith("- "))
            ):
                continue
            skipping_post_render = False

        if stripped and not stripped.startswith("#"):
            if indent == 0 and stripped.startswith("project:"):
                in_project = True
                project_indent = 0
            elif indent <= project_indent and not stripped.startswith("- "):
                in_project = False

            if in_project and re.match(r"^post-render:\s*(?:#.*)?$", stripped):
                skipping_post_render = True
                post_render_indent = indent
                continue

        out.append(line)

    return "".join(out)


def parse_frontmatter(qmd_text: str, rel_qmd: str) -> dict[str, Any]:
    """Extract ``title``, ``description``, and normalized ``aliases`` from a
    ``.qmd`` file's YAML frontmatter.
    """
    match = FRONTMATTER_RE.match(qmd_text)
    if not match:
        return {"title": "", "description": None, "aliases": []}

    fm_lines = match.group(1).splitlines()
    title = ""
    description: str | None = None
    raw_aliases: list[str] = []
    in_aliases = False
    aliases_indent = 0

    for raw_line in fm_lines:
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        if in_aliases:
            if indent >= aliases_indent and stripped.startswith("- "):
                val = _unquote_yaml_scalar(stripped[2:])
                if val:
                    raw_aliases.append(val)
                continue
            in_aliases = False

        if indent == 0 and ":" in stripped:
            key, rest = stripped.split(":", 1)
            key = key.strip()
            rest_clean = rest.strip()
            if key == "title" and rest_clean:
                title = _unquote_yaml_scalar(rest_clean)
            elif key == "description" and rest_clean:
                description = _unquote_yaml_scalar(rest_clean)
            elif key == "aliases":
                if rest_clean.startswith("[") and rest_clean.endswith("]"):
                    inner = rest_clean[1:-1]
                    for part in inner.split(","):
                        if part.strip():
                            raw_aliases.append(_unquote_yaml_scalar(part))
                elif not rest_clean or rest_clean.startswith("#"):
                    in_aliases = True
                    aliases_indent = indent

    qmd_parent = Path(rel_qmd).parent
    norm_aliases: list[str] = []
    for alias in raw_aliases:
        clean = alias.split("#", 1)[0].split("?", 1)[0].strip()
        if not clean:
            continue
        if clean.startswith("/"):
            rel_alias = clean.lstrip("/")
        else:
            rel_alias = os.path.normpath((qmd_parent / clean).as_posix()).replace("\\", "/")
        if not rel_alias.startswith("../") and rel_alias != ".":
            norm_aliases.append(rel_alias)

    return {
        "title": title,
        "description": description,
        "aliases": sorted(set(norm_aliases)),
    }


def discover_renderable_qmds(root: Path, output_dir: str) -> list[str]:
    """Find every renderable ``.qmd`` under ``root``, matching Quarto's render
    rules in ``_quarto.yml`` (``*.qmd``, ``!labs/_*.qmd``, ``!sources/``).
    """
    skip_dirs = set(SKIP_TOP_DIRS) | {output_dir.strip("/")}
    found: list[str] = []

    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = Path(dirpath).relative_to(root)
        is_root = rel_dir == Path(".")
        kept_dirs: list[str] = []
        for d in sorted(dirnames):
            if d.startswith(".") or d.startswith("_"):
                continue
            if is_root and d in skip_dirs:
                continue
            kept_dirs.append(d)
        dirnames[:] = kept_dirs

        for fname in sorted(filenames):
            if not fname.endswith(".qmd"):
                continue
            if fname.startswith(".") or fname.startswith("_"):
                continue
            rel_posix = (rel_dir / fname).as_posix() if not is_root else fname
            found.append(rel_posix)

    found.sort()
    return found


def _effective_qmd_hash(
    root: Path,
    qmd_path: Path,
    qmd_bytes: bytes,
    qmd_text: str,
    file_hash_cache: dict[Path, str],
    seen_includes: frozenset[Path] = frozenset(),
) -> str:
    """Hash a ``.qmd`` file together with any ``{{< include ... >}}`` partials
    and local ``figures/...`` files it references so asset or partial updates
    invalidate the referencing page.
    """
    resolved = qmd_path.resolve()
    parts = [b"QMD\0", sha256_bytes(qmd_bytes).encode("ascii"), b"\0"]

    for inc_match in INCLUDE_SHORTCODE_RE.finditer(qmd_text):
        inc_rel = inc_match.group(1).strip().strip("\"'")
        inc_path = (qmd_path.parent / inc_rel).resolve()
        if inc_path in seen_includes:
            continue
        try:
            inc_path.relative_to(root.resolve())
        except ValueError:
            continue
        if inc_path.is_file():
            inc_bytes = inc_path.read_bytes()
            inc_text = inc_bytes.decode("utf-8", errors="replace")
            inc_digest = _effective_qmd_hash(
                root,
                inc_path,
                inc_bytes,
                inc_text,
                file_hash_cache,
                seen_includes | {resolved},
            )
            parts.extend([b"INC:", inc_rel.encode("utf-8"), b"=", inc_digest.encode("ascii"), b"\0"])

    fig_refs: set[str] = set()
    for fig_match in LOCAL_FIGURE_REF_RE.finditer(qmd_text):
        fig_refs.add(fig_match.group(1))
    for fig_rel in sorted(fig_refs):
        fig_path = (qmd_path.parent / fig_rel).resolve()
        try:
            root_rel = fig_path.relative_to(root.resolve()).as_posix()
        except ValueError:
            continue
        if fig_path.is_file():
            fig_digest = sha256_file(fig_path, file_hash_cache)
            parts.extend([b"FIG:", root_rel.encode("utf-8"), b"=", fig_digest.encode("ascii"), b"\0"])

    return sha256_bytes(b"".join(parts))


def collect_qmds_state(
    root: Path, renderable_qmds: list[str], file_hash_cache: dict[Path, str]
) -> dict[str, dict[str, Any]]:
    state: dict[str, dict[str, Any]] = {}
    for rel_qmd in renderable_qmds:
        path = root / rel_qmd
        raw_bytes = path.read_bytes()
        text = raw_bytes.decode("utf-8", errors="replace")
        meta = parse_frontmatter(text, rel_qmd)
        digest = _effective_qmd_hash(root, path, raw_bytes, text, file_hash_cache)
        state[rel_qmd] = {
            "sha256": digest,
            "title": meta["title"],
            "description": meta["description"],
            "aliases": meta["aliases"],
        }
    return state


def expand_static_resources(
    root: Path,
    config: dict[str, Any],
    renderable_qmds: set[str],
    file_hash_cache: dict[Path, str],
) -> dict[str, str]:
    """Expand ``project.resources``, ``format.html.css``, and ``website.favicon``
    into ``{rel_posix: sha256}``.
    """
    output_dir = config["output_dir"].strip("/")
    excluded_roots = {output_dir, "_build", ".quarto", "_publish", ".git"}
    patterns: list[str] = []
    if config["favicon"]:
        patterns.append(config["favicon"].lstrip("/"))
    for css in config["css_files"]:
        if not css.startswith(("http://", "https://")):
            patterns.append(css.lstrip("/"))
    for res in config["resources"]:
        clean = res.lstrip("/")
        if clean and not clean.startswith("!"):
            patterns.append(clean)

    matched_paths: set[Path] = set()
    root_resolved = root.resolve()

    for pat in patterns:
        candidate = root / pat
        if pat.endswith("/") or (candidate.exists() and candidate.is_dir()):
            dir_target = root / pat.rstrip("/")
            if dir_target.is_dir():
                for sub in dir_target.rglob("*"):
                    if sub.is_file():
                        matched_paths.add(sub.resolve())
        elif any(ch in pat for ch in "*?["):
            for hit in glob.glob(str(root / pat), recursive=True):
                hit_path = Path(hit)
                if hit_path.is_file():
                    matched_paths.add(hit_path.resolve())
                elif hit_path.is_dir():
                    for sub in hit_path.rglob("*"):
                        if sub.is_file():
                            matched_paths.add(sub.resolve())
        elif candidate.is_file():
            matched_paths.add(candidate.resolve())

    resources_map: dict[str, str] = {}
    for abs_path in sorted(matched_paths):
        try:
            rel_posix = abs_path.relative_to(root_resolved).as_posix()
        except ValueError:
            continue
        top = rel_posix.split("/", 1)[0]
        if top in excluded_roots or rel_posix in renderable_qmds or rel_posix.endswith(".qmd"):
            continue
        resources_map[rel_posix] = sha256_file(abs_path, file_hash_cache)

    return resources_map


def get_quarto_version(quarto_bin: str = "quarto") -> str:
    res = subprocess.run(
        [quarto_bin, "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    return res.stdout.strip()


def compute_global_signature(
    root: Path,
    quarto_yml_bytes: bytes,
    config: dict[str, Any],
    quarto_version: str,
    file_hash_cache: dict[Path, str],
) -> dict[str, Any]:
    template_hashes: dict[str, str] = {}
    for rel in sorted(set(config["includes"]) | set(config["scss_files"])):
        target = root / rel
        template_hashes[rel] = sha256_file(target, file_hash_cache) if target.is_file() else "<missing>"

    post_render_hashes: dict[str, str] = {}
    tracked_scripts = set(config["post_render"]) | set(POST_RENDER_COMPANIONS)
    for rel in sorted(tracked_scripts):
        target = root / rel
        post_render_hashes[rel] = sha256_file(target, file_hash_cache) if target.is_file() else "<missing>"

    return {
        "schema_version": SCHEMA_VERSION,
        "quarto_version": quarto_version,
        "quarto_yml_sha256": sha256_bytes(quarto_yml_bytes),
        "template_files": template_hashes,
        "post_render_files": post_render_hashes,
    }


def _load_search_meta_module(root: Path):
    script = root / "search_meta.py"
    if not script.is_file():
        return None
    spec = importlib.util.spec_from_file_location("_statwiki_search_meta", script)
    if spec is None or spec.loader is None:
        return None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _specific_frontmatter_qmds(
    qmds_state: dict[str, dict[str, Any]], site_description: str, search_meta_mod: Any
) -> set[str]:
    """HTML paths whose ``.qmd`` carries a unique, valid frontmatter
    ``description`` that ``search_meta.py`` preserves verbatim.
    """
    counts: dict[str, int] = {}
    for info in qmds_state.values():
        desc = info.get("description")
        if desc:
            counts[desc] = counts.get(desc, 0) + 1

    shortest = getattr(search_meta_mod, "SHORTEST", 50) if search_meta_mod else 50
    banned = getattr(search_meta_mod, "BANNED", None) if search_meta_mod else None

    specific_html: set[str] = set()
    for rel_qmd, info in qmds_state.items():
        desc = info.get("description")
        if (
            desc
            and counts.get(desc, 0) == 1
            and len(desc) >= shortest
            and desc != site_description
            and (banned is None or not banned.search(desc))
        ):
            specific_html.add(rel_qmd[:-4] + ".html")
    return specific_html


def _set_html_descriptions(html_text: str, description: str) -> str:
    escaped = html.escape(description, quote=True)
    html_text = re.sub(
        r'<meta name="description" content="[^"]*">',
        lambda _: f'<meta name="description" content="{escaped}">',
        html_text,
        count=1,
    )
    html_text = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        lambda _: f'<meta property="og:description" content="{escaped}">',
        html_text,
        count=1,
    )
    html_text = re.sub(
        r'<meta name="twitter:description" content="[^"]*">',
        lambda _: f'<meta name="twitter:description" content="{escaped}">',
        html_text,
        count=1,
    )
    return html_text


def reset_prefixed_meta_pages(
    site_dir: Path,
    prefixed_pages: list[str],
    skip_html: set[str],
    qmds_state: dict[str, dict[str, Any]],
    site_description: str,
) -> None:
    """Reset ``<meta name="description">`` to its raw pre-``search_meta.py``
    value on cached pages whose description was collision-prefixed in the
    previous build so ``search_meta.py`` re-evaluates collisions cleanly.
    """
    for rel_html in prefixed_pages:
        if rel_html in skip_html:
            continue
        page = site_dir / rel_html
        if not page.is_file():
            continue
        rel_qmd = rel_html[:-5] + ".qmd" if rel_html.endswith(".html") else ""
        fm_desc = (qmds_state.get(rel_qmd) or {}).get("description")
        raw_desc = fm_desc if fm_desc else site_description
        if not raw_desc:
            continue
        text = page.read_text(encoding="utf-8")
        updated = _set_html_descriptions(text, raw_desc)
        if updated != text:
            page.write_text(updated, encoding="utf-8")


def detect_prefixed_meta_pages(
    site_dir: Path,
    candidate_html_rels: set[str] | None,
    specific_frontmatter_html: set[str],
    qmds_state: dict[str, dict[str, Any]],
    search_meta_mod: Any,
    previous_prefixed: set[str] | None = None,
) -> list[str]:
    """Identify HTML pages where ``search_meta.py`` disambiguated a shared
    description (so ``existing_description`` differs from its uncollided base).
    """
    if search_meta_mod is None or not site_dir.is_dir():
        return []

    prefixed = set(previous_prefixed or ())
    if candidate_html_rels is None:
        targets = [
            p.relative_to(site_dir).as_posix()
            for p in sorted(site_dir.rglob("*.html"))
            if "site_libs" not in p.parts
        ]
    else:
        targets = sorted(candidate_html_rels)

    for rel_html in targets:
        prefixed.discard(rel_html)
        if rel_html == "index.html":
            continue
        page = site_dir / rel_html
        if not page.is_file():
            continue
        text = page.read_text(encoding="utf-8")
        if "<title>Redirect</title>" in text and "var redirects" in text:
            continue
        actual = search_meta_mod.existing_description(text)
        if rel_html in specific_frontmatter_html:
            rel_qmd = rel_html[:-5] + ".qmd"
            base = (qmds_state.get(rel_qmd) or {}).get("description")
        else:
            base = search_meta_mod.describe(rel_html, text)
        if actual and base and actual != base:
            prefixed.add(rel_html)

    return sorted(prefixed)


def _snapshot_html_stats(site_dir: Path) -> dict[str, tuple[int, int]]:
    stats: dict[str, tuple[int, int]] = {}
    if not site_dir.is_dir():
        return stats
    for path in site_dir.rglob("*.html"):
        if "site_libs" in path.parts or not path.is_file():
            continue
        st = path.stat()
        stats[path.relative_to(site_dir).as_posix()] = (st.st_mtime_ns, st.st_size)
    return stats


def _remove_file_and_empty_parents(target: Path, stop_dir: Path) -> None:
    if target.is_file() or target.is_symlink():
        target.unlink()
    parent = target.parent
    stop_resolved = stop_dir.resolve()
    while parent.exists() and parent.resolve() != stop_resolved:
        try:
            parent.rmdir()
        except OSError:
            break
        parent = parent.parent


def _search_entry_page_path(entry: dict[str, Any]) -> str:
    raw = str(entry.get("href") or entry.get("objectID") or "")
    return raw.split("#", 1)[0].split("?", 1)[0].lstrip("/")


def quarto_output_page_order(renderable_qmds: Iterable[str]) -> list[str]:
    """Reproduce Quarto 1.6.40's deterministic ``defaultPandocRenderer`` page
    ordering (``renderedFiles.push(file); renderedFiles.reverse()`` across
    sorted project inputs, excluding ``404.html``).
    """
    order: list[str] = []
    for rel_qmd in renderable_qmds:
        order.append(rel_qmd[:-4] + ".html")
        order.reverse()
    return [rel_html for rel_html in order if rel_html != "404.html"]


def _qmd_iso_lastmod(path: Path) -> str:
    ms = path.stat().st_mtime_ns // 1_000_000
    dt = datetime.fromtimestamp(ms / 1000.0, tz=timezone.utc)
    return f"{dt:%Y-%m-%dT%H:%M:%S}.{ms % 1000:03d}Z"


def canonicalize_search_and_sitemap(
    root: Path,
    site_dir: Path,
    site_url: str,
    renderable_qmds: list[str],
) -> None:
    """Order ``_site/search.json`` and ``_site/sitemap.xml`` identically to a
    clean full ``quarto render`` of the current workspace tree.
    """
    expected_pages = quarto_output_page_order(renderable_qmds)

    search_json = site_dir / "search.json"
    if search_json.is_file():
        raw_search = search_json.read_text(encoding="utf-8")
        entries = json.loads(raw_search)
        by_page: dict[str, list[dict[str, Any]]] = {}
        for entry in entries:
            by_page.setdefault(_search_entry_page_path(entry), []).append(entry)
        ordered_entries: list[dict[str, Any]] = []
        for rel_html in expected_pages:
            if rel_html in by_page:
                ordered_entries.extend(by_page.pop(rel_html))
        for leftover in by_page.values():
            ordered_entries.extend(leftover)
        # Quarto's Deno writer calls JSON.stringify(docs, undefined, 2) with no trailing newline.
        formatted_search = json.dumps(ordered_entries, ensure_ascii=False, indent=2)
        if formatted_search != raw_search:
            search_json.write_text(formatted_search, encoding="utf-8")

    sitemap_xml = site_dir / "sitemap.xml"
    if sitemap_xml.is_file():
        raw_sm = sitemap_xml.read_text(encoding="utf-8")
        base = site_url.rstrip("/") + "/"
        url_blocks = re.findall(r"<url>\s*(.*?)\s*</url>", raw_sm, flags=re.S)
        if url_blocks:
            has_lastmod = any("<lastmod>" in blk for blk in url_blocks)
            blocks_by_rel: dict[str, tuple[str, str]] = {}
            extra_blocks: list[str] = []
            for blk in url_blocks:
                loc_m = re.search(r"<loc>(.*?)</loc>", blk, flags=re.S)
                if not loc_m:
                    continue
                loc = html.unescape(loc_m.group(1).strip())
                if loc in (base, base + "index.html"):
                    rel_html = "index.html"
                    canon_loc = base
                elif loc.startswith(base):
                    rel_html = loc[len(base) :]
                    canon_loc = loc
                else:
                    extra_blocks.append(f"  <url>\n    {blk}\n  </url>")
                    continue
                blocks_by_rel[rel_html] = (canon_loc, blk)

            out_lines = [
                '<?xml version="1.0" encoding="UTF-8"?>',
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
            ]
            for rel_html in expected_pages:
                if rel_html not in blocks_by_rel:
                    continue
                canon_loc, orig_blk = blocks_by_rel.pop(rel_html)
                escaped_loc = html.escape(canon_loc, quote=False)
                if has_lastmod:
                    qmd_path = root / (rel_html[:-5] + ".qmd")
                    if qmd_path.is_file():
                        lastmod = _qmd_iso_lastmod(qmd_path)
                    else:
                        lm_m = re.search(r"<lastmod>(.*?)</lastmod>", orig_blk, flags=re.S)
                        lastmod = lm_m.group(1).strip() if lm_m else _qmd_iso_lastmod(site_dir / rel_html)
                    out_lines.append("  <url>")
                    out_lines.append(f"    <loc>{escaped_loc}</loc>")
                    out_lines.append(f"    <lastmod>{lastmod}</lastmod>")
                    out_lines.append("  </url>")
                else:
                    out_lines.append("  <url>")
                    out_lines.append(f"    <loc>{escaped_loc}</loc>")
                    out_lines.append("  </url>")

            for canon_loc, orig_blk in blocks_by_rel.values():
                escaped_loc = html.escape(canon_loc, quote=False)
                lm_m = re.search(r"<lastmod>(.*?)</lastmod>", orig_blk, flags=re.S)
                out_lines.append("  <url>")
                out_lines.append(f"    <loc>{escaped_loc}</loc>")
                if has_lastmod and lm_m:
                    out_lines.append(f"    <lastmod>{lm_m.group(1).strip()}</lastmod>")
                out_lines.append("  </url>")

            out_lines.extend(extra_blocks)
            out_lines.append("</urlset>")
            formatted_sm = "\n".join(out_lines) + "\n"
            if formatted_sm != raw_sm:
                sitemap_xml.write_text(formatted_sm, encoding="utf-8")


def prune_deleted_artifacts(
    site_dir: Path,
    quarto_dir: Path,
    site_url: str,
    deleted_qmds: set[str],
    prev_qmds: dict[str, dict[str, Any]],
    curr_qmds: dict[str, dict[str, Any]],
    deleted_resources: set[str],
    curr_resources: dict[str, str],
    rerendered_qmds: Iterable[str] = (),
) -> bool:
    """Remove stale outputs for deleted ``.qmd`` files, dropped frontmatter
    ``aliases``, and deleted static resources, and drop all ``search.json``
    entries (including ``#section`` fragments) for pages about to be
    rerendered so renamed or deleted headings never linger. Returns True if
    anything was pruned from ``_site/``.
    """
    pruned_any = False

    # Active HTML files and aliases that must not be deleted.
    protected_site_files: set[str] = set(curr_resources)
    for rel_qmd, info in curr_qmds.items():
        protected_site_files.add(rel_qmd[:-4] + ".html")
        protected_site_files.update(info.get("aliases") or ())

    for rel_res in sorted(deleted_resources):
        if rel_res not in protected_site_files:
            target = site_dir / rel_res
            if target.exists():
                _remove_file_and_empty_parents(target, site_dir)
                pruned_any = True

    deleted_htmls: set[str] = set()
    stale_aliases: set[str] = set()

    for rel_qmd in sorted(deleted_qmds):
        rel_html = rel_qmd[:-4] + ".html"
        deleted_htmls.add(rel_html)
        prev_info = prev_qmds.get(rel_qmd) or {}
        stale_aliases.update(prev_info.get("aliases") or ())
        idx_file = quarto_dir / "idx" / f"{rel_qmd}.json"
        if idx_file.exists():
            _remove_file_and_empty_parents(idx_file, quarto_dir)

    for rel_qmd, curr_info in curr_qmds.items():
        prev_info = prev_qmds.get(rel_qmd)
        if not prev_info:
            continue
        dropped = set(prev_info.get("aliases") or ()) - set(curr_info.get("aliases") or ())
        stale_aliases.update(dropped)

    for rel_target in sorted(deleted_htmls | stale_aliases):
        if rel_target not in protected_site_files:
            target = site_dir / rel_target
            if target.exists():
                _remove_file_and_empty_parents(target, site_dir)
                pruned_any = True

    rerendered_htmls = {rel_qmd[:-4] + ".html" for rel_qmd in rerendered_qmds}
    search_drop_htmls = deleted_htmls | rerendered_htmls
    if search_drop_htmls:
        search_json = site_dir / "search.json"
        if search_json.is_file():
            entries = json.loads(search_json.read_text(encoding="utf-8"))
            filtered = [
                entry
                for entry in entries
                if str(entry.get("href") or "").split("#", 1)[0].split("?", 1)[0].lstrip("/")
                not in search_drop_htmls
                and str(entry.get("objectID") or "").split("#", 1)[0].split("?", 1)[0].lstrip("/")
                not in search_drop_htmls
            ]
            if len(filtered) != len(entries):
                search_json.write_text(
                    json.dumps(filtered, ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )
                pruned_any = True

    if deleted_htmls:
        sitemap_xml = site_dir / "sitemap.xml"
        if sitemap_xml.is_file():
            sm_text = sitemap_xml.read_text(encoding="utf-8")
            updated_sm = sm_text
            base = site_url.rstrip("/") + "/"
            for rel_html in sorted(deleted_htmls):
                loc_url = re.escape(base + rel_html)
                updated_sm = re.sub(
                    rf"\s*<url>\s*<loc>{loc_url}</loc>.*?</url>",
                    "",
                    updated_sm,
                    flags=re.S,
                )
            if updated_sm != sm_text:
                sitemap_xml.write_text(updated_sm, encoding="utf-8")
                pruned_any = True

    return pruned_any


def _sidebar_title_neighbors(
    prev_qmds: dict[str, dict[str, Any]],
    curr_qmds: dict[str, dict[str, Any]],
    sidebar_qmds: list[str],
) -> set[str]:
    """If a sidebar page's frontmatter ``title`` changed without changing
    ``_quarto.yml`` (e.g. a bare-path sidebar item), return ``index.qmd`` plus
    its immediate prev/next sidebar neighbors so ``sidebar-nav.js`` and
    ``page-navigation`` links stay fresh.
    """
    extra: set[str] = set()
    if not sidebar_qmds:
        return extra
    index_by_qmd = {rel: idx for idx, rel in enumerate(sidebar_qmds)}
    for rel_qmd, curr_info in curr_qmds.items():
        if rel_qmd not in index_by_qmd:
            continue
        prev_info = prev_qmds.get(rel_qmd)
        if prev_info and prev_info.get("title") != curr_info.get("title"):
            if "index.qmd" in curr_qmds:
                extra.add("index.qmd")
            pos = index_by_qmd[rel_qmd]
            if pos > 0 and sidebar_qmds[pos - 1] in curr_qmds:
                extra.add(sidebar_qmds[pos - 1])
            if pos + 1 < len(sidebar_qmds) and sidebar_qmds[pos + 1] in curr_qmds:
                extra.add(sidebar_qmds[pos + 1])
    return extra


def sync_fresh_wiki_json(root: Path, site_dir: Path) -> None:
    """Copy ``wiki.json`` into ``_site/wiki.json`` with a fresh timestamp so
    ``wait-for-wiki.sh`` observes ``Last-Modified >= PUBLISH_STARTED`` even when
    zero pages needed rendering.
    """
    src = root / "wiki.json"
    if not src.is_file() or not site_dir.is_dir():
        return
    dst = site_dir / "wiki.json"
    shutil.copy2(src, dst)
    now = time.time()
    os.utime(dst, (now, now))


def warm_cache_usable(
    site_dir: Path,
    quarto_dir: Path,
    prev_manifest: dict[str, Any] | None,
    curr_global_sig: dict[str, Any],
    has_sidebar_share: bool,
) -> tuple[bool, str]:
    if prev_manifest is None:
        return False, "no previous incremental manifest"
    if prev_manifest.get("schema_version") != SCHEMA_VERSION:
        return False, "manifest schema version changed"
    if prev_manifest.get("global_signature") != curr_global_sig:
        prev_sig = prev_manifest.get("global_signature") or {}
        for key in ("quarto_version", "quarto_yml_sha256", "template_files", "post_render_files"):
            if prev_sig.get(key) != curr_global_sig.get(key):
                return False, f"global input changed ({key})"
        return False, "global signature changed"
    if not site_dir.is_dir():
        return False, "missing _site directory"
    if not quarto_dir.is_dir():
        return False, "missing .quarto directory"
    required = ["index.html", "search.json", "sitemap.xml"]
    if has_sidebar_share:
        required.append("sidebar-nav.js")
    for req in required:
        if not (site_dir / req).is_file():
            return False, f"missing _site/{req}"
    return True, "warm cache valid"


def _write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def run_incremental_render(
    root: Path,
    *,
    manifest_path: Path | None = None,
    summary_path: Path | None = None,
    quarto_bin: str = "quarto",
    max_incremental_files: int = DEFAULT_MAX_INCREMENTAL_FILES,
    force_full: bool = False,
    dry_run: bool = False,
) -> dict[str, Any]:
    start_time = time.monotonic()
    root = root.resolve()
    quarto_yml_path = root / "_quarto.yml"
    if not quarto_yml_path.is_file():
        raise SystemExit(f"Missing {quarto_yml_path}")

    if manifest_path is None:
        manifest_path = root / "_build" / "incremental-manifest.json"
    if summary_path is None:
        summary_path = root / "_build" / "incremental-summary.json"

    quarto_yml_bytes = quarto_yml_path.read_bytes()
    quarto_yml_text = quarto_yml_bytes.decode("utf-8")
    config = parse_quarto_config(quarto_yml_text)
    site_dir = root / config["output_dir"]
    quarto_dir = root / ".quarto"

    file_hash_cache: dict[Path, str] = {}
    q_version = get_quarto_version(quarto_bin)
    curr_global_sig = compute_global_signature(
        root, quarto_yml_bytes, config, q_version, file_hash_cache
    )
    renderable_qmds = discover_renderable_qmds(root, config["output_dir"])
    curr_qmds = collect_qmds_state(root, renderable_qmds, file_hash_cache)
    curr_resources = expand_static_resources(
        root, config, set(renderable_qmds), file_hash_cache
    )

    prev_manifest: dict[str, Any] | None = None
    if manifest_path.is_file():
        try:
            prev_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            prev_manifest = None

    has_sidebar_share = "sidebar_share.py" in config["post_render"]
    if force_full or os.environ.get("STATWIKI_FORCE_FULL_RENDER") == "1":
        can_incremental, reason = False, "forced full render"
    else:
        can_incremental, reason = warm_cache_usable(
            site_dir, quarto_dir, prev_manifest, curr_global_sig, has_sidebar_share
        )

    to_render: list[str] = []
    deleted_qmds: set[str] = set()
    deleted_resources: set[str] = set()
    resources_changed = False

    if can_incremental and prev_manifest is not None:
        prev_qmds: dict[str, dict[str, Any]] = prev_manifest.get("qmds") or {}
        prev_resources: dict[str, str] = prev_manifest.get("resources") or {}

        changed_set = {
            rel_qmd
            for rel_qmd, info in curr_qmds.items()
            if (
                rel_qmd not in prev_qmds
                or prev_qmds[rel_qmd].get("sha256") != info["sha256"]
                or not (site_dir / (rel_qmd[:-4] + ".html")).is_file()
                or not (quarto_dir / "idx" / f"{rel_qmd}.json").is_file()
                or any(not (site_dir / alias).is_file() for alias in (info.get("aliases") or ()))
            )
        }
        changed_set |= _sidebar_title_neighbors(prev_qmds, curr_qmds, config["sidebar_qmds"])
        deleted_qmds = set(prev_qmds) - set(curr_qmds)
        deleted_resources = set(prev_resources) - set(curr_resources)
        resources_changed = (
            prev_resources != curr_resources
            or any(not (site_dir / rel_res).is_file() for rel_res in curr_resources)
        )

        # Keep index.qmd first when it is among the changed files so sidebar-nav.js
        # refreshes before nested pages are inspected.
        ordered = sorted(changed_set, key=lambda r: (0 if r == "index.qmd" else 1, r))
        to_render = ordered

        if len(to_render) > max_incremental_files:
            can_incremental = False
            reason = (
                f"{len(to_render)} pages changed, exceeding max_incremental_files="
                f"{max_incremental_files}"
            )

    search_meta_mod = _load_search_meta_module(root) if "search_meta.py" in config["post_render"] else None
    specific_fm_html = _specific_frontmatter_qmds(
        curr_qmds, config["site_description"], search_meta_mod
    )

    if not can_incremental:
        mode = "full"
        rendered_qmds = list(renderable_qmds)
        print(
            f"[incremental-render] Mode: FULL ({len(rendered_qmds)} pages) — reason: {reason}",
            flush=True,
        )
        if dry_run:
            return {
                "mode": mode,
                "reason": reason,
                "total_qmds": len(renderable_qmds),
                "rendered_qmds": rendered_qmds,
            }

        if site_dir.exists():
            shutil.rmtree(site_dir)
        if quarto_dir.exists():
            shutil.rmtree(quarto_dir)

        subprocess.run([quarto_bin, "render"], cwd=root, check=True)
        sync_fresh_wiki_json(root, site_dir)
        prefixed_pages = detect_prefixed_meta_pages(
            site_dir,
            None,
            specific_fm_html,
            curr_qmds,
            search_meta_mod,
            previous_prefixed=None,
        )
    else:
        assert prev_manifest is not None
        prev_qmds = prev_manifest.get("qmds") or {}
        prev_prefixed = list(prev_manifest.get("prefixed_meta_pages") or ())

        # Determine whether any dropped frontmatter aliases need pruning + post-render.
        dropped_aliases = any(
            set((prev_qmds.get(q) or {}).get("aliases") or ()) - set(info.get("aliases") or ())
            for q, info in curr_qmds.items()
            if q in prev_qmds
        )

        if to_render:
            mode = "incremental"
            rendered_qmds = list(to_render)
            reason = f"{len(rendered_qmds)}/{len(renderable_qmds)} pages changed"
        elif resources_changed or deleted_qmds or dropped_aliases:
            mode = "resources-only"
            anchor = "404.qmd" if "404.qmd" in curr_qmds else renderable_qmds[0]
            rendered_qmds = [anchor]
            reason = "0 .qmd pages changed; syncing resources and post-render via " + anchor
        else:
            mode = "noop"
            rendered_qmds = []
            reason = "0 .qmd pages and 0 resources changed"

        print(
            f"[incremental-render] Mode: {mode.upper()} "
            f"({len(rendered_qmds)}/{len(renderable_qmds)} pages rendered) — {reason}",
            flush=True,
        )
        if dry_run:
            return {
                "mode": mode,
                "reason": reason,
                "total_qmds": len(renderable_qmds),
                "rendered_qmds": rendered_qmds,
                "deleted_qmds": sorted(deleted_qmds),
                "deleted_resources": sorted(deleted_resources),
            }

        prune_deleted_artifacts(
            site_dir,
            quarto_dir,
            config["site_url"],
            deleted_qmds,
            prev_qmds,
            curr_qmds,
            deleted_resources,
            curr_resources,
            rerendered_qmds=rendered_qmds,
        )

        if rendered_qmds:
            overwritten_html = {q[:-4] + ".html" for q in rendered_qmds}
            reset_prefixed_meta_pages(
                site_dir,
                prev_prefixed,
                overwritten_html,
                curr_qmds,
                config["site_description"],
            )
            before_stats = _snapshot_html_stats(site_dir)

            if len(rendered_qmds) > 1 and config["post_render"]:
                stripped_yml = strip_post_render_block(quarto_yml_text)
                if "post-render:" in stripped_yml:
                    raise SystemExit("Failed to strip post-render block from _quarto.yml")
                quarto_yml_path.write_text(stripped_yml, encoding="utf-8")
                try:
                    for rel_qmd in rendered_qmds[:-1]:
                        subprocess.run([quarto_bin, "render", rel_qmd], cwd=root, check=True)
                finally:
                    quarto_yml_path.write_bytes(quarto_yml_bytes)

            subprocess.run([quarto_bin, "render", rendered_qmds[-1]], cwd=root, check=True)
            canonicalize_search_and_sitemap(root, site_dir, config["site_url"], renderable_qmds)

            after_stats = _snapshot_html_stats(site_dir)
            touched_html = {
                rel_html
                for rel_html, st in after_stats.items()
                if before_stats.get(rel_html) != st
            } | overwritten_html | set(prev_prefixed)
            existing_prev = {p for p in prev_prefixed if (site_dir / p).is_file()}
            prefixed_pages = detect_prefixed_meta_pages(
                site_dir,
                touched_html,
                specific_fm_html,
                curr_qmds,
                search_meta_mod,
                previous_prefixed=existing_prev,
            )
        else:
            prefixed_pages = [p for p in prev_prefixed if (site_dir / p).is_file()]

        sync_fresh_wiki_json(root, site_dir)

    elapsed = round(time.monotonic() - start_time, 2)
    new_manifest = {
        "schema_version": SCHEMA_VERSION,
        "global_signature": curr_global_sig,
        "qmds": curr_qmds,
        "resources": curr_resources,
        "prefixed_meta_pages": prefixed_pages,
    }
    _write_json_atomic(manifest_path, new_manifest)

    summary = {
        "mode": mode,
        "reason": reason,
        "total_qmds": len(renderable_qmds),
        "rendered_count": len(rendered_qmds),
        "rendered_qmds": rendered_qmds,
        "deleted_qmds": sorted(deleted_qmds),
        "elapsed_seconds": elapsed,
    }
    _write_json_atomic(summary_path, summary)
    print(
        f"[incremental-render] Finished {mode} render of "
        f"{len(rendered_qmds)}/{len(renderable_qmds)} pages in {elapsed:.2f}s",
        flush=True,
    )
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Incremental Quarto site renderer for StatWiki.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Project root containing _quarto.yml (default: repository root).",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=None,
        help="Path to incremental manifest JSON (default: <root>/_build/incremental-manifest.json).",
    )
    parser.add_argument(
        "--summary",
        type=Path,
        default=None,
        help="Path to summary output JSON (default: <root>/_build/incremental-summary.json).",
    )
    parser.add_argument(
        "--quarto",
        default="quarto",
        help="Quarto CLI executable (default: quarto).",
    )
    parser.add_argument(
        "--max-incremental-files",
        type=int,
        default=DEFAULT_MAX_INCREMENTAL_FILES,
        help=f"Fall back to full render when more than N .qmd files changed (default: {DEFAULT_MAX_INCREMENTAL_FILES}).",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Force a clean full render and refresh the incremental manifest.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned render mode and targets without invoking quarto render.",
    )
    args = parser.parse_args(argv)
    run_incremental_render(
        args.root,
        manifest_path=args.manifest,
        summary_path=args.summary,
        quarto_bin=args.quarto,
        max_incremental_files=args.max_incremental_files,
        force_full=args.full,
        dry_run=args.dry_run,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
