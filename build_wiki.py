"""Build the STAT3500 wiki from the course book, final booklet, and practice set.

Run from this folder: python build_wiki.py
Then: quarto preview

The course files are copies in sources/. GitHub runs the same two steps
(build, then quarto render) on every push and publishes the result.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parent
SOURCES = WIKI / "sources"
BOOK = SOURCES / "book"  # the lecture book (index, chapters, figures)
PREP = SOURCES / "prep"  # the final-exam booklet (index, chapters, figures)
PRACTICE_TEX = SOURCES / "practice" / "stat3500_final_practice.tex"
REPO_URL = "https://github.com/ChrisWnuczynski/stat3500-wiki"

PARTS = [
    (
        "Bayesian statistics",
        [
            ("bayes-01-foundations.qmd", "notes"),
            ("bayes-02-beta-binomial.qmd", "notes"),
            ("bayes-03-normal-models.qmd", "notes"),
            ("bayes-04-mcmc.qmd", "notes"),
            ("bayes-05-categorical.qmd", "notes"),
            ("bayes-06-testing.qmd", "notes"),
            ("bayes-07-exponential-families.qmd", "notes"),
            ("bayes-08-hierarchy.qmd", "notes"),
            ("bayes-09-linear-regression.qmd", "notes"),
            ("bayes-10-reference.qmd", "reference"),
        ],
    ),
    (
        "Generalised linear models",
        [
            ("01-introduction-to-glms.qmd", "notes"),
            ("02-inference-and-counts.qmd", "notes"),
            ("03-gamma-and-quasi.qmd", "notes"),
            ("04-categorical-responses.qmd", "notes"),
            ("05-comparisons-and-deviance.qmd", "notes"),
            ("06-pit-residuals.qmd", "notes"),
        ],
    ),
    (
        "Smoothing",
        [
            ("06-smooth-means.qmd", "notes"),
            ("07-additive-and-mixed.qmd", "notes"),
        ],
    ),
    (
        "Correlated data",
        [
            ("08-random-intercepts.qmd", "notes"),
            ("08-slopes-and-glmms.qmd", "notes"),
            ("09-marginal-models.qmd", "notes"),
            ("10-plants-and-series.qmd", "notes"),
        ],
    ),
    (
        "Time series",
        [
            ("12-time-series.qmd", "notes"),
            ("11-forecasting.qmd", "notes"),
        ],
    ),
]

ZERO_ARG = {
    "ind": r"\stackrel{\mathrm{ind}}{\sim}",
    "given": r"\mid",
    "dd": r"\,\mathrm{d}",
    "R": r"\mathbb{R}",
    "Pr": r"\mathbb{P}",
    "E": r"\mathbb{E}",
    "Var": r"\operatorname{Var}",
    "Cov": r"\operatorname{Cov}",
    "Normal": r"\operatorname{N}",
    "Bin": r"\operatorname{Bin}",
    "Bern": r"\operatorname{Bern}",
    "BetaDist": r"\operatorname{Beta}",
    "GammaDist": r"\operatorname{Gamma}",
    "InvGamma": r"\operatorname{InvGamma}",
    "Poisson": r"\operatorname{Poisson}",
    "Dir": r"\operatorname{Dirichlet}",
    "Mult": r"\operatorname{Multinomial}",
    "Exp": r"\operatorname{Exp}",
    "Geom": r"\operatorname{Geom}",
    "Po": r"\operatorname{Po}",
    "Weibull": r"\operatorname{Weibull}",
    "argmax": r"\operatorname*{arg\,max}",
    "argmin": r"\operatorname*{arg\,min}",
    "BF": r"\operatorname{BF}",
    # Bold symbols are wrapped in braces so that an accent such as
    # \widehat\pvec still receives a single group.
    "pvec": r"{\boldsymbol{p}}",
    "xvec": r"{\boldsymbol{x}}",
    "Xvec": r"{\boldsymbol{X}}",
    "yvec": r"{\boldsymbol{y}}",
    "Yvec": r"{\boldsymbol{Y}}",
    "betavec": r"{\boldsymbol{\beta}}",
    "thetavec": r"{\boldsymbol{\theta}}",
}

ONE_ARG = {
    "vect": lambda arg: rf"{{\boldsymbol{{{arg}}}}}",
    "mat": lambda arg: rf"{{\color{{blue}}\boldsymbol{{{arg}}}}}",
}

FIGURE_PAGES: dict[str, list[str]] = {}

EX_OPEN = re.compile(r"^::: \{#([\w:-]+)\s+\.exercise\}\s*$")
ANY_OPEN = re.compile(r"^:::\s*\{")
ANY_CLOSE = re.compile(r"^:::\s*$")
FENCE = re.compile(r"^\s*```")


def read_delim(text: str, j: int, open_c: str, close_c: str) -> tuple[str, int]:
    if j >= len(text) or text[j] != open_c:
        raise ValueError(f"expected {open_c} at {j}")
    depth = 0
    i = j
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text):
            i += 2
            continue
        if text[i] == open_c:
            depth += 1
        elif text[i] == close_c:
            depth -= 1
            if depth == 0:
                return text[j + 1 : i], i + 1
        i += 1
    raise ValueError(f"unbalanced {open_c}")


def read_macro_argument(text: str, j: int) -> tuple[str, int] | None:
    """Read one LaTeX argument, including an undelimited token such as \\alpha or X."""
    k = j
    while k < len(text) and text[k] in " \t":
        k += 1
    if k >= len(text):
        return None
    if text[k] == "{":
        arg, end = read_delim(text, k, "{", "}")
        return arg, end
    if text[k] == "\\":
        end = k + 1
        if end < len(text) and text[end].isalpha():
            while end < len(text) and text[end].isalpha():
                end += 1
        elif end < len(text):
            end += 1
        else:
            return None
        return text[k:end], end
    return text[k], k + 1


def expand_once(text: str) -> str:
    out: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] != "\\":
            out.append(text[i])
            i += 1
            continue
        if i + 1 < n and not text[i + 1].isalpha():
            out.append(text[i : i + 2])
            i += 2
            continue
        j = i + 1
        while j < n and text[j].isalpha():
            j += 1
        name = text[i + 1 : j]
        if name in ONE_ARG:
            arg = read_macro_argument(text, j)
            if arg is not None:
                body, k = arg
                out.append(ONE_ARG[name](body))
                i = k
                continue
        if name in ZERO_ARG:
            out.append(ZERO_ARG[name])
            i = j
            continue
        out.append(text[i:j])
        i = j
    return "".join(out)


def protect_code(text: str, fn) -> str:
    pieces = re.split(r"(```.*?```)", text, flags=re.S)
    built: list[str] = []
    for piece in pieces:
        if piece.startswith("```"):
            built.append(piece)
            continue
        bits = re.split(r"(`[^`\n]*`)", piece)
        for bit in bits:
            built.append(bit if bit.startswith("`") else fn(bit))
    return "".join(built)


def expand_macros(text: str) -> str:
    def run(segment: str) -> str:
        for _ in range(8):
            nxt = expand_once(segment)
            if nxt == segment:
                return segment
            segment = nxt
        return segment

    return protect_code(text, run)


def convert_enumerates(text: str) -> str:
    begin = r"\begin{enumerate}"
    out: list[str] = []
    i = 0
    while True:
        j = text.find(begin, i)
        if j < 0:
            out.append(text[i:])
            break
        out.append(text[i:j])
        k = j + len(begin)
        while k < len(text) and text[k].isspace():
            k += 1
        kind = "num"
        if k < len(text) and text[k] == "[":
            opt, k = read_delim(text, k, "[", "]")
            if "alph" in opt:
                kind = "alph"
            elif "roman" in opt:
                kind = "roman"
        body, k = read_environment_body(text, k, "enumerate")
        out.append(render_enumerate(body, kind))
        i = k
    return "".join(out)


def read_environment_body(text: str, k: int, name: str) -> tuple[str, int]:
    begin = r"\begin{" + name + "}"
    end = r"\end{" + name + "}"
    depth = 1
    i = k
    while i < len(text):
        next_b = text.find(begin, i)
        next_e = text.find(end, i)
        if next_e < 0:
            raise ValueError(f"unclosed {name} environment")
        if next_b != -1 and next_b < next_e:
            depth += 1
            i = next_b + len(begin)
            continue
        depth -= 1
        if depth == 0:
            return text[k:next_e], next_e + len(end)
        i = next_e + len(end)
    raise ValueError(f"unclosed {name} environment")


def to_roman(n: int) -> str:
    vals = (
        (10, "x"),
        (9, "ix"),
        (5, "v"),
        (4, "iv"),
        (1, "i"),
    )
    out = []
    for value, glyph in vals:
        while n >= value:
            out.append(glyph)
            n -= value
    return "".join(out)


def enum_label(kind: str, n: int) -> str:
    # Bold labels, as in the final booklet. A bare "(i)" after "(c)" would be
    # read as the next item of an automatic list and shown as "d.".
    if kind == "alph":
        return rf"\textbf{{({chr(ord('a') + n - 1)})}}"
    if kind == "roman":
        return rf"\textbf{{({to_roman(n)})}}"
    return rf"\textbf{{{n}.}}"


def render_enumerate(body: str, kind: str) -> str:
    body = convert_enumerates(body)
    parts = re.split(r"\\item\b", body)
    chunks = []
    if parts[0].strip():
        chunks.append(parts[0].strip() + "\n\n")
    for n, part in enumerate(parts[1:], 1):
        chunks.append(f"\n\n{enum_label(kind, n)} {part.strip()}\n\n")
    return "".join(chunks)


def find_commands(text: str, name: str, nargs: int) -> list[tuple[int, int, list[str]]]:
    token = "\\" + name
    found = []
    i = 0
    while True:
        j = text.find(token, i)
        if j < 0:
            break
        k = j + len(token)
        if k < len(text) and text[k].isalpha():
            i = k
            continue
        pos = k
        args = []
        ok = True
        for _ in range(nargs):
            while pos < len(text) and text[pos].isspace():
                pos += 1
            if pos >= len(text) or text[pos] != "{":
                ok = False
                break
            arg, pos = read_delim(text, pos, "{", "}")
            args.append(arg)
        if ok:
            found.append((j, pos, args))
            i = pos
        else:
            i = k
    return found


def replace_command(text: str, name: str, nargs: int, fn) -> str:
    matches = find_commands(text, name, nargs)
    if not matches:
        return text
    out = []
    last = 0
    for start, end, args in matches:
        out.append(text[last:start])
        out.append(fn(args))
        last = end
    out.append(text[last:])
    return "".join(out)


def strip_latex_comments(text: str) -> str:
    out: list[str] = []
    i = 0
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text):
            out.append(text[i : i + 2])
            i += 2
            continue
        if text[i] == "%":
            while i < len(text) and text[i] != "\n":
                i += 1
            continue
        out.append(text[i])
        i += 1
    return "".join(out)


def preprocess_practice_latex(text: str) -> str:
    text = strip_latex_comments(text)
    text = convert_enumerates(text)
    text = text.replace(r"\begin{keyresult}", "\n\\begin{quote}\\textbf{Key result.} ")
    text = text.replace(r"\end{keyresult}", " \\end{quote}\n")
    text = replace_command(text, "studyheading", 1, lambda a: rf"\textbf{{{a[0]}.}}")
    text = replace_command(text, "partmarks", 1, lambda a: rf" \textbf{{[{a[0]}]}}")
    text = replace_command(text, "answernav", 1, lambda a: "")
    text = replace_command(text, "textcolor", 2, lambda a: a[1])
    text = re.sub(r"\\hyperref\[[^\]]*\]", "", text)
    text = replace_command(text, "hyperlink", 2, lambda a: a[1])
    text = text.replace(r"\clearpage", "\n")
    text = text.replace(r"\newpage", "\n")
    text = re.sub(r"\\renewcommand\{\\arraystretch\}\{[^{}]*\}", "", text)
    return text


def yaml_quote(value: str) -> str:
    value = " ".join(value.replace("\n", " ").split())
    value = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{value}"'


def href(from_qmd: Path, to_qmd: Path) -> str:
    return Path(os.path.relpath(to_qmd, start=from_qmd.parent)).as_posix()


def rewrite_images(text: str, prefix: str) -> str:
    pattern = re.compile(
        r"!\[([^\]]*)\]\((?:\.\./)*figures/([^)/\s]+)\.pdf\)(\{[^}]*\})?"
    )

    def repl(match: re.Match) -> str:
        alt, stem, attrs = match.group(1), match.group(2), match.group(3) or ""
        pages = FIGURE_PAGES.get(stem)
        if not pages:
            return match.group(0)
        first = f"![{alt}]({prefix}/{pages[0]}){attrs}"
        extra = "".join(f"\n\n![{alt}]({prefix}/{page})" for page in pages[1:])
        return first + extra

    return pattern.sub(repl, text)


def localize_refs(text: str, notes_href: str) -> str:
    def at_ref(match: re.Match) -> str:
        kind, rest = match.group(1), match.group(2)
        nice = {
            "fig": "Figure",
            "eq": "Equation",
            "tbl": "Table",
            "sec": "Section",
        }.get(kind, "Note")
        return f"[{nice}]({notes_href}#{kind}-{rest})"

    # Equation references are resolved later, by resolve_links, with their numbers.
    text = re.sub(
        r"@(fig|tbl|thm|def|prp|exm|rem|exr|ex|sec)-([A-Za-z0-9_:-]+)",
        at_ref,
        text,
    )
    return text


def prepare(text: str, fig_prefix: str, notes_href: str | None = None, page: Path | None = None) -> str:
    text = re.sub(r"```\{=latex\}.*?```\n?", "", text, flags=re.S)
    if notes_href:
        text = localize_refs(text, notes_href)
    text = rewrite_images(text, fig_prefix)
    text = expand_macros(text)
    if page is not None:
        text = convert_equations(text, page)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ---------------------------------------------------------------------------
# Equations and links between pages
#
# The book numbers equations with LaTeX \label and cites them with \eqref.
# Pandoc drops an \eqref written in prose, and KaTeX numbers each page on its
# own, so a citation from another page cannot work. Labelled equations become
# Quarto equations ($$ ... $$ {#eq-...}); citations become Quarto references on
# the same page and numbered links across pages.
# ---------------------------------------------------------------------------

EQ_LABELS: dict[str, tuple[str, Path]] = {}  # LaTeX label -> (Quarto id, page)
EQ_PAGES: dict[str, Path] = {}  # Quarto id -> page
EQ_NUMBERS: dict[str, int] = {}  # Quarto id -> number on its page
PAGE_TITLES: dict[Path, str] = {}
ANCHOR_PAGES: dict[str, str] = {}  # ex-/sol- id -> page path, with an optional #fragment

EQ_ENV = re.compile(r"\\begin\{(equation|align)(\*?)\}(.*?)\\end\{\1\2\}", re.S)
LABEL = re.compile(r"\\label\{([^{}]+)\}")
QUARTO_EQ = re.compile(r"\$\$\s*\{#(eq-[A-Za-z0-9_-]+)\}")
MATH_SPAN = re.compile(
    r"\$\$.*?\$\$|\$(?:\\.|[^$\\\n])+\$|\\begin\{(align\*?|equation\*?|gather\*?|multline\*?)\}.*?\\end\{\1\}",
    re.S,
)


def eq_id(label: str) -> str:
    stem = label[3:] if label.startswith("eq:") else label
    return "eq-" + re.sub(r"[^A-Za-z0-9-]+", "-", stem).strip("-")


def convert_equations(text: str, page: Path) -> str:
    def repl(match: re.Match) -> str:
        env, _star, body = match.groups()
        labels = LABEL.findall(body)
        if not labels:
            return match.group(0)
        ident = eq_id(labels[0])
        for label in labels:
            EQ_LABELS[label] = (ident, page)
        body = LABEL.sub("", body)
        body = re.sub(r"\\(?:nonumber|notag)\b", "", body)
        body = "\n".join(line for line in body.strip().splitlines() if line.strip())
        if env == "align":
            body = "\\begin{aligned}\n" + body + "\n\\end{aligned}"
        # Keep the equation inside its paragraph, as the source has it.
        return f"\n$$\n{body}\n$$ {{#{ident}}}\n"

    return protect_code(text, lambda segment: EQ_ENV.sub(repl, segment))


def number_equations(path: Path, text: str) -> None:
    for n, match in enumerate(QUARTO_EQ.finditer(text), 1):
        EQ_PAGES.setdefault(match.group(1), path)
        if EQ_PAGES[match.group(1)] == path:
            EQ_NUMBERS[match.group(1)] = n


def resolve_links(text: str, page: Path) -> str:
    def eq_target(label_or_id: str) -> str | None:
        if label_or_id in EQ_LABELS:
            return EQ_LABELS[label_or_id][0]
        return label_or_id if label_or_id in EQ_PAGES else None

    def cite(ident: str, in_math: bool) -> str:
        number = EQ_NUMBERS.get(ident, "?")
        target = EQ_PAGES[ident]
        if in_math:
            return f"({number})"
        if target == page:
            return f"@{ident}"
        title = PAGE_TITLES.get(target, "another chapter")
        return f"[Equation ({number}) in *{title}*]({href(page, target)}#{ident})"

    def in_math(segment: str) -> str:
        def repl(match: re.Match) -> str:
            ident = eq_target(match.group(1))
            return cite(ident, True) if ident else "(?)"

        return re.sub(r"\\eqref\{([^{}]+)\}", repl, segment)

    def in_prose(segment: str) -> str:
        # "equations \eqref{a}--\eqref{b}" where both labels name one numbered
        # equation is a single reference, and the cite already says "Equation".
        def same_range(match: re.Match) -> str:
            a, b = eq_target(match.group(1)), eq_target(match.group(2))
            return f"\\eqref{{{match.group(1)}}}" if a and a == b else match.group(0)

        segment = re.sub(r"\\eqref\{([^{}]+)\}\s*(?:--|–|-|and)\s*\\eqref\{([^{}]+)\}", same_range, segment)
        segment = re.sub(r"\b[Ee]quations?\s+(?=\\eqref\{)", "", segment)

        def eqref(match: re.Match) -> str:
            ident = eq_target(match.group(1))
            return cite(ident, False) if ident else "the equation above"

        segment = re.sub(r"\\eqref\{([^{}]+)\}", eqref, segment)

        def at_eq(match: re.Match) -> str:
            ident = match.group(1)
            if ident in EQ_PAGES and EQ_PAGES[ident] != page:
                return cite(ident, False)
            return match.group(0)

        segment = re.sub(r"(?<![\w@])@(eq-[A-Za-z0-9_-]+)", at_eq, segment)

        def anchor(match: re.Match) -> str:
            target = ANCHOR_PAGES.get(match.group(1))
            if not target:
                return match.group(0)
            path, _, fragment = target.partition("#")
            link = href(page, Path(path))
            return f"]({link}{'#' + fragment if fragment else ''})"

        return re.sub(r"\]\(#((?:ex|exr|sol)-[\w-]+)\)", anchor, segment)

    def run(segment: str) -> str:
        out, last = [], 0
        for match in MATH_SPAN.finditer(segment):
            out.append(in_prose(segment[last : match.start()]))
            out.append(in_math(match.group(0)))
            last = match.end()
        out.append(in_prose(segment[last:]))
        return "".join(out)

    return protect_code(text, run)


def strip_first_heading(text: str) -> str:
    return re.sub(r"\A#\s+[^\n]*\n+", "", text.lstrip("\ufeff"), count=1)


def first_heading(text: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", text, flags=re.M)
    if not match:
        raise ValueError("chapter has no title")
    title = re.sub(r"\s*\{#.*$", "", match.group(1)).strip()
    title = re.sub(r"\s*\{\.[^}]*\}\s*$", "", title).strip()
    return title


def write_qmd(path: Path, title: str, body: str, description: str | None = None, categories: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["---", f"title: {yaml_quote(title)}"]
    if description:
        lines.append(f"description: {yaml_quote(description)}")
    if categories:
        lines.append("categories: [" + ", ".join(yaml_quote(c) for c in categories) + "]")
    lines.extend(["---", "", body.strip(), ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def pager(*parts: str) -> str:
    bits = [part for part in parts if part]
    return "::: {.pager}\n" + " · ".join(bits) + "\n:::\n"


def extract_exercises(text: str) -> tuple[str, list[tuple[str, str, str]]]:
    """Return prose before the exercises, and (lead, id, body) tuples."""
    lines = text.splitlines()
    split_at = None
    for i, line in enumerate(lines):
        if line.strip() == "## Exercises":
            split_at = i
            break
    if split_at is None:
        return text, []
    prose = "\n".join(lines[:split_at]).rstrip() + "\n"
    region = lines[split_at + 1 :]
    exercises = []
    lead: list[str] = []
    i = 0
    in_code = False
    while i < len(region):
        line = region[i]
        if FENCE.match(line):
            in_code = not in_code
            lead.append(line)
            i += 1
            continue
        if not in_code and EX_OPEN.match(line):
            ex_id = EX_OPEN.match(line).group(1)
            body_lines = []
            depth = 1
            i += 1
            while i < len(region):
                current = region[i]
                if FENCE.match(current):
                    in_code = not in_code
                    body_lines.append(current)
                    i += 1
                    continue
                if not in_code and ANY_OPEN.match(current):
                    depth += 1
                    body_lines.append(current)
                    i += 1
                    continue
                if not in_code and ANY_CLOSE.match(current):
                    depth -= 1
                    if depth == 0:
                        i += 1
                        break
                    body_lines.append(current)
                    i += 1
                    continue
                body_lines.append(current)
                i += 1
            lead_text = "\n".join(lead).strip()
            lead = []
            exercises.append((lead_text, ex_id, "\n".join(body_lines).strip()))
            continue
        lead.append(line)
        i += 1
    trailing = "\n".join(lead).strip()
    if trailing:
        prose += "\n\n" + trailing + "\n"
    return prose, exercises


def exercise_title(body: str) -> str:
    match = re.search(r"^##\s+(.+?)\s*$", body, flags=re.M)
    if not match:
        raise ValueError("exercise has no heading")
    return match.group(1).strip()


def without_title(body: str) -> str:
    return re.sub(r"^##\s+.+?\n+", "", body, count=1, flags=re.M).strip()


def solution_link(body: str) -> str | None:
    match = re.search(r"\[Solution\]\(#(sol-[\w-]+)\)", body)
    return match.group(1) if match else None


def exercise_list(items: list[tuple[str, str]], link_for) -> str:
    blocks = ["## Exercises", "", "Each question is on its own page. Worked answers, where the source has them, are separate.", ""]
    for lead, target in items:
        if lead:
            blocks.extend([lead, ""])
        blocks.append(f"- [{target[0]}]({link_for(target[1])})")
    return "\n".join(blocks)


def convert_figures() -> None:
    dest = WIKI / "figures"
    dest.mkdir(parents=True, exist_ok=True)
    # Sorted, so Windows and Linux builds list the figures in the same order.
    sources = sorted((BOOK / "figures").glob("*.pdf"))
    sources += sorted((PREP / "figures").glob("*.pdf"))
    print(f"Converting {len(sources)} figures")
    for src in sources:
        if src.stem in FIGURE_PAGES:
            raise SystemExit(f"Two figures share the name {src.stem}")
        info = subprocess.run(
            ["pdfinfo", str(src)],
            capture_output=True,
            text=True,
            check=True,
        )
        match = re.search(r"^Pages:\s+(\d+)", info.stdout, flags=re.M)
        pages = int(match.group(1)) if match else 1
        if pages == 1:
            png = dest / f"{src.stem}.png"
            if not png.exists():
                subprocess.run(
                    ["pdftocairo", "-png", "-r", "130", "-singlefile", str(src), str(dest / src.stem)],
                    check=True,
                    capture_output=True,
                )
            FIGURE_PAGES[src.stem] = [f"{src.stem}.png"]
        else:
            subprocess.run(
                ["pdftocairo", "-png", "-r", "130", str(src), str(dest / src.stem)],
                check=True,
                capture_output=True,
            )
            FIGURE_PAGES[src.stem] = [f"{src.stem}-{i}.png" for i in range(1, pages + 1)]


def pandoc_many(fragments: dict[str, str]) -> dict[str, str]:
    if not fragments:
        return {}
    chunks = ["\\documentclass{article}", "\\usepackage{amsmath,amssymb,mathtools,booktabs}", "\\begin{document}"]
    for key, body in fragments.items():
        chunks.append(f"\nWIKISPLIT-{key}-END\n")
        chunks.append(body)
    chunks.append("\nWIKISPLIT-ENDALL-END\n\\end{document}\n")
    tex = "\n".join(chunks)
    build = WIKI / "_build"
    build.mkdir(exist_ok=True)
    (build / "practice-fragments.tex").write_text(tex, encoding="utf-8")
    result = subprocess.run(
        ["quarto", "pandoc", "-f", "latex", "-t", "markdown", "--wrap=none", "--markdown-headings=atx"],
        input=tex.encode("utf-8"),
        capture_output=True,
    )
    if result.returncode != 0:
        (build / "pandoc-error.txt").write_bytes(result.stderr)
        raise SystemExit(result.stderr.decode("utf-8", errors="replace")[:4000])
    # Pandoc writes Windows line endings here, which the patterns below do not expect.
    md = result.stdout.decode("utf-8").replace("\r\n", "\n")
    (build / "practice-fragments.md").write_text(md, encoding="utf-8")
    parts = re.split(r"WIKISPLIT-([A-Za-z0-9]+)-END", md)
    parsed: dict[str, str] = {}
    # parts[0] is preamble, then key, body, key, body...
    i = 1
    while i + 1 < len(parts):
        parsed[parts[i]] = parts[i + 1].strip()
        i += 2
    missing = [key for key in fragments if key not in parsed]
    if missing:
        raise SystemExit(f"Pandoc dropped fragments: {missing[:8]}")
    parsed = move_footnotes(parsed)
    return {key: unescape_markdown(value) for key, value in parsed.items()}


FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:[^\n]*(?:\n(?:    |\t)[^\n]*)*", re.M)


def move_footnotes(parsed: dict[str, str]) -> dict[str, str]:
    """Pandoc puts every footnote at the end of the one document it converts.

    Give each footnote back to the fragment that cites it.
    """
    notes: dict[str, str] = {}
    for key, value in parsed.items():
        for match in FOOTNOTE_DEF.finditer(value):
            notes[match.group(1)] = match.group(0)
        parsed[key] = FOOTNOTE_DEF.sub("", value).rstrip()
    for key, value in parsed.items():
        cited = re.findall(r"\[\^([^\]]+)\](?!:)", value)
        extra = [notes[name] for name in dict.fromkeys(cited) if name in notes]
        if extra:
            parsed[key] = value + "\n\n" + "\n\n".join(extra)
    return parsed


def unescape_markdown(text: str) -> str:
    """Pandoc escapes brackets. Quarto would read \\( and \\[ as math."""
    text = re.sub(r"(?<!\\)\\([()\[\]])", r"\1", text)

    def unwrap_center(match: re.Match) -> str:
        import textwrap

        # Strip blank lines only: leading spaces mark an empty header cell.
        return "\n" + textwrap.dedent(match.group(1)).strip("\n") + "\n\n"

    # A centred block may also end the fragment, with no newline after it.
    text = re.sub(r"::: center\n(.*?)\n:::(?:\n|$)", unwrap_center, text, flags=re.S)
    return text.strip()


def load_practice() -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    raw = PRACTICE_TEX.read_text(encoding="utf-8")
    q_region = raw.split("% BEGIN CONCEPT QUESTIONS", 1)[1].split("% END CONCEPT QUESTIONS", 1)[0]
    topics = [(m.start(), m.group(1).strip()) for m in re.finditer(r"\\concepttopic\{([^{}]*)\}", q_region)]
    concept_qs = []
    for start, end, args in find_commands(q_region, "conceptquestion", 2):
        topic = ""
        for pos, name in topics:
            if pos < start:
                topic = name
        concept_qs.append({"n": int(args[0]), "text": args[1].strip(), "topic": topic})

    a_region = raw.split("% END CONCEPT QUESTIONS", 1)[1]
    concept_as = []
    answer_topics = [(m.start(), m.group(1).strip()) for m in re.finditer(r"\\concepttopic\{([^{}]*)\}", a_region)]
    cursor_base = 0
    for match in re.finditer(r"\\begin\{conceptanswer\}", a_region):
        k = match.end()
        while k < len(a_region) and a_region[k].isspace():
            k += 1
        n_arg, k = read_delim(a_region, k, "{", "}")
        while k < len(a_region) and a_region[k].isspace():
            k += 1
        title, k = read_delim(a_region, k, "{", "}")
        body, k = read_environment_body(a_region, k, "conceptanswer")
        topic = ""
        for pos, name in answer_topics:
            if pos < match.start():
                topic = name
        concept_as.append({"n": int(n_arg), "title": title.strip(), "topic": topic, "body": body.strip()})
        cursor_base = k

    exam_qs = []
    for match in re.finditer(r"\\begin\{examquestion\}", raw):
        k = match.end()
        while k < len(raw) and raw[k].isspace():
            k += 1
        title, k = read_delim(raw, k, "{", "}")
        body, k = read_environment_body(raw, k, "examquestion")
        exam_qs.append({"title": title.strip(), "body": body.strip()})

    ans_start = raw.find(r"\subsection{Answer 1:")
    ans_region = raw[ans_start:]
    marks = list(re.finditer(r"\\subsection\{Answer (\d+):\s*([^{}]*)\}", ans_region))
    exam_as = []
    for i, mark in enumerate(marks):
        body_start = mark.end()
        body_end = marks[i + 1].start() if i + 1 < len(marks) else len(ans_region)
        exam_as.append(
            {
                "n": int(mark.group(1)),
                "title": mark.group(2).strip(),
                "body": ans_region[body_start:body_end].strip(),
            }
        )
    return concept_qs, concept_as, exam_qs, exam_as


def self_test() -> None:
    assert expand_macros(r"$\xvec\given\theta$") == r"${\boldsymbol{x}}\mid\theta$"
    assert expand_macros(r"\vect{\hat{\beta}}") == r"{\boldsymbol{\hat{\beta}}}"
    assert expand_macros(r"\widehat\vect{p}") == r"\widehat{\boldsymbol{p}}"
    assert expand_macros(r"\mat{X}") == r"{\color{blue}\boldsymbol{X}}"
    assert expand_macros(r"\mat X") == r"{\color{blue}\boldsymbol{X}}"
    assert expand_macros(r"\vect\alpha") == r"{\boldsymbol{\alpha}}"
    assert expand_macros(r"\vect 0") == r"{\boldsymbol{0}}"
    eq = convert_equations("a \\begin{equation}\n x=1\n \\label{eq:one}\n\\end{equation} b", Path("p.qmd"))
    assert "$$ {#eq-one}" in eq and "\\label" not in eq, eq
    assert EQ_LABELS.pop("eq:one") == ("eq-one", Path("p.qmd"))
    fixed = unescape_markdown("::: center\n  a   b\n  --- ---\n  1   2\n:::")
    assert ":::" not in fixed and fixed.startswith("a   b"), fixed
    code = "Fit:\n\n    glm(y ~ x, family = binomial(link = \"probit\"))\n\nThen\n\n  a     b\n  ---   ---\n  probit 1\n"
    assert layout_blocks(code) and len(layout_blocks(code)) == 2, layout_blocks(code)
    listed = "-   An item\n\n    a continuation about probit\n"
    assert layout_blocks(listed) == [], layout_blocks(listed)
    fixed = unescape_markdown("Table:\n::: center\n       x   y\n  --- --- ---\n  r   1   2\n:::\nAfter")
    assert "\n     x   y\n" in fixed and ":::" not in fixed, fixed
    fenced = "```\n\\xvec\n```"
    assert expand_macros(fenced) == fenced
    sample = (
        r"\begin{enumerate}[label=(\alph*)]"
        r"\item First"
        r"\item Second"
        r"\begin{enumerate}[label=(\roman*)]\item inner\end{enumerate}"
        r"\end{enumerate}"
    )
    rendered = convert_enumerates(sample)
    assert "(a)" in rendered and "(b)" in rendered and "(i)" in rendered
    assert r"\item" not in rendered


def clean_output() -> None:
    for name in ("notes", "questions", "answers", "reference", "articles"):
        path = WIKI / name
        if not path.exists():
            continue
        for child in path.rglob("*"):
            if child.is_file():
                child.unlink()
        for child in sorted(path.rglob("*"), key=lambda item: len(item.parts), reverse=True):
            if child.is_dir():
                try:
                    child.rmdir()
                except OSError:
                    pass
        try:
            path.rmdir()
        except OSError:
            pass


# ---------------------------------------------------------------------------
# Topics
#
# Every question is filed under one chapter, so a chapter page can list all of
# the questions on it, whatever booklet they came from. Book exercises already
# belong to a chapter. The practice set, the final booklet and the concept
# checks are filed by hand below.
# ---------------------------------------------------------------------------

CHAPTER_CODES = {
    "B1": "bayes-01-foundations.qmd",
    "B2": "bayes-02-beta-binomial.qmd",
    "B3": "bayes-03-normal-models.qmd",
    "B4": "bayes-04-mcmc.qmd",
    "B5": "bayes-05-categorical.qmd",
    "B6": "bayes-06-testing.qmd",
    "B7": "bayes-07-exponential-families.qmd",
    "B8": "bayes-08-hierarchy.qmd",
    "B9": "bayes-09-linear-regression.qmd",
    "G1": "01-introduction-to-glms.qmd",
    "G2": "02-inference-and-counts.qmd",
    "G3": "03-gamma-and-quasi.qmd",
    "G4": "04-categorical-responses.qmd",
    "G5": "05-comparisons-and-deviance.qmd",
    "G6": "06-pit-residuals.qmd",
    "S1": "06-smooth-means.qmd",
    "S2": "07-additive-and-mixed.qmd",
    "C1": "08-random-intercepts.qmd",
    "C2": "08-slopes-and-glmms.qmd",
    "C3": "09-marginal-models.qmd",
    "C4": "10-plants-and-series.qmd",
    "T1": "12-time-series.qmd",
    "T2": "11-forecasting.qmd",
}

# Practice questions 1-59, in order.
PRACTICE_TOPICS = (
    "B7 B7 B1 B4 B4 B2 B3 B1 B4 B4 "
    "B6 B7 B1 B4 B1 B1 B2 B4 B4 B3 "
    "B6 B5 B8 B9 B4 B4 B7 B3 B6 G2 "
    "G2 G2 G1 G5 G1 S1 S2 S1 C2 C2 "
    "C2 B2 B3 B6 G3 G4 G3 B7 B3 B4 "
    "B4 B4 B6 G2 G3 G1 G1 B3 B4"
).split()

# Concept checks C1-C50, in order.
CONCEPT_TOPICS = (
    "B1 B2 B7 B7 B1 B1 B1 B6 B8 B3 "
    "B4 B4 B4 B4 B4 G1 G1 G1 G1 G1 "
    "G2 G2 G3 G4 G4 G5 G3 G3 G5 G5 "
    "S1 S1 S2 C1 C2 C3 C3 C3 C3 C3 "
    "C3 T1 T1 T1 T1 T1 T2 T1 T2 T1"
).split()

FINAL_TOPICS = {
    "ex-norm-mean": "B3",
    "ex-norm-var": "B3",
    "ex-norm-both": "B3",
    "ex-norm-nig": "B3",
    "ex-reg-nichisq": "B9",
    "ex-gibbs-geom": "B4",
    "ex-lognormal-var": "B3",
    "ex-device-bf": "B6",
    "ex-gibbs-mh": "B4",
    "ex-downtime": "B7",
    "ex-geom-beta": "B7",
    "ex-improper-normal": "B3",
    "ex-binom-beta-joint": "B4",
    "ex-mammal-ig": "B7",
    "ex-battery-bf": "B6",
    "ex-mixed-gibbs": "B4",
    "ex-pois-hier": "B8",
    "ex-model-selection": "B6",
    "ex-fish-poisson": "G2",
    "ex-toenail-glmm": "C2",
    "ex-cholesterol-gam": "S1",
    "ex-orthodont-lmm": "C2",
}

SOURCE_ORDER = ["book", "practice", "final", "concepts"]


def assign_topics(questions: list[dict]) -> None:
    if len(PRACTICE_TOPICS) != 59 or len(CONCEPT_TOPICS) != 50:
        raise SystemExit("Topic tables have the wrong length")
    for q in questions:
        if q["group"] == "book":
            q["topic"] = q["chapter_file"]
        elif q["group"] == "practice":
            q["topic"] = CHAPTER_CODES[PRACTICE_TOPICS[q["n"] - 1]]
        elif q["group"] == "concepts":
            q["topic"] = CHAPTER_CODES[CONCEPT_TOPICS[q["n"] - 1]]
        else:
            code = FINAL_TOPICS.get(q["id"])
            if not code:
                raise SystemExit(f"Final question {q['id']} has no topic")
            q["topic"] = CHAPTER_CODES[code]


def short_label(q: dict) -> str:
    """A short name for previous/next links."""
    if q["group"] == "practice":
        return f"Q{q['n']}"
    if q["group"] == "concepts":
        return f"C{q['n']}"
    if q["group"] == "final":
        return f"Question {q['n']}"
    return q["title"]


def cell(text: str) -> str:
    return text.replace("|", "\\|")


def question_table(questions: list[dict], page: Path, with_topic: bool = False) -> str:
    head = ["Question"]
    if with_topic:
        head.append("Topic")
    head.append("Answer")
    rows = ["| " + " | ".join(head) + " |", "|" + "|".join([":--"] * (len(head) - 1) + [":-:"]) + "|"]
    for q in questions:
        bits = [f"[{cell(q['title'])}]({href(page, q['path'])})"]
        if with_topic:
            topic = q["topic_note"]
            bits.append(f"[{cell(topic['title'])}]({href(page, topic['path'])})")
        bits.append("✓" if q.get("answer") else "–")
        rows.append("| " + " | ".join(bits) + " |")
    return "::: {.qtable}\n" + "\n".join(rows) + "\n:::\n"


def filter_box(placeholder: str) -> str:
    return f"""```{{=html}}
<div class="qfilter"><input type="search" placeholder="{placeholder}" aria-label="{placeholder}" oninput="wikiFilter(this.value)"><span class="qfilter-count"></span></div>
```
"""


RANDOM_AND_FILTER_JS = """<script>
(function () {
  var Q = __QUESTIONS__;
  var meta = document.querySelector('meta[name="quarto:offset"]');
  var offset = meta ? meta.getAttribute("content") : "./";
  document.addEventListener("click", function (event) {
    var link = event.target.closest ? event.target.closest("a") : null;
    if (!link) return;
    var target = link.getAttribute("href") || "";
    if (target.slice(-7) !== "#random") return;
    event.preventDefault();
    window.location.href = offset + Q[Math.floor(Math.random() * Q.length)];
  });
  // Highlight the top-bar section for this page's folder.
  var here = window.location.pathname.replace(/\\\\/g, "/");
  var section = /\\/notes\\//.test(here) ? "notes/index.html"
    : /\\/questions\\//.test(here) ? "questions/index.html"
    : /\\/reference\\/glossary|\\/articles\\//.test(here) ? "reference/glossary.html"
    : /\\/reference\\//.test(here) ? "reference/index.html"
    : "index.html";
  document.querySelectorAll("#navbarCollapse .nav-link").forEach(function (link) {
    var target = (link.getAttribute("href") || "").replace(/^(\\.\\.\\/|\\.\\/)+/, "");
    var on = target === section;
    link.classList.toggle("active", on);
    if (on) link.setAttribute("aria-current", "page"); else link.removeAttribute("aria-current");
  });
  window.wikiFilter = function (text) {
    var words = text.toLowerCase().split(/\\s+/).filter(Boolean);
    var shown = 0;
    document.querySelectorAll(".qtable tbody tr").forEach(function (row) {
      var hay = row.textContent.toLowerCase();
      var ok = words.every(function (w) { return hay.indexOf(w) >= 0; });
      row.style.display = ok ? "" : "none";
      if (ok) shown += 1;
    });
    document.querySelectorAll("main section.level2, main section.level3").forEach(function (sec) {
      var rows = sec.querySelectorAll(".qtable tbody tr");
      if (!rows.length) return;
      var any = Array.prototype.some.call(rows, function (r) { return r.style.display !== "none"; });
      sec.style.display = any || !words.length ? "" : "none";
    });
    var count = document.querySelector(".qfilter-count");
    if (count) count.textContent = words.length ? shown + " shown" : "";
  };
})();
</script>
"""


# ---------------------------------------------------------------------------
# Anchors, glossary, term links and backlinks
#
# 1. Every top-level heading in a chapter gets a stable id, and every
#    definition, theorem and proposition box is recorded. Those records are
#    the glossary.
# 2. The first mention of a key term on a page links to where the term is
#    defined (TERMS below). The book itself rarely links between chapters, so
#    without this there would be nothing to preview and nothing for
#    "What links here" to list.
# 3. Links in the content of every page are collected, and each chapter lists
#    the pages that link to it.
# ---------------------------------------------------------------------------

HEADING_ANCHORS: dict[tuple[str, str], str] = {}  # (chapter file, heading text) -> id
GLOSSARY: list[dict] = []

DIV_OPEN = re.compile(r"^(:{3,})\s*(\{[^}]*\}|[\w-]+)")
DIV_CLOSE = re.compile(r"^:{3,}\s*$")
BOX_OPEN = re.compile(r"^:{3,}\s*\{#((?:def|thm|prp|cor|rem)-[\w-]+)\s+\.(definition|theorem|proposition|corollary|remark)\}")
HEADING = re.compile(r"^(#{2,3})\s+(.+?)\s*(\{[^}]*\})?\s*$")

# Boxes whose source has no title line.
BOX_TITLES = {
    "def-expfam": "Exponential family",
    "def-glm": "Generalised linear model",
    "def-canonical": "Canonical link",
    "def-quasi": "Quasi-score and quasi-likelihood",
    "def-propodds": "Proportional-odds model",
    "def-multinom": "Baseline-category logit model",
    "def-marginal": "Marginal model",
    "def-definition": "Sufficient statistic",
    "def-definition-2": "Complete statistic",
    "thm-moments": "Mean and variance of an exponential family",
    "thm-wold": "Wold decomposition",
}

# Headings that are not topics in their own right.
SKIP_HEADINGS = {"key idea", "exercises", "questions on this topic", "see also", "what links here", "what this chapter does not cover"}

# Index entries that point at another entry.
SEE_ALSO = {
    "GLM": "Generalised linear model",
    "GLMM": "A Bernoulli response",
    "GAM": "Sums of smooth functions",
    "GEE": "Marginal model",
    "MCMC": "Markov chain",
    "HPD interval": "Credible-region constructions",
    "OLS": "Ordinary least squares",
    "ARMA": "Autoregression and moving averages",
    "Bayes factor": "Marginal likelihood and Bayes factor",
    "Sufficiency": "Sufficient statistic",
    "Deviance, analysis of": "Analysis of deviance",
}


def plain(text: str) -> str:
    """Heading text without math, markup or attributes, for ids and sorting."""
    text = re.sub(r"\$[^$]*\$", "", text)
    text = re.sub(r"[*_`\\]", "", text)
    return " ".join(text.replace("--", "–").split())


def heading_slug(text: str) -> str:
    return "s-" + (re.sub(r"[^a-z0-9]+", "-", plain(text).lower()).strip("-") or "section")


def snippet_from(lines: list[str]) -> str:
    """The first sentence or two of a definition, short enough for a table cell."""
    text = []
    for line in lines:
        if not line.strip():
            if text:
                break
            continue
        if line.lstrip().startswith(("$$", ":::", "#", "|", "!")):
            break
        text.append(line.strip())
    out = " ".join(text)
    # Never cut inside inline math: stop at a sentence end with even $ parity.
    if len(out) > 240:
        cut = None
        for match in re.finditer(r"[.;:](\s|$)", out):
            if match.end() > 240:
                break
            if out[: match.start()].count("$") % 2 == 0:
                cut = match.end()
        out = out[:cut].strip() if cut else ""
    return out.rstrip(",;:") + (" …" if out and not out.endswith((".", "?")) else "")


# ---------------------------------------------------------------------------
# Articles
#
# Every named object (a definition, theorem, proposition, corollary or remark
# box, or a card on the distribution sheet) gets a short page of its own in
# articles/. The chapter keeps the box and the derivation; the article is the
# lookup page. A box and a card with the same name share one article.
# ---------------------------------------------------------------------------

ARTICLES: dict[str, dict] = {}  # slug -> article
BOX_ARTICLE: dict[str, str] = {}  # box id -> slug
ARTICLE_DIR = WIKI / "articles"
DIST_SHEET = WIKI / "reference" / "distributions.qmd"
KIND_HEADINGS = {
    "definition": "Definition",
    "theorem": "Statement",
    "proposition": "Statement",
    "corollary": "Statement",
    "remark": "Remark",
}


def new_article(slug_: str, term: str) -> dict:
    article = {
        "slug": slug_,
        "path": ARTICLE_DIR / f"{slug_}.qmd",
        "term": term,
        "box": None,
        "card": None,
        "aliases": [],
    }
    ARTICLES[slug_] = article
    return article


def register_box_article(note, part, ident, kind, term, lines, snippet) -> dict:
    s = slug(term)
    if s in ARTICLES and ARTICLES[s]["box"] is not None:
        s = f"{s}-{note['path'].stem}"  # two boxes with one name in different chapters
    article = ARTICLES.get(s) or new_article(s, term)
    article["term"] = term
    article["box"] = {
        "chapter": note["path"],
        "chapter_title": note["title"],
        "part": part,
        "anchor": ident,
        "kind": kind,
        "lines": list(lines),
        "snippet": snippet,
    }
    BOX_ARTICLE[ident] = s
    return article


def dist_anchor(name: str) -> str:
    return "dist-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def distribution_cards() -> list[tuple[str, str]]:
    """(name, card body) for each card on the distribution sheet."""
    return [
        (m.group(1).strip(), m.group(2).strip())
        for m in re.finditer(r"::: \{\.dist-card\}\n### (.+?)\n(.*?)\n:::", distributions_body(), flags=re.S)
    ]


def register_card_articles() -> None:
    for name, body in distribution_cards():
        term = f"{name} distribution"
        article = ARTICLES.get(slug(term)) or new_article(slug(term), term)
        article["card"] = {"name": name, "anchor": dist_anchor(name), "body": body}


def article_home(article: dict) -> Path:
    return article["box"]["chapter"] if article["box"] else DIST_SHEET


MD_LINK_TARGET = re.compile(r"(!?\[(?:[^\[\]]|\[[^\]]*\])*\]\()([^)\s]+)((?:\s+\"[^\"]*\")?\))")


def rebase_links(text: str, source: Path, target: Path) -> str:
    """Rewrite relative links in text copied from one page to another."""

    def repl(match: re.Match) -> str:
        link = match.group(2)
        if re.match(r"^(?:[a-z]+:|/)", link):
            return match.group(0)
        path, _, fragment = link.partition("#")
        if not path and fragment in ANCHOR_PAGES:
            return match.group(0)  # an exercise or answer anchor: resolve_links maps it to its page
        resolved = Path(os.path.normpath(source.parent / path)) if path else source
        new = href(target, resolved) + (f"#{fragment}" if fragment else "")
        return match.group(1) + new + match.group(3)

    return protect_code(text, lambda segment: MD_LINK_TARGET.sub(repl, segment))


def copy_for_article(text: str, source: Path, article_path: Path) -> str:
    """Box or card text, ready to sit on an article page."""
    text = rebase_links(text, source, article_path)
    text = localize_refs(text, href(article_path, source))  # @fig-, @def- and the like point at the chapter
    text = re.sub(r"\$\$\s*\{#eq-[\w-]+\}", "$$", text)  # numbering belongs to the chapter
    text = re.sub(r"\[\^[^\]]+\](?!:)", "", text)  # the chapter's footnotes are not copied
    # A box that opens "Therefore ..." follows a derivation in its chapter; out of
    # that context the connective dangles, so a copy drops it.
    text = re.sub(r"\A\s*(?:Therefore|Hence|Thus|So),?\s+(\w?)", lambda m: m.group(1).upper(), text.lstrip())
    # Heading ids belong to the source page; two copies on one page would clash.
    text = re.sub(r"^(#{1,6} .*?)\s*\{#[\w-]+\s*([^}]*)\}\s*$", lambda m: m.group(1) + (f" {{{m.group(2).strip()}}}" if m.group(2).strip() else ""), text, flags=re.M)
    return text.strip()


def demote_headings(text: str) -> str:
    """One level down, so a copied answer's headings sit under its example's title."""
    return protect_code(text, lambda s: re.sub(r"^(#{2,5}) ", r"#\1 ", s, flags=re.M))


EXAMPLE_OPEN = re.compile(r"^:{3,}\s*\{#(exm-[\w-]+)\s+\.example\}")
FIGURE_MD = re.compile(r"!\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]*figures/([^)\s/]+))\)(\{[^}]*\})?")
BOOK_EXAMPLE_BOXES: dict[str, dict] = {}  # exm- id -> title, lines, chapter
FIGURE_INFO: dict[str, dict] = {}  # figure file -> caption, chapter, id
CHAPTER_FIGURES_SEEN: dict[Path, list[str]] = {}


def box_contents(lines: list[str], i: int) -> tuple[str | None, list[str]]:
    """Title (the box's own "## " line, if any) and content lines of the div opened at line i."""
    j = i + 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    title = None
    if j < len(lines) and lines[j].startswith("## "):
        title, j = lines[j][3:].strip(), j + 1
    out, inner = [], 0
    while j < len(lines):
        if DIV_CLOSE.match(lines[j]) and inner == 0:
            break
        if DIV_OPEN.match(lines[j]):
            inner += 1
        elif DIV_CLOSE.match(lines[j]):
            inner -= 1
        out.append(lines[j])
        j += 1
    return title, out


def index_chapter(note: dict, part: str, body: str) -> str:
    """Give each top-level heading an id and record the glossary entries."""
    fname = note["path"].name
    for match in FIGURE_MD.finditer(body):
        caption, src, file, attrs = match.groups()
        found = re.search(r"#(fig-[\w-]+)", attrs or "")
        FIGURE_INFO.setdefault(
            file,
            {"caption": caption.strip(), "chapter": note["path"], "chapter_title": note["title"], "id": found.group(1) if found else ""},
        )
        CHAPTER_FIGURES_SEEN.setdefault(note["path"], []).append(file)
    lines = body.split("\n")
    for i, line in enumerate(lines):
        example = EXAMPLE_OPEN.match(line)
        if example:
            title, content = box_contents(lines, i)
            BOOK_EXAMPLE_BOXES[example.group(1)] = {
                "title": plain(title or example.group(1)),
                "lines": content,
                "chapter": note["path"],
                "chapter_title": note["title"],
            }
    out = []
    depth = 0
    in_code = False
    used: set[str] = set()
    pending: dict[int, str] = {}  # line index of a box's closing fence -> link up to its article
    i = 0
    while i < len(lines):
        line = lines[i]
        if i in pending:
            out.extend(["", pending.pop(i), ""])
        if FENCE.match(line):
            in_code = not in_code
            out.append(line)
            i += 1
            continue
        if in_code:
            out.append(line)
            i += 1
            continue
        box = BOX_OPEN.match(line)
        if box:
            ident, kind = box.groups()
            # The box's own title is the next "## " line inside it, if any.
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            title = BOX_TITLES.get(ident)
            content_start = j
            if j < len(lines) and lines[j].startswith("## "):
                title = title or lines[j][3:].strip()
                content_start = j + 1
            title = title or ident.split("-", 1)[1].replace("-", " ").capitalize()
            box_lines = []
            k, inner = content_start, 0
            while k < len(lines):
                if DIV_CLOSE.match(lines[k]) and inner == 0:
                    break
                if DIV_OPEN.match(lines[k]):
                    inner += 1
                elif DIV_CLOSE.match(lines[k]):
                    inner -= 1
                box_lines.append(lines[k])
                k += 1
            snippet = snippet_from(box_lines)
            article = register_box_article(note, part, ident, kind, plain(title), box_lines, snippet)
            GLOSSARY.append(
                {
                    "term": plain(title),
                    "kind": kind,
                    "page": note["path"],
                    "anchor": ident,
                    "where": note["title"],
                    "snippet": snippet,
                    "article": article["slug"],
                }
            )
            HEADING_ANCHORS[(fname, plain(title))] = ident
            HEADING_ANCHORS[(fname, ident)] = ident
            # The box stays in the chapter and points up to its article.
            pending[k] = f"[Article: {article['term']} →]({href(note['path'], article['path'])}){{.box-article}}"
        if DIV_OPEN.match(line):
            depth += 1
        elif DIV_CLOSE.match(line):
            depth = max(0, depth - 1)
        heading = HEADING.match(line)
        if heading and depth == 0:
            hashes, text, attrs = heading.groups()
            if plain(text).lower() not in SKIP_HEADINGS:
                ident = None
                if attrs:
                    found = re.search(r"#([\w-]+)", attrs)
                    ident = found.group(1) if found else None
                if not ident:
                    ident = heading_slug(text)
                    while ident in used:
                        ident += "-x"
                    line = f"{hashes} {text} {{#{ident}}}" if not attrs else f"{hashes} {text} {attrs[:-1]} #{ident}}}"
                used.add(ident)
                HEADING_ANCHORS[(fname, plain(text))] = ident
                GLOSSARY.append(
                    {
                        "term": plain(text),
                        "kind": "section",
                        "page": note["path"],
                        "anchor": ident,
                        "where": note["title"],
                        "snippet": "",
                    }
                )
        out.append(line)
        i += 1
    return "\n".join(out)


# Term links: (pattern, chapter code, heading text or box id, parts where it applies).
# Order matters: a longer or more specific phrase must come before a shorter one.
B, G, S, C, T = "Bayesian statistics", "Generalised linear models", "Smoothing", "Correlated data", "Time series"
TERMS = [
    # Bayesian foundations
    (r"highest[- ](?:posterior[- ])?density (?:intervals?|regions?)|HPD (?:intervals?|regions?)", "B1", "def-credible-region-constructions", None),
    (r"equal-tailed (?:credible )?intervals?", "B1", "def-credible-region-constructions", None),
    (r"credible intervals?", "B1", "def-bayesian-credible-interval", None),
    (r"(?:prior|posterior) predictive distributions?", "B1", "def-prior-and-posterior-predictive-distributions", None),
    (r"improper priors?", "B1", "def-proper-prior-and-proper-posterior", None),
    (r"Bayes'? (?:rule|theorem)", "B1", "thm-bayes-rule", None),
    (r"MAP estimates?|posterior mode", "B1", "def-posterior-point-summaries", None),
    (r"Monte Carlo (?:standard )?errors?", "B1", "prp-posterior-summaries-from-draws", None),
    # Beta-Binomial and normal models
    (r"Beta(?:--|–|-)Binomial", "B2", "prp-beta-binomial-conjugacy", None),
    (r"Beta distributions?|Beta priors?", "B2", "def-beta-distribution", None),
    # Distribution-sheet articles. "ART" names an article by its slug.
    (r"Binomial distributions?", "ART", "binomial-distribution", None),
    (r"Geometric distributions?", "ART", "geometric-distribution", None),
    (r"Multinomial distributions?", "ART", "multinomial-distribution", None),
    (r"Poisson distributions?", "ART", "poisson-distribution", None),
    (r"Exponential distributions?", "ART", "exponential-distribution", None),
    (r"(?<!inverse )(?<!inverse-)Gamma distributions?", "ART", "gamma-distribution", None),
    (r"Normal distributions?", "ART", "normal-distribution", None),
    (r"pseudo-counts?", "B2", "Pseudo-counts and sequential updating", None),
    (r"Normal(?:--|–|-)Normal", "B3", "def-normal-normal-model", None),
    (r"Normal(?:--|–|-)inverse(?:--|–|-| )Gamma", "B9", "thm-normal-inverse-gamma-conjugacy", None),
    (r"inverse[- ]Gamma(?: distributions?| priors?)?", "B3", "def-inverse-gamma-distribution", None),
    (r"precision[- ]weight(?:ing|ed)", "B3", "rem-precision-weighting", None),
    # MCMC
    (r"Markov chains?|MCMC", "B4", "def-markov-chain", None),
    (r"detailed balance", "B4", "def-stationarity-and-detailed-balance", None),
    (r"stationary distributions?", "B4", "def-stationarity-and-detailed-balance", None),
    (r"full conditionals?(?: distributions?)?|Gibbs sampl(?:ers?|ing)", "B4", "def-systematic-scan-gibbs-sampler", None),
    (r"Metropolis(?:--|–|-)Hastings|random-walk Metropolis|acceptance probabilit(?:y|ies)", "B4", "def-metropolis-hastings-update", None),
    (r"warm-up|burn-in", "B4", "rem-warm-up-is-not-a-convergence-proof", None),
    # Dirichlet, testing
    (r"Dirichlet(?:--|–|-)Multinomial", "B5", "thm-dirichlet-multinomial-conjugacy", None),
    (r"Dirichlet(?: distributions?| priors?)?", "B5", "def-dirichlet-distribution", None),
    (r"Bayes factors?|marginal likelihoods?", "B6", "def-marginal-likelihood-and-bayes-factor", None),
    (r"posterior odds|prior odds", "B6", "thm-posterior-odds-factorisation", None),
    (r"posterior (?:model|hypothesis) probabilit(?:y|ies)", "B6", "def-posterior-hypothesis-probability", None),
    # Exponential families
    (r"minimal sufficien(?:t|cy)", "B7", "def-minimal-sufficiency", None),
    (r"Fisher(?:--|–|-)Neyman(?: factori[sz]ation)?|factori[sz]ation theorem", "B7", "thm-fisher-neyman-factorisation", None),
    (r"sufficient statistics?|sufficiency", "B7", "def-definition", None),
    (r"complete statistics?|completeness", "B7", "def-definition-2", None),
    (r"ancillary statistics?|ancillarity", "B7", "def-ancillary-statistic", None),
    (r"Basu'?s theorem", "B7", "thm-basu-s-theorem", None),
    (r"natural exponential famil(?:y|ies)", "B7", "def-natural-exponential-family", None),
    (r"conjugate priors?|conjugacy", "B7", "prp-generic-exponential-family-conjugate-update", None),
    # Hierarchies and regression
    (r"hierarchical (?:Bayes(?:ian)? )?models?|hierarchical Bayes", "B8", "def-hierarchical-bayesian-model", None),
    (r"hyperparameters?|hyperpriors?", "B8", "def-hyperparameter", None),
    (r"exchangeab(?:le|ility)", "B8", "def-exchangeability", None),
    (r"empirical Bayes", "B8", "def-empirical-bayes", None),
    (r"shrinkage", "B8", "prp-normal-hierarchical-shrinkage", None),
    (r"Gaussian linear models?", "B9", "def-gaussian-linear-model", None),
    (r"ordinary least squares|least[- ]squares estimat(?:es?|ors?)|OLS", "B9", "prp-ordinary-least-squares", None),
    (r"reference priors?", "B9", "Likelihood and reference prior", None),
    # GLMs
    (r"generali[sz]ed linear mixed models?|GLMMs?", "C2", "A Bernoulli response", None),
    (r"generali[sz]ed linear models?|GLMs?", "G1", "def-glm", None),
    (r"generali[sz]ed estimating equations?|GEEs?", "C3", "def-marginal", None),
    (r"generali[sz]ed additive models?|GAMs?", "S2", "Sums of smooth functions", None),
    (r"exponential famil(?:y|ies)", "G1", "def-expfam", None),
    (r"natural parameters?", "G1", "def-expfam", {G, S, C}),
    (r"natural parameters?", "B7", "def-natural-exponential-family", {B}),
    (r"canonical links?", "G1", "def-canonical", None),
    (r"link functions?|linear predictors?", "G1", "The three components of a GLM", None),
    (r"Fisher scoring|IRLS|iteratively reweighted least squares", "G1", "Fisher scoring", None),
    (r"Fisher information|score (?:functions?|vectors?|equations?)", "G1", "Maximum likelihood and Fisher scoring", None),
    (r"logistic regressions?|logit links?", "G1", "Interpreting a logistic regression", None),
    (r"probit", "G1", "Three links", None),
    (r"quasi-Poisson", "G2", "Quasi-Poisson", None),
    (r"over-?dispers(?:ion|ed)", "G2", "Quasi-Poisson", None),
    (r"negative[- ]binomial", "G2", "Two models with a real distribution", None),
    (r"Poisson regressions?|log-linear (?:models?|coefficients?)", "G2", "Reading a log-linear coefficient", None),
    (r"quasi-likelihood|quasi-score", "G3", "def-quasi", None),
    (r"under-?dispers(?:ion|ed)", "G3", "Bids for a bankrupt firm", None),
    (r"Gamma (?:GLMs?|regressions?)", "G3", "Positive continuous responses", None),
    (r"proportional[- ]odds", "G4", "def-propodds", None),
    (r"baseline[- ]category(?: logits?)?|multinomial logit|multinomial logistic(?: regression)?", "G4", "def-multinom", None),
    (r"Bradley(?:--|–|-)Terry", "G5", "Bradley–Terry", None),
    (r"analysis of deviance", "G5", "Analysis of deviance", None),
    (r"saturated models?|residual deviance|null deviance|deviance", "G5", "Deviance", None),
    (r"PIT residuals?|probability-integral(?:[- ]transform)? residuals?|randomi[sz]ed quantile residuals?", "G6", "", None),
    # Smoothing
    (r"roughness penalty|smoothing parameters?|penali[sz]ed (?:regression )?splines?|cubic splines?|regression splines?|splines?", "S1", "A roughness penalty", None),
    (r"effective degrees of freedom|additive models?", "S2", "Sums of smooth functions", None),
    # Correlated data
    (r"random intercepts?|linear mixed models?|mixed models?", "C1", "A random intercept", None),
    (r"fixed effects?|random effects?", "C1", "What is fixed, and what is random", None),
    (r"random slopes?", "C2", "A slope that belongs to the block", None),
    (r"marginal models?|population-averaged|working correlations?|sandwich (?:estimators?|variances?|standard errors?)|robust standard errors?", "C3", "def-marginal", None),
    # Time series
    (r"Wold(?:'s)? (?:decomposition|theorem)", "T1", "thm-wold", None),
    (r"autoregressi(?:ve|on)|moving[- ]averages?|ARMA|white noise", "T1", "Autoregression and moving averages", None),
    (r"(?:weak(?:ly)?|strict(?:ly)?|second-order) stationar(?:y|ity)", "T1", "Stationarity", None),
    (r"stationar(?:y|ity)", "T1", "Stationarity", {T}),
    (r"partial autocorrelations?|autocorrelation functions?|ACF|PACF", "T1", "", None),
    (r"ARIMA|forecasting", "T2", "", None),
]

# An alternative that starts with two capitals (GLM, MAP, ACF) matches in
# capitals only, so "MAP" never links the word "map". Others ignore case.
ACRONYMS = re.compile(r"^[A-Z]{2,}")


def split_alternatives(pattern: str) -> list[str]:
    """Split a regex on its top-level | only."""
    parts, depth, current, i = [], 0, [], 0
    while i < len(pattern):
        ch = pattern[i]
        if ch == "\\":
            current.append(pattern[i : i + 2])
            i += 2
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "|" and depth == 0:
            parts.append("".join(current))
            current = []
        else:
            current.append(ch)
        i += 1
    parts.append("".join(current))
    return parts

_COMPILED: list[tuple] = []  # (loose, strict, target page, anchor, scope, home chapter)

PROTECT = re.compile(
    r"```.*?```"  # fenced code
    r"|`[^`\n]*`"  # inline code
    r"|\$\$.*?\$\$|\$(?:\\.|[^$\\\n])+\$"  # math
    r"|\\begin\{(?P<env>[a-z*]+)\}.*?\\end\{(?P=env)\}"  # raw LaTeX math environments
    r"|!?\[(?:[^\[\]\n]|\[[^\]\n]*\])*\]\([^)\n]*\)(?:\{[^}\n]*\})?"  # links and images
    r"|\[[^\]\n]*\]\{[^}\n]*\}"  # spans
    r"|^#{1,6} [^\n]*$"  # headings
    r"|^:{3,}[^\n]*$"  # div fences
    r"|\{[#.][^}\n]*\}"  # attributes
    r"|<[^>\n]+>"  # html tags
    r"|https?://\S+"  # bare urls
    r"|\[\^[^\]\n]+\]",  # footnote markers
    re.S | re.M,
)


def compile_terms(notes: dict) -> None:
    """Resolve TERMS. A term whose target is a named box links to its article."""
    missing = []
    for pattern, code, key, scope in TERMS:
        if code == "ART":
            article = ARTICLES.get(key)
            if not article:
                missing.append(f"article {key}")
                continue
            page, anchor, home = article["path"], "", article_home(article)
        else:
            fname = CHAPTER_CODES[code]
            page = home = notes[fname]["path"]
            if key == "":
                anchor = ""
            elif key.startswith(("def-", "thm-", "prp-", "cor-", "rem-")):
                anchor = HEADING_ANCHORS.get((fname, key), "")
                if not anchor:
                    missing.append(f"{code} {key}")
                if key in BOX_ARTICLE:
                    page, anchor = ARTICLES[BOX_ARTICLE[key]]["path"], ""
            else:
                anchor = HEADING_ANCHORS.get((fname, plain(key)), "")
                if not anchor:
                    missing.append(f"{code} {key}")
        words = split_alternatives(pattern)
        acro = "|".join(w for w in words if ACRONYMS.match(w))
        rest = "|".join(w for w in words if not ACRONYMS.match(w))
        # An en dash joins names too: "Beta–Binomial distribution" is not a binomial distribution.
        loose = re.compile(rf"(?<![\w–-])(?:{rest})(?![\w–-])", re.I) if rest else None
        strict = re.compile(rf"(?<![\w–-])(?:{acro})(?![\w–-])") if acro else None
        _COMPILED.append((loose, strict, page, anchor, scope, home))
    if missing:
        raise SystemExit("Term links point at missing anchors: " + ", ".join(missing))


LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)]|\(\w+\))\s")
TABLE_RULE = re.compile(r"^\s*(?:-{3,}(?:\s+-{3,})+|\+[-=+:]+\+)\s*$")


def layout_blocks(text: str) -> list[tuple[int, int]]:
    """Spans where inserted text would break the layout.

    These are indented code blocks, and simple or grid tables, whose columns
    line up by spaces. Indented list continuations are left alone.
    """
    spans = []
    blocks = [(m.start(), m.end()) for m in re.finditer(r"(?:^[^\n]*\S[^\n]*(?:\n|$))+", text, flags=re.M)]
    prev_kind = "text"
    for start, end in blocks:
        lines = text[start:end].rstrip("\n").split("\n")
        indented = all(len(l) - len(l.lstrip(" ")) >= 4 for l in lines)
        if any(TABLE_RULE.match(l) for l in lines):
            spans.append((start, end))
            kind = "table"
        elif indented and prev_kind in {"text", "code", "table"}:
            spans.append((start, end))
            kind = "code"
        elif LIST_ITEM.match(lines[0]) or indented:
            kind = "list"
        else:
            kind = "text"
        prev_kind = kind
    return spans


def autolink(text: str, page: Path, part: str | None) -> str:
    """Link the first mention of each term on the page to its definition."""
    spans = [(m.start(), m.end()) for m in PROTECT.finditer(text)] + layout_blocks(text)
    spans.sort()
    merged: list[list[int]] = []
    for start, end in spans:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    segments: list[list] = []  # [text, protected]
    last = 0
    for start, end in merged:
        segments.append([text[last:start], False])
        segments.append([text[start:end], True])
        last = end
    segments.append([text[last:], False])
    done: set[tuple[Path, str]] = set()
    for loose, strict, target, anchor, scope, home in _COMPILED:
        # No link to the page itself, nor from the chapter that teaches the term.
        if target == page or home == page or (target, anchor) in done:
            continue
        if scope is not None and part not in scope:
            continue
        for i, (segment, protected) in enumerate(segments):
            if protected:
                continue
            hits = [m for m in (loose.search(segment) if loose else None, strict.search(segment) if strict else None) if m]
            if not hits:
                continue
            m = min(hits, key=lambda h: h.start())
            link = f"[{m.group(0)}]({href(page, target)}{'#' + anchor if anchor else ''}){{.term}}"
            segments[i : i + 1] = [[segment[: m.start()], False], [link, True], [segment[m.end() :], False]]
            done.add((target, anchor))
            break
    return "".join(segment for segment, _ in segments)


CONTENT_LINK = re.compile(r"\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s#]+\.qmd)(?:#[^)\s]*)?(?:\s+\"[^\"]*\")?\)")


def links_in(text: str, page: Path) -> list[tuple[Path, str]]:
    found = []
    for match in CONTENT_LINK.finditer(text):
        target = Path(os.path.normpath(page.parent / match.group(2)))
        if target != page:
            found.append((target, plain(match.group(1))))
    return found


PAGE_ORDER: list[Path] = []
COPIED_LABELS = {"property", "example"}  # article blocks copied from other pages


PREVIEW_JS = r"""<div id="wiki-preview" role="tooltip" hidden></div>
<script>
// Link previews: hover over a link to another page to see what is there.
(function () {
  if (window.matchMedia && !window.matchMedia("(hover: hover)").matches) return;
  var box = document.getElementById("wiki-preview");
  var cache = {}, showTimer = null, hideTimer = null, current = null;
  var meta = document.querySelector('meta[name="quarto:offset"]');
  var offset = meta ? meta.getAttribute("content") : "./";

  function getDoc(url) {
    if (!cache[url]) {
      cache[url] = fetch(url).then(function (r) {
        if (!r.ok) throw new Error(r.status);
        return r.text();
      }).then(function (html) { return new DOMParser().parseFromString(html, "text/html"); });
    }
    return cache[url];
  }

  function ensureKatex() {
    if (window.katex) return Promise.resolve();
    if (!ensureKatex.p) {
      ensureKatex.p = new Promise(function (done) {
        var css = document.createElement("link");
        // Relative to the site root, which may be a subfolder (GitHub Pages).
        css.rel = "stylesheet"; css.href = offset + "katex/katex.min.css";
        document.head.appendChild(css);
        var js = document.createElement("script");
        js.src = offset + "katex/katex.min.js"; js.onload = done; js.onerror = done;
        document.head.appendChild(js);
      });
    }
    return ensureKatex.p;
  }

  function renderMath(root) {
    root.querySelectorAll("span.math").forEach(function (el) {
      var tex = el.textContent.trim().replace(/^\\[\(\[]/, "").replace(/\\[\)\]]$/, "");
      try {
        window.katex.render(tex, el, { displayMode: el.classList.contains("display"), throwOnError: false });
      } catch (e) {}
    });
  }

  // Up to `limit` characters of blocks from a list of elements.
  function excerpt(nodes, limit) {
    var out = document.createElement("div"), used = 0;
    for (var i = 0; i < nodes.length && used < limit; i++) {
      var n = nodes[i];
      if (n.nodeType !== 1) continue;
      if (n.matches(".hatnote, .callout, #worked-answer, .qtable, .infobox, .mainarticle, script, nav, h1, h2, h3, header, .quarto-title-block, #title-block-header, .glossary-jump, .qfilter")) continue;
      if (!n.textContent.trim() && !n.querySelector("img, .math")) continue;
      out.appendChild(n.cloneNode(true));
      used += n.textContent.length;
    }
    return out;
  }

  function build(doc, url, hash) {
    var wrap = document.createElement("div");
    var titleEl = doc.querySelector("h1.title");
    var title = titleEl ? titleEl.textContent.trim() : doc.title;
    var head = document.createElement("div");
    head.className = "wp-title";
    var body = null;
    if (hash === "worked-answer") {
      head.textContent = title;
      body = document.createElement("p");
      body.className = "wp-note";
      body.textContent = "Worked answer, folded away on the question page. Open the page to reveal it.";
    } else if (hash) {
      var el = doc.getElementById(hash);
      if (el && /^(eq-)/.test(hash)) {
        head.textContent = "Equation in " + title;
        body = document.createElement("div");
        body.appendChild(el.cloneNode(true));
      } else if (el && el.tagName === "SECTION") {
        var h = el.querySelector("h2, h3, h4");
        head.textContent = (h ? h.textContent.trim() : hash) + " — " + title;
        body = excerpt(Array.prototype.slice.call(el.children), 700);
      } else if (el) {
        body = el.cloneNode(true);
        var label = body.querySelector(".theorem-title, .proof-title");
        if (label) {
          // "Definition 1 (Beta distribution)" -> heading "Beta distribution",
          // with "Definition in <chapter>" beneath. Numbers belong to the other page.
          var m = label.textContent.trim().match(/^(\w+)\s*[\d.]*\s*(?:\((.*)\))?\.?$/);
          head.textContent = m ? (m[2] || m[1]) : label.textContent.trim();
          var sub = document.createElement("div");
          sub.className = "wp-note";
          sub.textContent = (m ? m[1] : "Box") + " in " + title;
          head.appendChild(sub);
          label.remove();
        } else {
          var inner = body.querySelector("h2, h3");
          head.textContent = inner ? inner.textContent.trim() : title;
          if (inner) inner.remove();
        }
      }
    }
    if (!body) {
      head.textContent = title;
      var main = doc.querySelector("main#quarto-document-content") || doc.querySelector("main");
      var hat = main && main.querySelector(".hatnote");
      body = document.createElement("div");
      if (hat && /\/questions\//.test(url)) {
        var line = hat.cloneNode(true);
        line.querySelectorAll(".qnav").forEach(function (a) { a.remove(); });
        line.className = "wp-hat";
        body.appendChild(line);
      }
      var kids = main ? Array.prototype.slice.call(main.children) : [];
      var flat = [];
      kids.forEach(function (k) {
        if (k.tagName === "SECTION") flat = flat.concat(Array.prototype.slice.call(k.children));
        else flat.push(k);
      });
      // The infobox picture, if there is one, rides along as a thumbnail.
      var pic = main && main.querySelector(".infobox img");
      if (pic) {
        var thumb = document.createElement("img");
        thumb.className = "wp-thumb";
        thumb.alt = pic.getAttribute("alt") || "";
        thumb.src = pic.getAttribute("src");
        body.appendChild(thumb);
      }
      body.appendChild(excerpt(flat, 600));
    }
    // Fix relative links and images, and strip ids so nothing clashes with this page.
    body.querySelectorAll("[id]").forEach(function (n) { n.removeAttribute("id"); });
    body.querySelectorAll("img").forEach(function (img) { img.src = new URL(img.getAttribute("src"), url).href; });
    body.querySelectorAll("a[href]").forEach(function (a) { a.href = new URL(a.getAttribute("href"), url).href; });
    body.querySelectorAll(".footnote-ref, sup").forEach(function (n) { n.remove(); });
    wrap.appendChild(head);
    body.classList.add("wp-body");
    wrap.appendChild(body);
    return wrap;
  }

  function place(link) {
    var r = link.getBoundingClientRect();
    box.style.left = "0px"; box.style.top = "0px";
    box.hidden = false;
    var w = box.offsetWidth, h = box.offsetHeight;
    var left = Math.min(Math.max(8, r.left), window.innerWidth - w - 12);
    var top = r.bottom + 8;
    if (top + h > window.innerHeight - 8 && r.top - h - 8 > 8) top = r.top - h - 8;
    box.style.left = left + "px";
    box.style.top = top + "px";
  }

  function show(link) {
    var u = new URL(link.href, location.href);
    var page = u.origin + u.pathname;
    var hash = decodeURIComponent(u.hash.slice(1));
    current = link;
    Promise.all([getDoc(page), ensureKatex()]).then(function (res) {
      if (current !== link) return;
      box.innerHTML = "";
      box.appendChild(build(res[0], page, hash));
      renderMath(box);
      place(link);
    }).catch(function () {});
  }

  function hide() {
    current = null;
    box.hidden = true;
  }

  function previewable(a) {
    if (!a || !a.href || a.closest("#wiki-preview, .sidebar, nav, #TOC, .navbar, .pagination-link, .glossary-jump")) return false;
    var u = new URL(a.href, location.href);
    if (u.origin !== location.origin || u.hash === "#random") return false;
    if (u.pathname === location.pathname) return false;
    if (!/\.html$/.test(u.pathname)) return false;
    return !/(\/index|by-source|glossary)\.html$/.test(u.pathname);
  }

  document.addEventListener("mouseover", function (e) {
    var a = e.target.closest ? e.target.closest("a") : null;
    if (e.target.closest && e.target.closest("#wiki-preview")) { clearTimeout(hideTimer); return; }
    if (!previewable(a)) return;
    clearTimeout(hideTimer);
    clearTimeout(showTimer);
    showTimer = setTimeout(function () { show(a); }, 350);
  });
  document.addEventListener("mouseout", function (e) {
    var a = e.target.closest ? e.target.closest("a, #wiki-preview") : null;
    if (!a) return;
    clearTimeout(showTimer);
    hideTimer = setTimeout(hide, 250);
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") hide(); });
  window.addEventListener("scroll", hide, { passive: true });
})();
</script>
"""


def write_pages(notes: dict, questions: list[dict], answers: list[dict]) -> None:
    """Write every page: chapters as articles, questions with their answers folded in."""
    ids = [q["id"] for q in questions]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        raise SystemExit(f"Question ids collide: {dupes}")
    chapters = [(part, notes[name]) for part, files in PARTS for name, kind in files if kind == "notes"]
    final_notes = [notes[name] for name in ("final-preparation.qmd", "final-bayesian.qmd", "final-applied.qmd")]

    # Pair each question with its answer. Answers no longer get pages of their own.
    answers_by_id: dict[str, dict[str, dict]] = {}
    for answer in answers:
        answers_by_id.setdefault(answer["group"], {})[answer["id"]] = answer
    for q in questions:
        q["answer"] = answers_by_id.get(q["group"], {}).get(q.get("answer_id") or "")
        ANCHOR_PAGES[q["id"]] = q["path"].as_posix()
        if q["answer"]:
            ANCHOR_PAGES[q["answer"]["id"]] = q["path"].as_posix() + "#worked-answer"

    assign_topics(questions)
    for q in questions:
        q["topic_note"] = notes[q["topic"]] if q["topic"] in notes else notes["index.qmd"]

    # Order inside each source, used for previous/next links and the source lists.
    by_source: dict[str, list[dict]] = {g: [] for g in SOURCE_ORDER}
    for q in questions:
        by_source[q["group"]].append(q)
    by_source["practice"].sort(key=lambda q: q["n"])
    by_source["concepts"].sort(key=lambda q: q["n"])
    by_source["final"].sort(key=lambda q: q["n"])
    chapter_rank = {note["path"]: i for i, (_, note) in enumerate(chapters)}
    for i, q in enumerate(by_source["book"]):
        q["book_rank"] = i
    by_source["book"].sort(key=lambda q: (chapter_rank.get(q["notes_path"], 99), q["book_rank"]))

    by_topic: dict[str, list[dict]] = {}
    for group in SOURCE_ORDER:
        for q in by_source[group]:
            by_topic.setdefault(q["topic"], []).append(q)

    for note in notes.values():
        PAGE_TITLES[note["path"]] = note["title"]
    for q in questions:
        PAGE_TITLES[q["path"]] = q["title"]

    PAGE_ORDER[:] = [note["path"] for _, note in chapters] + [n["path"] for n in final_notes] + [
        n["path"] for n in notes.values() if n["kind"] == "reference"
    ]

    # Each page is a list of blocks: (is_content, label, text). Content is the
    # book's own text; the rest is navigation this script adds. Term links
    # and "What links here" use content only.
    pages: list[dict] = []

    def add_page(path, title, part, kind, blocks, meta=None):
        pages.append({"path": path, "title": title, "part": part, "kind": kind, "blocks": blocks, "meta": meta or {}})

    # Chapters.
    for part, note in chapters:
        own = by_topic.get(note["path"].name, [])
        prose = prepare(strip_first_heading(note["prose"]), "../figures", page=note["path"])
        prose = index_chapter(note, part, prose)
        hat = [f"Part of **{part}**"]
        if own:
            hat.append(f"[{len(own)} question{'s' if len(own) != 1 else ''} on this topic](#questions-on-this-topic)")
        hat.append("[What links here](#what-links-here)")
        blocks = [(False, "hatnote", "::: {.hatnote}\n" + " · ".join(hat) + "\n:::\n\n"), (True, "prose", prose)]
        if own:
            blocks.append(
                (
                    False,
                    "questions",
                    "\n\n## Questions on this topic {#questions-on-this-topic}\n\n"
                    "Open a question to attempt it. Its worked answer is folded away at the bottom of the page.\n\n"
                    + question_table(own, note["path"]),
                )
            )
        own_articles = [a for a in ARTICLES.values() if a["box"] and a["box"]["chapter"] == note["path"]]
        siblings = [n for p, n in chapters if p == part]
        blocks.insert(1, (False, "infobox", chapter_infobox(note, part, siblings, own, own_articles)))
        article_line = (
            "- Articles from this chapter: "
            + " · ".join(f"[{a['term']}]({href(note['path'], a['path'])})" for a in own_articles)
            + "\n"
            if own_articles
            else ""
        )
        blocks.append(
            (
                False,
                "see-also",
                "\n\n## See also\n\n"
                + article_line
                + f"- [All {part.lower()} chapters]({href(note['path'], WIKI / 'notes' / 'index.qmd')}#{slug(part)})\n"
                f"- [Glossary and index]({href(note['path'], WIKI / 'reference' / 'glossary.qmd')})\n"
                f"- [Distribution sheet]({href(note['path'], WIKI / 'reference' / 'distributions.qmd')}) and [formula lookup]({href(note['path'], WIKI / 'reference' / 'formulas.qmd')})\n",
            )
        )
        add_page(note["path"], note["title"], part, "chapter", blocks)

    # Reference page built from the book (formula lookup).
    for note in notes.values():
        if note["kind"] == "reference":
            body = prepare(strip_first_heading(note["prose"]), "../figures", page=note["path"])
            add_page(note["path"], note["title"], None, "reference", [(True, "prose", body)])

    # Final-preparation pages: the guide, and the two halves with their question lists.
    for note in final_notes:
        body = prepare(strip_first_heading(note["prose"]), "../figures", page=note["path"])
        blocks = [(True, "prose", body)]
        own = [q for q in by_source["final"] if q["notes_path"] == note["path"]]
        if own:
            blocks.append((False, "questions", "\n\n## Questions\n\n" + question_table(own, note["path"], with_topic=True)))
        add_page(note["path"], note["title"], None, "final", blocks)

    # Questions. Previous and next walk the other questions on the same topic.
    neighbors: dict[int, tuple[dict | None, dict | None]] = {}
    for seq in by_topic.values():
        for i, q in enumerate(seq):
            neighbors[id(q)] = (seq[i - 1] if i else None, seq[i + 1] if i + 1 < len(seq) else None)
    for q in questions:
        group = q["group"]
        prev_q, next_q = neighbors[id(q)]
        notes_href = href(q["path"], q["notes_path"]) if q.get("notes_path") else None
        use_refs = notes_href if group == "book" else None
        body = prepare(q["body"], "../figures", use_refs, page=q["path"])
        body = re.sub(r"\[Solution\]\(#sol-[\w-]+\)", "", body).strip()
        topic = q["topic_note"]
        nav = []
        if prev_q:
            nav.append(f"[‹ {cell(short_label(prev_q))}]({href(q['path'], prev_q['path'])}){{.qnav}}")
        if next_q:
            nav.append(f"[{cell(short_label(next_q))} ›]({href(q['path'], next_q['path'])}){{.qnav}}")
        hat = (
            "::: {.hatnote}\n"
            f"**Topic:** [{topic['title']}]({href(q['path'], topic['path'])}) · "
            f"[more questions on this topic]({href(q['path'], topic['path'])}#questions-on-this-topic)"
            + (("  \n" + " ".join(nav)) if nav else "")
            + "\n:::\n\n"
        )
        blocks = [(False, "hatnote", hat), (True, "question", body)]
        q["prepared_body"] = body  # reused when the question is an example on an article
        answer = q["answer"]
        if answer:
            answer_body = prepare(answer["body"], "../figures", page=q["path"])
            q["prepared_answer"] = answer_body
            blocks += [
                (False, "answer-open", "\n\n:::::::: {#worked-answer .callout-tip collapse=\"true\"}\n## Worked answer (click to show)\n\n"),
                (True, "answer", answer_body),
                (False, "answer-close", "\n::::::::\n"),
            ]
        elif group == "book":
            blocks.append((False, "no-answer", "\n\n::: {.callout-note appearance=\"minimal\"}\nThis exercise has no worked answer.\n:::\n"))
        add_page(q["path"], q["title"], topic.get("part"), "question", blocks, {"toc": "false"})

    # Articles: one per named box, merged with any distribution card of the same name.
    register_card_articles()
    for alias, target in SEE_ALSO.items():
        article = next((a for a in ARTICLES.values() if a["term"].lower() == target.lower()), None)
        if article:
            article["aliases"].append(f"{slug(alias)}.html")  # a redirect page, made by Quarto
    qmap = {q["id"]: q for q in questions}
    read_formula_tables(notes)
    check_extras(qmap)
    for article in sorted(ARTICLES.values(), key=lambda a: a["term"].lower()):
        PAGE_TITLES[article["path"]] = article["term"]
        blocks = article_blocks(article) + article_sections(article, qmap)
        meta = {"aliases": "[" + ", ".join(article["aliases"]) + "]"} if article["aliases"] else {}
        add_page(article["path"], article["term"], article["box"]["part"] if article["box"] else None, "article", blocks, meta)

    # Equation numbers first, then links that need them, then term links.
    compile_terms(notes)
    for page in pages:
        number_equations(page["path"], "".join(text for _, _, text in page["blocks"]))
    article_by_path = {a["path"]: a for a in ARTICLES.values()}
    backlinks: dict[Path, list[tuple[dict, str, str]]] = {}
    forward: dict[Path, list[Path]] = {}
    for page in pages:
        blocks = []
        for is_content, label, text in page["blocks"]:
            if is_content:
                text = resolve_links(text, page["path"])
                text = autolink(text, page["path"], page["part"])
                if label in COPIED_LABELS:
                    blocks.append((is_content, label, text))
                    continue  # copies of other pages' text are not links from this page
                for target, words in links_in(text, page["path"]):
                    backlinks.setdefault(target, []).append((page, label, words))
                    forward.setdefault(page["path"], []).append(target)
                    # A link to an article is also a link to the chapter that teaches it.
                    article = article_by_path.get(target)
                    if article and article["box"] and page["kind"] != "article":
                        home = article["box"]["chapter"]
                        if page["path"] != home:
                            backlinks.setdefault(home, []).append((page, label, words))
            blocks.append((is_content, label, text))
        page["blocks"] = blocks

    # What links here, on every chapter and on the formula lookup.
    for page in pages:
        if page["kind"] not in {"chapter", "reference"}:
            continue
        section = what_links_here(page, backlinks.get(page["path"], []), questions)
        at = next((i for i, (_, label, _) in enumerate(page["blocks"]) if label == "see-also"), len(page["blocks"]))
        page["blocks"].insert(at, (False, "what-links-here", section))

    # Infobox, Used in and See also, on every article.
    for page in pages:
        if page["kind"] == "article":
            article = article_by_path[page["path"]]
            links = backlinks.get(page["path"], [])
            box = resolve_links(article_infobox(article, links, by_topic), page["path"])
            page["blocks"].insert(1, (False, "infobox", box))
            page["blocks"] += article_tail(article, links, forward.get(page["path"], []), questions, by_topic)

    for page in pages:
        meta_lines = "".join(f"{k}: {v}\n" for k, v in page["meta"].items())
        body = "".join(text for _, _, text in page["blocks"]).strip()
        page["path"].parent.mkdir(parents=True, exist_ok=True)
        page["path"].write_text(f"---\ntitle: {yaml_quote(page['title'])}\n{meta_lines}---\n\n{body}\n", encoding="utf-8")

    write_indexes(notes, chapters, final_notes, questions, by_source, by_topic)
    write_glossary(questions)
    write_config(chapters, final_notes, questions)


def what_links_here(page: dict, links: list[tuple[dict, str, str]], questions: list[dict]) -> str:
    path = page["path"]
    head = "\n\n## What links here {#what-links-here}\n\n"
    if not links:
        return head + "No other page links here yet.\n"
    chapters: dict[Path, dict] = {}
    asked: dict[Path, dict] = {}
    for source, label, words in links:
        if source["kind"] == "question":
            entry = asked.setdefault(source["path"], {"page": source, "in": set()})
            entry["in"].add("answer" if label == "answer" else "question")
        else:
            entry = chapters.setdefault(source["path"], {"page": source, "words": []})
            if words and words.lower() not in (w.lower() for w in entry["words"]):
                entry["words"].append(words)
    # Articles are lookup pages made from the chapters; they are listed under See also.
    chapters = {p: e for p, e in chapters.items() if e["page"]["kind"] != "article"}
    if not chapters and not asked:
        return head + "No other page links here yet.\n"
    out = [head]
    if chapters:
        out.append(f"**Pages** ({len(chapters)})\n\n")
        order = {p: i for i, p in enumerate(PAGE_ORDER)}
        for target in sorted(chapters, key=lambda p: order.get(p, 999)):
            entry = chapters[target]
            words = entry["words"][:4]
            via = (" — via " + ", ".join(f"*{w}*" for w in words)) if words else ""
            out.append(f"- [{entry['page']['title']}]({href(path, target)}){via}\n")
        out.append("\n")
    if asked:
        by_q = {q["path"]: q for q in questions}
        groups: dict[str, list[str]] = {}
        for target in asked:
            q = by_q.get(target)
            if not q:
                continue
            where = asked[target]["in"]
            note = "" if where == {"question"} else " (answer)" if where == {"answer"} else ""
            label = short_label(q) if q["group"] != "book" else q["title"]
            title = q["title"].replace('"', "'")
            groups.setdefault(q["group"], []).append((q.get("n", 0), f'[{cell(label)}]({href(path, target)} "{cell(title)}"){note}'))
        total = sum(len(v) for v in groups.values())
        out.append(f"**Questions and answers** ({total})\n\n")
        items = []
        for group in SOURCE_ORDER:
            if group in groups:
                items.extend(text for _, text in sorted(groups[group], key=lambda t: t[0]))
        if items:
            out.append("- " + " · ".join(items) + "\n")
    return "".join(out)


def article_blocks(article: dict) -> list[tuple[bool, str, str]]:
    """Hatnote, lead and statement of an article. Used in and See also come later."""
    path, box, card = article["path"], article["box"], article["card"]
    hat = []
    if box:
        hat.append(
            f"{box['kind'].capitalize()} taught in "
            f"[*{box['chapter_title']}*]({href(path, box['chapter'])}#{box['anchor']}), part of {box['part']}"
        )
    if card:
        where = f"[distribution sheet]({href(path, DIST_SHEET)}#{card['anchor']})"
        hat.append(("Also on the " if box else "From the ") + where)
    blocks = [(False, "hatnote", "::: {.hatnote}\n" + " · ".join(hat) + "\n:::\n\n")]

    if box:
        # The lead is the stored snippet when that is the box's whole first
        # paragraph; the rest of the box follows under its heading. When the
        # snippet stops short (before an equation, say), the whole box is the lead.
        lines = box["lines"]
        start = next((i for i, l in enumerate(lines) if l.strip()), len(lines))
        end = start
        while end < len(lines) and lines[end].strip() and not lines[end].lstrip().startswith(("$$", ":::", "#", "|", "!")):
            end += 1
        first = " ".join(l.strip() for l in lines[start:end])
        snippet = box["snippet"]
        if snippet and " ".join(snippet.split()) == " ".join(first.split()):
            blocks.append((True, "lead", copy_for_article(snippet, box["chapter"], path) + "\n\n"))
            rest = copy_for_article("\n".join(lines[end:]), box["chapter"], path)
            if rest.strip():
                blocks.append((False, "statement-head", f"## {KIND_HEADINGS[box['kind']]} {{#statement}}\n\n"))
                blocks.append((True, "statement", rest + "\n\n"))
        else:
            blocks.append((True, "lead", copy_for_article("\n".join(lines), box["chapter"], path) + "\n\n"))
    else:
        blocks.append(
            (
                False,
                "lead",
                f"The {card['name'].lower()} distribution: "
                "parameters, support, probability function, mean and variance.\n\n",
            )
        )
    # The distribution card itself goes in the infobox.
    return blocks


def article_tail(article, links, forward, questions, by_topic) -> list[tuple[bool, str, str]]:
    path, box = article["path"], article["box"]
    home = article_home(article)
    by_q = {q["path"]: q for q in questions}
    lines = ["\n\n## Used in {#used-in}\n\n"]
    if box:
        lines.append(f"- **Taught in** [{box['chapter_title']}]({href(path, box['chapter'])}#{box['anchor']}), where the derivation and examples are.\n")
    else:
        lines.append(f"- **Listed on** the [distribution sheet]({href(path, DIST_SHEET)}#{article['card']['anchor']}).\n")

    pages_seen: dict[Path, str] = {}
    asked: dict[Path, set] = {}
    for source, label, _ in links:
        if source["kind"] == "question":
            asked.setdefault(source["path"], set()).add(label)
        elif source["kind"] != "article" and source["path"] != home:
            pages_seen[source["path"]] = source["title"]
    if pages_seen:
        order = {p: i for i, p in enumerate(PAGE_ORDER)}
        items = [f"[{title}]({href(path, p)})" for p, title in sorted(pages_seen.items(), key=lambda kv: order.get(kv[0], 999))]
        lines.append("- **Also used in** " + " · ".join(items) + "\n")
    if asked:
        groups: dict[str, list] = {}
        for qpath, where in asked.items():
            q = by_q.get(qpath)
            if not q:
                continue
            label = short_label(q) if q["group"] != "book" else q["title"]
            note = " (answer)" if where == {"answer"} else ""
            title = q["title"].replace('"', "'")
            groups.setdefault(q["group"], []).append((q.get("n", 0), f'[{cell(label)}]({href(path, qpath)} "{cell(title)}"){note}'))
        items = []
        for group in SOURCE_ORDER:
            if group in groups:
                items.extend(t for _, t in sorted(groups[group], key=lambda t: t[0]))
        lines.append(f"- **Questions that use it** ({len(items)}) — " + " · ".join(items) + "\n")
    if box:
        n = len(by_topic.get(box["chapter"].name, []))
        if n:
            lines.append(f"- [All {n} questions on *{box['chapter_title']}*]({href(path, box['chapter'])}#questions-on-this-topic)\n")

    # Neighbours: articles this one links to, articles that link here, then the chapter's other articles.
    article_paths = {a["path"]: a for a in ARTICLES.values()}
    near: list[dict] = []
    for p in forward:
        if p in article_paths and p != path:
            near.append(article_paths[p])
    for source, _, _ in links:
        if source["kind"] == "article" and source["path"] != path:
            near.append(article_paths[source["path"]])
    for other in ARTICLES.values():
        if other["path"] != path and article_home(other) == home:
            near.append(other)
    unique = list(dict.fromkeys(a["slug"] for a in near))[:8]
    see = ["\n\n## See also {#see-also}\n\n"]
    if unique:
        see.append(" · ".join(f"[{ARTICLES[s]['term']}]({href(path, ARTICLES[s]['path'])})" for s in unique) + "\n\n")
    see.append(f"[Glossary and index]({href(path, WIKI / 'reference' / 'glossary.qmd')})\n")
    return [(False, "used-in", "".join(lines)), (False, "see-also", "".join(see))]


# ---------------------------------------------------------------------------
# Infoboxes, properties, examples and figures
#
# The hand-chosen lists live in article_extras.py. Everything shown is copied
# from the book, the booklets or the formula lookup; nothing is written anew.
# ---------------------------------------------------------------------------

from article_extras import BOOK_EXAMPLES, CHAPTER_FIGURES, EXAMPLES, FIGURES, PROPERTIES  # noqa: E402

KERNEL_ROWS: dict[str, str] = {}  # distribution slug -> "Main summaries" cell of the kernel table
CONJ_ROWS: list[dict] = []  # likelihood, prior, posterior cells, with the distributions they name
OPERATOR_SLUGS = {
    "Bin": "binomial-distribution",
    "Beta": "beta-distribution",
    "Multinomial": "multinomial-distribution",
    "Dirichlet": "dirichlet-distribution",
    "N": "normal-distribution",
    "InvGamma": "inverse-gamma-distribution",
    "Gamma": "gamma-distribution",
    "Poisson": "poisson-distribution",
}
# Shape-rate letters: the kernel table writes Beta(a,b); the distribution sheet writes Beta(alpha,beta).
GREEK_PARAMS = {"beta-distribution", "gamma-distribution", "inverse-gamma-distribution"}


def first_operator(cell_text: str) -> str | None:
    match = re.search(r"\\operatorname\{(\w+)\}", cell_text)
    return OPERATOR_SLUGS.get(match.group(1)) if match else None


def table_rows(text: str, header: str) -> list[list[str]]:
    """Cells of the pipe table whose header row starts with `header`."""
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if l.startswith(header)), None)
    if start is None:
        return []
    rows = []
    for line in lines[start + 2 :]:
        if not line.startswith("|"):
            break
        rows.append([c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]])
    return rows


def read_formula_tables(notes: dict) -> None:
    """The kernel table and the conjugate update map from the formula lookup."""
    note = next(n for n in notes.values() if n["kind"] == "reference")
    text = prepare(strip_first_heading(note["prose"]), "../figures")
    for name, _density, summaries in table_rows(text, "| Distribution | Density or mass function"):
        slug_ = first_operator(name)
        if slug_:
            KERNEL_ROWS[slug_] = summaries
    for likelihood, prior, posterior in table_rows(text, "| Likelihood | Prior | Posterior"):
        lik, pri = first_operator(likelihood), first_operator(prior)
        if lik and pri and "_n" not in likelihood:  # the regression row is not a single distribution
            CONJ_ROWS.append({"likelihood": likelihood, "prior": prior, "posterior": posterior, "lik": lik, "pri": pri})
    if not KERNEL_ROWS or not CONJ_ROWS:
        raise SystemExit("Could not read the kernel table or the conjugate map from the formula lookup")


def to_greek(tex: str) -> str:
    tex = re.sub(r"(?<![\\A-Za-z])a(?![A-Za-z])", r"\\alpha", tex)
    return re.sub(r"(?<![\\A-Za-z])b(?![A-Za-z])", r"\\beta", tex)


def short_caption(caption: str) -> str:
    """The first sentence of a figure caption, for an infobox."""
    out = ""
    for match in re.finditer(r"[.](\s|$)", caption):
        if caption[: match.start()].count("$") % 2 == 0:
            out = caption[: match.end()].strip()
            break
    return out or caption


def figure_md(file: str, page: Path, short: bool = False, credit: bool = True) -> str:
    info = FIGURE_INFO[file]
    caption = short_caption(info["caption"]) if short else info["caption"]
    where = href(page, info["chapter"]) + (f"#{info['id']}" if info["id"] else "")
    source = f" *From [{info['chapter_title']}]({where}).*" if credit else ""
    caption = rebase_links(caption, info["chapter"], page)
    return f"![{caption}{source}]({href(page, WIKI / 'figures' / file)})"


def check_extras(qmap: dict) -> None:
    problems = []
    for table, name in ((PROPERTIES, "PROPERTIES"), (EXAMPLES, "EXAMPLES"), (FIGURES, "FIGURES")):
        for slug_ in table:
            if slug_ not in ARTICLES:
                problems.append(f"{name}: no article {slug_}")
    for slug_, results in PROPERTIES.items():
        problems += [f"PROPERTIES[{slug_}]: no article {r}" for r in results if r not in ARTICLES]
    for slug_, ids in EXAMPLES.items():
        for qid in ids:
            if qid not in qmap:
                problems.append(f"EXAMPLES[{slug_}]: no question {qid}")
            elif not qmap[qid].get("answer"):
                problems.append(f"EXAMPLES[{slug_}]: {qid} has no worked answer")
    for exm, slugs in BOOK_EXAMPLES.items():
        if exm not in BOOK_EXAMPLE_BOXES:
            problems.append(f"BOOK_EXAMPLES: no example box {exm}")
        problems += [f"BOOK_EXAMPLES[{exm}]: no article {s}" for s in slugs if s not in ARTICLES]
    for slug_, files in FIGURES.items():
        problems += [f"FIGURES[{slug_}]: no chapter figure {f}" for f in files if f not in FIGURE_INFO]
    for chapter, file in CHAPTER_FIGURES.items():
        if file not in FIGURE_INFO:
            problems.append(f"CHAPTER_FIGURES[{chapter}]: no chapter figure {file}")
    if problems:
        raise SystemExit("article_extras.py:\n  " + "\n  ".join(problems))


def article_sections(article: dict, qmap: dict) -> list[tuple[bool, str, str]]:
    """Properties, Examples and Figures, below an article's lead."""
    path, slug_ = article["path"], article["slug"]
    blocks: list[tuple[bool, str, str]] = []

    results = PROPERTIES.get(slug_, [])
    if results:
        blocks.append((False, "properties-head", "\n\n## Properties {#properties}\n\n"))
        for r in results:
            other = ARTICLES[r]
            box = other["box"]
            blocks.append(
                (
                    False,
                    "property-head",
                    f"### {other['term']} {{#property-{r}}}\n\n"
                    f"::: {{.mainarticle}}\nMain article: [{other['term']}]({href(path, other['path'])})\n:::\n\n",
                )
            )
            blocks.append((True, "property", copy_for_article("\n".join(box["lines"]), box["chapter"], path) + "\n\n"))

    worked = [e for e, slugs in BOOK_EXAMPLES.items() if slug_ in slugs]
    asked = EXAMPLES.get(slug_, [])
    if worked or asked:
        blocks.append((False, "examples-head", "\n\n## Examples {#examples}\n\n"))
    for exm in worked:
        box = BOOK_EXAMPLE_BOXES[exm]
        blocks.append(
            (
                False,
                "example-head",
                f"### {box['title']} {{#example-{exm}}}\n\n"
                f"::: {{.mainarticle}}\nWorked example from [{box['chapter_title']}]({href(path, box['chapter'])}#{exm})\n:::\n\n",
            )
        )
        blocks.append((True, "example", demote_headings(copy_for_article("\n".join(box["lines"]), box["chapter"], path)) + "\n\n"))
    for qid in asked:
        q = qmap[qid]
        blocks.append(
            (
                False,
                "example-head",
                f"### {q['title']} {{#example-{qid}}}\n\n"
                f"::: {{.mainarticle}}\nQuestion page: [{q['title']}]({href(path, q['path'])})\n:::\n\n",
            )
        )
        blocks.append((True, "example", demote_headings(copy_for_article(q["prepared_body"], q["path"], path)) + "\n\n"))
        blocks.append((False, "example-answer-open", ":::::::: {.callout-tip collapse=\"true\"}\n## Worked answer (click to show)\n\n"))
        blocks.append((True, "example", demote_headings(copy_for_article(q["prepared_answer"], q["path"], path)) + "\n"))
        blocks.append((False, "example-answer-close", "\n::::::::\n\n"))

    extra = FIGURES.get(slug_, [])[1:]  # the first figure is in the infobox
    if extra:
        blocks.append((False, "figures-head", "\n\n## Figures {#figures}\n\n"))
        for file in extra:
            blocks.append((False, "figure", figure_md(file, path) + "\n\n"))
    return blocks


def infobox_md(title: str, rows: list[tuple[str, str]], image: str = "", note: str = "") -> str:
    lines = [":::: {.infobox}", "::: {.infobox-title}", title, ":::", ""]
    if image:
        lines += [image, ""]
    lines += ["| | |", "|:--|:--|"]
    lines += [f"| {label} | {value} |" for label, value in rows if value]
    if note:
        lines += ["", f"::: {{.infobox-note}}\n{note}\n:::"]
    lines += ["::::", "", ""]
    return "\n".join(lines)


def article_infobox(article: dict, links: list, by_topic: dict) -> str:
    path, slug_, box, card = article["path"], article["slug"], article["box"], article["card"]
    rows: list[tuple[str, str]] = []
    note = ""
    if card:
        labels = {
            "Distribution": "Notation",
            "Parameters": "Parameters",
            "Support": "Support",
            "Probability mass function": "Mass function",
            "Probability density": "Density",
            "Expectation": "Mean",
            "Variance": "Variance",
        }
        cells = {}
        for line in card["body"].split("\n"):
            parts = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]] if line.startswith("|") else []
            if len(parts) == 2 and parts[0] in labels:
                cells[labels[parts[0]]] = parts[1]
        for label in ("Notation", "Parameters", "Support", "Mass function", "Density", "Mean"):
            if label in cells:
                rows.append((label, cells[label]))
        mode = re.search(r"mode (\$[^$]+\$)", KERNEL_ROWS.get(slug_, ""))
        if mode:
            rows.append(("Mode", to_greek(mode.group(1)) if slug_ in GREEK_PARAMS else mode.group(1)))
        if "Variance" in cells:
            rows.append(("Variance", cells["Variance"]))
        for row in CONJ_ROWS:
            if row["pri"] == slug_ and row["lik"] == slug_:
                # Normal mean with a normal prior: one row, not a link to this page.
                rows.append(("Conjugate prior for", f"{row['likelihood']} with prior {row['prior']}, giving {row['posterior']}"))
                continue
            if row["pri"] == slug_:
                posterior = to_greek(row["posterior"]) if slug_ in GREEK_PARAMS else row["posterior"]
                rows.append(("Conjugate prior for", f"{row['likelihood']}, giving {posterior}"))
            if row["lik"] == slug_ and row["pri"] in ARTICLES:
                prior = ARTICLES[row["pri"]]
                rows.append(("Conjugate prior", f"[{prior['term']}]({href(path, prior['path'])}): {row['prior']}, giving {row['posterior']}"))
        # Sentences on the card outside its table, such as a warning, keep their place.
        remarks = " ".join(l.strip() for l in card["body"].split("\n") if l.strip() and not l.startswith("|"))
        sources = f"From the [distribution sheet]({href(path, DIST_SHEET)}#{card['anchor']})"
        if mode or any(r["pri"] == slug_ or r["lik"] == slug_ for r in CONJ_ROWS):
            sources += f"; mode and conjugate pairs from the [formula lookup]({href(path, WIKI / 'reference' / 'formulas.qmd')})"
        note = (remarks + "\n\n" if remarks else "") + sources + "."
    else:
        rows.append(("Type", box["kind"].capitalize()))
    if box:
        rows.append(("Taught in", f"[{box['chapter_title']}]({href(path, box['chapter'])}#{box['anchor']})"))
        rows.append(("Part", box["part"]))
    else:
        rows.append(("Listed on", f"[Distribution sheet]({href(path, DIST_SHEET)}#{card['anchor']})"))
    n_props = len(PROPERTIES.get(slug_, []))
    n_examples = len(EXAMPLES.get(slug_, [])) + sum(1 for s in BOOK_EXAMPLES.values() if slug_ in s)
    n_questions = len({source["path"] for source, _, _ in links if source["kind"] == "question"})
    if n_props:
        rows.append(("Properties", f"[{n_props}](#properties)"))
    if n_examples:
        rows.append(("Worked examples", f"[{n_examples}](#examples)"))
    if n_questions:
        rows.append(("Questions using it", f"[{n_questions}](#used-in)"))
    figures = FIGURES.get(slug_, [])
    image = figure_md(figures[0], path, short=True) if figures else ""
    return infobox_md(article["term"], rows, image, note)


def chapter_infobox(note: dict, part: str, siblings: list[dict], own: list[dict], own_articles: list[dict]) -> str:
    path = note["path"]
    i = next(k for k, n in enumerate(siblings) if n["path"] == path)
    rows = [("Part", part), ("Chapter", f"{i + 1} of {len(siblings)} in this part")]
    if i > 0:
        rows.append(("Previous", f"[{siblings[i - 1]['title']}]({href(path, siblings[i - 1]['path'])})"))
    if i + 1 < len(siblings):
        rows.append(("Next", f"[{siblings[i + 1]['title']}]({href(path, siblings[i + 1]['path'])})"))
    if own:
        rows.append(("Questions", f"[{len(own)}](#questions-on-this-topic)"))
    defs = [a for a in own_articles if a["box"]["kind"] == "definition"]
    results = [a for a in own_articles if a["box"]["kind"] in {"theorem", "proposition", "corollary"}]
    if defs:
        rows.append(("Definitions", " · ".join(f"[{a['term']}]({href(path, a['path'])})" for a in defs)))
    if results:
        rows.append(("Results", " · ".join(f"[{a['term']}]({href(path, a['path'])})" for a in results)))
    seen = CHAPTER_FIGURES_SEEN.get(path, [])
    if seen:
        rows.append(("Figures", str(len(dict.fromkeys(seen)))))
    lead = CHAPTER_FIGURES.get(path.name) or (seen[0] if seen else "")
    image = figure_md(lead, path, short=True, credit=False) if lead else ""
    return infobox_md(note["title"], rows, image)


def write_glossary(questions: list[dict]) -> None:
    page = WIKI / "reference" / "glossary.qmd"
    # Named objects are articles: one row each, pointing at the article.
    entries = []
    for article in ARTICLES.values():
        box, card = article["box"], article["card"]
        kinds = ([box["kind"]] if box else []) + (["distribution"] if card else [])
        entries.append(
            {
                "term": article["term"],
                "kind": " · ".join(kinds),
                "page": article["path"],
                "anchor": "",
                "where": box["chapter_title"] if box else "Common distributions",
                "snippet": box["snippet"] if box else "",
                "home": article_home(article),
            }
        )
    named = {(e["term"].lower(), e["home"]) for e in entries}
    # Sections stay links into their chapter, unless a box of the same name has an article.
    for e in GLOSSARY:
        if e["kind"] == "section" and (e["term"].lower(), e["page"]) not in named:
            entries.append(dict(e))
    # Concept checks are short questions on one idea each.
    for q in questions:
        if q["group"] == "concepts":
            entries.append(
                {
                    "term": re.sub(r"^C\d+\.\s*", "", q["title"]),
                    "kind": "question",
                    "page": q["path"],
                    "anchor": "",
                    "where": q["topic_note"]["title"] if q.get("topic_note") else "Question bank",
                    "snippet": "",
                }
            )
    # Aliases are redirects: the row's own link goes straight to the real entry.
    by_term = {e["term"].lower(): e for e in entries}
    for alias, target in SEE_ALSO.items():
        found = by_term.get(target.lower())
        if not found:
            raise SystemExit(f"Redirect {alias!r} points at {target!r}, which has no entry")
        link = href(page, found["page"]) + (f"#{found['anchor']}" if found["anchor"] else "")
        entries.append(
            {
                **found,
                "term": alias,
                "kind": "redirect",
                "snippet": f"Redirects to [{found['term']}]({link}).",
                "keep_links": True,
            }
        )

    def clean_snippet(text: str) -> str:
        text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)(\{[^}]*\})?", r"\1", text)
        text = re.sub(r"\[\^[^\]]+\]", "", text)
        def eq_number(ident: str | None) -> str:
            n = EQ_NUMBERS.get(ident or "")
            return f"equation ({n})" if n else "a displayed equation"

        text = re.sub(r"\\eqref\{([^{}]+)\}", lambda m: eq_number(EQ_LABELS.get(m.group(1), (None,))[0]), text)
        text = re.sub(r"@(eq-[\w-]+)", lambda m: eq_number(m.group(1)), text)
        return cell(" ".join(text.split()))

    def sort_key(entry: dict) -> str:
        term = re.sub(r"^(the|a|an)\s+", "", entry["term"].lower())
        return re.sub(r"[^a-z0-9 ]", "", term)

    seen, rows_by_letter = set(), {}
    for entry in sorted(entries, key=sort_key):
        key = (entry["term"].lower(), entry["page"], entry["anchor"])
        if key in seen:
            continue
        seen.add(key)
        first = (sort_key(entry) or "#")[0]
        letter = first.upper() if first.isalpha() else "#"
        target = href(page, entry["page"]) + (f"#{entry['anchor']}" if entry["anchor"] else "")
        term = f"[{cell(entry['term'])}]({target})"
        kind = f"[{entry['kind']}]{{.gtype}}"
        meaning = cell(" ".join(entry["snippet"].split())) if entry.get("keep_links") else clean_snippet(entry["snippet"])
        rows_by_letter.setdefault(letter, []).append(f"| {term} {kind} | {meaning} | {cell(entry['where'])} |")

    letters = sorted(rows_by_letter, key=lambda l: (l == "#", l))
    jump = " · ".join(f"[{l}](#letter-{l.lower() if l != '#' else 'other'})" for l in letters)
    n_articles = len(ARTICLES)
    lines = [
        f"Every named idea, A to Z: {len(seen)} entries. "
        f"The {n_articles} definitions, theorems, remarks and distributions each have an article of their own; "
        "sections link into their chapter, questions link to their page, and redirects to the entry they stand for. "
        "Hover over a link to preview it.",
        "",
        filter_box("Filter the glossary, e.g. prior, deviance, stationary"),
        "",
        "::: {.glossary-jump}",
        jump,
        ":::",
        "",
    ]
    for letter in letters:
        ident = letter.lower() if letter != "#" else "other"
        lines += [
            f"## {letter} {{#letter-{ident}}}",
            "",
            "::: {.qtable .glossary}",
            "| Term | Meaning | Where |",
            "|:--|:--|:--|",
            *rows_by_letter[letter],
            ":::",
            "",
        ]
    page.write_text("---\ntitle: \"Glossary and index\"\ntoc: false\n---\n\n" + "\n".join(lines) + "\n", encoding="utf-8")


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def write_indexes(notes, chapters, final_notes, questions, by_source, by_topic) -> None:
    parts: dict[str, list[dict]] = {}
    for part, note in chapters:
        parts.setdefault(part, []).append(note)
    counts = {name: len(qs) for name, qs in by_topic.items()}
    n_answers = sum(1 for q in questions if q.get("answer"))

    # Topics: a contents page for the whole book.
    topics_path = WIKI / "notes" / "index.qmd"
    lines = [
        "Every chapter is an article. Each one ends with a table of the questions on its topic.",
        "",
    ]
    for part, members in parts.items():
        lines += [f"## {part} {{#{slug(part)}}}", "", "| Chapter | Questions |", "|:--|--:|"]
        for note in members:
            n = counts.get(note["path"].name, 0)
            lines.append(f"| [{cell(note['title'])}]({href(topics_path, note['path'])}) | {n or '–'} |")
        lines.append("")
    lines += ["## Final preparation {#final-preparation}", ""]
    for note in final_notes:
        lines.append(f"- [{note['title']}]({href(topics_path, note['path'])})")
    lines += ["", "## How the topics fit together", "", strip_first_heading(notes["index.qmd"]["prose"]).split("\n## On this site")[0].strip()]
    body = prepare("\n".join(lines), "../figures")
    topics_path.write_text(f"---\ntitle: \"Topics\"\n---\n\n{body}\n", encoding="utf-8")

    # Question bank, by topic.
    q_index = WIKI / "questions" / "index.qmd"
    lines = [
        f"All {len(questions)} questions, grouped by topic. {n_answers} have a worked answer, folded away at the bottom of the question page. "
        f"Or try a [random question](#random).",
        "",
        filter_box("Filter questions, e.g. gibbs, poisson, deviance"),
        "",
    ]
    for part, members in parts.items():
        lines += [f"## {part} {{#{slug(part)}}}", ""]
        for note in members:
            qs = by_topic.get(note["path"].name, [])
            if not qs:
                continue
            lines += [f"### [{note['title']}]({href(q_index, note['path'])})", "", question_table(qs, q_index), ""]
    body = "\n".join(lines)
    q_index.write_text(f"---\ntitle: \"Question bank\"\ntoc-depth: 3\n---\n\n{body}\n", encoding="utf-8")

    # Reference landing page and the distribution sheet.
    write_qmd(
        WIKI / "reference" / "index.qmd",
        "Reference",
        """Three lookup pages sit beside the chapters.

- [Glossary and index](glossary.qmd), every defined term, theorem and section from A to Z.
- [Common distributions](distributions.qmd), with the parameterisation used on these pages.
- [Formula lookup](formulas.qmd), the kernel table and the problem-solving workflow.
""",
    )
    def card_link(match: re.Match) -> str:
        article = ARTICLES.get(slug(f"{match.group(2)} distribution"))
        if not article:
            return match.group(0)
        up = f"[Article: {article['term']} →]({href(DIST_SHEET, article['path'])}){{.box-article}}"
        return f"{match.group(1)}\n\n{up}\n:::"

    sheet = re.sub(r"(::: \{\.dist-card\}\n### (.+?)\n.*?)\n:::", card_link, distributions_body(), flags=re.S)
    sheet = re.sub(r"^### (.+)$", lambda m: f"### {m.group(1)} {{#{dist_anchor(m.group(1))}}}", sheet, flags=re.M)
    write_qmd(WIKI / "reference" / "distributions.qmd", "Common distributions", prepare(sheet, "../figures"))

    # Main page, in the manner of a portal.
    home = WIKI / "index.qmd"
    boxes = []
    for part, members in parts.items():
        total = sum(counts.get(n["path"].name, 0) for n in members)
        items = "\n".join(f"- [{n['title']}]({href(home, n['path'])})" for n in members)
        boxes.append(f"::: {{.portal-box}}\n### {part}\n\n{items}\n\n[{total} questions →]({href(home, q_index)}#{slug(part)}){{.portal-more}}\n:::\n")
    final_items = "\n".join(f"- [{n['title']}]({href(home, n['path'])})" for n in final_notes)
    boxes.append(
        "::: {.portal-box}\n### Final preparation\n\n" + final_items
        + f"\n\n[{len(by_source['final'])} questions →]({href(home, WIKI / 'notes' / 'final-preparation.qmd')}){{.portal-more}}\n:::\n"
    )
    boxes.append(
        "::: {.portal-box}\n### Question bank\n\n"
        f"- [By topic]({href(home, q_index)})\n- [Random question](#random)\n:::\n"
    )
    boxes.append(
        "::: {.portal-box}\n### Reference\n\n"
        f"- [Common distributions]({href(home, WIKI / 'reference' / 'distributions.qmd')})\n"
        f"- [Formula lookup]({href(home, WIKI / 'reference' / 'formulas.qmd')})\n:::\n"
    )
    n_chapters = len(chapters)
    home.write_text(
        f"""---
title: "STAT3500 wiki"
toc: false
---

::: {{.portal-intro}}
A study wiki for STAT3500/7500: **{n_chapters} chapters** and **{len(questions)} questions**, {n_answers} of them with worked answers. Every chapter lists the questions on its topic, and every question links back to its chapter. Use the search box at the top to find any term, or open a [random question](#random) to test yourself.
:::

:::: {{.portal}}
{chr(10).join(boxes)}
::::

## How to study with it

1. Read a chapter. The contents on the right jump between its sections.
2. Scroll to **Questions on this topic** at the end and open one.
3. Attempt it, then open **Worked answer** at the bottom of the question page.
4. Use **‹ previous** and **next ›** at the top of a question to move through the questions on the same topic.

The source is on [GitHub]({REPO_URL}). Every change pushed there rebuilds this site.
""",
        encoding="utf-8",
    )


def write_config(chapters, final_notes, questions) -> None:
    question_paths = [q["path"].relative_to(WIKI).with_suffix(".html").as_posix() for q in questions]
    (WIKI / "_random.html").write_text(
        RANDOM_AND_FILTER_JS.replace("__QUESTIONS__", "[" + ",".join(f'"{p}"' for p in question_paths) + "]")
        + PREVIEW_JS,
        encoding="utf-8",
    )

    part_blocks = []
    parts: dict[str, list[dict]] = {}
    for part, note in chapters:
        parts.setdefault(part, []).append(note)
    for part, members in parts.items():
        entries = "\n".join(f"              - {n['path'].relative_to(WIKI).as_posix()}" for n in members)
        part_blocks.append(f"          - section: {yaml_quote(part)}\n            contents:\n{entries}")
    finals = "\n".join(f"              - {n['path'].relative_to(WIKI).as_posix()}" for n in final_notes)
    part_blocks.append(f"          - section: \"Final preparation\"\n            contents:\n{finals}")

    yml = f"""project:
  type: website
  output-dir: _site
  # Render the generated pages only, not the course files copied into sources/.
  render:
    - "*.qmd"
    - "!sources/"
  resources:
    - katex/

website:
  title: "STAT3500 wiki"
  description: "Study wiki for STAT3500/7500"
  search:
    location: navbar
    type: textbox
  navbar:
    left:
      - text: Main page
        href: index.qmd
      - text: Topics
        href: notes/index.qmd
      - text: Question bank
        href: questions/index.qmd
      - text: Glossary
        href: reference/glossary.qmd
      - text: Reference
        href: reference/index.qmd
      - text: Random question
        href: index.qmd#random
  sidebar:
    style: docked
    collapse-level: 2
    contents:
      - text: Main page
        href: index.qmd
      - text: Random question
        href: index.qmd#random
      - section: Topics
        href: notes/index.qmd
        contents:
{chr(10).join(part_blocks)}
      - section: Question bank
        href: questions/index.qmd
        contents:
          - text: By topic
            href: questions/index.qmd
      - section: Reference
        href: reference/index.qmd
        contents:
          - reference/glossary.qmd
          - reference/distributions.qmd
          - reference/formulas.qmd
  page-navigation: true
  page-footer:
    center: "STAT3500 study wiki. [Source on GitHub]({REPO_URL})"

format:
  html:
    # Two themes give a light/dark switch in the top bar; the choice is remembered.
    theme:
      light: cosmo
      dark: darkly
    css: styles.css
    toc: true
    toc-depth: 2
    toc-location: right
    toc-title: Contents
    # KaTeX is bundled in the katex folder, so equations work offline.
    html-math-method:
      method: katex
      url: /katex/
    smooth-scroll: true
    code-overflow: wrap
    link-external-newwindow: true
    include-after-body: _random.html
    # The site is published on GitHub Pages; ask search engines not to list it.
    include-in-header:
      text: '<meta name="robots" content="noindex, nofollow">'
"""
    (WIKI / "_quarto.yml").write_text(yml, encoding="utf-8")


def distributions_body() -> str:
    return r"""
The distributions below use the parameterisation fixed in each card. The second gamma parameter is a rate, and the second inverse-gamma parameter is the rate in $\exp(-\beta/x)$. The longer kernel table, with the problem-solving workflow, is on the [formula lookup](formulas.qmd) page.

## Discrete

::: {.dist-card}
### Binomial

| | |
|---|---|
| Distribution | $x\sim\operatorname{Bin}(n,p)$ |
| Parameters | $n\in\mathbb{Z}^{+}$, $p\in[0,1]$ |
| Support | $x=0,1,\ldots,n$ |
| Probability mass function | $p(x)=\binom{n}{x}p^{x}(1-p)^{n-x}$ |
| Expectation | $\mathbb{E}(x)=np$ |
| Variance | $\operatorname{Var}(x)=np(1-p)$ |
:::

::: {.dist-card}
### Geometric

| | |
|---|---|
| Distribution | $x\sim\operatorname{Geom}(p)$ |
| Parameters | $p\in(0,1]$ |
| Support | $x=1,2,3,\ldots$ |
| Probability mass function | $p(x)=p(1-p)^{x-1}$ |
| Expectation | $\mathbb{E}(x)=1/p$ |
| Variance | $\operatorname{Var}(x)=(1-p)/p^{2}$ |
:::

::: {.dist-card}
### Multinomial

| | |
|---|---|
| Distribution | $x\sim\operatorname{Mult}(n,p)$ |
| Parameters | $n\in\mathbb{Z}^{+}$, $p\in[0,1]^{K}$ with $\sum_{k=1}^{K}p_k=1$ |
| Support | $x_k\in\{0,1,\ldots,n\}$, $\sum_k x_k=n$ |
| Probability mass function | $p(x)=\frac{n!}{x_1!\cdots x_K!}p_1^{x_1}\cdots p_K^{x_K}$ |
| Expectation | $\mathbb{E}(x)=np$ |
| Variance | $\operatorname{Var}(x_k)=np_k(1-p_k)$ |
:::

::: {.dist-card}
### Poisson

| | |
|---|---|
| Distribution | $x\sim\operatorname{Poisson}(\theta)$ |
| Parameters | $\theta>0$ |
| Support | $x=0,1,2,\ldots$ |
| Probability mass function | $p(x)=e^{-\theta}\theta^{x}/x!$ |
| Expectation | $\mathbb{E}(x)=\theta$ |
| Variance | $\operatorname{Var}(x)=\theta$ |
:::

## Continuous

::: {.dist-card}
### Beta

| | |
|---|---|
| Distribution | $x\sim\operatorname{Beta}(\alpha,\beta)$ |
| Parameters | $\alpha,\beta>0$ |
| Support | $0<x<1$ |
| Probability density | $p(x)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}x^{\alpha-1}(1-x)^{\beta-1}$ |
| Expectation | $\mathbb{E}(x)=\alpha/(\alpha+\beta)$ |
| Variance | $\operatorname{Var}(x)=\alpha\beta/((\alpha+\beta)^{2}(\alpha+\beta+1))$ |
:::

::: {.dist-card}
### Dirichlet

| | |
|---|---|
| Distribution | $x\sim\operatorname{Dirichlet}(\alpha)$ |
| Parameters | $\alpha\in\mathbb{R}_{+}^{K}$, $\alpha_0=\sum_{k=1}^{K}\alpha_k$ |
| Support | $x_k>0$, $\sum_{k=1}^{K}x_k=1$ |
| Probability density | $p(x)=\frac{\Gamma(\alpha_0)}{\prod_{k=1}^{K}\Gamma(\alpha_k)}\prod_{k=1}^{K}x_k^{\alpha_k-1}$ |
| Expectation | $\mathbb{E}(x)=\alpha/\alpha_0$ |
| Variance | $\operatorname{Var}(x_k)=\alpha_k(\alpha_0-\alpha_k)/(\alpha_0^{2}(\alpha_0+1))$ |
:::

::: {.dist-card}
### Exponential

| | |
|---|---|
| Distribution | $x\sim\operatorname{Exp}(\lambda)$ |
| Parameters | $\lambda>0$ |
| Support | $x>0$ |
| Probability density | $p(x)=\lambda e^{-\lambda x}$ |
| Expectation | $\mathbb{E}(x)=1/\lambda$ |
| Variance | $\operatorname{Var}(x)=1/\lambda^{2}$ |
:::

::: {.dist-card}
### Gamma

| | |
|---|---|
| Distribution | $x\sim\operatorname{Gamma}(\alpha,\beta)$ |
| Parameters | $\alpha,\beta>0$, shape--rate |
| Support | $x>0$ |
| Probability density | $p(x)=\frac{\beta^{\alpha}}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x}$ |
| Expectation | $\mathbb{E}(x)=\alpha/\beta$ |
| Variance | $\operatorname{Var}(x)=\alpha/\beta^{2}$ |
:::

::: {.dist-card}
### Inverse gamma

| | |
|---|---|
| Distribution | $x\sim\operatorname{InvGamma}(\alpha,\beta)$ |
| Parameters | $\alpha,\beta>0$ |
| Support | $x>0$ |
| Probability density | $p(x)=\frac{\beta^{\alpha}}{\Gamma(\alpha)}x^{-\alpha-1}e^{-\beta/x}$ |
| Expectation | $\mathbb{E}(x)=\beta/(\alpha-1)$ for $\alpha>1$ |
| Variance | $\operatorname{Var}(x)=\beta^{2}/((\alpha-1)^{2}(\alpha-2))$ for $\alpha>2$ |

The mode is $\beta/(\alpha+1)$, which is not the variance.
:::

::: {.dist-card}
### Normal

| | |
|---|---|
| Distribution | $X\sim\operatorname{N}(\mu,\sigma^{2})$ |
| Parameters | $\mu\in\mathbb{R}$, $\sigma>0$ |
| Support | $x\in\mathbb{R}$ |
| Probability density | $p(x)=\frac{1}{\sqrt{2\pi}\,\sigma}\exp\Bigl(-\frac{(x-\mu)^{2}}{2\sigma^{2}}\Bigr)$ |
| Expectation | $\mathbb{E}(X)=\mu$ |
| Variance | $\operatorname{Var}(X)=\sigma^{2}$ |
:::
"""


def main() -> None:
    self_test()
    if not BOOK.exists():
        raise SystemExit(f"Missing book: {BOOK}")
    if not PRACTICE_TEX.exists():
        raise SystemExit(f"Missing practice source: {PRACTICE_TEX}")
    clean_output()
    convert_figures()

    notes: dict[str, dict] = {}
    questions: list[dict] = []
    answers: list[dict] = []
    book_questions_by_id: dict[str, dict] = {}

    print("Reading the course book")
    for part, files in PARTS:
        for filename, kind in files:
            raw = (BOOK / "chapters" / filename).read_text(encoding="utf-8")
            title = first_heading(raw)
            prose, exercises = extract_exercises(raw)
            if kind == "reference":
                path = WIKI / "reference" / "formulas.qmd"
            else:
                path = WIKI / "notes" / filename
            note = {
                "path": path,
                "title": title,
                "kind": kind,
                "part": part,
                "prose": prose,
                "exercises": [],
            }
            notes[filename] = note
            applied = False
            for lead, ex_id, body in exercises:
                applied = applied or "Applied" in lead
                q_title = exercise_title(body)
                q_path = WIKI / "questions" / f"{ex_id}.qmd"
                record = {
                    "group": "book",
                    "id": ex_id,
                    "title": q_title,
                    "body": without_title(body),
                    "path": q_path,
                    "lead": lead,
                    "part": part,
                    "chapter": title,
                    "chapter_file": filename,
                    "notes_path": path,
                    "answer_id": solution_link(body),
                    "applied": applied,
                    "description": f"Exercise · {title}",
                    "categories": ["Exercises", part, title],
                }
                questions.append(record)
                book_questions_by_id[ex_id] = record
                note["exercises"].append(record)

    solutions = (BOOK / "chapters" / "bayes-11-solutions.qmd").read_text(encoding="utf-8")
    matches = list(re.finditer(r"^\[\]\{#(sol-[\w-]+)\}", solutions, flags=re.M))
    for i, match in enumerate(matches):
        sol_id = match.group(1)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(solutions)
        body = solutions[match.end() : end]
        body = re.sub(r"(?m)^## Chapter [^\n]*\n", "", body)
        linked = re.search(r"\(#(ex-[\w-]+)\)", body)
        ex_id = linked.group(1) if linked else None
        body = re.sub(r"\*\*\[[^\]]*\]\(#ex-[\w-]+\)\.\*\*", "", body, count=1)
        q = book_questions_by_id.get(ex_id or "")
        title = "Answer: " + (q["title"] if q else sol_id)
        answers.append(
            {
                "group": "book",
                "id": sol_id,
                "title": title,
                "body": body.strip(),
                "path": WIKI / "answers" / "book" / f"{sol_id}.qmd",
                "question_id": ex_id,
                "question_path": q["path"] if q else None,
                "notes_path": q["notes_path"] if q else None,
                "description": "Worked answer · " + (q["chapter"] if q else "Applied exercise"),
                "categories": ["Exercise answers", q["part"] if q else "Bayesian statistics"],
            }
        )

    print("Reading the final-preparation booklet")
    guide = (PREP / "index.qmd").read_text(encoding="utf-8")
    guide = re.sub(
        r"\]\(#sec-distributions\)",
        "](../reference/distributions.qmd)",
        guide,
    )
    # Answers now sit folded inside their question pages; resolve_links
    # turns the remaining #ex- and #sol- anchors into links to those pages.
    guide = re.sub(r"\]\(#sec-ian\)", "](final-bayesian.qmd)", guide)
    guide = re.sub(r"\]\(#sec-alan\)", "](final-applied.qmd)", guide)
    guide = re.sub(r"\]\(#sec-ian-answers\)", "](final-bayesian.qmd)", guide)
    guide = re.sub(r"\]\(#sec-alan-answers\)", "](final-applied.qmd)", guide)
    notes["final-preparation.qmd"] = {
        "path": WIKI / "notes" / "final-preparation.qmd",
        "title": "How to use the final preparation",
        "kind": "notes",
        "part": "Final preparation",
        "prose": guide,
        "exercises": [],
    }

    final_sources = [
        ("final-bayesian.qmd", PREP / "chapters" / "ian.qmd", PREP / "chapters" / "ian-answers.qmd", "Bayesian final questions"),
        ("final-applied.qmd", PREP / "chapters" / "alan.qmd", PREP / "chapters" / "alan-answers.qmd", "Applied final questions"),
    ]
    for note_name, q_file, a_file, fallback_title in final_sources:
        raw = q_file.read_text(encoding="utf-8")
        lines = raw.splitlines()
        first_ex = next(i for i, line in enumerate(lines) if EX_OPEN.match(line))
        prose = "\n".join(lines[:first_ex]).rstrip() + "\n"
        # The source headings are "Ian's Half" and "Alan's Half"; say what each half covers.
        title = fallback_title
        note = {
            "path": WIKI / "notes" / note_name,
            "title": title,
            "kind": "notes",
            "part": "Final preparation",
            "prose": prose,
            "exercises": [],
        }
        notes[note_name] = note
        _, exercises = extract_exercises("## Exercises\n" + "\n".join(lines[first_ex:]))
        for lead, ex_id, body in exercises:
            q_title = exercise_title(body)
            number = re.match(r"Question\s+(\d+)", q_title)
            record = {
                "group": "final",
                "n": int(number.group(1)) if number else 99,
                "id": ex_id,
                "title": q_title,
                "body": without_title(body),
                "path": WIKI / "questions" / f"{ex_id}.qmd",
                "lead": lead,
                "part": "Final preparation",
                "chapter": title,
                "chapter_file": note_name,
                "notes_path": note["path"],
                "answer_id": solution_link(body),
                "description": "Final preparation",
                "categories": ["Final preparation", title],
            }
            questions.append(record)
            note["exercises"].append(record)
        answer_text = a_file.read_text(encoding="utf-8")
        blocks = re.split(r"(?=^## Question )", answer_text, flags=re.M)
        for block in blocks:
            heading = re.match(r"## Question .+?\{#(sol-[\w-]+)\}", block)
            if not heading:
                continue
            sol_id = heading.group(1)
            body = re.sub(r"^## Question .+?\n+", "", block, count=1).strip()
            body = re.sub(r"\[Question[^\]]*\]\(#ex-[\w-]+\)\n*", "", body).strip()
            q = next((item for item in note["exercises"] if item["answer_id"] == sol_id), None)
            answers.append(
                {
                    "group": "final",
                    "id": sol_id,
                    "title": "Answer: " + (q["title"] if q else sol_id),
                    "body": body,
                    "path": WIKI / "answers" / "final" / f"{sol_id}.qmd",
                    "question_id": q["id"] if q else None,
                    "question_path": q["path"] if q else None,
                    "notes_path": note["path"],
                    "description": "Final preparation answer",
                    "categories": ["Final preparation answers"],
                }
            )

    print("Converting the practice booklet")
    concept_qs, concept_as, exam_qs, exam_as = load_practice()
    if [q["n"] for q in concept_qs] != list(range(1, 51)):
        raise SystemExit("Concept questions are not numbered 1 through 50")
    if [a["n"] for a in concept_as] != list(range(1, 51)):
        raise SystemExit("Concept answers are not numbered 1 through 50")
    if [a["n"] for a in exam_as] != list(range(1, 60)):
        raise SystemExit(f"Practice answers are not 1 through 59: {[a['n'] for a in exam_as]}")
    if len(exam_qs) != 59:
        raise SystemExit(f"Expected 59 practice questions, found {len(exam_qs)}")

    fragments = {}
    for item in concept_qs:
        fragments[f"cq{item['n']:02d}"] = preprocess_practice_latex(item["text"])
    for item in concept_as:
        fragments[f"ca{item['n']:02d}"] = preprocess_practice_latex(
            "\\textbf{Definitions/notation.} " + item["body"]
        )
    for n, item in enumerate(exam_qs, 1):
        fragments[f"pq{n:02d}"] = preprocess_practice_latex(item["body"])
    for item in exam_as:
        fragments[f"pa{item['n']:02d}"] = preprocess_practice_latex(item["body"])
    converted = pandoc_many(fragments)

    concept_titles = {a["n"]: a["title"] for a in concept_as}
    for item in concept_qs:
        n = item["n"]
        title = f"C{n}. {concept_titles.get(n, item['topic'])}"
        questions.append(
            {
                "group": "concepts",
                "n": n,
                "id": f"c-{n:02d}",
                "title": title,
                "body": converted[f"cq{n:02d}"],
                "path": WIKI / "questions" / f"c-{n:02d}.qmd",
                "notes_path": None,
                "answer_id": f"c-{n:02d}",
                "description": "Concept check · " + item["topic"],
                "categories": ["Concept checks", item["topic"] or "Concept checks"],
                "question_path_for_answer": WIKI / "questions" / f"c-{n:02d}.qmd",
            }
        )
    for item in concept_as:
        n = item["n"]
        answers.append(
            {
                "group": "concepts",
                "id": f"c-{n:02d}",
                "title": f"Answer C{n}. {item['title']}",
                "body": converted[f"ca{n:02d}"],
                "path": WIKI / "answers" / "concepts" / f"c-{n:02d}.qmd",
                "question_path": WIKI / "questions" / f"c-{n:02d}.qmd",
                "notes_path": None,
                "description": "Concept-check answer · " + item["topic"],
                "categories": ["Concept-check answers", item["topic"] or "Concept checks"],
            }
        )
    for n, item in enumerate(exam_qs, 1):
        label = re.sub(r"^Question\s+\d+\s*:\s*", "", item["title"]).strip()
        questions.append(
            {
                "group": "practice",
                "n": n,
                "id": f"q-{n:02d}",
                "title": f"Q{n}. {label}",
                "body": converted[f"pq{n:02d}"],
                "path": WIKI / "questions" / f"q-{n:02d}.qmd",
                "notes_path": None,
                "answer_id": f"a-{n:02d}",
                "description": "Practice question",
                "categories": ["Practice questions"],
            }
        )
    for item in exam_as:
        n = item["n"]
        answers.append(
            {
                "group": "practice",
                "id": f"a-{n:02d}",
                "title": f"Answer {n}. {item['title']}",
                "body": converted[f"pa{n:02d}"],
                "path": WIKI / "answers" / "practice" / f"a-{n:02d}.qmd",
                "question_path": WIKI / "questions" / f"q-{n:02d}.qmd",
                "notes_path": None,
                "description": "Practice answer",
                "categories": ["Practice answers"],
            }
        )

    print("Writing pages")
    book_index = strip_first_heading((BOOK / "index.qmd").read_text(encoding="utf-8"))
    notes["index.qmd"] = {
        "path": WIKI / "notes" / "index.qmd",
        "title": "Topics",
        "kind": "index",
        "part": "Notes",
        "prose": book_index,
        "exercises": [],
    }

    write_pages(notes, questions, answers)

    leftover = []
    banned = re.compile(r"\\(vect|mat|BetaDist|GammaDist|InvGamma|xvec|betavec|thetavec|given|ind|eqref|label)\b")
    for path in WIKI.rglob("*.qmd"):
        if path.parts[len(WIKI.parts)] in {"_site", "_build", ".quarto", "_publish", "sources"}:
            continue
        pieces = re.split(r"(```.*?```)", path.read_text(encoding="utf-8"), flags=re.S)
        if any(banned.search(piece) for piece in pieces if not piece.startswith("```")):
            leftover.append(str(path.relative_to(WIKI)))
    if leftover:
        print("LaTeX macros still present in:")
        for name in leftover[:20]:
            print(" ", name)

    print(f"Chapter pages: {len([n for n in notes.values() if n['kind'] == 'notes'])}")
    print(f"Question pages: {len(questions)}, with answers: {sum(1 for q in questions if q.get('answer'))}")
    print("Wiki source is ready.")


if __name__ == "__main__":
    main()
