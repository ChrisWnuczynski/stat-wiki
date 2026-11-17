## Motivating example
Two production methods may have comparable mean output but very different consistency. The sample variance ratio estimates a relative spread, yet small samples can leave the population ratio very uncertain. An interval communicates that uncertainty more fully than a yes-or-no equal-variance test. The normal model supplies an exact $F$ pivot for this purpose.{{cite:dodge2008}} (pp. 199–200, “Fisher Distribution”)

## Definition
Let $r=S_1^2/S_2^2$ and $\rho=\sigma_1^2/\sigma_2^2$, with independent normal samples and positive variances. Then $r/\rho$ has an $F_{n_1-1,n_2-1}$ law because it is a ratio of independent chi-squared variables divided by their degrees of freedom. The numerator's degrees of freedom belong to the first population; reversing the ratio also swaps these degrees of freedom.{{cite:siegrist2022_normals}} (§6.8, “Ratios of Sample Variances”)

## Properties — Reciprocals and coverage
If $W\sim F_{a,b}$, its reciprocal is $F_{b,a}$. Thus $q_{a,b}(\alpha)=1/q_{b,a}(1-\alpha)$. Placing $r/\rho$ between quantiles of orders $\alpha/2$ and $1-\alpha/2$ and solving for the positive ratio gives the interval displayed below. This is an algebraic equivalence of events and therefore preserves probability. The unknown scale cancels, while the shape depends on both sample sizes.{{cite:dodge2008}} (p. 200, ratio of chi-squared variables)

The null ratio $1$ belongs to this interval exactly when the corresponding equal-tail $F$ test does not reject equality. This duality does not establish that pooling variances is appropriate: a wide interval containing one may also contain large departures from one.{{cite:siegrist2022_normals}} (§6.8, “Ratios of Sample Variances”)

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

## Assumptions and limits
The $F$ interval is sensitive to departures from normality because sample variances depend strongly on tail observations. Independence between samples and within each sample matters as well. A normal model with positive variance produces zero sample variance with probability zero; a recorded zero can instead indicate rounding, censoring, or a discrete measurement process requiring a different model. The repeated-sampling confidence interpretation concerns the whole interval rule.{{cite:dodge2008}} (pp. 106–107, confidence-interval construction and interpretation)
