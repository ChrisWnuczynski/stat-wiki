# Dendrogram

Rank 348. Lighter tier. Concept page.

## Facts checked

- Hastie, Tibshirani and Friedman, 2nd ed., p. 521: a monotone agglomerative hierarchy is drawn with node height equal to the intergroup dissimilarity; a horizontal cut returns the clusters whose merge height exceeds the cut; flipping branches does not change the merges.
- Dodge, printed p. 157: knots for groups, branches for aggregations, and a scale for the distances of those aggregations.
- Points \(0,1,4,10\). Single-linkage heights \(1\), \(3=\min(4,3)\), \(6=\min(10,9,6)\). Cuts at \(2\) and \(4\) give the partitions stated. The fifth point at \(11\) merges with \(10\) at height \(1\), and the cross distance remains \(6\).
- Complete linkage of \(\{0,1\}\) with \(4\) is \(4\).

## Assumed

- Single linkage is the minimum pairwise distance. That is the rule used for the arithmetic; the page's general statement that the height belongs to the linkage is what Dodge and ESL support.

## Disputed

- None. Dodge's historical sentence about Mayr et al. (1953) was not checked against that paper and is not repeated.

## Not opened

- Sneath (1957) and Sokal and Michener (1958), cited on the page, were not reopened.
