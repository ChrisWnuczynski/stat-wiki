# stat wiki

A Wikipedia-style study wiki for data analysis, probability, stochastic processes, statistical learning, and statistical inference, built with Quarto.

## How it is built

`build_wiki.py` turns the files in `sources/` into the wiki's pages. `quarto render` then turns those pages into the website in `_site/`.

On every push to `main`, the publish workflow runs both steps and publishes the result. It takes about 4 minutes. The generated pages are not stored in the repository.

## What to edit

| To change | Edit |
|---|---|
| Chapters, questions and answers | the files in `sources/` |
| Article properties, examples and pictures | `article_extras.py` |
| Topic pages, their titles, other names, and term links | `topics.py`. Every chapter heading gets a page of its own automatically; this file names the ones whose heading needs its chapter to make sense, adds pages for ideas named inside a paragraph, and lists the phrases that link to them. |
| Page layout, links and infoboxes | `build_wiki.py` |
| Colours, fonts and dark mode | `styles.css` |
| The browser-tab icon | `favicon.ico` (16 to 128 px) |
| The picture shown when a page is shared | `share-icon.png`, the browser-tab icon at 1200 by 630. `make_share_image.py` draws it. |
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

Edit a file in the repository and commit it. The site updates by itself.

To publish edits made in the local folder instead, run:

```
powershell -ExecutionPolicy Bypass -File publish.ps1 "What changed"
```

It commits everything, brings in any remote changes, and pushes.

## Checking pages locally

You need Python 3.12, Quarto 1.6 and poppler (`pdfinfo`, `pdftocairo`). Then run:

```
python build_wiki.py
quarto preview
```

## Desktop app

`_app/launch_wiki.pyw` opens the local `_site` folder in its own window, and works offline. After changes made elsewhere, refresh it with:

```
git pull
python build_wiki.py
quarto render
```
