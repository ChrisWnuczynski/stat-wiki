# Hierarchical clustering

Type: Concept. Rank 245. Tier: full.

## Material checked

- **Checked:** Frozen baseline 1,486 body words and no figures. The page keeps the chapter account of agglomerative and divisive clustering.
- **Checked:** Hastie, Tibshirani and Friedman, §14.3, pp. 520–524. A hierarchy has $N-1$ levels. Cophenetic dissimilarities have at most $N-1$ distinct values among $N(N-1)/2$ pairs and obey the ultrametric inequality.
- **Checked:** Dodge, pp. 84 and 157. Agglomerative rebuilding of the distance table, and a dendrogram as the tree drawn on a distance scale.
- **Checked by code:** Average-linkage final height $10.5$. Cophenetic averages $7.5$ (average linkage), $6.5$ (single), and $8.5$ (complete). The six original distances also average $7.5$.
- **Assumed:** Dissimilarity is absolute distance on the line, and ties are absent among the early pairs.
- **Disputed:** None.

## Sources opened and used

1. Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, §14.3, pp. 520–524. Key `hastie_esl2009`.
2. Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), pp. 84 and 157. Key `dodge2008`.
