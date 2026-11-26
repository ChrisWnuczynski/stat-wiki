## Lead context
Student’s t law is the reference distribution for a normal sample mean when the same small sample must also supply the scale.{{cite:student1908}} (pp. 1–2){{cite:dodge2008}} (p. 526)

## Motivating example
For $\nu=5$ the variance is $5/(5-2)=5/3\approx 1.6667$, against $1$ for a standard normal variable. The two-sided tail is
$$
P(|T|>2)=2\,P(T>2)\approx 0.1019.
$$
A standard normal variable has $P(|Z|>2)\approx 0.0455$, less than half the $t_5$ tail. For $\nu=8$ the variance is $8/6=4/3\approx 1.3333$, and the $0.975$ quantile used in a two-sided $95\%$ interval is $2.30600$. The normal quantile $1.95996$ is smaller because it does not pay for an estimated scale.

## Intuition — Estimating the scale thickens the tails
If the population standard deviation were known, a normal sample mean could be standardised to a standard normal variable. In a small sample the scale is estimated from the same observations, and that extra uncertainty produces a heavier-tailed reference law. Student’s 1908 paper treats the sample as one draw from a population of experiments and asks how to judge a mean when the sample itself is the only guide to the variability. The density is symmetric about zero. Its variance $\nu/(\nu-2)$ exceeds $1$ whenever the variance exists, and it falls toward $1$ only as the degrees of freedom grow.{{cite:student1908}} (pp. 1–2){{cite:dodge2008}} (p. 526)

## Definition
The density on $\nu>0$ degrees of freedom is
$$
f(t)=\frac{\Gamma((\nu+1)/2)}{\sqrt{\nu\pi}\,\Gamma(\nu/2)}\Bigl(1+\frac{t^{2}}{\nu}\Bigr)^{-(\nu+1)/2}.
$$
If $Z$ is standard normal, $X$ is chi-squared with $\nu$ degrees of freedom, and $Z$ and $X$ are independent, then $T=Z/\sqrt{X/\nu}$ has this density. For an independent sample from a normal population, the usual one-sample pivot
$$
T=\frac{\sqrt{n}\,(\bar x-\mu)}{S}
$$
has exactly the $t$ distribution on $n-1$ degrees of freedom, where $S^{2}$ is the sample variance with divisor $n-1$. The mean is $0$ for $\nu>1$. The variance is $\nu/(\nu-2)$ for $\nu>2$. At $\nu=1$ the density is the standard Cauchy density.{{cite:dodge2008}} (p. 526)

## Properties
The density is symmetric about zero, so every odd moment that exists is zero. The mean is $0$ for $\nu>1$; the variance is $\nu/(\nu-2)$ for $\nu>2$, is infinite for $1<\nu\le2$, and at $\nu=1$ even the mean fails to exist. The tails are heavier than the normal tails at every finite $\nu$: the density decays like $|t|^{-(\nu+1)}$, a power law rather than the normal law's exponential decay, which is why the $0.975$ quantile at $\nu=8$ is $2.30600$ rather than the normal $1.95996$. As $\nu$ grows, the density converges to the standard normal density and the variance falls to $1$.{{cite:siegrist2022_normals}} (§6.08, “The One Sample Model”, the $T$ variable)

## Worked example

**Your turn.** State the variance of a $t$ random variable on $3$ degrees of freedom, and say what the variance formula returns at $2$ degrees of freedom.

::: {.callout-tip collapse="true" title="Answer"}
At $\nu=3$ the variance is $3/(3-2)=3$. At $\nu=2$ the formula $\nu/(\nu-2)$ has a zero denominator. The second moment is not finite, so the variance is undefined. The mean still exists, because $2>1$.
:::

**Check yourself.** A $t$ statistic uses $S$ in the denominator and a normal statistic uses the known $\sigma$. Which reference distribution belongs to which statistic, for an independent normal sample?

::: {.callout-tip collapse="true" title="Answer"}
The statistic with $S$ and divisor $n-1$ has the $t_{n-1}$ law. The statistic that divides by the known $\sigma$ has the standard normal law. Using normal critical values when $S$ replaced $\sigma$ treats the scale as known.
:::

**Check yourself.** Why is a $t_1$ random variable a poor input to a sample-mean calculation?

::: {.callout-tip collapse="true" title="Answer"}
The $t_1$ law is the standard Cauchy law, which has no finite mean. An average of independent copies does not converge to a population mean, because that mean is not defined. The variance formula is already inapplicable at $\nu=1$.
:::

## Common misconceptions
The $t$ law is sometimes treated as a general small-sample correction that makes normal-theory intervals safe for any data. It is not. Its heavier tails price in one specific uncertainty — the scale estimated from the same sample — under the assumption that the observations are independent and normal. For skewed or heavy-tailed data the pivot's law is not $t$, and substituting $t$ critical values does not repair that; nor does a larger critical value make the procedure exact, since exactness here is a property of the sampling model, not of the sample size.{{cite:siegrist2022_normals}} (§6.08, “The One Sample Model”, the $T$ variable)

## Connections
The [normal distribution](normal-distribution.qmd) is the limit as the degrees of freedom grow, and it is the exact law when the scale is known. The [Cauchy distribution](cauchy-distribution.qmd) is the case $\nu=1$. A [chi-squared distribution](chi-squared-distribution.qmd) supplies the denominator of the representation $Z/\sqrt{X/\nu}$. Intervals that invert the $t$ statistic are built from a [pivot](pivot.qmd) whose reference law is this density.{{cite:dodge2008}} (p. 526)
