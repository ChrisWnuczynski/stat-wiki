## Lead context
Precision weighting gives the more precise of two normal estimates the larger share of their compromise.

## Motivating example
Four observations with mean $10$ and variance $1$, and a standard normal prior, put weight $0.8$ on the sample mean. The posterior mean is $8$ and the posterior variance is $0.2$.

## Intuition — Add the precisions, and weight the estimates by them
The precision of a normal estimate is the reciprocal of its variance. A sample mean from \(n\) observations with variance \(\sigma^2\) has precision \(n/\sigma^2\). A normal prior for the mean, with variance \(\sigma_0^2\), has precision \(1/\sigma_0^2\). The posterior precision is the sum, and the posterior mean is the corresponding weighted average of the sample mean and the prior mean. A vague prior has a small precision and barely moves the sample mean. A tight prior can outweigh a short sample.

## Definition — Known-variance normal mean
Let \(X_1,\ldots,X_n\) be independent \(N(\mu,\sigma^2)\) with \(\sigma^2\) known, and let the prior be \(\mu\sim N(\mu_0,\sigma_0^2)\). Write \(\kappa_0=\sigma^2/\sigma_0^2\). The posterior mean is
\[
\mu_1=\frac{n\bar x+\kappa_0\mu_0}{n+\kappa_0}.
\]
The weight on the sample mean is \(n/(n+\kappa_0)\), and the weight on the prior mean is \(\kappa_0/(n+\kappa_0)\). {{cite:gelman_bda2013}} (§2.5, p. 40, eq. 2.10)

## Properties — Precisions add
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The log posterior density in \(\mu\), up to a constant, is
\[
-\frac{n}{2\sigma^2}(\mu-\bar x)^2-\frac{1}{2\sigma_0^2}(\mu-\mu_0)^2.
\]
This is a quadratic \(-\frac12 A(\mu-\mu_1)^2\) with \(A=n/\sigma^2+1/\sigma_0^2\) and
\[
\mu_1=\frac{(n/\sigma^2)\bar x+(1/\sigma_0^2)\mu_0}{A}.
\]
Dividing numerator and denominator by \(1/\sigma^2\) gives \((n\bar x+\kappa_0\mu_0)/(n+\kappa_0)\). When \(\sigma^2=1\), \(\mu_0=0\) and \(\sigma_0^2=\tau^2\), the weight on \(\bar x\) is \(a=n/(n+1/\tau^2)\), and the posterior variance is \(a/n\). {{cite:gelman_bda2013}} (§2.5, p. 40, derivation around eqs. 2.9–2.10)
:::
:::

## Worked example — Four observations, prior standard deviation \(1\)
Take \(n=4\), \(\bar x=10\), \(\sigma^2=1\), \(\mu_0=0\) and \(\tau^2=1\). Then \(a=4/(4+1)=0.8\), the posterior mean is \(0.8\times 10=8\), and the posterior variance is \(0.8/4=0.2\). The prior, which is as precise as one observation, pulls the sample mean two units toward \(0\).

A second sample has \(n=5\), \(\bar x=20\), \(\sigma^2=4\), \(\mu_0=16\) and \(\sigma_0^2=4\). Then \(\kappa_0=1\), and
\[
\mu_1=\frac{5\cdot 20+1\cdot 16}{6}=\frac{116}{6}=\frac{58}{3}\approx 19.3333.
\]
The sample of five observations outweighs a prior that counts as one observation, so \(58/3\) sits closer to \(20\) than to \(16\).

**Your turn.** Return to \(\sigma^2=1\), \(\mu_0=0\) and \(\tau^2=1\), now with \(n=9\) and \(\bar x=3\). Find the posterior mean and variance.

::: {.callout-tip collapse="true" title="Answer"}
\(a=9/(9+1)=0.9\). The mean is \(0.9\times 3=2.7\), and the variance is \(0.9/9=0.1\).
:::

## Connections — Squared error, pseudo-counts, and unequal studies
The posterior mean is that precision-weighted average of the prior mean and the sample mean. {{cite:gelman_bda2013}} (§2.5, pp. 39–40, normal model and eq. 2.10) The prior precision \(\kappa_0\) plays the role of a prior sample size when \(\sigma^2\) is the observation variance. The same weights combine two independent normal estimates of one mean: each estimate is weighted by the reciprocal of its variance. A [posterior mean](posterior-mean.qmd) that is not a normal–normal update need not be a precision-weighted average of this form.

