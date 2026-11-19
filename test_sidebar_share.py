"""Unit checks for the shared sidebar and the breadcrumb cleanup."""

import unittest
from pathlib import Path

import sidebar_share


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


if __name__ == "__main__":
    unittest.main()
