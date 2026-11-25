"""Fail when rendered maths is a KaTeX error, still raw TeX, or has no MathML.

The static crawl never runs KaTeX, so a page can contain ``.katex-error`` only
after a browser paints it, and it can also look fine in the browser while the
served HTML is still raw TeX. This check loads each page in headless Chromium
twice: once with JavaScript, and once without. Both must show an accessible
form (MathML, or an aria-label on the formula).

    python tools/rendered_math_check.py --site _site articles/normal-distribution.html
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PROBE = r"""
() => {
  const problems = [];
  const errors = document.querySelectorAll(".katex-error");
  if (errors.length) problems.push(errors.length + " .katex-error");
  const rawCommand = /\\[A-Za-z]+/g;
  function withoutTexSource(node) {
    const copy = node.cloneNode(true);
    copy.querySelectorAll("annotation").forEach((ann) => {
      if ((ann.getAttribute("encoding") || "").toLowerCase() === "application/x-tex") ann.remove();
    });
    return copy;
  }
  function commandsIn(text) {
    return [...String(text || "").matchAll(rawCommand)].map((match) => match[0]);
  }
  const spans = document.querySelectorAll("span.math");
  let raw = 0;
  let bare = 0;
  const leaked = new Set();
  spans.forEach((el) => {
    const mathml = el.querySelector("math");
    const rendered = el.querySelector(".katex");
    const label = el.getAttribute("aria-label");
    if (!rendered && !mathml) raw += 1;
    else if (!mathml && !label) bare += 1;
    const visualRoot = el.querySelector(".katex-html") || el;
    const visual = withoutTexSource(visualRoot).textContent || "";
    let spoken = label || "";
    if (mathml) spoken += " " + (withoutTexSource(mathml).textContent || "");
    for (const command of commandsIn(visual).concat(commandsIn(spoken))) leaked.add(command);
  });
  if (raw) problems.push(raw + " untransformed TeX span(s)");
  if (bare) problems.push(bare + " formula(s) without MathML or aria-label");
  if (leaked.size) problems.push("raw command visible or spoken: " + [...leaked].join(", "));
  return problems;
}
"""


def page_problems(browser, url: str, javascript: bool) -> list[str]:
    context = browser.new_context(java_script_enabled=javascript)
    try:
        page = context.new_page()
        page.goto(url, wait_until="load")
        found = page.evaluate(PROBE)
    finally:
        context.close()
    prefix = "js" if javascript else "no-js"
    return [f"{prefix}: {item}" for item in found]


def check_pages(site: Path, names: list[str]) -> list[str]:
    from playwright.sync_api import sync_playwright

    problems: list[str] = []
    targets = names or [
        path.relative_to(site).as_posix()
        for path in sorted(site.rglob("*.html"))
        if "site_libs" not in path.parts
    ]
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        try:
            for name in targets:
                path = site / name
                if not path.is_file():
                    problems.append(f"{name}: missing")
                    continue
                url = path.resolve().as_uri()
                for javascript in (True, False):
                    for item in page_problems(browser, url, javascript):
                        problems.append(f"{name}: {item}")
        finally:
            browser.close()
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check rendered maths for errors and MathML.")
    parser.add_argument("--site", type=Path, default=ROOT / "_site")
    parser.add_argument("pages", nargs="*", help="HTML paths relative to the site")
    args = parser.parse_args(argv)
    site = args.site.resolve()
    if not site.is_dir():
        print(f"Missing site: {site}", file=sys.stderr)
        return 1
    problems = check_pages(site, args.pages)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        print(f"{len(problems)} rendered-maths problem(s)", file=sys.stderr)
        return 1
    checked = len(args.pages) if args.pages else "all"
    print(f"Rendered maths ok ({checked} page(s), with and without JavaScript)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
