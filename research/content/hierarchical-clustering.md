## Lead context
Hierarchical clustering builds a nested sequence of partitions, from single observations up to one cluster that contains every observation.

## Motivating example
Four clinics at $0$, $1$, $10$, and $12$ can be merged by average linkage. First $\{0\}$ joins $\{1\}$ at distance $1$. Then $\{10\}$ joins $\{12\}$ at distance $2$. Then the two pairs join at distance $10.5$. The result is not one partition. It is the whole nest: four singletons, then three clusters, then two, then one. A cut between heights $2$ and $10.5$ keeps the two pairs. A cut above $10.5$ returns a single cluster.{{cite:hastie_esl2009}} (§14.3, pp. 520–524)

## Intuition
Agglomerative clustering starts at the bottom, with each observation alone, and merges the closest pair of clusters at each step. Divisive clustering starts at the top and splits. Both produce $N-1$ levels for $N$ observations. A dendrogram draws each merge at a height equal to the dissimilarity at which it happened, with the observations at height zero. Flipping the left and right children of a node does not change the merges. It only changes the order of the leaves.{{cite:hastie_esl2009}} (§14.3, pp. 520–522){{cite:dodge2008}} (p. 157)

## Definition
An agglomerative step replaces the closest two clusters by their union and recomputes distances from that union to the clusters that remain. Single, complete, and average linkage are three definitions of "closest". The hierarchy is the sequence of partitions those steps produce. The cophenetic dissimilarity of two observations is the height at which they first sit in the same cluster.{{cite:hastie_esl2009}} (§14.3, pp. 522–523)

## Interpretation — Heights and ties
For the four clinics under average linkage the cophenetic dissimilarity of $0$ and $1$ is $1$, of $10$ and $12$ is $2$, and of every cross pair is $10.5$. There are $4\cdot 3/2=6$ pairs and only three distinct cophenetic values. In any dendrogram at most $N-1$ of the $N(N-1)/2$ pairwise cophenetic values can be distinct, because there are only $N-1$ merges. The four cross pairs are tied at the last merge.{{cite:hastie_esl2009}} (§14.3, p. 522)

Those tied values satisfy the ultrametric inequality. For observations $i$, $i'$, and $k$, the cophenetic dissimilarity obeys $C_{ii'}\le\max(C_{ik},C_{i'k})$. Here $C_{0,10}=C_{1,10}=10.5$, and $C_{0,1}=1$ is smaller than that common value. A Euclidean distance need not obey the same inequality. The dendrogram has forced the data into an ultrametric, whether or not the original distances were one.

## Properties
The clinic heights and the ultrametric inequality on this tree are immediate from the merges.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Average linkage on $\{0,1\}$ and $\{10,12\}$ uses the four gaps $10$, $12$, $9$, and $11$, whose mean is $10.5$. The earlier merges are the unique closest pairs, at distances $1$ and $2$, and those pairs do not interact. So the cophenetic values are as listed.

For any three leaves, two of them join at or before the height where the third joins their group. The two that joined earlier have the smaller cophenetic value, and each of them meets the third at the later height. Hence the smaller value is at most the maximum of the other two, which in this tree are equal.{{cite:hastie_esl2009}} (§14.3, p. 522)
:::
:::

## Statistical use — Choosing a cut
The hierarchy does not name a number of clusters. A cut does. For these clinics, every cut in $(2,10.5)$ returns the same two clusters, under average linkage. Under complete linkage the last merge is at $12$ rather than $10.5$, so the interval of cuts that preserve the two pairs is $(2,12)$. Under single linkage the last merge is at $9$, and the interval shrinks to $(2,9)$. Reporting "two clusters" without the linkage and the cut height hides which of these intervals was used.{{cite:hastie_esl2009}} (§14.3, pp. 520–524)

## Worked example
Positions $0,1,10,12$, absolute distance, average linkage.

Merge $0$ with $1$ at height $1$. Merge $10$ with $12$ at height $2$. Cross gaps $10,12,9,11$ average to $10.5$, so the last height is $10.5$.

The six cophenetic values are $1$, $2$, and four copies of $10.5$. Their average is $(1+2+4\cdot 10.5)/6=45/6=7.5$, and the six original distances average $(1+10+12+9+11+2)/6=45/6=7.5$ as well. Under average linkage this equality holds for any $N\ge 2$ observations with finite pairwise dissimilarities: merging clusters $A$ and $B$ assigns their block mean to each of the $|A|\,|B|$ cross pairs, preserving the block sum, and every unordered pair of distinct observations enters exactly one such block across the $N-1$ merges, so the total and the mean are preserved. Single and complete linkage need not preserve the pairwise mean, though they can: for three observations with pairwise distances $1$, $2$, and $2$, single, complete, and average linkage all give cophenetic values $1$, $2$, and $2$, with the original mean $5/3$. On the four clinics, single linkage writes $9$ for each cross pair, and the average of the cophenetic values becomes $(1+2+4\cdot 9)/6=39/6=6.5$, while the original distances still average $7.5$.

**Your turn.** Under complete linkage the last height is $12$. What is the average of the six cophenetic values?

::: {.callout-tip collapse="true" title="Answer"}
The values are $1$, $2$, and four copies of $12$. The average is $(1+2+48)/6=51/6=8.5$.
:::

## Common misconceptions
A dendrogram is not evidence that the data are nested. The algorithm imposes a nested sequence on every dissimilarity matrix. A cophenetic correlation, between the original pairwise dissimilarities and the cophenetic ones, is one check of how hard that imposition was. It is not a proof of a biological or administrative hierarchy.{{cite:hastie_esl2009}} (§14.3, p. 522)

The leaf order is not part of the clustering. Swapping the two children of a node preserves every merge and changes the picture. Two dendrograms that look different may record the same partitions.

Cutting at the largest gap in merge height is a heuristic. For the clinics the gap from $2$ to $10.5$ is large, and the two-pair cut is easy to see. A chain of nearly equal gaps has no such cut, and the heuristic then invents a number of clusters the heights do not support.

## Assumptions and limits — Ultrametric data, and data that are not
If the original dissimilarities already satisfy the ultrametric inequality, a single-linkage dendrogram can reproduce them. Ordinary Euclidean distances on the line do not. The distance $d(0,12)=12$ and the distances $d(0,1)=1$, $d(1,12)=11$ satisfy the triangle inequality, and $12\le\max(1,11)$ is false. The cophenetic version replaces $12$ by the merge height of the whole set, which does satisfy the ultrametric inequality, and in doing so it changes the number.

Divisive clustering is not the agglomerative sequence read backwards unless the split criterion is built to invert the merge criterion. Starting from the top and splitting by a different rule can produce a different nest.

Missing pairs remove terms from the group distance. The hierarchy then depends on which pairs were observed, not only on the linkage.

## Connections
[Single, complete, and average linkage](single-complete-and-average-linkage.qmd) are the three group distances used in the clinic tree. A [dendrogram](dendrogram.qmd) is the drawing of the heights. Agglomerative and divisive clustering are the two directions through the same nest. The cophenetic dissimilarity is the original distance as the tree remembers it.

## History
Agglomerative clustering repeatedly replaces the closest pair by a single element and rebuilds the distance table after each merge. A dendrogram is the tree of those aggregations drawn against a distance scale.{{cite:dodge2008}} (pp. 84 and 157) Hastie, Tibshirani and Friedman emphasise that the algorithm produces $N-1$ nested partitions whether or not the data are nested, and that the cophenetic dissimilarities obey an ultrametric inequality the original distances need not obey.{{cite:hastie_esl2009}} (§14.3, pp. 520–522)
