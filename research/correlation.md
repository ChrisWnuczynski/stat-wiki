# Correlation

Type: Concept/definition.

## Existing material read

- `articles/correlation.qmd` before the edit: population Pearson coefficient, correlation-matrix standardisation, affine invariance and equality interpretation, a two-variable covariance calculation, and 22 linked questions. Leading body: 497 words; no figures.
- `sources/stat3006/chapters/sl-01-multivariate-normal.qmd` around its correlation definition and derivation of the best linear predictor. The original article's covariance-matrix notation is retained.
- `questions/ex-da-correlation-reading.qmd`, `questions/ex-ur-exchangeable-bound.qmd`, `questions/ex-sl-03-3.qmd`, and `questions/ex-sl-01-3.qmd`, including their available answers.

## Sources opened and facts used

1. NIST, [Dataplot Reference Manual, “CORRELATION”](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/correlat.htm), created 23 January 2013. Read its centred-sum formula, linear interpretation, and bounds. Citation key `nist_correlation2013`, added here; corporate authorship is used because the page gives no individual byline.
2. Francis Galton, [“Regression towards Mediocrity in Hereditary Stature”](https://pdf.galton.org/essays/1880-1889/galton-1886-jaigi-regression-stature.pdf), original 1886 text opened earlier in this pass. Used for narrow historical context on paired family measurements. Key `galton1886`, already present.
3. Karl Pearson, [“Mathematical contributions to the theory of evolution—III. Regression, heredity, and panmixia”](https://doi.org/10.1098/rsta.1896.0007), 1896 publisher record and an image-only scan. The article's mathematical argument could not be read, so it is no longer cited on this page.
4. He Wang, [*Foundations of Probability and Statistical Theory*](https://wanghemath.github.io/Book-ProbabilityStatisticalTheory/), Ch. 3 §4.4.2, Ch. 6 Extra Example 27, Ch. 7 Example 24. Read the population correlation definition, the Gaussian independence case, and the Cauchy–Schwarz bound with equality. Key `wang2025_foundations`.
5. Korbinian Strimmer, [*Multivariate Statistics and Machine Learning*](https://strimmerlab.github.io/publications/lecture-notes/MATH38161/), 4 September 2025, Chs. 1 and 6. Read the correlation-matrix standardization, covariance positive semi-definiteness, partial correlation, and sampling discussion. Key `strimmer2025_mva`, added in this correction.
6. Kevin Hannay, [*Introduction to Statistics and Data Science*](https://faculty.nps.edu/rbassett/_book/), 13 September 2019, Ch. 11 §11.4. Read the slope, unit-free association, and $R^2$ discussion. Key `hannay2019_statsdata`, added in this correction.
7. CDC [*Field Epidemiology Manual*, “Analyzing and Interpreting Data”](https://www.cdc.gov/field-epi-manual/php/chapters/analyze-interpret-data.html), Ch. 8, Epidemiologic Interpretation Checklist 1. Read its explicit caution about chance, selection, and confounding in observed associations. Key `dicker2025_cdc`.

## Verification and decisions

- The population definition, matrix identity, $\rho=1/2$ calculation, and all 22 question links remain. Citations to Anderson, Wasserman, and Pearson were replaced after source review.
- The collapsed proof covers the bound and equality case, affine transformation, matrix standardisation and positive semi-definiteness, the best linear predictor, and the independence distinctions. A nonconstant squared variable is used in the zero-correlation counterexample to rule out a degenerate exception.
- `checks/correlation.py` recomputes the population example and the paired-data, transformation, and nonlinear examples, and asserts that the same numbers appear in the generated page.
- History describes Galton's paired stature measurements using pp. 246–247 of the original paper. The Pearson attribution is omitted.
