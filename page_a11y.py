"""Correct two accessibility faults in Quarto's page template after render.

Quarto 1.6.40 writes the navbar toggle as ``<button class="navbar-toggler"
... role="menu">``. The button opens a collapsed list of links; it is not a
menu, and the menu role tells assistive technology to expect menu items and
arrow-key navigation that are not there. ``aria-expanded`` and
``aria-controls`` already describe the disclosure, so the role is dropped.

The skip link points at ``main#quarto-document-content``, which Quarto writes
without a ``tabindex``. The skip-link script in ``_theme-body.html`` adds
``tabindex="-1"`` when the link is used, but the static page leaves the target
unable to take focus. Writing the attribute into the page makes the target
focusable whether or not JavaScript runs. ``styles.css`` already removes the
outline from that programmatic focus.

Both changes leave a page alone when it has already been processed.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE_DIR = ROOT / "_site"

TOGGLER = re.compile(r'<button\b[^>]*\bclass="navbar-toggler(?:\s[^"]*)?"[^>]*>')
MENU_ROLE = re.compile(r'\s+role="menu"')
MAIN = re.compile(r'<main\b[^>]*\bid="quarto-document-content"[^>]*>')


def drop_toggler_menu_role(html: str) -> str:
    """Remove role="menu" from the navbar toggle button only."""

    def fix(match: re.Match[str]) -> str:
        return MENU_ROLE.sub("", match.group(0))

    return TOGGLER.sub(fix, html, count=1)


def focusable_main(html: str) -> str:
    """Give the skip-link target tabindex="-1" unless it already has a tabindex."""

    def fix(match: re.Match[str]) -> str:
        tag = match.group(0)
        if re.search(r"\stabindex=", tag):
            return tag
        return tag[:-1] + ' tabindex="-1">'

    return MAIN.sub(fix, html, count=1)


def fix_page(html: str) -> str:
    return focusable_main(drop_toggler_menu_role(html))


def main(site_dir: Path = SITE_DIR) -> None:
    if not site_dir.is_dir():
        raise SystemExit(f"Missing site: {site_dir}")
    changed = 0
    for path in sorted(site_dir.rglob("*.html")):
        if "site_libs" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        updated = fix_page(text)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    home = site_dir / "index.html"
    if home.is_file():
        text = home.read_text(encoding="utf-8")
        toggler = TOGGLER.search(text)
        if toggler and MENU_ROLE.search(toggler.group(0)):
            raise SystemExit("The navbar toggle still has role=menu")
        target = MAIN.search(text)
        if target is None or "tabindex=" not in target.group(0):
            raise SystemExit("The skip-link target on the home page is not focusable")
    print(f"Page template accessibility fixes on {changed} pages")


if __name__ == "__main__":
    sys.exit(main() or 0)
