# Kernel trick

Generator input: [research prose](content/kernel-trick.md). Numerical verification: [Python check](../checks/kernel-trick.py).

## Sources read

- `scholkopf_smola2003_intro` (§6.2, pp. 54–56)
- `rasmussen_williams2006` (§2.1.2, pp. 11–12)
- `scholkopf_smola2003_intro` (§7, pp. 57–60)
- `rasmussen_williams2006` (§4.1, pp. 79–80)
- `scholkopf_smola2003_intro` (§§4, 6.2, pp. 49–51, 54–56)

## Calculations

Constructed the XOR Gram matrix and its eigenvalues, checked dual feasibility and unit margins, derived the complete decision polynomial symbolically and evaluated both prediction points. Verified the scalar quadratic feature map, squared-distance identity, linked feature separation and Gaussian Gram principal minors.

## Validation

Final build, all fifteen page checks, offline citation validation and full unit suite are recorded in the batch report. Shared corrections are staged outside tracked inputs for orchestrator integration.
