import assert from "node:assert/strict"
import test from "node:test"

import { IP_DAILY_LIMIT, SESSION_DAILY_LIMIT } from "../../core/config.ts"
import { admit, emptyDay, killEnabled, nextDayState } from "./gate.ts"

test("kill and a spent budget stop before any counter moves", () => {
  const counters = { session: 0, ip: 0, global: 3 }
  assert.equal(admit({ counters, kill: true, budget: 10, quotas: true }).ok, false)
  assert.deepEqual(admit({ counters, kill: true, budget: 10, quotas: true }), { ok: false, reason: "kill" })
  const spent = admit({ counters, kill: false, budget: 3, quotas: true })
  assert.deepEqual(spent, { ok: false, reason: "budget" })
  assert.deepEqual(counters, { session: 0, ip: 0, global: 3 })
})

test("a session allows 30 questions and the next one is refused", () => {
  let state = emptyDay()
  for (let i = 0; i < SESSION_DAILY_LIMIT; i++) {
    const step = nextDayState(state, { sessionId: "s", ipHash: "ip", kill: false, budget: 1000, quotas: true })
    assert.equal(step.decision.ok, true)
    state = step.state
  }
  assert.equal(state.sessions.s, 30)
  const blocked = nextDayState(state, { sessionId: "s", ipHash: "ip", kill: false, budget: 1000, quotas: true })
  assert.deepEqual(blocked.decision, { ok: false, reason: "session" })
  assert.equal(blocked.state.sessions.s, 30)
  assert.equal(blocked.state.global, 30)
})

test("an address allows 60 questions and the next one is refused", () => {
  let state = emptyDay()
  for (let i = 0; i < IP_DAILY_LIMIT; i++) {
    const step = nextDayState(state, { sessionId: `s${i}`, ipHash: "ip", kill: false, budget: 1000, quotas: true })
    assert.equal(step.decision.ok, true)
    state = step.state
  }
  const blocked = nextDayState(state, { sessionId: "fresh", ipHash: "ip", kill: false, budget: 1000, quotas: true })
  assert.deepEqual(blocked.decision, { ok: false, reason: "ip" })
  assert.equal(blocked.state.global, IP_DAILY_LIMIT)
  assert.equal(blocked.state.ips.ip, IP_DAILY_LIMIT)
})

test("the dev path still spends the global budget and still obeys the kill switch", () => {
  let state = emptyDay()
  const first = nextDayState(state, { sessionId: "dev", ipHash: "ip", kill: false, budget: 1, quotas: false })
  assert.equal(first.decision.ok, true)
  state = first.state
  assert.equal(state.global, 1)
  assert.equal(state.sessions.dev, undefined)
  const spent = nextDayState(state, { sessionId: "dev", ipHash: "ip", kill: false, budget: 1, quotas: false })
  assert.deepEqual(spent.decision, { ok: false, reason: "budget" })
  const killed = nextDayState(emptyDay(), { sessionId: "dev", ipHash: "ip", kill: true, budget: 10, quotas: false })
  assert.deepEqual(killed.decision, { ok: false, reason: "kill" })
  assert.equal(killed.state.global, 0)
})

test("only an explicit on value enables the kill switch", () => {
  assert.equal(killEnabled(undefined), false)
  assert.equal(killEnabled(""), false)
  assert.equal(killEnabled("0"), false)
  assert.equal(killEnabled("false"), false)
  assert.equal(killEnabled("off"), false)
  assert.equal(killEnabled("1"), true)
  assert.equal(killEnabled("true"), true)
})
