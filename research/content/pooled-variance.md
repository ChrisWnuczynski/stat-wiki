## Lead context
A pooled variance is the single scale estimate used when several groups are treated as sharing one population variance, with each group contributing in proportion to how many degrees of freedom it has.

## Motivating example
Two brands of computer are watched until the first fault. Eight machines of the first brand average 2800 hours, and the sum of squared deviations from that mean is 95000. Six machines of the second brand average 2600 hours, with sum of squared deviations 70000. If the two brands really share one variance, neither sample on its own is the best estimate of that common number: the first sample has seven degrees of freedom and the second has five. Pooling adds the sums of squares and divides by twelve, which is 165000/12 = 13750. That one number then scales a comparison of the two mean lifetimes.{{cite:dodge2008}} (pp. 427–428, Pooled Variance){{cite:siegrist2022_normals}} (§6.08, “The Two Sample Model”)

## Intuition
Each sample variance is already an average of squared deviations, using its own mean. If the populations have the same variance, those averages are noisy measurements of one quantity. A larger sample has a less noisy measurement, so it should pull the combined estimate more strongly. The right weight is the degrees of freedom, $n_i-1$, not the raw sample size, because one degree of freedom was spent estimating each sample mean. Adding the numerators and adding the denominators is exactly that weighted average. The result is still in squared units of the measurements, just as each sample variance was.{{cite:dodge2008}} (pp. 427–428, formula){{cite:siegrist2022_normals}} (§6.08, pooled estimate of $\sigma^2$)

## Definition
For $k$ independent samples, with sample $i$ of size $n_i$ and sample variance $s_i^2$, Dodge writes
$$
s_p^2=\frac{\sum_{i=1}^k(n_i-1)s_i^2}{\bigl(\sum_{i=1}^k n_i\bigr)-k},
$$
which is the same number as the total within-sample sum of squares divided by the total within-sample degrees of freedom. For two samples this is
$$
s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}.
$$
The estimator is for a variance that has been assumed equal across the populations. It is not defined by stacking the observations and computing one variance about the grand mean.{{cite:dodge2008}} (pp. 427–428, Pooled Variance){{cite:siegrist2022_normals}} (§6.08, “The $T$ Variable”)

## Interpretation — What the weights are doing
The numerator $(n_i-1)s_i^2$ is the residual sum of squares in group $i$. Dividing the sum of those residuals by the sum of the degrees of freedom produces a mean square. When the groups are the same size, the weights $n_i-1$ are equal, so $s_p^2$ is the ordinary average of the sample variances. When the sizes differ, the larger group dominates. In the computer example the weights are 7 and 5, so the first brand supplies $7/12$ of the estimate and the second supplies $5/12$. Replacing those weights by the sample sizes 8 and 6, and using $s_1^2=95000/7$, would give $(8\times95000/7+6\times14000)/14=13755.102$, a different number, because that average pretends the means were known.{{cite:dodge2008}} (p. 428, numerical example){{cite:siegrist2022_normals}} (§6.08, degrees of freedom as weights)

## Properties — Chi-squared sum and the two-sample pivot
Under independent normal samples with one common variance $\sigma^2$, $(n_i-1)s_i^2/\sigma^2$ has a chi-squared distribution on $n_i-1$ degrees of freedom, and these pieces are independent of each other and of the sample means. Their sum is chi-squared on $\sum(n_i-1)$ degrees of freedom, so
$$
\frac{\bigl(\sum_i(n_i-1)\bigr)s_p^2}{\sigma^2}\sim\chi^2_{\sum(n_i-1)}.
$$
A chi-squared variable has mean equal to its degrees of freedom, so $s_p^2$ is unbiased for $\sigma^2$. For two normal samples the difference of means, scaled by $\sigma\sqrt{1/n_1+1/n_2}$, is standard normal and independent of $s_p^2$. Dividing that normal variable by $\sqrt{s_p^2/\sigma^2}$ produces Student's $t$ on $n_1+n_2-2$ degrees of freedom.{{cite:siegrist2022_normals}} (§6.08, chi-square sum and the $T$ variable)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $V_i=(n_i-1)s_i^2/\sigma^2$. For an independent normal sample, $V_i\sim\chi^2_{n_i-1}$ and $V_i$ is independent of that sample's mean. Independence of the samples makes the $V_i$ independent of one another, so $\sum V_i\sim\chi^2_{\nu}$ with $\nu=\sum(n_i-1)$. The pooled variance is $s_p^2=\sigma^2(\sum V_i)/\nu$, hence $\nu s_p^2/\sigma^2\sim\chi^2_\nu$. Taking expectations, $\E(\sum V_i)=\nu$, so $\E(s_p^2)=\sigma^2$.

For two samples let $Z=\bigl((\overline Y-\overline X)-(\nu-\mu)\bigr)/\bigl(\sigma\sqrt{1/m+1/n}\bigr)$. Independence and normality give $Z\sim N(0,1)$, independent of both sample variances and therefore of $V=(m+n-2)s_p^2/\sigma^2$. The ratio $Z/\sqrt{V/(m+n-2)}$ has the $t_{m+n-2}$ law. If the two population variances differ, $V$ is no longer a single chi-squared multiple of one $\sigma^2$, and this ratio is not $t_{m+n-2}$.{{cite:siegrist2022_normals}} (§6.08, “The $T$ Variable” and its proofs)
:::
:::

## Statistical use — Intervals, tests, and the equal-variance check
The two-sample interval for a difference of normal means, when a common variance is assumed, is
$$
\overline X_1-\overline X_2\pm t_{n_1+n_2-2,\,1-\alpha/2}\,s_p\sqrt{\frac1{n_1}+\frac1{n_2}}.
$$
The same $s_p$ sits in the denominator of the two-sample $t$ statistic. Before pooling, the ratio of the two sample variances can be compared with an $F$ reference law: if the populations are independent and normal with equal variances, $s_1^2/s_2^2\sim F_{n_1-1,n_2-1}$. A confidence interval for $\sigma_1^2/\sigma_2^2$ that stays well away from 1 is a warning that the pooled standard error is the wrong scale. Equal sample sizes do not repair unequal population variances; they only make the weights equal.{{cite:siegrist2022_normals}} (§6.08, $T$ variable and variance ratio){{cite:nist_mean_limits2002}} (§1.3.5.2, “Definition: Confidence Interval”)

## Worked example
Take the computer lifetimes as Dodge records them. The first sample has $n_1=8$, mean 2800 and sum of squared deviations 95000, so
$$
s_1^2=\frac{95000}{7}=13571.429.
$$
The second has $n_2=6$, mean 2600 and sum of squared deviations 70000, so $s_2^2=70000/5=14000$. The pooled variance uses the sums of squares directly:
$$
s_p^2=\frac{95000+70000}{8+6-2}=\frac{165000}{12}=13750.
$$
The estimated standard error of the difference of means is
$$
\sqrt{13750\bigl(\tfrac18+\tfrac16\bigr)}=\sqrt{13750\cdot\tfrac{7}{24}}=\sqrt{4010.417}=63.328.
$$
A 95% interval would still need a $t_{12,0.975}$ multiplier; the pooled variance itself is 13750 square hours, and the separate sample variances 13571.429 and 14000 are close to it because the samples are not very different in size or spread.{{cite:dodge2008}} (p. 428, computer-brand example){{cite:siegrist2022_normals}} (§6.08, pooled estimate)

**Your turn.** Two independent samples have $n_1=10$, $s_1^2=16$ and $n_2=6$, $s_2^2=25$. Compute the pooled variance, and say what changes if the second population variance is not equal to the first.

::: {.callout-tip collapse="true" title="Answer"}
The degrees of freedom are 9 and 5, and $9\times16+5\times25=144+125=269$. Dividing by $10+6-2=14$ gives $s_p^2=269/14=19.214$. The arithmetic is valid as a weighted average either way. The chi-squared law, the unbiasedness claim for one common $\sigma^2$, and the $t_{14}$ reference for a difference of means all require the two populations to share a variance.{{cite:siegrist2022_normals}} (§6.08, pooled estimate and the equal-scale condition)
:::

## Common misconceptions
The pooled variance is not the variance of the stacked data. Four zeros and four tens have sample variances 0 and 0, so the pooled variance is 0, but the eight numbers about their grand mean 5 have sum of squared deviations 200 and sample variance $200/7=28.571$. Pooling describes scatter inside groups. The stacked variance also describes the gap between group means.

Equal weights are another slip. Averaging $s_1^2$ and $s_2^2$ is right only when $n_1=n_2$. Weighting by $n_i$ instead of $n_i-1$ agrees with the degrees-of-freedom formula only in the limit of large samples. And a small $p$-value on a difference of means, computed with $s_p$, is not evidence that the variances were equal: the test used that equality as an assumption.{{cite:dodge2008}} (pp. 427–428, equal-variance premise){{cite:siegrist2022_normals}} (§6.08, common standard deviation)

## Assumptions and limits — When the groups do not share a variance
Suppose one sample has $n_1=100$ and $s_1^2=1$, and the other has $n_2=10$ and $s_2^2=100$. The pooled value is
$$
s_p^2=\frac{99\times1+9\times100}{108}=\frac{999}{108}=9.250.
$$
Neither population has variance 9.250. Using $\sqrt{9.250/100}=0.304$ as the standard error of the first mean overstates a standard error that would have been $\sqrt{1/100}=0.100$ had the first variance been trusted on its own. Using $\sqrt{9.250/10}=0.962$ for the second mean understates $\sqrt{100/10}=3.162$. The pooled interval and the pooled $t$ test then have the wrong reference distribution, even though every algebraic step from the formula is correct. A Welch comparison, which keeps the two sample variances apart, is the procedure that matches unequal scales. Normality matters as well: the exact chi-squared sum is a normal-sample theorem, not a consequence of dividing one sum of squares by another.{{cite:siegrist2022_normals}} (§6.08, equal standard deviations required for the $T$ variable)

## Connections
The [two-sample t pivot](two-sample-t-pivot.qmd) is the studentised difference that uses $s_p$. The [F test for equal variances](f-test-for-equal-variances.qmd) is the check on the common-variance assumption, using the ratio of the unpooled sample variances. [Welch's interval](welch-interval.qmd) keeps a separate variance in each group. The [sample variance](sample-variance-and-standard-deviation.qmd) of one group is the ingredient; the [chi-squared distribution](chi-squared-distribution.qmd) is the reference law of the scaled residual sum.{{cite:siegrist2022_normals}} (§6.08, variance ratio and the $T$ variable)

## Check yourself

### Lost hours after a safety programme {#self-check-ex-inf-safety-interval}

Two independent normal samples of size 50 have standard deviations 14.1 and 14.3. Compute the pooled variance and the pooled standard deviation.

[Question-bank page](../questions/ex-inf-safety-interval.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The residual sums of squares are $49\times14.1^2=9741.69$ and $49\times14.3^2=10020.01$. Their total is 19761.70, and dividing by 98 gives $s_p^2=201.65$. The pooled standard deviation is $\sqrt{201.65}=14.200$.{{cite:siegrist2022_normals}} (§6.08, pooled estimate)
:::

### Checking equal variances {#self-check-ex-inf-variance-ratio-interval}

With the same two standard deviations and $F_{49,49;0.975}=1.762$, form the 95% interval for $\sigma_1^2/\sigma_2^2$ based on $s_1^2/s_2^2$ and say whether it contains 1.

[Question-bank page](../questions/ex-inf-variance-ratio-interval.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The point estimate is $14.1^2/14.3^2=198.81/204.49=0.97222$. Dividing and multiplying by 1.762 gives $(0.55177,\ 1.71306)$, which rounds to $(0.5518,\ 1.7131)$. The interval contains 1, so these samples do not by themselves rule out a common variance. The interval is wide: ratios from about 0.55 to 1.71 are still compatible with the $F$ calculation.{{cite:siegrist2022_normals}} (§6.08, ratio of sample variances)
:::

## History
Dodge's encyclopedia defines the pooled variance as the estimate used when several populations have unknown variances that can be treated as equal, and gives both the sums-of-squares form and the degrees-of-freedom weighted form. The computer-brand calculation on the following page is the numerical pattern above: two samples, sums of squares 95000 and 70000, and pooled value 13750. The exact $t$ and chi-squared laws that justify using that number in a mean comparison are normal-sample theorems, set out for the two-sample model by Siegrist.{{cite:dodge2008}} (pp. 427–428, Pooled Variance){{cite:siegrist2022_normals}} (§6.08, “The Two Sample Model”)
