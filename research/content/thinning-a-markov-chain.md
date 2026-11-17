## Motivating example
A sampler has produced a long sequence of correlated states. Saving every fifth state makes the saved sequence appear less correlated, but also leaves fewer observations. The relevant comparison is precision for a fixed computational budget, rather than correlation between two neighbouring saved values. An expensive calculation performed on each saved state can change that budget comparison.{{cite:owen2017_thinning}} (§§1–2)

## Definition — Observing the chain at a coarser time scale
Thinning by an integer $k\ge1$ replaces $X_1,X_2,\ldots$ by $X_k,X_{2k},\ldots$. For a homogeneous chain with transition matrix $P$, the sampled chain has transition matrix $P^k$. If $\pi P=\pi$, repeated multiplication gives $\pi P^k=\pi$: thinning preserves a stationary law. It changes dependence and the observation count, rather than correcting an unsuitable stationary distribution.{{cite:durrett2019}} (§§5.1 and 5.5)

## Properties — Variance depends on all the autocorrelations
Let $Y_t=g(X_t)$ be stationary with variance $\sigma_g^2$ and autocorrelations $\rho_h$. Expanding the variance of its average gives the finite-sample identity
$$
\operatorname{Var}(\overline Y_N)=\frac{\sigma_g^2}{N}
\left[1+2\sum_{h=1}^{N-1}\left(1-\frac hN\right)\rho_h\right].
$$
When the relevant covariance series converges, the large-sample variance factor is $\tau=1+2\sum_{h\ge1}\rho_h$. Thinning replaces $\rho_h$ by $\rho_{kh}$ while reducing the count from $N$ to approximately $N/k$. Both effects must enter an efficiency calculation.{{cite:owen2017_thinning}} (§2, eq. 1)

For AR(1) autocorrelations $\rho_h=\rho^h$, $|\rho|<1$, summing the geometric series gives $\tau=(1+\rho)/(1-\rho)$ and $\tau_k=(1+\rho^k)/(1-\rho^k)$. These formulas concern the particular scalar quantity $g$, since two summaries of the same chain can have different autocorrelations.{{cite:owen2017_thinning}} (§§2 and 2.2, eq. 4)

## Worked example — Lower correlation, fewer effective observations
Take $N=1000$, $\rho=0.8$ and unit marginal variance. Without thinning, $\tau=9$ and the asymptotic effective sample size is $1000/9=111.11$. Saving every fifth state leaves $200$ values with lag-one correlation $0.8^5=0.32768$. Their variance factor is $1.97477$, giving effective size $200/1.97477=101.28$.

The corresponding asymptotic mean variances are $0.00900$ and $0.00987$. The second sequence has lower adjacent correlation and lower precision for this fixed number of transitions. The calculation illustrates the AR(1) efficiency comparison.{{cite:owen2017_thinning}} (§2.2, eq. 4)

**Your turn.** For independent output, what happens to the variance of the mean if every fifth value of an already computed sequence is used?

::: {.callout-tip collapse="true" title="Answer"}
All nonzero-lag correlations are zero. Reducing the count from $N$ to $N/5$ multiplies mean variance from $\sigma_g^2/N$ to $5\sigma_g^2/N$.
:::

## Statistical use — Paying for transitions and for summaries
If one transition costs one unit and evaluating $g$ costs $\theta$ units, a budget $B$ allows about $B/(k+\theta)$ saved evaluations at spacing $k$. This differs from discarding values after all their summaries have already been computed. With sufficiently costly evaluations and slowly decaying positive correlations, spacing evaluations can improve precision per unit cost. The decision depends on the evaluation cost and covariance pattern.{{cite:owen2017_thinning}} (§§2–3)

