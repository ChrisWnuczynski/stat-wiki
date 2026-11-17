# Iteratively reweighted least squares

Generator input: [research prose](content/iteratively-reweighted-least-squares.md). Numerical verification: [Python check](../checks/iteratively-reweighted-least-squares.py).

## Sources read

- `nelder_wedderburn1972` (§§1.3–2.1, pp. 372–374)
- `nelder_wedderburn1972` (§2.1, pp. 372–374)
- `rasmussen_williams2006` (§3.2, pp. 37–38)
- `rasmussen_williams2006` (§3.2, p. 38)
- `nelder_wedderburn1972` (§2.1, eqs. 7–9, p. 373)

## Calculations

Recomputed the logistic working response, weights, first weighted-regression step, all subsequent iterations, likelihood, score, Hessian and information-based standard errors. Checked the intercept-only zero-score step and Poisson score/information identity.

## Validation

Final build, all fifteen page checks, offline citation validation and full unit suite are recorded in the batch report. Shared corrections are staged outside tracked inputs for orchestrator integration.
