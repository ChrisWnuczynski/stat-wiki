# Intraclass correlation

Generator input: [research prose](content/intraclass-correlation.md). Numerical verification: [Python check](../checks/intraclass-correlation.py).

## Sources read

- `laird_ware1982` (§2, pp. 964–965)
- `laird_ware1982` (§2, p. 965)
- `bates_lme4_2015` (§1.1, linear mixed models)
- `laird_ware1982` (§2, marginal covariance, p. 965)
- `bates_lme4_2015` (§1.1, covariance parametrisation)

## Calculations

Constructed the random-intercept covariance, recomputed the ICC, group-mean variance, design multiplier and effective independent sample size, and checked exchangeable eigenvalues including the negative-correlation counterexample.

## Validation

Final build, all fifteen page checks, offline citation validation and full unit suite are recorded in the batch report. Shared corrections are staged outside tracked inputs for orchestrator integration.
