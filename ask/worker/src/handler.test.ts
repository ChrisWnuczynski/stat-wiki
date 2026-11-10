import assert from "node:assert/strict"
import { dirname, resolve } from "node:path"
import test from "node:test"
import { fileURLToPath } from "node:url"

import { IP_DAILY_LIMIT, RESTING_MESSAGE, SESSION_DAILY_LIMIT, SESSION_TTL_SECONDS } from "../../core/config.ts"
import { buildPrompt } from "../../core/prompt.ts"
import { readJsonl, type MisusePrompt } from "../../core/questions.ts"
import type { ScoredMatch } from "../../core/select.ts"
import { sha256Hex } from "../../core/text.ts"
import { looksDeclined } from "../../core/xai.ts"
import { handleAsk, type AskDeps, type LogEvent } from "./handler.ts"
import { emptyDay, nextDayState, type DayState } from "./gate.ts"
import { signSession, verifySession } from "./session.ts"

const here = dirname(fileURLToPath(import.meta.url))
const SECRET = "session-secret"
const NOW = new Date("2026-11-10T12:00:00Z")

function match(entryId: string, score: number, url: string, chapterId: string): ScoredMatch {
  return {
    id: entryId,
    score,
    metadata: {
      chunkId: `${entryId}#0`,
      entryId,
      title: entryId,
      kind: "section",
      url,
      chapterId,
    },
  }
}

function sse(text: string): { event: string; data: Record<string, unknown> }[] {
  return text.split("\n\n").filter(Boolean).map((block) => {
    const event = block.split("\n").find((line) => line.startsWith("event:"))?.slice(6).trim() ?? ""
    const raw = block.split("\n").find((line) => line.startsWith("data:"))?.slice(5).trim() ?? "{}"
    return { event, data: JSON.parse(raw) as Record<string, unknown> }
  })
}

function harness(options?: {
  answer?: string
  kill?: boolean
  budget?: number
  k?: number
  matches?: ScoredMatch[]
  devToken?: string
}): { deps: AskDeps; calls: { model: number; users: string[] }; logs: LogEvent[]; state: { day: DayState } } {
  const state = { day: emptyDay() }
  const calls = { model: 0, users: [] as string[] }
  const logs: LogEvent[] = []
  const matches = options?.matches ?? [match("section:mean", 0.8, "/notes/a.html#mean", "chapter:a")]
  const deps: AskDeps = {
    now: () => NOW,
    devToken: options?.devToken ?? "dev-secret",
    kill: options?.kill ?? false,
    budget: options?.budget ?? 400,
    threshold: 0.41,
    k: options?.k ?? 8,
    sessionTtl: SESSION_TTL_SECONDS,
    verifySession: (token, nowSec) => verifySession(SECRET, token, nowSec),
    signSession: (sid, exp) => signSession(SECRET, sid, exp),
    verifyTurnstile: async (token) => token === "turnstile-ok",
    admit: async (input) => {
      const step = nextDayState(state.day, {
        sessionId: input.sessionId,
        ipHash: input.ipHash,
        kill: options?.kill ?? false,
        budget: options?.budget ?? 400,
        quotas: input.quotas,
      })
      if (!step.decision.ok) return step.decision
      state.day = step.state
      return { ok: true }
    },
    embedQuery: async () => [0.1, 0.2],
    queryVectors: async () => matches,
    getChunks: async (ids) => new Map(ids.map((id) => [id, JSON.stringify({ text: `Text for ${id}` })])),
    definesTargets: async () => new Set<string>(),
    chapterId: async () => "chapter:a",
    streamAnswer: async function* (input) {
      calls.model += 1
      calls.users.push(input.user)
      yield options?.answer ?? "I can only help with statistics, probability, data analysis, or R."
    },
    hashIp: async () => "ip-hash",
    log: (event) => logs.push(event),
  }
  return { deps, calls, logs, state }
}

async function session(): Promise<string> {
  return signSession(SECRET, "reader", Math.floor(NOW.getTime() / 1000) + 60)
}

function ask(body: unknown, headers: Record<string, string> = {}, url = "https://statwiki-ask.example.workers.dev/ask"): Request {
  return new Request(url, {
    method: "POST",
    headers: { "content-type": "application/json", ...headers },
    body: JSON.stringify(body),
  })
}

test("turnstile opens one session and a later ask uses it", async () => {
  const { deps, calls } = harness({ answer: "[1] The mean is $\\bar x$." })
  const opened = await handleAsk(new Request("https://statwiki-ask.example.workers.dev/session", {
    method: "POST",
    body: JSON.stringify({ turnstile: "turnstile-ok" }),
  }), deps)
  assert.equal(opened.status, 200)
  const token = (await opened.json() as { session: string }).session
  assert.deepEqual(await verifySession(SECRET, token, Math.floor(NOW.getTime() / 1000)), { sid: token ? (await verifySession(SECRET, token, Math.floor(NOW.getTime() / 1000)))?.sid : "" })
  const response = await handleAsk(ask({
    turns: [{ role: "user", content: "What is a mean?" }],
    page: "/notes/a.html",
    anchor: "mean",
    session: token,
  }), deps)
  assert.equal(response.status, 200)
  const events = sse(await response.text())
  assert.equal(events.at(-1)?.event, "citations")
  const citations = events.at(-1)?.data.citations as { number: number; id: string; title: string; kind: string; url: string }[]
  assert.deepEqual(citations, [{
    number: 1,
    id: "section:mean",
    title: "section:mean",
    kind: "section",
    url: "/notes/a.html#mean",
  }])
  assert.equal(calls.model, 1)
})

test("numbers outside 1..k and model urls are not citations", async () => {
  const { deps } = harness({ answer: "See [1] and [99] and [1](https://evil.example/secret)." })
  const response = await handleAsk(ask({
    turns: [{ role: "user", content: "What is a mean?" }],
    page: "/notes/a.html",
    anchor: "",
    session: await session(),
  }), deps)
  const events = sse(await response.text())
  const citations = events.at(-1)?.data.citations as { number: number; url: string }[]
  assert.deepEqual(citations.map((citation) => citation.number), [1])
  assert.equal(citations.some((citation) => citation.url.includes("evil.example")), false)
})

test("the page boost is applied by the shared reranker", async () => {
  const { deps } = harness({
    k: 1,
    answer: "[1] Here.",
    matches: [
      match("section:far", 0.8, "/other.html", "chapter:z"),
      match("section:here", 0.74, "/notes/a.html#here", "chapter:a"),
    ],
  })
  const response = await handleAsk(ask({
    turns: [{ role: "user", content: "What is on this page?" }],
    page: "/notes/a.html",
    anchor: "",
    session: await session(),
  }), deps)
  const citations = sse(await response.text()).at(-1)?.data.citations as { id: string }[]
  assert.equal(citations[0].id, "section:here")
})

test("closed-book exclusion is only available to the dev bypass", async () => {
  const matches = [
    match("question:q", 0.9, "/questions/q.html", "chapter:a"),
    match("section:other", 0.6, "/notes/a.html#other", "chapter:a"),
  ]
  const dev = harness({ k: 1, answer: "[1] Other.", matches, devToken: "dev-secret" })
  const devResponse = await handleAsk(ask({
    turns: [{ role: "user", content: "Why does this happen?" }],
    page: "/questions/q.html",
    anchor: "",
    exclude: ["question:q"],
    compare: true,
  }, { "x-dev-ask-token": "dev-secret" }), dev.deps)
  const devEvents = sse(await devResponse.text())
  assert.equal((devEvents.at(-1)?.data.citations as { id: string }[])[0].id, "section:other")
  const retrieval = devEvents.find((event) => event.event === "retrieval")?.data as { passages: { id: string }[] }
  assert.deepEqual(retrieval.passages.map((passage) => passage.id), ["section:other"])

  const reader = harness({ k: 1, answer: "[1] Own.", matches })
  const publicResponse = await handleAsk(ask({
    turns: [{ role: "user", content: "Why does this happen?" }],
    page: "/questions/q.html",
    anchor: "",
    session: await session(),
    exclude: ["question:q"],
    compare: true,
  }), reader.deps)
  const publicEvents = sse(await publicResponse.text())
  assert.equal(publicEvents.some((event) => event.event === "retrieval"), false)
  assert.equal((publicEvents.at(-1)?.data.citations as { id: string }[])[0].id, "question:q")
})

test("limits, the budget, and the kill switch do not call the model", async () => {
  const limited = harness()
  const token = await session()
  for (let i = 0; i < SESSION_DAILY_LIMIT; i++) {
    const response = await handleAsk(ask({
      turns: [{ role: "user", content: `Question ${i}` }],
      page: "/notes/a.html",
      anchor: "",
      session: token,
    }), limited.deps)
    assert.equal(response.status, 200)
    await response.text()
  }
  const blocked = await handleAsk(ask({
    turns: [{ role: "user", content: "One more" }],
    page: "/notes/a.html",
    anchor: "",
    session: token,
  }), limited.deps)
  assert.equal(blocked.status, 429)
  assert.equal(limited.calls.model, SESSION_DAILY_LIMIT)

  const addresses = harness()
  for (let i = 0; i < IP_DAILY_LIMIT; i++) {
    const fresh = await signSession(SECRET, `s${i}`, Math.floor(NOW.getTime() / 1000) + 60)
    const response = await handleAsk(ask({
      turns: [{ role: "user", content: "Again" }],
      page: "/notes/a.html",
      anchor: "",
      session: fresh,
    }), addresses.deps)
    assert.equal(response.status, 200)
    await response.text()
  }
  const ipBlocked = await handleAsk(ask({
    turns: [{ role: "user", content: "Again" }],
    page: "/notes/a.html",
    anchor: "",
    session: await signSession(SECRET, "overflow", Math.floor(NOW.getTime() / 1000) + 60),
  }), addresses.deps)
  assert.equal(ipBlocked.status, 429)
  assert.equal(addresses.calls.model, IP_DAILY_LIMIT)

  const budget = harness({ budget: 1, answer: "A short answer." })
  const first = await handleAsk(ask({
    turns: [{ role: "user", content: "First" }],
    page: "",
    anchor: "",
    session: token,
  }), budget.deps)
  assert.equal(first.status, 200)
  await first.text()
  const resting = await handleAsk(ask({
    turns: [{ role: "user", content: "Second" }],
    page: "",
    anchor: "",
    session: token,
  }), budget.deps)
  const restingText = await resting.text()
  assert.match(restingText, new RegExp(RESTING_MESSAGE))
  assert.equal(sse(restingText).at(-1)?.event, "citations")
  assert.equal(budget.calls.model, 1)

  const killed = harness({ kill: true })
  const killedResponse = await handleAsk(ask({
    turns: [{ role: "user", content: "UNIQUE-QUESTION-NEEDLE" }],
    page: "",
    anchor: "",
    session: token,
  }, { "cf-connecting-ip": "203.0.113.50" }), killed.deps)
  const killedBody = await killedResponse.text()
  assert.match(killedBody, new RegExp(`^event: delta\\ndata: \\{"text":"${RESTING_MESSAGE.replace(/'/g, "")}"\\}`))
  assert.equal(killed.calls.model, 0)
  const logged = JSON.stringify(killed.logs)
  assert.equal(logged.includes("UNIQUE-QUESTION-NEEDLE"), false)
  assert.equal(logged.includes("203.0.113.50"), false)
})

test("questions are capped at 2000 characters and at 6 turns", async () => {
  const { deps, calls } = harness()
  const token = await session()
  const long = await handleAsk(ask({
    turns: [{ role: "user", content: "x".repeat(2001) }],
    page: "",
    anchor: "",
    session: token,
  }), deps)
  assert.equal(long.status, 400)
  const many = await handleAsk(ask({
    turns: Array.from({ length: 7 }, () => ({ role: "user", content: "Hi" })),
    page: "",
    anchor: "",
    session: token,
  }), deps)
  assert.equal(many.status, 400)
  assert.equal(calls.model, 0)
})

test("the dev bypass is off without a secret and on the public hostname", async () => {
  const quiet = harness({ devToken: "" })
  const missing = await handleAsk(ask({
    turns: [{ role: "user", content: "Hello" }],
    page: "",
    anchor: "",
  }, { "x-dev-ask-token": "dev-secret" }), quiet.deps)
  assert.equal(missing.status, 401)
  const site = harness()
  const refused = await handleAsk(ask({
    turns: [{ role: "user", content: "Hello" }],
    page: "",
    anchor: "",
  }, { "x-dev-ask-token": "dev-secret" }, "https://www.statwiki.io/ask"), site.deps)
  assert.equal(refused.status, 401)
  assert.equal(site.calls.model, 0)
})

test("cors allows the site and localhost only", async () => {
  const { deps } = harness()
  const site = await handleAsk(new Request("https://statwiki-ask.example.workers.dev/health", {
    headers: { origin: "https://www.statwiki.io" },
  }), deps)
  assert.equal(site.headers.get("access-control-allow-origin"), "https://www.statwiki.io")
  const local = await handleAsk(new Request("https://statwiki-ask.example.workers.dev/health", {
    headers: { origin: "http://localhost:8080" },
  }), deps)
  assert.equal(local.headers.get("access-control-allow-origin"), "http://localhost:8080")
  const denied = await handleAsk(new Request("https://statwiki-ask.example.workers.dev/ask", {
    method: "POST",
    headers: { origin: "https://evil.example", "content-type": "application/json" },
    body: "{}",
  }), deps)
  assert.equal(denied.status, 403)
  const preflight = await handleAsk(new Request("https://statwiki-ask.example.workers.dev/ask", {
    method: "OPTIONS",
    headers: { origin: "http://127.0.0.1:3000" },
  }), deps)
  assert.equal(preflight.status, 204)
  assert.equal(preflight.headers.get("access-control-allow-origin"), "http://127.0.0.1:3000")
})

test("every misuse prompt is sent to the model and a decline carries no citation", async () => {
  const misuse = await readJsonl<MisusePrompt>(resolve(here, "../../harness/misuse.jsonl"))
  assert.equal(misuse.length, 30)
  const { deps, calls, logs } = harness()
  for (const item of misuse) {
    const response = await handleAsk(ask({
      turns: [{ role: "user", content: item.prompt }],
      page: "",
      anchor: "",
    }, { "x-dev-ask-token": "dev-secret", "x-dev-session": item.id }), deps)
    assert.equal(response.status, 200)
    const events = sse(await response.text())
    const text = events.filter((event) => event.event === "delta").map((event) => String(event.data.text ?? "")).join("")
    assert.equal(looksDeclined(text), true)
    assert.deepEqual(events.at(-1)?.data.citations, [])
    const expected = buildPrompt({
      question: item.prompt,
      passages: [{ n: 1, text: "Text for section:mean#0" }],
      covered: true,
    })
    assert.equal(sha256Hex(calls.users.at(-1) ?? ""), sha256Hex(expected.user))
    assert.match(expected.system, /decline in one sentence/)
    assert.match(expected.system, /Do not write URLs/)
    assert.equal(JSON.stringify(logs).includes(item.prompt), false)
  }
  assert.equal(calls.model, misuse.length)
})
