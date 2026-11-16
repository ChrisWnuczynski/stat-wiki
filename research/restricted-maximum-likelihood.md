# Restricted maximum likelihood

Type: concept. Rank 306. Tier: lighter.

## Facts

- **Checked:** Siegrist §6.08: $(n-1)S^2/\sigma^2$ is chi-squared on $n-1$ degrees of freedom for an iid normal sample.
- **Checked by code:** For $1,2,3,4,10$, $Q=50$, the ordinary estimate is $10$, and the restricted estimate is $12.5$. For $2,2,2,6$, $Q=12$, the ordinary estimate is $3$, and the restricted estimate is $4$. The derivative of the chi-squared log-likelihood vanishes at $Q/\nu$.
- **Assumed:** The one-sample normal model is the case proved here. A general linear mixed model has more than one variance component; that extension is described and not derived.
- **Disputed:** None. Patterson and Thompson (1971) was not opened.

## Sources read

1. Kyle Siegrist, §6.08, the chi-squared law of the residual sum of squares.
