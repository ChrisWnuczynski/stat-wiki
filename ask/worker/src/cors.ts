export const PUBLIC_SITE = "https://www.statwiki.io"

export function allowedOrigin(origin: string | null): string | null {
  if (!origin) return null
  let url: URL
  try {
    url = new URL(origin)
  } catch {
    return null
  }
  if (url.origin === PUBLIC_SITE) return PUBLIC_SITE
  const local = url.hostname === "localhost" || url.hostname === "127.0.0.1"
  if (local && (url.protocol === "http:" || url.protocol === "https:")) return url.origin
  return null
}

export function corsHeaders(origin: string | null): Headers {
  const headers = new Headers()
  headers.set("vary", "Origin")
  const allowed = allowedOrigin(origin)
  if (allowed) {
    headers.set("access-control-allow-origin", allowed)
    headers.set("access-control-allow-methods", "GET, POST, OPTIONS")
    headers.set("access-control-allow-headers", "content-type")
    headers.set("access-control-max-age", "86400")
  }
  return headers
}

export function originDenied(origin: string | null): boolean {
  return Boolean(origin) && !allowedOrigin(origin)
}
