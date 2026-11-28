"""Descriptive link text and top-bar orientation (STA-197)."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

import build_wiki
import sidebar_share

ROOT = Path(__file__).resolve().parent
SITE = sidebar_share.SITE_DIR

# The top bar as Quarto 1.6.40 writes it on an article: "Main page" is marked
# current because the sidebar also links to the home page.
NAVBAR = """<nav class="navbar">
<div class="collapse navbar-collapse" id="navbarCollapse">
<ul class="navbar-nav navbar-nav-scroll me-auto">
  <li class="nav-item">
    <a class="nav-link active" href="{up}index.html" aria-current="page"><span class="menu-text">Main page</span></a>
  </li>
  <li class="nav-item dropdown ">
    <a class="nav-link dropdown-toggle" href="#" id="nav-menu-study" role="link" data-bs-toggle="dropdown" aria-expanded="false"><span class="menu-text">Study</span></a>
    <ul class="dropdown-menu" aria-labelledby="nav-menu-study">
      <li><a class="dropdown-item" href="{up}overview.html"><span class="dropdown-text">Overview</span></a></li>
      <li><a class="dropdown-item" href="{up}notes/index.html"><span class="dropdown-text">Topics</span></a></li>
    </ul>
  </li>
  <li class="nav-item dropdown ">
    <a class="nav-link dropdown-toggle" href="#" id="nav-menu-reference" role="link" data-bs-toggle="dropdown" aria-expanded="false"><span class="menu-text">Reference</span></a>
    <ul class="dropdown-menu" aria-labelledby="nav-menu-reference">
      <li><a class="dropdown-item" href="{up}reference/index.html"><span class="dropdown-text">Lookup pages</span></a></li>
      <li><a class="dropdown-item" href="{up}reference/glossary.html"><span class="dropdown-text">Glossary and index</span></a></li>
    </ul>
  </li>
</ul>
</div>
</nav>
<nav id="quarto-sidebar"><a class="sidebar-link active" href="{up}index.html" aria-current="page">Main page</a></nav>
"""


def page(rel: str) -> tuple[Path, str]:
    depth = rel.count("/")
    return SITE / rel, NAVBAR.format(up="../" * depth if depth else "./")


def marked(html: str) -> dict[str, tuple[bool, str | None]]:
    """Top-bar link text -> (has the active class, aria-current value)."""
    bar = html[html.find('id="navbarCollapse"'): html.find("</nav>")]
    out = {}
    for tag, text in re.findall(r'(<a\b[^>]*>)<span class="[^"]*">([^<]+)</span>', bar):
        classes = re.search(r'class="([^"]*)"', tag).group(1).split()
        current = re.search(r'aria-current="([^"]*)"', tag)
        out[text] = ("active" in classes, current.group(1) if current else None)
    return out


class StaticTopBarTests(unittest.TestCase):
    def test_an_article_is_in_topics_not_on_the_main_page(self):
        path, html = page("articles/variance.html")
        state = marked(sidebar_share.orient_navbar(html, path))
        self.assertEqual(state["Main page"], (False, None))
        self.assertEqual(state["Topics"], (True, "true"), "Topics is the current section, not the current page")
        self.assertEqual(state["Study"], (True, None))
        self.assertEqual(state["Glossary and index"], (False, None))
        self.assertEqual(state["Reference"], (False, None))

    def test_the_main_page_is_current_only_on_the_home_page(self):
        path, html = page("index.html")
        state = marked(sidebar_share.orient_navbar(html, path))
        self.assertEqual(state["Main page"], (True, "page"))
        self.assertEqual(state["Topics"], (False, None))
        self.assertEqual(state["Study"], (False, None))

    def test_a_page_in_the_menu_is_the_current_page(self):
        for rel, name in (("reference/glossary.html", "Glossary and index"), ("notes/index.html", "Topics")):
            with self.subTest(rel=rel):
                path, html = page(rel)
                state = marked(sidebar_share.orient_navbar(html, path))
                self.assertEqual(state[name], (True, "page"))
                self.assertEqual(state["Main page"], (False, None))
                self.assertEqual(state["Study"], (False, None))

    def test_other_pages_claim_nothing_they_are_not(self):
        path, html = page("questions/q-12.html")
        state = marked(sidebar_share.orient_navbar(html, path))
        self.assertTrue(all(value == (False, None) for value in state.values()), state)

    def test_only_the_top_bar_is_changed_and_a_second_pass_changes_nothing(self):
        path, html = page("articles/variance.html")
        once = sidebar_share.orient_navbar(html, path)
        self.assertEqual(sidebar_share.orient_navbar(once, path), once)
        self.assertIn('<a class="sidebar-link active" href="../index.html" aria-current="page">', once)
        self.assertEqual(sidebar_share.orient_navbar("<html><body>No navbar</body></html>", path),
                         "<html><body>No navbar</body></html>")

    def test_the_site_pass_runs_it(self):
        source = (ROOT / "sidebar_share.py").read_text(encoding="utf-8")
        self.assertIn("updated = orient_navbar(updated, path)", source)


class PageScriptTests(unittest.TestCase):
    def test_articles_map_to_topics_in_the_study_menu_not_the_glossary(self):
        script = build_wiki.RANDOM_AND_FILTER_JS
        start = script.index("Highlight the top-bar section")
        block = script[start: script.index("window.wikiFilter", start)]
        self.assertIn('/\\/notes\\/|\\/articles\\//.test(here) ? "notes/index.html"', block)
        self.assertNotIn("glossary|\\/articles", block)
        self.assertIn('/\\/articles\\//.test(here) ? "Study"', block)
        self.assertIn('link.setAttribute("aria-current", "true")', block)


class LinkTextTests(unittest.TestCase):
    def test_check_yourself_link_names_its_question(self):
        article = {"slug": "fixture", "path": ROOT / "articles/fixture.qmd"}
        question = {
            "id": "fixture-q1", "title": "Pareto likelihood and Gamma posterior",
            "path": ROOT / "questions/fixture-q1.qmd",
            "prepared_body": "Body.", "prepared_answer": "Answer.",
        }
        check = build_wiki._render_bank_check(article, question)
        self.assertIn("[Question-bank page: Pareto likelihood and Gamma posterior](../questions/fixture-q1.qmd)", check)

    def test_generated_check_yourself_links_are_never_generic(self):
        pages = sorted((ROOT / "articles").glob("*.qmd"))
        if not pages:
            self.skipTest("Generated wiki directories are not built yet")
        generic = [p.name for p in pages if "[Question-bank page](" in p.read_text(encoding="utf-8")]
        self.assertEqual(generic, [])
        named = sum(p.read_text(encoding="utf-8").count("[Question-bank page: ") for p in pages)
        self.assertGreater(named, 0)

    def test_home_see_all_links_name_their_destinations(self):
        home = ROOT / "index.qmd"
        if not home.is_file():
            self.skipTest("Generated wiki directories are not built yet")
        text = home.read_text(encoding="utf-8")
        self.assertNotIn("[See all](", text)
        labels = re.findall(r"\[(See [^\]]+)\]\([^)]*\)\{\.library-more\}", text)
        self.assertGreaterEqual(len(labels), 10)
        self.assertEqual(len(labels), len(set(labels)), f"repeated link text: {labels}")
        for expected in ("See all questions", "See all laboratories", "See all reference pages",
                         "See all distributions", "See all topics in Probability"):
            self.assertIn(expected, labels)


if __name__ == "__main__":
    unittest.main()
