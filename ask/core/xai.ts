import { ANSWER_MAX_TOKENS, JUDGE_MODEL, XAI_BASE_URL } from "./config.ts"

export type Grade = "correct" | "minor error" | "wrong" | "did not answer"

export type Completion =
  | { called: false }
  | { called: true; text: string; promptTokens: number; completionTokens: number; latencyMs: number }

const GRADES = new Set<Grade>(["correct", "minor error", "wrong", "did not answer"])

function key(): string {
  return process.env.XAI_API_KEY?.trim() ?? ""
}

function messageText(content: unknown): string {
  if (typeof content === "string") return content
  if (Array.isArray(content)) {
    return content.map((part) => {
      if (typeof part === "string") return part
      if (part && typeof part === "object" && "text" in part) return String((part as { text: unknown }).text ?? "")
      return ""
    }).join("")
  }
  return ""
}

export async function completeChat(input: { model: string; system: string; user: string; maxTokens?: number }): Promise<Completion> {
  const apiKey = key()
  if (!apiKey) return { called: false }
  const started = Date.now()
  const response = await fetch(`${XAI_BASE_URL}/chat/completions`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: input.model,
      temperature: 0.2,
      max_tokens: input.maxTokens ?? ANSWER_MAX_TOKENS,
      messages: [
        { role: "system", content: input.system },
        { role: "user", content: input.user },
      ],
    }),
  })
  const body = await response.text()
  if (!response.ok) {
    throw new Error(`xAI chat failed (${response.status}): ${body.slice(0, 240)}`)
  }
  const json = JSON.parse(body) as {
    choices?: { message?: { content?: unknown } }[]
    usage?: { prompt_tokens?: number; completion_tokens?: number }
  }
  return {
    called: true,
    text: messageText(json.choices?.[0]?.message?.content),
    promptTokens: json.usage?.prompt_tokens ?? 0,
    completionTokens: json.usage?.completion_tokens ?? 0,
    latencyMs: Date.now() - started,
  }
}

export function parseGrade(text: string): { grade: Grade; reason: string } | null {
  const match = text.match(/\{[\s\S]*\}/)
  if (!match) return null
  try {
    const obj = JSON.parse(match[0]) as { grade?: unknown; reason?: unknown }
    const grade = String(obj.grade ?? "").toLowerCase() as Grade
    if (!GRADES.has(grade)) return null
    return { grade, reason: String(obj.reason ?? "").replace(/\s+/g, " ").trim().slice(0, 300) }
  } catch {
    return null
  }
}

export async function judgeAnswer(input: {
  question: string
  reference: string
  answer: string
  model?: string
}): Promise<{ called: false } | { called: true; grade: Grade; reason: string }> {
  const completion = await completeChat({
    model: input.model ?? JUDGE_MODEL,
    maxTokens: 200,
    system: "Grade the answer against the reference. Reply with one JSON object and nothing else: {\"grade\":\"correct\"|\"minor error\"|\"wrong\"|\"did not answer\",\"reason\":\"one line\"}.",
    user: `Question:\n${input.question}\n\nReference:\n${input.reference}\n\nAnswer:\n${input.answer}`,
  })
  if (!completion.called) return { called: false }
  const parsed = parseGrade(completion.text)
  if (!parsed) return { called: true, grade: "did not answer", reason: "judge output was not a grade" }
  return { called: true, ...parsed }
}

export function looksDeclined(answer: string): boolean {
  const text = answer.trim()
  if (!text) return true
  const lower = text.toLowerCase()
  const phrases = [
    "not about statistics",
    "not a statistics",
    "only help with statistics",
    "only answer questions about statistics",
    "i can't help with that",
    "i cannot help with that",
    "i can only help with",
    "outside what i can help",
    "i won't help",
    "i will not help",
  ]
  if (!phrases.some((phrase) => lower.includes(phrase))) return false
  const sentences = text.split(/(?<=[.!?])\s+/).filter(Boolean)
  return sentences.length <= 2 || !/\[[1-9]/.test(text)
}
