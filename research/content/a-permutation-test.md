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
