# Exponential loss

Generator input: [research prose](content/exponential-loss.md). Numerical verification: [Python check](../checks/exponential-loss.py).

## Sources read

- `schapire2013_explaining_adaboost` (§4, pp. 7–8)
- `schapire2013_explaining_adaboost` (§4, p. 7)
- `freund_schapire1997` (§4, AdaBoost and its training-error analysis)
- `schapire2013_explaining_adaboost` (§4, pp. 8–9)
- `freund_schapire1997` (§4, AdaBoost update)

## Calculations

Differentiated the conditional exponential risk symbolically; verified the unique interior optimum, its inverse probability transformation, the boundary directions and the complete five-weight AdaBoost update.

## Validation

Final build, all fifteen page checks, offline citation validation and full unit suite are recorded in the batch report. Shared corrections are staged outside tracked inputs for orchestrator integration.
