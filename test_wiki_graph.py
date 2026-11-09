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
        self.assertEqual(by_id["example:exm-a"]["text"], by_id["example:exm-b"]["text"])
        self.assertNotEqual(by_id["example:exm-a"]["id"], by_id["example:exm-b"]["id"])

    def test_edited_answer_keeps_id_and_worked_answer_url(self) -> None:
        _root, first = self._document("Because.")
        _root, second = self._document("Because the mean moved.")
        before = next(item for item in first["entries"] if item["kind"] == "answer" and item["id"].endswith("question:ex-a"))
        after = next(item for item in second["entries"] if item["kind"] == "answer" and item["id"].endswith("question:ex-a"))
        self.assertEqual(before["id"], "answer:question:ex-a")
        self.assertEqual(after["id"], before["id"])
        self.assertEqual(after["url"], before["url"])
        self.assertTrue(after["url"].endswith("/questions/ex-a.qmd#worked-answer"))
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
        self.assertEqual([item["id"] for item in document["entries"]], sorted(ids))
        for item in document["entries"]:
            self.assertEqual(set(item), {"id", "kind", "title", "text", "url", "fingerprint"})
            url = item["url"]
            self.assertTrue(url.startswith("/"), url)
            path, _, fragment = url.partition("#")
            file = root / path.lstrip("/")
            self.assertTrue(file.is_file(), url)
            if fragment:
                self.assertRegex(file.read_text(encoding="utf-8"), rf"#{fragment}(?![A-Za-z0-9_-])")
        question_urls = {item["url"] for item in document["entries"] if item["kind"] == "question"}
        self.assertIn("/questions/ex-a.qmd", question_urls)
        self.assertIn("/questions/q-01.qmd", question_urls)
        target = f"section:{Path(CHAPTER).stem}:{ANCHOR}"
        self.assertIn(target, ids)
        self.assertTrue(any(edge["type"] == "defines" and edge["to"] == target for edge in document["edges"]))
        self.assertTrue(all(edge["from"] in ids and edge["to"] in ids for edge in document["edges"]))
        practice = next(item for item in document["entries"] if item["id"] == PRACTICE_LABEL)
        self.assertEqual(practice["url"], "/questions/q-01.qmd")
        for item in document["entries"]:
            self.assertNotIn("GitHub", item["id"])
            self.assertNotRegex(item["id"], r"STAT\d")
            self.assertNotRegex(item["url"], r"STAT\d")


if __name__ == "__main__":
    unittest.main()
