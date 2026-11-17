# Gaussian process

Generator input: [research prose](content/gaussian-process.md). Numerical verification: [Python check](../checks/gaussian-process.py).

## Sources read

- `rasmussen_williams2006` (§2.2, Def. 2.1, p. 13)
- `rasmussen_williams2006` (§2.2, pp. 13–14)
- `rasmussen_williams2006` (§4.1, pp. 79–80)
- `rasmussen_williams2006` (§2.2, eqs. 2.23–2.24, p. 16)
- `durrett2019` (§7.1, Gaussian-process characterisation, p. 355)

## Calculations

Computed the one-observation posterior and both predictive variances. Symbolically transformed a joint covariance into observation/residual block-diagonal form and verified its Schur complement; checked the linked invalid covariance and Brownian covariance examples.

## Validation

Final build, all fifteen page checks, offline citation validation and full unit suite are recorded in the batch report. Shared corrections are staged outside tracked inputs for orchestrator integration.
