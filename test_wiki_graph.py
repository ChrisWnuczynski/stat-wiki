"""Tests for the page graph. They do not render the site."""

from __future__ import annotations

import copy
import collections
import json
import re
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

import build_wiki
import wiki_graph

CHAPTER = build_wiki.CHAPTER_CODES["G1"]
ANCHOR = "s-the-three-components-of-a-glm"
HEADING = "The three components of a GLM"
PRACTICE_LABEL = "question:practice-rayleigh-conjugate-prior"


def _prose_word_count(text: str) -> int:
    # Require an HTML tag name: R output also contains '<-' and '< 2e-16'.
    return len(re.findall(r"\b[\w-]+\b", re.sub(r"</?[A-Za-z][^>]*>", " ", text)))


def _world(root: Path, answer_body: str = "Because.") -> dict:
    notes = root / "notes"
    questions = root / "questions"
    articles = root / "articles"
    figures = root / "figures"
    reference = root / "reference"
    for path in (notes, questions, articles, figures, reference):
        path.mkdir(parents=True, exist_ok=True)
    chapter = notes / CHAPTER
    chapter.write_text(
        f"# GLMs\n\n## {HEADING} {{#{ANCHOR}}}\n\nThree parts.\n\n"
        "::: {#def-glm .definition}\n\nA glm.\n:::\n\n"
        "::: {#exm-a .example}\n\nSame.\n:::\n\n"
        "::: {#exm-b .example}\n\nSame.\n:::\n",
        encoding="utf-8",
    )
    asked = questions / "ex-a.qmd"
    asked.write_text(
        'Ask.\n\n:::::::: {#worked-answer .callout-tip}\nBecause.\n::::::::\n',
        encoding="utf-8",
    )
    practice = questions / "q-01.qmd"
    practice.write_text(
        'Practice.\n\n:::::::: {#worked-answer .callout-tip}\nWorked.\n::::::::\n',
        encoding="utf-8",
    )
    article = articles / "glm.qmd"
    article.write_text("# GLM\n", encoding="utf-8")
    (figures / "plot.png").write_bytes(b"png")
    (reference / "distributions.qmd").write_text(
        '---\ntitle: "Common distributions"\n---\n\n### Binomial {#dist-binomial}\n\n',
        encoding="utf-8",
    )
    return {
        "notes": {
            CHAPTER: {
                "path": chapter,
                "title": "Introduction to GLMs",
                "kind": "notes",
                "prose": "Chapter prose.",
            }
        },
        "questions": [
            {
                "group": "book",
                "id": "ex-a",
                "title": "A question",
                "body": "Ask.",
                "path": asked,
                "chapter_file": CHAPTER,
                "topic": CHAPTER,
                "answer_id": "sol-a",
            },
            {
                "group": "practice",
                "n": 1,
                "id": "q-01",
                "label": PRACTICE_LABEL,
                "title": "Q1. Rayleigh conjugate prior",
                "body": "Practice.",
                "path": practice,
                "topic": CHAPTER,
                "answer_id": "a-01",
            },
        ],
        "answers": [
            {
                "group": "book",
                "id": "sol-a",
                "title": "Answer",
                "body": answer_body,
                "question_id": "ex-a",
            },
            {"group": "practice", "id": "a-01", "title": "Answer 1", "body": "Worked."},
        ],
        "articles": {
            "glm": {
                "slug": "glm",
                "path": article,
                "term": "GLM",
                "box": {
                    "chapter": chapter,
                    "chapter_title": "Introduction to GLMs",
                    "anchor": "def-glm",
                    "kind": "definition",
                    "lines": ["A glm."],
                    "snippet": "A glm.",
                },
                "card": {"name": "Binomial", "anchor": "dist-binomial", "body": "n and p"},
                "aliases": [],
            }
        },
        "glossary": [
            {"term": "GLM", "kind": "definition", "page": chapter, "anchor": "def-glm", "snippet": "A glm."},
            {"term": HEADING, "kind": "section", "page": chapter, "anchor": ANCHOR, "snippet": ""},
        ],
        "heading_anchors": {
            (CHAPTER, "def-glm"): "def-glm",
            (CHAPTER, "GLM"): "def-glm",
            (CHAPTER, HEADING): ANCHOR,
        },
        "examples": {
            "exm-a": {"title": "One", "lines": ["Same."], "chapter": chapter, "chapter_title": "Introduction to GLMs"},
            "exm-b": {"title": "Two", "lines": ["Same."], "chapter": chapter, "chapter_title": "Introduction to GLMs"},
        },
        "figures": {
            "plot.png": {
                "caption": "A plot",
                "chapter": chapter,
                "chapter_title": "Introduction to GLMs",
                "id": "fig-plot",
            }
        },
        "sections": {(CHAPTER, ANCHOR): "Three parts."},
        "root": root,
        "terms": [
            (r"link functions?", "G1", HEADING, None),
            (r"GLMs?", "G1", "def-glm", None),
        ],
    }


class WikiGraphTests(unittest.TestCase):
    def _document(self, answer_body: str = "Because.") -> tuple[Path, dict]:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        kwargs = _world(root, answer_body)
        return root, wiki_graph.build_document(**kwargs)

    def test_practice_question_id_is_its_label(self) -> None:
        question = {"group": "practice", "n": 1, "id": "q-01", "label": PRACTICE_LABEL}
        self.assertEqual(wiki_graph.question_graph_id(question), PRACTICE_LABEL)
        self.assertNotEqual(wiki_graph.question_graph_id(question), "q-01")
        self.assertNotEqual(wiki_graph.question_graph_id(question), "question:q-01")
        self.assertEqual(wiki_graph.question_graph_id({"group": "book", "id": "ex-a"}), "question:ex-a")

        self.assertEqual(len(build_wiki.PRACTICE_TOPICS), 59)
        self.assertEqual(len(build_wiki.CONCEPT_TOPICS), 50)
        concept, _concept_answers, exam, _exam_answers = build_wiki.load_practice()
        self.assertEqual(len(exam), 59)
        self.assertEqual(len(concept), 50)
        practice_labels = [item["label"] for item in exam]
        concept_labels = [item["label"] for item in concept]
        self.assertEqual(len(set(practice_labels)), 59)
        self.assertEqual(len(set(concept_labels)), 50)
        self.assertEqual(len(set(practice_labels) & set(concept_labels)), 0)
        for number, label in enumerate(practice_labels, 1):
            built = {"group": "practice", "id": f"q-{number:02d}", "label": label, "n": number}
            self.assertEqual(wiki_graph.question_graph_id(built), label)
            self.assertNotIn(f"q-{number:02d}", label)
        for number, label in enumerate(concept_labels, 1):
            built = {"group": "concepts", "id": f"c-{number:02d}", "label": label, "n": number}
            self.assertEqual(wiki_graph.question_graph_id(built), label)
            self.assertNotIn(f"c-{number:02d}", label)
        for label in practice_labels + concept_labels:
            self.assertNotIn("GitHub", label)
            self.assertNotIn("github", label)
            self.assertNotRegex(label, r"STAT\d")

    def test_deleted_box_or_example_fails_and_deleted_section_warns(self) -> None:
        kept = {"id": "definition:def-keep", "kind": "definition", "text": "keep"}
        warnings = wiki_graph.check_identity(
            [kept, {"id": "section:ch:s-old", "kind": "section", "text": "old prose"}],
            [kept],
            {},
        )
        self.assertEqual(warnings, ["section:ch:s-old"])

        with self.assertRaises(SystemExit) as missing_box:
            wiki_graph.check_identity([{"id": "definition:def-old", "kind": "definition", "text": "A mean."}], [], {})
        self.assertIn("definition:def-old", str(missing_box.exception))

        with self.assertRaises(SystemExit) as missing_example:
            wiki_graph.check_identity([{"id": "example:exm-old", "kind": "example", "text": "Worked."}], [], {})
        self.assertIn("example:exm-old", str(missing_example.exception))

    def test_alias_rename_near_match_and_dangling_alias(self) -> None:
        previous = [{"id": "definition:def-old", "kind": "definition", "text": "A mean is a centre."}]
        current = [{"id": "definition:def-new", "kind": "definition", "text": "A mean is a centre."}]
        self.assertEqual(
            wiki_graph.check_identity(previous, current, {"definition:def-old": "definition:def-new"}),
            [],
        )

        with self.assertRaises(SystemExit) as caught:
            wiki_graph.check_identity(previous, current, {})
        self.assertIn("definition:def-new", str(caught.exception))
        self.assertIn("near-identical", str(caught.exception))

        with self.assertRaises(SystemExit) as dangling:
            wiki_graph.check_identity(previous, current, {"definition:def-old": "definition:missing"})
        self.assertIn("definition:missing", str(dangling.exception))
        self.assertIn("not emitted", str(dangling.exception))

    def test_registry_check_does_not_write_but_update_does(self) -> None:
        _root, document = self._document()
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        wiki = Path(tmp.name) / "wiki.json"
        registry = Path(tmp.name) / "graph" / "ids.json"
        self.assertEqual(wiki_graph.save_graph(document, wiki_path=wiki, registry_path=registry, update_ids=True), [])
        raw = registry.read_bytes()
        saved = json.loads(raw)
        self.assertEqual(set(saved), {"aliases", "ids"})
        self.assertTrue(saved["ids"])
        self.assertTrue(all(isinstance(kind, str) for kind in saved["ids"].values()))
        self.assertNotIn("fingerprint", saved["ids"].values())
        blob = raw.decode("utf-8")
        self.assertNotIn("fingerprint", blob)
        self.assertNotIn('"text"', blob)
        self.assertNotIn('"url"', blob)

        self.assertEqual(wiki_graph.save_graph(document, wiki_path=wiki, registry_path=registry, update_ids=False), [])
        self.assertEqual(registry.read_bytes(), raw)

        removed = copy.deepcopy(document)
        removed["entries"] = [item for item in removed["entries"] if item["id"] != "example:exm-a"]
        with self.assertRaises(SystemExit):
            wiki_graph.save_graph(removed, wiki_path=wiki, registry_path=registry, update_ids=False)
        self.assertEqual(registry.read_bytes(), raw)

        added = copy.deepcopy(document)
        added["entries"] = list(added["entries"]) + [
            {
                "id": "figure:fig-extra",
                "kind": "figure",
                "title": "Extra",
                "text": "Extra",
                "url": "/figures/plot.png",
                "fingerprint": "abc",
            }
        ]
        wiki_graph.save_graph(added, wiki_path=wiki, registry_path=registry, update_ids=True)
        self.assertNotEqual(registry.read_bytes(), raw)
        self.assertIn("figure:fig-extra", json.loads(registry.read_text(encoding="utf-8"))["ids"])

    def test_identical_bodies_keep_both_anchors(self) -> None:
        _root, document = self._document()
        by_id = {item["id"]: item for item in document["entries"]}
        kept, copied = by_id["example:exm-a"], by_id["example:exm-b"]
        self.assertEqual(kept["text"], "Same.")
        self.assertNotIn("text", copied)
        self.assertEqual(copied["copy_of"], kept["id"])
        self.assertNotEqual(kept["id"], copied["id"])
        self.assertTrue(kept["url"].endswith("#exm-a"))
        self.assertTrue(copied["url"].endswith("#exm-b"))
        self.assertTrue(any(edge["from"] == copied["id"] for edge in document["edges"]))

    def test_edited_answer_keeps_id_and_worked_answer_url(self) -> None:
        _root, first = self._document("Because.")
        _root, second = self._document("Because the mean moved.")
        before = next(item for item in first["entries"] if item["kind"] == "answer" and item["id"].endswith("question:ex-a"))
        after = next(item for item in second["entries"] if item["kind"] == "answer" and item["id"].endswith("question:ex-a"))
        self.assertEqual(before["id"], "answer:question:ex-a")
        self.assertEqual(after["id"], before["id"])
        self.assertEqual(after["url"], before["url"])
        self.assertTrue(after["url"].endswith("/questions/ex-a.html#worked-answer"))
        self.assertNotEqual(before["fingerprint"], after["fingerprint"])
        self.assertEqual(first["aliases"]["answer:sol-a"], before["id"])

    def test_duplicate_example_anchor_raises(self) -> None:
        saved = dict(build_wiki.BOOK_EXAMPLE_BOXES)
        build_wiki.BOOK_EXAMPLE_BOXES.clear()
        try:
            note = {"path": Path("notes/t.qmd"), "title": "T"}
            body = (
                "::: {#exm-dup .example}\n## Title\nAlpha\n:::\n\n"
                "::: {#exm-dup .example}\n## Title\nBeta\n:::\n"
            )
            with self.assertRaises(SystemExit) as caught:
                build_wiki.index_chapter(note, "Part", body)
            self.assertIn("exm-dup", str(caught.exception))
            self.assertEqual(build_wiki.BOOK_EXAMPLE_BOXES["exm-dup"]["lines"], ["Alpha"])
        finally:
            build_wiki.BOOK_EXAMPLE_BOXES.clear()
            build_wiki.BOOK_EXAMPLE_BOXES.update(saved)

    def test_urls_question_pages_and_terms_heading(self) -> None:
        root, document = self._document()
        ids = {item["id"] for item in document["entries"]}
        self.assertEqual(document["version"], 2)
        self.assertEqual([item["id"] for item in document["entries"]], sorted(ids))
        carried = []
        for item in document["entries"]:
            self.assertTrue({"id", "kind", "title", "url", "fingerprint"} <= set(item), item)
            self.assertFalse(".qmd" in item["url"], item["url"])
            if "copy_of" in item:
                self.assertNotIn("text", item)
                self.assertIn(item["copy_of"], ids)
            else:
                self.assertIn("text", item)
                if item["text"]:
                    carried.append(item["text"])
            url = item["url"]
            self.assertTrue(url.startswith("/"), url)
            path, _, fragment = url.partition("#")
            file = root / path.lstrip("/")
            if path.endswith(".html"):
                file = file.with_suffix(".qmd")
            self.assertTrue(file.is_file(), url)
            if fragment:
                self.assertRegex(file.read_text(encoding="utf-8"), rf"#{fragment}(?![A-Za-z0-9_-])")
        self.assertEqual(len(carried), len(set(carried)))
        question_urls = {item["url"] for item in document["entries"] if item["kind"] == "question"}
        self.assertIn("/questions/ex-a.html", question_urls)
        self.assertIn("/questions/q-01.html", question_urls)
        target = f"section:{Path(CHAPTER).stem}:{ANCHOR}"
        self.assertIn(target, ids)
        self.assertTrue(any(edge["type"] == "defines" and edge["to"] == target for edge in document["edges"]))
        self.assertTrue(all(edge["from"] in ids and edge["to"] in ids for edge in document["edges"]))
        practice = next(item for item in document["entries"] if item["id"] == PRACTICE_LABEL)
        self.assertEqual(practice["url"], "/questions/q-01.html")
        figure = next(item for item in document["entries"] if item["kind"] == "figure")
        self.assertEqual(figure["url"], "/figures/plot.png")
        for item in document["entries"]:
            self.assertNotIn("GitHub", item["id"])
            self.assertNotRegex(item["id"], r"STAT\d")
            self.assertNotRegex(item["url"], r"STAT\d")

    def test_chat_source_keeps_one_cleaned_copy(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        kwargs = _world(root)
        shared = (
            "See [joint density](../articles/x.qmd){.term}.\n\n"
            "![A cloud](../figures/plot.png){width=80%}\n\n"
            "A note.[^n]\n\n"
            "[^n]: The note text.\n\n"
            "::: {.callout}\n"
            "Inside $\\vect{\\beta}$.\n"
            ":::\n"
        )
        kwargs["notes"][CHAPTER]["title"] = r"Means \given data"
        kwargs["notes"][CHAPTER]["prose"] = (
            "Opening $\\xvec\\given\\theta$.\n\n"
            "## Later {#later}\n\n"
            "Section body that must stay out of the chapter.\n"
        )
        kwargs["sections"][(CHAPTER, ANCHOR)] = shared
        article = kwargs["articles"]["glm"]
        article["box"]["lines"] = [shared]
        article["card"] = None
        document = wiki_graph.build_document(**kwargs)
        by_id = {item["id"]: item for item in document["entries"]}
        section_id = f"section:{Path(CHAPTER).stem}:{ANCHOR}"
        section = by_id[section_id]
        chapter = by_id[f"chapter:{Path(CHAPTER).stem}"]
        self.assertEqual(chapter["title"], r"Means \mid data")
        self.assertIn(r"${\boldsymbol{x}}\mid\theta$", chapter["text"])
        self.assertNotIn("Section body that must stay out of the chapter.", chapter["text"])
        self.assertNotIn(section["text"], chapter["text"])
        self.assertNotIn("text", by_id["article:glm"])
        self.assertEqual(by_id["article:glm"]["copy_of"], section_id)
        self.assertNotIn("text", by_id["definition:def-glm"])
        self.assertEqual(by_id["definition:def-glm"]["copy_of"], section_id)
        self.assertIn("joint density", section["text"])
        self.assertIn("A cloud", section["text"])
        self.assertIn("[The note text.]", section["text"])
        self.assertIn("Inside", section["text"])
        self.assertIn(r"${\boldsymbol{\beta}}$", section["text"])
        self.assertNotRegex(section["text"], r"^:::")
        self.assertNotRegex(section["text"], r"\{[.#][\w-]")
        self.assertNotRegex(section["text"], r"\]\(")
        self.assertNotRegex(section["text"], r"!\[")
        for name in list(build_wiki.ZERO_ARG) + list(build_wiki.ONE_ARG):
            self.assertNotRegex(section["text"], rf"\\{name}(?![A-Za-z])")
            self.assertNotRegex(chapter["title"], rf"\\{name}(?![A-Za-z])")
        code = "```\n\\xvec\n:::\n![keep](x)\n```"
        self.assertEqual(wiki_graph.strip_markup(code), code.strip())
        self.assertEqual(
            wiki_graph.strip_markup("[joint density](../articles/x.qmd){.term}"),
            "joint density",
        )
        self.assertEqual(wiki_graph.strip_markup("A note.[^n]\n\n[^n]: The note text."), "A note. [The note text.]")
        self.assertEqual(wiki_graph.strip_markup("[^n]: The note text."), "The note text.")
        self.assertEqual(
            wiki_graph.strip_markup("See.[^n]\n\n```\ncode\n```\n\n[^n]: The note text."),
            "See. [The note text.]\n\n```\ncode\n```",
        )
        with self.assertRaises(SystemExit) as caught:
            wiki_graph._check_urls([{"url": "/questions/ex-a.qmd"}], root)
        self.assertIn(".qmd", str(caught.exception))

    def test_dashes_follow_pandoc_outside_maths_and_code(self) -> None:
        cases = {
            "The Beta--Binomial model": "The Beta\u2013Binomial model",
            "Normal--inverse-$\\chi^2$ conjugacy": "Normal\u2013inverse-$\\chi^2$ conjugacy",
            "pages 1--3 --- see": "pages 1\u20133 \u2014 see",
            "maths $a--b$ stays": "maths $a--b$ stays",
            "code `x--y` stays": "code `x--y` stays",
            "| --- | --- |": "| --- | --- |",
            "---": "---",
        }
        for raw, expected in cases.items():
            self.assertEqual(wiki_graph.smart_dashes(raw), expected, raw)
        table = "| a | b |\n| --- | --- |\n| 1--2 | x |"
        self.assertEqual(wiki_graph.strip_markup(table), "| a | b |\n| --- | --- |\n| 1\u20132 | x |")

    def test_cleaning_leaves_maths_and_drops_image_attributes(self) -> None:
        sums = (r"$\sum_{i=1}^n x_i$", r"$\sum_{y_i=f_m(x_i)} c_i$")
        for sample in sums:
            cleaned = build_wiki.expand_macros(wiki_graph.strip_markup(sample)).strip()
            self.assertEqual(cleaned, sample)
            self.assertEqual(wiki_graph.math_spans(cleaned), wiki_graph.math_spans(build_wiki.expand_macros(sample)))
        self.assertEqual(wiki_graph.strip_markup("![A plot](figures/x.png){width=50%}"), "A plot")
        caption = r"![A $\sum_{i=1}^n$ plot](figures/x.png){width=50%}"
        self.assertEqual(wiki_graph.strip_markup(caption), r"A $\sum_{i=1}^n$ plot")
        align = "\\begin{align*}\n&=e^{-\\alpha}\\sum_{y_i=f_m(x_i)}c_{m,i}\n\\end{align*}"
        self.assertEqual(wiki_graph.strip_markup(align), align)
        split = "$X_t=\\sum_{j=1}^p a_j+$\n\\sum_{k=1}^q b_k$"
        cleaned_split = wiki_graph.strip_markup(split)
        self.assertIn(r"\sum_{j=1}^p", cleaned_split)
        self.assertIn(r"\sum_{k=1}^q", cleaned_split)
        self.assertNotIn("_^", cleaned_split)
        self.assertNotIn("^_", cleaned_split)
        self.assertEqual(wiki_graph.strip_markup("## Title {#id}"), "## Title")
        self.assertEqual(wiki_graph.strip_markup("$$ {#eq-one}"), "$$")
        self.assertNotIn("{#", wiki_graph.strip_markup("[]{#sol-one} **[Name](#ex-one).**"))

        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        kwargs = _world(root)
        kwargs["notes"][CHAPTER]["prose"] = sums[0] + "\n\n## Later\n\nKept out."
        kwargs["sections"][(CHAPTER, ANCHOR)] = sums[1] + "\n\n![A plot](figures/x.png){width=50%}"
        kwargs["articles"]["glm"]["card"] = None
        kwargs["answers"][0]["body"] = align
        document = wiki_graph.build_document(**kwargs)
        for item in document["entries"]:
            body = item.get("text") or ""
            self.assertNotIn("_^", body, item["id"])
            self.assertNotIn("^_", body, item["id"])
            if body:
                self.assertNotRegex(body, r"\{[.#][\w-]")
        by_id = {item["id"]: item for item in document["entries"]}
        self.assertEqual(by_id[f"chapter:{Path(CHAPTER).stem}"]["text"], sums[0])
        self.assertEqual(by_id[f"section:{Path(CHAPTER).stem}:{ANCHOR}"]["text"], sums[1] + "\n\nA plot")
        self.assertIn(r"\sum_{y_i=f_m(x_i)}", by_id["answer:question:ex-a"]["text"])
        self.assertEqual(by_id["definition:def-glm"]["text"], "A glm.")
        self.assertNotIn("text", by_id["article:glm"])
        self.assertEqual(by_id["article:glm"]["copy_of"], "definition:def-glm")

    def test_retired_heading_page_aliases_its_section(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        kwargs = _world(Path(tmp.name))
        document = wiki_graph.build_document(**kwargs, retired={"old-step": (CHAPTER, ANCHOR)})
        section = f"section:{Path(CHAPTER).stem}:{ANCHOR}"
        self.assertEqual(document["aliases"]["article:old-step"], section)
        previous = [{"id": item["id"], "kind": item["kind"]} for item in document["entries"]]
        previous.append({"id": "article:old-step", "kind": "article"})
        self.assertEqual(wiki_graph.check_identity(previous, document["entries"], document["aliases"]), [])
        with self.assertRaises(SystemExit) as caught:
            wiki_graph.check_identity(previous, document["entries"], {})
        self.assertIn("vanished article article:old-step", str(caught.exception))

        with self.assertRaises(SystemExit) as missing:
            wiki_graph.build_document(**_world(Path(tmp.name)), retired={"old-step": (CHAPTER, "s-gone")})
        self.assertIn("not emitted", str(missing.exception))

        merged_doc = wiki_graph.build_document(**_world(Path(tmp.name)), merged={"glm-duplicate": "glm"})
        self.assertEqual(merged_doc["aliases"]["article:glm-duplicate"], "article:glm")
        prev_with_dup = [{"id": item["id"], "kind": item["kind"]} for item in merged_doc["entries"]]
        prev_with_dup.append({"id": "article:glm-duplicate", "kind": "article"})
        self.assertEqual(wiki_graph.check_identity(prev_with_dup, merged_doc["entries"], merged_doc["aliases"]), [])

    def test_retired_page_redirects_to_its_heading(self) -> None:
        import canonical_redirects

        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        chapter = root / "notes" / CHAPTER
        saved = (build_wiki.ARTICLE_DIR, dict(build_wiki.RETIRED), dict(build_wiki.PAGE_TITLES))
        try:
            build_wiki.ARTICLE_DIR = root / "articles"
            build_wiki.ARTICLE_DIR.mkdir()
            build_wiki.RETIRED.clear()
            build_wiki.RETIRED["old-step"] = (chapter, ANCHOR)
            build_wiki.PAGE_TITLES[chapter] = "GLMs & links"
            build_wiki.write_retired_pages()
            page = build_wiki.ARTICLE_DIR / "old-step.html"
            text = page.read_text(encoding="utf-8")
            target = f"../notes/{Path(CHAPTER).stem}.html#{ANCHOR}"
            self.assertIn(f'var redirects = {{"": "{target}"}};', text)
            self.assertIn(f'url={target}"', text)
            self.assertIn("GLMs &amp; links", text)
            self.assertIn("<title>Redirect</title>", text)  # the post-render steps know it by this

            site = root / "_site"
            (site / "articles").mkdir(parents=True)
            (site / "notes").mkdir()
            (site / "notes" / f"{Path(CHAPTER).stem}.html").write_text("<html></html>", encoding="utf-8")
            (site / "articles" / "old-step.html").write_text(text, encoding="utf-8")
            match = canonical_redirects.REDIRECTS.search(text)
            saved_site = canonical_redirects.SITE_DIR
            canonical_redirects.SITE_DIR = site
            try:
                href = canonical_redirects.canonical_for(site / "articles" / "old-step.html", match.group(1))
            finally:
                canonical_redirects.SITE_DIR = saved_site
            self.assertEqual(href, f"https://www.statwiki.io/notes/{Path(CHAPTER).stem}.html")

            build_wiki.RETIRED["glm"] = (chapter, ANCHOR)
            build_wiki.ARTICLES["glm"] = {"slug": "glm"}
            try:
                with self.assertRaises(SystemExit) as clash:
                    build_wiki.write_retired_pages()
                self.assertIn("glm", str(clash.exception))
            finally:
                del build_wiki.ARTICLES["glm"]
        finally:
            build_wiki.ARTICLE_DIR = saved[0]
            build_wiki.RETIRED.clear()
            build_wiki.RETIRED.update(saved[1])
            build_wiki.PAGE_TITLES.clear()
            build_wiki.PAGE_TITLES.update(saved[2])

    def test_naming_excerpt_finds_the_paragraph_that_names_a_topic(self) -> None:
        prose = (
            "Read the map of the data first.\n\n"
            "The [variance function](../articles/variance-function.qmd){.term} sets the spread:\n\n"
            "$$\nV(\\mu)=\\mu\n$$\n\n"
            "where $\\mu$ is the mean.\n\n"
            "The MAP estimate is the mode."
        )
        self.assertEqual(
            build_wiki.naming_excerpt(prose, ["Variance function"]),
            "The [variance function](../articles/variance-function.qmd){.term} sets the spread:\n\n"
            "$$\nV(\\mu)=\\mu\n$$\n\nwhere $\\mu$ is the mean.",
        )
        # An acronym matches in capitals only, so "map" is not MAP.
        self.assertEqual(build_wiki.naming_excerpt(prose, ["MAP estimate", "MAP"]), "The MAP estimate is the mode.")
        self.assertIsNone(build_wiki.naming_excerpt(prose, ["Posterior median"]))

        # A phrase inside a display equation or its lowercase continuation
        # keeps the whole grammatical paragraph, never a mid-sentence tail or a
        # lone box heading.
        boxed = (
            "::: {#def-summaries .definition}\n"
            "## Posterior point summaries\n\n"
            "For a scalar parameter, common summaries include\n\n"
            "$$\n\\widehat\\theta_{\\mathrm{MAP}}=\\arg\\max_\\theta p(\\theta\\mid x),\n$$ {#eq-map}\n\n"
            "the posterior median, and quantiles.\n\n"
            "[Article: Posterior point summaries →](posterior-point-summaries.qmd){.box-article}\n"
            ":::\n"
        )
        whole = (
            "For a scalar parameter, common summaries include\n\n"
            "$$\n\\widehat\\theta_{\\mathrm{MAP}}=\\arg\\max_\\theta p(\\theta\\mid x),\n$$ {#eq-map}\n\n"
            "the posterior median, and quantiles."
        )
        self.assertEqual(build_wiki.naming_excerpt(boxed, ["Posterior median"]), whole)
        self.assertEqual(build_wiki.naming_excerpt(boxed, ["MAP"]), whole)
        self.assertEqual(build_wiki.naming_excerpt(boxed, ["Posterior point summaries"]), whole)

    def test_built_text_rejects_broken_subscripts(self) -> None:
        entry = {
            "id": "definition:def-broken",
            "kind": "definition",
            "title": "Broken",
            "text": r"\sum_^n",
            "url": "/notes/x.html",
            "fingerprint": "abc",
        }
        with self.assertRaises(SystemExit) as caught:
            wiki_graph._check_chat_source([entry], [])
        self.assertIn("broken maths", str(caught.exception))
        self.assertIn(entry["id"], str(caught.exception))

    def test_alias_redirect_stubs_and_404_page(self) -> None:
        import canonical_redirects

        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        (root / "articles").mkdir()
        (root / "notes").mkdir()
        (root / "articles" / "expectation.qmd").write_text("---\ntitle: \"Expectation\"\n---\n", encoding="utf-8")
        (root / "notes" / "sl-03-principal-components.qmd").write_text("---\ntitle: \"PCA\"\n---\n", encoding="utf-8")

        saved = (
            build_wiki.WIKI,
            build_wiki.ARTICLE_DIR,
            dict(build_wiki.ARTICLES),
            dict(build_wiki.RETIRED),
            dict(build_wiki.SEARCH_ALIASES),
            dict(build_wiki.PAGE_TITLES),
        )
        try:
            build_wiki.WIKI = root
            build_wiki.ARTICLE_DIR = root / "articles"
            build_wiki.ARTICLES.clear()
            build_wiki.ARTICLES["expectation"] = {"slug": "expectation"}
            build_wiki.RETIRED.clear()
            build_wiki.SEARCH_ALIASES.clear()
            build_wiki.SEARCH_ALIASES["expected-value"] = ("articles/expectation.html", "Expected value")
            build_wiki.SEARCH_ALIASES["pca"] = ("notes/sl-03-principal-components.html", "PCA")
            build_wiki.SEARCH_ALIASES["expectation"] = ("articles/expectation.html", "Expectation")
            build_wiki.PAGE_TITLES[root / "articles" / "expectation.qmd"] = "Expectation"
            build_wiki.PAGE_TITLES[root / "notes" / "sl-03-principal-components.qmd"] = "Principal component analysis"

            build_wiki.write_alias_redirect_pages()
            self.assertFalse((root / "articles" / "expectation.html").exists())
            ev_stub = (root / "articles" / "expected-value.html").read_text(encoding="utf-8")
            mean_stub = (root / "articles" / "mean.html").read_text(encoding="utf-8")
            pca_stub = (root / "articles" / "pca.html").read_text(encoding="utf-8")
            self.assertIn('var redirects = {"": "expectation.html"};', ev_stub)
            self.assertIn('var redirects = {"": "../search.html#q=Mean"};', mean_stub)
            self.assertIn('var redirects = {"": "../notes/sl-03-principal-components.html"};', pca_stub)

            site = root / "_site"
            (site / "articles").mkdir(parents=True)
            (site / "notes").mkdir()
            (site / "search.html").write_text("<html></html>", encoding="utf-8")
            (site / "articles" / "expectation.html").write_text("<html></html>", encoding="utf-8")
            (site / "notes" / "sl-03-principal-components.html").write_text("<html></html>", encoding="utf-8")
            (site / "articles" / "expected-value.html").write_text(ev_stub, encoding="utf-8")
            (site / "articles" / "mean.html").write_text(mean_stub, encoding="utf-8")
            (site / "articles" / "pca.html").write_text(pca_stub, encoding="utf-8")

            saved_site = canonical_redirects.SITE_DIR
            canonical_redirects.SITE_DIR = site
            try:
                m_ev = canonical_redirects.REDIRECTS.search(ev_stub)
                m_mean = canonical_redirects.REDIRECTS.search(mean_stub)
                m_pca = canonical_redirects.REDIRECTS.search(pca_stub)
                self.assertEqual(
                    canonical_redirects.canonical_for(site / "articles" / "expected-value.html", m_ev.group(1)),
                    "https://www.statwiki.io/articles/expectation.html",
                )
                self.assertEqual(
                    canonical_redirects.canonical_for(site / "articles" / "mean.html", m_mean.group(1)),
                    "https://www.statwiki.io/search.html",
                )
                self.assertEqual(
                    canonical_redirects.canonical_for(site / "articles" / "pca.html", m_pca.group(1)),
                    "https://www.statwiki.io/notes/sl-03-principal-components.html",
                )
            finally:
                canonical_redirects.SITE_DIR = saved_site
        finally:
            build_wiki.WIKI = saved[0]
            build_wiki.ARTICLE_DIR = saved[1]
            build_wiki.ARTICLES.clear()
            build_wiki.ARTICLES.update(saved[2])
            build_wiki.RETIRED.clear()
            build_wiki.RETIRED.update(saved[3])
            build_wiki.SEARCH_ALIASES.clear()
            build_wiki.SEARCH_ALIASES.update(saved[4])
            build_wiki.PAGE_TITLES.clear()
            build_wiki.PAGE_TITLES.update(saved[5])

        nf_page = Path(__file__).resolve().parent / "404.qmd"
        self.assertTrue(nf_page.is_file())
        nf_text = nf_page.read_text(encoding="utf-8")
        self.assertIn("search-aliases.json", nf_text)
        self.assertIn("resolveExactMatch", nf_text)
        self.assertNotRegex(nf_text, r"STAT\s*\d|github|GitHub")

    def test_doubled_xref_nouns_stripped_and_absent_from_sources(self) -> None:
        sample = (
            "Equation @eq-score collapses, Theorem @thm-wold holds, "
            "Figure @fig-plot shows it, and `Equation @eq-code` stays in code."
        )
        cleaned = build_wiki.strip_doubled_xref_nouns(sample)
        self.assertEqual(
            cleaned,
            "@eq-score collapses, @thm-wold holds, @fig-plot shows it, and `Equation @eq-code` stays in code.",
        )
        localized = build_wiki.localize_refs("See Figure @fig-a and Table @tbl-b.", "../notes/ch.qmd")
        self.assertEqual(localized, "See [Figure](../notes/ch.qmd#fig-a) and [Table](../notes/ch.qmd#tbl-b).")

        saved_eq = (dict(build_wiki.EQ_PAGES), dict(build_wiki.EQ_NUMBERS), dict(build_wiki.PAGE_TITLES))
        try:
            chapter = Path("notes/01-introduction-to-glms.qmd")
            article = Path("articles/score-function.qmd")
            build_wiki.EQ_PAGES["eq-score"] = chapter
            build_wiki.EQ_NUMBERS["eq-score"] = 11
            build_wiki.PAGE_TITLES[chapter] = "Introduction to GLMs"
            same_page = build_wiki.resolve_links("Equation @eq-score is nonlinear.", chapter)
            cross_page = build_wiki.resolve_links("Equation @eq-score is nonlinear.", article)
            self.assertEqual(same_page, "@eq-score is nonlinear.")
            self.assertEqual(cross_page, "[Equation (11) in *Introduction to GLMs*](../notes/01-introduction-to-glms.qmd#eq-score) is nonlinear.")
        finally:
            build_wiki.EQ_PAGES.clear()
            build_wiki.EQ_PAGES.update(saved_eq[0])
            build_wiki.EQ_NUMBERS.clear()
            build_wiki.EQ_NUMBERS.update(saved_eq[1])
            build_wiki.PAGE_TITLES.clear()
            build_wiki.PAGE_TITLES.update(saved_eq[2])

        offenders = []
        for src in sorted(build_wiki.SOURCES.rglob("*.qmd")):
            pieces = build_wiki.re.split(r"(```.*?```)", src.read_text(encoding="utf-8"), flags=build_wiki.re.S)
            for piece in pieces:
                if piece.startswith("```"):
                    continue
                for m in build_wiki.DOUBLED_XREF.finditer(piece):
                    offenders.append(f"{src.relative_to(build_wiki.WIKI)}: {m.group(0)!r}")
        self.assertEqual(offenders, [])

    def test_brisbane_footer_singular_counts_and_article_framing(self) -> None:
        from datetime import datetime, timezone

        # 2026-11-12 18:00 UTC is 2026-11-13 04:00 AEST in Australia/Brisbane.
        stamp = build_wiki.footer_text(datetime(2026, 11, 12, 18, 0, tzinfo=timezone.utc))
        self.assertIn("Last updated 13 November 2026", stamp)

        self.assertIn("1 question.", build_wiki.qcount_marker(1))
        self.assertIn("2 questions.", build_wiki.qcount_marker(2))

        framed_in_place = build_wiki.frame_article_lead(
            {"term": "Random variable", "box": {"kind": "definition"}},
            "A random variable is a function $X$ from the [sample space](sample-space.qmd){.term} $\\Omega$.\n\n",
        )
        self.assertIn("A **random variable** is a function", framed_in_place)

        framed_pvalue = build_wiki.frame_article_lead(
            {"term": "p-value", "box": {"kind": "definition"}},
            "The $p$-value of an observed [statistic](statistic.qmd){.term} $t$ is small.\n\n",
        )
        self.assertIn("**$p$-value**", framed_pvalue)

        framed_topic = build_wiki.frame_article_lead(
            {"term": "Median", "box": {"kind": "topic", "topic": {"links": ["medians?"]}}},
            "The middle value of the ordered sample.\n\n",
        )
        self.assertTrue(framed_topic.startswith("**Median.** The middle value"))

        # Synonym-first openings tie the synonym back to the canonical page title.
        framed_synonym = build_wiki.frame_article_lead(
            {"term": "Explanatory variable", "box": {"kind": "topic", "topic": {"links": ["covariates?"]}}},
            "A variable $x$ used to explain $y$; also called a **covariate**.\n\n",
        )
        self.assertTrue(framed_synonym.startswith("**Explanatory variable.** A variable $x$"))
        self.assertIn("**covariate**", framed_synonym)

        # Theorem/proposition/box openings without in-prose title receive canonical bold framing.
        framed_theorem = build_wiki.frame_article_lead(
            {"term": "Central limit theorem", "box": {"kind": "theorem"}},
            "If the $X_i$ are independent and identically distributed with mean $\\mu$ and variance $\\sigma^2$, then\n\n",
        )
        self.assertTrue(framed_theorem.startswith("**Central limit theorem.** If the $X_i$"))

        framed_display_eq = build_wiki.frame_article_lead(
            {"term": "Beta–Binomial conjugacy", "box": {"kind": "proposition"}},
            "$$\n\\theta\\mid x\\sim\\operatorname{Beta}(\\alpha+x,\\beta+n-x).\n$$\n\n",
        )
        self.assertTrue(framed_display_eq.startswith("**Beta–Binomial conjugacy.**\n\n$$"))

        # Disambiguation hatnotes appear only when two live pages share a term.
        saved = dict(build_wiki.ARTICLES)
        try:
            build_wiki.ARTICLES.clear()
            lone = {"slug": "kernel", "term": "Kernel", "path": Path("articles/kernel.qmd"), "box": None}
            other_word = {
                "slug": "kernel-density-estimator",
                "term": "Kernel density estimator",
                "path": Path("articles/kernel-density-estimator.qmd"),
                "box": None,
            }
            build_wiki.ARTICLES["kernel"] = lone
            build_wiki.ARTICLES["kernel-density-estimator"] = other_word
            self.assertEqual(build_wiki.disambiguation_note(lone), "")
            twin = {
                "slug": "normal-distribution-b",
                "term": "Normal distribution",
                "path": Path("articles/normal-distribution-b.qmd"),
                "box": {"chapter": Path("notes/sl-01.qmd"), "chapter_title": "Multivariate normal"},
            }
            canon = {
                "slug": "normal-distribution",
                "term": "Normal distribution",
                "path": Path("articles/normal-distribution.qmd"),
                "box": {"chapter": Path("notes/prob-02.qmd"), "chapter_title": "Random variables"},
            }
            build_wiki.ARTICLES["normal-distribution"] = canon
            build_wiki.ARTICLES["normal-distribution-b"] = twin
            note = build_wiki.disambiguation_note(canon)
            self.assertIn("This term is also on another page", note)
            self.assertIn("normal-distribution-b.qmd", note)
            self.assertIn("Multivariate normal", note)
        finally:
            build_wiki.ARTICLES.clear()
            build_wiki.ARTICLES.update(saved)

    def test_site_wide_figure_and_svg_accessibility(self) -> None:
        import figure_alts
        import re

        root = build_wiki.WIKI
        figures_dir = root / "figures"
        if not figures_dir.is_dir():
            self.skipTest("Generated wiki directories are not built yet")

        png_files = sorted(p.name for p in figures_dir.glob("*.png") if not p.name.endswith("-full.png"))
        self.assertEqual(len(png_files), 88)
        self.assertEqual(set(png_files), set(figure_alts.FIGURE_ALTS))

        banned_generic = {"diagram", "plot", "figure", "chart", "image", "graph", "illustration"}
        for name, alt in figure_alts.FIGURE_ALTS.items():
            stem = Path(name).stem
            self.assertGreaterEqual(len(alt.strip()), 60, f"Alt text too brief for {name}: {alt!r}")
            self.assertNotIn(alt.strip().lower(), banned_generic | {stem.lower(), name.lower()})
            self.assertNotRegex(alt, r"STAT\s*\d|\bgithub\b", f"Banned token in {name} alt")

        # Every Markdown image across generated and authored .qmd files must carry meaningful fig-alt.
        md_img = re.compile(r"!\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)\)(\{[^}]*\})?")
        checked_images = 0
        for folder in ("notes", "articles", "questions", "reference", "files", "labs"):
            pdir = root / folder
            if not pdir.is_dir():
                continue
            for qmd in sorted(pdir.rglob("*.qmd")):
                if qmd.name.startswith("_"):
                    continue
                for match in md_img.finditer(qmd.read_text(encoding="utf-8")):
                    _cap, src, attrs = match.groups()
                    checked_images += 1
                    m_alt = re.search(r'fig-alt="((?:\\.|[^"\\])*)"', attrs or "")
                    self.assertIsNotNone(m_alt, f"Missing fig-alt on {src} in {qmd.relative_to(root)}")
                    alt_val = m_alt.group(1).strip()
                    self.assertGreaterEqual(len(alt_val), 60, f"Short fig-alt on {src} in {qmd.relative_to(root)}")
                    self.assertNotEqual(alt_val.lower(), Path(src).stem.lower())
        self.assertGreaterEqual(checked_images, 470)

        # Inline SVG roadmap on overview.qmd carries role="img", <title>, <desc>, and accessible box links.
        overview_text = (root / "overview.qmd").read_text(encoding="utf-8")
        svg_match = re.search(r'<svg\s+[^>]*class="overview-roadmap"[^>]*>(.*?)</svg>', overview_text, re.S)
        self.assertIsNotNone(svg_match)
        svg_tag = overview_text[svg_match.start() : overview_text.find(">", svg_match.start()) + 1]
        svg_inner = svg_match.group(1)
        self.assertIn('role="img"', svg_tag)
        self.assertIn("aria-labelledby=", svg_tag)
        self.assertIn("<title", svg_inner)
        self.assertIn("<desc", svg_inner)
        box_links = re.findall(r'<a\s+([^>]+)>', svg_inner)
        self.assertEqual(len(box_links), 8)
        for attrs in box_links:
            m_href = re.search(r'href="#([\w-]+)"', attrs)
            self.assertIsNotNone(m_href, attrs)
            anchor = m_href.group(1)
            self.assertIn('class="no-external"', attrs)
            self.assertIn('target="_self"', attrs)
            self.assertIn("aria-label=", attrs)
            self.assertRegex(overview_text, rf"\{{#{re.escape(anchor)}\}}", f"Missing heading #{anchor} in overview.qmd")

        # Interactive SVG charts carry role="img", aria-label, and <title>, while decorative icons carry aria-hidden="true".
        svg_chart_js = (root / "labs" / "svg-chart.js").read_text(encoding="utf-8")
        self.assertIn('svg.setAttribute("role", "img")', svg_chart_js)
        self.assertIn('svg.setAttribute("aria-label"', svg_chart_js)
        self.assertIn('createElementNS(SVG, "title")', svg_chart_js)
        kde_qmd = (root / "labs" / "_kde-figure.qmd").read_text(encoding="utf-8")
        self.assertIn('chart.setAttribute("role", "img")', kde_qmd)
        self.assertIn('createElementNS("http://www.w3.org/2000/svg", "title")', kde_qmd)
        loader_ts = (root / "ask" / "widget" / "src" / "loader.ts").read_text(encoding="utf-8")
        self.assertIn('aria-hidden="true"', loader_ts)
        lab_chrome_js = (root / "labs" / "lab-chrome.js").read_text(encoding="utf-8")
        self.assertIn('mark.setAttribute("aria-hidden", "true")', lab_chrome_js)

    def test_all_concept_leads_homepage_counts_navboxes_cite_and_backlinks(self) -> None:
        import re

        root = build_wiki.WIKI
        articles_dir = root / "articles"
        notes_dir = root / "notes"
        home_path = root / "index.qmd"
        if not articles_dir.is_dir() or not home_path.is_file():
            self.skipTest("Generated wiki directories are not built yet")

        article_files = sorted(articles_dir.glob("*.qmd"))
        self.assertEqual(len(article_files), 718)
        for path in article_files:
            text = path.read_text(encoding="utf-8")
            m_title = re.search(r'^title:\s*"(.*)"$', text, re.M)
            self.assertIsNotNone(m_title, path.name)
            body = re.sub(r"\A---\n.*?\n---\n+", "", text, count=1, flags=re.S)
            body = re.sub(r"\A::: \{\.hatnote\}\n.*?\n:::\n+", "", body, count=1, flags=re.S)
            body = re.sub(r"\A:::: \{\.infobox\}\n.*?\n::::\n+", "", body, count=1, flags=re.S).lstrip()
            first_para = body.split("\n\n", 1)[0].strip()
            self.assertFalse(
                first_para.startswith((":::", "##", "###", "$$", "\\begin{", "|", "!")),
                f"{path.name} opens with unframed block: {first_para[:80]!r}",
            )
            bolds = re.findall(r"\*\*([^*]+)\*\*", first_para)
            lead_info = build_wiki.ARTICLE_LEADS[path.stem]
            self.assertEqual(bolds, [lead_info["term"]], path.name)
            self.assertTrue(first_para.startswith(build_wiki.article_lead({"slug": path.stem})), path.name)
            # Topic navbox, categories, and Cite this page (never Edit this page or GitHub/course codes)
            self.assertIn('<nav class="topic-navbox"', text, path.name)
            self.assertIn('aria-current="page"', text, path.name)
            self.assertIn('class="wiki-categories"', text, path.name)
            self.assertIn('<details class="cite-this-page">', text, path.name)
            self.assertIn(f"https://www.statwiki.io/articles/{path.stem}.html", text, path.name)
            self.assertNotIn("Edit this page", text, path.name)
            self.assertNotRegex(text, r"STAT\s*\d|\bgithub\b(?!\.io)", path.name)

        # Reconcile homepage counts with PARTS, final-preparation pages, and concept articles
        n_topic_chapters = sum(1 for _, files in build_wiki.PARTS for _, kind in files if kind == "notes")
        final_files = ("final-preparation.qmd", "final-bayesian.qmd", "final-applied.qmd")
        self.assertEqual(n_topic_chapters, 97)
        self.assertEqual(len(final_files), 3)
        home_text = home_path.read_text(encoding="utf-8")
        self.assertIn(f"**{n_topic_chapters} topic chapters**", home_text)
        self.assertIn(f"**{len(final_files)} final-preparation pages**", home_text)
        self.assertIn(f"**{len(article_files)} concept articles**", home_text)

        # Final-preparation pages include What links here and Cite this page
        for fname in final_files:
            ftext = (notes_dir / fname).read_text(encoding="utf-8")
            self.assertIn("## What links here {#what-links-here}", ftext, fname)
            self.assertIn('<details class="cite-this-page">', ftext, fname)
            self.assertNotIn("Edit this page", ftext, fname)

        # Overview, reference sheets, and labs include Cite this page and zero Edit/GitHub/course-code mentions
        for extra_page in (
            root / "overview.qmd",
            root / "reference" / "distributions.qmd",
            root / "reference" / "formulas.qmd",
            root / "reference" / "glossary.qmd",
            root / "labs" / "index.qmd",
            root / "labs" / "beta-binomial.qmd",
            root / "labs" / "ci-coverage.qmd",
            root / "labs" / "kernel-density.qmd",
            root / "labs" / "markov-chain.qmd",
        ):
            etext = extra_page.read_text(encoding="utf-8")
            self.assertIn('<details class="cite-this-page">', etext, str(extra_page))
            self.assertNotIn("Edit this page", etext, str(extra_page))
            self.assertNotRegex(etext, r"STAT\s*\d|\bgithub\b(?!\.io)", str(extra_page))

    def test_search_normalisation_shorthands_disambiguation_and_hatnotes(self) -> None:
        import topics

        cases = [
            ("Cramér–Rao lower bound", "cramer-rao-lower-bound"),
            ("Hölder's inequality", "holder-inequality"),
            ("Itô", "ito"),
            ("Lévy's continuity theorem", "levy-continuity-theorem"),
            ("Rényi", "renyi"),
            ("Fréchet", "frechet"),
            ("Bayes' theorem", "bayes-theorem"),
            ("Bayes’ theorem", "bayes-theorem"),
            ("Student's t", "student-t"),
            ("Students t", "student-t"),
            ("Fisher's exact test", "fisher-exact-test"),
            ("Fishers exact test", "fisher-exact-test"),
            ("Jensen's inequality", "jensen-inequality"),
            ("Jensens inequality", "jensen-inequality"),
            ("Slutsky's theorem", "slutsky-theorem"),
            ("Wilks' theorem", "wilk-theorem"),
            ("Wilks theorem", "wilk-theorem"),
            ("Hotelling's T² test", "hotelling-t2-test"),
            ("Simpson's paradox", "simpson-paradox"),
            ("Chebyshev's inequality", "chebyshev-inequality"),
            ("Markov's inequality", "markov-inequality"),
            ("Tukey's", "tukey"),
            ("Stirling's", "stirling"),
            ("i.i.d.", "iid"),
            ("s.d.", "sd"),
            ("t-test", "t-test"),
            ("t test", "t-test"),
            ("p-value", "p-value"),
            ("p value", "p-value"),
        ]
        for raw, expected in cases:
            self.assertEqual(build_wiki.canonical_search_key(raw), expected, raw)

        # Verify generated search-aliases.json and article hatnotes when build_wiki has run.
        alias_json = build_wiki.WIKI / "search-aliases.json"
        if alias_json.is_file():
            payload = json.loads(alias_json.read_text(encoding="utf-8"))
            self.assertIn("pages", payload)
            self.assertIn("aliases", payload)
            self.assertIn("disambiguations", payload)
            self.assertEqual(len([p for p in payload["pages"].values() if p.get("kind") == "article"]), 718)
            for key in ("sd", "se", "ci", "pi", "cv", "df", "rv", "iid", "bf", "kl", "em", "ar", "ma", "var", "cov", "corr", "rss", "ess", "tss", "t", "z", "f", "p", "r"):
                self.assertIn(key, payload["aliases"], f"missing shorthand {key!r}")
            for dis_key in ("mean", "variance", "standard-deviation", "t-test", "kernel", "score", "residual", "bootstrap", "independence", "normal", "prior", "power", "information", "scale"):
                self.assertIn(dis_key, payload["disambiguations"], f"missing disambiguation {dis_key!r}")
                opts = payload["disambiguations"][dis_key]["options"]
                self.assertGreaterEqual(len(opts), 2, dis_key)
                for opt in opts:
                    base = opt["href"].split("#", 1)[0]
                    self.assertIn(base, payload["pages"], f"{dis_key}: {opt}")

        # Verify disambiguation hatnotes exist and resolve to real target files on built articles.
        articles_dir = build_wiki.WIKI / "articles"
        if articles_dir.is_dir():
            for slug_name, rows in topics.HATNOTES.items():
                art_path = articles_dir / f"{slug_name}.qmd"
                self.assertTrue(art_path.is_file(), f"missing article for hatnote {slug_name}")
                art_text = art_path.read_text(encoding="utf-8")
                self.assertIn("::: {.hatnote}", art_text)
                for _prefix, target_rel, label in rows:
                    self.assertIn(f"[{label}]({target_rel})", art_text)
                    target_path = (art_path.parent / target_rel.split("#", 1)[0]).resolve()
                    self.assertTrue(target_path.is_file(), f"broken hatnote target {target_rel} on {slug_name}")
                    if "#" in target_rel:
                        frag = target_rel.split("#", 1)[1]
                        self.assertIn(frag, target_path.read_text(encoding="utf-8"))


class DistributionCatalogueTests(unittest.TestCase):
    def test_named_families_have_complete_catalogue_records(self) -> None:
        required = {
            "student-t", "chi-squared", "f", "cauchy", "bernoulli", "lognormal",
            "weibull", "pareto", "negative-binomial", "multivariate-normal",
            "wishart", "inverse-gaussian", "conway-maxwell-poisson",
        }
        self.assertTrue({f"{name}-distribution" for name in required} <= build_wiki.DISTRIBUTIONS.keys())
        for slug, fact in build_wiki.DISTRIBUTIONS.items():
            with self.subTest(slug=slug):
                self.assertTrue(all(fact[key] for key in ("name", "notation", "parameters", "support", "description", "symbols")))
                self.assertTrue(fact["pmf"] or fact["pdf"])
                if fact["plot"]:
                    self.assertTrue(fact["plot"]["parameters"])
                    self.assertTrue(fact["plot"]["views"])
                self.assertTrue(set(fact["related"]) <= build_wiki.DISTRIBUTIONS.keys())

    def test_generated_distribution_infoboxes_and_plots(self) -> None:
        articles = build_wiki.WIKI / "articles"
        if not articles.is_dir():
            self.skipTest("Wiki has not been generated")
        for slug in build_wiki.DISTRIBUTIONS:
            with self.subTest(slug=slug):
                page = articles / f"{slug}.qmd"
                self.assertTrue(page.is_file())
                body = page.read_text(encoding="utf-8")
                self.assertIn("::: {.infobox-title}", body)
                self.assertIn("## Definition {#definition}", body)
                self.assertIn('aria-label="Probability distributions"', body)
                headings = [h.strip() for h in re.findall(r"^## ([^\n{]+)", body, flags=re.M)]
                order = ["Definition", "Properties", "Related distributions", "Statistical inference",
                         "Generating random samples", "History", "Examples", "See also", "References"]
                self.assertEqual(headings, [name for name in order if name in headings], page.name)
                self.assertEqual("Generating random samples" in headings, bool(build_wiki.DISTRIBUTIONS[slug]["sampling"]))
                lead = re.search(r"^In [^\n]+", body, flags=re.M).group()
                self.assertNotIn("$", lead)
                for kind in build_wiki.DISTRIBUTIONS[slug]["plot"].get("views", []):
                    self.assertTrue((build_wiki.WIKI / "reference" / "plots" / f"{slug}-{kind}.png").is_file())
        notation = build_wiki.WIKI / "reference" / "notation.qmd"
        self.assertTrue(notation.is_file())
        self.assertIn("| Symbol | Meaning | First used |", notation.read_text(encoding="utf-8"))

    def test_generated_local_link_targets_exist(self) -> None:
        if not (build_wiki.WIKI / "articles").is_dir():
            self.skipTest("Wiki has not been generated")
        missing = []
        missing_fragments = []
        targets: dict[Path, set[str]] = {}
        for folder in ("articles", "notes", "questions", "reference"):
            for page in (build_wiki.WIKI / folder).rglob("*.qmd"):
                body = page.read_text(encoding="utf-8")
                for chunk in re.split(r"```.*?```", body, flags=re.S):
                    for match in build_wiki.MD_LINK_TARGET.finditer(chunk):
                        destination, _, fragment = unquote(match.group(2)).partition("#")
                        if (not destination and not fragment) or re.match(r"^[a-z]+:|^/", destination):
                            continue
                        target = (page.parent / destination).resolve() if destination else page
                        if target.suffix == ".html" and not target.exists():
                            target = target.with_suffix(".qmd")
                        if not target.exists():
                            missing.append(f"{page.relative_to(build_wiki.WIKI)} -> {destination}")
                        elif fragment and target.suffix == ".qmd":
                            if target not in targets:
                                target_body = target.read_text(encoding="utf-8")
                                targets[target] = set(re.findall(r"\{#([\w:-]+)", target_body))
                                targets[target].update(re.findall(r"id=[\"']([\w:-]+)", target_body))
                                targets[target].update(
                                    build_wiki.slug(heading)
                                    for heading in re.findall(r"^#{1,6}\s+([^\n{]+)", target_body, flags=re.M)
                                )
                            if fragment not in targets[target]:
                                missing_fragments.append(f"{page.relative_to(build_wiki.WIKI)} -> {destination}#{fragment}")
                for destination in re.findall(r'href="([^"]+)"', body):
                    parsed = urlsplit(unquote(destination))
                    if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
                        continue
                    target = (page.parent / parsed.path).resolve()
                    if target.suffix == ".html":
                        target = target.with_suffix(".qmd")
                    if target.suffix in {".qmd", ".png", ".jpg", ".svg", ".pdf"} and not target.exists():
                        missing.append(f"{page.relative_to(build_wiki.WIKI)} -> {destination}")
        self.assertEqual(missing, [])
        self.assertEqual(missing_fragments, [])

    def test_distribution_rows_escapes_and_multivariate_previews(self) -> None:
        for slug, facts in build_wiki.DISTRIBUTIONS.items():
            for field, value in facts.items():
                if isinstance(value, str):
                    self.assertIsNone(re.search(r"\\\\[A-Za-z]", value), f"double escape in {slug}.{field}")
            page = (build_wiki.WIKI / "articles" / f"{slug}.qmd").read_text(encoding="utf-8")
            box = page.split(":::: {.infobox}", 1)[1].split("\n::::", 1)[0]
            self.assertIsNone(re.search(r"^\|[^|]*\|\s*\|$", box, flags=re.M), slug)
            if facts["kind"] == "continuous":
                self.assertNotIn("| Probability mass function |", box)
            else:
                self.assertNotIn("| Probability density |", box)
            for field, label in build_wiki.DISTRIBUTION_ROW_LABELS:
                self.assertEqual(f"| {label} |" in box, bool(facts[field]), f"{slug}.{field}")
            for view in facts["plot"].get("views", []):
                caption = re.search(rf"!\[([^]]+)\]\([^)]*{slug}-{view}\.png\)", box)
                self.assertIsNotNone(caption, f"missing plot caption on {slug}.{view}")
                self.assertIn(facts["plot"]["parameters"], caption.group(1))
                if facts["plot"]["scipy"] not in {"dirichlet3", "multinomial3", "mvnorm2"}:
                    self.assertFalse(caption.group(1).startswith(facts["name"] + " "), slug)
        for slug in ("dirichlet", "multinomial", "multivariate-normal", "wishart"):
            spec = build_wiki.DISTRIBUTIONS[f"{slug}-distribution"]["plot"]
            self.assertTrue(not spec or spec["scipy"] in {"dirichlet3", "multinomial3", "mvnorm2"}, slug)

    def test_standard_closed_form_rows_are_populated(self) -> None:
        expected = {
            "normal": ("median", "mode", "skewness", "excess_kurtosis", "entropy", "mgf", "characteristic_function", "fisher_information"),
            "exponential": ("median", "mode", "skewness", "excess_kurtosis", "entropy", "mgf", "characteristic_function", "fisher_information"),
            "gamma": ("mode", "skewness", "excess_kurtosis", "entropy", "mgf", "characteristic_function", "fisher_information"),
            "beta": ("mode", "skewness", "excess_kurtosis", "entropy", "mgf", "characteristic_function", "fisher_information"),
            "uniform": ("median", "mode", "skewness", "excess_kurtosis", "entropy", "mgf", "characteristic_function"),
            "binomial": ("mode", "skewness", "excess_kurtosis", "entropy", "mgf", "characteristic_function", "fisher_information"),
            "poisson": ("mode", "skewness", "excess_kurtosis", "mgf", "characteristic_function", "fisher_information"),
            "bernoulli": ("median", "mode", "skewness", "excess_kurtosis", "entropy", "mgf", "characteristic_function", "fisher_information"),
            "geometric": ("median", "mode", "skewness", "excess_kurtosis", "entropy", "mgf", "characteristic_function", "fisher_information"),
        }
        for family, fields in expected.items():
            facts = build_wiki.DISTRIBUTIONS[f"{family}-distribution"]
            for field in fields:
                self.assertTrue(facts[field], f"{family}.{field}")

    def test_general_notation_has_first_use_links(self) -> None:
        page = (build_wiki.WIKI / "reference" / "notation.qmd").read_text(encoding="utf-8")
        for entry in build_wiki.GENERAL_NOTATION:
            self.assertIn(entry["symbol"], page)
            self.assertIn(f"../articles/{entry['article']}.qmd", page)

    def test_restored_distribution_rows_and_notation(self) -> None:
        data = build_wiki.DISTRIBUTIONS
        for family in ("gamma", "beta", "dirichlet", "inverse-gamma"):
            self.assertTrue(data[f"{family}-distribution"]["mode"], family)
        conjugate = {slug for slug, facts in data.items()
                     if facts["conjugate_prior_for"] or facts["conjugate_prior"]}
        self.assertEqual(len(conjugate), 8)
        for slug, facts in data.items():
            self.assertNotIn(r"$x\sim", facts["notation"], slug)
            self.assertNotIn(r"\mathbb{E}(x)", facts["mean"], slug)
            self.assertNotIn(r"\operatorname{Var}(x)", facts["variance"], slug)
        for family, symbol in (("gamma", r"\lambda"), ("poisson", r"\lambda"),
                               ("student-t", r"\nu"), ("chi-squared", r"\nu"),
                               ("f", "d_1"), ("bernoulli", "(p)")):
            facts = data[f"{family}-distribution"]
            self.assertIn(symbol, facts["notation"], family)
        for family, parameter in (("gamma", "λ="), ("poisson", "λ="),
                                  ("student-t", "ν="), ("chi-squared", "ν="),
                                  ("f", "d₁="), ("bernoulli", "p=")):
            self.assertIn(parameter, data[f"{family}-distribution"]["plot"]["parameters"])
        poisson = (build_wiki.WIKI / "articles" / "poisson-distribution.qmd").read_text(encoding="utf-8")
        self.assertNotIn(r"\theta", poisson)
        inverse_gamma = (build_wiki.WIKI / "articles" / "inverse-gamma-distribution.qmd").read_text(encoding="utf-8")
        self.assertIn(r"The mode is $\beta/(\alpha+1)$, which is not the variance.", inverse_gamma)


class TheoremTemplateTests(unittest.TestCase):
    def test_every_result_has_a_proof_or_todo_entry(self) -> None:
        articles = build_wiki.WIKI / "articles"
        todo_file = build_wiki.WIKI / "proofs-todo.json"
        if not articles.is_dir() or not todo_file.is_file():
            self.skipTest("Wiki has not been generated")
        todo = {row["slug"] for row in json.loads(todo_file.read_text(encoding="utf-8"))}
        results = []
        for page in articles.glob("*.qmd"):
            body = page.read_text(encoding="utf-8")
            if "| Statement | [Read statement](#statement) |" not in body:
                continue
            results.append(page.stem)
            self.assertIn("## Statement {#statement}", body, page.name)
            headings = [h.strip() for h in re.findall(r"^## ([^\n{]+)", body, flags=re.M)]
            order = ["Statement", "Motivating example", "Intuition", "Key results", "Generalizations", "Related concepts", "Statistical use", "Common misconceptions",
                     "History", "Examples", "See also", "References"]
            self.assertEqual(headings, [name for name in order if name in headings], page.name)
            proof_box = '::: {.callout-note collapse="true" title="Proof"}'
            self.assertTrue(proof_box in body or page.stem in todo, page.name)
            self.assertEqual(body.count(proof_box), int(page.stem not in todo), page.name)
            self.assertNotIn("## Proof", body, page.name)
            self.assertNotIn("*Proof.*", body, page.name)
            self.assertNotIn("## In *", body, page.name)
            lead = re.search(r"^In [^\n]+", body, flags=re.M).group()
            self.assertNotIn("$", lead, page.name)
        self.assertGreaterEqual(len(results), 90)
        self.assertTrue({slug for slug in todo if "#property-" not in slug} <= set(results))

    def test_memoryless_and_product_rule_proofs_cover_their_statements(self) -> None:
        articles = build_wiki.WIKI / "articles"
        memoryless = (articles / "memoryless-property.qmd").read_text(encoding="utf-8")
        product = (articles / "product-rule.qmd").read_text(encoding="utf-8")
        self.assertIn("Conversely", memoryless)
        self.assertIn("only continuous memoryless", memoryless)
        self.assertIn("geometric law", memoryless)
        self.assertIn("induction hypothesis", product)
        self.assertIn("$n$-event product", product)


class ConceptTemplateTests(unittest.TestCase):
    def test_reviewed_leads_have_one_term_and_matching_agreement(self) -> None:
        articles = build_wiki.WIKI / "articles"
        if not articles.is_dir():
            self.skipTest("Wiki has not been generated")
        pages = {page.stem: page for page in articles.glob("*.qmd")}
        self.assertEqual(set(pages), set(build_wiki.ARTICLE_LEADS))
        singular_suffix_exceptions = {
            "bayes-action-for-two-hypotheses", "bayes-consistency-of-nearest-neighbours",
            "chi-squared-test-with-estimated-parameters", "chi-squared-test-with-known-cell-probabilities",
            "choosing-the-number-of-principal-components", "classification-with-unequal-costs",
            "empirical-bayes", "f-test-for-equal-variances", "interval-for-a-difference-of-means",
            "interval-for-a-ratio-of-variances", "law-of-large-numbers", "method-of-moments",
            "pearson-test-with-estimated-parameters", "sampling-distribution-of-the-regression-estimators",
            "soft-thresholding-for-orthonormal-predictors", "softmax-is-multinomial-logistic-regression",
        }
        singular_endings = ("analysis", "process", "class", "loss", "bias", "statistics", "series",
                            "squares", "synthesis", "basis", "hypothesis", "status", "radius",
                            "calculus", "cross", "ness", "gas", "is")
        for slug, page in pages.items():
            info = build_wiki.ARTICLE_LEADS[slug]
            body = page.read_text(encoding="utf-8")
            lead = re.search(r"^In [^\n]+$", body, flags=re.M).group()
            title = re.search(r'^title: "(.*)"$', body, flags=re.M).group(1)
            self.assertEqual(re.findall(r"\*\*([^*]+)\*\*", lead), [info["term"]], slug)
            self.assertIn(f"**{info['term']}** {info['verb']} ", lead, slug)
            self.assertIn(info["verb"], {"is", "are"}, slug)
            self.assertIn(info["article"], {"", "a", "an", "the"}, slug)
            if info["article"] in {"a", "an"}:
                self.assertEqual(info["verb"], "is", slug)
            if not info.get("proper"):
                self.assertTrue(info["term"][0].islower(), slug)
                if title[0].isupper():
                    self.assertNotIn(f"**{title}**", lead, slug)
            last = re.findall(r"[A-Za-z]+", info["term"])[-1].lower()
            if last.endswith("s") and not last.endswith(singular_endings) and slug not in singular_suffix_exceptions:
                self.assertEqual(info["verb"], "are", slug)
            self.assertNotRegex(lead, r"\*\*[^*]+\*\* is (?:is|are)\b", slug)

    def test_lead_descriptions_are_specific(self) -> None:
        placeholder = re.compile(
            r"(?:proposition about|dataset used to study|model that describes|"
            r"function used to describe|procedure used to analyse)\b", re.I
        )
        for slug, info in build_wiki.ARTICLE_LEADS.items():
            self.assertNotRegex(info["description"], placeholder, slug)

    def test_posterior_mean_keeps_source_definitions_and_figure(self) -> None:
        body = (build_wiki.WIKI / "articles" / "posterior-mean.qmd").read_text(encoding="utf-8")
        self.assertIn("Posterior point summaries", body)
        self.assertIn("Credible-region constructions", body)
        self.assertIn("part1-fig-01-credible-regions.png", body)
        self.assertNotIn("*Proof.*", (build_wiki.WIKI / "articles" / "metropolis-hastings-algorithm.qmd").read_text(encoding="utf-8"))

    def test_mapped_articles_link_their_laboratory(self) -> None:
        import topics

        articles = build_wiki.WIKI / "articles"
        if not articles.is_dir():
            self.skipTest("Wiki has not been generated")
        for slug, (lab, _label, _action) in topics.LAB_FOR_TOPIC.items():
            with self.subTest(slug=slug):
                page = articles / f"{slug}.qmd"
                self.assertTrue(page.is_file())
                self.assertTrue((build_wiki.WIKI / "labs" / lab).is_file())
                body = page.read_text(encoding="utf-8")
                self.assertIn('title="Try it"', body)
                self.assertIn(f"../labs/{lab}", body)

    def test_all_article_leads_are_plain_language(self) -> None:
        articles = build_wiki.WIKI / "articles"
        if not articles.is_dir():
            self.skipTest("Wiki has not been generated")
        pages = list(articles.glob("*.qmd"))
        self.assertGreaterEqual(len(pages), 700)
        for page in pages:
            body = page.read_text(encoding="utf-8")
            lead = re.search(r"^In [^\n]+", body, flags=re.M).group()
            self.assertTrue(lead.startswith("In "), page.name)
            self.assertIsNone(re.search(r"\$|\\\(|\\\[|\\begin\{", lead), page.name)
            self.assertNotIn("## In *", body, page.name)

    def test_no_chapter_placeholders_or_duplicate_normal_density(self) -> None:
        for page in (build_wiki.WIKI / "articles").glob("*.qmd"):
            body = page.read_text(encoding="utf-8")
            self.assertIsNone(re.search(r"^## (?:In|From) \*|^## Taught in\b", body, flags=re.M), page.name)
            self.assertNotRegex(body, r"::: \{\.mainarticle\}\nFrom \[", page.name)
            self.assertNotIn("- **Taught in**", body, page.name)
        normal = (build_wiki.WIKI / "articles" / "normal-distribution.qmd").read_text(encoding="utf-8")
        definition = normal.split("## Definition {#definition}", 1)[1].split("\n## ", 1)[0]
        self.assertEqual(definition.count("The probability density is"), 1)

    def test_concepts_follow_the_fixed_section_order(self) -> None:
        articles = build_wiki.WIKI / "articles"
        if not articles.is_dir():
            self.skipTest("Wiki has not been generated")
        for page in articles.glob("*.qmd"):
            body = page.read_text(encoding="utf-8")
            if page.stem in build_wiki.DISTRIBUTIONS or "| Statement | [Read statement](#statement) |" in body:
                continue
            headings = [h.strip() for h in re.findall(r"^## ([^\n{]+)", body, flags=re.M)]
            if (build_wiki.WIKI / "research" / "content" / f"{page.stem}.md").is_file():
                order = ["Motivating example", "Intuition", "Definition", "Interpretation", "Properties", "Statistical use",
                         "Worked example", "Examples", "Common misconceptions", "Assumptions and limits",
                         "Connections", "Check yourself", "History", "See also", "References"]
            else:
                order = ["Definition", "Properties", "Interpretation", "History", "Examples", "See also", "References"]
            self.assertEqual(headings, [name for name in order if name in headings], page.name)

    def test_research_pass_preserves_article_words_and_figures(self) -> None:
        baseline_path = build_wiki.WIKI / "research" / "baseline.json"
        if not baseline_path.is_file():
            self.skipTest("Research baseline has not been recorded")
        baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
        self.assertEqual(len(baseline), len(list((build_wiki.WIKI / "articles").glob("*.qmd"))))
        for slug, minimum in baseline.items():
            text = (build_wiki.WIKI / "articles" / f"{slug}.qmd").read_text(encoding="utf-8")
            leading = text.split("## See also", 1)[0]
            words = _prose_word_count(leading)
            figures = len(re.findall(r"!\[[^]]*\]\(", text))
            self.assertGreaterEqual(words, minimum["words"], slug)
            self.assertGreaterEqual(figures, minimum["figures"], slug)

    def test_prose_word_count_keeps_r_output_and_following_text(self) -> None:
        sample = 'model <- lm(y ~ x)\n# Pr(>|t|) < 2e-16\nA fitted association. <sup>[1]</sup>'
        self.assertIn("A fitted association.", re.sub(r"</?[A-Za-z][^>]*>", " ", sample))
        self.assertEqual(_prose_word_count(sample), _prose_word_count(sample.replace(" <sup>[1]</sup>", " [1]")))

    def test_curated_histories_are_cited(self) -> None:
        import article_extras

        articles = build_wiki.WIKI / "articles"
        if not articles.is_dir():
            self.skipTest("Wiki has not been generated")
        for slug in article_extras.ARTICLE_HISTORIES:
            page = articles / f"{slug}.qmd"
            body = page.read_text(encoding="utf-8")
            self.assertIn("## History {#history}", body, slug)
            history = body.split("## History {#history}", 1)[1].split("\n## ", 1)[0]
            self.assertIn('class="cite-ref"', history, slug)


class ContentRetentionTests(unittest.TestCase):
    """Compare generated articles with the archived pre-#57 build (5359ad2)."""

    @staticmethod
    def figure_targets(body: str) -> collections.Counter:
        found = []
        for line in body.splitlines():
            if "![" in line:
                match = re.search(r"!\[.*\]\((\.\./figures/[^)]+)\)", line)
                if match:
                    found.append(match.group(1))
        return collections.Counter(found)

    @staticmethod
    def prose_words(body: str) -> int:
        body = re.split(r"^## References", body, flags=re.M)[0]
        body = re.sub(r"(?ms)^:::: \{\.infobox\}.*?^::::\s*", "", body)
        body = re.sub(r"(?ms)^::: \{\.hatnote\}.*?^:::\s*", "", body)
        body = re.sub(r"(?m)^## (?:In|From) [^\n]*\n", "", body)
        body = re.sub(r"(?ms)^::: \{\.mainarticle\}\n(?:From|Main article):[^\n]*\n:::\s*", "", body)
        body = re.sub(r"(?m)^- \*\*Taught in\*\*[^\n]*\n", "", body)
        body = re.sub(r"\[[^]]+\]\([^)]+\)", lambda match: match.group().split("]")[0][1:], body)
        return len(re.findall(r"\b[\w-]+\b", body))

    def test_no_article_loses_source_figures_or_substantive_text(self) -> None:
        fixture = json.loads((build_wiki.WIKI / "pre57_article_baseline.json").read_text(encoding="utf-8"))
        self.assertEqual(fixture["commit"], "5359ad2")
        articles = build_wiki.WIKI / "articles"
        self.assertEqual(len(fixture["articles"]), len(list(articles.glob("*.qmd"))))
        for slug, before in fixture["articles"].items():
            body = (articles / f"{slug}.qmd").read_text(encoding="utf-8")
            self.assertFalse(collections.Counter(before["figures"]) - self.figure_targets(body), slug)
            self.assertGreaterEqual(self.prose_words(body) * 10, before["words"] * 9, slug)


class DistributionDepthBatchTests(unittest.TestCase):
    def test_depth_sections_are_specific_and_proved(self) -> None:
        data = build_wiki.DISTRIBUTIONS
        self.assertEqual(len(data), 25)
        history_todo = {row["slug"] for row in json.loads(
            (build_wiki.WIKI / "distribution-history-todo.json").read_text(encoding="utf-8"))}
        self.assertEqual(history_todo, {slug for slug, facts in data.items() if not facts["history"]})
        for slug, facts in data.items():
            body = (build_wiki.WIKI / "articles" / f"{slug}.qmd").read_text(encoding="utf-8")
            self.assertTrue(facts["lead_context"].strip(), slug)
            self.assertNotIn("$", facts["lead_context"], slug)
            self.assertGreaterEqual(len(facts["statistical_use"].split()), 25, slug)
            self.assertIn("{{cite:", facts["statistical_use"], slug)
            self.assertIn(facts["key_result"]["title"], body, slug)
            self.assertIn('::: {.callout-note collapse="true" title="Proof"}', body, slug)
            proof_source = facts["key_result"]["proof"]
            if not proof_source.strip():
                research_file = build_wiki.WIKI / "research" / "content" / f"{slug}.md"
                self.assertTrue(research_file.is_file(), slug)
                proof_source = research_file.read_text(encoding="utf-8")
                self.assertIn('::: {.callout-note collapse="true" title="Proof"}', proof_source, slug)
            self.assertIn("{{cite:", proof_source, slug)
            self.assertIn("### ", facts["worked_example"], slug)
            self.assertRegex(facts["worked_example"], r"\d", slug)
            self.assertIn("{{cite:", facts["worked_example"], slug)
            inference = body.split("## Statistical inference {#used-in}", 1)[1].split("\n## ", 1)[0]
            self.assertIn("class=\"cite-ref\"", inference, slug)
            related = body.split("## Related distributions {#related-distributions}", 1)[1].split("\n## ", 1)[0]
            self.assertIn(".qmd", related, slug)
            self.assertGreaterEqual(len(related.split()), 20, slug)
            if slug not in history_todo:
                self.assertEqual(len(facts["history"].split("\n\n")), 2, slug)
                self.assertGreaterEqual(facts["history"].count("{{cite:"), 2, slug)

    def test_relationships_are_reciprocal_and_cover_old_links(self) -> None:
        data = build_wiki.DISTRIBUTIONS
        relationships = build_wiki.DISTRIBUTION_RELATIONSHIPS
        pairs = {frozenset((row["a"], row["b"])) for row in relationships}
        self.assertEqual(len(pairs), len(relationships))
        self.assertEqual({slug for pair in pairs for slug in pair}, set(data))
        for row in relationships:
            self.assertIn(row["a"], data)
            self.assertIn(row["b"], data)
            for end, other, text in ((row["a"], row["b"], row["a_text"]),
                                     (row["b"], row["a"], row["b_text"])):
                self.assertIn("{target}", text, end)
                self.assertIn("{{cite:", text, end)
                page = (build_wiki.WIKI / "articles" / f"{end}.qmd").read_text(encoding="utf-8")
                self.assertIn(f"({other}.qmd)", page, end)
        for slug, facts in data.items():
            for other in facts["related"]:
                self.assertIn(frozenset((slug, other)), pairs)

    def test_first_batch_preserves_previous_build(self) -> None:
        baseline = json.loads((build_wiki.WIKI / "depth_distribution_baseline.json").read_text(encoding="utf-8"))
        self.assertEqual(baseline["commit"], "5dc5301")
        for slug, old in baseline["articles"].items():
            body = (build_wiki.WIKI / "articles" / f"{slug}.qmd").read_text(encoding="utf-8")
            self.assertGreaterEqual(ContentRetentionTests.prose_words(body), old["words"], slug)
            self.assertFalse(collections.Counter(old["figures"]) - ContentRetentionTests.figure_targets(body), slug)
            citation_keys = set(re.findall(r'data-cite-key="([^"]+)"', body))
            expected_keys = set(old["citation_keys"])
            if slug in {"normal-distribution", "chi-squared-distribution"}:
                # The normal-sample theorem now cites the opened Siegrist §6.08
                # in place of two unverified historical attributions.
                expected_keys -= {"student1908", "fisher1925_smrw"}
                self.assertIn("siegrist2022_normals", citation_keys, slug)
            if slug == "uniform-distribution":
                # The inherited inverse-transform statement now cites the
                # opened proof in Billingsley §14.
                expected_keys -= {"vonneumann1951"}
                self.assertIn("billingsley1995", citation_keys, slug)
            if slug == "multivariate-normal-distribution":
                # The affine-normal statement now cites the opened treatments
                # by Strimmer and Wang in place of unexamined textbook entries.
                expected_keys -= {"feller1968", "casella_berger2002"}
                self.assertIn("strimmer2025_mva", citation_keys, slug)
                self.assertIn("wang2025_foundations", citation_keys, slug)
            if slug == "student-t-distribution":
                # The shared normal-sample and slope passages now cite the
                # opened Siegrist and Fox derivations.
                expected_keys -= {"neyman1937", "davison2003"}
                self.assertIn("siegrist2022_normals", citation_keys, slug)
                self.assertIn("fox2016_regression", citation_keys, slug)
            if slug == "normal-distribution":
                # Unread bibliography-only entries and citations to unopened
                # books were replaced with located citations to opened sources.
                expected_keys -= {"box_tiao1973", "casella_berger2002", "feller1968",
                                  "fisher1925_smrw", "gauss1809", "gelfand_smith1990",
                                  "laplace1812", "student1908"}
                self.assertIn("siegrist2022_normal_distribution", citation_keys, slug)
                self.assertIn("gelman_bda2013", citation_keys, slug)
            if slug == "gamma-distribution":
                # The shared conjugate-update statement now cites the opened
                # Diaconis–Ylvisaker paper and Geyer's located derivation.
                expected_keys.discard("raiffa_schlaifer1961")
                self.assertIn("geyer2025_conjugate", citation_keys, slug)
            if slug == "poisson-distribution":
                # The same shared update replaces two unlocated book markers.
                expected_keys.difference_update({"raiffa_schlaifer1961", "gelman_bda2013"})
                self.assertIn("geyer2025_conjugate", citation_keys, slug)
            self.assertTrue(expected_keys <= citation_keys, slug)
            self.assertTrue(set(old["question_links"]) <= set(re.findall(r'\.\./questions/[^)#]+\.qmd', body)), slug)
            self.assertTrue(set(old["example_headings"]) <= set(re.findall(r'^### [^\n]+\{#example-[^}]+\}', body, re.M)), slug)
            box = body.split(":::: {.infobox}", 1)[1].split("\n::::", 1)[0]
            for label, value in old["infobox_rows"].items():
                self.assertIn(f"| {label} | {value} |", box, slug)

    def test_copied_distribution_results_have_proofs_or_todos(self) -> None:
        todo = {row["slug"] for row in json.loads(
            (build_wiki.WIKI / "proofs-todo.json").read_text(encoding="utf-8"))}
        for slug in build_wiki.DISTRIBUTIONS:
            body = (build_wiki.WIKI / "articles" / f"{slug}.qmd").read_text(encoding="utf-8")
            properties = body.split("## Properties {#properties}", 1)[1].split("\n## ", 1)[0]
            heads = list(re.finditer(r"^### (.+?) \{#(property-[^}]+)\}", properties, re.M))
            for i, head in enumerate(heads):
                section = properties[head.end():heads[i + 1].start() if i + 1 < len(heads) else None]
                self.assertTrue('::: {.proof}' in section or f"{slug}#{head.group(2)}" in todo,
                                f"{slug}: {head.group(1)}")


class BayesianResultDepthBatchTests(unittest.TestCase):
    def test_result_depth_and_reciprocal_relationships(self) -> None:
        import theorem_depth

        data = theorem_depth.RESULT_DEPTH
        self.assertEqual(len(data), 25)
        todo = {row["slug"] for row in json.loads(
            (build_wiki.WIKI / "proofs-todo.json").read_text(encoding="utf-8"))}
        self.assertFalse(set(data) & todo)
        for slug, proof in theorem_depth.PROOFS.items():
            self.assertIn(slug, data)
            self.assertIn("{{cite:", proof, slug)
        relationships = theorem_depth.RELATIONSHIPS
        pairs = {frozenset((row["a"], row["b"])) for row in relationships}
        self.assertEqual(len(pairs), len(relationships))
        self.assertEqual({slug for pair in pairs for slug in pair}, set(data))
        history_todo = {row["slug"] for row in json.loads(
            (build_wiki.WIKI / "theorem-history-todo.json").read_text(encoding="utf-8"))}
        def has_research_history(slug: str) -> bool:
            path = build_wiki.WIKI / "research" / "content" / f"{slug}.md"
            return path.is_file() and "## History\n" in path.read_text(encoding="utf-8")

        self.assertEqual(history_todo, {slug for slug, x in data.items()
                                        if "history" not in x and "history_add" not in x
                                        and not has_research_history(slug)})
        for slug, x in data.items():
            body = (build_wiki.WIKI / "articles" / f"{slug}.qmd").read_text(encoding="utf-8")
            self.assertTrue(x["context"].strip(), slug)
            self.assertNotIn("$", x["context"], slug)
            self.assertIn('::: {.callout-note collapse="true" title="Proof"}', body, slug)
            self.assertEqual(body.count('title="Proof"'), 1, slug)
            self.assertIn("## Intuition {#intuition}", body, slug)
            self.assertIn("## Related concepts {#related-concepts}", body, slug)
            self.assertIn("## Statistical use {#statistical-use}", body, slug)
            self.assertIn("class=\"cite-ref\"", body.split("## Statistical use", 1)[1].split("\n## ", 1)[0], slug)
            self.assertIn("## Examples {#examples}", body, slug)
            examples = body.split("## Examples {#examples}", 1)[1].split("\n## ", 1)[0]
            self.assertTrue(x.get("example") or "**Solution" in examples or "Worked answer" in examples, slug)
            if slug not in history_todo:
                history = body.split("## History {#history}", 1)[1].split("\n## ", 1)[0]
                self.assertGreaterEqual(len(history.strip().split("\n\n")), 2, slug)
        for row in relationships:
            for slug, other, text in ((row["a"], row["b"], row["a_text"]),
                                      (row["b"], row["a"], row["b_text"])):
                self.assertIn("{target}", text, slug)
                self.assertIn("{{cite:", text, slug)
                body = (build_wiki.WIKI / "articles" / f"{slug}.qmd").read_text(encoding="utf-8")
                related = body.split("## Related concepts {#related-concepts}", 1)[1].split("\n## ", 1)[0]
                self.assertIn(f"({other}.qmd)", related, slug)

    def test_previous_bayesian_result_content_is_preserved(self) -> None:
        baseline = json.loads((build_wiki.WIKI / "depth_bayesian_results_baseline.json").read_text(encoding="utf-8"))
        self.assertEqual(baseline["commit"], "d1b91cb")
        for slug, old in baseline["articles"].items():
            body = (build_wiki.WIKI / "articles" / f"{slug}.qmd").read_text(encoding="utf-8")
            self.assertGreaterEqual(ContentRetentionTests.prose_words(body), old["words"], slug)
            self.assertFalse(collections.Counter(old["figures"]) - ContentRetentionTests.figure_targets(body), slug)
            expected_keys = set(old["citation_keys"])
            citation_keys = set(re.findall(r'data-cite-key="([^"]+)"', body))
            if slug == "normal-normal-conjugacy":
                expected_keys.discard("box_tiao1973")
                self.assertIn("gelman_bda2013", citation_keys, slug)
                self.assertIn("raiffa_schlaifer1961", citation_keys, slug)
            if slug == "full-conditionals-under-independent-priors":
                # Gelfand–Smith discusses a different multivariate model;
                # the displayed normal and inverse-gamma forms use these texts.
                expected_keys.discard("gelfand_smith1990")
                self.assertIn("gelman_bda2013", citation_keys, slug)
                self.assertIn("raiffa_schlaifer1961", citation_keys, slug)
            if slug == "bayes-rule":
                # Replace the bibliography-only Laplace and Jeffreys entries and
                # the unlocated Gelman passage with passages read for this article.
                expected_keys.difference_update({"laplace1812", "jeffreys1961", "gelman_bda2013"})
                self.assertTrue({"wang2025_foundations", "hoff2013_bayes_estimators"} <= citation_keys)
            if slug == "log-partition-moment-identities":
                # Replace two unopened textbooks in the shared proposition
                # with an opened, located exponential-family derivation.
                expected_keys.difference_update({"lehmann_casella1998", "mccullagh_nelder1989"})
                self.assertIn("geyer2022_exp_family", citation_keys, slug)
            self.assertTrue(expected_keys <= citation_keys, slug)
            self.assertTrue(set(old["question_links"]) <= set(re.findall(r'\.\./questions/[^)#]+\.qmd', body)), slug)
            self.assertTrue(set(old["example_headings"]) <= set(re.findall(r'^### [^\n]+\{#example-[^}]+\}', body, re.M)), slug)
            box = body.split(":::: {.infobox}", 1)[1].split("\n::::", 1)[0]
            for label, value in old["infobox_rows"].items():
                self.assertIn(f"| {label} | {value} |", box, slug)
        mode = (build_wiki.WIKI / "articles" / "interior-dirichlet-mode.qmd").read_text(encoding="utf-8")
        statement = mode.split("## Statement {#statement}", 1)[1].split("\n## ", 1)[0]
        self.assertNotIn(r"\operatorname{mode}(P_k)", statement)
        self.assertIn(r"\widehat p_{k,\mathrm{joint\,MAP}}", statement)
        self.assertIn("density may maximise on the boundary", statement)


if __name__ == "__main__":
    unittest.main()
