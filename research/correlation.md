# Correlation

Type: Concept/definition.

## Existing material read

- `articles/correlation.qmd` before the edit: population Pearson coefficient, correlation-matrix standardisation, affine invariance and equality interpretation, a two-variable covariance calculation, and 22 linked questions. Leading body: 497 words; no figures.
- `sources/stat3006/chapters/sl-01-multivariate-normal.qmd` around its correlation definition and derivation of the best linear predictor. The original article's covariance-matrix notation is retained.
- `questions/ex-da-correlation-reading.qmd`, `questions/ex-ur-exchangeable-bound.qmd`, `questions/ex-sl-03-3.qmd`, and `questions/ex-sl-01-3.qmd`, including their available answers.

## Sources opened and facts used

1. NIST, [Dataplot Reference Manual, “CORRELATION”](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/correlat.htm), created 23 January 2013. Read its centred-sum formula, linear interpretation, and bounds. Citation key `nist_correlation2013`, added here; corporate authorship is used because the page gives no individual byline.
2. Francis Galton, [“Regression towards Mediocrity in Hereditary Stature”](https://pdf.galton.org/essays/1880-1889/galton-1886-jaigi-regression-stature.pdf), original 1886 text opened earlier in this pass. Used for narrow historical context on paired family measurements. Key `galton1886`, already present.
3. Karl Pearson, [“Mathematical contributions to the theory of evolution—III. Regression, heredity, and panmixia”](https://doi.org/10.1098/rsta.1896.0007), 1896 publisher record. Full text was inaccessible; only publication date and topic are used in History. Key `pearson1896`, already present.
4. Anderson, *An Introduction to Multivariate Statistical Analysis* (2003), the existing source-chapter reference for population and matrix identities. Its full text was unavailable, so the derivations were independently checked against the source chapter and NIST's definitions. Key `anderson2003_mva`.
5. CDC [Field Epidemiology Manual, “Analyzing and Interpreting Data”](https://www.cdc.gov/field-epi-manual/php/chapters/analyze-interpret-data.html), opened for the preceding explanatory-variable article. Used only for the observational-association caveat. Key `dicker2025_cdc`.

## Verification and decisions

- The original population definition, matrix identity, $\rho=1/2$ calculation, citations, and all 22 question links remain. No figure or worked example was removed.
- The collapsed proof covers the bound and equality case, affine transformation, matrix standardisation and positive semi-definiteness, the best linear predictor, and the independence distinctions. A nonconstant squared variable is used in the zero-correlation counterexample to rule out a degenerate exception.
- `checks/correlation.py` recomputes the old population example and the new paired-data, transformation, and nonlinear examples.
- History does not attribute modern correlation notation or its formula to the inaccessible Pearson paper.
