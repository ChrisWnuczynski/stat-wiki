# Multinomial distribution

Type: Distribution. Rank 274. Tier: lighter.

## Material checked

- **Checked:** Baseline 2417 words, 2 figures. Dodge printed p. 363: joint probability, the constraint that the counts sum to n, E[X_i]=n p_i, and Var(X_i)=n p_i(1-p_i), with each margin described as binomial. Dodge writes 0<p_i<1; the article notes that the formula also returns 0 when a coordinate probability is 0.
- **Checked by code:** P(1,1,1)=1/6 for n=3 and probabilities 1/2, 1/3, 1/6. P(3,0,0)=1/8. The ten-trial probability 0.08505 matches the catalogue example. Covariance −1/2. `checks/multinomial-distribution.py`.
- **Assumed:** The negative covariance −n p_i p_j is the indicator argument already proved in the catalogue. The check-yourself answer repeats that one-trial calculation.
- **Not opened:** Agresti 2002 and Forbes et al.

## Sources opened

1. Dodge, printed p. 363. Key `dodge2008`.
