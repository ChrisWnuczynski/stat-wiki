# Cholesterol and heart disease — research notes (rank 214)

## Sources read

- Checked: sources/book/chapters/01-introduction-to-glms.qmd, §§“Disease and cholesterol” and “The cholesterol fit,” including the one-hundred-patient description, scatterplot, displayed logistic fit and conditional sex interpretation. Also read 05-comparisons-and-deviance.qmd for the linked three-link comparison.
- Checked: Nelder and Wedderburn (1972), full original GLM paper from McGill University course archive, https://jhanley.biostat.mcgill.ca/bios601/Likelihood/NelderWedderburn1972.pdf, opened 2026-11-16. §§1 and 3.3, pp. 370–380 give the binomial/linear-predictor/link framework used to read the displayed fit.
- Checked: Geyer (2022), full author-hosted exponential-families chapter, https://www.stat.umn.edu/geyer/f22/5421/notes/expfam.html, opened 2026-11-16, §7.1 gives inverse logit, Bernoulli mean and natural parameter.
- Checked by code: printed coefficient-to-odds conversions, intercept probability, conditional fitted probabilities, and fit comparison identities where possible.
- Assumed: the disease indicator and cholesterol measurements in the chapter are correctly recorded; the plot shows the intended hundred-patient teaching sample.
- Disputed/unverified: `data/cholest.csv` is absent from this checkout (as noted in PROGRESS rank 56). The fitted coefficients, group comparisons and figure cannot be independently refit or traced to a documented clinical source. Preserve them and check only their internal arithmetic. Avoid claims of causation, population representativeness or external validation.
- Dodge: no dataset entry.

## Preservation

Baseline has 1,605 words and one figure. Keep the plot, reported coefficients, original examples and question links. Dataset page should identify its sampling/provenance limit without inventing metadata.
