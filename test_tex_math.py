"""Delimiter conversion and the build guard that rejects \\( and \\[."""

import unittest

import build_wiki
import tex_math


class TexDelimiterTests(unittest.TestCase):
    def test_inline_and_display(self) -> None:
        source = "See \\(E[X]\\) and\n\\[\nE[X^k]=k!.\n\\]\n"
        converted = tex_math.convert_tex_delimiters(source)
        self.assertIn("$E[X]$", converted)
        self.assertIn("\n$$\nE[X^k]=k!.\n$$\n", converted)
        self.assertEqual(tex_math.tex_delimiter_offenders(converted), [])

    def test_strips_edge_spaces_and_protects_a_following_digit(self) -> None:
        self.assertEqual(tex_math.convert_tex_delimiters("\\( t \\)"), "$t$")
        self.assertEqual(tex_math.convert_tex_delimiters("\\(n\\)2"), "$n$ 2")

    def test_code_spans_fences_escaped_backslash_and_existing_dollars(self) -> None:
        source = "\n".join(
            [
                "A `\\(x\\)` stays.",
                "```",
                "\\(y\\)",
                "```",
                "Escaped \\\\(z\\\\) stays.",
                "Already $a\\(b\\)c$ stays.",
                "",
            ]
        )
        converted = tex_math.convert_tex_delimiters(source)
        self.assertIn("`\\(x\\)`", converted)
        self.assertIn("\\(y\\)", converted)
        self.assertIn("\\\\(z\\\\)", converted)
        self.assertIn("$a\\(b\\)c$", converted)
        self.assertEqual(tex_math.tex_delimiter_offenders(converted), [])
        self.assertEqual(tex_math.tex_delimiter_offenders("\\\\[4pt]"), [])

    def test_nested_brackets_are_not_delimiters(self) -> None:
        converted = tex_math.convert_tex_delimiters("\\(\\mathbb E[X^k]\\)")
        self.assertEqual(converted, "$\\mathbb E[X^k]$")
        self.assertEqual(tex_math.tex_delimiter_offenders(converted), [])

    def test_guard_rejects_a_leftover_delimiter(self) -> None:
        self.assertTrue(tex_math.tex_delimiter_offenders("see \\(x\\)"))
        with self.assertRaises(SystemExit):
            build_wiki.assert_no_tex_delimiters_in_text("see \\(x\\)", "sample.md")
        build_wiki.assert_no_tex_delimiters_in_text("see $x$", "sample.md")


if __name__ == "__main__":
    unittest.main()
