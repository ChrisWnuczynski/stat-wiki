

## Lead context

Three or more groups are measured on the same numerical response, and the analyst is not willing to treat the response as normal or the variances as equal. The Kruskal–Wallis test asks whether the groups could reasonably be samples from the same continuous distribution, using only the ranks of the combined data. A large value of its statistic is evidence that at least one group tends to produce larger observations than the others.{{cite:dodge2008}} (pp. 288–289){{cite:nist_kruskal2002}} (§7.4.1)

## Motivating example

Four cooking oils are compared by the amount of fat potatoes absorb. Five, six, four, and five batches give twenty numbers, which are replaced by their ranks from 1 to 20, with tied values sharing a mean rank. The rank sums are 37, 98, 53.5, and 21.5. If the oils were exchangeable, those sums would be four pieces of one ranking. They are not close. The rank statistic equals 13.64, and a tie correction moves it only to 13.67. At level 0.05 the chi-squared reference value with 3 degrees of freedom is 7.81, so the hypothesis of identical distributions is rejected. Which oil differs from which is a later, pairwise question.{{cite:dodge2008}} (pp. 289–290)

## Definition

Let there be $k\ge 2$ independent random samples, of sizes $n_1,\ldots,n_k$, from continuous distributions, and write $N=\sum_i n_i$. Rank all $N$ observations together, rank 1 for the smallest. Ties receive the average of the ranks they span. Let $R_i$ be the sum of the ranks in sample $i$. When ties are absent or few, the Kruskal–Wallis statistic is

$$
H=\frac{12}{N(N+1)}\sum_{i=1}^k\frac{R_i^2}{n_i}-3(N+1).
$$

If there are $g$ groups of tied values, of sizes $t_1,\ldots,t_g$, the tie-corrected statistic is $H$ divided by $1-\sum_i(t_i^3-t_i)/(N^3-N)$.{{cite:dodge2008}} (pp. 288–289){{cite:nist_kruskal2002}} (§7.4.1)

The null hypothesis is that the $k$ populations are identical. The alternative is that at least one population tends to produce different observations from the others. For three samples each of size at most 5 and no ties, an exact table of $H$ is available. Otherwise, when each $n_i$ is not tiny, $H$ is referred to a chi-squared distribution with $k-1$ degrees of freedom, and the test rejects for large $H$ only.{{cite:dodge2008}} (pp. 288–289){{cite:nist_kruskal2002}} (§7.4.1)

Pooling the samples and ranking them throws away the original scale and keeps the order. If every group is a sample from the same continuous law, the ranks are a random deal of $\{1,\ldots,N\}$ into groups of the observed sizes, and each group’s rank sum has a known expectation. A group that systematically sits high in the list pulls its rank sum up. Squaring the rank sums, weighting by group size, and comparing with the chi-squared law is a way of asking whether the deal is too uneven to credit to the shuffle.{{cite:nist_kruskal2002}} (§7.4.1){{cite:dodge2008}} (p. 288)

Under the null, and with continuous distributions so that ties have probability zero, the ranks are a random allocation. The chi-squared approximation is a large-sample description of $H$, recommended in handbook calculations when every $n_i>4$. The rejection region is one-sided: only a large $H$ counts against the null, because the statistic measures unevenness of rank sums, not a signed direction.{{cite:nist_kruskal2002}} (§7.4.1)

The tie correction is close to 1 when ties are scarce. In the potato-oil data the uncorrected value 13.64 and the corrected value 13.67 lead to the same decision at the usual 5% chi-squared threshold. A correction that large would matter only with heavy tying, where many observations share a rank and the uncorrected $H$ is a bit inflated.{{cite:dodge2008}} (p. 290)

If the test rejects, it does not name the differing group. Pairwise two-sample rank tests, such as the Wilcoxon rank-sum test, are a follow-up, with the usual warning that several pairs are being examined. The Kruskal–Wallis test itself remains a single test of the global null.{{cite:dodge2008}} (p. 289)

The test is the rank analogue of a one-way comparison of several groups when a normal model for the response is unattractive. Handbook practice states the null as similarity of the populations in central tendency, or in their medians, under the assumption that the underlying distributions are continuous and of the same shape. The samples must be random, independent within and across groups, and measured on at least an ordinal scale, so that a combined ranking is meaningful.{{cite:nist_kruskal2002}} (§7.4.1){{cite:dodge2008}} (p. 289)

Report $k$, the sample sizes, whether ties were corrected, the value of $H$, the degrees of freedom $k-1$, and the reference value or table value used. A significant $H$ is a finding about the family of groups. It is not a list of pairwise differences, and it is not an estimate of how far apart the groups are on the original scale. An [effect size](effect-size.qmd) on that scale is a separate summary.{{cite:dodge2008}} (pp. 289–290)

A significant Kruskal–Wallis test does not say that every pair of groups differs, and it does not say that the group with the largest rank sum differs from each of the others by a scientifically important amount. The null is identical continuous distributions, not merely equal means inside a normal model. Replacing the data by ranks is the method, not a preliminary check that one may ignore when the raw averages look tidy. Using a two-sided chi-squared critical value, as if small $H$ were also evidence, contradicts the one-sided rejection rule.{{cite:nist_kruskal2002}} (§7.4.1){{cite:dodge2008}} (p. 289)

The samples are assumed random and mutually independent, and the measurements must be rankable. The chi-squared reference wants sample sizes that are not very small; a handbook states the approximation for $n_i>4$, and exact tables cover the smallest three-sample designs. Heavy ties should be corrected. The test is not a licence to ignore how the groups were formed. If the grouping was chosen after seeing the data, the reference distribution no longer matches the procedure that was run.{{cite:dodge2008}} (p. 289){{cite:nist_kruskal2002}} (§7.4.1)

## Worked example

Three groups have sizes $n_i=3$ and rank sums $R_i=10$, $15$, and $20$, so $N=9$ and there are no ties. Then

$$
\sum_i\frac{R_i^2}{n_i}=\frac{10^2+15^2+20^2}{3}=\frac{725}{3},
$$

and

$$
H=\frac{12}{9\cdot 10}\cdot\frac{725}{3}-3\cdot 10=\frac{2}{15}\cdot\frac{725}{3}-30=\frac{290}{9}-30=\frac{20}{9}.
$$

So $H=20/9\approx 2.222$. The chi-squared reference with $k-1=2$ degrees of freedom at level 0.05 is about 5.99. Because $20/9<5.99$, this ranking does not reject the null at that level. The groups are too small for the chi-squared approximation to be the exact test; the arithmetic is the definition of $H$. The chi-squared tail is an approximation, so the numerical comparison with 5.99 is not an exact $p$-value.{{cite:dodge2008}} (p. 288){{cite:nist_kruskal2002}} (§7.4.1)

**Your turn.** Keep three groups of size 4, with rank sums 10, 26, and 42, so $N=12$. Compute $H$.

::: {.callout-tip collapse="true" title="Answer"}
The weighted sum of squared rank sums is $(100+676+1764)/4=2540/4=635$. Then $H=12/(12\cdot 13)\cdot 635-3\cdot 13=635/13-39=(635-507)/13=128/13\approx 9.846$. The value is large beside a chi-squared reference with 2 degrees of freedom. These group sizes still sit at the edge of the usual chi-squared recommendation.
:::

## Connections

[One-way analysis of variance](one-way-analysis-of-variance.qmd) asks a related question under a normal model and compares means rather than rank sums. The Wilcoxon rank-sum test is the two-sample ancestor and the usual pairwise follow-up. A chi-squared distribution is the large-sample reference, here with $k-1$ degrees of freedom. An [effect size](effect-size.qmd) describes the magnitude of a difference once the test has only said that a difference is detectable.

## History

Kruskal and Wallis published the procedure in 1952, in the *Journal of the American Statistical Association*, under the title “Use of ranks in one-criterion variance analysis,” with an erratum the next year. The paper placed a rank statistic beside the one-way analysis of variance for the case of a single grouping factor. Exact critical values for the smallest three-sample layouts were tabled separately, and the chi-squared approximation was stated for larger samples. The test has stayed in that role: a single rank comparison of several groups, with pairwise rank tests held back until the global comparison rejects.{{cite:dodge2008}} (pp. 288–290)
