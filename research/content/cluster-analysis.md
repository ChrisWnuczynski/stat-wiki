

## Lead context

A file of measurements often looks smoother once the rows are gathered into a few bundles. Cluster analysis is the set of methods that make those bundles from the measurements alone, so that rows in one bundle are closer to each other than to rows placed elsewhere.{{cite:hastie_esl2009}} (pp. 501–503) {{cite:james_islr2021}} (Ch. 12, pp. 514–515)

## Motivating example

Four points in the plane are enough to see the choice. Place $A$ at $(0,0)$, $B$ at $(1,0)$, $C$ at $(5,0)$ and $D$ at $(6,1)$. Nothing in the file says which points share a label. A grouping that first joins $A$ with $B$, and $C$ with $D$, is using distance. A grouping that cuts the plane at $x=3$ is using a different summary of the same four points. Cluster analysis is the family of such groupings, not any one cut.{{cite:dodge2008}} (pp. 83–84) {{cite:james_islr2021}} (Ch. 12, p. 515)

## Definition

Cluster analysis, also called data segmentation, groups objects so that those inside a cluster are more closely related than objects assigned to different clusters. An object may be described by its measurements or by its relations to the other objects. A second goal is a hierarchy: clusters themselves are grouped so that, at each level, members of a branch are more similar than members of different branches.{{cite:hastie_esl2009}} (pp. 501–502)

The same idea can be stated with a distance. Clustering partitions a data set into subsets so that association is strong inside a subset and weak between subsets, for a distance or similarity that has been defined. The two organisations named there are partitional clustering and hierarchical clustering.{{cite:dodge2008}} (p. 83)

K-means partitions the observations into a pre-specified number of non-overlapping clusters. Hierarchical clustering does not fix that number in advance. It returns a tree, a dendrogram, from which every partition from one cluster up to one cluster per point can be read. One may cluster the observations, or transpose the table and cluster the features.{{cite:james_islr2021}} (Ch. 12, pp. 515–516)

The target of K-means is a small within-cluster variation. If $C_1,\ldots,C_K$ are the index sets, they cover $\{1,\ldots,n\}$ and they do not overlap, and the fit minimises $\sum_{k=1}^K W(C_k)$ for a within-cluster measure $W$.{{cite:james_islr2021}} (Ch. 12, pp. 515–516, (12.15))

Closeness has to be supplied. Euclidean distance is one choice; a correlation between profiles is another. Once closeness is fixed, two organisations are common. One chooses a number of groups in advance and partitions the points. The other joins groups step by step and keeps every intermediate partition. The first is [K-means](lloyd-s-k-means-algorithm.qmd). The second is [hierarchical clustering](hierarchical-clustering.qmd). They answer different questions about the same distances.{{cite:james_islr2021}} (Ch. 12, p. 515) {{cite:hastie_esl2009}} (pp. 502–503)

K-means alternates two steps from an initial guess at the centres. Each point is given to the nearest centre in Euclidean distance. Each centre is then replaced by the coordinate-wise average of the points just given to it. The steps repeat until the assignment stops changing. The procedure is top-down from a chosen $K$. Agglomerative hierarchical clustering is bottom-up: it starts from separate points and joins groups.{{cite:hastie_esl2009}} (pp. 502–503)

Single linkage, one hierarchical rule, measures the distance between two groups by the minimum of the pairwise distances. Complete linkage uses the maximum. The only change between those two rules is that minimum. For the four points above, the Euclidean distances include $d(A,B)=1$, $d(C,D)=\sqrt{2}$ and $d(B,C)=4$. Single linkage therefore joins $A$ with $B$ at distance $1$, joins $C$ with $D$ at distance $\sqrt{2}$, and joins the two pairs at distance $4$.{{cite:dodge2008}} (pp. 84–85)

With those same pairs treated as K-means clusters, the centre of $\{A,B\}$ is $(1/2,0)$ and the within-cluster sum of squares is $1/2$. The centre of $\{C,D\}$ is $(11/2,1/2)$ and the within-cluster sum of squares is $1$. The total is $3/2$. That number is the [K-means criterion](k-means-criterion.qmd) for this one partition. Another partition can have a smaller value, and a run of the algorithm from a different start can find it.{{cite:james_islr2021}} (Ch. 12, pp. 515–517)

Use a partition when the number of groups is part of the question: market segments, a small number of unknown subtypes, a compression of a sample into $K$ centres. Use a hierarchy when the question is which groups nest inside which, and when cutting the tree at several heights is useful. The marketing table with income, occupation, and distance to a city, and no record of who buys the product, is the usual setting: the groups are a proposal about the customers, not a forecast of a purchase.{{cite:james_islr2021}} (Ch. 12, pp. 514–515; Ch. 2, pp. 26–28)

The distance is not a detail to be left at the default. Standardising a feature that was recorded in tiny units, or leaving it raw, changes which points look close. Subject-matter reasons for the distance play the role that a loss function plays in a prediction problem.{{cite:hastie_esl2009}} (p. 502)

[Principal component directions](principal-component-directions.qmd) are a different reduction of the same table. They look for a few directions of large variation. Clustering looks for homogeneous subgroups. A plot of the first two component scores is often where a clustering is inspected, and it is not itself the clustering.{{cite:james_islr2021}} (Ch. 12, pp. 497–498, 514)

Cluster analysis is not a synonym for hierarchical clustering alone. A partition into $K$ groups, with the within-cluster sum of squares as the score, is the other standard member of the family. The tree and the partition use the same distances and return different objects.{{cite:james_islr2021}} (Ch. 12, p. 515) {{cite:dodge2008}} (p. 83)

The colours on a cluster plot are not labels that were hidden in the file. They are the output of the algorithm. In the simulated three-group picture, two of the groups overlap, and the word segmentation is the more honest description of what the cut achieved.{{cite:hastie_esl2009}} (pp. 502–503)

A smaller within-cluster sum of squares at a larger $K$ does not mean that the larger $K$ is the right description. More centres can sit closer to the points even when the extra centre has split a single cloud. Cross-validation of a prediction error does not choose $K$, because there is no response to predict.{{cite:hastie_esl2009}} (pp. 519–520) {{cite:james_islr2021}} (Ch. 12, pp. 516–519)

The methods assume a distance that represents the similarity one cares about. If that distance is wrong, a clean partition is a clean answer to the wrong question. K-means, in the form that alternates nearest centres and averages, uses Euclidean distance and a fixed $K$, and it stops at a local minimum of the criterion. A second start can return a criterion value different from the $3/2$ of this one partition.{{cite:hastie_esl2009}} (pp. 502–503) {{cite:james_islr2021}} (Ch. 12, pp. 515–517)

Hierarchical clustering will draw a tree whether or not the points have a nested structure. Single linkage, because it uses the nearest pair, can chain together points that are only neighbours of neighbours. Complete linkage refuses that chain and can refuse a perfectly reasonable elongated group.{{cite:dodge2008}} (pp. 84–85)

There is no direct analogue of a test-set error. Agreement with a label that was never shown to the algorithm is a later check, not the criterion that was minimised.{{cite:hastie_esl2009}} (pp. 486–487)

## Worked example

The six Euclidean distances among $A(0,0)$, $B(1,0)$, $C(5,0)$ and $D(6,1)$ that matter for the first joins are $d(A,B)=1$, $d(C,D)=\sqrt{(6-5)^2+(1-0)^2}=\sqrt{2}$, and $d(B,C)=4$. The other cross distances are $5$, $\sqrt{26}$ and $\sqrt{37}$, all larger than $4$. Single linkage joins $A$ to $B$ at distance $1$ and $C$ to $D$ at distance $\sqrt{2}$. The distance from $\{A,B\}$ to $\{C,D\}$ is the minimum of the four cross distances, which is $4$.

For the squared Euclidean criterion, the centre of $\{A,B\}$ is $(1/2, 0)$. The two squared distances to it are $(1/2)^2+(0)^2=1/4$ each, and they sum to $1/2$. The centre of $\{C,D\}$ is $(11/2, 1/2)$. Each point contributes $(1/2)^2+(1/2)^2=1/2$, and the pair sums to $1$. The partition therefore has within-cluster sum of squares $1/2+1=3/2$.

**Your turn.** Under single linkage, what is the distance between the groups $\{A,B\}$ and $\{C,D\}$?

::: {.callout-tip collapse="true" title="Answer"}
The distance is $4$, the gap from $B$ to $C$. Every other cross distance is larger.
:::

## Connections

The two algorithms to read next are [hierarchical clustering](hierarchical-clustering.qmd) and [Lloyd's K-means algorithm](lloyd-s-k-means-algorithm.qmd), together with the [K-means criterion](k-means-criterion.qmd). Cluster analysis is the grouping part of [unsupervised learning](unsupervised-learning.qmd). It is not [classification](classification.qmd): classification predicts a label that was observed on the training cases. A [principal component](principal-component-directions.qmd) plot is a map on which clusters are often drawn, and the map optimises variance rather than a within-cluster sum of squares.{{cite:james_islr2021}} (Ch. 12, pp. 495–498, 514–515) {{cite:hastie_esl2009}} (pp. 485–487, 501–503)

## History

Grouping similar objects runs from ancient typologies through Adanson in the eighteenth century to the clustering methods of Zubin, Tryon, and Thorndike, and the later growth of those methods follows the computer. Single linkage and complete linkage are the hierarchical rules written as updates to a distance table.{{cite:dodge2008}} (pp. 82–85)

The modern statistical development puts the same split, partition versus hierarchy, under unsupervised learning, with K-means as the alternating assignment of points to centres and hierarchical clustering as the tree. The gap statistic is one later proposal for reading the number of groups off the drop in the within-cluster criterion, by comparing that drop with the drop for points distributed uniformly in a rectangle around the data.{{cite:hastie_esl2009}} (pp. 501–503, 519–520) {{cite:james_islr2021}} (Ch. 12, pp. 514–515)
