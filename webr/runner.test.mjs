// Node test for the page session, with a stand-in engine. No webR, no browser.

import assert from "node:assert/strict";
import test from "node:test";
import { rBlocks } from "./blocks.js";
import { PageSession } from "./session.js";
import { WEBR_BASE, WEBR_VERSION } from "./version.js";
import { readFileSync } from "node:fs";

function fakeEngine(log, { fail = {}, missing = [], hang = null } = {}) {
  return {
    async install(names) {
      log.push(["install", names]);
      return { missing: names.filter((name) => missing.includes(name)) };
    },
    async run(code) {
      log.push(["run", code]);
      if (hang && code === hang.code) await hang.promise;
      if (fail[code]) return { items: [], images: [], error: fail[code] };
      return { items: [{ kind: "out", text: `ran ${code}` }], images: [], error: null };
    },
    close() {
      log.push(["close"]);
    },
  };
}

function session(codes, engineOptions) {
  const log = [];
  let starts = 0;
  const s = new PageSession({
    codeOf: (i) => codes[i],
    count: codes.length,
    startEngine: async () => {
      starts++;
      log.push(["start"]);
      return fakeEngine(log, engineOptions);
    },
  });
  return { s, log, starts: () => starts };
}

test("Run on a later block runs the blocks above it first, once", async () => {
  const { s, log } = session(["a <- 1", "b <- a", "c <- b"]);
  const done = [];
  assert.equal(await s.run(2, { blockDone: (i, r) => done.push([i, r.earlier]) }), "done");
  assert.deepEqual(done, [[0, true], [1, true], [2, false]]);
  assert.deepEqual(log.filter(([k]) => k === "run").map(([, c]) => c), ["a <- 1", "b <- a", "c <- b"]);
  log.length = 0;
  await s.run(2);
  assert.deepEqual(log, [["run", "c <- b"]]);
  assert.deepEqual(s.plan(1), [1]);
});

test("packages are installed once, before any block runs, and only those named", async () => {
  const { s, log } = session(["x <- dplyr::n()", "ggplot2::ggplot(); dplyr::n()", "stats::lm(y ~ x)"]);
  await s.run(1);
  assert.deepEqual(log.slice(0, 2), [["start"], ["install", ["dplyr", "ggplot2"]]]);
  log.length = 0;
  await s.run(2);
  assert.deepEqual(log, [["run", "stats::lm(y ~ x)"]]);
});

test("an earlier block that fails does not stop the blocks after it", async () => {
  const fail = { 'readr::read_csv("data/m.csv")': "'data/m.csv' does not exist in current working directory ('/home/web_user')." };
  const { s } = session(["a <- 1", 'readr::read_csv("data/m.csv")', "a + 1"], { fail });
  const results = [];
  assert.equal(await s.run(2, { blockDone: (i, r) => results.push([i, r.error ? "error" : "ok", r.explanation]) }), "done");
  assert.equal(results.length, 3);
  assert.equal(results[1][1], "error");
  assert.match(results[1][2], /file from your own computer/);
  assert.deepEqual(results[2], [2, "ok", null]);
});

test("a package missing from webR is explained, and not tried again", async () => {
  const fail = { "mclust::Mclust(x)": "there is no package called ‘mclust’" };
  const { s, log } = session(["mclust::Mclust(x)"], { fail, missing: ["mclust"] });
  let result;
  await s.run(0, { blockDone: (_, r) => (result = r) });
  assert.match(result.explanation, /mclust package is not available for R in the browser/);
  log.length = 0;
  await s.run(0);
  assert.deepEqual(log, [["run", "mclust::Mclust(x)"]]);
});

test("Stop closes R, drops what ran, and the next Run starts again from the top", async () => {
  let release;
  const hang = { code: "while (TRUE) {}", promise: new Promise((resolve) => (release = resolve)) };
  const { s, log, starts } = session(["a <- 1", "while (TRUE) {}", "a"], { hang });
  const running = s.run(1);
  await new Promise((resolve) => setTimeout(resolve, 5));
  assert.equal(await s.run(2), "busy");
  s.stop();
  release();
  assert.equal(await running, "stopped");
  assert.ok(log.some(([k]) => k === "close"));
  assert.equal(s.ran.size, 0);
  log.length = 0;
  assert.equal(await s.run(2), "done");
  assert.equal(starts(), 2);
  assert.deepEqual(log.filter(([k]) => k === "run").map(([, c]) => c), ["a <- 1", "while (TRUE) {}", "a"]);
});

test("a block that fails because a block above failed says so", async () => {
  const fail = { "mclust::Mclust(x)": "there is no package called ‘mclust’", "best <- fit": "Error: object 'fit' not found" };
  const { s } = session(["x <- 1", "mclust::Mclust(x)", "best <- fit"], { fail, missing: ["mclust"] });
  const notes = [];
  await s.run(2, { blockDone: (i, r) => notes.push(r.explanation) });
  assert.equal(notes[0], null);
  assert.match(notes[1], /not available for R in the browser/);
  assert.match(notes[2], /Block 2 above did not run/);
});

test("a WebAssembly fault in R closes it, and the next Run starts again", async () => {
  const log = [];
  let starts = 0;
  const s = new PageSession({
    codeOf: (i) => ["a <- 1", "crash()", "a"][i],
    count: 3,
    startEngine: async () => {
      starts++;
      const engine = fakeEngine(log);
      const run = engine.run;
      engine.run = async (code) => (code === "crash()" && starts === 1
        ? { items: [], images: [], error: "null function or function signature mismatch", fatal: true }
        : run(code));
      return engine;
    },
  });
  const seen = [];
  assert.equal(await s.run(2, { blockDone: (i, r) => seen.push([i, r.explanation]) }), "restarted");
  assert.deepEqual(seen.map(([i]) => i), [0, 1]);
  assert.match(seen[1][1], /fresh R/);
  assert.ok(log.some(([k]) => k === "close"));
  assert.equal(s.ran.size, 0);
  assert.equal(await s.run(2), "done");
  assert.equal(starts, 2);
});

test("edited code is what runs, for the block and for the blocks above", async () => {
  const codes = ["a <- 1", "a"];
  const { s, log } = session(codes);
  codes[0] = "a <- 2";
  await s.run(1);
  assert.deepEqual(log.filter(([k]) => k === "run").map(([, c]) => c), ["a <- 2", "a"]);
});

test("R that fails to start is reported and the next Run tries again", async () => {
  let starts = 0;
  const s = new PageSession({
    codeOf: () => "1",
    count: 1,
    startEngine: async () => {
      starts++;
      if (starts === 1) throw new Error("network");
      return fakeEngine([]);
    },
  });
  const seen = [];
  assert.equal(await s.run(0, { status: (kind, detail) => seen.push([kind, detail]) }), "stopped");
  assert.deepEqual(seen.at(-1), ["failed", "network"]);
  assert.equal(await s.run(0), "done");
});

test("a block index outside the page is an error", async () => {
  const { s } = session(["1"]);
  await assert.rejects(() => s.run(1), /no block 1/);
  await assert.rejects(() => s.run(-1), /no block -1/);
});

test("the R blocks of a chapter are read in order, and untagged fences are not R", () => {
  const source = "Text\n\n```r\na <- 1\n```\n\n```\noutput\n```\n\n```{r}\n#| echo: true\nb <- a\n```\n\n````r\nx <- '```'\n````\n";
  assert.deepEqual(rBlocks(source), ["a <- 1", "#| echo: true\nb <- a", "x <- '```'"]);
});

test("the site and the block check load the same webR release", () => {
  const pkg = JSON.parse(readFileSync(new URL("./package.json", import.meta.url), "utf8"));
  assert.equal(pkg.devDependencies.webr, WEBR_VERSION);
  assert.equal(WEBR_BASE, `https://webr.r-wasm.org/v${WEBR_VERSION}/`);
});
