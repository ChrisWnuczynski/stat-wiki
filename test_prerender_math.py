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
        macros = json.loads((ROOT / "katex_macros.json").read_text(encoding="utf-8"))
        self.assertEqual(set(macros), {"\\E", "\\Var", "\\Cov"})
        literal = build_wiki.katex_macros_literal()
        self.assertIn('"\\\\E"', literal)
        preview = build_wiki.PREVIEW_JS.replace("/*__KATEX_MACROS__*/{}", literal, 1)
        self.assertIn("htmlAndMathml", preview)
        self.assertIn('querySelector(".katex, math")', preview)
        self.assertIn(literal, preview)

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


if __name__ == "__main__":
    unittest.main()
