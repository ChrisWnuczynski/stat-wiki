## Lead context
The F distribution is the law of a ratio of two independent scaled chi-squared variables.

## Motivating example
For an $F_{8,20}$ variable the mean exists and equals $20/(20-2)=10/9$. The mode equals $15/22$. The reciprocal law is $F_{20,8}$, whose mean is $4/3$.

## Intuition — A comparison of two scatter estimates
A sample variance from a normal population, divided by the population variance it estimates, is a chi-squared variable divided by its degrees of freedom: $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$, so $S^2/\sigma^2$ is $\chi^2_{n-1}/(n-1)$. The ratio of two such scaled variances, from independent samples, is an $F$ variable. The unscaled ratio $S_1^2/S_2^2$ has that same $F$ law only when the two population variances are equal; when they differ, $S_1^2/S_2^2$ is $(\sigma_1^2/\sigma_2^2)$ times an $F$ variable, because each sample variance estimates its own population variance. Large values of the ratio mean the numerator scatter is large relative to the denominator scatter. The ratio is not centred at one. Writing $X=(U/d_1)/(V/d_2)$, independence gives $\mathbb E X=\mathbb E(U/d_1)\,\mathbb E(d_2/V)=d_2\,\mathbb E(1/V)$, and since $1/v$ is strictly convex, Jensen's inequality gives $\mathbb E(1/V)>1/\mathbb E V=1/d_2$ whenever the mean exists. Inverting the positive denominator therefore inflates the mean above one — small denominator values receive disproportionate weight — yielding $d_2/(d_2-2)$.{{cite:nist_f_distribution}} (§1.3.6.6.5, mean) {{cite:siegrist2022_normals}} (§6.8, F ratio)

## Definition
**Numerator and denominator degrees of freedom.** If $U\sim\chi^2_{d_1}$ and $V\sim\chi^2_{d_2}$ are independent, then
$$
X=\frac{U/d_1}{V/d_2}
$$
has the F distribution $F_{d_1,d_2}$ on $(0,\infty)$. The density on that half-line is
$$
f(x)=\frac{(d_1/d_2)^{d_1/2}x^{d_1/2-1}}{B(d_1/2,d_2/2)\,(1+d_1 x/d_2)^{(d_1+d_2)/2}}.
$$
The mean is $d_2/(d_2-2)$, finite exactly when the denominator degrees of freedom satisfy $d_2>2$. The density has a positive interior mode at $d_2(d_1-2)/(d_1(d_2+2))$ when the numerator degrees of freedom satisfy $d_1>2$; for $d_1\le2$ the density is decreasing on $(0,\infty)$ — and unbounded at $0$ when $d_1<2$ — so that interior formula does not apply.{{cite:nist_f_distribution}} (§1.3.6.6.5, density, mean and mode)

## Properties
If $X\sim F_{d_1,d_2}$, then $1/X\sim F_{d_2,d_1}$. A lower quantile of one F law is therefore the reciprocal of an upper quantile of the swapped law. The mean of the reciprocal exists only when the new denominator degrees of freedom exceed two, that is when $d_1>2$.{{cite:nist_f_distribution}} (§1.3.6.6.5, mean)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $X=(U/d_1)/(V/d_2)$ with the independent chi-squared variables in the definition. Then
$$
\frac1X=\frac{V/d_2}{U/d_1},
$$
which is the F ratio with the degrees of freedom exchanged. The mean formula applied to this swapped ratio equals $d_1/(d_1-2)$ when $d_1>2$.{{cite:nist_f_distribution}} (§1.3.6.6.5, definition and mean)
:::
:::

## Worked example
For $X\sim F_{8,20}$ the denominator degrees of freedom exceed two, so the mean exists and equals $20/(20-2)=10/9\approx 1.111$. The numerator degrees of freedom exceed two, so the mode exists and equals $20(8-2)/(8(20+2))=15/22\approx 0.682$. The reciprocal $1/X$ is $F_{20,8}$ and has mean $8/(8-2)=4/3\approx 1.333$. The original mean and the reciprocal mean are not reciprocals of each other: $1/1.111\approx 0.900$, which is well below $1.333$.{{cite:nist_f_distribution}} (§1.3.6.6.5, mean and mode)

**Your turn.** For $F_{4,6}$, find the mean and the variance. The variance formula is $2d_2^2(d_1+d_2-2)/(d_1(d_2-2)^2(d_2-4))$ when $d_2>4$.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $6/(6-2)=1.5$. The variance is $2(6)^2(4+6-2)/(4(6-2)^2(6-4))=4.5$. Both exist because $d_2=6$ is greater than $4$.
:::

For $F_{3,4}$, does a finite mean exist, and does a finite variance exist?

::: {.callout-tip collapse="true" title="Answer"}
The mean is $4/(4-2)=2$, because $d_2>2$. The variance formula requires $d_2>4$, and $d_2=4$ is not greater than $4$, so the variance is not finite.
:::

The square of a $t_5$ variable is an $F_{1,5}$ variable. What is the mean of that F law?

::: {.callout-tip collapse="true" title="Answer"}
The mean is $5/(5-2)=5/3\approx 1.667$. The numerator has one degree of freedom, so this law has no mode of the interior form that needs $d_1>2$.
:::

## Common misconceptions
The mean of $1/X$ is not the reciprocal of the mean of $X$. For $X\sim F_{8,20}$ the mean is $10/9\approx1.111$, while $1/X\sim F_{20,8}$ has mean $4/3\approx1.333$, not $1/1.111\approx0.900$: inversion swaps the degrees of freedom and changes the law, rather than merely reciprocating its summaries. Nor does a mean above one make a value near one surprising under equal variances. The law is right-skewed, and for $F_{8,20}$ its mode, $15/22\approx0.682$, sits below one; the mean is pulled above one by the inversion of the denominator, as the Intuition section explains.{{cite:nist_f_distribution}} (§1.3.6.6.5, mean and mode)

## Assumptions and limits
The $F$ law for a ratio of sample variances rests on independent samples from normal populations: the chi-squared laws of the two scaled variances are exact only under normality. The moment summaries have their own limits, set by the denominator degrees of freedom alone: the mean is finite only when $d_2>2$, and the variance only when $d_2>4$, however large $d_1$ is.{{cite:nist_f_distribution}} (§1.3.6.6.5, density, mean and mode) {{cite:siegrist2022_normals}} (§6.8, exact normality assumption)

## Connections
An analysis-of-variance comparison of normal means uses an F ratio of a between-group mean square to a within-group mean square. A comparison of two independent normal variances uses the same reference law with the sample sizes minus one as the two degrees of freedom. The square of a [Student's t](student-t-distribution.qmd) variable on $m$ degrees of freedom is $F_{1,m}$, because the squared normal numerator is chi-squared on one degree of freedom.{{cite:nist_f_distribution}} (§1.3.6.6.5, comments on tests)

::: {.callout-tip collapse="true" title="Answer"}
The mean is $5/(5-2)=5/3\approx 1.667$. The numerator has one degree of freedom, so this law has no mode of the interior form that needs $d_1>2$.
:::
