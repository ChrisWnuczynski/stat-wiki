"""Build-time KaTeX leaves MathML in the page and does not need the client script."""

from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import build_wiki


ROOT = Path(__file__).resolve().parent

PAGE = """<!DOCTYPE html><html><head>
<script defer="" src="./katex/katex.min.js"></script>
<script>document.addEventListener("DOMContentLoaded", function () {
 var mathElements = document.getElementsByClassName("math");
 var macros = [];
 for (var i = 0; i < mathElements.length; i++) {
  var texText = mathElements[i].firstChild;
  if (mathElements[i].tagName == "SPAN") {
   katex.render(texText.data, mathElements[i], {
    displayMode: mathElements[i].classList.contains('display'),
    throwOnError: false,
    macros: macros,
    fleqn: false
   });
}}});
  </script>
<link rel="stylesheet" href="./katex/katex.min.css">
<script>
const typesetMath = (el) => {
  if (window.MathJax) {
    window.MathJax.typeset([el]);
  } else if (window.katex) {
    var mathElements = el.getElementsByClassName("math");
    var macros = [];
    for (var i = 0; i < mathElements.length; i++) {
      var texText = mathElements[i].firstChild;
      if (mathElements[i].tagName == "SPAN") {
        window.katex.render(texText.data, mathElements[i], {
          displayMode: mathElements[i].classList.contains('display'),
          throwOnError: false,
          macros: macros,
          fleqn: false
        });
      }
    }
  }
}
window.Quarto = { typesetMath };
</script>
</head><body>
<p>Inline <span class="math inline">a&lt;b</span> and <span class="math display">\\E[X]</span></p>
<span class="math-example">not a formula</span>
<span data-class="math">data class only</span>
<!-- <span class="math">comment formula</span> -->
<script>
var example = '<span class="math">script formula</span>';
function ensureKatex() {}
function renderMath(root) {
  root.querySelectorAll("span.math").forEach(function (el) {
    window.katex.render("x", el, { throwOnError: false });
  });
}
</script>
</body></html>
"""


class PrerenderMathTests(unittest.TestCase):
    def test_shared_macros_reach_the_hover_preview(self) -> None:
        definitions = build_wiki.katex_macro_definitions()
        on_disk = json.loads((ROOT / "katex_macros.json").read_text(encoding="utf-8"))
        preview = json.loads(build_wiki.katex_macros_literal())
        self.assertEqual(on_disk, definitions)
        self.assertEqual(preview, definitions)
        reader = (ROOT / "ask" / "widget" / "src" / "browser.ts").read_text(encoding="utf-8")
        self.assertIn('from "../../../katex_macros.json"', reader)
        self.assertIn("katexMacrosForFormula()", reader)
        self.assertNotIn('"\\\\Bin"', reader)
        rendered = build_wiki.PREVIEW_JS.replace("/*__KATEX_MACROS__*/{}", build_wiki.katex_macros_literal(), 1)
        self.assertIn("htmlAndMathml", rendered)
        self.assertIn('querySelector(".katex, math")', rendered)
        self.assertIn(build_wiki.katex_macros_literal(), rendered)
        for name in (r"\given", r"\Bin", r"\vect"):
            self.assertIn(name, definitions)

    def test_page_gains_mathml_and_loses_the_client_renderer(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            (site / "index.html").write_text(PAGE, encoding="utf-8")
            subprocess.run(
                ["node", str(ROOT / "tools" / "prerender_math.mjs"), "--site", str(site)],
                cwd=ROOT,
                check=True,
                text=True,
            )
            html = (site / "index.html").read_text(encoding="utf-8")
            self.assertIn("<math", html)
            self.assertIn("katex-mathml", html)
            self.assertNotIn("katex-error", html)
            self.assertNotIn("katex.min.js", html)
            self.assertIn("katex.min.css", html)
            self.assertIn("function ensureKatex()", html)
            self.assertIn(">not a formula</span>", html)
            self.assertIn(">data class only</span>", html)
            self.assertIn("comment formula", html)
            self.assertIn("script formula", html)
            self.assertNotIn('getElementsByClassName("math");', html.split("typesetMath", 1)[0])
            self.assertIn('querySelector(".katex, math")', html)
            again = subprocess.run(
                ["node", str(ROOT / "tools" / "prerender_math.mjs"), "--site", str(site)],
                cwd=ROOT,
                check=True,
                text=True,
            )
            self.assertEqual((site / "index.html").read_text(encoding="utf-8"), html)
            self.assertEqual(again.returncode, 0)

    def test_given_bin_and_vect_prerender_and_gdef_does_not_leak(self) -> None:
        page = """<!DOCTYPE html><html><body>
<span class="math inline">\\given</span>
<span class="math inline">\\Bin(n,p)</span>
<span class="math inline">\\vect{x}</span>
</body></html>
"""
        leak = """<!DOCTYPE html><html><body>
<span class="math inline">\\gdef\\foo{9}</span>
<span class="math inline">\\foo</span>
</body></html>
"""
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            (site / "ok.html").write_text(page, encoding="utf-8")
            subprocess.run(
                ["node", str(ROOT / "tools" / "prerender_math.mjs"), "--site", str(site)],
                cwd=ROOT,
                check=True,
                text=True,
            )
            html = (site / "ok.html").read_text(encoding="utf-8")
            self.assertNotIn("katex-error", html)
            self.assertEqual(html.count("<math"), 3)
            self.assertIn(">Bin<", html)
            isolated = subprocess.run(
                ["node", "--input-type=module", "-e", r"""
import { formulaMacros } from "./tools/prerender_math.mjs";
import { createRequire } from "node:module";
const katex = createRequire(import.meta.url)("./katex/katex.min.js");
const used = formulaMacros();
katex.renderToString("\\gdef\\foo{9}", { throwOnError: true, strict: "ignore", macros: used });
const next = formulaMacros();
if (Object.prototype.hasOwnProperty.call(next, "\\foo")) process.exit(2);
try {
  katex.renderToString("\\foo", { throwOnError: true, strict: "ignore", macros: next });
  process.exit(3);
} catch (error) {
  if (!String(error.message).includes("Undefined control sequence")) throw error;
}
"""],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(isolated.returncode, 0, isolated.stdout + isolated.stderr)
            (site / "leak.html").write_text(leak, encoding="utf-8")
            leaked = subprocess.run(
                ["node", str(ROOT / "tools" / "prerender_math.mjs"), "--site", str(site)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(leaked.returncode, 0, leaked.stdout + leaked.stderr)


if __name__ == "__main__":
    unittest.main()
