"""Fail when a laboratory would send KaTeX a site shorthand it cannot render.

Articles are expanded by build_wiki.expand_macros. Laboratories are not, so
the same definitions have to reach KaTeX as macros. A shorthand that is
neither a native KaTeX command nor in that generated table fails this check.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import build_wiki


def main() -> None:
    problems = build_wiki.lab_shorthand_problems(ROOT)
    header = ROOT / build_wiki.KATEX_MACRO_HEADER
    if not header.is_file():
        problems.append(f"missing {build_wiki.KATEX_MACRO_HEADER}")
    elif header.read_text(encoding="utf-8") != build_wiki.katex_macro_header():
        problems.append(
            f"{build_wiki.KATEX_MACRO_HEADER} does not match the table generated from ZERO_ARG and ONE_ARG"
        )
    yml = ROOT / "_quarto.yml"
    if not yml.is_file():
        problems.append("missing _quarto.yml")
    elif "_katex-macros.html" not in yml.read_text(encoding="utf-8"):
        problems.append("_quarto.yml does not include the KaTeX macro header")
    if problems:
        raise SystemExit("Laboratory shorthand KaTeX cannot render:\n  " + "\n  ".join(problems))
    print(f"Laboratory shorthand is covered ({len(build_wiki.katex_macro_definitions())} KaTeX macros)")


if __name__ == "__main__":
    main()
