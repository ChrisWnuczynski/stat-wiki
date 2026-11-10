import { FETCH_K, NOT_COVERED_REPLY, RESTING_MESSAGE } from "../../core/config.ts"
import { publicCitations } from "../../core/citations.ts"
import { buildPrompt } from "../../core/prompt.ts"
import { DEFAULT_BOOSTS, isCovered, packPassages, rerank } from "../../core/retrieve.ts"
import { rankMatches, takePool, textsFromStored, type ScoredMatch } from "../../core/select.ts"
import { estimateTokens } from "../../core/text.ts"
import { parseAskBody } from "./body.ts"
import { corsHeaders, originDenied } from "./cors.ts"
import type { AdmitReason } from "./gate.ts"
import { newSessionId } from "./session.ts"

export type LogEvent = Record<string, string | number>

export type AskDeps = {
  now(): Date
  kill: boolean
  budget: number
  threshold: number
  k: number
  verifySession(token: string, nowSec: number): Promise<{ sid: string } | null>
  signSession(sid: string, exp: number): Promise<string>
  sessionTtl: number
  verifyTurnstile(token: string, ip: string): Promise<boolean>
  admit(input: { sessionId: string; ipHash: string; day: string; quotas: boolean }): Promise<{ ok: true } | { ok: false; reason: AdmitReason }>
  embedQuery(text: string): Promise<number[]>
  queryVectors(vector: number[], topK: number): Promise<ScoredMatch[]>
  getChunks(ids: string[]): Promise<Map<string, string | null>>
  definesTargets(): Promise<Set<string>>
  chapterId(page: string, anchor: string): Promise<string>
  streamAnswer(input: { system: string; user: string }): AsyncIterable<string>
  hashIp(ip: string): Promise<string>
  log(event: LogEvent): void
}

function json(status: number, body: unknown, cors: Headers): Response {
  const headers = new Headers(cors)
  headers.set("content-type", "application/json; charset=utf-8")
  headers.set("cache-control", "no-store")
  return new Response(JSON.stringify(body), { status, headers })
}

function sse(body: BodyInit, cors: Headers): Response {
  const headers = new Headers(cors)
  headers.set("content-type", "text/event-stream; charset=utf-8")
  headers.set("cache-control", "no-store")
  return new Response(body, { status: 200, headers })
}

function encode(events: [string, unknown][]): string {
  return events.map(([event, data]) => `event: ${event}\ndata: ${JSON.stringify(data)}\n\n`).join("")
}

function clientIp(request: Request): string {
  return request.headers.get("cf-connecting-ip")?.trim() || ""
}


export async function handleAsk(request: Request, deps: AskDeps): Promise<Response> {
  const url = new URL(request.url)
  const origin = request.headers.get("origin")
  const cors = corsHeaders(origin)
  if (request.method === "OPTIONS") {
    if (originDenied(origin)) return json(403, { error: "This origin is not allowed." }, cors)
    return new Response(null, { status: 204, headers: cors })
  }
  if (originDenied(origin)) return json(403, { error: "This origin is not allowed." }, cors)
  if (request.method === "GET" && (url.pathname === "/" || url.pathname === "/health")) {
    return json(200, { ok: true }, cors)
  }
  if (request.method === "POST" && url.pathname === "/session") return openSession(request, deps, cors)
  if (request.method === "POST" && url.pathname === "/ask") return answer(request, deps, cors)
  return json(404, { error: "Not found." }, cors)
}

async function openSession(request: Request, deps: AskDeps, cors: Headers): Promise<Response> {
  let token = ""
  try {
    const jsonBody = await request.json() as { turnstile?: unknown }
    token = typeof jsonBody.turnstile === "string" ? jsonBody.turnstile : ""
  } catch {
    return json(400, { error: "The request body must be JSON." }, cors)
  }
  if (!token || token.length > 4000) return json(400, { error: "A Turnstile token is required." }, cors)
  let passed = false
  try {
    passed = await deps.verifyTurnstile(token, clientIp(request))
  } catch {
    deps.log({ kind: "error", result: "turnstile", status: 0 })
    return json(503, { error: "Ask StatWiki could not check the browser." }, cors)
  }
  if (!passed) {
    deps.log({ kind: "session", result: "rejected" })
    return json(403, { error: "The browser check failed." }, cors)
  }
  const nowSec = Math.floor(deps.now().getTime() / 1000)
  const session = await deps.signSession(newSessionId(), nowSec + deps.sessionTtl)
  deps.log({ kind: "session", result: "ok" })
  return json(200, { session, expires: nowSec + deps.sessionTtl }, cors)
}

async function answer(request: Request, deps: AskDeps, cors: Headers): Promise<Response> {
  const raw = await request.text()
  const parsed = parseAskBody(raw)
  if (!parsed.ok) return json(400, { error: parsed.error }, cors)
  const body = parsed.body
  const question = body.turns[body.turns.length - 1]?.content ?? ""
  // Every question needs a session from the Turnstile check. There is no other way in.
  const verified = await deps.verifySession(body.session, Math.floor(deps.now().getTime() / 1000))
  if (!verified) return json(401, { error: "A session token is required." }, cors)
  const sessionId = verified.sid
  const day = deps.now().toISOString().slice(0, 10)
  const ipHash = await deps.hashIp(clientIp(request) || "unknown")
  const decision = await deps.admit({ sessionId, ipHash, day, quotas: true })
  if (!decision.ok) {
    if (decision.reason === "kill" || decision.reason === "budget") {
      deps.log({ kind: "ask", result: "resting", reason: decision.reason })
      return sse(encode([
        ["delta", { text: RESTING_MESSAGE }],
        ["citations", { citations: [] }],
      ]), cors)
    }
    deps.log({ kind: "ask", result: "limited", reason: decision.reason })
    return json(429, { error: "Too many questions for today." }, cors)
  }

  let prompt: { system: string; user: string }
  let cited: { n: number; entryId: string; url: string; title: string; kind: string }[]
  let covered = true
  try {
    const vector = await deps.embedQuery(question)
    const matches = await deps.queryVectors(vector, FETCH_K)
    const ranked = rankMatches(matches)
    const pool = takePool(ranked, "open", new Set(), matches.length)
    const texts = textsFromStored(await deps.getChunks(pool.candidates.map((candidate) => candidate.chunkId)))
    const definesTargets = await deps.definesTargets()
    const chapterId = await deps.chapterId(body.page, body.anchor)
    const reranked = rerank(question, pool.candidates, {
      ...DEFAULT_BOOSTS,
      definesTargets,
      pagePath: body.page,
      chapterId,
    })
    const packed = packPassages(reranked, texts, deps.k)
    const byChunk = new Map(reranked.map((candidate) => [candidate.chunkId, candidate]))
    cited = packed.map((passage) => {
      const candidate = byChunk.get(passage.chunkId)
      return {
        n: passage.n,
        entryId: passage.entryId,
        url: passage.url,
        title: candidate?.title ?? "",
        kind: candidate?.kind ?? "",
      }
    })
    covered = isCovered(pool.best, deps.threshold)
    prompt = buildPrompt({
      question,
      passages: packed.map((passage) => ({ n: passage.n, text: passage.text })),
      covered,
      history: body.turns.slice(0, -1),
    })
  } catch {
    deps.log({ kind: "error", result: "retrieve", status: 0 })
    return json(502, { error: "Ask failed." }, cors)
  }

  // Nothing in StatWiki is close enough: reply without calling the model.
  if (!covered) {
    deps.log({ kind: "ask", result: "not covered" })
    const events: [string, unknown][] = []
    events.push(["status", { covered: false }], ["delta", { text: NOT_COVERED_REPLY }], ["citations", { citations: [] }])
    return sse(encode(events), cors)
  }

  const started = Date.now()
  const stream = new ReadableStream({
    async start(controller) {
      const encoder = new TextEncoder()
      const send = (event: string, data: unknown) => {
        controller.enqueue(encoder.encode(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`))
      }
      // The model can think for a minute before its first word. An SSE comment
      // every 15 s keeps the connection from looking idle; clients ignore it.
      const keepAlive = setInterval(() => controller.enqueue(encoder.encode(": thinking\n\n")), 15_000)
      try {
        send("status", { covered: true })
        let full = ""
        for await (const piece of deps.streamAnswer(prompt)) {
          if (!piece) continue
          full += piece
          send("delta", { text: piece })
        }
        send("citations", { citations: publicCitations(full, cited) })
        deps.log({
          kind: "ask",
          result: "ok",
          passages: cited.length,
          tokens: estimateTokens(full),
          ms: Date.now() - started,
        })
      } catch {
        deps.log({ kind: "error", result: "model", status: 0 })
        send("error", { error: "Ask failed." })
        send("citations", { citations: [] })
      } finally {
        clearInterval(keepAlive)
        controller.close()
      }
    },
  })
  return sse(stream, cors)
}
