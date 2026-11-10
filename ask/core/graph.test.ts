import assert from "node:assert/strict"
import test from "node:test"

import { buildGraph, definesDirection } from "./graph.ts"
import { splitBank } from "./split.ts"
import type { WikiDoc } from "./types.ts"

const doc: WikiDoc = {
  version: 2,
  entries: [
    { id: "chapter:c", kind: "chapter", title: "Models", text: "Open.", url: "/c.html", fingerprint: "c" },
    { id: "section:c:s", kind: "section", title: "Mean", text: "Body.", url: "/c.html#s", fingerprint: "s" },
    { id: "definition:mean", kind: "definition", title: "Sample mean", text: "Def.", url: "/c.html#mean", fingerprint: "d" },
    { id: "article:mean", kind: "article", title: "About the mean", text: "Art.", url: "/articles/mean.html", fingerprint: "art" },
    { id: "question:q", kind: "question", title: "Q", text: "Ask.", url: "/questions/q.html", fingerprint: "q" },
    { id: "answer:q", kind: "answer", title: "A", text: "Solved.", url: "/questions/q.html#worked-answer", fingerprint: "a" },
  ],
  edges: [
    { from: "section:c:s", type: "in", to: "chapter:c" },
    { from: "definition:mean", type: "stated-in", to: "chapter:c" },
    { from: "chapter:c", type: "defines", to: "definition:mean" },
    { from: "article:mean", type: "for", to: "section:c:s" },
    { from: "question:q", type: "on", to: "chapter:c" },
    { from: "answer:q", type: "of", to: "question:q" },
  ],
}

test("chapter links follow in, for, of, and defines from the chapter", () => {
  const graph = buildGraph(doc)
  assert.equal(graph.chapterOf("section:c:s"), "chapter:c")
  assert.equal(graph.chapterOf("article:mean"), "chapter:c")
  assert.equal(graph.chapterOf("answer:q"), "chapter:c")
  assert.equal(graph.chapterOf("definition:mean"), "chapter:c")
  assert.ok(graph.definesTargets.has("definition:mean"))
  assert.deepEqual(graph.answersOf.get("question:q"), ["answer:q"])
  assert.deepEqual(definesDirection(doc).from, { chapter: 1 })
})

test("the bank split is fixed at 100 and 445 for 545 ids", () => {
  const ids = Array.from({ length: 545 }, (_, index) => `question:${index}`)
  const first = splitBank(ids)
  const second = splitBank(ids)
  assert.equal(first.dev.length, 100)
  assert.equal(first.heldout.length, 445)
  assert.deepEqual(first, second)
  assert.equal(new Set([...first.dev, ...first.heldout]).size, 545)
})
