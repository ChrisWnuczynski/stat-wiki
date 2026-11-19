"""Review follow-ups: infobox keyboard control, path highlighting, glossary case."""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

import build_wiki


ROOT = Path(__file__).resolve().parent


class InfoboxKeyboardTests(unittest.TestCase):
    def test_title_is_a_tab_stop_only_while_compact(self):
        js = build_wiki.SIDEBAR_JS
        sync = js.split("function syncCompact", 1)[1].split("function armInfoboxes", 1)[0]
        arm = js.split("function armInfoboxes", 1)[1].split("function applySidebar", 1)[0]
        self.assertIn('setAttribute("tabindex", "0")', sync)
        self.assertIn('setAttribute("role", "button")', sync)
        self.assertIn('setAttribute("aria-expanded"', sync)
        self.assertIn('removeAttribute("role")', sync)
        self.assertIn('removeAttribute("tabindex")', sync)
        self.assertIn('removeAttribute("aria-expanded")', sync)
        self.assertNotIn('setAttribute("role"', arm)
        self.assertNotIn('setAttribute("tabindex"', arm)
        self.assertLess(arm.find("infobox-compact"), arm.find('setAttribute("aria-expanded"'))
        self.assertIn('event.key !== "Enter"', arm)
        self.assertIn('event.key !== " "', arm)
        css = (ROOT / "styles.css").read_text(encoding="utf-8")
        self.assertIn(
            "html.infobox-compact .infobox:not(.is-open) > :not(.infobox-title)",
            css,
        )
        rule = css.split("html.infobox-compact .infobox:not(.is-open) > :not(.infobox-title)", 1)[1]
        self.assertIn("visibility: hidden", rule.split("}", 1)[0])


class PathHighlightTests(unittest.TestCase):
    def test_extensionless_and_index_urls_match(self):
        js = build_wiki.SIDEBAR_JS
        start = js.find("function normalisePath")
        end = js.find("function markCurrent")
        self.assertGreater(start, 0)
        self.assertIn("normalisePath(location.pathname)", js)
        self.assertIn("normalisePath(links[i].pathname)", js)
        script = js[start:end] + r"""
const cases = [
  ["/notes/foo/index.html", "/notes/foo"],
  ["/notes/foo.html", "/notes/foo"],
  ["/notes/foo/", "/notes/foo"],
  ["/notes/foo", "/notes/foo"],
  ["/notes/", "/notes"],
  ["/notes/index.html", "/notes"],
  ["/", "/"],
  ["/index.html", "/"],
  ["/articles/kurtosis.html", "/articles/kurtosis"],
  ["/articles/kurtosis/", "/articles/kurtosis"],
  ["/articles/kurtosis/index.html", "/articles/kurtosis"],
];
for (const [raw, want] of cases) {
  const got = normalisePath(raw);
  if (got !== want) {
    console.error("FAIL", raw, got, "!=", want);
    process.exit(1);
  }
}
"""
        subprocess.run(["node", "-e", script], check=True)


class GlossaryCaseTests(unittest.TestCase):
    def test_k_names_keep_their_case(self):
        anonymity = build_wiki.glossary_plain_lead({"slug": "k-anonymity"})
        self.assertTrue(anonymity.startswith("k-anonymity "))
        clustering = build_wiki.glossary_plain_lead({"slug": "k-means-as-a-limiting-case"})
        self.assertTrue(clustering.startswith("k-means "))
        criterion = build_wiki.glossary_plain_lead({"slug": "k-means-criterion"})
        self.assertTrue(criterion.startswith("The k-means criterion "))
        lloyd = build_wiki.glossary_plain_lead({"slug": "lloyd-s-k-means-algorithm"})
        self.assertTrue(lloyd.startswith("Lloyd's K-means algorithm "))


if __name__ == "__main__":
    unittest.main()
