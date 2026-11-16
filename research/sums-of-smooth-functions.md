# Sums of smooth functions

Type: Concept. Rank 231. Tier: full.

## Material checked

- **Checked:** Baseline 863 words and 1 figure. The kyphosis smooths and the figure stay on the generated page. The added table is a four-corner additive predictor.
- **Checked:** R `mgcv::gam` manual, Details. A GAM linear predictor is a sum of smooths plus a parametric term. Smooths are centred on the observed covariates. The basis size $k$ caps the effective degrees of freedom, usually by $k-1$. Tensor-product terms are the interaction extension.
- **Checked by code:** corners $0.2,1.2,0.8,1.8$; dose contrast $0.6$; interaction $0$; $e^{0.6}\approx 1.8221$; $e^{1.8}\approx 6.0496$; $e^{2.4}\approx 11.0232$.
- **Assumed:** Each of $x\in\{0,1\}$ and $z\in\{0,1\}$ is observed, so the sum-to-zero constraint is the two-point condition used in the proof.
- **Disputed:** Nothing in the manual's definition contradicts the contrast identity.

## Sources opened and used

1. R `mgcv::gam` manual, `https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/gam.html`. New pending key `r_mgcv_gam2026`.

Hastie and Tibshirani (1986) was not opened; the manual's comparison with Hastie's `gam` is reported as the manual's statement.
