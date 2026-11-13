// Ranking, unified normalisation, conversational/comparison query parsing,
// disambiguation resolution, and live Quarto autocomplete integration for StatWiki.

const SYNONYM_GROUPS = [
  ["mean", "average", "sample mean"],
  ["standard deviation", "sample standard deviation", "sd"],
  ["standard error", "se"],
  ["confidence interval", "ci"],
  ["random variable", "rv"],
  ["degrees of freedom", "df"],
];

const BOILERPLATE_SECTIONS = new Set([
  "used in",
  "see also",
  "what links here",
  "exercises",
  "questions on this topic",
  "questions",
  "figures",
  "file usage",
  "download",
  "summary",
  "references",
]);

const STOP_WORDS = new Set([
  "the",
  "a",
  "an",
  "of",
  "in",
  "for",
  "and",
  "on",
  "to",
  "with",
  "by",
  "as",
  "is",
  "are",
  "was",
  "were",
  "be",
  "been",
  "being",
  "do",
  "does",
  "did",
  "can",
  "should",
  "would",
  "could",
  "i",
  "we",
  "you",
  "it",
  "its",
  "this",
  "that",
  "these",
  "those",
  "my",
  "our",
  "from",
  "at",
  "into",
  "about",
]);

// Statistical single-letter and short tokens that must never be dropped even
// when they are 1 or 2 characters long.
const STAT_SHORT_TOKENS = new Set([
  "t",
  "z",
  "f",
  "p",
  "r",
  "k",
  "n",
  "q",
  "x",
  "y",
  "sd",
  "se",
  "ci",
  "pi",
  "cv",
  "df",
  "rv",
  "bf",
  "kl",
  "em",
  "ar",
  "ma",
  "qq",
  "ks",
  "bh",
  "gd",
  "nn",
  "cf",
  "r2",
  "t2",
  "l1",
  "l2",
]);

const GREEK_WORDS = [
  [/σ/g, "sigma"],
  [/α/g, "alpha"],
  [/β/g, "beta"],
  [/γ/g, "gamma"],
  [/δ/g, "delta"],
  [/ε/g, "epsilon"],
  [/θ/g, "theta"],
  [/λ/g, "lambda"],
  [/μ/g, "mu"],
  [/π/g, "pi"],
  [/ρ/g, "rho"],
  [/τ/g, "tau"],
  [/φ/g, "phi"],
  [/χ/g, "chi"],
  [/ω/g, "omega"],
];

function fold(value) {
  let s = String(value || "")
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[’‘`´]/g, "'")
    .replace(/[–—−]/g, "-")
    .replace(/²/g, "2")
    .replace(/³/g, "3")
    .replace(/∞/g, "infinity")
    .toLowerCase();
  for (const [rx, word] of GREEK_WORDS) {
    s = s.replace(rx, word);
  }
  s = s.replace(/\^([0-9]+)\b/g, "$1");
  return s.replace(/\s+/g, " ").trim();
}

export function slugKey(value) {
  return fold(value)
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

const EPONYM_STEMS = [
  "akaike",
  "basu",
  "chebyshev",
  "cramer",
  "fatou",
  "fisher",
  "frechet",
  "fubini",
  "gambler",
  "gumbel",
  "holder",
  "hotelling",
  "ito",
  "jensen",
  "kolmogorov",
  "laplace",
  "levy",
  "little",
  "lloyd",
  "markov",
  "mercer",
  "newton",
  "neyman",
  "pearson",
  "renyi",
  "simpson",
  "slutsky",
  "spearman",
  "stirling",
  "student",
  "sylvester",
  "tukey",
  "vapnik",
  "wald",
  "ward",
  "welch",
  "wilcoxon",
  "wilk",
  "wold",
];
const EPONYM_PLURAL_RE = new RegExp("\\b(" + EPONYM_STEMS.join("|") + ")s\\b", "g");

// Canonical search key shared identically by build_wiki.py and search-rank.js:
// folds diacritics, strips English possessives ('s, trailing s', and unapostrophised
// eponymous -s like "Students t" / "Jensens inequality"), collapses dotted initialisms
// (i.i.d. -> iid, s.d. -> sd), and treats hyphens, slashes, and punctuation equivalently.
export function canonicalSearchKey(value) {
  let s = fold(value);
  if (!s) return "";
  // Collapse dotted initialisms such as i.i.d., s.d., s.e., r.v., q.q.
  s = s.replace(/\b(?:[a-z]\.){2,}[a-z]?(?=\W|$)/g, (m) => m.replace(/\./g, ""));
  // Strip possessives: Student's -> student, Bayes' -> bayes, Wilks's -> wilks
  s = s.replace(/([a-z])'s\b/g, "$1");
  s = s.replace(/([s])'(?=\W|$)/g, "$1");
  // Normalize unapostrophised eponymous possessives (Students -> student, Wilks -> wilk, Cramers -> cramer)
  s = s.replace(EPONYM_PLURAL_RE, "$1");
  return s
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function bareKey(value) {
  return canonicalSearchKey(value).replace(/^(?:the|a|an)-/, "");
}

function compactKey(value) {
  return bareKey(value).replace(/-/g, "");
}

function singularKey(key) {
  if (!key || key.length <= 3) return key;
  if (key.endsWith("ies") && key.length > 4) return key.slice(0, -3) + "y";
  if (key.endsWith("ses") || key.endsWith("xes") || key.endsWith("zes")) return key.slice(0, -2);
  if (
    key.endsWith("s") &&
    !key.endsWith("ss") &&
    !key.endsWith("us") &&
    !key.endsWith("is") &&
    !key.endsWith("os") &&
    !key.endsWith("means") &&
    !key.endsWith("series") &&
    !key.endsWith("bayes") &&
    !key.endsWith("wilks")
  ) {
    return key.slice(0, -1);
  }
  return key;
}

// Conversational / interrogative framing patterns stripped iteratively from the
// start of natural-language queries while preserving statistical tokens.
const LEADING_CONVERSATIONAL = [
  /^(?:please\s+|can\s+you\s+|could\s+you\s+|help\s+me\s+)/,
  /^(?:what\s+(?:is|are|does|do)\s+(?:the\s+|a\s+|an\s+)?)/,
  /^(?:how\s+to\s+(?:compute|calculate|find|estimate|interpret|do|run|perform|use|check|test(?:\s+for)?)\s+(?:the\s+|a\s+|an\s+)?)/,
  /^(?:how\s+(?:do|can|should)\s+(?:i|we|you)\s+(?:compute|calculate|find|estimate|interpret|do|run|perform|use|check|test(?:\s+for)?)\s+(?:the\s+|a\s+|an\s+)?)/,
  /^(?:how\s+(?:is|are|does|do)\s+(?:the\s+|a\s+|an\s+)?)/,
  /^(?:how\s+to\s+)/,
  /^(?:when\s+(?:to|should\s+(?:i|we|you)|do\s+(?:i|we|you))\s+use\s+(?:the\s+|a\s+|an\s+)?)/,
  /^(?:when\s+is\s+(?:the\s+|a\s+|an\s+)?)/,
  /^(?:why\s+(?:do\s+(?:we|i|you)\s+)?use\s+(?:the\s+|a\s+|an\s+)?)/,
  /^(?:why\s+(?:is|are|does|do)\s+(?:the\s+|a\s+|an\s+)?)/,
  /^(?:(?:the\s+)?(?:definition|meaning|formula|equation|intuition|derivation|example|examples|properties|summary|overview|explanation)\s+(?:of|for)\s+(?:the\s+|a\s+|an\s+)?)/,
  /^(?:(?:define|explain|compute|calculate|derive|describe|show\s+me)\s+(?:what\s+(?:is|are)\s+)?(?:the\s+|a\s+|an\s+)?)/,
];

const TRAILING_CONVERSATIONAL = [
  /\s+(?:mean|means|work|works|tell\s+us|measure|measures|used\s+for)$/,
  /\s+in\s+(?:statistics|probability|statwiki|data\s+analysis)$/,
];

function stripArticles(text) {
  return String(text || "")
    .trim()
    .replace(/^(?:the|a|an)\s+(?=\S)/i, "")
    .trim();
}

const COMPARISON_PATTERNS = [
  /^(?:what\s+is\s+)?(?:the\s+)?difference(?:s)?\s+between\s+(.+?)\s+and\s+(.+)$/i,
  /^(?:compare|comparing|comparison\s+of)\s+(.+?)\s+(?:and|vs\.?|versus|with|to)\s+(.+)$/i,
  /^(.+?)\s+(?:vs\.?|versus|compared\s+(?:with|to)|or)\s+(.+)$/i,
];

export function parseQuery(rawQuery) {
  const raw = String(rawQuery || "").trim();
  const cleanedPunct = fold(raw).replace(/[?!.;:,]+$/g, "").trim();
  if (!cleanedPunct) {
    return { raw, core: "", isConversational: false, comparison: null };
  }

  let working = cleanedPunct;
  let strippedLead = false;
  for (let pass = 0; pass < 3; pass += 1) {
    let changed = false;
    for (const rx of LEADING_CONVERSATIONAL) {
      const next = working.replace(rx, "").trim();
      if (next && next !== working) {
        working = next;
        strippedLead = true;
        changed = true;
      }
    }
    if (strippedLead) {
      for (const rx of TRAILING_CONVERSATIONAL) {
        const next = working.replace(rx, "").trim();
        if (next && next !== working) {
          working = next;
          changed = true;
        }
      }
    } else {
      // Even without a conversational prefix, strip trailing "in statistics"
      const nextIn = working.replace(TRAILING_CONVERSATIONAL[1], "").trim();
      if (nextIn && nextIn !== working) {
        working = nextIn;
        strippedLead = true;
        changed = true;
      }
    }
    if (!changed) break;
  }

  working = stripArticles(working) || cleanedPunct;

  // Detect comparison queries: "X vs Y", "difference between X and Y", etc.
  for (const rx of COMPARISON_PATTERNS) {
    const m = cleanedPunct.match(rx) || working.match(rx);
    if (m) {
      // Do not split intrinsic "X and Y" / "X or Y" titles when "or" matched unless it's "vs"/"difference between"
      const isOrRule = rx === COMPARISON_PATTERNS[2] && /\bor\b/.test(m[0]) && !/\b(?:vs\.?|versus|compared)\b/.test(m[0]);
      if (isOrRule) continue;
      const left = stripArticles(m[1].replace(/[?!.;:,]+$/g, ""));
      const right = stripArticles(m[2].replace(/[?!.;:,]+$/g, ""));
      if (left && right && canonicalSearchKey(left) !== canonicalSearchKey(right)) {
        return {
          raw,
          core: working,
          isConversational: true,
          comparison: [left, right],
        };
      }
    }
  }

  return {
    raw,
    core: working,
    isConversational: strippedLead || /[?]/.test(raw),
    comparison: null,
  };
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function hasTerm(text, term) {
  const hay = fold(text)
    .replace(/([a-z])'s\b/g, "$1")
    .replace(/([s])'(?=\W|$)/g, "$1")
    .replace(EPONYM_PLURAL_RE, "$1");
  const needle = fold(term)
    .replace(/([a-z])'s\b/g, "$1")
    .replace(/([s])'(?=\W|$)/g, "$1")
    .replace(EPONYM_PLURAL_RE, "$1");
  if (!needle) return false;
  const flexNeedle = escapeRegExp(needle).replace(/(?:\\-|\\\/| )+/g, "[-/ ]+");
  const pattern = new RegExp("(^|[^a-z0-9])" + flexNeedle + "([^a-z0-9]|$)");
  if (pattern.test(hay)) return true;
  if (!needle.includes(" ") && !needle.includes("-") && needle.length >= 4) {
    const dehyphenHay = hay.replace(/([a-z0-9])[-/]([a-z0-9])/g, "$1$2");
    const compactPattern = new RegExp("(^|[^a-z0-9])" + escapeRegExp(needle) + "([^a-z0-9]|$)");
    return compactPattern.test(dehyphenHay);
  }
  return false;
}

function queryTokens(query) {
  const tokens = canonicalSearchKey(query).split("-").filter(Boolean);
  const filtered = tokens.filter(
    (tok) => !STOP_WORDS.has(tok) && (tok.length >= 2 || STAT_SHORT_TOKENS.has(tok) || /^\d+$/.test(tok))
  );
  return filtered.length ? filtered : tokens;
}

export function canonicalHref(href) {
  return String(href || "").split("?")[0].split("#")[0];
}

function cleanHrefWithHash(href) {
  const raw = String(href || "");
  const [beforeHash, hash] = raw.split("#");
  const base = beforeHash.split("?")[0];
  return hash ? `${base}#${hash}` : base;
}

function pageKey(href) {
  return canonicalHref(href).replace(/^(?:\.\/|\.\.\/|\/)+/, "");
}

function stemOfHref(href) {
  const key = pageKey(href);
  const last = key.split("/").pop() || "";
  return last.replace(/\.html$/i, "");
}

export function expandedTerms(query) {
  const parsed = parseQuery(query);
  if (parsed.comparison) {
    const out = [];
    for (const side of parsed.comparison) {
      const f = fold(side);
      if (f && !out.includes(f)) out.push(f);
    }
    return out.length ? out : [fold(query)].filter(Boolean);
  }
  const q = fold(parsed.core || query);
  if (!q) return [];
  const cKey = canonicalSearchKey(q);
  for (const group of SYNONYM_GROUPS) {
    const hit = group.some((term) => {
      const tKey = canonicalSearchKey(term);
      return cKey === tKey || (term.includes(" ") && q.includes(fold(term)));
    });
    if (hit) {
      if (group.some((term) => canonicalSearchKey(term) === cKey)) {
        return group.slice();
      }
      return [q, ...group.filter((term) => fold(term) !== q)];
    }
  }
  return [q];
}

export function tierOf(href) {
  const path = pageKey(href);
  if (path.startsWith("files/") || path.includes("/files/")) return 3;
  if (path.startsWith("articles/") || path.includes("/articles/")) return 0;
  if (path.startsWith("notes/") || path.includes("/notes/") || path.startsWith("reference/")) return 1;
  return 2;
}

let cachedMetaRef = null;
let cachedNormalizedMeta = null;

function normalizeMeta(meta) {
  if (!meta || typeof meta !== "object") {
    return {
      pages: new Map(),
      aliasToTarget: new Map(),
      compactToTarget: new Map(),
      targetAliases: new Map(),
      disambigByKey: new Map(),
    };
  }
  if (meta === cachedMetaRef && cachedNormalizedMeta) {
    return cachedNormalizedMeta;
  }

  const pages = new Map();
  const aliasToTarget = new Map();
  const compactToTarget = new Map();
  const ambiguousCompact = new Set();
  const targetAliases = new Map();
  const disambigByKey = new Map();

  function recordKey(map, key, entry) {
    if (!key) return;
    if (!map.has(key)) {
      map.set(key, entry);
    }
  }

  function addAlias(label, rawHref) {
    const cleanTarget = cleanHrefWithHash(rawHref);
    const targetKey = pageKey(cleanTarget);
    const cleanLabel = String(label || "").trim();
    if (!targetKey || !cleanLabel) return;
    const sKey = slugKey(cleanLabel);
    const cSearchKey = canonicalSearchKey(cleanLabel);
    const bKey = bareKey(cleanLabel);
    const singKey = singularKey(bKey);
    const comp = compactKey(cleanLabel);
    if (!sKey && !cSearchKey) return;

    let list = targetAliases.get(targetKey);
    if (!list) {
      list = [];
      targetAliases.set(targetKey, list);
    }
    if (!list.some((existing) => fold(existing) === fold(cleanLabel))) {
      list.push(cleanLabel);
    }

    const entry = {
      targetKey,
      href: canonicalHref(cleanTarget),
      fullHref: cleanTarget,
      alias: cleanLabel,
    };
    for (const k of [sKey, cSearchKey, bKey, singKey]) {
      recordKey(aliasToTarget, k, entry);
    }
    if (comp.length >= 2) {
      const prev = compactToTarget.get(comp);
      if (prev && prev.targetKey !== targetKey) {
        ambiguousCompact.add(comp);
        compactToTarget.delete(comp);
      } else if (!prev && !ambiguousCompact.has(comp)) {
        compactToTarget.set(comp, entry);
      }
    }
  }

  if (meta.aliases && typeof meta.aliases === "object") {
    for (const [alias, target] of Object.entries(meta.aliases)) {
      if (typeof target === "string") {
        addAlias(alias, target);
      } else if (target && typeof target === "object" && target.href) {
        addAlias(target.label || alias, target.href);
      }
    }
  }

  if (meta.pages && typeof meta.pages === "object") {
    for (const [rawHref, info] of Object.entries(meta.pages)) {
      if (!info || typeof info !== "object") continue;
      const key = pageKey(info.href || rawHref);
      if (!key) continue;
      const href = canonicalHref(info.href || rawHref);
      const title = String(info.title || "").trim();
      pages.set(key, {
        key,
        href,
        title,
        kind: String(info.kind || ""),
        summary: String(info.summary || ""),
      });
      if (Array.isArray(info.aliases)) {
        for (const alias of info.aliases) addAlias(alias, href);
      }
    }
  }

  if (meta.disambiguations && typeof meta.disambiguations === "object") {
    for (const [rawKey, spec] of Object.entries(meta.disambiguations)) {
      if (!spec || typeof spec !== "object" || !Array.isArray(spec.options)) continue;
      const options = spec.options
        .filter((opt) => opt && opt.href)
        .map((opt) => {
          const cleanH = cleanHrefWithHash(opt.href);
          const baseK = pageKey(cleanH);
          const pageInfo = pages.get(baseK);
          return {
            href: cleanH.replace(/^\/+/, ""),
            baseHref: canonicalHref(cleanH).replace(/^\/+/, ""),
            pageKey: baseK,
            label: String(opt.label || (pageInfo && pageInfo.title) || cleanH),
            description: String(opt.description || (pageInfo && pageInfo.summary) || ""),
          };
        });
      if (options.length < 2) continue;
      const entry = {
        key: canonicalSearchKey(rawKey),
        term: String(spec.term || rawKey),
        options,
      };
      const keys = [
        rawKey,
        spec.term,
        ...(Array.isArray(spec.aliases) ? spec.aliases : []),
      ];
      for (const k of keys) {
        const ck = canonicalSearchKey(k);
        const bk = bareKey(k);
        const sk = singularKey(bk);
        const comp = compactKey(k);
        for (const variant of [slugKey(k), ck, bk, sk]) {
          if (variant && !disambigByKey.has(variant)) {
            disambigByKey.set(variant, entry);
          }
        }
        if (comp.length >= 2 && !disambigByKey.has(comp)) {
          disambigByKey.set(comp, entry);
        }
      }
    }
  }

  cachedMetaRef = meta;
  cachedNormalizedMeta = { pages, aliasToTarget, compactToTarget, targetAliases, disambigByKey };
  return cachedNormalizedMeta;
}

function titleWordsCount(title) {
  const words = canonicalSearchKey(title).split("-").filter(Boolean);
  return Math.max(1, words.length);
}

function queryKeys(query) {
  const qSlug = slugKey(query);
  const qCanon = canonicalSearchKey(query);
  const qBare = bareKey(query);
  const qSing = singularKey(qBare);
  const qCompact = compactKey(query);
  return { qSlug, qCanon, qBare, qSing, qCompact };
}

function exactTitleRank(title, keys) {
  if (!title || (!keys.qSlug && !keys.qCanon)) return 0;
  const tSlug = slugKey(title);
  const tCanon = canonicalSearchKey(title);
  const tBare = bareKey(title);
  const tSing = singularKey(tBare);
  const tCompact = compactKey(title);
  if (keys.qSlug && tSlug === keys.qSlug) return 3;
  if (keys.qCanon && tCanon === keys.qCanon) return 3;
  if (keys.qBare && (tBare === keys.qBare || tSing === keys.qSing)) return 2;
  if (keys.qCompact.length >= 3 && tCompact === keys.qCompact) return 2;
  return 0;
}

function lookupAliasMatch(normalizedMeta, keys) {
  if (!keys.qSlug && !keys.qCanon) return null;
  // Also strip trailing 's' on unapostrophised eponyms like "cramers" -> "cramer"
  const direct =
    normalizedMeta.aliasToTarget.get(keys.qSlug) ||
    normalizedMeta.aliasToTarget.get(keys.qCanon) ||
    (keys.qBare ? normalizedMeta.aliasToTarget.get(keys.qBare) : null) ||
    (keys.qSing ? normalizedMeta.aliasToTarget.get(keys.qSing) : null) ||
    (keys.qCompact.length >= 2 ? normalizedMeta.compactToTarget.get(keys.qCompact) : null);
  return direct || null;
}

export function resolveDisambiguation(query, meta = null) {
  const parsed = parseQuery(query);
  if (parsed.comparison) return null;
  const targetQuery = parsed.core || query;
  const keys = queryKeys(targetQuery);
  if (!keys.qCanon && !keys.qSlug) return null;
  const normalizedMeta = normalizeMeta(meta);
  const hit =
    normalizedMeta.disambigByKey.get(keys.qSlug) ||
    normalizedMeta.disambigByKey.get(keys.qCanon) ||
    normalizedMeta.disambigByKey.get(keys.qBare) ||
    normalizedMeta.disambigByKey.get(keys.qSing) ||
    (keys.qCompact.length >= 2 ? normalizedMeta.disambigByKey.get(keys.qCompact) : null);
  return hit || null;
}

function resolveSingleTarget(query, normalizedMeta, docs = null) {
  const keys = queryKeys(query);
  if (!keys.qSlug && !keys.qCanon) return null;

  const candidates = [];
  for (const page of normalizedMeta.pages.values()) {
    const tier = tierOf(page.href);
    if (tier === 3) continue;
    const rank = exactTitleRank(page.title, keys);
    if (rank > 0) {
      candidates.push({ href: page.href, title: page.title, tier, rank, matchedBy: "title", alias: "" });
    }
  }
  if (Array.isArray(docs)) {
    const seen = new Set(candidates.map((c) => pageKey(c.href)));
    for (const doc of docs) {
      const base = canonicalHref(doc && doc.href);
      const key = pageKey(base);
      const tier = tierOf(base);
      if (!key || tier === 3 || seen.has(key)) continue;
      const rank = exactTitleRank(doc.title, keys);
      if (rank > 0) {
        seen.add(key);
        candidates.push({ href: base, title: String(doc.title || base), tier, rank, matchedBy: "title", alias: "" });
      }
    }
  }
  if (candidates.length) {
    candidates.sort((a, b) => b.rank - a.rank || a.tier - b.tier || a.href.localeCompare(b.href));
    const best = candidates[0];
    return { href: best.href, title: best.title, matchedBy: best.matchedBy, alias: best.alias };
  }

  const aliasHit = lookupAliasMatch(normalizedMeta, keys);
  if (aliasHit && tierOf(aliasHit.href) < 3) {
    const pageInfo = normalizedMeta.pages.get(aliasHit.targetKey);
    let title = pageInfo ? pageInfo.title : "";
    if (!title && Array.isArray(docs)) {
      const foundDoc = docs.find((d) => pageKey(d && d.href) === aliasHit.targetKey);
      if (foundDoc) title = String(foundDoc.title || "");
    }
    return {
      href: cleanHrefWithHash(aliasHit.fullHref || aliasHit.href),
      title: title || aliasHit.href,
      matchedBy: "alias",
      alias: aliasHit.alias,
    };
  }

  const slugCandidates = [];
  for (const page of normalizedMeta.pages.values()) {
    const tier = tierOf(page.href);
    if (tier === 3) continue;
    const stem = stemOfHref(page.href);
    const stemCanon = canonicalSearchKey(stem);
    if (
      stem &&
      stem !== "index" &&
      (stem === keys.qSlug || stem === keys.qBare || stemCanon === keys.qCanon || stemCanon === keys.qSing)
    ) {
      slugCandidates.push({ href: page.href, title: page.title, tier });
    }
  }
  if (Array.isArray(docs)) {
    const seen = new Set(slugCandidates.map((c) => pageKey(c.href)));
    for (const doc of docs) {
      const base = canonicalHref(doc && doc.href);
      const key = pageKey(base);
      const tier = tierOf(base);
      const stem = stemOfHref(base);
      if (!key || tier === 3 || seen.has(key) || !stem || stem === "index") continue;
      const stemCanon = canonicalSearchKey(stem);
      if (stem === keys.qSlug || stem === keys.qBare || stemCanon === keys.qCanon || stemCanon === keys.qSing) {
        seen.add(key);
        slugCandidates.push({ href: base, title: String(doc.title || base), tier });
      }
    }
  }
  if (slugCandidates.length) {
    slugCandidates.sort((a, b) => a.tier - b.tier || a.href.localeCompare(b.href));
    return { href: slugCandidates[0].href, title: slugCandidates[0].title, matchedBy: "slug", alias: "" };
  }

  return null;
}

export function resolveComparison(query, meta = null, docs = null) {
  const parsed = parseQuery(query);
  if (!parsed.comparison) return null;
  const normalizedMeta = normalizeMeta(meta);
  const resolved = [];
  const seen = new Set();
  for (const side of parsed.comparison) {
    const hit = resolveSingleTarget(side, normalizedMeta, docs);
    if (hit && !seen.has(pageKey(hit.href))) {
      seen.add(pageKey(hit.href));
      resolved.push({ query: side, ...hit });
    } else {
      const dis = resolveDisambiguation(side, meta);
      if (dis && dis.options.length) {
        const first = dis.options[0];
        if (!seen.has(first.pageKey)) {
          seen.add(first.pageKey);
          resolved.push({ query: side, href: first.href, title: first.label, matchedBy: "disambiguation", alias: side });
        }
      }
    }
  }
  return resolved.length >= 2 ? { queries: parsed.comparison, targets: resolved } : null;
}

export function resolveExactMatch(query, meta = null, docs = null) {
  const parsed = parseQuery(query);
  if (parsed.comparison) return null;
  const normalizedMeta = normalizeMeta(meta);
  const direct = resolveSingleTarget(query, normalizedMeta, docs);
  if (direct) return direct;
  if (parsed.core && parsed.core !== fold(query)) {
    return resolveSingleTarget(parsed.core, normalizedMeta, docs);
  }
  return null;
}

function headerScoreForPage(title, aliases, coreQuery, terms, coreTokens, fullTokens) {
  let score = 0;
  const qFold = fold(coreQuery);
  const qCanon = canonicalSearchKey(coreQuery);
  const nWords = titleWordsCount(title);
  const tCanon = canonicalSearchKey(title);

  for (const term of terms) {
    if (hasTerm(title, term)) {
      score += (term.includes(" ") ? 200 : 90) + Math.round(60 / nWords);
    }
    if (aliases.some((alias) => hasTerm(alias, term))) {
      score += term.includes(" ") ? 180 : 85;
    }
  }
  if (qFold && hasTerm(title, qFold)) {
    score += 25;
  }
  if (qCanon && tCanon.startsWith(qCanon + "-")) {
    score += 30;
  }
  if (coreTokens.length >= 2) {
    if (coreTokens.every((tok) => hasTerm(title, tok))) {
      score += 240 + Math.round(60 / nWords);
    } else if (aliases.some((alias) => coreTokens.every((tok) => hasTerm(alias, tok)))) {
      score += 200;
    } else {
      const matchedCount = coreTokens.filter((tok) => hasTerm(title, tok) || aliases.some((a) => hasTerm(a, tok))).length;
      if (matchedCount >= 2) {
        score += matchedCount * 45;
      }
    }
  }
  // Tie-break bonus from extra context words in conversational queries
  // (e.g. "how to compute sample variance" vs "variance").
  if (fullTokens.length > coreTokens.length) {
    for (const tok of fullTokens) {
      if (coreTokens.includes(tok)) continue;
      if (hasTerm(title, tok)) score += 20;
      else if (aliases.some((a) => hasTerm(a, tok))) score += 12;
    }
  }
  return score;
}

function scoreChunkFields(chunk, coreQuery, terms, coreTokens, fullTokens) {
  let score = 0;
  const secFold = fold(chunk.section);
  const isBoilerplate = BOILERPLATE_SECTIONS.has(secFold);
  const qBare = bareKey(coreQuery);

  for (const term of terms) {
    if (chunk.section && !isBoilerplate && hasTerm(chunk.section, term)) {
      score += term.includes(" ") ? 120 : 45;
    }
    if (hasTerm(chunk.text, term)) {
      score += isBoilerplate ? 2 : term.includes(" ") ? 70 : 14;
    }
  }
  if (chunk.section && !isBoilerplate && qBare && bareKey(chunk.section) === qBare) {
    score += 65;
  }
  if (coreTokens.length >= 2) {
    if (chunk.section && !isBoilerplate && coreTokens.every((tok) => hasTerm(chunk.section, tok))) {
      score += 95;
    }
    if (coreTokens.every((tok) => hasTerm(chunk.text, tok))) {
      score += isBoilerplate ? 4 : 45;
    }
  }
  if (fullTokens.length > coreTokens.length && !isBoilerplate) {
    for (const tok of fullTokens) {
      if (coreTokens.includes(tok)) continue;
      if (chunk.section && hasTerm(chunk.section, tok)) score += 15;
      if (hasTerm(chunk.text, tok)) score += 5;
    }
  }
  return { score, isBoilerplate };
}

function matchAliasOnList(aliases, keys) {
  return aliases.find((a) => {
    const aSlug = slugKey(a);
    const aCanon = canonicalSearchKey(a);
    const aBare = bareKey(a);
    const aSing = singularKey(aBare);
    const aComp = compactKey(a);
    return (
      (keys.qSlug && aSlug === keys.qSlug) ||
      (keys.qCanon && aCanon === keys.qCanon) ||
      (keys.qBare && (aBare === keys.qBare || aSing === keys.qSing)) ||
      (keys.qCompact.length >= 2 && aComp === keys.qCompact)
    );
  });
}

export function scoreDocument(doc, query, meta = null) {
  const parsed = parseQuery(query);
  const coreQuery = parsed.core || query;
  const terms = expandedTerms(query);
  if (!terms.length || !doc) return 0;
  const keys = queryKeys(coreQuery);
  const coreTokens = queryTokens(coreQuery);
  const fullTokens = queryTokens(query);
  const normalizedMeta = normalizeMeta(meta);
  const key = pageKey(doc.href);
  const tier = tierOf(doc.href);
  const aliases = [
    ...(Array.isArray(doc.aliases) ? doc.aliases : []),
    ...(normalizedMeta.targetAliases.get(key) || []),
  ];

  let exactRank = 0;
  if (tier < 3) {
    exactRank = exactTitleRank(doc.title, keys);
    if (!exactRank) {
      const aliasHit = lookupAliasMatch(normalizedMeta, keys);
      if (aliasHit && aliasHit.targetKey === key) {
        exactRank = 1;
      } else if (matchAliasOnList(aliases, keys)) {
        exactRank = 1;
      }
    }
  }

  const headScore = headerScoreForPage(doc.title, aliases, coreQuery, terms, coreTokens, fullTokens);
  const chunkScore = scoreChunkFields(doc, coreQuery, terms, coreTokens, fullTokens).score;
  return exactRank * 5000 + headScore + chunkScore;
}

export function rankDocuments(docs, query, meta = null) {
  const parsed = parseQuery(query);
  const coreQuery = parsed.core || query;
  const terms = expandedTerms(query);
  if (!terms.length) return [];

  const normalizedMeta = normalizeMeta(meta);
  const keys = queryKeys(coreQuery);
  const rawKeys = queryKeys(query);
  const coreTokens = queryTokens(coreQuery);
  const fullTokens = queryTokens(query);

  const aliasHit = lookupAliasMatch(normalizedMeta, rawKeys) || lookupAliasMatch(normalizedMeta, keys);
  const disambig = resolveDisambiguation(query, meta);
  const comparison = resolveComparison(query, meta, docs);

  // Map pageKey -> priority boost for comparison targets or disambiguation options.
  const comparisonOrder = new Map();
  if (comparison) {
    comparison.targets.forEach((t, idx) => {
      comparisonOrder.set(pageKey(t.href), { idx, target: t });
    });
  }
  const disambigOrder = new Map();
  if (disambig) {
    disambig.options.forEach((opt, idx) => {
      if (!disambigOrder.has(opt.pageKey)) {
        disambigOrder.set(opt.pageKey, { idx, opt });
      }
    });
  }

  const groups = new Map();
  for (const doc of docs || []) {
    if (!doc || !doc.href) continue;
    const key = pageKey(doc.href);
    if (!key) continue;
    let group = groups.get(key);
    if (!group) {
      const metaPage = normalizedMeta.pages.get(key);
      group = {
        key,
        baseHref: canonicalHref(doc.href),
        title: (metaPage && metaPage.title) || String(doc.title || ""),
        chunks: [],
        rootChunk: null,
        aliases: [...(normalizedMeta.targetAliases.get(key) || [])],
      };
      groups.set(key, group);
    }
    if (Array.isArray(doc.aliases)) {
      for (const a of doc.aliases) {
        if (a && !group.aliases.some((existing) => fold(existing) === fold(a))) {
          group.aliases.push(a);
        }
      }
    }
    if (!String(doc.href).includes("#") && !group.rootChunk) {
      group.rootChunk = doc;
      group.baseHref = canonicalHref(doc.href);
      if (doc.title && !normalizedMeta.pages.has(key)) {
        group.title = String(doc.title);
      }
    }
    group.chunks.push(doc);
  }

  // Synthesize canonical entries from meta.pages even when Quarto's Fuse search
  // returned 0 chunks or missed the canonical concept page.
  for (const [key, metaPage] of normalizedMeta.pages.entries()) {
    if (groups.has(key)) continue;
    const synth = {
      href: metaPage.href,
      title: metaPage.title,
      section: "",
      text: metaPage.summary || "",
    };
    groups.set(key, {
      key,
      baseHref: metaPage.href,
      title: metaPage.title,
      chunks: [synth],
      rootChunk: synth,
      aliases: [...(normalizedMeta.targetAliases.get(key) || [])],
    });
  }

  const ranked = [];
  for (const group of groups.values()) {
    const tier = tierOf(group.baseHref);
    let exactRank = 0;
    let matchedAlias = "";
    let disambigNote = "";

    if (tier < 3) {
      if (comparisonOrder.has(group.key)) {
        const compHit = comparisonOrder.get(group.key);
        exactRank = 4 - Math.min(2, compHit.idx);
        if (compHit.target.alias && fold(compHit.target.alias) !== fold(group.title)) {
          matchedAlias = compHit.target.alias;
        }
      } else {
        exactRank = Math.max(
          exactTitleRank(group.title, rawKeys),
          exactTitleRank(group.title, keys)
        );
        if (!exactRank) {
          if (aliasHit && aliasHit.targetKey === group.key) {
            exactRank = 1;
            matchedAlias = aliasHit.alias;
          } else {
            const hit = matchAliasOnList(group.aliases, rawKeys) || matchAliasOnList(group.aliases, keys);
            if (hit) {
              exactRank = 1;
              matchedAlias = hit;
            }
          }
        }
        if (!exactRank && group.key !== "index.html") {
          const stem = stemOfHref(group.baseHref);
          const stemCanon = canonicalSearchKey(stem);
          if (
            stem &&
            stem !== "index" &&
            (stem === keys.qSlug || stem === keys.qBare || stemCanon === keys.qCanon || stemCanon === keys.qSing)
          ) {
            exactRank = 1;
          }
        }
      }
      if (disambigOrder.has(group.key)) {
        const dEntry = disambigOrder.get(group.key);
        disambigNote = dEntry.opt.description || "";
        // Surface all registered disambiguation meanings near the top, preserving
        // any direct canonical title/alias winner at #1 while keeping every other
        // disambiguated meaning immediately after it.
        if (exactRank === 0) {
          exactRank = 1;
        }
      }
    }

    let headScore = 0;
    if (comparison) {
      for (const side of comparison.queries) {
        const sideTerms = expandedTerms(side);
        const sideTokens = queryTokens(side);
        headScore = Math.max(
          headScore,
          headerScoreForPage(group.title, group.aliases, side, sideTerms, sideTokens, fullTokens)
        );
      }
    } else {
      headScore = headerScoreForPage(group.title, group.aliases, coreQuery, terms, coreTokens, fullTokens);
    }

    let bestChunk = group.rootChunk || group.chunks[0];
    let bestChunkScore = -1;
    let rootChunkScore = 0;
    let bestSectionChunk = null;
    let bestSectionScore = 0;
    let contentChunkHits = 0;

    for (const chunk of group.chunks) {
      const { score: cScore, isBoilerplate } = scoreChunkFields(
        chunk,
        coreQuery,
        terms,
        coreTokens,
        fullTokens
      );
      if (chunk === group.rootChunk) {
        rootChunkScore = cScore;
      }
      if (!isBoilerplate && cScore > 0) {
        contentChunkHits += 1;
      }
      const adjusted = isBoilerplate ? cScore : cScore + 0.5;
      if (adjusted > bestChunkScore) {
        bestChunkScore = adjusted;
        bestChunk = chunk;
      }
      const hasSection =
        Boolean(chunk.section) &&
        !isBoilerplate &&
        fold(chunk.section) !== fold(group.title) &&
        String(chunk.href || "").includes("#");
      if (hasSection && cScore > bestSectionScore) {
        bestSectionScore = cScore;
        bestSectionChunk = chunk;
      }
    }

    const rawBest = Math.max(0, Math.floor(bestChunkScore));
    const depthBonus = Math.min(15, Math.max(0, contentChunkHits - 1) * 3);
    const disambigBonus = disambigOrder.has(group.key)
      ? Math.max(0, 600 - disambigOrder.get(group.key).idx * 80)
      : 0;
    const totalScore = exactRank * 5000 + disambigBonus + headScore + rawBest + depthBonus;
    if (totalScore <= 0) continue;

    const showSection =
      exactRank < 2 &&
      bestSectionChunk !== null &&
      bestSectionScore > rootChunkScore;

    let chosenText = String(
      (showSection
        ? bestSectionChunk
        : group.rootChunk && String(group.rootChunk.text || "").trim()
        ? group.rootChunk
        : bestChunk
      )?.text || ""
    );
    if (!chosenText && disambigNote) {
      chosenText = disambigNote;
    }

    let outHref = group.baseHref;
    let outSection = showSection ? String(bestSectionChunk.section || "") : "";
    let outSectionHref = showSection ? String(bestSectionChunk.href || "") : "";
    if (disambigOrder.has(group.key)) {
      const optHref = disambigOrder.get(group.key).opt.href;
      if (optHref.includes("#") && !outSectionHref) {
        outSectionHref = optHref;
        outSection = disambigOrder.get(group.key).opt.label;
      }
    } else if (aliasHit && aliasHit.targetKey === group.key && aliasHit.fullHref && aliasHit.fullHref.includes("#") && !outSectionHref) {
      outSectionHref = aliasHit.fullHref;
    }

    const resultDoc = {
      ...(group.rootChunk || bestChunk),
      href: outHref,
      title: group.title || bestChunk.title || group.baseHref,
      section: outSection,
      sectionHref: outSectionHref,
      text: chosenText,
    };
    if (matchedAlias && fold(matchedAlias) !== fold(resultDoc.title)) {
      resultDoc.matchedAlias = matchedAlias;
    }
    if (disambigNote) {
      resultDoc.disambiguation = disambigNote;
    }

    ranked.push({
      doc: resultDoc,
      score: totalScore,
      tier,
      exactRank,
      disambigRank: disambigOrder.has(group.key) ? disambigOrder.get(group.key).idx : 999,
      nWords: titleWordsCount(resultDoc.title),
    });
  }

  ranked.sort((a, b) => {
    const fileOrder = Number(a.tier === 3) - Number(b.tier === 3);
    if (fileOrder !== 0) return fileOrder;
    if (a.exactRank !== b.exactRank) return b.exactRank - a.exactRank;
    if (a.disambigRank !== 999 || b.disambigRank !== 999) {
      if (a.disambigRank !== b.disambigRank) return a.disambigRank - b.disambigRank;
    }
    if (a.tier !== b.tier) return a.tier - b.tier;
    if (b.score !== a.score) return b.score - a.score;
    if (a.nWords !== b.nWords) return a.nWords - b.nWords;
    return (
      fold(a.doc.title).localeCompare(fold(b.doc.title)) ||
      String(a.doc.href).localeCompare(String(b.doc.href))
    );
  });

  return ranked.map((item) => item.doc);
}

// Synthesize canonical/ranked items for Quarto's live autocomplete widget so
// abbreviations ("sd", "ci"), unpunctuated names ("Bayes theorem", "t test"),
// conversational questions ("what is a p value"), comparisons ("mean vs median"),
// and disambiguations ("mean", "kernel") always appear in the live dropdown
// even when Fuse.js returns 0 results or misses the canonical target.
export function augmentQuartoSearchItems(fuseItems, query, meta = null, allDocs = null, limit = 25) {
  const q = String(query || "").trim();
  if (!q) return [];
  const pool = Array.isArray(allDocs) && allDocs.length ? allDocs : fuseItems || [];
  const ranked = rankDocuments(pool, q, meta);
  if (!ranked.length) return fuseItems || [];

  const out = [];
  for (const doc of ranked.slice(0, limit)) {
    const targetHref = doc.sectionHref || doc.href;
    const summaryParts = [];
    if (doc.matchedAlias) {
      summaryParts.push(`Alias: ${doc.matchedAlias}`);
    }
    if (doc.disambiguation) {
      summaryParts.push(doc.disambiguation);
    } else if (doc.text) {
      const clean = String(doc.text).replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim();
      if (clean) summaryParts.push(clean.slice(0, 180));
    }
    out.push({
      href: targetHref,
      title: doc.title || doc.href,
      section: doc.section || "",
      text: summaryParts.join(" — ") || doc.title || "",
      crumbs: Array.isArray(doc.crumbs) ? doc.crumbs : undefined,
    });
  }
  return out;
}

export function documentsFromIndex(payload) {
  if (Array.isArray(payload)) return payload;
  if (payload && Array.isArray(payload.docs)) return payload.docs;
  if (payload && Array.isArray(payload.items)) return payload.items;
  return [];
}

if (typeof window !== "undefined") {
  window.wikiRankDocuments = rankDocuments;
  window.wikiResolveExactMatch = resolveExactMatch;
  window.wikiResolveDisambiguation = resolveDisambiguation;
  window.wikiResolveComparison = resolveComparison;
  window.wikiParseQuery = parseQuery;
  window.wikiCanonicalSearchKey = canonicalSearchKey;
  window.wikiAugmentQuartoSearchItems = augmentQuartoSearchItems;
  window.wikiSearchTier = tierOf;
  window.wikiExpandedTerms = expandedTerms;
  window.wikiDocumentsFromIndex = documentsFromIndex;
  window.wikiCanonicalHref = canonicalHref;
}
