## Motivating example
A nearest-neighbour search based on height and income can be dominated by whichever coordinate uses larger numerical units. Ranking each coordinate replaces spacing with order. The procedure then regards movement across a given number of sample ranks as comparable across coordinates. This solves a particular invariance problem, but it deliberately discards information about how far apart adjacent values are. Coordinate-wise rank metrics are a documented alternative to Euclidean distances.{{cite:biau_devroye2015}} (pp. 98–99, Rem. 8.2)

## Definition — Rank the query and training points together
Fix a query $x$ and training points $x_1,\ldots,x_n$ in $p$ dimensions. In each coordinate, rank the query together with all training values. With no coordinate ties, let $r_j$ be the query's rank and $r_{ij}$ the rank of training point $i$. The maximum-coordinate rank distance is
$$\rho(x,x_i)=\max_{1\le j\le p}|r_{ij}-r_j|.$$
Other choices use an $\ell_q$ norm of the vector of rank differences. The construction depends on the comparison sample; its numerical distances need not stay unchanged after new training observations enter. Ties require an explicitly stated convention such as midranks.{{cite:biau_devroye2015}} (pp. 98–99, Rem. 8.2)

## Properties — Monotone transformations preserve the comparison
A strictly increasing transformation of one coordinate preserves its rank ordering. A strictly decreasing transformation reverses the ordering, taking each untied rank $r$ to $n+2-r$. Absolute pairwise rank differences are unchanged in either case. Taking their maximum therefore preserves $\rho$. This is an elementary consequence of order and absolute differences. Ranks likewise underlie rank-based comparisons that do not use the numerical spacing of observations.{{cite:dodge2008}} (p. 502, Spearman rank correlation); {{cite:biau_devroye2015}} (pp. 98–99, Rem. 8.2)

For a single fixed pooled collection, maximum coordinate distance is symmetric, nonnegative and obeys a triangle inequality. For example, for each coordinate $|r_{ij}-r_{kj}|\le |r_{ij}-r_{lj}|+|r_{lj}-r_{kj}|$; the maximum is bounded by the sum of the two maxima. If observations have the same rank vector, their distance is zero. With midranks, different recorded units that have identical coordinate values cannot be distinguished. A query-specific ranking rule should not be assumed to define one fixed metric across every future comparison without specifying which pooled collection is used.{{cite:biau_devroye2015}} (pp. 98–99, Rem. 8.2, coordinate-rank construction)

## Worked example — Three possible neighbours
Use training points $(1,10)$, $(2,0)$ and $(4,5)$, and query $(3,7)$. The query has rank three on both coordinates. The training rank vectors are $(1,4)$, $(2,1)$ and $(4,2)$. Their absolute differences from the query are $(2,1)$, $(1,2)$ and $(1,1)$, giving maximum distances $2,2,1$. The third point is therefore the unique nearest neighbour under this distance.

Changing income from dollars to thousands of dollars leaves those ranks unchanged. So does replacing each positive income by its logarithm. This invariance does not mean that multiplying a coordinate by a constant cannot affect an ordinary Euclidean neighbour. It means that the rank calculation has chosen not to use that spacing.

**Your turn.** Use the sum, rather than the maximum, of the coordinate rank gaps. What are the distances for the same three points?

::: {.callout-tip collapse="true" title="Answer"}
The distances are $3,3,2$. The third point is still the unique nearest neighbour in this example.
:::

## Statistical use — Fit transformations within the training data
A prediction analysis must specify how a future value is ranked relative to training values, including values outside the observed range and ties. Validation observations should not be used to learn an empirical transformation that the deployed procedure would not have available. A rank transformation can reduce sensitivity to units and extreme spacing, but can also erase a scientifically meaningful magnitude difference. The relevant invariance should be chosen from the intended comparison.{{cite:biau_devroye2015}} (pp. 98–99, Rem. 8.2)

## Assumptions and limits — A distance does not prove consistency
Nearest-neighbour consistency also requires assumptions on how neighbourhood size changes with sample size. A finite rank calculation alone cannot establish that a fitted classifier approaches its optimal risk. General results require their stated sampling and weighting conditions. Consistency theory for the rank construction imposes regularity on the marginal distributions, including nonatomic marginals to avoid coordinate ties.{{cite:biau_devroye2015}} (pp. 98–99, Rem. 8.2; Thm. 11.1)
