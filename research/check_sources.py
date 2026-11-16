"""Fail early when the private Dodge reference is unavailable for research."""

from __future__ import annotations

import argparse
import csv
import os
import sys
from pathlib import Path


def source_candidates(explicit: str | None) -> list[Path]:
    if explicit:
        return [Path(explicit).expanduser()]
    configured = os.environ.get("STATWIKI_DODGE_DIR")
    if configured:
        return [Path(configured).expanduser()]
    workspace = Path(__file__).resolve().parents[2]
    return [Path.home() / "statwiki-sources" / "dodge2008",
            workspace / "statwiki-sources" / "dodge2008"]


def validate(path: Path) -> list[str]:
    missing = [name for name in ("index.tsv", "dodge2008.pdf", "pages/pdf-0009.txt")
               if not (path / name).is_file()]
    if missing:
        return [f"missing {', '.join(missing)}"]
    with (path / "index.tsv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    required = {"entry", "printed_page", "pdf_page"}
    if not rows or not required <= rows[0].keys():
        return ["index.tsv has no entry/printed_page/pdf_page rows"]
    if not any(row["entry"] == "Binomial Distribution" and row["printed_page"] == "44"
               for row in rows):
        return ["index.tsv does not map Binomial Distribution to printed page 44"]
    sample = (path / "pages" / "pdf-0009.txt").read_text(encoding="utf-8")
    if not sample.startswith("PDF page: 9\nPrinted page: 1\n"):
        return ["pages/pdf-0009.txt lacks the PDF and printed page markers"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", help="check this Dodge directory only")
    args = parser.parse_args()
    problems = []
    for path in source_candidates(args.source_dir):
        errors = validate(path)
        if not errors:
            print(f"Dodge source ready: {path}")
            return 0
        problems.append(f"{path}: {'; '.join(errors)}")
    print("Dodge source unavailable. Stop before writing new research pages.", file=sys.stderr)
    for problem in problems:
        print(problem, file=sys.stderr)
    print("Attach an authorized Dodge PDF and extract it outside the repository.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
