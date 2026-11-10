// Run every R block of the Using R chapters in webR, page by page, the way a
// reader's browser does: the same page session (session.js), the same engine
// (engine.js), and the same explanations under a block that fails.
//
// Each page gets a fresh R, as a browser tab does, and Run is pressed on its
// last block, so every block above runs first, in order. Plots go to a null
// device here; the browser draws them with webr::canvas.
//
// A block that fails with an explanation is one the browser cannot run (a
// package that is not available for webR, a file on the reader's computer)
// and the reader is told why. A block that fails without one is a problem
// to fix, and the check exits with status 1.
//
// Needs network access to webR's package repository (repo.r-wasm.org).
// Whether a package is available is read from that repository's index, so a
// download that fails is a failure, not a missing package. Behind a proxy,
// set NODE_USE_ENV_PROXY=1: R's downloads go through a local pass-through to
// the repository, which uses Node's fetch.
//
//   cd webr && npm ci
//   node check-blocks.mjs                 every Using R chapter
//   node check-blocks.mjs ur-02 ur-05     chapters whose file name contains these
//   node check-blocks.mjs --out runs/x.json

import { mkdirSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { createServer } from "node:http";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";
import { WebR } from "webr";
import { rBlocks } from "./blocks.js";
import { webREngine } from "./engine.js";
import { BASE_PACKAGES, packagesForBlocks } from "./packages.js";
import { PageSession } from "./session.js";
import { WEBR_VERSION } from "./version.js";

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, "..");
const BLOCK_SECONDS = 240;
const REPO = "https://repo.r-wasm.org/";

function chapters() {
  const using = join(root, "sources", "using-r", "chapters");
  const files = readdirSync(using).filter((name) => name.endsWith(".qmd")).sort().map((name) => join(using, name));
  return [join(root, "sources", "stat1301", "chapters", "da-03-using-r.qmd"), ...files];
}

function parseArgs(argv) {
  const filters = [];
  let out = join(here, "runs", `${new Date().toISOString().slice(0, 10)}.json`);
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === "--out") out = join(process.cwd(), argv[++i]);
    else filters.push(argv[i]);
  }
  return { filters, out };
}

// A local server that fetches each requested path from the repository.
// R inside webR then needs no proxy settings of its own.
async function startMirror() {
  const server = createServer(async (request, response) => {
    try {
      const upstream = await fetch(new URL(request.url.replace(/^\/+/, ""), REPO));
      response.writeHead(upstream.status, { "content-type": upstream.headers.get("content-type") ?? "application/octet-stream" });
      response.end(Buffer.from(await upstream.arrayBuffer()));
    } catch (error) {
      response.writeHead(502);
      response.end(String(error));
    }
  });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  return { server, url: `http://127.0.0.1:${server.address().port}/` };
}

// Package names in the repository index for this R version, with their
// dependencies, so a package whose dependency is missing also counts as missing.
async function repoIndex(rVersion) {
  const url = new URL(`bin/emscripten/contrib/${rVersion}/PACKAGES`, REPO);
  const response = await fetch(url);
  if (!response.ok) throw new Error(`could not read ${url} (${response.status})`);
  const index = new Map();
  for (const record of (await response.text()).split(/\n\s*\n/)) {
    const name = record.match(/^Package:\s*(\S+)/m)?.[1];
    if (!name) continue;
    const field = (key) => record.match(new RegExp(`^${key}:\\s*([\\s\\S]*?)(?=\\n\\S|$)`, "m"))?.[1] ?? "";
    const deps = [field("Depends"), field("Imports"), field("LinkingTo")].join(",")
      .split(",").map((item) => item.trim().split(/[\s(]/)[0]).filter((item) => item && item !== "R");
    index.set(name, deps);
  }
  if (index.size < 1000) throw new Error(`the index at ${url} lists only ${index.size} packages`);
  return index;
}

function missingFrom(index, wanted) {
  const missing = [];
  const seen = new Set();
  const visit = (name, top) => {
    if (seen.has(name + " " + top) || BASE_PACKAGES.has(name)) return;
    seen.add(name + " " + top);
    if (!index.has(name)) {
      if (!missing.includes(top)) missing.push(top);
      return;
    }
    for (const dep of index.get(name)) visit(dep, top);
  };
  for (const name of wanted) visit(name, name);
  return missing;
}

async function checkPage(file, mirror) {
  const blocks = rBlocks(readFileSync(file, "utf8"));
  const page = { file: relative(root, file).replaceAll("\\", "/"), blocks: [], packages: packagesForBlocks(blocks) };
  page.notInRepository = missingFrom(mirror.index, page.packages);
  if (blocks.length === 0) return page;
  // A block that faulted R is not run again on the pass after the restart.
  const skip = new Set();
  const session = new PageSession({
    codeOf: (i) => (skip.has(i) ? "invisible(NULL)" : blocks[i]),
    count: blocks.length,
    startEngine: () => webREngine({
      WebR,
      options: { repoUrl: mirror.url },
      setup: `options(device = function(...) grDevices::pdf(NULL), repos = c(webr = "${mirror.url}"), webr_pkg_repos = "${mirror.url}")`,
      timeoutMs: BLOCK_SECONDS * 1000,
    }),
  });
  let installStarted = 0;
  // Press Run on the last block. A fault in R restarts it, so press again
  // until every block has a result.
  for (let attempt = 0; attempt < blocks.length && page.blocks.length < blocks.length; attempt++) {
    const outcome = await session.run(blocks.length - 1, {
      status: (kind, detail) => {
        if (kind === "install") {
          installStarted = Date.now();
          page.installed = detail;
        }
        if (kind === "run" && installStarted) {
          page.installMs = Date.now() - installStarted;
          installStarted = 0;
        }
        if (kind === "failed") page.startError = detail;
      },
      blockDone: (i, result) => {
        if (page.blocks.some((row) => row.block === i + 1)) return;
        const row = {
          block: i + 1,
          ms: result.ms,
          ok: !result.error,
          plots: result.images.length,
          first: blocks[i].split("\n")[0].slice(0, 90),
        };
        if (result.error) {
          row.error = result.error.slice(0, 400);
          row.explanation = result.explanation;
          row.fatal = Boolean(result.fatal);
        }
        const warnings = result.items.filter((item) => item.kind === "warning").map((item) => item.text);
        if (warnings.length) row.warnings = warnings;
        page.blocks.push(row);
        const mark = row.ok ? "ok  " : row.explanation ? "note" : "FAIL";
        console.log(`  ${mark} block ${row.block} (${row.ms} ms) ${row.first}`);
        if (!row.ok) console.log(`       ${row.error.split("\n")[0].slice(0, 200)}\n       ${row.explanation ?? "(no explanation)"}`);
      },
    });
    if (outcome === "stopped") break;
    if (outcome === "done") break;
    // "restarted": the next pass reruns the blocks above and continues after the fault.
    // A block that already has a result keeps its first result.
    for (const row of page.blocks) if (row.fatal) skip.add(row.block - 1);
  }
  session.stop();
  page.blocks.sort((a, b) => a.block - b.block);
  return page;
}

const { filters, out } = parseArgs(process.argv.slice(2));
const files = chapters().filter((file) => filters.length === 0 || filters.some((f) => file.includes(f)));
const probe = new WebR();
await probe.init();
const rVersion = await probe.evalRString("paste(R.version$major, sub('[.].*', '', R.version$minor), sep = '.')");
const rString = await probe.evalRString("R.version.string");
probe.close();
const mirror = await startMirror();
mirror.index = await repoIndex(rVersion);
const report = { webr: WEBR_VERSION, r: rString, date: new Date().toISOString(), pages: [] };
for (const file of files) {
  console.log(relative(root, file));
  const page = await checkPage(file, mirror);
  if (page.notInRepository.length) console.log(`  not in the webR repository: ${page.notInRepository.join(", ")}`);
  report.pages.push(page);
}
mirror.server.close();
const all = report.pages.flatMap((page) => page.blocks);
const expected = report.pages.reduce((sum, page) => sum + rBlocks(readFileSync(join(root, page.file), "utf8")).length, 0);
report.summary = {
  blocks: expected,
  ok: all.filter((b) => b.ok).length,
  explained: all.filter((b) => !b.ok && b.explanation).length,
  failed: all.filter((b) => !b.ok && !b.explanation).length,
  noResult: expected - all.length,
};
mkdirSync(dirname(out), { recursive: true });
writeFileSync(out, JSON.stringify(report, null, 2) + "\n");
console.log(JSON.stringify(report.summary));
console.log(`Saved ${relative(process.cwd(), out)}`);
process.exit(report.summary.failed || report.summary.noResult ? 1 : 0);
