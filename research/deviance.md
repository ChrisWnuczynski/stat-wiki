# Deviance

Type: Concept. Rank 56.

## Material checked

- Frozen baseline: 639 body words, one cholesterol-links figure. Read the four family formulas, cholesterol code and its reported deviances and AIC, discussion of nonnested links, infobox and four question links. Retain these. The original `data/cholest.csv` is absent from this checkout, so the fitted cholesterol values cannot be independently reproduced; their internal AIC arithmetic and degrees of freedom are checked.
- **Checked:** McCullagh's introduction to Nelder and Wedderburn, pp. 543–544, sets GLM fitting and response-family context. The author-hosted PDF was opened. Official R `glm` documentation, Value, defines reported `deviance`, `null.deviance`, AIC and degrees of freedom; official R `family` documentation, Value and Details, defines family-level deviance residuals, variance and dispersion. These support the software interpretation and comparison convention.
- **Checked by derivation:** Poisson, binomial, normal and Gamma deviance formulas are derived from their likelihoods in one collapsed Proof box. The zero-count convention and nested-model deviance difference are also derived there.
- **Checked by code:** the three-count worked and two-count practice contributions, inherited cholesterol AIC relationships and q34 numerical comparisons are recomputed in `checks/deviance.py`.
- **Assumed:** The worked Poisson counts are independent and the proposed means are positive. Fitted means are supplied rather than estimated from a specified regression, so no degrees of freedom or p-value is inferred.
- **Disputed:** A nonnested link pair lacks the *usual nested chi-squared* likelihood-ratio test, but other comparison methods exist. The inherited source text says “We cannot test that improvement”; the new article qualifies this claim. A low training deviance alone is not evidence of predictive adequacy.

## Sources opened and used

1. Peter McCullagh, [“Introduction to Nelder and Wedderburn (1972): Generalized Linear Models”](https://www.stat.uchicago.edu/~pmcc/pubs/paper32.pdf), in *Breakthroughs in Statistics* II (1992), pp. 543–545. Author-hosted PDF, read pp. 543–544. Existing key `mccullagh1992_glm_intro`.
2. R Core Team, [*Family Objects for Models*](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/family.html), official R documentation, Usage, Arguments, Details and Value. Existing key `rstats_family2026`.
3. R Core Team, [*Fitting Generalized Linear Models*](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html), official R documentation, Value, especially entries for `deviance`, `aic`, `null.deviance`, `df.residual` and `df.null`. New key `rstats_glm2026`.

Dodge index directory was absent from `~/statwiki-sources/dodge2008`.

## Changes and checks

- Add likelihood interpretation, the four-family proof, worked and practice count examples, concrete failures and two answered bank questions. Preserve the inherited cholesterol figure and values.
- The generated body has 4,167 words and retains its one cholesterol-links figure. The narrowed nested-test wording also appears correctly in null-deviance and the shared chapter after build. The fitted cholesterol output remains unverified numerically because `data/cholest.csv` is absent; its AIC arithmetic, ranking and degrees of freedom are internally consistent.
- Verification: `checks/deviance.py` passes the new calculations and inherited internal numbers; the generator builds 718 articles and 557 questions; all 67 Python tests pass; offline verification covers 442 bibliography entries; and `git diff --check` passes. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator used the system Pandoc shim.
