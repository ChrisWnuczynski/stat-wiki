import type { WikiDoc, WikiEdge, WikiEntry } from "./types.ts"

export type Graph = {
  byId: Map<string, WikiEntry>
  chapterOf: (id: string) => string | null
  definesTargets: Set<string>
  answersOf: Map<string, string[]>
}

export function buildGraph(doc: WikiDoc): Graph {
  const byId = new Map(doc.entries.map((entry) => [entry.id, entry]))
  const out = new Map<string, WikiEdge[]>()
  const incoming = new Map<string, WikiEdge[]>()
  for (const edge of doc.edges) {
    const from = out.get(edge.from) ?? []
    from.push(edge)
    out.set(edge.from, from)
    const to = incoming.get(edge.to) ?? []
    to.push(edge)
    incoming.set(edge.to, to)
  }

  const memo = new Map<string, string | null>()
  const chapterOf = (id: string, stack = new Set<string>()): string | null => {
    if (memo.has(id)) return memo.get(id) ?? null
    if (stack.has(id)) return null
    stack.add(id)
    try {
      const entry = byId.get(id)
      if (!entry) {
        memo.set(id, null)
        return null
      }
      if (entry.kind === "chapter") {
        memo.set(id, id)
        return id
      }
      const direct = (out.get(id) ?? [])
        .filter((edge) =>
          (edge.type === "in" || edge.type === "stated-in" || edge.type === "on")
          && byId.get(edge.to)?.kind === "chapter",
        )
        .map((edge) => edge.to)
        .sort()
      if (direct.length > 0) {
        memo.set(id, direct[0])
        return direct[0]
      }
      const walks = (out.get(id) ?? [])
        .filter((edge) => edge.type === "of" || edge.type === "for")
        .sort((a, b) => a.to.localeCompare(b.to) || a.type.localeCompare(b.type))
      for (const edge of walks) {
        const found = chapterOf(edge.to, stack)
        if (found) {
          memo.set(id, found)
          return found
        }
      }
      const definedBy = (incoming.get(id) ?? [])
        .filter((edge) => edge.type === "defines" && byId.get(edge.from)?.kind === "chapter")
        .map((edge) => edge.from)
        .sort()
      const result = definedBy[0] ?? null
      memo.set(id, result)
      return result
    } finally {
      stack.delete(id)
    }
  }

  const definesTargets = new Set<string>()
  const answersOf = new Map<string, string[]>()
  for (const edge of doc.edges) {
    if (edge.type === "defines") definesTargets.add(edge.to)
    if (edge.type === "of") {
      const list = answersOf.get(edge.to) ?? []
      list.push(edge.from)
      answersOf.set(edge.to, list)
    }
  }

  return { byId, chapterOf: (id) => chapterOf(id), definesTargets, answersOf }
}

export function definesDirection(doc: WikiDoc): { from: Record<string, number>; to: Record<string, number> } {
  const byId = new Map(doc.entries.map((entry) => [entry.id, entry]))
  const from: Record<string, number> = {}
  const to: Record<string, number> = {}
  for (const edge of doc.edges) {
    if (edge.type !== "defines") continue
    const source = byId.get(edge.from)?.kind ?? "missing"
    const target = byId.get(edge.to)?.kind ?? "missing"
    from[source] = (from[source] ?? 0) + 1
    to[target] = (to[target] ?? 0) + 1
  }
  return { from, to }
}
