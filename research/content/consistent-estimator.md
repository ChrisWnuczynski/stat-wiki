## Motivating example
An estimator can be correct on average while failing to use new information. Using the first observation as an estimate of a population mean is unbiased under independent identical sampling, but collecting further observations never changes it. Consistency instead asks whether an estimator concentrates near its target as the sample size grows. Laws of large numbers explain why averages often have that property.{{cite:grinstead_snell1997}} (§8.1)

## Definition — A sequence indexed by sample size
For each parameter value $\theta$, consistency means $T_n\to\theta$ in probability under the corresponding sampling law:
$$
\mathbb P_\theta(|T_n-\theta|>\varepsilon)\longrightarrow0
\quad\text{for every }\varepsilon>0.
$$
The probability is over hypothetical repetitions of the data-generating experiment. The definition does not say that each realised estimate becomes closer at every step, or that convergence is uniform over all parameter values.{{cite:durrett2019}} (§2.2)

## Properties — Mean squared error supplies a sufficient condition
If $\mathbb E_\theta[(T_n-\theta)^2]\to0$, Markov's inequality applied to the squared error gives
$$
\mathbb P_\theta(|T_n-\theta|>\varepsilon)
\le\frac{\mathbb E_\theta[(T_n-\theta)^2]}{\varepsilon^2}\to0.
$$
This proves consistency directly. With finite second moments, the mean squared error is the sum of variance and squared bias, so both tending to zero is sufficient. It is not necessary to have zero bias at every sample size.{{cite:durrett2019}} (§§1.6.1 and 2.2.1)

For iid observations with mean $\theta$ and finite variance $\sigma^2$, the sample mean has variance $\sigma^2/n$. Hence it is consistent. The sequence $\overline X_n+1/n$ is biased, but its mean squared error is $\sigma^2/n+1/n^2$, which also tends to zero. Conversely, the estimator $X_1$ has the same distribution at every sample size and generally fails to concentrate.{{cite:grinstead_snell1997}} (§8.1)

## Worked example — Exact normal error probabilities
Let $X_i$ be iid normal with mean $\theta$ and variance $1$. Then
$$
\mathbb P_\theta(|\overline X_n-\theta|>0.2)
=2\{1-\Phi(0.2\sqrt n)\}.
$$
The probabilities are $0.31731$ at $n=25$, $0.04550$ at $n=100$, and $0.00006334$ at $n=400$. Their decrease quantifies concentration for this model and tolerance, rather than giving a universal sample-size prescription. The calculation uses the normal distribution of a sum of independent normal variables.{{cite:grinstead_snell1997}} (§7.2)

For the unbiased estimator $T_n=X_1$, the corresponding probability stays $2\{1-\Phi(0.2)\}$ at every $n$. Its failure is visible without any limiting approximation. Bias and consistency answer different questions: one compares an expectation with the target, while the other compares entire sampling distributions as $n$ grows.{{cite:durrett2019}} (§2.2)

**Your turn.** If the sample size is multiplied by four in this normal-mean model, what happens to the variance and standard error of the sample mean?

::: {.callout-tip collapse="true" title="Answer"}
Variance changes from $1/n$ to $1/(4n)$, so it is divided by four. Standard error changes from $1/\sqrt n$ to $1/(2\sqrt n)$, so it is halved.
:::

## Check yourself

### Consistency of a Poisson mean {#self-check-ex-inf-poisson-mle}
[A Poisson mean](../questions/ex-inf-poisson-mle.qmd): find its estimator and show consistency.

::: {.callout-tip collapse="true" title="Answer"}
The likelihood is maximised at $\overline X$, including the boundary value zero if all observations vanish. Its expectation is $\theta$ and variance is $\theta/n$, so its mean squared error tends to zero and the probability bound above proves consistency.
:::

### Concentration and coverage {#self-check-ex-inf-two-standard-errors}
[Two standard errors](../questions/ex-inf-two-standard-errors.qmd): find the exact normal coverage and a 99% multiplier.

::: {.callout-tip collapse="true" title="Answer"}
Coverage is $2\Phi(2)-1=0.9545$. The 99% multiplier is $\Phi^{-1}(0.995)=2.57583$. The interval shrinks with $n$ while preserving that fixed coverage under the stated normal model.
:::
### An exponential rate {#self-check-ex-inf-exponential-mle}

[An exponential rate](../questions/ex-inf-exponential-mle.qmd)

Let $X_1,\ldots,X_n$ be a random sample from the exponential distribution with rate $\lambda$, density $\lambda e^{-\lambda x}$ for $x>0$.{{cite:siegrist_mle2022}} (§ “The Gamma Distribution; Extending the Method and the Invariance Property”)

(a) Find the maximum likelihood estimator of $\lambda$, and check that it is a maximum.

(b) Find the method-of-moments estimator of $\lambda$.

(c) Use invariance to find the maximum likelihood estimator of the median lifetime $(\log 2)/\lambda$.

:::::::: {.callout-tip collapse="true" title="Answer"}

(a) For this exponential model, the log likelihood has the following form.

$$
\log L(\lambda)=n\log\lambda-\lambda\sum_{i=1}^nx_i.
$$

Its derivative $n/\lambda-\sum x_i$ is zero at $\lambda=n/\sum x_i=1/\overline x$. The second derivative, $-n/\lambda^2$, is negative, so this is a maximum. The estimator is $\widehat\lambda=1/\overline X$.

(b) $\mathbb{E} X=1/\lambda$. Setting $1/\lambda=\overline x$ gives the same estimator, $1/\overline X$.

(c) The median lifetime $m$ solves $1-e^{-\lambda m}=1/2$, so $m=(\log2)/\lambda$. By invariance its maximum likelihood estimator is $(\log2)/\widehat\lambda=\overline X\log2$.

::::::::
