import { readFile } from "node:fs/promises"
import { dirname, resolve } from "node:path"
import { fileURLToPath } from "node:url"

import { Cloudflare, type VectorMatch } from "../core/cloudflare.ts"
import {
  ANSWER_MODEL,
  CANDIDATE_K,
  COMPARE_MODEL,
  DEV_SIZE,
  FETCH_K,
  PAGE_BOOST,
  SPLIT_SEED,
  WIKI_URL,
} from "../core/config.ts"
import { chunkDocument } from "../core/chunk.ts"
import { buildGraph, definesDirection, loadWiki } from "../core/graph.ts"
import { excludeIdsForQuestion, findOverlaps } from "../core/overlap.ts"
import { buildPrompt } from "../core/prompt.ts"
import { missingExpect, readJsonl, studentLeaks, type MisusePrompt, type StudentQuestion } from "../core/questions.ts"
import { bestSimilarity, DEFAULT_BOOSTS, isCovered, packPassages, rerank, calibrateThreshold } from "../core/retrieve.ts"
import { mapPool } from "../core/pool.ts"
import { splitBank } from "../core/split.ts"
import type { Candidate } from "../core/types.ts"
import { pagePath, parseArgs, sha256Hex } from "../core/text.ts"
import { completeChat } from "../core/xai.ts"
import { writeRunFiles, type IndexPass, type ScoreRow } from "./report.ts"

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..")

type Work = {
  set: "bank" | "student" | "misuse"
  split: string
  id: string
  question: string
  chapterId: string
  page: string
  exclude: Set<string>
  expect: string[]
  modes: ("open" | "closed")[]
}

type Retrieved = Work & {
  mode: "open" | "closed"
  best: number
  latencyMs: number
  candidates: Candidate[]
  texts: Map<string, string>
  short: boolean
}

const CONFIGS = [
  { name: "page-on-k6", pageBoost: PAGE_BOOST, k: 6 },
  { name: "page-off-k6", pageBoost: 0, k: 6 },
  { name: "page-on-k10", pageBoost: PAGE_BOOST, k: 10 },
  { name: "page-off-k10", pageBoost: 0, k: 10 },
]

function cap<T>(items: T[], limit: number): T[] {
  return limit > 0 ? items.slice(0, limit) : items
}

function toCandidate(match: VectorMatch): Candidate | null {
  const metadata = match.metadata ?? {}
  const entryId = String(metadata.entryId ?? "")
  const chunkId = String(metadata.chunkId ?? "")
  if (!entryId || !chunkId) return null
  return {
    chunkId,
    entryId,
    score: match.score,
    title: String(metadata.title ?? ""),
    kind: String(metadata.kind ?? ""),
    chapterId: String(metadata.chapterId ?? ""),
    url: String(metadata.url ?? ""),
    part: Number(metadata.part ?? 0),
  }
}

async function retrieve(client: Cloudflare, work: Work): Promise<Retrieved[]> {
  const started = Date.now()
  const vector = await client.embedQuery(work.question)
  const embedMs = Date.now() - started
  const queried = Date.now()
  const matches = await client.query(vector, FETCH_K)
  const queryMs = Date.now() - queried
  const ranked = matches
    .map(toCandidate)
    .filter((candidate): candidate is Candidate => candidate !== null)
    .sort((a, b) => b.score - a.score || a.chunkId.localeCompare(b.chunkId))
  const open = ranked.slice(0, CANDIDATE_K)
  const closedAll = ranked.filter((candidate) => !work.exclude.has(candidate.entryId))
  const closed = closedAll.slice(0, CANDIDATE_K)
  const wanted = work.modes.includes("closed") ? [...open, ...closed] : open
  const ids = [...new Set(wanted.map((candidate) => candidate.chunkId))]
  const fetched = Date.now()
  const stored = ids.length > 0 ? await client.kvGetMany(ids) : new Map<string, string | null>()
  const kvMs = Date.now() - fetched
  const texts = new Map<string, string>()
  for (const [key, value] of stored) {
    if (!value) continue
    const parsed = JSON.parse(value) as { text?: string }
    if (parsed.text) texts.set(key, parsed.text)
  }
  const latencyMs = embedMs + queryMs + kvMs
  return work.modes.map((mode) => ({
    ...work,
    mode,
    best: bestSimilarity(mode === "closed" ? closed : open),
    latencyMs,
    candidates: mode === "closed" ? closed : open,
    texts,
    short: mode === "closed" && matches.length >= FETCH_K && closedAll.length < CANDIDATE_K,
  }))
}

async function answerFor(question: string, passages: { n: number; text: string }[], covered: boolean): Promise<string> {
  if (!process.env.XAI_API_KEY?.trim()) return "not called"
  const prompt = buildPrompt({ question, passages, covered })
  const completion = await completeChat({ model: ANSWER_MODEL, system: prompt.system, user: prompt.user })
  return completion.called ? completion.text : "not called"
}

async function readPasses(path: string): Promise<IndexPass[]> {
  try {
    const text = await readFile(path, "utf8")
    return text.split("\n").map((line) => line.trim()).filter(Boolean).map((line) => JSON.parse(line) as IndexPass)
  } catch {
    return []
  }
}

const args = parseArgs(process.argv.slice(2))
const source = typeof args.wiki === "string" ? args.wiki : WIKI_URL
const splitArg = typeof args.split === "string" ? args.split : "dev"
const runAll = args.all === true || splitArg === "all"
const limit = typeof args.limit === "string" ? Number(args.limit) : 0
const outDir = typeof args.out === "string" ? resolve(args.out) : resolve(root, "harness/runs")
if (!runAll && splitArg === "heldout" && typeof args.threshold !== "string") {
  throw new Error("pass --threshold from the dev calibration; held-out is not used to tune")
}

const wiki = await loadWiki(source)
const graph = buildGraph(wiki)
const overlaps = findOverlaps(wiki)
const direction = definesDirection(wiki)
const chunks = chunkDocument(wiki)
const questions = wiki.entries.filter((entry) => entry.kind === "question" && entry.text)
const split = splitBank(questions.map((entry) => entry.id), SPLIT_SEED, DEV_SIZE)
const student = await readJsonl<StudentQuestion>(resolve(root, "harness/student.jsonl"))
const misuse = await readJsonl<MisusePrompt>(resolve(root, "harness/misuse.jsonl"))
const leaks = studentLeaks(wiki, student)
const missing = missingExpect(wiki, student)
if (leaks.length > 0 || missing.length > 0) {
  console.error(JSON.stringify({ leaks: leaks.slice(0, 20), missing: missing.slice(0, 20) }))
  process.exit(1)
}
if (student.length < 45 || misuse.length < 28) {
  throw new Error(`expected about 50 student questions and 30 misuse prompts, found ${student.length} and ${misuse.length}`)
}

const byId = graph.byId
const bankSplits = runAll ? ["dev", "heldout"] : [splitArg]
const work: Work[] = []
for (const name of bankSplits) {
  const ids = cap(name === "heldout" ? split.heldout : split.dev, limit)
  for (const id of ids) {
    const entry = byId.get(id)
    if (!entry?.text) continue
    const answers = graph.answersOf.get(id) ?? []
    work.push({
      set: "bank",
      split: name,
      id,
      question: entry.text,
      chapterId: graph.chapterOf(id) ?? "",
      page: pagePath(entry.url),
      exclude: new Set(excludeIdsForQuestion(id, answers, overlaps)),
      expect: [],
      modes: ["open", "closed"],
    })
  }
}
for (const item of cap(student, limit)) {
  const target = byId.get(item.expect[0])
  const chapterId = item.chapterId || (target ? graph.chapterOf(target.id) ?? "" : "")
  const chapter = chapterId ? byId.get(chapterId) : undefined
  work.push({
    set: "student",
    split: "student",
    id: item.id,
    question: item.question,
    chapterId,
    page: item.page || (chapter ? pagePath(chapter.url) : ""),
    exclude: new Set(),
    expect: item.expect,
    modes: ["open"],
  })
}
for (const item of cap(misuse, limit)) {
  work.push({
    set: "misuse",
    split: "misuse",
    id: item.id,
    question: item.prompt,
    chapterId: "",
    page: "",
    exclude: new Set(),
    expect: [],
    modes: ["open"],
  })
}

const client = await Cloudflare.connect()
const count = await client.vectorCount()
if (count === 0) throw new Error("vector index is empty")
console.log(`retrieving ${work.length} questions from ${count} vectors`)

const retrieved: Retrieved[] = []
let done = 0
await mapPool(work, 4, async (item) => {
  const rows = await retrieve(client, item)
  retrieved.push(...rows)
  done += 1
  if (done % 25 === 0) console.log(`retrieved ${done}/${work.length}`)
})
console.log(`retrieved ${done}/${work.length}`)

const devScores = retrieved.filter((row) => row.set === "bank" && row.split === "dev" && row.mode === "closed").map((row) => row.best)
const misuseScores = retrieved.filter((row) => row.set === "misuse").map((row) => row.best)
const calibration = typeof args.threshold === "string"
  ? { threshold: Number(args.threshold), devCovered: 0, misuseBelow: 0 }
  : calibrateThreshold(devScores, misuseScores)
if (typeof args.threshold === "string") {
  calibration.devCovered = devScores.length === 0 ? 0 : devScores.filter((score) => score >= calibration.threshold).length / devScores.length
  calibration.misuseBelow = misuseScores.length === 0 ? 0 : misuseScores.filter((score) => score < calibration.threshold).length / misuseScores.length
}
console.log(`threshold ${calibration.threshold.toFixed(3)} dev covered ${(100 * calibration.devCovered).toFixed(1)}% misuse below ${(100 * calibration.misuseBelow).toFixed(1)}%`)

const rows: ScoreRow[] = []
for (const config of CONFIGS) {
  for (const item of retrieved) {
    const ranked = rerank(item.question, item.candidates, {
      ...DEFAULT_BOOSTS,
      pageBoost: config.pageBoost,
      definesTargets: graph.definesTargets,
      pagePath: item.page,
      chapterId: item.chapterId,
    })
    const passages = packPassages(ranked, item.texts, config.k)
    const covered = isCovered(item.best, calibration.threshold)
    const chapterHit = item.set === "bank"
      ? (item.chapterId && passages.some((passage) => item.candidates.find((candidate) => candidate.chunkId === passage.chunkId)?.chapterId === item.chapterId) ? "1" : "0")
      : ""
    const expectedHit = item.expect.length > 0
      ? (passages.some((passage) => item.expect.includes(passage.entryId)) ? "1" : "0")
      : ""
    rows.push({
      set: item.set,
      split: item.split,
      mode: item.mode,
      config: config.name,
      questionId: item.id,
      covered,
      best: item.best,
      chapterHit,
      expectedHit,
      passages: passages.length,
      tokens: passages.reduce((sum, passage) => sum + passage.tokens, 0),
      latencyMs: item.latencyMs,
      answer: await answerFor(item.question, passages.map((passage) => ({ n: passage.n, text: passage.text })), covered),
      entries: [...new Set(passages.map((passage) => passage.entryId))].join("|"),
    })
  }
}

const passes = await readPasses(resolve(root, "harness/runs/index-log.jsonl"))
const textEntries = wiki.entries.filter((entry) => entry.text && !entry.copy_of).length
const baseline = await writeRunFiles(outDir, new Date().toISOString().slice(0, 10), {
  rows,
  configs: CONFIGS,
  overlaps,
  threshold: calibration.threshold,
  devCovered: calibration.devCovered,
  misuseBelow: calibration.misuseBelow,
  definesFrom: direction.from,
  definesTo: direction.to,
  wikiVersion: wiki.version,
  wikiSha: sha256Hex(JSON.stringify(wiki)),
  entries: wiki.entries.length,
  textEntries,
  questions: questions.length,
  answers: wiki.entries.filter((entry) => entry.kind === "answer" && entry.text).length,
  chunks: chunks.length,
  passes,
  answerModel: ANSWER_MODEL,
  compareModel: COMPARE_MODEL,
  xaiCalled: Boolean(process.env.XAI_API_KEY?.trim()),
  devSize: split.dev.length,
  heldoutSize: split.heldout.length,
  closedShort: retrieved.filter((row) => row.short).length,
})
console.log(baseline)
