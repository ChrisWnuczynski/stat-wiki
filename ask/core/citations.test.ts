import assert from "node:assert/strict"
import test from "node:test"

import { citationsFromAnswer, publicCitations } from "./citations.ts"

const passages = [
  { n: 1, entryId: "definition:mean", url: "/notes/a.html#mean" },
  { n: 2, entryId: "definition:mean", url: "/notes/a.html#mean" },
  { n: 3, entryId: "theorem:var", url: "/notes/a.html#var" },
]

test("several chunks from one entry become one citation", () => {
  const citations = citationsFromAnswer("The average is [1]. The same page adds [2]. Spread is [3].", passages)
  assert.deepEqual(citations, [
    { entryId: "definition:mean", url: "/notes/a.html#mean", numbers: [1, 2] },
    { entryId: "theorem:var", url: "/notes/a.html#var", numbers: [3] },
  ])
})

test("numbers outside 1..k are dropped", () => {
  const citations = citationsFromAnswer("See [0], [1], [3], [4], and [1, 9].", passages)
  assert.deepEqual(citations.map((citation) => citation.entryId), ["definition:mean", "theorem:var"])
  assert.deepEqual(citations[0].numbers, [1])
  assert.deepEqual(citations[1].numbers, [3])
})

test("a comma list maps each in-range number", () => {
  const citations = citationsFromAnswer("Both [1, 3] matter.", passages)
  assert.equal(citations.length, 2)
})

test("the public list has number, id, title, kind, and url", () => {
  const items = publicCitations("See [1] and [2] and [8] and [the notes](https://evil.example).", [
    { n: 1, entryId: "definition:mean", url: "/notes/a.html#mean", title: "Mean", kind: "definition" },
    { n: 2, entryId: "definition:mean", url: "/notes/a.html#mean", title: "Mean", kind: "definition" },
    { n: 3, entryId: "theorem:var", url: "/notes/a.html#var", title: "Variance", kind: "theorem" },
  ])
  assert.deepEqual(items, [
    { number: 1, id: "definition:mean", title: "Mean", kind: "definition", url: "/notes/a.html#mean" },
    { number: 2, id: "definition:mean", title: "Mean", kind: "definition", url: "/notes/a.html#mean" },
  ])
  assert.equal(JSON.stringify(items).includes("evil.example"), false)
})

test("model output is not treated as a url citation", () => {
  const citations = citationsFromAnswer("See [the notes](https://example.com) and [2].", passages)
  assert.deepEqual(citations.map((citation) => citation.numbers), [[2]])
})
