import { CHUNK_CHARS, CHUNKER_VERSION, EMBEDDING_DIMENSIONS, EMBEDDING_MODEL } from "./config.ts"
import type { Chunk } from "./types.ts"
import { vectorIdFor } from "./text.ts"

export type ManifestChunk = { chunkId: string; vectorId: string }

export type ManifestEntry = { fingerprint: string; chunks: ManifestChunk[] }

export type Manifest = {
  embeddingModel: string
  dimensions: number
  chunkerVersion: number
  maxChars: number
  entries: Record<string, ManifestEntry>
}

export type IndexPlan = {
  embed: Chunk[]
  deleteVectorIds: string[]
  deleteChunkIds: string[]
  unchanged: number
}

export function emptyManifest(): Manifest {
  return {
    embeddingModel: EMBEDDING_MODEL,
    dimensions: EMBEDDING_DIMENSIONS,
    chunkerVersion: CHUNKER_VERSION,
    maxChars: CHUNK_CHARS,
    entries: {},
  }
}

export function manifestConfigMatches(manifest: Manifest): boolean {
  return manifest.embeddingModel === EMBEDDING_MODEL
    && manifest.dimensions === EMBEDDING_DIMENSIONS
    && manifest.chunkerVersion === CHUNKER_VERSION
    && manifest.maxChars === CHUNK_CHARS
}

export function planIndex(manifest: Manifest, chunks: Chunk[]): IndexPlan {
  const configOk = manifestConfigMatches(manifest)
  const byEntry = new Map<string, Chunk[]>()
  for (const chunk of chunks) {
    const list = byEntry.get(chunk.entryId) ?? []
    list.push(chunk)
    byEntry.set(chunk.entryId, list)
  }
  const embed: Chunk[] = []
  const deleteVectorIds: string[] = []
  const deleteChunkIds: string[] = []
  let unchanged = 0
  for (const [entryId, list] of byEntry) {
    const previous = manifest.entries[entryId]
    const fingerprint = list[0]?.fingerprint ?? ""
    if (configOk && previous && previous.fingerprint === fingerprint) {
      unchanged++
      continue
    }
    const nextIds = new Set(list.map((chunk) => chunk.id))
    for (const old of previous?.chunks ?? []) {
      if (!nextIds.has(old.chunkId)) {
        deleteVectorIds.push(old.vectorId)
        deleteChunkIds.push(old.chunkId)
      }
    }
    embed.push(...list)
  }
  for (const [entryId, previous] of Object.entries(manifest.entries)) {
    if (byEntry.has(entryId)) continue
    for (const old of previous.chunks) {
      deleteVectorIds.push(old.vectorId)
      deleteChunkIds.push(old.chunkId)
    }
  }
  return { embed, deleteVectorIds, deleteChunkIds, unchanged }
}

export function manifestEntry(chunks: Chunk[]): ManifestEntry {
  return {
    fingerprint: chunks[0]?.fingerprint ?? "",
    chunks: chunks.map((chunk) => ({ chunkId: chunk.id, vectorId: vectorIdFor(chunk.id) })),
  }
}
