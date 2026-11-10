import { ANSWER_MODEL, DEFAULT_DAILY_BUDGET, EMBEDDING_MODEL, QUERY_INSTRUCTION, SESSION_TTL_SECONDS, WIKI_URL, WORKER_K, WORKER_MAX_TOKENS } from "../../core/config.ts"
import { buildGraph, type Graph } from "../../core/graph.ts"
import type { WikiDoc } from "../../core/types.ts"
import { streamChat } from "../../core/xai.ts"
import { AskBudget } from "./budget.ts"
import { handleAsk, type AskDeps } from "./handler.ts"
import { killEnabled } from "./gate.ts"
import { chapterFor } from "./reader.ts"
import { hashIp, signSession, verifySession } from "./session.ts"

export { AskBudget }

type Env = {
  AI: { run(model: string, input: unknown): Promise<unknown> }
  VECTORS: {
    query(vector: number[], options: { topK: number; returnMetadata: "all" }): Promise<{
      matches?: { id: string; score: number; metadata?: Record<string, unknown> | null }[]
    }>
  }
  CHUNKS: { get(key: string): Promise<string | null> }
  BUDGET: {
    idFromName(name: string): unknown
    get(id: unknown): { fetch(input: string, init?: RequestInit): Promise<Response> }
  }
  XAI_API_KEY: string
  TURNSTILE_SECRET: string
  SESSION_SECRET: string
  DEV_ASK_TOKEN: string
  ASK_KILL: string
  ASK_DAILY_BUDGET: string
  COVERAGE_THRESHOLD: string
}

function vectorsOf(result: unknown): number[][] {
  const record = result && typeof result === "object" ? result as { data?: unknown; result?: { data?: unknown } } : {}
  const data = Array.isArray(record.data) ? record.data : record.result?.data
  if (!Array.isArray(data) || !Array.isArray(data[0])) throw new Error("embed")
  return data as number[][]
}

function budgetOf(value: string | undefined): number {
  const parsed = Number(value)
  if (!Number.isFinite(parsed) || parsed < 0) return DEFAULT_DAILY_BUDGET
  return Math.floor(parsed)
}

function thresholdOf(value: string | undefined): number {
  const parsed = Number(value)
  if (!Number.isFinite(parsed)) return 0.41
  return parsed
}

let graphPromise: Promise<Graph> | null = null

function readerGraph(): Promise<Graph> {
  if (!graphPromise) {
    graphPromise = fetch(WIKI_URL, { headers: { "user-agent": "statwiki-ask/1.0" } }).then(async (response) => {
      if (!response.ok) throw new Error("wiki")
      return buildGraph(await response.json() as WikiDoc)
    })
    graphPromise.catch(() => {
      graphPromise = null
    })
  }
  return graphPromise
}

function deps(env: Env): AskDeps {
  return {
    now: () => new Date(),
    devToken: env.DEV_ASK_TOKEN ?? "",
    kill: killEnabled(env.ASK_KILL),
    budget: budgetOf(env.ASK_DAILY_BUDGET),
    threshold: thresholdOf(env.COVERAGE_THRESHOLD),
    k: WORKER_K,
    sessionTtl: SESSION_TTL_SECONDS,
    verifySession: (token, nowSec) => verifySession(env.SESSION_SECRET ?? "", token, nowSec),
    signSession: (sid, exp) => signSession(env.SESSION_SECRET ?? "", sid, exp),
    verifyTurnstile: async (token, ip) => {
      const secret = env.TURNSTILE_SECRET?.trim() ?? ""
      if (!secret) throw new Error("turnstile")
      const form = new FormData()
      form.set("secret", secret)
      form.set("response", token)
      if (ip) form.set("remoteip", ip)
      const response = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", { method: "POST", body: form })
      if (!response.ok) throw new Error("turnstile")
      const json = await response.json() as { success?: boolean }
      return json.success === true
    },
    admit: async (input) => {
      const stub = env.BUDGET.get(env.BUDGET.idFromName("global"))
      const response = await stub.fetch("https://budget.internal/admit", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
          sessionId: input.sessionId,
          ipHash: input.ipHash,
          day: input.day,
          kill: killEnabled(env.ASK_KILL),
          budget: budgetOf(env.ASK_DAILY_BUDGET),
          quotas: input.quotas,
        }),
      })
      const json = await response.json() as { ok?: boolean; reason?: "kill" | "budget" | "session" | "ip" }
      if (json.ok === true) return { ok: true }
      return { ok: false, reason: json.reason ?? "budget" }
    },
    embedQuery: async (text) => {
      const result = await env.AI.run(EMBEDDING_MODEL, { queries: [text], instruction: QUERY_INSTRUCTION })
      const vectors = vectorsOf(result)
      const vector = vectors[0]
      if (!vector) throw new Error("embed")
      return vector
    },
    queryVectors: async (vector, topK) => {
      const result = await env.VECTORS.query(vector, { topK, returnMetadata: "all" })
      return (result.matches ?? []).map((match) => ({
        id: String(match.id),
        score: Number(match.score),
        metadata: match.metadata ?? {},
      }))
    },
    getChunks: async (ids) => new Map(await Promise.all(ids.map(async (id) => [id, await env.CHUNKS.get(id)] as const))),
    definesTargets: async () => (await readerGraph()).definesTargets,
    chapterId: async (page, anchor) => chapterFor(await readerGraph(), page, anchor),
    streamAnswer: async function* (input) {
      const stream = await streamChat({
        apiKey: env.XAI_API_KEY ?? "",
        model: ANSWER_MODEL,
        system: input.system,
        user: input.user,
        maxTokens: WORKER_MAX_TOKENS,
      })
      const reader = stream.getReader()
      try {
        for (;;) {
          const { done, value } = await reader.read()
          if (done) return
          if (value) yield value
        }
      } finally {
        reader.releaseLock()
      }
    },
    hashIp: (ip) => hashIp(env.SESSION_SECRET ?? "", ip),
    log: (event) => {
      console.log(JSON.stringify(event))
    },
  }
}

export default {
  fetch(request: Request, env: Env): Promise<Response> {
    return handleAsk(request, deps(env))
  },
}
