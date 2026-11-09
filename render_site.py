#!/usr/bin/env python3
"""Render this Quarto website on every CPU core, then merge the sites.

Run it from the repository after ``python build_wiki.py``:

    python render_site.py

The page list comes from ``quarto inspect`` (``files.input``). The pages are
split into one group per CPU core. Each group is rendered in its own copy of
the project, kept outside this repository, and the copies' ``_site`` folders
are merged back into ``_site/``.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

# Copies have to live outside the repository. The "*.qmd" pattern in
# _quarto.yml matches subfolders, so a copy left inside the repo is rendered
# again as part of the site.
SKIP_COPY = {".git", "_site", ".quarto"}
MAX_COMMAND_CHARS = 8000
SEARCH_JSON = "search.json"
SITEMAP_XML = "sitemap.xml"
URL_RE = re.compile(
    r"[ \t]*<url>\s*<loc>(.*?)</loc>\s*<lastmod>(.*?)</lastmod>\s*</url>",
    re.S,
)

_print_lock = threading.Lock()


def log(message: str) -> None:
    with _print_lock:
        print(message, flush=True)


def cpu_cores() -> int:
    try:
        return max(1, len(os.sched_getaffinity(0)))
    except (AttributeError, OSError):
        return max(1, os.cpu_count() or 1)


def command_length(pages: list[str]) -> int:
    """Length of ``quarto render <pages> --quiet`` as the OS would pass it."""
    argv = ["quarto", "render", *pages, "--quiet"]
    windows = len(subprocess.list2cmdline(argv))
    posix = len(" ".join(argv))
    return max(windows, posix)


def split_batches(pages: list[str]) -> list[list[str]]:
    """Split pages so each render command stays under 8,000 characters.

    Windows rejects longer command lines. A single path that is already over
    the limit is left on its own; it cannot be split further.
    """
    batches: list[list[str]] = []
    current: list[str] = []
    for page in pages:
        if current and command_length(current + [page]) >= MAX_COMMAND_CHARS:
            batches.append(current)
            current = [page]
        else:
            current.append(page)
    if current:
        batches.append(current)
    return batches


def parse_inspect(stdout: str) -> dict | None:
    text = stdout.strip()
    if not text:
        return None
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start < 0 or end <= start:
            return None
        try:
            data = json.loads(text[start : end + 1])
        except json.JSONDecodeError:
            return None
    return data if isinstance(data, dict) else None


def inspect_pages(root: Path) -> list[Path] | None:
    """Return the project's input pages, or None when inspect cannot be used."""
    try:
        proc = subprocess.run(
            ["quarto", "inspect"],
            cwd=root,
            capture_output=True,
            text=True,
            errors="replace",
            check=False,
        )
    except OSError as exc:
        log(f"quarto inspect could not be started: {exc}")
        return None
    if proc.returncode != 0:
        log("quarto inspect failed.")
        if proc.stderr.strip():
            log(proc.stderr.rstrip())
        if proc.stdout.strip():
            log(proc.stdout[:2000].rstrip())
        return None
    data = parse_inspect(proc.stdout)
    inputs = None if data is None else data.get("files", {}).get("input")
    if not isinstance(inputs, list) or not inputs:
        log("quarto inspect did not return a files.input list.")
        return None
    pages: list[Path] = []
    seen: set[Path] = set()
    for item in inputs:
        if not isinstance(item, str):
            log(f"quarto inspect returned an unexpected input: {item!r}")
            return None
        path = Path(item)
        if not path.is_absolute():
            path = root / path
        try:
            path = path.resolve()
            path.relative_to(root)
        except ValueError:
            log(f"quarto inspect listed a file outside the project: {path}")
            return None
        if not path.is_file():
            log(f"quarto inspect listed a missing file: {path}")
            return None
        if path not in seen:
            seen.add(path)
            pages.append(path)
    return pages


def render_plain(root: Path) -> int:
    log("Falling back to quarto render.")
    try:
        proc = subprocess.run(["quarto", "render"], cwd=root)
    except OSError as exc:
        log(f"quarto render could not be started: {exc}")
        return 1
    return proc.returncode


def group_pages(pages: list[Path], groups: int) -> list[list[Path]]:
    """One group per core, with roughly the same total file size in each."""
    if not pages:
        return []
    groups = max(1, min(groups, len(pages)))
    ordered = sorted(pages, key=lambda page: (-page.stat().st_size, page.as_posix()))
    totals = [0] * groups
    buckets: list[list[Path]] = [[] for _ in range(groups)]
    for page in ordered:
        size = page.stat().st_size
        index = min(range(groups), key=lambda i: (totals[i], i))
        buckets[index].append(page)
        totals[index] += size
    for bucket in buckets:
        bucket.sort(key=lambda page: page.as_posix())
    return [bucket for bucket in buckets if bucket]


def relative_page(root: Path, page: Path) -> str:
    return page.resolve().relative_to(root.resolve()).as_posix()


def is_root_index(root: Path, page: Path) -> bool:
    return page.resolve() == (root / "index.qmd").resolve()


def make_work_root(root: Path) -> Path:
    work = Path(tempfile.mkdtemp(prefix="render-site-"))
    resolved = work.resolve()
    if resolved == root or root in resolved.parents:
        shutil.rmtree(work, ignore_errors=True)
        raise SystemExit("The temporary render directory was inside the repository.")
    return work


def copy_project(root: Path, dest: Path) -> None:
    def ignore(directory: str, names: list[str]) -> list[str]:
        if Path(directory).resolve() == root:
            return [name for name in names if name in SKIP_COPY]
        return []

    shutil.copytree(root, dest, ignore=ignore)


@dataclass
class GroupResult:
    number: int
    pages: list[Path]
    site: Path | None
    has_index: bool
    ok: bool
    log: str
    seconds: float


def render_group(number: int, pages: list[Path], root: Path, work: Path) -> GroupResult:
    started = time.perf_counter()
    try:
        return _render_group(number, pages, root, work, started)
    except Exception as exc:
        return GroupResult(
            number,
            pages,
            None,
            any(is_root_index(root, page) for page in pages),
            False,
            f"{type(exc).__name__}: {exc}",
            time.perf_counter() - started,
        )


def _render_group(number: int, pages: list[Path], root: Path, work: Path, started: float) -> GroupResult:
    dest = work / f"group-{number}"
    rel_pages = [relative_page(root, page) for page in pages]
    batches = split_batches(rel_pages)
    has_index = any(is_root_index(root, page) for page in pages)
    chunks: list[str] = []
    try:
        copy_project(root, dest)
    except OSError as exc:
        chunks.append(f"Could not copy the project: {exc}")
        return GroupResult(number, pages, None, has_index, False, "\n".join(chunks), time.perf_counter() - started)

    for batch_number, batch in enumerate(batches, start=1):
        # An option has to follow the file names. Otherwise Quarto hands every
        # name after the first one to pandoc instead of rendering it.
        command = ["quarto", "render", *batch, "--quiet"]
        log(f"Group {number} batch {batch_number}/{len(batches)}: {len(batch)} pages")
        try:
            proc = subprocess.run(
                command,
                cwd=dest,
                capture_output=True,
                text=True,
                errors="replace",
                check=False,
            )
        except OSError as exc:
            chunks.append(f"$ {' '.join(command)}\nCould not start quarto: {exc}")
            return GroupResult(number, pages, None, has_index, False, "\n".join(chunks), time.perf_counter() - started)
        output = "\n".join(part.rstrip() for part in (proc.stdout, proc.stderr) if part and part.strip())
        if output:
            chunks.append(output)
        if proc.returncode != 0:
            chunks.append(f"$ {' '.join(command)}\nquarto render exited with status {proc.returncode}.")
            return GroupResult(number, pages, None, has_index, False, "\n".join(chunks), time.perf_counter() - started)

    seconds = time.perf_counter() - started
    site = dest / "_site"
    if not site.is_dir():
        chunks.append("quarto render finished without writing _site.")
        return GroupResult(number, pages, None, has_index, False, "\n".join(chunks), seconds)
    log(f"Group {number} finished in {seconds:.1f}s ({len(pages)} pages).")
    return GroupResult(number, pages, site, has_index, True, "\n".join(chunks), seconds)


def copy_site_files(site: Path, dest: Path) -> None:
    skip = {SEARCH_JSON, SITEMAP_XML}
    for dirpath, _dirnames, filenames in os.walk(site):
        rel_dir = Path(dirpath).relative_to(site)
        target = dest / rel_dir
        target.mkdir(parents=True, exist_ok=True)
        for name in filenames:
            if (rel_dir / name).as_posix() in skip:
                continue
            shutil.copy2(Path(dirpath) / name, target / name)


def merge_search(sites: list[Path]) -> str:
    docs: list[dict] = []
    seen: dict[str, dict] = {}
    for site in sites:
        path = site / SEARCH_JSON
        try:
            loaded = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SystemExit(f"Could not read {path}: {exc}") from exc
        if not isinstance(loaded, list):
            raise SystemExit(f"{path} is not a JSON array.")
        for doc in loaded:
            if not isinstance(doc, dict) or "objectID" not in doc:
                raise SystemExit(f"{path} has a search entry without objectID.")
            object_id = doc["objectID"]
            if not isinstance(object_id, str):
                raise SystemExit(f"{path} has a non-text objectID.")
            previous = seen.get(object_id)
            if previous is not None:
                if previous != doc:
                    raise SystemExit(f"Search entries for {object_id} do not match.")
                continue
            seen[object_id] = doc
            docs.append(doc)
    return json.dumps(docs, ensure_ascii=False, indent=2)


def merge_sitemaps(texts: list[str]) -> str:
    parsed: list[tuple[str, list[re.Match[str]]]] = []
    for text in texts:
        matches = list(URL_RE.finditer(text))
        if not matches:
            raise SystemExit("A group wrote a sitemap.xml with no <url> entries.")
        parsed.append((text, matches))
    first_text, first_matches = parsed[0]
    header = first_text[: first_matches[0].start()]
    footer = first_text[first_matches[-1].end() :]
    if len(first_matches) >= 2:
        separator = first_text[first_matches[0].end() : first_matches[1].start()]
    else:
        separator = "\n"
    seen: set[str] = set()
    blocks: list[str] = []
    for _text, matches in parsed:
        for match in matches:
            loc = match.group(1)
            if loc in seen:
                continue
            seen.add(loc)
            blocks.append(match.group(0))
    return header + separator.join(blocks) + footer


def merge_sites(root: Path, groups: list[GroupResult]) -> None:
    """Copy every group's _site into the project.

    A group that does not render the root index.qmd writes a redirect
    index.html. The group that does contain index.qmd is copied last so the
    real home page replaces that redirect.
    """
    ordered = sorted(groups, key=lambda group: (group.has_index, group.number))
    dest = root / "_site"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)

    sites: list[Path] = []
    for group in ordered:
        if group.site is None:
            raise SystemExit(f"Group {group.number} has no _site to merge.")
        copy_site_files(group.site, dest)
        sites.append(group.site)

    search_sites = [site for site in sites if (site / SEARCH_JSON).is_file()]
    if search_sites:
        missing = [site for site in sites if not (site / SEARCH_JSON).is_file()]
        if missing:
            raise SystemExit("Some groups did not write search.json, so the search index would be incomplete.")
        (dest / SEARCH_JSON).write_text(merge_search(sites), encoding="utf-8", newline="\n")

    sitemap_texts: list[str] = []
    sitemap_count = 0
    for site in sites:
        path = site / SITEMAP_XML
        if path.is_file():
            sitemap_count += 1
            sitemap_texts.append(path.read_text(encoding="utf-8"))
    if sitemap_texts:
        if sitemap_count != len(sites):
            raise SystemExit("Some groups did not write sitemap.xml, so the sitemap would be incomplete.")
        (dest / SITEMAP_XML).write_text(merge_sitemaps(sitemap_texts), encoding="utf-8", newline="\n")


def is_redirect(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    return "<title>Redirect to " in text and 'http-equiv="refresh"' in text


def verify_site(root: Path, pages: list[Path]) -> list[str]:
    problems: list[str] = []
    missing: list[Path] = []
    for page in pages:
        html = root / "_site" / page.resolve().relative_to(root).with_suffix(".html")
        if not html.is_file():
            missing.append(html)
    if missing:
        problems.append(f"{len(missing)} pages have no HTML in _site:")
        for html in missing[:40]:
            problems.append(f"  {html.relative_to(root / '_site')}")
        if len(missing) > 40:
            problems.append(f"  ... and {len(missing) - 40} more")
    index_html = root / "_site" / "index.html"
    if not index_html.is_file():
        problems.append("index.html is missing from _site.")
    elif is_redirect(index_html):
        problems.append("index.html is a redirect.")
    return problems


def main() -> int:
    started = time.perf_counter()
    root = Path(__file__).resolve().parent
    log("Reading the page list with quarto inspect.")
    pages = inspect_pages(root)
    if pages is None:
        return render_plain(root)
    inspect_done = time.perf_counter()

    groups = group_pages(pages, cpu_cores())
    assigned = [page for group in groups for page in group]
    if len(assigned) != len(pages) or {page.resolve() for page in assigned} != {page.resolve() for page in pages}:
        log("The page groups do not cover the inspected page list.")
        return 1
    log(f"{len(pages)} pages, {len(groups)} groups.")

    work = make_work_root(root)
    try:
        results: list[GroupResult] = []
        with ThreadPoolExecutor(max_workers=len(groups)) as pool:
            futures = [
                pool.submit(render_group, number, group, root, work)
                for number, group in enumerate(groups, start=1)
            ]
            for future in as_completed(futures):
                results.append(future.result())
        results.sort(key=lambda group: group.number)
        failed = [group for group in results if not group.ok]
        if failed:
            for group in failed:
                log(f"Group {group.number} failed.")
                if group.log.strip():
                    log(group.log.rstrip())
            return 1
        render_done = time.perf_counter()
        merge_sites(root, results)
    finally:
        shutil.rmtree(work, ignore_errors=True)

    problems = verify_site(root, pages)
    if problems:
        for problem in problems:
            log(problem)
        return 1

    total = time.perf_counter() - started
    log(
        f"Rendered {len(pages)} pages on {len(groups)} cores in {total:.1f}s "
        f"(inspect {inspect_done - started:.1f}s, render {render_done - inspect_done:.1f}s, "
        f"merge {time.perf_counter() - render_done:.1f}s)."
    )
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass
    sys.exit(main())
