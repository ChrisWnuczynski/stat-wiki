import assert from "node:assert/strict"
import { dirname, resolve } from "node:path"
import test from "node:test"
import { fileURLToPath } from "node:url"

import { readJsonl, studentLeaks, type MisusePrompt, type StudentQuestion } from "./questions.ts"
import type { WikiDoc } from "./types.ts"

const here = dirname(fileURLToPath(import.meta.url))

test("student questions must not reuse content words from the expected title", () => {
  const doc: WikiDoc = {
    version: 2,
    entries: [
      { id: "definition:bias", kind: "definition", title: "Bias of an estimator", text: "Gap.", url: "/a.html", fingerprint: "1" },
    ],
    edges: [],
  }
  const leaks = studentLeaks(doc, [{
    id: "s",
    question: "What is the bias of that procedure?",
    expect: ["definition:bias"],
  }])
  assert.deepEqual(leaks, [{ id: "s", words: ["bias"] }])
  const clean = studentLeaks(doc, [{
    id: "s2",
    question: "If the long-run average of a procedure misses the quantity it targets, what is that gap?",
    expect: ["definition:bias"],
  }])
  assert.deepEqual(clean, [])
})

test("the checked-in question files have the expected shape", async () => {
  const student = await readJsonl<StudentQuestion>(resolve(here, "../harness/student.jsonl"))
  const misuse = await readJsonl<MisusePrompt>(resolve(here, "../harness/misuse.jsonl"))
  assert.equal(student.length, 50)
  assert.equal(misuse.length, 30)
  assert.equal(new Set(student.map((row) => row.id)).size, 50)
  assert.ok(student.every((row) => row.question && row.expect.length > 0))
  const categories = new Set(misuse.map((row) => row.category))
  for (const category of ["other-subject", "chatbot", "system-prompt", "jailbreak", "offensive"]) {
    assert.ok(categories.has(category))
  }
})
