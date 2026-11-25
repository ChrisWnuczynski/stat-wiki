"""Search result counts are a polite live region."""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MARK = 'role="status" aria-live="polite" aria-atomic="true"'


class SearchStatusTests(unittest.TestCase):
    def test_home_search_and_not_found_name_the_status_region(self) -> None:
        wiki = (ROOT / "build_wiki.py").read_text(encoding="utf-8")
        self.assertIn(f'<p id="home-search-note" class="home-search-note" {MARK}></p>', wiki)
        self.assertIn(f'<p id="site-search-note" {MARK}></p>', wiki)
        missing = (ROOT / "404.qmd").read_text(encoding="utf-8")
        self.assertIn(f'<p id="nf-note" {MARK}></p>', missing)
        for path in (ROOT / "home-search.js", ROOT / "404.qmd", ROOT / "build_wiki.py"):
            text = path.read_text(encoding="utf-8")
            self.assertIn('setAttribute("aria-live", "polite")', text, path.name)
            self.assertIn('setAttribute("role", "status")', text, path.name)


if __name__ == "__main__":
    unittest.main()
