# Handoff: R in the browser, interactive labs, search by meaning

Written 10 November 2026, when the work was stopped partway through. Branch `claude/kind-davinci-gi4qgs`. Delete this file once the work it describes is finished or dropped.

## The brief

The site owner chose three features for StatWiki:

1. **Run R in the browser.** Live code boxes on the Using R chapters, with webR (R compiled to WebAssembly), so students can run and edit the examples without installing anything.
2. **Interactive demos.** Slider-driven labs: a Beta prior updating, a Markov chain running, confidence intervals covering or missing. Plain JavaScript, free to host.
3. **Search by meaning.** "How do I know if my estimator is the best one" should find UMVU. Reuse the Vectorize index the Ask StatWiki chatbot already has.

## Status at a glance

| Feature | State | What remains |
|---|---|---|
| 1. R in the browser | **Done and verified.** The unit tests and a README row are in the publish workflow. | Nothing required. The six blocks that cannot run are listed below. |
| 2. Labs | **Done and checked against SciPy.** Three pages, the chart helper, navigation, chapter links, Node tests, and a browser test. | Nothing required for this feature. |
| 3. Search by meaning | **Not started.** A plan is below. Do not deploy the Ask worker while building it. | Everything in that plan |
| Wrap-up | Labs and the R runner are in CI and the README. | Search, then delete this file |

## Two premises that turned out wrong

These change the design, so read them first.

- **The site is on GitHub Pages, not Cloudflare Pages.** `.github/workflows/publish.yml` deploys through the GitHub Pages API, and the live site answers with `server: GitHub.com`. Only the Ask worker (`ask.statwiki.io`) runs on Cloudflare. "Hosted on Pages" in the brief means GitHub Pages.
- **webR does not need special hosting.** webR's fast channel needs the page to be cross-origin isolated (`Cross-Origin-Opener-Policy` and `Cross-Origin-Embedder-Policy` headers). GitHub Pages can't send those headers, so webR falls back to its `PostMessage` channel, which its own docs describe for exactly this case. The cost: running R can't be interrupted, and `readline()`, `menu()` and `browser()` don't work. Moving to Cloudflare Pages to get the headers would not be free either: `require-corp` blocks cross-origin frames such as the Turnstile check the Ask chat depends on. **Decision: stay on GitHub Pages and use the PostMessage channel.** "Stop R" closes R and restarts it rather than interrupting.

## Feature 1: R in the browser (done)

### What a reader gets

On the 12 pages of the "Using R" part (`notes/da-03-using-r` and `notes/ur-01` … `ur-11`), every ```` ```r ```` block gets **Run**, **Edit**, **Reset** (after an edit) and **Stop R** (while running).

- Nothing downloads until the first Run. R then loads from the webR CDN, pinned to `https://webr.r-wasm.org/v0.6.0/`, and the page's packages come from `repo.r-wasm.org`.
- Each page has one R session. Run on block k first runs every block above k that hasn't run yet, in order, because later blocks use objects from earlier ones (for example `aq`). A failing block above does not stop the ones below.
- Packages are found from `pkg::`, `pkg:::`, `library()`, `require()`, `requireNamespace()`, `loadNamespace()` and `package = "x"`, ignoring comments and strings. The chapters use `pkg::fn` style with no `library()` calls, so this matters. `webr::shim_install()` is on, so a student who types `install.packages("x")` or `library(x)` gets the webR build.
- Output, messages, warnings, errors and ggplot or base plots appear under the block. Plots are drawn on a canvas at 2× scale. In the browser, R started and ran three blocks in about 3.5 s; a cold start of ur-02 that installed ggplot2, dplyr and purrr took 11.9 s.
- When a block can't run in a browser, the note under it says why:
  - a package webR doesn't have,
  - a file on the reader's own computer,
  - "block N above did not run, and this block uses something it makes",
  - a WebAssembly fault in a package's compiled code, after which R restarts.
- The editor is a plain `<textarea>`: Ctrl/Cmd+Enter runs, Tab indents, Escape then Tab leaves the box.

### Files (all new unless marked)

| File | Role |
|---|---|
| `webr/runner.js` | DOM layer: buttons, editor, output rendering, intro line. Exports `install({ startEngine })`. Loads webR from the CDN. |
| `webr/engine.js` | webR behind `{ install(names) → {missing}, run(code) → {items, images, error, fatal}, close() }`. No DOM; shared by the browser and the Node check. Uses `captureR` with `withAutoprint`, `captureConditions`, `throwJsException: false` and `captureGraphics`. Formats conditions like R's console and hides webR's internal `eval(ei, envir)` call. Decides which packages are missing with `system.file()`, because the install shim makes `requireNamespace()` misbehave for packages it couldn't fetch. |
| `webr/session.js` | `PageSession`: run-above ordering, package install batching, failure tracking, Stop and restart, and restart after a fatal fault. No DOM, no webR. |
| `webr/packages.js` | `packagesIn`, `packagesForBlocks`, `scan` (strips comments and strings), and `browserExplanation` (the notes listed above). |
| `webr/version.js` | `WEBR_VERSION = "0.6.0"`. 0.6.1 was published on 10 Nov 2026, the day of this work, so 0.6.0 (May 2026) is pinned. |
| `webr/blocks.js` | `rBlocks(source)`: the ```` ```r ```` and ```` ```{r} ```` blocks of a chapter, in order. |
| `webr/check-blocks.mjs` | Runs every block of the Using R chapters in a fresh webR per page, through the same `PageSession` and `engine.js`, and writes `webr/runs/<date>.json`. Exits 1 on a failure that has no explanation, or a block with no result. Has a local pass-through mirror of `repo.r-wasm.org`, because R inside webR in Node ignores the proxy, and it reads the repo's PACKAGES index to tell "not in the repo" from "download failed". |
| `webr/runs/2026-11-10.json` | The committed record of the final run. |
| `webr/packages.test.mjs`, `webr/runner.test.mjs` | Node unit tests (22 pass): package reader, explanations, session ordering, Stop, restart, edited code, version pin. No network. |
| `webr/test/page.html`, `webr/test/e2e.mjs` | Playwright test against a fixture with Quarto's exact code-block markup, served without cross-origin isolation like GitHub Pages. Covers run-above, messages and warnings, a plot (checks for ink pixels), editing with Ctrl+Enter, Reset, an R error, a dplyr install, and Stop then restart. **Passes.** Needs network. |
| `webr/package.json`, `webr/package-lock.json` | Dev dependency `webr@0.6.0` for the check. `npm test` runs the unit tests. |
| `webr/README.md` | How it works, why PostMessage, files, checks, the run results, and how to change the webR release. |
| `build_wiki.py` (modified) | Adds `import json`, plus `RUNNABLE_PARTS = ("Using R",)`, `WEBR_FILES`, the `WEBR_JS` loader and `runnable_pages()`. The loader is appended to `_random.html`, which is on every page; it imports `webr/runner.js` only when the page is in the list and has `pre.sourceCode.r`. The five runner files are added to `resources:` in the generated `_quarto.yml`. |
| `.gitignore` (modified) | Adds `/webr/node_modules/`. |

### Verification done

- `node --test webr/packages.test.mjs webr/runner.test.mjs`: 22/22 pass.
- `node webr/check-blocks.mjs` with webR 0.6.0 (R 4.6.0): **67 blocks. 61 run cleanly, 6 fail with a correct explanation, 0 unexplained.** The six:
  - `ur-01` block 11 reads `data/measurements.csv`, a template for the reader's own file.
  - `ur-04` blocks 2, 5 and 6 need **mclust**, which is not in the webR repo (all 22 other packages are).
  - `ur-04` block 3 depends on block 2.
  - `ur-04` block 7: **`EMMIXmfa::mcfa` faults inside webR** ("null function or function signature mismatch") even on a tiny fit. This was isolated by hand. `EMMIXmfa::mfa` works (about 10 s).
- `node webr/test/e2e.mjs`: passes.
- The live ur-02 page, fetched from www.statwiki.io with the new loader injected, works in Chromium in light and dark themes, with no page errors.
- `python build_wiki.py` runs and writes the expected loader list and resources. Quarto itself couldn't be installed here (see "Environment"), so `quarto render` of these changes has **not** been run. The risk is low: the change is one more `<script>` in `_random.html` and five more `resources:` entries.

### Possible follow-ups for feature 1 (not required)

- Put the R chapters' blocks that can't run in the browser (mclust, mcfa) in front of the owner. A content change, such as replacing mclust with a package webR has, is the owner's call.
- The `da-03` block 1 `install.packages(c(...16 packages...))` works in the browser through the shim, but downloads everything (21 s in Node).
- Dark-mode code blocks on the live site have low contrast (light grey background). That predates this work and isn't caused by it.

## Feature 2: interactive labs (done)

### Decision: plain ES modules with hand-drawn SVG, not Observable JS

The existing lab (`labs/kernel-density.qmd`, `_kde-figure.qmd`, `kde-math.js`, `kde-math.test.mjs`, `reference_kde.py`, `lab-chrome.js`) uses Quarto OJS cells with Observable Plot. The new labs instead use **plain ES modules that export `mount(root)` and draw their own SVG**, reusing `labs/lab-chrome.js` (`controlRow`, `graphFrame`, `readoutLine`, `markerLegend`, `watchTheme`, `themeInk`, `installLabChrome`) for a matching look. Reasons:

- Quarto couldn't be installed in the cloud session, so OJS cells couldn't be rendered or tested.
- Plain modules can be tested in Playwright against a fixture page.
- No CDN dependency: OJS's `Plot` loads lazily from jsdelivr. Plain modules therefore also work offline in the desktop app (`_app/launch_wiki.pyw`).

If you can run Quarto and prefer OJS for consistency, that is a valid alternative. Keep the maths modules either way.

### The pattern to keep from the KDE lab

- A pure maths module with no DOM.
- A Python reference script, using scipy and numpy (installed with `pip install scipy numpy`), that writes `labs/fixtures/*.json` without importing the JS.
- A Node test that holds the JS to those numbers with stated tolerances.
- A `.qmd` page with these sections: what the page investigates; predict first; the model the controls change (with formulas); the figure; what the picture shows; where this fails; on the theory page (links).
- `<div data-lab-page hidden></div>` widens the page; see `lab-chrome.js` CSS.
- Seeded generator: `mulberry32`, so a seed reproduces the page. It is not R's RNG, and the pages say so.

### Written so far (not yet tested against a reference)

- **`labs/stat-math.js`**: `lgamma` (Lanczos g=7), `lbeta`, `lchoose`, `betaCdf` and `betaSurvival` (Lentz continued fraction), `betaPdf`, `betaQuantile` (bisection in the accurate tail), `gammaP` and `gammaQ`, `normalPdf`, `normalCdf` (from `gammaQ(1/2, z²/2)`), `normalQuantile` (Acklam plus Halley refinement), `tCdf`, `tQuantile` (through `betaQuantile`), `binomPmf`, `betaBinomPmf`, `mulberry32` (returns uniforms in (0,1), same core as `kde-math.js`), `normalStream` (Box–Muller), and `formatNumber`. Smoke check only: it loads, and `betaQuantile(0.975, 8, 12) = 0.61642…`, which has **not** been checked against scipy.
- **`labs/beta-binomial-math.js`**: `DEFAULTS`, `LIMITS`, `PRESETS` (the chapter's Beta(5,5), Beta(1,1) and Beta(0.6,0.6)), `validate`, `betaSummary` (mean, sd, mode with boundary cases, equal-tailed interval), `update` (posterior, prior weight w = (α+β)/(α+β+n), and the blended-mean identity), `densityCurves` (prior, scaled likelihood = Beta(x+1, n−x+1), posterior, on a cosine grid denser near 0 and 1), `prediction` (beta-binomial predictive against plug-in binomial, with both variances), and `tosses` (seeded coin, prefix-stable). Smoke check: uniform prior with 3 heads in 10 gives a posterior mean of 1/3, which matches the chapter.

### What was built, in the order it was specified

These steps are done. `labs/reference_stats.py` checked the shared functions, the Beta–Binomial summaries, the Markov stationary vectors, and the coverage formulas against SciPy and NumPy. `node --test` on the four new modules passes. `labs/test/e2e.mjs` passes in Chromium, including empty inputs, a blank matrix cell, a sample of size 1, no intervals, dark mode, and a narrow window. Quarto 1.6.40 rendered `labs/index.qmd`, `labs/beta-binomial.qmd`, `labs/markov-chain.qmd`, and `labs/ci-coverage.qmd`; the rendered pages mount and respond. The site-wide post-render step still expects a full site, so it was not part of this pass.

1. **`labs/reference_stats.py`** writes `labs/fixtures/stats-reference.json` from scipy: `gammaln`, `betaln`, `beta.pdf/cdf/sf/ppf` (include shapes below 1 and large shapes such as 500), `norm.cdf/ppf` (tails to 1e-12), `t.cdf/ppf` (df 1, 2, 5, 30, 1000), `binom.pmf`, `betabinom.pmf`. Add lab-level cases: Beta–Binomial posterior summaries; Markov stationary vectors from numpy null-space; exact Wald and Wilson coverage sums; the t and z-with-s coverage formulas. Put tolerances in the JSON, as `reference_kde.py` does.
2. **`labs/stat-math.test.mjs`** and **`labs/beta-binomial-math.test.mjs`**. Fix anything the reference exposes.
3. **`labs/markov-math.js`** (2 to 6 states):
   - `validateMatrix` (rows non-negative and summing to 1 within 1e-9) and `normaliseRows`.
   - Communicating classes from reachability; closed classes; period as the gcd of `level[u]+1−level[v]` over edges inside a class.
   - `stationary`: unique if there is exactly one closed class (Gaussian elimination with pivoting on that class, zeros elsewhere); otherwise one vector per closed class, marked not unique.
   - `distributionPath` (π⁽⁰⁾Pᵗ, exact), `simulate` (inverse transform on rows, seeded), running occupation fractions, and `tv` (total variation distance).
   - Presets from `sources/stat2003/chapters/prob-06-markov-chains.qmd`: the **six stepping stones** (default, start at stone 1; known π = (12, 4, 20, 25, 22, 36)/119, and P² row 1 = (1/6, 0, 1/6, 1/6, 0, 1/2), both good fixtures), the **two-state weather chain** [[0.8, 0.2], [0.4, 0.6]] with π = (2/3, 1/3) and rate 0.4, the **two-cycle** [[0, 1], [1, 0]] (periodic: Pᵗ oscillates while time averages converge, which is the teaching point), a **sticky** 3-state chain (diagonal 0.96, slow mixing), and a **reducible** chain with two closed classes and a transient start, so the time average depends on the path.
   - **Leave out** the exercise chain [[.5, .5, 0], [.25, .5, .25], [0, .5, .5]] so the lab doesn't give away an exercise answer.
4. **`labs/coverage-math.js`**:
   - Mean of a population: N(10, 2²) or Exponential(mean 2). Methods: t interval, and z with s (the small-sample mistake).
   - Proportion: Bernoulli(p). Methods: Wald and Wilson.
   - `draw(seed, config, M)` is prefix-stable, so "100 more" keeps the earlier intervals.
   - Exact coverage: t under the normal is 1−α; z-with-s under the normal is 2·tCdf(z, n−1)−1; Wald and Wilson by exact sum Σₓ pmf(x)·1{p ∈ CI(x)}.
   - Exponential: Monte Carlo long-run coverage (fixed seed, 20,000 repetitions) with its standard error, labelled as Monte Carlo.
   - A band for the realised fraction after m intervals (normal approximation, labelled as such).
5. **`labs/svg-chart.js`**: a small helper for linear scales, nice ticks, axes and grid, lines, areas, segments, dots, rules and text. Responsive through `viewBox` and a ResizeObserver, and redrawn on `watchTheme`. Colours come from `themeInk()`. The KDE figure's accent palettes are in `_kde-figure.qmd` (`themeColors`).
6. **UIs**, each exporting `mount(root)`:
   - `labs/beta-binomial.js`: α and β sliders with number boxes, preset buttons, n and x sliders, "+ head", "+ tail", "toss 10 from θ_true" (seeded), the true θ slider, and future m.
     - Panel A: prior (dashed), scaled likelihood, posterior, the 95% band shaded, a rule at x/n, and an optional θ_true. Unbounded densities clipped, with a note.
     - Panel B: predictive against plug-in pmf bars.
     - Readout: Beta(α+x, β+n−x), mean = w·prior mean + (1−w)·x/n, sd, mode, interval.
   - `labs/markov-chain.js`: matrix grid editor, presets, start state, steps, seed.
     - Panel A: path, first ~120 steps.
     - Panel B: exact π⁽⁰⁾Pᵗ per state, π as dashed lines, and running occupation fractions dotted.
     - Readout: classes, period, π (or "not unique"), TV distance.
   - `labs/ci-coverage.js`: population, method, n, level, M, seed, "100 more", and p for proportions.
     - Panel A: stacked intervals, misses in a contrasting colour, a rule at the truth.
     - Panel B: running coverage for means, or exact coverage against p for proportions (the Wald sawtooth against Wilson).
7. **Pages**: `labs/beta-binomial.qmd`, `labs/markov-chain.qmd`, `labs/ci-coverage.qmd`, each mounting the module through a raw HTML block that imports `offset + "labs/<name>.js"` (see `_kde-figure.qmd` for how `quarto:offset` is read). Add `labs/index.qmd` listing all four labs.
8. **`build_wiki.py` wiring**:
   - In `write_config`, add the new `.js` files to `resources:`.
   - Point the navbar "Laboratories" at `labs/index.qmd`, and list all four labs in the sidebar "Laboratories" section.
   - In `RANDOM_AND_FILTER_JS`, around line 1276, change `"labs/kernel-density.html"` to `"labs/index.html"` so the section highlight still works.
   - `render:` already covers `labs/*.qmd` and skips `labs/_*.qmd`.
9. **Links from chapters**: add one sentence to each source chapter pointing at its lab, as `sl-07` does for the KDE lab. The chapters are `sources/book/chapters/bayes-02-beta-binomial.qmd` (after the conjugacy proposition or the prior-sensitivity section), `sources/stat2003/chapters/prob-06-markov-chains.qmd` (in "The limiting distribution"), and the confidence-interval chapter `sources/stat2004/chapters/inf-03-confidence-intervals.qmd`. The README says chapter content is edited in `sources/`.
10. **Tests**: add Node tests for each maths module to the publish workflow beside `node --test labs/kde-math.test.mjs`, and add a Playwright test for the three UIs, modelled on `webr/test/e2e.mjs`.

## Feature 3: search by meaning (not started; plan)

Ask StatWiki already has what's needed (`ask/core`, `ask/worker`):

- Vectorize index `statwiki-ask`: 1024-dimensional cosine embeddings from `@cf/qwen/qwen3-embedding-0.6b`, with `QUERY_INSTRUCTION` for queries.
- KV `CHUNKS` holds chunk text.
- `rankMatches`, `takePool` and `rerank` in `ask/core`.
- Every `/ask` call needs a Turnstile session, and the worker's daily budget limits model calls.

The plan:

1. **`GET /search?q=…&k=…`** on the same worker (`ask/worker/src/handler.ts`, `index.ts`):
   - Embed the query, run a Vectorize query (FETCH_K about 50), `rankMatches`, then group chunks by entry and page.
   - Return the top ~10 entries as `{ title, url, kind, score, snippet }`. Metadata already carries title, url and kind; check `ask/core/chunk.ts` and the metadata fields. Take the snippet from the KV chunk text, or skip it to save reads.
   - **No LLM call**, so no Turnstile and no budget charge.
2. **Abuse controls**: CORS stays as in `ask/worker/src/cors.ts`. Rate-limit by IP, either with the Workers Rate Limiting binding or a counter in the existing `AskBudget` Durable Object. Cap query length at about 200 characters. Cache responses with the Cache API, keyed on the normalised query. Embeddings cost Workers AI neurons; Vectorize queries are cheap.
3. **Tests**: add handler tests beside `ask/worker/src/handler.test.ts`, with stand-in deps as the existing tests use.
4. **Retrieval check**: add a harness script in `ask/harness`, modelled on `run.ts`, scoring search on the dev questions and on hand-written paraphrase queries.
   - The brief's own example, "how do I know if my estimator is the best one" → UMVU, belongs among those queries.
   - Note that `inf-08-information-and-bounds` and `inf-09-rao-blackwell` hold Cramér–Rao, Rao–Blackwell, Lehmann–Scheffé and UMVU; check which page or entry ids should count as correct.
   - The cloud session had `api.cloudflare.com` and `api.x.ai` credentials injected by its proxy. Elsewhere, set `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_API_TOKEN` as `ask/README.md` says.
5. **Front end**. Two options:
   - (a) A small module that adds a "Search by meaning" section under Quarto's navbar search results. Quarto's search is algolia-autocomplete with Fuse, so hooking it is fiddly.
   - (b) A `search.qmd` page with its own box, linked from the navbar search, showing meaning-based results next to Quarto's keyword results.
   
   Prefer (b) for robustness, and possibly (a) later. It should only appear on `statwiki.io`, as `ask/widget/src/loader.ts` does, and degrade quietly if the endpoint is down.
6. **Do not deploy the worker without the owner's go-ahead.** `cf deploy` from `ask/worker` publishes to production at `ask.statwiki.io`.

## Wrap-up

Done with the laboratories and the R runner:

- `.github/workflows/publish.yml` runs the webR unit tests and the laboratory maths tests in the `build` job, and a `labs` job runs the same tests on pull requests. None of them need `npm ci`.
- `README.md` has rows for `webr/` and `labs/`.

Still open, with search:

- `ask/README.md`: document `/search` once it exists.
- Remove this file when search is finished or dropped.

## Environment notes (cloud session)

- The cloud environment's network allowlist gained `webr.r-wasm.org` and `repo.r-wasm.org` (approved by the owner) so webR could be tested. jsdelivr is still blocked.
- **Quarto was not installed**: the download was refused by the session's safety check. To run `python build_wiki.py`, a scratch shim stood in for `quarto` and forwarded `quarto pandoc …` to the system pandoc 3.1.3. Quarto 1.6.40 bundles a different pandoc, so treat that build as a smoke test only. Nothing in the repo depends on the shim.
- webR under Node behind a proxy needs `NODE_USE_ENV_PROXY=1 NODE_EXTRA_CA_CERTS=<ca bundle>`, and R's own downloads inside webR still bypass it. That is why `check-blocks.mjs` has its own pass-through mirror.
- Playwright's Chromium needs `proxy: { server: HTTPS_PROXY }` behind a proxy. `webr/test/e2e.mjs` already does this.

## Commands

```
cd webr && npm ci && npm test
cd webr && node check-blocks.mjs            # needs repo.r-wasm.org; several minutes
cd webr && node test/e2e.mjs                # needs webr.r-wasm.org and repo.r-wasm.org
node --test labs/kde-math.test.mjs
python build_wiki.py && quarto render
```
