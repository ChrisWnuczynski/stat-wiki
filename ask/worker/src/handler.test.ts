import assert from "node:assert/strict"
import { dirname, resolve } from "node:path"
import test from "node:test"
import { fileURLToPath } from "node:url"

import { IP_DAILY_LIMIT, NOT_COVERED_REPLY, RESTING_MESSAGE, SESSION_DAILY_LIMIT, SESSION_TTL_SECONDS } from "../../core/config.ts"
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
  here?: { entryId: string; chunkId: string; title: string; kind: string; url: string }
}): { deps: AskDeps; calls: { model: number; users: string[] }; logs: LogEvent[]; state: { day: DayState } } {
  const state = { day: emptyDay() }
  const calls = { model: 0, users: [] as string[] }
  const logs: LogEvent[] = []
  const matches = options?.matches ?? [match("section:mean", 0.8, "/notes/a.html#mean", "chapter:a")]
  const deps: AskDeps = {
    now: () => NOW,
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
    pageEntry: async () => options?.here ?? null,
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

test("closed-book fields in a request are ignored", async () => {
  const matches = [
    match("question:q", 0.9, "/questions/q.html", "chapter:a"),
    match("section:other", 0.6, "/notes/a.html#other", "chapter:a"),
  ]
  const reader = harness({ k: 1, answer: "[1] Own.", matches })
  const response = await handleAsk(ask({
    turns: [{ role: "user", content: "Why does this happen?" }],
    page: "/questions/q.html",
    anchor: "",
    session: await session(),
    exclude: ["question:q"],
    compare: true,
  }), reader.deps)
  const events = sse(await response.text())
  assert.equal(events.some((event) => event.event === "retrieval"), false)
  assert.equal((events.at(-1)?.data.citations as { id: string }[])[0].id, "question:q")
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

test("a dev token header is not a way in", async () => {
  const { deps, calls } = harness()
  for (const url of ["https://statwiki-ask.example.workers.dev/ask", "https://ask.statwiki.io/ask"]) {
    const response = await handleAsk(ask({
      turns: [{ role: "user", content: "Hello" }],
      page: "",
      anchor: "",
    }, { "x-dev-ask-token": "dev-secret", "x-dev-session": "dev" }, url), deps)
    assert.equal(response.status, 401)
  }
  assert.equal(calls.model, 0)
  const preflight = await handleAsk(new Request("https://ask.statwiki.io/ask", {
    method: "OPTIONS",
    headers: { origin: "https://www.statwiki.io" },
  }), deps)
  assert.equal(preflight.headers.get("access-control-allow-headers"), "content-type")
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

test("a covered misuse prompt reaches the model and a decline carries no citation", async () => {
  const misuse = await readJsonl<MisusePrompt>(resolve(here, "../../harness/misuse.jsonl"))
  assert.equal(misuse.length, 30)
  const { deps, calls, logs } = harness()
  for (const item of misuse) {
    const response = await handleAsk(ask({
      turns: [{ role: "user", content: item.prompt }],
      page: "",
      anchor: "",
      session: await signSession(SECRET, item.id, Math.floor(NOW.getTime() / 1000) + 60),
    }), deps)
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
    assert.match(expected.system, /never write a URL yourself/)
    assert.equal(JSON.stringify(logs).includes(item.prompt), false)
  }
  assert.equal(calls.model, misuse.length)
})

test("below the coverage threshold the fixed reply is sent and the model is not called", async () => {
  const { deps, calls, logs } = harness({ matches: [match("section:mean", 0.3, "/notes/a.html#mean", "chapter:a")] })
  const response = await handleAsk(ask({
    turns: [{ role: "user", content: "Give me a vegetarian pasta recipe for four people." }],
    page: "",
    anchor: "",
    session: await session(),
  }), deps)
  assert.equal(response.status, 200)
  const events = sse(await response.text())
  assert.deepEqual(events.map((event) => event.event), ["status", "delta", "citations"])
  assert.deepEqual(events[0].data, { covered: false })
  assert.equal(events[1].data.text, NOT_COVERED_REPLY)
  assert.deepEqual(events[2].data.citations, [])
  assert.equal(calls.model, 0)
  assert.equal(logs.some((event) => event.result === "not covered"), true)
})

test("a covered question starts with a status event", async () => {
  const { deps, calls } = harness({ answer: "The mean is the average [1]." })
  const response = await handleAsk(ask({
    turns: [{ role: "user", content: "What is a mean?" }],
    page: "/notes/a.html",
    anchor: "mean",
    session: await session(),
  }), deps)
  const events = sse(await response.text())
  assert.equal(events[0].event, "status")
  assert.deepEqual(events[0].data, { covered: true })
  assert.equal(calls.model, 1)
})

test("a keep-alive comment goes out every 15 seconds while the model thinks", async (t) => {
  t.mock.timers.enable({ apis: ["setInterval"] })
  let release: () => void = () => {}
  const gate = new Promise<void>((done) => { release = done })
  const { deps } = harness()
  deps.streamAnswer = async function* () {
    await gate
    yield "Done [1]."
  }
  const response = await handleAsk(ask({
    turns: [{ role: "user", content: "What is a mean?" }],
    page: "/notes/a.html",
    anchor: "",
    session: await session(),
  }), deps)
  const reader = response.body!.getReader()
  const decoder = new TextDecoder()
  const first = decoder.decode((await reader.read()).value)
  assert.match(first, /event: status/)
  t.mock.timers.tick(15_000)
  assert.equal(decoder.decode((await reader.read()).value), ": thinking\n\n")
  release()
  let rest = ""
  for (;;) {
    const { done, value } = await reader.read()
    if (done) break
    rest += decoder.decode(value)
  }
  assert.match(rest, /event: citations/)
})

test("the reader's page is named, and added as a passage when retrieval missed it", async () => {
  const here = { entryId: "chapter:bb", chunkId: "chapter:bb#0", title: "The Beta–Binomial model", kind: "chapter", url: "/notes/bb.html" }
  const { deps, calls } = harness({ answer: "This chapter is [2].", here })
  const response = await handleAsk(ask({
    turns: [{ role: "user", content: "Can you give me a link to this chapter?" }],
    page: "/notes/bb.html",
    anchor: "",
    session: await session(),
  }), deps)
  const events = sse(await response.text())
  assert.match(calls.users.at(-1) ?? "", /The reader is on this page: The Beta–Binomial model \[2\]\./)
  assert.match(calls.users.at(-1) ?? "", /\[2\] Text for chapter:bb#0/)
  assert.deepEqual(events.at(-1)?.data.citations, [{ number: 2, id: "chapter:bb", title: "The Beta–Binomial model", kind: "chapter", url: "/notes/bb.html" }])
})

test("when retrieval already has the reader's page, its number is reused", async () => {
  const here = { entryId: "section:mean", chunkId: "section:mean#0", title: "Means", kind: "section", url: "/notes/a.html#mean" }
  const { deps, calls } = harness({ here })
  await (await handleAsk(ask({
    turns: [{ role: "user", content: "Why is this true?" }],
    page: "/notes/a.html",
    anchor: "mean",
    session: await session(),
  }), deps)).text()
  const user = calls.users.at(-1) ?? ""
  assert.match(user, /The reader is on this page: Means \[1\]\./)
  assert.equal((user.match(/^\[\d\] /gm) ?? []).length, 1)
})
