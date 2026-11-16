# Saturated model

Type: Concept/definition. Rank 173.

## Material checked

- **Checked:** Frozen baseline: 197 body words, no figures, original definition, three question links and three cited source keys. The new article retains these and adds the Poisson worked calculation.
- **Checked:** Nelder and Wedderburn (1972), full original paper, §2.3 p. 375 and §2.4 p. 376, university faculty-hosted copy of the published article. Their “complete” model fits exactly; they define deviance from its likelihood, list family forms and give residual degrees of freedom.
- **Checked:** R `glm` manual, Value (null and residual deviance), and R `family` manual, Details (binomial response representations) and Value (`dev.resids`). These are full official documentation pages, opened through web access.
- **Checked by code:** Poisson deviance contributions for `(0,2,4)` against mean two and `(1,3)` against mean two; exact identities and rounded values in `checks/saturated-model.py`.
- **Assumed:** The displayed count examples use independent Poisson responses. The simple likelihood identities hold at fixed dispersion and for the same family and observations; a chi-squared calibration needs additional conditions.
- **Disputed:** The old plain definition said a saturated fit “predicts nothing.” It can mechanically produce a prediction if supplemented with a rule, but the saturated parameters alone provide no generalizable predictor for a new observation; the new text makes that distinction. A Bernoulli saturated logit parameter is a boundary limit, not finite.

## Sources opened and used

1. Nelder and Wedderburn, “Generalized Linear Models,” *JRSS A* **135** (1972), §§2.3–2.4, pp. 375–376, full paper hosted by McGill faculty at `https://jhanley.biostat.mcgill.ca/bios601/Likelihood/NelderWedderburn1972.pdf`; existing key `nelder_wedderburn1972`.
2. R Core Team, `glm` manual, Description, Details and Value, `https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html`; existing key `rstats_glm2026`.
3. R Core Team, `family` manual, Details and Value, `https://stat.ethz.ch/R-manual/R-devel/library/stats/html/family.html`; existing key `rstats_family2026`.

Dodge's index has no saturated-model or deviance entry. Its likelihood-ratio-test entry is nearby background, but this page makes its historical attribution directly from the original GLM paper.

## Changes and checks

One collapsed proof covers the Poisson saturated optimizer, nonnegative deviance, nested deviance identity and normal known-variance case. The two existing answered question-bank pages are requested as hidden self-checks in pending shared changes. Full build, tests and verification results recorded in the commit run.
