# Sparsity

Type: concept. Rank 307. Tier: lighter.

## Facts

- **Checked by code:** With $\lambda=2$, the soft-threshold values are $2$, $0$, and $-3$ for inputs $3$, $0.4$, and $-4$. Inputs $-0.5$ and $1$ both give $0$. The ridge example has eigenvalues $4$ and $0$ and coefficients $(0.8,0.8)$.
- **Checked:** James et al., ISLR corrected 7th printing, §6.2.2, pp. 219–222, and Figure 6.7: the $\ell_1$ penalty yields sparse models, and the constraint region is a diamond that a smooth contour can meet at a corner. The article proves the one-coefficient rule and states the diamond as the constraint $|\beta_1|+|\beta_2|\le s$.
- **Assumed:** The criterion is $(y-\beta)^2+\lambda|\beta|$, so the threshold is $\lambda/2$. Other normalisations of the penalty move the threshold.
- **Disputed:** None. Tibshirani (1996) was not opened.

## Sources read

1. James et al., ISLR, corrected 7th printing, §6.2.2 and Figure 6.7.
