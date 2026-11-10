import assert from "node:assert/strict"
import test from "node:test"

import { buildGraph } from "../../core/graph.ts"
import type { WikiDoc } from "../../core/types.ts"
import { chapterFor, pageEntryFor } from "./reader.ts"

const doc: WikiDoc = {
  version: 2,
  entries: [
    { id: "chapter:c", kind: "chapter", title: "Counts", text: "Counts.", url: "/notes/counts.html", fingerprint: "1" },
    { id: "question:q", kind: "question", title: "A question", text: "Why?", url: "/questions/q.html", fingerprint: "2" },
    { id: "answer:q", kind: "answer", title: "Worked answer", text: "Because.", url: "/questions/q.html#worked-answer", fingerprint: "3" },
    { id: "section:c:s-one", kind: "section", title: "One count", text: "One.", url: "/notes/counts.html#s-one", fingerprint: "4" },
    { id: "article:counts", kind: "article", title: "Counts", url: "/articles/counts.html", fingerprint: "5", copy_of: "chapter:c" },
  ],
  edges: [
    { from: "question:q", type: "on", to: "chapter:c" },
    { from: "answer:q", type: "of", to: "question:q" },
    { from: "section:c:s-one", type: "in", to: "chapter:c" },
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

test("the reader's place is the section in view, else the page's own entry", () => {
  const graph = buildGraph(doc)
  assert.deepEqual(pageEntryFor(graph, "/notes/counts.html", ""), { entryId: "chapter:c", chunkId: "chapter:c#0", title: "Counts", kind: "chapter", url: "/notes/counts.html" })
  assert.deepEqual(pageEntryFor(graph, "/notes/counts.html", "s-one"), { entryId: "section:c:s-one", chunkId: "section:c:s-one#0", title: "Counts › One count", kind: "section", url: "/notes/counts.html#s-one" })
  assert.equal(pageEntryFor(graph, "/questions/q.html", "")?.entryId, "question:q")
  assert.equal(pageEntryFor(graph, "/articles/counts.html", "")?.chunkId, "chapter:c#0")
  assert.equal(pageEntryFor(graph, "/nowhere.html", ""), null)
  assert.equal(pageEntryFor(graph, "", ""), null)
})
