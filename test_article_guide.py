"""Article pages get the same study guide chapters already have."""

from __future__ import annotations

import unittest

import build_wiki


class ArticleGuideTests(unittest.TestCase):
    def setUp(self) -> None:
        self._articles = dict(build_wiki.ARTICLES)
        self._titles = dict(build_wiki.PAGE_TITLES)
        self._order = dict(build_wiki._CHAPTER_ORDER)

    def tearDown(self) -> None:
        build_wiki.ARTICLES.clear()
        build_wiki.ARTICLES.update(self._articles)
        build_wiki.PAGE_TITLES.clear()
        build_wiki.PAGE_TITLES.update(self._titles)
        build_wiki._CHAPTER_ORDER.clear()
        build_wiki._CHAPTER_ORDER.update(self._order)

    def test_guide_uses_the_chapter_level_needs_and_neighbors(self) -> None:
        chapter = build_wiki.WIKI / "notes" / "prob-02-random-variables.qmd"
        earlier = build_wiki.WIKI / "notes" / "prob-01-experiments.qmd"
        build_wiki.PAGE_TITLES[chapter] = "Random variables"
        build_wiki.PAGE_TITLES[earlier] = "Experiments"
        build_wiki.ARTICLES["earlier-page"] = {
            "slug": "earlier-page",
            "term": "Earlier page",
            "path": build_wiki.WIKI / "articles" / "earlier-page.qmd",
            "box": {"chapter": chapter, "anchor": "aaa-not-in-the-chapter"},
        }
        build_wiki.ARTICLES["later-page"] = {
            "slug": "later-page",
            "term": "Later page",
            "path": build_wiki.WIKI / "articles" / "later-page.qmd",
            "box": {"chapter": chapter, "anchor": "zzz-not-in-the-chapter"},
        }
        guide = build_wiki.article_study_guide(build_wiki.ARTICLES["later-page"])
        self.assertIn("[Beginner]{.level}", guide)
        self.assertIn("**What you need first.**", guide)
        self.assertIn("Experiments", guide)
        self.assertIn("This page sits in [Random variables]", guide)
        self.assertIn("[‹ Earlier page](earlier-page.qmd){.qnav}", guide)
        self.assertNotIn("›", guide)

    def test_fundamentals_path_uses_the_previous_page(self) -> None:
        first, second = build_wiki.topic_hubs.FUNDAMENTALS_ORDER[:2]
        for slug in (first, second):
            build_wiki.ARTICLES[slug] = {
                "slug": slug,
                "term": slug.replace("-", " ").title(),
                "path": build_wiki.WIKI / "articles" / f"{slug}.qmd",
                "standalone": "Fundamentals",
            }
        guide = build_wiki.article_study_guide(build_wiki.ARTICLES[second])
        self.assertIn("[Beginner]{.level}", guide)
        self.assertIn(build_wiki.ARTICLES[first]["term"], guide)
        self.assertIn("Fundamentals", guide)
        self.assertIn("{.qnav}", guide)


if __name__ == "__main__":
    unittest.main()
