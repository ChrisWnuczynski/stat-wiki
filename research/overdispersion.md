# Overdispersion — rank 128

Type: Concept. Baseline: 394 body words, zero figures, seven question links. The pre-pass generated page was read; its Poisson generating-function derivation, quasi-Poisson distinction, R family reference, negative-binomial alternative, infobox values and all question links are retained.

## Material checked

- **Checked:** Hua Zhou's [UCLA GLM lecture](https://ucla-biostat-200c-2020spring.github.io/slides/09-glm/glm.html), “Exponential family distribution,” Examples 1–4 and Moments, was opened in full. Its Poisson example gives $E(Y)=\operatorname{Var}(Y)=\mu$, and its general form distinguishes dispersion from the mean.
- **Checked:** R Core Team's official [family](https://search.r-project.org/R/refmans/stats/html/family.html) manual, “Details” and “Value,” was opened. It distinguishes the fixed Poisson dispersion from free quasi-Poisson dispersion and states that quasi families provide neither AIC nor simulation.
- **Checked:** R Core Team's official [summary.glm](https://search.r-project.org/R/refmans/stats/html/summary.glm.html) manual was opened. Its “Details” gives the Pearson chi-squared over residual degrees of freedom estimate and scaled coefficient covariance.
- **Checked:** R Core Team's official [negative binomial](https://search.r-project.org/R/refmans/stats/html/NegBinomial.html) manual was opened. “Details” gives the gamma–Poisson mixture and $\mu+\mu^2/k$ variance.
- **Checked:** R. A. Bailey's author-hosted [Nelder historical lecture](https://webspace.maths.qmul.ac.uk/r.a.bailey/neldbeam.pdf), slide 23/32, was opened. It records the 1972 Nelder–Wedderburn GLM scheme and its response-family examples.
- **Checked by code:** the generating-function moments, two-group variance decomposition, five-night Pearson estimate, adjusted standard error and hidden practice arithmetic are asserted in `checks/overdispersion.py`.
- **Assumed:** all worked nightly counts are illustrative observations, not records from an actual clinic. The simple Pearson calibration assumes independent counts and an adequate mean model.
- **Disputed:** “overdispersion” can describe excess variance relative to different reference families. The page states the Poisson conditional benchmark explicitly. A raw sample variance-to-mean ratio in a heterogeneous sample is not a conclusive diagnosis.

## Dodge and inherited sources

Dodge's `index.tsv` points to printed p. 168, “Dispersion”; the entry concerns descriptive spread and does not establish the GLM-specific claims here. The inherited article cites Wedderburn (1974), McCullagh and Nelder (1989), and Davison (2003). Those citations remain in the generated source excerpt; the new narrative cites only the sources opened above. The publisher abstract of Wedderburn's paper and a metadata listing of the Nelder–Wedderburn paper were located, but neither was used to support a new mathematical claim.

## Result

The one collapsed proof derives the Poisson variance, gamma–Poisson mixture variance and common-scale quasi-score equality. There is no new unproved stated result. The two selected answered bank questions, `q-47` and `q-54`, test quasi-Poisson inference and interpretation without duplicating the page's numeric examples. Their IDs are in the page-local pending manifest for integration into the shared self-check map.
