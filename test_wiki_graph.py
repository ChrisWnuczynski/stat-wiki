"""Tests for the page graph. They do not render the site."""

from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

import build_wiki
import wiki_graph

CHAPTER = build_wiki.CHAPTER_CODES["G1"]
ANCHOR = "s-the-three-components-of-a-glm"
HEADING = "The three components of a GLM"
PRACTICE_LABEL = "question:practice-rayleigh-conjugate-prior"


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
            build_wiki.SEARCH_ALIASES["mean"] = ("articles/expectation.html", "Mean")
            build_wiki.SEARCH_ALIASES["pca"] = ("notes/sl-03-principal-components.html", "PCA")
            build_wiki.SEARCH_ALIASES["expectation"] = ("articles/expectation.html", "Expectation")
            build_wiki.PAGE_TITLES[root / "articles" / "expectation.qmd"] = "Expectation"
            build_wiki.PAGE_TITLES[root / "notes" / "sl-03-principal-components.qmd"] = "Principal component analysis"

            build_wiki.write_alias_redirect_pages()
            self.assertFalse((root / "articles" / "expectation.html").exists())
            mean_stub = (root / "articles" / "mean.html").read_text(encoding="utf-8")
            pca_stub = (root / "articles" / "pca.html").read_text(encoding="utf-8")
            self.assertIn('var redirects = {"": "expectation.html"};', mean_stub)
            self.assertIn('var redirects = {"": "../notes/sl-03-principal-components.html"};', pca_stub)

            site = root / "_site"
            (site / "articles").mkdir(parents=True)
            (site / "notes").mkdir()
            (site / "articles" / "expectation.html").write_text("<html></html>", encoding="utf-8")
            (site / "notes" / "sl-03-principal-components.html").write_text("<html></html>", encoding="utf-8")
            (site / "articles" / "mean.html").write_text(mean_stub, encoding="utf-8")
            (site / "articles" / "pca.html").write_text(pca_stub, encoding="utf-8")

            saved_site = canonical_redirects.SITE_DIR
            canonical_redirects.SITE_DIR = site
            try:
                m1 = canonical_redirects.REDIRECTS.search(mean_stub)
                m2 = canonical_redirects.REDIRECTS.search(pca_stub)
                self.assertEqual(
                    canonical_redirects.canonical_for(site / "articles" / "mean.html", m1.group(1)),
                    "https://www.statwiki.io/articles/expectation.html",
                )
                self.assertEqual(
                    canonical_redirects.canonical_for(site / "articles" / "pca.html", m2.group(1)),
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


if __name__ == "__main__":
    unittest.main()
