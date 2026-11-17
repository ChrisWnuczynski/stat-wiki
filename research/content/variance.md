## Lead context
It lets you distinguish outcomes that have the same average but very different risks of landing far from it. For observations in a sample, the related [sample variance](sample-variance-and-standard-deviation.qmd) estimates this population quantity.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)

## Motivating example
Two buses both have an average delay of ten minutes. Bus A is always ten minutes late; bus B is on time half the days and twenty minutes late on the other half. The average alone makes the services look identical, yet bus B is much less predictable. Variance assigns zero to A's delay and 100 squared minutes to B's delay, capturing the difference that matters if you must plan a connection.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)

## Intuition
Subtracting the mean measures how far each outcome strays from its centre. The positive and negative deviations cancel if simply averaged, so variance squares them first. A large miss then counts more than a small one. The result has squared units; its square root, the [standard deviation](sample-variance-and-standard-deviation.qmd), has the original units.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)

## Definition
Here $X$ is the random variable and $\mu=\mathbb{E}X$ is its mean. The definition requires a finite second moment, $\mathbb{E}X^2<\infty$; otherwise a finite variance is unavailable. For a discrete $X$ with values $x$ and mass function $p(x)$, the expectation in the definition is $\sum_x (x-\mu)^2p(x)$; for a continuous $X$ with density $f(x)$ it is $\int_{-\infty}^{\infty}(x-\mu)^2f(x)\,\mathrm{d}x$. These are the same definition applied to two kinds of distribution.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)

## Properties
Variance is nonnegative, and $\operatorname{Var}(X)=0$ exactly when $X$ equals its mean with probability one. For constants $a$ and $b$, $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$: shifting every outcome leaves spread alone, while doubling the measurement scale quadruples variance. If $X$ and $Y$ have finite second moments, then $\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)$, where $\operatorname{Cov}$ denotes [covariance](covariance.qmd). The final term vanishes for independent variables, but independence is a sufficient condition, not a necessary one.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)

Proof idea: expand squared centred deviations and use linearity of expectation. For the zero case, a nonnegative random variable has expectation zero only if it is zero almost surely.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $\mu=\mathbb{E}X$. Expanding the square gives $\mathbb{E}(X-\mu)^2=\mathbb{E}X^2-2\mu\mathbb{E}X+\mu^2=\mathbb{E}X^2-\mu^2$, proving the equivalent formula in the definition. The square is nonnegative. If its expectation is zero, then for every $\varepsilon>0$, $\mathbb{P}((X-\mu)^2\geq\varepsilon)\leq\mathbb{E}(X-\mu)^2/\varepsilon=0$; hence $X=\mu$ almost surely. The converse follows directly. Also $aX+b-\mathbb{E}(aX+b)=a(X-\mu)$, so taking the expected square yields the scaling identity. Finally put $\nu=\mathbb{E}Y$, expand $((X-\mu)+(Y-\nu))^2$, and take expectations. The cross term is $2\mathbb{E}[(X-\mu)(Y-\nu)]=2\operatorname{Cov}(X,Y)$. Under independence this expectation factors into the product of two zero means. Repeatedly applying that independent-sum identity to $X_1,\ldots,X_n$ gives variance $n\sigma^2$ for their sum; scaling by $1/n$ gives variance $\sigma^2/n$ for their average.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)
:::
:::

## Statistical use
If $X_1,\ldots,X_n$ are independent measurements with the same variance $\sigma^2$, their average $\overline X$ has variance $\sigma^2/n$. This is why repeated independent measurements make the mean more precise; the standard error falls in proportion to $1/\sqrt n$. Correlated measurements need covariance terms, so the same sample size can give less precision. In data analysis, [sample variance and standard deviation](sample-variance-and-standard-deviation.qmd) estimate population spread, and a [standard error](standard-error.qmd) describes the spread of an estimator across repeated samples.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)

## Worked example
Suppose a delivery is early by two minutes with probability $1/4$, on time with probability $1/2$, and late by four minutes with probability $1/4$. Let $X$ be its signed delay in minutes, so its possible values are $-2$, $0$, and $4$. The mean is $\mu=(-2)(1/4)+0(1/2)+4(1/4)=1/2$ minute. The second moment is $\mathbb{E}X^2=4(1/4)+0+16(1/4)=5$ square minutes. Thus $\operatorname{Var}(X)=5-(1/2)^2=19/4=4.75$ square minutes and the standard deviation is $\sqrt{19}/2\approx2.179$ minutes. The occasional four-minute delay raises spread even though half the deliveries are exactly on time.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)

**Your turn.** A fair three-sided spinner pays $1$, $3$, or $5$ dollars. Find the mean and variance of the payout.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $(1+3+5)/3=3$ dollars. The squared deviations are $4$, $0$, and $4$, so the variance is $(4+0+4)/3=8/3$ square dollars.
:::

The [normal-variance derivation](../questions/ex-prob-normal-variance.qmd) applies the second-moment identity to a continuous density.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)

Try [recovering the second moment](../questions/ex-prob-second-moment.qmd) from a mean and variance. Then try [proving the normal variance](../questions/ex-prob-normal-variance.qmd) by integration. Reveal each answer when you are ready.

::: {.callout-tip collapse="true" title="Answers"}
In the first question, $\mathbb{E}X^2=\operatorname{Var}(X)+(\mathbb{E}X)^2=1+2^2=5$. In the second, integration by parts gives variance $1$ for a standard normal; the affine scaling identity then gives $\operatorname{Var}(\mu+\sigma X)=\sigma^2$.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)
:::

## Common misconceptions
Variance and standard deviation describe the same spread on different scales: a variance of $4$ square metres corresponds to a standard deviation of $2$ metres, not $4$ metres. The variance of a distribution is also distinct from the variance computed from one sample; the latter changes when a new sample is drawn. Finally, variances of sums add only when the covariance terms are zero. For example, if $Y=-X$ and $\operatorname{Var}(X)>0$, then $\operatorname{Var}(X+Y)=0$, although each summand has positive variance.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)

## Assumptions and limits
A mean need not describe the typical outcome when the tails are very heavy. The [Cauchy distribution](cauchy-distribution.qmd) has no finite mean or variance, so a reported variance from a finite Cauchy sample is merely a volatile sample summary, not an estimate of a finite population variance. Even with finite variance, squaring gives extreme observations considerable influence; a median absolute deviation may better describe spread for contaminated data.{{cite:nist_handbook2002}} (§1.3.5.6)

## Connections
[Covariance](covariance.qmd) generalises variance to two random variables; setting both arguments equal recovers $\operatorname{Var}(X)=\operatorname{Cov}(X,X)$. The [standard error](standard-error.qmd) is a standard deviation of an estimator, so the independent-measurement calculation above connects population variance to the uncertainty of a sample mean. [Sample variance](sample-variance-and-standard-deviation.qmd) uses the observed deviations from the sample mean to estimate this population quantity.{{cite:grinstead_snell1997}} (Ch. 6, §§6.2–6.3)

## History
Fisher used the word *variance* in his study of resemblance between relatives, read to the Royal Society of Edinburgh in 1918 and published in its 1919 volume. He sought to separate sources of variation in inherited traits; squared standard deviations were useful because independent contributions could be added. His paper explicitly named that square the variance.{{cite:fisher1919_variance}} (p. 399)
