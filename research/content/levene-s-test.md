## Lead context
It tests equality of variances by replacing each observation with its absolute deviation from a centre of its own group, and then comparing those deviations with a one-way analysis of variance. The centre may be the group mean, the group median, or a trimmed mean. The three choices do not test the same finite-sample statistic, and on a skewed group they need not reach the same decision.

## Motivating example
Three groups of three observations are
$$
(3, 5, 7), \qquad (2, 4, 6), \qquad (0, 2, 13).
$$
The first two groups are symmetric and have the same spacing. The third has the same two small values a short step apart and one value, $13$, far to the right. An ordinary one-way analysis of the raw numbers would ask whether the means differ, and it would do so under a common variance. The question here is that common variance. Levene’s test answers it by running the one-way analysis on the absolute deviations from a group centre. Using the mean, the resulting $F$ is $16/3 \approx 5.333$, just above the upper $5\%$ point $5.143$ of $F$ on $(2, 6)$ degrees of freedom. Using the median, the $F$ is $27/37 \approx 0.730$, and the test does not reject. The same three groups, with $13$ replaced by $4$, give $F = 0$ for the mean-centred statistic. One observation, and the choice of centre, both decide the $5\%$ conclusion.

## Definition — One-way analysis of variance on absolute deviations
Let $Y_{ij}$ be observation $j$ in group $i$, with $j = 1, \ldots, n_i$, $i = 1, \ldots, k$, and $N = \sum_i n_i$. Choose a centre $c_i$ for each group and set $Z_{ij} = |Y_{ij} - c_i|$. Write $\bar Z_{i\cdot}$ for the mean of the $Z_{ij}$ in group $i$ and $\bar Z_{\cdot\cdot}$ for the mean of all $N$ of them. The Levene statistic is the one-way $F$ statistic of the $Z_{ij}$:
$$
W = \frac{(N-k)}{(k-1)} \frac{\sum_{i=1}^{k} n_i (\bar Z_{i\cdot} - \bar Z_{\cdot\cdot})^2}{\sum_{i=1}^{k} \sum_{j=1}^{n_i} (Z_{ij} - \bar Z_{i\cdot})^2}.
$$
The numerator measures how far the groups’ typical absolute deviations are from one another. The denominator measures the scatter of those absolute deviations inside the groups. Large $W$ is evidence against equal variances. Under the equal-variance null, and with the usual normal-theory reference for this $F$ ratio, $W$ is compared with the upper point of the $F$ distribution on $(k-1,\, N-k)$ degrees of freedom. That critical value is the upper point $F_{\alpha}$. The mean-centred form is this $F$ statistic applied to $d_{ij} = |Y_{ij} - \bar Y_{i\cdot}|$. It is not exactly an $F_{k-1,\, N-k}$ random variable, because the absolute deviations are not normal and are not independent within a group.{{cite:gastwirth_gel_miao2009}} (§1, equation (3)); {{cite:nist_levene2002}} (§1.3.5.10); {{cite:dodge2008}} (p. 399)

Three centres are in use. The original statistic takes $c_i$ to be the group mean. Replacing that mean by a more robust centre, for example the group median, puts $Z_{ij} = |Y_{ij} - \hat\mu_i|$ in place of $d_{ij}$ in the same $F$ statistic. The $10\%$ trimmed mean is the third centre. The three definitions change both the robustness of the test and its power. Robustness here means that equal variances are not declared unequal merely because the data are non-normal. Power means that unequal variances are detected when they are present.{{cite:gastwirth_gel_miao2009}} (§1); {{cite:nist_levene2002}} (§1.3.5.10)

The one-way model that this $F$ is borrowing writes $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$ and compares a between-group sum of squares with a within-group sum of squares. Applied to the $Z_{ij}$, the “treatments” are the groups and the “observations” are absolute deviations. Rejection says that the groups differ in the location of $|Y - c|$, which is the sense in which the scale differs. It does not say which group is more variable, and it does not by itself name a transformation.{{cite:dodge2008}} (pp. 399–400)

## Properties — Mean, median, and trimmed mean
As summarised in the NIST/SEMATECH account, sampling comparisons put the trimmed mean ahead when the underlying distribution is Cauchy, and the median ahead when it is chi-squared on $4$ degrees of freedom, a skewed law. The mean-centred form has the best power of the three when the distribution is symmetric with tails that are not extreme. No single centre wins for every distribution. When the shape is unknown, the median is the centre recommended as a default: it keeps the type I behaviour under a range of non-normal laws and still has power. If the shape is known to be symmetric and not heavy-tailed, the mean is the more powerful centre.{{cite:nist_levene2002}} (§1.3.5.10)

The contrast with the other classical variance tests is the reason for going through absolute deviations at all. Bartlett’s test of several variances is sensitive to non-normality: a significant result can be a statement about shape rather than about variance. Levene’s test is the less sensitive alternative. The two-sample variance-ratio test compares $s_1^2/s_2^2$ with an $F$ reference and is the two-group special case of that classical approach, not an analysis of absolute deviations. A Levene statistic can be computed for two groups; it is still the $F$ ratio of the $Z_{ij}$, not the ratio of the sample variances.{{cite:nist_bartlett2002}} (§1.3.5.7); {{cite:nist_ftest2002}} (§1.3.5.9)

`leveneTest` in the car package implements the same analysis. The default centre is the median. Setting the centre to the mean recovers the original statistic. Passing `trim = 0.1` with that mean centre uses a $10\%$ trimmed mean. The default is the resistant choice, not the historically first one, and a published $F$ is not interpretable until the centre is named.{{cite:car_levene2026}} (Usage and Arguments, `center`)

## Worked example — Three groups, two centres
The groups are those in the motivating example, $n_i = 3$, $k = 3$, $N = 9$. The analysis-of-variance $F$ therefore has $2$ and $6$ degrees of freedom, and the upper $5\%$ point of that $F$ law is $5.143$.

The group means are $5$, $4$ and $5$. The absolute deviations from those means are
$$
(2, 0, 2), \qquad (2, 0, 2), \qquad (5, 3, 8).
$$
Their group means are $4/3$, $4/3$ and $16/3$. The nine deviations add to $24$, so the grand mean is $8/3$. The between-group sum of squares is
$$
3\Bigl[\Bigl(\frac{4}{3}-\frac{8}{3}\Bigr)^2 + \Bigl(\frac{4}{3}-\frac{8}{3}\Bigr)^2 + \Bigl(\frac{16}{3}-\frac{8}{3}\Bigr)^2\Bigr] = 3 \cdot \frac{16+16+64}{9} = 32.
$$
Inside the first group the deviations from $4/3$ are $2/3$, $-4/3$ and $2/3$, and the sum of squares is $8/3$. The second group contributes the same $8/3$. Inside the third group the deviations from $16/3$ are $-1/3$, $-7/3$ and $8/3$, and the sum of squares is $38/3$. The within-group sum of squares is $8/3 + 8/3 + 38/3 = 18$. Then
$$
W = \frac{32/2}{18/6} = \frac{16}{3} \approx 5.333.
$$
Since $16/3 > 5.143$, the mean-centred test rejects equal variances at $5\%$. The upper-tail $F$ probability is $0.0467$.

The group medians are $5$, $4$ and $2$. Groups $A$ and $B$ are symmetric, so their absolute deviations do not change. Group $C = (0, 2, 13)$ has median $2$, and its absolute deviations are $2$, $0$ and $11$. The group means of the deviations are $4/3$, $4/3$ and $13/3$, and the grand mean is $7/3$. The between-group sum of squares is $18$ and the within-group sum of squares is $74$, so
$$
W = \frac{18/2}{74/6} = \frac{27}{37} \approx 0.730.
$$
The upper-tail probability is $0.520$. The median-centred test does not reject. `leveneTest` with `center = mean` returns $F = 5.3333$ on $(2, 6)$ degrees of freedom, and with the default median centre it returns $F = 0.7297$. The hand arithmetic and the function agree.{{cite:car_levene2026}} (Usage, `center`)

The two calculations use the same observations and the same $F$ reference. They differ in $c_i$ for the skewed group. The mean of $(0, 2, 13)$ is $5$, pulled toward the outlier, and the absolute deviations $5, 3, 8$ are moderately spread. The median stays at $2$, and the absolute deviations $2, 0, 11$ put almost all of the within-group square on the single large residual. That inflates the denominator of $W$ and the statistic falls from $16/3$ to $27/37$. Choosing the centre is part of the test. On this sample it changes the $5\%$ decision.

Replace $13$ by $4$, so the third group is $(0, 2, 4)$. Every group is then an arithmetic progression with the same spacing, and the absolute deviations from each group mean are $(2, 0, 2)$. The three groups of $Z_{ij}$ are identical, the between-group sum of squares is $0$, and $W = 0$. The mean-centred rejection was carried by the value $13$. A variance test that ignores that fact has reported a property of one observation.

**Your turn.** Two groups are $(0, 2, 4)$ and $(0, 2, 10)$. The centres are the group means, $2$ and $4$. The absolute deviations are $(2, 0, 2)$ and $(4, 2, 6)$. Compute the mean-centred $W$. The upper $5\%$ point of $F$ on $(1, 4)$ degrees of freedom is $7.709$. Does the test reject?

::: {.callout-tip collapse="true" title="Answer"}
The group means of the absolute deviations are $4/3$ and $4$, and the grand mean is $8/3$. The between sum of squares is $32/3$ and the within sum of squares is $32/3$. Then $W = (32/3) / ((32/3)/4) = 4$. Since $4 < 7.709$, the mean-centred test does not reject equal variances at $5\%$.
:::

## Interpretation — What a rejection changes about the next comparison
A rejection says that a single variance is not a fair description of all the groups. It does not order the groups. In the mean-centred example the third group’s absolute deviations are the large ones, which is visible from $(5, 3, 8)$ against $(2, 0, 2)$, but that comparison of the $Z$ means is descriptive. The test itself is one $F$ on all $k$ groups.

The procedures that used the rejected assumption are the ones to set aside. A two-sample statistic that pools the two sample variances assumes those variances are equal. If that assumption is not tenable, the comparison of the two means $\bar Y_1$ and $\bar Y_2$ uses the unpooled statistic
$$
t = \frac{\bar Y_1 - \bar Y_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}},
$$
where $n_1$ and $n_2$ are the sample sizes and $s_1^2$ and $s_2^2$ are the sample variances. The degrees of freedom are the Welch–Satterthwaite values used for a [Welch interval](welch-interval.qmd). If the two standard deviations cannot be treated as equal, the comparison uses this unpooled statistic rather than a pooled variance. A pooled error mean square in a larger layout is the same assumption.{{cite:nist_two_sample_t2002}} (§1.3.5.3); {{cite:nist_means2002}} (§7.3.1)

A non-rejection does not prove the variances equal, any more than a large Shapiro–Wilk $p$-value proves normality. With $N = 9$ and $k = 3$ the $F$ reference on $(2, 6)$ degrees of freedom is wide: the median-centred $W = 0.730$ has tail probability $0.520$. That is a failure to detect a difference in scale, not a demonstration that the scales match. The mean-centred rejection at $p = 0.0467$ is itself close to $5\%$. Reporting $16/3$ and $5.143$, rather than only the word “significant”, shows how little room there was.

## Statistical use — Name the centre, then choose the comparison of means
State $k$, the $n_i$, the centre, $W$, the degrees of freedom, and the reference probability. “Levene’s test was significant” leaves out the choice that, in the worked example, changes the decision. In `leveneTest` the call `leveneTest(y, group)` uses the median. The call with `center = mean` is the original statistic. The two $F$ values $5.333$ and $0.730$ are those two calls on these nine numbers.{{cite:car_levene2026}} (Usage and Arguments, `center`)

If the scientific question is a difference of means and $W$ has rejected a common variance, the follow-up is the unpooled comparison above, not a pooled $t$ and not a further transformation chosen because it makes $W$ smaller. A transformation changes the scale on which the means are compared. That may be the right scientific step, but it is not what the rejection by itself instructs. If the question is the variances, the $F$ on the absolute deviations is already the answer, and the next description is which groups’ deviations are large.

Bartlett’s test remains the more powerful variance comparison when there is strong evidence that the data are nearly normal. Levene’s test is the one to use when that evidence is absent or when a Shapiro–Wilk check on the residuals has already made normality doubtful. The two checks are not substitutes: one is about shape, the other is about scale.{{cite:nist_levene2002}} (§1.3.5.10); {{cite:nist_bartlett2002}} (§1.3.5.7)

## Assumptions and limits — The $F$ reference is an approximation to a ratio of absolute deviations
The statistic $W$ is exactly the one-way $F$ of the constructed variables $Z_{ij}$. The comparison of $W$ with $F_{k-1, N-k}$ treats that ratio as if it had the normal-theory $F$ distribution. The $Z_{ij}$ are absolute deviations, hence skewed and dependent within a group, because the centre $c_i$ is computed from the same observations. The $F$ tail is an approximation to the null distribution of this ratio, not a theorem that $|Y_{ij} - c_i|$ is normal. The case for the procedure is that the approximation is less easily wrecked by a non-normal $Y$ than Bartlett’s chi-squared form. That is an empirical claim about type I behaviour, taken from the sampling comparisons, not an exact null.{{cite:nist_levene2002}} (§1.3.5.10)

With $n_i = 3$ the median of a group is the middle observation, so one of the three absolute deviations is zero whenever the median is unique. The within-group sum of squares is then carried by the other two points. That is visible in the median-centred third group, where $11^2$ dominates $74$. With a larger group the centre is estimated from more observations, and one wild point is a smaller share of the within-group sum of squares. The worked example shows the effect of the centre at $n_i = 3$. It does not estimate power at large $n_i$.

The rejection rule is $W$ greater than the upper point of $F_{k-1,\, N-k}$.{{cite:nist_levene2002}} (§1.3.5.10)

## History — The mean in 1960, the median and the trimmed mean in 1974
The mean-centred statistic is the analysis of variance of absolute deviations from the group means, the form dated to 1960. Replacing those means by the group medians is the 1974 modification. The comparison of the mean, the median and the $10\%$ trimmed mean, as summarised in the NIST/SEMATECH account, is the guidance that the trimmed mean behaves best for a heavy-tailed symmetric law such as the Cauchy, the median best for a skewed law such as $\chi^2_4$, and the mean best for symmetric distributions with moderate tails. When the shape is not known in advance, the median is the robust default drawn from that summary.{{cite:gastwirth_gel_miao2009}} (§1, equation (3)); {{cite:nist_levene2002}} (§1.3.5.10) The software default is the same median centre.{{cite:car_levene2026}} (Arguments, `center`)

## Connections — The variance ratio, the pooled comparison, and the shape check
The [F test for equal variances](f-test-for-equal-variances.qmd) is the two-sample ratio $s_1^2/s_2^2$. [One-way analysis of variance](one-way-analysis-of-variance.qmd) is both the motive for checking a common variance and the arithmetic applied to the absolute deviations. A [Welch interval](welch-interval.qmd) is the two-sample comparison of means that does not pool the variances. The [two-sample $t$ test](two-sample-t-test.qmd) is that comparison in either its pooled or its unpooled form; which form is legal depends on the variance conclusion. The [Shapiro–Wilk test](shapiro-wilk-test.qmd) concerns normality rather than scale. A doubt it raises about the residuals is a reason to prefer Levene’s variance check to Bartlett’s.

## Check yourself
**1.** Two new groups are $(1, 2, 9)$ and $(4, 5, 6)$. Using the group means as centres, what is $W$? The upper $5\%$ point of $F$ on $(1, 4)$ degrees of freedom is $7.709$.

::: {.callout-tip collapse="true" title="Answer"}
The means are $4$ and $5$. The absolute deviations are $(3, 2, 5)$ and $(1, 0, 1)$, with group means $10/3$ and $2/3$ and grand mean $2$. The between sum of squares is $32/3$ and the within sum of squares is $16/3$, so $W = (32/3)/((16/3)/4) = 8$. Since $8 > 7.709$, the mean-centred test rejects at $5\%$.
:::

**2.** For the same two groups, $(1, 2, 9)$ and $(4, 5, 6)$, use the group medians as centres. What is $W$, and does the $5\%$ test reject? The upper $5\%$ point is again $7.709$.

::: {.callout-tip collapse="true" title="Answer"}
The medians are $2$ and $5$. The absolute deviations are $(1, 0, 7)$ and $(1, 0, 1)$. The between sum of squares is $6$ and the within sum of squares is $88/3$, so $W = 6/((88/3)/4) = 9/11 \approx 0.818$. Since $9/11 < 7.709$, the median-centred test does not reject. The choice of centre changes the $5\%$ decision.
:::

**3.** The mean-centred test has rejected a common variance, and the next question is a difference between two of the group means. Which two-sample statistic does not use the rejected assumption?

::: {.callout-tip collapse="true" title="Answer"}
The unpooled statistic, $(\bar Y_1 - \bar Y_2)$ divided by the square root of $s_1^2/n_1 + s_2^2/n_2$, with Welch–Satterthwaite degrees of freedom. The pooled two-sample statistic uses one variance for both groups.
:::
