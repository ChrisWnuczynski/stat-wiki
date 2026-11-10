// The Worker's own handler, wired to the real index, chunk store and model,
// for checks run from a terminal. Nothing is deployed and no bypass is used:
// each request carries a session signed here.

import { Cloudflare } from "../core/cloudflare.ts"
import { COVERAGE_THRESHOLD, WORKER_K, WORKER_MAX_TOKENS } from "../core/config.ts"
import type { Graph } from "../core/graph.ts"
import { streamChat } from "../core/xai.ts"
import { handleAsk } from "../worker/src/handler.ts"
import { chapterFor, pageEntryFor } from "../worker/src/reader.ts"
import { signSession, verifySession } from "../worker/src/session.ts"
import { chat, modelSpec } from "./answers.ts"

export type LocalReply = {
  status: number
  covered: boolean
  reply: string
  citations: { number: number; id: string; title: string; kind: string; url: string }[]
}

export type LocalAsk = (question: string, options?: { page?: string; anchor?: string }) => Promise<LocalReply>

function events(text: string): { event: string; data: Record<string, unknown> }[] {
  return text.split("\n\n").filter((block) => block.includes("event:")).map((block) => {
    const event = block.split("\n").find((line) => line.startsWith("event:"))?.slice(6).trim() ?? ""
    const raw = block.split("\n").find((line) => line.startsWith("data:"))?.slice(5).trim() ?? "{}"
    return { event, data: JSON.parse(raw) as Record<string, unknown> }
  })
}

/** Ask through the Worker's handler with model `spec` ("grok-4.7" or "grok-4.7@low"). */
export async function localAsk(client: Cloudflare, graph: Graph, spec: string, apiKey: string): Promise<{ ask: LocalAsk; modelCalls: () => number }> {
  const secret = "local-check"
  const session = await signSession(secret, "local-check", Math.floor(Date.now() / 1000) + 3600)
  let calls = 0
  const deps = {
    now: () => new Date(),
    kill: false,
    budget: 1_000_000,
    threshold: COVERAGE_THRESHOLD,
    k: WORKER_K,
    sessionTtl: 3600,
    verifySession: (token: string, now: number) => verifySession(secret, token, now),
    signSession: (sid: string, exp: number) => signSession(secret, sid, exp),
    verifyTurnstile: async () => false,
    admit: async () => ({ ok: true as const }),
    embedQuery: (text: string) => client.embedQuery(text),
    queryVectors: (vector: number[], topK: number) => client.query(vector, topK),
    getChunks: (ids: string[]) => client.kvGetMany(ids),
    definesTargets: async () => graph.definesTargets,
    chapterId: async (page: string, anchor: string) => chapterFor(graph, page, anchor),
    pageEntry: async (page: string, anchor: string) => pageEntryFor(graph, page, anchor),
    streamAnswer: async function* (input: { system: string; user: string }) {
      calls += 1
      const { model, effort } = modelSpec(spec)
      if (effort) {
        // The harness client sends the thinking level and survives the proxy's 30 s cut-off.
        yield (await chat(spec, input.system, input.user, WORKER_MAX_TOKENS)).text
        return
      }
      const stream = await streamChat({ apiKey, model, system: input.system, user: input.user, maxTokens: WORKER_MAX_TOKENS })
      const reader = stream.getReader()
      for (;;) {
        const { done, value } = await reader.read()
        if (done) return
        if (value) yield value
      }
    },
    hashIp: async () => "local",
    log: () => {},
  }
  const ask: LocalAsk = async (question, options = {}) => {
    const response = await handleAsk(new Request("https://ask.statwiki.io/ask", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ turns: [{ role: "user", content: question }], page: options.page ?? "", anchor: options.anchor ?? "", session }),
    }), deps)
    const parsed = events(await response.text())
    return {
      status: response.status,
      covered: parsed.find((event) => event.event === "status")?.data.covered === true,
      reply: parsed.filter((event) => event.event === "delta").map((event) => String(event.data.text ?? "")).join(""),
      citations: (parsed.find((event) => event.event === "citations")?.data.citations ?? []) as LocalReply["citations"],
    }
  }
  return { ask, modelCalls: () => calls }
}
