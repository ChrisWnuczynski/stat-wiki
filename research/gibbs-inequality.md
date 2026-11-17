# Gibbs inequality

Generator input: [research prose](content/gibbs-inequality.md). Numerical verification: [Python check](../checks/gibbs-inequality.py).

## Sources read

- `goodfellow_bengio_courville2016` (§3.13, eqs. 3.50–3.51, pp. 72–73)
- `goodfellow_bengio_courville2016` (§3.13, eq. 3.50, p. 72)
- `shannon1948` (§6, Thm. 2)
- `goodfellow_bengio_courville2016` (§3.13, eq. 3.51, p. 73)
- `goodfellow_bengio_courville2016` (§3.13, p. 72)
- `goodfellow_bengio_courville2016` (§3.13, pp. 72–73)

## Calculations

Checked both directed binary KL values, entropy and cross-entropy identities, zero-support conventions and the logarithm inequality with symbolic calculus and representative probability vectors.

## Validation

Final build, all fifteen page checks, offline citation validation and full unit suite are recorded in the batch report. Shared corrections are staged outside tracked inputs for orchestrator integration.
