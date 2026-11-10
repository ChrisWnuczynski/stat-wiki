import { sha256Hex } from "./text.ts"
import { CHUNK_CHARS } from "./config.ts"
import type { Chunk, WikiDoc, WikiEntry } from "./types.ts"
import { buildGraph } from "./graph.ts"

type Range = [number, number]

function isEscaped(text: string, index: number): boolean {
  let slashes = 0
  for (let i = index - 1; i >= 0 && text[i] === "\\"; i--) slashes++
  return slashes % 2 === 1
}

function protectedRanges(text: string): Range[] {
  const ranges: Range[] = []
  let i = 0
  while (i < text.length) {
    if (text.startsWith("```", i)) {
      const close = text.indexOf("```", i + 3)
      if (close < 0) {
        ranges.push([i, text.length])
        break
      }
      ranges.push([i, close + 3])
      i = close + 3
      continue
    }
    if (text.startsWith("$$", i) && !isEscaped(text, i)) {
      const close = text.indexOf("$$", i + 2)
      if (close < 0) {
        i += 2
        continue
      }
      ranges.push([i, close + 2])
      i = close + 2
      continue
    }
    if (text.startsWith("\\begin{", i)) {
      const nameEnd = text.indexOf("}", i + 7)
      const name = nameEnd > i ? text.slice(i + 7, nameEnd) : ""
      if (/^[A-Za-z*]+$/.test(name)) {
        const open = `\\begin{${name}}`
        const closeToken = `\\end{${name}}`
        let depth = 1
        let j = nameEnd + 1
        while (j < text.length && depth > 0) {
          const nextOpen = text.indexOf(open, j)
          const nextClose = text.indexOf(closeToken, j)
          if (nextClose < 0) {
            j = text.length
            break
          }
          if (nextOpen >= 0 && nextOpen < nextClose) {
            depth++
            j = nextOpen + open.length
          } else {
            depth--
            j = nextClose + closeToken.length
          }
        }
        ranges.push([i, j])
        i = j
        continue
      }
    }
    if (text[i] === "$" && !isEscaped(text, i)) {
      let close = -1
      for (let j = i + 1; j < text.length; j++) {
        if (text[j] === "$" && !isEscaped(text, j)) {
          close = j
          break
        }
      }
      if (close < 0) {
        i += 1
        continue
      }
      ranges.push([i, close + 1])
      i = close + 1
      continue
    }
    i++
  }
  return ranges
}

function inside(ranges: Range[], index: number): boolean {
  for (const [start, end] of ranges) {
    if (index < start) return false
    if (index >= start && index < end) return true
  }
  return false
}

export function splitBody(text: string, maxChars = CHUNK_CHARS): string[] {
  const trimmed = text.trim()
  if (!trimmed) return []
  const ranges = protectedRanges(trimmed)
  const breaks: number[] = []
  const pattern = /\n[ \t]*\n/g
  let match: RegExpExecArray | null
  while ((match = pattern.exec(trimmed))) {
    if (!inside(ranges, match.index)) breaks.push(match.index + match[0].length)
  }
  const cuts = [0, ...breaks, trimmed.length]
  const parts: string[] = []
  let current = ""
  for (let i = 0; i < cuts.length - 1; i++) {
    const segment = trimmed.slice(cuts[i], cuts[i + 1])
    if (!segment) continue
    if (!current) {
      current = segment
      continue
    }
    if (current.length + segment.length <= maxChars) current += segment
    else {
      parts.push(current)
      current = segment
    }
  }
  if (current) parts.push(current)
  return parts
}

export function headerLine(chapterTitle: string | null, title: string, kind: string): string {
  const clean = (value: string) => value.replace(/\s+/g, " ").trim()
  const label = `${clean(title)} (${kind})`
  const chapter = chapterTitle ? clean(chapterTitle) : ""
  return chapter ? `${chapter} › ${label}` : label
}

export function chunkEntry(
  entry: Pick<WikiEntry, "id" | "kind" | "title" | "text" | "url" | "fingerprint">,
  chapterTitle: string | null,
  chapterId: string | null,
  maxChars = CHUNK_CHARS,
): Chunk[] {
  if (!entry.text?.trim()) return []
  const header = headerLine(chapterTitle, entry.title, entry.kind)
  return splitBody(entry.text, maxChars).map((body, part) => ({
    id: `${entry.id}#${part}`,
    entryId: entry.id,
    part,
    text: `${header}\n\n${body}`,
    url: entry.url,
    title: entry.title,
    kind: entry.kind,
    chapterId,
    chapterTitle,
    // The header is part of what is embedded, so a title change re-embeds too.
    fingerprint: sha256Hex(`${entry.fingerprint}\n${header}`),
  }))
}

export function chunkDocument(doc: WikiDoc, maxChars = CHUNK_CHARS): Chunk[] {
  const graph = buildGraph(doc)
  const chunks: Chunk[] = []
  const entries = [...doc.entries].sort((a, b) => a.id.localeCompare(b.id))
  for (const entry of entries) {
    if (!entry.text?.trim() || entry.copy_of) continue
    const chapterId = graph.chapterOf(entry.id)
    const chapterTitle = chapterId ? graph.byId.get(chapterId)?.title ?? null : null
    chunks.push(...chunkEntry(entry, chapterTitle, chapterId, maxChars))
  }
  return chunks
}
