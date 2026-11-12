"""Confirm every internal link on the overview points at a file that exists.

Run from the wiki root, after build_wiki.py:

    python check_overview_links.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import build_wiki

ROOT = Path(__file__).resolve().parent
PAGE = ROOT / "overview.qmd"
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"^```")


def body(text: str) -> str:
    pieces = []
    fenced = False
    for line in text.splitlines(keepends=True):
        if FENCE.match(line):
            fenced = not fenced
            continue
        if not fenced:
            pieces.append(line)
    return "".join(pieces)


def main() -> None:
    if not PAGE.is_file():
        raise SystemExit("Missing overview.qmd")
    problems: list[str] = []
    targets: set[str] = set()
    for match in LINK.finditer(body(PAGE.read_text(encoding="utf-8"))):
        raw = match.group(1)
        if raw.startswith(("http://", "https://", "mailto:")):
            problems.append(f"external link {raw}")
            continue
        path = raw.split("#", 1)[0]
        anchor = raw.split("#", 1)[1] if "#" in raw else ""
        if not path:
            problems.append(f"link has no file: {raw}")
            continue
        target = (PAGE.parent / path).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            problems.append(f"link leaves the site: {raw}")
            continue
        if not target.is_file():
            problems.append(f"missing file for {raw}")
            continue
        targets.add(target.relative_to(ROOT).as_posix())
        if anchor and anchor not in target.read_text(encoding="utf-8"):
            problems.append(f"missing anchor #{anchor} in {path}")

    for part, files in build_wiki.PARTS:
        for filename, kind in files:
            if kind != "notes":
                continue
            rel = f"notes/{filename}"
            if rel not in targets:
                problems.append(f"{part} chapter not linked: {rel}")

    home = ROOT / "index.qmd"
    config = ROOT / "_quarto.yml"
    if home.is_file():
        home_text = home.read_text(encoding="utf-8")
        start = home_text.find("## New to statistics? Start here")
        if start < 0 or "overview.qmd" not in home_text[start : start + 500]:
            problems.append("homepage start-here box does not lead with overview.qmd")
    else:
        problems.append("index.qmd is missing; run build_wiki.py first")
    if config.is_file():
        yml = config.read_text(encoding="utf-8")
        if "href: overview.qmd" not in yml:
            problems.append("navbar does not link overview.qmd")
    else:
        problems.append("_quarto.yml is missing; run build_wiki.py first")

    if problems:
        raise SystemExit("Overview links:\n  " + "\n  ".join(problems))
    print(f"Overview: {len(targets)} internal targets, every chapter linked.")


if __name__ == "__main__":
    sys.exit(main())
