## Motivating example — A criterion that rewards more groups
A clustering objective can select the best partition among candidates with a fixed number of groups while failing to select that number. Within-cluster squared distances illustrate the distinction. Giving the procedure more centres makes a closer centre available, so the best achievable value cannot increase. A method that reports a smaller raw sum of squares after increasing the group count has therefore demonstrated a built-in property of its objective.{{cite:murtagh_legendre2014}} (§2, within-cluster sum of squares)

## Definition — Compare optimised values on a common data set
Let $W_K^*$ be the minimum of $\sum_i\|x_i-c_{z_i}\|^2$ over partitions into $K$ nonempty clusters and their centres. Use the same observations, features and Euclidean scaling for each $K$. For $1\le K<n$, a cluster containing at least two observations can be split into two nonempty pieces. Retaining its old centre as a candidate centre for each piece gives exactly its former cost; replacing the two centres by their respective means cannot increase that cost. Thus $W_{K+1}^*\le W_K^*$.{{cite:murtagh_legendre2014}} (§2, within-cluster centre and sum-of-squares criterion)

## Properties — The singleton endpoint fixes the outcome
At $K=n$, each observation forms a singleton with its own value as centre, so $W_n^*=0$. Since squared distances are nonnegative, this is the smallest possible cost. Minimising the raw objective over $K$ therefore permits the maximal group count as a winner. Repeated values can produce zero cost sooner, so uniqueness of that choice is not guaranteed. The obstruction is overflexibility of the comparison criterion rather than a numerical failure. The analogous issue in regression is that extra fitted terms can reduce training residual error without establishing better prediction.{{cite:openintro2019}} (§9.2, “Model selection”)

For a split into groups $A,B$, the exact cost reduction is $\frac{n_A n_B}{n_A+n_B}\|\bar x_A-\bar x_B\|^2$. It is positive when the two new means differ, and zero when they coincide. This is the reverse of Ward's merge increase. It provides a quantitative account of why refining a partition cannot raise its optimised within-group cost.{{cite:murtagh_legendre2014}} (§2, within/between decomposition)

## Worked example — Three values reveal the degeneracy
For observations $0,1,10$, the one-group mean is $11/3$. The squared deviations sum to $546/9=182/3\approx60.666667$. With groups $\{0,1\}$ and $\{10\}$, the within-group sum is $0.5$. With three singletons it is zero. The cost reduction in the first split is $(2\times1/3)(0.5-10)^2=361/6\approx60.166667$, matching $182/3-1/2$.

The two-group partition captures the visibly large separation, but the raw objective still prefers the zero-cost singleton partition. A scientific interpretation of two groups is therefore additional information about what kinds of structure should count, rather than a consequence of minimising the unpenalised objective over all group counts.

**Your turn.** If a cluster contains two copies of seven, does splitting it into two singleton clusters strictly reduce the within-cluster sum of squares?

::: {.callout-tip collapse="true" title="Answer"}
No. Both before and after splitting, all distances to the relevant means are zero. The nonincrease can be an equality.
:::

## Statistical use — Add a comparison with a meaningful reference
A penalty, a prediction target, a stability assessment or a reference-data comparison adds information that the raw cost lacks. A penalty charges extra groups; a reference approach asks whether the observed reduction exceeds reductions expected from its specified unclustered data model. Such methods answer different questions and depend on their calibration. A reference uniform over coordinate ranges also depends on the feature representation. Model selection requires a criterion matched to the purpose of the analysis.{{cite:openintro2019}} (§9.2, “Model selection”); {{cite:murtagh_legendre2014}} (§2)

The gap statistic makes the reference comparison explicit: $\operatorname{Gap}(K)=E_*[\log W_K^*]-\log W_K$. A usual rule selects the smallest $K$ whose gap is at least the next gap minus its simulation uncertainty term. The comparison is against reference samples whose own raw costs also decrease as centres are added.{{cite:holmes_huber2019_msmb}} (§5.7.1, algorithm and selection inequality)

## Assumptions and limits — Optimisation error can obscure the pattern
The nonincrease is a statement about optimal costs, or a controlled refinement that uses the preceding solution as a candidate. Independent random starts of a local optimisation routine can return a worse value at a larger $K$. That observation does not reverse the mathematical inequality; it shows that at least one fitted solution is not the global optimum. Separating the objective's properties from the optimiser's performance prevents a poor run from being read as evidence for a preferred cluster count.{{cite:murtagh_legendre2014}} (§§2–3, criterion versus algorithm)
