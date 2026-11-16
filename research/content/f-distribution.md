## Lead context
The F distribution is the law of a ratio of two independent scaled chi-squared variables.

## Intuition — A comparison of two scatter estimates
A variance estimate from normal data is a chi-squared variable divided by its degrees of freedom. Comparing two such estimates, from independent samples, cancels the unknown population variance and leaves a ratio. Large values mean the numerator scatter is large relative to the denominator scatter. The ratio is not centred at one: its mean, when the mean exists, sits above one because the reciprocal of a chi-squared denominator is pulled upward by its right tail.{{cite:nist_f_distribution}} (§1.3.6.6.5, mean)

## Definition — Numerator and denominator degrees of freedom
If $U\sim\chi^2_{d_1}$ and $V\sim\chi^2_{d_2}$ are independent, then
$$
X=\frac{U/d_1}{V/d_2}
$$
has the F distribution $F_{d_1,d_2}$ on $(0,\infty)$. The density on that half-line is
$$
f(x)=\frac{(d_1/d_2)^{d_1/2}x^{d_1/2-1}}{B(d_1/2,d_2/2)\,(1+d_1 x/d_2)^{(d_1+d_2)/2}}.
$$
The mean is $d_2/(d_2-2)$ when $d_2>2$, and the mode is $d_2(d_1-2)/(d_1(d_2+2))$ when $d_1>2$.{{cite:nist_f_distribution}} (§1.3.6.6.5, density, mean and mode)

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
The mean is $6/(6-2)=1.5$. The variance is $2(6)^2(4+6-2)/(4(6-2)^2(6-4))=4.5$. Both exist because $d_2=6$ is greater than $4$.{{cite:nist_f_distribution}} (§1.3.6.6.5, mean and standard deviation)
:::

**Check yourself.** For $F_{3,4}$, does a finite mean exist, and does a finite variance exist?

::: {.callout-tip collapse="true" title="Answer"}
The mean is $4/(4-2)=2$, because $d_2>2$. The variance formula requires $d_2>4$, and $d_2=4$ is not greater than $4$, so the variance is not finite.{{cite:nist_f_distribution}} (§1.3.6.6.5, mean and standard deviation)
:::

**Check yourself.** The square of a $t_5$ variable is an $F_{1,5}$ variable. What is the mean of that F law?

::: {.callout-tip collapse="true" title="Answer"}
The mean is $5/(5-2)=5/3\approx 1.667$. The numerator has one degree of freedom, so this law has no mode of the interior form that needs $d_1>2$.{{cite:nist_f_distribution}} (§1.3.6.6.5, mean and mode)
:::

## Connections
An analysis-of-variance comparison of normal means uses an F ratio of a between-group mean square to a within-group mean square. A comparison of two independent normal variances uses the same reference law with the sample sizes minus one as the two degrees of freedom. The square of a [Student's t](student-t-distribution.qmd) variable on $m$ degrees of freedom is $F_{1,m}$, because the squared normal numerator is chi-squared on one degree of freedom.{{cite:nist_f_distribution}} (§1.3.6.6.5, comments on tests)
