# Maximum likelihood in a GLM

Type: concept. Rank 304. Tier: lighter.

## Facts

- **Checked by code:** For a Poisson count $2$ and log intercept, the step from $0$ is $1$, the next value is $2/e\approx 0.735759$, and $\log 2\approx 0.693147$. The score at $\log 2$ is $0$. Also $e\approx 2.718282$ and $e^{2/e}>2$.
- **Checked:** R `glm` documentation: `glm.fit` uses iteratively reweighted least squares.
- **Assumed:** For the Poisson log link the observed Hessian equals the expected information, which the proof shows because the Hessian is $-e^{\beta}$.
- **Disputed:** None. Nelder and Wedderburn (1972) was not opened; the Poisson score is differentiated directly.

## Sources read

1. R Core Team, `glm` documentation, method `glm.fit`.
