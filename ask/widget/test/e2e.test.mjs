// Browser tests for the Ask StatWiki widget, against test/server.mjs.
// Build first: npm run build && npm run e2e

import assert from "node:assert/strict"
import { stat } from "node:fs/promises"
import { dirname, resolve } from "node:path"
import { after, before, beforeEach, test } from "node:test"
import { fileURLToPath } from "node:url"

import { chromium } from "playwright"

import { start } from "./server.mjs"

const here = dirname(fileURLToPath(import.meta.url))
const TURNSTILE_STUB = `window.turnstile = {
  render(el, options) { setTimeout(() => options.callback("turnstile-ok"), 5); return "w1" },
  remove() {},
}`

let server
let browser

before(async () => {
  server = await start()
  browser = await chromium.launch()
})
after(async () => {
  await browser?.close()
  await server?.close()
})
beforeEach(() => {
  server.log.sessions = 0
  server.log.asks = []
})

async function page(viewport = { width: 1280, height: 900 }) {
  const context = await browser.newContext({ viewport })
  await context.route("https://challenges.cloudflare.com/**", (route) => route.fulfill({ contentType: "text/javascript", body: TURNSTILE_STUB }))
  const tab = await context.newPage()
  const requests = []
  tab.on("request", (request) => requests.push(request.url()))
  return { context, tab, requests }
}

async function ask(tab, question) {
  await tab.fill("#ask-statwiki-input", question)
  await tab.keyboard.press("Enter")
}

test("an unopened page loads only the small launcher", async () => {
  const { context, tab, requests } = await page()
  await tab.goto(`${server.url}/notes/chapter.html`)
  await tab.waitForSelector("#ask-statwiki-launch")
  assert.equal(requests.some((url) => url.endsWith("/app.js")), false)
  assert.equal(requests.some((url) => url.includes("challenges.cloudflare.com")), false)
  const size = (await stat(resolve(here, "../dist/loader.js"))).size
  assert.ok(size < 10 * 1024, `loader.js is ${size} bytes`)
  await context.close()
})

test("asking streams an answer with rendered maths and citation buttons", async () => {
  const { context, tab } = await page()
  await tab.goto(`${server.url}/notes/chapter.html`)
  await tab.evaluate(() => document.getElementById("s-mle").scrollIntoView())
  await tab.click("#ask-statwiki-launch")
  await tab.waitForSelector("#ask-statwiki-input")
  assert.equal(await tab.evaluate(() => document.activeElement?.id), "ask-statwiki-input")
  await ask(tab, "Why do we take the log of the likelihood?")
  await tab.waitForSelector(".ask-assistant .ask-cite[data-n='2']")
  // Passages 4, 2, 4 are shown as sources 1, 2, 1; the stray [7] is gone.
  assert.deepEqual(await tab.locator(".ask-assistant .ask-cite").allTextContents(), ["1", "2", "1"])
  assert.deepEqual(await tab.locator(".ask-source-n").allTextContents(), ["1", "2"])
  assert.match(await tab.locator(".ask-source").nth(1).textContent(), /Log\u2013likelihood/)
  assert.ok(await tab.locator(".ask-assistant .ask-body .katex").count() >= 1)
  assert.equal(await tab.locator(".ask-assistant .ask-body").textContent().then((t) => t.includes("[7]")), false)
  assert.equal(await tab.locator(".ask-source").count(), 2)
  assert.equal(server.log.sessions, 1)
  const sent = server.log.asks.at(-1)
  assert.equal(sent.page, "/notes/chapter.html")
  assert.equal(sent.anchor, "s-mle")
  assert.equal(sent.session, "s1")
  assert.deepEqual(sent.turns, [{ role: "user", content: "Why do we take the log of the likelihood?" }])
  await context.close()
})

test("a citation opens the passage beside the chat, and the chat survives a page change", async () => {
  const { context, tab } = await page()
  await tab.goto(`${server.url}/notes/chapter.html`)
  await tab.click("#ask-statwiki-launch")
  await ask(tab, "Why logs?")
  await tab.click(".ask-assistant .ask-cite[data-n='1']")
  await tab.waitForSelector(".ask-reader .ask-reader-body .katex")
  assert.match(await tab.locator(".ask-reader .ask-title").textContent(), /The target section/)
  assert.equal(await tab.locator(".ask-chat").isVisible(), true)
  assert.equal(await tab.evaluate(() => window.__fromPassage), undefined)
  assert.equal(await tab.locator(".ask-reader-body [id]").count(), 0)

  await tab.click(".ask-reader-foot a")
  await tab.waitForURL(/target\.html#s-target/)
  await tab.waitForSelector(".ask-assistant .ask-cite")
  assert.equal(await tab.locator(".ask-user").textContent(), "Why logs?")
  assert.equal(await tab.locator(".ask-reader").isVisible(), true)
  assert.equal(await tab.getAttribute("#ask-statwiki-launch", "aria-expanded"), "true")

  // The second question carries the first exchange, and reuses the session.
  await ask(tab, "And for the Poisson?")
  await tab.waitForFunction(() => document.querySelectorAll(".ask-assistant .ask-sources").length === 2)
  const sent = server.log.asks.at(-1)
  assert.deepEqual(sent.turns.map((t) => t.role), ["user", "assistant", "user"])
  assert.equal(sent.page, "/notes/target.html")
  assert.equal(server.log.sessions, 1)
  await context.close()
})

test("a question StatWiki doesn't cover gets the fixed reply", async () => {
  const { context, tab } = await page()
  await tab.goto(`${server.url}/notes/chapter.html`)
  await tab.click("#ask-statwiki-launch")
  await ask(tab, "Give me a pasta recipe")
  await tab.waitForSelector(".ask-not-covered .ask-body")
  assert.equal(await tab.locator(".ask-cite").count(), 0)
  await context.close()
})

test("model text cannot add HTML, links, images or scripts", async () => {
  const { context, tab } = await page()
  await tab.goto(`${server.url}/notes/chapter.html`)
  await tab.click("#ask-statwiki-launch")
  await ask(tab, "xss please")
  await tab.waitForSelector(".ask-assistant .ask-body strong")
  const body = tab.locator(".ask-assistant .ask-body")
  assert.equal(await body.locator("img, script, a, iframe").count(), 0)
  assert.equal(await tab.evaluate(() => window.__xss), undefined)
  assert.match(await body.textContent(), /click/)
  await context.close()
})

test("Escape closes the passage, then the chat", async () => {
  const { context, tab } = await page()
  await tab.goto(`${server.url}/notes/chapter.html`)
  await tab.click("#ask-statwiki-launch")
  await ask(tab, "Why logs?")
  await tab.click(".ask-assistant .ask-cite[data-n='2']")
  await tab.waitForSelector(".ask-reader")
  assert.match(await tab.locator(".ask-reader .ask-title").textContent(), /Log-likelihood|Definition/)
  await tab.keyboard.press("Escape")
  await tab.waitForSelector(".ask-reader", { state: "detached" })
  assert.equal(await tab.locator(".ask-chat").isVisible(), true)
  await tab.keyboard.press("Escape")
  await tab.waitForSelector(".ask-chat", { state: "detached" })
  assert.equal(await tab.getAttribute("#ask-statwiki-launch", "aria-expanded"), "false")
  assert.equal(await tab.evaluate(() => document.activeElement?.id), "ask-statwiki-launch")
  await context.close()
})

test("on a phone the chat and the passage fill the screen", async () => {
  const { context, tab } = await page({ width: 390, height: 844 })
  await tab.goto(`${server.url}/notes/chapter.html`)
  await tab.click("#ask-statwiki-launch")
  const chat = await tab.locator(".ask-chat").boundingBox()
  assert.equal(Math.round(chat.width), 390)
  assert.equal(await tab.locator("#ask-statwiki-launch").isVisible(), false)
  await ask(tab, "Why logs?")
  await tab.click(".ask-assistant .ask-cite[data-n='1']")
  await tab.waitForSelector(".ask-reader .ask-reader-body p")
  assert.equal(await tab.locator(".ask-chat").isVisible(), false)
  await tab.click(".ask-back")
  assert.equal(await tab.locator(".ask-chat").isVisible(), true)
  await context.close()
})

test("an answer cut off by a page change can be tried again", async () => {
  const { context, tab } = await page()
  await tab.goto(`${server.url}/notes/chapter.html`)
  await tab.click("#ask-statwiki-launch")
  await ask(tab, "slow question")
  await tab.waitForSelector(".ask-thinking")
  await tab.goto(`${server.url}/notes/target.html`)
  await tab.waitForSelector(".ask-error")
  assert.match(await tab.locator(".ask-error").textContent(), /cut off/)
  await tab.click(".ask-error .ask-link")
  await tab.waitForSelector(".ask-assistant .ask-cite", { timeout: 15000 })
  assert.equal(await tab.locator(".ask-error").count(), 0)
  await context.close()
})

test("an expired session runs the browser check once more", async () => {
  const { context, tab } = await page()
  await tab.goto(`${server.url}/notes/chapter.html`)
  await tab.evaluate(() => localStorage.setItem("ask-statwiki-session", JSON.stringify({ session: "expired", expires: Date.now() / 1000 + 3600 })))
  await tab.click("#ask-statwiki-launch")
  await ask(tab, "Why logs?")
  await tab.waitForSelector(".ask-assistant .ask-cite")
  assert.equal(server.log.sessions, 1)
  assert.equal(server.log.asks.length, 2)
  assert.equal(server.log.asks[0].session, "expired")
  assert.notEqual(server.log.asks[1].session, "expired")
  await context.close()
})
