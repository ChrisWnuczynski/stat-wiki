"""Render the site on every CPU core.

`quarto render` makes the pages one after another on a single core, which takes
15 to 25 minutes for this site on GitHub. This script splits the pages into one
group per core and renders the groups at the same time, each in its own copy of
the project, then merges them into _site.

Every copy keeps the whole project, so links, the sidebar and redirects come
out exactly as in a plain `quarto render`. Each copy writes a search index and
sitemap for its own pages only; the script joins them.

Run it after build_wiki.py:

    python render_site.py            # one group per core
    python render_site.py --jobs 1   # the same as quarto render
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from xml.etree import ElementTree
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "_site"
# Not copied into the group folders: git history, earlier output, local tools.
SKIP = {".git", "_site", ".quarto", "_publish", "_screenshots", ".claude", "__pycache__"}
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
# Rough cost of a page in bytes of source: a fixed part plus its length.
PAGE_COST = 6000


def quarto() -> str:
    path = shutil.which("quarto")
    if not path:
        sys.exit("quarto is not on PATH.")
    return path


def pages_to_render() -> list[str] | None:
    """The pages Quarto would render, from its own reading of _quarto.yml."""
    result = subprocess.run([quarto(), "inspect"], cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print("quarto inspect failed, so the pages are rendered one after another:\n" + result.stderr[-4000:])
        return None
    info = json.loads(result.stdout)
    project = Path(info["dir"]).resolve()
    return sorted(Path(p).resolve().relative_to(project).as_posix() for p in info["files"]["input"])


def split(pages: list[str], n: int) -> list[list[str]]:
    """Give each group about the same amount of work, largest pages first."""
    groups: list[list[str]] = [[] for _ in range(n)]
    load = [0] * n
    cost = {p: PAGE_COST + (ROOT / p).stat().st_size for p in pages}
    for page in sorted(pages, key=cost.get, reverse=True):
        i = load.index(min(load))
        groups[i].append(page)
        load[i] += cost[page]
    return [sorted(g) for g in groups if g]


def batches(pages: list[str], limit: int = 8000) -> list[list[str]]:
    """Short enough lists of pages for one command line, also on Windows."""
    out: list[list[str]] = [[]]
    length = 0
    for page in pages:
        if out[-1] and length + len(page) + 1 > limit:
            out.append([])
            length = 0
        out[-1].append(page)
        length += len(page) + 1
    return out


def render_group(i: int, pages: list[str], work: Path) -> tuple[int, float, str]:
    copy = work / str(i)
    shutil.copytree(ROOT, copy, symlinks=True, ignore=lambda d, names: SKIP & set(names) if Path(d) == ROOT else ())
    start = time.monotonic()
    log = []
    for batch in batches(pages):
        # Quarto reads every name before the first option as a file to render,
        # so a trailing option is needed. --quiet keeps the log to errors.
        result = subprocess.run(
            [quarto(), "render", *batch, "--quiet"],
            cwd=copy,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        log.append(result.stdout)
        if result.returncode != 0:
            return result.returncode, time.monotonic() - start, "".join(log)
    return 0, time.monotonic() - start, "".join(log)


def merge_search(groups: list[Path]) -> int:
    docs, seen = [], set()
    for site in groups:
        path = site / "search.json"
        if not path.exists():
            continue
        for doc in json.loads(path.read_text(encoding="utf-8")):
            if doc["objectID"] not in seen:
                seen.add(doc["objectID"])
                docs.append(doc)
    if docs:
        (SITE / "search.json").write_text(json.dumps(docs, indent=2, ensure_ascii=False), encoding="utf-8")
    return len(docs)


def merge_sitemap(groups: list[Path]) -> int:
    urls: dict[str, str] = {}
    for site in groups:
        path = site / "sitemap.xml"
        if not path.exists():
            continue
        for url in ElementTree.parse(path).getroot().findall(f"{{{SITEMAP_NS}}}url"):
            loc = url.findtext(f"{{{SITEMAP_NS}}}loc")
            urls.setdefault(loc, url.findtext(f"{{{SITEMAP_NS}}}lastmod") or "")
    if urls:
        lines = ['<?xml version="1.0" encoding="UTF-8"?>', f'<urlset xmlns="{SITEMAP_NS}">']
        for loc, lastmod in urls.items():
            lines += ["  <url>", f"    <loc>{escape(loc)}</loc>"]
            if lastmod:
                lines.append(f"    <lastmod>{escape(lastmod)}</lastmod>")
            lines.append("  </url>")
        lines.append("</urlset>")
        (SITE / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(urls)


def check(pages: list[str]) -> None:
    """Stop the build if a page is missing, so a broken site is never published."""
    missing = [p for p in pages if not (SITE / Path(p).with_suffix(".html")).exists()]
    if missing:
        sys.exit(f"{len(missing)} pages are missing from _site, for example {missing[:5]}")
    # A group without the main page writes a redirect in its place; the real one must win.
    home = (SITE / "index.html").read_text(encoding="utf-8")
    if 'http-equiv="refresh"' in home:
        sys.exit("_site/index.html is a redirect, not the main page.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--jobs", type=int, default=os.cpu_count() or 1, help="number of groups (default: CPU cores)")
    args = parser.parse_args()

    start = time.monotonic()
    pages = pages_to_render() if args.jobs > 1 else None
    if pages is None:
        sys.exit(subprocess.run([quarto(), "render"], cwd=ROOT).returncode)
    groups = split(pages, args.jobs)
    print(f"{len(pages)} pages in {len(groups)} groups of {', '.join(str(len(g)) for g in groups)}"
          f" (listed in {time.monotonic() - start:.0f} s)", flush=True)

    with tempfile.TemporaryDirectory(prefix="stat-wiki-render-") as tmp:
        work = Path(tmp)
        with ThreadPoolExecutor(max_workers=len(groups)) as pool:
            results = list(pool.map(lambda ig: render_group(ig[0], ig[1], work), enumerate(groups)))

        failed = False
        for i, (code, seconds, log) in enumerate(results):
            print(f"Group {i}: {len(groups[i])} pages in {seconds / 60:.1f} min" + ("" if code == 0 else f", FAILED ({code})"))
            if log.strip():
                print(log.rstrip()[-6000:])
            failed |= code != 0
        if failed:
            sys.exit(1)

        # Copy the group with the main page last, so its index.html wins.
        order = sorted(range(len(groups)), key=lambda i: "index.qmd" in groups[i])
        sites = [work / str(i) / "_site" for i in order]
        if SITE.exists():
            shutil.rmtree(SITE)
        for site in sites:
            shutil.copytree(site, SITE, dirs_exist_ok=True)
        docs = merge_search(sites)
        urls = merge_sitemap(sites)

    check(pages)
    print(f"Merged into _site: {len(pages)} pages, {docs} search entries, {urls} sitemap entries,"
          f" {(time.monotonic() - start) / 60:.1f} min in all")


if __name__ == "__main__":
    main()
