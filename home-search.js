// Homepage search. Uses Quarto's search.json and the same ranker as the search page.
import { documentsFromIndex, rankDocuments, tierOf } from "./search-rank.js";

const form = document.getElementById("home-search");
const input = document.getElementById("home-search-q");
const list = document.getElementById("home-search-results");
const note = document.getElementById("home-search-note");

if (form && input && list && note) {
  note.setAttribute("role", "status");
  note.setAttribute("aria-live", "polite");
  note.setAttribute("aria-atomic", "true");
  const desktop = window.matchMedia("(min-width: 992px)");
  let docs = null;
  let meta = null;
  let shown = [];
  let selected = 0;
  let timer = 0;
  let loading = null;

  function kindOf(href) {
    const path = String(href || "").split("#")[0].replace(/^\//, "");
    if (path.startsWith("labs/")) return "Laboratory";
    if (path.startsWith("questions/")) return "Question";
    if (path.startsWith("reference/")) return "Reference";
    const tier = tierOf(href);
    if (tier === 0) return "Article";
    if (tier === 1) return "Chapter";
    if (tier === 3) return "Figure";
    return "Page";
  }

  function asDocs(payload) {
    return documentsFromIndex(payload)
      .map((doc) => ({
        ...doc,
        href: doc.href || doc.objectID || "",
        title: doc.title || doc.href || doc.objectID || "",
        text: doc.text || "",
      }))
      .filter((doc) => doc.href);
  }

  function load() {
    if (docs) return Promise.resolve();
    if (loading) return loading;
    loading = Promise.all([
      fetch(new URL("search.json", location.href)),
      fetch(new URL("search-aliases.json", location.href)).catch(() => null),
    ]).then(async ([indexRes, aliasRes]) => {
      if (!indexRes.ok) throw new Error("index unavailable");
      docs = asDocs(await indexRes.json());
      meta = aliasRes && aliasRes.ok ? await aliasRes.json() : null;
    });
    return loading;
  }

  function setExpanded(open) {
    input.setAttribute("aria-expanded", open ? "true" : "false");
    list.hidden = !open;
  }

  function choose(index) {
    selected = index;
    const options = list.querySelectorAll("[role='option']");
    options.forEach((option, i) => {
      const on = i === selected;
      option.setAttribute("aria-selected", on ? "true" : "false");
      option.classList.toggle("is-selected", on);
      if (on) option.scrollIntoView({ block: "nearest" });
    });
  }

  function openSelected() {
    const doc = shown[selected] || shown[0];
    if (doc) window.location.href = doc.href;
  }

  function render(query) {
    const q = query.trim();
    list.innerHTML = "";
    shown = [];
    selected = 0;
    if (!q) {
      note.textContent = "Results appear as you type. Arrow keys move, and Enter opens the highlighted result.";
      setExpanded(false);
      return;
    }
    shown = rankDocuments(docs, q, meta).slice(0, 8);
    if (!shown.length) {
      note.textContent = "No pages match.";
      setExpanded(false);
      return;
    }
    note.textContent = shown.length + (shown.length === 1 ? " result." : " results.");
    shown.forEach((doc, i) => {
      const item = document.createElement("li");
      item.className = "home-search-result";
      item.setAttribute("role", "option");
      item.id = "home-search-result-" + i;
      item.setAttribute("aria-selected", i === 0 ? "true" : "false");
      if (i === 0) item.classList.add("is-selected");
      const link = document.createElement("a");
      link.href = doc.href;
      link.textContent = doc.title || doc.href;
      const kind = document.createElement("span");
      kind.className = "search-kind";
      kind.textContent = kindOf(doc.href);
      item.append(link, kind);
      item.addEventListener("mousemove", () => choose(i));
      list.appendChild(item);
    });
    input.setAttribute("aria-activedescendant", "home-search-result-0");
    setExpanded(true);
  }

  async function schedule() {
    window.clearTimeout(timer);
    timer = window.setTimeout(async () => {
      try {
        await load();
      } catch (_err) {
        note.textContent = "The search index is not available.";
        setExpanded(false);
        return;
      }
      render(input.value);
    }, 40);
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!shown.length) {
      schedule();
      return;
    }
    openSelected();
  });

  input.addEventListener("input", schedule);
  input.addEventListener("keydown", (event) => {
    if (event.key === "ArrowDown" || event.key === "ArrowUp") {
      if (!shown.length) return;
      event.preventDefault();
      const next = event.key === "ArrowDown"
        ? Math.min(shown.length - 1, selected + 1)
        : Math.max(0, selected - 1);
      choose(next);
      input.setAttribute("aria-activedescendant", "home-search-result-" + next);
    } else if (event.key === "Enter") {
      if (!shown.length) return;
      event.preventDefault();
      openSelected();
    } else if (event.key === "Escape") {
      setExpanded(false);
      note.textContent = "";
    }
  });

  if (desktop.matches) input.focus();
  note.textContent = "Results appear as you type. Arrow keys move, and Enter opens the highlighted result.";
}
