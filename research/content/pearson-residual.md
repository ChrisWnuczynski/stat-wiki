## Lead context
A Pearson residual divides the gap between an observation and its fitted mean by the standard deviation the model gives that mean.

## Motivating example
A count of 7 against a Poisson mean of 2, and a count of 45 against a Poisson mean of 50, are both five away from the fit. The raw gaps are equal. The model standard deviations are $\sqrt{2}$ and $\sqrt{50}$, so the Pearson residuals are $5/\sqrt{2}=3.5355$ and $-5/\sqrt{50}=-0.7071$. The first miss is several model standard deviations. The second is less than one. Dodge's residual is the raw gap $y-\hat y$. The Pearson residual is that gap in the model's own units.{{cite:dodge2008}} (p. 457, residual equals observation minus fitted value)

## Intuition
A probability near 0 or 1, or a Poisson mean near 0, cannot wobble as far as a probability near 1/2 or a large Poisson mean. Judging every $y-\hat\mu$ on the response scale treats those wobbles as comparable. Dividing by $\sqrt{\hat\phi V(\hat\mu)}$ asks instead how many model standard deviations the observation sits from the mean. The sign stays the sign of $y-\hat\mu$. The size becomes comparable across observations only to the extent that the variance function $V$ is right.

## Definition
For a response with mean $\mu$ and variance $\phi V(\mu)$, the Pearson residual at a fitted mean $\hat\mu$ is
$$
r_P=\frac{y-\hat\mu}{\sqrt{\hat\phi\, V(\hat\mu)}}.
$$
For a Poisson observation $\phi=1$ and $V(\mu)=\mu$, so $r_P=(y-\hat\mu)/\sqrt{\hat\mu}$. For a binary observation $V(\mu)=\mu(1-\mu)$. For a normal linear model $V=1$ and $\phi=\sigma^2$, so $r_P$ is the raw residual divided by $\sigma$, or by $s$ if $\sigma$ is estimated. Dodge's $e_i=Y_i-\hat Y_i$ is the numerator.{{cite:dodge2008}} (p. 457, $e_i=Y_i-\hat Y_i$)

## Interpretation — Two misses of size five
$(7-2)/\sqrt{2}=3.5355$. $(45-50)/\sqrt{50}=-0.7071$. The Poisson variance equals the mean, so the same absolute gap is more surprising at the smaller mean. The sign of the second residual is negative because 45 is below 50. Replacing 45 by 55 flips the sign and keeps the absolute value 0.7071. A Poisson distribution is not symmetric, so equal Pearson residuals of opposite sign are not equally likely events. The residual has been scaled to have model variance 1. It has not been transformed into a normal or a symmetric variable.

## Properties — Binary scores
At $\hat p=0.7$, $V=0.7\times0.3=0.21$ and $\sqrt{V}=0.4583$. A success has Pearson residual $(1-0.7)/\sqrt{0.21}=0.6547$. A failure has $(0-0.7)/\sqrt{0.21}=-1.5275$. The failure is the larger residual in absolute value, because 0 is further from 0.7 than 1 is, and the denominator is the same. At $\hat p=0.5$ the two residuals are $(1-0.5)/\sqrt{0.25}=1$ and $(0-0.5)/0.5=-1$. At $\hat p=0.2$ they are $(1-0.2)/\sqrt{0.16}=2$ and $(0-0.2)/0.4=-0.5$. Moving the fitted probability toward the observation shrinks the residual. Moving it toward the other outcome inflates the residual.{{cite:dodge2008}} (p. 457, the residual is what the fitted value does not explain)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
By definition $\Var(Y\mid\mu)=\phi V(\mu)$ when the variance function is correct, so $(Y-\mu)/\sqrt{\phi V(\mu)}$ has mean 0 and variance 1. Substituting the fitted $\hat\mu$ and $\hat\phi$ produces $r_P$. The mean and variance are then no longer exactly 0 and 1, because $\hat\mu$ was computed from $Y$. For a single observation with $\mu$ known, the identity is exact.

For the Poisson calculations, $\phi=1$ and $V(\mu)=\mu$, so the denominator is $\sqrt{\mu}$. Then $7-2=5$ and $5/\sqrt{2}=5/\sqrt{2}$. Also $50-45=5$ and $5/\sqrt{50}=1/\sqrt{2}=0.7071$. For the binary observation, $V(p)=p(1-p)$ and the two possible numerators are $1-p$ and $-p$, which are not opposites unless $p=1/2$.{{cite:dodge2008}} (p. 457, numerator $Y-\hat Y$)
:::
:::

## Statistical use — Plots, not a single threshold
Plot Pearson residuals against the fitted mean or the linear predictor. A fan shape, or a curve, says the variance function or the mean function is missing something. A binary plot cannot be a formless cloud: every success lies on $(1-\hat p)/\sqrt{\hat p(1-\hat p)}$ and every failure on $-\hat p/\sqrt{\hat p(1-\hat p)}$. Those two curves are the support, not a missed covariate. A Poisson plot bands once for each integer that appears. The sum of squared Pearson residuals, divided by the residual degrees of freedom, is a dispersion diagnostic. A value far from 1 suggests the $V$ function is scaled wrong, or the mean is wrong, and the diagnostic does not say which.

## Worked example
Poisson, $\hat\mu=2$, $y=7$: $r_P=5/\sqrt{2}=3.5355$. Poisson, $\hat\mu=50$, $y=45$: $r_P=-5/\sqrt{50}=-0.7071$. Binary, $\hat p=0.2$, $y=1$: $r_P=0.8/0.4=2$. Binary, $\hat p=0.2$, $y=0$: $r_P=-0.2/0.4=-0.5$. The success at a small fitted probability is a larger Pearson residual than the failure. That matches the distance on the probability scale: 1 is 0.8 away from 0.2, and 0 is only 0.2 away, and both are divided by the same 0.4.

**Your turn.** For a Poisson mean of 8, find the Pearson residual of $y=14$ and of $y=2$.

::: {.callout-tip collapse="true" title="Answer"}
The denominator is $\sqrt{8}=2.8284$. Then $(14-8)/2.8284=2.1213$ and $(2-8)/2.8284=-2.1213$. The absolute gaps are equal, so the absolute Pearson residuals are equal. The Poisson probabilities of 14 and of 2, given mean 8, are not equal. Equal residuals are not equal likelihoods.{{cite:dodge2008}} (p. 457, scale the gap only after it is defined)
:::

## Common misconceptions
The Pearson residual is not the raw residual. Dodge's $e_i$ is the numerator. It is not the deviance residual either. The deviance residual scores the observation by its contribution to the likelihood, not by the variance function. At a Poisson mean of 2 the Pearson residual of 7 is 3.5355, while a deviance residual uses $7\log(7/2)-(7-2)$ inside a square root and comes out smaller. A Pearson residual of 2 is not automatically an outlier in a binary regression: at $\hat p=0.2$ the success has residual exactly 2, and a success is a possible outcome. The plot of binary Pearson residuals is two curves. Seeing those curves is the model, not a discovery.

## Assumptions and limits — When the denominator is the wrong scale
If the variance is not $\phi V(\mu)$, dividing by $\sqrt{\hat\phi V(\hat\mu)}$ standardises to the wrong unit. Overdispersed counts, with variance larger than the mean, produce Pearson residuals that look too big if $\phi$ is left at 1. The remedy is a larger $\phi$, or a different $V$, not an automatic deletion of the large points. If $\hat\mu=0$ for a Poisson observation the denominator vanishes. A fitted mean of 0 is a boundary problem, and the residual is not defined by the displayed ratio. If the observations are dependent, each $r_P$ can still be computed, and the collection is not a set of variance-1 uncorrelated numbers. A sum of squares then overstates how much evidence the residuals contain.

## Connections
The [deviance residual](deviance-residual.qmd) uses the likelihood contribution instead of the variance function. A [generalised linear model](generalised-linear-model.qmd) is where $V(\mu)$ is chosen by the family. The ordinary [residual](error-and-residual.qmd) is the numerator Dodge defines. An [inverse Gaussian](inverse-gaussian-distribution.qmd) or [gamma](gamma-distribution.qmd) family changes $V$ and therefore changes the denominator.{{cite:dodge2008}} (p. 457, residual as observation minus fit)

## Check yourself

### One cell in a count model {#self-check-ex-inf-pearson-one-cell}

A Poisson mean is 18 and the count is 27. What is the Pearson residual?

[Question-bank page](../questions/ex-inf-pearson-one-cell.qmd)

::: {.callout-tip collapse="true" title="Answer"}
$(27-18)/\sqrt{18}=9/\sqrt{18}=9/(3\sqrt{2})=\sqrt{18}/2=2.1213$. The same absolute residual would attach to a count of 9, which is 9 below the mean. The two counts are not equally probable.{{cite:dodge2008}} (p. 457, gap divided by a scale)
:::

### A log-link mean {#self-check-ex-ur-log-link}

Why can a Pearson residual of a count be large when the raw gap $y-\hat\mu$ is moderate?

[Question-bank page](../questions/ex-ur-log-link.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The denominator is $\sqrt{\hat\mu}$ for a Poisson model. A moderate gap on top of a small mean is many standard deviations. The count 7 against mean 2 has gap 5 and Pearson residual 3.5355. The count 45 against mean 50 has the same gap and Pearson residual $-0.7071$.{{cite:dodge2008}} (p. 457, the fitted value sets the comparison)
:::

## History
Dodge defines a residual as the difference between the observed value and the fitted value, the part the regression equation does not explain. Scaling that difference by a model standard deviation is the further step that makes residuals from different means comparable when the variance depends on the mean. The Poisson and binary arithmetic above is that scaling, with $\phi=1$ and with $V(\mu)=\mu$ or $V(p)=p(1-p)$.{{cite:dodge2008}} (p. 457, Residual)
