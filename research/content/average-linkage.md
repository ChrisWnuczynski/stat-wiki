## Lead context
Average linkage measures the gap between two clusters by the mean of every cross-pair, not by the nearest pair or the farthest pair.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.43, p. 523)

## Motivating example
On the line with absolute difference, the points $0$, $2$, $3$ and $8$ first fuse $\{2,3\}$ at distance $1$. The average distance from $\{2,3\}$ to $0$ is $(2+3)/2=2.5$, and from $\{2,3\}$ to $8$ is $(6+5)/2=5.5$. The next fusion attaches $0$ at height $2.5$. The last fusion has three cross-distances $8$, $6$ and $5$, with mean $19/3\approx 6.333$. Single linkage finishes at $5$ and complete linkage at $8$. The average sits between them on this last step, and it is not the average of $5$ and $8$.

## Intuition — Every cross-pair casts a vote
If $D_1$ and $D_2$ are clusters, the group-average dissimilarity is the arithmetic mean of $d(x,y)$ over $x\in D_1$ and $y\in D_2$. A single close pair does not decide the comparison, and a single far pair does not either. The denominator is the product of the two cardinalities, so a repeated point is counted as many times as it occurs. The rule does not need the points to have coordinates. It needs the dissimilarities. Replacing those dissimilarities by their squares can change which pair of clusters is closer, because an average does not preserve order under a strictly increasing transformation. The minimum and the maximum do.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525){{cite:james_islr2021}} (Ch. 12, §12.4, p. 524)

## Definition
In agglomerative clustering the group-average linkage is
$$
d_A(D_1,D_2)=\frac{1}{|D_1|\,|D_2|}\sum_{x\in D_1}\sum_{y\in D_2} d(x,y).
$$
At each step the two clusters with the smallest $d_A$ are fused. This is not the distance between the two centroids. Centroid linkage can draw a later fusion below an earlier one. Group-average linkage does not.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.43, pp. 523–525){{cite:james_islr2021}} (Ch. 12, §12.4, p. 524)

## Properties — The next average cannot undercut the last height
If every current inter-cluster distance is at least $h$, the average linkage distance from a newly fused cluster to any other cluster is also at least $h$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Suppose $D_a$ and $D_b$ fuse at height $h$, the minimum group-average distance among the current clusters. For any other cluster $D_k$, both $d_A(D_a,D_k)$ and $d_A(D_b,D_k)$ are at least $h$. The cross-pairs from $D_a\cup D_b$ to $D_k$ are the disjoint union of the cross-pairs from $D_a$ and from $D_b$. Their average is the corresponding weighted average of $d_A(D_a,D_k)$ and $d_A(D_b,D_k)$, with weights proportional to $|D_a|$ and $|D_b|$. A weighted average of two numbers that are at least $h$ is at least $h$. The next fusion height is therefore at least $h$.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, eq. 14.43, p. 523)
:::
:::

## Worked example

Squaring the dissimilarities can reorder a comparison. Cross-distances $1$ and $5$ have mean $3$. Cross-distances $16/5$ and $16/5$ have mean $3.2$. The first pair of clusters is closer on the raw scale. After squaring, the means are $(1+25)/2=13$ and $(256/25)=10.24$. The second pair is now closer. Complete linkage would have compared $\max(1,5)=5$ with $\max(16/5,16/5)=3.2$ before squaring and $\max(1,25)=25$ with $\max(256/25,256/25)=10.24$ after, and the second pair would have stayed closer.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 524–525)

**Your turn.** Clusters $\{0,2\}$ and $\{6,8\}$ on the line have cross-distances $6$, $8$, $4$ and $6$. Find the average-linkage distance, and the single-linkage and complete-linkage distances of the same pair.

::: {.callout-tip collapse="true" title="Answer"}
The average is $(6+8+4+6)/4=6$. The minimum is $4$ and the maximum is $8$. The average is the middle value on this particular set of four numbers, not a general identity.
:::

## Connections
[Single linkage](single-linkage.qmd) uses the nearest cross-pair and can chain. [Complete linkage](complete-linkage.qmd) uses the farthest cross-pair and tracks diameter. Average linkage is the compromise that depends on the numerical scale of $d$. All three are options in [hierarchical clustering](hierarchical-clustering.qmd), and the picture of the fusions is a [dendrogram](dendrogram.qmd). As the clusters grow like samples from two fixed densities, the group average estimates the expected dissimilarity between independent draws from those densities. The single-linkage height collapses toward zero and the complete-linkage height runs off to the extremes of the supports, so those two heights are not estimating that same population contrast.{{cite:hastie_esl2009}} (Ch. 14, §14.3.12, pp. 523–525){{cite:james_islr2021}} (Ch. 12, §12.4, p. 524)

