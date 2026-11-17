## Lead context
A positive continuous response is a measurement that can take any value above zero, so its mean has to stay positive even when a linear predictor would not.

## Motivating example
A log mean $0.5+0.2x$ equals $e^{0.5}\approx 1.649$ at $x=0$ and $e^{0.9}\approx 2.460$ at $x=2$. Each extra unit of $x$ multiplies the mean by $e^{0.2}$. The inverse predictor $0.4-0.2x$ is negative at $x=3$, and the reciprocal is not a positive mean.

## Intuition — The link is chosen separately from the scatter
A clotting time or a claim amount cannot be negative. In a generalised linear model the distribution and the link are separate pieces. The gamma family sits in the exponential dispersion family with the normal, exponential, Poisson and binomial, and the variance has the form $\phi V(\mu)$. The link $\eta=g(\mu)$ is what turns that mean into an unrestricted linear predictor $\eta=x^\top\beta$.{{cite:mccullagh1992_glm_intro}} (p. 544, the family and the link)

## Definition — A mean that stays positive
The log link sets $\log\mu=x^\top\beta$, so $\mu=\exp(x^\top\beta)$. Every finite predictor then gives a positive mean, and increasing one covariate by one unit, with the others held fixed, multiplies the mean by $e^{\beta_j}$. The inverse link $\mu=1/(x^\top\beta)$ is the canonical link for the gamma family. It stays positive only while the linear predictor stays positive. A sign change makes the fitted mean negative, which a positive response cannot have.{{cite:mccullagh1992_glm_intro}} (p. 544, link function)

## Properties — Multiplication under the log link
Let $\log\mu=\beta_0+\beta_1 x$. Then $\mu(x+1)/\mu(x)=e^{\beta_1}$, a factor that does not depend on $x$. The inverse link has no such constant factor: the change in the mean depends on how close the predictor is to zero.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
If $\log\mu(x)=\beta_0+\beta_1 x$, then $\mu(x)=\exp(\beta_0+\beta_1 x)$. The exponential of a real number is positive, so the mean cannot leave $(0,\infty)$. The ratio of means one unit of $x$ apart is
$$
\frac{\mu(x+1)}{\mu(x)}=\exp(\beta_1),
$$
because the terms in $x$ cancel. For the inverse link, $\mu=1/\eta$ is positive only when $\eta>0$, and $\eta=0$ makes the expression undefined.{{cite:mccullagh1992_glm_intro}} (p. 544, the link)
:::
:::

## Worked example
Take $\log\mu=0.5+0.2x$. At $x=0$ the mean is $e^{0.5}\approx 1.649$. At $x=2$ it is $e^{0.9}\approx 2.460$. Each extra unit of $x$ multiplies the mean by $e^{0.2}\approx 1.221$, and two such steps multiply $e^{0.5}$ by $e^{0.4}$ to give $e^{0.9}$. The inverse predictor $\eta=0.4-0.2x$ equals $0.2$ at $x=1$, so the fitted mean is $1/0.2=5$. At $x=3$ the predictor is $-0.2$, and $1/(-0.2)=-5$ is not a legal mean for a positive response.{{cite:mccullagh1992_glm_intro}} (p. 544, link function)

**Your turn.** Let $\log\mu=\log 10+0.1x$. Find the mean at $x=0$ and at $x=3$.

::: {.callout-tip collapse="true" title="Answer"}
At $x=0$ the mean is $10$. At $x=3$ it is $10e^{0.3}\approx 13.499$. The factor for three units is $e^{0.3}\approx 1.350$, not three times the one-unit factor $e^{0.1}$.
:::

## Connections
The log link is the same construction used for a [Poisson](poisson-distribution.qmd) mean. Gamma and Poisson are different members of the family, so they do not share the variance function $V(\mu)$ that multiplies the dispersion $\phi$. The [gamma distribution](gamma-distribution.qmd) is the continuous positive member named on that list. An identity link can leave the positive half-line as soon as the predictor does.{{cite:mccullagh1992_glm_intro}} (p. 544, gamma in the family and $\phi V(\mu)$)

