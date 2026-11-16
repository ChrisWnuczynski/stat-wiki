## Lead context
Complete linkage judges two clusters by their farthest pair, so a merge is cheap only when every cross-pair is close.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525)

## Motivating example
A botanist has five leaf specimens and a table of pairwise shape distances, and wants groups that are tight rather than groups that merely touch. Nearest-neighbour clustering would join two clumps as soon as one pair of leaves sits close together, even if other leaves in those clumps are far apart. Furthest-neighbour clustering refuses that join until the worst cross-pair is also small. The dendrogram then records the diameter of each newly formed group, which is the question the botanist actually asked.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.42 and 14.44, pp. 523–525){{cite:james_islr2021}} (Ch. 12, §12.4, p. 524)

## Intuition — The worst cross-pair sets the height
Single linkage asks whether any cross-pair is close. Complete linkage asks whether every cross-pair is close. If $D_1$ and $D_2$ are clusters and $d$ is the dissimilarity between points, the complete-linkage dissimilarity is the maximum of $d(x,y)$ over $x\in D_1$ and $y\in D_2$. A proposed merge at height $h$ means that no two points, one from each side, differ by more than $h$. The height is therefore the diameter of the union, when diameter means the largest pairwise dissimilarity inside the union. Compact groups are favoured because a long link anywhere in the cross-pairs blocks the merge. The rule uses only the dissimilarities. It does not need coordinates, means, or a Euclidean embedding, so an edit distance between sequences is a legal input.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525){{cite:dodge2008}} (p. 102)

The same maximum is unchanged if every dissimilarity is replaced by a strictly increasing function of itself. Only the order of the pairwise numbers matters. That is a different property from group-average linkage, whose numerical averages can reorder when the scale of $d$ is stretched.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 524–525)

## Definition
Agglomerative clustering begins with each observation as its own cluster. At each step the two clusters with the smallest inter-cluster dissimilarity are fused, and the dissimilarity at which they fuse is the height of that node. Under complete linkage that inter-cluster dissimilarity is
$$
d_C(D_1,D_2)=\max\{d(x,y):x\in D_1,\, y\in D_2\}.
$$
There are $n-1$ fusions for $n$ observations. Cutting the tree at one height returns a partition in which every cluster has diameter at most that height. A different height returns a coarser or finer partition, and the partitions are nested.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 520–525){{cite:james_islr2021}} (Ch. 12, §12.4, pp. 524–525){{cite:dodge2008}} (pp. 84–85, 102)

## Properties — Later merges cannot sit lower
Once the closest pair of current clusters has been fused at height $h$, every remaining complete-linkage distance is at least $h$. The dendrogram of complete linkage therefore has nondecreasing node heights. Inversions, in which a later fusion is drawn below an earlier one, do not arise. Centroid linkage does not share this guarantee.{{cite:james_islr2021}} (Ch. 12, §12.4, pp. 524–525)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let the current clusters be $D_1,\ldots,D_m$ and let $h$ be the smallest complete-linkage distance among them, achieved by $D_a$ and $D_b$. For any other cluster $D_k$,
$$
d_C(D_a\cup D_b,\, D_k)=\max\bigl(d_C(D_a,D_k),\, d_C(D_b,D_k)\bigr).
$$
Each of $d_C(D_a,D_k)$ and $d_C(D_b,D_k)$ is at least $h$, because $h$ was the minimum. The maximum of two numbers that are at least $h$ is at least $h$. Every distance from the new cluster to a cluster that was not merged is therefore at least $h$, and the next fusion height is at least $h$.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.42, pp. 523–524)
:::
:::

The diameter identity is separate from monotonicity. If $D_1$ and $D_2$ fuse at $d_C(D_1,D_2)$, that value is the largest cross-pair. The diameter of the union is the largest of that cross-pair and the two within-cluster diameters. When each of $D_1$ and $D_2$ was itself built by complete linkage, those within-cluster diameters are at most the heights at which $D_1$ and $D_2$ were formed, hence at most $d_C(D_1,D_2)$. The fusion height and the diameter of the union therefore coincide.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.44, pp. 524–525)

## Statistical use — Reading a cut as a diameter bound
A horizontal cut at height $h$ produces clusters whose complete-linkage diameters are at most $h$. That statement is about the dissimilarities that were supplied. It is not a posterior probability that those clusters are the groups which generated the sample, and the construction does not supply one. If the scientific target is a fixed number of groups rather than a diameter bound, the cut can be chosen to yield that number, and nearby cuts should be compared before a label is attached to one of them. When the clusters in the sample are compact and well separated, single, complete, and average linkage often draw similar trees. When they are not, complete linkage keeps diameters small and can place a point nearer to another cluster than to some member of its own.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525){{cite:james_islr2021}} (Ch. 12, §12.4, pp. 524–525)

## Worked example
Place four observations on the line at $0$, $2$, $3$ and $8$, and let $d$ be absolute difference. The six pairwise distances are $2$, $1$, $3$, $8$, $6$ and $5$. The closest pair is $\{2,3\}$ at height $1$. The complete-linkage distance from $\{2,3\}$ to $0$ is $\max(2,3)=3$, and from $\{2,3\}$ to $8$ is $\max(6,5)=6$. The next fusion is therefore $\{0\}$ with $\{2,3\}$ at height $3$. The last fusion joins $8$ at
$$
\max(8-0,\,8-2,\,8-3)=\max(8,6,5)=8.
$$
The node heights are $1$, $3$ and $8$. The final height $8$ is the diameter of $\{0,2,3,8\}$. Single linkage on the same points would make the last fusion at $\min(8,6,5)=5$, because only the nearest cross-pair would count. The two rules agree on the first fusion and disagree on how costly it is to absorb the point at $8$.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.42, pp. 523–524)

**Your turn.** On the same line, cluster $0$, $1$ and $4$ by complete linkage. Report both fusion heights, and say which height equals the diameter of all three points.

::: {.callout-tip collapse="true" title="Answer"}
The closest pair is $\{0,1\}$ at height $1$. The complete-linkage distance from that pair to $4$ is $\max(4-0,4-1)=\max(4,3)=4$. The heights are $1$ and $4$. The diameter of $\{0,1,4\}$ is $4$, which matches the last fusion.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.42 and 14.44, pp. 523–525)
:::

## Common misconceptions
Complete linkage is not the distance between cluster centroids, and it is not the average of the cross-pairs. Those are different extensions of $d$, and they can fuse different pairs at the next step. The rule does not require Euclidean distance: any dissimilarity may be dropped into the maximum. A Euclidean formula in a worked table is one choice of $d$, not part of the definition.{{cite:dodge2008}} (pp. 84–85, 102){{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–524)

A tendency toward compact clusters is not a theorem that the groups are spherical or of equal size. Those shapes are extra assumptions about the sample. Complete linkage also does not estimate a population gap in the way a group-average dissimilarity can: as the sample grows inside two fixed densities, the maximum cross-pair typically runs off to the extremes of the supports, so the complete-linkage height need not settle on a feature of the two densities.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 524–525)

## Assumptions and limits — One distant point sets the diameter
Add a fifth point at $20$ to the worked example and attach it, at any earlier step, to the point at $8$. Every later complete-linkage comparison that involves that enlarged cluster is at least $20-0=20$ once the point at $0$ is still outside, and the diameter of any cluster that contains both $0$ and $20$ is $20$. One remote observation raises the maximum and can postpone a fusion of groups that are otherwise close. The monotone-height property still holds. What fails is the hope that a single remote point will be ignored.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 524–525)

A second limit is geometric rather than about outliers. Two groups can be fused only when all of their cross-pairs are similar, yet a point inside the resulting cluster can still sit closer to a point outside it than to the far side of its own cluster. Small diameter does not imply that the nearest neighbour of every member lies inside the cluster.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 524–525)

Ties need a rule. If two pairs share the same minimum distance, the pair fused first does not change the later complete-linkage distances to untouched points, but the drawing order of the dendrogram does depend on which tied pair is recorded first. The heights do not.{{cite:dodge2008}} (pp. 84–85)

## Connections
[Single linkage](single-linkage.qmd) replaces the maximum by a minimum and can chain distant points through a bridge of neighbours. [Average linkage](average-linkage.qmd) averages the cross-pairs and, unlike the maximum, can change its fusions when dissimilarities are squared. All three are agglomerative rules inside [hierarchical clustering](hierarchical-clustering.qmd), and the picture of the fusions is a [dendrogram](dendrogram.qmd). Ward's criterion instead merges the pair whose union least increases a within-cluster sum of squares, which needs coordinates or an equivalent inner product and is a different objective.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525){{cite:james_islr2021}} (Ch. 12, §12.4, pp. 524–525)

## Check yourself
### Diameter after two fusions {#self-check-complete-heights}

Observations sit at $0$, $2$, $3$ and $8$ with absolute difference as the dissimilarity. Complete linkage has already fused $\{2,3\}$ at height $1$ and then fused $0$ with that pair at height $3$. What is the height of the last fusion, and why does it equal the diameter of the four points?

::: {.callout-tip collapse="true" title="Answer"}
The last height is $\max(8,6,5)=8$. Under complete linkage the fusion height is the largest cross-pair, and the within-cluster diameters already formed are $1$ and then $3$, both smaller than $8$. The diameter of the union is therefore $8$.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.42 and 14.44, pp. 523–525)
:::

### A squared distance cannot reorder the maximum {#self-check-complete-monotone}

The cross-pairs between two clusters have dissimilarities $1$ and $9$. Another candidate pair of clusters has cross-pairs $4$ and $6$. Which pair does complete linkage regard as closer, and does replacing every dissimilarity by its square change that comparison?

::: {.callout-tip collapse="true" title="Answer"}
Complete linkage compares $\max(1,9)=9$ with $\max(4,6)=6$, so the second pair is closer. After squaring, the maxima are $81$ and $36$, and $36$ is still smaller. A strictly increasing transformation preserves the larger of two numbers, so it preserves every complete-linkage comparison.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 524–525)
:::

### An outlier and a bridge {#self-check-complete-outlier}

Points at $0$, $1$, $2$ and $10$ are clustered by complete linkage. The first fusion is $\{0,1\}$ or a tie involving the gap of $1$ between neighbours in $\{0,1,2\}$. Explain why the point at $10$ does not slip into an early fusion, whereas single linkage can attach it only at the end but through a chain whose diameter is already large before that last step.

::: {.callout-tip collapse="true" title="Answer"}
Any cluster that contains a point of $\{0,1,2\}$ and also $10$ has a cross-pair of length at least $8$. Complete linkage will not pay that cost while fusions of height $1$ are still available inside $\{0,1,2\}$. The three close points fuse first, at heights $1$ and then $2$, and $10$ joins at $10$. Single linkage also postpones $10$ until height $8$, but the cluster $\{0,1,2\}$ was built at height $1$ even though its diameter is $2$. The defect complete linkage avoids is that early, large diameter; the cost it accepts is that one remote point fixes the last height.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525)
:::

## History
Dodge's dictionary records complete linkage as the hierarchical rule that takes the distance between the farthest members of two classes, and it records the companion single-link rule that takes the nearest members. The agglomerative algorithm that both rules plug into rebuilds a distance table after each fusion and can be drawn as a dendrogram.{{cite:dodge2008}} (pp. 84–85, 102, 157) Hastie, Tibshirani and Friedman treat the maximum, the minimum and the group average as the three usual extensions of a pairwise dissimilarity, and they separate the compactness that the maximum encourages from the population quantity that a group average estimates.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525)
