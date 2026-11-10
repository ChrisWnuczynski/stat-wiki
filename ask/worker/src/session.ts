export async function sameSecret(a: string, b: string): Promise<boolean> {
  if (!a || !b) return false
  const enc = new TextEncoder()
  const [left, right] = await Promise.all([
    crypto.subtle.digest("SHA-256", enc.encode(a)),
    crypto.subtle.digest("SHA-256", enc.encode(b)),
  ])
  const x = new Uint8Array(left)
  const y = new Uint8Array(right)
  let diff = a.length === b.length ? 0 : 1
  for (let i = 0; i < x.length; i++) diff |= x[i] ^ y[i]
  return diff === 0
}

function bytesToB64url(bytes: Uint8Array): string {
  let bin = ""
  for (const byte of bytes) bin += String.fromCharCode(byte)
  return btoa(bin).replaceAll("+", "-").replaceAll("/", "_").replaceAll("=", "")
}

function b64urlToString(text: string): string | null {
  const pad = text.length % 4 === 0 ? "" : "=".repeat(4 - (text.length % 4))
  try {
    return atob(text.replaceAll("-", "+").replaceAll("_", "/") + pad)
  } catch {
    return null
  }
}

async function hmac(secret: string, payload: string): Promise<string> {
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  )
  const sig = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(payload))
  return bytesToB64url(new Uint8Array(sig))
}

export async function hashIp(secret: string, ip: string): Promise<string> {
  return hmac(secret, `ip:${ip}`)
}

export function newSessionId(): string {
  const bytes = new Uint8Array(16)
  crypto.getRandomValues(bytes)
  return [...bytes].map((byte) => byte.toString(16).padStart(2, "0")).join("")
}

export async function signSession(secret: string, sid: string, exp: number): Promise<string> {
  const payload = bytesToB64url(new TextEncoder().encode(JSON.stringify({ v: 1, sid, exp })))
  const sig = await hmac(secret, payload)
  return `v1.${payload}.${sig}`
}

export async function verifySession(secret: string, token: string, nowSec: number): Promise<{ sid: string } | null> {
  const parts = token.split(".")
  if (parts.length !== 3 || parts[0] !== "v1" || !parts[1] || !parts[2]) return null
  const expected = await hmac(secret, parts[1])
  if (!(await sameSecret(expected, parts[2]))) return null
  const raw = b64urlToString(parts[1])
  if (!raw) return null
  try {
    const parsed = JSON.parse(raw) as { v?: unknown; sid?: unknown; exp?: unknown }
    if (parsed.v !== 1 || typeof parsed.sid !== "string" || !parsed.sid) return null
    if (typeof parsed.exp !== "number" || parsed.exp < nowSec) return null
    return { sid: parsed.sid }
  } catch {
    return null
  }
}
