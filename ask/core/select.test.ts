import assert from "node:assert/strict"
import test from "node:test"

import { FETCH_K } from "./config.ts"
import { rankMatches, takePool, textsFromStored, type ScoredMatch } from "./select.ts"

function match(id: string, score: number, entryId = id): ScoredMatch {
  return {
    id,
    score,
    metadata: { chunkId: `${entryId}#0`, entryId, title: entryId, kind: "section", url: `/${entryId}.html`, chapterId: "chapter:c" },
  }
}

test("closed-book drops excluded entries before the top 20", () => {
  const matches = [match("question:q", 0.9, "question:q"), match("answer:a", 0.8, "answer:a"), match("section:s", 0.7, "section:s")]
  const ranked = rankMatches(matches)
  const closed = takePool(ranked, "closed", new Set(["question:q", "answer:a"]), matches.length)
  assert.deepEqual(closed.candidates.map((candidate) => candidate.entryId), ["section:s"])
  assert.equal(closed.best, 0.7)
  const open = takePool(ranked, "open", new Set(["question:q"]), matches.length)
  assert.equal(open.candidates[0].entryId, "question:q")
})

test("a short closed pool is flagged only when the fetch filled the window", () => {
  const ranked = rankMatches([match("keep", 0.5)])
  assert.equal(takePool(ranked, "closed", new Set(), FETCH_K).short, true)
  assert.equal(takePool(ranked, "closed", new Set(), FETCH_K - 1).short, false)
})

test("stored chunk records yield text and skip malformed values", () => {
  const texts = textsFromStored(new Map([
    ["a#0", JSON.stringify({ text: "Alpha" })],
    ["b#0", "not-json"],
    ["c#0", null],
    ["d#0", JSON.stringify({ text: "" })],
  ]))
  assert.deepEqual([...texts.entries()], [["a#0", "Alpha"]])
})
