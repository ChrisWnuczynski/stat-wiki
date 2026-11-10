// Answer check: the model answers the dev questions with the same retrieval,
// prompt and limits as the Worker, and a judge grades each answer against the
// worked answer. Writes a report, a CSV and every answer in full.
//
//   node --experimental-strip-types harness/answers.ts --limit 5
//   node --experimental-strip-types harness/answers.ts --models grok-4.7,grok-4.6 --modes closed,open --student
//
// Needs CLOUDFLARE_ACCOUNT_ID, CLOUDFLARE_API_TOKEN and XAI_API_KEY.

import { mkdir, writeFile } from "node:fs/promises"
import { dirname, resolve } from "node:path"
import { fileURLToPath } from "node:url"

import { citationsFromAnswer } from "../core/citations.ts"
import { Cloudflare } from "../core/cloudflare.ts"
import {
  ANSWER_MODEL,
  COVERAGE_THRESHOLD,
  DEV_SIZE,
  FETCH_K,
  JUDGE_MODEL,
  SPLIT_SEED,
  WIKI_URL,
  WORKER_K,
  WORKER_MAX_TOKENS,
  XAI_BASE_URL,
} from "../core/config.ts"
import { buildGraph } from "../core/graph.ts"
import { GRADES, parseJsonObject, parseJudge, UNREADABLE, type Grade } from "../core/judge.ts"
import { mathsReport } from "../core/maths.ts"
import { excludeIdsForQuestion, findOverlaps } from "../core/overlap.ts"
import { mapPool } from "../core/pool.ts"
import { buildPrompt, NOT_COVERED_SENTENCE, PROMPT_VERSION } from "../core/prompt.ts"
import { readJsonl, type StudentQuestion } from "../core/questions.ts"
import { DEFAULT_BOOSTS, isCovered, packPassages, rerank } from "../core/retrieve.ts"
import { rankMatches, takePool, textsFromStored } from "../core/select.ts"
import { splitBank } from "../core/split.ts"
import { pagePath, parseArgs, percentile } from "../core/text.ts"
import type { Candidate, Passage } from "../core/types.ts"
import { loadWiki } from "../core/wiki-file.ts"

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..")

export const JUDGE_SYSTEM = `You grade a statistics tutor's answer against the course's worked answer.

Grades:
- correct: every part asked for is answered, and each final result and key step agrees with the worked answer. Equivalent forms, different notation and a different valid method count as agreement.
- minor error: the main results are right, but there is a small slip, such as an arithmetic or sign slip that does not carry into the conclusion, a missing condition, or one small part left out.
- wrong: a main result or key claim disagrees with the worked answer or is mathematically false, or a major part of the question is not answered.
- did not answer: the tutor declined, only said the material is not covered, or asked for clarification instead of answering.

Judge the mathematics and statistics only. Ignore style, length, formatting and bracketed citation numbers such as [2]. If the worked answer itself looks wrong, grade against correct mathematics and say what looks wrong in "reference_doubt"; otherwise leave it empty.

Reply with one JSON object and nothing else:
{"grade": "correct" | "minor error" | "wrong" | "did not answer", "reason": "one sentence naming the part that decided the grade", "reference_doubt": ""}`

export const SUPPORT_SYSTEM = `You check one citation in a statistics tutor's answer. Given a sentence from the answer and the passage it cites, decide whether the passage supports what the sentence says.

- supported: the passage states or directly implies the sentence's claim.
- partly: the passage supports some of the claim, or supports it only with an extra step it does not show.
- not supported: the passage does not support the claim, or contradicts it.

Reply with one JSON object and nothing else: {"verdict": "supported" | "partly" | "not supported", "reason": "one sentence"}`

type Usage = { prompt: number; completion: number; reasoning: number; costUsd: number }
type Call = { text: string; finish: string; usage: Usage; latencyMs: number }

const prices = new Map<string, { input: number; output: number }>()

export async function loadPrices(): Promise<void> {
  try {
    const response = await fetch(`${XAI_BASE_URL}/language-models`, { headers: { Authorization: `Bearer ${process.env.XAI_API_KEY ?? ""}` } })
    const json = await response.json() as { models?: { id: string; prompt_text_token_price?: number; completion_text_token_price?: number }[] }
    for (const model of json.models ?? []) {
      // xAI lists prices in units of 1e-10 US dollars per token.
      prices.set(model.id, { input: (model.prompt_text_token_price ?? 0) * 1e-10, output: (model.completion_text_token_price ?? 0) * 1e-10 })
    }
  } catch {
    // Cost is reported as unknown.
  }
}

export function costOf(model: string, usage: Usage): number {
  if (Number.isFinite(usage.costUsd)) return usage.costUsd
  const price = prices.get(modelSpec(model).model)
  if (!price) return Number.NaN
  return usage.prompt * price.input + (usage.completion + usage.reasoning) * price.output
}

// Streams the reply. The session proxy cuts a response that is silent for 30 s,
// and these models can think for longer than that before the first word.
// A model may carry a thinking level, as in "grok-4.7@low".
export function modelSpec(spec: string): { model: string; effort: string } {
  const [model, effort = ""] = spec.split("@")
  return { model, effort }
}

export async function chat(spec: string, system: string, user: string, maxTokens: number, attempt = 0): Promise<Call> {
  const started = Date.now()
  const { model, effort } = modelSpec(spec)
  let response: Response
  try {
    response = await fetch(`${XAI_BASE_URL}/chat/completions`, {
      method: "POST",
      headers: { Authorization: `Bearer ${process.env.XAI_API_KEY ?? ""}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        model,
        temperature: 0.2,
        max_tokens: maxTokens,
        stream: true,
        stream_options: { include_usage: true },
        ...(effort ? { reasoning_effort: effort } : {}),
        messages: [{ role: "system", content: system }, { role: "user", content: user }],
      }),
    })
  } catch (error) {
    if (attempt < 5) {
      await new Promise((done) => setTimeout(done, 2000 * 2 ** attempt))
      return chat(spec, system, user, maxTokens, attempt + 1)
    }
    throw error
  }
  if (!response.ok || !response.body) {
    const raw = await response.text()
    console.error(`xAI ${response.status} after ${((Date.now() - started) / 1000).toFixed(1)}s (attempt ${attempt + 1}): ${raw.slice(0, 120)}`)
    if ((response.status === 429 || response.status >= 500) && attempt < 5) {
      await new Promise((done) => setTimeout(done, 2000 * 2 ** attempt))
      return chat(spec, system, user, maxTokens, attempt + 1)
    }
    throw new Error(`xAI ${response.status}: ${raw.slice(0, 200)}`)
  }
  let text = ""
  let finish = ""
  let usage: { prompt_tokens?: number; completion_tokens?: number; completion_tokens_details?: { reasoning_tokens?: number }; cost_in_usd_ticks?: number } = {}
  const reader = response.body.getReader()
  const decoder = new TextDecoder()
  let buffer = ""
  try {
    for (;;) {
      const { done, value } = await reader.read()
      if (done) break
      buffer += decoder.decode(value, { stream: true }).replaceAll("\r\n", "\n")
      let nl = buffer.indexOf("\n")
      while (nl >= 0) {
        const line = buffer.slice(0, nl).trim()
        buffer = buffer.slice(nl + 1)
        nl = buffer.indexOf("\n")
        if (!line.startsWith("data:")) continue
        const data = line.slice(5).trim()
        if (!data || data === "[DONE]") continue
        const json = JSON.parse(data) as {
          choices?: { delta?: { content?: string }; finish_reason?: string | null }[]
          usage?: typeof usage
        }
        const choice = json.choices?.[0]
        if (choice?.delta?.content) text += choice.delta.content
        if (choice?.finish_reason) finish = choice.finish_reason
        if (json.usage) usage = json.usage
      }
    }
  } catch (error) {
    if (attempt < 5) {
      console.error(`xAI stream broke after ${((Date.now() - started) / 1000).toFixed(1)}s (attempt ${attempt + 1})`)
      return chat(spec, system, user, maxTokens, attempt + 1)
    }
    throw error
  }
  return {
    text,
    finish,
    usage: {
      prompt: usage.prompt_tokens ?? 0,
      completion: usage.completion_tokens ?? 0,
      reasoning: usage.completion_tokens_details?.reasoning_tokens ?? 0,
      // xAI reports the exact charge in ticks of 1e-10 US dollars.
      costUsd: (usage.cost_in_usd_ticks ?? Number.NaN) * 1e-10,
    },
    latencyMs: Date.now() - started,
  }
}

// Asks the judge once more when its reply cannot be read; returns the last reply
// and the cost of both calls.
export async function judgeTwice<T>(model: string, system: string, user: string, maxTokens: number, read: (text: string) => T | null): Promise<{ value: T | null; text: string; cost: number }> {
  let call = await chat(model, system, user, maxTokens)
  let cost = costOf(model, call.usage)
  let value = read(call.text)
  if (value === null) {
    call = await chat(model, system, user, maxTokens)
    cost += costOf(model, call.usage)
    value = read(call.text)
  }
  return { value, text: call.text, cost }
}

// Sentences that carry a citation, paired with each number they cite.
export function citedSentences(answer: string): { sentence: string; n: number }[] {
  const out: { sentence: string; n: number }[] = []
  const sentences = answer.replace(/\$\$[\s\S]*?\$\$/g, (block) => block.replace(/\n/g, " ")).split(/(?<=[.!?])\s+|\n{2,}/)
  for (const sentence of sentences) {
    for (const match of sentence.matchAll(/\[(\d+(?:\s*,\s*\d+)*)\]/g)) {
      for (const part of match[1].split(",")) out.push({ sentence: sentence.trim(), n: Number(part.trim()) })
    }
  }
  return out
}

export function invalidCitationNumbers(answer: string, k: number): number[] {
  const bad: number[] = []
  for (const match of answer.matchAll(/\[(\d+(?:\s*,\s*\d+)*)\]/g)) {
    for (const part of match[1].split(",")) {
      const n = Number(part.trim())
      if (!Number.isInteger(n) || n < 1 || n > k) bad.push(n)
    }
  }
  return bad
}

// Deterministic sample: mulberry32 shuffle.
export function sample<T>(items: T[], size: number, seed: number): T[] {
  let state = seed >>> 0
  const next = () => {
    state = (state + 0x6d2b79f5) >>> 0
    let t = state
    t = Math.imul(t ^ (t >>> 15), t | 1)
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61)
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
  const copy = [...items]
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(next() * (i + 1))
    ;[copy[i], copy[j]] = [copy[j], copy[i]]
  }
  return copy.slice(0, size)
}

type Item = {
  set: "bank" | "student"
  id: string
  question: string
  reference: string
  chapterId: string
  page: string
  exclude: Set<string>
}

export type Record_ = {
  set: "bank" | "student"
  id: string
  mode: "open" | "closed"
  model: string
  question: string
  reference: string
  passages: { n: number; entryId: string; url: string; chunkId: string }[]
  best: number
  covered: boolean
  answer: string
  finish: string
  usage: Usage
  latencyMs: number
  cost: number
  citations: number
  invalidCitations: number[]
  mathsSpans: number
  mathsFailures: number
  notCovered: boolean
  grade: Grade | "no reference" | typeof UNREADABLE | ""
  gradeReason: string
  referenceDoubt: string
  judgeCost: number
}

const pct = (n: number, d: number) => (d === 0 ? "n/a" : `${(100 * n / d).toFixed(1)}%`)

// One row per model and mode. n counts graded answers only; replies the judge
// gave that could not be read are counted on their own.
export function correctnessTable(records: { set: string; model: string; mode: string; grade: string }[]): string[] {
  const lines = [
    "| model | mode | n | correct | minor error | wrong | did not answer | correct or minor | judge unreadable |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
  ]
  const groups = new Map<string, typeof records>()
  for (const rec of records) {
    if (rec.set !== "bank") continue
    const key = `${rec.model}|${rec.mode}`
    groups.set(key, [...(groups.get(key) ?? []), rec])
  }
  for (const [key, recs] of groups) {
    const [model, mode] = key.split("|")
    const graded = recs.filter((rec) => GRADES.includes(rec.grade as Grade))
    const count = (grade: string) => graded.filter((rec) => rec.grade === grade).length
    const unreadable = recs.filter((rec) => rec.grade === UNREADABLE).length
    lines.push(`| ${model} | ${mode} | ${graded.length} | ${pct(count("correct"), graded.length)} | ${pct(count("minor error"), graded.length)} | ${pct(count("wrong"), graded.length)} | ${pct(count("did not answer"), graded.length)} | ${pct(count("correct") + count("minor error"), graded.length)} | ${unreadable} |`)
  }
  return lines
}

export const SUPPORT_VERDICTS = ["supported", "partly", "not supported", "unparsed"]

if (import.meta.url === `file://${process.argv[1]}`) {
  const args = parseArgs(process.argv.slice(2))
  const limit = typeof args.limit === "string" ? Number(args.limit) : 0
  const models = (typeof args.models === "string" ? args.models : ANSWER_MODEL).split(",").map((m) => m.trim()).filter(Boolean)
  const modes = (typeof args.modes === "string" ? args.modes : "closed").split(",").map((m) => m.trim()) as ("open" | "closed")[]
  const judgeModel = typeof args.judge === "string" ? args.judge : JUDGE_MODEL
  const concurrency = typeof args.concurrency === "string" ? Number(args.concurrency) : 4
  const supportSize = typeof args.support === "string" ? Number(args.support) : 40
  const tag = typeof args.tag === "string" ? args.tag : "answers"
  const withStudent = args.student === true
  const secondModes = typeof args["second-modes"] === "string" ? args["second-modes"].split(",") : ["closed"]

  if (!process.env.XAI_API_KEY?.trim()) throw new Error("XAI_API_KEY is missing")
  await loadPrices()

  const wiki = await loadWiki(typeof args.wiki === "string" ? args.wiki : WIKI_URL)
  const graph = buildGraph(wiki)
  const overlaps = findOverlaps(wiki)
  const byId = graph.byId
  const questions = wiki.entries.filter((entry) => entry.kind === "question" && entry.text)
  const split = splitBank(questions.map((entry) => entry.id), SPLIT_SEED, DEV_SIZE)
  const dev = limit > 0 ? split.dev.slice(0, limit) : split.dev

  const items: Item[] = []
  for (const id of dev) {
    const entry = byId.get(id)
    if (!entry?.text) continue
    const answers = graph.answersOf.get(id) ?? []
    const reference = answers.map((answerId) => byId.get(answerId)?.text ?? "").filter(Boolean).join("\n\n")
    items.push({
      set: "bank",
      id,
      question: entry.text,
      reference,
      chapterId: graph.chapterOf(id) ?? "",
      page: pagePath(entry.url),
      exclude: new Set(excludeIdsForQuestion(id, answers, overlaps)),
    })
  }
  if (withStudent) {
    const student = await readJsonl<StudentQuestion>(resolve(root, "harness/student.jsonl"))
    for (const item of limit > 0 ? student.slice(0, limit) : student) {
      const target = byId.get(item.expect[0])
      const chapterId = item.chapterId || (target ? graph.chapterOf(target.id) ?? "" : "")
      const chapter = chapterId ? byId.get(chapterId) : undefined
      items.push({
        set: "student",
        id: item.id,
        question: item.question,
        reference: "",
        chapterId,
        page: item.page || (chapter ? pagePath(chapter.url) : ""),
        exclude: new Set(),
      })
    }
  }

  const client = await Cloudflare.connect()
  console.log(`questions ${items.length}, models ${models.join(", ")}, modes ${modes.join(", ")}, judge ${judgeModel}`)

  type Retrieved = { item: Item; mode: "open" | "closed"; best: number; candidates: Candidate[]; texts: Map<string, string> }
  const retrieved: Retrieved[] = []
  await mapPool(items, 4, async (item) => {
    const vector = await client.embedQuery(item.question)
    const matches = await client.query(vector, FETCH_K)
    const ranked = rankMatches(matches)
    const wanted = item.set === "student" ? ["open" as const] : modes
    const pools = wanted.map((mode) => ({ mode, pool: takePool(ranked, mode, item.exclude, matches.length) }))
    const ids = [...new Set(pools.flatMap(({ pool }) => pool.candidates.map((candidate) => candidate.chunkId)))]
    const texts = textsFromStored(ids.length > 0 ? await client.kvGetMany(ids) : new Map())
    for (const { mode, pool } of pools) retrieved.push({ item, mode, best: pool.best, candidates: pool.candidates, texts })
  })
  console.log(`retrieved ${retrieved.length}`)

  const jobs: { r: Retrieved; model: string }[] = []
  for (const r of retrieved) {
    for (const [index, model] of models.entries()) {
      if (index > 0 && (r.item.set === "student" || !secondModes.includes(r.mode))) continue
      jobs.push({ r, model })
    }
  }

  const records: Record_[] = []
  let done = 0
  await mapPool(jobs, concurrency, async ({ r, model }) => {
    const ranked = rerank(r.item.question, r.candidates, {
      ...DEFAULT_BOOSTS,
      definesTargets: graph.definesTargets,
      pagePath: r.item.page,
      chapterId: r.item.chapterId,
    })
    const passages: Passage[] = packPassages(ranked, r.texts, WORKER_K)
    const covered = isCovered(r.best, COVERAGE_THRESHOLD)
    const prompt = buildPrompt({ question: r.item.question, passages: passages.map((p) => ({ n: p.n, text: p.text })), covered })
    const call = await chat(model, prompt.system, prompt.user, WORKER_MAX_TOKENS)
    const maths = mathsReport(call.text)
    const record: Record_ = {
      set: r.item.set,
      id: r.item.id,
      mode: r.mode,
      model,
      question: r.item.question,
      reference: r.item.reference,
      passages: passages.map((p) => ({ n: p.n, entryId: p.entryId, url: p.url, chunkId: p.chunkId })),
      best: r.best,
      covered,
      answer: call.text,
      finish: call.finish,
      usage: call.usage,
      latencyMs: call.latencyMs,
      cost: costOf(model, call.usage),
      citations: citationsFromAnswer(call.text, passages).length,
      invalidCitations: invalidCitationNumbers(call.text, passages.length),
      mathsSpans: maths.spans,
      mathsFailures: maths.failures,
      notCovered: call.text.includes(NOT_COVERED_SENTENCE),
      grade: "",
      gradeReason: "",
      referenceDoubt: "",
      judgeCost: 0,
    }
    if (r.item.set === "bank") {
      if (!r.item.reference) {
        record.grade = "no reference"
      } else {
        const judged = await judgeTwice(judgeModel, JUDGE_SYSTEM, `Question:\n${r.item.question}\n\nWorked answer:\n${r.item.reference}\n\nTutor's answer:\n${call.text}`, 2000, parseJudge)
        const parsed = judged.value
        record.grade = parsed?.grade ?? UNREADABLE
        record.gradeReason = parsed ? parsed.reason : `judge output was not a grade: ${judged.text.slice(0, 400)}`
        record.referenceDoubt = parsed?.doubt ?? ""
        record.judgeCost = judged.cost
      }
    }
    records.push(record)
    done += 1
    if (done % 10 === 0 || done === jobs.length) console.log(`answered ${done}/${jobs.length}`)
  })

  // Citation support on a sample of cited sentences from the main model's closed answers.
  const mainModel = models[0]
  const pairs = records
    .filter((rec) => rec.set === "bank" && rec.model === mainModel && rec.mode === (modes.includes("closed") ? "closed" : modes[0]))
    .sort((a, b) => a.id.localeCompare(b.id))
    .flatMap((rec) => citedSentences(rec.answer).filter((pair) => pair.n >= 1 && pair.n <= rec.passages.length).map((pair) => ({ rec, ...pair })))
  const chosen = sample(pairs, supportSize, SPLIT_SEED)
  type Support = { id: string; n: number; sentence: string; entryId: string; verdict: string; reason: string }
  const support: Support[] = []
  let supportCost = 0
  const textByChunk = new Map(retrieved.flatMap((r) => [...r.texts.entries()]))
  await mapPool(chosen, concurrency, async (pair) => {
    const passage = pair.rec.passages.find((p) => p.n === pair.n)
    const text = passage ? textByChunk.get(passage.chunkId) ?? "" : ""
    const judged = await judgeTwice(judgeModel, SUPPORT_SYSTEM, `Sentence:\n${pair.sentence}\n\nPassage [${pair.n}]:\n${text}`, 1000, parseJsonObject)
    const obj = judged.value
    supportCost += judged.cost
    support.push({
      id: pair.rec.id,
      n: pair.n,
      sentence: pair.sentence,
      entryId: passage?.entryId ?? "",
      verdict: String(obj?.verdict ?? "unparsed"),
      reason: String(obj?.reason ?? judged.text.slice(0, 120)),
    })
  })

  records.sort((a, b) => a.set.localeCompare(b.set) || a.model.localeCompare(b.model) || a.mode.localeCompare(b.mode) || a.id.localeCompare(b.id))
  const date = new Date().toISOString().slice(0, 10)
  const outDir = resolve(root, "harness/runs")
  await mkdir(outDir, { recursive: true })
  const base = resolve(outDir, `${date}-${tag}`)
  await writeFile(`${base}.jsonl`, records.map((rec) => JSON.stringify(rec)).join("\n") + "\n")
  await writeFile(`${base}-support.jsonl`, support.map((row) => JSON.stringify(row)).join("\n") + "\n")

  const lines: string[] = []
  lines.push(`# Answer check ${date}`)
  lines.push("")
  lines.push(`Prompt ${PROMPT_VERSION}. Retrieval as in the Worker: k=${WORKER_K}, page and section boosts on, threshold ${COVERAGE_THRESHOLD}. Answers capped at ${WORKER_MAX_TOKENS} tokens. Judge ${judgeModel}${models.includes(judgeModel) ? " (also an answer model, so it may favour its own answers; grade a blind sample by hand to check)" : ""}.`)
  lines.push("")
  lines.push("Closed mode removes the question's own worked answer (and copies of it) from retrieval, so the tutor has to teach from the chapters. Open mode is the index as it is in production.")
  lines.push("")
  lines.push("## Correctness (dev questions with a worked answer)")
  lines.push("")
  lines.push(...correctnessTable(records))
  const groups = new Map<string, Record_[]>()
  for (const rec of records) {
    const key = `${rec.set}|${rec.model}|${rec.mode}`
    groups.set(key, [...(groups.get(key) ?? []), rec])
  }
  lines.push("")
  lines.push("## Answers")
  lines.push("")
  lines.push("| set | model | mode | n | cut off at the cap | at least one citation | invalid citation numbers | maths renders | said not covered | input tokens (mean) | output tokens (mean) | reasoning tokens (mean) | latency p50 / p95 s | cost per answer |")
  lines.push("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
  for (const [key, recs] of groups) {
    const [set, model, mode] = key.split("|")
    const mean = (f: (rec: Record_) => number) => recs.reduce((sum, rec) => sum + f(rec), 0) / recs.length
    const lat = recs.map((rec) => rec.latencyMs / 1000)
    lines.push(`| ${set} | ${model} | ${mode} | ${recs.length} | ${pct(recs.filter((rec) => rec.finish === "length").length, recs.length)} | ${pct(recs.filter((rec) => rec.citations > 0).length, recs.length)} | ${recs.filter((rec) => rec.invalidCitations.length > 0).length} answers | ${pct(recs.filter((rec) => rec.mathsFailures === 0).length, recs.length)} | ${pct(recs.filter((rec) => rec.notCovered).length, recs.length)} | ${mean((rec) => rec.usage.prompt).toFixed(0)} | ${mean((rec) => rec.usage.completion).toFixed(0)} | ${mean((rec) => rec.usage.reasoning).toFixed(0)} | ${percentile(lat, 50).toFixed(1)} / ${percentile(lat, 95).toFixed(1)} | $${mean((rec) => rec.cost).toFixed(4)} |`)
  }
  lines.push("")
  lines.push(`## Citation support (sample of ${support.length} cited sentences, ${mainModel})`)
  lines.push("")
  lines.push(SUPPORT_VERDICTS.map((v) => `${v}: ${support.filter((row) => row.verdict === v).length}`).join(" · "))
  lines.push("")
  const doubts = records.filter((rec) => rec.referenceDoubt)
  lines.push(`## Worked answers the judge doubted (${doubts.length})`)
  lines.push("")
  lines.push("These need a person to check. The judge can be wrong.")
  lines.push("")
  for (const rec of doubts) lines.push(`- \`${rec.id}\` (${rec.model}, ${rec.mode}): ${rec.referenceDoubt}`)
  lines.push("")
  lines.push("## Wrong answers")
  lines.push("")
  for (const rec of records.filter((r) => r.grade === "wrong")) lines.push(`- \`${rec.id}\` (${rec.model}, ${rec.mode}): ${rec.gradeReason}`)
  lines.push("")
  const answerCost = records.reduce((sum, rec) => sum + rec.cost, 0)
  const judgeCost = records.reduce((sum, rec) => sum + rec.judgeCost, 0) + supportCost
  lines.push("## Cost")
  lines.push("")
  lines.push(`From the cost xAI reports with each request: answers $${answerCost.toFixed(2)}, judging $${judgeCost.toFixed(2)}, total $${(answerCost + judgeCost).toFixed(2)}.`)
  lines.push("")
  lines.push(`Every answer is in \`${date}-${tag}.jsonl\`; citation checks are in \`${date}-${tag}-support.jsonl\`.`)
  await writeFile(`${base}.md`, lines.join("\n") + "\n")
  console.log(`${base}.md`)
}
