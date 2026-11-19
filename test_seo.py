"""Sitemap, article structured data, figure-page titles, and redirect stubs."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from urllib.parse import urlsplit

import build_wiki
import canonical_redirects
import search_meta
import share_preview

ROOT = Path(__file__).resolve().parent

SITE = search_meta.SITE

SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.statwiki.io/index.html</loc>
    <lastmod>2026-11-19T08:11:00Z</lastmod>
  </url>
  <url>
    <loc>https://www.statwiki.io/reference/index.html</loc>
    <lastmod>2026-11-19T08:11:00Z</lastmod>
  </url>
  <url>
    <loc>https://www.statwiki.io/questions/index.html</loc>
    <lastmod>2026-11-19T08:11:00Z</lastmod>
  </url>
  <url>
    <loc>https://www.statwiki.io/notes/index.html</loc>
    <lastmod>2026-11-19T08:11:00Z</lastmod>
  </url>
  <url>
    <loc>https://www.statwiki.io/labs/index.html</loc>
    <lastmod>2026-11-19T08:11:00Z</lastmod>
  </url>
  <url>
    <loc>https://www.statwiki.io/files/index.html</loc>
    <lastmod>2026-11-19T08:11:00Z</lastmod>
  </url>
  <url>
    <loc>https://www.statwiki.io/search.html</loc>
    <lastmod>2026-11-19T08:11:00Z</lastmod>
  </url>
  <url>
    <loc>https://www.statwiki.io/questions/random.html</loc>
    <lastmod>2026-11-19T08:11:00Z</lastmod>
  </url>
  <url>
    <loc>https://www.statwiki.io/articles/variance.html</loc>
    <lastmod>2026-11-19T08:11:00Z</lastmod>
  </url>
  <url>
    <loc>https://www.statwiki.io/questions/q-01.html</loc>
    <lastmod>2026-11-19T08:11:00Z</lastmod>
  </url>
</urlset>
"""


def _page(title: str, description: str, canonical: str, body: str = "<p>A page.</p>") -> str:
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
</head><body><main>
{body}
</main></body></html>
"""


def _ld(text: str, script_id: str) -> dict:
    match = re.search(
        rf'<script type="application/ld\+json" id="{script_id}">\n(.*?)\n</script>',
        text,
        re.S,
    )
    if not match:
        raise AssertionError(f"missing {script_id}")
    return json.loads(match.group(1))


class SitemapTests(unittest.TestCase):
    def test_canonical_indexes_utility_pages_and_no_lastmod(self) -> None:
        text = search_meta.fix_sitemap_text(SITEMAP)
        locs = re.findall(r"<loc>([^<]*)</loc>", text)
        self.assertEqual(
            locs[:6],
            [
                "https://www.statwiki.io/",
                "https://www.statwiki.io/reference/",
                "https://www.statwiki.io/questions/",
                "https://www.statwiki.io/notes/",
                "https://www.statwiki.io/labs/",
                "https://www.statwiki.io/files/",
            ],
        )
        self.assertIn("https://www.statwiki.io/articles/variance.html", locs)
        self.assertIn("https://www.statwiki.io/questions/q-01.html", locs)
        self.assertNotIn("search.html", text)
        self.assertNotIn("random.html", text)
        self.assertNotIn("index.html", text)
        self.assertNotIn("lastmod", text)
        self.assertNotIn("<lastmod>", text)
        for loc in locs:
            self.assertFalse(search_meta.is_index_html_url(loc), loc)

    def test_canonical_and_og_url_use_the_directory_form(self) -> None:
        page = """
<link rel="canonical" href="https://www.statwiki.io/index.html">
<link href="https://www.statwiki.io/reference/index.html" rel="canonical">
<meta property="og:url" content="https://www.statwiki.io/notes/index.html">
<meta content="https://www.statwiki.io/labs/index.html" property="og:url">
<link rel="canonical" href="https://www.statwiki.io/files/index.html">
<link rel="canonical" href="https://www.statwiki.io/questions/index.html">
<link rel="canonical" href="https://www.statwiki.io/articles/variance.html">
<link rel="canonical" href="https://www.statwiki.io/articles/gini-index.html">
<a href="https://www.statwiki.io/notes/index.html">Topics</a>
"""
        updated = search_meta.rewrite_directory_urls(page)
        canonicals = re.findall(r'rel="canonical" href="([^"]+)"', updated)
        canonicals += re.findall(r'href="([^"]+)" rel="canonical"', updated)
        og_urls = re.findall(r'property="og:url" content="([^"]+)"', updated)
        og_urls += re.findall(r'content="([^"]+)" property="og:url"', updated)
        self.assertEqual(
            set(canonicals),
            {
                "https://www.statwiki.io/",
                "https://www.statwiki.io/reference/",
                "https://www.statwiki.io/files/",
                "https://www.statwiki.io/questions/",
                "https://www.statwiki.io/articles/variance.html",
                "https://www.statwiki.io/articles/gini-index.html",
            },
        )
        self.assertEqual(
            og_urls,
            [
                "https://www.statwiki.io/notes/",
                "https://www.statwiki.io/labs/",
            ],
        )
        for url in canonicals + og_urls:
            self.assertFalse(search_meta.is_index_html_url(url), url)
        self.assertIn('<a href="https://www.statwiki.io/notes/index.html">Topics</a>', updated)
        self.assertEqual(
            share_preview.public_url(
                share_preview.SITE_DIR / "notes" / "index.html",
                "https://www.statwiki.io/notes/index.html",
            ),
            "https://www.statwiki.io/notes/",
        )
        self.assertEqual(
            share_preview.public_url(share_preview.SITE_DIR / "index.html", "https://www.statwiki.io/index.html"),
            "https://www.statwiki.io/",
        )

    def test_redirect_stubs_are_left_out_of_the_sitemap(self) -> None:
        stubs = sorted((ROOT / "articles").glob("*.html"))
        self.assertGreater(len(stubs), 100, "build_wiki.py has not written the redirect stubs")
        listed = "\n".join(
            "  <url><loc>https://www.statwiki.io/articles/"
            f"{path.name}</loc><lastmod>2026-11-19T08:11:00Z</lastmod></url>"
            for path in stubs
        )
        text = search_meta.fix_sitemap_text(
            SITEMAP.replace("</urlset>", listed + "\n</urlset>\n"),
            {f"https://www.statwiki.io/articles/{path.name}" for path in stubs},
        )
        for path in stubs:
            self.assertNotIn(f"articles/{path.name}", text)
        self.assertIn("https://www.statwiki.io/articles/variance.html", text)
        for loc in re.findall(r"<loc>([^<]*)</loc>", text):
            self.assertFalse(search_meta.is_index_html_url(loc), loc)


class StructuredDataTests(unittest.TestCase):
    def test_home_keeps_one_website_block(self) -> None:
        page = _page("StatWiki", "A statistics study wiki.", SITE)
        updated = search_meta.home_page(page)
        self.assertEqual(updated.count('type="application/ld+json"'), 1)
        self.assertIn('id="website-data"', updated)
        self.assertNotIn('id="article-data"', updated)
        data = _ld(updated, "website-data")
        self.assertEqual(data["@type"], "WebSite")
        self.assertNotIn("@graph", data)
        self.assertNotIn("Article", json.dumps(data))
        again = search_meta.home_page(updated)
        self.assertEqual(again.count('type="application/ld+json"'), 1)

    def test_article_json_ld_and_topic_breadcrumb(self) -> None:
        body = (
            '<div class="wiki-categories" role="navigation" aria-label="Categories">\n'
            '    <span class="cat-label">Categories:</span> '
            '<a href="../notes/index.html#statistical-inference">Statistical inference</a>'
            " · "
            '<a href="../notes/inf-02-estimation.html">Estimation</a>\n'
            "</div>\n"
            "<p>Maximum likelihood picks the parameter that makes the sample most probable.</p>"
        )
        page = _page(
            "Maximum likelihood – StatWiki",
            "Maximum likelihood picks the parameter that makes the sample most probable.",
            f"{SITE}articles/maximum-likelihood.html",
            body,
        )
        description = "Maximum likelihood picks the parameter that makes the sample most probable."
        updated = search_meta.with_article_data(page, "articles/maximum-likelihood.html", description)
        self.assertEqual(updated.count('type="application/ld+json"'), 1)
        self.assertNotIn('id="website-data"', updated)
        data = _ld(updated, "article-data")
        self.assertEqual([node["@type"] for node in data["@graph"]], ["Article", "BreadcrumbList"])
        article = data["@graph"][0]
        self.assertEqual(article["headline"], "Maximum likelihood")
        self.assertEqual(article["description"], description)
        self.assertEqual(article["url"], f"{SITE}articles/maximum-likelihood.html")
        self.assertEqual(article["inLanguage"], "en")
        self.assertEqual(article["isPartOf"], {"@type": "WebSite", "name": "StatWiki", "url": SITE})
        crumbs = data["@graph"][1]["itemListElement"]
        self.assertEqual([c["name"] for c in crumbs], ["Home", "Statistical inference", "Maximum likelihood"])
        self.assertEqual(crumbs[0]["item"], SITE)
        self.assertEqual(crumbs[1]["item"], f"{SITE}notes/#statistical-inference")
        self.assertEqual(crumbs[2]["item"], f"{SITE}articles/maximum-likelihood.html")
        self.assertEqual([c["position"] for c in crumbs], [1, 2, 3])
        again = search_meta.with_article_data(updated, "articles/maximum-likelihood.html", description)
        self.assertEqual(again.count('type="application/ld+json"'), 1)

    def test_known_hub_is_used_and_an_unknown_topic_has_no_breadcrumb(self) -> None:
        variance = search_meta.with_article_data(
            _page("Variance – StatWiki", "Variance measures spread.", f"{SITE}articles/variance.html"),
            "articles/variance.html",
            "Variance measures spread.",
        )
        data = _ld(variance, "article-data")
        crumbs = data["@graph"][1]["itemListElement"]
        self.assertEqual(crumbs[1]["name"], "Fundamentals")
        self.assertEqual(crumbs[1]["item"], f"{SITE}notes/fundamentals.html")

        normal = search_meta.with_article_data(
            _page(
                "Normal distribution – StatWiki",
                "The normal distribution is a symmetric bell curve.",
                f"{SITE}articles/normal-distribution.html",
            ),
            "articles/normal-distribution.html",
            "The normal distribution is a symmetric bell curve.",
        )
        normal_data = _ld(normal, "article-data")
        self.assertEqual(normal_data["@graph"][1]["itemListElement"][1]["name"], "Probability distributions")

        plain = search_meta.with_article_data(
            _page("Made up – StatWiki", "A page with no topic hub on the site.", f"{SITE}articles/made-up-page.html"),
            "articles/made-up-page.html",
            "A page with no topic hub on the site.",
        )
        made = _ld(plain, "article-data")
        self.assertEqual(made["@type"], "Article")
        self.assertNotIn("@graph", made)
        self.assertNotIn("BreadcrumbList", json.dumps(made))
        self.assertNotEqual(made["@type"], "WebSite")

    def test_og_type_is_website_or_article_and_questions_are_left_alone(self) -> None:
        self.assertEqual(share_preview.og_type_for("index.html"), "website")
        self.assertEqual(share_preview.og_type_for("articles/variance.html"), "article")
        self.assertIsNone(share_preview.og_type_for("questions/q-01.html"))
        self.assertIsNone(share_preview.og_type_for("notes/inf-02-estimation.html"))
        home = share_preview.add_og_type(
            '<link rel="canonical" href="https://www.statwiki.io/">',
            "website",
        )
        self.assertIn('<meta property="og:type" content="website">', home)
        article = share_preview.add_og_type(
            '<link rel="canonical" href="https://www.statwiki.io/articles/variance.html">\n'
            '<meta property="og:url" content="https://www.statwiki.io/articles/variance.html">',
            "article",
        )
        self.assertIn('<meta property="og:type" content="article">', article)
        self.assertEqual(article.count("og:type"), 1)


class RedirectStubTests(unittest.TestCase):
    def test_every_stub_has_a_canonical_refresh_and_visible_link(self) -> None:
        stubs = sorted((ROOT / "articles").glob("*.html"))
        self.assertGreater(len(stubs), 100, "build_wiki.py has not written the redirect stubs")
        for path in stubs:
            text = path.read_text(encoding="utf-8")
            self.assertTrue(search_meta.is_redirect_stub(text), path.name)
            self.assertNotIn("noindex", text.lower(), path.name)
            refresh = re.search(r'<meta http-equiv="refresh" content="0; url=([^"]+)">', text)
            link = re.search(r'<a href="([^"]+)">', text)
            canon = re.search(r'<link rel="canonical" href="([^"]+)">', text)
            self.assertIsNotNone(refresh, path.name)
            self.assertIsNotNone(link, path.name)
            self.assertIsNotNone(canon, path.name)
            self.assertEqual(link.group(1), refresh.group(1), path.name)
            href = canon.group(1)
            self.assertTrue(href.startswith("https://www.statwiki.io/"), path.name)
            self.assertFalse(search_meta.is_index_html_url(href), href)
            self.assertEqual(urlsplit(href).fragment, "", path.name)
            expected = canonical_redirects.absolute_redirect_url(path, refresh.group(1), site_dir=ROOT)
            self.assertEqual(href, expected, path.name)
            own = "https://www.statwiki.io/" + path.relative_to(ROOT).as_posix()
            self.assertNotEqual(href, own, path.name)


class RobotsTests(unittest.TestCase):
    def test_figure_sources_are_disallowed(self) -> None:
        text = (ROOT / "robots.txt").read_text(encoding="utf-8")
        self.assertIn("User-agent: *\n", text)
        self.assertIn("Allow: /\n", text)
        self.assertIn("Disallow: /figures/*.tex\n", text)
        self.assertIn("Disallow: /figures/*.pdf\n", text)
        self.assertIn("Sitemap: https://www.statwiki.io/sitemap.xml\n", text)


class FigureTitleTests(unittest.TestCase):
    def test_caption_becomes_a_plain_title_and_empty_caption_keeps_the_file_name(self) -> None:
        sleep = (
            "Reaction time for the eighteen subjects. The black line is the population fit, "
            "about 251 milliseconds plus 10.5 milliseconds a day."
        )
        self.assertEqual(
            build_wiki.figure_page_title(sleep, "sleep.png"),
            "Figure: Reaction time for the eighteen subjects",
        )
        maths = (
            r"Forty samples of size 10 from $\Normal(10,1)$, each with its 95% $t$ interval for $\mu$. "
            r"Thirty-eight cover $\mu=10$."
        )
        title = build_wiki.figure_page_title(maths, "inf-coverage.png")
        self.assertTrue(title.startswith("Figure: "))
        self.assertNotIn("$", title)
        self.assertNotIn("\\", title)
        self.assertNotIn("File:", title)
        self.assertLessEqual(len(title), 90)
        linked = "See the [normal density](../articles/normal-distribution.qmd) in this picture of $\\sigma$."
        linked_title = build_wiki.figure_page_title(linked, "sigma.png")
        self.assertIn("normal density", linked_title)
        self.assertNotIn("](", linked_title)
        self.assertNotIn("$", linked_title)
        self.assertNotIn("\\", linked_title)
        penalty = (
            r"The roughness penalty $\lambda\int\{g''(x)\}^2\,\mathrm{d}x$ in Gaussian squared-error fitting. "
            r"With distinct observed $x$ values, a vanishing penalty approaches the interpolating cubic spline."
        )
        penalty_title = build_wiki.figure_page_title(penalty, "06-smooth-means-roughness-penalty.png")
        self.assertEqual(
            penalty_title,
            "Figure: The roughness penalty λ∫g″(x)² dx in Gaussian squared-error fitting",
        )
        self.assertNotIn("$", penalty_title)
        self.assertNotIn("\\", penalty_title)
        densities = (
            r"Densities of $(\overline X-\mu_0)/(\sigma/\sqrt n)$ under $H_0$ and under an alternative "
            r"$1.8$ standard errors above $\mu_0$."
        )
        densities_title = build_wiki.figure_page_title(densities, "inf-np-region.png")
        self.assertEqual(
            densities_title,
            "Figure: Densities of (X\u0304-μ₀)/(σ/√n) under H₀ and under an alternative 1.8 standard errors above μ₀",
        )
        priors = (
            r"The three priors, then the posteriors they produce after $3$ heads in $10$ tosses "
            r"and after $30$ heads in $100$. Both datasets have the same observed proportion."
        )
        priors_title = build_wiki.figure_page_title(priors, "part1-fig-02-prior-sensitivity.png")
        self.assertFalse(priors_title.endswith(" in"))
        self.assertIn("30 heads", priors_title)
        self.assertEqual(build_wiki.figure_page_title("", "sleep.png"), "File:sleep.png")
        self.assertEqual(build_wiki.figure_page_title("   ", "sleep.png"), "File:sleep.png")


if __name__ == "__main__":
    unittest.main()
