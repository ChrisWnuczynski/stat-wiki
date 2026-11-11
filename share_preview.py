"""Add each page's public URL to its share tags.

Quarto writes the Open Graph title, description, and image, and the matching
Twitter card. It does not write og:url. The canonical link is already the
public URL, so copy that into og:url. The main page's canonical link is the
site root.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

SITE = "https://www.statwiki.io/"
IMAGE = "https://www.statwiki.io/share-icon.png"
DESCRIPTION = (
    "Study wiki for data analysis, probability, stochastic processes, "
    "statistical learning, statistical inference, and the R used to compute them"
)
ALT = "Contours of a bivariate normal density in viridis, the stat wiki icon"
TITLE_SUFFIX = " \u2013 stat wiki"

ROOT = Path(__file__).resolve().parent
SITE_DIR = ROOT / "_site"

CANONICAL = re.compile(r'<link rel="canonical" href="([^"]+)">')
ATTR = re.compile(r"""([^\s=/>]+)\s*=\s*(?:"([^"]*)"|'([^']*)')""")


def meta_tags(text: str):
    """Each meta tag, including one whose quoted value contains >.

    Quarto writes a title straight into the attribute. A greater-than sign is
    allowed there, and the HTML is well formed. A pattern that stops at the
    first > never sees the content, and reports the tag missing.
    """
    i = 0
    n = len(text)
    while i < n:
        start = text.find("<meta", i)
        if start < 0:
            return
        if start + 5 < n and (text[start + 5].isalnum() or text[start + 5] in "-_:"):
            i = start + 5
            continue
        j = start + 5
        quote = ""
        while j < n:
            ch = text[j]
            if quote:
                if ch == quote:
                    quote = ""
            elif ch in "\"'":
                quote = ch
            elif ch == ">":
                yield text[start : j + 1]
                i = j + 1
                break
            j += 1
        else:
            return


def meta_map(text: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for tag in meta_tags(text):
        attrs: dict[str, str] = {}
        for match in ATTR.finditer(tag):
            raw = match.group(2) if match.group(2) is not None else match.group(3)
            attrs[match.group(1).lower()] = html.unescape(raw)
        key = attrs.get("property") or attrs.get("name")
        if key and "content" in attrs:
            found[key] = attrs["content"]
    return found


def public_url(page: Path, canonical: str) -> str:
    if not canonical.startswith(SITE):
        raise SystemExit(f"Canonical link leaves the site: {page} -> {canonical}")
    if page == SITE_DIR / "index.html":
        return SITE
    return canonical


def require(page: Path, found: dict[str, str], key: str, expected: str | None = None) -> str:
    value = found.get(key)
    if value is None:
        raise SystemExit(f"{page.relative_to(SITE_DIR)} is missing {key}")
    if expected is not None and value != expected:
        raise SystemExit(f"{page.relative_to(SITE_DIR)} {key} is {value!r}, expected {expected!r}")
    return value


def add_url(text: str, url: str) -> str:
    tag = f'<meta property="og:url" content="{url}">'
    existing = re.search(r'<meta property="og:url" content="([^"]*)">', text)
    if existing:
        if existing.group(1) != url:
            raise SystemExit(f"og:url is {existing.group(1)!r}, expected {url!r}")
        return text
    match = CANONICAL.search(text)
    if not match:
        raise SystemExit("No canonical link to place og:url beside")
    return text.replace(match.group(0), match.group(0) + "\n" + tag, 1)


def check_page(page: Path, text: str) -> None:
    found = meta_map(text)
    if re.search(r'<meta[^>]+name="robots"[^>]+noindex', text):
        raise SystemExit(f"{page.relative_to(SITE_DIR)} sends noindex")
    url = require(page, found, "og:url")
    if not url.startswith(SITE):
        raise SystemExit(f"{page.relative_to(SITE_DIR)} og:url leaves the site: {url}")
    title = require(page, found, "og:title")
    if page == SITE_DIR / "index.html":
        require(page, found, "og:title", "stat wiki")
        require(page, found, "og:url", SITE)
    elif not (title == "stat wiki" or title.endswith(TITLE_SUFFIX)):
        raise SystemExit(f"{page.relative_to(SITE_DIR)} og:title is {title!r}")
    require(page, found, "og:description", DESCRIPTION)
    require(page, found, "og:image", IMAGE)
    require(page, found, "og:image:width", "1200")
    require(page, found, "og:image:height", "630")
    require(page, found, "og:image:alt", ALT)
    require(page, found, "twitter:card", "summary_large_image")
    require(page, found, "twitter:title", title)
    require(page, found, "twitter:description", DESCRIPTION)
    require(page, found, "twitter:image", IMAGE)
    for key in ("og:title", "og:description", "og:image:alt", "twitter:title", "twitter:description"):
        value = found[key]
        if re.search(r"STAT\s*\d|github", value, re.I):
            raise SystemExit(f"{page.relative_to(SITE_DIR)} {key} names a course or a forge")


def main() -> None:
    if not SITE_DIR.is_dir():
        raise SystemExit(f"Missing site: {SITE_DIR}")
    pages = [
        path
        for path in sorted(SITE_DIR.rglob("*.html"))
        if "site_libs" not in path.parts
    ]
    if not pages:
        raise SystemExit("No HTML pages to tag")
    changed = 0
    for path in pages:
        text = path.read_text(encoding="utf-8")
        match = CANONICAL.search(text)
        if not match:
            raise SystemExit(f"No canonical link in {path.relative_to(SITE_DIR)}")
        updated = add_url(text, public_url(path, match.group(1)))
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            text = updated
        if "<title>Redirect</title>" in text and "var redirects" in text:
            continue
        check_page(path, text)
    image = SITE_DIR / "share-icon.png"
    if not image.is_file():
        raise SystemExit("Share image was not copied to _site/share-icon.png")
    print(f"Share URLs on {changed} pages")


if __name__ == "__main__":
    sys.exit(main() or 0)
