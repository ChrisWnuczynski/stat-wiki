# Single, complete, and average linkage

Type: Concept. Rank 242. Tier: full.

## Material checked

- **Checked:** Frozen baseline 516 body words and no figures. The page keeps the chapter definition of the three linkages.
- **Checked:** Hastie, Tibshirani and Friedman, pp. 523–526. Equations (14.41)–(14.43) are the minimum, maximum, and average cross dissimilarities. Page 525 records monotone invariance of the first two and the failure of that invariance for the average. Pages 525–526 give the population integral that the average estimates.
- **Checked:** Dodge, printed p. 84, defines single linkage as the closest Euclidean pair and complete linkage as the furthest, inside the agglomerative algorithm. Printed p. 157 describes a dendrogram.
- **Checked by code:** Cross gaps $10,12,9,11$ have min $9$, max $12$, mean $10.5$. Squared gaps average $111.5$, not $10.5^2=110.25$. Chain gaps $2$ and $1$ give $1$, $2$, and $1.5$.
- **Assumed:** Dissimilarity along the line is absolute distance.
- **Disputed:** None.

## Sources opened and used

1. Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, §14.3, pp. 523–526. Key `hastie_esl2009`.
2. Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), pp. 84 and 157. Key `dodge2008`.
