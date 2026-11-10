// Run the R blocks of a Using R page in the browser, with webR.
//
// The page loads this module only when it has R blocks and is a Using R page
// (the loader is in _random.html, written by build_wiki.py). Nothing is
// downloaded until a reader presses Run. R then comes from the webR CDN and
// packages from the webR package repository.
//
// Each block gets Run and Edit. Run executes the block in one R session for
// the page, after any block above it that has not run yet (session.js).
// Output, messages, warnings, errors and plots appear under the block.

import { webREngine } from "./engine.js";
import { PageSession } from "./session.js";
import { WEBR_BASE } from "./version.js";

const STYLE_ID = "r-run-style";

const CSS = `
.r-run-intro {
  margin: 0.4rem 0 0.6rem;
  font-size: 0.88rem;
  color: var(--wiki-muted);
}
.r-run {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.35rem 0.5rem;
  margin: -0.6rem 0 0.9rem;
  padding: 0.3rem 0.5rem;
  background: var(--wiki-panel);
  border: 1px solid var(--wiki-rule);
  border-top: none;
  font-size: 0.85rem;
}
.r-run button {
  font: inherit;
  color: var(--wiki-text);
  background: var(--wiki-bg);
  border: 1px solid var(--wiki-border);
  border-radius: 2px;
  padding: 0.15rem 0.6rem;
  cursor: pointer;
}
.r-run button:hover:not(:disabled) { background: var(--wiki-panel-head); }
.r-run button:disabled { opacity: 0.55; cursor: default; }
.r-run button.r-run-go { font-weight: 650; }
.r-run :focus-visible { outline: 2px solid var(--wiki-link); outline-offset: 2px; }
.r-run-status {
  color: var(--wiki-muted);
  font-variant-numeric: tabular-nums;
  min-width: 0;
}
.r-run-editor {
  display: block;
  box-sizing: border-box;
  width: 100%;
  margin: 1rem 0 0.6rem;
  padding: 0.55rem 0.7rem;
  font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
  font-size: 0.875em;
  line-height: 1.45;
  color: var(--wiki-text);
  background: var(--wiki-bg);
  border: 1px solid var(--wiki-link);
  border-radius: 2px;
  resize: vertical;
  tab-size: 2;
  white-space: pre;
  overflow-x: auto;
}
.r-output {
  margin: -0.5rem 0 1.1rem;
  padding: 0.5rem 0.7rem;
  border: 1px solid var(--wiki-rule);
  border-left: 3px solid var(--wiki-link);
  background: var(--wiki-bg);
}
.r-output pre {
  margin: 0;
  padding: 0;
  background: none;
  border: none;
  color: var(--wiki-text);
  font-size: 0.85em;
  white-space: pre;
  overflow-x: auto;
}
.r-output .r-out-message { color: var(--wiki-muted); }
.r-output .r-out-warning { color: #9a6b12; }
.r-output .r-out-error { color: #b42318; font-weight: 600; }
body.quarto-dark .r-output .r-out-warning { color: #e0b15a; }
body.quarto-dark .r-output .r-out-error { color: #f0a0a0; }
.r-output .r-out-note {
  margin: 0.35rem 0 0;
  font-size: 0.85rem;
  color: var(--wiki-text);
}
.r-output .r-out-earlier {
  margin: 0 0 0.3rem;
  font-size: 0.8rem;
  color: var(--wiki-muted);
}
.r-output canvas {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 0.4rem 0;
  background: #ffffff;
  border: 1px solid var(--wiki-rule);
}
`;

function installStyle() {
  if (document.getElementById(STYLE_ID)) return;
  const style = document.createElement("style");
  style.id = STYLE_ID;
  style.textContent = CSS;
  document.head.appendChild(style);
}

// The code a block shows. Quarto writes one <span> per line inside <code>,
// with an empty anchor for each line number, so the text is the source.
export function codeOfBlock(pre) {
  const code = pre.querySelector("code") ?? pre;
  return code.textContent.replace(/\n$/, "");
}

// webR from the CDN. The postMessage channel is chosen by webR itself, because
// GitHub Pages cannot send the headers that cross-origin isolation needs.
async function cdnEngine({ progress, plotSize }) {
  const { WebR } = await import(WEBR_BASE + "webr.mjs");
  return webREngine({ WebR, options: { baseUrl: WEBR_BASE }, progress, plotSize });
}

// Join consecutive stdout lines into one <pre>, as R prints them.
function renderItems(target, items) {
  let pre = null;
  let kind = null;
  for (const item of items) {
    if (!pre || kind !== item.kind) {
      pre = document.createElement("pre");
      pre.className = "r-out-" + item.kind;
      target.appendChild(pre);
      kind = item.kind;
      pre.textContent = item.text;
    } else {
      pre.textContent += "\n" + item.text;
    }
  }
}

function drawImages(target, images, blockNumber) {
  images.forEach((image, i) => {
    const canvas = document.createElement("canvas");
    canvas.width = image.width;
    canvas.height = image.height;
    // webr::canvas draws at twice the device size.
    canvas.style.width = Math.round(image.width / 2) + "px";
    canvas.setAttribute("role", "img");
    canvas.setAttribute("aria-label", `Plot ${i + 1} from R block ${blockNumber}`);
    canvas.getContext("2d").drawImage(image, 0, 0);
    target.appendChild(canvas);
  });
}

function seconds(ms) {
  return ms < 1000 ? `${ms} ms` : `${(ms / 1000).toFixed(1)} s`;
}

export function install({ startEngine } = {}) {
  const pres = [...document.querySelectorAll("main pre.sourceCode.r, #quarto-document-content pre.sourceCode.r")]
    .filter((pre, i, all) => all.indexOf(pre) === i);
  if (!pres.length) return null;
  installStyle();

  const blocks = pres.map((pre, index) => {
    const holder = pre.closest("div.sourceCode") ?? pre;
    return { index, pre, holder, original: codeOfBlock(pre), editor: null, bar: null, output: null };
  });
  const codeOf = (i) => (blocks[i].editor ? blocks[i].editor.value : blocks[i].original);
  const plotSize = () => {
    const width = Math.max(320, Math.min(720, Math.round(blocks[0].holder.getBoundingClientRect().width || 640)));
    return { width, height: Math.round(width * 0.62) };
  };
  let installing = [];
  let downloaded = [];
  let statusBlock = null;
  const session = new PageSession({
    codeOf,
    count: blocks.length,
    startEngine: () => (startEngine ?? cdnEngine)({
      plotSize,
      progress: (name) => {
        downloaded.push(name);
        if (statusBlock) setStatus(statusBlock, `Installing ${installing.join(", ")}: downloaded ${name} (${downloaded.length} packages so far)…`);
      },
    }),
  });

  const intro = document.createElement("p");
  intro.className = "r-run-intro";
  intro.textContent =
    "The R blocks on this page run in your browser. Run executes a block after any block above it that has not run yet, in one R session for the page. The first Run downloads R and the packages the page uses, which takes a while once.";
  blocks[0].holder.before(intro);

  function setStatus(block, text) {
    block.bar.querySelector(".r-run-status").textContent = text;
  }

  function setBusy(busy, active) {
    for (const block of blocks) {
      block.bar.querySelector(".r-run-go").disabled = busy;
      block.bar.querySelector(".r-run-stop").hidden = !(busy && block === active);
      if (!busy || block !== active) {
        const status = block.bar.querySelector(".r-run-status");
        if (busy && status.dataset.kind === "running") status.textContent = "";
      }
    }
  }

  function outputFor(block) {
    if (!block.output) {
      block.output = document.createElement("div");
      block.output.className = "r-output";
      block.output.setAttribute("aria-live", "polite");
      block.output.setAttribute("aria-label", `Output of R block ${block.index + 1}`);
      block.bar.after(block.output);
    }
    return block.output;
  }

  function showResult(block, result) {
    const out = outputFor(block);
    out.replaceChildren();
    if (result.earlier) {
      const note = document.createElement("p");
      note.className = "r-out-earlier";
      note.textContent = "Ran first, because a block below it was run.";
      out.appendChild(note);
    }
    renderItems(out, result.items);
    drawImages(out, result.images, block.index + 1);
    if (result.explanation) {
      const note = document.createElement("p");
      note.className = "r-out-note";
      note.textContent = result.explanation;
      out.appendChild(note);
    }
    if (!result.items.length && !result.images.length) {
      const pre = document.createElement("pre");
      pre.className = "r-out-message";
      pre.textContent = "(no output)";
      out.appendChild(pre);
    }
    const status = block.bar.querySelector(".r-run-status");
    status.dataset.kind = "";
    status.textContent = (result.error ? "Error" : "Ran") + " in " + seconds(result.ms) + ".";
  }

  function toggleEdit(block) {
    const button = block.bar.querySelector(".r-run-edit");
    if (block.editor && !block.editor.hidden) {
      block.editor.focus();
      return;
    }
    const editor = document.createElement("textarea");
    editor.className = "r-run-editor";
    editor.spellcheck = false;
    editor.autocapitalize = "off";
    editor.setAttribute("autocorrect", "off");
    editor.setAttribute("aria-label", `R code of block ${block.index + 1}. Control and Enter runs it.`);
    editor.value = codeOf(block.index);
    editor.rows = Math.min(30, editor.value.split("\n").length + 1);
    let escaped = false;
    editor.addEventListener("keydown", (event) => {
      if (event.key === "Enter" && (event.ctrlKey || event.metaKey)) {
        event.preventDefault();
        run(block);
        return;
      }
      // Tab indents. Escape first, then Tab, leaves the box.
      if (event.key === "Escape") {
        escaped = true;
        return;
      }
      if (event.key === "Tab" && !event.shiftKey && !escaped) {
        event.preventDefault();
        const { selectionStart: start, selectionEnd: end, value } = editor;
        editor.value = value.slice(0, start) + "  " + value.slice(end);
        editor.selectionStart = editor.selectionEnd = start + 2;
        editor.dispatchEvent(new Event("input"));
      }
      escaped = false;
    });
    editor.addEventListener("input", () => {
      block.bar.querySelector(".r-run-reset").hidden = editor.value === block.original;
    });
    block.holder.hidden = true;
    block.holder.after(editor);
    block.editor = editor;
    button.textContent = "Editing";
    button.disabled = true;
    editor.focus();
  }

  function resetEdit(block) {
    if (!block.editor) return;
    block.editor.remove();
    block.editor = null;
    block.holder.hidden = false;
    const button = block.bar.querySelector(".r-run-edit");
    button.textContent = "Edit";
    button.disabled = false;
    block.bar.querySelector(".r-run-reset").hidden = true;
    setStatus(block, "Back to the code on the page.");
  }

  async function run(block) {
    statusBlock = block;
    setBusy(true, block);
    const outcome = await session.run(block.index, {
      status: (kind, detail) => {
        if (kind === "start") setStatus(block, "Starting R in your browser…");
        if (kind === "install") {
          installing = detail;
          downloaded = [];
          setStatus(block, `Installing ${detail.join(", ")} for this page…`);
        }
        if (kind === "run") {
          const target = blocks[detail];
          const status = block.bar.querySelector(".r-run-status");
          status.dataset.kind = "running";
          status.textContent = detail === block.index ? "Running…" : `Running block ${detail + 1} above first…`;
          if (target !== block) {
            target.bar.querySelector(".r-run-status").textContent = "Running…";
          }
        }
        if (kind === "failed") setStatus(block, `R did not start or stopped working: ${detail}. Press Run to try again.`);
        if (kind === "restarted") setStatus(block, "R stopped working and was closed. The next Run starts a fresh R.");
      },
      blockDone: (i, result) => showResult(blocks[i], result),
    });
    if (outcome === "busy") return;
    statusBlock = null;
    setBusy(false, null);
  }

  for (const block of blocks) {
    const bar = document.createElement("div");
    bar.className = "r-run";
    bar.setAttribute("role", "group");
    bar.setAttribute("aria-label", `R block ${block.index + 1}`);
    bar.innerHTML = `<button type="button" class="r-run-go">Run</button>
      <button type="button" class="r-run-edit">Edit</button>
      <button type="button" class="r-run-reset" hidden>Reset</button>
      <button type="button" class="r-run-stop" hidden>Stop R</button>
      <span class="r-run-status" role="status"></span>`;
    block.bar = bar;
    block.holder.after(bar);
    bar.querySelector(".r-run-go").addEventListener("click", () => run(block));
    bar.querySelector(".r-run-edit").addEventListener("click", () => toggleEdit(block));
    bar.querySelector(".r-run-reset").addEventListener("click", () => resetEdit(block));
    bar.querySelector(".r-run-stop").addEventListener("click", () => {
      session.stop();
      statusBlock = null;
      setBusy(false, null);
      setStatus(block, "R stopped. The next Run starts R again and reruns the blocks above.");
    });
  }
  return { session, blocks };
}
