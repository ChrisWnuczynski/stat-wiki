"""Turn \\( \\) and \\[ \\] into Pandoc dollar maths.

Pandoc's default markdown does not treat a backslash-parenthesis as maths, so a
command inside one is dropped and the reader sees empty brackets. Dollar
delimiters are the form this site already renders.

The converter leaves fenced and inline code alone, leaves an escaped
backslash-parenthesis alone, and does not touch maths that is already in
dollars. Display maths is placed on its own lines. A closing single dollar is
never left immediately before a digit, which Pandoc would read as currency.
"""

from __future__ import annotations

import re

_FENCE = re.compile(r"(?ms)^(```+|~~~+)[^\n]*\n.*?\n\1[ \t]*$")


def convert_tex_delimiters(text: str) -> str:
    """Replace TeX-style maths delimiters with $ and $$."""
    return _convert_fenced(text)


def tex_delimiter_offenders(text: str) -> list[str]:
    """Snippets of \\( or \\[ outside code and outside dollar maths."""
    hits: list[str] = []
    for segment in _plain_segments(text):
        hits.extend(_odd_backslash_hits(segment))
    return hits


def _convert_fenced(text: str) -> str:
    out: list[str] = []
    pos = 0
    for match in _FENCE.finditer(text):
        out.append(_convert_inline_code(text[pos : match.start()]))
        out.append(match.group(0))
        pos = match.end()
    out.append(_convert_inline_code(text[pos:]))
    return "".join(out)


def _convert_inline_code(text: str) -> str:
    out: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] != "`":
            nxt = text.find("`", i)
            chunk = text[i:] if nxt < 0 else text[i:nxt]
            out.append(_convert_math(chunk))
            if nxt < 0:
                break
            i = nxt
            continue
        ticks = 1
        while i + ticks < n and text[i + ticks] == "`":
            ticks += 1
        close = text.find("`" * ticks, i + ticks)
        if close < 0:
            out.append(_convert_math(text[i:]))
            break
        out.append(text[i : close + ticks])
        i = close + ticks
    return "".join(out)


def _convert_math(text: str) -> str:
    out: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        if text.startswith("\\$", i):
            out.append(text[i : i + 2])
            i += 2
            continue
        if text[i] == "$":
            if text.startswith("$$", i):
                close = text.find("$$", i + 2)
                if close < 0:
                    out.append(text[i:])
                    break
                out.append(text[i : close + 2])
                i = close + 2
                continue
            close = _find_single_dollar(text, i + 1)
            if close < 0:
                out.append(text[i:])
                break
            out.append(text[i : close + 1])
            i = close + 1
            continue
        if text[i] == "\\":
            j = i
            while j < n and text[j] == "\\":
                j += 1
            run = j - i
            if j < n and text[j] in "([ " and run % 2 == 1 and text[j] in "([":
                out.append("\\" * (run - 1))
                repl, i = _take_delimited(text, j - 1)
                if repl.endswith("$") and not repl.endswith("$$") and i < n and (text[i].isdigit() or text[i] == "$"):
                    repl += " "
                prev = "".join(out)
                out.append(_fit_display(prev, repl))
                continue
            out.append(text[i:j])
            i = j
            continue
        out.append(text[i])
        i += 1
    return "".join(out)


def _find_single_dollar(text: str, start: int) -> int:
    i = start
    while i < len(text):
        if text.startswith("\\$", i):
            i += 2
            continue
        if text[i] == "$":
            return i
        i += 1
    return -1


def _take_delimited(text: str, start: int) -> tuple[str, int]:
    """start points at the backslash of \\( or \\[."""
    opener = text[start + 1]
    closer = ")" if opener == "(" else "]"
    open_pair = "\\" + opener
    close_pair = "\\" + closer
    depth = 1
    j = start + 2
    n = len(text)
    while j < n:
        if text[j] == "\\" and j + 1 < n:
            pair = text[j : j + 2]
            if pair == open_pair:
                depth += 1
                j += 2
                continue
            if pair == close_pair:
                depth -= 1
                if depth == 0:
                    return _format_math(text[start + 2 : j], display=opener == "["), j + 2
                j += 2
                continue
            j += 2
            continue
        j += 1
    return text[start : start + 2], start + 2


def _format_math(inner: str, display: bool) -> str:
    converted = _convert_math(inner)
    multiline = display or "\n" in inner
    if multiline:
        body = "\n".join(line.strip() for line in converted.strip().split("\n"))
        if not body:
            return ("\\[" if display else "\\(") + inner + ("\\]" if display else "\\)")
        return "\n\n$$\n" + body + "\n$$\n\n"
    body = converted.strip()
    if not body:
        return "\\(" + inner + "\\)"
    return f"${body}$"


def _fit_display(prev: str, repl: str) -> str:
    """Don't stack blank lines when display maths already sat on its own line."""
    if not repl.startswith("\n"):
        return repl
    core = repl.strip("\n")
    if not prev:
        return core + ("\n\n" if repl.endswith("\n") else "")
    if prev.endswith("\n\n"):
        lead = ""
    elif prev.endswith("\n"):
        lead = "\n"
    else:
        lead = "\n\n"
    tail = "\n\n" if repl.endswith("\n") else ""
    return lead + core + tail


def _plain_segments(text: str):
    """Text outside fenced code, inline code, and dollar maths."""
    pos = 0
    for match in _FENCE.finditer(text):
        yield from _plain_outside_inline(text[pos : match.start()])
        pos = match.end()
    yield from _plain_outside_inline(text[pos:])


def _plain_outside_inline(text: str):
    i = 0
    n = len(text)
    while i < n:
        if text[i] != "`":
            nxt = text.find("`", i)
            chunk = text[i:] if nxt < 0 else text[i:nxt]
            yield from _plain_outside_dollars(chunk)
            if nxt < 0:
                break
            i = nxt
            continue
        ticks = 1
        while i + ticks < n and text[i + ticks] == "`":
            ticks += 1
        close = text.find("`" * ticks, i + ticks)
        if close < 0:
            yield from _plain_outside_dollars(text[i:])
            break
        i = close + ticks


def _plain_outside_dollars(text: str):
    i = 0
    n = len(text)
    start = 0
    while i < n:
        if text.startswith("\\$", i):
            i += 2
            continue
        if text[i] == "$":
            if start < i:
                yield text[start:i]
            if text.startswith("$$", i):
                close = text.find("$$", i + 2)
                if close < 0:
                    return
                i = close + 2
            else:
                close = _find_single_dollar(text, i + 1)
                if close < 0:
                    return
                i = close + 1
            start = i
            continue
        i += 1
    if start < n:
        yield text[start:]


def _odd_backslash_hits(segment: str) -> list[str]:
    hits: list[str] = []
    i = 0
    n = len(segment)
    while i < n:
        if segment[i] != "\\":
            i += 1
            continue
        j = i
        while j < n and segment[j] == "\\":
            j += 1
        run = j - i
        if j < n and segment[j] in "([ " and run % 2 == 1 and segment[j] in "([":
            snippet = segment[max(0, i - 24) : j + 24].replace("\n", " ")
            hits.append(snippet.strip())
        i = j if j > i else i + 1
    return hits
