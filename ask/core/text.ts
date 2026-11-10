import { createHash } from "node:crypto"

const TITLE_STOP = new Set(
  "the a an of and or to in on for with by from at as is be its into over per are was were this that these those not but if than then so such only about across after before between within without using use used how what when where which who why does did do can may will shall should would could".split(" "),
)

export function estimateTokens(text: string): number {
  return Math.max(1, Math.ceil(text.length / 4))
}

export function percentile(values: number[], p: number): number {
  if (values.length === 0) return 0
  const sorted = [...values].sort((a, b) => a - b)
  const rank = Math.ceil((p / 100) * sorted.length)
  const index = Math.min(sorted.length - 1, Math.max(0, rank - 1))
  return sorted[index]
}

export function mean(values: number[]): number {
  if (values.length === 0) return 0
  return values.reduce((sum, value) => sum + value, 0) / values.length
}

export function pagePath(url: string): string {
  return url.split("#", 1)[0]
}

export function normalizeWords(text: string): string[] {
  return text
    .toLowerCase()
    .replace(/\$+/g, " ")
    .replace(/[-–—]+/g, " ")
    .replace(/[^\p{L}\p{N}\s]/gu, " ")
    .split(/\s+/)
    .filter(Boolean)
}

export function titleHits(question: string, title: string): boolean {
  const titleWords = normalizeWords(title)
  if (titleWords.join("").length < 4) return false
  const questionWords = normalizeWords(question)
  if (titleWords.length === 0 || titleWords.length > questionWords.length) return false
  outer: for (let i = 0; i + titleWords.length <= questionWords.length; i++) {
    for (let j = 0; j < titleWords.length; j++) {
      if (questionWords[i + j] !== titleWords[j]) continue outer
    }
    return true
  }
  return false
}

export function titleContentWords(title: string): string[] {
  return normalizeWords(title).filter((word) => word.length >= 3 && !TITLE_STOP.has(word))
}

export function titleLeaks(question: string, title: string): string[] {
  const words = new Set(normalizeWords(question))
  return titleContentWords(title).filter((word) => words.has(word))
}

export function sha256Hex(text: string): string {
  return createHash("sha256").update(text).digest("hex")
}

export function vectorIdFor(chunkId: string): string {
  return sha256Hex(chunkId).slice(0, 32)
}

export function parseArgs(argv: string[]): Record<string, string | boolean> {
  const out: Record<string, string | boolean> = {}
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i]
    if (!arg.startsWith("--")) continue
    const key = arg.slice(2)
    const next = argv[i + 1]
    if (next === undefined || next.startsWith("--")) out[key] = true
    else {
      out[key] = next
      i++
    }
  }
  return out
}
