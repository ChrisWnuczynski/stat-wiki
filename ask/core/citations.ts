import type { Citation, Passage } from "./types.ts"

export function citationsFromAnswer(answer: string, passages: Pick<Passage, "n" | "entryId" | "url">[]): Citation[] {
  const byNumber = new Map(passages.map((passage) => [passage.n, passage]))
  const max = passages.reduce((highest, passage) => Math.max(highest, passage.n), 0)
  const order: string[] = []
  const grouped = new Map<string, Citation>()
  const pattern = /\[(\d+(?:\s*,\s*\d+)*)\]/g
  let match: RegExpExecArray | null
  while ((match = pattern.exec(answer))) {
    const numbers = match[1].split(",").map((part) => Number(part.trim()))
    for (const n of numbers) {
      if (!Number.isInteger(n) || n < 1 || n > max) continue
      const passage = byNumber.get(n)
      if (!passage) continue
      const existing = grouped.get(passage.entryId)
      if (existing) {
        if (!existing.numbers.includes(n)) existing.numbers.push(n)
        continue
      }
      grouped.set(passage.entryId, { entryId: passage.entryId, url: passage.url, numbers: [n] })
      order.push(passage.entryId)
    }
  }
  return order.map((id) => grouped.get(id)!).filter(Boolean)
}
