import assert from "node:assert/strict"
import test from "node:test"

import { mathsReport, spanRenders } from "./maths.ts"

test("katex renders a valid span and rejects a broken one", () => {
  assert.equal(spanRenders("$x^2$"), true)
  assert.equal(spanRenders("$$\\frac{1}{2}$$"), true)
  assert.equal(spanRenders("$\\frac{$"), false)
  const report = mathsReport("The mean is $\\bar x$ and $$y^2$$.")
  assert.equal(report.spans, 2)
  assert.equal(report.ok, true)
  const broken = mathsReport("Broken $\\frac{$.")
  assert.equal(broken.ok, false)
})
