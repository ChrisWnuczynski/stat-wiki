# White noise

Type: Concept. Rank 226. Tier: full.

## Material checked

- **Checked:** Baseline 495 words and no figures. The source note's product sequence $\varepsilon_t=z_t z_{t-1}$ stays on the page. The added pair is the single-variable version $Z$ and $Z^2-1$.
- **Checked:** Dodge printed p. 20: white noise described as mutually independent and identically distributed in the moving-average paragraph, and a weak white noise in the ARMA equation.
- **Checked:** Hyndman and Athanasopoulos §§9.1 and 9.3: white noise is stationary; an AR(1) with coefficient 0 and constant 0 is white noise; the figures use normal innovations of mean 0 and variance 1; a random walk is the coefficient-1 boundary.
- **Checked by code:** mean variance $4/4=1$; difference correlation $-1/2$; $\mathbb E(Z^4)=3$ so $\operatorname{Var}(Z^2-1)=2$; practice variance $9/9=1$.
- **Assumed:** Joint normality is what upgrades uncorrelated to independent. The weak definition does not assume normality.
- **Disputed:** Nothing. Dodge's page uses both the independent phrase and the words "weak white noise"; the article keeps both and says which is which.

## Sources opened and used

1. Dodge, printed p. 20, from `pdf-0028.txt`. Existing key `dodge2008`.
2. Hyndman and Athanasopoulos, §§9.1 and 9.3. Existing key `hyndman_athanasopoulos2021`.
