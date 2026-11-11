// Ranking for the site search. Articles and other pages come before figure
// files. The words mean, average, and sample mean are one query.

const SYNONYM_GROUPS = [["mean", "average", "sample mean"]];

function fold(value) {
  return String(value || "").toLowerCase().replace(/\s+/g, " ").trim();
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function hasTerm(text, term) {
  const hay = fold(text);
  const needle = fold(term);
  if (!needle) return false;
  const pattern = new RegExp("(^|[^a-z0-9])" + escapeRegExp(needle) + "([^a-z0-9]|$)");
  return pattern.test(hay);
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
  const path = String(href || "").split("#")[0].replace(/^\//, "");
  if (path.startsWith("files/") || path.includes("/files/")) return 3;
  if (path.startsWith("articles/") || path.includes("/articles/")) return 0;
  if (path.startsWith("notes/") || path.includes("/notes/") || path.startsWith("reference/")) return 1;
  return 2;
}

function fieldScore(doc, term) {
  let score = 0;
  if (hasTerm(doc.title, term)) score += term.includes(" ") ? 200 : 80;
  if (hasTerm(doc.section, term)) score += term.includes(" ") ? 120 : 40;
  if (hasTerm(doc.text, term)) score += term.includes(" ") ? 70 : 12;
  return score;
}

export function scoreDocument(doc, query) {
  const terms = expandedTerms(query);
  if (!terms.length) return 0;
  let score = 0;
  for (const term of terms) score += fieldScore(doc, term);
  const q = fold(query);
  if (q && hasTerm(doc.title, q)) score += 15;
  return score;
}

export function rankDocuments(docs, query) {
  const ranked = [];
  for (const doc of docs || []) {
    const score = scoreDocument(doc, query);
    if (score <= 0) continue;
    ranked.push({ doc, score, tier: tierOf(doc.href) });
  }
  ranked.sort((a, b) => a.tier - b.tier || b.score - a.score || fold(a.doc.title).localeCompare(fold(b.doc.title)) || String(a.doc.href).localeCompare(String(b.doc.href)));
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
  window.wikiSearchTier = tierOf;
  window.wikiExpandedTerms = expandedTerms;
  window.wikiDocumentsFromIndex = documentsFromIndex;
}
