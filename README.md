# StatWiki

A Wikipedia-style study wiki for data analysis, probability, stochastic processes, statistical learning, and statistical inference, built with Quarto.

## How it is built

`build_wiki.py` turns the files in `sources/` into the wiki's pages. `quarto render` then turns those pages into the website in `_site/`.

On every push to `main`, the publish workflow runs both steps and publishes the result. It takes about 4 minutes. The generated pages are not stored in the repository.

## What to edit

| To change | Edit |
|---|---|
| Chapters, questions and answers | the files in `sources/` |
| Article properties, examples and pictures | `article_extras.py` |
| Topic pages, their titles, other names, and term links | `topics.py`. A chapter heading gets a page of its own when something names it: a link phrase, a topic, an other name, or the `PAGES` list. Other headings stay in their chapter, and any page one used to have redirects there. This file also titles headings whose own words need their chapter to make sense, adds pages for ideas named inside a paragraph, and lists the phrases that link to them. |
| Page layout, links and infoboxes | `build_wiki.py` |
| Colours, fonts and dark mode | `styles.css`. `_theme-head.html` and `_theme-body.html` apply a reader's saved dark mode before each page is drawn. |
| The browser-tab icon | `favicon.ico` (16 to 128 px) |
| The picture shown when a page is shared | `share-icon.png`, the browser-tab icon at 1200 by 630. `make_share_image.py` draws it. |
| The site's name, the home page's title in search results, and the description under each page in search results | `search_meta.py`. It runs after `quarto render`: each page gets a description from its opening sentences (or from its title when it opens with a formula), and the home page gets a longer title and WebSite structured data naming the site for Google. |
| The Ask StatWiki chat | `ask/widget` for the chat on the pages, `ask/worker` for the server at `ask.statwiki.io`. See `ask/README.md`. |
| R in the browser | `webr/`. Which pages get Run buttons is `RUNNABLE_PARTS` in `build_wiki.py`. See `webr/README.md`. |
| Laboratories | `labs/`. Kernel density, Beta–Binomial updating, a Markov chain, and confidence-interval coverage. The navigation is written in `build_wiki.py`. |
| Figures for the probability, inference and data analysis chapters | `make_figures.py` in `sources/stat2003/figures`, `sources/stat2004/figures` or `sources/stat1301/figures`, then commit the PDFs it writes. A `.tex` file beside a PDF is its TikZ source. |
| Data behind the data analysis figures | `sources/stat1301/data` (heart-failure records and `birthwt`) |

The build reads only the copies in `sources/`:

- `sources/book` comes from the lecture book (the Alan Book folder).
- `sources/prep` comes from the final-exam booklet (FINAL PREP).
- `sources/practice` comes from the practice set (Codex Notes).
- `sources/stat2003` holds the probability notes. The chapters are `sources/stat2003/chapters`, and the PDF copy is `sources/stat2003/notes.pdf`.
- `sources/stat2004` holds the inference notes. Only the inference part is turned into chapters; the probability part links to `sources/stat2003`. The PDF copy is `sources/stat2004/notes.pdf`.
- `sources/stat1301` holds the data-analysis notes. Studies and description become chapters. The language chapter `sources/stat1301/chapters/da-03-using-r.qmd` is filed under Using R. Repeated inference chapters keep their examples and exercises and link to `sources/stat2004`. The PDF copy is `sources/stat1301/notes.pdf`.
- `sources/using-r` holds the rest of the Using R section: exploration, simulation, resampling, mixtures, Bayesian computation, and the model fits.
- `sources/stat3004` holds the stochastic-process notes. The chapters are `sources/stat3004/chapters`, and the PDF copy is `sources/stat3004/notes.pdf`. Where a chapter continues a probability page, it links to that page and develops the further argument.
- `sources/stat3006` holds the statistical-learning notes, including the R calculations. The chapters are `sources/stat3006/chapters`, and the PDF copy is `sources/stat3006/notes.pdf`. Where a chapter continues a regression, GLM, ANOVA, or smoothing page, it links to that page and develops the further argument.

Edits to the original folders do not reach the wiki until they are copied into `sources/`.

## Publishing a change

Open a pull request from a fresh branch off current `main`. The title and description say what changed and why. The rules for bots and agents are in `AGENTS.md`.

After the pull request is merged, the site updates by itself. The publish workflow then purges the Cloudflare cache for www.statwiki.io, so a long edge TTL does not keep the previous pages. `CLOUDFLARE_PURGE_TOKEN` is a custom Cloudflare API token with only Zone > Cache Purge > Purge on statwiki.io. Until that Actions secret is set, the purge step prints a notice and does nothing.

## Checking pages locally

You need Python 3.12, Quarto 1.6 and poppler (`pdfinfo`, `pdftocairo`). Then run:

```
python build_wiki.py
quarto preview
```

Before starting a research depth pass, run `python research/check_sources.py`. It
checks the private Dodge source outside the repository and stops with a clear
error when the index, extracted pages, or PDF are missing. Set
`STATWIKI_DODGE_DIR` if the source is in another directory.

### Full validation setup

The quick start above is enough to build and preview pages, but the full
check suite — `python -m unittest discover` plus every script in `checks/` —
needs more. Several page checks shell out to R, and the browser tests and
`tools/visual_check.py` need Playwright's Chromium. Without them the suite
fails partway with missing-tool errors instead of real failures. CI pins the
exact versions in `.github/workflows/publish.yml`; match them locally:

- Python 3.12 with `matplotlib==3.10.8`, `scipy==1.17.0`, `sympy==1.14.0`
  and `scikit-learn==1.6.1`.
- R 4.5.0 with the packages the page checks use: `mgcv` 1.9.3, `rpart`
  4.1.24, `proxy` 0.4.27, `e1071` 1.7.13 and `gee` 4.13.25. The workflow
  installs them from the CRAN archive and asserts those versions.
- Quarto 1.6.40, the exact version CI uses, so pages render the same way.
- Node 22 for the `labs/`, `webr/` and search `node --test` suites and the
  Ask widget.
- Playwright with Chromium. The Ask widget's browser tests use Node
  Playwright 1.63.0 (`npx playwright install --with-deps chromium` in
  `ask/widget`); `tools/visual_check.py` uses Python Playwright
  (`pip install playwright`, then `playwright install chromium`).
- Poppler (`poppler-utils`: `pdfinfo`, `pdftocairo`) and `fonts-liberation`.

Run this preflight before the full suite; it fails fast with a clear message
when a piece is missing:

```
Rscript -e 'for (p in c("mgcv", "rpart", "e1071", "gee", "proxy")) if (!requireNamespace(p, quietly = TRUE)) stop("missing R package: ", p); cat("R packages OK\n")'
python -c "from playwright.sync_api import sync_playwright; p = sync_playwright().start(); b = p.chromium.launch(); print('Chromium OK', b.version); b.close(); p.stop()"
```

The commands to run before every push are listed in `AGENTS.md` under
"Before every push".

## Desktop app

`_app/launch_wiki.pyw` opens the local `_site` folder in its own window, and works offline. After changes made elsewhere, refresh it with:

```
git pull
python build_wiki.py
quarto render
```
