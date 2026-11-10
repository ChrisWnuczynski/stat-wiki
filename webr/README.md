# R in the browser

The R blocks on the Using R pages have Run and Edit buttons. Run executes the block with [webR](https://docs.r-wasm.org/webr/latest/), R compiled to WebAssembly, in the reader's browser. Nothing is installed on the reader's computer, and no server runs R.

## What a reader sees

- Nothing downloads until someone presses Run. The first Run starts R (a few seconds) and installs the packages the page names, from the webR package repository. A Using R page with ggplot2 and dplyr is ready in about 10 to 15 seconds on a fast connection; the browser keeps the files for the next page.
- A page has one R session. Run on a block first runs every block above it that has not run yet, in order, because a chapter's later blocks use objects the earlier ones make. A block above that fails does not stop the ones after it.
- Edit swaps the block for a text box. Control and Enter (Command and Enter on a Mac) runs it, and Reset puts the page's code back. Tab indents; Escape and then Tab leaves the box.
- Output, messages, warnings, errors and plots appear under the block.
- Stop R closes R. The next Run starts a fresh R and reruns the blocks above.
- When a block cannot run in a browser, the note under it says why: a package that is not built for webR, a file on the reader's own computer, or a package whose compiled code faults in webR.

## Why the postMessage channel

webR's fastest channel needs the page to be cross-origin isolated, which needs two response headers. GitHub Pages cannot send them, so webR falls back to its postMessage channel by itself. The cost: running R code cannot be interrupted, and `readline()`, `menu()` and `browser()` do not work. Stop therefore closes R instead of interrupting it. Moving the site to a host that can send the headers would not be free either: the same headers block the Turnstile check that the Ask StatWiki chat uses unless that frame is allowed explicitly.

## Files

| File | What it is |
|---|---|
| `runner.js` | The buttons, the edit box and the output on the page. Loaded only on a Using R page with an R block. |
| `engine.js` | webR behind a small interface: install packages, run a block, close. No DOM, so the check uses it too. |
| `session.js` | One page's R session: which blocks run, in what order, and what a failure means. No DOM and no webR. |
| `packages.js` | The packages a block names: `pkg::`, `library()`, `require()`, and `package = "pkg"`. |
| `version.js` | The webR release the site loads. `package.json` pins the same release for the check. |
| `blocks.js` | The R blocks of a chapter source, for the check. |
| `check-blocks.mjs` | Runs every R block of the Using R chapters in webR, the way a browser does. |
| `runs/` | The check's results, one file per run. |
| `test/` | A fixture page and the browser test. |

The loader is in `build_wiki.py` (`WEBR_JS`), and `RUNNABLE_PARTS` names the parts whose pages get Run buttons.

## Checks

```
cd webr
npm ci
npm test
node check-blocks.mjs
node test/e2e.mjs
```

- `npm test` checks the package reader and the page session with a stand-in R. It needs no network.
- `check-blocks.mjs` runs every block of the Using R chapters in a fresh webR per page and saves the result in `runs/`. It exits with status 1 if a block fails without an explanation. Run it after changing a Using R chapter or the webR release. It needs `repo.r-wasm.org`; behind a proxy, set `NODE_USE_ENV_PROXY=1`.
- `test/e2e.mjs` drives the runner in Chromium against `test/page.html`: run-above, messages and warnings, a plot, editing, an error, a package install, and Stop. It needs `webr.r-wasm.org` and `repo.r-wasm.org`.

## The run on 10 November 2026

webR 0.6.0 (R 4.6.0): 61 of the 67 blocks ran. The other six are explained under the block:

- `ur-01` block 11 reads `data/measurements.csv`, a file on the reader's computer.
- `ur-04` blocks 2, 5 and 6 use `mclust`, which the webR repository does not have. Block 3 uses what block 2 makes.
- `ur-04` block 7 calls `EMMIXmfa::mcfa`, which faults inside webR ("function signature mismatch"). `EMMIXmfa::mfa` works.

## Changing the webR release

Set the release in `version.js` and in `package.json`, run `npm install`, then run both checks. `npm test` fails if the two releases differ.
