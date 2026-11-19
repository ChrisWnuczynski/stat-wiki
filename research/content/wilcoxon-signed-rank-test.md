## Lead context
It is the paired procedure that keeps the direction of each difference and weights that direction by the rank of the absolute difference. The weighting is valid as a test of a median, or of a mean, when the differences are symmetric.

## Motivating example
Eight students sit a short test, take a lesson, and sit a parallel test. Seven scores rise, by $1, 2, 3, 4, 5, 6$ and $7$ points. The eighth falls by $12$. A procedure that counts only signs sees seven improvements out of eight and treats the fall of $12$ as one negative sign, the same kind of evidence as a fall of half a point. A procedure that ranks the absolute differences gives that fall rank $8$, the largest rank in the sample, and the conclusion moves. The signed-rank test is the second procedure. The comparison with the sign count, on these same eight numbers, is the worked example below.

## Definition — Signed ranks of the paired differences
Let the paired measurements be $(X_i, Y_i)$ for $i = 1, \ldots, n$, and write $D_i = Y_i - X_i$. Drop every pair with $D_i = 0$, and let $m$ be the number that remain. Rank the absolute values $|D_i|$ from $1$, the smallest, to $m$, the largest. If several absolute values are equal they share the average of the ranks they occupy. When there are no such ties, the signed-rank statistic $W_+$ is the sum of the ranks attached to the positive differences. The negative ranks sum to $m(m+1)/2 - W_+$, so either sum determines the other.{{cite:dodge2008}} (pp. 571–572)

The null used with untied ranks says that the differences are independent and symmetric about zero. Symmetry about zero makes a positive sign and a negative sign equally likely at every rank, and independence makes the $2^m$ ways of signing the ranks equally likely. The same null can be stated for the median of the $D_i$ or for their mean: under symmetry those two centres coincide.{{cite:dodge2008}} (pp. 572–573); {{cite:nist_signrank2023}} (Purpose and assumptions)

A one-sided alternative in the positive direction rejects for large $W_+$. A two-sided alternative rejects for a value far from the null mean in either direction. The same construction tests whether a single sample is symmetric about a stated centre $M$, by pairing each observation with $M$ and ranking those differences.{{cite:dodge2008}} (pp. 572–573)

## Properties — The exact law obtained by signing the ranks
Under the null just stated, $W_+$ is the sum of a random subset of $\{1, 2, \ldots, m\}$, and every subset has probability $2^{-m}$. That is an exact finite law, not an approximation. For a positive-direction alternative the exact $p$-value is the number of subsets whose elements add to at least the observed $W_+$, divided by $2^m$. Because the distribution is symmetric about its mean, the lower tail of the same size is the number of subsets adding to at most $m(m+1)/2 - W_+$. The two tails are disjoint when the observed value is not the mean, and a two-sided probability is then twice the smaller tail. The attainable probabilities are multiples of $2^{-m}$, so a nominal level such as $0.05$ need not be hit exactly.{{cite:nist_signrank2023}} (the $2^m$ signings); {{cite:wilcoxon1945}} (p. 82, enumeration by partitions of the rank sum)

The null mean and variance follow from the same signings. The rank $j$ enters $W_+$ with probability $1/2$, independently of the other ranks, so
$$
\mathrm{E}(W_+) = \sum_{j=1}^{m} \frac{j}{2} = \frac{m(m+1)}{4},
$$
$$
\mathrm{Var}(W_+) = \sum_{j=1}^{m} \frac{j^2}{4} = \frac{m(m+1)(2m+1)}{24}.
$$
The summands $j I_j$ are independent but not identically distributed, because the ranks that weight the signs are different. For $m > 20$ the standardised statistic $(W_+ - \mathrm{E} W_+)/\sqrt{\mathrm{Var} W_+}$ is compared with a normal reference. For smaller $m$ the exact subset count is the probability, and the normal formula is only a description of where the observation sits.{{cite:dodge2008}} (p. 572)

A zero difference is removed before $m$ is chosen, so it contributes neither a sign nor a rank. A tie among absolute values replaces two or more distinct ranks by their average. The uniform distribution on the $2^m$ subsets of $\{1,\ldots,m\}$ is then the wrong reference, because those integers are no longer the ranks in hand. The probability is computed from the midranks that actually occurred.{{cite:dodge2008}} (pp. 571, 574)

## Interpretation — What symmetry adds, and what it does not
The sign test uses only the indicators $I\{D_i > 0\}$. The signed-rank test uses those indicators and the order of the $|D_i|$. When the differences really are symmetric, that extra information is why the signed-rank test is the more powerful of the two against a shift. When symmetry is not a fair description, the sign test is the procedure that still matches the question it asks, which is whether positive and negative differences are equally likely. The gain and the extra assumption are the same fact.{{cite:nist_signrank2023}} (comparison with the sign test)

Symmetry is also what lets the null be read as a statement about the mean. Without it, a mean can sit away from zero while the median is zero, or the reverse, and a large $W_+$ is not by itself a statement about either centre. The paired $t$ statistic $\bar D / s_{\bar D}$ targets the mean difference and takes its critical value from the Student table on $n-1$ degrees of freedom. The signed-rank null replaces that normal-theory reference by symmetry of the differences.{{cite:dodge2008}} (pp. 409, 573); {{cite:nist_signrank2023}} (assumptions)

The worked numbers show that “uses the magnitudes” is not the same sentence as “has the smaller $p$-value in this sample”. One large negative difference pulls $W_+$ down and can leave the signed-rank test short of a $5\%$ rejection while the sign count still rejects. Power is a property of the tests under a stated alternative, not a comparison of two $p$-values on one sample.

## Worked example — Eight pairs and one large decline
The scores before the lesson are $18, 22, 19, 25, 21, 24, 20, 30$. The scores after it are $19, 24, 22, 29, 26, 30, 27, 18$. The differences $D_i = \text{after} - \text{before}$ are
$$
1,\; 2,\; 3,\; 4,\; 5,\; 6,\; 7,\; -12.
$$
None is zero and the eight absolute values are distinct, so $m = 8$ and the ranks of $|D_i|$ are $1$ through $8$ in that order. The only negative rank is $8$. Hence $W_+ = 1+2+3+4+5+6+7 = 28$, and the negative ranks sum to $8$.

The exact reference set is the $256$ subsets of $\{1,\ldots,8\}$. A subset sums to $28$ or more precisely when the ranks left out, the ones that would have been negative, sum to $8$ or less. There is $1$ such signing of negative-sum $0$, $1$ of sum $1$ and $1$ of sum $2$. The counts for negative sums $3$ through $8$ are $2, 2, 3, 4, 5$ and $6$. These add to $25$, so the exact one-sided probability is
$$
P(W_+ \ge 28) = \frac{25}{256} \approx 0.0977.
$$
The matching lower tail is $P(W_+ \le 8) = 25/256$ as well, and the two events are disjoint, so the two-sided probability is $50/256 \approx 0.195$. At a one-sided $5\%$ level the signed-rank test does not reject.

The sign test on the same differences keeps seven positive signs out of eight. Its one-sided probability is
$$
P(N_+ \ge 7) = \frac{\binom{8}{7}+\binom{8}{8}}{256} = \frac{9}{256} \approx 0.0352.
$$
At the same one-sided $5\%$ level the sign test does reject. The two procedures disagree because the fall of $12$ is one sign to the sign test and the rank $8$ to the signed-rank test.{{cite:dodge2008}} (p. 486)

Replace $-12$ by $-1/2$ and leave the other seven differences as they are. The signs are unchanged, so the sign-test probability is still $9/256$. The absolute values are now $1/2, 1, 2, 3, 4, 5, 6, 7$, and the negative difference carries rank $1$ rather than rank $8$. Then $W_+ = 36 - 1 = 35$, and only the empty negative set and the singleton $\{1\}$ produce a positive rank sum of $35$ or $36$. The exact one-sided probability falls from $25/256$ to $2/256 \approx 0.00781$, and the signed-rank test rejects. One observation, changed in magnitude but not in sign, reverses the signed-rank conclusion and leaves the sign test untouched.

The normal approximation is a different object from either exact probability. For $m = 8$,
$$
\mathrm{E}(W_+) = 18, \qquad \mathrm{Var}(W_+) = 51.
$$
The mean and the variance are those of the exact null, and the normal approximation is the reference intended for $m > 20$.{{cite:dodge2008}} (p. 572) The standardised value of $W_+ = 28$ is $10/\sqrt{51} \approx 1.400$, and the corresponding upper normal probability is about $0.0807$. The continuity correction that `wilcox.test` applies by default to this approximation compares $(27.5 - 18)/\sqrt{51} \approx 1.330$ with the same normal curve and gives about $0.0917$.{{cite:r_wilcox_test2026}} (Details, `correct`) Both approximations are smaller than the exact $25/256$. At $m = 8$ the subset count is the probability to report.

The point estimate that accompanies the exact test is the median of the $m(m+1)/2 = 36$ averages $(D_i + D_j)/2$ with $1 \le i \le j \le m$. For these eight differences that median is $3.5$. This is the Hodges–Lehmann estimate of the pseudomedian. For a distribution $F$, the pseudomedian is the median of $(U+V)/2$ where $U$ and $V$ are independent draws from $F$; if $F$ is symmetric, the pseudomedian and the ordinary median are the same number.{{cite:r_wilcox_test2026}} (Details, pseudomedian and the Hodges–Lehmann estimator)

The exact interval is the set of shifts that the exact two-sided test does not reject. With $256$ equally likely signings, $P(W_+ \le 3) = 5/256$, and $5/256 \le 0.025$ while $P(W_+ \le 4) = 7/256 > 0.025$. The test that rejects only for $W_+ \le 3$ or $W_+ \ge 33$ therefore has two-sided size $10/256$. Inverting it on these differences gives the open interval from $-4.5$ to $6$, which are the $4$th and the $33$rd of the ordered pairwise averages. Every shift strictly between those endpoints leaves the untied positive rank sum between $4$ and $32$. Under a continuous symmetric law the coverage of that interval is
$$
P(4 \le W_+ \le 32) = 1 - \frac{10}{256} = \frac{246}{256} \approx 0.9609,
$$
rather than exactly $0.95$, because the exact test cannot spend probability in fractions finer than $1/256$.

In R, `wilcox.test(after, before, paired = TRUE, alternative = "greater")` returns the statistic $V = 28$ and the exact one-sided probability $0.09766$. The default two-sided call returns $0.1953$. Adding `conf.int = TRUE` returns the estimate $3.5$ and the interval from $-4.5$ to $6$. Exact probabilities are the default when fewer than $50$ untied values are present. The argument `exact = FALSE` switches on the normal approximation, and `correct = TRUE`, the default for that approximation, applies the continuity correction whose probability was $0.0917$ above.{{cite:r_wilcox_test2026}} (Usage and Details)

**Your turn.** Five differences are $+3, +1, 0, -2, +4$. Drop the zero, rank the remaining absolute values, and compute $W_+$ and the exact one-sided probability of a positive rank sum at least that large.

::: {.callout-tip collapse="true" title="Answer"}
The zero is removed, so four ranks remain. The absolute values $1, 2, 3, 4$ receive ranks $1, 2, 3, 4$, and the negative difference carries rank $2$. Thus $W_+ = 1+3+4 = 8$. Of the $16$ subsets of $\{1,2,3,4\}$, the three subsets $\{1,3,4\}$, $\{2,3,4\}$ and $\{1,2,3,4\}$ sum to at least $8$. The probability is $3/16 = 0.1875$.
:::

## Statistical use — Reporting the exact count, the interval, and the approximation
For a one-sided question, state the direction before seeing $W_+$, report $m$ after zeros have been dropped, and report the subset count when the absolute values are untied and $m$ is small. The normal probability is the substitute once $m > 20$, and it should be labelled as an approximation. A two-sided report from a symmetric null doubles the smaller tail and stops at $1$ if the two tails meet.{{cite:dodge2008}} (p. 572)

The interval from the inverted exact test is a statement about the pseudomedian, and under the symmetry assumption that the test already uses, that is a statement about the median of the differences. The eight-pair calculation gives the interval, the estimate $3.5$, and the coverage $246/256$ forced by the discreteness of $W_+$. It does not identify the interval as the shortest one with that coverage.

## Assumptions and limits — Where the subset count stops
The exact $2^m$ count uses independence across pairs, symmetry of each difference about the null centre, and no ties among the absolute values. Dependence between pairs, as when several pairs share a ward or a day, does not by itself bias each sign, but it does destroy the claim that all $2^m$ signings are equally likely. The variance formula $m(m+1)(2m+1)/24$ is then the wrong variance for $W_+$.{{cite:dodge2008}} (p. 572); {{cite:nist_signrank2023}} (assumptions)

Symmetry is an assumption about the shape of the differences, not a consequence of pairing. Pairing fixes how $D_i$ is formed. A skewed difference can have median zero and mean far from zero; $W_+$ is then aimed at a centre the distribution does not have. In that case the sign test remains a test of the sign probability, and the signed-rank conclusion does not transfer to it.{{cite:nist_signrank2023}} (comparison with the sign test)

With ties, or with zeros already removed, software that still prints an exact probability is using the conditional law of the signed midranks, not the count over equally likely subsets of $\{1,\ldots,m\}$. Those two numbers answer different reference experiments. For these eight untied differences they coincide, which is why the hand count and `wilcox.test` agree at $25/256$.{{cite:r_wilcox_test2026}} (Details, ties)

## Common misconceptions — Magnitudes do not guarantee a smaller probability
A non-rejection is sometimes read as evidence that the median difference is zero. Here $W_+ = 28$ against a null mean of $18$ and a null standard deviation $\sqrt{51} \approx 7.14$. The exact one-sided probability is $0.0977$. That is what a null distribution of this width does with a moderate rank sum. It is not a measurement of the shift. The Hodges–Lehmann estimate on the same differences is $3.5$, and the exact interval runs from $-4.5$ to $6$: the test’s silence at $5\%$ is compatible with shifts of several points either way.

A second misreading is that the signed-rank test simply “corrects” the sign test and must therefore be more significant whenever the magnitudes are informative. On these eight differences the sign test’s one-sided probability is $9/256$ and the signed-rank probability is $25/256$. Using the magnitudes made the evidence weaker, because the one negative difference was the largest. After that difference is reduced to $1/2$, the signed-rank probability becomes $2/256$ and the sign-test probability does not move. Magnitude is information. It is not a guarantee of a smaller $p$-value.

## History — Paired ranks in 1945
Frank Wilcoxon introduced the ranking of paired differences in 1945, as a quick substitute for the paired comparison of means. In the paired form, ranks $1, 2, \ldots$ replace the absolute differences and a negative difference gives its rank a negative sign. The probability of a small rank total is found by counting the partitions of that total, which is the subset enumeration above in the language of partitions. For eight pairs his table gives probability $0.0078$ for a smaller rank sum of $0$, and $0.024$ for a smaller rank sum of $2$ or less, matching $2/256$ and $6/256$. He also noted that Friedman’s rank method, when only two treatments are compared, reduces to the binomial test that uses the signs alone, and that the signed ranks keep the sizes as well.{{cite:wilcoxon1945}} (pp. 80–82)

A later treatment of the pairs whose difference is exactly zero, removing them before the ranking, was set out in 1949. The null mean $m(m+1)/4$, the null standard deviation, and the normal approximation for $m > 20$ are the form in which the procedure is now calculated when the subset count is no longer the practical reference.{{cite:dodge2008}} (pp. 571–572)

## Connections — Paired signs, unpaired ranks, and the permutation count
The [sign test](sign-test.qmd) is the paired comparison that gives every untied difference the same weight. The [Wilcoxon rank-sum test](wilcoxon-rank-sum-test.qmd) ranks observations pooled from two independent samples; it does not start from pairs. [Paired samples](paired-samples.qmd) are the design that produces the differences $D_i$. The [one-sample $t$ test](one-sample-t-test.qmd), applied to those differences, is the normal-theory comparison of the mean. A [permutation test](a-permutation-test.qmd) is the broader idea of which the $2^m$ signings are one case: the reference distribution is generated by a group of rearrangements that the null says are equally likely.

## Check yourself
**1.** All eight differences in the worked example are positive. What are $W_+$ and the exact one-sided probability?

::: {.callout-tip collapse="true" title="Answer"}
Every rank from $1$ to $8$ is positive, so $W_+ = 36$. Only one of the $256$ signings does this. The probability is $1/256 \approx 0.00391$.
:::

**2.** A ninth pair is added and its difference is $0$. The other eight differences stay as in the worked example. What are $m$ and $W_+$?

::: {.callout-tip collapse="true" title="Answer"}
The zero is dropped before ranking, so $m = 8$ still. The remaining absolute values and their signs are unchanged, and $W_+$ is still $28$. The reference set still has $256$ signings.
:::

**3.** The difference $-12$ is replaced by $-30$. It is still the unique largest absolute value, and it is still negative. What happens to $W_+$ and to the sign count?

::: {.callout-tip collapse="true" title="Answer"}
The order of the absolute values is unchanged, so the ranks are unchanged and $W_+$ stays $28$. The signs are unchanged, so the sign count stays at seven positives out of eight. Increasing a difference that is already the largest, without changing its sign, moves neither statistic.
:::
