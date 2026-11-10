export type WikiEntry = {
  id: string
  kind: string
  title: string
  text?: string
  url: string
  fingerprint: string
  copy_of?: string
}

export type WikiEdge = {
  from: string
  type: string
  to: string
}

export type WikiDoc = {
  version: number
  aliases?: Record<string, string>
  entries: WikiEntry[]
  edges: WikiEdge[]
}

export type Chunk = {
  id: string
  entryId: string
  part: number
  text: string
  url: string
  title: string
  kind: string
  chapterId: string | null
  chapterTitle: string | null
  fingerprint: string
}

export type Candidate = {
  chunkId: string
  entryId: string
  score: number
  title: string
  kind: string
  chapterId: string
  url: string
  part: number
}

export type Passage = {
  n: number
  chunkId: string
  entryId: string
  url: string
  text: string
  tokens: number
}

export type Citation = {
  entryId: string
  url: string
  numbers: number[]
}
