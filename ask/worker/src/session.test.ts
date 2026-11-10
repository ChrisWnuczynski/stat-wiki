import assert from "node:assert/strict"
import test from "node:test"

import { hashIp, signSession, verifySession } from "./session.ts"

test("a session token expires and a bad signature is rejected", async () => {
  const token = await signSession("secret", "sid-1", 1_700_000_000)
  assert.deepEqual(await verifySession("secret", token, 1_700_000_000), { sid: "sid-1" })
  assert.equal(await verifySession("secret", token, 1_700_000_001), null)
  assert.equal(await verifySession("other", token, 1_700_000_000), null)
  const [prefix, payload, sig] = token.split(".")
  assert.equal(await verifySession("secret", `${prefix}.${payload}.${sig.slice(0, -1)}x`, 1_700_000_000), null)
})

test("an address hash does not contain the address", async () => {
  const ip = "203.0.113.50"
  const hash = await hashIp("secret", ip)
  assert.equal(hash.includes(ip), false)
  assert.notEqual(await hashIp("secret", ip), await hashIp("secret", "203.0.113.51"))
})
