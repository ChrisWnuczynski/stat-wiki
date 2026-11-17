# Ising model

Generator input: [research prose](content/ising-model.md). Numerical verification: [Python check](../checks/ising-model.py).

## Sources read

- `goodfellow_bengio_courville2016` (§§16.2.2–16.2.4, pp. 562–567)
- `goodfellow_bengio_courville2016` (§16.2.4, eq. 16.7, pp. 566–567)
- `goodfellow_bengio_courville2016` (§§16.2.2, 16.2.4, local factors and energy)
- `metropolis1953` (p. 1088, acceptance algorithm)
- `metropolis1953` (§II, pp. 1088–1089, sampling law and limitations on equilibration)

## Calculations

Enumerated all two-spin configurations, the partition function, conditional probabilities and both Metropolis directions. Verified the local target-ratio identity and linked two-step transition calculation.

## Validation

Final build, all fifteen page checks, offline citation validation and full unit suite are recorded in the batch report. Shared corrections are staged outside tracked inputs for orchestrator integration.
