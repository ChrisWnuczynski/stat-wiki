import {
  EMBEDDING_DIMENSIONS,
  EMBEDDING_METRIC,
  EMBEDDING_MODEL,
  KV_TITLE,
  QUERY_INSTRUCTION,
  VECTORIZE_INDEX,
} from "./config.ts"

export type VectorMatch = {
  id: string
  score: number
  metadata: Record<string, unknown>
}

type CfJson = {
  success?: boolean
  errors?: unknown
  result?: unknown
}

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

export class Cloudflare {
  private readonly account: string
  private readonly token: string
  private namespaceId: string

  private constructor(account: string, token: string, namespaceId: string) {
    this.account = account
    this.token = token
    this.namespaceId = namespaceId
  }

  static async connect(): Promise<Cloudflare> {
    const account = process.env.CLOUDFLARE_ACCOUNT_ID?.trim() ?? ""
    const token = process.env.CLOUDFLARE_API_TOKEN?.trim() ?? ""
    if (!account) throw new Error("CLOUDFLARE_ACCOUNT_ID is missing")
    if (!token) throw new Error("CLOUDFLARE_API_TOKEN is missing")
    const client = new Cloudflare(account, token, "")
    await client.ensureIndex()
    client.namespaceId = await client.ensureNamespace()
    return client
  }

  private async call(method: string, path: string, body?: unknown, attempt = 0): Promise<CfJson> {
    const url = `https://api.cloudflare.com/client/v4/accounts/${this.account}${path}`
    try {
      const response = await fetch(url, {
        method,
        headers: {
          Authorization: `Bearer ${this.token}`,
          ...(body !== undefined ? { "Content-Type": "application/json" } : {}),
        },
        body: body !== undefined ? JSON.stringify(body) : undefined,
      })
      const raw = await response.text()
      let json: CfJson = {}
      try {
        json = raw ? JSON.parse(raw) as CfJson : {}
      } catch {
        json = {}
      }
      if (response.status === 429 || response.status >= 500) {
        if (attempt >= 8) throw new Error(`Cloudflare ${method} failed (${response.status})`)
        const retryAfter = Number(response.headers.get("retry-after"))
        const wait = Math.min(30000, Number.isFinite(retryAfter) && retryAfter > 0 ? retryAfter * 1000 : 1000 * 2 ** attempt)
        await sleep(wait)
        return this.call(method, path, body, attempt + 1)
      }
      if (!response.ok || json.success === false) {
        const detail = JSON.stringify(json.errors ?? raw.slice(0, 240)).slice(0, 300)
        throw new Error(`Cloudflare ${method} failed (${response.status}): ${detail}`)
      }
      return json
    } catch (error) {
      if (error instanceof Error && error.message.startsWith("Cloudflare ")) throw error
      if (attempt >= 8) throw error
      await sleep(1000 * 2 ** attempt)
      return this.call(method, path, body, attempt + 1)
    }
  }

  private async ensureIndex(): Promise<void> {
    const listed = await this.call("GET", "/vectorize/v2/indexes")
    const indexes = Array.isArray(listed.result) ? listed.result as { name?: string; config?: { dimensions?: number; metric?: string } }[] : []
    const existing = indexes.find((index) => index.name === VECTORIZE_INDEX)
    if (!existing) {
      await this.call("POST", "/vectorize/v2/indexes", {
        name: VECTORIZE_INDEX,
        description: "StatWiki ask passage index",
        config: { dimensions: EMBEDDING_DIMENSIONS, metric: EMBEDDING_METRIC },
      })
      return
    }
    const dimensions = existing.config?.dimensions
    const metric = existing.config?.metric
    if (dimensions !== EMBEDDING_DIMENSIONS || metric !== EMBEDDING_METRIC) {
      throw new Error(`index ${VECTORIZE_INDEX} is ${dimensions} ${metric}, expected ${EMBEDDING_DIMENSIONS} ${EMBEDDING_METRIC}`)
    }
  }

  private async ensureNamespace(): Promise<string> {
    const listed = await this.call("GET", "/storage/kv/namespaces")
    const namespaces = Array.isArray(listed.result) ? listed.result as { id?: string; title?: string }[] : []
    const existing = namespaces.find((namespace) => namespace.title === KV_TITLE)
    if (existing?.id) return existing.id
    const created = await this.call("POST", "/storage/kv/namespaces", { title: KV_TITLE })
    const id = (created.result as { id?: string } | undefined)?.id
    if (!id) throw new Error("KV namespace was created without an id")
    return id
  }

  async embedDocuments(texts: string[]): Promise<number[][]> {
    if (texts.length === 0) return []
    return this.embed({ documents: texts })
  }

  async embedQuery(text: string): Promise<number[]> {
    const vectors = await this.embed({ queries: [text], instruction: QUERY_INSTRUCTION })
    const vector = vectors[0]
    if (!vector) throw new Error("query embedding was empty")
    return vector
  }

  private async embed(body: unknown): Promise<number[][]> {
    const json = await this.call("POST", `/ai/run/${EMBEDDING_MODEL}`, body)
    const result = json.result as { data?: unknown; shape?: unknown } | undefined
    const data = result?.data
    const shape = result?.shape
    if (!Array.isArray(data) || !Array.isArray(shape) || data.length === 0 || !Array.isArray(data[0])) {
      throw new Error("unexpected embedding response")
    }
    if (shape[1] !== EMBEDDING_DIMENSIONS) throw new Error(`embedding dimensions ${String(shape[1])}`)
    return data as number[][]
  }

  async upsert(vectors: { id: string; values: number[]; metadata: Record<string, string | number> }[]): Promise<void> {
    if (vectors.length === 0) return
    for (const vector of vectors) {
      if ("text" in vector.metadata) throw new Error("refusing to store chunk text in vector metadata")
      for (const value of Object.values(vector.metadata)) {
        if (typeof value === "string" && value.length > 4000) {
          throw new Error("refusing to store a long metadata string")
        }
      }
    }
    await this.call("POST", `/vectorize/v2/indexes/${VECTORIZE_INDEX}/upsert`, { vectors })
  }

  async deleteVectors(ids: string[]): Promise<void> {
    for (let i = 0; i < ids.length; i += 1000) {
      const slice = ids.slice(i, i + 1000)
      if (slice.length === 0) continue
      await this.call("POST", `/vectorize/v2/indexes/${VECTORIZE_INDEX}/delete_by_ids`, { ids: slice })
    }
  }

  async query(vector: number[], topK: number): Promise<VectorMatch[]> {
    const json = await this.call("POST", `/vectorize/v2/indexes/${VECTORIZE_INDEX}/query`, {
      vector,
      topK,
      returnMetadata: "all",
    })
    const result = json.result as { matches?: VectorMatch[] } | undefined
    const matches = result?.matches ?? []
    return matches.map((match) => ({
      id: String(match.id),
      score: Number(match.score),
      metadata: match.metadata ?? {},
    }))
  }

  async vectorCount(): Promise<number> {
    const json = await this.call("GET", `/vectorize/v2/indexes/${VECTORIZE_INDEX}/info`)
    const result = json.result as { vectorCount?: number } | undefined
    return Number(result?.vectorCount ?? 0)
  }

  async kvPut(pairs: { key: string; value: string }[]): Promise<void> {
    for (let i = 0; i < pairs.length; i += 100) {
      const slice = pairs.slice(i, i + 100)
      if (slice.length === 0) continue
      await this.call("PUT", `/storage/kv/namespaces/${this.namespaceId}/bulk`, slice)
    }
  }

  async kvGetMany(keys: string[]): Promise<Map<string, string | null>> {
    const out = new Map<string, string | null>()
    for (let i = 0; i < keys.length; i += 100) {
      const slice = keys.slice(i, i + 100)
      if (slice.length === 0) continue
      const json = await this.call("POST", `/storage/kv/namespaces/${this.namespaceId}/bulk/get`, {
        keys: slice,
        type: "text",
      })
      const values = (json.result as { values?: Record<string, string | null> } | undefined)?.values ?? {}
      for (const key of slice) out.set(key, values[key] ?? null)
    }
    return out
  }

  async kvDelete(keys: string[]): Promise<void> {
    for (let i = 0; i < keys.length; i += 100) {
      const slice = keys.slice(i, i + 100)
      if (slice.length === 0) continue
      await this.call("POST", `/storage/kv/namespaces/${this.namespaceId}/bulk/delete`, slice)
    }
  }
}

export async function embedDocumentsResilient(client: Cloudflare, texts: string[]): Promise<number[][]> {
  if (texts.length === 0) return []
  try {
    const vectors = await client.embedDocuments(texts)
    if (vectors.length !== texts.length) throw new Error("embedding count did not match the batch")
    return vectors
  } catch (error) {
    if (texts.length === 1) throw error
    const mid = Math.ceil(texts.length / 2)
    const left = await embedDocumentsResilient(client, texts.slice(0, mid))
    const right = await embedDocumentsResilient(client, texts.slice(mid))
    return left.concat(right)
  }
}
