import assert from "node:assert/strict"
import test from "node:test"

import { findOverlaps, textsOverlap } from "./overlap.ts"
import type { WikiDoc } from "./types.ts"

test("a copied 40-word stretch is an overlap even with a prefix", () => {
  const words = Array.from({ length: 45 }, (_, index) => `token${index}`).join(" ")
  const answer = `The solution starts here.\n\n${words}`
  const section = `A lead-in sentence sits above the copy.\n\n${words}\n\nTrailing remark.`
  assert.equal(textsOverlap(answer, section), true)
  const doc: WikiDoc = {
    version: 2,
    entries: [
      { id: "question:q", kind: "question", title: "Q", text: "Ask.", url: "/q.html", fingerprint: "q" },
      { id: "answer:q", kind: "answer", title: "A", text: answer, url: "/q.html#worked-answer", fingerprint: "a" },
      { id: "section:s", kind: "section", title: "Copied solution", text: section, url: "/s.html", fingerprint: "s" },
      { id: "section:other", kind: "section", title: "Different", text: "This paragraph shares no long stretch with the worked solution at all.", url: "/o.html", fingerprint: "o" },
    ],
    edges: [{ from: "answer:q", type: "of", to: "question:q" }],
  }
  const hits = findOverlaps(doc)
  assert.deepEqual(hits.map((hit) => hit.entryId), ["section:s"])
})

test("a shared short phrase is not an overlap", () => {
  assert.equal(
    textsOverlap("The mean of the sample is large.", "The mean of the sample is small and the rest of this section is original."),
    false,
  )
})

test("a copied paragraph of at least 180 characters is an overlap", () => {
  const paragraph = "alpha ".repeat(40).trim()
  assert.ok(paragraph.length >= 180)
  assert.equal(textsOverlap(`Intro.\n\n${paragraph}`, `Notes.\n\n${paragraph}\n\nMore.`), true)
})
