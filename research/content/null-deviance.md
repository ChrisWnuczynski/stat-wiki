## Lead context
The null deviance is the deviance of the intercept-only model, the benchmark against which the covariates are judged.

## Intuition — How far the grand mean is from a perfect fit
A saturated model fits a mean for every observation and, for a binary response, can match every \(0\) and \(1\). An intercept-only model fits one common probability to all of them. The null deviance is twice the drop in log-likelihood between those two fits. A large value means the common probability is a poor description. Covariates are then judged by how much of that deviance they remove, not by the null deviance alone.

## Definition — Deviance of the model with no covariates
For a log-likelihood \(\ell\), the deviance of a model is \(D=2(\ell_{\mathrm{sat}}-\ell_{\mathrm{model}})\), using the saturated fit as the reference. The null deviance is this number for the intercept-only fit. In R, `null.deviance` is that deviance and `df.null` is its residual degrees of freedom. With an intercept and \(n\) binary observations, one parameter is fitted, so the null residual degrees of freedom are \(n-1\).{{cite:rstats_glm2026}} (Description, ‘null.deviance’)

## Properties — Binary data, and a zero saturated log-likelihood
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a Bernoulli observation the saturated fit sets the probability equal to the observation. The contribution \(y\log y+(1-y)\log(1-y)\) is \(0\) for \(y\in\{0,1\}\), with the convention \(0\log 0=0\). So \(\ell_{\mathrm{sat}}=0\) and the null deviance of independent Bernoulli observations with common fitted probability \(\hat p\) is
\[
D_0=-2\sum_i\bigl(y_i\log\hat p+(1-y_i)\log(1-\hat p)\bigr).
\]
The maximiser is \(\hat p=\bar y\).
:::
:::

## Worked example — Four binary observations, three of them ones
The observations are \(1,1,0,1\). Then \(\hat p=3/4\), and
\[
D_0=-2\bigl(3\log(3/4)+\log(1/4)\bigr)\approx 4.4987.
\]
The null residual degrees of freedom are \(4-1=3\). If a covariate model later reports residual deviance \(1.4987\) on \(2\) degrees of freedom, the drop is \(4.4987-1.4987=3\) on \(3-2=1\) degree of freedom. That difference is a comparison with the intercept-only fit, not a comparison of the covariate model with a perfect fit beyond what the residual deviance already measures.

**Your turn.** Observations \(1,0,0,0\). Compute \(\hat p\) and the null deviance to four decimal places.

::: {.callout-tip collapse="true" title="Answer"}
\(\hat p=1/4\). By symmetry with the worked example, swapping the labels \(0\) and \(1\) leaves the Bernoulli log-likelihood unchanged, so \(D_0\) is again approximately \(4.4987\), now \(-2(\log(1/4)+3\log(3/4))\).
:::

## Connections — Residual deviance, degrees of freedom, and the likelihood ratio
The [residual deviance](residual-deviance.qmd) replaces the intercept-only log-likelihood by the fitted model's. Their difference is the likelihood-ratio comparison of the two models, and the change in [degrees of freedom](degrees-of-freedom.qmd) is the number of covariates added when the intercept is already present. The [saturated model](saturated-model.qmd) is the reference that makes both deviances zero when the fit is perfect. For a binary response that reference contributes nothing, which is why the formula collapsed to \(-2\ell_{\mathrm{null}}\).

## Check yourself — Two null fits
Five binary observations contain four ones. What is \(\hat p\), and what is `df.null` for an intercept-only fit?

::: {.callout-tip collapse="true" title="Answer"}
\(\hat p=4/5\). One intercept is estimated, so `df.null` is \(5-1=4\).{{cite:rstats_glm2026}} (Description, ‘df.null’)
:::

Why is the null deviance of \(1,1,0,1\) not equal to \(-2\log((3/4)^4)\), which would be the deviance if all four observations equalled \(3/4\) in a continuous likelihood?

::: {.callout-tip collapse="true" title="Answer"}
Three observations contribute \(\log(3/4)\) and the zero contributes \(\log(1/4)\), so the sum is \(3\log(3/4)+\log(1/4)\), not \(4\log(3/4)\). The zero is a failure at probability \(3/4\), and it is in the likelihood.
:::
