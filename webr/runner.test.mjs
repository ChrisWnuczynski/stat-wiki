// Node tests for the page session and runner UI, with a stand-in engine and DOM.

import assert from "node:assert/strict";
import test from "node:test";
import { rBlocks } from "./blocks.js";
import { PageSession } from "./session.js";
import { WEBR_BASE, WEBR_VERSION } from "./version.js";
import { readFileSync } from "node:fs";
import { install } from "./runner.js";
import { pageDocument } from "./test/dom.mjs";

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

function deferred() {
  let resolve, reject;
  const promise = new Promise((yes, no) => { resolve = yes; reject = no; });
  return { promise, resolve, reject };
}

function runner(t, codes, startEngine) {
  const previous = Object.getOwnPropertyDescriptor(globalThis, "document");
  globalThis.document = pageDocument(codes);
  t.after(() => {
    if (previous) Object.defineProperty(globalThis, "document", previous);
    else delete globalThis.document;
  });
  const ui = install({ startEngine });
  return {
    ...ui,
    control: (i, name) => ui.blocks[i].bar.querySelector(`.r-run-${name}`),
    status: (i) => ui.blocks[i].bar.querySelector(".r-run-status").textContent,
  };
}

const outputResult = (text) => ({ items: [{ kind: "out", text }], images: [], error: null });

for (const settlement of ["resolve", "reject"]) {
  for (const nextBlock of [2, 3]) {
    test(`stopped predecessor may ${settlement} while a new run on block ${nextBlock + 1} owns the UI`, async (t) => {
      const aStarted = deferred(), a = deferred(), bStarted = deferred(), b = deferred();
      const codes = ["completed", "pending", "requested", "other"];
      const calls = [], closed = [];
      let starts = 0;
      const ui = runner(t, codes, async () => {
        const id = ++starts;
        return {
          async run(code) {
            calls.push([id, code]);
            if (id === 1 && code === "pending") { aStarted.resolve(); return a.promise; }
            if (id === 2 && code === "completed") { bStarted.resolve(); return b.promise; }
            return outputResult(`${id}: ${code}`);
          },
          close() { closed.push(id); },
        };
      });

      const runA = ui.control(2, "go").click();
      await aStarted.promise;
      assert.equal(ui.status(1), "Running…");
      assert.match(ui.status(2), /Running block 2 above first/);
      const completedOutput = ui.blocks[0].output;
      const completedText = completedOutput.textContent;
      const completedStatus = ui.status(0);

      await ui.control(2, "stop").click();
      // Collect this separately: an old UI must also reach the stale-cleanup
      // assertions below, even though its predecessor already says Running.
      const stoppedStatus = ui.status(1);
      assert.deepEqual(closed, [1]);
      assert.equal(ui.session.ran.size, 0);
      assert.match(ui.status(2), /R stopped/);
      for (const block of ui.blocks) assert.equal(ui.control(block.index, "go").disabled, false);
      assert.equal(ui.blocks[0].output, completedOutput);
      assert.equal(completedOutput.textContent, completedText);
      assert.equal(ui.status(0), completedStatus);

      const runB = ui.control(nextBlock, "go").click();
      await bStarted.promise;
      const pendingStatus = ui.status(nextBlock);
      if (settlement === "resolve") a.resolve(outputResult("obsolete result"));
      else a.reject(new Error("obsolete failure"));
      await runA;
      try {
        assert.equal(ui.control(nextBlock, "stop").hidden, false, "old cleanup must leave B's Stop visible");
        for (const block of ui.blocks) assert.equal(ui.control(block.index, "go").disabled, true, "Run stays disabled until B settles");
        assert.equal(ui.status(nextBlock), pendingStatus);
        assert.equal(ui.session.busy, true);
        assert.doesNotMatch(stoppedStatus, /Running/, "Stop must clear the interrupted predecessor's status immediately");
        assert.equal(ui.blocks[1].output, null, "a stopped predecessor must not publish stale output");
        assert.equal(completedOutput.textContent, completedText);
      } finally {
        b.resolve(outputResult("2: completed"));
        await runB;
      }
      assert.equal(starts, 2);
      assert.deepEqual(calls, [[1, "completed"], [1, "pending"], ...codes.slice(0, nextBlock + 1).map((code) => [2, code])]);
      assert.deepEqual(closed, [1]);
      for (const block of ui.blocks) {
        assert.equal(ui.control(block.index, "go").disabled, false);
        assert.equal(ui.control(block.index, "stop").hidden, true);
        assert.doesNotMatch(ui.status(block.index), /Running/);
      }
      assert.match(ui.status(nextBlock), /^Ran in/);
      assert.match(ui.blocks[nextBlock].output.textContent, new RegExp(`2: ${codes[nextBlock]}`));
    });
  }
}

test("Control+Enter during a run cannot move its Stop control to another block", async (t) => {
  const started = deferred(), pending = deferred();
  const ui = runner(t, ["first", "second"], async () => ({
    run() { started.resolve(); return pending.promise; },
    close() {},
  }));
  await ui.control(1, "edit").click();
  const running = ui.control(0, "go").click();
  await started.promise;
  try {
    await ui.blocks[1].editor.dispatchEvent({ type: "keydown", key: "Enter", ctrlKey: true, preventDefault() {} });
    assert.equal(ui.control(0, "stop").hidden, false);
    assert.equal(ui.control(1, "stop").hidden, true);
    assert.equal(ui.status(0), "Running…");
    assert.equal(ui.control(1, "go").disabled, true);
  } finally {
    pending.resolve(outputResult("done"));
    await running;
  }
  assert.match(ui.status(0), /^Ran in/);
  assert.equal(ui.control(0, "go").disabled, false);
});

test("the new run can still be stopped after the stopped run settles", async (t) => {
  const started = [deferred(), deferred()];
  const pending = [deferred(), deferred()];
  let starts = 0;
  const closed = [];
  const ui = runner(t, ["earlier", "requested"], async () => {
    const id = starts++;
    return {
      run() { started[id].resolve(); return pending[id].promise; },
      close() { closed.push(id); },
    };
  });
  const a = ui.control(1, "go").click();
  await started[0].promise;
  await ui.control(1, "stop").click();
  const b = ui.control(1, "go").click();
  await started[1].promise;
  pending[0].resolve(outputResult("stale A"));
  await a;
  assert.equal(ui.control(1, "stop").hidden, false);
  await ui.control(1, "stop").click();
  pending[1].reject(new Error("stopped B"));
  await b;
  assert.deepEqual(closed, [0, 1]);
  assert.equal(ui.session.busy, false);
  assert.equal(ui.status(0), "");
  assert.match(ui.status(1), /R stopped/);
  assert.equal(ui.control(1, "stop").hidden, true);
  assert.equal(ui.control(1, "go").disabled, false);
  assert.equal(ui.blocks[0].output, null);
});

for (const failure of ["ordinary", "fatal", "worker"]) {
  test(`the UI preserves ${failure} error handling and clears temporary statuses`, async (t) => {
    const calls = [], closed = [];
    const ui = runner(t, ["earlier", "requested"], async () => ({
      async run(code) {
        calls.push(code);
        if (code === "requested") return outputResult("later result");
        if (failure === "worker") throw new Error("worker died");
        return {
          items: [{ kind: "error", text: "Error: boom" }], images: [], error: "boom", fatal: failure === "fatal",
        };
      },
      close() { closed.push("closed"); },
    }));
    await ui.control(1, "go").click();
    assert.deepEqual(calls, failure === "ordinary" ? ["earlier", "requested"] : ["earlier"]);
    assert.equal(closed.length, failure === "ordinary" ? 0 : 1);
    if (failure === "worker") {
      assert.equal(ui.status(0), "");
      assert.match(ui.status(1), /R did not start or stopped working: worker died/);
    } else {
      assert.match(ui.status(0), /^Error in/);
      assert.match(ui.blocks[0].output.textContent, /Error: boom/);
      if (failure === "fatal") assert.match(ui.status(1), /R stopped working and was closed/);
      else {
        assert.match(ui.status(1), /^Ran in/);
        assert.match(ui.blocks[1].output.textContent, /later result/);
      }
    }
    for (const block of ui.blocks) {
      assert.equal(ui.control(block.index, "go").disabled, false);
      assert.equal(ui.control(block.index, "stop").hidden, true);
      assert.doesNotMatch(ui.status(block.index), /Running/);
    }
  });
}
