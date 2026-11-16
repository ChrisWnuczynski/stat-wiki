# Single linkage

Type: Concept. Rank 265. Tier: full.

## Material checked

- **Checked:** Baseline 289 words, 0 figures. Dodge pp. 84–85 gives the minimum update. ESL pp. 523–525, eq. 14.41 and 14.44, describes chaining and the diameter. ISLR Table 12.3, p. 524, describes trailing clusters.
- **Checked by code:** On {0,2,3,8} the heights are 1, 2, 5 and the diameter is 8. On {0,1,2,10} the last height is 8 and the diameter of {0,1,2} is 2. `checks/single-linkage.py`.
- **Assumed:** Tied pairs at distance 1 may be fused in either order without changing the later height.
- **Disputed:** None with ESL. Dodge’s illustration uses Euclidean distance; the rule here is the minimum of a general dissimilarity.

## Sources opened

1. Dodge, printed pp. 84–85, 102. Key `dodge2008`.
2. Hastie, Tibshirani and Friedman, ESL, Ch. 14 §14.3.12, pp. 522–525. Key `hastie_esl2009`.
3. James, Witten, Hastie and Tibshirani, ISLR, Ch. 12 §12.4, p. 524. Key `james_islr2021`.
