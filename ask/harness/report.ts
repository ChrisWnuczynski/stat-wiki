import { mkdir, writeFile } from "node:fs/promises"
import { resolve } from "node:path"

import {
  CHUNK_CHARS,
  DEFINES_BOOST,
  EMBEDDING_DIMENSIONS,
  EMBEDDING_MODEL,
  PAGE_BOOST,
  QUERY_INSTRUCTION,
  SECTION_BOOST,
  TITLE_BOOST,
  TOKEN_BUDGET,
} from "../core/config.ts"
import { OVERLAP_RULE, type OverlapHit } from "../core/overlap.ts"
import { PROMPT_VERSION } from "../core/prompt.ts"
import { mean, percentile } from "../core/text.ts"

export type ScoreRow = {
  set: string
  split: string
  mode: string
  config: string
  questionId: string
  covered: boolean
  best: number
  chapterHit: string
  expectedHit: string
  passages: number
  tokens: number
  latencyMs: number
  answer: string
  entries: string
}

export type IndexPass = {
  at: string
  embedded: number
  deleted: number
  unchanged: number
  chunks: number
  maxBody?: number
  bodiesOverLimit?: number
  vectorCount: number
  wikiSha256: string
  model: string
}

type Summary = {
  n: number
  chapterHit: string
  expectedHit: string
  covered: string
  passages: string
  tokens: string
}

function pct(values: number[]): string {
  if (values.length === 0) return "n/a"
  return `${(100 * values.reduce((sum, value) => sum + value, 0) / values.length).toFixed(1)}%`
}

function num(value: number): string {
  return value.toFixed(1)
}

export function summarize(rows: ScoreRow[]): Summary {
  const chapter = rows.filter((row) => row.chapterHit === "0" || row.chapterHit === "1")
  const expected = rows.filter((row) => row.expectedHit === "0" || row.expectedHit === "1")
  return {
    n: rows.length,
    chapterHit: pct(chapter.map((row) => Number(row.chapterHit))),
    expectedHit: pct(expected.map((row) => Number(row.expectedHit))),
    covered: pct(rows.map((row) => row.covered ? 1 : 0)),
    passages: num(mean(rows.map((row) => row.passages))),
    tokens: num(mean(rows.map((row) => row.tokens))),
  }
}

function csvField(value: string | number | boolean): string {
  const text = String(value)
  if (/[",\n]/.test(text)) return `"${text.replaceAll("\"", "\"\"")}"`
  return text
}

function csv(rows: ScoreRow[]): string {
  const header = "set,split,mode,config,question_id,covered,best_similarity,chapter_hit,expected_hit,n_passages,passage_tokens,latency_ms,answer,retrieved_entries"
  const lines = rows.map((row) => [
    row.set,
    row.split,
    row.mode,
    row.config,
    row.questionId,
    row.covered,
    row.best.toFixed(4),
    row.chapterHit,
    row.expectedHit,
    row.passages,
    row.tokens,
    row.latencyMs,
    row.answer,
    row.entries,
  ].map(csvField).join(","))
  return `${header}\n${lines.join("\n")}\n`
}

function table(headers: string[], rows: string[][]): string {
  const head = `| ${headers.join(" | ")} |`
  const rule = `| ${headers.map(() => "---").join(" | ")} |`
  const body = rows.map((row) => `| ${row.join(" | ")} |`)
  return [head, rule, ...body].join("\n")
}

function latencyLine(values: number[]): string {
  if (values.length === 0) return "n/a"
  return `p50 ${Math.round(percentile(values, 50))} ms, p95 ${Math.round(percentile(values, 95))} ms (n=${values.length})`
}

export async function writeRunFiles(dir: string, date: string, input: {
  rows: ScoreRow[]
  configs: { name: string; pageBoost: number; k: number }[]
  overlaps: OverlapHit[]
  threshold: number
  devCovered: number
  misuseBelow: number
  definesFrom: Record<string, number>
  definesTo: Record<string, number>
  wikiVersion: number
  wikiSha: string
  entries: number
  textEntries: number
  questions: number
  answers: number
  chunks: number
  passes: IndexPass[]
  answerModel: string
  compareModel: string
  xaiCalled: boolean
  devSize: number
  heldoutSize: number
  closedShort: number
}): Promise<string> {
  await mkdir(dir, { recursive: true })
  const configNames = input.configs.map((config) => config.name)
  for (const config of input.configs) {
    const rows = input.rows.filter((row) => row.config === config.name)
    await writeFile(resolve(dir, `${date}-${config.name}.csv`), csv(rows))
    const lines = [
      `# ${date} ${config.name}`,
      "",
      `Prompt ${PROMPT_VERSION}. Embedding ${EMBEDDING_MODEL}. Answer model ${input.answerModel} (${input.xaiCalled ? "called" : "not called"}).`,
      `k=${config.k}, page boost ${config.pageBoost}, section boost ${SECTION_BOOST}, title boost ${TITLE_BOOST}, defines boost ${DEFINES_BOOST}, chunk body ${CHUNK_CHARS}, token budget ${TOKEN_BUDGET}, threshold ${input.threshold.toFixed(3)}.`,
      "",
      table(
        ["set", "split", "mode", "n", "chapter hit", "expected hit", "covered", "passages", "tokens"],
        ["dev", "heldout", "student", "misuse"].flatMap((split) =>
          ["open", "closed"].map((mode) => {
            const subset = rows.filter((row) => row.split === split && row.mode === mode)
            if (subset.length === 0) return null
            const summary = summarize(subset)
            return [subset[0].set, split, mode, String(summary.n), summary.chapterHit, summary.expectedHit, summary.covered, summary.passages, summary.tokens]
          }),
        ).filter((row): row is string[] => row !== null),
      ),
      "",
      "Closed-book chapter hit is the main bank score. Answers were not graded by a judge in this run when the model was not called.",
      "",
    ]
    await writeFile(resolve(dir, `${date}-${config.name}.md`), lines.join("\n"))
  }

  const overlapBody = input.overlaps.length === 0
    ? "None."
    : input.overlaps.map((hit) => `- ${hit.answerId} → ${hit.entryId} (${hit.kind}): ${hit.title}`).join("\n")
  const passLines = input.passes.length === 0
    ? "No index log was found."
    : input.passes.map((pass) => `- ${pass.at}: embedded ${pass.embedded}, deleted ${pass.deleted}, unchanged ${pass.unchanged}, chunks ${pass.chunks}, vector count ${pass.vectorCount}`).join("\n")

  const comparisonRows = configNames.flatMap((name) =>
    ["dev", "heldout"].flatMap((split) =>
      ["closed", "open"].map((mode) => {
        const subset = input.rows.filter((row) => row.config === name && row.split === split && row.mode === mode && row.set === "bank")
        if (subset.length === 0) return null
        const summary = summarize(subset)
        return [name, split, mode, String(summary.n), summary.chapterHit, summary.covered, summary.passages]
      }),
    ),
  ).filter((row): row is string[] => row !== null)

  const studentRows = configNames.map((name) => {
    const subset = input.rows.filter((row) => row.config === name && row.set === "student" && row.mode === "open")
    const summary = summarize(subset)
    return [name, String(summary.n), summary.expectedHit, summary.covered]
  }).filter((row) => row[1] !== "0")

  const devLatency = input.rows.filter((row) => row.set === "bank" && row.split === "dev" && row.mode === "open" && row.config === configNames[0]).map((row) => row.latencyMs)
  const heldLatency = input.rows.filter((row) => row.set === "bank" && row.split === "heldout" && row.mode === "open" && row.config === configNames[0]).map((row) => row.latencyMs)
  const misuseScores = input.rows.filter((row) => row.set === "misuse" && row.config === configNames[0]).map((row) => row.best)
  const misuseCovered = input.rows.filter((row) => row.set === "misuse" && row.config === configNames[0] && row.covered).length

  const baseline = [
    `# Ask harness baseline ${date}`,
    "",
    "Phase 1 index and harness. No worker and no widget.",
    "",
    "## Setup",
    "",
    `- Wiki version ${input.wikiVersion}, sha256 \`${input.wikiSha}\`, ${input.entries} entries, ${input.textEntries} with text, ${input.questions} questions, ${input.answers} worked answers.`,
    `- Chunks: ${input.chunks}. Body limit ${CHUNK_CHARS} characters. The header is repeated on every part and is not counted in that limit. Bodies kept whole past that limit: ${input.passes.at(-1)?.bodiesOverLimit ?? "n/a"}. Longest body: ${input.passes.at(-1)?.maxBody ?? "n/a"} characters.`,
    `- Embeddings: ${EMBEDDING_MODEL}, ${EMBEDDING_DIMENSIONS} dimensions, cosine. Passages are embedded as documents. Questions use the query input with instruction: "${QUERY_INSTRUCTION}".`,
    "- Chunk text is stored in KV under the chunk id. Vector metadata has ids, title, url, kind, and chapter only.",
    "- Vector ids are a 32-character sha256 prefix because ids are limited to 64 bytes. The logical chunk id remains `<entry id>#<part>`.",
    `- Prompt ${PROMPT_VERSION}. Answer model ${input.answerModel}. Comparison model ${input.compareModel}.`,
    input.xaiCalled
      ? "- The answer model was called."
      : "- XAI_API_KEY is unset. Answers are marked not called. The judge was skipped. The owner will hand-grade 40 later.",
    `- Split seed 1729. Dev ${input.devSize}. Held out ${input.heldoutSize}. Held out was scored once, after the threshold was frozen.`,
    `- Threshold ${input.threshold.toFixed(3)}. It was calibrated on closed-book dev similarities against the misuse set, so a question matching its own entry does not set the bar. Closed-book dev coverage at this threshold: ${(100 * input.devCovered).toFixed(1)}%. Misuse prompts below it: ${(100 * input.misuseBelow).toFixed(1)}%. The choice maximises that pair and keeps at least 90% of those dev questions covered when any threshold does.`,
    `- Boosts: page ${PAGE_BOOST} (toggled), section ${SECTION_BOOST}, exact title ${TITLE_BOOST}, defines-term ${DEFINES_BOOST}. Candidate pool ${20}, token budget ${TOKEN_BUDGET}.`,
    `- Defines edges in this file run from ${Object.entries(input.definesFrom).map(([kind, count]) => `${kind} (${count})`).join(", ") || "nowhere"} to ${Object.entries(input.definesTo).map(([kind, count]) => `${kind} (${count})`).join(", ") || "nowhere"}. The file does not point a term at a box. A defines-term match boosts the target entry, the \`to\` side.`,
    "- Bank context: the current page is the question page, and the current section is the chapter on the question's `on` edge. Student context: the current page is the chapter page, so a section on that page can receive the page boost, and the expected entry's chapter receives the section boost.",
    `- Closed retrieval drops the question, its worked answer, and overlapping entries from the top 50, then keeps 20. Questions with fewer than 20 closed candidates: ${input.closedShort}.`,
    "",
    "## Index passes",
    "",
    passLines,
    "",
    "## Defines direction",
    "",
    "Checked on the live file before using the edges. Every `defines` edge found here starts at a chapter and ends at the defined entry (a definition, section, theorem, article, proposition, or remark). Retrieval uses that direction.",
    "",
    "## Overlap list",
    "",
    OVERLAP_RULE,
    "",
    `${input.overlaps.length} overlapping entries.`,
    "",
    overlapBody,
    "",
    "## Bank retrieval",
    "",
    "Chapter hit means a kept passage is from the question's chapter. Closed is the main score.",
    "",
    table(["config", "split", "mode", "n", "chapter hit", "covered", "passages"], comparisonRows),
    "",
    `Dev retrieval latency ${latencyLine(devLatency)}.`,
    `Held-out retrieval latency ${latencyLine(heldLatency)}.`,
    "Answer tokens and answer latency were not measured because the model was not called.",
    "",
    "## Student questions",
    "",
    "Expected hit means a kept passage comes from a listed entry. These questions do not reuse content words from those titles.",
    "",
    studentRows.length === 0 ? "None in this run." : table(["config", "n", "expected hit", "covered"], studentRows),
    "",
    "## Misuse",
    "",
    misuseScores.length === 0
      ? "None in this run."
      : `Best similarity min ${Math.min(...misuseScores).toFixed(3)}, median ${percentile(misuseScores, 50).toFixed(3)}, max ${Math.max(...misuseScores).toFixed(3)}. Treated as covered: ${misuseCovered} of ${misuseScores.length}. ${input.xaiCalled ? "Decline labels come from the answer text." : "Decline rate was not scored because the model was not called. Student questions were not checked for wrong declines for the same reason."}`,
    "",
    "## Not scored",
    "",
    "- Correctness: judge skipped. Hand-grading of 40 is left to the owner.",
    "- Citations: not scored. The mapper is in place and drops numbers outside 1..k, and collapses chunks from one entry.",
    "- Maths: not scored. The checker renders spans with katex and throwOnError.",
    "",
  ].join("\n")

  const baselinePath = resolve(dir, `${date}-baseline.md`)
  await writeFile(baselinePath, baseline)
  await writeFile(resolve(dir, `${date}-overlaps.json`), JSON.stringify({
    rule: OVERLAP_RULE,
    count: input.overlaps.length,
    overlaps: input.overlaps,
  }, null, 2))
  return baselinePath
}
