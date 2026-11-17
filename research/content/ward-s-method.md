## Motivating example
Suppose a hierarchical clustering procedure must combine two current groups. A merger of two large groups can greatly increase within-group spread even when their centres are reasonably close. Ward's method compares that increase directly. This places a size adjustment beside the distance between centres. It is an agglomerative method: groups are combined step by step into a hierarchy rather than chosen independently at each requested group count.{{cite:dodge2008}} (pp. 83–84, Cluster Analysis)

## Definition — Minimise the rise in within-cluster squares
For a cluster $A$, write $W(A)=\sum_{i\in A}\|x_i-\bar x_A\|^2$. Ward's merge criterion is
$$\Delta(A,B)=W(A\cup B)-W(A)-W(B)
=\frac{n_A n_B}{n_A+n_B}\|\bar x_A-\bar x_B\|^2.$$
The distance is Euclidean and the clusters have positive sizes. At a step, choose the pair with smallest increase. This is a greedy hierarchical decision; it is not a guarantee of a globally optimal partition for a later fixed number of clusters. The sum-of-squares criterion and the details of distance input and reported heights must be distinguished.{{cite:murtagh_legendre2014}} (§§2–3, author manuscript)

## Properties — Derive the size factor
Let $m=(n_A\bar x_A+n_B\bar x_B)/(n_A+n_B)$. For $i\in A$, expand $x_i-m=(x_i-\bar x_A)+(\bar x_A-m)$. The cross term sums to zero because the centred deviations in $A$ sum to zero. Hence $\sum_{i\in A}\|x_i-m\|^2=W(A)+n_A\|\bar x_A-m\|^2$, with the analogous expression for $B$. Substituting the weighted mean leaves the factor $n_An_B/(n_A+n_B)$ multiplying the squared centre difference. This explains why centre distance alone omits part of the criterion.{{cite:murtagh_legendre2014}} (§2, within- and between-group sum-of-squares decomposition)

The merge increase is nonnegative. It is zero exactly when the two centres coincide, even if the groups contain different points. Scaling every coordinate by a common constant scales all increases by its square, preserving the chosen pair in the absence of ties. Scaling only one feature can change the hierarchy because it changes the geometry. A dendrogram therefore reflects the selected representation as well as the merger rule.{{cite:murtagh_legendre2014}} (§§2–3)

## Worked example — Calculate an increase in two ways
Let $A=\{0,2\}$ and $B=\{3\}$. Their sizes are two and one, and their means are one and three. The size-adjusted criterion is $(2/3)(1-3)^2=8/3$. Directly, $W(A)=2$, $W(B)=0$, and the merged mean is $5/3$. The merged sum of squares is $14/3$, so its increase is indeed $14/3-2=8/3$.

Compare $A$ with a singleton at five instead. Its criterion is $(2/3)(1-5)^2=32/3$, four times the earlier increase. Compare two singleton points at three and five: their criterion is $(1/2)(3-5)^2=2$. Thus, if all these groups were available at a step, checking only which centre is nearest to $A$ would miss the smaller increase between the two singletons.

**Your turn.** Clusters of sizes three and six have means two and five. What is their merge increase in one dimension?

::: {.callout-tip collapse="true" title="Answer"}
The size factor is $18/9=2$ and the squared difference is nine, so the increase is eighteen.
:::

## Statistical use — Keep the objective and implementation aligned
Some implementations expect Euclidean distances and square them internally; others apply a recurrence to an already squared dissimilarity. Supplying squared input to an algorithm that squares again changes the criterion. Report the input transformation and method option when reproducibility matters. The distinction between Ward variants has been analysed explicitly in the clustering literature.{{cite:murtagh_legendre2014}} (§3, algorithm variants and input dissimilarities)

## Assumptions and limits — Compactness is the chosen preference
Within-cluster squares favour compact groups in the selected Euclidean coordinates. Elongated groups, very unequal spreads, extreme observations or arbitrary variable units can make that preference scientifically unsuitable. An external label comparison can assess agreement with a classification the algorithm did not use, but selecting the clustering rule using those labels spends that information on selection. Hierarchical grouping supplies an exploratory structure whose usefulness still depends on the problem.{{cite:dodge2008}} (pp. 83–84); {{cite:murtagh_legendre2014}} (§2)
