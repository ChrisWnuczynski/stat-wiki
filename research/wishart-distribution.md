# Wishart distribution

Type: Distribution. Rank 236. Tier: full.

## Material checked

- **Checked:** Frozen baseline 1,165 body words and no figures. The page keeps the density, the normal-sample statement, the scalar reduction at $p=1$, and the catalogue mean $\nu\Sigma$.
- **Checked:** Durrett, 11 January 2019 PDF, Theorem 1.6.1 (linearity) and Example 1.6.11 ($\mathrm{E} Z^2=1$ for a standard normal). The recurrence $\mathrm{E} Z^4=3$ is derived on the page from $\varphi'=-z\varphi$.
- **Checked:** Dodge printed p. 235 (Wishart as editor of Student's collected papers) and p. 350 (Allan and Wishart, 1930, on a missing field plot). No scatter-matrix entry was found, so the distribution is not cited to Dodge.
- **Checked by code:** For $\nu=3$ and $\Sigma$ with diagonals $2$ and off-diagonal $1$, the entry moments are $24$, $6$, and $15$, and $\sqrt{24}$ rounds to $4.899$. The scalar case $\nu=4$, $\Sigma=2$ has mean $8$ and variance $32$. The diagonal case $\nu=5$, $\Sigma=\mathrm{diag}(1,4)$ has $\mathrm{Var}(W_{22})=160$.
- **Assumed:** The entry covariance formula in the infobox is the Gaussian one. The new proof derives the mean without normality and the scalar variance from $\mathrm{E} Z^4=3$. It does not re-derive every mixed moment in the general covariance formula.
- **Disputed:** A footnote in Hastie, Tibshirani and Friedman, p. 631, calls the distribution of a Gaussian graphical model a Wishart law. That confuses the sample scatter with the observations. It is not used.

The catalogue's Laplace-transform proof of the mean is omitted by the generator once Properties contains a proof box. The outer-product argument on the page proves the same mean.

## Sources opened and used

1. Rick Durrett, *Probability: Theory and Examples*, version 5, 11 January 2019, Theorem 1.6.1 and Example 1.6.11. Key `durrett2019`.
2. Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), pp. 235 and 350. Key `dodge2008`.
3. Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, p. 631, footnote only, not cited.
