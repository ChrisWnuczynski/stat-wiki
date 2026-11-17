## Lead context
Single linkage joins two clusters as soon as their closest points touch, so a chain of neighbours can connect distant ends.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525)

## Motivating example
Five towns lie along a road, each a short walk from the next, except that the last gap is long. A clustering rule that watches the nearest pair will attach each town to the growing chain at the length of its own gap. The early groups are already stretched from the first town to the latest one, even though every individual step was short. That is the pattern single linkage is built to record, and it is the pattern one refuses when the scientific question is about compact groups.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.41, pp. 523–524){{cite:james_islr2021}} (Ch. 12, §12.4, p. 524)

## Intuition — One close pair is enough
The single-linkage dissimilarity of clusters $D_1$ and $D_2$ is the smallest $d(x,y)$ with $x$ in one cluster and $y$ in the other. The rest of the cross-pairs do not enter. Two clouds are declared close when they touch, regardless of how far their far sides sit. The resulting clusters can have a large diameter, the largest dissimilarity inside the cluster, while every fusion that built them was short. The rule is also called nearest-neighbour linkage. It needs only the pairwise dissimilarities, not coordinates or centroids.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525){{cite:dodge2008}} (pp. 84–85){{cite:james_islr2021}} (Ch. 12, §12.4, p. 524)

Because the rule uses a minimum, a strictly increasing transformation of every dissimilarity leaves the fusions unchanged. The numerical scale of $d$ does not matter, only the order.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 524–525)

## Definition
Agglomerative clustering starts from singleton clusters and repeatedly fuses the closest pair. Under single linkage the distance between clusters is
$$
d_S(D_1,D_2)=\min\{d(x,y):x\in D_1,\, y\in D_2\}.
$$
After $D_a$ and $D_b$ fuse, the distance from the union to another cluster $D_k$ is the minimum of the two distances that $D_a$ and $D_b$ already had to $D_k$. The dendrogram height of a fusion is that minimum. There are $n-1$ fusions.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.41, pp. 523–524){{cite:dodge2008}} (pp. 84–85)

## Properties — The next height still cannot fall
Single linkage, like complete linkage, produces nondecreasing fusion heights. The reason is the minimum rather than the maximum: each distance that survives a fusion was already at least as large as the height just used.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $h$ be the smallest single-linkage distance among the current clusters, achieved by $D_a$ and $D_b$. For any other cluster $D_k$,
$$
d_S(D_a\cup D_b,\, D_k)=\min\bigl(d_S(D_a,D_k),\, d_S(D_b,D_k)\bigr).
$$
Both distances on the right are at least $h$, so their minimum is at least $h$. The next fusion is therefore at a height of at least $h$.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.41, pp. 523–524)

The diameter need not equal that height. If points $0,1,2$ fuse by the gaps of length $1$, both fusions sit at height $1$, but the diameter of $\{0,1,2\}$ is $2$. The minimum cross-pair that authorised each fusion was smaller than the largest pair inside the finished cluster.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.44, pp. 524–525)
:::
:::

A further population limit is sharper. If two clusters are random samples from fixed densities with overlapping support, the nearest cross-pair tends to zero as the samples grow, whether or not the densities are separated in any average sense. The single-linkage height between them does not settle on a stable contrast of the two populations.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 524–525)

## Statistical use — A cut records a nearest-neighbour threshold
Cutting the dendrogram at height $h$ returns clusters inside which every point can be joined to every other by steps of dissimilarity at most $h$. That is a connectivity statement. It is not a bound on the diameter, and it is not a probability that the clusters are the groups which generated the data. When the sample really does consist of compact, well-separated clumps, single linkage often agrees with complete and average linkage. When a bridge of intermediate points is present, single linkage follows the bridge and can produce one long group beside several singletons.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525){{cite:james_islr2021}} (Ch. 12, §12.4, pp. 524–525)

## Worked example
Use absolute difference on the points $0$, $2$, $3$ and $8$. The closest pair is $\{2,3\}$ at distance $1$. Single linkage from $\{2,3\}$ to $0$ is $\min(2,3)=2$, and from $\{2,3\}$ to $8$ is $\min(6,5)=5$. The next fusion attaches $0$ at height $2$. The last fusion attaches $8$ at
$$
\min(8,6,5)=5.
$$
The heights are $1$, $2$ and $5$. Complete linkage on the same points uses maxima and finishes at $8$, the diameter of the whole set. Single linkage finishes at $5$, the gap from $3$ to $8$, and never consults the gap from $0$ to $8$. The cluster $\{0,2,3\}$ was completed at height $2$, while its diameter is $3$.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.41, pp. 523–524)

**Your turn.** Cluster $0$, $1$, $2$ and $10$ by single linkage with absolute difference. Give the three fusion heights and the diameter of $\{0,1,2\}$.

::: {.callout-tip collapse="true" title="Answer"}
The neighbour gaps inside $\{0,1,2\}$ are $1$ and $1$. Those two fusions both occur at height $1$, in either order of the tied pairs. The distance from the finished triple to $10$ is $\min(10,9,8)=8$, so the last height is $8$. The diameter of $\{0,1,2\}$ is $2$, which is larger than the height $1$ at which the triple was built.
:::

## Common misconceptions
Single linkage is not the distance between centroids, and a Euclidean formula is not required. A worked distance table may use Euclidean distance between examination marks; the update itself is the minimum of whatever dissimilarities were supplied.{{cite:dodge2008}} (pp. 84–85) Chaining is not a coding error. It is what the minimum does when intermediate points exist. A balanced dendrogram is not a property the rule promises: extended, trailing clusters, with observations fused one at a time, are the usual picture.{{cite:james_islr2021}} (Ch. 12, §12.4, p. 524)

The monotone-height property does not say that the diameter equals the fusion height. That coincidence belongs to complete linkage. Confusing the two makes a short chain look as tight as its last step.

## Assumptions and limits — A bridge or a single noisy point
Points at $0$, $1$, $2$, $3$ and $10$ have neighbour gaps $1$, $1$, $1$ and $7$. Single linkage builds $\{0,1,2,3\}$ by three fusions at height $1$, then attaches $10$ at height $7$. The diameter of the first four points is $3$, three times the height that assembled them. One intermediate point placed in a gap that used to separate two groups will close that gap for single linkage and join the groups. Complete linkage would still see the far pairs.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525)

A second limit appears as the sample grows. The nearest cross-pair between two fixed regions tends to become smaller merely because more points are available to sit near the boundary. A cut height chosen on a small sample need not keep the same groups apart in a larger sample from the same distribution.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 524–525)

## Connections
[Complete linkage](complete-linkage.qmd) replaces the minimum by a maximum and tracks diameter. [Average linkage](average-linkage.qmd) averages every cross-pair and can change when dissimilarities are rescaled. The three rules are the usual linkages in [hierarchical clustering](hierarchical-clustering.qmd), and the tree is a [dendrogram](dendrogram.qmd). The cophenetic dissimilarity read off that tree obeys the ultrametric inequality, a much tighter constraint than a general distance, which is why the tree should be read as the structure imposed by the linkage rather than as a recovery of every pairwise distance.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.40, pp. 522–525){{cite:james_islr2021}} (Ch. 12, §12.4, pp. 524–525)

## Check yourself
### Minimum versus diameter {#self-check-single-diameter}

On the points $0$, $2$, $3$ and $8$, single linkage finishes by attaching $8$ at height $5$. Is $5$ the diameter of $\{0,2,3,8\}$?

::: {.callout-tip collapse="true" title="Answer"}
No. The diameter is $8-0=8$. The height $5$ is only the nearest distance from $8$ to the cluster $\{0,2,3\}$, namely $8-3$. Single linkage does not record the far pairs.
:::

### A chain of unit gaps {#self-check-single-chain}

Points sit at $0$, $1$, $2$, $3$ and $6$. List the single-linkage fusion heights in order, and compare the height at which $\{0,1,2,3\}$ is completed with the diameter of that set.

::: {.callout-tip collapse="true" title="Answer"}
The neighbour gaps are $1$, $1$, $1$ and $3$. The three gaps of length $1$ fuse first, all at height $1$, and $\{0,1,2,3\}$ is complete at height $1$. Its diameter is $3$. The point at $6$ then joins at height $3$.
:::

## History
Single linkage builds a hierarchical classification from a distance table by aggregating the closest elements and replacing their distances to every other element by the minimum of the two old distances. Complete linkage is the same algorithm with the minimum replaced by a maximum.{{cite:dodge2008}} (pp. 84–85, 102) Later surveys include both rules, warned that the minimum chains, and noted that the minimum between large samples from fixed densities collapses toward zero.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525)
