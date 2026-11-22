"""Review follow-ups: infobox keyboard control, path highlighting, glossary case."""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

import build_wiki


ROOT = Path(__file__).resolve().parent


class InfoboxKeyboardTests(unittest.TestCase):
    """Exercise the actual enhancement in Chromium, including native key input."""

    @classmethod
    def setUpClass(cls):
        from playwright.sync_api import sync_playwright
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()
        cls.fixture = (
            '<!doctype html><html><head><style>'
            + (ROOT / "styles.css").read_text(encoding="utf-8")
            + '</style></head><body><main id="quarto-document-content">'
            '<p id="lead">The lead precedes the summary.</p>'
            '<div class="infobox"><div class="infobox-title"><p>Beta distribution</p></div>'
            '<table><tbody><tr><td>Support</td><td><a href="#after">A body link</a></td>'
            '</tr></tbody></table></div><a id="after" href="#lead">After summary</a>'
            '</main>' + build_wiki.SIDEBAR_JS + '</body></html>'
        )

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def page(self, width=1024, **options):
        context = self.browser.new_context(viewport={"width": width, "height": 800}, **options)
        self.addCleanup(context.close)
        page = context.new_page()
        return page

    def test_native_control_keyboard_state_and_resize(self):
        page = self.page()
        page.set_content(self.fixture)
        button = page.get_by_role("button", name="Beta distribution Show details")
        self.assertEqual(button.count(), 1)
        button = page.locator('.infobox-toggle')
        self.assertEqual(button.evaluate("el => el.parentElement.tagName"), "H2")
        self.assertEqual(button.get_attribute("type"), "button")
        body_id = button.get_attribute("aria-controls")
        body = page.locator('#' + body_id)
        self.assertEqual(body.count(), 1)
        self.assertEqual(button.get_attribute("aria-expanded"), "false")
        self.assertTrue(body.evaluate("el => el.inert"))
        page.keyboard.press("Tab")
        self.assertTrue(button.evaluate("el => el === document.activeElement"))
        page.keyboard.press("Tab")
        self.assertEqual(page.evaluate("document.activeElement.id"), "after")
        for key in ("Enter", "Space"):
            button.focus()
            page.keyboard.press(key)
            self.assertEqual(button.get_attribute("aria-expanded"), "true")
            self.assertFalse(body.evaluate("el => el.inert"))
            page.keyboard.press("Tab")
            self.assertEqual(page.evaluate("document.activeElement.textContent"), "A body link")
            button.focus()
            page.keyboard.press(key)
            self.assertEqual(button.get_attribute("aria-expanded"), "false")
        for width in (899, 900, 1200, 1201, 1366, 390, 1024):
            page.set_viewport_size({"width": width, "height": 800})
            compact = 900 <= width <= 1200
            page.wait_for_function(
                "compact => document.querySelector('.infobox').classList.contains('is-compact') === compact",
                arg=compact,
            )
            self.assertEqual(button.is_visible(), compact)
            self.assertEqual(button.is_enabled(), compact)
            self.assertEqual(body.evaluate("el => el.inert"), compact)
            self.assertEqual(button.get_attribute("aria-controls"), body_id)
            self.assertEqual(page.locator('.infobox-toggle').count(), 1)
        # Resizing a focused body link into the closed compact range moves
        # focus to its control, without leaving focus inside an inert subtree.
        page.set_viewport_size({"width": 1366, "height": 800})
        page.wait_for_function("""() =>
            window.innerWidth === 1366 &&
            !document.querySelector('.infobox').classList.contains('is-compact') &&
            !document.querySelector('.infobox-body').inert
        """)
        body.locator('a').focus()
        self.assertTrue(body.locator('a').evaluate("el => el === document.activeElement"))
        page.set_viewport_size({"width": 1024, "height": 800})
        page.wait_for_function("document.activeElement.matches('.infobox-toggle')")
        page.keyboard.press("Enter")
        self.assertEqual(button.get_attribute("aria-expanded"), "true")
        page.set_viewport_size({"width": 1366, "height": 800})
        page.wait_for_function("document.activeElement.matches('.infobox-label')")
        page.set_viewport_size({"width": 1024, "height": 800})
        page.wait_for_function("document.querySelector('.infobox').classList.contains('is-compact')")
        self.assertEqual(button.get_attribute("aria-expanded"), "true")
        self.assertFalse(body.evaluate("el => el.inert"))

    def test_no_script_and_failed_initialization_leave_content_readable(self):
        self.assertNotIn('infobox-compact', (ROOT / '_theme-head.html').read_text())
        for width in (390, 900, 1024, 1200, 1366):
            with self.subTest(width=width, javascript=False):
                page = self.page(width, java_script_enabled=False)
                page.set_content(self.fixture)
                self.assertTrue(page.get_by_text('A body link').is_visible())
                self.assertEqual(page.get_by_role('button').count(), 0)
            with self.subTest(width=width, initialization='failed'):
                page = self.page(width)
                failing = """<script>
                const add = HTMLElement.prototype.addEventListener;
                HTMLElement.prototype.addEventListener = function (...args) {
                  if (this.matches('.infobox-toggle')) throw Error('initialization failed');
                  return add.apply(this, args);
                };
                </script>"""
                page.set_content(self.fixture.replace('<body>', '<body>' + failing))
                self.assertTrue(page.get_by_text('A body link').is_visible())
                self.assertEqual(page.locator('.is-compact').count(), 0)

    def test_action_cue_contrast_focus_and_lead_order(self):
        page = self.page()
        page.set_content(self.fixture)
        for dark in (False, True):
            page.evaluate("dark => document.body.classList.toggle('quarto-dark', dark)", dark)
            colors = page.locator('.infobox-cue').evaluate("""el => [
                getComputedStyle(el).color,
                getComputedStyle(el.closest('.infobox')).backgroundColor
            ]""")
            def luminance(rgb):
                import re
                values = [int(n)/255 for n in re.findall(r"\d+", rgb)[:3]]
                linear = [v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in values]
                return sum(v*w for v, w in zip(linear, (.2126, .7152, .0722)))
            light, dim = sorted(map(luminance, colors), reverse=True)
            self.assertGreaterEqual((light+.05)/(dim+.05), 3)
            button = page.locator('.infobox-toggle')
            button.focus()
            self.assertEqual(button.evaluate("el => getComputedStyle(el).outlineWidth"), '3px')
        self.assertTrue(page.evaluate("""() =>
            document.querySelector('#lead').getBoundingClientRect().bottom <=
            document.querySelector('.infobox').getBoundingClientRect().top
        """))


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
