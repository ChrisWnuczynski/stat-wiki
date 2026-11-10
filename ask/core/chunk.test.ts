import assert from "node:assert/strict"
import { readFileSync } from "node:fs"
import { dirname, resolve } from "node:path"
import test from "node:test"
import { fileURLToPath } from "node:url"

import { chunkDocument, chunkEntry, splitBody } from "./chunk.ts"

const here = dirname(fileURLToPath(import.meta.url))

function entry(text: string, id = "definition:sample") {
  return {
    id,
    kind: "definition",
    title: "Sample",
    text,
    url: "/notes/sample.html#sample",
    fingerprint: "fp",
  }
}

test("a long align environment stays in one chunk", () => {
  const raw = readFileSync(resolve(here, "../harness/fixtures/long-align.md"), "utf8")
  const start = raw.indexOf("\\begin{align*}")
  const end = raw.indexOf("\\end{align*}") + "\\end{align*}".length
  const env = raw.slice(start, end)
  assert.ok(env.length > 3000)
  const chunks = chunkEntry(entry(raw, "fixture:align"), "Displays", "chapter:displays")
  const holders = chunks.filter((chunk) => chunk.text.includes("\\begin{align*}") || chunk.text.includes("\\end{align*}"))
  assert.equal(holders.length, 1)
  assert.ok(holders[0].text.includes(env))
  assert.ok(chunks.some((chunk) => chunk.text.includes("Before the display.")))
  assert.ok(chunks.some((chunk) => chunk.text.includes("After the display.")))
  assert.ok(chunks.every((chunk) => chunk.text.startsWith("Displays › Sample (definition)")))
  assert.deepEqual(chunks.map((chunk) => chunk.id), chunks.map((_, index) => `fixture:align#${index}`))
})

test("paragraphs pack to 3000 characters and repeat the header", () => {
  const paragraph = "word ".repeat(400).trim()
  assert.ok(paragraph.length < 3000)
  assert.ok(paragraph.length * 2 > 3000)
  const text = `${paragraph}\n\n${paragraph}\n\n${paragraph}`
  const chunks = chunkEntry(entry(text), "Chapter", "chapter:c")
  assert.equal(chunks.length, 3)
  for (const chunk of chunks) {
    assert.ok(chunk.text.startsWith("Chapter › Sample (definition)\n\n"))
    const body = chunk.text.split("\n\n").slice(1).join("\n\n")
    assert.ok(body.length <= 3000)
  }
})

test("a protected block longer than 3000 stays whole", () => {
  const fence = "```\n" + "line\n".repeat(800) + "```"
  assert.ok(fence.length > 3000)
  const text = `Intro paragraph.\n\n${fence}\n\nAfter.`
  const parts = splitBody(text)
  const holders = parts.filter((part) => part.includes("```"))
  assert.equal(holders.length, 1)
  assert.ok(holders[0].includes(fence))
  assert.ok(parts[0].includes("Intro paragraph."))
  assert.ok(parts[parts.length - 1].includes("After."))
})

test("display maths with a blank line inside is not split", () => {
  const math = "$$\nx\n\n=\ny\n$$"
  const text = `Intro.\n\n${math}\n\n${"outro ".repeat(400).trim()}`
  const parts = splitBody(text)
  const holders = parts.filter((part) => part.includes("$$"))
  assert.equal(holders.length, 1)
  assert.ok(holders[0].includes(math.trim()))
})

test("a stray dollar does not swallow the next paragraph", () => {
  const left = "Price is $5 today. " + "alpha ".repeat(200)
  const right = "beta ".repeat(500).trim()
  const parts = splitBody(`${left}\n\n${right}`)
  assert.ok(parts.length >= 2)
  assert.ok(parts[parts.length - 1].includes("beta"))
  assert.ok(!parts[parts.length - 1].includes("Price is"))
})

test("inline maths stays intact across the split decision", () => {
  const text = `Before.\n\nThe value is $x^2 + y^2$ exactly.\n\n${"tail ".repeat(700).trim()}`
  const parts = splitBody(text)
  const holder = parts.find((part) => part.includes("$x^2 + y^2$"))
  assert.ok(holder)
  assert.ok(!parts.some((part) => part.includes("$x^2") && !part.includes("$x^2 + y^2$")))
})

test("copy_of entries and empty text are skipped", () => {
  const chunks = chunkDocument({
    version: 2,
    entries: [
      { id: "chapter:c", kind: "chapter", title: "Chapter", text: "Opening.", url: "/c.html", fingerprint: "1" },
      { id: "section:c:s", kind: "section", title: "Kept", text: "Body.", url: "/c.html#s", fingerprint: "2" },
      { id: "article:copy", kind: "article", title: "Copy", url: "/a.html", fingerprint: "2", copy_of: "section:c:s" },
      { id: "figure:blank", kind: "figure", title: "Blank", text: "   ", url: "/f.png", fingerprint: "3" },
    ],
    edges: [{ from: "section:c:s", type: "in", to: "chapter:c" }],
  })
  assert.deepEqual(chunks.map((chunk) => chunk.entryId).sort(), ["chapter:c", "section:c:s"])
  const section = chunks.find((chunk) => chunk.entryId === "section:c:s")
  assert.equal(section?.chapterId, "chapter:c")
  assert.ok(section?.text.startsWith("Chapter › Kept (section)"))
})

test("a chunk's fingerprint changes with its title and chapter title, not only its text", () => {
  const entry = { id: "section:c:s", kind: "section", title: "The Beta--Binomial model", text: "Body.", url: "/c.html#s", fingerprint: "same-text" }
  const before = chunkEntry(entry, "Chapter", "chapter:c")[0].fingerprint
  assert.notEqual(chunkEntry({ ...entry, title: "The Beta\u2013Binomial model" }, "Chapter", "chapter:c")[0].fingerprint, before)
  assert.notEqual(chunkEntry(entry, "New chapter title", "chapter:c")[0].fingerprint, before)
  assert.equal(chunkEntry(entry, "Chapter", "chapter:c")[0].fingerprint, before)
})
