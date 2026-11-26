## Lead context
Conditional response distributions and the distribution of latent group effects play different roles in a GLMM.

## Motivating example
Several binary outcomes are observed for each patient. A Bernoulli model describes each outcome's conditional variation, while a patient intercept allows outcomes from the same person to share a tendency toward success or failure. Treating those repeated outcomes as independent without the shared effect can misrepresent their dependence.{{cite:bolker2009_glmm}} (pp. 127–128)

## Definition — A GLM conditional on latent effects
For group $j$, suppose responses are conditionally independent given a latent vector $b_j$, with an exponential-family response distribution and
$$
g\{\E(Y_{ji}\mid b_j,x_{ji},z_{ji})\}=x_{ji}^\top\beta+z_{ji}^\top b_j,
\qquad b_j\stackrel{\mathrm{iid}}\sim N(0,\Sigma).
$$
The covariance matrix $\Sigma$ must be positive semidefinite. A random intercept uses a constant coordinate in $z$; random slopes use predictor values as further coordinates. The normal distribution describes the latent coefficients on the link scale. The response can be Bernoulli, Poisson, Gaussian or another specified family. Normal random effects do not make a binary outcome normally distributed.{{cite:bolker2009_glmm}} (pp. 127–130, Box 2){{cite:nelder_wedderburn1972}} (§§1.1–1.3, pp. 371–372)

Conditioning clarifies the two sources of variation. For a Poisson log-link model, $\operatorname{Var}(Y\mid b)=\E(Y\mid b)$. After mixing over $b$, the variance generally exceeds the marginal mean because the conditional mean itself varies. The analogous mixture identity applies to any response with finite second moments:
$$
\operatorname{Var}(Y)=\E\{\operatorname{Var}(Y\mid b)\}+\operatorname{Var}\{\E(Y\mid b)\}.
$$
It is the mixture distribution that determines the marginal response law.{{cite:wuthrich_merz2022_glm}} (§5.3.5, pp. 155–156, eqs. 5.36–5.37)

## Properties — Integrate a group's shared effect once
For independent groups with random-effects density $\varphi_\Sigma$, the marginal likelihood is
$$
L(\beta,\Sigma,\phi)=\prod_j\int\left\{\prod_i f(y_{ji}\mid b_j;\beta,\phi)\right\}\varphi_\Sigma(b_j)\,db_j.
$$
The product over observations stays inside the group integral. Integrating each observation separately would assign different independent latent effects and change their joint distribution. Logistic-normal group integrals usually require numerical approximation, including Laplace approximation or adaptive quadrature. Some other mixtures, such as Poisson with gamma mixing, have closed forms.{{cite:bolker2009_glmm}} (p. 130, Box 2){{cite:wuthrich_merz2022_glm}} (§5.3.5, p. 156)

A numerical optimiser and an integration approximation solve different problems. Convergence of an optimiser does not establish that its approximate integral is accurate, while agreement across starting values does not rule out all competing optima. Sensitivity to quadrature, scaling and starting values is part of assessing a difficult fit.{{cite:bolker2009_glmm}} (pp. 129–130, Estimation)

## Interpretation — Conditional slopes and marginal means
With a logit link, $e^{\beta_k}$ is a conditional odds ratio for a unit change in predictor $k$, holding the other predictors and random effects fixed. Marginal success probability is an integral of the expit over the random-effects distribution, rather than simply the expit at $b=0$. With a random slope, the conditional contrast itself varies across groups. These distinctions also affect the interpretation of a plotted “typical group” curve.{{cite:bolker2009_glmm}} (pp. 127–130, random effects and Box 2)

## Worked example
Let two counts in the same group be conditionally independent with
$$
Y_1,Y_2\mid b\sim\operatorname{Poisson}(2e^b),\qquad b\sim N(0,1/2).
$$
For a centred normal variable of variance $s^2$, completing the square in its density gives $\E(e^{tb})=e^{t^2s^2/2}$. Thus the group with $b=0$ has conditional mean $2$, while the marginal mean is
$$
m=2e^{1/4}\approx2.568051.
$$
The conditional-mean variance is $4e^{1/2}(e^{1/2}-1)\approx4.278242$. Total variance therefore gives
$$
\operatorname{Var}(Y_1)=m+4.278242\approx6.846293.
$$
Conditional independence makes the within-group covariance equal to that conditional-mean variance, about $4.278242$. The resulting correlation is approximately $0.624899$. Shared heterogeneity creates dependence even though the responses are independent after conditioning on $b$.{{cite:wuthrich_merz2022_glm}} (§5.3.5, pp. 155–156){{cite:bolker2009_glmm}} (p. 130, Box 2)

**Your turn.** What happens to these marginal quantities when the random-intercept variance is zero?

::: {.callout-tip collapse="true" title="Answer"}
Then $b=0$ almost surely. Both marginal means and variances become $2$, and the covariance and correlation between the two counts become zero. The model reduces to independent Poisson responses with a fixed mean.
:::

## Check yourself
### Patient-specific trends {#self-check-q-41}
[Random slopes and changed conclusions](../questions/q-41.qmd): describe the extra random coefficient and compare the two interaction uncertainties.

::: {.callout-tip collapse="true" title="Answer"}
Add $b_{1i}t$ to the patient intercept $b_{0i}$ and give $(b_{0i},b_{1i})$ a joint centred normal law with a positive semidefinite covariance matrix. The interaction statistics change from $-0.080/0.030\approx-2.667$ to $-0.070/0.055\approx-1.273$. The second standard error is larger, so its estimated difference is less precisely determined. Its approximate interval is $-0.070\pm1.96(0.055)=(-0.1778,0.0378)$, which includes nonzero differences as well as zero.
:::

### Dependence from a patient intercept {#self-check-ex-toenail-glmm}
[Toenail infection GLMM](../questions/ex-toenail-glmm.qmd): explain why random allocation does not remove repeated-measure dependence.

::: {.callout-tip collapse="true" title="Answer"}
Repeated visits share the same patient's latent intercept. The conditional logit includes treatment, week, their interaction and that intercept. Given the intercept the visits are modelled as independent; marginally their probabilities covary through it. Random treatment assignment addresses the treatment comparison but does not make repeated measurements from a person independent.
:::
