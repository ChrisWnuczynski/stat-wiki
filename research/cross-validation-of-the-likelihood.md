# Cross validation of the likelihood

Generator input: [research prose](content/cross-validation-of-the-likelihood.md). Numerical verification: [Python check](../checks/cross-validation-of-the-likelihood.py).

## Sources read

- `rasmussen_williams2006` (§5.4.2, pp. 116–117)
- `rasmussen_williams2006` (§5.4.2, eqs. 5.10–5.11, p. 116)
- `cawley_talbot2010` (§1, pp. 2079–2081)
- `rasmussen_williams2006` (§5.3, pp. 110–112)
- `goodfellow_bengio_courville2016` (§3.13, eqs. 3.50–3.51, pp. 72–73)
- `cawley_talbot2010` (§2, pp. 2081–2084)

## Calculations

Independently evaluated both four-observation log scores, the change-of-units shift, the Gaussian predictive log-density identity and the KL score rearrangement. Generated text is checked against the numerical results.

## Validation

Final build, all fifteen page checks, offline citation validation and full unit suite are recorded in the batch report. Shared corrections are staged outside tracked inputs for orchestrator integration.
