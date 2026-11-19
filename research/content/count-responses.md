## Lead context
Count responses are nonnegative integer outcomes, such as events in a period, and a log link holds their mean positive for every covariate value.

## Motivating example
Take $\log\mu=0.5-0.2x$. At $x=10$,

$$
\mu=\exp(0.5-2)=\exp(-1.5)=0.2231
$$

to four decimals. One extra unit of $x$ multiplies the mean by $e^{-0.2}=0.8187$ to four decimals. The exact mean at $x=11$ is $\exp(-1.7)$, which also rounds to $0.1827$. The mean stays positive. An identity link with the same coefficients would give $0.5-0.2\times 10=-1.5$, which is not a mean count.

## Intuition — A mean that must not cross zero
A count cannot be negative, so its mean cannot be negative either. A linear predictor can be any real number, and an identity link will eventually follow it below zero. The log link writes $\mu=e^{\eta}$, which is positive for every finite $\eta$. On that scale a coefficient is a multiplier: increasing a covariate by one unit multiplies the mean by $e$ to the power of the coefficient. The Poisson distribution is the usual starting random component, with variance equal to the mean. Real counts often vary more than that, which is a fact about the variance function rather than a reason to drop the log link.{{cite:hastie_esl2009}} (Ch. 9, §9.1, p. 296)

## Definition — Nonnegative integers and a log mean
A count response $Y$ takes values in $\{0,1,2,\ldots\}$. In a log-linear specification,

$$
\log\mu=x^\top\beta,
\qquad
\mu=\exp(x^\top\beta),
$$

with $\mu=\mathbb{E}(Y\mid x)$.{{cite:hastie_esl2009}} (Ch. 9, §9.1, p. 296) For a Poisson component, $\operatorname{Var}(Y\mid x)=\mu$. A quasi-Poisson description replaces that variance by $\phi\mu$ with $\phi>0$. The log link is still available; the extra factor $\phi$ is not a second mean.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

## Properties — The multiplier
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $\log\mu(x)=\beta_0+\beta_1 x$, with other covariates held fixed. Then

$$
\frac{\mu(x+1)}{\mu(x)}
=\frac{\exp(\beta_0+\beta_1(x+1))}{\exp(\beta_0+\beta_1 x)}
=\exp(\beta_1).
$$

The ratio does not depend on $x$ or on $\beta_0$. A positive $\beta_1$ multiplies the mean by a constant greater than $1$. A negative $\beta_1$ multiplies it by a constant in $(0,1)$. The identity link would have added $\beta_1$ instead, and that sum can be negative.
:::
:::

## Worked example — A slope on the log scale

**Your turn.** For the same log-linear mean, give $\mu$ at $x=0$ and at $x=1$, to four decimals.

::: {.callout-tip collapse="true" title="Answer"}
At $x=0$, $\mu=\exp(0.5)=1.6487$. At $x=1$, $\mu=\exp(0.3)=1.3499$. The exact ratio $\exp(0.3)/\exp(0.5)$ is $e^{-0.2}$.
:::

## Connections — Poisson, overdispersion and the link
The [Poisson distribution](poisson-distribution.qmd) is the random component with variance equal to the mean. The [log link](log-link.qmd) is the map used above, and it is one of the classical [link functions](link-function.qmd). A [dispersion parameter](dispersion-parameter.qmd) $\phi$ scales the variance when the Poisson variance is too small or too large; it does not change the log-mean equation. A [generalised linear model](generalised-linear-model.qmd) is the combination of that random component, the linear predictor and the link.
