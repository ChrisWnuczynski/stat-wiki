"""Keyboard regression against Quarto 1.6.40 and real Chromium.

Run after build_wiki.py. Set STATWIKI_ANSWER_EVIDENCE to retain the complete
rendered fixture site, render log and screenshots outside the temporary folder.
"""
from __future__ import annotations

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os
import json
import re
from pathlib import Path
import shutil
import subprocess
import tempfile
import threading
import unittest
from unittest.mock import patch

import build_wiki

ROOT = Path(__file__).resolve().parent
MARKER = "statwiki-generated-check-answer"

OPEN = ":::::::::: {." + MARKER + "}\n\n"
CLOSE = "\n::::::::::\n"


def wrap(inner):
    return "\n" + OPEN + inner + CLOSE


def unwrap(text):
    return text.replace(OPEN, "").replace(CLOSE, "")


class GeneratedAnswerProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.article = {"slug": "answer-fixture", "path": ROOT / "articles/answer-fixture.qmd"}
        self.question = {
            "id": "answer-fixture-q1", "title": "A question",
            "path": ROOT / "questions/answer-fixture-q1.qmd",
            "prepared_body": "Compute the margin.",
            "prepared_answer": "A sufficiently long answer explains the calculation in detail, "
                               "preserving the original body and its comparison key.\n\n"
                               "## Reasoning\n\nThe conclusion follows from the calculation.",
        }
        self.check = build_wiki._render_bank_check(self.article, self.question)
        self.inner = next(item[1] for item in build_wiki._iter_callouts(unwrap(self.check))
                          if item[0] == "callout")
        self.wrapper = next(item[1] for item in build_wiki._iter_callouts(self.check)
                            if item[0] == "callout")

    def test_real_fences_headings_and_original_comparison_key(self):
        original = (
            "\n### A question {#self-check-answer-fixture-q1}\n\n"
            "[Question-bank page: A question](../questions/answer-fixture-q1.qmd)\n\n"
            "Compute the margin.\n\n"
            ':::::::: {.callout-tip collapse="true" title="Answer"}\n\n'
            + self.question["prepared_answer"].replace("## Reasoning", "### Reasoning")
            + "\n\n::::::::\n")
        self.assertEqual(unwrap(self.check), original)
        old = next(item[2] for item in build_wiki._iter_callouts(original) if item[0] == "callout")
        new = next(item[2] for item in build_wiki._iter_callouts(self.check) if item[0] == "callout")
        self.assertEqual(new, old)
        intro, sections = build_wiki._split_prompts(self.check)
        self.assertEqual(len(sections), 1)
        self.assertIn("### Reasoning", sections[0])
        self.assertIn(self.wrapper, sections[0])

    def test_keep_drop_and_authored_duplicates_leave_no_empty_wrapper(self):
        key = build_wiki._callout_key(self.question["prepared_answer"].replace("## Reasoning", "### Reasoning"))
        self.assertEqual(build_wiki._strip_duplicate_callouts(self.wrapper, set()), self.wrapper)
        self.assertEqual(build_wiki._strip_duplicate_callouts(self.wrapper, {key}), "")
        for first, second in ((self.inner, self.wrapper), (self.wrapper, self.inner)):
            result = build_wiki._strip_duplicate_callouts(first + "\n\n" + second, set())
            self.assertEqual(result.strip(), first)
        # No other named div gets this special balancing treatment.
        ordinary = self.wrapper.replace(MARKER, "authored-wrapper")
        items = list(build_wiki._iter_callouts(ordinary))
        self.assertEqual(next(item[1] for item in items if item[0] == "callout"), self.inner)

    def test_balancing_parks_or_drops_whole_provenance(self):
        example = "\n## Examples {#examples}\n\n[Question](../questions/answer-fixture-q1.qmd)\n"
        for already_answered in (False, True):
            with self.subTest(already_answered=already_answered), \
                    patch.dict(build_wiki.EXAMPLES, {self.article["slug"]: [self.question["id"]]}), \
                    patch.object(build_wiki, "CHECK_GAPS", []):
                blocks = [(True, "examples", example + (self.inner if already_answered else "")),
                          (True, "check-yourself", "\n## Check yourself {#check-yourself}\n" + self.check)]
                result = build_wiki.balance_check_yourself(self.article, blocks, {})
                combined = "".join(text for _, _, text in result)
                self.assertEqual(combined.count(self.inner), 1)
                self.assertEqual(combined.count(MARKER), 0 if already_answered else 1)
                self.assertIn(self.inner if already_answered else self.wrapper, result[0][2])
                self.assertFalse(any(label == "check-yourself" for _, label, _ in result))

    def test_graph_keeps_answers_separate_and_does_not_index_wrapper(self):
        graph = json.loads((ROOT / "wiki.json").read_text())
        entries = {entry["id"]: entry for entry in graph["entries"]}
        answer = entries["answer:question:depth-hinge-loss-q1"]["text"]
        self.assertIn("The hinge is", answer)
        for key in ("article:hinge-loss", "question:depth-hinge-loss-q1"):
            self.assertNotIn(answer, entries[key].get("text", ""))
            self.assertNotIn("The hinge is $1-0.2=0.8$", entries[key].get("text", ""))
        self.assertNotIn(MARKER, json.dumps(graph))


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class AnswerDisclosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from playwright.sync_api import sync_playwright

        version = subprocess.check_output(["quarto", "--version"], text=True).strip()
        if version != "1.6.40":
            raise AssertionError(f"Expected pinned Quarto 1.6.40, got {version}")
        cls.temp = tempfile.TemporaryDirectory(prefix="statwiki-answer-")
        cls.addClassCleanup(cls.temp.cleanup)
        cls.root = Path(cls.temp.name)
        for name in ("styles.css", "theme.scss", "_theme-head.html", "_theme-body.html"):
            shutil.copyfile(ROOT / name, cls.root / name)
        shutil.copytree(ROOT / "katex", cls.root / "katex")
        (cls.root / "_sidebar.html").write_text(build_wiki.SIDEBAR_JS + build_wiki.PREVIEW_JS, encoding="utf-8")
        (cls.root / "_quarto.yml").write_text('''project:
  type: website
  output-dir: _site
  render:
    - articles/hinge-loss.qmd
    - articles/hazard-rate.qmd
    - questions/depth-hinge-loss-q1.qmd
    - articles/linear-separators-and-the-margin.qmd
    - article-fixture.qmd
    - plain-fixture.qmd
    - hover-fixture.qmd
  resources: [katex/]
website:
  sidebar:
    contents:
      - href: articles/hinge-loss.qmd
        text: Hinge loss
      - href: articles/hazard-rate.qmd
        text: Hazard rate
format:
  html:
    theme:
      light: [cosmo, theme.scss]
      dark: [darkly, theme.scss]
    css: styles.css
    html-math-method:
      method: katex
      url: /katex/
    include-in-header: _theme-head.html
    include-before-body: _theme-body.html
    include-after-body: _sidebar.html
''', encoding="utf-8")
        # Copy complete generated pages, without normalising bodies or fixtures.
        for name in ("articles/hinge-loss.qmd", "articles/hazard-rate.qmd",
                     "questions/depth-hinge-loss-q1.qmd",
                     "articles/linear-separators-and-the-margin.qmd"):
            source = ROOT / name
            if not source.exists():
                raise AssertionError("Run build_wiki.py before this test")
            dest = cls.root / name
            dest.parent.mkdir(exist_ok=True)
            shutil.copyfile(source, dest)
        article = {"slug": "disclosure-fixture", "path": ROOT / "articles/disclosure-fixture.qmd"}
        question = {"id": "fixture-bank", "title": "Bank question",
                    "path": ROOT / "questions/fixture-bank.qmd",
                    "prepared_body": "Compute $2^2$.",
                    "prepared_answer": 'Answer $2^2=4$. [Body link](/article-fixture.html#after){#answer-link}.'}
        with patch.dict(build_wiki.SELF_CHECKS, {article["slug"]: [
                {"prompt": "Compute $1+1$.", "answer": "Answer $1+1=2$."}, "fixture-bank"]}):
            checks = build_wiki.self_check_section(article, {"fixture-bank": question})
        bank = build_wiki._render_bank_check(article, {
            **question, "id": "fixture-fallback", "prepared_answer": "Answer $2^2=4$."})
        relocated = build_wiki._render_bank_check(article, {
            **question, "id": "fixture-relocated", "prepared_answer": "Relocated answer $2^2=4$."})
        cls.generated = checks + bank
        # The relocated wrapper and authored lookalike must stay out of scope.
        # The linked title must remain a DIV: never nest a link in a button.
        fixture = (
            '---\ntitle: Disclosure fixtures\n---\n\n[Before](#after){#before}\n' + checks + bank
            + wrap('::: {.callout-tip collapse="false" title="Answer"}\n'
                   'Initially open answer $3^2=9$.\n:::\n')
            + wrap('::: {.callout-tip collapse="true" title="Answer [link](#after)" #interactive-title}\n'
                   'Unsafe title body.\n:::\n')
            + '\n::: {.callout-tip collapse="true" title="Answer" #unmarked-answer}\n'
              'Authored answer.\n:::\n'
            + '\n## Other section {#other}\n' + relocated
            + '\n[After](#before){#after}\n')
        (cls.root / "article-fixture.qmd").write_text(fixture, encoding="utf-8")
        (cls.root / "plain-fixture.qmd").write_text(unwrap(fixture), encoding="utf-8")
        (cls.root / "hover-fixture.qmd").write_text(
            '---\ntitle: Hover checks\n---\n'
            '[Generated](article-fixture.qmd#self-check-fixture-bank)\n\n'
            '[Relocated](article-fixture.qmd#self-check-fixture-relocated)\n\n'
            '[Real practice](articles/hinge-loss.qmd#self-check-depth-hinge-loss-q1)\n\n'
            '[Worked answer](questions/depth-hinge-loss-q1.qmd#worked-answer)\n', encoding="utf-8")
        result = subprocess.run(["quarto", "render"], cwd=cls.root, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (cls.root / "render.log").write_text(result.stdout, encoding="utf-8")
        cls.evidence = os.environ.get("STATWIKI_ANSWER_EVIDENCE")
        if cls.evidence:
            cls.addClassCleanup(lambda: shutil.copytree(cls.root, cls.evidence, dirs_exist_ok=True))
        if result.returncode:
            raise AssertionError(result.stdout)
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), partial(
            QuietHandler, directory=str(cls.root / "_site")))
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.addClassCleanup(cls.server.server_close)
        cls.addClassCleanup(cls.server.shutdown)
        cls.base = f"http://127.0.0.1:{cls.server.server_port}/"
        cls.playwright = sync_playwright().start()
        cls.addClassCleanup(cls.playwright.stop)
        cls.browser = cls.playwright.chromium.launch()
        cls.addClassCleanup(cls.browser.close)

    def page(self, name, width=1280, **options):
        context = self.browser.new_context(viewport={"width": width, "height": 900}, **options)
        self.addCleanup(context.close)
        page = context.new_page()
        page.goto(self.base + name, wait_until="networkidle")
        return page

    def tab_to(self, page, header):
        """Start from the browser's current position; never call focus()."""
        trail = []
        for _ in range(100):
            page.keyboard.press("Tab")
            if header.evaluate("el => el.contains(document.activeElement)"):
                return
            trail.append(page.evaluate("document.activeElement.outerHTML.slice(0, 160)"))
        self.fail("Natural Tab skipped the answer trigger: " + repr(trail))

    def assert_state(self, page, button, body, expanded):
        page.wait_for_function("id => !document.getElementById(id).classList.contains('collapsing')",
                               arg=body.get_attribute("id"))
        self.assertEqual(button.get_attribute("aria-expanded"), str(expanded).lower())
        self.assertEqual(body.is_visible(), expanded)
        self.assertEqual(body.evaluate("el => el.classList.contains('show')"), expanded)
        hint = button.locator(".callout-title-container").evaluate(
            "el => getComputedStyle(el, '::after').content")
        self.assertEqual("click to show" in hint, not expanded)
        transform = button.locator(".callout-toggle").evaluate(
            "el => getComputedStyle(el, '::before').transform")
        self.assertEqual(transform == "none", expanded)

    def test_real_article_and_standalone_natural_keyboard(self):
        for name, selector, label in (
            ("articles/hinge-loss.html", "#self-check-depth-hinge-loss-q1 .callout", "Answer"),
            ("questions/depth-hinge-loss-q1.html", "#worked-answer", "Worked answer"),
        ):
            for width in (1280, 1024, 390):
                with self.subTest(page=name, width=width):
                    page = self.page(name, width)
                    self.assertEqual(page.evaluate("document.activeElement.tagName"), "BODY")
                    callout = page.locator(selector)
                    header = callout.locator(":scope > .callout-header")
                    body = callout.locator(":scope > .callout-collapse")
                    self.assertFalse(body.is_visible())
                    # This assertion fails on the real unmodified Quarto output.
                    self.tab_to(page, header)
                    button = header.get_by_role("button", name=label, exact=True)
                    self.assertEqual(button.count(), 1)
                    self.assertTrue(button.evaluate("el => el === document.activeElement"))
                    self.assertEqual(button.get_attribute("type"), "button")
                    self.assertEqual(button.get_attribute("aria-controls"), body.get_attribute("id"))
                    self.assertTrue(body.evaluate("(el, sel) => el.matches(sel)",
                                                  button.get_attribute("data-bs-target")))
                    for attr in ("data-bs-toggle", "data-bs-target", "aria-expanded", "aria-controls",
                                 "aria-label", "tabindex", "role"):
                        self.assertIsNone(header.get_attribute(attr))
                    self.assertEqual(button.locator("div, p, h2, a, button, input, [tabindex]").count(), 0)
                    self.assertTrue(button.evaluate("el => el.matches(':focus-visible')"))
                    self.assertEqual(button.evaluate("el => getComputedStyle(el).outlineWidth"), "3px")
                    self.assertEqual(button.evaluate("el => getComputedStyle(el).outlineOffset"), "-3px")
                    self.assertNotEqual(button.evaluate("el => getComputedStyle(el).outlineStyle"), "none")
                    page.screenshot(path=str(self.root / f"{Path(name).stem}-{width}-focus.png"))
                    self.assert_state(page, button, body, False)
                    original = body.inner_html()
                    page.keyboard.press("Tab")
                    self.assertFalse(header.evaluate("el => el.contains(document.activeElement)"))
                    page.keyboard.press("Shift+Tab")
                    self.assertTrue(button.evaluate("el => el === document.activeElement"))
                    for key in ("Enter", "Space"):
                        page.keyboard.press(key)
                        self.assert_state(page, button, body, True)
                        self.assertGreater(body.locator(".katex").count(), 0)
                        self.assertEqual(body.locator(".katex-error").count(), 0)
                        page.keyboard.press(key)
                        self.assert_state(page, button, body, False)
                    button.click()
                    self.assert_state(page, button, body, True)
                    self.assertEqual(body.inner_html(), original)
                    box = button.bounding_box()
                    self.assertGreaterEqual(box["x"], 0)
                    self.assertLessEqual(box["x"] + box["width"], width)
                    if "articles/" in name:
                        sibling = page.locator("#self-check-depth-hinge-loss-q2 .callout-collapse")
                        self.assertFalse(sibling.is_visible())
                        self.assertEqual(page.locator("#self-check-depth-hinge-loss-q1").count(), 1)
                        # The link names its question, not just "Question-bank page" (STA-197).
                        link = page.locator("#self-check-depth-hinge-loss-q1").get_by_role(
                            "link", name=re.compile(r"^Question-bank page: What is the hinge at margin"))
                        self.assertEqual(link.count(), 1)
                        self.assertEqual(link.evaluate("el => new URL(el.href).pathname"),
                                         "/questions/depth-hinge-loss-q1.html")
                    else:
                        link = body.get_by_role("link", name="margin", exact=True)
                        self.assertEqual(link.count(), 1)
                        self.assertEqual(link.evaluate("el => new URL(el.href).pathname"),
                                         "/articles/linear-separators-and-the-margin.html")
                        page.keyboard.press("Tab")
                        self.assertTrue(link.evaluate("el => el === document.activeElement"))
                    page.screenshot(path=str(self.root / f"{Path(name).stem}-{width}.png"))
                    button.click()
                    self.assert_state(page, button, body, False)

    def test_all_emitters_initial_state_independence_and_scope(self):
        self.assertEqual(self.generated.count("." + MARKER), 3)
        self.assertEqual(self.generated.count('collapse="true" title="Answer"'), 3)
        page = self.page("article-fixture.html")
        buttons = page.locator("#check-yourself .statwiki-answer-toggle")
        self.assertEqual(buttons.count(), 4)
        for index in range(4):
            button = buttons.nth(index)
            body = page.locator("#" + button.get_attribute("aria-controls"))
            self.assert_state(page, button, body, index == 3)
        first, second = buttons.nth(0), buttons.nth(1)
        first.click()
        second.click()
        self.assert_state(page, first, page.locator("#" + first.get_attribute("aria-controls")), True)
        self.assert_state(page, second, page.locator("#" + second.get_attribute("aria-controls")), True)
        first.click()
        self.assert_state(page, first, page.locator("#" + first.get_attribute("aria-controls")), False)
        self.assert_state(page, second, page.locator("#" + second.get_attribute("aria-controls")), True)
        page.locator("#answer-link").first.click()
        self.assertTrue(page.url.endswith("#after"))
        for selector in ("#other .callout-header", "#interactive-title > .callout-header",
                         "#unmarked-answer > .callout-header"):
            header = page.locator(selector)
            self.assertEqual(header.get_attribute("data-bs-toggle"), "collapse")
            self.assertEqual(header.locator("button").count(), 0)
        title_link = page.locator("#interactive-title").get_by_role("link", name="link", exact=True)
        self.assertEqual(title_link.count(), 1)
        self.assertEqual(title_link.evaluate("el => new URL(el.href).hash"), "#after")
        # Re-entering DOM ready must not duplicate controls or reset state.
        page.evaluate("document.dispatchEvent(new Event('DOMContentLoaded'))")
        self.assertEqual(buttons.count(), 4)
        self.assertEqual(second.get_attribute("aria-expanded"), "true")

    def test_hover_excerpts_do_not_clone_wrapped_answers(self):
        page = self.page("hover-fixture.html")
        for label, absent in (("Generated", "Body link"), ("Relocated", "Relocated answer"),
                              ("Real practice", "The hinge is"), ("Worked answer", "The hinge is")):
            with self.subTest(link=label):
                page.get_by_role("link", name=label, exact=True).hover()
                preview = page.locator("#wiki-preview")
                preview.wait_for(state="visible")
                self.assertNotIn(absent, preview.inner_text())
                self.assertEqual(preview.locator(
                    "." + MARKER + ", .callout-collapse, [data-bs-toggle=collapse], [aria-controls]"
                ).count(), 0)
                self.assertEqual(preview.locator("[id]").count(), 0)
                self.assertGreater(len(preview.locator(".wp-body").inner_text()), 20)
                page.keyboard.press("Escape")
                preview.wait_for(state="hidden")

    def test_wrapper_adds_no_search_content_or_answer_identifiers(self):
        # Quarto already indexes answer text. Wrapping must not add new entries,
        # expose provenance strings, or change any indexed text from its output
        # for the exact original inner fences.
        rows = json.loads((self.root / "_site/search.json").read_text())
        def records(name):
            return [(r.get("section", ""), re.sub(r"\s+", " ", r["text"]).strip())
                    for r in rows if r["href"].split("#")[0] == name]
        wrapped, plain = records("article-fixture.html"), records("plain-fixture.html")
        self.assertTrue(wrapped)
        self.assertEqual(wrapped, plain)
        self.assertNotIn(MARKER, json.dumps(rows))
        self.assertFalse(any("callout-" in r["href"] for r in rows))

    def test_authored_controls_infobox_sidebar_and_no_js_unchanged(self):
        for name, selectors in (
            ("articles/hinge-loss.html", ("#properties .callout", "#worked-example .callout")),
            ("articles/hazard-rate.html", ("#check-yourself .callout:not(." + MARKER + " > .callout)",)),
        ):
            with self.subTest(page=name):
                page = self.page(name, 1024)
                nojs = self.page(name, 1024, java_script_enabled=False)
                for selector in selectors:
                    enhanced = page.locator(selector)
                    original = nojs.locator(selector)
                    self.assertGreater(enhanced.count(), 0)
                    self.assertEqual(enhanced.count(), original.count())
                    for index in range(enhanced.count()):
                        header = enhanced.nth(index).locator(":scope > .callout-header")
                        raw = original.nth(index).locator(":scope > .callout-header")
                        self.assertEqual(header.evaluate("el => el.outerHTML"), raw.evaluate("el => el.outerHTML"))
                        self.assertEqual(header.get_attribute("data-bs-toggle"), "collapse")
                        self.assertEqual(header.locator("button").count(), 0)
                self.assertEqual(page.locator(".infobox-toggle").count(), 1)
                self.assertEqual(page.locator(".infobox-toggle .statwiki-answer-toggle").count(), 0)
                self.assertEqual(page.locator("#quarto-sidebar .statwiki-answer-toggle").count(), 0)
                self.assertEqual(nojs.locator(".statwiki-answer-toggle").count(), 0)
                self.assertEqual(nojs.locator(".callout-collapse.show").count(), 0)
        nojs = self.page("questions/depth-hinge-loss-q1.html", java_script_enabled=False)
        self.assertFalse(nojs.locator("#worked-answer .callout-collapse").is_visible())
        self.assertEqual(nojs.locator("#worked-answer > .callout-header").get_attribute("data-bs-toggle"), "collapse")


if __name__ == "__main__":
    unittest.main()
