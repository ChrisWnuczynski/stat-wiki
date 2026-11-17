# graphical-lasso

Rank: 387. Batch V.

Source locators actually read during this pass:

- `friedman_glasso2008`: §§1–2.
- `friedman_glasso2008`: §2, eq. 1.
- `banerjee_elghaoui_daspremont2008`: §2.1, eq. 1.
- `banerjee_elghaoui_daspremont2008`: §1.
- `friedman_glasso2008`: §2, subgradient equations.
- `banerjee_elghaoui_daspremont2008`: §2.2, pp. 487–488.
- `banerjee_elghaoui_daspremont2008`: §§2.1–2.2.
- `friedman_glasso2008`: §2.
- `banerjee_elghaoui_daspremont2008`: §3.

Research prose: 663 whitespace-separated words; 10 citation markers. Numerical and algebraic checks: `checks/graphical-lasso.py`.

Checks and integration results are recorded in `/workspace/statwiki-run/report-v.json`. External reference PDFs/text remain outside the repository.

Full-body citation audit: additionally read `foygel_drton2010` (§§1–2.2, EBIC formula and consistency conditions); exact old-marker replacement staged for shared-source integration.

The covariance initialisation is positive definite for a singular sample covariance only at a strictly positive penalty. The shared interpretation states this condition explicitly; the check verifies the singular example's shifted eigenvalues.
