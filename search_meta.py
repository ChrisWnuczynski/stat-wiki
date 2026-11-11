"""Write what search engines read about each page, after quarto render.

- Every page gets a meta description of its own. A page keeps the description
  it was written with when that is specific to it (the laboratories have
  one). Otherwise the description is the page's opening sentences: the
  summary under a chapter's title, the first paragraph of a topic page, the
  text of a question. Simple maths becomes plain text (theta, X_0 and t^2
  become θ, X₀ and t²); a sentence with harder maths ends the description
  there. A page with no usable opening gets a sentence made from its title.
  The same text becomes the Open Graph and Twitter description, so a shared
  link describes its own page.
- The home page gets a longer title naming StatWiki.io, the site
  description, and WebSite structured data giving Google the site's name
  and the alternatives to use if that name is taken.
- sitemap.xml lists the home page at the site root, its canonical URL,
  rather than at index.html.

Google ignores a description repeated on many pages. Two pages that end up
with the same one get their titles put in front; any still shared are
reported, without stopping the build.
"""

from __future__ import annotations

import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SITE = "https://www.statwiki.io/"
SITE_NAME = "StatWiki"
# Google tries these in order if it does not use SITE_NAME. The lowercase
# domain is its documented last resort.
ALTERNATE_NAMES = ["StatWiki.io", "statwiki.io"]
HOME_TITLE = "StatWiki.io: Statistics notes, practice questions and labs"
DESCRIPTION = (
    "A statistics study wiki: chapters from probability to statistical learning, "
    "practice questions with worked answers, interactive labs and R in your browser."
)
LIMIT = 160  # Google cuts a snippet at about this many characters.
SHORTEST = 50

# Share and search text names no course code and no code host.
BANNED = re.compile(r"STAT\s*\d|github", re.I)

ROOT = Path(__file__).resolve().parent
SITE_DIR = ROOT / "_site"


# ---------------------------------------------------------------- maths

GREEK = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε", "varepsilon": "ε",
    "zeta": "ζ", "eta": "η", "theta": "θ", "vartheta": "ϑ", "iota": "ι", "kappa": "κ",
    "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "pi": "π", "rho": "ρ", "sigma": "σ",
    "tau": "τ", "upsilon": "υ", "phi": "φ", "varphi": "φ", "chi": "χ", "psi": "ψ", "omega": "ω",
    "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ", "Xi": "Ξ", "Pi": "Π",
    "Sigma": "Σ", "Phi": "Φ", "Psi": "Ψ", "Omega": "Ω",
}
SYMBOLS = {
    "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "ne": "≠", "neq": "≠", "to": "→",
    "rightarrow": "→", "infty": "∞", "cdot": "·", "times": "×", "sim": "~", "ldots": "…",
    "dots": "…", "cdots": "…", "in": "∈", "notin": "∉", "mid": "|", "pm": "±", "approx": "≈",
    "subset": "⊂", "subseteq": "⊆", "cup": "∪", "cap": "∩", "emptyset": "∅", "partial": "∂",
    "propto": "∝", "perp": "⊥", "ell": "ℓ", "vert": "|", "lvert": "|", "rvert": "|",
    "langle": "⟨", "rangle": "⟩", "quad": " ", "qquad": " ", "{": "{", "}": "}", "%": "%",
    "_": "_", ",": " ", ";": " ", ":": " ", " ": " ", "!": "", "log": "log", "exp": "exp",
    "ln": "ln", "max": "max", "min": "min", "sin": "sin", "cos": "cos", "det": "det",
}
DROPPED = {"left", "right", "big", "Big", "bigg", "Bigg", "displaystyle", "textstyle", "limits"}
WRAPPERS = {
    "mathrm", "operatorname", "text", "textrm", "textit", "mathbf", "boldsymbol", "bm",
    "mathbb", "mathcal", "mathit", "mathsf", "mathtt", "textbf", "emph",
}
ACCENTS = {"hat": "̂", "widehat": "̂", "bar": "̄", "overline": "̄",
           "tilde": "̃", "widetilde": "̃", "dot": "̇"}
SUB = dict(zip("0123456789+-=()aehijklmnoprstuvx", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ"))
SUP = dict(zip("0123456789+-=()abcdefghijklmnoprstuvwxyzT", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᵀ"))
SUP["*"] = "*"
SUP["′"] = "′"


class Hard(Exception):
    """Maths with no faithful plain-text form."""


# Marks the end of an operator name such as Var or log: a space follows it
# when a letter or digit comes next, as in Var X, but not before a bracket.
WORD = "\x01"
TOKEN = re.compile(r"\\[A-Za-z]+|\\.|[{}^_]|[^\\{}^_]")


def latex_to_text(source: str) -> str:
    """Plain text for simple inline maths. Raise Hard for anything else."""
    tokens = TOKEN.findall(source.replace("\n", " "))
    out, rest = _sequence(tokens, 0, closing=False)
    if rest != len(tokens):
        raise Hard(source)
    text = re.sub(WORD + r"(?=\w)", " ", out).replace(WORD, "")
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        raise Hard(source)
    return text


def _sequence(tokens: list[str], i: int, closing: bool) -> tuple[str, int]:
    parts: list[str] = []
    while i < len(tokens):
        tok = tokens[i]
        if tok == "}":
            if closing:
                return "".join(parts), i + 1
            raise Hard("unbalanced")
        if tok in "^_":
            if not parts:
                raise Hard("script without base")
            body, i = _argument(tokens, i + 1)
            table = SUP if tok == "^" else SUB
            if tok == "^" and body in ("\\prime", "'"):
                parts.append("′")
                continue
            if not body or any(ch not in table for ch in body):
                raise Hard(f"script {body!r}")
            parts.append("".join(table[ch] for ch in body))
            continue
        text, i = _atom(tokens, i)
        parts.append(text)
    if closing:
        raise Hard("unclosed group")
    return "".join(parts), i


def _argument(tokens: list[str], i: int) -> tuple[str, int]:
    """One argument: a braced group or a single atom."""
    if i >= len(tokens):
        raise Hard("missing argument")
    if tokens[i] == "{":
        return _sequence(tokens, i + 1, closing=True)
    return _atom(tokens, i)


def _atom(tokens: list[str], i: int) -> tuple[str, int]:
    tok = tokens[i]
    if tok == "{":
        return _sequence(tokens, i + 1, closing=True)
    if not tok.startswith("\\"):
        if tok in "&$#~":
            raise Hard(tok)
        return ("" if tok.isspace() else tok), i + 1
    name = tok[1:]
    if name in GREEK:
        return GREEK[name], i + 1
    if name in SYMBOLS:
        symbol = SYMBOLS[name]
        return (symbol + WORD if symbol.isalpha() and len(symbol) > 1 else symbol), i + 1
    if name in DROPPED:
        return "", i + 1
    if name == "prime":
        return "′", i + 1
    if name in WRAPPERS:
        body, j = _argument(tokens, i + 1)
        return (body + WORD if body.isalpha() and len(body) > 1 else body), j
    if name in ACCENTS:
        body, j = _argument(tokens, i + 1)
        if len(body) != 1:
            raise Hard(f"accent over {body!r}")
        return body + ACCENTS[name], j
    if name in ("frac", "dfrac", "tfrac"):
        top, j = _argument(tokens, i + 1)
        bottom, j = _argument(tokens, j)
        wrap = lambda s: s if re.fullmatch(r"[\w.′]+", s) else f"({s})"  # noqa: E731
        return f"{wrap(top)}/{wrap(bottom)}", j
    if name == "sqrt":
        body, j = _argument(tokens, i + 1)
        return ("√" + body) if re.fullmatch(r"[\w.]+", body) else f"√({body})", j
    raise Hard(name)


# ---------------------------------------------------------------- reading pages

SKIP_TAGS = {"script", "style", "nav", "table", "figure", "pre", "button", "svg", "img", "details", "header", "form"}
SKIP_CLASSES = {
    "hatnote", "infobox", "mainarticle", "callout", "level", "qnav", "qpos", "pager",
    "proof-title", "theorem-title", "quarto-appendix", "portal-box", "ask-statwiki",
    "sourceCode", "cell-output", "code-copy-button", "lab-root",
}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
HARD = "\x00"


class Opening(HTMLParser):
    """The paragraphs of a page's main text, in order, with maths marked."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_main = False
        self.depth = 0  # elements open inside <main>
        self.skip_at: int | None = None
        self.math_at: int | None = None
        self.math_display = False
        self.math: list[str] = []
        self.p_at: int | None = None
        self.p: list[str] = []
        self.paragraphs: list[str] = []
        self.hatnote: str | None = None
        self.hat: list[str] | None = None

    def handle_starttag(self, tag, attrs):
        if tag == "main" and not self.in_main:
            self.in_main = True
            self.depth = 0
            return
        if not self.in_main or tag in VOID:
            return
        self.depth += 1
        if self.skip_at is not None:
            return
        classes = set((dict(attrs).get("class") or "").split())
        if tag in SKIP_TAGS or classes & SKIP_CLASSES:
            self.skip_at = self.depth
            if "hatnote" in classes and self.hatnote is None:
                self.hat = []
            return
        if tag == "span" and "math" in classes:
            self.math_at = self.depth
            self.math_display = "display" in classes
            self.math = []
            return
        if tag in ("p", "li") and self.p_at is None:
            self.p_at = self.depth
            self.p = []

    def handle_endtag(self, tag):
        if not self.in_main or tag in VOID:
            return
        if tag == "main" and self.depth == 0:
            self.in_main = False
            return
        if self.skip_at is not None and self.depth == self.skip_at:
            self.skip_at = None
            if self.hat is not None:
                self.hatnote = re.sub(r"\s+", " ", "".join(self.hat)).strip()
                self.hat = None
        elif self.math_at is not None and self.depth == self.math_at:
            self.math_at = None
            if self.p_at is not None:
                if self.math_display:
                    self.p.append(HARD)
                else:
                    try:
                        self.p.append(latex_to_text("".join(self.math)))
                    except Hard:
                        self.p.append(HARD)
        elif self.p_at is not None and self.depth == self.p_at:
            self.p_at = None
            self.paragraphs.append("".join(self.p))
        self.depth -= 1

    def handle_data(self, data):
        if self.hat is not None:
            self.hat.append(data)
        if not self.in_main or self.skip_at is not None:
            return
        if self.math_at is not None:
            self.math.append(data)
        elif self.p_at is not None:
            self.p.append(data)


LABEL = re.compile(r"^(?:Description|Summary|Definition|Example|Remark|Note)\s*\d*\.\s+")
MARKS = re.compile(r"\[\s*\d+\s*marks?\s*\]", re.I)
SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9(“\"‘'θμσλπαβγ])")
SKIP_PARAGRAPH = re.compile(r"^(What you need first|Size of this preview|Topic:|Part of )")


def clean(paragraph: str) -> str:
    text = MARKS.sub(" ", paragraph)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+([,.;:!?)])", r"\1", text)
    text = re.sub(r"([(])\s+", r"\1", text)
    return LABEL.sub("", text)


def shorten(sentence: str, limit: int = LIMIT) -> str:
    cut = sentence[: limit - 1]
    cut = cut[: cut.rfind(" ")] if " " in cut else cut
    return cut.rstrip(" ,;:–-") + "…"


TERMINAL = re.compile(r"[.!?…][\"”’)\]]*$")


def opening_description(paragraphs: list[str]) -> str | None:
    """The page's first sentences, up to LIMIT characters, or None.

    The description ends at the first displayed formula, the first sentence
    with maths that has no plain-text form, and the first sentence that does
    not end like one (a lead-in such as "They fit:" introduces a formula).
    """
    chosen: list[str] = []
    for raw in paragraphs:
        text = clean(raw)
        if len(text.replace(HARD, "")) < 25:
            if HARD in text:
                return finish(chosen)
            continue
        if SKIP_PARAGRAPH.match(text):
            continue
        for sentence in SENTENCE_END.split(text):
            if HARD in sentence or BANNED.search(sentence) or not TERMINAL.search(sentence):
                return finish(chosen)
            joined = " ".join(chosen + [sentence])
            if len(joined) > LIMIT:
                so_far = len(" ".join(chosen))
                if so_far < SHORTEST:
                    room = LIMIT - so_far - (1 if chosen else 0)
                    return finish(chosen + [shorten(sentence, room)])
                return finish(chosen)
            chosen.append(sentence)
        # Carry on into the next paragraph only while the text is short.
        if len(" ".join(chosen)) >= 90:
            break
    return finish(chosen)


def finish(sentences: list[str]) -> str | None:
    text = " ".join(sentences).strip()
    return text if len(text) >= SHORTEST else None


def title_of(text: str) -> str:
    match = re.search(r"<title>(.*?)</title>", text, re.S)
    title = html.unescape(match.group(1)).strip() if match else ""
    return title.removesuffix(f" – {SITE_NAME}").strip()


HATNOTE = re.compile(
    r"^(?P<kind>[A-Z][a-z]+)(?: taught in| of) (?P<chapter>.+?), part of (?P<part>[^·]+?)\s*(?:·|$)")
QUESTION_HATNOTE = re.compile(r"^(?P<level>Beginner|Intermediate|Advanced)?\s*Topic: (?P<topic>.+?)\s*·")


def fallback(rel: str, title: str, hatnote: str | None = None) -> str:
    """A sentence made from the title, for a page with no usable opening."""
    match = HATNOTE.match(hatnote or "")
    if rel.startswith("articles/") and match:
        kind = match["kind"].lower()
        place = "from" if kind != "topic" else "in"
        article = "an" if kind[0] in "aeiou" else "a"
        part = "" if match["part"] == match["chapter"] else f", in {match['part']}"
        long = f"{title}: {article} {kind} {place} {match['chapter']}{part}, with the questions that use it, on {SITE_NAME}."
        if len(long) <= LIMIT:
            return long
        return f"{title}: {article} {kind} {place} {match['chapter']}, on {SITE_NAME}."
    if rel.startswith("notes/"):
        return f"{title}: chapter notes with definitions, worked examples and practice questions on {SITE_NAME}."
    if rel.startswith("articles/"):
        return f"{title}: what it means, the chapter that teaches it, and the questions that use it, on {SITE_NAME}."
    question = QUESTION_HATNOTE.match(hatnote or "")
    if rel.startswith("questions/") and question:
        level = f"{question['level']} practice" if question["level"] else "Practice"
        base = f"{level} question on {question['topic']}: {title}."
        for ending in (f" Try it, then open the worked answer on {SITE_NAME}.", " Try it, then open the worked answer.", ""):
            if len(base + ending) <= LIMIT:
                return base + ending
    if rel.startswith("questions/"):
        return f"Practice question on {SITE_NAME}: {title}. Try it, then open the worked answer."
    if rel.startswith("files/"):
        return f"{title}: a figure from {SITE_NAME}, with its description, downloads and the pages that use it."
    return f"{title} on {SITE_NAME}, a statistics study wiki of chapters, topic pages and practice questions."


def existing_description(text: str) -> str | None:
    match = re.search(r'<meta name="description" content="([^"]*)">', text)
    return html.unescape(match.group(1)) if match else None


# ---------------------------------------------------------------- writing pages

def set_meta(text: str, pattern: str, tag: str, after: str) -> str:
    if re.search(pattern, text):
        return re.sub(pattern, lambda _: tag, text, count=1)
    match = re.search(after, text)
    if not match:
        raise SystemExit(f"Nowhere to put {tag[:40]}")
    return text[: match.end()] + "\n" + tag + text[match.end():]


def with_description(text: str, description: str) -> str:
    value = html.escape(description, quote=True)
    text = set_meta(text, r'<meta name="description" content="[^"]*">',
                    f'<meta name="description" content="{value}">', r"</title>")
    for key, attr in (("og:description", "property"), ("twitter:description", "name")):
        text = set_meta(text, rf'<meta {attr}="{key}" content="[^"]*">',
                        f'<meta {attr}="{key}" content="{value}">', r"</title>")
    return text


def website_data() -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE_NAME,
        "alternateName": ALTERNATE_NAMES,
        "url": SITE,
        "description": DESCRIPTION,
        "inLanguage": "en",
    }
    body = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    return f'<script type="application/ld+json" id="website-data">\n{body}\n</script>'


def home_page(text: str) -> str:
    text = re.sub(r"<title>.*?</title>", f"<title>{html.escape(HOME_TITLE)}</title>", text, count=1, flags=re.S)
    text = with_description(text, DESCRIPTION)
    text = re.sub(r'\n?<script type="application/ld\+json" id="website-data">.*?</script>', "", text, flags=re.S)
    return text.replace("</head>", website_data() + "\n</head>", 1)


def fix_sitemap(site_dir: Path) -> None:
    path = site_dir / "sitemap.xml"
    if not path.is_file():
        raise SystemExit("Missing sitemap.xml")
    text = path.read_text(encoding="utf-8")
    text = text.replace(f"<loc>{SITE}index.html</loc>", f"<loc>{SITE}</loc>")
    if f"<loc>{SITE}</loc>" not in text:
        raise SystemExit("sitemap.xml does not list the home page")
    path.write_text(text, encoding="utf-8")


def describe(rel: str, text: str) -> str:
    """The description a page should carry."""
    if rel == "search.html":
        return f"Search {SITE_NAME}: every chapter, topic page and practice question, ranked by how well each matches."
    parser = Opening()
    parser.feed(text)
    found = opening_description(parser.paragraphs)
    return found or fallback(rel, title_of(text), parser.hatnote)


def main(site_dir: Path = SITE_DIR) -> None:
    if not site_dir.is_dir():
        raise SystemExit(f"Missing site: {site_dir}")
    pages = [p for p in sorted(site_dir.rglob("*.html")) if "site_libs" not in p.parts]
    texts: dict[Path, str] = {}
    chosen: dict[Path, str] = {}
    own: dict[str, int] = {}
    for path in pages:
        text = path.read_text(encoding="utf-8")
        if "<title>Redirect</title>" in text and "var redirects" in text:
            continue
        texts[path] = text
        mine = existing_description(text)
        if mine:
            own[mine] = own.get(mine, 0) + 1
    for path, text in texts.items():
        rel = path.relative_to(site_dir).as_posix()
        if rel == "index.html":
            continue
        mine = existing_description(text)
        # Keep a written description when it is specific to this page.
        if mine and own[mine] == 1 and len(mine) >= SHORTEST and not BANNED.search(mine) and mine != DESCRIPTION:
            chosen[path] = mine
        else:
            chosen[path] = describe(rel, text)

    seen: dict[str, list[Path]] = {}
    for path, description in chosen.items():
        seen.setdefault(description, []).append(path)
    for description, paths in seen.items():
        if len(paths) > 1:
            for path in paths:
                title = title_of(texts[path])
                chosen[path] = f"{title}: {description}" if len(title) + len(description) + 2 <= LIMIT else fallback(
                    path.relative_to(site_dir).as_posix(), title)
    repeats = [d for d, n in _counts(chosen.values()).items() if n > 1]
    if repeats:
        # Worth fixing in the pages, but not worth stopping a publish for.
        print(f"Warning: {len(repeats)} descriptions are shared by more than one page, e.g. {repeats[0]!r}")

    for path, text in texts.items():
        if path == site_dir / "index.html":
            updated = home_page(text)
        else:
            updated = with_description(text, chosen[path])
        if updated != text:
            path.write_text(updated, encoding="utf-8")
    fix_sitemap(site_dir)
    print(f"Descriptions on {len(chosen) + 1} pages")


def _counts(values) -> dict[str, int]:
    counts: dict[str, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


if __name__ == "__main__":
    sys.exit(main() or 0)
