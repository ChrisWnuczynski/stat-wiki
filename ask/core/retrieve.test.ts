import assert from "node:assert/strict"
import test from "node:test"

import type { Candidate } from "./types.ts"
import { bestSimilarity, calibrateThreshold, isCovered, packPassages, rerank } from "./retrieve.ts"

function candidate(patch: Partial<Candidate> & Pick<Candidate, "chunkId" | "entryId" | "score">): Candidate {
  return {
    title: "Other",
    kind: "section",
    chapterId: "chapter:other",
    url: "/other.html",
    part: 0,
    ...patch,
  }
}

test("page boost can outrank a slightly closer chunk", () => {
  const ranked = rerank("how does this page define the gap", [
    candidate({ chunkId: "far#0", entryId: "far", score: 0.56, url: "/far.html" }),
    candidate({ chunkId: "here#0", entryId: "here", score: 0.5, url: "/here.html" }),
  ], {
    pageBoost: 0.08,
    sectionBoost: 0,
    titleBoost: 0,
    definesBoost: 0,
    definesTargets: new Set(),
    pagePath: "/here.html",
  })
  assert.equal(ranked[0].entryId, "here")
})

test("defines-term boost uses the target entry", () => {
  const ranked = rerank("what is the sample mean of these numbers", [
    candidate({ chunkId: "chapter:c#0", entryId: "chapter:c", score: 0.7, title: "Models", kind: "chapter", chapterId: "chapter:c" }),
    candidate({ chunkId: "definition:mean#0", entryId: "definition:mean", score: 0.62, title: "Sample mean", url: "/c.html#mean", chapterId: "chapter:c" }),
  ], {
    pageBoost: 0,
    sectionBoost: 0,
    titleBoost: 0.1,
    definesBoost: 0.06,
    definesTargets: new Set(["definition:mean"]),
  })
  assert.equal(ranked[0].entryId, "definition:mean")
  assert.ok(ranked[0].boosted > ranked[1].boosted)
})

test("turning the page boost off leaves similarity order", () => {
  const options = {
    pageBoost: 0,
    sectionBoost: 0,
    titleBoost: 0,
    definesBoost: 0,
    definesTargets: new Set<string>(),
    pagePath: "/here.html",
  }
  const ranked = rerank("question", [
    candidate({ chunkId: "far#0", entryId: "far", score: 0.56, url: "/far.html" }),
    candidate({ chunkId: "here#0", entryId: "here", score: 0.5, url: "/here.html" }),
  ], options)
  assert.equal(ranked[0].entryId, "far")
})

test("packing stops at k and at the token budget", () => {
  const ranked = [0, 1, 2, 3].map((part) => ({
    ...candidate({ chunkId: `e#${part}`, entryId: "e", score: 1 - part / 10 }),
    boosted: 1 - part / 10,
  }))
  const texts = new Map(ranked.map((item, index) => [item.chunkId, index === 0 ? "short" : "word ".repeat(2000)]))
  const packed = packPassages(ranked, texts, 6, 6000)
  assert.ok(packed.length < 4)
  assert.ok(packed.length >= 1)
  assert.equal(packed[0].n, 1)
  const limited = packPassages(ranked, new Map(ranked.map((item) => [item.chunkId, "short text"])), 2, 6000)
  assert.equal(limited.length, 2)
})

test("threshold calibration keeps most dev questions and rejects low misuse scores", () => {
  const dev = [0.62, 0.7, 0.66, 0.8, 0.71, 0.69, 0.74, 0.68, 0.73, 0.77]
  const misuse = [0.31, 0.28, 0.4, 0.22, 0.35, 0.33, 0.3, 0.26, 0.38, 0.29]
  const result = calibrateThreshold(dev, misuse)
  assert.ok(result.threshold > 0.4)
  assert.ok(result.threshold <= 0.62)
  assert.equal(result.devCovered, 1)
  assert.equal(result.misuseBelow, 1)
  assert.equal(isCovered(0.2, result.threshold), false)
  assert.equal(bestSimilarity([{ score: 0.2 }, { score: 0.5 }]), 0.5)
})
