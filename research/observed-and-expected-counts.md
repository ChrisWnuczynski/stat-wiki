# Observed and expected counts

Type: Concept/topic. Rank 42.

## Material checked

- Frozen baseline: 254 body words, no figures, and 13 related questions. The generated article contained the Pearson count formula, the hundred-balls example, and a short lead.
- Read the chi-squared chapter `sources/stat2004/chapters/inf-05-chi-square.qmd`, the examples chapter `sources/stat1301/chapters/da-09-chi-square-examples.qmd`, and the two answered questions selected for this page.

## Sources opened and used

1. [NIST/SEMATECH e-Handbook §1.3.5.15](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35f.htm), especially the test-statistic and critical-region subsections, for observed and expected bin counts, CDF-based expectations, bin sensitivity, and the chi-squared reference with estimated parameters. Key `nist_chi_square_gof2002` points to the official NIST page.
2. [NIST/SEMATECH e-Handbook §7.4.5](https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm), especially expected cell frequencies and degrees of freedom, for fitted independence expectations and contingency-table calculations. Key `nist_contingency2002` points to the official NIST page.
3. [NIST Dataplot reference, Chi Square Goodness of Fit Test](https://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/chsqgood.htm), description, for the usual minimum expected-frequency rule and combining sparse tail bins. Key `nist_dataplot_chisq_gof2002` points to the official NIST page.
4. Prakash Gorroochurn, [“Karl Pearson's Chi-Squared Goodness-of-Fit Test”](https://doi.org/10.1002/9781119127963.ch3), in *Classic Topics on the History of Modern Mathematical Statistics* (Wiley, 2016), Ch. 3, pp. 293–347. The publisher summary confirms the 1900 paper's role, and the publisher book listing and table of contents locate §3.2.2 on p. 299 and §3.3.1 on p. 306. Key `gorroochurn2016_pearson` points to the publisher DOI.

All new URLs are official institutional or publisher pages, with no unauthorised copies.

## Changes and checks

- Added a four-colour motivating example, count definitions for specified and fitted probabilities, interpretation, conservation properties, a collapsed proof, a four-colour worked example, and a hidden “Your turn” answer. The page distinguishes known-probability goodness of fit from independence-table expectations and from fitted-parameter tests.
- Replaced unlocated book citations in the inherited Pearson definition with the opened NIST source. The hundred-balls excerpt in its source chapter now has a located NIST citation. The historic Pearson claim remains, now sourced to a page-located secondary history.
- Selected two answered bank questions, the frizzled-chicken and die-fairness problems, for the generated “Check yourself” section.
- The page check computes all new printed values from exact fractions, checks the fitted-margin identity on a separate two-by-two table, verifies the citation keys and proof/practice sections, and preserves all 13 question links.

## Verification

The generator completed 718 articles and 557 question pages. The generated article has 2,478 body words versus 254 before and still has no figures. All 42 page arithmetic checks, 67 Python tests, offline verification of 432 bibliography entries, and the overview link check pass. Quarto is unavailable in this workspace, so the generator uses the Pandoc shim for its conversion step.
