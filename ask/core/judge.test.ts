import assert from "node:assert/strict"
import { test } from "node:test"

import { leadingField, parseJsonObject, parseJudge, repairBackslashes } from "./judge.ts"

test("a reply with LaTeX in its strings is read", () => {
  const reply = String.raw`{"grade": "correct", "reason": "The MLEs \(\widehat\mu=\overline x\) and \(\beta\), \theta, \nu, \rho and \frac{1}{n} all match.", "reference_doubt": ""}`
  assert.throws(() => JSON.parse(reply))
  const parsed = parseJudge(reply)
  assert.equal(parsed?.grade, "correct")
  assert.equal(parsed?.reason, String.raw`The MLEs \(\widehat\mu=\overline x\) and \(\beta\), \theta, \nu, \rho and \frac{1}{n} all match.`)
})

test("valid escapes are kept", () => {
  const reply = String.raw`{"verdict": "partly", "reason": "says \"a\\b\" on one line\nthen é"}`
  assert.deepEqual(parseJsonObject(reply), { verdict: "partly", reason: "says \"a\\b\" on one line\nthen é" })
  assert.equal(repairBackslashes(String.raw`\\(x\\)`), String.raw`\\(x\\)`)
})

test("text around the object and unknown grades", () => {
  assert.equal(parseJudge('Here it is: {"grade": "Minor Error", "reason": "slip"} done')?.grade, "minor error")
  assert.equal(parseJudge('{"grade": "great", "reason": "x"}'), null)
  assert.equal(parseJudge(""), null)
  assert.equal(parseJsonObject("[1, 2]"), null)
})

test("a field is read from a reply that was cut off", () => {
  const cut = String.raw`{"grade": "minor error", "reason": "The tutor states that the cross term equals \(2n(\overline X-\mu)^2\) rather than \(`
  assert.equal(parseJudge(cut), null)
  assert.equal(leadingField(cut, "grade"), "minor error")
  assert.equal(leadingField(cut, "verdict"), null)
})
