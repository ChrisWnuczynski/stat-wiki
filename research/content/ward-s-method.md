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

## Interpretation — The size factor is half the harmonic-type weight
The coefficient $n_An_B/(n_A+n_B)$ equals the product of the sizes divided by the merged size. Two singletons have coefficient $1/2$. A squared Euclidean distance of $10$ between them therefore costs $(1/2)\times10=5$. Clusters of sizes $3$ and $6$ with means $2$ and $5$ have coefficient $18/9=2$ and squared separation $9$, so the increase is $18$. Two groups with the same centre have increase zero even when the points inside them differ: the formula depends on the centres and the sizes, and a shared centre makes the squared distance zero. A common scaling of every coordinate by $c$ multiplies every squared distance by $c^2$ and multiplies every Ward increase by $c^2$. With no ties, the chosen pair is unchanged. Scaling a single coordinate changes the geometry and can change the pair.{{cite:murtagh_legendre2014}} (§§2–3)

The worked clusters $A=\{0,2\}$ and $B=\{3\}$ have increase $8/3$. Directly, $W(A)=2$, $W(B)=0$ and the merged sum of squares is $14/3$, so the difference is $14/3-2=8/3$. Replacing the singleton $3$ by $5$ multiplies the squared centre gap by four, from $4$ to $16$, and the increase rises from $8/3$ to $32/3$. The nearest centre to $A$ is not automatically the cheapest merge once a third cluster of two close singletons is available: those singletons at $3$ and $5$ cost only $2$, which is less than $8/3\approx2.666667$. The size adjustment, not the centre gap alone, produces that ordering.{{cite:murtagh_legendre2014}} (§2, within- and between-group sum-of-squares decomposition)

### Statistical use — Squared input and squared-inside-the-algorithm are different criteria
Some implementations square a Euclidean distance that the user supplies. Others expect the dissimilarity to be squared already and then apply a recurrence that updates those dissimilarities. Supplying squared distances to a routine that squares again minimises a fourth-power criterion. The hierarchy and the reported heights both change. A reproducible description names the distance, whether it was squared before the call, and which Ward variant the software selects. The agglomerative sequence is still a greedy path. The partition cut from that tree at a chosen number of groups need not minimise $W$ over all partitions with that number of groups.{{cite:murtagh_legendre2014}} (§3, algorithm variants and input dissimilarities)

## Connections
The objective is a rise in within-cluster sum of squares, the same squared Euclidean scatter used by $K$-means at a fixed number of groups. Ward's method builds a nested sequence of candidate partitions. $K$-means searches for one partition and can move points between groups after the initial assignment. Agreement with an external labelling, when it is computed, is a comparison after the clustering, not a term in $\Delta(A,B)$. Using the labels to pick the linkage spends them on selection.{{cite:dodge2008}} (pp. 83–84, Cluster Analysis){{cite:murtagh_legendre2014}} (§§2–3, author manuscript)
