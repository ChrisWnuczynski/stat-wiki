"""Typing in search updates the live count, including when nothing matches."""

from __future__ import annotations

import shutil
import tempfile
import threading
import unittest
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

import build_wiki


ROOT = Path(__file__).resolve().parent

HOME = """<!DOCTYPE html><html><body>
<form id="home-search" role="search">
  <label for="home-search-q">Search</label>
  <input id="home-search-q" type="search" name="q" autocomplete="off">
</form>
<p id="home-search-note" class="home-search-note" role="status" aria-live="polite" aria-atomic="true"></p>
<ul id="home-search-results" role="listbox" hidden></ul>
<script type="module" src="home-search.js"></script>
</body></html>
"""

INDEX = """[
  {"href": "articles/variance.html", "title": "Variance", "text": "The variance of a sample."}
]
"""


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:
        return


class SearchStatusTests(unittest.TestCase):
    def test_typing_and_submitting_updates_the_count_and_the_empty_state(self) -> None:
        from playwright.sync_api import sync_playwright

        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            shutil.copy(ROOT / "home-search.js", site / "home-search.js")
            shutil.copy(ROOT / "search-rank.js", site / "search-rank.js")
            (site / "search.json").write_text(INDEX, encoding="utf-8")
            (site / "home.html").write_text(HOME, encoding="utf-8")
            with patch.object(build_wiki, "WIKI", site):
                build_wiki.write_search_page()
            qmd = (site / "search.qmd").read_text(encoding="utf-8")
            fragment = qmd.split("```{=html}", 1)[1].rsplit("```", 1)[0]
            (site / "search.html").write_text(
                "<!DOCTYPE html><html><body>\n" + fragment + "\n</body></html>",
                encoding="utf-8",
            )
            server = ThreadingHTTPServer(("127.0.0.1", 0), partial(Quiet, directory=str(site)))
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            self.addCleanup(server.shutdown)
            self.addCleanup(server.server_close)
            base = f"http://127.0.0.1:{server.server_port}/"
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch()
                page = browser.new_page()
                try:
                    page.goto(base + "home.html", wait_until="load")
                    box = page.locator("#home-search-q")
                    note = page.locator("#home-search-note")
                    box.fill("variance")
                    page.wait_for_function(
                        "() => document.getElementById('home-search-note').textContent === '1 result.'"
                    )
                    box.fill("zzzznotapage")
                    page.wait_for_function(
                        "() => document.getElementById('home-search-note').textContent === 'No pages match.'"
                    )
                    box.press("Enter")
                    self.assertEqual(note.inner_text(), "No pages match.")

                    page.goto(base + "search.html", wait_until="load")
                    field = page.locator("#site-search-q")
                    status = page.locator("#site-search-note")
                    field.fill("variance")
                    page.locator("#site-search button").click()
                    page.wait_for_function(
                        "() => document.getElementById('site-search-note').textContent === '1 page.'"
                    )
                    field.fill("zzzznotapage")
                    page.locator("#site-search button").click()
                    page.wait_for_function(
                        "() => document.getElementById('site-search-note').textContent === '0 pages.'"
                    )
                    self.assertEqual(status.inner_text(), "0 pages.")
                finally:
                    browser.close()


if __name__ == "__main__":
    unittest.main()
