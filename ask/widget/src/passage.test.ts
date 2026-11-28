// The cited-passage reader must not typeset a formula that is already KaTeX.

import assert from "node:assert/strict"
import { createServer, type Server } from "node:http"
import { createRequire } from "node:module"
import { readFileSync } from "node:fs"
import { dirname, resolve } from "node:path"
import { fileURLToPath } from "node:url"
import test from "node:test"
import type { AddressInfo } from "node:net"

import { chromium, type Browser } from "playwright"
import { createServer as createVite, type ViteDevServer } from "vite"

const here = dirname(fileURLToPath(import.meta.url))
const widget = resolve(here, "..")
const repo = resolve(widget, "../..")
const require = createRequire(import.meta.url)
const katex = require(resolve(repo, "katex/katex.min.js")) as {
  renderToString(tex: string, options: Record<string, unknown>): string
}

const typeset = katex.renderToString("\\bar{x}_n", {
  displayMode: false,
  throwOnError: true,
  output: "htmlAndMathml",
  strict: "ignore",
})

const article = `<!DOCTYPE html><html><body>
<main id="quarto-document-content">
<section id="sample">
<h2>Sample mean</h2>
<p>The mean <span class="math inline already">${typeset}</span> and the square <span class="math inline raw">a^2</span>.</p>
</section>
</main></body></html>`

const host = `<!DOCTYPE html><html><body>
<script src="/katex/katex.min.js"></script>
<script type="module">
import { loadPassage, renderPageMath } from "/src/browser.ts"
window.__loadPassage = loadPassage
window.__renderPageMath = renderPageMath
</script>
</body></html>`

test("cited passage keeps typeset maths and renders only raw TeX", { timeout: 60_000 }, async () => {
  const vite: ViteDevServer = await createVite({
    root: widget,
    configFile: resolve(widget, "vite.config.ts"),
    base: "/",
    server: { middlewareMode: true },
    appType: "custom",
    logLevel: "error",
  })
  const server: Server = createServer((req, res) => {
    const path = new URL(req.url ?? "/", "http://127.0.0.1").pathname
    if (path === "/fixture/article.html") {
      res.writeHead(200, { "content-type": "text/html; charset=utf-8" })
      res.end(article)
      return
    }
    if (path === "/fixture/host.html") {
      res.writeHead(200, { "content-type": "text/html; charset=utf-8" })
      res.end(host)
      return
    }
    if (path === "/katex/katex.min.js") {
      res.writeHead(200, { "content-type": "text/javascript" })
      res.end(readFileSync(resolve(repo, "katex/katex.min.js")))
      return
    }
    vite.middlewares(req, res, () => {
      res.statusCode = 404
      res.end()
    })
  })
  await new Promise<void>((done) => server.listen(0, "127.0.0.1", done))
  const port = (server.address() as AddressInfo).port
  let browser: Browser | undefined
  try {
    browser = await chromium.launch()
    const page = await browser.newPage()
    await page.goto(`http://127.0.0.1:${port}/fixture/host.html`, { waitUntil: "networkidle" })
    await page.waitForFunction(() => "window" in globalThis && "__loadPassage" in window)
    const result = await page.evaluate(async () => {
      const win = window as unknown as {
        __loadPassage: (href: string) => Promise<{ node: HTMLElement }>
        __renderPageMath: (root: HTMLElement, katex: unknown) => void
        katex?: unknown
      }
      const passage = await win.__loadPassage("/fixture/article.html#sample")
      const root = document.createElement("div")
      root.appendChild(passage.node)
      const already = root.querySelector(".already")
      const before = already?.querySelector("math")?.outerHTML ?? ""
      win.__renderPageMath(root, win.katex)
      win.__renderPageMath(root, win.katex)
      const formulas = [...root.querySelectorAll("span.math")].map((el) => ({
        kind: el.classList.contains("already") ? "already" : "raw",
        katex: el.querySelectorAll(".katex").length,
        nested: el.querySelectorAll(".katex .katex").length,
        math: el.querySelectorAll("math").length,
      }))
      return {
        before,
        after: root.querySelector(".already math")?.outerHTML ?? "",
        formulas,
        nestedInPassage: root.querySelectorAll(".katex .katex").length,
      }
    })
    assert.equal(result.before.length > 0, true)
    assert.equal(result.after, result.before)
    assert.equal(result.nestedInPassage, 0)
    assert.deepEqual(result.formulas, [
      { kind: "already", katex: 1, nested: 0, math: 1 },
      { kind: "raw", katex: 1, nested: 0, math: 1 },
    ])
  } finally {
    await browser?.close()
    await new Promise<void>((done) => server.close(() => done()))
    await vite.close()
  }
})

test("the bundle's other maths renderers leave a typeset span alone", () => {
  const preview = readFileSync(resolve(repo, "build_wiki.py"), "utf8")
  const prerender = readFileSync(resolve(repo, "tools/prerender_math.mjs"), "utf8")
  const reader = readFileSync(resolve(here, "browser.ts"), "utf8")
  for (const source of [preview, prerender, reader]) {
    assert.match(source, /querySelector\(\s*["']\.katex, math["']\s*\)/)
  }
  // Answers are new TeX from the model, rendered once to a string. They are
  // not written back over a span that already holds KaTeX.
  assert.match(reader, /renderToString\(piece\.tex/)
  assert.equal(reader.includes("katex.render(piece"), false)
})
