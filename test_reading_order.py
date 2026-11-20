"""Chapter reading order and one autolink pass across a split chapter."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

import build_wiki


class ChapterOpeningTests(unittest.TestCase):
    def test_a_heading_stays_under_the_infobox(self) -> None:
        prose = "## What is random?\n\nStatistical inference is not exhausted by two schools.\n"
        before, after = build_wiki.chapter_prose_around_infobox(prose)
        self.assertEqual(before, "")
        self.assertTrue(after.startswith("## What is random?"))

    def test_an_opening_paragraph_stays_before_the_infobox(self) -> None:
        prose = "A random variable is a numerical summary.\n\n## Random variables\n\nThe rest.\n"
        before, after = build_wiki.chapter_prose_around_infobox(prose)
        self.assertIn("A random variable is a numerical summary.", before)
        self.assertNotIn("## Random variables", before)
        self.assertTrue(after.startswith("## Random variables"))

    def test_a_leading_callout_stays_above_a_heading(self) -> None:
        prose = "::: {.callout}\nNote.\n:::\n\n## Heading\n\nParagraph.\n"
        before, after = build_wiki.chapter_prose_around_infobox(prose)
        self.assertIn(":::", before)
        self.assertNotIn("## Heading", before)
        self.assertTrue(after.startswith("## Heading"))


class SharedAutolinkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.saved = list(build_wiki._COMPILED)
        article = Path("articles/linear-predictor.qmd")
        section = Path("articles/three-components-of-a-glm.qmd")
        home = Path("notes/elsewhere.qmd")
        pattern = re.compile(r"(?<![\w–-])(?:linear predictors?)(?![\w–-])", re.I)
        build_wiki._COMPILED[:] = [
            (pattern, None, article, "", None, home, set()),
            (pattern, None, section, "", None, home, set()),
        ]
        self.page = Path("notes/01-introduction-to-glms.qmd")

    def tearDown(self) -> None:
        build_wiki._COMPILED[:] = self.saved

    def test_split_prose_links_each_term_once_and_keeps_the_second_target(self) -> None:
        opening = "A first model keeps a linear predictor in the opening.\n\n"
        remainder = "Later the linear predictor is the systematic part.\n"
        linked: set = set()
        first = build_wiki.autolink(opening, self.page, "Generalised linear models", linked)
        second = build_wiki.autolink(remainder, self.page, "Generalised linear models", linked)
        combined = first + second
        self.assertEqual(combined.count("articles/linear-predictor.qmd"), 1)
        self.assertIn("articles/three-components-of-a-glm.qmd", second)
        self.assertNotIn("articles/linear-predictor.qmd", second)
        # A fresh set on the second block would point that mention at the article.
        repeated = build_wiki.autolink(remainder, self.page, "Generalised linear models")
        self.assertIn("articles/linear-predictor.qmd", repeated)
