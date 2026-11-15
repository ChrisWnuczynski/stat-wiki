# Mean vector and covariance matrix

Type: Concept/definition.

## Existing material read

- `articles/mean-vector-and-covariance-matrix.qmd` before the edit: population mean and covariance definitions, positive semi-definiteness and linear-combination facts, a two-coordinate numerical calculation, and links to 39 questions. Leading body: 560 words; no figures.
- `sources/stat3006/chapters/sl-01-multivariate-normal.qmd` around its mean/covariance definition and multivariate normal construction, plus `sources/stat2003/chapters/prob-04-joint-distributions.qmd` for the parallel covariance-matrix definition.
- `questions/ex-sl-01-1.qmd`, `questions/ex-sl-01-2.qmd`, and `questions/ex-sl-01-3.qmd`, including their worked answers.

## Sources opened and facts used

1. NIST/SEMATECH, [e-Handbook §6.5.4.1, “Mean Vector and Covariance Matrix”](https://www.itl.nist.gov/div898/handbook/pmc/section5/pmc541.htm). Read its definitions, five-item measurement example, and corrected sample covariance. Key `nist_covariance2002`, already present.
2. Francis Galton, [“Regression towards Mediocrity in Hereditary Stature”](https://pdf.galton.org/essays/1880-1889/galton-1886-jaigi-regression-stature.pdf), original 1886 paper opened earlier in this research pass. Used only to contextualise paired family measurements. Key `galton1886`, already present.
3. Karl Pearson, [“Mathematical contributions to the theory of evolution—III. Regression, heredity, and panmixia”](https://doi.org/10.1098/rsta.1896.0007), *Philosophical Transactions* (1896). Publisher metadata was opened during the covariance page; the full text was inaccessible. History here is limited to verified date and subject, with no invention-of-notation claim. Key `pearson1896`, already present.
4. T. W. Anderson, *An Introduction to Multivariate Statistical Analysis* (2003), the existing standard reference cited in the source chapter for population mean/covariance formulas. Key `anderson2003_mva`, already present. Its full book was not available here; the NIST page and the book-derived source chapter supply the checked formulas.

## Verification and decisions

- The existing definition, two-coordinate calculation, interpretation, citations, and 39 question links remain; no figure or worked example was removed. The new Definition clarifies that $p$ counts coordinates and $n$ counts observations, resolving the original's mixed labels without deleting its sentence.
- A single collapsed proof covers every explicit property retained in Interpretation and added in Properties: symmetry, positive semi-definiteness, linear-combination variance, affine transformations, independent sums, trace/eigenvalue identity, correlation bound, and unbiased sample covariance.
- `checks/mean-vector-and-covariance-matrix.py` recomputes the original population-matrix numbers and the new three-pair sample matrix, contrasts, and sums.
- No claim is made about who invented the mean-vector or covariance-matrix notation; the inaccessible Pearson full text is flagged above.

## Correction pass

- The Anderson and Wasserman books and Pearson's full article were not opened for the new formulas. The extracted definition and new prose now cite the opened NIST §6.5.4.1 and Golub–Van Loan §4.2 passages, with Grinstead–Snell chapter 6 for the zero-covariance example. The Galton citation is limited to the paired-height comparison on pp. 246–247.
- The shared source definition now uses $p$ for the vector dimension and $n$ for the sample size. Removed page-assembly language, a repetitive modern-practice History paragraph, and new multivariate-normal claims that the opened passages did not verify. The arithmetic check asserts the exact numbers and matrix entries printed in the article.
