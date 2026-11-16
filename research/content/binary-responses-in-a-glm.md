## Motivating example

A hospital records whether each patient has heart disease, alongside cholesterol and other predictors. The response is either yes or no, so its conditional mean is the chance of disease for a patient with those predictors. A straight-line model for that chance could predict values below zero or above one. A binary generalised linear model keeps a linear predictor for the covariates while a link maps its fitted value to a valid probability. The Bernoulli distribution supplies the sampling variation around that probability.{{cite:nelder_wedderburn1972}} (§§1.1–1.2, pp. 371–372; §3.3, pp. 379–380)

## Intuition

The model has three separable pieces: a two-outcome response distribution, a linear combination of predictors, and a link connecting the combination to the event probability. The link changes how a one-unit predictor difference translates into probability, while the Bernoulli part fixes the mean–variance relationship once that probability is specified. The cholesterol figure shows why predicted probabilities can vary smoothly even though every recorded response is at zero or one. Its vertical jitter is a display device, not a fractional disease outcome.{{cite:nelder_wedderburn1972}} (§§1.1–1.2, pp. 371–372)

## Definition — Bernoulli response and link

For patient $i$, write $Y_i\mid\boldsymbol x_i\sim\operatorname{Bernoulli}(p_i)$ with $0<p_i<1$ and $g(p_i)=\boldsymbol x_i^\top\boldsymbol\beta$. The conditional mean is $p_i$ and the conditional variance is $p_i(1-p_i)$. The logit, probit and complementary log-log are possible links; the Bernoulli likelihood alone does not choose among them. With the logit, the natural parameter of the Bernoulli exponential family equals the linear predictor, which is why logit is called the canonical link.{{cite:geyer2022_exp_family}} (§7.1, binomial natural parameter and cumulant){{cite:nelder_wedderburn1972}} (§§1.1–1.2, 3.3, pp. 371–372, 379–380)

## Properties — Likelihood and the mean–variance rule

For conditionally independent responses, the likelihood is the product of the probability assigned to each observed zero or one: $L(\boldsymbol\beta)=\prod_i p_i^{y_i}(1-p_i)^{1-y_i}$. The same probability also determines $\operatorname{Var}(Y_i\mid\boldsymbol x_i)=p_i(1-p_i)$, largest at $p_i=1/2$ and smaller near either boundary. Neither formula asserts that patients are marginally independent when predictors or unmeasured factors are shared. Conditional dependence from repeat visits or common households requires an additional model or suitable inference adjustment.{{cite:nelder_wedderburn1972}} (§1.1, pp. 371–372){{cite:geyer2022_exp_family}} (§7.1)

::: {.callout-note collapse="true" title="Proof"}
For a Bernoulli variable, $\Pr(Y=1\mid\boldsymbol x)=p$ and $\Pr(Y=0\mid\boldsymbol x)=1-p$, so the mass of an observed $y\in\{0,1\}$ is $p^y(1-p)^{1-y}$. Conditional independence multiplies those masses across observations. Since $Y^2=Y$, $\mathbb E(Y\mid\boldsymbol x)=p$ and $\operatorname{Var}(Y\mid\boldsymbol x)=\mathbb E(Y^2\mid\boldsymbol x)-p^2=p-p^2=p(1-p)$. Differentiating gives $1-2p$, which vanishes at $p=1/2$; the variance there is $1/4$. For the logit link, $\log\{p/(1-p)\}=\eta$ solves to $p=e^\eta/(1+e^\eta)$, always in $(0,1)$.{{cite:geyer2022_exp_family}} (§7.1, eqs. 7.1–7.5)
:::

## Interpretation — Coefficients depend on the link

Under a logit link, a one-unit change in predictor $j$ at fixed other predictors adds $\beta_j$ to log odds and multiplies odds by $e^{\beta_j}$. It does not usually add a constant amount to probability, because the inverse logistic curve is steepest near one half and flatter near the boundaries. Under a probit link, the coefficient moves a standard-normal quantile scale; under complementary log-log it moves the log negative-log no-event scale. Calling every binary-GLM coefficient an odds ratio therefore loses the link that defines it.{{cite:geyer2022_exp_family}} (§7.1){{cite:nelder_wedderburn1972}} (§3.3, pp. 379–380)

## Statistical use

Decide which outcome is coded as the event and which covariates are available before fitting. The fitted mean is a probability for a specified predictor profile, so report that profile when comparing patients or groups. Evaluate calibration and important tail probabilities, since a model may classify most patients correctly while assigning poor probabilities. Check whether independent Bernoulli observations are plausible: repeated measurements on one patient can be correlated, and a common unmeasured cause can create extra variability. Model adequacy also depends on whether the chosen link and linear predictor describe the systematic variation.{{cite:nelder_wedderburn1972}} (§§1–3.3, pp. 371–380)

## Worked example

Fit a logistic binary GLM with intercept $-1$ and slope $0.8$ for an exposure $x$. At $x=0$, $\eta=-1$ and $p=1/(1+e^1)\approx0.26894$. At $x=1$, $\eta=-0.2$ and $p\approx0.45017$. For one patient at each exposure with outcomes $y_0=0$ and $y_1=1$, their conditional likelihood contribution is $(1-0.26894)(0.45017)\approx0.32910$. The slope yields an odds multiplier $e^{0.8}\approx2.22554$, while the probability rises by about $0.18122$ over this particular comparison. The odds multiplier stays constant across a one-unit change; the probability difference does not.{{cite:geyer2022_exp_family}} (§7.1, inverse logit and binomial likelihood)

**Your turn.** Under the same fitted model, find the event probability and Bernoulli variance at $x=2$. Give the odds multiplier from $x=1$ to $x=2$, and explain why that number is not a probability multiplier.

::: {.callout-tip collapse="true" title="Answer"}
At $x=2$, $\eta=-1+0.8(2)=0.6$, so $p=e^{0.6}/(1+e^{0.6})\approx0.64566$. The variance is $p(1-p)\approx0.22878$. The one-unit odds multiplier remains $e^{0.8}\approx2.22554$; multiplying $0.45017$ by that number would give a value above one, so it cannot be the probability multiplier.{{cite:geyer2022_exp_family}} (§7.1)
:::

## Common misconceptions

A binary GLM does not assume a normally distributed response; its individual outcomes are zero or one. The linear predictor is not itself the event probability, so a fitted coefficient is not generally a fixed probability difference. The Bernoulli mean–variance relationship does not make repeated outcomes independent. A good classification threshold score is not the same as calibrated probabilities. Finally, the canonical logit is convenient but not mandatory; probit or complementary log-log can model the same Bernoulli response with different meanings for coefficients.{{cite:nelder_wedderburn1972}} (§§1.1–1.2, 3.3, pp. 371–372, 379–380){{cite:geyer2022_exp_family}} (§7.1)

## Assumptions and limits — Concrete model failures

If each patient contributes five measurements, treating all rows as conditionally independent can understate uncertainty even if the fitted mean curve looks sensible. If a laboratory labels some diseased patients as healthy, the recorded Bernoulli event probability is not the underlying disease probability without a misclassification model. If a single linear cholesterol term misses a sharp threshold, a logit link alone cannot repair the systematic shape. Complete separation, such as every exposed patient having the event and every unexposed patient lacking it, can make finite maximum-likelihood logit coefficients unavailable. These are different failures of dependence, measurement, mean specification, and estimation.{{cite:nelder_wedderburn1972}} (§§1–3.3, pp. 371–380)

## Connections

The [Bernoulli distribution](bernoulli-distribution.qmd) defines one observation's random part; the [linear predictor](linear-predictor.qmd) and [inverse link](inverse-link.qmd) define its conditional mean. The [logit link](logit-link.qmd) is canonical, while [probit](probit-link.qmd) and [complementary log-log](complementary-log-log-link.qmd) offer other response curves. [Generalised estimating equations](generalised-estimating-equations.qmd) address clustered outcomes when repeated observations make the independence approximation unsuitable.{{cite:geyer2022_exp_family}} (§7.1){{cite:nelder_wedderburn1972}} (§§1.1–1.2, pp. 371–372)

## Check yourself

**1. Event and variance.** If a fitted Bernoulli probability is $0.8$, what are the conditional mean and variance of the binary outcome?

::: {.callout-tip collapse="true" title="Answer"}
The mean is $0.8$ and the variance is $0.8(0.2)=0.16$. A higher probability need not mean a higher variance: the Bernoulli variance peaks at probability $0.5$.{{cite:geyer2022_exp_family}} (§7.1)
:::

**2. Link choice.** Does choosing a probit instead of a logit change the Bernoulli likelihood for a given fitted probability?

::: {.callout-tip collapse="true" title="Answer"}
No. For a given $p_i$, an observed zero contributes $1-p_i$ and an observed one contributes $p_i$ under either model. The link changes how predictors determine $p_i$, and so it can change the fitted probabilities and coefficients.{{cite:nelder_wedderburn1972}} (§§1.1–1.2, 3.3, pp. 371–372, 379–380)
:::

## History

Nelder and Wedderburn's 1972 paper brought binomial regression together with other exponential-family responses under a common likelihood, linear predictor and link structure. They included the older probit setting as one example, making clear that the binary response distribution and the function linking its mean to predictors can be chosen as distinct components. That distinction is what permits logit, probit and other binary links to share the same Bernoulli likelihood.{{cite:nelder_wedderburn1972}} (introduction and §§1, 3.3, pp. 370–380)
