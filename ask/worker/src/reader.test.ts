import assert from "node:assert/strict"
import test from "node:test"

import { buildGraph } from "../../core/graph.ts"
import type { WikiDoc } from "../../core/types.ts"
import { chapterFor } from "./reader.ts"

const doc: WikiDoc = {
  version: 2,
  entries: [
    { id: "chapter:c", kind: "chapter", title: "Counts", text: "Counts.", url: "/notes/counts.html", fingerprint: "1" },
    { id: "question:q", kind: "question", title: "A question", text: "Why?", url: "/questions/q.html", fingerprint: "2" },
    { id: "answer:q", kind: "answer", title: "Worked answer", text: "Because.", url: "/questions/q.html#worked-answer", fingerprint: "3" },
  ],
  edges: [
    { from: "question:q", type: "on", to: "chapter:c" },
    { from: "answer:q", type: "of", to: "question:q" },
  ],
}

test("the page and the anchor resolve to the chapter", () => {
  const graph = buildGraph(doc)
  assert.equal(chapterFor(graph, "/notes/counts.html", ""), "chapter:c")
  assert.equal(chapterFor(graph, "/questions/q.html", ""), "chapter:c")
  assert.equal(chapterFor(graph, "/questions/q.html", "worked-answer"), "chapter:c")
  assert.equal(chapterFor(graph, "/questions/q.html", "question:q"), "chapter:c")
  assert.equal(chapterFor(graph, "", "question:q"), "")
})
