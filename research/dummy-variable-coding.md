# Dummy variable coding

Type: concept. Rank 300. Tier: lighter.

## Facts

- **Checked by code:** Means $11,15,21$ give reference-$A$ coefficients $11,4,10$ and reference-$C$ coefficients $21,-10,-6$. The $2\times 2$ interaction residuals are $1,-1,-1,1$ and the sum of squares is $4$. The reference-cell means are $10,8,14,15$, and the level-2 contrast of A at level 2 of B is $7$.
- **Checked:** James et al., ISLR corrected 7th printing, §3.3.1, equations (3.26)–(3.30), pp. 84–86, describe $0/1$ indicators, a dropped baseline, and coefficients as differences from that baseline. The article derives the same reading for three groups, so the printing is not given a new bibliography key.
- **Assumed:** Equal variance and independent observations for the least-squares claim. With another covariate, the coefficients are differences at a fixed value of that covariate.
- **Disputed:** None.

## Sources read

1. James, Witten, Hastie, and Tibshirani, ISLR, corrected 7th printing, §3.3.1.
2. Wilkinson and Rogers (1973), opening page: the paper is about symbolic factorial formulae, not about the indicator column sum, so it is not cited for that sum.
