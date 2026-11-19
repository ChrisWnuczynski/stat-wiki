## Motivating example
A Bernoulli response cannot be fitted by assuming a constant Gaussian error variance around an unrestricted straight line. Logistic regression instead models its probability through a linear predictor. IRLS solves its likelihood equations through a sequence of weighted regressions with newly computed responses and weights.{{cite:nelder_wedderburn1972}} (§§1.3–2.1, pp. 372–374)

## Definition — Working responses and changing weights
For independent responses with mean $\mu_i$, variance $\phi V(\mu_i)$ and differentiable link $\eta_i=g(\mu_i)=x_i^\top\beta$, scoring uses a working response
$$z_i=\eta_i+(y_i-\mu_i)\frac{d\eta_i}{d\mu_i}$$
and weights proportional to $\{d\mu_i/d\eta_i\}^2/V(\mu_i)$. At each iteration the current coefficient vector supplies the means, derivatives and weights, then weighted least squares fits $z$ on $X$. A common dispersion factor cancels from the coefficient step.{{cite:nelder_wedderburn1972}} (§2.1, pp. 372–374)

For Bernoulli logistic regression, $d\mu_i/d\eta_i=p_i(1-p_i)$ and $V(p_i)=p_i(1-p_i)$, so $w_i=p_i(1-p_i)$ and $z_i=\eta_i+(y_i-p_i)/w_i$. Multiplying the weighted normal equations out recovers the Newton step.{{cite:nelder_wedderburn1972}} (§2.1, pp. 372–374)

## Properties — Curvature and existence of a finite solution
The logistic log-likelihood has score $X^\top(y-p)$ and Hessian $-X^\top WX$. Nonnegative weights make it concave. Full column rank and finite predictors give strictly positive weights and a nonsingular weighted system, but a finite maximiser still requires more than concavity. Separable labels can drive coefficients without bound.{{cite:rasmussen_williams2006}} (§3.2, pp. 37–38)

Numerically, one solves the weighted linear system rather than explicitly forming a matrix inverse. A rank-deficient design needs an identified parametrisation, and an extreme fitted probability can make the working response unstable. Convergence diagnostics should inspect the likelihood and score as well as changes in coefficients.{{cite:rasmussen_williams2006}} (§3.2, p. 38)

## Worked example — Four Bernoulli observations
Take $x=(0,1,2,3)$ and $y=(0,1,0,1)$. Starting at zero gives $p_i=1/2$, weights $1/4$ and working response $(-2,2,-2,2)$. Weighted least squares yields $\beta=(-1.2,0.8)$. The log-likelihood increases from $-2.772589$ to $-2.352595$. Continuing the same updates gives approximately $(-1.362276,0.908184)$ and log-likelihood $-2.347487$. At that point, the information-based standard errors are approximately $1.974883$ and $1.085192$; these are asymptotic uncertainty summaries for a very small dataset.

**Your turn.** If the model contains only an intercept and the current probability is one half, what does one step do when half the outcomes are successes?

::: {.callout-tip collapse="true" title="Answer"}
The score $\sum_i(y_i-1/2)$ is zero. The weighted mean of the working response is zero, so the intercept stays at zero.
:::

## Assumptions and limits — Newton and scoring can differ
IRLS is a weighted-regression representation of Fisher scoring for a GLM. The observed Hessian and expected information coincide in Bernoulli logistic regression, which makes its Newton and scoring steps identical. With another link, the observed Hessian can include additional response-dependent terms; the same equivalence between all algorithms then needs separate checking.{{cite:nelder_wedderburn1972}} (§2.1, eqs. 7–9, p. 373)
