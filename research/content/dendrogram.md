## Lead context
A dendrogram draws each merge of a hierarchical clustering at a height equal to the dissimilarity of the two groups that merged.

## Motivating example
Points at $0$, $1$, $4$ and $10$ are joined by single linkage. The merge heights are $1$, $3$ and $6$. A horizontal cut at height $2$ leaves $\{0,1\}$, $\{4\}$ and $\{10\}$.

## Intuition — Height is the dissimilarity of that merge, and a horizontal cut is a partition
Agglomerative clustering starts with one point in each group and joins groups until one group remains. If the merge dissimilarities increase, the joins can be drawn as a tree whose leaves sit at height zero and whose internal nodes sit at the dissimilarity of the join. A horizontal line at one height crosses a set of vertical branches. The groups hanging from those branches are the partition obtained by stopping when the next merge would exceed that height. Flipping the left and right children of a node changes the picture and not the merges.{{cite:hastie_esl2009}} (p. 521)

## Definition — Leaves, knots, and a scale
The leaves are the observations. Each internal knot is a cluster formed by a merge, and the height of the knot is the linkage dissimilarity of that merge. Knots stand for groups, branches for the associations made at each step, and a scale for the distances at which the aggregations took place. The heights belong to the linkage and to the sample. They are not posterior probabilities that those clusters generated the data.{{cite:dodge2008}} (p. 157){{cite:hastie_esl2009}} (p. 521)

## Worked example — Single linkage of four points on a line
Place points at $0$, $1$, $4$ and $10$. Single linkage uses the minimum pairwise distance between clusters. The closest pair is $\{0,1\}$, at distance $1$. The distance from $\{0,1\}$ to $4$ is $\min(4-0,4-1)=3$. The distance from $\{0,1,4\}$ to $10$ is $\min(10-0,10-1,10-4)=6$. The dendrogram therefore has merge heights $1$, $3$ and $6$.

A cut at height $2$ falls after the first merge and before the second, so the partition is $\{0,1\}$, $\{4\}$, $\{10\}$. A cut at height $4$ also includes the merge at height $3$, so the partition is $\{0,1,4\}$, $\{10\}$. The same numbers in the opposite order of children still record those three merges.

**Your turn.** Add a fifth point at $11$, and keep single linkage. At what height does $11$ join, and what partition does a cut at height $4$ give?

::: {.callout-tip collapse="true" title="Answer"}
The distance from $11$ to $10$ is $1$, so $\{10,11\}$ merges at height $1$, alongside $\{0,1\}$. The cluster $\{0,1,4\}$ is still $6$ from $\{10,11\}$, because the nearest pair across that cut is $4$ and $10$. A cut at height $4$ gives $\{0,1,4\}$ and $\{10,11\}$.
:::

## Connections — Linkage chooses the height, and the tree is not a model
[Single linkage](single-linkage.qmd) uses the minimum distance, which is what produced heights $1$, $3$ and $6$. Complete linkage would use the maximum instead, so the height at which $\{0,1\}$ joins $4$ would be $4-0=4$, not $3$. [Average linkage](average-linkage.qmd) uses a mean of the pairwise distances. Different linkages on the same points can produce different trees.{{cite:hastie_esl2009}} (p. 521){{cite:dodge2008}} (p. 157)

## Check yourself
On the four-point dendrogram, how many clusters does a cut at height $0.5$ return, and how many does a cut at height $7$ return?

::: {.callout-tip collapse="true" title="Answer"}
Height $0.5$ is below every merge, so there are four clusters, the four points. Height $7$ is above the last merge at $6$, so there is one cluster.
:::

Why is the single-linkage distance from $\{0,1\}$ to $4$ equal to $3$ rather than $4$?

::: {.callout-tip collapse="true" title="Answer"}
Single linkage takes the closest pair across the two groups. That pair is $1$ and $4$, at distance $3$. The distance $4$ is the complete-linkage height, using $0$ and $4$.
:::
