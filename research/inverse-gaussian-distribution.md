# Inverse Gaussian distribution

Type: Distribution. Rank 257. Tier: full.

## Material checked

- **Checked by code:** For $\mu=2$, $\lambda=4$, variance 2, density at the mean 0.2821, distribution function at the mean 0.6277, $\Pr(X>3)=0.1756$, $\Pr(X<1)=0.2324$. SciPy's `invgauss` matches this law at shape $\mu/\lambda$ and scale $\lambda$. The docstring of SciPy  was read for that parameter map. There is no bibliography key for it yet, so the article states the scaling algebra without a software citation.
- **Assumed:** The moment generating function recorded with the distribution is the one already on the page. Tweedie (1957) was not opened.
- **Disputed:** Nothing in the printed numbers. The distribution template has no Check yourself slot, so the two hidden answers sit in the worked example.

## Sources opened

The density and mean–variance formulae on the distribution card, differentiated and checked numerically. SciPy's `invgauss` docstring, for the shape-scale map only.
