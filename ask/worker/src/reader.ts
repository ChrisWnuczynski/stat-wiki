import type { Graph } from "../../core/graph.ts"
import { pagePath } from "../../core/text.ts"

export function chapterFor(graph: Graph, page: string, anchor: string): string {
  const path = pagePath(page)
  if (!path) return ""
  const entries = [...graph.byId.values()].filter((entry) => pagePath(entry.url) === path)
  const hash = anchor.replace(/^#/, "")
  if (hash) {
    const named = graph.byId.get(hash)
    if (named && pagePath(named.url) === path) return graph.chapterOf(named.id) ?? ""
    const anchored = entries.find((entry) => (entry.url.split("#")[1] ?? "") === hash)
    if (anchored) return graph.chapterOf(anchored.id) ?? ""
  }
  const chapter = entries.find((entry) => entry.kind === "chapter")
  if (chapter) return chapter.id
  for (const entry of entries) {
    const id = graph.chapterOf(entry.id)
    if (id) return id
  }
  return ""
}
