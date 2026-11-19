## Lead context

Three or more groups are measured on the same numerical response, and the analyst is not willing to treat the response as normal or the variances as equal. The Kruskal–Wallis test asks whether the groups could reasonably be samples from the same continuous distribution, using only the ranks of the combined data. A large value of its statistic is evidence that at least one group tends to produce larger observations than the others. {{cite:dodge2008}} (pp. 288–289) {{cite:nist_kruskal2002}} (§7.4.1)

## Motivating example

Four cooking oils are compared by the amount of fat potatoes absorb. Five, six, four, and five batches give twenty numbers, which are replaced by their ranks from 1 to 20, with tied values sharing a mean rank. The rank sums are 37, 98, 53.5, and 21.5. If the oils were exchangeable, those sums would be four pieces of one ranking. They are not close. The rank statistic equals 13.64, and a tie correction moves it only to 13.67. At level 0.05 the chi-squared reference value with 3 degrees of freedom is 7.81. Because $13.64>7.81$, the hypothesis of identical distributions is rejected. Which oil differs from which is a later, pairwise question. {{cite:dodge2008}} (pp. 289–290)

## Definition

Let there be $k\ge 2$ independent random samples, of sizes $n_1,\ldots,n_k$, from continuous distributions, and write $N=\sum_i n_i$. Rank all $N$ observations together, rank 1 for the smallest. Ties receive the average of the ranks they span. Let $R_i$ be the sum of the ranks in sample $i$. When ties are absent or few, the Kruskal–Wallis statistic is

$$
H=\frac{12}{N(N+1)}\sum_{i=1}^k\frac{R_i^2}{n_i}-3(N+1).
$$


If there are $g$ groups of tied values, of sizes $t_1,\ldots,t_g$, the tie-corrected statistic divides $H$ by $1-\sum_i(t_i^3-t_i)/(N^3-N)$. {{cite:dodge2008}} (pp. 288–289) {{cite:nist_kruskal2002}} (§7.4.1)

The null hypothesis is that the $k$ populations are identical. The alternative is that at least one population tends to produce observations different from the others. NIST phrases the same null as similarity of the populations in central tendency, or in their medians, under continuous distributions of the same shape. The rejection region is one-sided: only a large $H$ counts against the null, because the statistic measures unevenness of the rank sums. For three samples each of size at most 5 and no ties, Dodge uses the exact Kruskal–Wallis table. Otherwise $H$ is referred to a chi-squared distribution with $k-1$ degrees of freedom. NIST states the chi-squared approximation when every $n_i>4$. {{cite:dodge2008}} (pp. 288–289) {{cite:nist_kruskal2002}} (§7.4.1)

## Interpretation

Pooling the samples and ranking them throws away the original scale and keeps the order. If every group is a sample from the same continuous law, the ranks are a random deal of $\{1,\ldots,N\}$ into groups of the observed sizes. The ranks from 1 through $N$ sum to $N(N+1)/2$. For $N=12$ that total is 78, so three rank sums on a partition of those ranks must add to 78. A group of four is at most the four largest ranks, $9+10+11+12=42$, and at least the four smallest, $1+2+3+4=10$. Rank sums 12, 24, and 48 cannot occur: 48 exceeds 42, and $12+24+48=84$ is not 78.

Under the null each group’s rank sum has a known expectation, $n_i(N+1)/2$. A group that sits high in the list pulls its rank sum up. Squaring the rank sums, weighting by group size, and comparing with the chi-squared law asks whether the deal is too uneven to credit to the shuffle. The tie correction is close to 1 when ties are scarce. In the potato-oil data the uncorrected value 13.64 and the corrected value 13.67 lead to the same decision at the 5 percent chi-squared threshold. If the test rejects, it does not name the differing group. Pairwise two-sample rank tests are a follow-up. The Kruskal–Wallis test itself remains a single test of the global null. {{cite:nist_kruskal2002}} (§7.4.1) {{cite:dodge2008}} (pp. 288–290)

The samples are random and mutually independent, and the measurements must be rankable. A grouping chosen after seeing the data is a different procedure, and the reference distribution of $H$ no longer matches the procedure that was run.

## Worked example

Three groups of four have rank sums $R_i=10$, $26$, and $42$. These are the extreme allocation: ranks $1+2+3+4$, $5+6+7+8$, and $9+10+11+12$. Then $N=12$, each $n_i=4$, the sums add to 78, and there are no ties.

$$
\sum_i\frac{R_i^2}{n_i}=\frac{10^2+26^2+42^2}{4}=\frac{100+676+1764}{4}=\frac{2540}{4}=635.
$$


$$
H=\frac{12}{12\cdot 13}\cdot 635-3\cdot 13=\frac{635}{13}-39=\frac{635-507}{13}=\frac{128}{13}\approx 9.846.
$$


The chi-squared 5 percent point with $k-1=2$ degrees of freedom is about 5.991, and $128/13>5.991$. For three samples of size 4 the exact reference is the Kruskal–Wallis table, because each sample size is at most 5. The value $128/13$ is the statistic. The table, not the chi-squared point, is the critical value Dodge specifies for this size. {{cite:dodge2008}} (pp. 288–289) {{cite:nist_kruskal2002}} (§7.4.1)

**Your turn.** Three other groups of four have rank sums 18, 26, and 34. Compute $H$.

::: {.callout-tip collapse="true" title="Answer"}
The rank sums add to 78. The weighted sum of squares is $(324+676+1156)/4=2156/4=539$. Then $H=539/13-39=(539-507)/13=32/13\approx 2.462$.
:::

## Connections

[One-way analysis of variance](one-way-analysis-of-variance.qmd) asks a related question under a normal model and compares means rather than rank sums. The Wilcoxon rank-sum test is the two-sample ancestor and the usual pairwise follow-up. A chi-squared distribution is the large-sample reference, here with $k-1$ degrees of freedom. An [effect size](effect-size.qmd) describes the magnitude of a difference once the test has only said that a difference is detectable. The oil comparison rejected a global null. It did not estimate how many grams of fat separated the oils.

## History

Kruskal and Wallis published the procedure in 1952, in the *Journal of the American Statistical Association*, under the title “Use of ranks in one-criterion variance analysis,” with an erratum the next year. The paper placed a rank statistic beside the one-way analysis of variance for a single grouping factor. Exact critical values for the smallest three-sample layouts were tabled for sample sizes up to 5, and the chi-squared approximation was stated for larger samples. The test has stayed in that role: a single rank comparison of several groups, with pairwise rank tests held back until the global comparison rejects. {{cite:dodge2008}} (pp. 288–290)
