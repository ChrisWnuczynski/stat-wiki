// Talking to the Worker: open a session with a Turnstile token, then stream an answer.

import type { Turn } from "./text.ts"

export class AskError extends Error {
  status: number
  constructor(status: number, message: string) {
    super(message)
    this.status = status
  }
}

async function errorFrom(response: Response): Promise<AskError> {
  let message = ""
  try {
    message = String(((await response.json()) as { error?: unknown }).error ?? "")
  } catch {
    // No JSON body.
  }
  return new AskError(response.status, message)
}

export async function openSession(endpoint: string, turnstile: string): Promise<{ session: string; expires: number }> {
  const response = await fetch(`${endpoint}/session`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ turnstile }),
  })
  if (!response.ok) throw await errorFrom(response)
  return (await response.json()) as { session: string; expires: number }
}

export type AskEvent = { event: string; data: Record<string, unknown> }

/** POST /ask and yield the server-sent events as they arrive. */
export async function* askStream(
  endpoint: string,
  body: { turns: Turn[]; page: string; anchor: string; session: string },
  signal?: AbortSignal,
): AsyncGenerator<AskEvent> {
  const response = await fetch(`${endpoint}/ask`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body),
    signal,
  })
  if (!response.ok || !response.body) throw await errorFrom(response)
  const reader = response.body.getReader()
  const decoder = new TextDecoder()
  let buffer = ""
  for (;;) {
    const { done, value } = await reader.read()
    if (done) break
    buffer += decoder.decode(value, { stream: true }).replaceAll("\r\n", "\n")
    let end = buffer.indexOf("\n\n")
    while (end >= 0) {
      const block = buffer.slice(0, end)
      buffer = buffer.slice(end + 2)
      end = buffer.indexOf("\n\n")
      const event = block.split("\n").find((line) => line.startsWith("event:"))?.slice(6).trim() ?? ""
      const raw = block.split("\n").find((line) => line.startsWith("data:"))?.slice(5).trim()
      if (!event || raw === undefined) continue
      try {
        yield { event, data: JSON.parse(raw) as Record<string, unknown> }
      } catch {
        // Skip a malformed event.
      }
    }
  }
}
