## Motivating example
In a sample of twenty independent items, finding no failures does not establish that the population failure probability is zero. Yet the Wald interval collapses to $[0,0]$ in precisely that situation. This exposes the difference between an estimate and a calibrated interval. Binomial discreteness and boundary values require special care.{{cite:nist_handbook2002}} (§7.2.4.1, exact intervals for small numbers of failures)

## Definition
The binomial model assumes a fixed number $n$ of independent trials with a common success probability $p$. The estimate $\widehat p=X/n$ has variance $p(1-p)/n$. The Wald formula replaces this unknown variance by its plug-in estimate. Its normal approximation needs enough successes and failures for the probability being requested; a count of expected successes is a diagnostic for that approximation, not an exact coverage theorem. The binomial variance $p(1-p)$ is largest at $p=1/2$ and falls to zero at the endpoints, which is why a plug-in standard error can look artificially precise when the observed fraction is $0$ or $1$.{{cite:grinstead_snell1997}} (§§5.1, 6.2, binomial distribution and variance)

## Properties — Keeping the parameter inside the standard error
Instead of substituting $\widehat p$ immediately, solve the score inequality
$$\frac{n(\widehat p-p)^2}{p(1-p)}\le z^2.$$
Multiplication and collection of powers give
$$(n+z^2)p^2-(2n\widehat p+z^2)p+n\widehat p^2\le0.$$
The roots define the Wilson interval,
$$\frac{\widehat p+z^2/(2n)\ \pm\ z\sqrt{\widehat p(1-\widehat p)/n+z^2/(4n^2)}}{1+z^2/n}.$$
It remains inside $[0,1]$ and avoids the zero-width boundary failure, while still using an approximate score-test calibration.{{cite:nist_handbook2002}} (§7.2.4.1, Wilson formulas)

## Worked example — No failures in twenty trials
For $X=0$, $n=20$, and $z=1.96$, the Wilson interval simplifies to $[0,z^2/(n+z^2)]\approx[0,0.1611]$. A two-sided equal-tail exact binomial interval instead has upper endpoint $1-(0.025)^{1/20}=0.1684$, because $\mathbb{P}_p(X=0)=(1-p)^{20}$. The exact interval is conservative in the sense of guaranteeing at least the advertised coverage under the binomial model, with coverage varying across $p$.{{cite:nist_handbook2002}} (§7.2.4.1, exact intervals for small numbers of failures)

**Your turn.** For zero successes in ten trials, calculate the Wilson upper endpoint with $z=1.96$ and compare it with the Wald upper endpoint.

::: {.callout-tip collapse="true" title="Answer"}
The Wilson upper endpoint is $3.8416/(10+3.8416)=0.2775$. The Wald endpoint is zero because its estimated standard error vanishes. The difference reflects the Wald method's failure at the boundary.
:::

## Interpretation — A difference of proportions
The nightmare example uses independent groups and adds their variance estimates. With the exact sample fractions, the estimated difference is $55/160-60/192=0.03125$ and its standard error is $0.050288$. The approximate 95% interval is $(-0.0673,0.1298)$. An interval that includes zero also allows substantively meaningful differences in either direction. Independence between groups and a sampling design supporting population inference remain necessary. For independent binomial counts the variance of a difference of sample proportions is the sum of the two binomial variances. A covariance term appears only when the same trials contribute to both proportions.{{cite:grinstead_snell1997}} (§§5.1, 6.2, binomial distribution and variance){{cite:dodge2008}} (pp. 106–107, confidence-interval construction and interpretation)

## Assumptions and limits
Clipping a Wald interval to $[0,1]$ removes impossible endpoints but cannot repair its coverage. Survey nonresponse, unequal sampling probabilities, and cluster sampling require additional design information. The success probability refers to a defined population and measurement process; mathematical precision in the binomial calculation does not remove systematic sampling error.{{cite:dodge2008}} (p. 107, domains and limitations of confidence intervals)

## Connections — The plug-in interval and a score interval answer neighbouring questions
Write $z$ for the standard normal quantile used as the multiplier. The Wald interval is
$$\widehat p\pm z\sqrt{\widehat p(1-\widehat p)/n}.$$
It recentres a normal approximation at the estimate and inserts the estimated variance. At $X=8$ successes in $n=10$ trials, $\widehat p=0.8$ and the plug-in standard error is $\sqrt{0.16/10}=0.126491$. The Wald interval with $z=1.96$ is $(0.5521,1.0479)$ before any clipping, so the upper end leaves the unit interval. Clipping it to $(0.5521,1)$ changes the displayed numbers and leaves the coverage of the original procedure unproved. The Wilson interval for the same count solves the score inequality instead of plugging $\widehat p$ into the variance. Its endpoints are approximately $0.4902$ and $0.9433$, both inside $(0,1)$. The shift of the lower end below $0.55$ is the score interval's response to variance that depends on the candidate $p$, not a different dataset.{{cite:nist_handbook2002}} (§7.2.4.1, Wilson formulas){{cite:grinstead_snell1997}} (§§5.1, 6.2, binomial distribution and variance)

An exact equal-tail binomial interval inverts the tests $\mathbb{P}_p(X\ge x)\le\alpha/2$ and $\mathbb{P}_p(X\le x)\le\alpha/2$. Because $X$ is discrete, the resulting coverage is at least $1-\alpha$ at every $p$ and is strictly larger at many $p$. The twenty-trial, zero-success calculation $1-(0.025)^{1/20}=0.1684$ is the upper end of that inversion when the lower end is $0$. The Wilson upper end $0.1611$ is a nearby approximation. Choosing the exact interval buys a guaranteed minimum coverage under the binomial model. Choosing the Wilson interval buys a shorter approximate interval that stays inside $[0,1]$. The Wald interval buys neither property at the boundary.{{cite:nist_handbook2002}} (§7.2.4.1, exact intervals for small numbers of failures)

## Statistical use — Planning a width still uses a variance
A planning formula for the Wald half-width replaces the unknown $p(1-p)$ by a provisional value. The largest binomial variance is $1/4$, at $p=1/2$, so $n\ge z^2/(4d^2)$ is a conservative normal-approximation sample size for half-width $d$. With $z=1.96$ and $d=0.05$, the bound is $384.16$, hence $385$ trials. If a provisional proportion $0.1$ is credible, $p(1-p)=0.09$ and the same half-width asks for about $139$ trials. Both calculations assume independent trials, a stable $p$, and a normal approximation that the eventual success and failure counts will have to justify. They do not repair a sample that stops when the proportion looks favourable.{{cite:grinstead_snell1997}} (§§5.1, 6.2, binomial distribution and variance){{cite:dodge2008}} (pp. 106–107, pivot construction and error allocation)

## Common misconceptions
A sample proportion of zero is a statement about the observed trials. It is compatible with a range of positive population probabilities, which is what the Wilson and exact upper endpoints display. A Wald interval of $[0,0]$ reports the plug-in variance, not that range. Adding two successes and two failures, or any other continuity adjustment, produces yet another interval and needs its own coverage argument. The numerical agreement of two such intervals on one sample is not a proof that they have the same coverage function.{{cite:nist_handbook2002}} (§7.2.4.1, Wilson formulas)

For two groups, an interval for $p_1-p_2$ that contains zero says the data are compatible with equality under the approximation and the sampling model. The nightmare interval $(-0.0673,0.1298)$ also contains differences of several percentage points. Compatibility with zero and compatibility with a scientifically large difference are simultaneous features of a wide interval. A test that fails to reject equality uses a variance computed at a common probability and need not invert the unpooled interval exactly. Report the interval when the scientific target is the size of the difference.{{cite:dodge2008}} (pp. 106–107, confidence-interval construction and interpretation)
