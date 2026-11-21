"""Add a canonical link to each alias redirect page.

Quarto writes these short redirect pages after the normal HTML is rendered,
so they do not go through the page template. Point each one at the public
page it stands in for.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urljoin

from search_meta import directory_url

SITE = "https://www.statwiki.io/"
ROOT = Path(__file__).resolve().parent
SITE_DIR = ROOT / "_site"

REDIRECTS = re.compile(r"var redirects = (\{.*?\});", re.S)
PAIR = re.compile(r'"((?:\\.|[^"\\])*)"\s*:\s*"((?:\\.|[^"\\])*)"')


def redirect_target(redirect_map: str, page: Path) -> str:
    pairs = PAIR.findall(redirect_map)
    target = dict(pairs).get("")
    if not target and pairs:
        target = pairs[0][1]
    if not target:
        raise SystemExit(f"No redirect target in {page}")
    return target


def absolute_redirect_url(page: Path, target: str, site_dir: Path | None = None) -> str:
    """Absolute canonical for a stub. The fragment is not part of the canonical URL."""
    root = SITE_DIR if site_dir is None else site_dir
    page_url = SITE + page.relative_to(root).as_posix()
    absolute = urljoin(page_url, target.split("#", 1)[0])
    if not absolute.startswith(SITE):
        raise SystemExit(f"Redirect leaves the site: {page} -> {absolute}")
    return directory_url(absolute)


def canonical_for(page: Path, redirect_map: str) -> str:
    target = redirect_target(redirect_map, page)
    absolute = urljoin(SITE + page.relative_to(SITE_DIR).as_posix(), target.split("#", 1)[0])
    if not absolute.startswith(SITE):
        raise SystemExit(f"Redirect leaves the site: {page} -> {absolute}")
    destination = SITE_DIR / absolute.removeprefix(SITE)
    if not destination.is_file():
        raise SystemExit(f"Redirect target is missing: {page} -> {absolute}")
    return directory_url(absolute)


def main() -> None:
    if not SITE_DIR.is_dir():
        raise SystemExit(f"Missing site: {SITE_DIR}")
    changed = 0
    for path in sorted(SITE_DIR.rglob("*.html")):
        if "site_libs" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if "<title>Redirect</title>" not in text or "var redirects" not in text:
            continue
        match = REDIRECTS.search(text)
        if not match:
            raise SystemExit(f"No redirect map in {path}")
        href = canonical_for(path, match.group(1))
        if 'name="robots"' in text and "noindex" in text.lower():
            raise SystemExit(f"Redirect stub sends noindex: {path}")
        link = f'<link rel="canonical" href="{href}">'
        if link in text:
            continue
        if 'rel="canonical"' in text:
            raise SystemExit(f"Redirect already has a different canonical: {path}")
        if "<head>\n" not in text:
            raise SystemExit(f"Redirect head is not where it should be: {path}")
        path.write_text(text.replace("<head>\n", "<head>\n  " + link + "\n", 1), encoding="utf-8")
        changed += 1
    print(f"Canonical links on {changed} redirect pages")


if __name__ == "__main__":
    sys.exit(main())
