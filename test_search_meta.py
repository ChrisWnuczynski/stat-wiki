"""Tests for search_meta.py post-render search.json cleanup and skip-link preservation."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import build_wiki
import search_meta


class SearchIndexSkipLinkTests(unittest.TestCase):
    """STA-214: search.json strips 'Skip to main content' while pages keep a working skip link."""

    def test_clean_search_index_strips_leading_skip_link_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            rows = [
                {
                    "objectID": "search.html",
                    "href": "search.html",
                    "title": "Search",
                    "section": "",
                    "text": "Skip to main content\n\n\nPress Enter in the search box at the top.",
                },
                {
                    "objectID": "articles/expectation.html",
                    "href": "articles/expectation.html",
                    "title": "Expectation",
                    "section": "",
                    "text": "Skip to main content\nIn probability theory, expectation is the probability-weighted average.",
                },
                {
                    "objectID": "files/roughness.html",
                    "href": "files/roughness.html",
                    "title": "Roughness",
                    "section": "",
                    "text": "Skip to main content",
                },
                {
                    "objectID": "files/roughness.html#summary",
                    "href": "files/roughness.html#summary",
                    "title": "Roughness",
                    "section": "Summary",
                    "text": "Summary\nCurvature penalty across knots.",
                },
                {
                    "objectID": "questions/empty.html",
                    "href": "questions/empty.html",
                    "title": "Standalone",
                    "section": "",
                    "text": "Skip to main content",
                },
                {
                    "objectID": "articles/expectation.html#properties",
                    "href": "articles/expectation.html#properties",
                    "title": "Expectation",
                    "section": "Properties",
                    "text": "Properties\nLinearity holds without independence.",
                },
                {
                    "objectID": "articles/body-mention.html",
                    "href": "articles/body-mention.html",
                    "title": "Body mention",
                    "section": "",
                    "text": "Keyboard users rely on a Skip to main content link.",
                },
                {
                    "objectID": "articles/prefix-guard.html",
                    "href": "articles/prefix-guard.html",
                    "title": "Prefix guard",
                    "section": "",
                    "text": "Skip to main contents of the appendix.",
                },
            ]
            search_path = site / "search.json"
            search_path.write_text(json.dumps(rows, indent=2), encoding="utf-8")

            changed = search_meta.clean_search_index(site)
            self.assertEqual(changed, 4)
            cleaned = json.loads(search_path.read_text(encoding="utf-8"))
            by_id = {row["objectID"]: row for row in cleaned}
            self.assertNotIn("files/roughness.html", by_id)
            self.assertEqual(by_id["files/roughness.html#summary"]["text"], "Summary\nCurvature penalty across knots.")
            self.assertEqual(by_id["questions/empty.html"]["text"], "")
            self.assertEqual(by_id["search.html"]["text"], "Press Enter in the search box at the top.")
            self.assertEqual(
                by_id["articles/expectation.html"]["text"],
                "In probability theory, expectation is the probability-weighted average.",
            )
            self.assertEqual(by_id["articles/expectation.html#properties"]["text"], "Properties\nLinearity holds without independence.")
            self.assertEqual(by_id["articles/body-mention.html"]["text"], "Keyboard users rely on a Skip to main content link.")
            self.assertEqual(by_id["articles/prefix-guard.html"]["text"], "Skip to main contents of the appendix.")
            self.assertFalse(
                any(r["text"].startswith("Skip to main content") for r in cleaned if r["href"] != "articles/prefix-guard.html")
            )

            saved = search_path.read_text(encoding="utf-8")
            self.assertEqual(search_meta.clean_search_index(site), 0)
            self.assertEqual(search_path.read_text(encoding="utf-8"), saved)

    def test_rendered_site_strips_skip_link_from_search_json_and_preserves_skip_link(self) -> None:
        quarto = shutil.which("quarto")
        if not quarto:
            self.skipTest("Quarto is not installed")

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ("_theme-body.html", "_theme-head.html", "styles.css", "theme.scss", "search_meta.py"):
                shutil.copyfile(build_wiki.WIKI / name, root / name)
            (root / "articles").mkdir()
            (root / "files").mkdir()
            (root / "_quarto.yml").write_text(
                "lang: en\n"
                "project:\n"
                "  type: website\n"
                "  output-dir: _site\n"
                "  post-render:\n"
                "    - search_meta.py\n"
                "  render:\n"
                "    - '*.qmd'\n"
                "    - 'articles/*.qmd'\n"
                "    - 'files/*.qmd'\n"
                "website:\n"
                "  title: StatWiki\n"
                "  site-url: https://www.statwiki.io\n"
                "  search:\n"
                "    location: navbar\n"
                "    type: textbox\n"
                "format:\n"
                "  html:\n"
                "    theme:\n"
                "      light: [cosmo, theme.scss]\n"
                "      dark: [darkly, theme.scss]\n"
                "    css: styles.css\n"
                "    include-in-header: _theme-head.html\n"
                "    include-before-body: _theme-body.html\n"
                "    canonical-url: true\n",
                encoding="utf-8",
            )
            (root / "index.qmd").write_text(
                "---\ntitle: StatWiki\ntoc: false\n---\n\n"
                "A study wiki for probability, inference, and statistical learning.\n",
                encoding="utf-8",
            )
            (root / "search.qmd").write_text(
                "---\ntitle: Search\ntoc: false\n---\n\n"
                "Press Enter in the search box at the top to open this page.\n",
                encoding="utf-8",
            )
            (root / "articles" / "sample.qmd").write_text(
                "---\ntitle: Sample mean\n---\n\n"
                "::: {.chapter-guide}\n[Beginner]{.level}\n:::\n\n"
                "::: {.hatnote}\nDefinition taught in Descriptive statistics\n:::\n\n"
                "**Sample mean.** The arithmetic average of observed values in a sample.\n\n"
                "## Properties {#properties}\n\n"
                "Adding a constant shifts the sample mean by that constant.\n",
                encoding="utf-8",
            )
            (root / "files" / "figure.qmd").write_text(
                "---\ntitle: Roughness figure\n---\n\n"
                "## Summary {#summary}\n\n"
                "Curvature penalty plotted across candidate smoothing values.\n",
                encoding="utf-8",
            )

            res = subprocess.run([quarto, "render"], cwd=root, text=True, capture_output=True)
            self.assertEqual(res.returncode, 0, res.stdout + "\n" + res.stderr)

            rows = json.loads((root / "_site" / "search.json").read_text(encoding="utf-8"))
            self.assertGreaterEqual(len(rows), 5)
            for row in rows:
                self.assertFalse(
                    row["text"].lstrip().startswith("Skip to main content"),
                    f"search.json record {row['objectID']} still starts with Skip to main content: {row['text']!r}",
                )
                self.assertNotIn("Skip to main content", row["text"], row["objectID"])

            by_id = {row["objectID"]: row for row in rows}
            self.assertTrue(by_id["search.html"]["text"].startswith("Press Enter in the search box"))
            self.assertTrue(by_id["articles/sample.html"]["text"].startswith("Sample mean. The arithmetic average"))
            self.assertNotIn("Definition taught in", by_id["articles/sample.html"]["text"])
            self.assertNotIn("files/figure.html", by_id)
            self.assertIn("Curvature penalty", by_id["files/figure.html#summary"]["text"])

            for rel in ("index.html", "search.html", "articles/sample.html", "files/figure.html"):
                html_text = (root / "_site" / rel).read_text(encoding="utf-8")
                self.assertIn('<a class="skip-link" href="#quarto-document-content">Skip to main content</a>', html_text, rel)
                self.assertIn('id="quarto-document-content"', html_text, rel)

    def test_skip_link_script_moves_anchor_first_in_body_and_focuses_main(self) -> None:
        node = shutil.which("node")
        if not node:
            self.skipTest("Node is not installed")
        theme_body = (build_wiki.WIKI / "_theme-body.html").read_text(encoding="utf-8")
        first_script = re.search(r"<script>(.*?)</script>", theme_body, re.S)
        self.assertIsNotNone(first_script)
        probe = (
            "const script = " + json.dumps(first_script.group(1)) + ";\n"
            "let focused = null;\n"
            "const attrs = new Map();\n"
            "let clickHandler = null;\n"
            "const brand = { id: 'brand' };\n"
            "const link = {\n"
            "  classList: { contains: (c) => c === 'skip-link' },\n"
            "  addEventListener: (ev, fn) => { if (ev === 'click') clickHandler = fn; },\n"
            "};\n"
            "const scriptEl = { previousElementSibling: link };\n"
            "const main = {\n"
            "  id: 'quarto-document-content',\n"
            "  hasAttribute: (k) => attrs.has(k),\n"
            "  setAttribute: (k, v) => attrs.set(k, String(v)),\n"
            "  focus: () => { focused = main; },\n"
            "};\n"
            "const children = [brand, main];\n"
            "const body = {\n"
            "  get firstChild() { return children[0]; },\n"
            "  insertBefore(node, ref) {\n"
            "    const idx = children.indexOf(ref);\n"
            "    children.splice(idx < 0 ? 0 : idx, 0, node);\n"
            "  },\n"
            "};\n"
            "globalThis.document = {\n"
            "  currentScript: scriptEl,\n"
            "  body,\n"
            "  querySelector: (sel) => sel === 'a.skip-link' ? link : null,\n"
            "  getElementById: (id) => id === 'quarto-document-content' ? main : null,\n"
            "};\n"
            "eval(script);\n"
            "if (children[0] !== link) { console.error('skip-link not moved before navbar'); process.exit(1); }\n"
            "if (!clickHandler) { console.error('missing click handler'); process.exit(2); }\n"
            "clickHandler();\n"
            "if (attrs.get('tabindex') !== '-1' || focused !== main) { console.error('main not focused'); process.exit(3); }\n"
        )
        res = subprocess.run([node, "-e", probe], text=True, capture_output=True)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)


if __name__ == "__main__":
    unittest.main()
