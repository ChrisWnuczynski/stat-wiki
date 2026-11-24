## Lead context
Precision here means a comparison of variances for that mean. The matching independent sample size is not a count of stored draws, and nothing in the comparison forces it to be smaller than the length of the series.

## Motivating example
A Markov chain is run for 1000 steps and the autocorrelation of the stored values is about 0.8 at lag 1, decaying geometrically. Those 1000 numbers are not 1000 independent looks at the target. For a long geometric autocorrelation the variance of the sample mean is about $(1+\rho)/(1-\rho)=9$ times the independent-sample variance. The effective sample size is $1000/9=111.11$. A standard error computed as if the draws were independent is too small by a factor of 3.

## Intuition
Precision of a mean depends on how many fresh pieces of information the sample contains. If $X_{t+1}$ is almost a copy of $X_t$, storing both of them barely improves the average. The effective sample size rescales the length $n$ by the multiplier in the variance of the average. A multiplier above one makes the mean less precise than $n$ independent draws. A multiplier strictly between zero and one makes it more precise, and the matching independent sample is then finite and longer than $n$. In either case the rescaling describes that mean, not a change in the number of draws stored. The effective sample size is not a property of the target distribution alone. The same target, sampled by a stickier transition, has a smaller effective sample size at the same $n$. It is also not a single number for the whole chain. A mean, a tail probability and a quantile can have different autocorrelations and therefore different effective sizes.{{cite:geyer1992}} (§§3.3–3.7, pp. 477–480)

## Definition
Suppose $X_1,\ldots,X_n$ are stationary with variance $\sigma^2$ and autocorrelation $\rho_k=\mathrm{Corr}(X_1,X_{1+k})$. The variance of the sample mean is
$$
\Var(\overline X)=\frac{\sigma^2}{n}\left(1+2\sum_{k=1}^{n-1}\Bigl(1-\frac{k}{n}\Bigr)\rho_k\right).
$$
The term in parentheses is the variance multiplier for the mean. Those autocorrelations are defined only when the common marginal variance $\sigma^2$ is positive and finite. This page's convention then defines a finite $n_{\mathrm{eff}}$ by the identity $\sigma^2/n_{\mathrm{eff}}=\Var(\overline X)$ when the variance of the mean is also positive, so $n_{\mathrm{eff}}$ is $n$ divided by that positive multiplier. The weights $(1-k/n)$ are the exact pair counts $(n-k)/n$ in a series of length $n$. When the $X_i$ are uncorrelated, every $\rho_k$ is 0, the multiplier is 1 and $n_{\mathrm{eff}}=n$. When the correlations are positive, the multiplier exceeds 1 and $n_{\mathrm{eff}}<n$. When the weighted sum of the correlations is negative and the multiplier remains positive, $n_{\mathrm{eff}}>n$. If the multiplier is zero, $\Var(\overline X)=0$ while $\sigma^2>0$. Every finite independent sample of size $m$ still has mean variance $\sigma^2/m>0$, so none matches that mean.

## Interpretation — Geometric correlation
If $\rho_k=\rho^k$ for $|\rho|<1$, the infinite sum $1+2\sum_{k=1}^\infty\rho^k$ equals $(1+\rho)/(1-\rho)$. For a long run the multiplier is close to that constant, and
$$
n_{\mathrm{eff}}\approx n\frac{1-\rho}{1+\rho}.
$$
At $\rho=0.8$ the factor is $0.2/1.8=1/9$. At $\rho=0$ it is 1. At $\rho=-1/2$ the constant equals $1/3$, so the long-run formula is about $3n$, which is larger than $n$. At $\rho$ close to 1 the effective size collapses even if $n$ is large. The approximation drops the factors $(1-k/n)$ and the tail of the sum beyond $n$. For a short series those omissions matter, so the finite sum should be used.

## Properties — A short series, computed exactly
Take $n=5$ and $\rho_k=(1/2)^k$. Then
$$
\sum_{k=1}^{4}\Bigl(1-\frac{k}{5}\Bigr)\Bigl(\frac12\Bigr)^k=\frac45\cdot\frac12+\frac35\cdot\frac14+\frac25\cdot\frac18+\frac15\cdot\frac{1}{16}=0.6125.
$$
The multiplier is $1+2\times0.6125=2.225$, and $n_{\mathrm{eff}}=5/2.225=2.247$. The large-sample formula $5(1-1/2)/(1+1/2)=5/3=1.667$ is in the right direction and is not yet accurate. Five observations are not a long run.

A different weakly stationary series of five draws, with alternating lag correlations, shows that the multiplier need not exceed 1. Reversing the sign of every centered draw would leave the correlations unchanged, because each product of centered variables changes sign twice. Alternating those signs, $Y_t=(-1)^t(X_t-\mu)$, multiplies the lag-$k$ correlation by $(-1)^k$. The centered variables keep mean zero and a common variance, and the new covariances still depend only on lag, so weak stationarity is preserved. Strict stationarity need not survive that alternation unless the centered variables are symmetric about zero: negating a skewed variable changes its distribution, and the odd and even times then have different laws. Applied to $\rho_k=(1/2)^k$, the new correlations are $\rho_k=(-1/2)^k$. Keep $n=5$ and a positive finite variance $\sigma^2$, and use that alternating series. The finite-sample weights are unchanged:
$$
\sum_{k=1}^{4}\Bigl(1-\frac{k}{5}\Bigr)\Bigl(-\frac12\Bigr)^k=\frac45\cdot\Bigl(-\frac12\Bigr)+\frac35\cdot\frac14+\frac25\cdot\Bigl(-\frac18\Bigr)+\frac15\cdot\frac{1}{16}=-\frac{23}{80}.
$$
The variance multiplier is $1+2(-23/80)=17/40=0.425$. Under this page's convention, $\sigma^2/n_{\mathrm{eff}}=\Var(\overline X)$ and $\Var(\overline X)$ equals $(\sigma^2/n)$ times the multiplier, so
$$
\Var(\overline X)=\frac{17}{200}\sigma^2=0.085\sigma^2,\qquad n_{\mathrm{eff}}=\frac{5}{0.425}=\frac{200}{17},
$$
which is $11.765$ to three decimal places. The double sum gives the same variance of the mean. With $S=\sum_{i=1}^5(X_i-\mu)$,
$$
\frac{\Var(S)}{\sigma^2}=5+2\sum_{k=1}^{4}(5-k)\Bigl(-\frac12\Bigr)^k=\frac{17}{8},
$$
and $\Var(\overline X)=\Var(S)/25=(17/200)\sigma^2$. The lag-one correlation does most of the work. There are $2(5-1)=8$ ordered pairs at lag one, each with correlation $-1/2$, and those pairs contribute $-4\sigma^2$ to $\Var(S)$. The later alternating lags do not restore the uncorrelated value $5\sigma^2$. The sum is less variable than the sum of five uncorrelated draws, so the mean is more precise, and the independent sample that matches its variance is longer than five.

That longer number is not a longer series. Whatever mechanism produced the dependence still contributes five random variables. The exact size $200/17$, reported as $11.765$ to three decimal places, says only that $\Var(\overline X)$ equals the variance of the mean of that many independent draws with the same $\sigma^2$. The comparison is for this mean. A different function of the same variables can have different autocorrelations and a different effective size. It is not evidence of convergence: the algebra assumes the stated stationary autocorrelations and does not test them. The long-run formula drops $(1-k/n)$ and extends the geometric series to infinity. For $\rho=-1/2$ that limiting multiplier is $(1+\rho)/(1-\rho)=1/3$, and $5/(1/3)=15$, which is not $11.765$. Version 2.39 of the Stan reference manual gives effective sample size the role in the Markov chain central limit theorem that the number of independent draws has in the ordinary central limit theorem.{{cite:stan_reference_analysis2026}} (§16.4, p. 196) The same section defines that size by the infinite sum $N/(1+2\sum_{t=1}^{\infty}\rho_t)$ and notes that anticorrelated draws can make it larger than the number of iterations.{{cite:stan_reference_analysis2026}} (§16.4, p. 197) The value $0.425$ is the finite-$n$ multiplier just computed, not that infinite sum and not a quantity estimated from simulated draws.

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
provided $|\rho|<1$. Dividing $n$ by that constant is the limiting effective sample size. If $-1<\rho<0$, the constant is smaller than $1$, so the limit exceeds $n$. The finite-sum weights $(1-k/n)$ are exactly $(n-k)/n$, so the display in the definition matches this expansion. Those weights are why a short alternating series need not agree with the limit.
:::
:::

## Statistical use — Reporting a Monte Carlo mean
If a posterior mean is estimated by $\overline X$ from a stationary chain, the Monte Carlo standard error is $\sqrt{\Var(\overline X)}$, not $\sigma/\sqrt{n}$, unless the multiplier is 1. Quoting $n_{\mathrm{eff}}$ beside the estimate states that variance comparison for the mean being reported. It does not say that some fraction of the stored length remains after dependence. For the five draws with $\rho_k=(-1/2)^k$, the multiplier is $0.425$ and the mean's effective size is $11.765$, which is larger than the number stored. The comparison does not add draws, and it does not check convergence. A second function of the same draws, such as $\overline{g(X)}$, needs its own autocorrelations. One effective sample size does not serve every functional. Thinning, keeping every $k$th draw, reduces $n$ and usually does not increase $n_{\mathrm{eff}}$ by the same factor, because the discarded draws still carried some information.{{cite:geyer1992}} (§§3.3–3.7, pp. 477–480)

## Worked example
For the geometric case $\rho=0.8$ and $n=1000$, $(1+\rho)/(1-\rho)=9$ and $n_{\mathrm{eff}}\approx111.11$. If $\sigma^2=1$, the independent-draw variance of the mean would be $0.001$, with standard error $0.03162$. The dependent variance is about $0.009$, with standard error $0.09487$. The ratio of those standard errors is $\sqrt{9}=3$.

For the exact five-term sum above, the multiplier is $2.225$ and $n_{\mathrm{eff}}=2.247$. A report that said "5 draws" would overstate the precision by a factor of $\sqrt{2.225}=1.492$. The alternating correlations $\rho_k=(-1/2)^k$ run the comparison the other way. The same finite-sample convention gives multiplier $0.425$ and $n_{\mathrm{eff}}=11.765$ from those five draws, so a report of five draws would understate the precision of this mean. The number $11.765$ is still the independent sample whose mean has the same variance. It is not a count of extra stored draws, and it is not evidence that the series has converged.

**Your turn.** For a long run with $\rho=1/3$, what is $(1-\rho)/(1+\rho)$, and what is $n_{\mathrm{eff}}$ when $n=900$?

::: {.callout-tip collapse="true" title="Answer"}
$(1-1/3)/(1+1/3)=(2/3)/(4/3)=1/2$. Then $n_{\mathrm{eff}}\approx900/2=450$. Positive correlation has halved the effective length. The formula is the long-run limit, not the exact finite-sum multiplier.
:::

## Common misconceptions
The iteration count is not the effective sample size. A chain of length 1000 with $\rho=0.8$ is worth about 111 independent draws for the mean. The effective sample size is not evidence that the chain has the right stationary distribution. It measures dependence given that the draws are already stationary with variance $\sigma^2$. A large $n_{\mathrm{eff}}$ from the wrong target is a precise estimate of the wrong mean. And one number does not describe every summary. The indicator $1_{\{X>c\}}$ can be much more, or much less, autocorrelated than $X$.

Effective sample size is also not a portion of the stored run left after dependence, and it is not bounded by the stored length. That bound would follow only if $n_{\mathrm{eff}}$ counted a subset of the draws. The definition matches variances instead. Positive correlation makes the match smaller than $n$, as with $\rho_k=(1/2)^k$ and $n_{\mathrm{eff}}=2.247$. Negative correlation can make it larger. For $\rho_k=(-1/2)^k$ the finite-sample multiplier is $0.425$ and $n_{\mathrm{eff}}=11.765$ from five draws, because successive deviations tend to cancel in the sum and this mean is more precise than the mean of five independent draws with the same variance. A remark that dependent draws always contain less information than the same number of independent draws is the positive-correlation case. It does not hold for this alternating series. The larger value does not mean more draws were stored, and the cancellation assumes the stated stationary correlations rather than establishing them. Effective sample size replaces the independent count in the Markov chain central limit theorem.{{cite:stan_reference_analysis2026}} (§16.4, p. 196) Anticorrelation can place it above the number of iterations.{{cite:stan_reference_analysis2026}} (§16.4, p. 197) Neither statement is evidence that the chain has converged.

## Assumptions and limits — Stationarity, and a variance that exists
The variance formula uses a single $\sigma^2$ and autocorrelations that depend on lag only. That is stationarity, and the correlations themselves require $0<\sigma^2<\infty$. The formula does not assume that those correlations are positive. A negative weighted sum is a valid input. It produces a finite effective size above $n$ only when the multiplier is positive, so that the variance of the mean is positive. An effective size above $n$ remains conditional on those assumptions. It is not a test that they hold, and it is not a test of convergence.

A multiplier of zero is a different boundary, and it does not define a finite effective sample size. Let $Z$ be symmetric about zero, not almost surely constant, and of finite variance $\sigma^2>0$, and set $X_t=(-1)^t Z$. Symmetry about zero gives $-Z$ the same distribution as $Z$, so the marginal law does not depend on time and the lag correlation is $\rho_k=(-1)^k$. When $n$ is even, $\sum_{t=1}^n(-1)^t=0$, hence $\sum_{t=1}^n X_t=0$ and the sample mean is zero with probability one. The finite-sample multiplier is therefore zero. No finite independent sample matches that mean. The geometric series with $\rho_k=(-1/2)^k$ is not this process: its correlations decay, the multiplier at $n=5$ is the positive number $0.425$, and the variance of its mean is positive.

A chain that is still drifting has a mean that changes with time, and the sum does not describe $\overline X$. If $\sigma^2$ is infinite, there is no $\sigma^2/n_{\mathrm{eff}}$ to compute. Heavy tails break the formula before dependence does. The geometric formula also needs $|\rho|<1$. At $\rho=1$ the series does not decay, the inflation grows with $n$, and the effective size stays bounded while $n$ grows. Finally, the plug-in estimate of $\rho_k$ from a single chain is itself random. The identity above is for known autocorrelations. An estimated $n_{\mathrm{eff}}$ carries its own error, especially when the sum is truncated at a lag chosen from the same series.

## Connections
A [Markov chain](markov-chain.qmd) is the usual source of the dependence. [Monte Carlo](monte-carlo-method.qmd) with independent draws is the case $n_{\mathrm{eff}}=n$. [Metropolis–Hastings](metropolis-hastings-algorithm.qmd) can be stationary and still have $\rho$ near 1 if the proposals are tiny. [Detailed balance](detailed-balance.qmd) fixes the stationary distribution of a reversible kernel and says nothing about the size of $\rho$.{{cite:geyer1992}} (§§3.3–3.7, pp. 477–480)

## Check yourself

### One change in a trace {#self-check-ex-ur-one-change}

A stored series has $n=400$ and geometric autocorrelation $\rho=0.5$. Using the long-run formula, what is $n_{\mathrm{eff}}$?

[Exercise](../questions/ex-ur-one-change.qmd)

::: {.callout-tip collapse="true" title="Answer"}
$(1-0.5)/(1+0.5)=1/3$, so $n_{\mathrm{eff}}\approx400/3=133.33$. The variance of the mean is about three times the independent-draw variance. The exact finite-sample multiplier is a little different, because the factors $(1-k/n)$ have been replaced by 1.
:::

### A posterior mean {#self-check-ex-ur-posterior-mean}

Why can two posterior summaries from the same chain have different effective sample sizes?

[Exercise](../questions/ex-ur-posterior-mean.qmd)

::: {.callout-tip collapse="true" title="Answer"}
Each summary is a function $g(X_t)$. The autocorrelations of $g(X_t)$ need not equal the autocorrelations of $X_t$. The variance multiplier is computed from the series actually averaged. A precise mean does not imply a precise tail probability.
:::

## History
The variance formula for a mean of a stationary sequence is the double sum of the lag covariances. Dependence is separate from stationarity: a stationary chain has one marginal at every time, and the dependence between times is what the effective sample size converts into an equivalent independent count. The numerical factor $(1+\rho)/(1-\rho)$ is the long-run geometric special case of the same sum. On a short series the factors $(1-k/n)$ remain, so a negative geometric correlation can make the finite-sample effective size larger than $n$.
