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
        import search_meta

        # The import Quarto emits when the variable does not win. Both live bundles use this shape.
        for sample in (
            '@import"https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;400;700&display=swap";:root{}',
            '@import"https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap";:root{}',
            '@import url("https://fonts.googleapis.com/css2?family=Source+Sans+Pro&display=swap");',
        ):
            cleaned = search_meta.strip_google_font_imports(sample)
            self.assertNotIn("fonts.googleapis.com", cleaned)
            self.assertNotIn("@import", cleaned)
        bootstrap = build_wiki.WIKI / "_site" / "site_libs" / "bootstrap"
        if not bootstrap.is_dir():
            return
        css_files = sorted(bootstrap.glob("*.css"))
        self.assertTrue(css_files, "built Bootstrap CSS is missing")
        for path in css_files:
            text = path.read_text(encoding="utf-8", errors="replace")
            self.assertNotIn(
                "fonts.googleapis.com",
                text,
                f"{path.name} still requests a Google font",
            )


if __name__ == "__main__":
    unittest.main()
