## Lead context
A reported half-width depends on the confidence level, the sampling variability, and the method used to construct the interval.

## Motivating example
A study planner wants an estimated mean to lie within one unit of the population mean with a stated confidence level. A pilot study supplies a rough standard deviation, and the margin of error translates that variability into an approximate sample-size requirement. Increasing the confidence level or reducing the target width generally requires more observations. The familiar normal interval has the form estimate plus or minus a critical value times a standard error.{{cite:openintro2019}} (§5.2)

## Definition — The half-width of a symmetric interval
For an interval $\hat\theta\pm c\,\widehat{SE}(\hat\theta)$, its margin of error is $M=c\,\widehat{SE}(\hat\theta)$. The full width is $2M$. The critical value $c$ comes from the reference distribution and the chosen confidence level; a standard error alone is not a confidence interval. An asymmetric interval has separate distances to its endpoints, so a single symmetric margin can conceal its shape.{{cite:openintro2019}} (§5.2, margin-of-error box)

For iid observations with finite variance, the sample mean has standard error $\sigma/\sqrt n$. A central-limit approximation gives $c=z_{1-\alpha/2}$, often with $s$ substituting for $\sigma$. Its accuracy depends on the sampling model and on how well the normal approximation applies. Under a normal sampling model with unknown variance, the usual exact mean interval instead uses a Student critical value with $n-1$ degrees of freedom.{{cite:grinstead_snell1997}} (§9.3);{{cite:openintro2019}} (§7.1)

## Statistical use — Planning the width
Holding the variability estimate and critical value fixed gives
$$
M=\frac{cs}{\sqrt n},\qquad
n\geq\left(\frac{cs}{M_0}\right)^2
$$
for target margin $M_0>0$. Round the calculated sample size upward. Halving the target margin multiplies the required size by four under these assumptions. If the critical value depends on $n$, as in a Student interval, this calculation is an initial planning approximation and the final width can be checked at the proposed size.{{cite:openintro2019}} (§§5.2, 7.1)

The scaling follows from the variance of an iid average. For clustered or otherwise dependent observations, the variance includes covariance terms and need not equal $\sigma^2/n$. A small nominal margin also cannot correct systematic measurement error, undercoverage, or a nonrepresentative sampling frame. These are separate features of how the data are obtained.{{cite:grinstead_snell1997}} (§§6.2, 9.3);{{cite:openintro2019}} (§§1.3, 5.2)

## Worked example
Suppose a sample mean is $100$, a planning standard deviation is $12$, and $n=64$. With $z_{0.975}\approx1.959964$, the normal-approximation margin is
$$
M=1.959964\frac{12}{8}\approx2.939946.
$$
The reported interval is approximately $(97.0601,102.9399)$. Its half-width is about $2.94$, while its full width is about $5.88$. The confidence statement describes coverage of the interval-producing procedure across repeated samples.{{cite:openintro2019}} (§5.2)

For a target margin of one using the same planning standard deviation and normal critical value, $(1.959964\cdot12)^2\approx553.17$, so the required integer size is $554$. A target margin of two requires $139$ observations under the same calculation. This planning exercise treats the estimated standard deviation as a value to carry forward; the realised sample standard deviation can differ.{{cite:openintro2019}} (§§5.2, 7.1)

**Your turn.** Keeping the same confidence level and variability, how large must the sample be to halve the margin of a study using $64$ observations?

::: {.callout-tip collapse="true" title="Answer"}
The margin scales as $1/\sqrt n$, so halving it requires four times as many observations: $4\cdot64=256$.
:::

## Interpretation — Units and confidence levels
A proportion interval has margin measured on the probability scale. A margin of $0.04$ corresponds to four percentage points; it is not four percent of the point estimate. Increasing the central confidence level increases the critical value and widens the interval at fixed standard error. A confidence percentage specifies a coverage target, while the margin specifies a distance in the parameter's units.{{cite:openintro2019}} (§5.2)

