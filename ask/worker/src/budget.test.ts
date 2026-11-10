import assert from "node:assert/strict"
import test from "node:test"

import { SESSION_DAILY_LIMIT } from "../../core/config.ts"
import { AskBudget } from "./budget.ts"

class MemoryStorage {
  map = new Map<string, unknown>()
  async get<T>(key: string): Promise<T | undefined> {
    return this.map.get(key) as T | undefined
  }
  async put(key: string, value: unknown): Promise<void> {
    this.map.set(key, value)
  }
  async delete(key: string): Promise<boolean> {
    return this.map.delete(key)
  }
  async list(options: { prefix: string }): Promise<Map<string, unknown>> {
    const out = new Map<string, unknown>()
    for (const [key, value] of this.map) if (key.startsWith(options.prefix)) out.set(key, value)
    return out
  }
}

function request(body: unknown): Request {
  return new Request("https://budget.internal/admit", {
    method: "POST",
    body: JSON.stringify(body),
  })
}

test("the durable object stores the daily budget and drops the previous day", async () => {
  const storage = new MemoryStorage()
  storage.map.set("day:2026-11-09", { global: 9, sessions: {}, ips: {} })
  const budget = new AskBudget({ storage }, {})
  const first = await budget.fetch(request({
    sessionId: "s",
    ipHash: "ip",
    day: "2026-11-10",
    kill: false,
    budget: 2,
    quotas: true,
  }))
  assert.equal((await first.json() as { ok: boolean }).ok, true)
  assert.equal(storage.map.has("day:2026-11-09"), false)
  const second = await budget.fetch(request({
    sessionId: "s",
    ipHash: "ip",
    day: "2026-11-10",
    kill: true,
    budget: 2,
    quotas: true,
  }))
  assert.deepEqual(await second.json(), { ok: false, reason: "kill" })
  const stored = storage.map.get("day:2026-11-10") as { global: number }
  assert.equal(stored.global, 1)
})

test("the durable object enforces the session cap", async () => {
  const storage = new MemoryStorage()
  const budget = new AskBudget({ storage }, {})
  for (let i = 0; i < SESSION_DAILY_LIMIT; i++) {
    const response = await budget.fetch(request({
      sessionId: "s",
      ipHash: "ip",
      day: "2026-11-10",
      kill: false,
      budget: 1000,
      quotas: true,
    }))
    assert.equal((await response.json() as { ok: boolean }).ok, true)
  }
  const blocked = await budget.fetch(request({
    sessionId: "s",
    ipHash: "ip",
    day: "2026-11-10",
    kill: false,
    budget: 1000,
    quotas: true,
  }))
  assert.deepEqual(await blocked.json(), { ok: false, reason: "session" })
})
