## Motivating example
A laboratory wants an interval for the mean error of an instrument. If the population standard deviation were known, the mean error divided by its standard deviation would be standard normal. Estimating that standard deviation from the same measurements introduces additional uncertainty. The Student pivot accounts for that uncertainty through its degrees of freedom.{{cite:dodge2008}} (p. 526, Student Distribution)

## Statement
Assume $n\ge2$, independent measurements $X_i\sim N(\mu,\sigma^2)$ and $\sigma^2>0$. Define $S^2=(n-1)^{-1}\sum_i(X_i-\bar X)^2$. The pivot $T=(\bar X-\mu)/(S/\sqrt n)$ is distributed as $t_{n-1}$. A pivot is a function of the data and the parameter whose sampling law has no unknown parameter. In a sample from this continuous model, $S>0$ with probability one.{{cite:siegrist2022_normals}} (§6.08, “The T Variable”)

The centring parameter is the true $\mu$, rather than an arbitrary hypothesised value. Replacing it by $\mu_0$ gives a test statistic with the central $t$ law only when $\mu=\mu_0$. Away from the null it has a noncentral $t$ distribution with noncentrality $\sqrt n(\mu-\mu_0)/\sigma$. The distinction matters for power: a null reference distribution determines a rejection threshold, while an alternative sampling law determines how often that threshold is crossed.

## Intuition — Two independent pieces produce the ratio
The numerator $Z=\sqrt n(\bar X-\mu)/\sigma$ is standard normal. The denominator's squared scale $V=(n-1)S^2/\sigma^2$ is chi-squared with $n-1$ degrees of freedom. Normal sampling also makes $Z$ independent of $V$. Thus $T=Z/\sqrt{V/(n-1)}$, precisely the construction of the Student distribution. The scale estimate occasionally falls below the population scale; this is why the ratio has heavier tails than a standard normal variable.{{cite:dodge2008}} (p. 526, mathematical aspects){{cite:siegrist2022_normals}} (§6.08, sample variance and the T variable)

## Proof
Choose an orthogonal $n\times n$ matrix whose first row is $n^{-1/2}(1,\ldots,1)$. Apply it to the standardised error vector $(X-\mu\mathbf1)/\sigma$. Orthogonal invariance of the standard normal density makes all transformed coordinates independent standard normals. The first is $Z$; the sum of squares of the remaining $n-1$ coordinates is $V$, by preservation of squared length and the identity $\sum_i(X_i-\mu)^2=\sum_i(X_i-\bar X)^2+n(\bar X-\mu)^2$. Therefore $V$ is chi-squared and independent of $Z$, proving the pivot law.{{cite:siegrist2022_normals}} (§6.08, independence and chi-square law of the sample variance)

## Statistical use — Invert the probability statement
If $c=t_{n-1;1-\alpha/2}$, then $P(-c\le T\le c)=1-\alpha$. Multiply the inequalities by $S/\sqrt n$ and rearrange to obtain $\bar X\pm cS/\sqrt n$. The coverage statement concerns intervals from repeated samples at a fixed population mean. The realised endpoints are numbers; the frequentist probability is attached to the random procedure before the measurements are observed.{{cite:nist_mean_limits2002}} (§1.3.5.2)

The same calculation supplies a test of a specified mean. The two-sided test rejects precisely when the corresponding interval omits that mean. This equivalence follows directly from the same pair of inequalities and uses the same confidence level and model assumptions. It does not extend automatically to a data-dependent choice of one-sided or two-sided testing after looking at the sign of the observed mean.

## Worked example
### Nine calibration measurements
Suppose nine measurements have mean $2.4$ and corrected standard deviation $1.8$. Testing a zero mean gives $t=2.4/(1.8/3)=4.000$ with eight degrees of freedom. The two-sided tail probability is $0.003950$. For a 95% interval, $c=2.306004$, so the margin is $1.383602$ and the interval is $(1.016398,3.783602)$. These are illustrations of the pivot calculation, rather than a normality diagnosis.{{cite:nist_process_mean2002}} (§7.2.2, test statistic and rejection rules)

**Your turn.** Keep the same sample mean and standard deviation but increase the sample size to 36. What is the estimated standard error and the statistic for a zero mean?

::: {.callout-tip collapse="true" title="Answer"}
The standard error becomes $1.8/6=0.300$ and the statistic becomes $2.4/0.3=8.000$, with 35 degrees of freedom under normal sampling.
:::

## Common misconceptions — Studentisation needs its sampling model
Using a Student quantile does not turn arbitrary observations into a normal sample. Strong dependence, an extreme outlier or a heavily skewed small sample can invalidate exact calibration. With non-normal independent observations, large-sample approximations need separate conditions; the exact finite-sample independence of the mean and variance is a special normal property. A standard error computed from a clustered design must reflect that design before a reference distribution is chosen.{{cite:openintro2019}} (§7.1.2, conditions for inference on a mean)
