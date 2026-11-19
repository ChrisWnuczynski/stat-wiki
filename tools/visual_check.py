"""Render checks for the visual audit.

Layout checks use headless Chromium. The maths scan reads every rendered page
and ignores KaTeX, so a dropped command cannot hide inside a formula.

    python tools/visual_check.py --site _site --screenshots /opt/cursor/artifacts
"""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

MATH_RE = re.compile(r"\\\(|\\\[|\^\{|_\{|\(\s*\)|\[\s*,\s*\]")
SKIP_TAGS = {"script", "style", "katex", "annotation", "code", "pre"}


class VisibleText(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.nodes: list[str] = []
        self._skip = 0
        self._stack: list[bool] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        classes = dict(attrs).get("class", "")
        names = set(str(classes).split())
        skip = tag in SKIP_TAGS or "katex" in names or "math" in names
        self._stack.append(skip)
        if skip:
            self._skip += 1

    def handle_endtag(self, tag: str) -> None:
        if self._stack and self._stack.pop() and self._skip:
            self._skip -= 1

    def handle_data(self, data: str) -> None:
        if self._skip or not data.strip():
            return
        self.nodes.append(data)


def maths_hits(html: str) -> list[str]:
    """Broken fragments in one text node.

    A parenthesis that only wraps a rendered formula is two text nodes around
    the formula, so it is not an empty pair.
    """
    parser = VisibleText()
    parser.feed(html)
    hits: list[str] = []
    for node in parser.nodes:
        hits.extend(match.group(0) for match in MATH_RE.finditer(node))
    return hits


def scan_site(site: Path) -> tuple[int, list[tuple[str, str]]]:
    pages = sorted(site.rglob("*.html"))
    bad: list[tuple[str, str]] = []
    for path in pages:
        hits = maths_hits(path.read_text(encoding="utf-8", errors="replace"))
        if hits:
            bad.append((path.relative_to(site).as_posix(), hits[0]))
    return len(pages), bad


def layout_checks(site: Path, screenshots: Path | None) -> list[str]:
    from playwright.sync_api import sync_playwright

    problems: list[str] = []
    screenshots = screenshots.resolve() if screenshots else None
    if screenshots:
        screenshots.mkdir(parents=True, exist_ok=True)

    def page_url(name: str) -> str:
        return (site / name).resolve().as_uri()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        for width in (1024, 1280, 390):
            page.set_viewport_size({"width": width, "height": 800})
            page.goto(page_url("articles/beta-distribution.html"), wait_until="networkidle")
            info = page.evaluate(
                """() => {
                  const box = document.querySelector('.infobox');
                  const content = document.querySelector('#quarto-document-content');
                  const table = box && box.querySelector('table');
                  if (!box || !table || !content) return {missing: true};
                  const br = box.getBoundingClientRect();
                  const tr = table.getBoundingClientRect();
                  const floated = getComputedStyle(box).float === 'right' || getComputedStyle(box).float === 'left';
                  const contentWidth = content.getBoundingClientRect().width;
                  let column = contentWidth;
                  if (floated) column = contentWidth - br.width - 24;
                  return {
                    floated,
                    tablePast: tr.right - br.right,
                    tableBefore: br.left - tr.left,
                    paraWidth: column,
                    contentWidth,
                  };
                }"""
            )
            if info.get("missing"):
                problems.append(f"beta-distribution at {width}: no infobox table")
            else:
                if info["tablePast"] > 2 or info["tableBefore"] > 2:
                    problems.append(
                        f"beta-distribution at {width}: table escapes the infobox "
                        f"by {info['tablePast']:.1f}px"
                    )
                if width >= 1000:
                    if info["paraWidth"] < 400:
                        problems.append(
                            f"beta-distribution at {width}: body column is {info['paraWidth']:.0f}px"
                        )
                elif info["floated"] or info["paraWidth"] < info["contentWidth"] * 0.85:
                    problems.append(f"beta-distribution at {width}: infobox still squeezes the column")
            if screenshots and width in {1024, 1280}:
                page.screenshot(path=str(screenshots / f"beta-distribution-{width}.png"), full_page=False)

        for name, shot in (
            ("articles/conditional-expectation.html", "conditional-expectation.png"),
            ("articles/kurtosis.html", "kurtosis.png"),
        ):
            page.set_viewport_size({"width": 1280, "height": 800})
            page.goto(page_url(name), wait_until="networkidle")
            hits = maths_hits(page.content())
            if hits:
                problems.append(f"{name}: visible maths fragment {hits[0]!r}")
            active = page.locator("#quarto-sidebar a.sidebar-link.active")
            if name.endswith("kurtosis.html") and active.count() < 1:
                problems.append("kurtosis: sidebar has no active item")
            if screenshots:
                page.screenshot(path=str(screenshots / shot), full_page=False)
                if name.endswith("kurtosis.html"):
                    page.screenshot(path=str(screenshots / "kurtosis-sidebar-desktop.png"), full_page=False)
                    page.set_viewport_size({"width": 390, "height": 844})
                    toggle = page.locator(".quarto-btn-toggle, #quarto-sidebar-toggle").first
                    if toggle.count():
                        toggle.click()
                        page.wait_for_timeout(400)
                    page.screenshot(path=str(screenshots / "kurtosis-sidebar-mobile.png"), full_page=False)
        browser.close()
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, default=Path("_site"))
    parser.add_argument("--screenshots", type=Path)
    parser.add_argument("--skip-browser", action="store_true")
    args = parser.parse_args()
    site = args.site
    if not site.is_dir():
        print(f"No rendered site at {site}", file=sys.stderr)
        return 1
    total, bad = scan_site(site)
    print(f"maths pages: {len(bad)} of {total} still show a broken fragment")
    for path, hit in bad[:20]:
        print(f"  {path}: {hit}")
    problems = [] if args.skip_browser else layout_checks(site, args.screenshots)
    for problem in problems:
        print("layout:", problem)
    if bad or problems:
        return 1
    print("visual checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
