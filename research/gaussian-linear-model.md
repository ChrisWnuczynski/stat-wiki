# Gaussian linear model

Type: Definition. Rank 255. Tier: full.

## Material checked

- **Checked:** Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, 2nd edition, corrected 12th printing, §3.2, pp. 45–47. Least squares is defined before normality. Gaussian errors give normality of $\hat\beta$, covariance $\sigma^2(X^\top X)^{-1}$, and a chi-squared residual sum of squares.
- **Checked by code:** four-point fit $\hat\beta=(0.1,0.6)$, $s^2=0.1$, slope standard error $\sqrt{1/50}=0.1414$, $t=3\sqrt{2}=4.243$ against $t_{2,0.975}=4.3027$. The altered sample $y=(0,1,3,2)$ has slope 0.8 and residual sum of squares 1.8.
- **Assumed:** Full column rank. Exact $t$ probabilities need independent normal homoscedastic errors.
- **Disputed:** The copied chapter sentence "This does not claim..." is source text. It was left in place. Schwarz's paper and the Bayesian chapter's other books were not reopened.

## Comparison with the first article

The pooled-variance page has a motivating numerical story, a proof, a worked example, a hidden prompt, two checked questions, distinct misreadings and a concrete failure. This page has the same pieces, with the four-point $t_2$ calculation playing the role of the computer-lifetime arithmetic.
