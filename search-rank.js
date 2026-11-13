// Ranking and canonical-page grouping for StatWiki search.
// Quarto writes one search.json chunk per section heading; this module merges
// chunks onto their canonical page, surfaces the best matching section anchor,
// and ranks exact canonical titles and registered concept aliases first.

const SYNONYM_GROUPS = [["mean", "average", "sample mean"]];

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
]);

function fold(value) {
  return String(value || "")
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[’‘]/g, "'")
    .replace(/[–—]/g, "-")
    .toLowerCase()
    .replace(/\s+/g, " ")
    .trim();
}

export function slugKey(value) {
  return fold(value)
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function bareSlugKey(value) {
  return slugKey(value).replace(/^(?:the|a|an)-/, "");
}

function compactKey(value) {
  return bareSlugKey(value).replace(/-/g, "");
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function hasTerm(text, term) {
  const hay = fold(text);
  const needle = fold(term);
  if (!needle) return false;
  const flexNeedle = escapeRegExp(needle).replace(/(?:\\-| )+/g, "[- ]+");
  const pattern = new RegExp("(^|[^a-z0-9])" + flexNeedle + "([^a-z0-9]|$)");
  if (pattern.test(hay)) return true;
  if (!needle.includes(" ") && !needle.includes("-") && needle.length >= 5) {
    const dehyphenHay = hay.replace(/([a-z0-9])-([a-z0-9])/g, "$1$2");
    const compactPattern = new RegExp("(^|[^a-z0-9])" + escapeRegExp(needle) + "([^a-z0-9]|$)");
    return compactPattern.test(dehyphenHay);
  }
  return false;
}

function queryTokens(query) {
  const tokens = slugKey(query).split("-").filter(Boolean);
  const filtered = tokens.filter((tok) => tok.length >= 2 && !STOP_WORDS.has(tok));
  return filtered.length ? filtered : tokens;
}

export function canonicalHref(href) {
  return String(href || "").split("#")[0];
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
  const q = fold(query);
  if (!q) return [];
  for (const group of SYNONYM_GROUPS) {
    const hit = group.some((term) => q === term || (term.includes(" ") && q.includes(term)));
    if (hit) return group.slice();
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

function normalizeMeta(meta) {
  const pages = new Map();
  const aliasToTarget = new Map();
  const compactToTarget = new Map();
  const ambiguousCompact = new Set();
  const targetAliases = new Map();

  function addAlias(label, rawHref) {
    const targetKey = pageKey(rawHref);
    const cleanLabel = String(label || "").trim();
    if (!targetKey || !cleanLabel) return;
    const sKey = slugKey(cleanLabel);
    const bKey = bareSlugKey(cleanLabel);
    const cKey = compactKey(cleanLabel);
    if (!sKey) return;
    let list = targetAliases.get(targetKey);
    if (!list) {
      list = [];
      targetAliases.set(targetKey, list);
    }
    if (!list.some((existing) => fold(existing) === fold(cleanLabel))) {
      list.push(cleanLabel);
    }
    for (const k of [sKey, bKey]) {
      if (k && !aliasToTarget.has(k)) {
        aliasToTarget.set(k, { targetKey, href: canonicalHref(rawHref), alias: cleanLabel });
      }
    }
    if (cKey.length >= 3) {
      const prev = compactToTarget.get(cKey);
      if (prev && prev.targetKey !== targetKey) {
        ambiguousCompact.add(cKey);
        compactToTarget.delete(cKey);
      } else if (!prev && !ambiguousCompact.has(cKey)) {
        compactToTarget.set(cKey, { targetKey, href: canonicalHref(rawHref), alias: cleanLabel });
      }
    }
  }

  if (meta && typeof meta === "object") {
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
    if (meta.aliases && typeof meta.aliases === "object") {
      for (const [alias, target] of Object.entries(meta.aliases)) {
        if (typeof target === "string") {
          addAlias(alias, target);
        } else if (target && typeof target === "object" && target.href) {
          addAlias(target.label || alias, target.href);
        }
      }
    }
  }

  return { pages, aliasToTarget, compactToTarget, targetAliases };
}

function titleWordsCount(title) {
  const words = slugKey(title).split("-").filter(Boolean);
  return Math.max(1, words.length);
}

function exactTitleRank(title, qSlug, qBare, qCompact) {
  if (!title || !qSlug) return 0;
  const tSlug = slugKey(title);
  const tBare = bareSlugKey(title);
  const tCompact = compactKey(title);
  if (tSlug === qSlug) return 3;
  if (qBare && tBare === qBare) return 2;
  if (qCompact.length >= 4 && tCompact === qCompact) return 2;
  return 0;
}

function lookupAliasMatch(normalizedMeta, qSlug, qBare, qCompact) {
  if (!qSlug) return null;
  const direct =
    normalizedMeta.aliasToTarget.get(qSlug) ||
    (qBare ? normalizedMeta.aliasToTarget.get(qBare) : null) ||
    (qCompact.length >= 3 ? normalizedMeta.compactToTarget.get(qCompact) : null);
  return direct || null;
}

export function resolveExactMatch(query, meta = null, docs = null) {
  const qSlug = slugKey(query);
  if (!qSlug) return null;
  const qBare = bareSlugKey(query);
  const qCompact = compactKey(query);
  const normalizedMeta = normalizeMeta(meta);

  const candidates = [];
  for (const page of normalizedMeta.pages.values()) {
    const tier = tierOf(page.href);
    if (tier === 3) continue;
    const rank = exactTitleRank(page.title, qSlug, qBare, qCompact);
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
      const rank = exactTitleRank(doc.title, qSlug, qBare, qCompact);
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

  const aliasHit = lookupAliasMatch(normalizedMeta, qSlug, qBare, qCompact);
  if (aliasHit && tierOf(aliasHit.href) < 3) {
    const pageInfo = normalizedMeta.pages.get(aliasHit.targetKey);
    let title = pageInfo ? pageInfo.title : "";
    if (!title && Array.isArray(docs)) {
      const foundDoc = docs.find((d) => pageKey(d && d.href) === aliasHit.targetKey);
      if (foundDoc) title = String(foundDoc.title || "");
    }
    return {
      href: canonicalHref(aliasHit.href),
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
    if (stem && stem !== "index" && (stem === qSlug || stem === qBare)) {
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
      if (stem === qSlug || stem === qBare) {
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

function headerScoreForPage(title, aliases, query, terms, qTokens) {
  let score = 0;
  const qFold = fold(query);
  const qSlug = slugKey(query);
  const nWords = titleWordsCount(title);

  for (const term of terms) {
    if (hasTerm(title, term)) {
      score += (term.includes(" ") ? 200 : 90) + Math.round(60 / nWords);
    }
    if (aliases.some((alias) => hasTerm(alias, term))) {
      score += term.includes(" ") ? 180 : 85;
    }
  }
  if (qFold && hasTerm(title, qFold)) {
    score += 20;
  }
  if (qSlug && slugKey(title).startsWith(qSlug + "-")) {
    score += 25;
  }
  if (qTokens.length >= 2) {
    if (qTokens.every((tok) => hasTerm(title, tok))) {
      score += 220 + Math.round(60 / nWords);
    } else if (aliases.some((alias) => qTokens.every((tok) => hasTerm(alias, tok)))) {
      score += 190;
    }
  }
  return score;
}

function scoreChunkFields(chunk, query, terms, qTokens) {
  let score = 0;
  const secFold = fold(chunk.section);
  const isBoilerplate = BOILERPLATE_SECTIONS.has(secFold);
  const qBare = bareSlugKey(query);

  for (const term of terms) {
    if (chunk.section && !isBoilerplate && hasTerm(chunk.section, term)) {
      score += term.includes(" ") ? 120 : 45;
    }
    if (hasTerm(chunk.text, term)) {
      score += isBoilerplate ? 2 : term.includes(" ") ? 70 : 14;
    }
  }
  if (chunk.section && !isBoilerplate && qBare && bareSlugKey(chunk.section) === qBare) {
    score += 65;
  }
  if (qTokens.length >= 2) {
    if (chunk.section && !isBoilerplate && qTokens.every((tok) => hasTerm(chunk.section, tok))) {
      score += 95;
    }
    if (qTokens.every((tok) => hasTerm(chunk.text, tok))) {
      score += isBoilerplate ? 4 : 45;
    }
  }
  return { score, isBoilerplate };
}

export function scoreDocument(doc, query, meta = null) {
  const terms = expandedTerms(query);
  if (!terms.length || !doc) return 0;
  const qSlug = slugKey(query);
  const qBare = bareSlugKey(query);
  const qCompact = compactKey(query);
  const qTokens = queryTokens(query);
  const normalizedMeta = normalizeMeta(meta);
  const key = pageKey(doc.href);
  const tier = tierOf(doc.href);
  const aliases = [
    ...(Array.isArray(doc.aliases) ? doc.aliases : []),
    ...(normalizedMeta.targetAliases.get(key) || []),
  ];

  let exactRank = 0;
  if (tier < 3) {
    exactRank = exactTitleRank(doc.title, qSlug, qBare, qCompact);
    if (!exactRank) {
      const aliasHit = lookupAliasMatch(normalizedMeta, qSlug, qBare, qCompact);
      if (aliasHit && aliasHit.targetKey === key) {
        exactRank = 1;
      } else if (
        aliases.some((a) => {
          const aSlug = slugKey(a);
          const aBare = bareSlugKey(a);
          const aComp = compactKey(a);
          return aSlug === qSlug || (qBare && aBare === qBare) || (qCompact.length >= 3 && aComp === qCompact);
        })
      ) {
        exactRank = 1;
      }
    }
  }

  const headScore = headerScoreForPage(doc.title, aliases, query, terms, qTokens);
  const chunkScore = scoreChunkFields(doc, query, terms, qTokens).score;
  return exactRank * 5000 + headScore + chunkScore;
}

export function rankDocuments(docs, query, meta = null) {
  const terms = expandedTerms(query);
  if (!terms.length) return [];
  const qSlug = slugKey(query);
  const qBare = bareSlugKey(query);
  const qCompact = compactKey(query);
  const qTokens = queryTokens(query);
  const normalizedMeta = normalizeMeta(meta);
  const aliasHit = lookupAliasMatch(normalizedMeta, qSlug, qBare, qCompact);

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

  // Ensure pages registered in meta.pages can still match by title/alias even if
  // their prose chunk did not repeat an abbreviation.
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

    if (tier < 3) {
      exactRank = exactTitleRank(group.title, qSlug, qBare, qCompact);
      if (!exactRank) {
        if (aliasHit && aliasHit.targetKey === group.key) {
          exactRank = 1;
          matchedAlias = aliasHit.alias;
        } else {
          const hit = group.aliases.find((a) => {
            const aSlug = slugKey(a);
            const aBare = bareSlugKey(a);
            const aComp = compactKey(a);
            return aSlug === qSlug || (qBare && aBare === qBare) || (qCompact.length >= 3 && aComp === qCompact);
          });
          if (hit) {
            exactRank = 1;
            matchedAlias = hit;
          }
        }
      }
      if (!exactRank && group.key !== "index.html") {
        const stem = stemOfHref(group.baseHref);
        if (stem && stem !== "index" && (stem === qSlug || stem === qBare)) {
          exactRank = 1;
        }
      }
    }

    const headScore = headerScoreForPage(group.title, group.aliases, query, terms, qTokens);
    let bestChunk = group.rootChunk || group.chunks[0];
    let bestChunkScore = -1;
    let rootChunkScore = 0;
    let bestSectionChunk = null;
    let bestSectionScore = 0;
    let contentChunkHits = 0;

    for (const chunk of group.chunks) {
      const { score: cScore, isBoilerplate } = scoreChunkFields(chunk, query, terms, qTokens);
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
    const totalScore = exactRank * 5000 + headScore + rawBest + depthBonus;
    if (totalScore <= 0) continue;

    const showSection =
      exactRank < 2 &&
      bestSectionChunk !== null &&
      bestSectionScore > rootChunkScore;

    const chosenTextChunk = showSection
      ? bestSectionChunk
      : (group.rootChunk && String(group.rootChunk.text || "").trim() ? group.rootChunk : bestChunk);

    const resultDoc = {
      ...(group.rootChunk || bestChunk),
      href: group.baseHref,
      title: group.title || bestChunk.title || group.baseHref,
      section: showSection ? String(bestSectionChunk.section || "") : "",
      sectionHref: showSection ? String(bestSectionChunk.href || "") : "",
      text: String((chosenTextChunk && chosenTextChunk.text) || ""),
    };
    if (matchedAlias && fold(matchedAlias) !== fold(resultDoc.title)) {
      resultDoc.matchedAlias = matchedAlias;
    }

    ranked.push({
      doc: resultDoc,
      score: totalScore,
      tier,
      exactRank,
      nWords: titleWordsCount(resultDoc.title),
    });
  }

  ranked.sort((a, b) => {
    const fileOrder = Number(a.tier === 3) - Number(b.tier === 3);
    if (fileOrder !== 0) return fileOrder;
    if (a.exactRank !== b.exactRank) return b.exactRank - a.exactRank;
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

export function documentsFromIndex(payload) {
  if (Array.isArray(payload)) return payload;
  if (payload && Array.isArray(payload.docs)) return payload.docs;
  if (payload && Array.isArray(payload.items)) return payload.items;
  return [];
}

if (typeof window !== "undefined") {
  window.wikiRankDocuments = rankDocuments;
  window.wikiResolveExactMatch = resolveExactMatch;
  window.wikiSearchTier = tierOf;
  window.wikiExpandedTerms = expandedTerms;
  window.wikiDocumentsFromIndex = documentsFromIndex;
  window.wikiCanonicalHref = canonicalHref;
}
