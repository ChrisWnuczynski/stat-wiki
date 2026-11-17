## Motivating example
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

## Intuition
Squared distance to a centre is a cost of representation. With more centres, the procedure is allowed a richer menu of representatives. Any partition into $K$ groups is still available when $K+1$ groups are allowed: leave one extra centre unused, or split one group and keep the old centre for both pieces. The second option is the one used in the proof, and replacing those centres by the new group means cannot raise the cost. The optimised cost is therefore a nonincreasing function of $K$. The singleton partition drives it to zero whenever every observation can sit at its own centre.

The regression analogue is the training residual sum of squares. Adding a column that is free to receive a coefficient can only reduce that sum, or leave it unchanged if the column lies in the span of the columns already fitted. A smaller training residual is then a property of the enlarged model class. It becomes evidence about prediction only when the comparison is changed: a penalty, a held-out sample, or a reference distribution supplies the missing standard.{{cite:openintro2019}} (§9.2, “Model selection”)

## Interpretation — The split formula is an exact identity
Suppose a cluster with $n_A+n_B$ points and centre equal to the grand mean of those points is divided into groups of sizes $n_A$ and $n_B$, with means $\bar x_A$ and $\bar x_B$. The drop in within-cluster sum of squares is
$$\frac{n_A n_B}{n_A+n_B}\|\bar x_A-\bar x_B\|^2.$$
The drop is zero when the two means coincide, and positive when they differ. For the observations $0,1,10$, the one-group cost is $182/3$. Splitting off the point $10$ uses sizes $2$ and $1$ and means $1/2$ and $10$, so the formula returns
$$\frac{2\cdot 1}{3}\left(10-\frac12\right)^2=\frac{361}{6}\approx 60.166667.$$
The two-group cost is $1/2$, and $182/3-1/2=361/6$. The identity accounts for the whole reduction. It also shows why a split of two identical values, such as two copies of $7$, has reduction zero: the new means are both $7$, and the squared gap is zero.

Ward's merge step runs the same identity in reverse. Merging two clusters increases the within-cluster cost by that weighted squared distance between means. Choosing the merge with the smallest increase is a greedy path through partitions. The path's costs still fall as clusters are split, and the raw cost at the end of the path, one cluster per distinct point, is still zero. A dendrogram displays the costs. It does not turn the smallest cost into a preferred number of groups.{{cite:murtagh_legendre2014}} (§2, within/between decomposition)

## Common misconceptions
A plot of $W_K$ against $K$ that declines and then flattens is often read as evidence for an elbow. The decline itself is guaranteed for the optimised costs, whether or not the observations form separated groups. An elbow is a judgement about the size of successive drops relative to a purpose. The gap statistic makes one such judgement explicit by comparing $\log W_K$ with the same quantity on reference samples that have no clusters in the chosen null model. The reference costs also decline with $K$. The gap is the difference of the two declines.{{cite:holmes_huber2019_msmb}} (§5.7.1, algorithm and selection inequality)

A local algorithm can report a larger cost at $K=6$ than at $K=5$. That pair of outputs is compatible with $W_6^*\le W_5^*$, because the $K=6$ run may have missed the optimal partition. The inequality constrains the minimised values. It does not constrain every pair of suboptimal fits. Repeating the starts, or initialising the larger model from a split of the smaller one, is a check on optimisation. It is not a substitute for a criterion that can prefer a small $K$.

## Connections
The decomposition used here is the same within-group and between-group split that appears in a one-way sum of squares. There the number of groups is fixed by the design, and the $F$ ratio compares the two sums under a probability model. Here the number of groups is a choice, and the within-group sum is being asked to make that choice. The probability model is absent until a reference distribution or a sampling scheme is added. Feature scaling sits in the same gap: multiplying one coordinate by ten changes Euclidean squared distances, changes $W_K^*$, and can change which partition a penalty or a gap calculation selects. The monotonicity in $K$ survives that rescaling. The scientific meaning of a selected $K$ does not.
