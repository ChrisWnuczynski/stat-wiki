// A local stand-in for the site and the Worker, for the widget's browser tests.
// Serves test/site, the built widget at /ask/widget/dist, the site's KaTeX at
// /katex, and a fake /api that behaves like the Worker's /session and /ask.

import { readFile } from "node:fs/promises"
import { createServer } from "node:http"
import { dirname, extname, join, normalize, resolve } from "node:path"
import { fileURLToPath } from "node:url"

const here = dirname(fileURLToPath(import.meta.url))
const roots = [
  ["/ask/widget/dist/", resolve(here, "../dist")],
  ["/katex/", resolve(here, "../../../katex")],
  ["/", resolve(here, "site")],
]
const types = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf" }

export const ANSWER = "Taking logs turns the product into a sum [1], so $\\ell(\\theta)=\\sum_{i=1}^n \\log f(x_i;\\theta)$ is easier to maximise [2]. Stray [7]."
export const CITATIONS = [
  { number: 1, id: "section:target:s-target", title: "The target section", kind: "section", url: "/notes/target.html#s-target" },
  { number: 2, id: "definition:def-thing", title: "Log-likelihood", kind: "definition", url: "/notes/target.html#def-thing" },
]
export const NOT_COVERED = "StatWiki doesn't cover that."
export const XSS = "<img src=x onerror=\"window.__xss=1\"> [click](javascript:window.__xss=2) <script>window.__xss=3</script> ![pic](https://evil.example/p.png) **bold**"

const sse = (event, data) => `event: ${event}\ndata: ${JSON.stringify(data)}\n\n`
const sleep = (ms) => new Promise((done) => setTimeout(done, ms))

export async function start() {
  const log = { sessions: 0, asks: [] }
  let sessionCount = 0
  const server = createServer(async (req, res) => {
    const url = new URL(req.url, "http://localhost")
    if (url.pathname.startsWith("/api/")) {
      let body = ""
      for await (const chunk of req) body += chunk
      if (url.pathname === "/api/session") {
        log.sessions += 1
        sessionCount += 1
        res.writeHead(200, { "content-type": "application/json" })
        res.end(JSON.stringify({ session: `s${sessionCount}`, expires: Math.floor(Date.now() / 1000) + 3600 }))
        return
      }
      if (url.pathname === "/api/ask") {
        const parsed = JSON.parse(body)
        log.asks.push(parsed)
        if (parsed.session === "expired") {
          res.writeHead(401, { "content-type": "application/json" })
          res.end(JSON.stringify({ error: "A session token is required." }))
          return
        }
        const question = parsed.turns.at(-1).content
        res.writeHead(200, { "content-type": "text/event-stream" })
        if (/pasta/i.test(question)) {
          res.end(sse("status", { covered: false }) + sse("delta", { text: NOT_COVERED }) + sse("citations", { citations: [] }))
          return
        }
        if (/xss/i.test(question)) {
          res.end(sse("status", { covered: true }) + sse("delta", { text: XSS }) + sse("citations", { citations: [] }))
          return
        }
        res.write(sse("status", { covered: true }))
        if (/slow/i.test(question)) await sleep(4000)
        for (const piece of ANSWER.match(/.{1,12}/gs)) {
          res.write(sse("delta", { text: piece }))
          await sleep(5)
        }
        res.end(sse("citations", { citations: CITATIONS }))
        return
      }
      res.writeHead(404).end()
      return
    }
    for (const [prefix, dir] of roots) {
      if (!url.pathname.startsWith(prefix)) continue
      const file = normalize(join(dir, decodeURIComponent(url.pathname.slice(prefix.length))))
      if (!file.startsWith(dir)) break
      try {
        const data = await readFile(file)
        res.writeHead(200, { "content-type": types[extname(file)] ?? "application/octet-stream" })
        res.end(data)
        return
      } catch {
        break
      }
    }
    res.writeHead(404).end("not found")
  })
  await new Promise((done) => server.listen(0, "127.0.0.1", done))
  const { port } = server.address()
  return { url: `http://127.0.0.1:${port}`, log, close: () => new Promise((done) => server.close(done)) }
}
