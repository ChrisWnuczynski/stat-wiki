# Normal linear model — rank 165

Type: model/concept. Baseline 1,876 words, zero figures. Preserve matrix and simple-regression definitions, likelihood, unbiasedness argument, exact sampling statements, heart-rate/oxygen example with its data table, interpretation, and related links.

## Sources opened

- Michal Kulich, *Advanced Regression Models: Extended Course Notes* (Charles University, 2022), complete author/university-hosted PDF, §§1.1–1.5, printed pp. 6–10. Read fixed/random design framing, normal linear model, hat-matrix projection, coefficient distribution, residual chi-squared law, independence, t and F pivots, and assumptions.
- James, Witten, Hastie and Tibshirani (2013), *An Introduction to Statistical Learning*, complete author/publisher-hosted first-edition seventh-printing PDF, Ch. 3 §§3.1–3.3 pp. 61–101. Read simple regression/least squares, standard errors, residual error, prediction versus association, nonlinearity, unequal error variance and correlated errors. The same `james_islr2013` record is already pending under rank 163.
- Dodge (2008), printed pp. 304–307, *Least-Squares Method* and Legendre entry, for the 1805 orbital-analysis introduction and normal equations. The historical fact is attributed to this opened encyclopedia rather than an unexamined scan of Legendre's original book.
- Fox (2016) publisher and author sites were opened, but only a book overview/links, not Ch. 6; inherited Fox citations remain to be localized by shared-source review. No pirated mirror used.

## Fact ledger

- **Checked:** Under fixed full-rank `A`, `Y=A beta+epsilon`, `epsilon~N(0,sigma² I)` implies OLS/MLE `beta_hat=(A'A)^−1 A'Y`, `beta_hat~N(beta,sigma²(A'A)^−1)` and `RSS/sigma²~chi²_(n-p)` independently (Kulich §§1.2–1.3, pp. 7–8). Proof in one box.
- **Checked:** `RSS/n` is normal-likelihood MLE for error variance but biased; `RSS/(n-p)` is unbiased. Any coefficient contrast standardized by its residual SE is `t_(n-p)`, and nested subspace RSS differences yield F (Kulich §1.3, p. 8). Proof in box.
- **Checked:** Without normality, fixed-design zero-mean errors preserve OLS unbiasedness; homoscedastic uncorrelated errors give the conventional covariance formula, but exact t/F reference is not generally justified (Kulich §§1.1–1.4, pp. 6–9).
- **Checked:** The 19 heart-rate/oxygen values were recalculated using NumPy/SciPy, yielding the displayed fitted coefficients, residual SE, slope SE, intercept SE, t value and confidence interval. The four-point worked and three-point Your-turn examples were computed by exact arithmetic and numerics in focused check.
- **Assumed:** Design rows are fixed or inference is conditional on a valid observed design. The small worked data are illustrative; their residuals alone cannot validate Gaussian independence.
- **Disputed:** The inherited heart-rate exercise's Fox p. 111–112 citation supports regression formulas in general but the source data table was not verified in the publisher sample. Keep the example and data; the source chapter itself is the immediate source for those values. Historical priority for least squares is complicated; article states the documented 1805 Legendre publication rather than a claim of first private discovery.
