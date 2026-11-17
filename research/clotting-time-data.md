# Clotting time data

Generator input: [research prose](content/clotting-time-data.md). Numerical verification: [Python check](../checks/clotting-time-data.py).

## Sources read

- `nelder_wedderburn1972` (§§1.1–1.3, pp. 371–372)
- `dodge2008` (p. 216, Gamma Distribution)
- `nelder_wedderburn1972` (§§1.2–1.3, p. 372)
- `nelder_wedderburn1972` (§1.3, p. 372)
- `nelder_wedderburn1972` (§2.1, pp. 372–374)

## Calculations

Recomputed both displayed and fully refitted inverse-link predictions. Independent Gamma likelihood fits check coefficients, common dispersion, standard errors, test statistics, p-values and AIC; constrained inverse-Gaussian fits check the inverse-link and inverse-square-link comparisons. The script also verifies the Gamma variance and two linked coefficient interpretations.

## Validation

Final build, all fifteen page checks, offline citation validation and full unit suite are recorded in the batch report. Shared corrections are staged outside tracked inputs for orchestrator integration.

The nine concentrations and both response vectors were read in the R glm Examples section. The check refits their inverse-link Gamma coefficients independently. Historical Hurn provenance remains an item to verify; an exact source-opening replacement removes that unverified attribution from the article.
