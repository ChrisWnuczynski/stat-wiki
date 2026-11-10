import assert from "node:assert/strict"
import test from "node:test"

import { NOT_COVERED_SENTENCE, PROMPT_VERSION, buildPrompt } from "./prompt.ts"
import { deltaFromChunk, parseGrade, looksDeclined } from "./xai.ts"
import { vectorIdFor } from "./text.ts"

test("the prompt is versioned and does not name a course code or a url", () => {
  const prompt = buildPrompt({
    question: "What is a mean?",
    passages: [{ n: 1, text: "The average of the observations." }],
    covered: false,
  })
  assert.equal(prompt.version, PROMPT_VERSION)
  assert.equal(PROMPT_VERSION, "v2")
  assert.match(prompt.system, /Never say you cannot give a link, and never write a URL yourself/)
  assert.match(prompt.system, new RegExp(NOT_COVERED_SENTENCE.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")))
  assert.match(prompt.user, /\[1\] The average/)
  assert.match(prompt.user, /not covering the question/)
  const visible = `${prompt.system}\n${prompt.user}`
  assert.doesNotMatch(visible, /\bSTAT\d/i)
  assert.doesNotMatch(visible, /github/i)
  assert.doesNotMatch(visible, /https?:\/\//i)
})

test("a follow-up keeps the single-question prompt and adds earlier turns", () => {
  const alone = buildPrompt({
    question: "What is a mean?",
    passages: [{ n: 1, text: "The average." }],
    covered: true,
  })
  assert.equal(alone.user, "Question:\nWhat is a mean?\n\nPassages:\n[1] The average.")
  const follow = buildPrompt({
    question: "And the variance?",
    passages: [{ n: 1, text: "Spread." }],
    covered: true,
    history: [
      { role: "user", content: "What is a mean?" },
      { role: "assistant", content: "The average [1]." },
    ],
  })
  assert.match(follow.user, /^Conversation so far:\nReader: What is a mean\?\n\nTutor: The average \[1\]\.\n\nQuestion:/)
})

test("streamed model chunks yield text and ignore the done marker", () => {
  assert.equal(deltaFromChunk('{"choices":[{"delta":{"content":"Hi"}}]}'), "Hi")
  assert.equal(deltaFromChunk("[DONE]"), "")
  assert.equal(deltaFromChunk("not-json"), "")
})

test("grades parse and a not-covered sentence is not a decline", () => {
  const parsed = parseGrade('{"grade":"minor error","reason":"dropped a sign"}')
  assert.deepEqual(parsed, { grade: "minor error", reason: "dropped a sign" })
  assert.equal(parseGrade("no json"), null)
  assert.equal(looksDeclined("StatWiki doesn't cover this directly. A mean is an average."), false)
  assert.equal(looksDeclined("I can only help with statistics, probability, data analysis, or R."), true)
})

test("vector ids fit the 64 byte limit", () => {
  const chunkId = `${"section:".padEnd(90, "x")}#0`
  const id = vectorIdFor(chunkId)
  assert.equal(id.length, 32)
  assert.notEqual(vectorIdFor("a#0"), vectorIdFor("b#0"))
})
