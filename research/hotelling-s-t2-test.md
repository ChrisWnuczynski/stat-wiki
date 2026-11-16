# Hotelling's T² test

Type: Concept. Rank 232. Tier: full.

## Material checked

- **Checked:** Baseline 2,469 words and no figures. The source derivation of the likelihood ratio and the normal-sample $F$ calibration stay on the page. The added arithmetic is a $p=1$ identity and one $p=2$ quadratic form.
- **Checked:** SciPy `scipy.stats.f` notes and methods `ppf` and `sf` / `cdf`. $F_{2,4;0.95}=6.944$ and $\Pr(F_{2,4}\ge 2.4)=0.2066$. The notes define $F$ as a rescaled ratio of independent chi-squared variables. The identification of a squared $t$ with $F_{1,\nu}$ is that definition together with a squared standard normal being chi-squared on one degree of freedom.
- **Checked by code:** $T^2=6$, transformed value $2.4$, one-dimensional $T^2=20$, $t\approx 4.4721$, practice $T^2=12$.
- **Assumed:** The normal-sample map from $T^2$ to $F_{p,n-p}$ is the calibration already developed on the page. The added proof shows the $p=1$ reduction and the numerical factor, not the Wishart argument.
- **Disputed:** Nothing in the quadratic-form arithmetic.

## Sources opened and used

1. SciPy `scipy.stats.f`, `https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f.html`. The quantile and tail were computed from that distribution. New pending key `scipy_f2026`.

Hotelling (1931) was not reopened; the project file was blocked. The history on the page is not given a new citation to that paper.

## Skipped

A self-contained derivation of the Wishart null distribution is logged in proofs_todo.
