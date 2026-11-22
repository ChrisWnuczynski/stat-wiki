"""Unit checks for the shared sidebar and the breadcrumb cleanup."""

import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

import build_wiki
import sidebar_share


def _script_sources(html):
    class Scripts(HTMLParser):
        def __init__(self):
            super().__init__()
            self.sources = []

        def handle_starttag(self, tag, attrs):
            if tag == "script" and "src" in dict(attrs):
                self.sources.append(dict(attrs)["src"])

    parser = Scripts()
    parser.feed(html)
    return parser.sources


SAMPLE = """
<nav id="quarto-sidebar">
<div class="sidebar-menu-container">
<ul class="list-unstyled">
<li class="sidebar-item-section">
<a class="sidebar-link" href="notes/fundamentals.qmd">Overview</a>
<ul>
<li><a class="sidebar-link active" href="./articles/mean.qmd" aria-current="page">Mean</a></li>
<li><a class="sidebar-link" href="../articles/variance.qmd">Variance</a></li>
</ul>
</li>
<li class="sidebar-item-section">
<span class="menu-text">Further reading</span>
<ul>
<li class="sidebar-item-section">
<span class="menu-text">D–R</span>
<ul>
<li><a class="sidebar-link" href="articles/kurtosis.qmd">Kurtosis</a></li>
</ul>
</li>
</ul>
</li>
<li><a class="sidebar-link" href="notes/prob-01.qmd">Chapter notes</a></li>
</ul>
</div>
</nav>
"""


class SidebarShareTests(unittest.TestCase):
    def test_prune_drops_articles_and_empty_buckets(self):
        bounds = sidebar_share.sidebar_list(SAMPLE)
        self.assertIsNotNone(bounds)
        _ul, start, end = bounds
        inner = SAMPLE[start:end]
        pruned = sidebar_share.prune_menu(sidebar_share.strip_active(inner))
        self.assertNotIn("articles/", pruned)
        self.assertIn("notes/fundamentals.qmd", pruned)
        self.assertNotIn("Chapter notes", pruned)
        self.assertNotIn("notes/prob-01.qmd", pruned)
        self.assertNotIn("Kurtosis", pruned)
        self.assertNotIn("D–R", pruned)
        self.assertNotIn("active", pruned)

    def test_bucket_crumbs_keep_the_current_page(self):
        html = """
        <nav aria-label="breadcrumb"><ol>
        <li class="breadcrumb-item"><a href="topics.html">Topics</a></li>
        <li class="breadcrumb-item">Further reading</li>
        <li class="breadcrumb-item">D–R</li>
        <li class="breadcrumb-item"><a href="kurtosis.html">Kurtosis</a></li>
        <li class="breadcrumb-item active" aria-current="page">K</li>
        </ol></nav>
        """
        cleaned = sidebar_share.strip_bucket_crumbs(html)
        self.assertNotIn("Further reading", cleaned)
        self.assertNotIn("D–R", cleaned)
        self.assertIn("Kurtosis", cleaned)
        self.assertIn(">K<", cleaned)

    def test_page_keys_and_relative_links(self):
        site = sidebar_share.SITE_DIR
        self.assertEqual(sidebar_share.page_key(site / "index.html"), "")
        self.assertEqual(sidebar_share.href_key("./index.html"), "")
        self.assertEqual(sidebar_share.href_key("notes/fundamentals.qmd#x"), "notes/fundamentals.qmd")
        page = site / "articles" / "mean.html"
        rewritten = sidebar_share.rewrite_hrefs(
            '<a href="notes/fundamentals.qmd">Overview</a>', page
        )
        self.assertIn('href="../notes/fundamentals.qmd"', rewritten)

    def test_loader_goes_before_the_inline_script(self):
        page = sidebar_share.SITE_DIR / "articles" / "mean.html"
        html = "<script>\nfunction sidebarRoot() { return null; }\n</script>"
        updated = sidebar_share.insert_loader(html, page)
        self.assertLess(updated.find("sidebar-nav.js"), updated.find("function sidebarRoot"))
        self.assertIn('src="../sidebar-nav.js"', updated)
        self.assertEqual(sidebar_share.insert_loader(updated, page), updated)

    def test_production_inline_gets_one_loader_at_each_depth(self):
        html = "<!doctype html><html><body>" + build_wiki.SIDEBAR_JS + "</body></html>"
        self.assertIn('new URL(offset + "sidebar-nav.js", location.href)', html)
        self.assertEqual(_script_sources(html), [])
        for name, src in (
            ("index.html", "sidebar-nav.js"),
            ("articles/beta-distribution.html", "../sidebar-nav.js"),
            ("notes/advanced/index.html", "../../sidebar-nav.js"),
        ):
            with self.subTest(page=name):
                page = sidebar_share.SITE_DIR / name
                updated = sidebar_share.insert_loader(html, page)
                self.assertEqual(_script_sources(updated), [src])
                loader = sidebar_share.script_tag(page)
                self.assertLess(updated.index(loader), updated.index(build_wiki.SIDEBAR_JS.strip()))
                self.assertEqual(updated.replace(loader, "", 1), html)
                self.assertEqual(sidebar_share.insert_loader(updated, page), updated)

    def test_inline_strings_comments_and_data_attributes_are_not_loaders(self):
        html = (
            '<!-- <script src="sidebar-nav.js"></script> -->\n'
            '<script>const example = \'<script src="sidebar-nav.js">\';</script>\n'
            '<script data-src="sidebar-nav.js"></script>\n'
            + build_wiki.SIDEBAR_JS
        )
        page = sidebar_share.SITE_DIR / "index.html"
        updated = sidebar_share.insert_loader(html, page)
        self.assertEqual(_script_sources(updated), ["sidebar-nav.js"])
        self.assertEqual(updated.replace(sidebar_share.script_tag(page), "", 1), html)

    def test_existing_external_loader_is_not_duplicated(self):
        for tag in (
            '<script src="sidebar-nav.js"></script>',
            "<script defer src='../sidebar-nav.js?version=1#cache'></script>",
            '<SCRIPT SRC=/sidebar-nav.js></SCRIPT>',
        ):
            with self.subTest(tag=tag):
                html = tag + build_wiki.SIDEBAR_JS
                page = sidebar_share.SITE_DIR / "articles" / "beta-distribution.html"
                self.assertEqual(sidebar_share.insert_loader(html, page), html)


FULL_MENU = """<!DOCTYPE html><html><body>
<nav id="quarto-sidebar"><div class="sidebar-menu-container">
<ul class="list-unstyled mt-1">
<li class="sidebar-item sidebar-item-section">
<div class="sidebar-item-container">
<a class="sidebar-item-text sidebar-link text-start{collapsed}" data-bs-toggle="collapse" data-bs-target="#quarto-sidebar-section-1" aria-expanded="{expanded}"><span class="menu-text">Probability distributions</span></a>
</div>
<ul id="quarto-sidebar-section-1" class="collapse list-unstyled sidebar-section depth1{show}">
<li class="sidebar-item"><div class="sidebar-item-container">
<a href="{notes}" class="sidebar-item-text sidebar-link"><span class="menu-text">Overview</span></a>
</div></li>
<li class="sidebar-item"><div class="sidebar-item-container">
<a href="{article}" class="sidebar-item-text sidebar-link"><span class="menu-text">Beta distribution</span></a>
</div></li>
</ul></li>
<li class="sidebar-item sidebar-item-section">
<div class="sidebar-item-container">
<a class="sidebar-item-text sidebar-link text-start collapsed" data-bs-toggle="collapse" data-bs-target="#quarto-sidebar-section-2" aria-expanded="false"><span class="menu-text">Applications</span></a>
</div>
<ul id="quarto-sidebar-section-2" class="collapse list-unstyled sidebar-section depth1">
<li class="sidebar-item"><div class="sidebar-item-container">
<a href="{apps}" class="sidebar-item-text sidebar-link"><span class="menu-text">Overview</span></a>
</div></li>
</ul></li>
</ul></div></nav>
<script>
function sidebarRoot() {{ return null; }}
</script>
</body></html>
"""


def _menu(open_section: bool, *, nested: bool) -> str:
    prefix = "../" if nested else ""
    return FULL_MENU.format(
        collapsed="" if open_section else " collapsed",
        expanded="true" if open_section else "false",
        show=" show" if open_section else "",
        notes=f"{prefix}notes/probability-distributions.qmd",
        article=f"{prefix}articles/beta-distribution.qmd",
        apps=f"{prefix}notes/applications.qmd",
    )


class SidebarSecondPassTests(unittest.TestCase):
    def test_production_inline_survives_root_and_nested_postprocess_reruns(self):
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            (site / "articles").mkdir()
            pages = (site / "index.html", site / "articles" / "beta-distribution.html")
            stub = "<script>\nfunction sidebarRoot() { return null; }\n</script>"
            for page, nested in zip(pages, (False, True)):
                html = _menu(nested, nested=nested).replace(".qmd", ".html")
                self.assertIn(stub, html)
                html = html.replace(stub, build_wiki.SIDEBAR_JS)
                self.assertEqual(_script_sources(html), [])
                page.write_text(html, encoding="utf-8")
            previous = sidebar_share.SITE_DIR
            sidebar_share.SITE_DIR = site
            try:
                snapshots = None
                for _ in range(3):
                    sidebar_share.main()
                    current = [page.read_text(encoding="utf-8") for page in pages]
                    for html, src in zip(current, ("sidebar-nav.js", "../sidebar-nav.js")):
                        self.assertEqual(_script_sources(html), [src])
                        self.assertIn(build_wiki.SIDEBAR_JS, html)
                    self.assertIn(
                        '<ul id="quarto-sidebar-section-1" class="collapse list-unstyled sidebar-section depth1 show">',
                        current[1],
                    )
                    self.assertIn('href="../notes/probability-distributions.html"', current[1])
                    if snapshots is not None:
                        self.assertEqual(current, snapshots)
                    snapshots = current
            finally:
                sidebar_share.SITE_DIR = previous

    def test_two_passes_keep_the_menu_and_the_open_section(self):
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            (site / "articles").mkdir()
            (site / "index.html").write_text(_menu(False, nested=False), encoding="utf-8")
            article = site / "articles" / "beta-distribution.html"
            article.write_text(_menu(True, nested=True), encoding="utf-8")
            previous = sidebar_share.SITE_DIR
            sidebar_share.SITE_DIR = site
            try:
                sidebar_share.main()
                stored = (site / "sidebar-nav.js").read_text(encoding="utf-8")
                self.assertIn("articles/beta-distribution.qmd", stored)
                first_index = (site / "index.html").read_text(encoding="utf-8")
                first_article = article.read_text(encoding="utf-8")
                self.assertNotIn("articles/", first_index)
                self.assertNotIn("articles/", first_article)
                self.assertIn("Overview", first_article)
                self.assertIn('id="quarto-sidebar-section-1"', first_article)
                self.assertIn("show", first_article)
                self.assertIn('aria-expanded="true"', first_article)
                self.assertNotIn("show", first_index.split("quarto-sidebar-section-1", 1)[1][:180])

                # A single-file render puts the full menu back on one article only.
                article.write_text(_menu(True, nested=True), encoding="utf-8")
                sidebar_share.main()
                second_article = article.read_text(encoding="utf-8")
                second_index = (site / "index.html").read_text(encoding="utf-8")
                self.assertNotIn("articles/", second_article)
                self.assertIn("notes/probability-distributions.qmd", second_article)
                self.assertIn("show", second_article)
                self.assertIn('aria-expanded="true"', second_article)
                self.assertEqual(second_index, first_index)
                sidebar_share.main()
                self.assertEqual(article.read_text(encoding="utf-8"), second_article)
                self.assertEqual((site / "index.html").read_text(encoding="utf-8"), second_index)
                self.assertIn("articles/", (site / "sidebar-nav.js").read_text(encoding="utf-8"))
            finally:
                sidebar_share.SITE_DIR = previous

    def test_a_rerendered_article_supplies_the_menu_if_the_store_is_gone(self):
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            (site / "articles").mkdir()
            (site / "index.html").write_text(_menu(False, nested=False), encoding="utf-8")
            article = site / "articles" / "beta-distribution.html"
            article.write_text(_menu(True, nested=True), encoding="utf-8")
            previous = sidebar_share.SITE_DIR
            sidebar_share.SITE_DIR = site
            try:
                sidebar_share.main()
                (site / "sidebar-nav.js").unlink()
                article.write_text(_menu(True, nested=True), encoding="utf-8")
                sidebar_share.main()
                text = article.read_text(encoding="utf-8")
                self.assertNotIn("articles/", text)
                self.assertIn("../notes/probability-distributions.qmd", text)
                self.assertIn("show", text)
                self.assertIn("articles/", (site / "sidebar-nav.js").read_text(encoding="utf-8"))
            finally:
                sidebar_share.SITE_DIR = previous


if __name__ == "__main__":
    unittest.main()
