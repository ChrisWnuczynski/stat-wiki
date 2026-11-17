## Lead context
A hierarchy can be built by merging small groups or by splitting large ones; the direction and the criterion are separate choices.

## Motivating example
Four measurements can be grouped coarsely into two populations, or more finely into individual observations. A hierarchical clustering records compatible groups at several resolutions. Rather than select one cluster count before inspecting the data, the procedure produces a nested family that can be cut at different levels.{{cite:dodge2008}} (pp. 82–84, Classification and Cluster Analysis)

## Definition — Merging upwards and splitting downwards
Agglomeration starts from singleton clusters. Each step merges two current clusters until only one remains. Divisive clustering starts from one cluster containing all observations and splits current clusters into smaller ones. A binary hierarchy on $n$ singleton leaves has $n-1$ merges, or $n-1$ splits when all the way to singletons. The two directions can generate different trees because their local choices optimise different conditional problems.{{cite:dodge2008}} (p. 83, agglomerating and dividing techniques){{cite:murtagh_contreras2012}} (§§4, 6)

## Properties — The linkage rule changes the next merge
For disjoint nonempty clusters $A,B$, common dissimilarities are
$$
d_{\rm single}(A,B)=\min_{i\in A,j\in B}d(i,j),\quad
d_{\rm complete}(A,B)=\max_{i\in A,j\in B}d(i,j),
$$
and
$$
d_{\rm average}(A,B)=\frac1{|A||B|}\sum_{i\in A,j\in B}d(i,j).
$$
Single linkage can connect groups through a chain of nearby points. Complete linkage requires every cross-pair to be close before two groups have a small dissimilarity. Average linkage uses every cross-pair and differs from the distance between the two centroids.{{cite:murtagh_contreras2012}} (§4, Table 1)

A merge commits the hierarchy to a grouping: later agglomerative steps cannot separate members of that cluster. In a divisive algorithm, a split similarly prevents later subclusters from crossing its boundary. A top-down rule can focus on a broad partition early, while a bottom-up rule focuses first on local relationships. Neither direction guarantees a global optimum over all possible trees.{{cite:murtagh_contreras2012}} (§§4, 6)

## Worked example
Use points $0,2,3,10$ on the real line with absolute distance. Every linkage starts by merging $\{2\}$ and $\{3\}$ at height one. The distance from $\{2,3\}$ to $\{0\}$ is two under single linkage, three under complete linkage and $2.5$ under average linkage. The next merge joins these clusters in every case. The final merge with ten occurs at height seven, ten or $25/3$, respectively.

| Linkage | Merge heights |
|:--|:--|
| Single | $1,2,7$ |
| Complete | $1,3,10$ |
| Average | $1,2.5,25/3$ |

The final average is $(10+8+7)/3=25/3$. The order happens to agree here, but the heights differ because they summarise different cross-pairs. Those summaries define the vertical scale of the dendrogram.{{cite:murtagh_contreras2012}} (§4, dissimilarity update formulas)

**Your turn.** After merging $\{2,3\}$, compute its average-linkage distance to $\{10\}$.

::: {.callout-tip collapse="true" title="Answer"}
The two cross-distances are eight and seven, so their average is $7.5$. The distance between centroids is also $7.5$ for this particular singleton comparison, but the equality does not hold for arbitrary multivariate clusters.
:::

## Assumptions and limits — Scale, ties and the meaning of height
A dissimilarity measure is an input to the hierarchy. Rescaling one feature changes Euclidean dissimilarities and may change the merges; standardisation is therefore a substantive choice. Equal dissimilarities need a tie rule, and different choices can produce different binary trees. Centroid and median linkage can have inversions, where a later merge has a smaller height than an earlier merge; the usual linkage methods avoid that behaviour.{{cite:murtagh_contreras2012}} (§§2, 5)

A dendrogram does not by itself establish that its groups correspond to distinct generating populations. It summarises a specified dissimilarity and algorithm. The purpose of clustering may be description or prediction, and the interpretation requires the variables and scientific setting.{{cite:dodge2008}} (pp. 83–84, domains and limitations)

