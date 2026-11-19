## Lead context
Tukey intervals are simultaneous intervals for every pairwise difference of group means, sized so that the whole family misses with at most a preset probability.{{cite:nist_scheffe2002}} (§7.4.7.2, comparison with Tukey)

## Motivating example
Take $k=3$, $r=4$, so $\nu=8$, and $S^2=6.25$. The $0.95$ studentised-range quantile is $4.041$ to three decimals, and

$$
4.041\times\sqrt{6.25}/\sqrt{4}=5.051
$$


to three decimals. Group means $10$, $14$ and $18$ give the difference $18-10=8$, with interval $(2.949,\ 13.051)$, and the difference $14-10=4$, with interval $(-1.051,\ 9.051)$. The first excludes zero and the second does not. The same half-width is used for every pair.{{cite:nist_scheffe2002}} (§7.4.7.2, comparison with Tukey)

## Intuition — One critical value for every pair
Separate 95% intervals for ten pairs do not each fail with probability 5% inside one experiment: the chance that the worst pair fails is larger. The studentised range looks at the biggest gap among the standardised group means and divides by one error scale. A critical value from that law is wide enough for every pair at once, because every pairwise gap is at most the gap from the largest standardised mean to the smallest.

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


with probability $1-\alpha$, simultaneously in the pairs.{{cite:nist_scheffe2002}} (§7.4.7.2, comparison with Tukey)

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

The argument needs equal group sizes, a common variance, independence and normality. A pair whose interval excludes zero is separated at familywise level $\alpha$. Unequal sizes replace $\sqrt{r}$ by a pair-specific scale; that extension is not the formula above.

## Worked example — Three groups of four

**Your turn.** With this same half-width $5.051$, give the interval for a mean difference whose estimate is $6$, and say whether the familywise test separates those two groups.

::: {.callout-tip collapse="true" title="Answer"}
The interval is $6\pm 5.051=(0.949,\ 11.051)$. It excludes zero, so the test separates the two groups at familywise level $0.05$. The conclusion uses the normal equal-size model; the arithmetic does not check that model.
:::

## Connections — Familywise error, not a discovery rate
These intervals are a [one-way analysis of variance](one-way-analysis-of-variance.qmd) follow-up. They control the [family-wise error rate](family-wise-error-rate.qmd) for the pairwise family. A [Bonferroni correction](bonferroni-correction.qmd) also controls that rate, by widening each interval with a smaller tail probability, and it does not use the range law. [Benjamini–Hochberg](benjamini-hochberg.qmd) controls a different error, the expected share of false discoveries, and is not a substitute for these simultaneous mean intervals.

## Check yourself
### A zero difference
The estimated difference is $0$ and the half-width is $5.051$. Does the interval exclude zero?

::: {.callout-tip collapse="true" title="Answer"}
The interval is $(-5.051,\ 5.051)$. It contains zero, so the test does not separate the groups.
:::

### Doubling the error mean square
Keep $Q=4.041$, $r=4$ and replace $S^2=6.25$ by $25$. What is the half-width to three decimals?

::: {.callout-tip collapse="true" title="Answer"}
$\sqrt{25}=5$ and $\sqrt{4}=2$, so the half-width is $4.041\times 5/2=10.103$. The quantile did not change; only the error scale did.
:::
