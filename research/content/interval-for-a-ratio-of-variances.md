## Motivating example
Two production methods may have comparable mean output but very different consistency. The sample variance ratio estimates a relative spread, yet small samples can leave the population ratio very uncertain. An interval communicates that uncertainty more fully than a yes-or-no equal-variance test. The normal model supplies an exact $F$ pivot for this purpose.{{cite:dodge2008}} (pp. 199–200, “Fisher Distribution”)

## Definition
Let $r=S_1^2/S_2^2$ and $\rho=\sigma_1^2/\sigma_2^2$, with independent normal samples and positive variances. Then $r/\rho$ has an $F_{n_1-1,n_2-1}$ law because it is a ratio of independent chi-squared variables divided by their degrees of freedom. The numerator's degrees of freedom belong to the first population; reversing the ratio also swaps these degrees of freedom.

## Properties — Reciprocals and coverage
If $W\sim F_{a,b}$, its reciprocal is $F_{b,a}$. Thus $q_{a,b}(\alpha)=1/q_{b,a}(1-\alpha)$. Placing $r/\rho$ between quantiles of orders $\alpha/2$ and $1-\alpha/2$ and solving for the positive ratio gives the interval displayed below. This is an algebraic equivalence of events and therefore preserves probability. The unknown scale cancels, while the shape depends on both sample sizes.{{cite:dodge2008}} (p. 200, ratio of chi-squared variables)

The null ratio $1$ belongs to this interval exactly when the corresponding equal-tail $F$ test does not reject equality. This duality does not establish that pooling variances is appropriate: a wide interval containing one may also contain large departures from one.

## Worked example — Reading the ratio direction
Take $n_1=13$, $n_2=9$, $s_1^2=9$ and $s_2^2=4$. The estimated ratio is $2.25$. Using $(12,8)$ degrees of freedom, the 95% interval is
$$\left(\frac{2.25}{F_{12,8;0.975}},\frac{2.25}{F_{12,8;0.025}}\right)\approx(0.5358,7.9015).$$
It includes equality and ratios indicating materially greater variability in population 1. The interval for the reversed population ratio is obtained by reciprocating the endpoints in reverse order. Using the same critical values without swapping their roles would give an inconsistent comparison.{{cite:dodge2008}} (p. 200, Fisher distribution and reciprocal relationship)

**Your turn.** An interval for $\sigma_1^2/\sigma_2^2$ is $(0.5,8)$. Find the corresponding intervals for $\sigma_2^2/\sigma_1^2$ and $\sigma_1/\sigma_2$.

::: {.callout-tip collapse="true" title="Answer"}
The reversed variance ratio has interval $(1/8,1/0.5)=(0.125,2)$. The standard-deviation ratio has interval $(\sqrt{0.5},\sqrt8)\approx(0.7071,2.8284)$.
:::

### Transforming the target changes its interpretation
The variance ratio is dimensionless when both samples measure the same quantity in the same units. Multiplying every observation in both samples by $a\ne0$ multiplies each variance by $a^2$, leaving the ratio and its interval unchanged. Taking logarithms gives an interval for $\log\rho$; taking square roots gives one for the relative standard deviations. These are exact monotone transformations of the inclusion event, but symmetry on one scale does not imply symmetry on another. For equal denominator and numerator degrees of freedom, the reciprocal quantile relation makes the endpoints multiplicatively symmetric about the observed ratio: their product is $r^2$. That property explains the wide factor-of-four example without suggesting additive error bars around the ratio. The ratio pivot depends on independent variance estimators rather than a pooled estimate.{{cite:dodge2008}} (p. 200, Fisher ratio construction)

Take equal samples of size $9$, so both variance estimators have $8$ degrees of freedom, and let the observed ratio be $4$. The upper $2.5\%$ point of $F_{8,8}$ rounds to $4.43$. The equal-tail $95\%$ interval for $\sigma_1^2/\sigma_2^2$ is formed with the unrounded quantile, and those unrounded endpoints multiply to $16=4^2$. Rounded, the interval is $(0.902,17.73)$. The interval for the standard-deviation ratio is $(\sqrt{0.902},\sqrt{17.73})\approx(0.95,4.21)$. Equality is inside the variance-ratio interval, and so are ratios several times larger than the estimate. The multiplicative symmetry is about the observed ratio $4$, in the sense that the endpoints multiply to $4^2$, rather than an additive symmetry about $4$. With unequal degrees of freedom the product of the critical values need not be one, so the worked interval $(0.5358,7.9015)$ does not obey the same identity.{{cite:dodge2008}} (p. 200, Fisher distribution and reciprocal relationship)

## Statistical use — When the ratio is the scientific target
A production comparison often asks whether one method is more variable, and by how much. The interval $(0.5358,7.9015)$ in the worked sample says that the data, under the normal model, remain compatible with population 1 being about half as variable as population 2 and with it being nearly eight times as variable. A test that merely asks whether the ratio equals $1$ collapses that range to a yes-or-no decision. If a specification requires $\sigma_1/\sigma_2\le1.5$, square the limit and compare $2.25$ with the variance-ratio interval. Here $2.25$ lies inside $(0.5358,7.9015)$, so the equal-tail $95\%$ procedure does not exclude that standard-deviation ratio. The comparison uses the same inclusion event as the variance interval.{{cite:nist_handbook2002}} (§1.3.5.8, interval and test relationship){{cite:dodge2008}} (pp. 106–107, confidence-interval construction and interpretation)

Pooling the two sample variances into one estimate is a different operation. Pooling is reasonable when a confidence interval has already made a large departure from $1$ implausible and the scientific model really does share one variance. A wide interval that happens to contain $1$ leaves large departures plausible, and pooling then treats a weakly supported restriction as if it were known. The ratio interval is the summary that keeps the restriction visible.

## Common misconceptions
The label on the ratio is part of the claim. An interval for $\sigma_1^2/\sigma_2^2$ that is $(0.5,8)$ is an interval $(0.125,2)$ for $\sigma_2^2/\sigma_1^2$ and an interval about $(0.7071,2.8284)$ for $\sigma_1/\sigma_2$. Quoting $(0.5,8)$ as a standard-deviation comparison overstates the upper relative spread, because the square root of $8$ is about $2.83$, not $8$. The degrees of freedom travel with the populations: the numerator degrees of freedom belong to the variance in the numerator. Swapping the names without swapping the critical values builds an interval for a different ordering of the same numbers.{{cite:dodge2008}} (p. 200, ratio of chi-squared variables)

A large observed ratio from small samples can still produce an interval that contains $1$. That is a statement about precision. It is also possible for a ratio near $1$ from very large normal samples to exclude values that a scientist would still call practically interchangeable. The interval reports the sampling uncertainty under the model. The judgment that a particular ratio is operationally important is a separate sentence.{{cite:dodge2008}} (pp. 106–107, confidence-interval construction and interpretation)

## Assumptions and limits
The $F$ interval is sensitive to departures from normality because sample variances depend strongly on tail observations. Independence between samples and within each sample matters as well. A normal model with positive variance produces zero sample variance with probability zero; a recorded zero can instead indicate rounding, censoring, or a discrete measurement process requiring a different model. The repeated-sampling confidence interpretation concerns the whole interval rule.{{cite:dodge2008}} (pp. 106–107, confidence-interval construction and interpretation)
