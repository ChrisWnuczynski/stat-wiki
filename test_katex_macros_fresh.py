"""The committed KaTeX macro table check passes fresh and fails stale."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import build_wiki
from tools.check_katex_macros_fresh import stale_problems


class KatexMacrosFreshTests(unittest.TestCase):
    def test_committed_table_is_current(self) -> None:
        root = Path(__file__).resolve().parent
        self.assertEqual(stale_problems(root), [])

    def test_missing_changed_and_extra_entries_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.assertTrue(any("missing" in problem for problem in stale_problems(root)))
            (root / "katex_macros.json").write_text(
                build_wiki.katex_macros_json_text(), encoding="utf-8"
            )
            self.assertEqual(stale_problems(root), [])
            stale = build_wiki.katex_macro_definitions()
            stale[r"\E"] = r"\mathrm{E}"
            stale[r"\Stale"] = r"\operatorname{Stale}"
            del stale[r"\Var"]
            (root / "katex_macros.json").write_text(
                json.dumps(stale, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            problems = stale_problems(root)
            self.assertTrue(any(r"\E" in problem for problem in problems), problems)
            self.assertTrue(any(r"\Stale" in problem for problem in problems), problems)
            self.assertTrue(any(r"\Var" in problem for problem in problems), problems)


if __name__ == "__main__":
    unittest.main()
