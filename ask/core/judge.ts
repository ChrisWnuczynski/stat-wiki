// Reading the judge's replies. The judge is asked for one JSON object, but it
// often writes LaTeX such as \( or \beta inside the strings, which is not valid
// JSON. Those replies still carry a readable grade, so they are repaired, not
// thrown away.

export const GRADES = ["correct", "minor error", "wrong", "did not answer"] as const
export type Grade = typeof GRADES[number]

// A judge reply that could not be read even after one retry. It is not a grade
// and is left out of the graded counts.
export const UNREADABLE = "judge unreadable"

// Doubles every backslash that does not start a JSON escape. \b \f \n \r \t
// followed by a letter are LaTeX commands (\beta, \frac, \nu, \rho, \theta),
// not escapes.
export function repairBackslashes(text: string): string {
  return text.replace(/\\(u[0-9a-fA-F]{4}|["\\/]|[bfnrt](?![A-Za-z]))?/g, (whole, escape) => (escape ? whole : "\\\\"))
}

export function parseJsonObject(text: string): Record<string, unknown> | null {
  const match = text.match(/\{[\s\S]*\}/)
  if (!match) return null
  for (const candidate of [match[0], repairBackslashes(match[0])]) {
    try {
      const value = JSON.parse(candidate) as unknown
      if (value && typeof value === "object" && !Array.isArray(value)) return value as Record<string, unknown>
    } catch {
      // try the repaired text next
    }
  }
  return null
}

const clean = (value: unknown) => String(value ?? "").replace(/\s+/g, " ").trim().slice(0, 400)

export function parseJudge(text: string): { grade: Grade; reason: string; doubt: string } | null {
  const obj = parseJsonObject(text)
  if (!obj) return null
  const grade = String(obj.grade ?? "").toLowerCase().trim() as Grade
  if (!GRADES.includes(grade)) return null
  return { grade, reason: clean(obj.reason), doubt: clean(obj.reference_doubt) }
}

// Reads one string field from the start of a reply that may be cut off, as in
// older run files that kept only the first 120 characters of an unread reply.
export function leadingField(text: string, field: string): string | null {
  const match = text.match(new RegExp(`"${field}"\\s*:\\s*"([^"\\\\]*)"`))
  return match ? match[1].toLowerCase().trim() : null
}
