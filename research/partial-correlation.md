# Partial correlation

Type: Concept. Rank 269. Tier: full.

## Material checked

- **Checked:** Baseline 905 words, 0 figures. Dodge printed pp. 412–413 defines partial correlation as the correlation of least-squares residuals and states the three-correlation fraction. The chain precision matrix and its inverse were recomputed.
- **Checked by code:** Correlations 0.8, 0.6, 0.5 give partial correlation ≈0.7217. Equal correlations 0.5 give 1/3. The displayed precision matrix inverts to the stated covariance, and the marginal correlation of the ends is 1/3. `checks/partial-correlation.py`.
- **Assumed:** For a non-degenerate normal vector, the conditional covariance of two coordinates given the rest is the inverse of the corresponding precision block. The correlation simplification is then algebra. That block-inverse step is the usual Gaussian identity and is not re-derived from the density here.
- **Not opened:** Yule 1907 (Royal Society PDF returned HTTP 403). Dodge’s historical pointer to Yule is what was read.

## Sources opened

1. Dodge, *The Concise Encyclopedia of Statistics*, printed pp. 412–413. Key `dodge2008`.
