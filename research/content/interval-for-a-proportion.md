## Motivating example
In a sample of twenty independent items, finding no failures does not establish that the population failure probability is zero. Yet the Wald interval collapses to $[0,0]$ in precisely that situation. This exposes the difference between an estimate and a calibrated interval. Binomial discreteness and boundary values require special care.{{cite:openintro2019}} (§6.1.4, when conditions are not met)

## Definition
The binomial model assumes a fixed number $n$ of independent trials with a common success probability $p$. The estimate $\widehat p=X/n$ has variance $p(1-p)/n$. The Wald formula replaces this unknown variance by its plug-in estimate. Its normal approximation needs enough successes and failures; a rule based on their counts is a diagnostic, not an exact coverage theorem. OpenIntro uses at least ten expected successes and failures as its normal-approximation guideline.{{cite:openintro2019}} (§6.1.1–6.1.2, normal approximation and intervals)

## Properties — Keeping the parameter inside the standard error
Instead of substituting $\widehat p$ immediately, solve the score inequality
$$\frac{n(\widehat p-p)^2}{p(1-p)}\le z^2.$$
Multiplication and collection of powers give
$$(n+z^2)p^2-(2n\widehat p+z^2)p+n\widehat p^2\le0.$$
The roots define the Wilson interval,
$$\frac{\widehat p+z^2/(2n)\ \pm\ z\sqrt{\widehat p(1-\widehat p)/n+z^2/(4n^2)}}{1+z^2/n}.$$
It remains inside $[0,1]$ and avoids the zero-width boundary failure, while still using an approximate score-test calibration.{{cite:nist_handbook2002}} (§7.2.4.1, Wilson formulas)

## Worked example — No failures in twenty trials
For $X=0$, $n=20$, and $z=1.96$, the Wilson interval simplifies to $[0,z^2/(n+z^2)]\approx[0,0.1611]$. A two-sided equal-tail exact binomial interval instead has upper endpoint $1-(0.025)^{1/20}=0.1684$, because $P_p(X=0)=(1-p)^{20}$. The exact interval is conservative in the sense of guaranteeing at least the advertised coverage under the binomial model, with coverage varying across $p$.{{cite:nist_handbook2002}} (§7.2.4.1, exact intervals for small numbers of failures)

**Your turn.** For zero successes in ten trials, calculate the Wilson upper endpoint with $z=1.96$ and compare it with the Wald upper endpoint.

::: {.callout-tip collapse="true" title="Answer"}
The Wilson upper endpoint is $3.8416/(10+3.8416)=0.2775$. The Wald endpoint is zero because its estimated standard error vanishes. The difference reflects the Wald method's failure at the boundary.
:::

## Interpretation — A difference of proportions
The nightmare example uses independent groups and adds their variance estimates. With the exact sample fractions, the estimated difference is $55/160-60/192=0.03125$ and its standard error is $0.050288$. The approximate 95% interval is $(-0.0673,0.1298)$. An interval that includes zero also allows substantively meaningful differences in either direction. Independence between groups and a sampling design supporting population inference remain necessary.{{cite:openintro2019}} (§6.2.2, confidence intervals for two proportions)

## Assumptions and limits
Clipping a Wald interval to $[0,1]$ removes impossible endpoints but cannot repair its coverage. Survey nonresponse, unequal sampling probabilities, and cluster sampling require additional design information. The success probability refers to a defined population and measurement process; mathematical precision in the binomial calculation does not remove systematic sampling error.{{cite:openintro2019}} (§6.1, independence and success-failure conditions)
