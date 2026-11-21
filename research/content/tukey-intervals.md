## Lead context
Tukey intervals are simultaneous intervals for every pairwise difference of group means, sized so that the whole family misses with at most a preset probability.{{cite:oehlert2010}} (§5.4.3, p. 90, simultaneous confidence intervals)

## Motivating example
Take $k=3$, $r=4$, so $\nu=k(r-1)=9$, and $S^2=6.25$. The $0.95$ studentised-range quantile is $Q\approx 3.948492$. Using the unrounded quantile gives

$$
Q\sqrt{6.25}/\sqrt{4}\approx 4.936.
$$

Group means $10$, $14$ and $18$ give the difference $18-10=8$, with interval approximately $(3.064,\ 12.936)$, and the difference $14-10=4$, with interval approximately $(-0.936,\ 8.936)$. The endpoints use the unrounded half-width before rounding to three decimals. The first interval excludes zero and the second does not. The same half-width is used for every pair.{{cite:nist_tukey2002}} (§7.4.7.1, “Confidence limits for Tukey's method”, interval formula and error degrees of freedom)

## Intuition — One critical value for every pair
Each valid individual 95% interval has 5% marginal noncoverage, but the probability that at least one interval in a family misses can be higher. These misses need not be independent.{{cite:oehlert2010}} (§5.1, p. 79, comparisonwise and familywise error rates) The studentised range looks at the biggest gap among the standardised group means and divides by one error scale. A critical value from that law is wide enough for every pair at once, because every pairwise gap is at most the gap from the largest standardised mean to the smallest.{{cite:oehlert2010}} (§5.4.2, pp. 89–90, Studentized range)

## Definition — Equal groups and a common variance
In a one-way layout, group $j$ has $r$ independent normal observations with mean $\mu_j$ and common variance $\sigma^2$, and the groups are independent. With $k$ groups the error degrees of freedom are $\nu=k(r-1)$ when every group has size $r$. Let $S^2$ be the error mean square. The studentised range is

$$
R=\frac{\max_j Z_j-\min_j Z_j}{S/\sigma},
\qquad
Z_j=\frac{\sqrt{r}\,(\overline Y_{\cdot j}-\mu_j)}{\sigma}.
$$

If $Q$ is the $1-\alpha$ quantile of $R$, every difference $\mu_i-\mu_j$ lies in

$$
\overline Y_{\cdot i}-\overline Y_{\cdot j}\pm Q\,S/\sqrt{r}
$$

with probability $1-\alpha$, simultaneously in the pairs.{{cite:nist_tukey2002}} (§7.4.7.1, Studentized range definition and “Confidence limits for Tukey's method”)

## Properties — The range event is the coverage event
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Take the $Z_j$ to be independent standard normal and independent of the positive scale $S/\sigma$, which is the reference law in the definition. For any pair,

$$
\bigl|(\overline Y_{\cdot i}-\overline Y_{\cdot j})-(\mu_i-\mu_j)\bigr|
=\frac{\sigma}{\sqrt{r}}\,|Z_i-Z_j|
\le\frac{\sigma}{\sqrt{r}}(\max Z-\min Z)
=\frac{S}{\sqrt{r}}\,R.
$$

The half-width $Q S/\sqrt{r}$ therefore covers pair $(i,j)$ whenever $R\le Q$. The largest pairwise absolute gap of the $Z_j$ equals $\max Z-\min Z$, so the inequality runs the other way for that extreme pair: if $R>Q$, that pair is missed. All pairs are covered if and only if $R\le Q$. By the choice of $Q$, that event has probability $1-\alpha$.
:::
:::

The argument needs equal group sizes, a common variance, independence and normality. A pair whose interval excludes zero is separated at familywise level $\alpha$. Unequal sizes replace $\sqrt{r}$ by a pair-specific scale; that extension is not the formula above.{{cite:oehlert2010}} (§5.4.3, pp. 90–91, HSD and Tukey–Kramer formulas)

## Worked example — Three groups of four

**Your turn.** With this same unrounded half-width, approximately $4.936$, give the interval for a mean difference whose estimate is $6$, and say whether the familywise test separates those two groups.

::: {.callout-tip collapse="true" title="Answer"}
Using the unrounded half-width, the interval is approximately $(1.064,\ 10.936)$. It excludes zero, so the test separates the two groups at familywise level $0.05$. The conclusion uses the normal equal-size model; the arithmetic does not check that model.
:::

## Connections — Familywise error, not a discovery rate
These intervals are a [one-way analysis of variance](one-way-analysis-of-variance.qmd) follow-up. They control the [family-wise error rate](family-wise-error-rate.qmd) for the pairwise family. A [Bonferroni correction](bonferroni-correction.qmd) also controls that rate, by widening each interval with a smaller tail probability, and it does not use the range law. [Benjamini–Hochberg](benjamini-hochberg.qmd) controls a different error, the expected share of false discoveries, and is not a substitute for these simultaneous mean intervals.{{cite:oehlert2010}} (§5.1, p. 79, false discovery rate; §5.2, p. 81, Bonferroni intervals; §5.4.3, p. 90, HSD)
