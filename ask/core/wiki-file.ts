import { readFile } from "node:fs/promises"

import type { WikiDoc } from "./types.ts"

export async function loadWiki(source: string): Promise<WikiDoc> {
  if (source.startsWith("http://") || source.startsWith("https://")) {
    const response = await fetch(source)
    if (!response.ok) throw new Error(`failed to fetch wiki (${response.status})`)
    return response.json() as Promise<WikiDoc>
  }
  return JSON.parse(await readFile(source, "utf8")) as WikiDoc
}
