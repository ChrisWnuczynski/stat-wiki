# Cubic smoothing spline

Type: Concept. Rank 277. Tier: lighter.

## Material checked

- **Checked:** Baseline 534 words, 0 figures. ESL Ch. 5 §5.4, printed p. 151, equation 5.9: the penalised residual sum of squares, the λ=0 and λ=∞ extremes, and the statement that the minimiser is a natural cubic spline with knots at the distinct x_i. §5.4.1, pp. 153–154, equations 5.16 and 5.20: effective degrees of freedom tr(S_λ) and eigenvalues 1/(1+λ d_k).
- **Checked by code:** For (0,0), (1,1), (2,0) the least-squares slope is 0 and the residual sum of squares is 2/3. The interpolating quadratic 2x−x² has penalty integral 8. The criteria meet at λ=1/12. `checks/cubic-smoothing-spline.py`.
- **Assumed:** The natural-cubic-spline characterisation at finite λ is ESL’s stated theorem and is not reproved. It is logged for a later proof.
- **Not opened:** Reinsch 1967, Green and Silverman 1994, de Boor 1978, Wahba 1990. The copied chapter cites them.

## Sources opened

1. Hastie, Tibshirani and Friedman, ESL, Ch. 5 §5.4–5.4.1, pp. 151–154. Key `hastie_esl2009`.
