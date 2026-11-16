# Random forest

Rank 315. Lighter tier. Concept page.

## Sources read

- ESL, Chapter 15, §15.2, printed pp. 587–589. Algorithm: bootstrap sample, then $m$ random predictors at each split. Display (15.1) is the variance of an average of identically distributed, pairwise-correlated trees. Typical $m$ is near $\sqrt p$, or as small as $1$.

## Checked

- $\sigma^2=4$, $\rho=0.2$, $B=100$ gives $0.8+0.032=0.832$.
- Independent average: $0.04$. Ratio of floor to that average: $0.8/0.04=20$.
- $B=200$ gives $0.816$.
- Your turn: $\sigma^2=1$, $\rho=0.5$, $B=50$ gives $0.51$, against $0.02$ if independent.
- The variance algebra is proved on the page from the common-variance, common-correlation expansion.

## Not opened

- Breiman's 2001 paper is cited by the source definition. The file read for this pass was ESL, not the Machine Learning article, so new sentences cite ESL.
