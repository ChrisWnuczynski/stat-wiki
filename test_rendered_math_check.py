"""The Chromium maths check fails on errors and on raw TeX, and accepts MathML."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.rendered_math_check import check_pages


GOOD = """<!DOCTYPE html><html><body>
<span class="math inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></span></span></span>
</body></html>
"""

RAW = """<!DOCTYPE html><html><body>
<span class="math inline">\\mu</span>
</body></html>
"""

ERROR = """<!DOCTYPE html><html><body>
<span class="katex-error" title="ParseError">\\E</span>
</body></html>
"""

LABELLED = """<!DOCTYPE html><html><body>
<span class="math inline" aria-label="x squared"><span class="katex">x</span></span>
</body></html>
"""


class RenderedMathCheckTests(unittest.TestCase):
    def test_chromium_accepts_mathml_and_rejects_raw_tex_and_errors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            (site / "good.html").write_text(GOOD, encoding="utf-8")
            (site / "raw.html").write_text(RAW, encoding="utf-8")
            (site / "error.html").write_text(ERROR, encoding="utf-8")
            (site / "labelled.html").write_text(LABELLED, encoding="utf-8")
            self.assertEqual(check_pages(site, ["good.html"]), [])
            self.assertEqual(check_pages(site, ["labelled.html"]), [])
            raw = check_pages(site, ["raw.html"])
            self.assertTrue(any("untransformed" in item for item in raw), raw)
            broken = check_pages(site, ["error.html"])
            self.assertTrue(any("katex-error" in item for item in broken), broken)


if __name__ == "__main__":
    unittest.main()
