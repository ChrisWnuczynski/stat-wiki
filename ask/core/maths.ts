import { createRequire } from "node:module"
import { dirname, resolve } from "node:path"
import { fileURLToPath } from "node:url"

type Katex = {
  renderToString: (tex: string, options: { throwOnError: boolean; displayMode: boolean }) => string
}

const require = createRequire(import.meta.url)
const katexPath = resolve(dirname(fileURLToPath(import.meta.url)), "../../katex/katex.min.js")
const katex = require(katexPath) as Katex

const MATH_ENVS = "align\\*|align|aligned|cases|pmatrix|bmatrix|vmatrix|gathered|smallmatrix|equation\\*|equation"

export function mathSpans(text: string): string[] {
  const spans: string[] = []
  const consumed: Array<[number, number]> = []
  const take = (pattern: RegExp) => {
    for (const match of text.matchAll(pattern)) {
      const start = match.index ?? 0
      const end = start + match[0].length
      if (consumed.some(([a, b]) => start >= a && start < b)) continue
      consumed.push([start, end])
      spans.push(match[0])
    }
  }
  take(/\$\$[\s\S]+?\$\$/g)
  take(/(?<!\$)\$(?!\$)(?:\\.|[^$\n])+\$/g)
  take(new RegExp(`\\\\begin\\{(${MATH_ENVS})\\}[\\s\\S]*?\\\\end\\{\\1\\}`, "g"))
  return spans
}

export function spanRenders(span: string): boolean {
  const display = span.startsWith("$$") || span.startsWith("\\begin")
  const tex = span.startsWith("$$") ? span.slice(2, -2).trim() : span.startsWith("$") ? span.slice(1, -1).trim() : span
  try {
    katex.renderToString(tex, { throwOnError: true, displayMode: display })
    return true
  } catch {
    return false
  }
}

export function mathsReport(text: string): { spans: number; failures: number; ok: boolean } {
  const spans = mathSpans(text)
  let failures = 0
  for (const span of spans) if (!spanRenders(span)) failures++
  return { spans: spans.length, failures, ok: failures === 0 }
}
