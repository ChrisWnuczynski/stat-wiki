import assert from "node:assert/strict"
import test from "node:test"

import { buildTurns, extractMath, linkCitations, mapOutsideCode, MAX_TURNS, normalizeDelimiters, safePage, type Msg } from "./text.ts"

test("\\( \\) and \\[ \\] become dollar delimiters, but not inside code", () => {
  assert.equal(normalizeDelimiters("Here \\(n\\) and \\[x^2\\]."), "Here $n$ and $$x^2$$.")
  assert.equal(normalizeDelimiters("`\\(n\\)` stays"), "`\\(n\\)` stays")
})

test("formulas are lifted out, prices are not", () => {
  const { text, maths } = extractMath("The mean $\\bar x_n$ costs $5 and $10, and $$\\sum_{i=1}^n x_i$$ too.")
  assert.deepEqual(maths, [{ tex: "\\sum_{i=1}^n x_i", display: true }, { tex: "\\bar x_n", display: false }])
  assert.match(text, /costs \$5 and \$10/)
  assert.equal(text.includes("_"), false)
})

test("maths inside code is left alone", () => {
  const { text, maths } = extractMath("Run `mean(x$y)` then $a$.\n\n```r\nx$y <- 1\n```")
  assert.equal(maths.length, 1)
  assert.match(text, /`mean\(x\$y\)`/)
  assert.match(text, /x\$y <- 1/)
})

test("an unfinished code fence during streaming is still treated as code", () => {
  assert.equal(mapOutsideCode("a $x$ ```r\ny$z", (part) => part.toUpperCase()), "A $X$ ```r\ny$z")
})

test("only numbers the Worker returned become citation buttons", () => {
  const html = linkCitations("<p>Mean [1]. Both [1, 2]. Stray [9].</p>", new Set([1, 2]))
  assert.equal((html.match(/class="ask-cite"/g) ?? []).length, 3)
  assert.equal(html.includes("[9]"), false)
  assert.equal(html.includes("9"), false)
  assert.match(html, /Stray\.<\/p>/)
  assert.match(html, /Mean<button/)
})

test("turns keep the newest exchanges, start on a question and end on the new one", () => {
  const history: Msg[] = []
  for (let i = 0; i < 5; i++) {
    history.push({ id: `u${i}`, role: "user", content: `q${i}` })
    history.push({ id: `a${i}`, role: "assistant", content: `a${i}`, state: "done" })
  }
  history.push({ id: "bad", role: "assistant", content: "half", state: "error" })
  const turns = buildTurns(history, "new")
  assert.ok(turns.length <= MAX_TURNS)
  assert.equal(turns[0].role, "user")
  assert.deepEqual(turns.at(-1), { role: "user", content: "new" })
  assert.equal(turns.some((t) => t.content === "half"), false)
})

test("only plain root-relative page paths are sent", () => {
  assert.equal(safePage("/notes/prob-03-simulation.html"), "/notes/prob-03-simulation.html")
  assert.equal(safePage("/notes/a b.html"), "")
  assert.equal(safePage("javascript:alert(1)"), "")
})
