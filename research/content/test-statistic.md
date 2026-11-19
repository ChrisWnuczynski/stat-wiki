## Lead context

A hypothesis test ends in a comparison. Some function of the sample is set beside a reference distribution that was fixed with the hypothesis. That function is the test statistic. The reference distribution says which of its values are surprising if the hypothesis is true. The statistic itself is only the number the sample produced. {{cite:dodge2008}} (pp. 250–251) {{cite:openintro2019}} (Ch. 5, §5.3)

## Motivating example

A simple random sample of 1,028 US adults in March 2013 found that 56 percent supported nuclear arms reduction. The question is whether that is convincing evidence, at the 5 percent level, that a majority of Americans supported the policy. The null hypothesis takes the population proportion to be $p_0=0.5$. The sample proportion is $0.56$. The gap $0.06$ is not yet a test. It becomes one when it is divided by the standard error computed from the null value, the sample size, and the normal approximation. The resulting $Z$ is the test statistic. {{cite:openintro2019}} (Ch. 5, §5.3)

## Intuition

Dodge’s account of a test has a fixed order. State the null and the alternative. Choose a significance level. Name the distribution of the statistic under the null. Compute the critical value and the rejection region. Then see whether the statistic computed from the sample lands in that region. The statistic is the piece that the sample is allowed to change. The rejection region is chosen before the data, from the null distribution. A large value is evidence against the null only because the region was drawn in the tail of that distribution. A small value, for a statistic that rejects only when it is large, is what the null tends to produce. {{cite:dodge2008}} (pp. 250–251)

The same idea appears in a rank test and in a proportion test. The Kruskal–Wallis statistic $H$ is large when the rank sums are uneven, and the test rejects for large $H$ only. The normal $Z$ for a proportion is large when the sample proportion is far from the null value on the standard-error scale. In both cases the statistic is a reduction of the sample to one number, and the test is a rule for that number. {{cite:nist_kruskal2002}} (§7.4.1) {{cite:openintro2019}} (Ch. 5, §5.3)

## Definition

A test statistic is a function of the sample used to decide a hypothesis. For a single proportion, with null value $p_0$, sample proportion $\hat p$, and sample size $n$, the normal approximation uses

$$
Z=\frac{\hat p-p_0}{\mathrm{SE}},\qquad \mathrm{SE}=\sqrt{\frac{p_0(1-p_0)}{n}}.
$$


The standard error is computed from $p_0$, not from $\hat p$, because the reference distribution is the distribution of $Z$ when the null is true. Under that null, and when $np_0$ and $n(1-p_0)$ are both at least 10, $Z$ is referred to a standard normal curve. The $p$-value is a tail area of that curve beyond the observed $Z$. The test statistic and the $p$-value are different objects. One is the observed number. The other is a probability computed from it under the null. {{cite:openintro2019}} (Ch. 5, §5.3)

Neyman and Pearson’s formulation makes the statistic the quantity whose null distribution determines the critical value. The decision rule rejects the null when the observed statistic falls in the rejection region, and does not reject it when the statistic falls in the acceptance region. The level $\alpha$ is the null probability of the rejection region. It is set with the region, not read off after the sample has chosen a convenient threshold. {{cite:dodge2008}} (pp. 250–251)

## Statistical use

OpenIntro’s four steps for a one-proportion test put the statistic in the calculation step, after the hypotheses and the conditions. Prepare: name the parameter, the hypotheses, the level, $\hat p$, and $n$. Check: the observations are independent, and the success-failure counts $np_0$ and $n(1-p_0)$ are large enough for the normal approximation. Calculate: the standard error from $p_0$, then $Z$, then the tail probability. Conclude by comparing that probability with $\alpha$. If the $p$-value is below $\alpha$, reject the null. If it is not, the sample has not met the pre-set standard. In either case the conclusion is about the population claim, in the language of the study, and it reports the statistic that was compared. {{cite:openintro2019}} (Ch. 5, §5.3)

A different testing problem uses a different statistic and the same logic. A chi-squared comparison of several groups, or a rank comparison, reduces the sample to one number and refers that number to a distribution fixed by the null. Reporting “significant” without the statistic, the degrees of freedom or the table, and the level, leaves out the comparison the test consisted of. {{cite:dodge2008}} (p. 251) {{cite:nist_kruskal2002}} (§7.4.1)

## Worked example

For the arms-reduction poll, $n=1028$, $\hat p=0.56$, and $p_0=0.5$. The null success-failure counts are $1028\times 0.5=514$, well above 10. The standard error is

$$
\mathrm{SE}=\sqrt{\frac{0.5\times 0.5}{1028}}=\sqrt{\frac{0.25}{1028}}\approx 0.0156.
$$


The test statistic is

$$
Z=\frac{0.56-0.50}{0.0156}\approx 3.85.
$$


The upper tail beyond $3.85$ on a standard normal curve is about $0.0001$. Doubling it for a two-sided test gives a $p$-value of about $0.0002$, which is below $0.05$, so the test rejects $p=0.5$. The poll is evidence that a majority supported arms reduction in that sample’s population. The number $3.85$ is the test statistic. The number $0.0002$ is the tail probability. {{cite:openintro2019}} (Ch. 5, §5.3)

**Your turn.** A sample of size $100$ has $\hat p=0.60$, and the null value is again $0.5$. Compute the standard error from the null and the test statistic $Z$.

::: {.callout-tip collapse="true" title="Answer"}
The standard error is $\sqrt{0.25/100}=0.05$. Then $Z=(0.60-0.50)/0.05=2$.
:::

## Common misconceptions

The test statistic is not the $p$-value, and it is not the estimate. In the poll, $0.56$ is the estimate, $3.85$ is the statistic, and $0.0002$ is the $p$-value. Quoting only the estimate leaves out the standardisation. Quoting only the $p$-value leaves out the direction and the size of the departure. {{cite:openintro2019}} (Ch. 5, §5.3)

The standard error in the denominator is not the standard error of a confidence interval for $p$. A confidence interval usually plugs in $\hat p$. The test plugs in $p_0$, because the curve being used is the null curve. Using $\hat p$ in the test’s standard error refers $Z$ to a different distribution from the one the critical value was taken from. {{cite:openintro2019}} (Ch. 5, §5.3)

A statistic that was chosen after looking at several candidates is not the statistic whose null distribution was tabulated for one pre-specified comparison. The rejection region belongs to the procedure that was declared. Searching and then treating the winner as if it had been declared moves the test into a different procedure, with a different null probability of rejection. {{cite:dodge2008}} (pp. 250–251)

## Connections

A [p-value](p-value.qmd) is the null tail probability of the test statistic, or of values at least as extreme. A [significance level](significance-level.qmd) is the null probability of the rejection region, fixed before the statistic is compared with it. A [confidence interval](confidence-interval.qmd) standardises the same estimate with a standard error that does not lock the parameter at the null value. The [Kruskal–Wallis test](kruskal-wallis-test.qmd) is the rank version of the same pattern: one statistic, a one-sided rejection region, a reference distribution determined by the null. [Neyman and Pearson’s](null-and-alternative-hypotheses.qmd) separation of the null from the alternative is what gives the rejection region a type I error to control. The test statistic is the sample’s input to that region. {{cite:dodge2008}} (pp. 250–251) {{cite:openintro2019}} (Ch. 5, §5.3) {{cite:nist_kruskal2002}} (§7.4.1)
