// One R session for one page. No DOM. runner.js supplies the engine (webR).
//
// A chapter reads top to bottom, and a later block uses objects made by the
// blocks above it. So Run on block k first runs every block above k that has
// not run in this session, in order, with the code each block shows now.
// An earlier block that fails does not stop the ones after it: one block on a
// page may read a file the browser does not have, and the rest still work.
//
// Stop closes R. webR on a page without cross-origin isolation (GitHub Pages)
// talks to R by postMessage, and that channel cannot interrupt running code,
// so stopping means a fresh R on the next Run. The blocks above run again then.
//
// If R itself faults (a WebAssembly error in a package's compiled code), the
// block shows why, and the session closes R so the next Run starts fresh.
//
// The engine is engine.js: { install(names) -> { missing }, run(code) -> { items, images, error, fatal }, close() }.

import { browserExplanation, packagesIn } from "./packages.js";

export class PageSession {
  constructor({ codeOf, count, startEngine }) {
    this.codeOf = codeOf;
    this.count = count;
    this.startEngine = startEngine;
    this.engine = null;
    this.ran = new Map();
    this.failed = new Set();
    this.installed = new Set();
    this.missing = new Set();
    this.generation = 0;
    this.busy = false;
  }

  // The blocks Run on block k would execute, in order.
  plan(k) {
    const out = [];
    for (let i = 0; i < k; i++) if (!this.ran.has(i)) out.push(i);
    out.push(k);
    return out;
  }

  // Packages the planned blocks name that this session has not tried yet.
  packagesFor(indices) {
    const out = [];
    for (const i of indices) {
      for (const name of packagesIn(this.codeOf(i))) {
        if (!this.installed.has(name) && !this.missing.has(name) && !out.includes(name)) out.push(name);
      }
    }
    return out;
  }

  // hooks: status(kind, detail), blockStart(i, earlier), blockDone(i, result).
  // Returns "done", "busy", "stopped" (Stop was pressed, or R did not start),
  // or "restarted" (R faulted while running a block and was closed).
  async run(k, hooks = {}) {
    if (!Number.isInteger(k) || k < 0 || k >= this.count) throw new Error(`no block ${k}`);
    if (this.busy) return "busy";
    this.busy = true;
    const generation = this.generation;
    const live = () => generation === this.generation;
    const status = hooks.status ?? (() => {});
    try {
      if (!this.engine) {
        status("start");
        const engine = await this.startEngine();
        if (!live()) {
          engine.close();
          return "stopped";
        }
        this.engine = engine;
      }
      const engine = this.engine;
      const order = this.plan(k);
      const wanted = this.packagesFor(order);
      if (wanted.length) {
        status("install", wanted);
        const result = await engine.install(wanted);
        if (!live()) return "stopped";
        const missing = new Set(result?.missing ?? []);
        for (const name of wanted) (missing.has(name) ? this.missing : this.installed).add(name);
      }
      for (const i of order) {
        if (!live()) return "stopped";
        const code = this.codeOf(i);
        hooks.blockStart?.(i, i !== k);
        status("run", i);
        const started = Date.now();
        const result = await engine.run(code);
        if (!live()) return "stopped";
        this.ran.set(i, code);
        let explanation = null;
        if (result.error) {
          const above = [...this.failed].filter((j) => j < i);
          explanation = browserExplanation(result.error, {
            unavailable: [...this.missing],
            earlierFailed: above.length ? Math.max(...above) + 1 : null,
            fatal: Boolean(result.fatal),
          });
          this.failed.add(i);
        } else {
          this.failed.delete(i);
        }
        hooks.blockDone?.(i, { ...result, explanation, earlier: i !== k, ms: Date.now() - started });
        if (result.fatal) {
          this.reset();
          status("restarted");
          return "restarted";
        }
      }
      status("done");
      return "done";
    } catch (error) {
      if (!live()) return "stopped";
      // R itself failed (it did not load, or the worker died). Start again next time.
      this.reset();
      status("failed", String(error?.message ?? error));
      return "stopped";
    } finally {
      if (live()) this.busy = false;
    }
  }

  // Close R. Output already on the page stays; the next Run starts a fresh R.
  stop() {
    this.reset();
  }

  reset() {
    this.generation++;
    const engine = this.engine;
    this.engine = null;
    this.ran.clear();
    this.failed.clear();
    this.installed.clear();
    this.missing.clear();
    this.busy = false;
    try {
      engine?.close();
    } catch {
      // Already closed.
    }
  }
}
