"""Fail when the committed katex_macros.json is stale.

The Ask widget inlines the committed katex_macros.json when Vite bundles it,
while build_wiki.py rewrites that file from katex_macro_definitions() every
time it runs. A change that edits the Python definitions without regenerating
the JSON therefore ships the old table to Ask while the pages and the
pre-render get the new one, and any later build_wiki.py run hides the gap by
regenerating the file. This check compares the committed file with the
generated text and must run before anything regenerates it.

    python tools/check_katex_macros_fresh.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import build_wiki


def stale_problems(root: Path) -> list[str]:
    """How the committed macro table at root differs from the generated one."""
    path = root / build_wiki.KATEX_MACROS_JSON
    if not path.is_file():
        return [
            f"{build_wiki.KATEX_MACROS_JSON} is missing. "
            "Regenerate it with: python -c \"import build_wiki; build_wiki.write_katex_macro_header()\""
        ]
    committed_text = path.read_text(encoding="utf-8")
    if committed_text == build_wiki.katex_macros_json_text():
        return []
    try:
        committed = json.loads(committed_text)
    except json.JSONDecodeError as error:
        return [f"{build_wiki.KATEX_MACROS_JSON} is not valid JSON: {error}"]
    expected = build_wiki.katex_macro_definitions()
    problems = []
    for name in sorted(set(expected) - set(committed)):
        problems.append(f"{name} is defined in build_wiki.py but missing from {build_wiki.KATEX_MACROS_JSON}")
    for name in sorted(set(committed) - set(expected)):
        problems.append(f"{name} is in {build_wiki.KATEX_MACROS_JSON} but no longer defined in build_wiki.py")
    for name in sorted(set(committed) & set(expected)):
        if committed[name] != expected[name]:
            problems.append(
                f"{name} is {committed[name]!r} in {build_wiki.KATEX_MACROS_JSON} "
                f"but {expected[name]!r} in build_wiki.py"
            )
    if not problems:
        problems.append(f"{build_wiki.KATEX_MACROS_JSON} differs from the generated table only in formatting")
    problems.append(
        "Regenerate and commit the table with: "
        "python -c \"import build_wiki; build_wiki.write_katex_macro_header()\""
    )
    return problems


def main() -> int:
    problems = stale_problems(ROOT)
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        return 1
    print(f"{build_wiki.KATEX_MACROS_JSON} matches katex_macro_definitions().")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
