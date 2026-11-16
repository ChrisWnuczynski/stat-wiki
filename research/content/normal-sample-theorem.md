## Lead context
For a normal sample the mean and the sample variance have known laws, and they are independent, so a Student t interval does not need the unknown scale.

## Motivating example
Ten milk cartons have sample mean $1.0512$ litres and sample standard deviation $0.0317$. The standardised difference between that mean and a target of $1.10$ is about $-4.87$ on $9$ degrees of freedom. The reference distribution of that ratio is Student’s $t$ only because a normal sample makes the mean normal, the scaled variance chi-squared, and the two independent.{{cite:siegrist2022_normals}} (§6.08, The T Variable)

## Statement
Let $X_1,\ldots,X_n$ be independent $\operatorname{N}(\mu,\sigma^2)$ random variables, $n\ge 2$, with sample mean $\overline X$ and sample variance $S^2=(n-1)^{-1}\sum_i(X_i-\overline X)^2$. Then $\overline X$ is $\operatorname{N}(\mu,\sigma^2/n)$, $(n-1)S^2/\sigma^2$ is chi-squared on $n-1$ degrees of freedom, and $\overline X$ is independent of $S^2$.{{cite:siegrist2022_normals}} (§6.08, The Sample Mean; The Sample Variance)

The first claim is addition of independent normals and holds for the mean of any independent normal variables, whether or not the variance is the unbiased one. The chi-squared law and the independence use normality of the whole sample. Siegrist’s argument writes the deviations from $\overline X$ as a vector that is jointly normal with $\overline X$ and uncorrelated with it, hence independent of it, and then reads the chi-squared law from the moment generating function of the residual sum of squares.{{cite:siegrist2022_normals}} (§6.08, independence of $M$ and $S^2$; chi-square law of $V$)

## Intuition — Why the $t$ ratio has a known law
The ratio $T=(\overline X-\mu)/(S/\sqrt n)$ still contains $\mu$ and uses $S$ in place of $\sigma$. Under the three claims,
$$
T=\frac{Z}{\sqrt{V/(n-1)}},
$$
where $Z=(\overline X-\mu)/(\sigma/\sqrt n)$ is standard normal and $V=(n-1)S^2/\sigma^2$ is chi-squared on $n-1$ degrees of freedom, and $Z$ is independent of $V$. That is the definition of the Student $t$ law on $n-1$ degrees of freedom.{{cite:siegrist2022_normals}} (§6.08, The T Variable)

Without normality, $\E S^2=\sigma^2$ can still hold, and $\overline X$ is approximately normal for large $n$. The exact chi-squared divisor $n-1$, and the exact independence, do not survive an arbitrary change of distribution.{{cite:siegrist2022_normals}} (§6.08, The Sample Variance)

## Worked example
The sample $2,4,4,6$ has $n=4$ and $\overline x=4$. The sum of squared deviations is $4+0+0+4=8$, so $s^2=8/3$. If these were a normal sample with $\sigma=2$, the scaled variance would be $(n-1)s^2/\sigma^2=8/4=2$, a point on the $\chi^2_3$ scale. For a candidate mean $\mu=3$,
$$
t=\frac{4-3}{\sqrt{(8/3)/4}}=\sqrt{3/2}\approx 1.225
$$
on $3$ degrees of freedom. The number $1.225$ can be compared with a $t_3$ table; it is not itself a probability.

**Your turn.** For the sample $1,2,3,6$, compute $\overline x$ and $s^2$. Then compute the $t$ ratio for $\mu=0$, leaving it as a square root if you prefer.

::: {.callout-tip collapse="true" title="Answer"}
$\overline x=3$ and $\sum(x_i-\overline x)^2=14$, so $s^2=14/3$. The ratio is $3/\sqrt{(14/3)/4}=3\sqrt{6/7}\approx 2.777$ on $3$ degrees of freedom.
:::

**Check yourself.**

### Which expressions are statistics? {#self-check-ex-inf-which-are-statistics}

For a normal sample with both parameters unknown, which of $\overline X$, $\overline X-\mu$, and $(\overline X-\mu)/(S/\sqrt n)$ are statistics? For the last one, what is its distribution?

[Question-bank page](../questions/ex-inf-which-are-statistics.qmd)

::: {.callout-tip collapse="true" title="Answer"}
$\overline X$ is a statistic. $\overline X-\mu$ is not, because it contains $\mu$; its law is $\operatorname{N}(0,\sigma^2/n)$ and still depends on $\sigma$. The ratio $(\overline X-\mu)/(S/\sqrt n)$ is not a statistic either, but under the normal sample theorem its law is $t_{n-1}$ for every $\mu$ and $\sigma$.
:::

### Expectation of the sample variance {#self-check-ex-inf-expected-sample-variance}

For a random sample with mean $\mu$ and variance $\sigma^2$, show $\sum_i(X_i-\overline X)^2=\sum_i(X_i-\mu)^2-n(\overline X-\mu)^2$, and deduce $\E S^2=\sigma^2$.

[Question-bank page](../questions/ex-inf-expected-sample-variance.qmd)

::: {.callout-tip collapse="true" title="Answer"}
Expanding $X_i-\overline X=(X_i-\mu)-(\overline X-\mu)$ and summing gives the identity, because $\sum_i(X_i-\mu)=n(\overline X-\mu)$. Taking expectations, $\E\sum_i(X_i-\mu)^2=n\sigma^2$ and $\E[n(\overline X-\mu)^2]=\sigma^2$, so $\E[(n-1)S^2]=(n-1)\sigma^2$. This expectation does not need normality. The chi-squared law does.
:::

## Related concepts — The $t$ pivot and the chi-squared scale
The [pivot](pivot.qmd) $(\overline X-\mu)/(S/\sqrt n)$ is the $t$ ratio above. The [chi-squared distribution](chi-squared-distribution.qmd) on $n-1$ degrees of freedom is the law of $(n-1)S^2/\sigma^2$. The same three facts, applied inside groups, give the numerator and denominator of an [ANOVA $F$ statistic](anova-f-distribution.qmd). A [confidence interval](confidence-interval.qmd) for $\mu$ inverts $T$ and does not require a known $\sigma$.{{cite:siegrist2022_normals}} (§6.08, The T Variable)
