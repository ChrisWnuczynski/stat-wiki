# Soft-margin primal

Type: Concept. Rank 279. Tier: lighter.

## Facts

- **Checked:** ESL 12th printing, pp. 418–421. Equation (12.8) minimises \(\tfrac12\|\beta\|^2+C\sum\xi_i\) subject to \(\xi_i\ge 0\) and \(Y_i(X_i^\top\beta+\beta_0)\ge 1-\xi_i\). The separable case is \(C=\infty\). Misclassification corresponds to \(\xi_i>1\). Equations (12.12) and (12.17) give \(0\le\alpha_i\le C\) and \(\hat\beta=\sum\hat\alpha_i Y_i X_i\), with margin points at \(0<\hat\alpha_i<C\).
- **Checked by code:** For \(\beta=(1,0)\), \(\beta_0=0\), functional margins \(2\), \(0.5\) and \(-0.25\) give slacks \(0\), \(0.5\), \(1.25\), total \(1.75\), cost \(4\) at \(C=2\) and \(2.25\) at \(C=1\). The candidate with \(\|\beta\|^2=0.4\), functional margin \(0.2\) and \(C=5\) costs \(4.2\).
- **Assumed:** Labels are coded \(\pm 1\), matching ESL rather than \(0/1\).
- **Disputed:** Nothing numerical. The worked plane is feasible, not optimal. ESL's proportional-slack form (12.6) is a different convex programme; the article uses (12.8), which matches the page's primal.

## Sources opened

Hastie, Tibshirani and Friedman (2009), pp. 418–421 and 424. Key `hastie_esl2009`. Dodge has no soft-margin entry.

## Proofs

The smallest feasible slack for a fixed plane is proved. KKT uniqueness of the optimum is not.
