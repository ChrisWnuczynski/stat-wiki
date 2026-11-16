# Average linkage

Type: Concept. Rank 276. Tier: lighter.

## Material checked

- **Checked:** Baseline 481 words, 0 figures. ESL §14.3.12, p. 523, equation 14.43, and pp. 524–525 on scale dependence and the population limit. ISLR Table 12.3, p. 524, including the inversion warning for centroid linkage.
- **Checked by code:** On {0,2,3,8} the average heights after the first fusion are 2.5, 5.5 and 19/3. Distances 1 and 5 versus two copies of 16/5 reverse order after squaring (means 3 versus 3.2, then 13 versus 10.24). The weighted update (2·4+7)/3=5. `checks/average-linkage.py`.
- **Assumed:** The weighted-average step in the monotonicity proof treats the cross-pairs as a disjoint union, which they are when the two clusters are disjoint.
- **Disputed:** None with ESL.

## Sources opened

1. Hastie, Tibshirani and Friedman, ESL, Ch. 14 §14.3.12, pp. 523–525. Key `hastie_esl2009`.
2. James et al., ISLR, Ch. 12 §12.4, p. 524. Key `james_islr2021`.
