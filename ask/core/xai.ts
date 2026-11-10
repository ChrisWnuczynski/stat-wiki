import { ANSWER_MAX_TOKENS, XAI_BASE_URL } from "./config.ts"

export type Completion =
  | { called: false }
  | { called: true; text: string; promptTokens: number; completionTokens: number; latencyMs: number }

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

export function deltaFromChunk(data: string): string {
  if (!data || data === "[DONE]") return ""
  try {
    const json = JSON.parse(data) as {
      choices?: { delta?: { content?: unknown }; message?: { content?: unknown } }[]
    }
    const choice = json.choices?.[0]
    return messageText(choice?.delta?.content ?? choice?.message?.content)
  } catch {
    return ""
  }
}

export async function streamChat(input: {
  apiKey: string
  model: string
  system: string
  user: string
  maxTokens?: number
  reasoningEffort?: string
}): Promise<ReadableStream<string>> {
  const apiKey = input.apiKey.trim()
  if (!apiKey) throw Object.assign(new Error("xAI chat failed (0)"), { status: 0 })
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
      stream: true,
      ...(input.reasoningEffort ? { reasoning_effort: input.reasoningEffort } : {}),
      messages: [
        { role: "system", content: input.system },
        { role: "user", content: input.user },
      ],
    }),
  })
  if (!response.ok || !response.body) {
    throw Object.assign(new Error(`xAI chat failed (${response.status})`), { status: response.status })
  }
  const source = response.body
  return new ReadableStream<string>({
    async start(controller) {
      const reader = source.getReader()
      const decoder = new TextDecoder()
      let buffer = ""
      try {
        for (;;) {
          const { done, value } = await reader.read()
          if (done) break
          buffer += decoder.decode(value, { stream: true }).replaceAll("\r\n", "\n")
          let nl = buffer.indexOf("\n")
          while (nl >= 0) {
            const line = buffer.slice(0, nl)
            buffer = buffer.slice(nl + 1)
            if (line.startsWith("data:")) {
              const text = deltaFromChunk(line.slice(5).trim())
              if (text) controller.enqueue(text)
            }
            nl = buffer.indexOf("\n")
          }
        }
        controller.close()
      } catch (error) {
        controller.error(error)
      }
    },
  })
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
    throw Object.assign(new Error(`xAI chat failed (${response.status})`), { status: response.status })
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
