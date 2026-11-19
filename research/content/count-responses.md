## Lead context
A log link writes that mean as an exponential of the linear predictor, so the mean stays positive for every finite covariate pattern. An identity link with the same coefficients need not.

## Motivating example — A log mean stays positive when the predictor is large
Take $\log\mu=0.5-0.2x$. At $x=10$,

$$
\mu=\exp(0.5-2)=\exp(-1.5)=0.2231
$$

to four decimals. One extra unit of $x$ multiplies the mean by $e^{-0.2}=0.8187$ to four decimals. The exact mean at $x=11$ is $\exp(-1.7)$, which also rounds to $0.1827$. The mean stays positive. An identity link with the same coefficients would give $0.5-0.2\times 10=-1.5$, which is not a mean count.

## Intuition — A mean that must not cross zero
A count cannot be negative, so its mean cannot be negative either. A linear predictor can be any real number, and an identity link will eventually follow it below zero. The log link writes $\mu=e^{\eta}$, which is positive for every finite $\eta$. That is why an additive model for the mean is a poor default for counts: every linear combination $\eta=\mathbf{x}^\top\boldsymbol{\beta}$ is negative for some parameter values and some covariate values, even when it stays positive inside the observed window.{{cite:mccullagh_nelder1989}} (§1.2.7, p. 15; §2.2.3, p. 31) On the log scale a coefficient is a multiplier. Increasing a covariate by one unit multiplies the mean by $e$ to the power of the coefficient, and a contrast of log means is reported as a multiplicative effect on the original scale.{{cite:mccullagh_nelder1989}} (§1.2.7, pp. 14–15; §2.2.3, p. 31){{cite:hastie_esl2009}} (Ch. 9, §9.1, p. 296)

The Poisson distribution is the usual starting random component. It has a single adjustable parameter, the mean, and the mean, the variance and every cumulant equal that mean.{{cite:mccullagh_nelder1989}} (§6.2.1, p. 195){{cite:ver_hoef_boveng2007}} (p. 2766) Real counts often vary more than that. The extra variation is a fact about the variance function, not a reason to drop the log link: the variance assumption is usually less important than the choice of link and covariates.{{cite:mccullagh_nelder1989}} (§6.1, pp. 193–194)

## Definition — Nonnegative integers and a log mean
A count response $Y$ takes values in $\{0,1,2,\ldots\}$. For a Poisson sample the set of possible values is the non-negative integers, with no finite upper limit.{{cite:mccullagh_nelder1989}} (§6.2.1, p. 194; §1.2.7, p. 15) In a log-linear specification,

$$
\log\mu=x^\top\beta,
\qquad
\mu=\exp(x^\top\beta),
$$

with $\mu=\mathbb{E}(Y\mid x)$.{{cite:mccullagh_nelder1989}} (§6.1, eq. 6.2, p. 194){{cite:hastie_esl2009}} (Ch. 9, §9.1, p. 296) For a Poisson component, $\operatorname{Var}(Y\mid x)=\mu$, which is the case $\theta=\ln\mu$ and $V=\mu$ of the 1972 exponential-family scheme.{{cite:nelder_wedderburn1972}} (§3.2, p. 378) A quasi-Poisson description replaces that variance by $\phi\mu$ with $\phi>0$, the working form $\operatorname{var}(Y)=\sigma^2\mathbb{E}(Y)$. The log link is still available. The extra factor is a dispersion, not a second mean, and it can be smaller than one as well as larger.{{cite:mccullagh_nelder1989}} (§6.1, eq. 6.1, pp. 193–194){{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

## Properties — The multiplier
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $\log\mu(x)=\beta_0+\beta_1 x$, with other covariates held fixed. Then

$$
\frac{\mu(x+1)}{\mu(x)}
=\frac{\exp(\beta_0+\beta_1(x+1))}{\exp(\beta_0+\beta_1 x)}
=\exp(\beta_1).
$$

The ratio does not depend on $x$ or on $\beta_0$. A positive $\beta_1$ multiplies the mean by a constant greater than $1$. A negative $\beta_1$ multiplies it by a constant in $(0,1)$. The identity link would have added $\beta_1$ instead, and that sum can be negative. The cancellation is the same one that turns additive effects on $\eta$ into multiplicative effects on $\mu$.{{cite:mccullagh_nelder1989}} (§1.2.7, pp. 14–15; §2.2.3, p. 31)
:::
:::

## Worked example — A slope on the log scale

**Your turn.** For the same log-linear mean, give $\mu$ at $x=0$ and at $x=1$, to four decimals.

::: {.callout-tip collapse="true" title="Answer"}
At $x=0$, $\mu=\exp(0.5)=1.6487$. At $x=1$, $\mu=\exp(0.3)=1.3499$. The exact ratio $\exp(0.3)/\exp(0.5)$ is $e^{-0.2}$.
:::

## Connections — Poisson, overdispersion and the link
The [Poisson distribution](poisson-distribution.qmd) is the random component with variance equal to the mean. The [log link](log-link.qmd) is the map from the linear predictor to that positive mean, and it is one of the classical [link functions](link-function.qmd). A [dispersion parameter](dispersion-parameter.qmd) $\phi$ scales the variance when the Poisson variance is too small or too large; it does not change the log-mean equation.{{cite:mccullagh_nelder1989}} (§6.1, pp. 193–194) A [generalised linear model](generalised-linear-model.qmd) is the combination of that random component, the linear predictor and the link. When the variance is instead a multiple of the mean with the multiple greater than one, the same log mean is the quasi-Poisson regression used for overdispersed counts.{{cite:ver_hoef_boveng2007}} (p. 2767, eq. 1)

## Check yourself
### A doubling covariate step
For the mean $\log\mu=0.5-0.2x$, by what factor does $\mu$ change when $x$ increases by $2$? Give the factor to four decimals.

::: {.callout-tip collapse="true" title="Answer"}
The factor is $e^{-0.4}=0.6703$. Two steps of $e^{-0.2}$ multiply, and $(e^{-0.2})^2=e^{-0.4}$.
:::

### Where the identity fails
An identity specification $\mu=2-0.5x$ is used for a count. At what $x$ does the formula stop being a mean?

::: {.callout-tip collapse="true" title="Answer"}
$\mu=0$ at $x=4$, and $\mu<0$ for every $x>4$. A mean count cannot be negative, so the identity formula is not a count mean on the whole line. The log link does not have that break.
:::

## History — Multiplicative effects inside the 1972 model
Log-linear models for counts replaced the classical model's additive systematic effects and Normal errors by multiplicative effects and a nominal Poisson distribution. Writing $\mu=\exp(\eta)$ keeps $\mu$ positive for every parameter value and every covariate value.{{cite:mccullagh_nelder1989}} (§1.2.7, pp. 14–16) Nelder and Wedderburn's 1972 paper set that Poisson case inside the generalised linear model, with natural parameter $\theta=\ln\mu$ and variance function $V=\mu$. They named contingency tables as its main application.{{cite:nelder_wedderburn1972}} (§3.2, p. 378)
