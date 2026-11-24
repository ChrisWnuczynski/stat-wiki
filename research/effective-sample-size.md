# Effective sample size

Type: Topic. Rank 259. Tier: full.

## Material checked

- **Checked:** The variance of a stationary sample mean is the double sum of lag covariances. For geometric autocorrelation the long-run inflation is $(1+\rho)/(1-\rho)$. Geyer (2005), pp. 9–10, was read for stationarity of the marginal; the covariance sum is derived on the page.
- **Checked by code:** $n=5$, $\rho_k=(1/2)^k$ gives multiplier 2.225 and effective size 2.247. The same $n$ with $\rho_k=(-1/2)^k$ gives weighted sum $-23/80$, multiplier $17/40=0.425$, variance of the mean $(17/200)\sigma^2=0.085\sigma^2$, and effective size $200/17$, which is 11.765 to three decimal places. The page's convention is $\sigma^2/n_{\mathrm{eff}}=\Var(\overline X)$ with the exact finite-sample weights $(1-k/n)$. The infinite-sum factor for $\rho=-1/2$ is $1/3$, and $5/(1/3)=15$, which is not that finite-sample figure. For $\rho=0.8$ and $n=1000$ the long-run size is 111.11.
- **Assumed:** The chain is already stationary and the variance is finite. Estimated autocorrelations are not the known $\rho_k$ in the identity. The alternating example uses those known correlations.
- **Opened for this correction:** Stan Development Team, Stan Reference Manual, Posterior Analysis, section “Effective sample size”, https://mc-stan.org/docs/reference-manual/analysis.html#effective-sample-size . The manual defines effective sample size with the infinite autocorrelation sum and states that anticorrelated draws can make it larger than the number of iterations. The page's 0.425 is the finite-$n$ multiplier, not that infinite sum.
- **Disputed:** An earlier note said Geyer 1992 was not cited. The page does cite it. This pass did not re-open that article. The numerical contrast is an exact variance calculation for known autocorrelations, not a Stan estimate from simulated draws.

## Sources opened

Geyer (2005), pp. 9–11. Key `geyer2005_markov_chain`.

Stan Reference Manual, Posterior Analysis, “Effective sample size”. Key `stan_reference_analysis2026`.
