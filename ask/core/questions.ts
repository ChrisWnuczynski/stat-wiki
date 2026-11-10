import { readFile } from "node:fs/promises"

import type { WikiDoc } from "./types.ts"
import { titleLeaks } from "./text.ts"

export type StudentQuestion = {
  id: string
  question: string
  expect: string[]
  page?: string
  chapterId?: string
}

export type MisusePrompt = {
  id: string
  category: string
  prompt: string
}

export async function readJsonl<T>(path: string): Promise<T[]> {
  const text = await readFile(path, "utf8")
  return text.split("\n").map((line) => line.trim()).filter(Boolean).map((line) => JSON.parse(line) as T)
}

export function studentLeaks(doc: WikiDoc, questions: StudentQuestion[]): { id: string; words: string[] }[] {
  const titles = new Map(doc.entries.map((entry) => [entry.id, entry.title]))
  const leaks: { id: string; words: string[] }[] = []
  for (const question of questions) {
    const words = new Set<string>()
    for (const id of question.expect) {
      const title = titles.get(id)
      if (!title) continue
      for (const word of titleLeaks(question.question, title)) words.add(word)
    }
    if (words.size > 0) leaks.push({ id: question.id, words: [...words] })
  }
  return leaks
}

export function missingExpect(doc: WikiDoc, questions: StudentQuestion[]): string[] {
  const byId = new Map(doc.entries.map((entry) => [entry.id, entry]))
  const missing: string[] = []
  for (const question of questions) {
    for (const id of question.expect) {
      const entry = byId.get(id)
      if (!entry?.text || entry.copy_of) missing.push(`${question.id}:${id}`)
    }
  }
  return missing
}
