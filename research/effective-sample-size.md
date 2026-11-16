# Effective sample size

Type: Topic. Rank 259. Tier: full.

## Material checked

- **Checked:** The variance of a stationary sample mean is the double sum of lag covariances. For geometric autocorrelation the long-run inflation is $(1+\rho)/(1-\rho)$. Geyer (2005), pp. 9–10, was read for stationarity of the marginal; the covariance sum is derived on the page.
- **Checked by code:** $n=5$, $\rho=1/2$ gives inflation 2.225 and effective size 2.247. For $\rho=0.8$ and $n=1000$ the long-run size is 111.11.
- **Assumed:** The chain is already stationary and the variance is finite. Estimated autocorrelations are not the known $\rho_k$ in the identity.
- **Disputed:** Geyer 1992 was not opened, so the article does not cite it.

## Sources opened

Geyer (2005), pp. 9–11. Key `geyer2005_markov_chain`.
