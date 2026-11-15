# Median

Type: Concept/topic.

## Material checked

- The generated article before this edit had 214 body words, no figures, a short sample definition, a population-median condition, and five distinct question links. Its sample definition cited unopened Tukey, Fisher 1925, and Wasserman books without locations.
- The median topic data, the descriptive-statistics chapter definition, the sample-quantile and Cauchy pages, and the linked questions.

## Sources opened and used

1. Kyle Siegrist, [*Probability, Mathematical Statistics, and Stochastic Processes*, §6.6, “Order Statistics”](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/06:_Random_Samples/6.06:_Order_Statistics), “Order Statistics,” “The Sample Median,” and “Sample Quantiles.” Read the odd and even formulas, median interval, and quantile relationship. New key `siegrist2022_order_statistics`.
2. Siegrist, [§3.6, “Distribution and Quantile Functions”](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/03:_Distributions/3.06:_Distribution_and_Quantile_Functions), “Quantile Functions” and “Special Quantiles.” Read the population-quantile definition and nonuniqueness cases. New key `siegrist2022_quantiles`.
3. NIST/SEMATECH, [*e-Handbook of Statistical Methods*, §1.3.5.1, “Measures of Location”](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm). Read the sample median formula, robustness discussion, and normal, exponential, Cauchy and lognormal comparisons. The [NIST publication page](https://www.nist.gov/publications/handbook-151-nistsematech-e-handbook-statistical-methods) confirms the 2002 edition and authors. New key `nist_location2002`.
4. Neil Schwertman, A. J. Gilks and J. Cameron, [“A Simple Noncalculus Proof That the Median Minimizes the Sum of the Absolute Deviations”](https://tommasorigon.github.io/StatI/approfondimenti/Schwertman1990.pdf), *The American Statistician* **44** (1990), Theorem and proof, p. 38. Read the full one-page proof and publication metadata. New key `schwertman_gilks_cameron1990`.
5. Siegrist, [§6.5, “The Sample Variance”](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/06:_Random_Samples/6.05:_The_Sample_Variance), “Measures of Center and Spread,” for the squared-error comparison. Existing key `siegrist2022_sample_variance`.

## Changes and checks

- Added precise order-statistic notation, the even-sample median interval, a population-CDF equivalent, a numerical odd and even example, interpretation, robustness bounds, affine equivariance, statistical use, and exact relationships to quantiles, boxplots and the Cauchy law. One collapsed proof covers absolute-error minimization, the squared-error contrast, affine transformations and the one-replacement bound.
- Replaced the three unopened citations in the shared source definition with located citations to opened Siegrist and NIST sections. The median citation map is page-specific, leaving related article mappings in place. The repeated sample-definition wording in `topics.py` was replaced by the more specific population condition; the chapter still supplies the sample definition, and researched prose gives both formulas. This is the only content removed as genuine duplication.
- The origin and early naming of the median were not checked from an original source. The History section is omitted and the question is recorded in `todo.md`.
- `checks/median.py` asserts every printed example number and formula, the five question links, source keys, figure count and single Proof box.

## Verification

Generated article: 1,481 body words versus 214 before; zero figures versus zero before; five distinct question links; one collapsed Proof box. The exact-value check passes. The generator produced 718 articles and 557 question pages, all 67 Python tests pass, and offline validation passes for 416 bibliography entries. `git diff --check` is clean. The temporary Quarto-to-Pandoc shim was used for the generator's sole `quarto pandoc` call. No rendered HTML build was attempted.
