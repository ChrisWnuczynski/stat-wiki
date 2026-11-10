// Ask StatWiki launcher. This is the only part every page loads: one button.
// The chat itself (React, Markdown, the reading panel) is fetched on first use.

type Controller = { toggle(): void }
type AppModule = { mount(root: HTMLElement, options: Record<string, unknown>): Controller }
type Settings = { endpoint: string; sitekey: string }

const DEFAULTS: Settings = { endpoint: "https://ask.statwiki.io", sitekey: "0x4AAAAAAF6-zg9WIc3YvWfS" }
const STATE_KEY = "ask-statwiki-v1"

const CSS = `.ask-launch{position:fixed;right:20px;bottom:20px;z-index:1060;display:flex;align-items:center;gap:8px;padding:10px 16px;border:1px solid var(--wiki-border,#a2a9b1);border-radius:999px;background:var(--wiki-link,#3366cc);color:#fff;font:600 15px/1.2 system-ui,sans-serif;box-shadow:var(--wiki-shadow,0 6px 18px rgba(0,0,0,.18));cursor:pointer}
.ask-launch:hover{background:var(--wiki-link-hover,#2a4b8d)}
.ask-launch:focus-visible{outline:3px solid var(--wiki-text,#202122);outline-offset:2px}
.ask-launch svg{width:18px;height:18px}
body.quarto-dark .ask-launch{color:#101418}
@media (max-width:700px){.ask-launch{right:12px;bottom:12px;padding:10px 14px}.ask-launch[aria-expanded=true]{display:none}}
@media print{.ask-launch{display:none}}`

function settings(): Settings | null {
  const override = (window as unknown as { __ASK_STATWIKI__?: Partial<Settings> }).__ASK_STATWIKI__
  if (override && typeof override === "object") return { ...DEFAULTS, ...override }
  return /^(www\.)?statwiki\.io$/.test(location.hostname) ? DEFAULTS : null
}

function wasOpen(): boolean {
  try {
    return (JSON.parse(localStorage.getItem(STATE_KEY) ?? "{}") as { open?: unknown }).open === true
  } catch {
    return false
  }
}

const found = settings()
if (found && !document.getElementById("ask-statwiki-launch")) {
  const meta = document.querySelector('meta[name="quarto:offset"]')
  const offset = meta?.getAttribute("content") || "./"

  const style = document.createElement("style")
  style.textContent = CSS
  document.head.appendChild(style)

  const button = document.createElement("button")
  button.id = "ask-statwiki-launch"
  button.type = "button"
  button.className = "ask-launch"
  button.setAttribute("aria-expanded", "false")
  button.setAttribute("aria-controls", "ask-statwiki")
  button.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg><span>Ask StatWiki</span>'

  const root = document.createElement("div")
  root.id = "ask-statwiki"
  document.body.append(root, button)

  // Files next to this one. Built as strings so the bundler leaves them alone.
  const here = import.meta.url.slice(0, import.meta.url.lastIndexOf("/") + 1)
  let app: Promise<Controller> | null = null
  const load = (): Promise<Controller> => {
    if (!app) {
      const css = document.createElement("link")
      css.rel = "stylesheet"
      css.href = `${here}app.css`
      document.head.appendChild(css)
      app = import(/* @vite-ignore */ `${here}app.js`)
        .then((mod: AppModule) => mod.mount(root, { ...found, offset, launcher: button }))
      app.catch(() => {
        app = null
      })
    }
    return app
  }
  button.addEventListener("click", () => {
    void load().then((controller) => controller.toggle())
  })
  // Reopen the chat on the next page if it was open on the last one.
  if (wasOpen()) void load()
}
