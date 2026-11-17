## Motivating example — A slope can multiply a mean
A Poisson regression may predict 5 expected events at one predictor value and 10 at another. A log link represents this change by adding a coefficient on the log-mean scale, then exponentiating to obtain the mean ratio. This interpretation concerns the conditional mean response and does not require transforming the observed count itself.{{cite:wuthrich_merz2022_glm}} (§5.2.2, ex. 5.13, multiplicative model)

## Definition — Exponentiate the complete contrast
Suppose $\log\mu(x)=\beta_0+\beta_1x_1+\cdots+\beta_qx_q$, where $\mu(x)=E(Y\mid x)>0$. Holding the other predictors fixed and changing $x_j$ by $h$ gives
$$\log\frac{\mu(x+h e_j)}{\mu(x)}=h\beta_j,\qquad\frac{\mu(x+h e_j)}{\mu(x)}=e^{h\beta_j}.$$
The formula follows by subtracting the two linear predictors; the intercept and the unchanged predictors cancel. A one-unit increase therefore multiplies the mean by $e^{\beta_j}$, and its percentage change is $100(e^{\beta_j}-1)$, rather than exactly $100\beta_j$.{{cite:wuthrich_merz2022_glm}} (§5.2.2, ex. 5.13)

Changing several predictors gives the more general factor $\exp\{(x'-x)^\top\beta\}$. With an interaction, the coefficient for one predictor depends on the other predictor's value. For example, $\log\mu=\beta_0+\beta_1x+\beta_2z+\beta_3xz$ gives a one-unit $x$ factor $\exp(\beta_1+\beta_3z)$ at fixed $z$. The complete contrast is the reliable way to interpret either model.

## Interpretation — Mean, rate and odds are different targets
A Poisson model with exposure $t_i$ can use an offset $\log t_i$, giving $\mu_i=t_i\exp(x_i^\top\beta)$. Comparing equal exposures then yields a rate ratio $\exp\{(x'-x)^\top\beta\}$. If exposures differ, the expected-count ratio also contains their ratio. Exposure is part of the conditioning information, rather than an estimated regression coefficient when its offset coefficient is fixed at one.{{cite:wuthrich_merz2022_glm}} (§5.2.3, offsets and Poisson exposure, eqs. 5.26–5.27)

A log link is also possible for a gamma response with variance proportional to the squared mean. It has the same mean-ratio interpretation with different noise and likelihood. A logistic regression instead links log odds to predictors; exponentiating its coefficient produces an odds ratio. The response distribution and chosen link must therefore be identified before assigning a label to $e^\beta$.{{cite:nelder_wedderburn1972}} (§§1.1–1.3, pp. 371–372)

## Worked example — A two-unit change and its inverse
Suppose a fitted log-mean coefficient is $0.3$ per unit. A one-unit increase multiplies the mean by $e^{0.3}=1.349859$, a $34.985881\%$ increase. A two-unit increase multiplies it by $e^{0.6}=1.822119$. This is the square of the one-unit factor, not one plus twice its percentage change. A one-unit decrease multiplies the mean by $e^{-0.3}=0.740818$; positive and negative percentage changes are asymmetric because the reference mean changes.

If the baseline expected count is 5, the one-unit predicted count is $6.749294$ and the two-unit prediction is $9.110594$. These are means, so they need not be integers even though individual Poisson outcomes are integer counts. The multiplicative mean structure follows from the inverse link, while the Poisson variance assumption supplies a different part of the model.{{cite:nelder_wedderburn1972}} (§1.3 and §3.3, Poisson examples)

**Your turn.** An exposure doubles while predictors change enough to multiply the event rate by $1.5$. By what factor does the expected count change?

::: {.callout-tip collapse="true" title="Answer"}
Expected count is exposure times rate, so its factor is $2\times1.5=3.000$. The rate factor itself remains $1.5$.
:::

## Properties — Units and uncertainty transform together
If a predictor is converted from single units to tens of units, its coefficient is multiplied by ten. The factor for an equivalent scientific contrast is unchanged because the product of coefficient and predictor change stays the same. Comparing coefficients without comparing their predictor units can therefore reverse an apparent ranking of effect sizes.

If a confidence interval for a specified log-mean contrast is $(L,U)$, monotonicity of the exponential function maps it to $(e^L,e^U)$ for the corresponding mean ratio. The transformation preserves the interval event; it generally creates asymmetric distances around the point estimate on the ratio scale. A contrast involving several coefficients must use their covariance when constructing $(L,U)$ before transformation.{{cite:wuthrich_merz2022_glm}} (§5.3.2, Wald inference for regression parameters)

## Assumptions and limits — Conditional comparisons do not prove interventions
The coefficient describes a model-based comparison at fixed covariates and exposure. An observational coefficient can reflect confounding, selection or model misspecification. A log link guarantees positive fitted means but does not guarantee that the chosen covariates describe the mean adequately. In particular, fitting a straight line on the log scale can still miss curvature, interactions or systematic residual patterns.{{cite:wuthrich_merz2022_glm}} (§§5.3.1–5.3.4, model validation and feature specification)
