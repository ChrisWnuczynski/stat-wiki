import {
  DEFINES_BOOST,
  PAGE_BOOST,
  SECTION_BOOST,
  TITLE_BOOST,
  TOKEN_BUDGET,
} from "./config.ts"
import type { Candidate, Passage } from "./types.ts"
import { estimateTokens, pagePath, titleHits } from "./text.ts"

export type RerankOptions = {
  pageBoost: number
  sectionBoost: number
  titleBoost: number
  definesBoost: number
  definesTargets: Set<string>
  pagePath?: string
  chapterId?: string
}

export type Ranked = Candidate & { boosted: number }

export const DEFAULT_BOOSTS: Omit<RerankOptions, "definesTargets" | "pagePath" | "chapterId"> = {
  pageBoost: PAGE_BOOST,
  sectionBoost: SECTION_BOOST,
  titleBoost: TITLE_BOOST,
  definesBoost: DEFINES_BOOST,
}

export function rerank(question: string, candidates: Candidate[], options: RerankOptions): Ranked[] {
  const ranked = candidates.map((candidate) => {
    let boosted = candidate.score
    if (options.pageBoost && options.pagePath && pagePath(candidate.url) === options.pagePath) {
      boosted += options.pageBoost
    }
    if (options.sectionBoost && options.chapterId && candidate.chapterId === options.chapterId) {
      boosted += options.sectionBoost
    }
    if (titleHits(question, candidate.title)) {
      boosted += options.titleBoost
      if (options.definesTargets.has(candidate.entryId)) boosted += options.definesBoost
    }
    return { ...candidate, boosted }
  })
  ranked.sort((a, b) => b.boosted - a.boosted || b.score - a.score || a.chunkId.localeCompare(b.chunkId))
  return ranked
}

export function packPassages(
  ranked: Ranked[],
  texts: Map<string, string>,
  k: number,
  budget = TOKEN_BUDGET,
): Passage[] {
  const kept: Passage[] = []
  let used = 0
  for (const candidate of ranked) {
    if (kept.length >= k) break
    const text = texts.get(candidate.chunkId)
    if (!text) continue
    const n = kept.length + 1
    const tokens = estimateTokens(`[${n}] ${text}`)
    if (kept.length > 0 && used + tokens > budget) break
    kept.push({
      n,
      chunkId: candidate.chunkId,
      entryId: candidate.entryId,
      url: candidate.url,
      text,
      tokens,
    })
    used += tokens
  }
  return kept
}

export function bestSimilarity(candidates: { score: number }[]): number {
  if (candidates.length === 0) return 0
  return candidates.reduce((best, candidate) => Math.max(best, candidate.score), 0)
}

export function isCovered(best: number, threshold: number): boolean {
  return best >= threshold
}

export function calibrateThreshold(devScores: number[], misuseScores: number[]): {
  threshold: number
  devCovered: number
  misuseBelow: number
} {
  if (devScores.length === 0) {
    return { threshold: 1, devCovered: 0, misuseBelow: 0 }
  }
  const points = new Set<number>([0, 1])
  for (const score of [...devScores, ...misuseScores]) points.add(Math.round(score * 1000) / 1000)
  const ordered = [...points].sort((a, b) => a - b)
  const evaluate = (threshold: number) => {
    const devCovered = devScores.filter((score) => score >= threshold).length / devScores.length
    const misuseBelow = misuseScores.length === 0
      ? 0
      : misuseScores.filter((score) => score < threshold).length / misuseScores.length
    return { threshold, devCovered, misuseBelow, objective: devCovered + misuseBelow }
  }
  const ranked = ordered.map(evaluate).sort((a, b) =>
    b.objective - a.objective || b.misuseBelow - a.misuseBelow || a.threshold - b.threshold,
  )
  const constrained = ranked.filter((item) => item.devCovered >= 0.9)
  const chosen = (constrained.length > 0 ? constrained : ranked)[0]
  return { threshold: chosen.threshold, devCovered: chosen.devCovered, misuseBelow: chosen.misuseBelow }
}
