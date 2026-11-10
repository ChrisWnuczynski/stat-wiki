// Rescore: reads the judge's grade from replies an earlier answer check could
// not parse and rewrites that run's files. No model calls.
//
// Runs before the parser fix counted every judge reply it could not parse as
// "did not answer". The replies did carry a grade; the JSON was invalid only
// because of LaTeX backslashes inside it. The run files kept the first 120
// characters of each such reply, which is enough to read the grade.
//
//   node --experimental-strip-types harness/rescore.ts harness/runs/2026-11-10-dev-closed

import { existsSync } from "node:fs"
import { readFile, writeFile } from "node:fs/promises"

import { GRADES, leadingField, UNREADABLE, type Grade } from "../core/judge.ts"
import { correctnessTable, SUPPORT_VERDICTS } from "./answers.ts"

const PREFIX = "judge output was not a grade: "
const START = "<!-- rescore -->"
const END = "<!-- /rescore -->"

type Rec = { set: string; id: string; model: string; mode: string; grade: string; gradeReason: string; rescored?: boolean }
type Support = { verdict: string; reason: string; rescored?: boolean }

const readRows = async <T>(file: string): Promise<T[]> =>
  (await readFile(file, "utf8")).split("\n").filter((line) => line.trim()).map((line) => JSON.parse(line) as T)

const writeRows = (file: string, rows: unknown[]) => writeFile(file, rows.map((row) => JSON.stringify(row)).join("\n") + "\n")

// The reason as far as the saved text goes.
function partialReason(raw: string): string {
  const match = raw.match(/"reason"\s*:\s*"((?:[^"\\]|\\.)*)("?)/)
  if (!match) return ""
  return match[1].replace(/\\\\/g, "\\").replace(/\s+/g, " ").trim() + (match[2] ? "" : " …")
}

// Replaces the run of table rows that starts with the header line.
function replaceTable(lines: string[], header: string, table: string[]): string[] {
  const at = lines.findIndex((line) => line.startsWith(header))
  if (at < 0) return lines
  let end = at
  while (end < lines.length && lines[end].startsWith("|")) end += 1
  return [...lines.slice(0, at), ...table, ...lines.slice(end)]
}

const base = process.argv[2]?.replace(/\.(md|jsonl)$/, "")
if (!base) throw new Error("usage: rescore.ts harness/runs/<date>-<tag>")

const records = await readRows<Rec>(`${base}.jsonl`)
for (const rec of records) {
  if (!rec.gradeReason.startsWith(PREFIX)) continue
  const raw = rec.gradeReason.slice(PREFIX.length)
  const grade = leadingField(raw, "grade")
  rec.rescored = true
  if (grade && GRADES.includes(grade as Grade)) {
    rec.grade = grade
    rec.gradeReason = partialReason(raw)
  } else {
    rec.grade = UNREADABLE
  }
}
await writeRows(`${base}.jsonl`, records)
// Counted from the flags so that a second run reports the same numbers.
const total = records.filter((rec) => rec.rescored).length
const unreadable = records.filter((rec) => rec.rescored && rec.grade === UNREADABLE).length
const recovered = total - unreadable

let support: Support[] = []
const supportFile = `${base}-support.jsonl`
if (existsSync(supportFile)) {
  support = await readRows<Support>(supportFile)
  for (const row of support) {
    if (row.verdict !== "unparsed") continue
    const verdict = leadingField(row.reason, "verdict")
    if (verdict && SUPPORT_VERDICTS.includes(verdict) && verdict !== "unparsed") {
      row.verdict = verdict
      row.reason = partialReason(row.reason)
      row.rescored = true
    }
  }
  if (support.some((row) => row.rescored)) await writeRows(supportFile, support)
}
const supportRecovered = support.filter((row) => row.rescored).length

let lines = (await readFile(`${base}.md`, "utf8")).split("\n")
const from = lines.indexOf(START)
const to = lines.indexOf(END)
if (from >= 0 && to > from) lines.splice(from, to - from + 2)
const date = new Date().toISOString().slice(0, 10)
const note = [
  START,
  `> **Rescored ${date} with \`harness/rescore.ts\`.** The first version of this report counted ${total} judge replies it could not parse as "did not answer". ${unreadable ? `${recovered} of them` : `All ${recovered}`} gave a readable grade: the JSON was invalid only because of LaTeX backslashes inside it, and the grade was read from the saved text with no new model calls.${unreadable ? ` ${unreadable} had no readable grade and are counted as "judge unreadable".` : ""}${supportRecovered ? ` The same fix recovered ${supportRecovered} citation verdicts.` : ""} The correctness table, citation support and wrong answers below are corrected. The reasons of recovered grades are cut off where the saved text ends, and any doubt they raised about a worked answer was lost. Costs are unchanged.`,
  END,
  "",
]
lines.splice(1, 0, "", ...note.slice(0, -1))
lines = replaceTable(lines, "| model | mode | n | correct", correctnessTable(records))
const supportAt = lines.findIndex((line) => line.startsWith("supported: "))
if (supportAt >= 0) lines[supportAt] = SUPPORT_VERDICTS.map((v) => `${v}: ${support.filter((row) => row.verdict === v).length}`).join(" · ")
const wrongAt = lines.indexOf("## Wrong answers")
if (wrongAt >= 0) {
  let end = wrongAt + 1
  while (end < lines.length && !lines[end].startsWith("## ")) end += 1
  const wrong = records.filter((rec) => rec.grade === "wrong").map((rec) => `- \`${rec.id}\` (${rec.model}, ${rec.mode}): ${rec.gradeReason}`)
  lines.splice(wrongAt, end - wrongAt, "## Wrong answers", "", ...wrong, "")
}
await writeFile(`${base}.md`, lines.join("\n").replace(/\n{3,}/g, "\n\n"))
console.log(`${base}: ${recovered} grades recovered, ${unreadable} unreadable, ${supportRecovered} citation verdicts recovered`)
