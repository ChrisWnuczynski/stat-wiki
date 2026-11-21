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
  and the alternatives to use if that name is taken. That block stays on
  the home page only.
- An article page gets Article structured data (headline, description,
  url, language, and the site it belongs to). When its topic hub is known
  it also gets a breadcrumb: Home, that hub, then the page.
- sitemap.xml lists each directory index at its canonical /path/ URL,
  including the home page, never as index.html. The same trailing-slash
  form is written into every rel=canonical and og:url. It leaves out the
  search shell, the random-question page, and the article redirect stubs.
  It does not send lastmod: a build-time stamp changes on every publish,
  and Google ignores lastmod it cannot trust.
- Any fonts.googleapis.com import left in the built Bootstrap CSS is removed.
  The theme already sets $web-font-path to false; the strip is what the
  rendered files are checked against.

Google ignores a description repeated on many pages. Two pages that end up
with the same one get their titles put in front; any still shared are
reported, without stopping the build.
"""

from __future__ import annotations

import html
import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

import topic_hubs

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
    text = re.sub(
        r'\n?<script type="application/ld\+json" id="(?:website-data|article-data)">.*?</script>',
        "",
        text,
        flags=re.S,
    )
    return text.replace("</head>", website_data() + "\n</head>", 1)


# Utility pages. They stay on the site; they are not landing pages.
SITEMAP_OMIT = (f"{SITE}search.html", f"{SITE}questions/random.html")
_URL_BLOCK = re.compile(r"[ \t]*<url\b[^>]*>.*?</url>[ \t]*\r?\n?", re.S)
_LASTMOD = re.compile(r"\r?\n[ \t]*<lastmod>[^<]*</lastmod>")


def is_index_html_url(url: str) -> bool:
    """True when the URL path is a directory index file, not a page named index."""
    return urlsplit(url).path.endswith("/index.html")


def directory_url(url: str) -> str:
    """The trailing-slash form of a directory index, including the site root.

    ``/notes/index.html`` becomes ``/notes/`` and ``/index.html`` becomes ``/``.
    A page such as ``/articles/gini-index.html`` is left as it is.
    """
    parts = urlsplit(url)
    path = parts.path
    if path.endswith("/index.html"):
        path = path[: -len("index.html")]
    if path == "":
        path = "/"
    return urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))


def canonical_sitemap_loc(url: str) -> str:
    """Directory indexes use the same /path/ form as the page's canonical link."""
    return directory_url(url)


_CANONICAL_OR_OG = re.compile(r"<(?:link|meta)\b[^>]*>", re.I)
_URL_ATTR = re.compile(r"""((?:href|content)\s*=\s*(["']))(.*?)(\2)""", re.I)


def rewrite_directory_urls(text: str) -> str:
    """Point rel=canonical and og:url at /path/ rather than /path/index.html."""

    def tag(match: re.Match) -> str:
        block = match.group(0)
        lowered = block.lower()
        if not (
            (lowered.startswith("<link") and "canonical" in lowered)
            or (lowered.startswith("<meta") and "og:url" in lowered)
        ):
            return block

        def attr(found: re.Match) -> str:
            return found.group(1) + directory_url(found.group(3)) + found.group(4)

        return _URL_ATTR.sub(attr, block, count=1)

    return _CANONICAL_OR_OG.sub(tag, text)


def is_redirect_stub(text: str) -> bool:
    return "<title>Redirect</title>" in text and "var redirects" in text


def redirect_stub_locs(site_dir: Path) -> set[str]:
    """Public URLs of HTTP 200 redirect stubs. They must not be in the sitemap."""
    found: set[str] = set()
    if not site_dir.is_dir():
        return found
    for path in site_dir.rglob("*.html"):
        if "site_libs" in path.parts:
            continue
        head = path.read_text(encoding="utf-8", errors="replace")[:1500]
        if is_redirect_stub(head):
            found.add(SITE + path.relative_to(site_dir).as_posix())
    return found


def fix_sitemap_text(text: str, extra_omit: set[str] | None = None) -> str:
    """Canonical index URLs, no utility pages, no redirect stubs, and no build-time lastmod."""
    omit = set(SITEMAP_OMIT)
    if extra_omit:
        omit.update(extra_omit)

    def rewrite(match: re.Match) -> str:
        block = match.group(0)
        found = re.search(r"<loc>([^<]*)</loc>", block)
        if not found:
            return block
        url = found.group(1).strip()
        if url in omit or directory_url(url) in omit:
            return ""
        url = directory_url(url)
        block = block[: found.start(1)] + url + block[found.end(1) :]
        return _LASTMOD.sub("", block)

    return _URL_BLOCK.sub(rewrite, text)


def fix_sitemap(site_dir: Path) -> None:
    path = site_dir / "sitemap.xml"
    if not path.is_file():
        raise SystemExit("Missing sitemap.xml")
    text = path.read_text(encoding="utf-8")
    updated = fix_sitemap_text(text, redirect_stub_locs(site_dir))
    if f"<loc>{SITE}</loc>" not in updated:
        raise SystemExit("sitemap.xml does not list the home page")
    if is_index_html_url(SITE) or any(is_index_html_url(loc) for loc in re.findall(r"<loc>([^<]*)</loc>", updated)):
        raise SystemExit("sitemap.xml still lists an index.html URL")
    if updated != text:
        path.write_text(updated, encoding="utf-8")


GOOGLE_FONT_IMPORT = re.compile(
    r"@import\s*(?:url\(\s*)?[\"']?https://fonts\.googleapis\.com[^\"');\s]*[\"']?\s*\)?\s*;",
    re.IGNORECASE,
)


def strip_google_font_imports(css: str) -> str:
    """Drop a render-blocking Google Fonts import from one stylesheet."""
    return GOOGLE_FONT_IMPORT.sub("", css)


def strip_built_google_fonts(site_dir: Path) -> int:
    """Remove fonts.googleapis.com imports from the built Bootstrap CSS. Return how many files changed."""
    bootstrap = site_dir / "site_libs" / "bootstrap"
    if not bootstrap.is_dir():
        return 0
    changed = 0
    for path in sorted(bootstrap.glob("*.css")):
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        updated = strip_google_font_imports(text)
        if updated != text:
            path.write_bytes(updated.encode("utf-8"))
            changed += 1
    return changed


def _slug(text: str) -> str:
    text = "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


_DIST_SLUGS: set[str] | None = None


def _distribution_slugs() -> set[str]:
    global _DIST_SLUGS
    if _DIST_SLUGS is None:
        raw = json.loads((ROOT / "distributions.json").read_text(encoding="utf-8"))
        slugs = set(topic_hubs.distribution_page_slugs(list(raw)))
        slugs.update(topic_hubs.DISTRIBUTION_RELATIONS)
        _DIST_SLUGS = slugs
    return _DIST_SLUGS


def _hub_for_topic(topic: str) -> tuple[str, str]:
    if topic == "Fundamentals":
        return "Fundamentals", f"{SITE}notes/fundamentals.html"
    if topic == "Probability distributions":
        return "Probability distributions", f"{SITE}notes/probability-distributions.html"
    if topic == "Applications":
        return "Applications", f"{SITE}notes/applications.html"
    if topic == "History":
        return "History", f"{SITE}history.html"
    return topic, f"{SITE}notes/#{_slug(topic)}"


def curated_hub(slug: str) -> tuple[str, str] | None:
    """The topic hub that lists this article, when the article belongs to one."""
    if slug in topic_hubs.FUNDAMENTALS_ORDER:
        return _hub_for_topic("Fundamentals")
    if slug in _distribution_slugs():
        return _hub_for_topic("Probability distributions")
    for row in topic_hubs.STANDALONE:
        if row["slug"] == slug:
            return _hub_for_topic(row.get("topic", "Fundamentals"))
    return None


_CATEGORY_LINK = re.compile(
    r'<div class="wiki-categories"[^>]*>\s*<span class="cat-label">Categories:</span>\s*'
    r'<a href="([^"]+)">([^<]*)</a>',
    re.S,
)
_CANONICAL = re.compile(r'<link rel="canonical" href="([^"]+)">')


def absolute_page_url(page_url: str, href: str) -> str:
    """Resolve a page-relative link and use the directory form of an index URL."""
    joined = urljoin(page_url, html.unescape(href))
    parts = urlsplit(joined)
    path = parts.path
    if path.endswith("/index.html"):
        path = path[: -len("index.html")]
    return urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))


def topic_crumb(rel: str, text: str, page_url: str) -> tuple[str, str] | None:
    """Home's child in the breadcrumb: the topic hub, when this page has one."""
    if not rel.startswith("articles/") or not rel.endswith(".html"):
        return None
    slug = rel[len("articles/") : -len(".html")]
    hub = curated_hub(slug)
    if hub is None:
        match = _CATEGORY_LINK.search(text)
        if not match:
            return None
        href, name = match.group(1), html.unescape(match.group(2)).strip()
        if not href or not name:
            return None
        hub = (name, absolute_page_url(page_url, href))
    name, url = hub
    if url.split("#", 1)[0].rstrip("/") == page_url.split("#", 1)[0].rstrip("/"):
        return None
    return name, url


def _json_ld(data: dict) -> str:
    body = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    return f'<script type="application/ld+json" id="article-data">\n{body}\n</script>'


def article_data(headline: str, description: str, url: str, crumb: tuple[str, str] | None) -> str:
    """Article JSON-LD, plus a breadcrumb when the topic hub is known.

    isPartOf names the site. It is not a second copy of the home page's
    WebSite block, and this script is not given the website-data id.
    """
    article = {
        "@type": "Article",
        "headline": headline,
        "description": description,
        "url": url,
        "inLanguage": "en",
        "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": SITE},
    }
    if crumb is None:
        return _json_ld({"@context": "https://schema.org", **article})
    hub_name, hub_url = crumb
    return _json_ld(
        {
            "@context": "https://schema.org",
            "@graph": [
                article,
                {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
                        {"@type": "ListItem", "position": 2, "name": hub_name, "item": hub_url},
                        {"@type": "ListItem", "position": 3, "name": headline, "item": url},
                    ],
                },
            ],
        }
    )


def with_article_data(text: str, rel: str, description: str) -> str:
    text = re.sub(
        r'\n?<script type="application/ld\+json" id="(?:article-data|website-data)">.*?</script>',
        "",
        text,
        flags=re.S,
    )
    found = _CANONICAL.search(text)
    url = found.group(1) if found else SITE + rel
    script = article_data(title_of(text), description, url, topic_crumb(rel, text, url))
    return text.replace("</head>", script + "\n</head>", 1)


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
        raw = path.read_text(encoding="utf-8")
        text = rewrite_directory_urls(raw)
        if is_redirect_stub(text):
            if text != raw:
                path.write_text(text, encoding="utf-8")
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
        rel = path.relative_to(site_dir).as_posix()
        if path == site_dir / "index.html":
            updated = home_page(text)
        else:
            updated = with_description(text, chosen[path])
            if rel.startswith("articles/") and rel.endswith(".html"):
                updated = with_article_data(updated, rel, chosen[path])
        if updated != text:
            path.write_text(updated, encoding="utf-8")
    fix_sitemap(site_dir)
    stripped = strip_built_google_fonts(site_dir)
    if stripped:
        print(f"Removed a Google Fonts import from {stripped} stylesheet(s)")
    print(f"Descriptions on {len(chosen) + 1} pages")


def _counts(values) -> dict[str, int]:
    counts: dict[str, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


if __name__ == "__main__":
    sys.exit(main() or 0)
