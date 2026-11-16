# Multicollinearity

Type: Concept. Rank 224. Tier: full.

## Material checked

- **Checked:** Baseline 226 words and no figures.
- **Checked:** Dodge printed p. 96: exact collinearity is a linear combination and leaves least-squares estimators undefined as a unique solution; approximate collinearity leaves them defined with considerable variance. Printed p. 362: multicollinearity is a variable almost equal to a linear combination of others, met when explanatory variables are strongly correlated.
- **Checked by code:** $S_{11}=10$, $S_{22}=50$, $S_{12}=22$, $r^2=0.968$, $r\approx 0.9839$, inflation factor $31.25$, $\sqrt{31.25}\approx 5.590$, partial slopes $-1.5$ and $1$, simple slope $0.7$, exact-copy determinant $0$, and $1/(1-0.36)=1.5625$.
- **Assumed:** Uncorrelated equal-variance errors for the variance formula. The inflation factor is the two-predictor expression.
- **Disputed:** Nothing. Exact and approximate collinearity are different, and both are in Dodge.

## Sources opened and used

1. Yadolah Dodge, *The Concise Encyclopedia of Statistics*, 2008, printed pp. 96 and 362. Existing key `dodge2008`.

## Skipped

Hoerl and Kennard's ridge paper was not opened. The article does not describe ridge as a remedy beyond naming it as a different estimator.
