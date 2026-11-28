"""The post-render template fixes and the home page heading order."""

from __future__ import annotations

import re
import tempfile
import unittest
from pathlib import Path

import build_wiki
import page_a11y

# The navbar toggle and main element exactly as Quarto 1.6.40 writes them.
TOGGLER = (
    '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" '
    'data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" role="menu" '
    'aria-expanded="false" aria-label="Toggle navigation" '
    'onclick="if (window.quartoToggleHeadroom) { window.quartoToggleHeadroom(); }">'
)
MAIN = '<main class="content" id="quarto-document-content">'
PAGE = (
    "<html><body>\n"
    f"<header><nav>{TOGGLER}<span class=\"navbar-toggler-icon\"></span></button>\n"
    '<ul role="menu"><li role="menuitem">kept</li></ul></nav></header>\n'
    f'{MAIN}\n<a class="skip-link" href="#quarto-document-content">Skip</a>\n'
    '<script>var m = doc.querySelector("main#quarto-document-content");</script>\n'
    "</main></body></html>\n"
)


class TemplateFixTests(unittest.TestCase):
    def test_toggle_loses_only_the_menu_role(self) -> None:
        fixed = page_a11y.fix_page(PAGE)
        button = re.search(r'<button class="navbar-toggler"[^>]*>', fixed).group(0)
        self.assertNotIn("role=", button)
        for kept in ('aria-controls="navbarCollapse"', 'aria-expanded="false"',
                     'aria-label="Toggle navigation"', 'data-bs-toggle="collapse"'):
            self.assertIn(kept, button)
        # A role="menu" anywhere else on the page is not the toggle's to drop.
        self.assertIn('<ul role="menu">', fixed)

    def test_skip_link_target_is_focusable(self) -> None:
        fixed = page_a11y.fix_page(PAGE)
        self.assertIn('<main class="content" id="quarto-document-content" tabindex="-1">', fixed)
        self.assertEqual(fixed.count('tabindex="-1"'), 1)
        # Script text that names the element is not a tag.
        self.assertIn('doc.querySelector("main#quarto-document-content")', fixed)

    def test_existing_tabindex_is_kept(self) -> None:
        page = PAGE.replace(MAIN, '<main class="content" id="quarto-document-content" tabindex="0">')
        self.assertIn('tabindex="0">', page_a11y.focusable_main(page))
        self.assertNotIn('tabindex="-1"', page_a11y.focusable_main(page))

    def test_fix_is_idempotent(self) -> None:
        once = page_a11y.fix_page(PAGE)
        self.assertEqual(page_a11y.fix_page(once), once)

    def test_pages_without_the_template_are_unchanged(self) -> None:
        redirect = "<html><head><title>Redirect</title></head><body><script>var redirects = {};</script></body></html>"
        self.assertEqual(page_a11y.fix_page(redirect), redirect)

    def test_main_rewrites_the_site_and_checks_the_home_page(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            (site / "articles").mkdir()
            (site / "site_libs").mkdir()
            (site / "index.html").write_text(PAGE, encoding="utf-8")
            (site / "articles" / "variance.html").write_text(PAGE, encoding="utf-8")
            (site / "site_libs" / "untouched.html").write_text(PAGE, encoding="utf-8")
            page_a11y.main(site)
            for rel in ("index.html", "articles/variance.html"):
                text = (site / rel).read_text(encoding="utf-8")
                self.assertEqual(text, page_a11y.fix_page(PAGE), rel)
            self.assertEqual((site / "site_libs" / "untouched.html").read_text(encoding="utf-8"), PAGE)
            # A second run over a processed site changes nothing.
            page_a11y.main(site)
            self.assertEqual((site / "index.html").read_text(encoding="utf-8"), page_a11y.fix_page(PAGE))

    def test_post_render_runs_the_fix(self) -> None:
        source = (build_wiki.WIKI / "build_wiki.py").read_text(encoding="utf-8")
        block = re.search(r"  post-render:\n((?:    - .+\n)+)", source).group(1)
        self.assertIn("    - page_a11y.py\n", block)


class HomeHeadingTests(unittest.TestCase):
    def test_home_headings_do_not_skip_a_level(self) -> None:
        home = build_wiki.WIKI / "index.qmd"
        if not home.is_file():
            self.skipTest("Run python build_wiki.py first")
        text = home.read_text(encoding="utf-8")
        levels = []
        for line in text.splitlines():
            raw = re.match(r"<h([1-6])\b", line.strip())
            md = re.match(r"(#{1,6}) ", line)
            if raw:
                levels.append(int(raw.group(1)))
            elif md:
                levels.append(len(md.group(1)))
        # The page title is the h1.
        previous = 1
        for level in levels:
            self.assertLessEqual(level, previous + 1, f"heading levels {levels}")
            previous = level
        self.assertEqual(levels[0], 2)
        self.assertIn('<h2 class="visually-hidden">Browse the wiki</h2>', text)


if __name__ == "__main__":
    unittest.main()
