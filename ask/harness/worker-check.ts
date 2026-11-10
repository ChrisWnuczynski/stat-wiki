import { mkdir, writeFile } from "node:fs/promises"
import { dirname, resolve } from "node:path"
import { fileURLToPath } from "node:url"

import { Cloudflare } from "../core/cloudflare.ts"
import {
  COVERAGE_THRESHOLD,
  FETCH_K,
  PAGE_BOOST,
  QUESTION_CHAR_LIMIT,
  SPLIT_SEED,
  WIKI_URL,
  WORKER_K,
} from "../core/config.ts"
import { buildGraph } from "../core/graph.ts"
import { excludeIdsForQuestion, findOverlaps } from "../core/overlap.ts"
import { readJsonl, type MisusePrompt } from "../core/questions.ts"
import { DEFAULT_BOOSTS, isCovered, packPassages, rerank } from "../core/retrieve.ts"
import { rankMatches, takePool, textsFromStored } from "../core/select.ts"
import { splitBank } from "../core/split.ts"
import { pagePath, parseArgs } from "../core/text.ts"
import { loadWiki } from "../core/wiki-file.ts"
import { looksDeclined } from "../core/xai.ts"

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..")

type Passage = { n: number; chunkId: string; id: string; chapterId: string; score: number }

function events(text: string): { event: string; data: Record<string, unknown> }[] {
  return text.split("\n\n").filter(Boolean).map((block) => {
    const event = block.split("\n").find((line) => line.startsWith("event:"))?.slice(6).trim() ?? ""
    const raw = block.split("\n").find((line) => line.startsWith("data:"))?.slice(5).trim() ?? "{}"
    return { event, data: JSON.parse(raw) as Record<string, unknown> }
  })
}

const args = parseArgs(process.argv.slice(2))
const worker = typeof args.worker === "string" ? args.worker.replace(/\/$/, "") : ""
const limit = typeof args.limit === "string" ? Number(args.limit) : 5
const token = process.env.DEV_ASK_TOKEN?.trim() ?? ""
if (!worker) throw new Error("pass --worker")
if (!token) throw new Error("DEV_ASK_TOKEN is missing")

const wiki = await loadWiki(typeof args.wiki === "string" ? args.wiki : WIKI_URL)
const graph = buildGraph(wiki)
const overlaps = findOverlaps(wiki)
const questions = wiki.entries.filter((entry) => entry.kind === "question" && entry.text)
const dev = splitBank(questions.map((entry) => entry.id), SPLIT_SEED).dev.slice(0, limit > 0 ? limit : 5)
const misuse = await readJsonl<MisusePrompt>(resolve(root, "harness/misuse.jsonl"))
const client = await Cloudflare.connect()

type Offline = { best: number; covered: boolean; passages: Passage[]; chapterHit: boolean }

async function offline(question: string, page: string, chapterId: string, exclude: Set<string>): Promise<Offline> {
  const vector = await client.embedQuery(question)
  const matches = await client.query(vector, FETCH_K)
  const ranked = rankMatches(matches)
  const pool = takePool(ranked, "closed", exclude, matches.length)
  const ids = pool.candidates.map((candidate) => candidate.chunkId)
  const texts = textsFromStored(ids.length > 0 ? await client.kvGetMany(ids) : new Map())
  const reranked = rerank(question, pool.candidates, {
    ...DEFAULT_BOOSTS,
    pageBoost: PAGE_BOOST,
    definesTargets: graph.definesTargets,
    pagePath: page,
    chapterId,
  })
  const packed = packPassages(reranked, texts, WORKER_K)
  const byChunk = new Map(reranked.map((candidate) => [candidate.chunkId, candidate]))
  const passages = packed.map((passage) => ({
    n: passage.n,
    chunkId: passage.chunkId,
    id: passage.entryId,
    chapterId: byChunk.get(passage.chunkId)?.chapterId ?? "",
    score: byChunk.get(passage.chunkId)?.score ?? 0,
  }))
  return {
    best: pool.best,
    covered: isCovered(pool.best, COVERAGE_THRESHOLD),
    passages,
    chapterHit: Boolean(chapterId) && passages.some((passage) => passage.chapterId === chapterId),
  }
}

async function post(path: string, body: unknown, session: string): Promise<{ status: number; text: string }> {
  const response = await fetch(`${worker}${path}`, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "user-agent": "statwiki-ask-harness/1.0",
      "x-dev-ask-token": token,
      "x-dev-session": session,
    },
    body: JSON.stringify(body),
  })
  return { status: response.status, text: await response.text() }
}

const rows: string[] = []
let samePassages = 0
let sameChapter = 0
let asked = 0
for (const id of dev) {
  const entry = graph.byId.get(id)
  if (!entry?.text) continue
  if (entry.text.length > QUESTION_CHAR_LIMIT) {
    rows.push(`| ${id} | over the 2000 character cap | | | | |`)
    continue
  }
  const chapterId = graph.chapterOf(id) ?? ""
  const page = pagePath(entry.url)
  const exclude = new Set(excludeIdsForQuestion(id, graph.answersOf.get(id) ?? [], overlaps))
  const local = await offline(entry.text, page, chapterId, exclude)
  const remote = await post("/ask", {
    turns: [{ role: "user", content: entry.text }],
    page,
    anchor: "",
    exclude: [...exclude],
    compare: true,
  }, `dev-${asked + 1}`)
  asked += 1
  if (remote.status !== 200) {
    rows.push(`| ${id} | ${local.passages.map((passage) => passage.chunkId).join(" ")} | status ${remote.status} | no | ${local.chapterHit ? "yes" : "no"} | |`)
    continue
  }
  const parsed = events(remote.text)
  const retrieval = parsed.find((event) => event.event === "retrieval")?.data as {
    best?: number
    covered?: boolean
    passages?: Passage[]
  } | undefined
  const remotePassages = retrieval?.passages ?? []
  const localIds = local.passages.map((passage) => passage.chunkId).join(" ")
  const remoteIds = remotePassages.map((passage) => passage.chunkId).join(" ")
  const passagesMatch = localIds === remoteIds
  const remoteChapter = Boolean(chapterId) && remotePassages.some((passage) => passage.chapterId === chapterId)
  const chapterMatch = local.chapterHit === remoteChapter
  if (passagesMatch) samePassages += 1
  if (chapterMatch) sameChapter += 1
  const bestDelta = retrieval?.best === undefined ? "" : (retrieval.best - local.best).toFixed(4)
  rows.push(`| ${id} | ${localIds || "(none)"} | ${remoteIds || "(none)"} | ${passagesMatch ? "yes" : "no"} | ${local.chapterHit ? "yes" : "no"} | ${remoteChapter ? "yes" : "no"} | ${bestDelta} | ${local.covered === retrieval?.covered ? "yes" : "no"} |`)
  console.log(`compared ${asked}/${dev.length} passages ${passagesMatch ? "match" : "differ"}`)
}

let declined = 0
let misuseCalled = 0
const misuseRows: string[] = []
for (const item of misuse) {
  const remote = await post("/ask", {
    turns: [{ role: "user", content: item.prompt }],
    page: "",
    anchor: "",
  }, item.id)
  misuseCalled += 1
  if (remote.status !== 200) {
    misuseRows.push(`| ${item.id} | ${item.category} | status ${remote.status} |`)
    continue
  }
  const text = events(remote.text).filter((event) => event.event === "delta").map((event) => String(event.data.text ?? "")).join("")
  const ok = looksDeclined(text)
  if (ok) declined += 1
  misuseRows.push(`| ${item.id} | ${item.category} | ${ok ? "declined" : "not declined"} |`)
  console.log(`misuse ${misuseCalled}/${misuse.length} ${ok ? "declined" : "not declined"}`)
}

const date = new Date().toISOString().slice(0, 10)
const report = `# Worker check ${date}

Closed-book dev questions, limit ${dev.length}, against the deployed Worker. Offline retrieval uses the same selector, reranker, k=${WORKER_K}, page boost ${PAGE_BOOST}, and threshold ${COVERAGE_THRESHOLD.toFixed(3)}.

Passage lists matched ${samePassages} of ${asked}. Chapter hit agreed on ${sameChapter} of ${asked}.

| question | offline chunks | worker chunks | same passages | offline chapter | worker chapter | best delta | same covered |
| --- | --- | --- | --- | --- | --- | --- | --- |
${rows.join("\n")}

## Misuse

The misuse set was sent to the deployed Worker. Declined ${declined} of ${misuse.filter((item) => item.prompt.length <= QUESTION_CHAR_LIMIT).length}. Answers are not stored.

| id | category | result |
| --- | --- | --- |
${misuseRows.join("\n")}
`
const out = resolve(root, `harness/runs/${date}-worker.md`)
await mkdir(dirname(out), { recursive: true })
await writeFile(out, report)
console.log(out)
console.log(`passages ${samePassages}/${asked} chapter ${sameChapter}/${asked} misuse ${declined}/${misuseCalled}`)
