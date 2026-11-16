# Log link

Type: Concept. Rank 55.

## Material checked

- Frozen baseline: 573 body words, zero figures. Read the definition, three Gamma links, interpretation, exposure and unit examples, infobox and ten question links. Preserve their formulas and numbers.
- **Checked:** McCullagh's 1992 introduction to Nelder and Wedderburn, pp. 543–544, describes the exponential family, linear predictor and link as three GLM components and gives historical context. The author-hosted PDF was opened and read.
- **Checked:** Official R `family` documentation, Usage and Arguments, lists `poisson(link="log")` as default and `Gamma(link="inverse")` as default with log available; it distinguishes link and variance functions and documents quasipoisson dispersion. The shared chapter citation also uses McCullagh's read introduction and Davison's publisher extract in distinct sentences.
- **Checked by code:** multiplicative ratios, offset counts, transformed-mean counterexample, inherited numerical examples, and practice are recomputed in `checks/log-link.py`.
- **Assumed:** Exposures are positive and measured consistently; the worked count model assumes conditionally Poisson counts with rate constant over each exposure interval.
- **Disputed:** “usual Gamma log link” is context dependent because R's default Gamma link is inverse; the article calls it an available, common modelling choice without implying it is canonical or the R default.

## Sources opened and used

1. Peter McCullagh, [“Introduction to Nelder and Wedderburn (1972): Generalized Linear Models”](https://www.stat.uchicago.edu/~pmcc/pubs/paper32.pdf), in *Breakthroughs in Statistics* II (1992), pp. 543–545. Opened the author-hosted PDF and read pp. 543–544. Existing key `mccullagh1992_glm_intro`.
2. R Core Team, [*Family Objects for Models*](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/family.html), official R documentation, Usage, Arguments and Details. Existing key `rstats_family2026`.
3. A. C. Davison, [*Statistical Models*](https://www.cambridge.org/core/books/statistical-models/8EC19F80551F52D4C58FAA2022048FC7/listing), Ch. 10, §10.3 publisher extract; read its description of exponential-family responses in GLMs. Existing key `davison2003`. The extract does not support detailed link formulas; R documentation is cited for those.

Dodge index directory was absent from `~/statwiki-sources/dodge2008`.

## Changes and checks

- Add motivation, model and coefficient interpretation, one collapsed proof of ratio, offset and Poisson natural link, worked and practice arithmetic, two answered bank questions and concrete failures. Preserve inherited material and inspect the shared source chapter after build.
- The generated body has 3,926 words and zero figures. The shared paragraph also feeds inverse-link, link-function and positive-continuous-responses; after rebuilding, all three retain their formulas and each has sufficient inline citations. The 03-gamma-and-quasi chapter retains its three displayed links.
- Verification: `checks/log-link.py` passes the displayed and inherited calculations; the generator builds 718 articles and 557 questions; all 67 Python tests pass; offline verification covers 441 bibliography entries; and `git diff --check` passes. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator used the system Pandoc shim.
