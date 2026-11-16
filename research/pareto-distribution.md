# Pareto distribution

Type: Distribution. Rank 225. Tier: full.

## Material checked

- **Checked:** Baseline 934 words and 2 figures. The infobox formulas, the survival key result, and the shape-$3/2$ note stay in the generated page. The added worked example uses shape $2.5$.
- **Checked:** SciPy 1.18 `scipy.stats.pareto` notes. Standardised density $b/x^{b+1}$ for $x\ge 1$. `loc` and `scale` apply the affine map $x=\mathrm{scale}\cdot y+\mathrm{loc}$.
- **Checked by code:** mean $5/3\approx 1.6667$, variance $20/9\approx 2.2222$, median $2^{0.4}\approx 1.3195$, survival $2^{-2.5}\approx 0.1768$, shape-$4$ mean $8/3\approx 2.6667$, survival $1/16=0.0625$.
- **Assumed:** The classical minimum-$x_m$ density is SciPy's `scale=x_m`, `loc=0` transformation. That matches the change-of-variable calculation.
- **Disputed:** Nothing. `loc` and `scale` are different parameters in the manual, and the article keeps them different.

## Sources opened and used

1. SciPy developers, `scipy.stats.pareto`, version 1.18 notes, `https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pareto.html`. New pending key `scipy_pareto2026`.

Forbes and Pareto's 1909 manual are already named in the distribution record. They were not reopened for the added prose.

## Skipped

The distribution template has no Check yourself heading, so the three questions sit in the worked example. The built-in survival proof is replaced by the proof in Properties, which includes that integral.
