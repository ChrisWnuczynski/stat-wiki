## Lead context
A permutation test is exact for a specified null symmetry, not for every null assertion about means. Randomly sampling permutations adds a second source of variability to the reference calculation.{{cite:hemerik_goeman2018}} (§2.1, def. 1 and thm. 1)

## Motivating example
Four fixed outcomes are $1,2,4,5$, and two of the four units are assigned to each treatment. If all six assignments are equally plausible under the null, the observed split $(1,2)$ versus $(4,5)$ has mean difference $-3$. Its extremeness can be judged without estimating a normal error variance.

## Properties — Exactness comes from the assignment group
Let $G$ be a finite group of permitted label transformations and let $T$ measure extremeness. Under the null, transforming the observed data by any element of $G$ preserves its distribution. The exact upper-tail permutation probability is $|G|^{-1}\sum_{g\in G}1\{T(gX)\ge T(X)\}$. Under that symmetry, ordering transformed statistics gives a level-$\alpha$ test, with discreteness and ties possibly making it conservative.{{cite:hemerik_goeman2018}} (§2.1, thm. 1)

For a random reference set including the identity and $m$ independent uniform draws from the permitted group, use $(B+1)/(m+1)$, where $B$ counts drawn statistics at least as extreme as the observation. The observed arrangement supplies the extra one. This construction controls rejection probability under the random-permutation scheme; a zero exceedance count does not establish a zero tail probability.{{cite:phipson_smyth2010}} (§§4–6, Monte Carlo and permutation probabilities){{cite:hemerik_goeman2018}} (§3.3, thm. 2)

## Worked example
The six choices for the first group give signed differences $-3,-1,0,0,1,3$. For a two-sided statistic $|\bar Y_A-\bar Y_B|$, two of the six assignments are at least as extreme as the observed split, so the exact probability is $1/3$. Counting one of these assignments twice would change the reference weights and therefore the null experiment.

For sprays A and B in `InsectSprays`, the two observed means are $14.5$ and $15.3333$, giving difference $-0.833333$. Running the displayed code with R's default RNG and `set.seed(1)` gives $1364$ exceedances in $1999$ shuffles and corrected probability $1365/2000=0.6825$. Its grid spacing is $1/2000=0.0005$, but its conditional Monte Carlo standard error is approximately $\sqrt{0.6825(1-0.6825)/1999}=0.01041$. Grid spacing is not simulation accuracy. This distinction between estimating a permutation tail and constructing a valid Monte Carlo test is central to the random-permutation calculation.{{cite:phipson_smyth2010}} (§2, Monte Carlo tests; §§5–6, permutation sampling)

**Your turn.** A random-permutation calculation has $m=999$ and no exceedances. Find the corrected probability and the smallest attainable value.

::: {.callout-tip collapse="true" title="Answer"}
Both are $1/1000=0.001$. The result limits the resolution of this calculation; it does not show that the exact permutation tail equals $0.001$.
:::

## Assumptions and limits
Equality of two means alone does not imply exchangeability of all outcomes; unequal variances or distribution shapes can break that symmetry. Paired or blocked assignment schemes must preserve their restrictions when labels are shuffled. Independent plots and a defensible treatment-assignment mechanism cannot be manufactured by running more permutations.{{cite:hemerik_goeman2018}} (§2.1, group-invariance null; §3.1, sampling transformations)

## Intuition
A permutation test builds its reference distribution from the rearrangements the null itself declares exchangeable. With four numbers and two treatment labels, there are six ways to assign the labels. If the null says each of those assignments was equally likely, the observed mean difference is judged against the six differences those assignments produce. No normal variance is estimated. The price is that the null has to be a statement about the assignments, not merely a statement that two population means are equal. Randomly sampling the rearrangements adds a second layer of chance on top of that exact reference set.{{cite:hemerik_goeman2018}} (§2.1, thm. 1)

## Definition
Let $G$ be the finite set of permitted relabelings and let $T$ be a statistic for which larger values are more extreme. The exact upper-tail probability is the fraction of $g\in G$ with $T(gX)\ge T(X)$. The observed labeling is included, so the fraction is at least $1/|G|$. For the numbers $1,2,4,5$, the six signed mean differences are $-3,-1,0,0,1,3$. The observed split has absolute difference $3$, and two of the six absolute differences are at least that large, so the two-sided probability is $1/3$. If instead $m$ random permutations are drawn and $B$ of them are at least as extreme as the observed statistic, the Monte Carlo probability $(B+1)/(m+1)$ includes the observed arrangement as the extra one in the denominator.{{cite:phipson_smyth2010}} (§§4–6, Monte Carlo and permutation probabilities)

## Statistical use
The Monte Carlo version is used when $|G|$ is too large to enumerate. For the insect-spray means $14.5$ and $15.3333$, one seeded run with $1999$ random shuffles produced $1364$ exceedances and the corrected probability $1365/2000=0.6825$. The spacing of attainable Monte Carlo probabilities is $1/2000=0.0005$. The standard error of that particular estimate, read as a binomial proportion, is about $0.01041$. Those are different descriptions of precision. Spacing says which fractions the formula can return. The standard error says how much the fraction would move if the random permutations were drawn again. With $m=999$ and $B=0$, both the corrected probability and the smallest attainable value are $0.001$. That floor is the resolution of the Monte Carlo test. It is not an estimate that the exact permutation tail equals $0.001$. A run with $B=3$ and $m=99$ would report $4/100=0.04$. A separate proportion near $0.20$, computed from $m=1999$ draws, has binomial standard error $\sqrt{0.2\times 0.8/1999}\approx 0.00895$. That standard error is not the grid spacing $1/2000$.{{cite:phipson_smyth2010}} (§2, Monte Carlo tests; §§5–6, permutation sampling){{cite:hemerik_goeman2018}} (§3.3, thm. 2)

## Common misconceptions
Equality of two means does not license every possible shuffle. If the two groups have different spreads, or if the design was paired, unrestricted relabeling describes a different experiment from the one that was performed. Running more random permutations reduces the Monte Carlo noise. It does not create exchangeability that the design lacked. A reported probability of zero, obtained by ignoring the observed arrangement when $B=0$, is not a tail probability under the construction that keeps the test valid. Ties and a discrete reference set can make the test conservative relative to a nominal level, because the attainable probabilities jump.{{cite:hemerik_goeman2018}} (§2.1, group-invariance null; §3.1, sampling transformations)
