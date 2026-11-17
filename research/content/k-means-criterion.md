## Motivating example
Clustering asks for groups whose members resemble one another. K-means makes that request concrete through squared Euclidean distance to a representative centre. The criterion provides a way to compare partitions with the same number of groups, but its value is meaningful only relative to the selected measurements and their scales. A different distance can encode a different definition of similarity.{{cite:dodge2008}} (pp. 83–84, Cluster Analysis)

## Definition — Sum distances to the cluster means
For observations $x_1,\ldots,x_n\in\mathbb R^p$ and a partition into $K$ nonempty sets $C_1,\ldots,C_K$, define
$$W=\sum_{k=1}^K\sum_{i\in C_k}\|x_i-\bar x_k\|^2,\qquad \bar x_k=\frac1{n_k}\sum_{i\in C_k}x_i.$$
The objective uses each observation once and weights larger clusters through their number of members. It does not average the cluster variances with equal cluster weights. The global k-means problem minimises $W$ over partitions with the specified $K$, whereas practical transfer or alternating algorithms generally seek local optima.{{cite:hartigan_wong1979}} (p. 100, Description and Purpose)

## Properties — Three equivalent views of the same cost
For a fixed cluster $C$ and proposed centre $m$, expansion around its mean gives
$$\sum_{i\in C}\|x_i-m\|^2=\sum_{i\in C}\|x_i-\bar x_C\|^2+|C|\|m-\bar x_C\|^2.$$
The cross term vanishes because the centred observations sum to zero. Thus the cluster mean minimises its squared-distance loss. Conversely, for fixed centres, each observation minimises its contribution by joining a nearest centre, subject to handling ties and empty groups. Alternating those two optimisations cannot increase the objective, although it can stop at a local solution.{{cite:hartigan_wong1979}} (pp. 100–101, initial assignments and centroid updates)

There is also a pairwise-distance identity:
$$\sum_{i\in C}\|x_i-\bar x_C\|^2=\frac1{2|C|}\sum_{i,j\in C}\|x_i-x_j\|^2.$$
To prove it, expand both squared distances in the double sum and use $\sum_{i\in C}x_i=|C|\bar x_C$. This form explains why the criterion describes within-group cohesion, but the divisor depends on group size. Replacing it by an unnormalised sum of pairwise distances changes the clustering objective.

Finally, with overall mean $\bar x$, the total scatter splits as
$$\sum_i\|x_i-\bar x\|^2=W+\sum_k n_k\|\bar x_k-\bar x\|^2.$$
Apply the cluster-centre expansion separately to every cluster. For a fixed dataset and $K$, minimising within scatter is equivalent to maximising between-centre scatter weighted by cluster size. The identity is a geometric decomposition, not evidence that a probabilistic mixture model is true.{{cite:dodge2008}} (pp. 83–84, distance-based partitional clustering)

## Worked example — Compare two partitions on the line
Take the observations $0,2,8,10$ and $K=2$. The partition $\{0,2\},\{8,10\}$ has means one and nine, and within cost $W=2+2=4$. Its overall mean is five and total scatter is $25+9+9+25=68$. The between scatter is $2(1-5)^2+2(9-5)^2=64$, confirming $68=4+64$.

The crossed partition $\{0,8\},\{2,10\}$ instead has means four and six and cost $32+32=64$. Its between scatter is four. These are different fits to the same data, so their criterion values can be directly compared. A plot can make the distinction obvious in one dimension, while the same algebra continues to work when a visual comparison is difficult.

**Your turn.** What happens to both $W$ and total scatter if every observation is multiplied by three?

::: {.callout-tip collapse="true" title="Answer"}
Every squared distance multiplies by nine. The good partition has within cost $36$ and the total scatter is $612$. The relative allocation of scatter remains unchanged.
:::

## Statistical use — Distinguish choosing centres from choosing K
If $K=1$, $W$ equals the total scatter. If $K=n$ and all groups are singletons, $W=0$. Splitting a cluster and allowing both new centres to optimise cannot increase the objective, so training $W$ alone favours increasing $K$. Choosing the number of groups therefore requires another criterion, a stability assessment, external information or a specified tradeoff between fit and complexity. A low within cost is a property of a partition, rather than a complete validation of a clustering interpretation.{{cite:hartigan_wong1979}} (p. 100, fixed-$K$ optimisation target)

## Assumptions and limits — Scaling determines which errors are expensive
Changing all coordinates by a common factor rescales the objective but preserves its minimisers. Rescaling one coordinate alone generally changes them. Outlying observations can also dominate because a residual twice as large contributes four times the squared cost. Cluster sizes and shapes are not separately modelled: a large, diffuse population can be split into several compact groups even when it represents one substantive category. These are consequences of choosing a distance-based partitioning objective, so preprocessing and interpretation should be decided together.{{cite:dodge2008}} (pp. 83–84, similarity structure and distance choice)

## Interpretation — One number attached to a partition and a scaling

For a fixed data set the total scatter about the grand mean does not depend on the partition. The decomposition then says that any reduction in within-cluster scatter appears as an equal increase in size-weighted separation of the centres. The identity is algebraic. It does not say that the centres are population means, that the groups were drawn from a mixture, or that $K$ was chosen before the data were seen. [Within-cluster scatter](within-cluster-scatter.qmd) is this sum. [Cluster analysis](cluster-analysis.qmd) includes methods that optimise a different distance or return a tree rather than one partition. [K-means as a limiting case](k-means-as-a-limiting-case.qmd) connects the criterion to a spherical Gaussian mixture whose component variances are driven toward zero. That limit makes the modelling assumptions explicit.

Squaring treats a residual of length two as four times a residual of length one, so a point far from every centre can dominate the sum and drag a centre toward itself. Multiplying every coordinate by the same constant multiplies the criterion by the square of the constant and leaves the minimising partitions unchanged. Multiplying a single coordinate changes the geometry and can change which partition wins. The preprocessing and the criterion are one decision. Training scatter also falls whenever $K$ is allowed to grow and empty groups are forbidden only at $K=n$, where the scatter is zero because every point is its own centre. A small within-cluster sum is therefore not, by itself, a reason to prefer a larger $K$.{{cite:dodge2008}} (pp. 83–84, similarity structure and distance choice){{cite:hartigan_wong1979}} (p. 100, fixed-$K$ optimisation target)
