// Which R packages a block of R code needs.
// No DOM and no webR. The runner and the block check both import this module.
//
// A package is needed when the code names it as pkg::name or pkg:::name,
// loads it with library(), require(), requireNamespace() or loadNamespace(),
// or passes its name as package = "pkg", as in data("Orthodont", package = "nlme").
// Comments are ignored. Text inside a string is ignored, except the package
// name given as a string to one of the loading functions.
// Packages that ship with R are not reported: webR already has them.

export const BASE_PACKAGES = new Set([
  "base",
  "compiler",
  "datasets",
  "graphics",
  "grDevices",
  "grid",
  "methods",
  "parallel",
  "splines",
  "stats",
  "stats4",
  "tcltk",
  "tools",
  "utils",
  "webr",
]);

const NAME = "[A-Za-z][A-Za-z0-9.]*[A-Za-z0-9]";

// The code with comments removed and the inside of every string blanked.
// Quote characters stay, so positions and token boundaries do not move.
// strings lists each string's contents with its start offset.
export function scan(code) {
  let out = "";
  const strings = [];
  let i = 0;
  while (i < code.length) {
    const ch = code[i];
    if (ch === "#") {
      while (i < code.length && code[i] !== "\n") {
        out += " ";
        i++;
      }
      continue;
    }
    if (ch === '"' || ch === "'" || ch === "`") {
      const start = i;
      out += ch;
      i++;
      let body = "";
      while (i < code.length && code[i] !== ch) {
        if (code[i] === "\\" && i + 1 < code.length) {
          body += code[i] + code[i + 1];
          out += code[i + 1] === "\n" ? " \n" : "  ";
          i += 2;
          continue;
        }
        body += code[i];
        out += code[i] === "\n" ? "\n" : " ";
        i++;
      }
      if (i < code.length) {
        out += ch;
        i++;
      }
      strings.push({ start, quote: ch, body });
      continue;
    }
    out += ch;
    i++;
  }
  return { code: out, strings };
}

// Packages named in the code, in order of first appearance, base packages removed.
export function packagesIn(code) {
  if (typeof code !== "string" || code === "") return [];
  const { code: bare, strings } = scan(code);
  const found = [];
  const add = (name) => {
    if (!name || BASE_PACKAGES.has(name) || found.includes(name)) return;
    found.push(name);
  };
  const hits = [];
  const colon = new RegExp(`(?<![A-Za-z0-9._])(${NAME}):::?`, "g");
  for (const match of bare.matchAll(colon)) hits.push({ at: match.index, name: match[1] });
  // library(dplyr), library("dplyr"), require(pkg = "x") and the namespace loaders.
  const loader = /(?<![A-Za-z0-9._])(library|require|requireNamespace|loadNamespace)\s*\(/g;
  for (const match of bare.matchAll(loader)) {
    const open = match.index + match[0].length;
    const close = bare.indexOf(")", open);
    const args = bare.slice(open, close < 0 ? bare.length : close);
    if (/character\.only\s*=\s*(TRUE|T)\b/.test(args)) continue;
    const first = args.replace(/^\s*(package\s*=\s*)?/, "");
    const offset = open + (args.length - first.length);
    const quoted = strings.find((item) => item.start === offset);
    if (quoted) {
      if (new RegExp(`^${NAME}$`).test(quoted.body)) hits.push({ at: offset, name: quoted.body });
      continue;
    }
    const bareName = first.match(new RegExp(`^(${NAME})\\s*(,|$)`));
    if (bareName) hits.push({ at: offset, name: bareName[1] });
  }
  // package = "nlme" in data(), system.file(), help() and the like.
  const named = /(?<![A-Za-z0-9._])package\s*=\s*/g;
  for (const match of bare.matchAll(named)) {
    const offset = match.index + match[0].length;
    const quoted = strings.find((item) => item.start === offset);
    if (quoted && new RegExp(`^${NAME}$`).test(quoted.body)) hits.push({ at: offset, name: quoted.body });
  }
  hits.sort((a, b) => a.at - b.at);
  for (const hit of hits) add(hit.name);
  return found;
}

// Every package needed by a list of blocks, in order of first appearance.
export function packagesForBlocks(blocks) {
  const found = [];
  for (const block of blocks) {
    for (const name of packagesIn(block)) {
      if (!found.includes(name)) found.push(name);
    }
  }
  return found;
}

// What a reader is told when a block fails for a reason the browser causes.
// Returns null when the error is an ordinary R error the reader can fix.
//   unavailable   packages this session tried to install that still do not load
//   earlierFailed the number of a block above that failed in this session, or null
//   fatal         R itself faulted (a WebAssembly error), so it restarts
export function browserExplanation(message, { unavailable = [], earlierFailed = null, fatal = false } = {}) {
  const text = String(message || "");
  if (fatal) {
    return "R stopped working in the browser: compiled code in a package this block uses does not run in the browser build of R. The block runs in R or RStudio on a computer. The next Run starts a fresh R.";
  }
  for (const name of unavailable) {
    if (text.includes(`'${name}'`) || text.includes(`"${name}"`) || text.includes(`‘${name}’`)) {
      return `The ${name} package is not available for R in the browser, so this block cannot run here. It runs in R or RStudio on a computer.`;
    }
  }
  const absent = text.match(/there is no package called [‘'"]([^’'"]+)[’'"]/);
  if (absent) {
    return `The ${absent[1]} package is not installed in this browser session. Run install.packages("${absent[1]}") in an edited block, then run this block again.`;
  }
  if (/cannot open (file|the connection)|does not exist in current working directory|No such file or directory/i.test(text)) {
    return "This block reads a file from your own computer. The browser has no copy of it, so the error is expected here. Run it in R with the path to your file.";
  }
  if (earlierFailed !== null && /object '[^']+' not found|could not find function|object ‘[^’]+’ not found/.test(text)) {
    return `Block ${earlierFailed} above did not run in the browser, and this block uses something it makes.`;
  }
  return null;
}
