# Estimator

Type: Concept/definition.

## Existing material read

- `articles/estimator.qmd` before the edit: definition distinguishing the random rule $T$ from its observed value $t$, ten-thermometer example with four compliant items, original citations, and 12 linked questions. Leading body: 259 words; no figures.
- `sources/stat2004/chapters/inf-02-estimation.qmd` around the estimator definition and the bias–variance and MSE discussion.
- `questions/ex-inf-poisson-mle.qmd`, `questions/ex-inf-shrunk-mean.qmd`, and `questions/ex-inf-no-uniform-risk.qmd`, including answers where present.

## Sources opened and facts used

1. R. A. Fisher, [“On the Mathematical Foundations of Theoretical Statistics”](https://errorstatistics.com/wp-content/uploads/2021/04/fisher-1922.pdf), original 1922 text, especially pp. 309, 313–316, and 366–367. Opened the accessible scan and checked the sections on estimation and the distribution of statistics. Citation key `fisher1922`.
2. Penn State Department of Statistics, [STAT 415 Lesson 2](https://online.stat.psu.edu/stat415/Lesson02) and [Lesson 3](https://online.stat.psu.edu/stat415/Lesson03), search-index passages checked for bias, variance, MSE, and the Bernoulli sample proportion. Direct page fetch timed out, so the lessons are corroboration only, not cited in the article.
3. He Wang, [*Foundations of Probability and Statistical Theory*, Chapters 12–13](https://wanghemath.github.io/Book-ProbabilityStatisticalTheory/chapters/chapter-12-point-estimation1.html), §§15, 17.4 and [Chapter 13](https://wanghemath.github.io/Book-ProbabilityStatisticalTheory/chapters/chapter-13-point-estimation2.html), §§15–17, 18.2. Opened the definition of estimator and estimate, Bernoulli likelihood derivation, MSE and bias–variance theorem, and sample mean example. Citation key `wang2025_foundations`.
4. NIST [Glossary](https://www.itl.nist.gov/div898/handbook/glossary.htm), entries for sampling distribution, standard error, and sampling frame. Citation key `nist_glossary2002`.

Casella and Berger (2002), Lehmann and Casella (1998), and Wasserman (2004) were cited in the first draft but their books were not opened. The correction removes those citations from the generated Estimator article, including its inherited definition.

## Verification and decisions

- The definition, ten-thermometer data and result, and all 12 question links remain. No figure or worked example was removed.
- The new proof covers MSE decomposition, sample-mean moments, Bernoulli proportion moments and consistency, and its maximum-likelihood property including boundary samples.
- The worked example distinguishes the plug-in standard error from the sampling standard deviation at a specified true parameter. `checks/estimator.py` recomputes both examples, checks the exact rounded numbers printed on the article, and verifies the proof's small cases.
- The “No uniform winner” exercise asserts a universal claim that fails when the laws at two parameter values are mutually singular. Its link remains for preservation; the claim is not repeated in this article and is recorded in `research/todo.md` for a future exercise correction.
