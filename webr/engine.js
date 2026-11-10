// webR behind the engine interface session.js expects. No DOM.
// The browser runner and the block check both use this, so the check runs
// blocks the way a reader's browser does: the same install.packages shim,
// the same autoprint, and the same text for messages, warnings and errors.
//
//   install(names) -> { missing }   names that still do not load afterwards
//   run(code)      -> { items, images, error, fatal }
//   close()

// Text of a WebAssembly fault. R cannot be trusted after one, so the session restarts.
export const FATAL = /function signature mismatch|null function|RuntimeError|unreachable|memory access out of bounds|Aborted\(/;

export async function webREngine({ WebR, options = {}, setup = "", progress, plotSize, timeoutMs = 0 }) {
  const webR = new WebR(options);
  await webR.init();
  // Package downloads print "Downloading webR package: name". Report them as progress.
  let open = true;
  (async () => {
    while (open) {
      let message;
      try {
        message = await webR.read();
      } catch {
        return;
      }
      if (message?.type === "stdout" || message?.type === "stderr") {
        const name = String(message.data).match(/Downloading webR package: (\S+)/)?.[1];
        if (name) progress?.(name);
      }
      if (message?.type === "closed") return;
    }
  })();
  // A reader who types library(x) or install.packages("x") gets the webR build without a prompt.
  await webR.evalRVoid(`options(webr.show_menu = FALSE); webr::shim_install(); ${setup}`);
  const shelter = await new webR.Shelter();

  async function text(item) {
    if (item.type === "stdout") return { kind: "out", text: String(item.data) };
    if (item.type === "stderr") return { kind: "message", text: String(item.data) };
    const kind = item.type === "error" ? "error" : item.type === "warning" ? "warning" : "message";
    const label = kind === "error" ? "Error" : kind === "warning" ? "Warning" : "";
    try {
      const body = await webR.evalRString(
        `local({
          call <- conditionCall(cond)
          shown <- if (is.null(call)) "" else paste(deparse(call, nlines = 1L), collapse = "")
          # A top-level warning() or stop() reports the evaluator webR runs the block in; R's console shows no call there.
          if (shown %in% c("eval(ei, envir)", "eval(expr, envir)", "withVisible(eval(ei, envir))") || nchar(shown) > 60) shown <- ""
          where <- if (nzchar(shown)) paste0(" in ", shown) else ""
          msg <- sub("\\n$", "", conditionMessage(cond))
          if (nzchar("${label}")) paste0("${label}", where, ": ", msg) else msg
        })`,
        { env: { cond: item.data } },
      );
      return { kind, text: body };
    } catch {
      return { kind, text: label || "R condition" };
    }
  }

  async function capture(code) {
    const size = plotSize?.();
    return shelter.captureR(code, {
      withAutoprint: true,
      captureStreams: true,
      captureConditions: true,
      captureGraphics: size ? { width: size.width, height: size.height } : false,
      throwJsException: false,
    });
  }

  return {
    async install(names) {
      await webR.installPackages(names, { quiet: false });
      const vector = names.map((name) => JSON.stringify(name)).join(", ");
      try {
        // Installed or not, without loading: the install.packages shim also changes
        // what requireNamespace() returns for a package it could not fetch.
        const missing = await shelter.evalR(`Filter(function(p) !nzchar(system.file(package = p)), c(${vector}))`);
        return { missing: await missing.toArray() };
      } finally {
        await shelter.purge();
      }
    },
    async run(code) {
      let timer;
      try {
        const work = capture(code);
        const result = timeoutMs
          ? await Promise.race([
            work,
            new Promise((_, reject) => {
              timer = setTimeout(() => {
                webR.interrupt();
                reject(new Error(`stopped after ${Math.round(timeoutMs / 1000)} s`));
              }, timeoutMs);
            }),
          ])
          : await work;
        const items = [];
        for (const item of result.output) items.push(await text(item));
        const error = items.find((item) => item.kind === "error")?.text ?? null;
        return { items, images: result.images ?? [], error, fatal: Boolean(error && FATAL.test(error)) };
      } catch (error) {
        // The worker threw instead of returning an R error: a WebAssembly fault or a lost worker.
        const message = String(error?.message ?? error);
        return { items: [{ kind: "error", text: "Error: " + message }], images: [], error: message, fatal: true };
      } finally {
        clearTimeout(timer);
        try {
          await shelter.purge();
        } catch {
          // R is gone; the session restarts it.
        }
      }
    },
    close() {
      open = false;
      webR.close();
    },
  };
}
