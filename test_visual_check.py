"""Void elements must not hide a raw delimiter after a skipped region."""

import unittest

from tools.visual_check import maths_hits

_FOLLOWING = "<p>See \\(x\\).</p>"


def _then_visible(inner: str) -> str:
    return f"{inner}{_FOLLOWING}"


class MathsHitsTests(unittest.TestCase):
    def test_bare_void_elements_inside_code_flag_the_following_delimiter(self) -> None:
        for tag in ("<br>", "<wbr>", '<img src="x">'):
            with self.subTest(tag=tag):
                html = _then_visible(f"<code>\\(hidden\\){tag}</code>")
                self.assertEqual(maths_hits(html), ["\\("])

    def test_self_closed_void_elements_inside_code_flag_the_following_delimiter(self) -> None:
        for tag in ("<br/>", "<wbr/>", '<img src="x"/>'):
            with self.subTest(tag=tag):
                html = _then_visible(f"<code>\\(hidden\\){tag}</code>")
                self.assertEqual(maths_hits(html), ["\\("])

    def test_paired_span_inside_code_flags_the_following_delimiter(self) -> None:
        html = _then_visible("<code>\\(hidden\\)<span>note</span></code>")
        self.assertEqual(maths_hits(html), ["\\("])

    def test_skip_region_with_no_void_child_flags_the_following_delimiter(self) -> None:
        html = _then_visible("<code>\\(hidden\\)</code>")
        self.assertEqual(maths_hits(html), ["\\("])

    def test_bare_void_tag_outside_a_skip_region_flags_the_following_delimiter(self) -> None:
        html = _then_visible("<p>Line<br>break</p>")
        self.assertEqual(maths_hits(html), ["\\("])

    def test_delimiters_only_inside_skipped_regions_are_ignored(self) -> None:
        samples = (
            "<code>\\(x\\)</code>",
            "<pre>\\(x\\)</pre>",
            '<span class="katex">\\(x\\)</span>',
            '<span class="math">\\(x\\)</span>',
            "<annotation>\\(x\\)</annotation>",
            "<script>\\(x\\)</script>",
            "<style>\\(x\\)</style>",
        )
        for html in samples:
            with self.subTest(html=html):
                self.assertEqual(maths_hits(html), [])

    def test_katex_class_does_not_hide_the_following_delimiter(self) -> None:
        html = _then_visible('<span class="katex">\\(hidden\\)</span>')
        self.assertEqual(maths_hits(html), ["\\("])

    def test_code_and_pre_do_not_hide_the_following_delimiter(self) -> None:
        html = _then_visible("<code>\\(hidden\\)</code><pre>\\(also\\)</pre>")
        self.assertEqual(maths_hits(html), ["\\("])

    def test_stray_end_br_inside_code_does_not_pop_the_parent(self) -> None:
        html = _then_visible("<code><br></br>\\(hidden\\)</code>")
        self.assertEqual(maths_hits(html), ["\\("])


if __name__ == "__main__":
    unittest.main()
