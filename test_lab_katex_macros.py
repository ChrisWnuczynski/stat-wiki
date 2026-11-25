"""Laboratories receive the article shorthand table, and KaTeX builtins stay native."""

from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import build_wiki


ROOT = Path(__file__).resolve().parent
KATEX = ROOT / "katex" / "katex.min.js"

PROBE = r"""
import { createRequire } from "node:module";
import { readFileSync } from "node:fs";

const require = createRequire(import.meta.url);
const katex = require(process.argv[2]);
const macros = JSON.parse(readFileSync(process.argv[3], "utf8"));
const native = JSON.parse(readFileSync(process.argv[4], "utf8"));
const custom = JSON.parse(readFileSync(process.argv[5], "utf8"));
const header = readFileSync(process.argv[6], "utf8");
const mise = readFileSync(process.argv[7], "utf8");

for (const name of native) {
  katex.renderToString("\\" + name, { throwOnError: true, strict: "ignore" });
}
for (const name of custom) {
  let threw = false;
  try {
    katex.renderToString("\\" + name, { throwOnError: true, strict: "ignore" });
  } catch (error) {
    threw = true;
  }
  if (!threw) {
    console.error(name + " rendered without a macro; it must not be overridden");
    process.exit(2);
  }
}

const html = katex.renderToString(mise, { throwOnError: true, macros, strict: "ignore" });
if (html.includes("katex-error") || !html.includes('class="mord mathbb"')) {
  console.error("MISE equation did not paint a blackboard-bold E");
  process.exit(3);
}
const pr = katex.renderToString("\\Pr(K=k\\mid x)", { throwOnError: true, macros, strict: "ignore" });
if (pr.includes("katex-error") || !pr.includes('class="mop"') || pr.includes("mathbb")) {
  console.error("\\Pr was overridden or failed to render");
  process.exit(4);
}

const script = header.replace(/^<script>\n/, "").replace(/\n<\/script>\n?$/, "");
const listeners = [];
globalThis.document = {
  addEventListener(type, fn, capture) {
    listeners.push({ type, fn, capture });
  },
};
const calls = [];
globalThis.window = {
  katex: {
    render(tex, el, opts) { calls.push(opts); },
    renderToString(tex, opts) { calls.push(opts); return ""; },
  },
};
eval(script);
if (listeners.length !== 1 || listeners[0].type !== "DOMContentLoaded" || listeners[0].capture !== true) {
  console.error("macro script did not register a capture listener");
  process.exit(5);
}
listeners[0].fn();
window.katex.render("\\E", null, { macros: [], throwOnError: false });
const supplied = calls.at(-1).macros;
if (supplied["\\E"] !== "\\mathbb{E}" || Array.isArray(supplied)) process.exit(6);
window.katex.render("\\E", null, { macros: { "\\E": "\\mathrm{E}" } });
const overridden = calls.at(-1).macros;
if (overridden["\\E"] !== "\\mathrm{E}" || overridden["\\Var"] !== "\\operatorname{Var}") process.exit(7);
"""


class LabKatexMacroTests(unittest.TestCase):
    def test_shared_table_covers_shorthand_and_leaves_native_commands(self) -> None:
        macros = build_wiki.katex_macro_definitions()
        self.assertEqual(macros[r"\E"], r"\mathbb{E}")
        self.assertEqual(macros[r"\Var"], r"\operatorname{Var}")
        self.assertEqual(macros[r"\Cov"], r"\operatorname{Cov}")
        self.assertEqual(macros[r"\vect"], r"{\boldsymbol{#1}}")
        self.assertEqual(macros[r"\mat"], r"{\color{blue}\boldsymbol{#1}}")
        for name in build_wiki.KATEX_NATIVE:
            self.assertNotIn("\\" + name, macros)
        for name, body in build_wiki.ZERO_ARG.items():
            if name in build_wiki.KATEX_NATIVE:
                continue
            self.assertEqual(macros["\\" + name], body)
        header = build_wiki.katex_macro_header()
        self.assertIn(json.dumps(r"\E"), header)
        self.assertIn(json.dumps(r"\mathbb{E}"), header)
        self.assertNotIn(json.dumps(r"\Pr"), header)
        source = (ROOT / "build_wiki.py").read_text(encoding="utf-8")
        self.assertIn("- _katex-macros.html", source)

    def test_kernel_density_expectation_is_handled_and_pr_is_not_rewritten(self) -> None:
        kde = (ROOT / "labs" / "kernel-density.qmd").read_text(encoding="utf-8")
        self.assertIn(r"\E\int", kde)
        self.assertEqual(
            build_wiki.unhandled_lab_shorthand(kde, build_wiki.katex_macro_definitions(), build_wiki.KATEX_NATIVE),
            [],
        )
        beta = (ROOT / "labs" / "beta-binomial.qmd").read_text(encoding="utf-8")
        self.assertIn(r"\Pr(K=k", beta)
        self.assertEqual(
            build_wiki.unhandled_lab_shorthand(beta, build_wiki.katex_macro_definitions(), build_wiki.KATEX_NATIVE),
            [],
        )
        self.assertEqual(build_wiki.lab_shorthand_problems(ROOT), [])
        bare = build_wiki.unhandled_lab_shorthand(r"$$\E[X]$$", {}, build_wiki.KATEX_NATIVE)
        self.assertEqual(bare, [(1, r"\E")])
        self.assertEqual(build_wiki.unhandled_lab_shorthand("```\n\\E\n```", {}, frozenset()), [])

    def test_vendored_katex_accepts_the_table_and_the_header_script(self) -> None:
        macros = build_wiki.katex_macro_definitions()
        native = sorted(build_wiki.KATEX_NATIVE)
        custom = sorted(name for name in set(build_wiki.ZERO_ARG) | set(build_wiki.ONE_ARG) if name not in build_wiki.KATEX_NATIVE)
        mise = r"\mathrm{MISE}(h)=\mathrm{IVar}(h)+\mathrm{IBias}^2(h)=\E\int_{-\infty}^{\infty}\bigl(\widehat f_h(x)-f(x)\bigr)^2\,\mathrm{d}x."
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            (folder / "macros.json").write_text(json.dumps(macros), encoding="utf-8")
            (folder / "native.json").write_text(json.dumps(native), encoding="utf-8")
            (folder / "custom.json").write_text(json.dumps(custom), encoding="utf-8")
            (folder / "header.html").write_text(build_wiki.katex_macro_header(), encoding="utf-8")
            (folder / "mise.tex").write_text(mise, encoding="utf-8")
            (folder / "probe.mjs").write_text(PROBE, encoding="utf-8")
            result = subprocess.run(
                [
                    "node",
                    str(folder / "probe.mjs"),
                    str(KATEX),
                    str(folder / "macros.json"),
                    str(folder / "native.json"),
                    str(folder / "custom.json"),
                    str(folder / "header.html"),
                    str(folder / "mise.tex"),
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
