## Motivating example
Two groups of measured responses can be compared by where their observations fall in the pooled ordering. The Wilcoxon rank-sum procedure uses those positions rather than the numerical distances between values. This can be useful when an ordering is meaningful but a normal location model is doubtful. Its null hypothesis and interpretation still need explicit assumptions; a test on ranks is not automatically a general test of equal means or equal medians.{{cite:fay_proschan2010}} (§5.1, pp. 10–13)

## Definition — Condition on pooled observations
For independent samples of sizes $n$ and $m$, pool all $N=n+m$ observations and assign ranks, using midranks for tied values. Let $W$ be the sum of the ranks in the first sample. Under an identical-distribution null with exchangeable group labels, each subset of $n$ pooled observation indices is equally likely conditional on the pooled values. The exact reference law follows by enumerating those subsets. The ranks are fixed in this conditional calculation; the random element is which indices carry the first label.{{cite:dodge2008}} (p. 575); {{cite:fay_proschan2010}} (§5.1.1, pp. 10–12)

## Properties — Relate rank sums to pairwise wins
With no ties, write $U=W-n(n+1)/2$. The quantity $U$ counts pairs in which an observation in the first group exceeds one in the second. With ties, use half a win for equal values. This formulation shows why ordering, rather than a difference of sample means, is central. Under the exchangeable null,
$$E(W)=\frac{n(N+1)}2,\qquad
\operatorname{Var}(W)=\frac{nm(N+1)}{12}$$
when all pooled values differ. Ties reduce the variability of the fixed ranks; they do not justify silently using the untied null law.{{cite:dodge2008}} (p. 575, statistic and tie correction)

For a direct derivation of the mean, each fixed pooled rank is selected with probability $n/N$, and their total is $N(N+1)/2$. For the variance, the random subset samples without replacement from that finite list of ranks. The finite-population covariance between selection indicators produces the factor $nm/(N-1)$ multiplying the population variance of the ranks. Substituting $(N^2-1)/12$ gives the displayed expression. This argument also computes a tie-adjusted variance by substituting the variance of the midranks.{{cite:dodge2008}} (p. 575)

## Worked example — Enumerate every possible rank sum
For groups $1,4,6$ and $3,8,11$, the first group has ranks $1,3,4$, so $W=8$ and $U=2$. There are $\binom63=20$ equally likely index subsets. Their mean rank sum is $10.5$, and four subsets have sum at most eight. The lower-tail exact p-value is therefore $4/20=0.2$. A two-sided p-value requires a specified extremeness rule; in this symmetric untied example, doubling the smaller tail gives $0.4$.

For a tie illustration, use pooled midranks $(1,2.5,2.5,4)$ and groups of size two. The six index subsets have sums $3.5,3.5,5,5,6.5,6.5$. Their variance is $1.5$, below the untied variance $5/3$. The repeated values are counted with their index multiplicities, because the permutation calculation assigns labels to observations.

**Your turn.** In the first example, what is $U$ if the first group instead occupies the three smallest ranks?

::: {.callout-tip collapse="true" title="Answer"}
Its rank sum is $1+2+3=6$, so $U=6-3(4)/2=0$. No first-group observation exceeds a second-group observation.
:::

## Assumptions and limits — Location language needs a location model
If the two populations differ only by a continuous location shift, the test can be interpreted as evidence about that shift. Equal medians alone permit different spreads and shapes and do not supply the exchangeability null. Similarly, a pairwise probability of one half can occur without identical distributions, and the unmodified permutation calibration need not test that weaker null at its nominal level. These interpretations should be distinguished before selecting a procedure.{{cite:fay_proschan2010}} (§§5.1.1–5.1.2, pp. 10–13)

## Statistical use — Exact and approximate calculations answer the same declared comparison
For small samples, subset enumeration gives a transparent reference calculation. Larger samples often use a normal approximation with an appropriate tie correction and, when chosen, a continuity correction. Neither a larger sample nor an approximation removes the need for a valid sampling null. Report the statistic convention, alternative direction and treatment of ties so a reported probability can be reproduced.{{cite:dodge2008}} (pp. 575–576); {{cite:fay_proschan2010}} (§5.1)

## Intuition
Pooling the observations and ranking them throws away the spacing between adjacent values and keeps their order. The rank sum $W$ then asks whether the labels of the first sample sit systematically toward one end of that order. Under an exchangeable null, the labels are a random subset of fixed size. A small rank sum means the first sample occupies low positions more often than that random subset would suggest. The numerical gaps between $1$, $4$, and $6$ do not enter $W$, once the ranks $1,3,4$ have been assigned. Replacing $11$ by $110$ in the second sample of the worked example does not change those ranks, and it does not change $W=8$ or $U=2$.

The Mann–Whitney form $U$ counts pairwise victories. With no ties, each of the $nm$ pairs contributes one if the first-sample member is larger and zero otherwise. The translation $U=W-n(n+1)/2$ removes the ranks the first sample would contribute if it occupied the lowest $n$ positions, namely $1+\cdots+n=n(n+1)/2$. In the worked example $n=3$, that baseline is $6$, and $U=8-6=2$. If the first sample instead holds ranks $1,2,3$, then $U=0$: it wins no pairwise comparison.

### Properties — Mean and variance from sampling without replacement
The $N$ pooled ranks, or midranks, are a finite population. The first sample is a simple random subset of size $n$. Each rank is included with probability $n/N$, so
$$E(W)=\frac{n}{N}\sum_{j=1}^N r_j.$$
With untied ranks $1,\ldots,N$, the sum is $N(N+1)/2$ and $E(W)=n(N+1)/2$. For $n=5$ and $m=5$, this expectation is $5\cdot 11/2=27.5$. The variance is the without-replacement variance of a sample sum. For untied ranks it simplifies to $nm(N+1)/12$. For $n=m=3$ that variance is $3\cdot 3\cdot 7/12=5.25$, matching the variance of the $\binom{6}{3}=20$ equally likely rank sums.

Ties replace the ranks by midranks and reduce their population variance. The worked midranks $(1,2.5,2.5,4)$ have variance $1.5$ across the six equally likely pair-sums, below the untied two-plus-two variance $2\cdot 2\cdot 5/12=5/3$. The null probability of each subset is still $1/\binom{N}{n}$. Averaging the midranks does not change how many subsets are enumerated. It changes the value attached to some of them, and several subsets can share one value.

## Common misconceptions
A significant rank-sum test is sometimes reported as evidence that the medians differ. Equal medians are not the null that the permutation distribution calibrates. The permutation null says that the group labels are exchangeable given the pooled values, which is the null of identical distributions when the samples are independent. Two continuous laws can share a median and still produce a drift in the rank sum, if one is more spread out than the other. A pure location shift is an extra model. Under that model the test speaks about the shift. Without it, the test speaks about the exchangeability assumption that was used to build the reference distribution.{{cite:fay_proschan2010}} (§§5.1.1–5.1.2, pp. 10–13)

The one-sided probability in the worked example is $4/20=0.2$. Doubling it to $0.4$ uses symmetry of the untied null distribution of $W$ about its mean $10.5$. Ties can break that symmetry. A two-sided rule then has to say whether extremeness is measured by the tail probability, by the distance from the mean, or by the distribution of $|W-E(W)|$. Those rules can disagree. The reported probability should name the rule.

## Connections
The sign test is the paired special case that keeps only the sign of each within-pair difference. The rank-sum test keeps the order of all pooled values and ignores pairing. A paired rank procedure, such as a signed-rank statistic, uses both the pairing and the ranks of the absolute differences. Choosing among them is a choice of the comparison and of the null, not a choice of which table has the smallest $p$-value on one sample. The normal approximation with a tie correction is a large-sample stand-in for the same subset distribution. It inherits that distribution's null. It does not create a null of equal means that the subset enumeration did not have.
