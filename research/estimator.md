# Estimator

Type: Concept/definition.

## Existing material read

- `articles/estimator.qmd` before the edit: definition distinguishing the random rule $T$ from its observed value $t$, ten-thermometer example with four compliant items, original citations, and 12 linked questions. Leading body: 259 words; no figures.
- `sources/stat2004/chapters/inf-02-estimation.qmd` around the estimator definition and the bias–variance and MSE discussion.
- `questions/ex-inf-poisson-mle.qmd`, `questions/ex-inf-shrunk-mean.qmd`, and `questions/ex-inf-no-uniform-risk.qmd`, including answers where present.

## Sources opened and facts used

1. R. A. Fisher, [“On the Mathematical Foundations of Theoretical Statistics”](https://www.stats.org.uk/statistical-inference/Fisher1922.pdf), original 1922 text, especially pp. 309, 313–316, and 366–367. The paper distinguishes population parameters, sample statistics used for estimation, and sampling distributions. Existing citation key `fisher1922`.
2. Penn State Department of Statistics, [STAT 415 Lesson 2](https://online.stat.psu.edu/stat415/Lesson02) and [Lesson 3](https://online.stat.psu.edu/stat415/Lesson03), search-index passages checked for bias, variance, MSE, and the Bernoulli sample proportion. Direct page fetch timed out, so the lessons are corroboration only, not cited in the article.
3. The existing source chapter's point-estimation discussion and its citations to Casella and Berger (2002), Lehmann and Casella (1998), and Wasserman (2004). The publishers' full book texts were unavailable; all new equations are independently proved in the collapsed box and numerically checked. Existing keys `casella_berger2002`, `lehmann_casella1998`, and `wasserman2004`.
4. NIST [Glossary](https://www.itl.nist.gov/div898/handbook/glossary.htm), consulted earlier for the meanings of sampling distribution and standard error. Existing key `nist_glossary2002`.

## Verification and decisions

- The original definition, ten-thermometer data and result, three original citations, and all 12 question links remain. No figure or worked example was removed.
- The new proof covers MSE decomposition, sample-mean moments, Bernoulli proportion moments and consistency, and its maximum-likelihood property including boundary samples.
- The worked example distinguishes the plug-in standard error from the sampling standard deviation at a specified true parameter. `checks/estimator.py` recomputes both examples and the proof's small cases.
- The “No uniform winner” exercise asserts a universal claim that fails when the laws at two parameter values are mutually singular. Its link remains for preservation; the claim is not repeated in this article and is recorded in `research/todo.md` for a future exercise correction.
