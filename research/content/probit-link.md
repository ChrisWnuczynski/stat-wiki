## Motivating example

Suppose a toxicity experiment records whether an animal responds to a dose, with the chance of response rising smoothly as dose increases. A linear formula for probability could leave the interval from zero to one. A probit model instead places the linear predictor on a standard-normal quantile scale and converts it to a valid probability. This is especially useful when a normally distributed latent threshold is a plausible account of the binary outcome.

## Intuition — Why a normal threshold produces a link

For a given success probability, the probit asks where that probability falls on the standard normal axis. A probability of one half corresponds to a probit of zero; probabilities above one half have positive probits, and probabilities below one half have negative probits. In a regression, the covariates add on that quantile scale. The inverse link, $\Phi$, maps any real predictor back into a probability. The coefficient is therefore a change in *normal-score units*, not a change in probability or log-odds.{{cite:nelder_wedderburn1972}} (§3.3, pp. 379–380)

## Definition

For $Y_i\mid x_i\sim\operatorname{Bernoulli}(p_i)$, a probit GLM specifies

$$
g(p_i)=\Phi^{-1}(p_i)=\eta_i=x_i^\top\beta,
\qquad p_i=\Phi(x_i^\top\beta),
$$

where $\Phi$ is the standard normal cumulative distribution function.{{cite:nelder_wedderburn1972}} (§3.3, pp. 379–380) The model specifies the conditional mean $p_i$ and the Bernoulli response distribution; the link is only the map between that mean and the linear predictor. A fitted probability requires the entire predictor, including intercept and all covariates, followed by $\Phi${{cite:nelder_wedderburn1972}} (§3.3, pp. 379–380).

## Interpretation

If a scalar predictor has coefficient $\beta_1$, increasing it by one unit shifts the normal score by $\beta_1$. Its effect on probability varies with the starting score: $\partial p/\partial x=\beta_1\varphi(\eta)$, where $\varphi$ is the standard normal density. The density is largest at $\eta=0$, so an equal score shift changes probability most near one half and less near either extreme. This is why a coefficient cannot be reported as a constant percentage-point effect.

The model has a latent-variable interpretation. Let $Z_i=x_i^\top\beta+\varepsilon_i$, with $\varepsilon_i\sim N(0,1)$, and observe $Y_i=1$ when $Z_i>0$. Then $P(Y_i=1\mid x_i)=\Phi(x_i^\top\beta)$. Fixing the error variance to one sets the scale: binary data alone cannot separately identify a common multiplier on both the coefficients and an unknown latent-error standard deviation. The threshold story is one interpretation of the fitted probabilities, not proof that an actual unrecorded normal variable exists.

## Properties

The standard-normal symmetry gives $\Phi(-\eta)=1-\Phi(\eta)$; therefore reversing the event label changes the signs of the predictor coefficients and complements fitted probabilities. The inverse link is strictly increasing with derivative $\varphi(\eta)>0$. For a single positive slope $\beta_1$, the half-probability point solves $\beta_0+\beta_1x=0$, so it lies at $-\beta_0/\beta_1$ when $\beta_1\ne0$.

At the centre, the standard probit inverse link has slope $\varphi(0)=1/\sqrt{2\pi}\approx0.39894$. The logistic inverse link has central slope $1/4$. Rescaling the normal score by $c=\sqrt{\pi/8}\approx0.62666$ makes these slopes agree, but this local match does not make the two curves identical, especially in the tails. Coefficients from separately fitted logit and probit models therefore require a scale conversion for rough comparison, and an approximate multiplier is not a mathematical identity for every dataset.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The latent threshold model gives $P(Z_i>0\mid x_i)=P(\varepsilon_i>-\eta_i)=1-\Phi(-\eta_i)=\Phi(\eta_i)$ by symmetry of the standard normal law. Differentiating $p(x)=\Phi(\beta_0+\beta_1x)$ yields $p'(x)=\beta_1\varphi(\eta)$ by the chain rule. Because $\varphi(\eta)=e^{-\eta^2/2}/\sqrt{2\pi}$, it is positive, maximal at zero and decreases as $|\eta|$ grows. Normal symmetry yields $\Phi(-\eta)=1-\Phi(\eta)$, and $\Phi(0)=1/2$ gives the half-probability equation. For the slope comparison, the logistic function $\sigma(\eta)$ has $\sigma'(0)=1/4$, while $\frac{d}{d\eta}\Phi(c\eta)|_{\eta=0}=c/\sqrt{2\pi}$; equality gives $c=\sqrt{2\pi}/4=\sqrt{\pi/8}$. These statements establish the link interpretation without requiring a particular fitting algorithm.
:::
:::

## Statistical use

State which event is coded as one and the scale of every predictor. Estimate the full model, then calculate probabilities at meaningful covariate combinations or average marginal effects over observed combinations. When comparing probit with logit or complementary log-log, refit each model: changing the link changes the mapping between coefficients and probabilities, so copying estimates across links is not a fit. Predictive validation and residual checks address fit; a coefficient's sign alone does not establish causality.

Probit also appears in models with latent normal variables, including threshold models for ordinal outcomes. The binary probit is the simplest instance, with one threshold. Such extensions need additional assumptions about thresholds and the latent variance; the binary formula by itself does not identify them.

With a wrong linear predictor, the probit's valid probability range does not save the fit: if the dose-response relationship turns down at high doses, a one-slope probit forces monotonicity and can miss that decline. Complete separation can send unpenalised binary-regression coefficients toward infinity rather than produce a finite estimate. A latent error distribution with heavy or asymmetric tails can make a normal link a poor description at extreme doses. If outcomes within a household are dependent, a Bernoulli likelihood that treats them as conditionally independent understates uncertainty unless the dependence is modelled or the variance is adjusted.
## Worked example

Let $p(x)=\Phi(-0.5+0.8x)$ for a dose score $x$. At $x=0$, the predictor is $-0.5$ and the response probability is $\Phi(-0.5)\approx0.30854$. At $x=1$, it is $0.3$ and $p(1)\approx0.61791$; at $x=2$, it is $1.1$ and $p(2)\approx0.86433$. The half-probability dose solves $-0.5+0.8x=0$, giving $x=0.625$. At $x=1$, the local probability slope is $0.8\varphi(0.3)\approx0.30511$ per dose-score unit. The increases from $x=0$ to $1$ and from $1$ to $2$ differ, even though the score rises by the same $0.8$ each time.

**Your turn.** For $p(x)=\Phi(-1+0.5x)$, find $p(0)$, $p(2)$, $p(4)$ and the value of $x$ where $p(x)=0.5$. Explain why $0.5$ is not the constant probability gain from one more unit of $x$.

::: {.callout-tip collapse="true" title="Answer"}
The scores are $-1,0,1$, giving probabilities about $0.15866,0.5,0.84134$. The half-probability point is $x=2$. The coefficient $0.5$ is a normal-score change; the probability derivative is $0.5\varphi(-1+0.5x)$, which depends on $x$.
:::

## Common misconceptions

A probit coefficient is not an odds ratio; exponentiating it does not give a constant odds multiplier. A change of $0.5$ in the linear predictor is not a change of $0.5$ in probability. Similar fitted logit and probit probabilities do not imply equal numerical coefficients, because the link scales differ. The latent-normal construction explains one way to obtain the link but is not an empirical test of normally distributed individual thresholds.

## Connections

The [logit link](logit-link.qmd) models log-odds and often gives similar central probabilities on a different coefficient scale. The [complementary log-log link](complementary-log-log-link.qmd) is asymmetric in its tails. The [normal distribution](normal-distribution.qmd) supplies $\Phi$ and $\varphi$, while the [generalised linear model](generalised-linear-model.qmd) framework separates response family, linear predictor and link.

Probit, logit and complementary log-log links are three maps from a probability to a linear predictor for a binary or ordinal response.{{cite:mccullagh1980}} (pp. 109–127)

The probit link is the standard normal quantile function.{{cite:nelder_wedderburn1972}} (§3.3, pp. 379–380)
