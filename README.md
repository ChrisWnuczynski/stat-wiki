# stat wiki

A Wikipedia-style study wiki for STAT3500/7500, built with Quarto.

The site: <https://chriswnuczynski.github.io/stat-wiki/>

## How it is built

`build_wiki.py` turns the course files in `sources/` into the wiki's pages. `quarto render` then turns those pages into the website in `_site/`.

On every push to `main`, GitHub runs both steps and publishes the result. It takes about 4 minutes, and progress shows in the [Actions tab](https://github.com/ChrisWnuczynski/stat-wiki/actions). The generated pages are not stored in the repository.

## What to edit

| To change | Edit |
|---|---|
| Chapters, questions and answers | the files in `sources/` |
| Article properties, examples and pictures | `article_extras.py` |
| Page layout, links and infoboxes | `build_wiki.py` |
| Colours, fonts and dark mode | `styles.css` |

The build reads only the copies in `sources/`:

- `sources/book` comes from the lecture book (the Alan Book folder).
- `sources/prep` comes from the final-exam booklet (FINAL PREP).
- `sources/practice` comes from the practice set (Codex Notes).
- `sources/stat2003` holds the probability notes. The chapters are `sources/stat2003/chapters`, and the PDF copy is `sources/stat2003/notes.pdf`.

Edits to the original folders do not reach the wiki until they are copied into `sources/`.

## Publishing a change

Edit a file on GitHub and commit it. The site updates by itself.

To publish edits made in the local folder instead, run:

```
powershell -ExecutionPolicy Bypass -File publish.ps1 "What changed"
```

It commits everything, brings in any changes made on GitHub, and pushes.

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
