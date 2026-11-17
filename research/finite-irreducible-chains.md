# Finite irreducible chains

Generator input: [research prose](content/finite-irreducible-chains.md). Numerical verification: [Python check](../checks/finite-irreducible-chains.py).

## Sources read

- `grinstead_snell1997` (§11.3, Thms. 11.10–11.11, p. 438)
- `grinstead_snell1997` (§11.3, Thm. 11.10, p. 438)
- `durrett2019` (§5.5, Thm. 5.5.11, p. 306; §5.6, Thm. 5.6.1, pp. 310–311)
- `durrett2019` (§5.6, Lem. 5.6.4 and Thm. 5.6.6, pp. 312–314)
- `grinstead_snell1997` (§§11.3–11.4, pp. 438, 447–450)
- `durrett2019` (§5.6, Ex. 5.6.2 and Ex. 5.6.1, pp. 311, 315)

## Calculations

Computed stationary laws, powers, the exact two-state recurrence and step-six distribution, the mean return time, and periodic two- and three-state counterexamples. The finite-state stationary existence/positivity/uniqueness proof is local; general aperiodic convergence and the return-time identity remain anchored proof gaps.

## Validation

Final build, all fifteen page checks, offline citation validation and full unit suite are recorded in the batch report. Shared corrections are staged outside tracked inputs for orchestrator integration.

The local proof establishes stationary existence, positivity and uniqueness. General aperiodic convergence and the return-time identity are staged in the proof-gap overrides, with explicit result anchors.
