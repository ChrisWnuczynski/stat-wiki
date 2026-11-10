import { CANDIDATE_K, FETCH_K } from "./config.ts"
import { bestSimilarity } from "./retrieve.ts"
import type { Candidate } from "./types.ts"

export type ScoredMatch = {
  id: string
  score: number
  metadata?: Record<string, unknown> | null
}

export function candidateFromMatch(match: ScoredMatch): Candidate | null {
  const metadata = match.metadata ?? {}
  const entryId = String(metadata.entryId ?? "")
  const chunkId = String(metadata.chunkId ?? "")
  if (!entryId || !chunkId) return null
  return {
    chunkId,
    entryId,
    score: Number(match.score),
    title: String(metadata.title ?? ""),
    kind: String(metadata.kind ?? ""),
    chapterId: String(metadata.chapterId ?? ""),
    url: String(metadata.url ?? ""),
    part: Number(metadata.part ?? 0),
  }
}

export function rankMatches(matches: ScoredMatch[]): Candidate[] {
  return matches
    .map(candidateFromMatch)
    .filter((candidate): candidate is Candidate => candidate !== null)
    .sort((a, b) => b.score - a.score || a.chunkId.localeCompare(b.chunkId))
}

export function takePool(
  ranked: Candidate[],
  mode: "open" | "closed",
  exclude: ReadonlySet<string>,
  fetched: number,
): { candidates: Candidate[]; best: number; short: boolean } {
  if (mode === "closed") {
    const closedAll = ranked.filter((candidate) => !exclude.has(candidate.entryId))
    const candidates = closedAll.slice(0, CANDIDATE_K)
    return {
      candidates,
      best: bestSimilarity(candidates),
      short: fetched >= FETCH_K && closedAll.length < CANDIDATE_K,
    }
  }
  const candidates = ranked.slice(0, CANDIDATE_K)
  return { candidates, best: bestSimilarity(candidates), short: false }
}

export function textsFromStored(stored: Map<string, string | null>): Map<string, string> {
  const texts = new Map<string, string>()
  for (const [key, value] of stored) {
    if (!value) continue
    try {
      const parsed = JSON.parse(value) as { text?: unknown }
      if (typeof parsed.text === "string" && parsed.text) texts.set(key, parsed.text)
    } catch {
      continue
    }
  }
  return texts
}
