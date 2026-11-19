import assert from "node:assert/strict"
import test from "node:test"

import { Cloudflare } from "./cloudflare.ts"
import { VECTORIZE_INDEX } from "./config.ts"

type CloudflareCtor = new (account: string, token: string, namespaceId: string) => Cloudflare

function client(): Cloudflare {
  return new (Cloudflare as unknown as CloudflareCtor)("account", "token", "namespace")
}

function ids(count: number): string[] {
  return Array.from({ length: count }, (_, index) => `id-${index}`)
}

function ok(): Response {
  return new Response(JSON.stringify({ success: true, result: { mutationId: "m" } }), {
    status: 200,
    headers: { "content-type": "application/json" },
  })
}

async function withFetch(fetchImpl: typeof fetch, run: () => Promise<void>): Promise<void> {
  const previous = globalThis.fetch
  globalThis.fetch = fetchImpl
  try {
    await run()
  } finally {
    globalThis.fetch = previous
  }
}

test("deleteVectors sends ids in sequential requests of at most 100", async () => {
  const cases = [
    { count: 0, sizes: [] as number[] },
    { count: 100, sizes: [100] },
    { count: 101, sizes: [100, 1] },
    { count: 172, sizes: [100, 72] },
    { count: 250, sizes: [100, 100, 50] },
  ]
  for (const item of cases) {
    const batches: string[][] = []
    let active = 0
    let maxActive = 0
    await withFetch(async (input, init) => {
      active += 1
      maxActive = Math.max(maxActive, active)
      assert.equal(init?.method, "POST")
      assert.equal(
        String(input),
        `https://api.cloudflare.com/client/v4/accounts/account/vectorize/v2/indexes/${VECTORIZE_INDEX}/delete_by_ids`,
      )
      const body = JSON.parse(String(init?.body)) as { ids: string[] }
      assert.ok(body.ids.length <= 100)
      batches.push(body.ids)
      await new Promise((resolve) => setTimeout(resolve, 5))
      active -= 1
      return ok()
    }, async () => {
      await client().deleteVectors(ids(item.count))
    })
    assert.deepEqual(batches.map((batch) => batch.length), item.sizes)
    assert.deepEqual(batches.flat(), ids(item.count))
    assert.equal(maxActive, item.count === 0 ? 0 : 1)
  }
})
