import assert from "node:assert/strict"
import test from "node:test"

import { NOT_COVERED_SENTENCE, PROMPT_VERSION, buildPrompt } from "./prompt.ts"
import { parseGrade, looksDeclined } from "./xai.ts"
import { vectorIdFor } from "./text.ts"

test("the prompt is versioned and does not name a course code or a url", () => {
  const prompt = buildPrompt({
    question: "What is a mean?",
    passages: [{ n: 1, text: "The average of the observations." }],
    covered: false,
  })
  assert.equal(prompt.version, PROMPT_VERSION)
  assert.equal(PROMPT_VERSION, "v1")
  assert.match(prompt.system, new RegExp(NOT_COVERED_SENTENCE.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")))
  assert.match(prompt.user, /\[1\] The average/)
  assert.match(prompt.user, /not covering the question/)
  const visible = `${prompt.system}\n${prompt.user}`
  assert.doesNotMatch(visible, /\bSTAT\d/i)
  assert.doesNotMatch(visible, /github/i)
  assert.doesNotMatch(visible, /https?:\/\//i)
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
