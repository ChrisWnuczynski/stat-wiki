import { appendFile, mkdir } from "node:fs/promises"
import { dirname, resolve } from "node:path"
import { fileURLToPath } from "node:url"

import { Cloudflare, embedDocumentsResilient } from "../core/cloudflare.ts"
import {
  CHUNK_CHARS,
  CHUNKER_VERSION,
  EMBEDDING_DIMENSIONS,
  EMBEDDING_MODEL,
  WIKI_URL,
} from "../core/config.ts"
import { chunkDocument, headerLine } from "../core/chunk.ts"
import { loadWiki } from "../core/wiki-file.ts"
import { emptyManifest, manifestConfigMatches, manifestEntry, planIndex, type Manifest } from "../core/plan.ts"
import { batches, mapPool } from "../core/pool.ts"
import type { Chunk } from "../core/types.ts"
import { parseArgs, sha256Hex, vectorIdFor } from "../core/text.ts"

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..")
const logPath = resolve(root, "harness/runs/index-log.jsonl")

function sleep(ms: number): Promise<void> {
  return new Promise((resolvePromise) => setTimeout(resolvePromise, ms))
}

function metadata(chunk: Chunk): Record<string, string | number> {
  const fields: Record<string, string | number> = {
    chunkId: chunk.id,
    entryId: chunk.entryId,
    part: chunk.part,
    kind: chunk.kind,
    title: chunk.title,
    url: chunk.url,
    chars: chunk.text.length,
  }
  if (chunk.chapterId) fields.chapterId = chunk.chapterId
  if ("text" in fields) throw new Error("refusing to store chunk text in vector metadata")
  return fields
}

async function loadManifest(client: Cloudflare): Promise<Manifest> {
  const stored = await client.kvGetMany(["manifest"])
  const raw = stored.get("manifest")
  if (!raw) return emptyManifest()
  return JSON.parse(raw) as Manifest
}

async function saveManifest(client: Cloudflare, manifest: Manifest): Promise<void> {
  await client.kvPut([{ key: "manifest", value: JSON.stringify(manifest) }])
}

const args = parseArgs(process.argv.slice(2))
const source = typeof args.wiki === "string" ? args.wiki : WIKI_URL
const wiki = await loadWiki(source)
const wikiSha = sha256Hex(JSON.stringify(wiki))
const chunks = chunkDocument(wiki)
const bodies = chunks.map((chunk) => {
  const header = headerLine(chunk.chapterTitle, chunk.title, chunk.kind)
  return Math.max(0, chunk.text.length - header.length - 2)
})
const over = bodies.filter((size) => size > CHUNK_CHARS).length
const maxBody = bodies.length === 0 ? 0 : Math.max(...bodies)
console.log(`wiki version ${wiki.version} entries ${wiki.entries.length} chunks ${chunks.length}`)
console.log(`max body ${maxBody} bodies over ${CHUNK_CHARS}: ${over}`)
for (const chunk of chunks) {
  const header = headerLine(chunk.chapterTitle, chunk.title, chunk.kind)
  const body = Math.max(0, chunk.text.length - header.length - 2)
  if (body > CHUNK_CHARS) console.log(`unsplittable ${chunk.id} body ${body}`)
}
if (args.plan) process.exit(0)

const client = await Cloudflare.connect()
const manifest = await loadManifest(client)
if (!manifestConfigMatches(manifest)) {
  for (const entry of Object.values(manifest.entries)) entry.fingerprint = ""
  manifest.embeddingModel = EMBEDDING_MODEL
  manifest.dimensions = EMBEDDING_DIMENSIONS
  manifest.chunkerVersion = CHUNKER_VERSION
  manifest.maxChars = CHUNK_CHARS
  await saveManifest(client, manifest)
  console.log("index config changed; re-embedding stored entries")
}

const plan = planIndex(manifest, chunks)
console.log(`embed ${plan.embed.length} delete ${plan.deleteVectorIds.length} unchanged ${plan.unchanged}`)
if (plan.deleteVectorIds.length > 0) await client.deleteVectors(plan.deleteVectorIds)
if (plan.deleteChunkIds.length > 0) await client.kvDelete(plan.deleteChunkIds)

const liveIds = new Set(chunks.map((chunk) => chunk.entryId))
for (const id of Object.keys(manifest.entries)) {
  if (!liveIds.has(id)) delete manifest.entries[id]
}

let saved = Promise.resolve()
let sinceSave = 0
let embedded = 0
const needed = new Map<string, number>()
const finished = new Map<string, number>()
for (const chunk of plan.embed) needed.set(chunk.entryId, (needed.get(chunk.entryId) ?? 0) + 1)

function remember(chunkList: Chunk[]): Promise<void> {
  const run = saved.then(async () => {
    for (const chunk of chunkList) {
      finished.set(chunk.entryId, (finished.get(chunk.entryId) ?? 0) + 1)
      if (finished.get(chunk.entryId) === needed.get(chunk.entryId)) {
        const group = plan.embed.filter((item) => item.entryId === chunk.entryId)
        manifest.entries[chunk.entryId] = manifestEntry(group)
      }
    }
    embedded += chunkList.length
    sinceSave += chunkList.length
    if (sinceSave >= 24) {
      await saveManifest(client, manifest)
      sinceSave = 0
      console.log(`embedded ${embedded}/${plan.embed.length}`)
    }
  })
  saved = run.then(() => undefined, () => undefined)
  return run
}

await mapPool(batches(plan.embed, 24), 3, async (batch) => {
  const vectors = await embedDocumentsResilient(client, batch.map((chunk) => chunk.text))
  await client.upsert(batch.map((chunk, index) => ({
    id: vectorIdFor(chunk.id),
    values: vectors[index],
    metadata: metadata(chunk),
  })))
  await client.kvPut(batch.map((chunk) => ({
    key: chunk.id,
    value: JSON.stringify({
      text: chunk.text,
      entryId: chunk.entryId,
      part: chunk.part,
      fingerprint: chunk.fingerprint,
    }),
  })))
  await remember(batch)
})
await saved
if (embedded > 0 || plan.deleteVectorIds.length > 0 || plan.deleteChunkIds.length > 0) {
  await saveManifest(client, manifest)
}
console.log(`embedded ${embedded}/${plan.embed.length}`)

let vectorCount = 0
for (let attempt = 0; attempt < 80; attempt++) {
  vectorCount = await client.vectorCount()
  console.log(`vector count ${vectorCount}/${chunks.length}`)
  if (vectorCount >= chunks.length) break
  await sleep(5000)
}

await mkdir(dirname(logPath), { recursive: true })
await appendFile(logPath, `${JSON.stringify({
  at: new Date().toISOString(),
  embedded,
  deleted: plan.deleteVectorIds.length,
  unchanged: plan.unchanged,
  chunks: chunks.length,
  maxBody,
  bodiesOverLimit: over,
  vectorCount,
  wikiSha256: wikiSha,
  model: EMBEDDING_MODEL,
})}\n`)
console.log(`index log ${logPath}`)
