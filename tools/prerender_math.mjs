// Replace Quarto's raw TeX spans with KaTeX HTML and MathML before the page
// is served. The stylesheet stays. The client render script is removed, so a
// browser with JavaScript off still shows the formula and a screen reader
// still gets MathML. Quarto's own typesetMath is left in place but skips a
// span that already contains MathML, so a later hover preview cannot wipe it.

import { createRequire } from "node:module";
import { readFileSync, writeFileSync, readdirSync, statSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, "..");
const require = createRequire(import.meta.url);
const katex = require(join(root, "katex", "katex.min.js"));
const macros = JSON.parse(readFileSync(join(root, "katex_macros.json"), "utf8"));

function siteFromArgs(argv) {
  const flag = argv.indexOf("--site");
  if (flag >= 0 && argv[flag + 1]) return argv[flag + 1];
  return join(root, "_site");
}

function walk(dir, out) {
  for (const name of readdirSync(dir)) {
    const path = join(dir, name);
    if (name === "site_libs") continue;
    const info = statSync(path);
    if (info.isDirectory()) walk(path, out);
    else if (name.endsWith(".html")) out.push(path);
  }
  return out;
}

function decode(text) {
  return text
    .replace(/&#x([0-9a-f]+);/gi, (_, hex) => String.fromCodePoint(parseInt(hex, 16)))
    .replace(/&#(\d+);/g, (_, dec) => String.fromCodePoint(Number(dec)))
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'")
    .replace(/&#39;/g, "'")
    .replace(/&amp;/g, "&");
}

function classOf(openTag) {
  const match = /class\s*=\s*"([^"]*)"/i.exec(openTag);
  return match ? match[1] : "";
}

// Depth-matched spans. A rendered formula contains nested spans, so the first
// </span> is not the end of the math span.
function mathSpans(html) {
  const opener = /<span\b[^>]*\bclass="[^"]*\bmath\b[^"]*"[^>]*>/gi;
  const found = [];
  let match;
  while ((match = opener.exec(html))) {
    const start = match.index;
    const openEnd = start + match[0].length;
    let depth = 1;
    let cursor = openEnd;
    let close = -1;
    while (cursor < html.length && depth > 0) {
      const nextOpen = html.indexOf("<span", cursor);
      const nextClose = html.indexOf("</span>", cursor);
      if (nextClose < 0) break;
      if (nextOpen >= 0 && nextOpen < nextClose) {
        depth += 1;
        cursor = nextOpen + 5;
      } else {
        depth -= 1;
        if (depth === 0) close = nextClose;
        cursor = nextClose + 7;
      }
    }
    if (close >= 0) found.push({ start, openEnd, close, end: close + 7, open: match[0] });
  }
  return found;
}

function renderInner(openTag, inner) {
  if (inner.includes('class="katex"') || /<math[\s>]/.test(inner)) return null;
  const tex = decode(inner)
    .trim()
    .replace(/^\\\(([\s\S]*)\\\)$/, "$1")
    .replace(/^\\\[([\s\S]*)\\\]$/, "$1")
    .trim();
  if (!tex) return null;
  const display = /\bdisplay\b/.test(classOf(openTag));
  return katex.renderToString(tex, {
    displayMode: display,
    throwOnError: true,
    output: "htmlAndMathml",
    strict: "ignore",
    macros,
    fleqn: false,
  });
}

function stripAutoload(html) {
  const pattern = /<script\b[^>]*>\s*document\.addEventListener\("DOMContentLoaded", function \(\) \{\s*var mathElements = document\.getElementsByClassName\("math"\);[\s\S]*?katex\.render\([\s\S]*?<\/script>/gi;
  const next = html.replace(pattern, "");
  if (/document\.addEventListener\("DOMContentLoaded", function \(\) \{\s*var mathElements = document\.getElementsByClassName\("math"\)/.test(next)) {
    throw new Error("The KaTeX autoload script is still in the page");
  }
  return next;
}

function guardTypeset(html) {
  const needle = 'if (mathElements[i].tagName == "SPAN")';
  const guard = 'if (mathElements[i].tagName == "SPAN" && texText && texText.nodeType === 3 && !mathElements[i].querySelector(".katex, math"))';
  if (!html.includes(needle)) {
    // A second run has already rewritten the test. An unguarded call would
    // still match the shorter pattern and wipe the MathML once KaTeX loads.
    if (/tagName == "SPAN"\) \{\s*(?:window\.)?katex\.render/.test(html)) {
      throw new Error("Quarto's typesetMath no longer matches the expected guard point");
    }
    return html;
  }
  return html.replaceAll(needle, guard);
}

function dropKatexScript(html) {
  const pattern = /<script\b[^>]*\bsrc="[^"]*katex\.min\.js"[^>]*>\s*<\/script>/gi;
  const next = html.replace(pattern, "");
  if (/src="[^"]*katex\.min\.js"/.test(next)) {
    throw new Error("katex.min.js is still loaded by the page");
  }
  return next;
}

export function prerenderHtml(html) {
  const failures = [];
  const spans = mathSpans(html);
  let rendered = 0;
  // Right to left, so an earlier span's offsets stay valid.
  for (let i = spans.length - 1; i >= 0; i -= 1) {
    const span = spans[i];
    const inner = html.slice(span.openEnd, span.close);
    try {
      const replacement = renderInner(span.open, inner);
      if (replacement == null) continue;
      html = html.slice(0, span.openEnd) + replacement + html.slice(span.close);
      rendered += 1;
    } catch (error) {
      const tex = decode(inner).trim().replace(/\s+/g, " ").slice(0, 140);
      failures.push(`${error.message} :: ${tex}`);
    }
  }
  if (!failures.length) {
    html = dropKatexScript(guardTypeset(stripAutoload(html)));
  }
  return { html, rendered, failures };
}

function main() {
  const site = siteFromArgs(process.argv);
  const pages = walk(site, []);
  let changed = 0;
  let rendered = 0;
  const problems = [];
  for (const path of pages) {
    const original = readFileSync(path, "utf8");
    if (original.includes("<title>Redirect</title>") && original.includes("var redirects")) continue;
    if (!original.includes('class="math') && !original.includes("katex.min.js")) continue;
    const result = prerenderHtml(original);
    rendered += result.rendered;
    if (result.failures.length) {
      for (const failure of result.failures.slice(0, 8)) problems.push(`${path}: ${failure}`);
      continue;
    }
    if (result.html !== original) {
      writeFileSync(path, result.html);
      changed += 1;
    }
  }
  console.log(`Pre-rendered ${rendered} formulae on ${changed} pages (KaTeX ${katex.version}, htmlAndMathml)`);
  if (problems.length) {
    console.error(problems.slice(0, 30).join("\n"));
    process.exit(1);
  }
}

const invoked = process.argv[1] ? pathToFileURL(process.argv[1]).href : "";
if (invoked === import.meta.url) main();
