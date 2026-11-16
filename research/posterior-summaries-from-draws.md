# Posterior summaries from draws — research notes (rank 209)

## Sources read

- Checked: Geyer (1992), *Practical Markov Chain Monte Carlo*, full original paper at https://www2.stat.duke.edu/homeweb/scs/Courses/Stat376/Papers/GeyerStatSci1992.pdf, opened 2026-11-16. §§1–3, pp. 473–479 distinguish chain averages from independent Monte Carlo and discuss their error using autocovariance; §3.6 addresses spacing.
- Checked: Wang (2025), *Foundations of Probability and Statistical Theory*, full author-hosted Chapter 20, https://wanghemath.github.io/Book-ProbabilityStatisticalTheory/chapters/chapter-20-bayesian-inference.html, opened 2026-11-16. §§24.1–24.2 and 28.1 distinguish posterior mean, median, mode, and equal-tail credible intervals.
- Checked: Wang (2025), same full author-hosted textbook, Chapter 9 at https://wanghemath.github.io/Book-ProbabilityStatisticalTheory/chapters/chapter-09-convergence-theory.html, opened 2026-11-16. §§18–19 state weak and strong laws of large numbers used in the iid part of the proof.
- Checked: sources/book/chapters/bayes-01-foundations.qmd, proposition and examples. Original 1000-draw order-statistic convention, mode warning, source examples and linked questions must remain.
- Checked by code: example means, sample variance, event frequencies and empirical quantiles; finite-sample variance-bias convention and Bernoulli Monte Carlo standard error.
- Assumed: exact iid posterior draws for the simple finite-sample worked example; dependent MCMC requires convergence/ergodicity and autocorrelation-aware Monte Carlo error.
- Disputed: the empirical spread of posterior draws is not the numerical uncertainty of their mean; the most repeated continuous draw is not a mode estimator.
- Dodge: index has no direct posterior-summaries entry.

## Preservation

Baseline has 1,470 words and zero figures. Preserve the source proposition, all examples, and question links. Existing proof debt should be removed when the collapsed proof is integrated.
