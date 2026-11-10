import { nextDayState, type DayState } from "./gate.ts"

type Storage = {
  get<T>(key: string): Promise<T | undefined>
  put(key: string, value: unknown): Promise<void>
  delete(key: string): Promise<boolean>
  list(options: { prefix: string }): Promise<Map<string, unknown>>
}

export class AskBudget {
  private ctx: { storage: Storage }

  constructor(ctx: { storage: Storage }, _env: unknown) {
    this.ctx = ctx
  }

  async fetch(request: Request): Promise<Response> {
    let body: {
      sessionId?: unknown
      ipHash?: unknown
      day?: unknown
      kill?: unknown
      budget?: unknown
      quotas?: unknown
    }
    try {
      body = await request.json() as typeof body
    } catch {
      return Response.json({ ok: false, reason: "budget" }, { status: 400 })
    }
    const day = typeof body.day === "string" && /^\d{4}-\d{2}-\d{2}$/.test(body.day) ? body.day : ""
    const sessionId = typeof body.sessionId === "string" ? body.sessionId.slice(0, 80) : ""
    const ipHash = typeof body.ipHash === "string" ? body.ipHash.slice(0, 80) : ""
    if (!day || !sessionId || !ipHash) return Response.json({ ok: false, reason: "budget" }, { status: 400 })
    const key = `day:${day}`
    const current = await this.ctx.storage.get<DayState>(key) ?? { global: 0, sessions: {}, ips: {} }
    const budget = typeof body.budget === "number" && Number.isFinite(body.budget) ? body.budget : 0
    const { state, decision } = nextDayState(current, {
      sessionId,
      ipHash,
      kill: body.kill === true,
      budget,
      quotas: body.quotas === true,
    })
    if (decision.ok) {
      await this.ctx.storage.put(key, state)
      const listed = await this.ctx.storage.list({ prefix: "day:" })
      for (const old of listed.keys()) {
        if (old !== key) await this.ctx.storage.delete(old)
      }
    }
    return Response.json(decision.ok ? { ok: true } : { ok: false, reason: decision.reason })
  }
}
