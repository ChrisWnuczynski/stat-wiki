"""The Chromium maths check fails on errors and on raw TeX, and accepts MathML."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.rendered_math_check import check_pages

ROOT = Path(__file__).resolve().parent
# The kernel-density laboratory writes this expectation. KaTeX paints a literal
# red \\E when the command is undefined, still with a .katex wrapper and MathML
# and with no .katex-error element.
MISE = (
    r"\mathrm{MISE}(h)=\mathrm{IVar}(h)+\mathrm{IBias}^2(h)="
    r"\E\int_{-\infty}^{\infty}\bigl(\widehat f_h(x)-f(x)\bigr)^2\,\mathrm{d}x."
)


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

    def test_visible_raw_command_fails_and_colour_and_tex_source_do_not(self) -> None:
        script = r"""
import { createRequire } from "node:module";
import { writeFileSync } from "node:fs";
const require = createRequire(import.meta.url);
const katex = require(process.argv[1]);
const tex = process.argv[2];
const out = process.argv[3];
const bad = katex.renderToString(tex, { throwOnError: false, output: "htmlAndMathml", strict: "ignore" });
const good = katex.renderToString(tex, {
  throwOnError: true, output: "htmlAndMathml", strict: "ignore",
  macros: { "\\E": "\\mathbb{E}" },
});
const red = katex.renderToString("\\textcolor{red}{x+y}", { throwOnError: true, output: "htmlAndMathml" });
const page = (body) => "<!DOCTYPE html><html><body><span class=\"math inline\">" + body + "</span></body></html>";
writeFileSync(out + "/bad-e.html", page(bad));
writeFileSync(out + "/good-e.html", page(good));
writeFileSync(out + "/red.html", page(red));
if (bad.includes("katex-error")) throw new Error("the gap is a raw command with no katex-error");
"""
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            subprocess.run(
                ["node", "--input-type=module", "-e", script, str(ROOT / "katex" / "katex.min.js"), MISE, str(site)],
                check=True,
                cwd=ROOT,
            )
            bad = check_pages(site, ["bad-e.html"])
            self.assertTrue(any(r"\E" in item and "raw command" in item for item in bad), bad)
            self.assertFalse(any("katex-error" in item for item in bad), bad)
            self.assertEqual(check_pages(site, ["good-e.html"]), [])
            self.assertEqual(check_pages(site, ["red.html"]), [])
            good = (site / "good-e.html").read_text(encoding="utf-8")
            self.assertIn('encoding="application/x-tex"', good)
            self.assertIn(r"\E", good)


if __name__ == "__main__":
    unittest.main()
