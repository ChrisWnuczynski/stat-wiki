# Complete linkage

Type: Concept. Rank 263. Tier: full.

## Material checked

- **Checked:** Baseline 472 words, 0 figures. Dodge pp. 84–85 and p. 102 define single and complete linkage as min and max cross-pair rules; p. 157 describes the dendrogram. ESL 2nd ed. (author PDF, 12th printing) §14.3.12, printed pp. 523–525, equations 14.41–14.44: maximum, diameter, chaining, monotone transformations, and the large-sample limits of single and complete linkage. ISLR 2nd ed. (author PDF, corrected June 2023) §12.4, printed pp. 524–525, Table 12.3 and Algorithm 12.3.
- **Checked by code:** Fusion heights on {0,2,3,8} are 1, 3, 8; on {0,1,4} the last height is 4; squared distances do not reorder maxima 9 and 6; points {0,1,2,10} finish at height 10. `checks/complete-linkage.py`.
- **Assumed:** Within-cluster diameters of clusters built by complete linkage are at most the fusion height, so the fusion height equals the diameter of the union. The proof uses that induction together with the maximum definition.
- **Disputed:** Dodge’s cluster-analysis entry illustrates the rules with Euclidean distance. The definition used here allows any dissimilarity, as in ESL.

## Sources opened

1. Yadolah Dodge, *The Concise Encyclopedia of Statistics*, Springer, 2008, printed pp. 84–85, 102, 157. Key `dodge2008`.
2. Trevor Hastie, Robert Tibshirani and Jerome Friedman, *The Elements of Statistical Learning*, 2nd ed., 12th printing, Springer, 2009, Ch. 14 §14.3.12, pp. 520–525. Key `hastie_esl2009`. Author-hosted PDF.
3. Gareth James, Daniela Witten, Trevor Hastie and Robert Tibshirani, *An Introduction to Statistical Learning*, 2nd ed., corrected June 2023 printing, Ch. 12 §12.4, pp. 524–525. Key `james_islr2021`. Author-hosted PDF.
