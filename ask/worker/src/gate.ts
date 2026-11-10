import { IP_DAILY_LIMIT, SESSION_DAILY_LIMIT } from "../../core/config.ts"

export type AdmitReason = "kill" | "budget" | "session" | "ip"

export type AdmitDecision =
  | { ok: true; next: { session: number; ip: number; global: number } }
  | { ok: false; reason: AdmitReason }

export type DayState = {
  global: number
  sessions: Record<string, number>
  ips: Record<string, number>
}

export function emptyDay(): DayState {
  return { global: 0, sessions: {}, ips: {} }
}

export function killEnabled(value: string | undefined): boolean {
  const text = (value ?? "").trim().toLowerCase()
  if (!text) return false
  return text !== "0" && text !== "false" && text !== "no" && text !== "off"
}

export function admit(input: {
  counters: { session: number; ip: number; global: number }
  kill: boolean
  budget: number
  quotas: boolean
  sessionLimit?: number
  ipLimit?: number
}): AdmitDecision {
  const sessionLimit = input.sessionLimit ?? SESSION_DAILY_LIMIT
  const ipLimit = input.ipLimit ?? IP_DAILY_LIMIT
  if (input.kill) return { ok: false, reason: "kill" }
  if (!Number.isFinite(input.budget) || input.counters.global >= input.budget) return { ok: false, reason: "budget" }
  if (input.quotas && input.counters.session >= sessionLimit) return { ok: false, reason: "session" }
  if (input.quotas && input.counters.ip >= ipLimit) return { ok: false, reason: "ip" }
  return {
    ok: true,
    next: {
      global: input.counters.global + 1,
      session: input.quotas ? input.counters.session + 1 : input.counters.session,
      ip: input.quotas ? input.counters.ip + 1 : input.counters.ip,
    },
  }
}

export function nextDayState(state: DayState, input: {
  sessionId: string
  ipHash: string
  kill: boolean
  budget: number
  quotas: boolean
}): { state: DayState; decision: AdmitDecision } {
  const decision = admit({
    counters: {
      global: state.global,
      session: state.sessions[input.sessionId] ?? 0,
      ip: state.ips[input.ipHash] ?? 0,
    },
    kill: input.kill,
    budget: input.budget,
    quotas: input.quotas,
  })
  if (!decision.ok) return { state, decision }
  const next: DayState = {
    global: decision.next.global,
    sessions: { ...state.sessions },
    ips: { ...state.ips },
  }
  if (input.quotas) {
    next.sessions[input.sessionId] = decision.next.session
    next.ips[input.ipHash] = decision.next.ip
  }
  return { state: next, decision }
}
