"""Question pages keep a heading order with no skips (STA-27).

A question page's worked answer sits in a callout whose first heading,
"## Worked answer", Quarto renders as the callout title, not as an <h2>. The
answer's sub-parts must therefore start at level 2 themselves, or the page
jumps from its <h1> title straight to <h3>.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

import build_wiki

ROOT = Path(__file__).resolve().parent
CALLOUT_OPEN = re.compile(r"^:{3,}\s*\{[^}]*\.callout")
HEADING = re.compile(r"^(#{1,6}) ")


def rendered_heading_levels(qmd: str) -> list[int]:
    """Heading levels as the rendered page shows them, starting with the h1 title.

    The first heading inside a callout is its title, so it is not counted.
    Lines inside fenced code are not headings.
    """
    levels = [1]
    in_fence = False
    callout_title_pending = False
    for line in qmd.split("\n"):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if CALLOUT_OPEN.match(line):
            callout_title_pending = True
            continue
        match = HEADING.match(line)
        if match:
            if callout_title_pending:
                callout_title_pending = False
                continue
            levels.append(len(match.group(1)))
        elif line.strip():
            callout_title_pending = False
    return levels


def skips(levels: list[int]) -> list[tuple[int, int]]:
    return [(a, b) for a, b in zip(levels, levels[1:]) if b > a + 1]


class LiftHeadingsTests(unittest.TestCase):
    def test_shallowest_heading_becomes_level_two_and_relative_depth_is_kept(self):
        text = "### (a) Likelihood\n\nText.\n\n### (e) Limits\n\n#### (i) As m grows.\n"
        self.assertEqual(
            build_wiki.lift_headings(text),
            "## (a) Likelihood\n\nText.\n\n## (e) Limits\n\n### (i) As m grows.\n",
        )

    def test_answers_already_at_level_two_or_without_headings_are_unchanged(self):
        for text in ("## Reasoning\n\nBecause.\n\n### Detail\n", "No headings, just $x$.\n", ""):
            with self.subTest(text=text):
                self.assertEqual(build_wiki.lift_headings(text), text)

    def test_code_is_not_a_heading(self):
        text = "### (a) Fit\n\n```r\n## a comment, not a heading\nx <- 1\n```\n\n### (b) Check\n"
        lifted = build_wiki.lift_headings(text)
        self.assertIn("## a comment, not a heading\n", lifted)
        self.assertTrue(lifted.startswith("## (a) Fit\n"))
        self.assertIn("\n## (b) Check\n", lifted)

    def test_the_callout_title_is_not_counted_as_a_heading(self):
        page = (
            "Question text.\n\n"
            ':::::::: {#worked-answer .callout-tip collapse="true"}\n## Worked answer\n\n'
            "### (a) Likelihood\n\n### (b) Posterior\n\n::::::::\n"
        )
        self.assertEqual(rendered_heading_levels(page), [1, 3, 3])
        self.assertEqual(skips(rendered_heading_levels(page)), [(1, 3)])


class GeneratedQuestionPageTests(unittest.TestCase):
    def test_no_question_page_skips_a_heading_level(self):
        pages = sorted((ROOT / "questions").glob("*.qmd"))
        if not pages:
            self.skipTest("Generated wiki directories are not built yet")
        bad = {}
        with_answers = 0
        for path in pages:
            text = path.read_text(encoding="utf-8")
            with_answers += "#worked-answer" in text
            levels = rendered_heading_levels(text)
            if skips(levels):
                bad[path.name] = levels
        self.assertGreater(with_answers, 0, "No question page has a worked answer")
        self.assertEqual(bad, {}, "Question pages that skip a heading level")

    def test_lettered_sub_parts_are_level_two_under_the_title(self):
        path = ROOT / "questions" / "q-12.qmd"
        if not path.is_file():
            self.skipTest("Generated wiki directories are not built yet")
        text = path.read_text(encoding="utf-8")
        for part in ("(a) Likelihood", "(b) Posterior distribution", "(c) Posterior mean and MAP estimate"):
            self.assertRegex(text, rf"(?m)^## {re.escape(part)} ")


if __name__ == "__main__":
    unittest.main()
