import { OVERLAP_PARAGRAPH_CHARS, OVERLAP_WORDS } from "./config.ts"
import type { WikiDoc } from "./types.ts"

export const OVERLAP_RULE = "A worked answer overlaps another entry when a whitespace-normalised paragraph of at least 180 characters is copied into that entry, or when 40 consecutive words are copied. The question and the answer themselves are not listed. This is a copy check, not a topical similarity check."

export type OverlapHit = {
  questionId: string
  answerId: string
  entryId: string
  kind: string
  title: string
}

export function normSpace(text: string): string {
  return text.replace(/\s+/g, " ").trim().toLowerCase()
}

export function textsOverlap(answer: string, other: string): boolean {
  const otherNorm = normSpace(other)
  for (const paragraph of answer.split(/\n\s*\n/)) {
    const normalized = normSpace(paragraph)
    if (normalized.length >= OVERLAP_PARAGRAPH_CHARS && otherNorm.includes(normalized)) return true
  }
  const words = normSpace(answer).split(" ").filter(Boolean)
  if (words.length < OVERLAP_WORDS) return false
  for (let i = 0; i + OVERLAP_WORDS <= words.length; i++) {
    if (otherNorm.includes(words.slice(i, i + OVERLAP_WORDS).join(" "))) return true
  }
  return false
}

export function findOverlaps(doc: WikiDoc): OverlapHit[] {
  const byId = new Map(doc.entries.map((entry) => [entry.id, entry]))
  const questionOfAnswer = new Map<string, string>()
  for (const edge of doc.edges) {
    if (edge.type === "of") questionOfAnswer.set(edge.from, edge.to)
  }
  const candidates = doc.entries.filter((entry) => entry.text && entry.kind !== "answer" && entry.kind !== "question")
  const grams = new Map<string, string[]>()
  for (const entry of candidates) {
    const words = normSpace(entry.text!).split(" ").filter(Boolean)
    const seen = new Set<string>()
    for (let i = 0; i + 8 <= words.length; i++) {
      const key = words.slice(i, i + 8).join(" ")
      if (seen.has(key)) continue
      seen.add(key)
      const list = grams.get(key) ?? []
      list.push(entry.id)
      grams.set(key, list)
    }
  }

  const hits: OverlapHit[] = []
  const seenPair = new Set<string>()
  for (const answer of doc.entries) {
    if (answer.kind !== "answer" || !answer.text) continue
    const questionId = questionOfAnswer.get(answer.id)
    if (!questionId) continue
    const words = normSpace(answer.text).split(" ").filter(Boolean)
    const counts = new Map<string, number>()
    for (let i = 0; i + 8 <= words.length; i += 4) {
      const key = words.slice(i, i + 8).join(" ")
      for (const id of grams.get(key) ?? []) counts.set(id, (counts.get(id) ?? 0) + 1)
    }
    const pool = new Set(
      [...counts.entries()]
        .filter(([, count]) => count >= 2)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 15)
        .map(([id]) => id),
    )
    const shortParas = answer.text.split(/\n\s*\n/).map(normSpace).filter((paragraph) =>
      paragraph.length >= OVERLAP_PARAGRAPH_CHARS && paragraph.split(" ").filter(Boolean).length < 8,
    )
    if (shortParas.length > 0) {
      for (const entry of candidates) {
        const haystack = normSpace(entry.text!)
        if (shortParas.some((paragraph) => haystack.includes(paragraph))) pool.add(entry.id)
      }
    }
    for (const id of pool) {
      if (id === answer.id || id === questionId) continue
      const other = byId.get(id)
      if (!other?.text) continue
      if (!textsOverlap(answer.text, other.text)) continue
      const key = `${answer.id}\t${id}`
      if (seenPair.has(key)) continue
      seenPair.add(key)
      hits.push({
        questionId,
        answerId: answer.id,
        entryId: id,
        kind: other.kind,
        title: other.title,
      })
    }
  }
  hits.sort((a, b) => a.questionId.localeCompare(b.questionId) || a.entryId.localeCompare(b.entryId))
  return hits
}

export function excludeIdsForQuestion(questionId: string, answerIds: string[], overlaps: OverlapHit[]): string[] {
  const ids = new Set<string>([questionId, ...answerIds])
  for (const hit of overlaps) {
    if (hit.questionId === questionId) ids.add(hit.entryId)
  }
  return [...ids]
}
