// Pure text helpers for the chat. No DOM, so they run under node --test.

export type MathPiece = { tex: string; display: boolean }

export type Citation = { number: number; id: string; title: string; kind: string; url: string }

export type Msg = {
  id: string
  role: "user" | "assistant"
  content: string
  citations?: Citation[]
  covered?: boolean
  state?: "streaming" | "done" | "error" | "interrupted"
  error?: string
}

export type Turn = { role: "user" | "assistant"; content: string }

// The Worker's limits (ask/core/config.ts and ask/worker/src/body.ts).
export const MAX_TURNS = 6
export const QUESTION_CHARS = 2000
export const ASSISTANT_CHARS = 8000

// Private-use characters mark where a formula was lifted out of the text.
const OPEN = ""
const CLOSE = ""
export const MATH_TOKEN = /(\d+)/g

const CODE = /(```[\s\S]*?(?:```|$)|`[^`\n]*`)/g

/** Apply `fn` to the parts of `text` that are not code. */
export function mapOutsideCode(text: string, fn: (part: string) => string): string {
  return text.split(CODE).map((part, i) => (i % 2 === 1 ? part : fn(part))).join("")
}

/** Turn \( \) and \[ \] into $ and $$, the delimiters the wiki uses. */
export function normalizeDelimiters(text: string): string {
  return mapOutsideCode(text, (part) =>
    part
      .replace(/\\\[([\s\S]+?)\\\]/g, (_m, tex: string) => `$$${tex}$$`)
      .replace(/\\\(([\s\S]+?)\\\)/g, (_m, tex: string) => `$${tex}$`))
}

/**
 * Lift formulas out before Markdown sees them, so underscores and asterisks
 * inside maths are not read as emphasis. "$5 and $10" is not maths: an inline
 * formula cannot start or end with a space, and cannot be followed by a digit.
 */
export function extractMath(text: string): { text: string; maths: MathPiece[] } {
  const maths: MathPiece[] = []
  const lift = (tex: string, display: boolean) => {
    maths.push({ tex: tex.trim(), display })
    return `${OPEN}${maths.length - 1}${CLOSE}`
  }
  const out = mapOutsideCode(text, (part) =>
    part
      .replace(/\$\$([\s\S]+?)\$\$/g, (_m, tex: string) => lift(tex, true))
      .replace(/\$(?!\s)((?:\\.|[^$\n\\])+?)(?<!\s)\$(?!\d)/g, (_m, tex: string) => lift(tex, false)))
  return { text: out, maths }
}

/**
 * Replace [n] and [n, m] with citation buttons for the numbers the Worker
 * returned. Numbers it did not return are dropped, so a stray [9] never shows.
 */
export function linkCitations(html: string, known: ReadonlySet<number>): string {
  // The space before a marker goes too: the button sits against its word, like a footnote mark.
  return html.replace(/[ \t]?\[(\d+(?:\s*,\s*\d+)*)\]/g, (_match, list: string) => {
    const numbers = list.split(",").map((n) => Number(n.trim())).filter((n) => known.has(n))
    return numbers
      .map((n) => `<button type="button" class="ask-cite" data-n="${n}" aria-label="Source ${n}">${n}</button>`)
      .join("")
  })
}

export function escapeHtml(text: string): string {
  return text.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c] as string)
}

/** The turns sent with a question: the last few exchanges, within the Worker's limits. */
export function buildTurns(history: Msg[], question: string): Turn[] {
  const turns: Turn[] = []
  for (const msg of history) {
    if (msg.role === "assistant" && (msg.state !== "done" || !msg.content.trim())) continue
    const limit = msg.role === "user" ? QUESTION_CHARS : ASSISTANT_CHARS
    turns.push({ role: msg.role, content: msg.content.slice(0, limit) })
  }
  turns.push({ role: "user", content: question.slice(0, QUESTION_CHARS) })
  // Keep the newest turns, and start on a question.
  let kept = turns.slice(-MAX_TURNS)
  while (kept.length > 1 && kept[0].role !== "user") kept = kept.slice(1)
  return kept
}

/** Graph anchors the Worker can map to a chapter. */
export const ANCHOR = /^(s-|def-|thm-|prp-|cor-|rem-|exm-|ex-|exr-|sol-|fig-|sec-)/

/** The Worker accepts only plain root-relative paths. */
export function safePage(path: string): string {
  return /^\/[A-Za-z0-9._~/-]*$/.test(path) ? path : ""
}
