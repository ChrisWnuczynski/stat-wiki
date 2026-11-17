## Motivating example — Compare ordering without modelling the spacing
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
