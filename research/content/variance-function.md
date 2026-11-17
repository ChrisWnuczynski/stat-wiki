## Motivating example

If the mean number of arrivals in an hour rises from $2$ to $6$, a Poisson model raises the variance from $2$ to $6$ as well. For positive reaction times, a Gamma model with fixed shape can instead make the variance proportional to the *square* of the mean: tripling the mean multiplies the variance by $9$. The regression's mean curve alone does not say which description of scatter is credible. A variance function supplies that missing part{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374).

## Definition

Write $\mu_i=\operatorname{E}(Y_i\mid\boldsymbol{x}_i)$ for the conditional mean at predictor setting $\boldsymbol{x}_i$. A generalized linear model specifies
$$
\operatorname{Var}(Y_i\mid\boldsymbol{x}_i)=\phi V(\mu_i)/w_i,
$$
where $V$ is the *variance function*, $\phi>0$ is a common dispersion scale, and $w_i>0$ is a known prior weight when that convention is used. With unit weights the formula is $\phi V(\mu_i)$. The function is defined on the attainable mean domain and must be nonnegative there. The link $g(\mu_i)=\boldsymbol{x}_i^{\mathsf T}\boldsymbol\beta$ is a different object: it describes the mean's dependence on predictors, while $V$ describes spread conditional on that mean{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374).

The usual unit-weight choices are $V(\mu)=1$ for a normal response, $V(\mu)=\mu$ for a Poisson count, $V(\mu)=\mu(1-\mu)$ for a Bernoulli outcome, $V(\mu)=\mu^2$ for a Gamma response, and $V(\mu)=\mu^3$ for an inverse Gaussian response. The scale is not always free: ordinary Poisson and Bernoulli models fix $\phi=1$, whereas a normal GLM estimates its residual variance and a Gamma GLM estimates its dispersion. For a binomial *proportion* formed from $m$ trials, the variance is $\mu(1-\mu)/m$, making the denominator part of the observation's precision{{cite:wuthrich_merz2022_glm}} (§5.4).

## Interpretation

The variance function is a pattern of heteroscedasticity tied to the mean, not a separate variance estimate for every observation. Under a Poisson model, a group expected to produce twice as many counts has twice the variance. Under a Gamma model with common $\phi$, doubling the mean quadruples the variance and doubles the standard deviation, so the coefficient of variation stays at $\sqrt\phi$. For a Bernoulli outcome, variance is largest at $\mu=1/2$ and shrinks toward zero as the probability approaches either boundary. Each pattern follows from the response family, not from a change in link{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374).

An empirical mean–variance plot can suggest a family, but repeated observations or grouping are needed to see spread at comparable means. A sample with only one outcome at each predictor setting cannot directly reveal the conditional variance without smoothing or model assumptions. Residual diagnostics then check whether the chosen relation is plausible.

## Properties

For a regular one-parameter exponential-family density written as $f(y;\theta,\phi)=\exp\{[y\theta-b(\theta)]/\phi+c(y,\phi)\}$, differentiation of its normalizing identity gives $\mu=b'(\theta)$ and $\operatorname{Var}(Y)=\phi b''(\theta)$. Since $b'$ maps the canonical parameter to the mean, the family supplies $V(\mu)=b''\{(b')^{-1}(\mu)\}$. This is why a variance function is built into the standard family choices. Choosing $V$ alone, however, does not specify every feature of a response distribution; a quasi-likelihood can use the mean and variance relation without claiming a full probability law{{cite:wuthrich_merz2022_glm}} (§5.4).

The variance relation also controls precision in estimating the mean curve. For an independent GLM observation with linear predictor $\eta_i$, its Fisher-scoring weight is proportional to $[d\mu_i/d\eta_i]^2/[\phi V(\mu_i)]$. A larger conditional variance gives less weight when the derivative of the mean with respect to the predictor is held fixed. Thus a wrong variance function can give misleading model-based standard errors even when a plausible mean curve has been fitted.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Assume differentiation can pass under the integral. Normalization gives $1=\int f(y;\theta,\phi)\,dy$. Differentiating with respect to $\theta$ yields $0=\operatorname{E}[(Y-b'(\theta))/\phi]$, so $\operatorname{E}Y=b'(\theta)$. Differentiating once more, or differentiating that expectation using the score, gives $d\operatorname{E}Y/d\theta=\operatorname{Var}(Y)/\phi=b''(\theta)$. Hence $\operatorname{Var}(Y)=\phi b''(\theta)$. For a Gamma response with shape $1/\phi$ and rate $1/(\phi\mu)$, the elementary Gamma mean and variance formulas give $\operatorname{E}Y=\mu$ and $\operatorname{Var}(Y)=\phi\mu^2$; therefore $V(\mu)=\mu^2$. The same calculation for a Bernoulli indicator gives $\operatorname{E}Y=\mu$ and $\operatorname{Var}(Y)=\mu-\mu^2=\mu(1-\mu)${{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374).
:::
:::

## Statistical use — Choosing and checking a spread model

Begin with the response's support: counts, binary outcomes and positive continuous measurements cannot automatically share one variance rule. Compare observed spread at similar fitted means, inspect Pearson or deviance residuals, and ask whether high fitted values show more scatter than the chosen function allows. A Poisson count model with variance much greater than its mean may need a quasi-Poisson or negative-binomial alternative; the latter is a full count distribution with a different variance relation, while quasi-Poisson retains $V(\mu)=\mu$ and estimates a free scale $\phi${{cite:wuthrich_merz2022_glm}} (§5.4).

The choice matters even in a joint model with several kinds of responses. Each component of a vector response can have its own marginal variance function. A Gamma reaction time makes variance grow with the square of the mean, while a count component can use a different variance function{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374).

If counts contain excess zeros or unmodelled heterogeneity, their conditional spread can exceed $\mu$ even when the fitted mean curve looks reasonable; Poisson standard errors may then be too small. If Bernoulli outcomes from the same household are correlated, the variance of a household total is not the sum of isolated Bernoulli variances because covariance terms remain. A Gamma variance function on data containing genuine zero or negative values clashes with the Gamma response support. And estimating a free quasi dispersion changes standard errors, but cannot repair an incorrectly specified mean curve{{cite:wuthrich_merz2022_glm}} (§5.4).
## Worked example

Suppose reaction times in two temperature groups have fitted means $\mu_1=2$ and $\mu_2=6$ minutes. A Gamma model with $\phi=1/4$ predicts variances $(1/4)2^2=1$ and $(1/4)6^2=9$ square minutes, hence standard deviations $1$ and $3$ minutes. Both groups have coefficient of variation $1/2$. A Poisson variance function evaluated at the same numerical means would instead give variances $2$ and $6$, but Poisson outcomes are counts, not continuous reaction times. The numerical comparison isolates what $V$ does; it does not make Poisson a plausible response law for time{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374).

For binary outcomes, probabilities $0.2$ and $0.8$ both have Bernoulli variance $0.16$, whereas probability $0.5$ has variance $0.25$. The spread is largest in the middle of the probability scale rather than at its high end{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374).

**Your turn.** A Gamma model has $\phi=1/2$. Find its predicted variances when the fitted means are $3$ and $6$, and explain how doubling the mean changes the standard deviation.

::: {.callout-tip collapse="true" title="Answer"}
With $V(\mu)=\mu^2$, the variances are $(1/2)3^2=4.5$ and $(1/2)6^2=18$. Their standard deviations are $\sqrt{4.5}\approx2.121$ and $\sqrt{18}\approx4.243$: doubling the mean quadruples variance and doubles standard deviation.
:::

## Common misconceptions

The link function does not determine the variance function: a log link can accompany Poisson or Gamma responses, whose variances grow at different rates. Freeing $\phi$ in a quasi-Poisson model does not turn its counts into Gamma observations; it scales the Poisson-shaped mean–variance relation. Observing variance greater than the mean in one small group does not by itself prove overdispersion, since sample variances fluctuate. Finally, selecting $V(\mu)$ is not the same as specifying a full distribution; quasi-likelihood deliberately works with fewer assumptions{{cite:wuthrich_merz2022_glm}} (§5.4).

## Connections

The [dispersion parameter](dispersion-parameter.qmd) multiplies $V$ without changing its shape. A [link function](link-function.qmd) maps the conditional mean into a linear predictor. [Quasi-likelihood](quasi-likelihood.qmd) uses a specified mean and variance relation without a full distribution, while the [Pearson dispersion ratio](pearson-dispersion-ratio.qmd) helps diagnose departures from a nominal variance. The [negative binomial distribution](negative-binomial-distribution.qmd) supplies a count model whose variance can rise faster than its mean{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374).

## History

The generalized linear model framework put normal, Poisson, binomial and Gamma responses into one family of mean models, making their different mean–variance relations comparable. Later quasi-family implementations made the variance function an explicit input, so an analyst could model dispersion without a fully specified likelihood. R's `family` objects name a variance component for every family and accept user-specified variance forms for `quasi`.{{cite:rstats_family2026}} (§Description; Arguments, `variance`; Value)
