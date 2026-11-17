## Motivating example
A count model may predict the average number of machine failures well while underestimating how variable the counts are. A Poisson likelihood ties mean and variance together; quasi-likelihood lets the analyst retain a mean regression and specify a more suitable variance without claiming a complete count distribution. Its quasi-score then estimates coefficients by matching weighted residuals to zero.{{cite:wuthrich_merz2022_glm}} (§5.4)

## Intuition
The mean function says what response is expected at given covariates. The variance function says how much trust to place in each residual when estimating the mean. If responses with large predicted means are also more variable, they should not count as if all observations had equal precision. A quasi-score combines each residual with the sensitivity of its mean to the coefficient, divided by its assumed variance. This retains the score-like calculation while demanding fewer distributional commitments.{{cite:wuthrich_merz2022_glm}} (§5.4)

## Definition
For independent observations, choose $\mu_i(\beta)=E(Y_i\mid x_i)$ and $\operatorname{Var}(Y_i\mid x_i)=\phi V(\mu_i)$, with $\phi>0$ and positive $V$. The quasi-score is $U(\beta)=\sum_i (Y_i-\mu_i)\{\phi V(\mu_i)\}^{-1}\partial\mu_i/\partial\beta$. A scalar quasi-likelihood contribution $Q_i(\mu_i;y_i)$ satisfies $\partial Q_i/\partial\mu_i=(y_i-\mu_i)/\{\phi V(\mu_i)\}$ and is defined up to a term independent of $\mu_i$. Its derivative gives the estimating equation, but $Q_i$ is not automatically a log density.{{cite:wuthrich_merz2022_glm}} (§5.4)

## Interpretation
When the mean model is correct, $E(Y_i-\mu_i\mid x_i)=0$, so the quasi-score has expectation zero even without specifying a probability mass function. The variance function still matters: it determines the weights and model-based uncertainty. A common positive $\phi$ rescales every score term by the same factor and therefore leaves its roots unchanged; it changes standard errors through their square-root scale. Observation-specific dispersion does not cancel. The residual figure and examples show why the shape of $V(\mu)$ should be checked against residual spread.{{cite:wuthrich_merz2022_glm}} (§5.4; §5.5, opening discussion)

## Properties
With a log-linear count mean $\mu_i=\exp(x_i^\top\beta)$ and quasi-Poisson variance $\phi\mu_i$, the quasi-score becomes $\phi^{-1}\sum_i x_i(Y_i-\mu_i)$. This is the ordinary Poisson score divided by $\phi$, so a common dispersion leaves coefficient estimates unchanged when the same unpenalised mean model has a well-defined solution. Under the stated independent moment model, the usual model-based covariance is scaled by $\phi$; standard errors are scaled by $\sqrt\phi$. None of this supplies a genuine likelihood-ratio statistic or an ordinary AIC, because the probability law is unspecified.{{cite:wuthrich_merz2022_glm}} (§5.4)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The mean model gives $E[U(\beta)\mid X]=\sum_i E(Y_i-\mu_i\mid X)\{\phi V(\mu_i)\}^{-1}\partial\mu_i/\partial\beta=0$. For the log link, $\partial\mu_i/\partial\beta=\mu_ix_i$; with $V(\mu_i)=\mu_i$, substitution gives $U(\beta)=\phi^{-1}\sum_i x_i(Y_i-\mu_i)$. Multiplying an equation by the same nonzero constant does not change its roots. In an intercept-only model, $U(\beta)=\phi^{-1}\sum_i(Y_i-e^\beta)$, which vanishes at $e^{\widehat\beta}=\bar Y$ when $\bar Y>0$. The last identity uses only the mean and variance setup, not a full Poisson law.{{cite:wuthrich_merz2022_glm}} (§5.4)
:::
:::

## Statistical use
Specify the link, mean model, variance function, independence units and any exposure offset. Fit the quasi-score and inspect Pearson residuals against fitted means to see whether the chosen variance shape is plausible. Estimate dispersion from residual variation with an appropriate degrees-of-freedom allowance, then report how it changes standard errors. For model comparison, use procedures justified for quasi-models or predictive assessment; ordinary likelihood criteria require an actual likelihood. If repeated observations share a subject, the independence covariance needs replacement by a correlation-aware estimating method.{{cite:wuthrich_merz2022_glm}} (§5.4)

If failures occur in shared shutdown episodes, the independence assumption fails even if each individual count has variance $\phi\mu_i$; a clustered covariance or GEE is needed. If the true mean grows quadratically with machine age but the fitted log mean is linear, fixing overdispersion does not cure biased predictions. If the variance changes as $\mu_i^2$ but $V(\mu)=\mu$ is used, weighting and standard errors can be wrong. And when a simulation of full response trajectories or an exact likelihood-ratio test is required, a mean–variance specification alone cannot provide it.{{cite:wuthrich_merz2022_glm}} (§5.4)

## Worked example
Suppose an intercept-only log-mean model is fitted to four counts $(1,2,3,4)$. The quasi-Poisson score is $\phi^{-1}\sum_i(Y_i-\mu)$, so it vanishes at $\widehat\mu=(1+2+3+4)/4=2.5$ and $\widehat\beta=\log 2.5\approx0.91629$ for any common $\phi>0$. If an external dispersion assessment gives $\widehat\phi=2.25$ and the model-based Poisson standard error for a coefficient is $0.12$, its quasi standard error is $\sqrt{2.25}(0.12)=0.18$. The coefficients need not change, while the uncertainty does.{{cite:wuthrich_merz2022_glm}} (§5.4)

**Your turn.** If a common dispersion estimate is $9$ and a Poisson standard error is $0.05$, what quasi standard error results? Does the dispersion alone move the coefficient estimate?

::: {.callout-tip collapse="true" title="Answer"}
The standard error is $\sqrt9(0.05)=0.15$, three times the Poisson value. In the same mean model with a common dispersion, multiplying every score term by $1/9$ does not change the root, so dispersion alone does not move the coefficient estimate.
:::

## Common misconceptions
Quasi-likelihood is not a newly specified probability distribution; its defining gradient uses moments. An unchanged coefficient estimate after adjusting $\phi$ does not imply unchanged uncertainty. A quasi-score with expectation zero does not guarantee an adequate mean model or correctly chosen variance function. And a numerical quasi-likelihood value is not automatically comparable to a full log likelihood by ordinary AIC or likelihood-ratio rules.{{cite:wuthrich_merz2022_glm}} (§5.4)

## Connections
The [quasi-Poisson model](quasi-poisson.qmd) is the count-data case $V(\mu)=\mu$. The [machine-failure question](../questions/q-54.qmd) compares Poisson score and overdispersion in a setting different from the embedded examples above. The [dispersion question](../questions/c-28.qmd) isolates the meaning of $\phi$ across variance functions. These check coefficient fitting and variance interpretation separately.{{cite:wuthrich_merz2022_glm}} (§5.4)

## History
Wedderburn's 1974 *Biometrika* paper introduced quasi-likelihood functions to fit regression models when a mean–variance relation is available without a full response distribution. Later generalised-linear-model treatments developed the corresponding estimating and uncertainty calculations, placing Wedderburn's formulation beside overdispersed count models.{{cite:wuthrich_merz2022_glm}} (§5.4, opening discussion)
