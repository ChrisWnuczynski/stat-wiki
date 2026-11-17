## Motivating example
Suppose a study records whether each person develops an infection and also records an exposure level. Ordinary linear regression can predict probabilities below zero or above one and imposes constant error variance. A generalized linear model instead starts with a binary response distribution, builds a predictor from exposure, and maps that predictor to a probability. Each choice answers a different question: which outcomes are possible, how covariates enter, and how the resulting mean stays in its valid range.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

## Intuition
The response distribution controls the kind of random outcome and its mean–variance relationship. The linear predictor collects explanatory variables into one number, $\eta_i=\mathbf x_i^\top\boldsymbol\beta$. The link connects the mean to that number through $g(\mu_i)=\eta_i$. For Bernoulli data, $\mu_i$ is a probability. A logit link makes any real $\eta_i$ correspond to a probability strictly between zero and one. For counts, a Poisson distribution with log link gives a positive mean. The three choices fit together, but selecting a distribution does not by itself dictate the scientifically useful link.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

## Definition
A conventional GLM specifies conditionally independent responses from an exponential-dispersion family, a systematic predictor $\eta_i=\mathbf x_i^\top\boldsymbol\beta$, and a link $g$ satisfying $g\{E(Y_i\mid\mathbf x_i)\}=\eta_i$. The first choice determines a variance function, possibly with a dispersion parameter. The second specifies which transformed covariates, interactions and offsets are present. The third sets the scale on which those effects add. The model is complete only after all three are stated. In R, the formula describes the predictor and the `family` object supplies both the response family and link.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

The term *random component* here refers to a response family; it should not be confused with a random effect in a mixed model. A *canonical link* makes the linear predictor equal to the family's natural parameter in a chosen exponential-family parametrization. Poisson with log link and Bernoulli with logit link are familiar examples. A canonical link is mathematically convenient, but another valid link can better express the scientific effect of interest.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

## Interpretation — What each choice contributes
For Bernoulli responses with logit link, $\log\{p_i/(1-p_i)\}=\beta_0+\beta_1x_i$ gives an odds ratio $e^{\beta_1}$ for a one-unit increase in $x_i$. The Bernoulli family separately supplies variance $p_i(1-p_i)$. A probit link could use the same Bernoulli response and the same linear predictor, but it would put the slope on a standard-normal quantile scale. Changing the link changes coefficient interpretation even if the possible observations remain zero and one.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

For a Poisson count with log link, $\mu_i=e^{\eta_i}$ and a unit change in a predictor multiplies the expected count by $e^{\beta_1}$, while the Poisson variance equals $\mu_i$. If the observed conditional spread is larger, the three-part specification may need a different variance account, such as quasi-Poisson or negative binomial. Replacing only the link cannot repair an inadequate response distribution.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

## Properties — Canonical links and moments
In the exponential-family form $f(y\mid\theta,\phi)=\exp\{[y\theta-b(\theta)]/a(\phi)+c(y,\phi)\}$, the mean is $b'(\theta)$ and variance is $b''(\theta)a(\phi)$. The natural parameter $\theta$ need not itself equal the mean. For Bernoulli, $\theta=\log\{p/(1-p)\}$; for Poisson, $\theta=\log\mu$; and for a normal family with fixed variance, the identity link is canonical under the usual mean parametrization. Gamma conventions can differ by a sign in the canonical parameter, which is why the inverse link should be stated with its domain. These examples explain why the canonical link depends on the response family.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For Bernoulli $Y\in\{0,1\}$, $f(y\mid p)=p^y(1-p)^{1-y}=\exp\{y\log[p/(1-p)]+\log(1-p)\}$. Thus its natural parameter is $\theta=\log[p/(1-p)]$ and its canonical link is logit. Since $b(\theta)=\log(1+e^\theta)$, differentiation gives $b'(\theta)=e^\theta/(1+e^\theta)=p$ and $b''(\theta)=p(1-p)$.

For Poisson $Y$, $f(y\mid\mu)=e^{-\mu}\mu^y/y!=\exp\{y\log\mu-\mu-\log(y!)\}$. Its natural parameter is $\theta=\log\mu$ and $b(\theta)=e^\theta$, so $b'(\theta)=b''(\theta)=\mu$. This yields the log canonical link and equal mean and variance. Both derivations identify the response-family part before any covariates are put into $\eta_i$.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)
:::
:::

## Statistical use — Specifying a GLM in practice
First identify the response's support and sampling arrangement: a single binary result, a count over a stated exposure, or a positive continuous measurement require different families. Then choose covariates and transformations in $\eta$, including offsets for known exposure where appropriate. Finally choose a link whose inverse respects the mean's range and whose coefficients answer the study's question. Check that the fitted mean and residual spread are credible; a neat coefficient interpretation does not guarantee an adequate variance model.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

The standard normal linear model is a GLM with normal responses, identity link and constant variance. Logistic regression uses Bernoulli responses and often a logit link. Gamma regression can use a log link when multiplicative effects on a positive mean are clearer than an inverse-mean effect. These are instances of one construction, not unrelated algorithms that happen to share software. R's `glm` represents a model using a formula and a family object, and its default fitter uses iteratively reweighted least squares.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374){{cite:rstats_glm2026}} (Description, Arguments and Details)

## Worked example
Let $Y_i$ indicate an infection and let $x_i$ be zero for unexposed and one for exposed. Choose Bernoulli responses, predictor $\eta_i=\beta_0+\beta_1x_i$, and logit link. Suppose $\beta_0=0$ and $\beta_1=\log3$. For $x=0$, $\eta=0$ and $p=e^0/(1+e^0)=1/2=0.50$. For $x=1$, $\eta=\log3$ and $p=3/(1+3)=3/4=0.75$. The odds rise from one to three, an odds ratio of three; the probability rises by $0.25$ and its ratio is $0.75/0.50=1.5$. These are different effect summaries. The Bernoulli variance is $0.50(0.50)=0.25$ in the first group and $0.75(0.25)=0.1875$ in the second, demonstrating that the family controls spread while the link and predictor control the two means.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

**Your turn.** Keep a linear predictor $\eta=\beta_0+\beta_1x$, but let $Y$ be a Poisson count with log link. If $\beta_0=\log4$ and $\beta_1=\log(1.5)$, find the means and variances at $x=0$ and $x=1$, and the multiplicative mean effect of one unit of $x$.

::: {.callout-tip collapse="true" title="Answer"}
At $x=0$, $\mu=e^{\log4}=4$ and the Poisson variance is $4$. At $x=1$, $\mu=e^{\log4+\log1.5}=4(1.5)=6$ and the variance is $6$. Increasing $x$ by one multiplies the mean by $e^{\beta_1}=1.5$. The log link makes the means positive; the Poisson family supplies the variance equality.
:::

## Common misconceptions
Choosing a Bernoulli family does not force a logit link; probit and complementary log–log links also map a predictor to a valid probability. A link acts on the *conditional mean*, so $\log\mu_i=\eta_i$ does not assert that $\log Y_i$ has normal errors. A linear predictor is linear in coefficients, although a covariate column can be a transformation such as log dose. Finally, a canonical link is convenient but is not a requirement of the GLM definition.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

## Assumptions and limits — When a component fails
An ordinary Poisson GLM for outbreak counts can understate uncertainty when units share an unobserved exposure and variance exceeds the mean. A logit Bernoulli model cannot represent a measured outcome of two unless the outcome is recoded as a number of successes with a specified number of trials. A gamma GLM with inverse link can produce an invalid nonpositive fitted mean if a proposed predictor leaves its allowed domain; using a log link keeps the mean positive. And if repeated outcomes from one patient remain dependent after covariates are specified, the conditional-independence assumption in the ordinary GLM is violated. Each failure points to a different component or sampling assumption.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

## Connections
The [linear predictor](linear-predictor.qmd) specifies additive covariate effects, the [link function](link-function.qmd) connects that scale to the mean, and the [exponential family](exponential-family.qmd) supplies familiar response distributions. A [canonical link](canonical-link.qmd) matches the predictor to a natural parameter. [Overdispersion](overdispersion.qmd) shows why checking the family variance matters after the three pieces have been chosen. These connections are useful when transferring an idea from logistic to Poisson or gamma regression without confusing response, mean and predictor.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

## History
Nelder and Wedderburn's 1972 paper assembled normal, binomial, Poisson and gamma examples under a common exponential-family regression framework with a link to a linear predictor. Bailey's account of Nelder's work describes the shared fitting scheme that made these examples part of one method. Later software preserved the distinction among formula, family and link in its model specification.{{cite:bailey2011_nelder}} (p. 23, slide 23 of 32, “1972 paper on generalized linear models”)
