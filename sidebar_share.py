"""Keep one copy of the full sidebar, and a short menu in every page.

Quarto repeats the whole navigation in each HTML file. After render, this
script stores that menu once as ``sidebar-nav.js`` and leaves each page with
a short menu: the topic hubs, laboratories, and reference links. The page
script puts the full menu back, highlights the current page, and scrolls it
into view. Without JavaScript the topic hubs remain.

Alphabetical "Further reading" buckets are removed from the breadcrumb.
Prev/next links are left as Quarto wrote them.
"""

from __future__ import annotations

import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE_DIR = ROOT / "_site"
BUCKET = re.compile(r"^[A-Z](?:–[A-Z])?$")
CRUMB_NAV = re.compile(
    r'(<nav\b[^>]*aria-label="breadcrumb"[^>]*>)(.*?)(</nav>)',
    re.I | re.S,
)
CRUMB_ITEM = re.compile(r"<li\b[^>]*breadcrumb-item[^>]*>.*?</li>", re.I | re.S)


def _opening_end(html: str, start: int) -> int:
    end = html.find(">", start)
    if end < 0:
        raise SystemExit("Unclosed tag in the sidebar")
    return end + 1


def _match_pair(html: str, start: int, open_name: str, close_name: str) -> tuple[int, int, int]:
    """Return (inner_start, inner_end, outer_end) for the element at start."""
    token_open = f"<{open_name}"
    token_close = f"</{open_name}>"
    if not html.startswith(token_open, start):
        raise SystemExit(f"Expected <{open_name}> at offset {start}")
    inner_start = _opening_end(html, start)
    depth = 1
    i = inner_start
    while i < len(html):
        next_open = html.find(token_open, i)
        next_close = html.find(token_close, i)
        if next_close < 0:
            raise SystemExit(f"Unclosed <{open_name}> in the sidebar")
        if 0 <= next_open < next_close:
            depth += 1
            i = next_open + len(token_open)
            continue
        depth -= 1
        if depth == 0:
            return inner_start, next_close, next_close + len(token_close)
        i = next_close + len(token_close)
    raise SystemExit(f"Unclosed <{open_name}> in the sidebar")


def sidebar_list(html: str) -> tuple[int, int, int] | None:
    """Inner bounds and the start of the sidebar's top list, if this page has one."""
    nav = html.find('id="quarto-sidebar"')
    if nav < 0:
        return None
    ul = html.find("<ul", nav)
    if ul < 0:
        return None
    inner_start, inner_end, _outer_end = _match_pair(html, ul, "ul", "ul")
    return ul, inner_start, inner_end


def top_elements(html: str, name: str) -> list[tuple[int, int]]:
    """Spans of the top-level elements named ``name`` (their nested copies are inside)."""
    spans: list[tuple[int, int]] = []
    i = 0
    token = f"<{name}"
    while True:
        start = html.find(token, i)
        if start < 0:
            break
        _inner, _inner_end, outer_end = _match_pair(html, start, name, name)
        spans.append((start, outer_end))
        i = outer_end
    return spans


def normalise_href(href: str) -> str:
    path = href.split("#", 1)[0].split("?", 1)[0]
    while path.startswith("./"):
        path = path[2:]
    while path.startswith("../"):
        path = path[3:]
    return path.lstrip("/")


HUB_NOTES = {
    "notes/index.html",
    "notes/index.qmd",
    "notes/fundamentals.html",
    "notes/fundamentals.qmd",
    "notes/probability-distributions.html",
    "notes/probability-distributions.qmd",
    "notes/applications.html",
    "notes/applications.qmd",
    "notes/final-preparation.html",
    "notes/final-preparation.qmd",
    "notes/final-bayesian.html",
    "notes/final-bayesian.qmd",
    "notes/final-applied.html",
    "notes/final-applied.qmd",
}


def is_article_href(href: str) -> bool:
    return normalise_href(href).startswith("articles/")


def is_omitted_href(href: str) -> bool:
    """Article pages and chapter notes are restored from the shared menu."""
    path = normalise_href(href)
    if path.startswith("articles/"):
        return True
    return path.startswith("notes/") and path not in HUB_NOTES


def first_href(html: str, limit: int | None = None) -> str:
    chunk = html if limit is None else html[:limit]
    match = re.search(r'href="([^"]*)"', chunk)
    return match.group(1) if match else ""


def strip_active(html: str) -> str:
    html = re.sub(r'\s+aria-current="page"', "", html)
    html = re.sub(r'(\s)active(\s)', r"\1", html)
    html = re.sub(r'(\s)active"', '"', html)
    html = re.sub(r'"active(\s)', '"', html)
    html = re.sub(r"\s{2,}", " ", html)
    return html


def prune_menu(html: str) -> str:
    """Drop article and chapter-note links, then drop empty sections."""
    pieces: list[str] = []
    last = 0
    for start, end in top_elements(html, "li"):
        pieces.append(html[last:start])
        kept = prune_item(html[start:end])
        if kept:
            pieces.append(kept)
        last = end
    pieces.append(html[last:])
    return "".join(pieces)


def prune_item(item: str) -> str | None:
    uls = top_elements(item, "ul")
    href = first_href(item, uls[0][0] if uls else None)
    if not uls:
        return None if is_omitted_href(href) else item
    ul_start, ul_end = uls[0]
    inner_start, inner_end, _outer = _match_pair(item, ul_start, "ul", "ul")
    pruned = prune_menu(item[inner_start:inner_end])
    if "<li" not in pruned:
        if not href or is_omitted_href(href):
            return None
        return item[:ul_start] + item[ul_end:]
    return item[:inner_start] + pruned + item[inner_end:]


def to_relative(site_href: str, page: Path) -> str:
    if re.match(r"^[a-z][a-z0-9+.-]*:", site_href, re.I) or site_href.startswith(("#", "/")):
        return site_href
    path, sep, frag = site_href.partition("#")
    path = path.removeprefix("./")
    target = (SITE_DIR / path).resolve()
    rel = os.path.relpath(target, page.parent.resolve()).replace("\\", "/")
    return f"{rel}#{frag}" if sep else rel


def rewrite_hrefs(html: str, page: Path) -> str:
    def repl(match: re.Match[str]) -> str:
        return f'href="{to_relative(match.group(1), page)}"'

    return re.sub(r'href="([^"]*)"', repl, html)


def page_key(page: Path) -> str:
    rel = page.relative_to(SITE_DIR).as_posix()
    if rel == "index.html":
        return ""
    if rel.endswith("/index.html"):
        return rel[: -len("index.html")]
    return rel


def href_key(href: str) -> str:
    path = normalise_href(href.split("#", 1)[0])
    if path.endswith("/index.html"):
        path = path[: -len("index.html")]
    if path == "index.html":
        return ""
    return path


def mark_current(html: str, page: Path) -> str:
    current = page_key(page)

    def repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        href_match = re.search(r'href="([^"]*)"', tag)
        if not href_match or href_key(href_match.group(1)) != current:
            return tag
        if "active" not in tag.split("class=", 1)[-1]:
            tag = tag.replace('class="', 'class="active ', 1) if 'class="' in tag else tag
        if "aria-current" not in tag:
            tag = tag[:-1] + ' aria-current="page">'
        return tag

    return re.sub(r"<a\b[^>]*>", repl, html)


def crumb_text(item: str) -> str:
    text = re.sub(r"<[^>]+>", "", item)
    return re.sub(r"\s+", " ", text).strip()


def strip_bucket_crumbs(html: str) -> str:
    """Remove Further reading and its A–C / D–R labels from the breadcrumb."""

    def nav_repl(match: re.Match[str]) -> str:
        body = CRUMB_ITEM.sub(item_repl, match.group(2))
        return match.group(1) + body + match.group(3)

    def item_repl(match: re.Match[str]) -> str:
        item = match.group(0)
        text = crumb_text(item)
        if "active" in item and "breadcrumb-item" in item and "aria-current" in item:
            return item
        if text == "Further reading" or BUCKET.fullmatch(text):
            return ""
        return item

    return CRUMB_NAV.sub(nav_repl, html)


def script_tag(page: Path) -> str:
    depth = len(page.relative_to(SITE_DIR).parent.parts)
    src = f"{'../' * depth}sidebar-nav.js"
    return f'<script src="{src}"></script>\n'


class _LoaderParser(HTMLParser):
    """Recognise the external loader without matching inline source or comments."""

    def __init__(self) -> None:
        super().__init__()
        self.found = False

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag == "script":
            src = dict(attrs).get("src") or ""
            path = src.split("?", 1)[0].split("#", 1)[0]
            if path.rsplit("/", 1)[-1] == "sidebar-nav.js":
                self.found = True


def insert_loader(html: str, page: Path) -> str:
    parser = _LoaderParser()
    parser.feed(html)
    if parser.found:
        return html
    marker = "function sidebarRoot"
    at = html.find(marker)
    if at < 0:
        return html
    script = html.rfind("<script", 0, at)
    if script < 0:
        return html
    return html[:script] + script_tag(page) + html[script:]


def fallback_for(template: str, page: Path) -> str:
    return mark_current(rewrite_hrefs(template, page), page)


def _class_tokens(tag: str) -> set[str]:
    match = re.search(r'class="([^"]*)"', tag)
    return set(match.group(1).split()) if match else set()


def _set_class(tag: str, token: str, present: bool) -> str:
    match = re.search(r'class="([^"]*)"', tag)
    if not match:
        if not present:
            return tag
        return tag[:-1] + f' class="{token}">'
    tokens = [part for part in match.group(1).split() if part != token]
    if present:
        tokens.append(token)
    return tag[: match.start(1)] + " ".join(tokens) + tag[match.end(1) :]


def section_open_state(html: str) -> dict[str, bool]:
    """Which sidebar sections Quarto left open on this page."""
    state: dict[str, bool] = {}
    for match in re.finditer(r"<ul\b[^>]*>", html):
        tag = match.group(0)
        id_match = re.search(r'\bid="([^"]+)"', tag)
        if not id_match:
            continue
        state[id_match.group(1)] = "show" in _class_tokens(tag)
    return state


def apply_open_state(menu: str, state: dict[str, bool]) -> str:
    """Keep the current section open in the short menu, so its hub link is visible without JavaScript."""

    def ul_repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        id_match = re.search(r'\bid="([^"]+)"', tag)
        if not id_match or id_match.group(1) not in state:
            return tag
        return _set_class(tag, "show", state[id_match.group(1)])

    def a_repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        target = re.search(r'data-bs-target="#([^"]+)"', tag)
        if not target or target.group(1) not in state:
            return tag
        open_ = state[target.group(1)]
        tag = _set_class(tag, "collapsed", not open_)
        expanded = "true" if open_ else "false"
        if "aria-expanded" in tag:
            return re.sub(r'aria-expanded="(?:true|false)"', f'aria-expanded="{expanded}"', tag, count=1)
        return tag[:-1] + f' aria-expanded="{expanded}">'

    menu = re.sub(r"<ul\b[^>]*>", ul_repl, menu)
    return re.sub(r"<a\b[^>]*>", a_repl, menu)


def absolutise_hrefs(html: str, page: Path, site: Path) -> str:
    """Rewrite menu links as paths from the site root, wherever the page sits."""

    def repl(match: re.Match[str]) -> str:
        href = match.group(1)
        if re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I) or href.startswith(("#", "/")):
            return match.group(0)
        path, sep, frag = href.partition("#")
        target = (page.parent / path).resolve()
        try:
            rel = target.relative_to(site.resolve()).as_posix()
        except ValueError:
            return match.group(0)
        new = f"{rel}#{frag}" if sep else rel
        return f'href="{new}"'

    return re.sub(r'href="([^"]*)"', repl, html)


def stored_sidebar_html(site: Path) -> str | None:
    path = site / "sidebar-nav.js"
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    marker = "window.__STATWIKI_SIDEBAR = "
    if marker not in text:
        return None
    payload = text.split(marker, 1)[1].strip()
    if payload.endswith(";"):
        payload = payload[:-1].rstrip()
    try:
        data = json.loads(payload)
    except json.JSONDecodeError:
        return None
    html = data.get("html") if isinstance(data, dict) else None
    if not isinstance(html, str) or "articles/" not in html:
        return None
    return html


def menu_with_articles(site: Path, index_inner: str) -> str:
    """The full menu, from this render or from the menu already stored beside the site."""
    if "articles/" in index_inner:
        return strip_active(index_inner)
    stored = stored_sidebar_html(site)
    if stored:
        return strip_active(stored)
    for path in sorted(site.rglob("*.html")):
        if "site_libs" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        bounds = sidebar_list(text)
        if not bounds:
            continue
        inner = text[bounds[1] : bounds[2]]
        if "articles/" in inner:
            return strip_active(absolutise_hrefs(inner, path, site))
    raise SystemExit("The sidebar menu has no article links to share")


def measure(site: Path) -> tuple[int, int, int]:
    sizes: list[int] = []
    total = 0
    for path in site.rglob("*"):
        if not path.is_file():
            continue
        size = path.stat().st_size
        total += size
        if path.suffix == ".html" and "site_libs" not in path.parts:
            sizes.append(size)
    sizes.sort()
    median = sizes[len(sizes) // 2] if sizes else 0
    return len(sizes), median, total


def main() -> None:
    if not SITE_DIR.is_dir():
        raise SystemExit(f"Missing site: {SITE_DIR}")
    index = SITE_DIR / "index.html"
    if not index.is_file():
        raise SystemExit("Missing _site/index.html")
    source = index.read_text(encoding="utf-8")
    found = sidebar_list(source)
    if not found:
        raise SystemExit("index.html has no sidebar menu")
    _ul, inner_start, inner_end = found
    full = menu_with_articles(SITE_DIR, source[inner_start:inner_end])
    payload = json.dumps({"html": full}, ensure_ascii=False, separators=(",", ":"))
    (SITE_DIR / "sidebar-nav.js").write_text(
        "window.__STATWIKI_SIDEBAR = " + payload + ";\n",
        encoding="utf-8",
    )
    template = prune_menu(full)
    if "articles/" in template:
        raise SystemExit("The no-JavaScript sidebar still lists articles")
    changed = 0
    for path in sorted(SITE_DIR.rglob("*.html")):
        if "site_libs" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        bounds = sidebar_list(text)
        if not bounds:
            continue
        _ul, start, end = bounds
        menu = apply_open_state(fallback_for(template, path), section_open_state(text[start:end]))
        updated = text[:start] + menu + text[end:]
        updated = strip_bucket_crumbs(updated)
        updated = insert_loader(updated, path)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    pages, median, total = measure(SITE_DIR)
    print(
        f"Shared sidebar on {changed} pages; "
        f"{pages} HTML pages, median {median} bytes, _site {total} bytes"
    )


if __name__ == "__main__":
    sys.exit(main() or 0)
