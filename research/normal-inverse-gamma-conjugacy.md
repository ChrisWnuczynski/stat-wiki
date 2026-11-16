# Normal–inverse-Gamma conjugacy — research notes (rank 207)

## Sources read

- Checked: Gelman et al. (2013), *Bayesian Data Analysis*, complete author-hosted third-edition PDF, https://sites.stat.columbia.edu/gelman/book/BDA3.pdf, opened 2026-11-16. Chapter 3 §3.3, pp. 67–69, gives normal–inverse-chi-squared joint conjugacy, parameter update, dependence of mean and variance, and Student marginal.
- Checked: Forssén and Ekström, *Learning from data*, full public Chalmers University online lecture chapter, https://cforssen.gitlab.io/tif285-book/content/BayesianStatistics/BayesianLinearRegression/BayesianLinearRegression_ConjugatePrior.html, opened 2026-11-16. Chapter 25 §§25.1–25.3, especially equations 25.2, 25.7–25.8, states the regression normal–inverse-Gamma prior, posterior and marginal Student law. Preface identifies the site as Chalmers lecture notes. Site lacks a publication date; pending bibliography uses 2026 as accessed edition, not a verified first publication date.
- Checked: source chapter sources/book/chapters/bayes-09-linear-regression.qmd and generated theorem. The statement, collapsed proof, detailed inverse-chi-squared example and original question links are preserved.
- Checked by code: intercept-only design, posterior parameters, inverse-Gamma mean and mode and Student scales in worked and practice examples.
- Assumed: iid Gaussian errors with common positive variance, a positive-definite prior scale and positive inverse-Gamma hyperparameters. The numeric example is conditional on these modelling assumptions.
- Disputed: V_n is not the marginal coefficient covariance, and b_n is not the posterior variance mean; those need the inverse-Gamma moment and may fail to exist when shape is too small.
- Dodge: index has no normal–inverse-Gamma entry.

## Preservation

Baseline has 3,319 words and zero figures. Its long example, source theorem, and existing proof remain generated; research content supplements them.
