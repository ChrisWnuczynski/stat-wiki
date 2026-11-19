"""The top bar stays short enough that search and the theme toggle fit."""

from __future__ import annotations

import re
import unittest

import build_wiki


class NavbarTests(unittest.TestCase):
    def test_five_items_collapse_below_xl(self) -> None:
        nav = build_wiki.navbar_yaml()
        self.assertIn("collapse-below: xl\n", nav)
        top = re.findall(r"(?m)^      - text: .+$", nav)
        self.assertEqual(
            top,
            [
                "      - text: Main page",
                "      - text: Study",
                "      - text: Questions",
                "      - text: Reference",
                "      - text: Laboratories",
            ],
        )
        self.assertIn("href: overview.qmd", nav)
        self.assertIn("href: reference/glossary.qmd", nav)
        self.assertIn("href: questions/random.qmd", nav)
        # Menu entries are indented further, so they are not a sixth top-level item.
        self.assertEqual(nav.count("\n      - text:"), 5)

    def test_themes_do_not_load_a_web_font(self) -> None:
        scss = (build_wiki.WIKI / "theme.scss").read_text(encoding="utf-8")
        self.assertIn("$web-font-path: false;", scss)
        yml_src = (build_wiki.WIKI / "build_wiki.py").read_text(encoding="utf-8")
        self.assertIn("light: [cosmo, theme.scss]", yml_src)
        self.assertIn("dark: [darkly, theme.scss]", yml_src)


if __name__ == "__main__":
    unittest.main()
