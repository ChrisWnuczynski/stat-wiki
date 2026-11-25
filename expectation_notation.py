"""Fail new non-standard expectation notation, and leave the backlog alone.

The house standard is the ``\\E`` shorthand, which ``build_wiki.expand_macros``
rewrites to ``\\mathbb{E}``.

``read_research_content`` expands ``\\E``, ``\\Var``, and ``\\Cov`` when it
copies ``research/content/*.md`` into an article, after the delimiter
conversion. Those three are not KaTeX commands, so a raw copy is red. A new
or edited ``\\E`` in that tree is blackboard bold on the published page.
The other shorthand is left as written: ``\\Pr`` is already a KaTeX operator,
and the page checks still look for those commands. ``prepare`` expands the
whole shorthand table for chapter, question, and answer sources, and
article-extra notes call ``expand_macros`` directly.

Laboratories are not rewritten. ``\\E``, ``\\Var`` and ``\\Cov`` in
``labs/*.qmd`` render through the ``_katex-macros.html`` header that
``build_wiki.write_katex_macro_header`` adds to every page (STA-140, #170).
The guard accepts ``\\E`` and still fails a new non-standard form in a lab.

Not guarded, and still carrying the old forms: ``distributions.json``,
``research/self-checks.json``, ``article_extras.py``, and ``sources/**/*.qmd``.
Those inputs are left to the normalisation pass.

This module reports three other forms inside maths in ``research/content/*.md``
and ``labs/**/*.qmd``:

- bare italic ``E`` used as the operator
- ``\\mathrm{E}``
- ``\\operatorname{E}`` (a star, as in ``\\operatorname*``, is included)

Generated ``articles/*.qmd`` are not read. ``\\E`` and ``\\mathbb{E}``
pass, including ``\\mathbb E`` and ``\\mathbb EX`` (the font applies to E
and X is its argument).

The check is diff-scoped against the pull-request base (``GITHUB_BASE_REF``,
otherwise ``origin/main``). A maths block includes its delimiters. If any
added or replaced line touches that block, every non-standard operator inside
the block fails, including one that sits on a line the diff did not change.
Wrapping prose ``E(X)`` in new ``$$`` lines, adding ``[X]`` after a bare
``E`` in a display, or deleting a line inside a display so that ``E`` and
``[X]`` become one operator, is therefore a failure. A formula whose block
the diff does not touch is left alone, and so is a file the diff does not
touch. Deleting a prose line outside a formula does not touch that formula. On
``main`` the diff is empty, so the suite stays green. Untracked in-scope
files count as entirely added.
On a pull request, Actions checks out the merge commit. With
``fetch-depth: 2`` the comparison is against that commit's first parent, the
base GitHub merged, so a later push to the base cannot make an untouched
backlog formula look added. A checkout that has no parent falls back to the
merge-base, then to a direct diff against the base ref.

Ambiguous italic E
------------------
The checker does not read the prose around a formula, so it cannot tell an
expectation from another function that happens to be named E.

Bare italic E is reported only when it is applied to an argument. An argument
is an opening ``(``, ``[``, or ``\\{``; a ``\\left`` / ``\\bigl`` style opener;
a vertical bar that starts an absolute value or a condition (``E|X|``, ``E|X``);
or juxtaposition with a following variable or symbol (``E X``, ``EX``,
``E \\hat{X}``, ``E \\log X``). A bar that only closes around the symbol
(``|E|``) is not an argument.

A subscripted E is a quantity name, not the operator, when the subscript is an
index: the letters i, j, k, m, n, r, c, and I, a run of those letters
(``E_{ij}``), an optional sign (``E_{i+}``), or a comma pair (``E_{i,j}``).
That exemption holds even if parentheses follow, so expected counts ``E_i``
and a case loss ``E_i(w)`` or ``E_I(w)`` pass. Any other subscript is the
operator once an argument follows (``E_\\theta(X)``, ``E_q[h]``, ``E_t(h)``).
With no argument, a bare E is not reported: a total expected count ``E``, an
edge set ``|E|``, and ``SS_E`` are quantity names. A loss written ``E(w)`` is
reported, because it has the same shape as ``E(X)``.

``\\mathrm{E}`` and ``\\operatorname{E}`` are reported wherever they occur,
including with a subscript. They are the named non-standard forms, not italic
quantity names. ``\\text{E}``, ``\\textrm{E}``, ``\\mathsf{E}``, and ``E^*(X)``
are not reported. ``\\mathcal{E}`` and ``\\mathbf{E}`` are out of scope.
"""

from __future__ import annotations

import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


_FENCE = re.compile(r"(?ms)^(```+|~~~+)[^\n]*\n.*?\n\1[ \t]*$")
_ENV_OPEN = re.compile(
    r"\\begin\{(align\*?|aligned\*?|equation\*?|gather\*?|gathered\*?|"
    r"multline\*?|eqnarray\*?|flalign\*?|split)\}"
)
_MATHRM = re.compile(r"\\mathrm\s*\{\s*E\s*\}")
_OPERATORNAME = re.compile(r"\\operatorname\s*\*?\s*\{\s*E\s*\}")
# A font command takes only the following E. ``\mathbb EX`` is blackboard E
# applied to X, the same standard form as ``\mathbb{E}X``. TeX needs the space
# so the control word ends before the letter E.
_FONT = re.compile(
    r"\\(?:mathbb|mathbf|boldsymbol|mathcal|mathit|mathsf|widehat|overline|"
    r"tilde|bar|hat|vec|bm)"
    r"(?:\s*\{\s*E\s*\}|\s+E)"
)
_ESHORT = re.compile(r"\\E(?![A-Za-z])")
_INDEX_BODY = re.compile(
    r"^(?:[ijkmnrcI]+|[ijkmnrc][+\-]|[+\-][ijkmnrc]|[ijkmnrc],[ijkmnrc])$"
)
_OPENERS = {"left", "bigl", "Bigl", "biggl", "Biggl", "lvert", "langle", "lbrace"}
_SYMBOLS = {
    "hat", "bar", "tilde", "widehat", "overline", "vec", "dot", "ddot",
    "mathbb", "mathbf", "boldsymbol", "mathcal", "mathit", "mathsf", "bm",
    "frac", "tfrac", "dfrac", "exp", "log", "ln", "sqrt", "sum", "prod",
    "int", "partial", "nabla", "theta", "Theta", "mu", "sigma", "lambda",
    "Lambda", "pi", "phi", "varphi", "psi", "omega", "alpha", "beta",
    "gamma", "delta", "epsilon", "varepsilon", "eta", "xi", "rho", "tau",
    "chi", "Phi", "Psi", "Omega", "Gamma", "Delta", "Sigma",
}
_SPACING = {"quad", "qquad", "enspace", "thinspace", "hspace"}
_CLOSERS = {"right", "rvert", "rbrace", "rangle", "bigr", "Bigr", "biggr", "Biggr"}


class GuardError(Exception):
    """The diff could not be read, so the check must not pass silently."""


@dataclass(frozen=True)
class Violation:
    line: int
    offset: int
    snippet: str
    block_first: int = 0
    block_last: int = 0

    def message(self, path: str) -> str:
        return (
            f"{path}:{self.line}: non-standard expectation `{self.snippet}`; "
            "use the \\E shorthand"
        )


def in_scope(path: str) -> bool:
    """Research prose and laboratory sources. Generated articles are out of scope.

    ``distributions.json``, ``research/self-checks.json``, ``article_extras.py``,
    and ``sources/**/*.qmd`` are not included.
    """
    path = path.replace("\\", "/").lstrip("./")
    if path.startswith("research/content/") and path.endswith(".md") and path.count("/") == 2:
        return True
    return path.startswith("labs/") and path.endswith((".qmd", ".md"))


def _line_span(text: str, start: int, end: int) -> tuple[int, int]:
    """1-based inclusive line numbers covering offsets ``[start, end)``."""
    if end <= start:
        line = text.count("\n", 0, start) + 1
        return line, line
    return text.count("\n", 0, start) + 1, text.count("\n", 0, end - 1) + 1


def find_violations(text: str) -> list[Violation]:
    """Non-standard expectation operators in ``text``, with 1-based lines."""
    found: list[Violation] = []
    seen: set[int] = set()
    for inner_start, inner_end, block_start, block_end in math_spans(text):
        inner = text[inner_start:inner_end]
        block_first, block_last = _line_span(text, block_start, block_end)
        for rel, length in scan_math(inner):
            offset = inner_start + rel
            if offset in seen:
                continue
            seen.add(offset)
            snippet = _snippet(inner, rel, rel + length)
            line = text.count("\n", 0, offset) + 1
            found.append(Violation(line, offset, snippet, block_first, block_last))
    found.sort(key=lambda item: item.offset)
    return found


def _block_line_ranges(text: str) -> list[tuple[int, int]]:
    return [_line_span(text, block_start, block_end) for _a, _b, block_start, block_end in math_spans(text)]


def _lines_meet_a_block(first: int, last: int, blocks: list[tuple[int, int]]) -> bool:
    return any(start <= last and first <= end for start, end in blocks)


def changed_new_lines(old: str, new: str) -> set[int]:
    """1-based lines in ``new`` that edit a maths block.

    Inserts and replacements count directly. A pure deletion counts when the
    removed lines sat inside a maths block: the surviving lines on either side
    of the gap are marked, so the block that remains is checked even though
    none of its own lines were rewritten.
    """
    import difflib

    old_lines = old.splitlines()
    new_lines = new.splitlines()
    matcher = difflib.SequenceMatcher(a=old_lines, b=new_lines)
    changed: set[int] = set()
    old_blocks = _block_line_ranges(old)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag in {"insert", "replace"}:
            changed.update(range(j1 + 1, j2 + 1))
        if tag == "delete" and _lines_meet_a_block(i1 + 1, i2, old_blocks):
            if j1 > 0:
                changed.add(j1)
            if j1 < len(new_lines):
                changed.add(j1 + 1)
    return changed


def violations_touching(text: str, changed: set[int]) -> list[Violation]:
    """Operators whose maths block includes an added or replaced line.

    The block includes its opening and closing delimiters, so a new ``$$``
    line counts as touching the formula it wraps.
    """
    if not changed:
        return []
    return [
        item
        for item in find_violations(text)
        if any(line in changed for line in range(item.block_first, item.block_last + 1))
    ]


def violations_in_changed_spans(old: str, new: str) -> list[Violation]:
    """Operators in maths blocks that ``new`` added or edited relative to ``old``."""
    return violations_touching(new, changed_new_lines(old, new))


def parse_added_lines(diff: str) -> dict[str, set[int]]:
    """Map a path to 1-based new-file line numbers that the unified diff adds."""
    added: dict[str, set[int]] = {}
    path: str | None = None
    new_line = 0
    for line in diff.splitlines():
        if line.startswith("diff --git "):
            path = None
            new_line = 0
            continue
        if line.startswith("+++ "):
            path = _diff_path(line[4:])
            if path is not None:
                added.setdefault(path, set())
            new_line = 0
            continue
        if line.startswith("@@"):
            match = re.search(r"\+(\d+)", line)
            new_line = int(match.group(1)) if match else 0
            continue
        if path is None or new_line <= 0:
            continue
        if line.startswith("+"):
            added[path].add(new_line)
            new_line += 1
        elif line.startswith("-") or line.startswith("\\"):
            continue
        else:
            new_line += 1
    return added


def math_spans(text: str) -> list[tuple[int, int, int, int]]:
    """Maths regions as ``(inner_start, inner_end, block_start, block_end)``.

    The block offsets include the delimiters. Interiors skip fenced and inline
    code. All four values are offsets into ``text``, and ``block_end`` is
    exclusive.
    """
    blanked = _blank_code(text)
    spans: list[tuple[int, int, int, int]] = []
    i = 0
    n = len(blanked)
    while i < n:
        if blanked.startswith("\\$", i):
            i += 2
            continue
        if blanked[i] == "$":
            if blanked.startswith("$$", i):
                close = blanked.find("$$", i + 2)
                if close < 0:
                    i += 2
                    continue
                spans.append((i + 2, close, i, close + 2))
                i = close + 2
                continue
            close = _find_single_dollar(blanked, i + 1)
            if close < 0:
                i += 1
                continue
            spans.append((i + 1, close, i, close + 1))
            i = close + 1
            continue
        if blanked[i] == "\\":
            j = i
            while j < n and blanked[j] == "\\":
                j += 1
            run = j - i
            if j < n and blanked[j] in "([ " and run % 2 == 1 and blanked[j] in "([":
                end = _take_tex_delimiter(blanked, i)
                if end is None:
                    i = j
                    continue
                spans.append((i + 2, end - 2, i, end))
                i = end
                continue
            if run == 1:
                match = _ENV_OPEN.match(blanked, i)
                if match:
                    closer = "\\end{" + match.group(1) + "}"
                    close = blanked.find(closer, match.end())
                    if close >= 0:
                        spans.append((match.end(), close, i, close + len(closer)))
                        i = close + len(closer)
                        continue
            i = j if j > i else i + 1
            continue
        i += 1
    return spans


def scan_math(inner: str) -> list[tuple[int, int]]:
    """``(offset, length)`` of each hit inside one maths interior."""
    hits: list[tuple[int, int]] = []
    for cre in (_MATHRM, _OPERATORNAME):
        for match in cre.finditer(inner):
            hits.append((match.start(), match.end() - match.start()))
    masked = _mask_standard(inner)
    i = 0
    n = len(masked)
    while i < n:
        if masked[i] != "E":
            i += 1
            continue
        if _skipped_letter(inner, i):
            i += 1
            continue
        end = _bare_operator_end(inner, i)
        if end is not None:
            hits.append((i, max(1, end - i)))
        i += 1
    hits.sort()
    return hits


def collect_added_lines(root: Path) -> dict[str, set[int]]:
    """Added in-scope lines in ``root`` relative to the pull-request base."""
    base = resolve_base(root)
    target = _diff_target(root, base)
    diff = _git(root, ["diff", "-U0", "--find-renames", target], check=True)
    added = parse_added_lines(diff.stdout)
    untracked = _git(root, ["ls-files", "--others", "--exclude-standard"], check=True)
    for rel in untracked.stdout.splitlines():
        rel = rel.strip()
        if not rel or not in_scope(rel):
            continue
        file = root / rel
        if not file.is_file():
            continue
        count = file.read_text(encoding="utf-8").count("\n") + 1
        added.setdefault(rel, set()).update(range(1, count + 1))
    return {path: lines for path, lines in added.items() if in_scope(path)}


def resolve_base(root: Path) -> str:
    """Commit-ish the working tree is compared with."""
    override = os.environ.get("EXPECTATION_NOTATION_BASE", "").strip()
    if override:
        if _ref_exists(root, override):
            return override
        raise GuardError(
            "expectation notation: EXPECTATION_NOTATION_BASE "
            f"{override!r} is not a commit in this repository"
        )
    candidates: list[str] = []
    base_ref = os.environ.get("GITHUB_BASE_REF", "").strip()
    if base_ref:
        candidates.append(f"origin/{base_ref}")
    candidates.extend(["origin/main", "main"])
    for candidate in candidates:
        if _ref_exists(root, candidate):
            return candidate
    joined = ", ".join(candidates)
    raise GuardError(
        "expectation notation: no base ref "
        f"(looked for {joined}). Fetch the pull request base and re-run."
    )


def messages_for_repo(root: Path) -> list[str]:
    """Failure lines for expectation operators introduced since the base."""
    base = resolve_base(root)
    target = _diff_target(root, base)
    messages: list[str] = []
    for path, old_path in _changed_files(root, target):
        if not in_scope(path):
            continue
        file = root / path
        if not file.is_file():
            continue
        text = file.read_text(encoding="utf-8")
        changed = set(range(1, text.count("\n") + 2)) if old_path is None else None
        if changed is None:
            old_text = _file_at(root, target, old_path or path)
            changed = changed_new_lines(old_text, text)
        for item in violations_touching(text, changed):
            messages.append(item.message(path))
    return messages


def main() -> int:
    try:
        root = Path(_git(None, ["rev-parse", "--show-toplevel"], check=True).stdout.strip())
        messages = messages_for_repo(root)
    except GuardError as exc:
        print(exc)
        return 1
    if messages:
        print(
            f"expectation notation: {len(messages)} new non-standard form(s). "
            "Use the \\E shorthand."
        )
        for message in messages[:50]:
            print(message)
        extra = len(messages) - 50
        if extra > 0:
            print(f"... and {extra} more")
        return 1
    print("expectation notation: no new non-standard expectation operators")
    return 0


def _snippet(inner: str, start: int, end: int) -> str:
    stop = end
    limit = min(len(inner), start + 60)
    while stop < limit and inner[stop] not in "\n":
        stop += 1
    text = " ".join(inner[start:stop].split())
    text = text.replace("`", "'")
    if len(text) > 80:
        return text[:77] + "..."
    return text


def _skipped_letter(text: str, index: int) -> bool:
    if index > 0 and (text[index - 1].isalpha() or text[index - 1] in "_^"):
        return True
    return _escaped_as_command(text, index)


def _escaped_as_command(text: str, index: int) -> bool:
    slashes = 0
    cursor = index - 1
    while cursor >= 0 and text[cursor] == "\\":
        slashes += 1
        cursor -= 1
    return slashes % 2 == 1


def _bare_operator_end(text: str, index: int) -> int | None:
    """Return the end offset of an operator starting at ``E``, or None."""
    cursor, subscript = _read_scripts(text, index + 1)
    if subscript is not None and _INDEX_BODY.match(re.sub(r"\s+", "", subscript)):
        return None
    if cursor < len(text) and text[cursor].isascii() and text[cursor].isupper():
        if cursor + 1 >= len(text) or not text[cursor + 1].isalpha():
            return cursor + 1
    if _bar_wraps_symbol(text, index, cursor):
        return None
    return _argument_end(text, cursor)


def _read_scripts(text: str, cursor: int) -> tuple[int, str | None]:
    subscript: str | None = None
    while cursor < len(text):
        if text[cursor] == "'":
            cursor += 1
            continue
        if text.startswith("\\prime", cursor) and not (
            cursor + 6 < len(text) and text[cursor + 6].isalpha()
        ):
            cursor += 6
            continue
        if text[cursor] not in "_^":
            break
        kind = text[cursor]
        cursor, body = _read_atom(text, cursor + 1)
        if kind == "_" and subscript is None:
            subscript = body
    return cursor, subscript


def _read_atom(text: str, cursor: int) -> tuple[int, str]:
    if cursor >= len(text):
        return cursor, ""
    if text[cursor] == "{":
        depth = 1
        cursor += 1
        start = cursor
        while cursor < len(text) and depth:
            if text[cursor] == "\\":
                cursor = min(len(text), cursor + 2)
                continue
            if text[cursor] == "{":
                depth += 1
            elif text[cursor] == "}":
                depth -= 1
                if depth == 0:
                    return cursor + 1, text[start:cursor]
            cursor += 1
        return cursor, text[start:cursor]
    if text[cursor] == "\\":
        name = _command_name(text, cursor)
        if name:
            return cursor + 1 + len(name), "\\" + name
        if cursor + 1 < len(text):
            return cursor + 2, text[cursor : cursor + 2]
        return cursor + 1, text[cursor]
    if text[cursor].isalnum():
        return cursor + 1, text[cursor]
    return cursor, ""


def _bar_wraps_symbol(text: str, index: int, after: int) -> bool:
    """True when bars enclose E itself, as in ``|E|``, not ``E|X|``."""
    if not _bar_before(text, index):
        return False
    cursor = _skip_soft(text, after, newlines=True)
    if cursor < len(text) and text[cursor] == "|":
        return True
    name = _command_name(text, cursor)
    if name in _CLOSERS:
        rest = _skip_soft(text, cursor + 1 + len(name), newlines=True)
        return rest < len(text) and text[rest] == "|"
    return False


def _bar_before(text: str, index: int) -> bool:
    cursor = index - 1
    while cursor >= 0 and text[cursor] in " \t":
        cursor -= 1
    if cursor >= 0 and text[cursor] == "|":
        return True
    for name in ("lvert", "vert"):
        token = "\\" + name
        start = cursor + 1 - len(token)
        if start >= 0 and text.startswith(token, start):
            if start == 0 or not text[start - 1].isalpha():
                return True
    return False


def _argument_end(text: str, cursor: int) -> int | None:
    delimited = _skip_soft(text, cursor, newlines=True)
    if delimited < len(text) and text[delimited] in "([":
        return delimited + 1
    if text.startswith("\\{", delimited):
        return delimited + 2
    if delimited < len(text) and text[delimited] == "|" and not _pipe_closes(text, delimited):
        return delimited + 1
    opened = _command_opens(text, delimited)
    if opened is not None:
        return opened
    # A letter glued on (EBIC, ELBO, Err) is a word. EX is handled earlier.
    # A letter after space or a spacing command is juxtaposition: E X, E\,X.
    adjacent = _skip_soft(text, cursor, newlines=False)
    if adjacent != cursor and adjacent < len(text) and text[adjacent].isalpha():
        return adjacent + 1
    opened = _command_opens(text, adjacent)
    if opened is not None:
        return opened
    return None


def _pipe_closes(text: str, pipe: int) -> bool:
    """A bar closes ``|E|`` when what follows is not the start of an argument."""
    cursor = _skip_soft(text, pipe + 1, newlines=True)
    if cursor >= len(text):
        return True
    if text[cursor] in "|=+-*/,;:)]}&<>":
        return True
    if text[cursor] == "\\":
        return _command_name(text, cursor) in _CLOSERS
    if text[cursor].isalpha() or text[cursor] in "{([":
        return False
    return True


def _command_opens(text: str, cursor: int) -> int | None:
    name = _command_name(text, cursor)
    if not name:
        return None
    if name in _SYMBOLS:
        return cursor + 1
    if name not in _OPENERS:
        return None
    if name in {"lbrace", "lvert", "langle"}:
        return cursor + 1
    rest = _skip_soft(text, cursor + 1 + len(name), newlines=True)
    if rest < len(text) and text[rest] in "([|.":
        return cursor + 1
    if text.startswith("\\{", rest) or _command_name(text, rest) in {"lvert", "lbrace", "langle", "vert"}:
        return cursor + 1
    return None


def _command_name(text: str, cursor: int) -> str:
    if cursor >= len(text) or text[cursor] != "\\":
        return ""
    start = cursor + 1
    end = start
    while end < len(text) and text[end].isalpha():
        end += 1
    return text[start:end]


def _skip_soft(text: str, cursor: int, newlines: bool) -> int:
    while cursor < len(text):
        if text[cursor] in " \t" or (newlines and text[cursor] == "\n"):
            cursor += 1
            continue
        nxt = _skip_spacing_command(text, cursor)
        if nxt == cursor:
            break
        cursor = nxt
    return cursor


def _skip_spacing_command(text: str, cursor: int) -> int:
    if cursor >= len(text) or text[cursor] != "\\":
        return cursor
    name = _command_name(text, cursor)
    if name in _SPACING:
        cursor += 1 + len(name)
        if name == "hspace" and cursor < len(text) and text[cursor] == "{":
            cursor, _body = _read_atom(text, cursor)
        return cursor
    if not name and cursor + 1 < len(text) and text[cursor + 1] in " ,;:!":
        return cursor + 2
    return cursor


def _mask_standard(inner: str) -> str:
    chars = list(inner)

    def wipe(match: re.Match[str]) -> None:
        for pos in range(match.start(), match.end()):
            if chars[pos] != "\n":
                chars[pos] = " "

    for match in _FONT.finditer(inner):
        wipe(match)
    for match in _MATHRM.finditer(inner):
        wipe(match)
    for match in _OPERATORNAME.finditer(inner):
        wipe(match)
    for match in _ESHORT.finditer(inner):
        if _escaped_as_command(inner, match.end() - 1):
            wipe(match)
    return "".join(chars)


def _blank_code(text: str) -> str:
    chars = list(text)

    def wipe(start: int, end: int) -> None:
        for pos in range(start, end):
            if chars[pos] != "\n":
                chars[pos] = " "

    for match in _FENCE.finditer(text):
        wipe(match.start(), match.end())
    cursor = 0
    n = len(chars)
    while cursor < n:
        if chars[cursor] != "`":
            cursor += 1
            continue
        ticks = 1
        while cursor + ticks < n and chars[cursor + ticks] == "`":
            ticks += 1
        close = _find_ticks(chars, cursor + ticks, ticks)
        if close < 0:
            break
        wipe(cursor, close + ticks)
        cursor = close + ticks
    return "".join(chars)


def _find_ticks(chars: list[str], start: int, ticks: int) -> int:
    needle = "`" * ticks
    haystack = "".join(chars)
    return haystack.find(needle, start)


def _find_single_dollar(text: str, start: int) -> int:
    cursor = start
    while cursor < len(text):
        if text.startswith("\\$", cursor):
            cursor += 2
            continue
        if text[cursor] == "$":
            return cursor
        cursor += 1
    return -1


def _take_tex_delimiter(text: str, start: int) -> int | None:
    """``start`` points at the backslash of ``\\(`` or ``\\[``. Return the end, or None."""
    opener = text[start + 1]
    closer = ")" if opener == "(" else "]"
    open_pair = "\\" + opener
    close_pair = "\\" + closer
    depth = 1
    cursor = start + 2
    n = len(text)
    while cursor < n:
        if text[cursor] == "\\" and cursor + 1 < n:
            pair = text[cursor : cursor + 2]
            if pair == open_pair:
                depth += 1
                cursor += 2
                continue
            if pair == close_pair:
                depth -= 1
                if depth == 0:
                    return cursor + 2
                cursor += 2
                continue
            cursor += 2
            continue
        cursor += 1
    return None


def _diff_path(raw: str) -> str | None:
    name = raw.strip()
    if name.startswith('"') and name.endswith('"') and len(name) >= 2:
        name = name[1:-1]
    if name == "/dev/null":
        return None
    if name.startswith("b/"):
        name = name[2:]
    return name.replace("\\", "/")


def _changed_files(root: Path, target: str) -> list[tuple[str, str | None]]:
    """``(new path, old path)`` for files that differ from ``target``.

    The old path is ``None`` when the file is new or untracked, so the whole
    file is compared with empty text.
    """
    diff = _git(root, ["diff", "--name-status", "--find-renames", "-z", target], check=True)
    parts = diff.stdout.split("\0")
    pairs: list[tuple[str, str | None]] = []
    index = 0
    while index < len(parts) and parts[index]:
        status = parts[index]
        index += 1
        if status.startswith(("R", "C")):
            old_path, new_path = parts[index], parts[index + 1]
            index += 2
            pairs.append((new_path, old_path))
            continue
        path = parts[index]
        index += 1
        if status.startswith("D"):
            continue
        pairs.append((path, None if status.startswith("A") else path))
    untracked = _git(root, ["ls-files", "--others", "--exclude-standard", "-z"], check=True)
    for rel in untracked.stdout.split("\0"):
        if rel:
            pairs.append((rel, None))
    return pairs


def _file_at(root: Path, target: str, path: str) -> str:
    shown = _git(root, ["show", f"{target}:{path}"], check=False)
    if shown.returncode != 0:
        return ""
    return shown.stdout


def _diff_target(root: Path, base: str) -> str:
    # The pull-request checkout is a merge commit. Its first parent is the
    # base at the moment GitHub built that merge, which stays stable if the
    # base branch moves before this step fetches it.
    if os.environ.get("GITHUB_EVENT_NAME") == "pull_request":
        parent = _git(root, ["rev-parse", "--verify", "--quiet", "HEAD^1"], check=False)
        if parent.returncode == 0 and parent.stdout.strip():
            return parent.stdout.strip()
    merged = _git(root, ["merge-base", "HEAD", base], check=False)
    if merged.returncode == 0 and merged.stdout.strip():
        return merged.stdout.strip()
    return base


def _ref_exists(root: Path, ref: str) -> bool:
    proc = _git(root, ["rev-parse", "--verify", "--quiet", ref], check=False)
    return proc.returncode == 0


def _git(
    root: Path | None,
    args: list[str],
    check: bool,
) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if check and proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "git failed").strip()
        raise GuardError(f"expectation notation: git {' '.join(args)} failed: {detail}")
    return proc


if __name__ == "__main__":
    raise SystemExit(main())
