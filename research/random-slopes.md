# Random slopes

Type: Concept. Rank 270. Tier: full.

## Material checked

- **Checked:** Baseline 355 words, 0 figures. Bates, Mächler, Bolker and Walker, *JSS* 67 (2015), pp. 1–3, equations (2)–(4): conditional normal mean Xβ+Zb, random effects N(0, Σ), and Σ = σ² ΛΛᵀ. The sleep-deprivation study is their running example; the numerical `lmer` summary was not refitted because R is not installed here.
- **Checked by code:** With σ_a²=4, σ_b²=1, σ_ab=−1/2 and σ²=1, Var(Y_2)=7, Cov(Y_0,Y_2)=3, Var(Y_1)=5. With σ_ab=0 the variance at t=2 is 9. The proposed covariance with correlation 1.5 has determinant −1.25. `checks/random-slopes.py`.
- **Assumed:** Residuals are independent of the random effects and of each other, with variance σ², which is the conditional model in equation (2) when the weight matrix is the identity.
- **Not opened:** Laird and Ware 1982, Self and Liang 1987, Belenky et al. 2003. Boundary likelihood-ratio tails are not stated.

## Sources opened

1. Douglas Bates, Martin Mächler, Benjamin Bolker and Steven Walker, “Fitting linear mixed-effects models using lme4”, *Journal of Statistical Software* 67 (2015), pp. 1–3. Key `bates_lme4_2015`. JSS PDF.
