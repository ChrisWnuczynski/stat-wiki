"""Build the stat wiki from the course book, final booklet, practice set, and probability notes.

Run from this folder: python build_wiki.py
Then: quarto preview

The course files are copies in sources/. The publish workflow runs the same
two steps (build, then quarto render) on every push and publishes the result.
"""

from __future__ import annotations

import json
import os
from collections import Counter
from datetime import datetime, timezone
from html import escape as html_escape
from zoneinfo import ZoneInfo

import chapter_guides
import re
import struct
import unicodedata
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
PROBABILITY = SOURCES / "stat2003"  # probability notes (chapters and worked solutions)
INFERENCE = SOURCES / "stat2004"  # inference notes; the probability part is not copied
DATA = SOURCES / "stat1301"  # studies, description, and examples that point at inference
USING = SOURCES / "using-r"  # the Using R section; the language chapter stays in DATA
STOCHASTIC = SOURCES / "stat3004"  # stochastic processes, then measure and convergence
LEARNING = SOURCES / "stat3006"  # statistical learning, including the R calculations

PARTS = [
    (
        "Probability",
        [
            ("prob-01-experiments.qmd", "notes"),
            ("prob-02-random-variables.qmd", "notes"),
            ("prob-03-simulation.qmd", "notes"),
            ("prob-04-joint-distributions.qmd", "notes"),
            ("prob-05-transforms-and-limits.qmd", "notes"),
            ("prob-06-markov-chains.qmd", "notes"),
            ("prob-07-reliability.qmd", "notes"),
        ],
    ),
    (
        "Stochastic processes",
        [
            ("sp-01-stochastic-processes.qmd", "notes"),
            ("sp-02-branching.qmd", "notes"),
            ("sp-03-random-walks.qmd", "notes"),
            ("sp-04-discrete-markov.qmd", "notes"),
            ("sp-05-classes-and-reversibility.qmd", "notes"),
            ("sp-06-poisson-processes.qmd", "notes"),
            ("sp-07-continuous-markov.qmd", "notes"),
            ("sp-08-queues.qmd", "notes"),
            ("sp-09-probability-spaces.qmd", "notes"),
            ("sp-10-random-variables.qmd", "notes"),
            ("sp-11-convergence.qmd", "notes"),
            ("sp-12-extremes.qmd", "notes"),
        ],
    ),
    (
        "Statistical inference",
        [
            ("inf-01-statistical-inference.qmd", "notes"),
            ("inf-02-estimation.qmd", "notes"),
            ("inf-08-information-and-bounds.qmd", "notes"),
            ("inf-09-rao-blackwell.qmd", "notes"),
            ("inf-10-large-sample-estimation.qmd", "notes"),
            ("inf-03-confidence-intervals.qmd", "notes"),
            ("inf-04-hypothesis-tests.qmd", "notes"),
            ("inf-11-most-powerful-tests.qmd", "notes"),
            ("inf-12-generalised-likelihood-ratio.qmd", "notes"),
            ("inf-05-chi-square.qmd", "notes"),
            ("inf-13-exact-tests.qmd", "notes"),
            ("inf-06-regression.qmd", "notes"),
            ("inf-07-anova.qmd", "notes"),
            ("inf-14-linear-hypotheses.qmd", "notes"),
            ("inf-15-two-factor-anova.qmd", "notes"),
            ("inf-16-predictive-values.qmd", "notes"),
        ],
    ),
    (
        "Data analysis",
        [
            ("da-01-studies-and-data.qmd", "notes"),
            ("da-02-descriptive-statistics.qmd", "notes"),
            ("da-04-estimation-examples.qmd", "notes"),
            ("da-05-testing-examples.qmd", "notes"),
            ("da-06-anova-examples.qmd", "notes"),
            ("da-07-regression-examples.qmd", "notes"),
            ("da-08-linear-model-examples.qmd", "notes"),
            ("da-09-chi-square-examples.qmd", "notes"),
        ],
    ),
    (
        "Using R",
        [
            ("da-03-using-r.qmd", "notes"),
            ("ur-01-exploratory-data-analysis.qmd", "notes"),
            ("ur-02-probability-and-simulation.qmd", "notes"),
            ("ur-03-bootstrap-and-numerical.qmd", "notes"),
            ("ur-04-mixtures-and-clustering.qmd", "notes"),
            ("ur-05-bayesian-computation.qmd", "notes"),
            ("ur-06-model-objects.qmd", "notes"),
            ("ur-07-glms-in-r.qmd", "notes"),
            ("ur-08-additive-models.qmd", "notes"),
            ("ur-09-repeated-measures.qmd", "notes"),
            ("ur-10-time-series.qmd", "notes"),
            ("ur-11-checking-a-fit.qmd", "notes"),
        ],
    ),
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
        "Statistical learning",
        [
            ("sl-01-multivariate-normal.qmd", "notes"),
            ("sl-02-normal-inference.qmd", "notes"),
            ("sl-03-principal-components.qmd", "notes"),
            ("sl-04-kmeans.qmd", "notes"),
            ("sl-05-mixtures-em.qmd", "notes"),
            ("sl-06-model-selection.qmd", "notes"),
            ("sl-07-linkage-and-density.qmd", "notes"),
            ("sl-08-discriminant-analysis.qmd", "notes"),
            ("sl-09-error-rates.qmd", "notes"),
            ("sl-10-logistic-regression.qmd", "notes"),
            ("sl-11-nearest-neighbours.qmd", "notes"),
            ("sl-12-classification-trees.qmd", "notes"),
            ("sl-13-ensembles.qmd", "notes"),
            ("sl-14-neural-units.qmd", "notes"),
            ("sl-15-backpropagation.qmd", "notes"),
            ("sl-16-networks-in-practice.qmd", "notes"),
            ("sl-17-support-vectors.qmd", "notes"),
            ("sl-18-high-dimensional.qmd", "notes"),
            ("sl-19-graphical-models.qmd", "notes"),
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
FIGURE_FILES: dict[str, dict] = {}  # PNG name -> the PDF, source and how it was drawn

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
        r"!\[((?:[^\[\]]|\[[^\]]*\])*)\]\((?:\.\./)*figures/([^)/\s]+)\.pdf\)(\{[^}]*\})?"
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


XREF_NOUNS = (
    r"Equations?|Theorems?|Lemmas?|Propositions?|Corollar(?:y|ies)"
    r"|Definitions?|Examples?|Figures?|Tables?|Sections?|Chapters?"
)
DOUBLED_XREF = re.compile(
    rf"\b(?:{XREF_NOUNS})\s+(?=@(?:eq|thm|lem|prp|cor|def|exm|fig|tbl|sec|rem|exr|ex)-[A-Za-z0-9_:-]+)",
    re.I,
)


def strip_doubled_xref_nouns(text: str) -> str:
    """Drop a redundant noun immediately before a Quarto @-reference, outside code."""
    return protect_code(text, lambda segment: DOUBLED_XREF.sub("", segment))


def localize_refs(text: str, notes_href: str) -> str:
    text = strip_doubled_xref_nouns(text)

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
        segment = DOUBLED_XREF.sub("", segment)

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
    # Figures drawn by make_figures.py in each notes folder.
    for notes in (PROBABILITY, INFERENCE, DATA):
        sources += sorted((notes / "figures").glob("*.pdf"))
    print(f"Converting {len(sources)} figures")
    scripts_copied: set[Path] = set()
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
        # The file page offers the original PDF and whatever drew it.
        shutil.copy2(src, dest / src.name)
        tex, script = src.with_suffix(".tex"), src.parent / "make_figures.py"
        if tex.exists():
            shutil.copy2(tex, dest / tex.name)
            made = {"source": tex.name, "how": "Drawn in TikZ. The source is a standalone LaTeX file."}
        elif script.exists():
            published = {
                "stat2003": "probability-make_figures.py",
                "stat2004": "inference-make_figures.py",
                "stat1301": "data-analysis-make_figures.py",
            }.get(src.parent.parent.name, "make_figures.py")
            if script not in scripts_copied:
                shutil.copy2(script, dest / published)
                scripts_copied.add(script)
            made = {"source": published, "how": "Drawn with Python and matplotlib from the example data. One script draws every figure in its section."}
        else:
            made = {"source": "", "how": "A figure from the course chapter."}
        # A high-resolution copy for the file page, as Wikipedia offers the original.
        full = f"{src.stem}-full.png"
        if pages == 1 and not (dest / full).exists():
            subprocess.run(
                ["pdftocairo", "-png", "-r", "300", "-singlefile", str(src), str(dest / Path(full).stem)],
                check=True,
                capture_output=True,
            )
        for png in FIGURE_PAGES[src.stem]:
            FIGURE_FILES[png] = {"pdf": src.name, "pages": pages, "full": full if pages == 1 else "", **made}


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
    for start, end, args in find_commands(q_region, "conceptquestion", 3):
        topic = ""
        for pos, name in topics:
            if pos < start:
                topic = name
        concept_qs.append({"n": int(args[0]), "text": args[1].strip(), "topic": topic, "label": args[2].strip()})

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
        while k < len(raw) and raw[k].isspace():
            k += 1
        label, k = read_delim(raw, k, "{", "}")
        body, k = read_environment_body(raw, k, "examquestion")
        exam_qs.append({"title": title.strip(), "label": label.strip(), "body": body.strip()})

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
    assert plain_question_title("Q22. Overdispersion") == "Overdispersion"
    assert plain_question_title("C37. Exchangeable correlation") == "Exchangeable correlation"
    assert plain_question_title("Question 6. Geometric--beta Gibbs sampler") == "Geometric--beta Gibbs sampler"
    chapter_guides.validate([name for _, files in PARTS for name, kind in files if kind == "notes"])


def clean_output() -> None:
    for name in ("notes", "questions", "answers", "reference", "articles", "files"):
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
    "P1": "prob-01-experiments.qmd",
    "P2": "prob-02-random-variables.qmd",
    "P3": "prob-03-simulation.qmd",
    "P4": "prob-04-joint-distributions.qmd",
    "P5": "prob-05-transforms-and-limits.qmd",
    "P6": "prob-06-markov-chains.qmd",
    "P7": "prob-07-reliability.qmd",
    "I1": "inf-01-statistical-inference.qmd",
    "I2": "inf-02-estimation.qmd",
    "I8": "inf-08-information-and-bounds.qmd",
    "I9": "inf-09-rao-blackwell.qmd",
    "I10": "inf-10-large-sample-estimation.qmd",
    "I3": "inf-03-confidence-intervals.qmd",
    "I4": "inf-04-hypothesis-tests.qmd",
    "I11": "inf-11-most-powerful-tests.qmd",
    "I12": "inf-12-generalised-likelihood-ratio.qmd",
    "I5": "inf-05-chi-square.qmd",
    "I13": "inf-13-exact-tests.qmd",
    "I6": "inf-06-regression.qmd",
    "I7": "inf-07-anova.qmd",
    "I14": "inf-14-linear-hypotheses.qmd",
    "I15": "inf-15-two-factor-anova.qmd",
    "I16": "inf-16-predictive-values.qmd",
    "D1": "da-01-studies-and-data.qmd",
    "D2": "da-02-descriptive-statistics.qmd",
    "D3": "da-03-using-r.qmd",
    "D4": "da-04-estimation-examples.qmd",
    "D5": "da-05-testing-examples.qmd",
    "D6": "da-06-anova-examples.qmd",
    "D7": "da-07-regression-examples.qmd",
    "D8": "da-08-linear-model-examples.qmd",
    "D9": "da-09-chi-square-examples.qmd",
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
    "SP1": "sp-01-stochastic-processes.qmd",
    "SP2": "sp-02-branching.qmd",
    "SP3": "sp-03-random-walks.qmd",
    "SP4": "sp-04-discrete-markov.qmd",
    "SP5": "sp-05-classes-and-reversibility.qmd",
    "SP6": "sp-06-poisson-processes.qmd",
    "SP7": "sp-07-continuous-markov.qmd",
    "SP8": "sp-08-queues.qmd",
    "SP9": "sp-09-probability-spaces.qmd",
    "SP10": "sp-10-random-variables.qmd",
    "SP11": "sp-11-convergence.qmd",
    "SP12": "sp-12-extremes.qmd",
    "L1": "sl-01-multivariate-normal.qmd",
    "L2": "sl-02-normal-inference.qmd",
    "L3": "sl-03-principal-components.qmd",
    "L4": "sl-04-kmeans.qmd",
    "L5": "sl-05-mixtures-em.qmd",
    "L6": "sl-06-model-selection.qmd",
    "L7": "sl-07-linkage-and-density.qmd",
    "L8": "sl-08-discriminant-analysis.qmd",
    "L9": "sl-09-error-rates.qmd",
    "L10": "sl-10-logistic-regression.qmd",
    "L11": "sl-11-nearest-neighbours.qmd",
    "L12": "sl-12-classification-trees.qmd",
    "L13": "sl-13-ensembles.qmd",
    "L14": "sl-14-neural-units.qmd",
    "L15": "sl-15-backpropagation.qmd",
    "L16": "sl-16-networks-in-practice.qmd",
    "L17": "sl-17-support-vectors.qmd",
    "L18": "sl-18-high-dimensional.qmd",
    "L19": "sl-19-graphical-models.qmd",
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


def plain_question_title(title: str) -> str:
    """Drop a positional label such as Q22, C37, or Question 6."""
    cleaned = re.sub(r"^(?:Q|C)\s*\d+\.\s*", "", title.strip())
    cleaned = re.sub(r"^Question\s+\d+\s*[.:]\s*", "", cleaned).strip()
    if not cleaned:
        raise SystemExit(f"Question title is only a number label: {title!r}")
    return cleaned


def short_label(q: dict) -> str:
    """The question's title, for lists that used to show Q22 or C37."""
    return q["title"]


def cell(text: str) -> str:
    return text.replace("|", "\\|")


def question_table(questions: list[dict], page: Path, with_topic: bool = False) -> str:
    head = ["Question", "Level"]
    if with_topic:
        head.append("Topic")
    head.append("Answer")
    aligns = [":--", ":-:"] + ([":--"] if with_topic else []) + [":-:"]
    rows = ["| " + " | ".join(head) + " |", "|" + "|".join(aligns) + "|"]
    for q in questions:
        bits = [f"[{cell(q['title'])}]({href(page, q['path'])})", cell(q["level"].capitalize())]
        if with_topic:
            topic = q["topic_note"]
            bits.append(f"[{cell(topic['title'])}]({href(page, topic['path'])})")
        bits.append("✓" if q.get("answer") else "–")
        rows.append("| " + " | ".join(bits) + " |")
    return "::: {.qtable}\n" + "\n".join(rows) + "\n:::\n"


def qcount_marker(n: int) -> str:
    noun = "question" if n == 1 else "questions"
    return f"<!-- qcount:{n} -->\n{n} {noun}.\n\n"


def check_qcounts(text: str, where: str) -> None:
    """The number written above a question table matches the rows in that table."""
    for part in text.split("<!-- qcount:")[1:]:
        n_str, rest = part.split("-->", 1)
        rows = len(re.findall(r"^\| \[", rest, re.M))
        if rows != int(n_str):
            raise SystemExit(f"{where}: stated {n_str} questions but listed {rows}")


def join_and(items: list[str]) -> str:
    if len(items) <= 1:
        return items[0] if items else ""
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return ", ".join(items[:-1]) + ", and " + items[-1]


def chapter_guide_md(filename: str, page: Path, notes: dict) -> str:
    guide = chapter_guides.GUIDES[filename]
    lines = [f"[{guide['level'].capitalize()}]{{.level}}", "", guide["summary"], "", "**What you need first.** "]
    if guide["needs"]:
        links = [f"[{notes[name]['title']}]({href(page, notes[name]['path'])})" for name in guide["needs"]]
        sentence = "Read " + join_and(links) + "."
        if guide["note"]:
            sentence += " " + guide["note"]
        lines.append(sentence)
    else:
        lines.append(guide["note"])
    return "::: {.chapter-guide}\n" + "\n".join(lines) + "\n:::\n\n"


def filter_box(placeholder: str) -> str:
    return f"""```{{=html}}
<div class="qfilter"><input type="search" placeholder="{placeholder}" aria-label="{placeholder}" oninput="wikiFilter(this.value)"><span class="qfilter-count"></span></div>
```
"""


RANDOM_AND_FILTER_JS = """<script>
(function () {
  var meta = document.querySelector('meta[name="quarto:offset"]');
  var offset = meta ? meta.getAttribute("content") : "./";
  var mod = document.createElement("script");
  mod.type = "module";
  mod.src = new URL(offset + "search-rank.js", location.href).href;
  document.head.appendChild(mod);
  if (location.hash === "#random" && !/\\/questions\\/random\\.html$/.test(location.pathname)) {
    location.replace(offset + "questions/random.html");
  }
  document.addEventListener("click", function (event) {
    var link = event.target.closest ? event.target.closest("a") : null;
    if (!link) return;
    var target = link.getAttribute("href") || "";
    if (target.slice(-7) !== "#random") return;
    event.preventDefault();
    window.location.href = offset + "questions/random.html";
  });
  var aliasMeta = null;
  var aliasPromise = null;
  var arrowMoved = false;
  function loadAliases() {
    if (aliasPromise) return aliasPromise;
    aliasPromise = fetch(new URL(offset + "search-aliases.json", location.href))
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (data) { aliasMeta = data; return data; })
      .catch(function () { return null; });
    return aliasPromise;
  }
  function goSearch(event) {
    var input = document.querySelector("#quarto-search input");
    var q = input ? input.value.trim() : "";
    if (!q) return;
    if (arrowMoved) {
      var active = document.querySelector('#quarto-search-results .aa-Item[aria-selected="true"] a[href]');
      var href = active ? active.getAttribute("href") || "" : "";
      if (href && href.indexOf("0767FDFD-") < 0) {
        event.preventDefault();
        event.stopPropagation();
        window.location.href = active.href;
        return;
      }
    }
    event.preventDefault();
    event.stopPropagation();
    window.location.href = offset + "search.html?query=" + encodeURIComponent(q);
  }
  document.addEventListener("focusin", function (event) {
    if (event.target && event.target.closest && event.target.closest("#quarto-search")) {
      loadAliases().then(function () { rankPanel(); });
    }
  });
  document.addEventListener("input", function (event) {
    if (event.target && event.target.closest && event.target.closest("#quarto-search")) {
      arrowMoved = false;
      loadAliases().then(function () { rankPanel(); });
    }
  });
  document.addEventListener("keydown", function (event) {
    if (!event.target.closest || !event.target.closest("#quarto-search")) return;
    if (event.key === "ArrowDown" || event.key === "ArrowUp") {
      arrowMoved = true;
      return;
    }
    if (event.key !== "Enter") return;
    goSearch(event);
  }, true);
  document.addEventListener("submit", function (event) {
    if (!event.target.closest || !event.target.closest("#quarto-search")) return;
    goSearch(event);
  }, true);
  function tierOf(href) {
    if (window.wikiSearchTier) return window.wikiSearchTier(href);
    var path = String(href || "").split("#")[0].replace(/^\\//, "");
    if (path.indexOf("files/") >= 0) return 3;
    if (path.indexOf("articles/") >= 0) return 0;
    if (path.indexOf("notes/") >= 0 || path.indexOf("reference/") >= 0) return 1;
    return 2;
  }
  function normHrefKey(href) {
    return String(href || "").split("?")[0].split("#")[0].replace(/^(\\.\\.\\/|\\.\\/|\\/)+/, "");
  }
  function rankPanel() {
    var input = document.querySelector("#quarto-search input");
    var q = input ? input.value.trim() : "";
    var exact = (q && window.wikiResolveExactMatch) ? window.wikiResolveExactMatch(q, aliasMeta) : null;
    var exactKey = exact ? normHrefKey(exact.href) : "";
    document.querySelectorAll(".aa-Panel").forEach(function (panel) {
      var prevBanner = panel.querySelector(".aa-DirectMatch");
      if (!exact) {
        if (prevBanner) prevBanner.remove();
      } else {
        var targetUrl = new URL(offset + exact.href.replace(/^\\//, ""), location.href).href;
        if (!prevBanner) {
          prevBanner = document.createElement("div");
          prevBanner.className = "aa-DirectMatch";
          panel.insertBefore(prevBanner, panel.firstChild);
        }
        prevBanner.textContent = "";
        var prefix = document.createTextNode("Direct match: ");
        var anchor = document.createElement("a");
        anchor.href = targetUrl;
        anchor.textContent = exact.title;
        prevBanner.appendChild(prefix);
        prevBanner.appendChild(anchor);
        if (exact.alias && exact.alias.toLowerCase() !== exact.title.toLowerCase()) {
          prevBanner.appendChild(document.createTextNode(" (" + exact.alias + ")"));
        }
      }
    });
    document.querySelectorAll(".aa-List").forEach(function (list) {
      var children = Array.prototype.slice.call(list.children);
      if (children.length < 2) return;
      var groups = [];
      children.forEach(function (item) {
        var link = item.querySelector("a");
        var href = link ? link.getAttribute("href") || "" : "";
        var isChild = href.indexOf("0767FDFD-") >= 0 || !!item.querySelector(".search-item, .search-more");
        if (isChild && groups.length) {
          groups[groups.length - 1].nodes.push(item);
        } else {
          var key = normHrefKey(href);
          groups.push({ key: key, href: href, tier: tierOf(href), isExact: !!(exactKey && key === exactKey), nodes: [item] });
        }
      });
      if (groups.length < 2) return;
      var ranked = groups.slice().sort(function (a, b) {
        if (a.isExact !== b.isExact) return a.isExact ? -1 : 1;
        return a.tier - b.tier;
      });
      var flat = [];
      ranked.forEach(function (g) { g.nodes.forEach(function (n) { flat.push(n); }); });
      var changed = flat.some(function (node, i) { return node !== children[i]; });
      if (!changed) return;
      flat.forEach(function (node) { list.appendChild(node); });
    });
  }
  var searchRoot = document.getElementById("quarto-search") || document.body;
  var rankingPanel = false;
  new MutationObserver(function () {
    if (rankingPanel) return;
    rankingPanel = true;
    try { rankPanel(); } finally { rankingPanel = false; }
  }).observe(searchRoot, { childList: true, subtree: true });
  // Highlight the top-bar section for this page's folder.
  var here = window.location.pathname.replace(/\\\\/g, "/");
  var section = /\\/labs\\//.test(here) ? "labs/index.html"
    : /\\/notes\\//.test(here) ? "notes/index.html"
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
  var menuName = /\\/questions\\//.test(here) ? "Question bank"
    : /\\/labs\\//.test(here) ? "Laboratories"
    : /\\/reference\\//.test(here) && !/\\/reference\\/glossary/.test(here) ? "Reference"
    : "";
  if (menuName) {
    document.querySelectorAll("#navbarCollapse .nav-link").forEach(function (link) {
      if ((link.textContent || "").trim().indexOf(menuName) === 0) link.classList.add("active");
    });
  }
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
    "def-sl-09-kfold": "K-fold cross-validation",
    "def-sl-11-knn": "K-nearest neighbours",
    "thm-moments": "Mean and variance of an exponential family",
    "thm-wold": "Wold decomposition",
    "thm-sl-02-hotelling": "Null distribution of Hotelling's T²",
    "thm-sl-02-two-sample": "Two-sample Hotelling F critical value",
}

# Headings that are not topics in their own right.
SKIP_HEADINGS = {"key idea", "exercises", "questions on this topic", "see also", "what links here", "what this chapter does not cover"}

# Index entries that point at another entry.
SEE_ALSO = {
    "GLM": "Generalised linear model",
    "GLMM": "Generalised linear mixed model",
    "GAM": "Sums of smooth functions",
    "GEE": "Generalised estimating equations",
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
PENDING_MERGED_BOXES: list[tuple[str, dict]] = []  # (target slug, box dict)
MERGED_ARTICLES: dict[str, str] = {}  # retired duplicate article slug -> canonical article slug
ARTICLE_DIR = WIKI / "articles"
DIST_SHEET = WIKI / "reference" / "distributions.qmd"
BOX_SLUG_OVERRIDES = {
    "def-sl-09-kfold": "fold-cross-validation",
    "def-sl-11-knn": "nearest-neighbours",
    "thm-sl-02-hotelling": "null-distribution-of-hotelling-s",
    "thm-sl-02-two-sample": "two-sample-hotelling-test",
}
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
        "extra_boxes": [],
        "extra_sections": [],
    }
    ARTICLES[slug_] = article
    return article


def register_box_article(note, part, ident, kind, term, lines, snippet) -> dict:
    box_dict = {
        "chapter": note["path"],
        "chapter_title": note["title"],
        "part": part,
        "anchor": ident,
        "kind": kind,
        "lines": list(lines),
        "snippet": snippet,
    }
    same = getattr(topics, "BOX_SAME_AS", {}).get(ident)
    if same:
        target_slug, old_slug = same
        MERGED_ARTICLES[old_slug] = target_slug
        BOX_ARTICLE[ident] = target_slug
        PENDING_MERGED_BOXES.append((target_slug, box_dict))
        return {"slug": target_slug, "path": ARTICLE_DIR / f"{target_slug}.qmd", "term": term}
    s = BOX_SLUG_OVERRIDES.get(ident) or slug(term)
    if s in ARTICLES and ARTICLES[s]["box"] is not None:
        s = f"{s}-{note['path'].stem}"  # two boxes with one name in different chapters
    article = ARTICLES.get(s) or new_article(s, term)
    article["term"] = term
    article["box"] = box_dict
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


# ---------------------------------------------------------------------------
# Topic pages
#
# A chapter heading that something names (a link phrase, a topic, an other
# name, a See also group, article_extras.py, a hand-written link, a title shared
# across chapters, or topics.PAGES) gets a page of its own in articles/ with the
# section's text on it, unless an article of the same name already exists. Its
# heading gains a "Main article" line. Other headings stay in their chapter
# only, so a chapter's story is not copied onto a page per step; a page such a
# heading used to have becomes a redirect to it. Ideas that a chapter names
# inside a paragraph get pages too, from topics.py, with a short lead and the
# paragraphs that discuss them.
# ---------------------------------------------------------------------------

import topics  # noqa: E402
from search_meta import DESCRIPTION as SITE_DESCRIPTION, SITE_NAME  # noqa: E402

TOPIC_KINDS = {"section", "topic"}
PAGE_PART: dict[Path, str] = {}  # chapter path -> part
SECTION_PAGE: dict[tuple[str, str], str] = {}  # (chapter file, heading id) -> article slug
TOPIC_TERMS: list[tuple] = []  # term links for named topics, in topics.py order
TOPIC_TERMS_LATE: list[tuple] = []
TOPIC_ERRORS: list[str] = []
TOPIC_EXAMPLES: dict[str, list[str]] = {}  # topic slug -> worked examples (exm- ids) shown on its page
SECTION_TEXT: dict[tuple[str, str], str] = {}  # (chapter file, heading id) -> text below the heading
SECTION_SLICES: dict[tuple[str, str], str] = {}  # (chapter file, heading id) -> slice captured in index_chapter
SECTION_TITLE: dict[tuple[str, str], str] = {}  # (chapter file, heading id) -> the heading as a page title
NO_PAGE: set[tuple[str, str]] = set()  # (chapter file, heading id) of headings left in their chapter only
RETIRED: dict[str, tuple[Path, str]] = {}  # published slug of a heading page no longer made -> (chapter, heading id)
REGISTRY = WIKI / "graph" / "ids.json"

# Inline maths in a heading, written out for a page title.
TITLE_MATH = {
    r"\lambda": "λ", r"\mu": "μ", r"\infty": "∞", r"\times": "×", r"\le": "≤", r"\ge": "≥",
    r"\sigma": "σ", r"\pi": "π", r"\alpha": "α", r"\beta": "β", r"\theta": "θ", r"\Sigma": "Σ",
}
SUPERSCRIPT = str.maketrans("0123456789T", "⁰¹²³⁴⁵⁶⁷⁸⁹ᵀ")
SUBSCRIPT = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def title_text(heading: str) -> str:
    """A heading as a page title: maths written out, markup and a leading "The" dropped."""

    def math(match: re.Match) -> str:
        tex = match.group(1)
        for cmd, char in TITLE_MATH.items():
            tex = re.sub(re.escape(cmd) + r"(?![A-Za-z])", char, tex)
        tex = re.sub(r"\\(?:mathbf|boldsymbol|mathrm|operatorname|text)\{([^{}]*)\}", r"\1", tex)
        tex = re.sub(r"\^\{?([0-9T]+)\}?", lambda m: m.group(1).translate(SUPERSCRIPT), tex)
        tex = re.sub(r"_\{?([0-9]+)\}?", lambda m: m.group(1).translate(SUBSCRIPT), tex)
        tex = tex.replace("{", "").replace("}", "").replace("\\", "")
        tex = re.sub(r"\s*([<>=−-])\s*", lambda m: f" {'−' if m.group(1) == '-' else m.group(1)} ", tex)
        return tex.strip()

    text = re.sub(r"\$([^$]+)\$", math, heading)
    text = re.sub(r"[*_`]", "", text)
    text = " ".join(text.replace("--", "–").split())
    text = re.sub(r"^The\s+(?=\S)", "", text)
    return text[:1].upper() + text[1:]


def chapter_sections(note: dict, prose: str) -> list[dict]:
    """The headings of a chapter outside boxes, each with the text below it."""
    lines = prose.split("\n")
    heads, depth = [], 0
    for i, line in enumerate(lines):
        if DIV_OPEN.match(line):
            depth += 1
            continue
        if DIV_CLOSE.match(line):
            depth = max(0, depth - 1)
            continue
        found = HEADING.match(line)
        if depth == 0 and found:
            hashes, text, attrs = found.groups()
            ident = re.search(r"#([\w-]+)", attrs or "")
            heads.append((i, len(hashes), text, ident.group(1) if ident else None))
    sections = []
    for k, (i, level, text, ident) in enumerate(heads):
        if not ident or plain(text).lower() in SKIP_HEADINGS:
            continue
        end = next((j for j, lv, _, _ in heads[k + 1 :] if lv <= level), len(lines))
        body = FOOTNOTE_DEF.sub("", "\n".join(lines[i + 1 : end])).strip()
        sections.append({"line": i, "level": level, "heading": text, "anchor": ident, "text": body})
    return sections


def paragraph_excerpt(prose: str, phrase: str, where: str) -> str:
    """The paragraph that first mentions phrase, with any display maths and the
    sentence that finishes it."""
    needle = phrase.lower()
    text = first_paragraph(prose, lambda flat: needle in flat.lower())
    if text is None:
        TOPIC_ERRORS.append(f"no paragraph mentions {phrase!r} in {where}")
        return ""
    return text


def naming_excerpt(prose: str, phrases: list[str]) -> str | None:
    """The paragraph that first names a topic by its title or a link phrase, as
    paragraph_excerpt finds it, or None when no paragraph does."""
    found = []
    for pattern in phrases:
        words = split_alternatives(topics.phrase_regex(pattern))
        acro = "|".join(w for w in words if ACRONYMS.match(w))
        rest = "|".join(w for w in words if not ACRONYMS.match(w))
        if rest:
            found.append(re.compile(rf"(?<![\w–-])(?:{rest})(?![\w–-])", re.I))
        if acro:
            found.append(re.compile(rf"(?<![\w–-])(?:{acro})(?![\w–-])"))
    return first_paragraph(prose, lambda flat: any(p.search(flat) for p in found))


def paragraph_blocks(prose: str) -> list[str]:
    """Logical blocks of prose: fenced code and display maths kept whole, div
    fences and box-article pointers dropped, headings separated from their bodies,
    and each prose paragraph joined with any display maths and continuation
    sentence that finishes it."""
    lines = prose.split("\n")
    chunks: list[str] = []
    cur: list[str] = []
    in_code = False
    in_math = False
    math_end = ""
    close_dd = re.compile(r"\$\$(?:\s*\{#[^}]*\})?\s*$")

    def flush() -> None:
        if cur:
            piece = "\n".join(cur).strip()
            if piece:
                chunks.append(piece)
            cur.clear()

    for line in lines:
        if re.match(r"^\s*```", line):
            if not in_code:
                flush()
                in_code = True
                cur.append(line)
            else:
                cur.append(line)
                in_code = False
                flush()
            continue
        if in_code:
            cur.append(line)
            continue
        if in_math:
            cur.append(line)
            if math_end == "$$" and close_dd.search(line.strip()):
                in_math = False
                flush()
            elif math_end != "$$" and math_end in line:
                in_math = False
                flush()
            continue
        stripped = line.strip()
        if stripped.startswith("$$"):
            flush()
            cur.append(line)
            if stripped == "$$" or not close_dd.search(stripped[2:]):
                in_math = True
                math_end = "$$"
            else:
                flush()
            continue
        m_env = re.match(r"^\\begin\{(align\*?|equation\*?|gather\*?)\}", stripped)
        if m_env:
            flush()
            cur.append(line)
            end_tok = rf"\end{{{m_env.group(1)}}}"
            if end_tok not in stripped:
                in_math = True
                math_end = end_tok
            else:
                flush()
            continue
        if re.match(r"^\s*:{3,}", line) or "{.box-article}" in line:
            flush()
            continue
        if re.match(r"^#{1,6}\s+", line):
            flush()
            chunks.append(stripped)
            continue
        if not stripped:
            flush()
            continue
        cur.append(line)
    flush()

    def is_display_math(block: str) -> bool:
        s = block.lstrip()
        return s.startswith(("$$", r"\begin{align", r"\begin{equation", r"\begin{gather"))

    def is_prose(block: str) -> bool:
        s = block.lstrip()
        return not s.startswith(("#", "|", "!", "```")) and not is_display_math(s)

    merged: list[str] = []
    i = 0
    while i < len(chunks):
        block = chunks[i]
        if is_prose(block):
            parts = [block]
            j = i + 1
            while j < len(chunks) and is_display_math(chunks[j]):
                parts.append(chunks[j])
                j += 1
                if j < len(chunks) and is_prose(chunks[j]) and re.match(r"\s*(?:[a-z]|where\b)", chunks[j]):
                    parts.append(chunks[j])
                    j += 1
            merged.append("\n\n".join(parts))
            i = j
        else:
            merged.append(block)
            i += 1
    return merged


def first_paragraph(prose: str, names) -> str | None:
    """The first paragraph whose text, links removed, passes names; with any
    display maths after it and the sentence that finishes that maths."""
    blocks = paragraph_blocks(prose)
    flat = [re.sub(r"\]\([^)]*\)(\{[^}]*\})?", "]", b).replace("[", "") for b in blocks]
    for i, b in enumerate(flat):
        if not b.lstrip().startswith(("#", "|", "!", "```", "$$", r"\begin{")) and names(b):
            return blocks[i]
    for i, b in enumerate(flat):
        if b.lstrip().startswith("#") and names(b):
            for j in range(i + 1, len(blocks)):
                cand = blocks[j].lstrip()
                if cand.startswith("#"):
                    break
                if not cand.startswith(("|", "!", "```")):
                    return blocks[j]
    for i, b in enumerate(flat):
        if b.lstrip().startswith("```") and names(b):
            if i > 0 and not blocks[i - 1].lstrip().startswith(("#", "|", "!", "```")):
                return blocks[i - 1] + "\n\n" + blocks[i]
            return blocks[i]
    return None


def section_title(fname: str, sec: dict) -> str:
    return topics.TITLES.get(f"{fname}#{sec['anchor']}") or title_text(sec["heading"])


def existing_article(title: str) -> str | None:
    """An article from a box or a card with this name, or its singular."""
    s = slug(title)
    for cand in (s, re.sub(r"ies$", "y", s), re.sub(r"s$", "", s), re.sub(r"es$", "", s)):
        a = ARTICLES.get(cand)
        if a and (a["card"] or (a["box"] and a["box"]["kind"] not in TOPIC_KINDS)):
            return cand
    return None


def topic_article(s: str, term: str, kind: str, note: dict, part: str, anchor: str) -> dict:
    article = ARTICLES.get(s) or new_article(s, term)
    if article["box"] is None:
        article["box"] = {
            "chapter": note["path"],
            "chapter_title": note["title"],
            "part": part,
            "anchor": anchor,
            "kind": kind,
            "lines": [],
            "snippet": "",
            "excerpts": [],
            "lead": "",
        }
    return article


def published_slugs() -> set[str]:
    """Article slugs the site has published, from the id registry. A heading
    page that is no longer made keeps its address only if it was published."""
    if not REGISTRY.exists():
        return set()
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    return {i.split(":", 1)[1] for i in [*data.get("ids", {}), *data.get("aliases", {})] if i.startswith("article:")}


def named_pages() -> tuple[set[str], set[tuple[str, str]], set[str]]:
    """The slugs, headings and titles that something names.

    A heading's page is worth having when a reader can arrive at it by name: a
    link phrase, a named topic, an other name or See also group, material in
    article_extras.py, a hand-written link in a source file, a title shared by
    headings in different chapters, or topics.PAGES. Each heading has its text
    in its chapter already.
    """
    slugs: set[str] = set()
    headings: set[tuple[str, str]] = set()
    for row in topics.LINKS + TERMS + topics.LINKS_LAST:
        code, key = row[1], row[2]
        if code == "ART":
            slugs.add(key)
        elif key and not key.startswith(("def-", "thm-", "prp-", "cor-", "rem-")):
            fname = CHAPTER_CODES[code]
            anchor = HEADING_ANCHORS.get((fname, plain(key)))
            if anchor:
                headings.add((fname, anchor))
    slugs |= {slug(spec["term"]) for spec in topics.TOPICS}
    slugs |= set(topics.ALIASES.values()) | {s for group in topics.RELATED for s in group}
    slugs |= set(PROPERTIES) | set(EXAMPLES) | set(FIGURES)
    slugs |= {s for group in PROPERTIES.values() for s in group} | {s for group in BOOK_EXAMPLES.values() for s in group}
    for path in SOURCES.rglob("*.qmd"):
        slugs |= set(re.findall(r"\barticles/([\w-]+)\.qmd", path.read_text(encoding="utf-8")))
    uses = Counter(topics.TITLES.values())
    keys = [k for k, title in topics.TITLES.items() if uses[title] > 1] + list(topics.SLUGS) + sorted(topics.PAGES)
    headings |= {tuple(k.split("#", 1)) for k in keys}
    titles = {t.lower() for t in SEE_ALSO.values()}
    return slugs, headings, titles


def register_topic_pages(prepared: list[tuple[str, dict, str]]) -> None:
    """Make a page for every named heading and every named topic."""
    by_file = {note["path"].name: (part, note, prose) for part, note, prose in prepared}
    for alias, target in topics.SAME_AS.items():
        if target not in ARTICLES:
            raise SystemExit(f"topics.SAME_AS[{alias!r}]: no article {target!r}")
    named_slugs, named_headings, named_titles = named_pages()
    sections: dict[str, list[dict]] = {}
    pending = []
    for part, note, prose in prepared:
        fname = note["path"].name
        sections[fname] = chapter_sections(note, prose)
        for sec in sections[fname]:
            key = f"{fname}#{sec['anchor']}"
            title = section_title(fname, sec)
            SECTION_TITLE[(fname, sec["anchor"])] = title
            target = topics.SAME_AS.get(key) or (None if key in topics.TITLES else existing_article(title))
            if target:
                SECTION_PAGE[(fname, sec["anchor"])] = target
                continue
            s = topics.SLUGS.get(key) or slug(title)
            if s in ARTICLES and ARTICLES[s]["box"] and ARTICLES[s]["box"]["kind"] not in TOPIC_KINDS:
                raise SystemExit(f"Heading {key} would replace the article {s}; give it a title in topics.TITLES")
            pending.append((part, note, sec, title, s))
    for key in sorted(topics.PAGES):
        fname, _, anchor = key.partition("#")
        if not any(sec["anchor"] == anchor for sec in sections.get(fname, [])):
            raise SystemExit(f"topics.PAGES: no heading {key}")
    # Headings with one title share a page, so a page is kept or not as a whole.
    kept = named_slugs | {
        s for _, note, sec, title, s in pending if (note["path"].name, sec["anchor"]) in named_headings or title.lower() in named_titles
    }
    published = published_slugs()
    for part, note, sec, title, s in pending:
        if s in kept:
            topic_article(s, title, "section", note, part, sec["anchor"])
            SECTION_PAGE[(note["path"].name, sec["anchor"])] = s
            continue
        NO_PAGE.add((note["path"].name, sec["anchor"]))
        if s in published:
            RETIRED.setdefault(s, (note["path"], sec["anchor"]))

    for spec in topics.TOPICS:
        s = slug(spec["term"])
        if s in ARTICLES and (ARTICLES[s]["card"] or ARTICLES[s]["box"]["kind"] not in TOPIC_KINDS):
            raise SystemExit(f"Topic {spec['term']!r} is already an article; list it in topics.ALIASES instead")
        homes = [spec["home"]] + spec["also"]
        places = []
        for place in homes:
            fname, _, rest = place.partition("#") if "#" in place else place.partition(":")
            fname = fname.strip()
            if fname not in by_file:
                raise SystemExit(f"Topic {spec['term']!r}: no chapter {fname}")
            part, note, prose = by_file[fname]
            if "#" in place and rest.startswith("exm-"):
                if rest not in BOOK_EXAMPLE_BOXES:
                    raise SystemExit(f"Topic {spec['term']!r}: no example #{rest} in {fname}")
                TOPIC_EXAMPLES.setdefault(s, []).append(rest)
                places.append((part, note, rest, ""))
            elif "#" in place:
                sec = next((x for x in sections[fname] if x["anchor"] == rest), None)
                if not sec:
                    raise SystemExit(f"Topic {spec['term']!r}: no heading #{rest} in {fname}")
                places.append((part, note, rest, None))
            else:
                places.append((part, note, "", rest.strip()))
        part, note, anchor, _ = places[0]
        article = topic_article(s, spec["term"], "topic", note, part, anchor)
        article["term"] = spec["term"]
        box = article["box"]
        box["kind"] = "topic"
        box["lead"] = spec["lead"]
        box["topic"] = spec
        box["places"] = places
        for phrase in spec["links"]:
            entry = (topics.phrase_regex(phrase), "ART", s, spec["scope"], spec["exclude"])
            (TOPIC_TERMS_LATE if spec["late"] else TOPIC_TERMS).append(entry)
    for group in topics.RELATED:
        for r in group:
            if r not in ARTICLES:
                raise SystemExit(f"topics.RELATED: no page {r!r}")


def add_main_article_notes(note: dict, prose: str) -> str:
    """A "Main article" line under each heading that has a page."""
    fname = note["path"].name
    lines = prose.split("\n")
    for sec in reversed(chapter_sections(note, prose)):
        s = SECTION_PAGE.get((fname, sec["anchor"]))
        if not s:
            continue
        a = ARTICLES[s]
        lines[sec["line"] + 1 : sec["line"] + 1] = [
            "",
            f"::: {{.mainarticle}}\nMain article: [{a['term']}]({href(note['path'], a['path'])})\n:::",
        ]
    out = "\n".join(lines)
    for sec in chapter_sections(note, out):
        text = re.sub(r"\A::: \{\.mainarticle\}\n.*?\n:::\s*", "", sec["text"], flags=re.S)
        SECTION_TEXT[(fname, sec["anchor"])] = text
    return out


def strip_paged_subsections(fname: str, text: str) -> str:
    """Remove child H3 subsections that already have their own article page."""
    out: list[str] = []
    skip = False
    depth = 0
    in_code = False
    for line in text.split("\n"):
        if re.match(r"^\s*```", line):
            in_code = not in_code
        if not in_code:
            if DIV_OPEN.match(line):
                depth += 1
            elif DIV_CLOSE.match(line):
                depth = max(0, depth - 1)
            elif depth == 0:
                found_head = HEADING.match(line)
                if found_head and len(found_head.group(1)) == 3:
                    found_id = re.search(r"#([\w-]+)", found_head.group(3) or "")
                    child_id = found_id.group(1) if found_id else ""
                    skip = bool(child_id and SECTION_PAGE.get((fname, child_id)))
        if not skip:
            out.append(line)
    return "\n".join(out).strip()


def fill_topic_pages(prepared: list[tuple[str, dict, str]]) -> None:
    """Copy each heading's text, and each named topic's paragraphs, onto its page."""
    by_file = {note["path"].name: prose for _, note, prose in prepared}
    MERGED_ARTICLES.update(getattr(topics, "MERGED", {}))
    for old_slug, target_slug in sorted(MERGED_ARTICLES.items()):
        if target_slug not in ARTICLES:
            raise SystemExit(f"MERGED[{old_slug!r}]: no canonical article {target_slug!r}")
        if old_slug in ARTICLES:
            raise SystemExit(f"MERGED[{old_slug!r}] was still emitted as an article")
        RETIRED.pop(old_slug, None)
    for target_slug, extra_box in PENDING_MERGED_BOXES:
        if target_slug not in ARTICLES:
            raise SystemExit(f"BOX_SAME_AS target {target_slug!r} was not emitted")
        ARTICLES[target_slug]["extra_boxes"].append(extra_box)
    sec_topic_refs = Counter(
        (note["path"].name, anchor)
        for a in ARTICLES.values()
        if a["box"] and a["box"].get("kind") == "topic"
        for _, note, anchor, phrase in a["box"]["places"]
        if phrase is None
    )
    for (fname, anchor), s in SECTION_PAGE.items():
        box = ARTICLES[s]["box"]
        note = next(n for _, n, _ in prepared if n["path"].name == fname)
        if not box or box["kind"] not in TOPIC_KINDS:
            # A chapter section unified onto a canonical box article via SAME_AS:
            # carry any prose outside the primary box onto the canonical article.
            sec_text = SECTION_TEXT[(fname, anchor)]
            if box and box.get("anchor"):
                own_box_re = re.compile(
                    rf"^:+\s*\{{#{re.escape(box['anchor'])}\s+\.[^}}]+\}}.*?^:+\s*$",
                    re.M | re.S,
                )
                sec_text = own_box_re.sub("", sec_text)
                sec_text = re.sub(r"^\[Article:[^\n]*\]\([^\n]*\)\{\.box-article\}\s*$", "", sec_text, flags=re.M)
            sec_text = sec_text.strip()
            if sec_text and (box is None or note["path"] != box["chapter"] or len(sec_text) > 120):
                ARTICLES[s]["extra_sections"].append(
                    {"chapter": note["path"], "chapter_title": note["title"], "part": PAGE_PART.get(note["path"], ""), "anchor": anchor, "text": sec_text}
                )
            continue
        box["excerpts"].append({"chapter": note["path"], "chapter_title": note["title"], "anchor": anchor, "text": SECTION_TEXT[(fname, anchor)]})
    for a in ARTICLES.values():
        box = a["box"]
        if not box or box.get("kind") != "topic":
            continue
        names = [box["topic"]["term"], *box["topic"]["links"]]
        for idx, (part, note, anchor, phrase) in enumerate(box["places"]):
            if phrase == "":
                continue  # a worked example, or the lead alone
            main = None
            if phrase is None:
                fname = note["path"].name
                text = SECTION_TEXT[(fname, anchor)]
                # A heading that is not this topic's own page is taught in full
                # in its chapter, and perhaps on a page of its own or under other
                # topics too. When the heading was retired and only this topic
                # claims it as its home, keep its text (minus child H3s with
                # pages of their own) instead of slicing off its setup or proof.
                own = SECTION_PAGE.get((fname, anchor))
                if own is None and sec_topic_refs[(fname, anchor)] == 1 and idx == 0:
                    trimmed = strip_paged_subsections(fname, text)
                    if trimmed:
                        text = trimmed
                elif own != a["slug"]:
                    part_text = naming_excerpt(text, names)
                    if part_text is None and own:
                        part_text = ""
                    if part_text is not None and part_text != text:
                        text = part_text
                        main = (ARTICLES[own]["term"], ARTICLES[own]["path"], "") if own else (SECTION_TITLE[(fname, anchor)], note["path"], anchor)
            else:
                text = paragraph_excerpt(by_file[note["path"].name], phrase, note["path"].name)
            if not any(e["chapter"] == note["path"] and e["text"] == text and e.get("main") == main for e in box["excerpts"]):
                box["excerpts"].append({"chapter": note["path"], "chapter_title": note["title"], "anchor": anchor, "text": text, "main": main})
    if TOPIC_ERRORS:
        raise SystemExit("topics.py:\n  " + "\n  ".join(TOPIC_ERRORS))
    for a in ARTICLES.values():
        box = a["box"]
        if box and box["kind"] in TOPIC_KINDS:
            source = box["lead"] or (box["excerpts"][0]["text"] if box["excerpts"] else "")
            source = re.split(r"\\begin\{", source)[0]  # a display environment does not fit a glossary cell
            box["snippet"] = snippet_from(source.split("\n"))


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
            ident = example.group(1)
            if ident in BOOK_EXAMPLE_BOXES:
                raise SystemExit(f"duplicate example anchor {ident}")
            title, content = box_contents(lines, i)
            BOOK_EXAMPLE_BOXES[ident] = {
                "title": plain(title or ident),
                "lines": content,
                "chapter": note["path"],
                "chapter_title": note["title"],
            }
    out = []
    depth = 0
    in_code = False
    used: set[str] = set()
    heading_marks: list[tuple[int, int, str | None]] = []
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
                if ident in BOX_TITLES:
                    lines[j] = f"## {title}"
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
            ident = None
            if plain(text).lower() not in SKIP_HEADINGS:
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
            heading_marks.append((len(out), len(hashes), ident))
        out.append(line)
        i += 1
    for mark, (idx, level, ident) in enumerate(heading_marks):
        if not ident:
            continue
        end = len(out)
        for later, later_level, _later_ident in heading_marks[mark + 1 :]:
            if later_level <= level:
                end = later
                break
        SECTION_SLICES[(fname, ident)] = "\n".join(out[idx + 1 : end]).strip()
    return "\n".join(out)


# Term links: (pattern, chapter code, heading text or box id, parts where it applies).
# Order matters: a longer or more specific phrase must come before a shorter one.
B, G, S, C, T = "Bayesian statistics", "Generalised linear models", "Smoothing", "Correlated data", "Time series"
P = "Probability"
I = "Statistical inference"
D = "Data analysis"
TERMS = [
    # Probability. Scoped so a phrase already owned by a later chapter
    # (Bayes' rule, a named distribution, MCMC) keeps that target.
    (r"conditional probabilit(?:y|ies)", "P1", "def-conditional-probability", {P, I, D}),
    (r"sample spaces?", "P1", "def-sample-space", {P}),
    (r"laws? of total probability", "P1", "thm-total-probability", {P}),
    (r"probability generating functions?", "P2", "def-probability-generating-function", {P}),
    (r"moment generating functions?", "P2", "def-moment-generating-function", {P}),
    (r"hypergeometric distributions?", "P2", "def-hypergeometric-distribution", None),
    (r"uniform distributions?", "P2", "def-uniform-distribution", None),
    (r"inverse[- ]transform methods?", "P3", "def-inverse-transform", None),
    (r"acceptance(?:-|–)rejection methods?", "P3", "def-acceptance-rejection", None),
    (r"covariance matrices|covariances?", "P4", "def-covariance", {P}),
    (r"central limit theorems?|CLT", "P5", "thm-central-limit-theorem", None),
    (r"laws? of large numbers|LLN", "P5", "thm-law-of-large-numbers", None),
    (r"finite[- ]state Markov chains?", "P6", "def-finite-state-markov-chain", None),
    (r"structure functions?", "P7", "def-structure-function", {P}),
    (r"reliability functions?", "P7", "def-reliability-function", {P}),
    (r"hazard rates?|failure rates?", "P7", "def-hazard-rate", None),
    (r"Weibull distributions?", "P7", "def-weibull-distribution", None),
    # Inference. Phrases already owned elsewhere (least squares, deviance, Bayes' rule) keep those targets.
    (r"maximum likelihood (?:estimates?|estimators?)|MLEs?", "I2", "def-maximum-likelihood", None),
    (r"methods? of moments", "I2", "def-method-of-moments", {I}),
    (r"unbiased estimators?", "I2", "def-unbiased-estimator", {I}),
    (r"confidence intervals?", "I3", "def-confidence-interval", None),
    (r"p-values?", "I4", "def-p-value", {I}),
    (r"type I errors?|type II errors?", "I4", "def-type-i-and-type-ii-errors", {I}),
    (r"goodness-of-fit tests?|contingency tables?", "I5", "def-pearson-statistic", {I}),
    (r"analysis of variance|ANOVA", "I7", "def-one-way-anova", None),
    (r"random samples?", "I1", "def-random-sample", {P, I, D}),
    (r"chi-squared distributions?|chi-square distributions?", "I1", "def-chi-squared-distribution", None),
    (r"Student(?:'s)? t[- ]distributions?|t[- ]distributions?", "I1", "def-student-t-distribution", None),
    (r"F[- ]distributions?", "I1", "def-f-distribution", None),
    (r"normal sample theorem", "I1", "thm-normal-sample-theorem", None),
    (r"likelihood functions?", "I2", "def-likelihood-function", {P, I, D}),
    (r"invariance of (?:the )?maximum likelihood(?: estimators?)?", "I2", "prp-invariance-of-maximum-likelihood", None),
    (r"mean squared errors?", "I2", "def-mean-squared-error", None),
    (r"consistent estimators?", "I2", "def-consistent-estimator", None),
    (r"sample correlations?(?: coefficients?)?", "I2", "def-sample-correlation-coefficient", None),
    (r"pivots?|pivotal quantit(?:y|ies)", "I3", "def-pivot", {I, D}),
    (r"pooled (?:sample )?variances?", "I3", "def-pooled-variance", None),
    (r"Wald intervals?", "I3", "def-wald-interval", {I, D}),
    (r"null hypothes[ie]s|alternative hypothes[ie]s", "I4", "def-null-and-alternative-hypotheses", {P, I, D}),
    (r"critical regions?|rejection regions?", "I4", "def-critical-region", None),
    (r"power functions?|power curves?", "I4", "def-power-function", None),
    (r"Neyman(?:--|–|-)Pearson lemma", "I11", "Neyman–Pearson lemma", None),
    (r"Neyman(?:--|–|-)Pearson(?: approach)?", "I4", "def-neyman-pearson-approach", None),
    (r"one-sample t[- ]tests?", "I4", "def-one-sample-t-test", None),
    (r"two-sample t[- ]tests?", "I4", "def-two-sample-t-test", None),
    (r"paired t[- ]tests?|paired samples?", "I4", "Paired samples", None),
    (r"F[- ]tests? for (?:equal|the equality of) variances", "I4", "def-f-test-for-equal-variances", None),
    (r"binomial tests?", "I4", "def-binomial-test", None),
    (r"two-proportion z[- ]tests?|tests? for (?:two )?proportions", "I4", "def-two-proportion-z-test", None),
    (r"sign tests?", "I4", "def-sign-test", None),
    (r"chi-squared tests? of independence|tests? of independence", "I5", "def-chi-squared-test-of-independence", None),
    (r"least-squares lines?|lines? of best fit", "I6", "def-least-squares-line", None),
    (r"coefficients? of determination", "I6", "def-coefficient-of-determination", None),
    (r"prediction intervals?", "I6", "def-prediction-interval", {I, D}),
    (r"regression effect|regression (?:towards?|to) (?:the mean|mediocrity)", "I6", "The regression effect", None),
    (r"contrasts?", "I7", "def-contrast", {I, D}),
    (r"Tukey(?:'s)? (?:intervals?|method|comparisons?)", "I7", "def-tukey-intervals", None),
    (r"randomi[sz]ed block designs?|block designs?", "I7", "def-randomised-block-design", None),
    # Probability terms that are more general than the inference phrases above.
    (r"joint (?:probability )?mass functions?", "P4", "def-joint-pmf", None),
    (r"joint (?:probability )?densit(?:y|ies)|joint density functions?", "P4", "def-joint-density", None),
    (r"independent random variables", "P4", "def-independent-random-variables", None),
    (r"independent events", "P1", "def-independent-events", None),
    (r"probability measures?", "P1", "def-probability-measure", {P}),
    (r"product rule", "P1", "thm-product-rule", {P, I, D}),
    (r"equally likely outcomes", "P1", "thm-equilikely", {P}),
    (r"random variables?", "P2", "def-random-variable", {P, I, D}),
    (r"cumulative distribution functions?|distribution functions?|cdfs?", "P2", "def-cdf", {P, I, D}),
    (r"probability mass functions?|mass functions?|pmfs?", "P2", "def-discrete-distribution", {P, I, D}),
    (r"probability density functions?|density functions?|pdfs?", "P2", "def-continuous-distribution", {P, I, D}),
    (r"expectations?|expected values?", "P2", "def-expectation", {P, I, D}),
    (r"Bernoulli (?:trials?|distributions?|variables?)", "P2", "def-bernoulli-distribution", None),
    (r"Poisson (?:limit|approximation)s?", "P2", "thm-poisson-limit-of-the-binomial", None),
    (r"memoryless(?: property)?|lack of memory", "P2", "thm-memoryless", None),
    (r"linear congruential generators?|pseudorandom numbers?|random number generators?", "P3", "def-linear-congruential-generator", None),
    (r"Box(?:--|–|-)Muller(?: method| transform)?", "P3", "Draws from the usual families", None),
    (r"expectation vectors?", "P4", "def-covariance-matrix", None),
    (r"conditional distributions?|conditional densit(?:y|ies)", "P4", "def-conditional-distribution", {P, I, D}),
    (r"tower property|law of (?:total|iterated) expectation", "P4", "thm-tower-property", None),
    (r"transformation rule|Jacobians?", "P5", "thm-transformation-rule", {P, I, D}),
    (r"convolutions?", "P5", "One variable, and a sum", None),
    (r"multivariate normal(?: distributions?)?|bivariate normal(?: distributions?)?|jointly normal", "P5", "def-multivariate-normal", None),
    (r"continuity corrections?", "P5", "Limit theorems", None),
    (r"limiting distributions?", "P6", "thm-limiting-distribution", None),
    (r"transition matri(?:x|ces)", "P6", "def-finite-state-markov-chain", None),
    (r"survival functions?|mean time to failure|MTTF", "P7", "def-survival", None),
    # Data analysis.
    (r"randomi[sz]ed controlled trials?|RCTs?", "D1", "def-randomised-controlled-trial", None),
    (r"confound(?:ing|ers?|ed)(?: variables?)?", "D1", "def-confounding-variable", None),
    (r"double-blind|blind(?:ed)? (?:experiments?|trials?)|placebos?", "D1", "def-blinding-and-placebo", None),
    (r"simple random samples?", "D1", "def-simple-random-sample", None),
    (r"stratified sampl(?:e|es|ing)|cluster sampl(?:e|es|ing)", "D1", "def-stratified-and-cluster-sampling", None),
    (r"sample quantiles?|percentiles?|quartiles?", "D2", "def-sample-quantile", {P, I, D}),
    (r"sample variances?|sample standard deviations?", "D2", "def-sample-variance-and-standard-deviation", {D}),
    (r"five-number summar(?:y|ies)|box ?plots?", "D2", "def-five-number-summary-and-boxplot", None),
    (r"normal quantile plots?|Q-Q plots?|QQ plots?", "D2", "def-normal-quantile-plot", None),
    (r"margins? of error", "D4", "def-margin-of-error", None),
    (r"Welch(?:'s)? (?:intervals?|t[- ]tests?|tests?)|Welch(?:--|–|-)Satterthwaite", "D4", "def-welch-interval", None),
    (r"Bonferroni(?: corrections?| methods?)?", "D6", "def-bonferroni-correction", None),
    (r"interactions?", "D6", "def-interaction", {D, I}),
    (r"multiple (?:linear )?regressions?", "D7", "def-multiple-linear-regression", {D, I}),
    (r"adjusted R-squared|adjusted \$R\^2\$", "D7", "def-adjusted-r-squared", None),
    (r"dummy variables?|indicator variables?|reference levels?", "D8", "def-dummy-variable-coding", {D, I}),
    (r"series systems?|parallel systems?|k-out-of-n systems?|minimal (?:path|cut) sets?", "P7", "def-structure-function", {P}),
    (r"observational studies?", "D1", "def-observational-study", None),
    (r"designed experiments?|randomised experiments?|randomized experiments?", "D1", "def-designed-experiment", None),
    (r"interquartile ranges?|IQRs?", "D2", "def-interquartile-range", None),
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
    # On the stochastic-process pages the stationary law and detailed balance are
    # developed for the process. The same phrases elsewhere stay with the sampler.
    (r"stationary distributions?", "SP4", "def-sp-stationary-distribution", {"Stochastic processes"}),
    (r"detailed balance", "SP5", "def-sp-detailed-balance", {"Stochastic processes"}),
    (r"Poisson processes?", "SP6", "def-sp-poisson-process", {"Stochastic processes"}),
    (r"Borel(?:--|–|-)Cantelli(?: lemmas?)?", "SP9", "thm-sp-borel-cantelli", {"Stochastic processes"}),
    (r"uniform integrability", "SP11", "def-sp-uniform-integrability", {"Stochastic processes"}),
    # MCMC
    # "Markov chain" on a probability page points at the finite-state chapter.
    # Elsewhere it stays with the Monte Carlo chapter. "MCMC" always does.
    (r"Markov chains?", "P6", "def-finite-state-markov-chain", {P, "Stochastic processes"}),
    (r"Markov chains?|MCMC", "B4", "def-markov-chain", {B, G, S, C, T, "Final preparation"}),
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
    # "Additive model" also means "no interaction" in an analysis of variance, and
    # Welch's test has effective degrees of freedom too, so this stays with smoothing.
    (r"effective degrees of freedom|additive models?", "S2", "Sums of smooth functions", {S, G, C, T}),
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

_COMPILED: list[tuple] = []  # (loose, strict, target page, anchor, scope, home chapter, pages excluded)

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
    entries = [tuple(t) + (set(),) * (5 - len(t)) for t in topics.LINKS + TOPIC_TERMS + TERMS + TOPIC_TERMS_LATE + topics.LINKS_LAST]
    for pattern, code, key, scope, exclude in entries:
        if code == "ART":
            article = ARTICLES.get(key)
            if not article:
                missing.append(f"article {key}")
                continue
            page, anchor, home = article["path"], "", article_home(article)
            if article["box"] and article["box"]["kind"] in TOPIC_KINDS:
                home = page  # a topic's own chapter links to it too
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
                elif (fname, anchor) in SECTION_PAGE:
                    page = home = ARTICLES[SECTION_PAGE[(fname, anchor)]]["path"]
                    anchor = ""
        words = split_alternatives(pattern)
        acro = "|".join(w for w in words if ACRONYMS.match(w))
        rest = "|".join(w for w in words if not ACRONYMS.match(w))
        # An en dash joins names too: "Beta–Binomial distribution" is not a binomial distribution.
        loose = re.compile(rf"(?<![\w–-])(?:{rest})(?![\w–-])", re.I) if rest else None
        strict = re.compile(rf"(?<![\w–-])(?:{acro})(?![\w–-])") if acro else None
        _COMPILED.append((loose, strict, page, anchor, scope, home, exclude))
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
    for loose, strict, target, anchor, scope, home, exclude in _COMPILED:
        # No link to the page itself, nor from the chapter that teaches the term.
        if target == page or home == page or (target, anchor) in done:
            continue
        if scope is not None and part not in scope:
            continue
        if page.stem in exclude:
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
COPIED_LABELS = {"property", "example", "excerpt"}  # article blocks copied from other pages


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
        // Relative to the site root, which may be a subfolder.
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


def with_kde_lab(note: dict, prose: str) -> str:
    """Mount the shared KDE figure on the chapter only.

    Article pages copy each section before this runs, so the bandwidth
    article keeps the link and does not grow a second copy of the script.
    """
    if note["path"].name != "sl-07-linkage-and-density.qmd":
        return prose
    marker = (
        "The [kernel density laboratory](../labs/kernel-density.qmd) draws this "
        "one-dimensional estimate from a known density. The sample stays fixed "
        "while the bandwidth moves. The figure reports that sample's integrated squared error "
        "and the mean integrated squared error."
    )
    if marker not in prose:
        raise SystemExit("sl-07 is missing the kernel density laboratory sentence; the figure has nowhere to go.")
    figure = (WIKI / "labs" / "_kde-figure.qmd").read_text(encoding="utf-8").strip()
    return prose.replace(marker, marker + "\n\n" + figure, 1)


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
    chapter_guides.validate([name for _, files in PARTS for name, kind in files if kind == "notes"])
    for q in questions:
        if q["topic"] not in chapter_guides.GUIDES:
            raise SystemExit(f"Question {q['id']} is filed under {q['topic']}, which has no level")
        q["level"] = chapter_guides.GUIDES[q["topic"]]["level"]
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

    # Chapters. Every chapter is read first, so that each heading's page can be
    # registered, and linked from its chapter, before any page is written.
    prepared = []
    for part, note in chapters:
        prose = prepare(strip_first_heading(note["prose"]), "../figures", page=note["path"])
        prepared.append((part, note, index_chapter(note, part, prose)))
    for part, note, _ in prepared:
        PAGE_PART[note["path"]] = part
    register_topic_pages(prepared)
    prepared = [(part, note, add_main_article_notes(note, prose)) for part, note, prose in prepared]
    fill_topic_pages(prepared)
    prepared = [(part, note, with_kde_lab(note, prose)) for part, note, prose in prepared]
    for part, note, prose in prepared:
        own = by_topic.get(note["path"].name, [])
        hat = [f"Part of **{part}**"]
        if own:
            noun = "question" if len(own) == 1 else "questions"
            hat.append(f"[{len(own)} {noun} on this topic](#questions-on-this-topic)")
        hat.append("[What links here](#what-links-here)")
        blocks = [
            (True, "guide", chapter_guide_md(note["path"].name, note["path"], notes)),
            (False, "hatnote", "::: {.hatnote}\n" + " · ".join(hat) + "\n:::\n\n"),
            (True, "prose", prose),
        ]
        if own:
            blocks.append(
                (
                    False,
                    "questions",
                    "\n\n## Questions on this topic {#questions-on-this-topic}\n\n"
                    "Open a question to attempt it. Its worked answer is folded away at the bottom of the page.\n\n"
                    + qcount_marker(len(own))
                    + question_table(own, note["path"]),
                )
            )
        own_articles = [a for a in ARTICLES.values() if a["box"] and a["box"]["chapter"] == note["path"] and a["box"]["kind"] not in TOPIC_KINDS]
        own_topics = [a for a in ARTICLES.values() if a["box"] and a["box"]["kind"] in TOPIC_KINDS and any(e["chapter"] == note["path"] for e in a["box"]["excerpts"])]
        siblings = [n for p, n in chapters if p == part]
        blocks.insert(2, (False, "infobox", chapter_infobox(note, part, siblings, own, own_articles)))
        article_line = (
            "- Articles from this chapter: "
            + " · ".join(f"[{a['term']}]({href(note['path'], a['path'])})" for a in own_articles)
            + "\n"
            if own_articles
            else ""
        )
        if own_topics:
            article_line += "- Topics in this chapter: " + " · ".join(f"[{a['term']}]({href(note['path'], a['path'])})" for a in own_topics) + "\n"
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
            blocks.append((False, "questions", "\n\n## Questions\n\n" + qcount_marker(len(own)) + question_table(own, note["path"], with_topic=True)))
        add_page(note["path"], note["title"], None, "final", blocks)

    # Questions. Previous and next walk the other questions on the same topic.
    for q in questions:
        group = q["group"]
        notes_href = href(q["path"], q["notes_path"]) if q.get("notes_path") else None
        use_refs = notes_href if group == "book" else None
        body = prepare(q["body"], "../figures", use_refs, page=q["path"])
        body = re.sub(r"\[Solution\]\(#sol-[\w-]+\)", "", body).strip()
        topic = q["topic_note"]
        seq = by_topic[q["topic"]]
        index = next(i for i, item in enumerate(seq) if item is q)
        total = len(seq)

        def pos_link(other: dict, label: str) -> str:
            title = cell(other["title"]).replace('"', "'")
            return f'[{label}]({href(q["path"], other["path"])} "{title}"){{.qnav}}'

        nav = [f'<span class="qpos">{index + 1} of {total}</span>']
        if index:
            nav.insert(0, pos_link(seq[index - 1], f"‹ {index} of {total}"))
        if index + 1 < total:
            nav.append(pos_link(seq[index + 1], f"{index + 2} of {total} ›"))
        more_q_label = "1 question on this topic" if total == 1 else "more questions on this topic"
        hat = (
            "::: {.hatnote}\n"
            f"[{q['level'].capitalize()}]{{.level}}\n\n"
            f"**Topic:** [{topic['title']}]({href(q['path'], topic['path'])}) · "
            f"[{more_q_label}]({href(q['path'], topic['path'])}#questions-on-this-topic)\n\n"
            + " ".join(nav)
            + "\n:::\n\n"
        )
        blocks = [(False, "hatnote", hat), (True, "question", body)]
        q["prepared_body"] = body  # reused when the question is an example on an article
        answer = q["answer"]
        if answer:
            answer_body = prepare(answer["body"], "../figures", page=q["path"])
            q["prepared_answer"] = answer_body
            blocks += [
                (False, "answer-open", "\n\n:::::::: {#worked-answer .callout-tip collapse=\"true\"}\n## Worked answer\n\n"),
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
    for alias, target in topics.ALIASES.items():
        if target not in ARTICLES:
            raise SystemExit(f"topics.ALIASES[{alias!r}]: no article {target!r}")
        if slug(alias) in ARTICLES:
            raise SystemExit(f"topics.ALIASES[{alias!r}]: {slug(alias)} is already a page")
        SEE_ALSO[alias] = ARTICLES[target]["term"]
        ARTICLES[target]["aliases"].append(f"{slug(alias)}.html")
    qmap = {q["id"]: q for q in questions}
    read_formula_tables(notes)
    check_extras(qmap)
    for article in sorted(ARTICLES.values(), key=lambda a: a["term"].lower()):
        PAGE_TITLES[article["path"]] = article["term"]
        blocks = article_blocks(article) + article_sections(article, qmap)
        add_page(article["path"], article["term"], article["box"]["part"] if article["box"] else None, "article", blocks, {})

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

    # Infobox, opening term framing, Used in and See also, on every article.
    for page in pages:
        if page["kind"] == "article":
            article = article_by_path[page["path"]]
            for idx, (is_c, lbl, txt) in enumerate(page["blocks"]):
                if is_c and lbl in {"lead", "excerpt"}:
                    page["blocks"][idx] = (is_c, lbl, frame_article_lead(article, txt))
                    break
            links = backlinks.get(page["path"], [])
            box = resolve_links(article_infobox(article, links, by_topic), page["path"])
            page["blocks"].insert(1, (False, "infobox", box))
            page["blocks"] += article_tail(article, links, forward.get(page["path"], []), questions, by_topic)

    for page in pages:
        meta_lines = "".join(f"{k}: {v}\n" for k, v in page["meta"].items())
        body = "".join(text for _, _, text in page["blocks"]).strip()
        page["path"].parent.mkdir(parents=True, exist_ok=True)
        page["path"].write_text(f"---\ntitle: {yaml_quote(page['title'])}\n{meta_lines}---\n\n{body}\n", encoding="utf-8")
        if page["kind"] in {"chapter", "final"}:
            check_qcounts(body, page["path"].name)

    write_indexes(notes, chapters, final_notes, questions, by_source, by_topic)
    write_glossary(questions)
    write_config(chapters, final_notes, questions)


REDIRECT_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirect</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url={target}">
<script type="text/javascript">
var redirects = {{"": "{target}"}};
var hash = window.location.hash.startsWith('#') ? window.location.hash.slice(1) : window.location.hash;
var redirect = redirects[hash] || redirects[""] || "/";
window.document.title = 'Redirect to ' + redirect;
window.location.replace(redirect);
</script>
</head>
<body>
<p>This section is in <a href="{target}">{chapter}</a>.</p>
</body>
</html>
"""


def write_retired_pages() -> None:
    """A redirect at the address of each heading page the site published and no
    longer makes, to the heading in its chapter, so outside links keep working.

    They are laid out like Quarto's alias redirects, so canonical_redirects.py
    gives each a canonical link and the other post-render steps pass over them.
    """
    redirects = {slug(alias) for alias in [*topics.ALIASES, *SEE_ALSO]}
    clash = sorted(s for s in RETIRED if s in ARTICLES or s in redirects)
    if clash:
        raise SystemExit(f"Retired heading pages clash with pages or redirects: {clash[:10]}")
    for s, (chapter, anchor) in sorted(RETIRED.items()):
        path = ARTICLE_DIR / f"{s}.html"
        target = f"{href(path, chapter.with_suffix('.html'))}#{anchor}"
        chapter_title = html_escape(PAGE_TITLES.get(chapter, "its chapter"))
        path.write_text(REDIRECT_HTML.format(target=target, chapter=chapter_title), encoding="utf-8")
    for old_slug, target_slug in sorted(MERGED_ARTICLES.items()):
        if old_slug in ARTICLES:
            raise SystemExit(f"Merged article {old_slug} was still written as a page")
        path = ARTICLE_DIR / f"{old_slug}.html"
        target = f"{target_slug}.html"
        dest_title = html_escape(ARTICLES[target_slug]["term"])
        path.write_text(REDIRECT_HTML.format(target=target, chapter=dest_title), encoding="utf-8")


def write_alias_redirect_pages() -> None:
    """Write canonical_redirects.py-compatible redirect stubs under articles/
    for unambiguous concept aliases that do not collide with real or retired pages."""
    ARTICLE_DIR.mkdir(parents=True, exist_ok=True)
    for s, (target_href, _label) in sorted(SEARCH_ALIASES.items()):
        if s in ARTICLES or s in RETIRED or s in MERGED_ARTICLES:
            continue
        if (ARTICLE_DIR / f"{s}.qmd").exists():
            continue
        base_target = target_href.split("#", 1)[0]
        target_qmd = (WIKI / base_target).with_suffix(".qmd")
        if not target_qmd.is_file():
            continue
        path = ARTICLE_DIR / f"{s}.html"
        rel_target = href(path, WIKI / base_target)
        if "#" in target_href:
            rel_target += "#" + target_href.split("#", 1)[1]
        dest_title = html_escape(PAGE_TITLES.get(target_qmd, target_qmd.stem.replace("-", " ")))
        path.write_text(REDIRECT_HTML.format(target=rel_target, chapter=dest_title), encoding="utf-8")


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
        out.append(f"**{'Page' if len(chapters) == 1 else 'Pages'}** ({len(chapters)})\n\n")
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
            groups.setdefault(q["group"], []).append((q.get("n", 0), f"[{cell(q['title'])}]({href(path, target)}){note}"))
        total = sum(len(v) for v in groups.values())
        if total == 1:
            only_in = next(iter(asked.values()))["in"]
            q_head = "Question" if only_in == {"question"} else "Question and answer"
        else:
            q_head = "Questions and answers"
        out.append(f"**{q_head}** ({total})\n\n")
        items = []
        for group in SOURCE_ORDER:
            if group in groups:
                items.extend(text for _, text in sorted(groups[group], key=lambda t: t[0]))
        if items:
            out.append("- " + " · ".join(items) + "\n")
    return "".join(out)


def topic_where(article: dict, path: Path) -> list[str]:
    """Links to every chapter place a topic page is taught in, home first."""
    box = article["box"]
    places = [(e["chapter"], e["chapter_title"], e["anchor"]) for e in box["excerpts"]]
    for part, note, anchor, phrase in box.get("places", []):
        places.append((note["path"], note["title"], anchor))
    if not places:
        places.append((box["chapter"], box["chapter_title"], box["anchor"]))
    out = []
    for chapter, title, anchor in places:
        item = f"[{title}]({href(path, chapter)}{'#' + anchor if anchor else ''})"
        if item not in out:
            out.append(item)
    return out


def extra_article_blocks(article: dict) -> list[tuple[bool, str, str]]:
    """Render unified secondary boxes and merged chapter sections on a canonical article."""
    path = article["path"]
    blocks: list[tuple[bool, str, str]] = []
    seen_heads: set[str] = set()
    for extra in article.get("extra_boxes") or []:
        head = extra["chapter_title"]
        if head in seen_heads:
            head = f"{head}, continued"
        seen_heads.add(head)
        ident = "in-" + slug(extra["chapter"].stem + "-" + extra["anchor"])
        source = f"{href(path, extra['chapter'])}#{extra['anchor']}"
        blocks.append(
            (
                False,
                "excerpt-head",
                f"## In *{head}* {{#{ident}}}\n\n"
                f"::: {{.mainarticle}}\n{extra['kind'].capitalize()} from [{extra['chapter_title']}]({source})\n:::\n\n",
            )
        )
        blocks.append((True, "excerpt", copy_for_article("\n".join(extra["lines"]), extra["chapter"], path) + "\n\n"))
    for extra in article.get("extra_sections") or []:
        head = extra["chapter_title"]
        if head in seen_heads:
            head = f"{head}, continued"
        seen_heads.add(head)
        ident = "in-" + slug(extra["chapter"].stem + "-" + extra["anchor"])
        source = f"{href(path, extra['chapter'])}#{extra['anchor']}"
        blocks.append(
            (
                False,
                "excerpt-head",
                f"## In *{head}* {{#{ident}}}\n\n"
                f"::: {{.mainarticle}}\nFrom [{extra['chapter_title']}]({source})\n:::\n\n",
            )
        )
        blocks.append((True, "excerpt", copy_for_article(extra["text"], extra["chapter"], path) + "\n\n"))
    return blocks


def part_link(part_name: str, from_path: Path) -> str:
    return f"[{part_name}]({href(from_path, WIKI / 'notes' / 'index.qmd')}#{slug(part_name)})"


def frame_article_lead(article: dict, text: str) -> str:
    """Bold or frame the opening defined term naturally in an article's first paragraph."""
    lead_body = text.rstrip("\n")
    trail = text[len(lead_body) :]
    first_para, sep, rest = lead_body.partition("\n\n")
    stripped = first_para.lstrip()
    if (
        not stripped
        or stripped.startswith(("$$", "\\begin{", ":::", "#", "|", "!"))
        or "**" in first_para
    ):
        return text
    term = article["term"]
    if f"*{term.lower()}*" in first_para.lower():
        return text

    candidates: list[str] = [term]
    box = article.get("box")
    if box and box.get("kind") == "topic":
        for raw_link in box["topic"].get("links", []):
            if not raw_link.startswith("re:") and not re.search(r"[\[\]()?|\\*+]", raw_link):
                candidates.append(raw_link)
            else:
                candidates.extend(plain_phrases_from_pattern(raw_link))

    spans = [(m.start(), m.end()) for m in PROTECT.finditer(first_para)]
    segments: list[tuple[str, bool]] = []
    last = 0
    for start, end in spans:
        segments.append((first_para[last:start], False))
        segments.append((first_para[start:end], True))
        last = end
    segments.append((first_para[last:], False))

    for cand in candidates:
        cand = cand.strip()
        if len(cand) < 2:
            continue
        pat = re.escape(cand.replace("–", " "))
        pat = pat.replace(r"\ ", "[-– ]+").replace(r"\-", "[-– ]?")
        pat = pat.replace(r"\'", "['’]?")
        if not ACRONYMS.match(cand) and cand[-1].isalpha() and not cand.endswith("s"):
            if cand.endswith("y") and len(cand) > 3 and cand[-2] not in "aeiou":
                pat = pat[:-1] + "(?:y|ies)"
            else:
                pat += "(?:s|es)?"
        flags = 0 if ACRONYMS.match(cand) else re.I
        rx = re.compile(rf"(?<![\w$–*-])(?:{pat})(?![\w$–*-])", flags)
        for i, (seg, is_prot) in enumerate(segments):
            if is_prot or not seg:
                continue
            m = rx.search(seg)
            if m:
                framed_seg = f"{seg[:m.start()]}**{m.group(0)}**{seg[m.end():]}"
                new_para = "".join(
                    framed_seg if idx == i else s for idx, (s, _) in enumerate(segments)
                )
                return f"{new_para}{sep}{rest}{trail}"

    # Handle inline-math letter prefixes such as "$p$-value" or "$t$-distribution".
    math_term = re.match(r"^([A-Za-z0-9²]+)[- ](.+)$", term)
    if math_term:
        sym, tail = math_term.groups()
        rx_math = re.compile(
            rf"(?<![\w*])(\${re.escape(sym)}\$[- ]{re.escape(tail)}(?:s|es)?)(?![\w–*-])",
            re.I,
        )
        m_math = rx_math.search(first_para)
        if m_math:
            new_para = f"{first_para[:m_math.start()]}**{m_math.group(1)}**{first_para[m_math.end():]}"
            return f"{new_para}{sep}{rest}{trail}"

    if box and box.get("kind") == "topic":
        return f"**{term}.** {first_para}{sep}{rest}{trail}"
    return text


def topic_blocks(article: dict) -> list[tuple[bool, str, str]]:
    """Hatnote, lead, and the chapter text of a heading's or a named topic's page."""
    path, box = article["path"], article["box"]
    excerpts = box["excerpts"]
    where = [re.sub(r"^\[(.*?)\]", r"[*\1*]", w) for w in topic_where(article, path)]
    for extra in article.get("extra_boxes") or []:
        w = f"[*{extra['chapter_title']}*]({href(path, extra['chapter'])}#{extra['anchor']})"
        if w not in where:
            where.append(w)
    noun = "Section" if box["kind"] == "section" else "Topic"
    p_link = part_link(box["part"], path)
    hat = f"{noun} of {where[0]}, part of {p_link}" if where else f"{noun}, part of {p_link}"
    if len(where) > 1:
        hat += " · Also in " + ", ".join(where[1:])
    blocks = [(False, "hatnote", "::: {.hatnote}\n" + hat + "\n:::\n\n")]
    if box["lead"]:
        blocks.append((True, "lead", box["lead"] + "\n\n"))
    single = len(excerpts) == 1 and not box["lead"]
    seen_heads = set()

    def main_link(e: dict) -> str:
        title, target, fragment = e["main"]
        return f"[{title}]({href(path, target)}{'#' + fragment if fragment else ''})"

    # Sections with a page of their own and no paragraph naming the topic are
    # listed together on one line, where the first of them would go.
    pointers = [main_link(e) for e in excerpts if not e["text"]]
    for e in excerpts:
        source = f"{href(path, e['chapter'])}{'#' + e['anchor'] if e['anchor'] else ''}"
        note = f"From [{e['chapter_title']}]({source})"
        if e.get("main"):  # one paragraph of a section that goes on
            note = f"Main article: {main_link(e)}"
        if not e["text"]:
            if pointers:
                label = "Main article" if len(pointers) == 1 else "Main articles"
                blocks.append((False, "excerpt-head", f"::: {{.mainarticle}}\n{label}: {join_and(pointers)}\n:::\n\n"))
                pointers = []
            continue
        if not single:
            head = e["chapter_title"]
            ident = "in-" + slug(e["chapter"].stem + "-" + (e["anchor"] or "text"))
            if head in seen_heads:
                head = f"{head}, continued"
            seen_heads.add(head)
            blocks.append((False, "excerpt-head", f"## In *{head}* {{#{ident}}}\n\n::: {{.mainarticle}}\n{note}\n:::\n\n"))
        elif e.get("main"):
            blocks.append((False, "excerpt-head", f"::: {{.mainarticle}}\n{note}\n:::\n\n"))
        blocks.append((True, "excerpt", copy_for_article(e["text"], e["chapter"], path) + "\n\n"))
    blocks.extend(extra_article_blocks(article))
    return blocks


def article_blocks(article: dict) -> list[tuple[bool, str, str]]:
    """Hatnote, lead and statement of an article. Used in and See also come later."""
    path, box, card = article["path"], article["box"], article["card"]
    if box and box["kind"] in TOPIC_KINDS:
        return topic_blocks(article)
    hat = []
    if box:
        hat.append(
            f"{box['kind'].capitalize()} taught in "
            f"[*{box['chapter_title']}*]({href(path, box['chapter'])}#{box['anchor']}), part of {part_link(box['part'], path)}"
        )
    also_places: list[str] = []
    for extra in (article.get("extra_boxes") or []) + (article.get("extra_sections") or []):
        w = f"[*{extra['chapter_title']}*]({href(path, extra['chapter'])}#{extra['anchor']})"
        if (not box or extra["chapter"] != box["chapter"]) and w not in also_places:
            also_places.append(w)
    if also_places:
        hat.append("Also in " + ", ".join(also_places))
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
                f"The **{card['name'].lower()} distribution**: "
                "parameters, support, probability function, mean and variance.\n\n",
            )
        )
    # The distribution card itself goes in the infobox.
    blocks.extend(extra_article_blocks(article))
    return blocks


def article_tail(article, links, forward, questions, by_topic) -> list[tuple[bool, str, str]]:
    path, box = article["path"], article["box"]
    home = article_home(article)
    by_q = {q["path"]: q for q in questions}
    lines = ["\n\n## Used in {#used-in}\n\n"]
    if box and box["kind"] in TOPIC_KINDS:
        taught = list(topic_where(article, path))
        for extra in article.get("extra_boxes") or []:
            item = f"[{extra['chapter_title']}]({href(path, extra['chapter'])}#{extra['anchor']})"
            if item not in taught:
                taught.append(item)
        lines.append("- **Taught in** " + " · ".join(taught) + "\n")
    elif box:
        taught = [f"[{box['chapter_title']}]({href(path, box['chapter'])}#{box['anchor']})"]
        for extra in (article.get("extra_boxes") or []) + (article.get("extra_sections") or []):
            item = f"[{extra['chapter_title']}]({href(path, extra['chapter'])}#{extra['anchor']})"
            if extra["chapter"] != box["chapter"] and item not in taught:
                taught.append(item)
        lines.append("- **Taught in** " + " · ".join(taught) + ", where the derivation and examples are.\n")
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
            note = " (answer)" if where == {"answer"} else ""
            groups.setdefault(q["group"], []).append((q.get("n", 0), f"[{cell(q['title'])}]({href(path, qpath)}){note}"))
        items = []
        for group in SOURCE_ORDER:
            if group in groups:
                items.extend(t for _, t in sorted(groups[group], key=lambda t: t[0]))
        use_label = "Question that uses it" if len(items) == 1 else "Questions that use it"
        lines.append(f"- **{use_label}** ({len(items)}) — " + " · ".join(items) + "\n")
    if box:
        n = len(by_topic.get(box["chapter"].name, []))
        if n == 1:
            lines.append(f"- [1 question on *{box['chapter_title']}*]({href(path, box['chapter'])}#questions-on-this-topic)\n")
        elif n > 1:
            lines.append(f"- [All {n} questions on *{box['chapter_title']}*]({href(path, box['chapter'])}#questions-on-this-topic)\n")

    # Neighbours: pages on the same idea elsewhere, articles this one links to,
    # articles that link here, then the chapter's other articles.
    article_paths = {a["path"]: a for a in ARTICLES.values()}
    near: list[dict] = [ARTICLES[r] for group in topics.RELATED if article["slug"] in group for r in group if r != article["slug"]]
    for p in forward:
        if p in article_paths and p != path:
            near.append(article_paths[p])
    for source, _, _ in links:
        if source["kind"] == "article" and source["path"] != path:
            near.append(article_paths[source["path"]])
    for other in ARTICLES.values():
        if other["path"] != path and article_home(other) == home:
            near.append(other)
    n_related = len({r for group in topics.RELATED if article["slug"] in group for r in group}) - (1 if any(article["slug"] in g for g in topics.RELATED) else 0)
    unique = list(dict.fromkeys(a["slug"] for a in near))[: max(8, n_related + 4)]
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

from article_extras import BOOK_EXAMPLES, CHAPTER_FIGURES, EXAMPLES, FIGURES, NOTES, PROPERTIES  # noqa: E402

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


def png_size(path: Path) -> tuple[int, int]:
    """Width and height from a PNG header."""
    head = path.read_bytes()[:24]
    return int.from_bytes(head[16:20], "big"), int.from_bytes(head[20:24], "big")


def kilobytes(path: Path) -> str:
    return f"{max(1, round(path.stat().st_size / 1024))} KB"


def write_file_pages() -> None:
    """One page per figure, as on Wikipedia: the image, what it shows, downloads, and where it is used."""
    figures_dir, files_dir = WIKI / "figures", WIKI / "files"
    files_dir.mkdir(exist_ok=True)
    usage: dict[str, list[tuple[str, Path]]] = {}
    alt_text: dict[str, str] = {}
    image = re.compile(r"!\[((?:[^\[\]]|\[[^\]]*\])*)\]\([^)\s]*figures/([^)\s/]+\.png)\)")
    for folder in ("notes", "articles", "questions", "reference"):
        for page in sorted((WIKI / folder).rglob("*.qmd")):
            text = page.read_text(encoding="utf-8")
            found = image.findall(text)
            if not found:
                continue
            title = re.search(r'^title:\s*"?(.*?)"?\s*$', text, re.M)
            name = title.group(1).replace('\\"', '"') if title else page.stem
            for alt, png in found:
                alt_text.setdefault(png, alt)
                if (name, page) not in usage.setdefault(png, []):
                    usage[png].append((name, page))
    gallery: dict[str, list[str]] = {}
    # Chapter order, as in the sidebar; figures that no chapter shows come last.
    order = {png: i for i, png in enumerate(FIGURE_INFO)}
    for png, made in sorted(FIGURE_FILES.items(), key=lambda item: (order.get(item[0], len(order)), item[0])):
        path = files_dir / f"{Path(png).stem}.qmd"
        info = FIGURE_INFO.get(png)
        if info:
            caption = rebase_links(info["caption"], info["chapter"], path)
            home = f"[{info['chapter_title']}]({href(path, info['chapter'])}{'#' + info['id'] if info['id'] else ''})"
        else:
            caption = re.sub(r"\s*\*From \[.*$", "", alt_text.get(png, "")).strip()
            home = ""
        width, height = png_size(figures_dir / png)
        lines = [
            '::: {.file-page}',
            f"[![{caption}]({href(path, figures_dir / png)})]({href(path, figures_dir / (made['full'] or png))})",
            "",
            f"*Size of this preview: {width} × {height} pixels. Select it to open the high-resolution file.*",
            ":::",
            "",
            "## Summary",
            "",
            f"**Description.** {caption}" if caption else "**Description.** None recorded.",
            "",
        ]
        if home:
            lines += [f"**Appears in.** {home}", ""]
        lines += [f"**Made by.** {made['how']}", "", "## Download", ""]
        if made["full"]:
            full_w, full_h = png_size(figures_dir / made["full"])
            lines.append(f"- [PNG, high resolution]({href(path, figures_dir / made['full'])}) ({full_w} × {full_h} pixels, {kilobytes(figures_dir / made['full'])})")
        lines.append(f"- [PNG, as shown on the wiki]({href(path, figures_dir / png)}) ({width} × {height} pixels, {kilobytes(figures_dir / png)})")
        pdf = figures_dir / made["pdf"]
        pages = f", {made['pages']} pages" if made["pages"] > 1 else ""
        lines.append(f"- [PDF, vector, prints at any size]({href(path, pdf)}) ({kilobytes(pdf)}{pages})")
        if made["source"]:
            kind = "TikZ source" if made["source"].endswith(".tex") else "Python script"
            lines.append(f"- [{kind}]({href(path, figures_dir / made['source'])}) (`{made['source']}`)")
        lines += ["", "## File usage", ""]
        used = usage.get(png, [])
        if used:
            lines.append(f"{'This page shows' if len(used) == 1 else f'These {len(used)} pages show'} the file:")
            lines.append("")
            lines += [f"- [{name}]({href(path, page)})" for name, page in sorted(used, key=lambda u: u[0].lower())]
        else:
            lines.append("No page shows this file yet.")
        write_qmd(path, f"File:{png}", "\n".join(lines) + "\n", description=f"Figure file · {info['chapter_title'] if info else SITE_NAME}")
        group = info["chapter_title"] if info else "Other figures"
        # An empty caption keeps a lone thumbnail from becoming a captioned figure.
        gallery.setdefault(group, []).append(f'[![]({href(files_dir / "index.qmd", figures_dir / png)}){{fig-alt="{Path(png).stem}"}}]({href(files_dir / "index.qmd", path)})')
    body = ["Select a figure to open its file page, with a larger view, a description, downloads, and the pages that use it.", ""]
    for group, thumbs in gallery.items():
        body += [f"## {group}", "", "::: {.file-gallery}", *thumbs, ":::", ""]
    write_qmd(files_dir / "index.qmd", "All figures", "\n".join(body), description="Every figure on the wiki")


def check_extras(qmap: dict) -> None:
    problems = []
    redirects = {slug(alias) for alias in [*topics.ALIASES, *SEE_ALSO]}
    for table, name in ((PROPERTIES, "PROPERTIES"), (EXAMPLES, "EXAMPLES"), (FIGURES, "FIGURES")):
        for slug_ in table:
            if slug_ not in ARTICLES:
                problems.append(f"{name}: no article {slug_}")
    for slug_, note_text in NOTES.items():
        if slug_ not in ARTICLES and slug_ not in RETIRED and slug_ not in redirects and slug_ not in MERGED_ARTICLES:
            problems.append(f"NOTES: no article {slug_}")
        elif slug_ in ARTICLES and note_text.strip():
            ARTICLES[slug_]["notes"] = expand_macros(note_text.strip())
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
    """Notes, Properties, Examples and Figures, below an article's lead."""
    path, slug_ = article["path"], article["slug"]
    blocks: list[tuple[bool, str, str]] = []

    if article.get("notes"):
        blocks.append((True, "explanation", "\n\n" + article["notes"] + "\n\n"))

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

    worked = [e for e, slugs in BOOK_EXAMPLES.items() if slug_ in slugs] + TOPIC_EXAMPLES.get(slug_, [])
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
        blocks.append((False, "example-answer-open", ":::::::: {.callout-tip collapse=\"true\"}\n## Worked answer\n\n"))
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
        mode = re.search(r"mode (\$[^$]+\$(?: (?:for|when) [^$;|]*\$[^$]+\$)?)", KERNEL_ROWS.get(slug_, ""))
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
    if box and box["kind"] in TOPIC_KINDS:
        taught = list(topic_where(article, path))
        for extra in article.get("extra_boxes") or []:
            item = f"[{extra['chapter_title']}]({href(path, extra['chapter'])}#{extra['anchor']})"
            if item not in taught:
                taught.append(item)
        rows.append(("Taught in", " · ".join(taught)))
        chapters_seen = (
            [e["chapter"] for e in box["excerpts"]]
            + [n["path"] for _, n, _, _ in box.get("places", [])]
            + [extra["chapter"] for extra in article.get("extra_boxes") or []]
        )
        parts = list(dict.fromkeys([box["part"]] + [PAGE_PART.get(c, box["part"]) for c in chapters_seen]))
        rows.append(("Part", " · ".join(part_link(p, path) for p in parts)))
    elif box:
        taught = [f"[{box['chapter_title']}]({href(path, box['chapter'])}#{box['anchor']})"]
        extra_chaps = []
        for extra in (article.get("extra_boxes") or []) + (article.get("extra_sections") or []):
            item = f"[{extra['chapter_title']}]({href(path, extra['chapter'])}#{extra['anchor']})"
            if extra["chapter"] != box["chapter"] and item not in taught:
                taught.append(item)
            extra_chaps.append(extra["chapter"])
        rows.append(("Taught in", " · ".join(taught)))
        parts = list(dict.fromkeys([box["part"]] + [PAGE_PART.get(c, box["part"]) for c in extra_chaps if c in PAGE_PART]))
        rows.append(("Part", " · ".join(part_link(p, path) for p in parts)))
    else:
        rows.append(("Listed on", f"[Distribution sheet]({href(path, DIST_SHEET)}#{card['anchor']})"))
    related_peers = list(
        dict.fromkeys(
            r for group in topics.RELATED if slug_ in group for r in group if r != slug_ and r in ARTICLES
        )
    )[:4]
    if related_peers:
        rows.append(
            (
                "Related",
                " · ".join(f"[{ARTICLES[r]['term']}]({href(path, ARTICLES[r]['path'])})" for r in related_peers),
            )
        )
    n_props = len(PROPERTIES.get(slug_, []))
    n_examples = len(EXAMPLES.get(slug_, [])) + sum(1 for s in BOOK_EXAMPLES.values() if slug_ in s) + len(TOPIC_EXAMPLES.get(slug_, []))
    n_questions = len({source["path"] for source, _, _ in links if source["kind"] == "question"})
    if n_props:
        rows.append(("Property" if n_props == 1 else "Properties", f"[{n_props}](#properties)"))
    if n_examples:
        rows.append(("Worked example" if n_examples == 1 else "Worked examples", f"[{n_examples}](#examples)"))
    if n_questions:
        rows.append(("Question using it" if n_questions == 1 else "Questions using it", f"[{n_questions}](#used-in)"))
    figures = FIGURES.get(slug_, [])
    image = figure_md(figures[0], path, short=True) if figures else ""
    return infobox_md(article["term"], rows, image, note)


def chapter_infobox(note: dict, part: str, siblings: list[dict], own: list[dict], own_articles: list[dict]) -> str:
    path = note["path"]
    i = next(k for k, n in enumerate(siblings) if n["path"] == path)
    level = chapter_guides.GUIDES[path.name]["level"].capitalize()
    rows = [("Part", part_link(part, path)), ("Level", level), ("Chapter", f"{i + 1} of {len(siblings)} in this part")]
    if i > 0:
        rows.append(("Previous", f"[{siblings[i - 1]['title']}]({href(path, siblings[i - 1]['path'])})"))
    if i + 1 < len(siblings):
        rows.append(("Next", f"[{siblings[i + 1]['title']}]({href(path, siblings[i + 1]['path'])})"))
    if own:
        rows.append(("Question" if len(own) == 1 else "Questions", f"[{len(own)}](#questions-on-this-topic)"))
    defs = [a for a in own_articles if a["box"]["kind"] == "definition"]
    results = [a for a in own_articles if a["box"]["kind"] in {"theorem", "proposition", "corollary"}]
    if defs:
        rows.append(("Definition" if len(defs) == 1 else "Definitions", " · ".join(f"[{a['term']}]({href(path, a['path'])})" for a in defs)))
    if results:
        rows.append(("Result" if len(results) == 1 else "Results", " · ".join(f"[{a['term']}]({href(path, a['path'])})" for a in results)))
    seen = CHAPTER_FIGURES_SEEN.get(path, [])
    if seen:
        n_figs = len(dict.fromkeys(seen))
        rows.append(("Figure" if n_figs == 1 else "Figures", str(n_figs)))
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
        if e["kind"] == "section" and (e["page"].name, e["anchor"]) in SECTION_PAGE:
            continue  # the heading's page is an entry already
        if e["kind"] == "section" and (e["page"].name, e["anchor"]) in NO_PAGE:
            continue  # a step in its chapter, not a term
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
        found = next((e for e in entries if e["term"].lower() == target.lower() and e["page"].parent.name == "articles"), None) or by_term.get(target.lower())
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
        f"The {n_articles} definitions, theorems, remarks, distributions, topics and sections each have a page of their own; "
        "questions link to their page, and redirects to the entry they stand for. "
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
    text = "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))  # Fréchet -> frechet
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def write_random_page(questions: list[dict]) -> None:
    page = WIKI / "questions" / "random.qmd"
    payload = [
        {
            "href": "/" + q["path"].relative_to(WIKI).with_suffix(".html").as_posix(),
            "title": q["title"],
            "topic": q["topic_note"]["title"],
            "part": q["topic_note"].get("part") or "",
            "level": q["level"],
            "answered": bool(q.get("answer")),
        }
        for q in questions
    ]
    blob = json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c")
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(
        f"""---
title: "Random question"
toc: false
---

Open one question. The list starts with questions that have a worked answer. Choose a topic, a level, or both.

{chapter_guides.LEVEL_RULE}

```{{=html}}
<form id="random-question" class="random-question">
  <label>Topic <select id="rq-topic"></select></label>
  <label>Level <select id="rq-level">
    <option value="">Any level</option>
    <option value="beginner">Beginner</option>
    <option value="intermediate">Intermediate</option>
    <option value="advanced">Advanced</option>
  </select></label>
  <label class="rq-check"><input id="rq-answered" type="checkbox" checked> Only questions with a worked answer</label>
  <button type="submit">Open a question</button>
  <p id="rq-status"></p>
</form>
<script id="rq-data" type="application/json">{blob}</script>
<script>
(function () {{
  var bank = JSON.parse(document.getElementById("rq-data").textContent);
  var topic = document.getElementById("rq-topic");
  var level = document.getElementById("rq-level");
  var answered = document.getElementById("rq-answered");
  var status = document.getElementById("rq-status");
  function pool() {{
    return bank.filter(function (q) {{
      if (answered.checked && !q.answered) return false;
      if (level.value && q.level !== level.value) return false;
      if (topic.value && q.topic !== topic.value) return false;
      return true;
    }});
  }}
  function fillTopics() {{
    var previous = topic.value;
    var seen = [];
    bank.forEach(function (q) {{
      if (answered.checked && !q.answered) return;
      if (level.value && q.level !== level.value) return;
      if (seen.some(function (item) {{ return item.topic === q.topic; }})) return;
      seen.push(q);
    }});
    seen.sort(function (a, b) {{ return a.part.localeCompare(b.part) || a.topic.localeCompare(b.topic); }});
    topic.innerHTML = "";
    var all = document.createElement("option");
    all.value = "";
    all.textContent = "All topics";
    topic.appendChild(all);
    var part = "";
    seen.forEach(function (q) {{
      if (q.part !== part) {{
        part = q.part;
        var group = document.createElement("optgroup");
        group.label = part || "Topics";
        topic.appendChild(group);
      }}
      var option = document.createElement("option");
      option.value = q.topic;
      option.textContent = q.topic;
      topic.lastChild.appendChild(option);
    }});
    var stillThere = Array.prototype.some.call(topic.options, function (option) {{ return option.value === previous; }});
    if (stillThere) topic.value = previous;
  }}
  function refresh() {{
    fillTopics();
    var n = pool().length;
    status.textContent = n ? (n === 1 ? "1 question matches." : n + " questions match.") : "No question matches. Clear a filter.";
  }}
  level.addEventListener("change", refresh);
  answered.addEventListener("change", refresh);
  topic.addEventListener("change", refresh);
  document.getElementById("random-question").addEventListener("submit", function (event) {{
    event.preventDefault();
    var matches = pool();
    if (!matches.length) {{ refresh(); return; }}
    window.location.href = matches[Math.floor(Math.random() * matches.length)].href;
  }});
  refresh();
}})();
</script>
```
""",
        encoding="utf-8",
    )


def plain_phrases_from_pattern(pattern: str) -> list[str]:
    """Extract plain-text alias phrases from simple regex alternatives in topics.py and TERMS."""
    out: list[str] = []
    for raw_alt in split_alternatives(pattern):
        alt = raw_alt.strip()
        if alt.startswith("re:"):
            alt = alt[3:].strip()
        if re.search(r"\(\?[=!<]|\\[dswDSW]|\.\*|\.\+", alt):
            continue
        s = alt.replace(r"\.", ".").replace(r"\'", "'")
        s = s.replace("σ", "sigma").replace("α", "alpha").replace("β", "beta").replace("λ", "lambda")
        s = s.replace("(?:--|–|-| )", "-").replace("(?:--|–|-)", "-")
        s = s.replace("[–-]", "-").replace("[- ]?", "-").replace("[- ]", " ")
        s = s.replace("['’]?", "'").replace("['’]", "'")
        s = s.replace("[sz]", "s").replace("u?", "u")
        s = re.sub(r"matri\(\?:x\|ces\)", "matrix", s)
        s = re.sub(r"\[ie\]s$", "is", s)
        s = re.sub(r"\(\?:y\|ies\)$", "y", s)
        s = re.sub(r"ies\?$", "y", s)
        s = re.sub(r"\(\?:s\|es\)\?$", "", s)
        s = re.sub(r"s\?$", "", s)
        if "(" in s or "[" in s or "\\" in s or "?" in s or "*" in s or "+" in s or "^" in s or "$" in s:
            short = re.sub(r"\(\?:[^()]+\)\?", "", s)
            short = re.sub(r"\s+", " ", short).strip(" -")
            if len(short) >= 2 and not re.search(r"[()\[\]\\?*+^$]", short):
                out.append(short)
            expanded = re.sub(r"\(\?:([^()|]+)\)\?", r"\1", s)
            expanded = re.sub(r"\s+", " ", expanded).strip(" -")
            if expanded != short and len(expanded) >= 2 and not re.search(r"[()\[\]\\?*+^$]", expanded):
                out.append(expanded)
            continue
        s = re.sub(r"\s+", " ", s).strip(" -")
        if len(s) >= 2:
            out.append(s)
    return out


def term_target_href(notes: dict, code: str, key: str) -> str | None:
    if code == "ART":
        article = ARTICLES.get(key)
        return f"articles/{article['slug']}.html" if article else None
    fname = CHAPTER_CODES.get(code)
    if not fname or fname not in notes:
        return None
    if key == "":
        return f"notes/{Path(fname).stem}.html"
    if key.startswith(("def-", "thm-", "prp-", "cor-", "rem-")):
        if key in BOX_ARTICLE:
            return f"articles/{BOX_ARTICLE[key]}.html"
        return f"notes/{Path(fname).stem}.html"
    anchor = HEADING_ANCHORS.get((fname, plain(key)), "")
    if (fname, anchor) in SECTION_PAGE:
        return f"articles/{SECTION_PAGE[(fname, anchor)]}.html"
    return f"notes/{Path(fname).stem}.html"


SEARCH_ALIASES: dict[str, tuple[str, str]] = {}  # alias slug -> (canonical href, display label)


def collect_search_aliases(notes: dict, chapters: list[tuple[str, dict]], final_notes: list[dict]) -> dict:
    """Build canonical concept metadata and unambiguous aliases for search and redirects."""
    pages: dict[str, dict] = {}
    for article in sorted(ARTICLES.values(), key=lambda a: a["slug"]):
        href_ = f"articles/{article['slug']}.html"
        pages[href_] = {"title": article["term"], "kind": "article", "aliases": []}
    for _part, note in chapters:
        href_ = f"notes/{note['path'].stem}.html"
        pages[href_] = {"title": note["title"], "kind": "chapter", "aliases": []}
    for note in final_notes:
        href_ = f"notes/{note['path'].stem}.html"
        pages[href_] = {"title": note["title"], "kind": "chapter", "aliases": []}
    pages["overview.html"] = {"title": "What statistics is", "kind": "overview", "aliases": []}
    pages["notes/index.html"] = {"title": "Topics", "kind": "index", "aliases": []}
    pages["questions/index.html"] = {"title": "Question bank", "kind": "index", "aliases": []}
    pages["questions/by-topic.html"] = {"title": "Questions by topic", "kind": "index", "aliases": []}
    pages["questions/random.html"] = {"title": "Random question", "kind": "index", "aliases": []}
    pages["reference/index.html"] = {"title": "Reference", "kind": "reference", "aliases": []}
    pages["reference/glossary.html"] = {"title": "Glossary and index", "kind": "reference", "aliases": []}
    pages["reference/distributions.html"] = {"title": "Common distributions", "kind": "reference", "aliases": []}
    pages["reference/formulas.html"] = {"title": "Formula lookup", "kind": "reference", "aliases": []}
    for lab_qmd in sorted((WIKI / "labs").glob("*.qmd")):
        if lab_qmd.name.startswith("_"):
            continue
        raw = lab_qmd.read_text(encoding="utf-8")
        m = re.search(r'^title:\s*"?(.*?)"?\s*$', raw, re.M)
        lab_title = m.group(1).replace('\\"', '"') if m else lab_qmd.stem
        pages[f"labs/{lab_qmd.stem}.html"] = {"title": lab_title, "kind": "laboratory", "aliases": []}

    title_slugs: set[str] = {slug(info["title"]) for info in pages.values() if slug(info["title"])}
    aliases_map: dict[str, str] = {}
    SEARCH_ALIASES.clear()

    def register_alias(label: str, target_href: str) -> None:
        s = slug(label)
        if not s or len(s) < 2 or target_href not in pages:
            return
        page_entry = pages[target_href]
        if label.strip() and label.strip().lower() != page_entry["title"].lower():
            if not any(existing.lower() == label.strip().lower() for existing in page_entry["aliases"]):
                page_entry["aliases"].append(label.strip())
        if s in ARTICLES or s in RETIRED or s in MERGED_ARTICLES or target_href == f"articles/{s}.html":
            return
        if s in aliases_map:
            return
        if s in title_slugs and slug(page_entry["title"]) != s:
            return
        aliases_map[s] = target_href
        SEARCH_ALIASES[s] = (target_href, label.strip())

    # 1. Explicit concept aliases in topics.ALIASES and SEE_ALSO.
    for alias, target in topics.ALIASES.items():
        if target in ARTICLES:
            register_alias(alias, f"articles/{target}.html")
    for alias, target_term in SEE_ALSO.items():
        found = next((a for a in ARTICLES.values() if a["term"].lower() == target_term.lower()), None)
        if found:
            register_alias(alias, f"articles/{found['slug']}.html")

    # 2. Distribution family short names (e.g. "normal", "beta", "poisson", "chi-squared").
    for article in sorted(ARTICLES.values(), key=lambda a: a["slug"]):
        term = article["term"]
        if term.lower().endswith(" distribution"):
            short = term[: -len(" distribution")].strip()
            if (
                len(slug(short)) >= 3
                and not re.search(r"\b(?:of|a|an|the|and|in|for)$", short, re.I)
                and slug(short) not in ARTICLES
                and slug(short) not in RETIRED
            ):
                register_alias(short, f"articles/{article['slug']}.html")

    # 3. Unambiguous phrases from topics.TOPICS, topics.LINKS, TERMS, and topics.LINKS_LAST.
    all_rows = [tuple(t)[:3] for t in topics.LINKS + TOPIC_TERMS + TERMS + TOPIC_TERMS_LATE + topics.LINKS_LAST]
    phrase_targets: dict[str, set[str]] = {}
    ordered_candidates: list[tuple[str, str]] = []
    for pattern, code, key in all_rows:
        target_href = term_target_href(notes, code, key)
        if not target_href:
            continue
        for phrase in plain_phrases_from_pattern(pattern):
            s = slug(phrase)
            if not s or len(s) < 2:
                continue
            phrase_targets.setdefault(s, set()).add(target_href)
            ordered_candidates.append((phrase, target_href))
    for phrase, target_href in ordered_candidates:
        s = slug(phrase)
        if len(phrase_targets.get(s, set())) == 1 and s not in RETIRED:
            register_alias(phrase, target_href)

    redirects_map = {
        s: f"notes/{chapter.stem}.html#{anchor}"
        for s, (chapter, anchor) in sorted(RETIRED.items())
    }
    for old_slug, target_slug in sorted(MERGED_ARTICLES.items()):
        redirects_map[old_slug] = f"articles/{target_slug}.html"
    return {"pages": pages, "aliases": aliases_map, "redirects": redirects_map}


def write_search_aliases(notes: dict, chapters: list[tuple[str, dict]], final_notes: list[dict]) -> dict:
    payload = collect_search_aliases(notes, chapters, final_notes)
    (WIKI / "search-aliases.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return payload


def write_search_page() -> None:
    page = WIKI / "search.qmd"
    page.write_text(
        """---
title: "Search"
toc: false
---

Press Enter in the search box at the top to open this page. Each page appears once, with exact concept and alias matches first and figure files last.

```{=html}
<form id="site-search" class="site-search" role="search">
  <label for="site-search-q">Search</label>
  <input id="site-search-q" type="search" name="q" autocomplete="off">
  <button type="submit">Search</button>
</form>
<div id="site-search-exact" class="search-exact" hidden></div>
<p id="site-search-note"></p>
<ol id="site-search-results"></ol>
<script type="module">
import { rankDocuments, resolveExactMatch, documentsFromIndex, expandedTerms, tierOf } from "./search-rank.js";

const form = document.getElementById("site-search");
const input = document.getElementById("site-search-q");
const exactBox = document.getElementById("site-search-exact");
const note = document.getElementById("site-search-note");
const list = document.getElementById("site-search-results");
const params = new URLSearchParams(location.search);
input.value = params.get("query") || "";

let cachedDocs = null;
let cachedMeta = null;
let lastRenderedQuery = "";

async function loadData() {
  if (cachedDocs) return { docs: cachedDocs, meta: cachedMeta };
  const [indexRes, aliasRes] = await Promise.all([
    fetch(new URL("search.json", location.href)),
    fetch(new URL("search-aliases.json", location.href)).catch(() => null),
  ]);
  if (!indexRes.ok) throw new Error("index unavailable");
  cachedDocs = documentsFromIndex(await indexRes.json());
  cachedMeta = aliasRes && aliasRes.ok ? await aliasRes.json() : null;
  return { docs: cachedDocs, meta: cachedMeta };
}

function kindOf(href) {
  const path = String(href || "").split("#")[0].replace(/^\\//, "");
  if (path.startsWith("labs/")) return "Laboratory";
  if (path.startsWith("questions/")) return "Question";
  if (path.startsWith("reference/")) return "Reference";
  const tier = tierOf(href);
  if (tier === 0) return "Article";
  if (tier === 1) return "Chapter";
  if (tier === 3) return "Figure";
  return "Page";
}

function snippet(doc, terms) {
  const text = String(doc.text || "").replace(/\\s+/g, " ").trim();
  if (!text) return "";
  const folded = text.toLowerCase();
  let at = -1;
  for (const term of terms) {
    const found = folded.indexOf(term.toLowerCase());
    if (found >= 0 && (at < 0 || found < at)) at = found;
  }
  if (at < 0) return text.slice(0, 180);
  const start = Math.max(0, at - 60);
  return (start ? "…" : "") + text.slice(start, start + 180) + (start + 180 < text.length ? "…" : "");
}

async function run(query, allowRedirect = false) {
  list.innerHTML = "";
  exactBox.hidden = true;
  exactBox.textContent = "";
  const q = query.trim();
  lastRenderedQuery = q;
  if (!q) {
    note.textContent = "Type a word, phrase, or abbreviation (such as ANOVA, OLS, MLE, CLT, GLM, or MCMC).";
    return;
  }
  let docs, meta;
  try {
    ({ docs, meta } = await loadData());
  } catch (_err) {
    note.textContent = "The search index is not available.";
    return;
  }
  const exact = resolveExactMatch(q, meta, docs);
  if (allowRedirect && exact) {
    window.location.href = exact.href;
    return;
  }
  if (exact) {
    const p = document.createElement("p");
    p.append("Direct match: ");
    const directLink = document.createElement("a");
    directLink.href = exact.href;
    directLink.style.fontWeight = "600";
    directLink.textContent = exact.title;
    p.append(directLink);
    if (exact.alias && exact.alias.toLowerCase() !== exact.title.toLowerCase()) {
      p.append(" (alias: " + exact.alias + ")");
    }
    p.append(" — press Enter again to open directly.");
    exactBox.appendChild(p);
    exactBox.hidden = false;
  }

  const found = rankDocuments(docs, q, meta);
  const terms = expandedTerms(q);
  const pageWord = found.length === 1 ? "page" : "pages";
  note.textContent = terms.length > 1
    ? found.length + " " + pageWord + ". Also matching " + terms.join(", ") + "."
    : found.length + " " + pageWord + ".";
  for (const doc of found.slice(0, 40)) {
    const item = document.createElement("li");
    const link = document.createElement("a");
    link.href = doc.href;
    link.textContent = doc.title || doc.href;
    const kind = document.createElement("span");
    kind.className = "search-kind";
    kind.textContent = kindOf(doc.href);
    item.append(link, kind);
    if (doc.matchedAlias) {
      const badge = document.createElement("span");
      badge.className = "search-alias";
      badge.textContent = doc.matchedAlias;
      item.append(badge);
    }
    const blurb = document.createElement("p");
    if (doc.section && doc.sectionHref) {
      const secLink = document.createElement("a");
      secLink.href = doc.sectionHref;
      secLink.className = "search-section-link";
      secLink.textContent = "§ " + doc.section;
      blurb.append(secLink, document.createTextNode(" — " + snippet(doc, terms)));
    } else {
      const sectionPrefix = doc.section ? doc.section + ". " : "";
      blurb.textContent = sectionPrefix + snippet(doc, terms);
    }
    item.append(blurb);
    list.appendChild(item);
  }
}

form.addEventListener("submit", async function (event) {
  event.preventDefault();
  const q = input.value.trim();
  if (q && q === lastRenderedQuery && cachedDocs) {
    const exact = resolveExactMatch(q, cachedMeta, cachedDocs);
    if (exact) {
      window.location.href = exact.href;
      return;
    }
  }
  const url = new URL(location.href);
  if (q) url.searchParams.set("query", q); else url.searchParams.delete("query");
  url.searchParams.delete("go");
  history.replaceState(null, "", url);
  await run(q, false);
});

run(input.value, params.get("go") === "1");
</script>
```
""",
        encoding="utf-8",
    )


def write_indexes(notes, chapters, final_notes, questions, by_source, by_topic) -> None:
    parts: dict[str, list[dict]] = {}
    for part, note in chapters:
        parts.setdefault(part, []).append(note)
    counts = {name: len(qs) for name, qs in by_topic.items()}
    n_answers = sum(1 for q in questions if q.get("answer"))

    # Topics: a contents page for the whole book.
    topics_path = WIKI / "notes" / "index.qmd"
    lines = [
        "Every chapter is an article. Each one ends with a table of the questions on its topic. "
        "The Probability section is the common language for the later chapters: experiments, random variables, simulation, dependence, limits, Markov chains and reliability. "
        "Stochastic processes continues from there: branching and first passage, Markov chains in discrete and continuous time, Poisson processes and queues, then sigma-algebras, modes of convergence, and maxima. "
        "Statistical learning builds classifiers, clusters, and high-dimensional fits on top of the regression, GLM, and smoothing chapters. "
        "Statistical inference then turns a random sample into an estimate, an interval, or a test. "
        "Data analysis is where a study and a table of summaries meet those methods. "
        "Using R is where those calculations are written down: objects, exploration, simulation, resampling, and the fits used in the later parts.",
        "",
        chapter_guides.LEVEL_RULE,
        "",
    ]
    for part, members in parts.items():
        lines += [f"## {part} {{#{slug(part)}}}", "", "| Chapter | Level | Questions |", "|:--|:-:|--:|"]
        for note in members:
            n = counts.get(note["path"].name, 0)
            level = chapter_guides.GUIDES[note["path"].name]["level"].capitalize()
            shown = str(n) if n else "–"
            lines.append(f"| [{cell(note['title'])}]({href(topics_path, note['path'])}) | {level} | {shown} |")
        lines.append("")
    lines += ["## Final preparation {#final-preparation}", ""]
    for note in final_notes:
        lines.append(f"- [{note['title']}]({href(topics_path, note['path'])})")
    fit = strip_first_heading(notes["index.qmd"]["prose"]).split("\n## On this site")[0].strip()
    # The prerequisites named in this paragraph are chapters on this site.
    fit = fit.replace(
        "a working knowledge of probability, the linear model,",
        "a working knowledge of [probability](prob-01-experiments.qmd), [the linear model](inf-06-regression.qmd),",
    )
    fit = fit.replace(
        "When a fit is shown, it is in R.",
        "When a fit is shown, it is in R, and the commands are gathered in [Using R](da-03-using-r.qmd).",
    )
    fit = autolink(prepare(fit, "../figures"), topics_path, None)
    lines += ["", "## How the topics fit together", "", fit]
    body = prepare("\n".join(lines), "../figures")
    topics_path.write_text(f"---\ntitle: \"Topics\"\n---\n\n{body}\n", encoding="utf-8")

    # Question bank is one list. By topic is the same questions under each chapter.
    q_index = WIKI / "questions" / "index.qmd"
    by_topic_path = WIKI / "questions" / "by-topic.qmd"
    random_path = WIKI / "questions" / "random.qmd"
    ordered: list[dict] = []
    part_totals: dict[str, int] = {}
    for part, members in parts.items():
        part_questions: list[dict] = []
        for note in members:
            part_questions.extend(by_topic.get(note["path"].name, []))
        ordered.extend(part_questions)
        part_totals[part] = len(part_questions)
    if {q["id"] for q in ordered} != {q["id"] for q in questions}:
        missing = [q["id"] for q in questions if q["id"] not in {item["id"] for item in ordered}]
        raise SystemExit(f"Question lists omit {missing[:8]}")
    lines = [
        f"All {len(ordered)} questions in one list. {n_answers} have a worked answer, folded away at the bottom of the question page.",
        "",
        chapter_guides.LEVEL_RULE,
        "",
        f"The [by topic]({href(q_index, by_topic_path)}) page groups these same questions under each chapter. "
        f"The [random question]({href(q_index, random_path)}) page draws one, from the worked answers unless you say otherwise.",
        "",
        filter_box("Filter questions, e.g. gibbs, poisson, deviance"),
        "",
        qcount_marker(len(ordered)) + question_table(ordered, q_index, with_topic=True),
    ]
    body = "\n".join(lines)
    check_qcounts(body, "question bank")
    q_index.write_text(f"---\ntitle: \"Question bank\"\ntoc: false\n---\n\n{body}\n", encoding="utf-8")

    lines = [
        f"The same {len(ordered)} questions as the [question bank]({href(by_topic_path, q_index)}), grouped under the chapter each one belongs to. "
        f"{n_answers} have a worked answer.",
        "",
        chapter_guides.LEVEL_RULE,
        "",
        filter_box("Filter questions, e.g. gibbs, poisson, deviance"),
        "",
    ]
    for part, members in parts.items():
        total = part_totals[part]
        if not total:
            continue
        noun = "question" if total == 1 else "questions"
        lines += [f"## {part} {{#{slug(part)}}}", "", f"{total} {noun} in this part.", ""]
        for note in members:
            qs = by_topic.get(note["path"].name, [])
            if not qs:
                continue
            lines += [
                f"### [{note['title']}]({href(by_topic_path, note['path'])})",
                "",
                qcount_marker(len(qs)) + question_table(qs, by_topic_path),
                "",
            ]
    body = "\n".join(lines)
    check_qcounts(body, "questions by topic")
    stated = sum(int(n) for n in re.findall(r"^(\d+) questions? in this part\.", body, flags=re.M))
    if stated != len(questions):
        raise SystemExit(f"By topic part counts sum to {stated}, not {len(questions)}")
    by_topic_path.write_text("---\ntitle: \"Questions by topic\"\ntoc-depth: 2\n---\n\n" + body + "\n", encoding="utf-8")
    write_random_page(questions)
    write_search_aliases(notes, chapters, final_notes)
    write_search_page()

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
        total = part_totals[part]
        items = "\n".join(f"- [{n['title']}]({href(home, n['path'])})" for n in members)
        more = ""
        if total:
            noun = "question" if total == 1 else "questions"
            more = f"\n\n[{total} {noun} →]({href(home, by_topic_path)}#{slug(part)}){{.portal-more}}"
        boxes.append(f"::: {{.portal-box}}\n### {part}\n\n{items}{more}\n:::\n")
    final_lines = []
    for note in final_notes:
        own_n = sum(1 for q in by_source["final"] if q["notes_path"] == note["path"])
        suffix = f" ({own_n} question{'s' if own_n != 1 else ''})" if own_n else ""
        final_lines.append(f"- [{note['title']}]({href(home, note['path'])}){suffix}")
    boxes.append("::: {.portal-box}\n### Final preparation\n\n" + "\n".join(final_lines) + "\n:::\n")
    boxes.append(
        "::: {.portal-box}\n### Question bank\n\n"
        "Every question in one list.\n\n"
        f"- [Question bank]({href(home, q_index)})\n"
        f"- [By topic]({href(home, by_topic_path)}), the same questions under each chapter\n"
        f"- [Random question]({href(home, random_path)})\n:::\n"
    )
    boxes.append(
        "::: {.portal-box}\n### Reference\n\n"
        "Lookup pages: a glossary, distributions, and formulas.\n\n"
        f"- [Reference]({href(home, WIKI / 'reference' / 'index.qmd')})\n"
        f"- [Common distributions]({href(home, WIKI / 'reference' / 'distributions.qmd')})\n"
        f"- [Formula lookup]({href(home, WIKI / 'reference' / 'formulas.qmd')})\n:::\n"
    )
    starter = "\n".join(
        f"{i}. [{notes[name]['title']}]({href(home, notes[name]['path'])})"
        for i, name in enumerate(chapter_guides.STARTER, 1)
    )
    overview_page = WIKI / "overview.qmd"
    if not overview_page.is_file():
        raise SystemExit("Missing overview.qmd")
    overview_href = href(home, overview_page)
    n_chapters = len(chapters)
    home_text = f"""---
title: {yaml_quote(SITE_NAME)}
toc: false
---

::: {{.portal-intro}}
A study wiki for data analysis, probability, stochastic processes, statistical learning, statistical inference, and the R used to compute them: **{n_chapters} chapters** and **{len(questions)} questions**, {n_answers} of them with worked answers. Every chapter lists the questions on its topic, and every question links back to its chapter. Press Enter in the search box for a results page, or open a [random question]({href(home, random_path)}).
:::

:::: {{.portal-top}}
::: {{.start-here}}
## New to statistics? Start here

[What statistics is]({overview_href}) is the map of the field as these pages teach it, and the place to start.

Then five chapters, in this order. Each later chapter says what to read first.

{starter}
:::

::: {{.how-to-study}}
## How to study with it

1. Read a chapter. The contents on the right jump between its sections.
2. Scroll to **Questions on this topic** at the end and open one.
3. Attempt it, then open **Worked answer** at the bottom of the question page.
4. The line **6 of 17** is your place among the questions on that topic. **‹ 5 of 17** and **7 of 17 ›** move to the previous and next one.
:::
::::

:::: {{.portal}}
{chr(10).join(boxes)}
::::
"""
    if home_text.find(overview_href) < 0 or home_text.find(overview_href) > home_text.find(starter.splitlines()[0]):
        raise SystemExit("Overview is not first in the start-here box")
    for part, total in part_totals.items():
        if not total:
            continue
        noun = "question" if total == 1 else "questions"
        needle = f"[{total} {noun} →]"
        if needle not in home_text:
            raise SystemExit(f"Home page is missing the {part} count {needle}")
    home.write_text(home_text, encoding="utf-8")


# Ask StatWiki: one small launcher on every page. The chat itself loads when
# someone opens it. Built from ask/widget by the publish workflow.
ASK_JS = """
<script>
(function () {
  var meta = document.querySelector('meta[name="quarto:offset"]');
  var offset = meta ? meta.getAttribute("content") : "./";
  var s = document.createElement("script");
  s.type = "module";
  s.src = offset + "ask/widget/dist/loader.js";
  document.head.appendChild(s);
})();
</script>
"""


# Run R in the browser on the Using R pages. This loader is on every page. It
# imports webr/runner.js only on a page of these parts that has an R block,
# and R itself downloads only when a reader presses Run. See webr/README.md.
RUNNABLE_PARTS = ("Using R",)
WEBR_FILES = ["runner.js", "engine.js", "session.js", "packages.js", "version.js"]
LAB_JS = [
    "lab-chrome.js",
    "svg-chart.js",
    "stat-math.js",
    "kde-math.js",
    "beta-binomial-math.js",
    "beta-binomial.js",
    "markov-math.js",
    "markov-chain.js",
    "coverage-math.js",
    "ci-coverage.js",
]
WEBR_JS = """
<script>
(function () {
  var pages = __RUNNABLE__;
  var meta = document.querySelector('meta[name="quarto:offset"]');
  var offset = meta ? meta.getAttribute("content") : "./";
  var root = new URL(offset, location.href).pathname;
  var here = location.pathname.slice(root.length).replace(/\\.html$/, "");
  if (pages.indexOf(here) < 0 || !document.querySelector("pre.sourceCode.r")) return;
  var start = function () {
    import(new URL(offset + "webr/runner.js", location.href).href).then(function (m) { m.install(); });
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
</script>
"""


def runnable_pages() -> list[str]:
    """Site paths, without .html, of the pages whose R blocks get Run buttons."""
    return [
        f"notes/{Path(filename).stem}"
        for part, files in PARTS
        if part in RUNNABLE_PARTS
        for filename, kind in files
        if kind == "notes"
    ]


# Every figure opens its file page, as an image does on Wikipedia. The file
# page itself links its image to the full PNG instead.
FILE_LINK_JS = """
<script>
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("main img").forEach((img) => {
    const src = img.getAttribute("src") || "";
    const m = src.match(/^(.*?)figures\\/([^\\/?#]+)\\.png$/);
    if (!m || img.closest("a")) return;
    const link = document.createElement("a");
    link.href = m[1] + "files/" + m[2] + ".html";
    link.className = "file-link";
    link.title = "Open the file page: larger view, downloads, and where it is used";
    img.parentNode.insertBefore(link, img);
    link.appendChild(img);
  });
});
</script>
"""


# Share cards use one wide image on every page: the browser-tab icon drawn
# at card size by make_share_image.py. The site's name and description live
# in search_meta.py, which also writes each page's own description after render.
SHARE_IMAGE = "share-icon.png"
SHARE_IMAGE_ALT = f"Contours of a bivariate normal density in viridis, the {SITE_NAME} icon"
SHARE_WIDTH = 1200
SHARE_HEIGHT = 630


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise SystemExit(f"{path.name} is not a PNG")
    return struct.unpack(">II", data[16:24])


BRISBANE_TZ = ZoneInfo("Australia/Brisbane")


def footer_text(now: datetime | None = None) -> str:
    """Copyright and the date of this build in Australia/Brisbane, for the foot of every page."""
    today = (now or datetime.now(BRISBANE_TZ)).astimezone(BRISBANE_TZ)
    return f"© {today.year} {SITE_NAME} · Last updated {today.day} {today:%B %Y}"


def write_config(chapters, final_notes, questions) -> None:
    share = WIKI / SHARE_IMAGE
    width, height = png_size(share)
    if (width, height) != (SHARE_WIDTH, SHARE_HEIGHT):
        raise SystemExit(f"{SHARE_IMAGE} must be {SHARE_WIDTH} by {SHARE_HEIGHT}, not {width} by {height}")

    (WIKI / "_random.html").write_text(
        RANDOM_AND_FILTER_JS
        + PREVIEW_JS
        + FILE_LINK_JS
        + ASK_JS
        + WEBR_JS.replace("__RUNNABLE__", json.dumps(runnable_pages())),
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
  # Quarto's alias pages are redirects. Give each one a canonical link after render.
  # Then write each page's search description and the home page's title and
  # site name, and check the share tags.
  post-render:
    - canonical_redirects.py
    - search_meta.py
    - share_preview.py
  # Render the generated pages only, not the course files copied into sources/.
  render:
    - "*.qmd"
    - "labs/*.qmd"
    - "!labs/_*.qmd"
    - "!sources/"
  resources:
    - katex/
    - figures/*.pdf
    - figures/*.tex
    - figures/*.py
    - figures/*-full.png
{chr(10).join(f"    - labs/{name}" for name in LAB_JS)}
{chr(10).join(f"    - webr/{name}" for name in WEBR_FILES)}
    - robots.txt
    - search-rank.js
    - search-aliases.json
    # Redirects from heading pages that are no longer made to their chapters.
    - articles/*.html
    - {SHARE_IMAGE}
    - wiki.json
    - ask/widget/dist/

website:
  title: {yaml_quote(SITE_NAME)}
  description: {yaml_quote(SITE_DESCRIPTION)}
  # Browser-tab icon: a bivariate normal density in viridis, 16 to 128 px.
  favicon: favicon.ico
  # Public host. Quarto writes sitemap.xml from this and each page's canonical link.
  site-url: "https://www.statwiki.io"
  # Leading slash: the same project file on every page, copied into the site root.
  image: /{SHARE_IMAGE}
  image-alt: {yaml_quote(SHARE_IMAGE_ALT)}
  open-graph:
    description: {yaml_quote(SITE_DESCRIPTION)}
    image: /{SHARE_IMAGE}
    image-alt: {yaml_quote(SHARE_IMAGE_ALT)}
    image-width: {SHARE_WIDTH}
    image-height: {SHARE_HEIGHT}
  twitter-card:
    card-style: summary_large_image
    description: {yaml_quote(SITE_DESCRIPTION)}
    image: /{SHARE_IMAGE}
    image-alt: {yaml_quote(SHARE_IMAGE_ALT)}
  search:
    location: navbar
    type: textbox
  navbar:
    left:
      - text: Main page
        href: index.qmd
      - text: Overview
        href: overview.qmd
      - text: Topics
        href: notes/index.qmd
      - text: Question bank
        menu:
          - text: "Question bank: every question in one list"
            href: questions/index.qmd
          - text: "By topic: the same questions under each chapter"
            href: questions/by-topic.qmd
      - text: Glossary
        href: reference/glossary.qmd
      - text: Reference
        menu:
          - text: "Lookup pages: glossary, distributions, and formulas"
            href: reference/index.qmd
          - text: Glossary and index
            href: reference/glossary.qmd
          - text: Common distributions
            href: reference/distributions.qmd
          - text: Formula lookup
            href: reference/formulas.qmd
      - text: Laboratories
        menu:
          - text: "All laboratories"
            href: labs/index.qmd
          - text: Kernel density estimation
            href: labs/kernel-density.qmd
          - text: "Beta–Binomial updating"
            href: labs/beta-binomial.qmd
          - text: A Markov chain
            href: labs/markov-chain.qmd
          - text: Interval coverage
            href: labs/ci-coverage.qmd
      - text: Random question
        href: questions/random.qmd
  sidebar:
    style: docked
    collapse-level: 2
    contents:
      - text: Main page
        href: index.qmd
      - text: Overview
        href: overview.qmd
      - text: Random question
        href: questions/random.qmd
      - section: Laboratories
        href: labs/index.qmd
        contents:
          - text: "All laboratories"
            href: labs/index.qmd
          - text: Kernel density estimation
            href: labs/kernel-density.qmd
          - text: "Beta–Binomial updating"
            href: labs/beta-binomial.qmd
          - text: A Markov chain
            href: labs/markov-chain.qmd
          - text: Interval coverage
            href: labs/ci-coverage.qmd
      - section: Topics
        href: notes/index.qmd
        contents:
{chr(10).join(part_blocks)}
      - section: Question bank
        href: questions/index.qmd
        contents:
          - text: "Question bank: every question in one list"
            href: questions/index.qmd
          - text: "By topic: the same questions under each chapter"
            href: questions/by-topic.qmd
      - section: Reference
        href: reference/index.qmd
        contents:
          - text: "Lookup pages: glossary, distributions, and formulas"
            href: reference/index.qmd
          - reference/glossary.qmd
          - reference/distributions.qmd
          - reference/formulas.qmd
          - files/index.qmd
  page-navigation: true
  page-footer:
    center: {yaml_quote(footer_text())}

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
    # Scroll, not wrap: R output is aligned in columns.
    code-overflow: scroll
    link-external-newwindow: true
    # In dark mode, apply the theme before the page is drawn; see _theme-head.html.
    include-in-header: _theme-head.html
    include-before-body: _theme-body.html
    include-after-body: _random.html
    # One canonical link per page, on the public host, so every page can be indexed.
    canonical-url: true
"""
    (WIKI / "_quarto.yml").write_text(yml, encoding="utf-8")
    if "noindex" in yml or "nofollow" in yml:
        raise SystemExit("Pages must not send noindex or nofollow")
    robots = (WIKI / "robots.txt").read_text(encoding="utf-8")
    if "User-agent: *" not in robots or "Allow: /" not in robots:
        raise SystemExit("robots.txt must allow every crawler")


def distributions_body() -> str:
    return r"""
The distributions below use the parameterisation fixed in each card. The second gamma parameter is a rate, and the second inverse-gamma parameter is the rate in $\exp(-\beta/x)$. The longer kernel table, with the problem-solving workflow, is on the [formula lookup](formulas.qmd) page. How a sample from one of these laws is summarised before a model is fitted is on [Descriptive statistics](../notes/da-02-descriptive-statistics.qmd).

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
### Hypergeometric

| | |
|---|---|
| Distribution | hypergeometric count of marked items |
| Parameters | population $N$, marked items $r$, draw $n$, with $p=r/N$ |
| Support | $\max(0,\,n-(N-r))\le x\le\min(n,r)$ |
| Probability mass function | $p(x)=\binom{r}{x}\binom{N-r}{n-x}/\binom{N}{n}$ |
| Expectation | $\mathbb{E}(x)=np$ |
| Variance | $\operatorname{Var}(x)=np(1-p)(N-n)/(N-1)$ |
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

::: {.dist-card}
### Uniform

| | |
|---|---|
| Distribution | $X\sim\operatorname{U}[a,b]$ |
| Parameters | $a<b$ |
| Support | $a\le x\le b$ |
| Probability density | $p(x)=1/(b-a)$ |
| Expectation | $\mathbb{E}(X)=(a+b)/2$ |
| Variance | $\operatorname{Var}(X)=(b-a)^{2}/12$ |
:::
"""


def chapter_source(filename: str) -> Path:
    """Chapter files live with the book, except the probability notes."""
    for folder in (BOOK / "chapters", PROBABILITY / "chapters", INFERENCE / "chapters", DATA / "chapters", USING / "chapters", STOCHASTIC / "chapters", LEARNING / "chapters"):
        path = folder / filename
        if path.exists():
            return path
    raise SystemExit(f"Missing chapter: {filename}")


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
            raw = chapter_source(filename).read_text(encoding="utf-8")
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

    for sol_path in (
        BOOK / "chapters" / "bayes-11-solutions.qmd",
        PROBABILITY / "chapters" / "prob-solutions.qmd",
        INFERENCE / "chapters" / "inf-solutions.qmd",
        DATA / "chapters" / "da-solutions.qmd",
        STOCHASTIC / "chapters" / "sp-solutions.qmd",
        LEARNING / "chapters" / "sl-solutions.qmd",
        USING / "chapters" / "ur-solutions.qmd",
    ):
        solutions = sol_path.read_text(encoding="utf-8")
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
            raw_title = exercise_title(body)
            q_title = plain_question_title(raw_title)
            number = re.match(r"Question\s+(\d+)", raw_title)
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
        title = plain_question_title(concept_titles.get(n) or item["topic"] or f"Concept {n}")
        questions.append(
            {
                "group": "concepts",
                "n": n,
                "id": f"c-{n:02d}",
                "label": item["label"],
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
        label = plain_question_title(re.sub(r"^Question\s+\d+\s*:\s*", "", item["title"]).strip())
        questions.append(
            {
                "group": "practice",
                "n": n,
                "id": f"q-{n:02d}",
                "label": item["label"],
                "title": label,
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
    import wiki_graph

    for item in wiki_graph.write_graph(
        notes,
        questions,
        answers,
        ARTICLES,
        GLOSSARY,
        HEADING_ANCHORS,
        BOOK_EXAMPLE_BOXES,
        FIGURE_INFO,
        SECTION_SLICES,
        update_ids="--update-ids" in sys.argv,
        retired={s: (chapter.name, anchor) for s, (chapter, anchor) in RETIRED.items()},
        merged=dict(MERGED_ARTICLES),
    ):
        print(f"Registry warning: vanished {item}")
    write_retired_pages()
    write_alias_redirect_pages()
    write_file_pages()

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

    # The wiki teaches each idea on its own pages. It does not send the reader
    # to a numbered section, a supplement or a set of notes somewhere else.
    outside = re.compile(
        r"\b(?:Example|Exercise|Section|Chapter|Theorem|Remark|Definition|Figure|Table|Supplement|Appendix|Lemma"
        r"|Corollary|Proposition)s? \d+\.\d+"
        r"|\bsupplement(?:ary)? notes?\b|\b(?:these|the|lecture|course) notes\b|\btextbook\b|\bthe book\b"
        r"|\bat the back\b|\?\?|\bMinitab\b|\bin lectures?\b|\bthe slides\b",
        re.I,
    )
    # A control character in a source file is almost always a lost backslash,
    # such as \b in \bmod turned into a backspace by a script.
    for path in sorted(SOURCES.rglob("*.qmd")):
        bad = re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", path.read_text(encoding="utf-8"))
        if bad:
            raise SystemExit(f"Control character {bad.group(0)!r} in {path.relative_to(WIKI)}")
    doubled_link_xref = re.compile(
        rf"\b(?:{XREF_NOUNS})\s+\[(?:Equation|Theorem|Lemma|Proposition|Corollary|Definition|Example|Figure|Table|Section|Chapter|Note)\b",
        re.I,
    )
    cited = []
    doubled = []
    for folder in ("notes", "questions", "articles", "reference"):
        for path in sorted((WIKI / folder).rglob("*.qmd")):
            pieces = re.split(r"(```.*?```)", path.read_text(encoding="utf-8"), flags=re.S)
            for piece in pieces:
                if not piece.startswith("```"):
                    cited += [f"{path.relative_to(WIKI)}: {m.group(0)}" for m in outside.finditer(piece)]
                    doubled += [f"{path.relative_to(WIKI)}: {m.group(0)}" for m in DOUBLED_XREF.finditer(piece)]
                    doubled += [f"{path.relative_to(WIKI)}: {m.group(0)}" for m in doubled_link_xref.finditer(piece)]
    if cited:
        raise SystemExit("Pages point at outside material:\n  " + "\n  ".join(cited[:20]))
    if doubled:
        raise SystemExit("Pages contain doubled cross-reference nouns:\n  " + "\n  ".join(doubled[:20]))

    print(f"Chapter pages: {len([n for n in notes.values() if n['kind'] == 'notes'])}")
    print(f"Question pages: {len(questions)}, with answers: {sum(1 for q in questions if q.get('answer'))}")
    print("Wiki source is ready.")


if __name__ == "__main__":
    main()
