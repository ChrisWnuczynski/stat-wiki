import { StrictMode, useCallback, useEffect, useMemo, useRef, useState, type KeyboardEvent, type MouseEvent } from "react"
import { createRoot } from "react-dom/client"

import { AskError, askStream, openSession } from "./api.ts"
import {
  clearSession,
  ensureKatex,
  loadPassage,
  loadSession,
  loadState,
  pageContext,
  renderAnswer,
  renderPageMath,
  saveSession,
  saveState,
  turnstileToken,
  type Passage,
} from "./browser.ts"
import { buildTurns, QUESTION_CHARS, type Citation, type Msg } from "./text.ts"
import "./styles.css"

type Options = { endpoint: string; sitekey: string; offset: string; launcher: HTMLButtonElement }
type Katex = NonNullable<Window["katex"]>

const uid = () => Math.random().toString(36).slice(2, 10)

function friendly(error: unknown): string {
  if (error instanceof AskError) {
    if (error.status === 429) return "That's the most questions allowed today. Try again tomorrow."
    if (error.status === 403 || error.status === 401) return "The browser check didn't pass. Reload the page and try again."
    if (error.status === 400 && error.message) return error.message
  }
  if (error instanceof Error && error.message === "turnstile") return "The browser check couldn't run. Check your connection, or turn off a blocker for this site, then try again."
  return "Ask StatWiki couldn't be reached. Try again in a minute."
}

function Answer({ msg, katex, onCite, onRetry }: {
  msg: Msg
  katex: Katex | null
  onCite: (citation: Citation) => void
  onRetry: (msg: Msg) => void
}) {
  const known = useMemo(() => (msg.state === "done" ? new Set((msg.citations ?? []).map((c) => c.number)) : null), [msg.state, msg.citations])
  const html = useMemo(() => renderAnswer(msg.content, known, katex), [msg.content, known, katex])
  const sources = useMemo(() => {
    const seen = new Map<string, Citation & { numbers: number[] }>()
    for (const c of msg.citations ?? []) {
      const prior = seen.get(c.id)
      if (prior) prior.numbers.push(c.number)
      else seen.set(c.id, { ...c, numbers: [c.number] })
    }
    return [...seen.values()]
  }, [msg.citations])
  const click = (event: MouseEvent<HTMLDivElement>) => {
    const target = (event.target as HTMLElement).closest<HTMLElement>(".ask-cite")
    if (!target) return
    const citation = msg.citations?.find((c) => c.number === Number(target.dataset.n))
    if (citation) onCite(citation)
  }
  const thinking = msg.state === "streaming" && !msg.content
  return (
    <div className={`ask-msg ask-assistant${msg.covered === false ? " ask-not-covered" : ""}`}>
      {thinking && (
        <p className="ask-thinking" role="status">
          Thinking<span aria-hidden="true">…</span>
          <span className="ask-hint">Careful answers can take up to a minute.</span>
        </p>
      )}
      {msg.content && <div className="ask-body" dangerouslySetInnerHTML={{ __html: html }} onClick={click} />}
      {sources.length > 0 && (
        <div className="ask-sources">
          <span className="ask-sources-label">Sources</span>
          {sources.map((s) => (
            <button key={s.id} type="button" className="ask-source" onClick={() => onCite(s)}>
              <span className="ask-source-n">{s.numbers.join(", ")}</span>
              {s.title || s.id}
            </button>
          ))}
        </div>
      )}
      {(msg.state === "error" || msg.state === "interrupted") && (
        <p className="ask-error" role="alert">
          {msg.state === "interrupted" ? "This answer was cut off when the page changed." : msg.error}
          <button type="button" className="ask-link" onClick={() => onRetry(msg)}>Try again</button>
        </p>
      )}
    </div>
  )
}

function Reader({ url, katex, onClose }: { url: string; katex: Katex | null; onClose: () => void }) {
  const [passage, setPassage] = useState<Passage | null>(null)
  const [failed, setFailed] = useState(false)
  const body = useRef<HTMLDivElement>(null)
  useEffect(() => {
    let live = true
    setPassage(null)
    setFailed(false)
    loadPassage(url).then((p) => live && setPassage(p)).catch(() => live && setFailed(true))
    return () => {
      live = false
    }
  }, [url])
  useEffect(() => {
    const el = body.current
    if (!el || !passage) return
    el.replaceChildren(passage.node.cloneNode(true))
    renderPageMath(el, katex)
    el.scrollTop = 0
  }, [passage, katex])
  return (
    <section className="ask-reader" aria-label="Cited passage">
      <header className="ask-head">
        <button type="button" className="ask-icon ask-back" onClick={onClose} aria-label="Back to the chat">‹</button>
        <h2 className="ask-title">{passage?.title ?? (failed ? "Couldn't load this passage" : "Loading…")}</h2>
        <button type="button" className="ask-icon ask-close-reader" onClick={onClose} aria-label="Close the passage">×</button>
      </header>
      <div className="ask-reader-body" ref={body} />
      <footer className="ask-reader-foot">
        <a href={url}>Open the full page</a>
      </footer>
    </section>
  )
}

type Controller = { toggle?: () => void; pending: number }

function App({ options, controller }: { options: Options; controller: Controller }) {
  const saved = useMemo(loadState, [])
  const [open, setOpen] = useState(saved.open)
  const [messages, setMessages] = useState<Msg[]>(saved.messages)
  const [panel, setPanel] = useState<string | null>(saved.panel)
  const [draft, setDraft] = useState("")
  const [busy, setBusy] = useState(false)
  const [katex, setKatex] = useState<Katex | null>(window.katex ?? null)
  const input = useRef<HTMLTextAreaElement>(null)
  const list = useRef<HTMLDivElement>(null)
  const check = useRef<HTMLDivElement>(null)

  controller.toggle = () => setOpen((o) => !o)
  useEffect(() => {
    // Clicks that arrived before the first render.
    if (controller.pending % 2 === 1) setOpen((o) => !o)
    controller.pending = 0
  }, [controller])

  useEffect(() => {
    ensureKatex(options.offset).then((k) => k && setKatex(k))
  }, [options.offset])
  useEffect(() => saveState({ open, messages, panel }), [open, messages, panel])
  useEffect(() => {
    options.launcher.setAttribute("aria-expanded", String(open))
    if (open) input.current?.focus()
  }, [open, options.launcher])
  useEffect(() => {
    list.current?.scrollTo({ top: list.current.scrollHeight })
  }, [messages])
  useEffect(() => {
    const onKey = (event: globalThis.KeyboardEvent) => {
      if (event.key !== "Escape") return
      if (panel) setPanel(null)
      else if (open) {
        setOpen(false)
        options.launcher.focus()
      }
    }
    document.addEventListener("keydown", onKey)
    return () => document.removeEventListener("keydown", onKey)
  }, [panel, open, options.launcher])

  const patch = useCallback((id: string, change: (m: Msg) => Msg) => {
    setMessages((all) => all.map((m) => (m.id === id ? change(m) : m)))
  }, [])

  const session = useCallback(async (fresh: boolean): Promise<string> => {
    if (!fresh) {
      const kept = loadSession()
      if (kept) return kept
    }
    if (!check.current) throw new Error("turnstile")
    const token = await turnstileToken(check.current, options.sitekey)
    const opened = await openSession(options.endpoint, token)
    saveSession(opened.session, opened.expires)
    return opened.session
  }, [options.endpoint, options.sitekey])

  const run = useCallback(async (history: Msg[], question: string, answerId: string) => {
    setBusy(true)
    const { page, anchor } = pageContext()
    const turns = buildTurns(history, question)
    try {
      for (let attempt = 0; attempt < 2; attempt++) {
        try {
          const token = await session(attempt > 0)
          for await (const { event, data } of askStream(options.endpoint, { turns, page, anchor, session: token })) {
            if (event === "status") patch(answerId, (m) => ({ ...m, covered: data.covered === true }))
            else if (event === "delta") patch(answerId, (m) => ({ ...m, content: m.content + String(data.text ?? "") }))
            else if (event === "citations") patch(answerId, (m) => ({ ...m, citations: (data.citations as Citation[]) ?? [] }))
            else if (event === "error") throw new AskError(502, "")
          }
          patch(answerId, (m) => ({ ...m, state: "done" }))
          return
        } catch (error) {
          // An expired or unknown session: run the browser check once more.
          if (error instanceof AskError && error.status === 401 && attempt === 0) {
            clearSession()
            continue
          }
          throw error
        }
      }
    } catch (error) {
      patch(answerId, (m) => ({ ...m, state: "error", error: friendly(error) }))
    } finally {
      setBusy(false)
    }
  }, [patch, session, options.endpoint])

  const send = () => {
    const question = draft.trim()
    if (!question || busy) return
    const user: Msg = { id: uid(), role: "user", content: question }
    const answer: Msg = { id: uid(), role: "assistant", content: "", state: "streaming" }
    const history = messages
    setMessages([...history, user, answer])
    setDraft("")
    void run(history, question, answer.id)
  }

  const retry = (failed: Msg) => {
    if (busy) return
    const index = messages.findIndex((m) => m.id === failed.id)
    const question = messages[index - 1]
    if (!question || question.role !== "user") return
    const history = messages.slice(0, index - 1)
    patch(failed.id, (m) => ({ ...m, content: "", citations: [], state: "streaming", error: undefined }))
    void run(history, question.content, failed.id)
  }

  const onKeyDown = (event: KeyboardEvent<HTMLTextAreaElement>) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault()
      send()
    }
  }

  if (!open) return null
  return (
    <div className={`ask-shell${panel ? " ask-with-reader" : ""}`}>
      {panel && <Reader url={panel} katex={katex} onClose={() => setPanel(null)} />}
      <section className="ask-chat" role="dialog" aria-label="Ask StatWiki">
        <header className="ask-head">
          <h2 className="ask-title">Ask StatWiki</h2>
          <button type="button" className="ask-link" onClick={() => { setMessages([]); setPanel(null) }} disabled={busy || messages.length === 0}>
            New conversation
          </button>
          <button type="button" className="ask-icon" onClick={() => { setOpen(false); options.launcher.focus() }} aria-label="Close Ask StatWiki">×</button>
        </header>
        <div className="ask-list" ref={list} aria-live="polite">
          {messages.length === 0 && (
            <p className="ask-empty">
              Ask about anything on StatWiki: a definition, a step in a proof, why a method works. Answers link to the passages they use.
            </p>
          )}
          {messages.map((msg) =>
            msg.role === "user"
              ? <div key={msg.id} className="ask-msg ask-user">{msg.content}</div>
              : <Answer key={msg.id} msg={msg} katex={katex} onCite={(c) => setPanel(c.url)} onRetry={retry} />)}
        </div>
        <div className="ask-check" ref={check} />
        <form className="ask-compose" onSubmit={(event) => { event.preventDefault(); send() }}>
          <label className="ask-visually-hidden" htmlFor="ask-statwiki-input">Your question</label>
          <textarea
            id="ask-statwiki-input"
            ref={input}
            rows={2}
            maxLength={QUESTION_CHARS}
            value={draft}
            placeholder="Ask a statistics question"
            onChange={(event) => setDraft(event.target.value)}
            onKeyDown={onKeyDown}
          />
          <button type="submit" className="ask-send" disabled={busy || !draft.trim()}>Send</button>
        </form>
        <p className="ask-note">
          Answers are written by xAI's Grok from StatWiki's pages and can be wrong, so check the sources. Questions go to xAI to be answered; StatWiki doesn't store them.
        </p>
      </section>
    </div>
  )
}

export function mount(root: HTMLElement, options: Options): { toggle(): void } {
  const controller: Controller = { pending: 0 }
  createRoot(root).render(
    <StrictMode>
      <App options={options} controller={controller} />
    </StrictMode>,
  )
  return {
    toggle() {
      if (controller.toggle) controller.toggle()
      else controller.pending += 1
    },
  }
}
