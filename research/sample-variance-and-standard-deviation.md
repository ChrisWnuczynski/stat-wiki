# Sample variance and standard deviation

Type: Concept. Rank 287. Tier: lighter.

## Facts

- **Checked:** Siegrist §6.5 defines s^2 with divisor n-1, proves E(S^2)=sigma^2 by the expansion sum (X_i-M)^2 = sum X_i^2 - n M^2, and applies Jensen to conclude E(S) <= sigma. Dodge, printed pp. 506–507, gives the same divisor n-1 estimator and the computational form, and records Gosset's 1908 divisor-n formula.
- **Checked by code:** 2, 4, 4, 8 have mean 4.5, sum of squared deviations 19, s^2=19/3, s=2.5166 to four decimals, and divisor-n mean square 4.75. Adding a fifth 4 gives mean 4.4 and s^2=4.8. A sum of squares 10 on n=6 gives s^2=2 and 10/6=5/3.
- **Assumed:** Independent observations with a common finite variance, so Var(M)=sigma^2/n.
- **Disputed:** Nothing numerical. Dodge's normal-coverage percentages 68.26, 95.44 and 99.74 were not copied; the exact normal probabilities were not needed.

## Sources opened

1. Siegrist (2022), §6.5, key `siegrist2022_sample_variance`.
2. Dodge (2008), printed pp. 505–507, Standard Deviation.

## Proofs

Unbiasedness of S^2 and the direction of the bias of S are proved, following Siegrist.
