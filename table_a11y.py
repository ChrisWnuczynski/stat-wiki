"""Captions, column scope, and row headers for rendered tables.

Pandoc turns markdown tables into HTML with no caption and no scope, and it
puts the row label in a ``td``. A screen reader then hears the numbers
without the label that gives them a meaning. This pass runs on the pages
Quarto has already written, so it covers chapter tables, research tables,
question tables, the glossary, and infoboxes together.

A synthesised caption is visually hidden. The page already shows a heading
or the infobox title, and the caption repeats that for assistive technology.
A caption the author wrote is left as it is.
"""

from __future__ import annotations

import re
import sys
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE_DIR = ROOT / "_site"

_SKIP_TAGS = {"nav", "footer"}
_HEADING = {"h1", "h2", "h3", "h4", "h5", "h6"}
_SECTION = {"thead", "tbody", "tfoot"}


def _classes(attrs) -> set[str]:
    for key, value in attrs:
        if key == "class" and value:
            return set(value.split())
    return set()


def _attr(attrs, name: str) -> str | None:
    for key, value in attrs:
        if key == name:
            return value
    return None


def _plain(fragment: str) -> str:
    text = re.sub(r"<[^>]+>", " ", fragment)
    text = unescape(text)
    text = text.replace(r"\(", " ").replace(r"\)", " ").replace(r"\[", " ").replace(r"\]", " ")
    text = text.replace("$", " ")
    return re.sub(r"\s+", " ", text).strip()


class _Tables(HTMLParser):
    """Content tables, each with the heading or infobox title that precedes it."""

    def __init__(self, text: str) -> None:
        super().__init__(convert_charrefs=False)
        self.text = text
        self.line_starts = [0]
        for index, char in enumerate(text):
            if char == "\n":
                self.line_starts.append(index + 1)
        self.main = 0
        self.skip: list[str] = []
        self.div_infobox: list[bool] = []
        self.infobox: list[str] = []
        self.capture: list[str] | None = None
        self.capture_kind: str | None = None
        self.capture_depth = 0
        self.heading = ""
        self.tables: list[tuple[int, int, str, bool]] = []
        self._open: list[tuple[int, str, bool]] = []

    def _pos(self) -> int:
        line, column = self.getpos()
        return self.line_starts[line - 1] + column

    def _add_text(self, text: str) -> None:
        if self.capture is not None and not self.skip:
            self.capture.append(text)

    def handle_starttag(self, tag: str, attrs) -> None:
        position = self._pos()
        classes = _classes(attrs)
        if tag == "main":
            self.main += 1
        if tag in _SKIP_TAGS or (tag == "header" and self.main == 0):
            self.skip.append(tag)
        if tag == "div":
            is_box = "infobox" in classes
            self.div_infobox.append(is_box)
            if is_box:
                self.infobox.append("")
        if self.capture is not None:
            self.capture_depth += 1
        elif not self.skip and self.main and tag in _HEADING:
            self.capture = []
            self.capture_kind = "heading"
            self.capture_depth = 1
        elif not self.skip and "infobox-title" in classes:
            self.capture = []
            self.capture_kind = "title"
            self.capture_depth = 1
        if tag != "table":
            return
        if self.skip:
            self._open.append((-1, "", False))
            return
        hint = self.infobox[-1] if self.infobox else self.heading
        self._open.append((position, hint, bool(self.infobox)))

    def handle_endtag(self, tag: str) -> None:
        if tag == "table" and self._open:
            start, hint, infobox = self._open.pop()
            if start >= 0:
                close = self.text.find(">", self._pos())
                if close >= 0:
                    self.tables.append((start, close + 1, hint, infobox))
        if self.capture is not None:
            self.capture_depth -= 1
            if self.capture_depth == 0:
                text = re.sub(r"\s+", " ", "".join(self.capture)).strip()
                if self.capture_kind == "heading" and self.main and not self.skip:
                    self.heading = text
                elif self.capture_kind == "title" and self.infobox:
                    self.infobox[-1] = text
                self.capture = None
                self.capture_kind = None
        if tag == "div" and self.div_infobox:
            if self.div_infobox.pop() and self.infobox:
                self.infobox.pop()
        if tag == "main" and self.main:
            self.main -= 1
        if self.skip and tag == self.skip[-1]:
            self.skip.pop()

    def handle_startendtag(self, tag: str, attrs) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        self._add_text(data)

    def handle_entityref(self, name: str) -> None:
        self._add_text(unescape(f"&{name};"))

    def handle_charref(self, name: str) -> None:
        self._add_text(unescape(f"&#{name};"))


def _tag_end(text: str, start: int) -> int:
    quote = ""
    for index in range(start, len(text)):
        char = text[index]
        if quote:
            if char == quote:
                quote = ""
            continue
        if char in "\"'":
            quote = char
        elif char == ">":
            return index
    raise ValueError("Unclosed tag")


class _Cells(HTMLParser):
    def __init__(self, text: str) -> None:
        super().__init__(convert_charrefs=False)
        self.text = text
        self.line_starts = [0]
        for index, char in enumerate(text):
            if char == "\n":
                self.line_starts.append(index + 1)
        self.section = "body"
        self.rows: list[dict] = []
        self._row: dict | None = None
        self._cell: dict | None = None
        self.role = ""
        self.has_caption = False
        self.table_end = 0
        self.depth = 0

    def _pos(self) -> int:
        line, column = self.getpos()
        return self.line_starts[line - 1] + column

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag == "table":
            self.depth += 1
            if self.depth == 1:
                position = self._pos()
                self.role = (_attr(attrs, "role") or "").lower()
                self.table_end = _tag_end(self.text, position) + 1
            return
        if self.depth != 1:
            return
        if tag == "caption":
            self.has_caption = True
        elif tag in _SECTION:
            self.section = tag
        elif tag == "tr" and self._cell is None:
            self._row = {"section": self.section, "cells": []}
        elif tag in {"td", "th"} and self._row is not None and self._cell is None:
            position = self._pos()
            self._cell = {
                "tag": tag,
                "start": position,
                "open_end": _tag_end(self.text, position),
                "attrs": attrs,
            }

    def handle_endtag(self, tag: str) -> None:
        if tag == "table":
            if self.depth:
                self.depth -= 1
            return
        if self.depth != 1:
            return
        if tag in {"td", "th"} and self._cell is not None and self._cell["tag"] == tag:
            self._cell["close"] = self._pos()
            if self._row is not None:
                self._row["cells"].append(self._cell)
            self._cell = None
        elif tag == "tr" and self._row is not None and self._cell is None:
            self.rows.append(self._row)
            self._row = None
        elif tag in _SECTION and self.section == tag:
            self.section = "body"

    def handle_startendtag(self, tag: str, attrs) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)


def _caption_text(hint: str, headers: list[str], infobox: bool) -> str:
    hint = re.sub(r"\s+", " ", hint).strip()
    headers = [header for header in headers if header]
    if infobox and hint:
        text = hint
    elif hint and headers:
        joined = ", ".join(headers[:8])
        if len(headers) > 8:
            joined += "…"
        text = hint if joined.lower() in hint.lower() else f"{hint}: {joined}"
    else:
        text = hint or ", ".join(headers[:8]) or "Data table"
    if len(text) > 180:
        text = text[:179].rstrip() + "…"
    return text


def rewrite_table(table_html: str, hint: str, infobox: bool) -> str:
    """Return the table with a caption, column scope, and row headers."""
    parsed = _Cells(table_html)
    parsed.feed(table_html)
    parsed.close()
    if parsed.role in {"presentation", "none"} or not parsed.rows:
        return table_html
    headers: list[str] = []
    for row in parsed.rows:
        if row["section"] == "thead":
            for cell in row["cells"]:
                headers.append(_plain(table_html[cell["open_end"] + 1 : cell["close"]]))
            break
    edits: list[tuple[int, int, str]] = []
    if not parsed.has_caption:
        caption = escape(_caption_text(hint, headers, infobox))
        snippet = f'\n<caption class="a11y-caption">{caption}</caption>'
        edits.append((parsed.table_end, parsed.table_end, snippet))
    for row in parsed.rows:
        cells = row["cells"]
        header_row = row["section"] == "thead" or bool(cells) and all(cell["tag"] == "th" for cell in cells)
        for index, cell in enumerate(cells):
            tag = cell["tag"]
            scope = _attr(cell["attrs"], "scope")
            open_end = cell["open_end"]
            if header_row and tag == "th" and not scope:
                edits.append((open_end, open_end, ' scope="col"'))
            elif not header_row and index == 0 and len(cells) > 1:
                if tag == "td":
                    if table_html[cell["start"] + 1 : cell["start"] + 3].lower() != "td":
                        continue
                    edits.append((cell["start"] + 1, cell["start"] + 3, "th"))
                    close = cell["close"]
                    if table_html[close : close + 5].lower() == "</td>":
                        edits.append((close, close + 5, "</th>"))
                    if not scope:
                        edits.append((open_end, open_end, ' scope="row"'))
                elif tag == "th" and not scope:
                    edits.append((open_end, open_end, ' scope="row"'))
    if not edits:
        return table_html
    # A scope insertion shifts the close tag of that cell. Apply from the right.
    for start, end, new in sorted(edits, key=lambda item: (item[0], item[1]), reverse=True):
        table_html = table_html[:start] + new + table_html[end:]
    return table_html


def accessible_tables(html: str) -> str:
    """Add captions and header scope to content tables. Already-fixed HTML is unchanged."""
    finder = _Tables(html)
    finder.feed(html)
    finder.close()
    pending = [list(item) for item in finder.tables]
    while pending:
        leaves = [
            item
            for item in pending
            if not any(item[0] < other[0] and other[1] < item[1] for other in pending)
        ]
        if not leaves:
            break
        leaf_ids = {id(item) for item in leaves}
        for start, end, hint, infobox in sorted(leaves, key=lambda item: item[0], reverse=True):
            new = rewrite_table(html[start:end], str(hint), bool(infobox))
            delta = len(new) - (end - start)
            html = html[:start] + new + html[end:]
            for item in pending:
                if id(item) in leaf_ids:
                    continue
                if item[0] >= end:
                    item[0] += delta
                    item[1] += delta
                elif item[0] < start and item[1] >= end:
                    item[1] += delta
        pending = [item for item in pending if id(item) not in leaf_ids]
    return html


def main(site_dir: Path = SITE_DIR) -> None:
    if not site_dir.is_dir():
        raise SystemExit(f"Missing site: {site_dir}")
    changed = 0
    tables = 0
    for path in sorted(site_dir.rglob("*.html")):
        if "site_libs" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if "<title>Redirect</title>" in text and "var redirects" in text:
            continue
        if "<table" not in text.lower():
            continue
        updated = accessible_tables(text)
        tables += updated.lower().count("<table")
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    print(f"Table captions and headers on {changed} pages ({tables} tables)")


if __name__ == "__main__":
    sys.exit(main() or 0)
