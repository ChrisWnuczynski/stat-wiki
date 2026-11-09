// Shared laboratory chrome for a Quarto page.
//
// A lab imports this module and uses controlRow, graphFrame, readoutLine,
// and markerLegend. watchTheme and themeInk follow the wiki light and dark
// tokens (--wiki-text, --wiki-panel, and the rest). Statistics stay in the
// lab's own module.

const STYLE_ID = "lab-chrome";

const CSS = `
body:has([data-lab-page]) #quarto-document-content {
  max-width: 70rem;
}

.control-row {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  gap: 0.45rem 0.75rem;
  margin: 0.2rem 0 0;
  padding: 0.55rem 0.75rem 0.6rem;
  background: var(--wiki-panel);
  border: 1px solid var(--wiki-border);
  color: var(--wiki-text);
  color-scheme: light;
}

body.quarto-dark .control-row {
  color-scheme: dark;
}

.control-field {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  flex: 1 1 9rem;
  min-width: 0;
  margin: 0;
  font-size: 0.82rem;
  color: var(--wiki-muted);
}

.control-field-wide {
  flex: 2 1 14rem;
}

.control-field-fixed {
  flex: 0 0 6.5rem;
}

.control-field > span:first-child {
  font-weight: 650;
  letter-spacing: 0.01em;
}

.control-slider {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  width: 100%;
  min-width: 0;
}

.control-slider input[type="range"] {
  flex: 1 1 auto;
  width: auto;
  min-width: 2.5rem;
  accent-color: var(--wiki-link);
}

.control-field > input,
.control-field > select,
.control-slider input[type="number"] {
  background: var(--wiki-bg);
  color: var(--wiki-text);
  border: 1px solid var(--wiki-border);
  border-radius: 2px;
  padding: 0.22rem 0.4rem;
  font: inherit;
  font-size: 0.95rem;
}

.control-field > input,
.control-field > select {
  width: 100%;
  min-width: 0;
}

.control-slider input[type="number"] {
  flex: 0 0 5.5rem;
  width: 5.5rem;
}

.control-slider output {
  min-width: 2.2rem;
  color: var(--wiki-text);
  font-size: 0.95rem;
  font-variant-numeric: tabular-nums;
}

.control-actions,
.control-toggles {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.35rem 0.7rem;
  margin: 0;
}

.control-actions { flex: 0 1 auto; }
.control-toggles { flex: 1 1 14rem; }

.control-row button {
  font: inherit;
  font-size: 0.9rem;
  color: var(--wiki-text);
  background: var(--wiki-bg);
  border: 1px solid var(--wiki-border);
  border-radius: 2px;
  padding: 0.28rem 0.6rem;
  cursor: pointer;
}

.control-row button:hover {
  background: var(--wiki-panel-head);
}

.control-toggles label {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  margin: 0;
  color: var(--wiki-text);
  font-size: 0.9rem;
}

.control-row :focus-visible {
  outline: 2px solid var(--wiki-link);
  outline-offset: 2px;
}

.control-hint {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.control-note {
  flex: 1 0 100%;
  margin: 0;
  color: #9a3412;
  font-size: 0.85rem;
}

.control-note:empty {
  display: none;
}

body.quarto-dark .control-note,
body.quarto-dark .graph-alert {
  color: #f0b7a4;
}

.readout-line {
  display: flex;
  flex-wrap: nowrap;
  gap: 0.15rem 0.85rem;
  margin: 0.4rem 0 0.1rem;
  padding: 0.1rem 0.05rem 0.4rem;
  overflow-x: auto;
  border-bottom: 1px solid var(--wiki-rule);
  color: var(--wiki-muted);
  font-size: 0.86rem;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}

.readout-label {
  margin-right: 0.28rem;
}

.readout-line b {
  color: var(--wiki-text);
  font-weight: 650;
}

.readout-line:has(.graph-alert) {
  flex-wrap: wrap;
  white-space: normal;
}

.graph-frame {
  margin: 0.85rem 0 0.3rem;
  padding: 0;
  max-width: 100%;
}

.graph-title {
  margin: 0 0 0.3rem;
  color: var(--wiki-text);
  font-family: "Linux Libertine", Georgia, "Times New Roman", serif;
  font-size: 1.35rem;
  font-weight: normal;
  line-height: 1.2;
}

.graph-plot {
  overflow-x: auto;
  max-width: 100%;
  background: var(--wiki-bg);
  border: 1px solid var(--wiki-border);
  border-radius: 2px;
}

.graph-plot svg {
  display: block;
  max-width: 100%;
  height: auto;
  background: transparent;
}

.graph-alert,
.graph-note {
  margin: 0.45rem 0 0;
  font-size: 0.9rem;
}

.graph-alert {
  color: #9a3412;
  font-weight: 650;
}

.readout-line .graph-alert {
  flex-basis: 100%;
  margin: 0.15rem 0 0;
}

.graph-note {
  color: var(--wiki-muted);
  font-weight: normal;
}

.legend-row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.25rem 0.9rem;
  list-style: none;
  margin: 0.4rem 0 0;
  padding: 0;
  color: var(--wiki-muted);
  font-size: 0.88rem;
}

.legend-row li {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

.legend-swatch,
.legend-tick,
.legend-rug {
  flex: 0 0 auto;
  align-self: center;
}

.legend-swatch {
  width: 1.15rem;
  height: 0;
  border-top: 3px solid currentColor;
}

.legend-tick {
  width: 2px;
  height: 0.85rem;
  background: currentColor;
}

.legend-rug {
  width: 2px;
  height: 0.7rem;
  background: currentColor;
}

@media (max-width: 767px) {
  .control-field,
  .control-field-wide,
  .control-field-fixed,
  .control-actions,
  .control-toggles {
    flex: 1 1 100%;
  }

  .readout-line {
    flex-wrap: wrap;
    white-space: normal;
  }
}

@media (prefers-reduced-motion: reduce) {
  .control-row,
  .control-row *,
  .graph-plot,
  .graph-plot * {
    transition: none !important;
    animation: none !important;
    scroll-behavior: auto !important;
  }
}
`;

export function installLabChrome() {
  if (typeof document === "undefined" || document.getElementById(STYLE_ID)) return;
  const style = document.createElement("style");
  style.id = STYLE_ID;
  style.textContent = CSS;
  document.head.appendChild(style);
}

function painted() {
  installLabChrome();
}

// Wiki ink for plots. Custom properties live on the page theme, so a later
// lab does not keep its own copy of the light and dark hexes.
export function themeInk() {
  const style = getComputedStyle(document.body);
  const pick = (name, fallback) => style.getPropertyValue(name).trim() || fallback;
  const dark = document.body.classList.contains("quarto-dark");
  return {
    dark,
    text: pick("--wiki-text", dark ? "#eaecf0" : "#202122"),
    muted: pick("--wiki-muted", dark ? "#a2a9b1" : "#54595d"),
    link: pick("--wiki-link", dark ? "#88a3e8" : "#3366cc"),
    border: pick("--wiki-border", dark ? "#54595d" : "#a2a9b1"),
    panel: pick("--wiki-panel", dark ? "#1b1e22" : "#f8f9fa"),
    bg: pick("--wiki-bg", dark ? "#101418" : "#ffffff"),
  };
}

// notify receives true when the wiki is in the dark theme. Returns a cleanup.
export function watchTheme(notify) {
  const read = () => document.body.classList.contains("quarto-dark");
  const observer = new MutationObserver(() => notify(read()));
  observer.observe(document.body, { attributes: true, attributeFilter: ["class"] });
  notify(read());
  return () => observer.disconnect();
}

export function controlRow(label) {
  painted();
  const form = document.createElement("form");
  form.className = "control-row";
  form.setAttribute("aria-label", label);
  form.addEventListener("submit", (event) => event.preventDefault());
  return form;
}

export function graphFrame(title) {
  painted();
  const section = document.createElement("section");
  section.className = "graph-frame";
  const heading = document.createElement("p");
  heading.className = "graph-title";
  heading.textContent = title;
  const plot = document.createElement("div");
  plot.className = "graph-plot";
  section.append(heading, plot);
  return { section, heading, plot };
}

// entries: { label, value, title? }
export function readoutLine(entries) {
  painted();
  const root = document.createElement("div");
  root.className = "readout-line";
  for (const entry of entries) {
    const item = document.createElement("span");
    if (entry.title) item.title = entry.title;
    const label = document.createElement("span");
    label.className = "readout-label";
    label.textContent = entry.label;
    const value = document.createElement("b");
    value.textContent = entry.value;
    item.append(label, value);
    root.appendChild(item);
  }
  return root;
}

// items: { text, color, kind: "line" | "tick" | "rug", dash?: "dashed" | "dotted" }
export function markerLegend(items) {
  painted();
  const list = document.createElement("ul");
  list.className = "legend-row";
  for (const item of items) {
    const li = document.createElement("li");
    const mark = document.createElement("span");
    mark.setAttribute("aria-hidden", "true");
    mark.className = item.kind === "line" ? "legend-swatch" : item.kind === "rug" ? "legend-rug" : "legend-tick";
    mark.style.color = item.color;
    if (item.kind === "line" && item.dash) mark.style.borderTopStyle = item.dash;
    li.append(mark, document.createTextNode(item.text));
    list.appendChild(li);
  }
  return list;
}
