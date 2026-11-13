"""Write the page graph the build already knows.

``wiki.json`` is generated on every run. ``graph/ids.json`` is written only
when the build is run with ``--update-ids``. A normal run reads that registry
and does not change it.

Schema version 2. The document is one object:

- ``version``: ``2``.
- ``aliases``: old id to the id this build emitted.
- ``entries``: one object per page, heading, box, example, question, answer, or figure.
- ``edges``: ``from``, ``type``, and ``to``, each end an id in ``entries``.

An entry has:

- ``id``: stable id. This file does not mint, drop, or rename one.
- ``kind``: ``chapter``, ``section``, ``definition``, ``theorem``, ``proposition``,
  ``corollary``, ``remark``, ``example``, ``article``, ``question``, ``answer``, or ``figure``.
- ``title``: the heading, with maths macros expanded.
- ``text``: Markdown and LaTeX, with Quarto fences, attributes, links, and images
  removed, each footnote marker replaced by its note in brackets, and maths macros
  expanded. Omitted when ``copy_of`` is set.
  A chapter's text is only the opening before its first ``##`` heading.
- ``url``: root-relative published path. A ``.qmd`` page is the ``.html`` page; the
  fragment is unchanged. A figure stays the image path.
- ``fingerprint``: sha256 of ``text``, or of the canonical entry's text when this
  entry omits ``text``.
- ``copy_of``: the id of the entry that keeps this text. Present only when another
  entry has the same text. A section keeps the text when one of the copies is a section.
  Otherwise a box keeps it when one of the copies is a box, so an article that repeats
  the box points at the box.
"""

from __future__ import annotations

import difflib
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from build_wiki import (
    CHAPTER_CODES,
    MATH_SPAN,
    ONE_ARG,
    TERMS,
    WIKI,
    ZERO_ARG,
    expand_macros,
    plain,
    protect_code,
)

BOX_KINDS = {"definition", "theorem", "proposition", "corollary", "remark"}
WARN_KINDS = {"section", "figure"}
BOX_PREFIX = {
    "def": "definition",
    "thm": "theorem",
    "prp": "proposition",
    "cor": "corollary",
    "rem": "remark",
}
DIST_STEM = "distributions"
DIST_FILE = Path("reference") / "distributions.qmd"


def fingerprint(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def question_graph_id(question: dict) -> str:
    """Stable id. Practice and concept questions use the label in the source."""
    if question.get("group") in {"practice", "concepts"}:
        label = (question.get("label") or "").strip()
        if not label:
            raise SystemExit(f"{question.get('group')} question {question.get('id')} has no stable label")
        return label
    return "question:" + question["id"]


def answer_graph_id(question_id: str) -> str:
    return "answer:" + question_id


def chapter_id(filename: str) -> str:
    return "chapter:" + Path(filename).stem


def section_id(filename: str, anchor: str) -> str:
    return f"section:{Path(filename).stem}:{anchor}"


def box_graph_id(anchor: str) -> str | None:
    kind = BOX_PREFIX.get(anchor.split("-", 1)[0])
    if not kind:
        return None
    return f"{kind}:{anchor}"


def root_url(path: Path, root: Path, fragment: str = "") -> str:
    """Published path. ``page.qmd`` is ``page.html``; a fragment is unchanged."""
    rel = path.relative_to(root)
    if rel.suffix == ".qmd":
        rel = rel.with_suffix(".html")
    url = "/" + rel.as_posix()
    if fragment:
        url += "#" + fragment
    return url


# Fenced and inline code, the same pieces protect_code leaves untouched.
_CODE = re.compile(r"```.*?```|`[^`\n]*`", re.S)
_FENCE_LINE = re.compile(r"^[ \t]*:{3,}[^\n]*\n?", re.M)
_FOOT_DEF = re.compile(r"^[ \t]*\[\^([^\]]+)\]:[ \t]*([^\n]*(?:\n[ \t]+[^\n]*)*)", re.M)
_FOOT_MARK = re.compile(r"\[\^([^\]]+)\]")
_CAPTION = r"((?:[^\[\]]|\[[^\]]*\])*)"
# Attribute braces only where Pandoc writes them: after a link or image, and
# `{#id}` / `{.class}` groups. A `{key=value}` group is not an attribute unless
# it is attached to that link or image, or it ends a heading or fence line.
_TRAILING_ATTRS = r"(?:[ \t]*\{[^{}\n]*\})*"
_IMAGE = re.compile(rf"!\[{_CAPTION}\]\([^)\n]*\){_TRAILING_ATTRS}")
_LINK = re.compile(rf"(?<!!)\[{_CAPTION}\]\([^)\n]*\){_TRAILING_ATTRS}")
_HEADING_ATTR = re.compile(r"^(#{1,6}[ \t]+\S.*?)[ \t]+\{[^{}\n]*\}[ \t]*$", re.M)
_QUARTO_ATTR = re.compile(r"\{[.#][^{}\n]*\}")
_H2 = re.compile(r"^##(?:\s|$)")
_NOTE = "\ue002"
_MARKUP = (
    ("div fence", re.compile(r"^:::", re.M)),
    ("attribute", re.compile(r"\{[.#][\w-]")),
    ("link", re.compile(r"\]\(")),
    ("image", re.compile(r"!\[")),
)
_MACRO = re.compile(r"\\(" + "|".join(sorted(set(ZERO_ARG) | set(ONE_ARG), key=len, reverse=True)) + r")(?![A-Za-z])")


def _hold(text: str, pattern: re.Pattern, mark: str) -> tuple[str, list[str]]:
    saved: list[str] = []

    def repl(match: re.Match) -> str:
        saved.append(match.group(0))
        return f"{mark}{len(saved) - 1}{mark}"

    return pattern.sub(repl, text), saved


def _release(text: str, saved: list[str], mark: str) -> str:
    return re.sub(
        re.escape(mark) + r"(\d+)" + re.escape(mark),
        lambda match: saved[int(match.group(1))],
        text,
    )


def opening_before_heading(text: str) -> str:
    """Chapter text: everything before the first level-2 heading."""
    kept: list[str] = []
    in_code = False
    for line in text.split("\n"):
        if re.match(r"^\s*```", line):
            in_code = not in_code
            kept.append(line)
            continue
        if not in_code and _H2.match(line) and not line.startswith("###"):
            break
        kept.append(line)
    return "\n".join(kept).strip()


def math_spans(text: str) -> list[str]:
    """Maths spans outside code, in order. Uses ``MATH_SPAN``."""
    found: list[str] = []

    def run(segment: str) -> str:
        found.extend(match.group(0) for match in MATH_SPAN.finditer(segment))
        return segment

    protect_code(text, run)
    return found


# Pandoc turns -- and --- between words into en and em dashes on the site.
# Do the same here, but only between letters, digits or brackets, so a Markdown
# table rule (| --- |) or a horizontal rule (---) is left alone.
_WORD_BEFORE = r"(?<=[^\W_)\]])"
_WORD_AFTER = r"(?=[^\W_(\[])"
_EM_DASH = re.compile(rf"{_WORD_BEFORE}---{_WORD_AFTER}|{_WORD_BEFORE} --- {_WORD_AFTER}")
_EN_DASH = re.compile(rf"{_WORD_BEFORE}--{_WORD_AFTER}|{_WORD_BEFORE} -- {_WORD_AFTER}")


def _dash_prose(text: str) -> str:
    text = _EM_DASH.sub(lambda match: match.group(0).replace("---", "\u2014"), text)
    return _EN_DASH.sub(lambda match: match.group(0).replace("--", "\u2013"), text)


def smart_dashes(text: str) -> str:
    """-- and --- between words become en and em dashes, outside code and maths."""
    shielded, code = _hold(text, _CODE, "\ue000")
    shielded, maths = _hold(shielded, MATH_SPAN, "\ue001")
    return _release(_release(_dash_prose(shielded), maths, "\ue001"), code, "\ue000")


def _strip_prose(text: str) -> str:
    """Attributes, links, images, fences, and dashes. Call only outside code and maths."""
    text = _FENCE_LINE.sub("", text)
    text = _HEADING_ATTR.sub(r"\1", text)
    text = _IMAGE.sub(lambda match: match.group(1), text)
    text = _LINK.sub(lambda match: match.group(1), text)
    text = _QUARTO_ATTR.sub("", text)
    return _dash_prose(text)


def strip_markup(text: str) -> str:
    """Quarto markup out. Maths and code stay as they are.

    Code is shielded the way ``protect_code`` shields it, and maths with
    ``MATH_SPAN``, before any attribute is removed. Attribute braces come off
    only where Pandoc puts them: after a link or image, at the end of a heading,
    and on a fence line. A cited footnote is inserted in brackets at its marker.
    """
    shielded, code = _hold(text, _CODE, "\ue000")
    shielded, maths = _hold(shielded, MATH_SPAN, "\ue001")
    notes: dict[str, str] = {}

    def grab(match: re.Match) -> str:
        notes[match.group(1)] = " ".join(match.group(2).split())
        return f"{_NOTE}{match.group(1)}{_NOTE}"

    shielded = _FOOT_DEF.sub(grab, shielded)
    current = shielded
    used: set[str] = set()

    def put(match: re.Match) -> str:
        body = notes.get(match.group(1), "")
        if not body:
            return ""
        used.add(match.group(1))
        bracketed = f"[{body}]"
        if match.start() and not current[match.start() - 1].isspace():
            return " " + bracketed
        return bracketed

    shielded = _FOOT_MARK.sub(put, current)
    # A note cited in this same text is inlined at the marker. A note that lives
    # only here stays as plain text where the page defined it.
    shielded = re.sub(
        re.escape(_NOTE) + r"(.+?)" + re.escape(_NOTE),
        lambda match: "" if match.group(1) in used else notes.get(match.group(1), ""),
        shielded,
    )
    shielded = _strip_prose(shielded)
    return _release(_release(shielded, maths, "\ue001"), code, "\ue000").strip()


def _text_keeper(item: dict) -> tuple:
    """Who keeps a shared text: a section, otherwise a box, otherwise the lowest id."""
    if item["kind"] == "section":
        band = 0
    elif item["kind"] in BOX_KINDS:
        band = 1
    else:
        band = 2
    return (band, item["id"])


def _prepare_entries(entries: list[dict]) -> None:
    """Expand macros, drop Quarto markup, and keep each distinct text once."""
    damaged: list[str] = []
    for entry in entries:
        text = entry.get("text") or ""
        if entry["kind"] == "chapter":
            text = opening_before_heading(text)
        cleaned = expand_macros(strip_markup(text)).strip()
        if Counter(math_spans(cleaned)) != Counter(math_spans(expand_macros(text))):
            damaged.append(entry["id"])
        entry["text"] = cleaned
        entry["title"] = smart_dashes(expand_macros(entry.get("title") or "")).strip() or entry["id"]
        entry["fingerprint"] = fingerprint(cleaned)
    if damaged:
        raise SystemExit("wiki.json maths changed: " + ", ".join(damaged[:20]))
    groups: dict[str, list[dict]] = {}
    for entry in entries:
        if entry["text"]:
            groups.setdefault(entry["text"], []).append(entry)
    for group in groups.values():
        if len(group) < 2:
            continue
        group.sort(key=_text_keeper)
        canon = group[0]["id"]
        for other in group[1:]:
            other.pop("text", None)
            other["copy_of"] = canon


def _check_chat_source(entries: list[dict], edges: list[dict]) -> None:
    """The chatbot file: published urls, one copy of each text, no Quarto markup."""
    by_id = {entry["id"]: entry for entry in entries}
    problems: list[str] = []
    seen: dict[str, str] = {}
    for entry in entries:
        if ".qmd" in entry["url"]:
            problems.append(f"qmd url {entry['id']}")
        title = entry.get("title") or ""
        found = _MACRO.search(title)
        if found:
            problems.append(f"macro in title {entry['id']}: {found.group(0)}")
        if "copy_of" in entry:
            if "text" in entry:
                problems.append(f"copy keeps text {entry['id']}")
            if entry["copy_of"] not in by_id:
                problems.append(f"copy_of missing target {entry['id']}")
            continue
        text = entry.get("text") or ""
        if not text:
            continue
        if "_^" in text or "^_" in text:
            problems.append(f"broken maths in {entry['id']}")
        found = _MACRO.search(text)
        if found:
            problems.append(f"macro in text {entry['id']}: {found.group(0)}")
        for name, pattern in _MARKUP:
            if pattern.search(text):
                problems.append(f"{name} in {entry['id']}")
                break
        prior = seen.get(text)
        if prior:
            problems.append(f"duplicate text {entry['id']} and {prior}")
        else:
            seen[text] = entry["id"]
    for edge in edges:
        if edge["type"] != "in":
            continue
        section = by_id.get(edge["from"])
        chapter = by_id.get(edge["to"])
        if not section or not chapter or section.get("kind") != "section" or chapter.get("kind") != "chapter":
            continue
        body = section.get("text") or ""
        opening = chapter.get("text") or ""
        if body and opening and body in opening:
            problems.append(f"chapter {chapter['id']} contains {section['id']}")
    if problems:
        raise SystemExit("wiki.json chat source: " + "; ".join(problems[:20]))


def _near(left: dict, right: dict) -> bool:
    if "text" not in left or "text" not in right:
        return False
    a, b = left["text"], right["text"]
    if a == b:
        return True
    if not a or not b:
        return False
    return difflib.SequenceMatcher(a=a, b=b).ratio() >= 0.9


def check_identity(previous: list[dict], current: list[dict], aliases: dict[str, str]) -> list[str]:
    """Compare a committed id set with the ids just built.

    A vanished section or figure is a warning. A vanished question, answer,
    box, or worked example fails unless an alias points at an id this build
    emitted. An alias whose target was not emitted fails. A new id fails
    unless it is the target of such an alias.
    """
    produced = {item["id"]: item for item in current}
    committed = {item["id"]: item for item in previous}
    errors: list[str] = []
    for src, dst in aliases.items():
        if dst not in produced:
            errors.append(f"alias {src} names {dst}, which was not emitted")

    vanished = set(committed) - set(produced)
    appeared = set(produced) - set(committed)
    accounted = {src for src in vanished if aliases.get(src) in produced}
    explained = {aliases[src] for src in accounted}
    warnings = sorted(src for src in vanished - accounted if committed[src].get("kind") in WARN_KINDS)
    hard_old = sorted(src for src in vanished - accounted if committed[src].get("kind") not in WARN_KINDS)
    hard_new = sorted(appeared - explained)

    pairs = [
        (src, dst)
        for src in hard_old
        for dst in hard_new
        if committed[src].get("kind") == produced[dst].get("kind") and _near(committed[src], produced[dst])
    ]
    if hard_old or hard_new or errors:
        parts = list(errors)
        parts.extend(f"vanished {committed[src].get('kind')} {src}" for src in hard_old)
        parts.extend(f"new id {dst}" for dst in hard_new)
        if len(pairs) == 1:
            src, dst = pairs[0]
            parts.append(f"near-identical new id {dst} for vanished {src}")
        raise SystemExit("identity registry: " + "; ".join(parts))
    return warnings


def _add(entries: list[dict], seen: set[str], *, ident: str, kind: str, title: str, text: str, url: str) -> None:
    if ident in seen:
        raise SystemExit(f"duplicate id {ident}")
    seen.add(ident)
    body = text or ""
    entries.append(
        {
            "id": ident,
            "kind": kind,
            "title": title or ident,
            "text": body,
            "url": url,
            "fingerprint": fingerprint(body),
        }
    )


def _check_urls(entries: list[dict], root: Path) -> None:
    cache: dict[Path, str] = {}

    def contents(path: Path) -> str:
        if path not in cache:
            cache[path] = path.read_text(encoding="utf-8")
        return cache[path]

    for entry in entries:
        url = entry["url"]
        if not url.startswith("/"):
            raise SystemExit(f"url is not root-relative: {url}")
        if ".qmd" in url:
            raise SystemExit(f"url names a source file: {url}")
        path_part, _, fragment = url.partition("#")
        file = root / path_part.lstrip("/")
        if path_part.endswith(".html"):
            file = file.with_suffix(".qmd")
        if not file.is_file():
            raise SystemExit(f"url is not a file the build wrote: {url}")
        if fragment and not re.search(rf"#{re.escape(fragment)}(?![A-Za-z0-9_-])", contents(file)):
            raise SystemExit(f"fragment {fragment} is missing from {path_part}")


def _pair_answers(questions: list[dict], answers: list[dict]) -> list[tuple[dict, dict]]:
    by_id = {(q["group"], q["id"]): q for q in questions}
    by_answer = {(q["group"], q["answer_id"]): q for q in questions if q.get("answer_id")}
    pairs = []
    for answer in answers:
        question = None
        if answer.get("question_id"):
            question = by_id.get((answer["group"], answer["question_id"]))
        if question is None and answer.get("id"):
            question = by_answer.get((answer["group"], answer["id"]))
        if question is None:
            raise SystemExit(f"answer {answer.get('group')} {answer.get('id')} has no question")
        pairs.append((answer, question))
    return pairs


def _terms_source(code: str, key: str, articles: dict) -> str:
    if code == "ART":
        box = (articles.get(key) or {}).get("box")
        if box and box.get("chapter") is not None:
            return chapter_id(Path(box["chapter"]).name)
        return chapter_id(DIST_STEM + ".qmd")
    return chapter_id(CHAPTER_CODES[code])


def _resolve_term(code: str, key: str, ids: set[str], articles: dict, heading_anchors: dict) -> str:
    if code == "ART":
        target = f"article:{key}"
        if key not in articles or target not in ids:
            raise ValueError(f"article {key!r} was not emitted")
        return target
    if code not in CHAPTER_CODES:
        raise ValueError(f"unknown chapter code {code}")
    fname = CHAPTER_CODES[code]
    home = chapter_id(fname)
    if home not in ids:
        raise ValueError(f"chapter {home} was not emitted")
    if key == "":
        return home
    boxed = box_graph_id(key)
    if boxed and key.startswith(("def-", "thm-", "prp-", "cor-", "rem-")):
        if boxed not in ids:
            raise ValueError(f"box {key} was not emitted")
        return boxed
    anchor = heading_anchors.get((fname, plain(key)))
    if anchor is None:
        anchor = heading_anchors.get((fname, key))
    if not anchor:
        raise ValueError(f"no heading {key!r} in {fname}")
    boxed = box_graph_id(anchor)
    if boxed and str(anchor).startswith(("def-", "thm-", "prp-", "cor-", "rem-")):
        if boxed not in ids:
            raise ValueError(f"box {anchor} was not emitted")
        return boxed
    target = section_id(fname, anchor)
    if target not in ids:
        raise ValueError(f"section {target} was not emitted")
    return target


def _article_target(article: dict, ids: set[str]) -> str | None:
    box = article.get("box")
    if not box:
        return None
    kind = box.get("kind")
    anchor = box.get("anchor") or ""
    if not anchor:
        return None
    if kind in BOX_KINDS:
        return f"{kind}:{anchor}"
    if kind == "section":
        return section_id(Path(box["chapter"]).name, anchor)
    if kind == "topic":
        candidate = section_id(Path(box["chapter"]).name, anchor)
        if candidate in ids:
            return candidate
    return None


def build_document(
    notes: dict,
    questions: list[dict],
    answers: list[dict],
    articles: dict,
    glossary: list[dict],
    heading_anchors: dict,
    examples: dict,
    figures: dict,
    sections: dict,
    *,
    root: Path | None = None,
    terms=None,
    retired: dict[str, tuple[str, str]] | None = None,
    merged: dict[str, str] | None = None,
) -> dict:
    """One graph document. Every url is a published path for a file under ``root``.

    ``retired`` maps the slug of a published article the build no longer makes
    to the (chapter file, heading id) its address now redirects to. Each becomes
    an alias from the article's id to that section's id.
    """
    root = root or WIKI
    rows = TERMS if terms is None else terms
    entries: list[dict] = []
    seen: set[str] = set()

    for filename, note in notes.items():
        if note.get("kind") != "notes":
            continue
        _add(
            entries,
            seen,
            ident=chapter_id(filename),
            kind="chapter",
            title=note.get("title") or Path(filename).stem,
            text=note.get("prose") or "",
            url=root_url(note["path"], root),
        )

    section_titles = {
        (item["page"].name, item["anchor"]): item.get("term") or item["anchor"]
        for item in glossary
        if item.get("kind") == "section"
    }
    for (fname, anchor), text in sections.items():
        _add(
            entries,
            seen,
            ident=section_id(fname, anchor),
            kind="section",
            title=section_titles.get((fname, anchor), anchor),
            text=text or "",
            url=root_url(root / "notes" / fname, root, anchor),
        )

    lines_for: dict[str, list[str]] = {}
    for article in articles.values():
        box = article.get("box")
        if box and box.get("kind") in BOX_KINDS and box.get("anchor"):
            lines_for[box["anchor"]] = list(box.get("lines") or [])
        for extra in article.get("extra_boxes") or []:
            if extra.get("kind") in BOX_KINDS and extra.get("anchor"):
                lines_for[extra["anchor"]] = list(extra.get("lines") or [])
    for item in glossary:
        if item.get("kind") not in BOX_KINDS:
            continue
        anchor = item["anchor"]
        body = "\n".join(lines_for.get(anchor) or [])
        if not body:
            body = item.get("snippet") or ""
        _add(
            entries,
            seen,
            ident=f"{item['kind']}:{anchor}",
            kind=item["kind"],
            title=item.get("term") or anchor,
            text=body,
            url=root_url(item["page"], root, anchor),
        )

    for ident, example in examples.items():
        _add(
            entries,
            seen,
            ident=f"example:{ident}",
            kind="example",
            title=example.get("title") or ident,
            text="\n".join(example.get("lines") or []),
            url=root_url(example["chapter"], root, ident),
        )

    cards: dict[str, dict] = {}
    for article in articles.values():
        card = article.get("card")
        if card and card.get("anchor"):
            cards.setdefault(card["anchor"], card)
    if cards:
        dist_path = root / DIST_FILE
        if not dist_path.is_file():
            raise SystemExit(f"url is not a file the build wrote: /{DIST_FILE.as_posix()}")
        dist_text = dist_path.read_text(encoding="utf-8")
        dist_text = re.sub(r"\A---\n.*?\n---\n+", "", dist_text, count=1, flags=re.S)
        _add(
            entries,
            seen,
            ident=chapter_id(DIST_STEM + ".qmd"),
            kind="chapter",
            title="Common distributions",
            text=dist_text.strip(),
            url=root_url(dist_path, root),
        )
        for anchor, card in cards.items():
            _add(
                entries,
                seen,
                ident=section_id(DIST_STEM + ".qmd", anchor),
                kind="section",
                title=card.get("name") or anchor,
                text=card.get("body") or "",
                url=root_url(dist_path, root, anchor),
            )

    for article in articles.values():
        parts = []
        box = article.get("box") or {}
        if box.get("lines"):
            parts.append("\n".join(box["lines"]))
        if box.get("lead"):
            parts.append(box["lead"])
        if box.get("excerpts"):
            parts.append("\n\n".join(piece["text"] for piece in box["excerpts"] if piece.get("text")))
        if article.get("card") and article["card"].get("body"):
            parts.append(article["card"]["body"])
        for extra in article.get("extra_boxes") or []:
            if extra.get("lines"):
                parts.append("\n".join(extra["lines"]))
        for extra in article.get("extra_sections") or []:
            if extra.get("text"):
                parts.append(extra["text"])
        _add(
            entries,
            seen,
            ident=f"article:{article['slug']}",
            kind="article",
            title=article.get("term") or article["slug"],
            text="\n\n".join(part for part in parts if part),
            url=root_url(article["path"], root),
        )

    for question in questions:
        _add(
            entries,
            seen,
            ident=question_graph_id(question),
            kind="question",
            title=question.get("title") or question["id"],
            text=question.get("prepared_body") or question.get("body") or "",
            url=root_url(question["path"], root),
        )

    aliases: dict[str, str] = {}
    for answer, question in _pair_answers(questions, answers):
        qid = question_graph_id(question)
        aid = answer_graph_id(qid)
        _add(
            entries,
            seen,
            ident=aid,
            kind="answer",
            title=answer.get("title") or aid,
            text=question.get("prepared_answer") or answer.get("body") or "",
            url=root_url(question["path"], root, "worked-answer"),
        )
        sol = answer.get("id") or ""
        if sol.startswith("sol-"):
            aliases["answer:" + sol] = aid
    for old, (fname, anchor) in sorted((retired or {}).items()):
        aliases[f"article:{old}"] = section_id(fname, anchor)
    for old, canon in sorted((merged or {}).items()):
        aliases[f"article:{old}"] = f"article:{canon}"

    for filename, info in figures.items():
        anchor = info.get("id") or ""
        ident = f"figure:{anchor}" if anchor.startswith("fig-") else f"figure:{filename}"
        _add(
            entries,
            seen,
            ident=ident,
            kind="figure",
            title=info.get("caption") or filename,
            text=info.get("caption") or "",
            url="/" + Path("figures", filename).as_posix(),
        )

    _prepare_entries(entries)
    entries.sort(key=lambda item: item["id"])
    ids = {item["id"] for item in entries}
    _check_urls(entries, root)
    question_urls = {item["url"].split("#", 1)[0] for item in entries if item["kind"] == "question"}
    for question in questions:
        url = root_url(question["path"], root)
        if url not in question_urls:
            raise SystemExit(f"question page has no entry: {url}")

    edges: list[dict] = []

    def edge(src: str, kind: str, dst: str) -> None:
        edges.append({"from": src, "type": kind, "to": dst})

    for question in questions:
        if question.get("group") in {"practice", "concepts"}:
            fname = question.get("topic") or ""
        else:
            fname = question.get("chapter_file") or question.get("topic") or ""
        edge(question_graph_id(question), "on", chapter_id(fname))
    for _answer, question in _pair_answers(questions, answers):
        qid = question_graph_id(question)
        edge(answer_graph_id(qid), "of", qid)
    for item in glossary:
        if item.get("kind") in BOX_KINDS:
            edge(f"{item['kind']}:{item['anchor']}", "stated-in", chapter_id(item["page"].name))
    for ident, example in examples.items():
        edge(f"example:{ident}", "stated-in", chapter_id(Path(example["chapter"]).name))
    for (fname, anchor) in sections:
        edge(section_id(fname, anchor), "in", chapter_id(fname))
    for anchor in cards:
        edge(section_id(DIST_STEM + ".qmd", anchor), "in", chapter_id(DIST_STEM + ".qmd"))
    for article in articles.values():
        src = f"article:{article['slug']}"
        target = _article_target(article, ids)
        if target:
            edge(src, "for", target)
        for extra in article.get("extra_boxes") or []:
            if extra.get("kind") in BOX_KINDS and extra.get("anchor"):
                extra_target = f"{extra['kind']}:{extra['anchor']}"
                if extra_target in ids:
                    edge(src, "for", extra_target)
        for extra in article.get("extra_sections") or []:
            if extra.get("chapter") is not None and extra.get("anchor"):
                sec_target = section_id(Path(extra["chapter"]).name, extra["anchor"])
                if sec_target in ids:
                    edge(src, "for", sec_target)
        card = article.get("card")
        if card and card.get("anchor"):
            edge(src, "for", section_id(DIST_STEM + ".qmd", card["anchor"]))

    problems = []
    for row in rows:
        pattern, code, key = row[0], row[1], row[2]
        try:
            target = _resolve_term(code, key, ids, articles, heading_anchors)
        except ValueError as exc:
            problems.append(f"TERMS row {pattern!r} ({code} -> {key!r}) {exc}")
            continue
        src = _terms_source(code, key, articles)
        if src != target:
            edge(src, "defines", target)
    if problems:
        raise SystemExit("\n".join(problems[:30]))

    unique = []
    seen_edges: set[tuple[str, str, str]] = set()
    for item in edges:
        key = (item["from"], item["type"], item["to"])
        if key in seen_edges:
            continue
        seen_edges.add(key)
        unique.append(item)
    unique.sort(key=lambda item: (item["from"], item["type"], item["to"]))
    missing = [
        f"{item['from']} -{item['type']}-> {item['to']}"
        for item in unique
        if item["from"] not in ids or item["to"] not in ids
    ]
    if missing:
        raise SystemExit("dangling edge: " + "; ".join(missing[:20]))

    for src, dst in aliases.items():
        if dst not in ids:
            raise SystemExit(f"alias {src} names {dst}, which was not emitted")

    _check_chat_source(entries, unique)
    return {"version": 2, "aliases": aliases, "entries": entries, "edges": unique}


def _read_registry(path: Path) -> tuple[list[dict], dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    previous = [{"id": ident, "kind": kind} for ident, kind in data.get("ids", {}).items()]
    aliases = {str(src): str(dst) for src, dst in data.get("aliases", {}).items()}
    return previous, aliases


def _registry_payload(entries: list[dict], aliases: dict[str, str]) -> dict:
    return {"aliases": aliases, "ids": {item["id"]: item["kind"] for item in entries}}


def _merge_aliases(produced: dict[str, str], previous: dict[str, str], ids: set[str]) -> dict[str, str]:
    merged: dict[str, str] = {}
    for src, dst in previous.items():
        if dst in ids:
            merged[src] = dst
    for src, dst in produced.items():
        if dst not in ids:
            raise SystemExit(f"alias {src} names {dst}, which was not emitted")
        merged[src] = dst
    return merged


def save_graph(document: dict, *, wiki_path: Path, registry_path: Path, update_ids: bool) -> list[str]:
    """Write ``wiki.json``. Write the id registry only when ``update_ids`` is set."""
    entries = document["entries"]
    ids = {item["id"] for item in entries}
    previous: list[dict] = []
    previous_aliases: dict[str, str] = {}
    if registry_path.exists():
        previous, previous_aliases = _read_registry(registry_path)
    document["aliases"] = _merge_aliases(document.get("aliases") or {}, previous_aliases, ids)
    payload = json.dumps(document, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    registry = json.dumps(_registry_payload(entries, document["aliases"]), ensure_ascii=False, indent=2, sort_keys=True) + "\n"

    if update_ids:
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        registry_path.write_text(registry, encoding="utf-8")
        wiki_path.write_text(payload, encoding="utf-8")
        return []

    if not registry_path.exists():
        raise SystemExit("graph/ids.json is missing; run python build_wiki.py --update-ids")
    before = registry_path.read_bytes()
    warnings = check_identity(previous, entries, previous_aliases)
    if registry_path.read_bytes() != before:
        raise SystemExit("registry check wrote graph/ids.json")
    wiki_path.write_text(payload, encoding="utf-8")
    return warnings


def write_graph(
    notes: dict,
    questions: list[dict],
    answers: list[dict],
    articles: dict,
    glossary: list[dict],
    heading_anchors: dict,
    examples: dict,
    figures: dict,
    sections: dict,
    *,
    update_ids: bool,
    root: Path | None = None,
    wiki_path: Path | None = None,
    registry_path: Path | None = None,
    terms=None,
    retired: dict[str, tuple[str, str]] | None = None,
    merged: dict[str, str] | None = None,
) -> list[str]:
    root = root or WIKI
    document = build_document(
        notes,
        questions,
        answers,
        articles,
        glossary,
        heading_anchors,
        examples,
        figures,
        sections,
        root=root,
        terms=terms,
        retired=retired,
        merged=merged,
    )
    return save_graph(
        document,
        wiki_path=wiki_path or (root / "wiki.json"),
        registry_path=registry_path or (root / "graph" / "ids.json"),
        update_ids=update_ids,
    )
