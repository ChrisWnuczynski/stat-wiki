# Random sample

Type: Concept/definition.

## Material checked

- The generated article before this edit had 245 body words, no figures, the iid definition, the sample-mean and sample-variance moment result, the normal-sample theorem, and thirteen distinct question links. The definition cited Casella–Berger and Wasserman passages that were unavailable for this page.
- The shared definition in `sources/stat2004/chapters/inf-01-statistical-inference.qmd`, the two linked property pages, the simple-random-sample page, the citation map, and all listed question links.

## Sources opened and used

1. Kyle Siegrist, [*Probability, Mathematical Statistics, and Stochastic Processes*, §6.1, “Introduction”](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/06:_Random_Samples/6.01:_Introduction), especially “The Basic Statistical Model,” “Statistics,” “Difficulties,” and “Random Samples.” Read the iid definition and statistical interpretation. New key `siegrist2022_random_samples`.
2. Siegrist, [§6.5, “The Sample Variance”](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/06:_Random_Samples/6.05:_The_Sample_Variance), “The Standard Sample Variance.” Read the mean–variance definitions and expectation argument. Existing key `siegrist2022_sample_variance`.
3. Siegrist, [§6.8, “Special Properties of Normal Samples”](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/06:_Random_Samples/6.08:_Special_Properties_of_Normal_Samples), “The One Sample Model.” Read its normal-mean, chi-squared variance and independence proofs. Existing key `siegrist2022_normals`.
4. R. A. Fisher, [“On the Mathematical Foundations of Theoretical Statistics”](https://www.stats.org.uk/statistical-inference/Fisher1922.pdf), *Philosophical Transactions A* **222** (1922), §§2–3, pp. 312–316. Read the sample/population interpretation and its connection to statistics and likelihood. Existing key `fisher1922` supports History only.
5. Statistics Canada, [*Survey Methods and Practices*](https://www150.statcan.gc.ca/n1/pub/12-587-x/12-587-x2003001-eng.pdf) (2003), §6.2.2, pp. 93–94. Read the equal-probability fixed-size design and its contrast with sampling with replacement. New key `statistics_canada2003_survey`.
6. Nelder and Wedderburn, [“Generalized Linear Models”](https://www.maths.usyd.edu.au/u/jchan/GLM/Nelder1972GLM.pdf), §§1.1–1.3, pp. 371–373, reopened from the preceding GLM pass to check the independent, non-identically-distributed regression comparison. Existing key `nelder_wedderburn1972`.

## Changes and checks

- Added a plain-language lead context, battery example, fully symbolised iid definition and joint factorisation, interpretation, statistical use, a numerical Bernoulli example, specific relationships, and two cited History paragraphs. One collapsed proof covers the product form, both general sample moment formulas, and all three normal-sample conclusions. The earlier property statements and thirteen question links remain.
- Replaced unopened Casella–Berger and Wasserman citations in the shared definition with the opened Siegrist section and a locator. The random-sample citation map is now page-specific; the other members of the former shared map retain their mapping.
- `checks/random-sample.py` asserts the exact printed fractions and sample variance, proof count, source keys, figure count and thirteen distinct question links. The numerical Bernoulli example was computed with exact fractions.

## Verification

Generated article: 1,775 body words versus 245 before; zero figures versus zero before; thirteen distinct question links; one collapsed Proof box. The exact-value check passes. The generator produced 718 articles and 557 question pages, all 67 Python tests pass, and offline validation passes for 412 bibliography entries. `git diff --check` is clean. The temporary Quarto-to-Pandoc shim used in the preceding page was used for the generator's sole `quarto pandoc` call. No rendered HTML build was attempted.
