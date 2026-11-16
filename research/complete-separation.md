# Complete separation

Type: concept. Rank 299. Tier: lighter.

## Facts

- **Checked by code:** For four separated observations and an intercept-free logit, $\ell(0)=-4\log 2\approx -2.773$, $\ell(1)\approx -1.253$, $\ell(2)\approx -0.508$, and $\ell(5)\approx -0.027$. The contribution equals $-\log(1+e^{-\beta})$ and the score $1/(1+e^{\beta})$ is positive.
- **Assumed:** The intercept-free path is a special case of a separating direction. The four-point exercise with an intercept, $\beta_0=-2.5s$ and $\beta_1=s$, is the bank question and was not refit numerically beyond the linear predictors $-1.5s,-0.5s,0.5s,1.5s$.
- **Disputed:** Albert and Anderson (1984) is the usual reference for the general existence theorem and was not opened. The article proves the one-predictor case directly and does not attribute a page of that paper.

## Sources read

1. The one-predictor log-likelihood was expanded algebraically and checked in `checks/complete-separation.py`.
