## Motivating example
Several clinics observe binary outcomes. Their underlying rates can differ while being related through a shared population distribution. Estimating only one common rate erases that heterogeneity; estimating every rate independently discards information about the population of clinics. A hierarchical beta–binomial model gives each clinic its own rate and uses shared beta parameters to describe their distribution. The hyperposterior updates those shared parameters after integrating the clinic rates.{{cite:blei_ng_jordan2003}} (§3, eqs. 2–3, latent-mixture marginalization)

The beta density is proportional to $\theta^{\alpha-1}(1-\theta)^{\beta-1}$ and is normalized by $B(\alpha,\beta)$. Its two concentrations encode both an average rate and a spread of rates. A hyperposterior concerns uncertainty in those concentrations, rather than uncertainty in one clinic's rate at fixed concentrations.{{cite:ng_tian_tang2011_dirichlet}} (§1.3, def. 1.1, eq. 1.5)

## Statement
For independent study contributions conditional on hyperparameters, let $Y_j\mid\theta_j\sim\operatorname{Binomial}(n_j,\theta_j)$ and $\theta_j\mid\alpha,\beta\sim\operatorname{Beta}(\alpha,\beta)$. With hyperprior $p(\alpha,\beta)$, the marginal hyperposterior is proportional to
$$p(\alpha,\beta)\prod_j\frac{B(\alpha+y_j,\beta+n_j-y_j)}{B(\alpha,\beta)}.$$
Each factor is a beta integral. Binomial coefficients have been omitted because they depend only on the fixed observations, not on the hyperparameters being compared. They must be restored when calculating a normalized predictive mass for a count or comparing models with different data descriptions.{{cite:ng_tian_tang2011_dirichlet}} (§1.3, beta normalization){{cite:blei_ng_jordan2003}} (§3, eqs. 2–3, integration over latent proportions)

## Proof
Multiplication of a study's binomial kernel by its beta prior density gives
$$\frac{\theta_j^{\alpha+y_j-1}(1-\theta_j)^{\beta+n_j-y_j-1}}{B(\alpha,\beta)}.$$
Integrating over $0<\theta_j<1$ produces the displayed ratio of beta functions. Conditional independence permits integration study by study, so their factors multiply. Bayes' rule then multiplies by the hyperprior. Replacing $B(a,b)$ by $\Gamma(a)\Gamma(b)/\Gamma(a+b)$ gives the gamma-function expression. This derivation uses a joint probability model; it does not replace the uncertain rates by point estimates.{{cite:ng_tian_tang2011_dirichlet}} (§1.3, eq. 1.5)

## Key results — Mean and concentration describe different directions
Writing $m=\alpha/(\alpha+\beta)$ and $k=\alpha+\beta$ gives a population mean rate $m$ and concentration $k$. Increasing $k$ at fixed $m$ makes the study rates less dispersed. A density specified in $(\alpha,\beta)$ does not carry the same numerical values into $(m,k)$: the inverse map $(\alpha,\beta)=(mk,(1-m)k)$ has absolute Jacobian $k$. A regular grid in the transformed coordinates must use that factor when approximating posterior integrals.

This distinction also separates full Bayesian learning from an empirical-Bayes plug-in analysis. Conditioning on one fitted hyperparameter pair omits its posterior uncertainty. Hierarchical mixture models integrate that uncertainty when computing marginal probabilities and predictions.{{cite:blei_ng_jordan2003}} (§§3, 5, latent integration and parameter estimation)

## Worked example
### Two possible population distributions
Take two studies with $(y_1,n_1)=(1,2)$ and $(y_2,n_2)=(2,2)$. Suppose a discrete hyperprior assigns equal probability to $(\alpha,\beta)=(1,1)$ and $(2,2)$. At the first pair the product of beta-function ratios is $1/18$; at the second it is $3/50$. Their ratio is $27/25$. Normalizing the two weighted possibilities gives posterior probabilities $25/52$ and $27/52$. The finite hyperprior converts the kernel comparison into a probability calculation. A continuous density evaluated at two points could not be normalized in this manner.{{cite:ng_tian_tang2011_dirichlet}} (§1.3, beta-integral normalization)

For the study with two successes, its conditional posterior rate is Beta(3,1) under the first hyperparameter pair and Beta(4,2) under the second. Its marginal posterior mean is therefore $(25/52)(3/4)+(27/52)(2/3)=147/208=0.706731$. Simply plugging in either candidate pair would miss this averaging step. The underlying operation is marginalization of a hierarchical mixture.{{cite:blei_ng_jordan2003}} (§3, eqs. 2–3)

**Your turn.** Under the same two-point posterior, find the marginal posterior mean rate for the study with one success in two trials.

::: {.callout-tip collapse="true" title="Answer"}
Its conditional posteriors are Beta(2,2) and Beta(3,3), each with mean one-half. Their weighted mixture therefore also has mean one-half.
:::

## Statistical use — Computation must match the integration measure
For many studies, evaluating products of gamma functions can overflow. Sum their log-gamma expressions and normalize log weights using a common offset. A bounded numerical grid also truncates the hyperparameter space; expanding it and checking tail contributions helps determine whether omitted mass matters. The result of a grid calculation should be interpreted as an approximation to integrals with respect to its stated coordinate measure.

A proper hyperprior guarantees a proper posterior when the count likelihood has positive prior predictive probability, because the likelihood is bounded by one. An improper hyperprior requires a separate integrability argument. A visually plausible local mode does not establish that the full hyperposterior integrates to a finite value. The normalization and mixture distinctions apply before choosing a numerical method.{{cite:blei_ng_jordan2003}} (§3, marginal likelihood and posterior normalization)

A grid that reports a local mode still has to show that the weights outside the grid are small on the scale of the integral. Summing log-gamma terms and subtracting their maximum before exponentiating keeps the same weights without overflow. The resulting normalised weights approximate the hyperposterior only for the coordinate measure the grid was built on.{{cite:blei_ng_jordan2003}} (§3, marginal likelihood and posterior normalization)
