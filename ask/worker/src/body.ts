import { MAX_TURNS, QUESTION_CHAR_LIMIT } from "../../core/config.ts"

const MAX_BODY = 48_000
const ASSISTANT_CHAR_LIMIT = 8000

export type Turn = { role: "user" | "assistant"; content: string }

export type AskBody = {
  turns: Turn[]
  page: string
  anchor: string
  session: string
  exclude: string[]
  compare: boolean
}

export type BodyResult = { ok: true; body: AskBody } | { ok: false; error: string }

function pageOk(page: string): boolean {
  if (!page) return true
  if (!page.startsWith("/") || page.includes("..") || /[\s?#]/.test(page)) return false
  return /^\/[A-Za-z0-9._~/-]*$/.test(page)
}

export function parseAskBody(raw: string): BodyResult {
  if (raw.length > MAX_BODY) return { ok: false, error: "The request is too large." }
  let json: unknown
  try {
    json = JSON.parse(raw)
  } catch {
    return { ok: false, error: "The request body must be JSON." }
  }
  if (!json || typeof json !== "object") return { ok: false, error: "The request body must be JSON." }
  const record = json as Record<string, unknown>
  if (!Array.isArray(record.turns) || record.turns.length < 1 || record.turns.length > MAX_TURNS) {
    return { ok: false, error: "Send at most 6 turns." }
  }
  const turns: Turn[] = []
  for (const turn of record.turns) {
    if (!turn || typeof turn !== "object") return { ok: false, error: "Each turn needs a role and text." }
    const role = (turn as { role?: unknown }).role
    const content = (turn as { content?: unknown }).content
    if ((role !== "user" && role !== "assistant") || typeof content !== "string") {
      return { ok: false, error: "Each turn needs a role and text." }
    }
    const limit = role === "user" ? QUESTION_CHAR_LIMIT : ASSISTANT_CHAR_LIMIT
    if (content.length > limit) {
      return {
        ok: false,
        error: role === "user" ? "Questions are limited to 2000 characters." : "A turn is too long.",
      }
    }
    turns.push({ role, content })
  }
  const last = turns[turns.length - 1]
  if (!last || last.role !== "user" || !last.content.trim()) return { ok: false, error: "The last turn must be a question." }
  const page = typeof record.page === "string" ? record.page : ""
  const anchor = typeof record.anchor === "string" ? record.anchor : ""
  if (!pageOk(page)) return { ok: false, error: "The page path is not valid." }
  if (anchor.length > 200 || /[\r\n]/.test(anchor)) return { ok: false, error: "The anchor is not valid." }
  const session = typeof record.session === "string" ? record.session.slice(0, 4000) : ""
  const exclude = Array.isArray(record.exclude)
    ? record.exclude.filter((id): id is string => typeof id === "string" && id.length > 0 && id.length <= 200).slice(0, 40)
    : []
  return { ok: true, body: { turns, page, anchor, session, exclude, compare: record.compare === true } }
}
