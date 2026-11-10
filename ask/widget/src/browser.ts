// Browser-side helpers: KaTeX, Turnstile, Markdown rendering, the reader's
// place on the page, the reading panel's extracts, and saved state.

import DOMPurify from "dompurify"
import MarkdownIt from "markdown-it"

import { ANCHOR, extractMath, escapeHtml, linkCitations, MATH_TOKEN, normalizeDelimiters, safePage, type MathPiece, type Msg } from "./text.ts"

type Katex = {
  render(tex: string, el: HTMLElement, options: Record<string, unknown>): void
  renderToString(tex: string, options: Record<string, unknown>): string
}

declare global {
  interface Window {
    katex?: Katex
    turnstile?: {
      render(el: HTMLElement, options: Record<string, unknown>): string
      remove(id: string): void
    }
  }
}

// ---- KaTeX: the copy the site already ships, in /katex/ ----

let katexLoading: Promise<Katex | null> | null = null

export function ensureKatex(offset: string): Promise<Katex | null> {
  if (window.katex) return Promise.resolve(window.katex)
  if (!katexLoading) {
    katexLoading = new Promise((resolve) => {
      const css = document.createElement("link")
      css.rel = "stylesheet"
      css.href = `${offset}katex/katex.min.css`
      document.head.appendChild(css)
      const js = document.createElement("script")
      js.src = `${offset}katex/katex.min.js`
      js.onload = () => resolve(window.katex ?? null)
      js.onerror = () => resolve(null)
      document.head.appendChild(js)
    })
  }
  return katexLoading
}

// ---- Turnstile ----

let turnstileLoading: Promise<void> | null = null

function loadTurnstile(): Promise<void> {
  if (window.turnstile) return Promise.resolve()
  if (!turnstileLoading) {
    turnstileLoading = new Promise((resolve, reject) => {
      const script = document.createElement("script")
      script.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit"
      script.async = true
      script.onload = () => resolve()
      script.onerror = () => {
        turnstileLoading = null
        reject(new Error("turnstile"))
      }
      document.head.appendChild(script)
    })
  }
  return turnstileLoading
}

/** A Turnstile token. Usually invisible; Cloudflare shows a checkbox only when it needs one. */
export async function turnstileToken(container: HTMLElement, sitekey: string): Promise<string> {
  await loadTurnstile()
  const api = window.turnstile
  if (!api) throw new Error("turnstile")
  return new Promise((resolve, reject) => {
    let id = ""
    const done = () => setTimeout(() => api.remove(id), 0)
    id = api.render(container, {
      sitekey,
      appearance: "interaction-only",
      callback: (token: string) => {
        done()
        resolve(token)
      },
      "error-callback": () => {
        done()
        reject(new Error("turnstile"))
      },
      "expired-callback": () => {
        done()
        reject(new Error("turnstile"))
      },
    })
  })
}

// ---- Answers ----

const markdown = new MarkdownIt({ html: false, linkify: false, typographer: false, breaks: false })

function mathHtml(piece: MathPiece | undefined, katex: Katex | null): string {
  if (!piece) return ""
  if (katex) {
    try {
      return katex.renderToString(piece.tex, { displayMode: piece.display, throwOnError: false, trust: false, strict: "ignore" })
    } catch {
      // Fall through to the source.
    }
  }
  const tex = escapeHtml(piece.tex)
  return piece.display ? `<pre class="ask-tex">${tex}</pre>` : `<code class="ask-tex">${tex}</code>`
}

/**
 * Model text to HTML. Raw HTML in the answer is escaped by markdown-it, and the
 * result is sanitised: no links, images, styles or ids survive, because the model
 * must never write URLs. Citations and KaTeX output are added after sanitising.
 */
export function renderAnswer(text: string, known: ReadonlySet<number> | null, katex: Katex | null): string {
  const { text: body, maths } = extractMath(normalizeDelimiters(text))
  const clean = DOMPurify.sanitize(markdown.render(body), {
    FORBID_TAGS: ["a", "img", "style", "iframe", "form", "input", "button", "svg", "math", "video", "audio"],
    FORBID_ATTR: ["style", "href", "src", "id", "class"],
    KEEP_CONTENT: true,
  })
  const cited = known ? linkCitations(clean, known) : clean
  return cited.replace(MATH_TOKEN, (_m, i: string) => mathHtml(maths[Number(i)], katex))
}

// ---- Where the reader is ----

export function pageContext(): { page: string; anchor: string } {
  const page = safePage(location.pathname)
  const main = document.querySelector("main#quarto-document-content") ?? document.querySelector("main")
  let anchor = ""
  if (main) {
    const limit = window.innerHeight * 0.35
    for (const el of main.querySelectorAll<HTMLElement>("[id]")) {
      if (ANCHOR.test(el.id) && el.getBoundingClientRect().top <= limit) anchor = el.id
    }
  }
  const hash = decodeURIComponent(location.hash.slice(1))
  if (!anchor && ANCHOR.test(hash)) anchor = hash
  return { page, anchor: anchor.slice(0, 200) }
}

// ---- Reading panel ----

export type Passage = { title: string; url: string; node: HTMLElement }

const docs = new Map<string, Promise<Document>>()

function getDoc(url: string): Promise<Document> {
  let doc = docs.get(url)
  if (!doc) {
    doc = fetch(url).then(async (response) => {
      if (!response.ok) throw new Error(String(response.status))
      return new DOMParser().parseFromString(await response.text(), "text/html")
    })
    doc.catch(() => docs.delete(url))
    docs.set(url, doc)
  }
  return doc
}

const SKIP = "script, style, nav, header, #title-block-header, .quarto-title-block, .glossary-jump, .qfilter, .qnav"

/** The cited block of another page, cleaned up to sit in the panel. */
export async function loadPassage(href: string): Promise<Passage> {
  const target = new URL(href, location.href)
  const page = target.origin + target.pathname
  const hash = decodeURIComponent(target.hash.slice(1))
  const doc = await getDoc(page)
  const pageTitle = doc.querySelector("h1.title")?.textContent?.trim() || doc.title || page
  let title = pageTitle
  let node: HTMLElement | null = null
  if (hash) {
    const el = doc.getElementById(hash)
    if (el) {
      node = el.cloneNode(true) as HTMLElement
      if (hash === "worked-answer") {
        title = `Worked answer — ${pageTitle}`
        node.querySelectorAll(".callout-header").forEach((n) => n.remove())
        node.querySelectorAll(".collapse").forEach((n) => n.classList.remove("collapse"))
      } else {
        const heading = el.tagName === "SECTION" ? el.querySelector("h2, h3, h4") : el.querySelector(".theorem-title, h2, h3")
        if (heading?.textContent?.trim()) title = `${heading.textContent.trim()} — ${pageTitle}`
      }
    }
  }
  if (!node) {
    node = document.createElement("div")
    const main = doc.querySelector("main#quarto-document-content") ?? doc.querySelector("main")
    for (const child of Array.from(main?.children ?? [])) {
      if (!child.matches(SKIP)) node.appendChild(child.cloneNode(true))
    }
  }
  node.querySelectorAll(SKIP).forEach((n) => n.remove())
  // The extract sits inside this page, so its ids and handlers go, the outer element's too.
  for (const el of [node, ...Array.from(node.querySelectorAll("*"))]) {
    el.removeAttribute("id")
    for (const attr of Array.from(el.attributes)) if (attr.name.startsWith("on")) el.removeAttribute(attr.name)
  }
  node.querySelectorAll<HTMLImageElement>("img[src]").forEach((img) => {
    img.src = new URL(img.getAttribute("src") ?? "", page).href
  })
  node.querySelectorAll<HTMLAnchorElement>("a[href]").forEach((a) => {
    a.href = new URL(a.getAttribute("href") ?? "", page).href
  })
  return { title, url: target.href, node }
}

/** Render the page's own maths spans, as the hover previews do. */
export function renderPageMath(root: HTMLElement, katex: Katex | null): void {
  if (!katex) return
  root.querySelectorAll<HTMLElement>("span.math").forEach((el) => {
    const tex = (el.textContent ?? "").trim().replace(/^\\[([]/, "").replace(/\\[)\]]$/, "")
    try {
      katex.render(tex, el, { displayMode: el.classList.contains("display"), throwOnError: false })
    } catch {
      // Leave the source.
    }
  })
}

// ---- Saved state ----

const STATE_KEY = "ask-statwiki-v1"
const SESSION_KEY = "ask-statwiki-session"

export type Saved = { open: boolean; messages: Msg[]; panel: string | null }

export function loadState(): Saved {
  try {
    const raw = JSON.parse(localStorage.getItem(STATE_KEY) ?? "{}") as Partial<Saved>
    const messages = Array.isArray(raw.messages) ? raw.messages : []
    return {
      open: raw.open === true,
      panel: typeof raw.panel === "string" ? raw.panel : null,
      // An answer that was still arriving when the page changed did not finish.
      messages: messages.map((m) => (m.state === "streaming" ? { ...m, state: "interrupted" as const } : m)),
    }
  } catch {
    return { open: false, messages: [], panel: null }
  }
}

export function saveState(state: Saved): void {
  try {
    localStorage.setItem(STATE_KEY, JSON.stringify({ ...state, messages: state.messages.slice(-40) }))
  } catch {
    // Storage full or blocked: the chat still works on this page.
  }
}

export function loadSession(): string {
  try {
    const raw = JSON.parse(localStorage.getItem(SESSION_KEY) ?? "{}") as { session?: unknown; expires?: unknown }
    if (typeof raw.session === "string" && typeof raw.expires === "number" && raw.expires - 60 > Date.now() / 1000) return raw.session
  } catch {
    // Fall through.
  }
  return ""
}

export function saveSession(session: string, expires: number): void {
  try {
    localStorage.setItem(SESSION_KEY, JSON.stringify({ session, expires }))
  } catch {
    // Not saved: the next page asks Turnstile again.
  }
}

export function clearSession(): void {
  try {
    localStorage.removeItem(SESSION_KEY)
  } catch {
    // Nothing to clear.
  }
}
