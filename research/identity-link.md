# Identity link

Type: concept. Rank 295. Tier: lighter.

## Facts

- **Checked:** R `family` documentation: `gaussian(link = "identity")` is the documented default, and `identity` is also an accepted link name for binomial and Gamma families.
- **Checked:** R `glm` documentation: the default method `glm.fit` uses iteratively reweighted least squares.
- **Checked by code:** The three-point fit has $\hat\beta=(1, 2.5)$, fitted values $1, 3.5, 3.5$, and residual sum of squares $4.5$. The practice fit has $\hat\beta=(3,3)$ and residual sum of squares $2$.
- **Checked and not cited in the article:** James, Witten, Hastie, and Tibshirani, *An Introduction to Statistical Learning*, corrected 7th printing, §3.1.2, equation (3.5), read from the author-hosted PDF. The same slope reading is derived in the article from $\mu=\beta_0+\beta_1 x$, so the printing was not given a new bibliography key.
- **Assumed:** Independence and a common variance are the conditions for the normal-equation proof.
- **Disputed:** None.

## Sources read

1. R Core Team, family objects, `gaussian(link = "identity")`.
2. R Core Team, `glm`, method `glm.fit`.
3. James et al., ISLR, corrected 7th printing, §3.1.2.
