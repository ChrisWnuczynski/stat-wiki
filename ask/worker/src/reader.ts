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

export type PageEntry = { entryId: string; chunkId: string; title: string; kind: string; url: string }

const PAGE_KINDS = new Set(["chapter", "article", "question"])

/**
 * What the reader is looking at: the entry for the anchor in view if it is on
 * this page, otherwise the page's own entry. The chunk is the first part of the
 * entry's text, or of the entry it copies.
 */
export function pageEntryFor(graph: Graph, page: string, anchor: string): PageEntry | null {
  const path = pagePath(page)
  if (!path) return null
  const onPage = [...graph.byId.values()].filter((entry) => pagePath(entry.url) === path)
  const hash = anchor.replace(/^#/, "")
  const fragment = (entry: { url: string }) => entry.url.split("#")[1] ?? ""
  const pick = (hash ? onPage.find((entry) => fragment(entry) === hash) : undefined)
    ?? onPage.find((entry) => !fragment(entry) && PAGE_KINDS.has(entry.kind))
    ?? onPage.find((entry) => !fragment(entry))
  if (!pick) return null
  const source = pick.copy_of ? graph.byId.get(pick.copy_of) ?? pick : pick
  if (!source.text) return null
  const chapterId = pick.kind === "chapter" ? "" : graph.chapterOf(pick.id) ?? ""
  const chapter = chapterId ? graph.byId.get(chapterId) : undefined
  const title = chapter && chapter.title !== pick.title ? `${chapter.title} › ${pick.title}` : pick.title
  return { entryId: pick.id, chunkId: `${source.id}#0`, title, kind: pick.kind, url: pick.url }
}
