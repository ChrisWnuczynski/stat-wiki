## Motivating example
Suppose five measurements form two visually separated groups, one with two points and one with three. A clustering algorithm needs a numerical way to judge whether points assigned the same label are close. Within-cluster scatter sums their squared separations. Its value helps compare candidate partitions, but the exact definition matters: a pairwise sum gives larger clusters extra weight compared with the ordinary K-means sum of squared distances to centres.

## Intuition — Why pairwise distances encode scatter
Every pair of points in a cluster contributes a squared distance. The factor one half in the definition removes double counting of the ordered pairs. Squared distance makes widely separated members costly, so moving a remote observation into an otherwise compact cluster can change the score sharply. Rewriting pairwise distances around the cluster mean reveals why the mean appears, but it also reveals a factor equal to the cluster size. That factor is easy to miss when comparing formulas called “within-cluster sum of squares.”

A partition with low scatter describes compact groups under the chosen coordinate scale. It does not establish that the groups correspond to natural populations. Changing units or adding a noisy feature changes the distances, and increasing the number of clusters usually lowers an unpenalized scatter score. A separate decision rule is needed for the number of clusters and for scientific interpretation.

## Definition
For a partition $C$ into nonempty clusters, define pairwise scatter $W(C)=\tfrac12\sum_k\sum_{C(i)=C(l)=k}\|x_i-x_l\|^2$. If cluster $k$ has $N_k$ points and mean $\bar x_k$, then $W(C)=\sum_kN_k\sum_{C(i)=k}\|x_i-\bar x_k\|^2$. The usual K-means objective instead uses $\widetilde W(C)=\sum_k\sum_{C(i)=k}\|x_i-\bar x_k\|^2$. The two expressions coincide only under special cluster-size conditions; the first weights each cluster's centre-based scatter by its size.

The features must be measured on a meaningful common scale for Euclidean distances to have an interpretable effect. Multiplying one coordinate by ten multiplies that coordinate's squared-distance contribution by one hundred. Standardizing can be appropriate, but it expresses a choice that each feature's empirical scale should count comparably.

## Properties
The cluster mean minimizes the sum of squared distances to a single proposed centre. The pairwise identity follows by centring each point and using the fact that the centered deviations sum to zero. Refining a partition can only remove nonnegative within-cluster pairs, so the *globally minimized* pairwise scatter cannot increase when more clusters are allowed. The same monotonicity holds for globally optimized ordinary K-means scatter. Neither monotonicity makes the raw score a selector of the best $K$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For one cluster with $N$ points and mean $\bar x$, expansion gives $\sum_i\|x_i-m\|^2=\sum_i\|x_i-\bar x\|^2+N\|m-\bar x\|^2$, since $\sum_i(x_i-\bar x)=0$; the mean is therefore a minimizer. Also $\sum_{i,l}\|x_i-x_l\|^2=\sum_{i,l}\|(x_i-\bar x)-(x_l-\bar x)\|^2=2N\sum_i\|x_i-\bar x\|^2$, because the cross-term sums to zero. Halving and summing over clusters proves the pairwise identity. Splitting a cluster deletes cross-subcluster pairs from the nonnegative pairwise sum, proving monotonicity at the optimum as $K$ grows. The ordinary centre-based objective can retain old centres after refinement and then reoptimize, so its global minimum also cannot increase. Finally, the number of onto maps from $n$ labelled observations to $K$ labelled nonempty groups is $\sum_{j=0}^K(-1)^j\binom Kj(K-j)^n$ by inclusion–exclusion. Dividing by $K!$ gives the stated Stirling count for unlabelled partitions.
:::
:::

## Interpretation
The pairwise and centre-based criteria give different weights to unequal clusters. For example, cluster A with points $0,2$ has mean $1$ and centre-based scatter $2$, hence pairwise scatter $2(2)=4$. Cluster B with $10,11,12$ has mean $11$ and centre-based scatter $2$, hence pairwise scatter $3(2)=6$. The two-cluster totals are $\widetilde W=4$ and $W=10$. Equal centre-based scatter in the two clusters did not give equal contributions to $W$.

Lloyd's nearest-centre reassignment is guaranteed to improve or preserve its *unweighted* objective, not the pairwise weighted one. A concrete example has clusters $(0,1,3)$ and $(2,7)$. Point $3$ is closer to the second current centre $4.5$ than to the first centre $4/3$, so reassignment followed by re-centring gives $(0,1)$ and $(2,3,7)$. Ordinary centre-based scatter falls from about $17.17$ to $14.5$, yet pairwise scatter rises from $39$ to $43$. The changing cluster sizes account for the difference.

## Statistical use
Name the objective before comparing algorithms or software output. If software reports `tot.withinss`, it usually refers to the unweighted distances to assigned centres, whereas the displayed $W(C)$ is a size-weighted pairwise criterion. Check whether a score is computed from the same feature scaling and the same number of groups. Multiple starts can reduce poor local solutions, but a low local score is not a proof of the global optimum. For choosing $K$, inspect stability or compare the observed decrease with a reference or penalty rather than selecting the largest permitted $K$ solely because its raw scatter is smallest.

## Worked example
Take the two one-dimensional clusters $A=\{0,2\}$ and $B=\{10,11,12\}$. The means are $1$ and $11$. The ordinary K-means sum is $(0-1)^2+(2-1)^2+(10-11)^2+(11-11)^2+(12-11)^2=2+2=4$. Pairwise squared distances within A sum to $4$ over its one unordered pair. Within B they sum to $1+4+1=6$, so $W=4+6=10$. Multiplying each cluster's centre-based scatter by its size gives the same result: $2(2)+3(2)=10$. The score is in squared measurement units and depends on this particular partition and scaling.

**Your turn.** For $A=\{0,4\}$ and $B=\{10,11\}$, calculate each mean, the ordinary centre-based sum of squares, and the pairwise $W$. Explain why the two totals differ.

::: {.callout-tip collapse="true" title="Answer"}
The means are $2$ and $10.5$. Cluster A has centre-based scatter $4+4=8$ and pairwise scatter $(4-0)^2=16$. Cluster B has centre-based scatter $0.25+0.25=0.5$ and pairwise scatter $(11-10)^2=1$. Thus $\widetilde W=8.5$ and $W=17$. Here both clusters have size two, so $W=2\widetilde W$; the formula still differs by the size factor.
:::

## Common misconceptions
The pairwise $W$ is not the unweighted K-means objective when cluster sizes differ. A smaller training scatter does not demonstrate a more meaningful $K$, since singleton clusters eventually drive it to zero. A cluster label is not a known class label, even if the numerical groups appear separated. And a small Euclidean scatter does not survive an arbitrary rescaling of one coordinate.

## Assumptions and limits
The score can prefer compact spherical-looking groups when the actual population consists of elongated bands or nested rings. A single extreme observation can dominate squared distances and alter centres. Multiplying one variable measured in metres by $100$ to express centimetres multiplies its squared contribution by $10{,}000$ unless the data are rescaled consistently. The Lloyd counterexample shows that even the direction of one algorithmic step differs between the pairwise and ordinary objectives. These are geometric, robustness and optimization limits, not one interchangeable problem.

## Connections
[K-means criterion](k-means-criterion.qmd) uses the unweighted centre-based score for algorithmic updates. [Lloyd's K-means algorithm](lloyd-s-k-means-algorithm.qmd) alternates assignment and centre updates. [Choosing K with the gap statistic](choosing-k-the-gap-statistic.qmd) compares observed fit with a reference, while [Ward's method](ward-s-method.qmd) uses within-group sums in hierarchical clustering. Dodge's cluster-analysis entry groups together methods that partition observations by measured similarity.{{cite:dodge2008}} (p. 83, “Cluster Analysis”)

## History
Dodge's account of cluster analysis cites Tryon's 1939 *Cluster Analysis* among earlier works and describes grouping objects by measured association.{{cite:dodge2008}} (p. 83, “Cluster Analysis”) The pairwise scatter here gives one precise geometric definition of similarity within a proposed group; the weighting choice is part of that definition.
