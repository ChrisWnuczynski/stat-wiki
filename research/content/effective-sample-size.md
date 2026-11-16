## Lead context
The effective sample size is the number of independent draws that would estimate a mean as precisely as a dependent sample of the length actually stored.

## Motivating example
A Markov chain is run for 1000 steps and the autocorrelation of the stored values is about 0.8 at lag 1, decaying geometrically. Those 1000 numbers are not 1000 independent looks at the target. For a long geometric autocorrelation the variance of the sample mean is about $(1+\rho)/(1-\rho)=9$ times the independent-sample variance. The effective sample size is $1000/9=111.11$. A standard error computed as if the draws were independent is too small by a factor of 3.{{cite:geyer2005_markov_chain}} (pp. 9–10, a stationary chain has a single marginal at every time; dependence between times is a separate fact)

## Intuition
Precision of a mean depends on how many fresh pieces of information the sample contains. If $X_{t+1}$ is almost a copy of $X_t$, storing both of them barely improves the average. The effective sample size rescales the length $n$ by the inflation in the variance of the average. It is not a property of the target distribution alone. The same target, sampled by a stickier transition, has a smaller effective sample size at the same $n$. It is also not a single number for the whole chain. A mean, a tail probability and a quantile can have different autocorrelations and therefore different effective sizes.{{cite:geyer2005_markov_chain}} (p. 10, stationarity fixes the marginal, not the dependence)

## Definition
Suppose $X_1,\ldots,X_n$ are stationary with variance $\sigma^2$ and autocorrelation $\rho_k=\mathrm{Corr}(X_1,X_{1+k})$. The variance of the sample mean is
$$
\Var(\overline X)=\frac{\sigma^2}{n}\left(1+2\sum_{k=1}^{n-1}\Bigl(1-\frac{k}{n}\Bigr)\rho_k\right).
$$
The term in parentheses is the variance inflation. The effective sample size is $n$ divided by that inflation, so that $\sigma^2/n_{\mathrm{eff}}=\Var(\overline X)$. When the $X_i$ are uncorrelated, every $\rho_k$ is 0, the inflation is 1 and $n_{\mathrm{eff}}=n$. When they are positively correlated, $n_{\mathrm{eff}}<n$.

## Interpretation — Geometric correlation
If $\rho_k=\rho^k$ for $|\rho|<1$, the infinite sum $1+2\sum_{k=1}^\infty\rho^k$ equals $(1+\rho)/(1-\rho)$. For a long run the inflation is close to that constant, and
$$
n_{\mathrm{eff}}\approx n\frac{1-\rho}{1+\rho}.
$$
At $\rho=0.8$ the factor is $0.2/1.8=1/9$. At $\rho=0$ it is 1. At $\rho$ close to 1 the effective size collapses even if $n$ is large. The approximation drops the factors $(1-k/n)$ and the tail of the sum beyond $n$. For a short series those omissions matter, so the finite sum should be used.

## Properties — A short series, computed exactly
Take $n=5$ and $\rho_k=(1/2)^k$. Then
$$
\sum_{k=1}^{4}\Bigl(1-\frac{k}{5}\Bigr)\Bigl(\frac12\Bigr)^k=\frac45\cdot\frac12+\frac35\cdot\frac14+\frac25\cdot\frac18+\frac15\cdot\frac{1}{16}=0.6125.
$$
The inflation is $1+2\times0.6125=2.225$, and $n_{\mathrm{eff}}=5/2.225=2.247$. The large-sample formula $5(1-1/2)/(1+1/2)=5/3=1.667$ is in the right direction and is not yet accurate. Five observations are not a long run.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $S=\sum_{i=1}^n(X_i-\mu)$. Then $\Var(S)=\sum_i\sum_j\Cov(X_i,X_j)=\sigma^2\sum_{i,j}\rho_{|i-j|}$. There are $n$ diagonal terms equal to 1, and for each lag $k\ge 1$ there are $2(n-k)$ ordered pairs. Hence
$$
\Var(S)=\sigma^2\left(n+2\sum_{k=1}^{n-1}(n-k)\rho_k\right),
$$
and dividing by $n^2$ gives the variance of the mean. For $\rho_k=\rho^k$,
$$
\sum_{k=1}^\infty\rho^k=\frac{\rho}{1-\rho},\qquad 1+2\frac{\rho}{1-\rho}=\frac{1+\rho}{1-\rho},
$$
provided $|\rho|<1$. Dividing $n$ by that constant is the limiting effective sample size. The finite-sum weights $(1-k/n)$ are exactly $(n-k)/n$, so the display in the definition matches this expansion.{{cite:geyer2005_markov_chain}} (p. 9, identical marginals in a stationary chain; the covariance sum is the second-moment calculation)
:::
:::

## Statistical use — Reporting a Monte Carlo mean
If a posterior mean is estimated by $\overline X$ from a stationary chain, the Monte Carlo standard error is $\sqrt{\Var(\overline X)}$, not $\sigma/\sqrt{n}$, unless the inflation is 1. Quoting $n_{\mathrm{eff}}$ beside the estimate tells a reader how much of the stored length survived the dependence. A second function of the same draws, such as $\overline{g(X)}$, needs its own autocorrelations. One effective sample size does not serve every functional. Thinning, keeping every $k$th draw, reduces $n$ and usually does not increase $n_{\mathrm{eff}}$ by the same factor, because the discarded draws still carried some information.{{cite:geyer2005_markov_chain}} (pp. 9–10, stationarity is about marginals; subsampling is a separate operation)

## Worked example
For the geometric case $\rho=0.8$ and $n=1000$, $(1+\rho)/(1-\rho)=9$ and $n_{\mathrm{eff}}\approx111.11$. If $\sigma^2=1$, the independent-draw variance of the mean would be $0.001$, with standard error $0.03162$. The dependent variance is about $0.009$, with standard error $0.09487$. The ratio of those standard errors is $\sqrt{9}=3$.

For the exact five-term sum above, inflation $2.225$ and $n_{\mathrm{eff}}=2.247$. A report that said "5 draws" would overstate the precision by a factor of $\sqrt{2.225}=1.492$.

**Your turn.** For a long run with $\rho=1/3$, what is $(1-\rho)/(1+\rho)$, and what is $n_{\mathrm{eff}}$ when $n=900$?

::: {.callout-tip collapse="true" title="Answer"}
$(1-1/3)/(1+1/3)=(2/3)/(4/3)=1/2$. Then $n_{\mathrm{eff}}\approx900/2=450$. Positive correlation has halved the effective length. The formula is the long-run limit, not the exact finite-sum inflation.{{cite:geyer2005_markov_chain}} (p. 10, dependence remains after the marginal has settled)
:::

## Common misconceptions
The iteration count is not the effective sample size. A chain of length 1000 with $\rho=0.8$ is worth about 111 independent draws for the mean. The effective sample size is not evidence that the chain has the right stationary distribution. It measures dependence given that the draws are already stationary with variance $\sigma^2$. A large $n_{\mathrm{eff}}$ from the wrong target is a precise estimate of the wrong mean. And one number does not describe every summary. The indicator $1_{\{X>c\}}$ can be much more, or much less, autocorrelated than $X$.

## Assumptions and limits — Stationarity, and a variance that exists
The variance formula uses a single $\sigma^2$ and autocorrelations that depend on lag only. That is stationarity. A chain that is still drifting has a mean that changes with time, and the sum does not describe $\overline X$. If $\sigma^2$ is infinite, there is no $\sigma^2/n_{\mathrm{eff}}$ to compute. Heavy tails break the formula before dependence does. The geometric formula also needs $|\rho|<1$. At $\rho=1$ the series does not decay, the inflation grows with $n$, and the effective size stays bounded while $n$ grows. Finally, the plug-in estimate of $\rho_k$ from a single chain is itself random. The identity above is for known autocorrelations. An estimated $n_{\mathrm{eff}}$ carries its own error, especially when the sum is truncated at a lag chosen from the same series.{{cite:geyer2005_markov_chain}} (pp. 9–10, the stationary regime is the setting in which a single marginal variance makes sense)

## Connections
A [Markov chain](markov-chain.qmd) is the usual source of the dependence. [Monte Carlo](monte-carlo-method.qmd) with independent draws is the case $n_{\mathrm{eff}}=n$. [Metropolis–Hastings](metropolis-hastings-algorithm.qmd) can be stationary and still have $\rho$ near 1 if the proposals are tiny. [Detailed balance](detailed-balance.qmd) fixes the stationary distribution of a reversible kernel and says nothing about the size of $\rho$.{{cite:geyer2005_markov_chain}} (pp. 9–11, stationarity and reversibility)

## Check yourself

### One change in a trace {#self-check-ex-ur-one-change}

A stored series has $n=400$ and geometric autocorrelation $\rho=0.5$. Using the long-run formula, what is $n_{\mathrm{eff}}$?

[Question-bank page](../questions/ex-ur-one-change.qmd)

::: {.callout-tip collapse="true" title="Answer"}
$(1-0.5)/(1+0.5)=1/3$, so $n_{\mathrm{eff}}\approx400/3=133.33$. The variance of the mean is about three times the independent-draw variance. The exact finite-sample inflation is a little different, because the factors $(1-k/n)$ have been replaced by 1.{{cite:geyer2005_markov_chain}} (p. 10, lag dependence)
:::

### A posterior mean {#self-check-ex-ur-posterior-mean}

Why can two posterior summaries from the same chain have different effective sample sizes?

[Question-bank page](../questions/ex-ur-posterior-mean.qmd)

::: {.callout-tip collapse="true" title="Answer"}
Each summary is a function $g(X_t)$. The autocorrelations of $g(X_t)$ need not equal the autocorrelations of $X_t$. The variance inflation is computed from the series actually averaged. A precise mean does not imply a precise tail probability.{{cite:geyer2005_markov_chain}} (p. 9, one stationary marginal, many functions of it)
:::

## History
The variance formula for a mean of a stationary sequence is the double sum of the lag covariances. Geyer's notes separate that dependence from stationarity itself: a stationary chain has one marginal at every time, and the dependence between times is what the effective sample size converts into an equivalent independent count. The numerical factor $(1+\rho)/(1-\rho)$ is the geometric special case of the same sum.{{cite:geyer2005_markov_chain}} (pp. 9–10, stationary Markov chains)
