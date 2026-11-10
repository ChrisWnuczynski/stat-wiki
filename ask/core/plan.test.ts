import assert from "node:assert/strict"
import test from "node:test"

import { emptyManifest, planIndex } from "./plan.ts"
import type { Chunk } from "./types.ts"

function chunk(id: string, fingerprint: string): Chunk {
  const entryId = id.split("#")[0]
  return {
    id,
    entryId,
    part: Number(id.split("#")[1]),
    text: `text ${id}`,
    url: "/x.html",
    title: "T",
    kind: "section",
    chapterId: null,
    chapterTitle: null,
    fingerprint,
  }
}

test("unchanged fingerprints are kept and missing entries are deleted", () => {
  const manifest = emptyManifest()
  manifest.entries = {
    a: { fingerprint: "same", chunks: [{ chunkId: "a#0", vectorId: "va" }] },
    b: { fingerprint: "old", chunks: [{ chunkId: "b#0", vectorId: "vb" }] },
    gone: { fingerprint: "g", chunks: [{ chunkId: "gone#0", vectorId: "vg" }] },
  }
  const plan = planIndex(manifest, [chunk("a#0", "same"), chunk("b#0", "new"), chunk("b#1", "new")])
  assert.equal(plan.unchanged, 1)
  assert.deepEqual(plan.embed.map((item) => item.id), ["b#0", "b#1"])
  assert.deepEqual(plan.deleteVectorIds.sort(), ["vg"])
  assert.deepEqual(plan.deleteChunkIds, ["gone#0"])
})

test("a changed entry drops chunk ids that disappeared", () => {
  const manifest = emptyManifest()
  manifest.entries = {
    a: {
      fingerprint: "old",
      chunks: [
        { chunkId: "a#0", vectorId: "v0" },
        { chunkId: "a#1", vectorId: "v1" },
      ],
    },
  }
  const plan = planIndex(manifest, [chunk("a#0", "new")])
  assert.deepEqual(plan.embed.map((item) => item.id), ["a#0"])
  assert.deepEqual(plan.deleteVectorIds, ["v1"])
})
