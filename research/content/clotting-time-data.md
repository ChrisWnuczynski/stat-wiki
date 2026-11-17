## Motivating example
Two laboratory reagents can produce different clotting times even at the same plasma concentration. A useful comparison asks how the mean response changes with concentration and whether the difference between reagents changes along that curve. Positive responses and a nonlinear mean can be handled within the same regression framework.{{cite:nelder_wedderburn1972}} (§§1.1–1.3, pp. 371–372)

## Definition — Mean curves for positive times
Write $c>0$ for concentration, $L\in\{1,2\}$ for reagent lot and $Y>0$ for clotting time. A Gamma model with mean $\mu_L(c)$ and dispersion $\phi>0$ has shape $1/\phi$ and rate $1/(\phi\mu_L(c))$. Its variance is $\phi\mu_L(c)^2$. The coefficient of variation is therefore $\sqrt{\phi}$ at every concentration.{{cite:dodge2008}} (p. 216, Gamma Distribution)

An inverse-link interaction model writes $1/\mu_L(c)=a_L+b_L\log c$, with the predictor restricted to be positive. A log-link model instead writes $\log\mu_L(c)=a_L+b_L\log c$, or $\mu_L(c)=e^{a_L}c^{b_L}$. Both specify conditional means; neither says that the logarithm of an observed time is normally distributed.{{cite:nelder_wedderburn1972}} (§§1.2–1.3, p. 372)

## Properties — Separating shape, mean and extrapolation
Under the inverse link, the derivative of the mean with respect to log concentration is $-b_L/(a_L+b_L\log c)^2$. A positive $b_L$ therefore produces decreasing times wherever the model is defined. The fitted intercept is the reciprocal-mean predictor at $c=1$, not a mean time at zero concentration. The logarithm is undefined at zero. A limiting biological interpretation needs an explicit limit of the fitted curve and an appropriate experimental range.{{cite:nelder_wedderburn1972}} (§1.3, p. 372)

A Gamma model allows positive skew and a constant relative standard deviation. Changing its dispersion changes the scatter around a specified mean curve. Changing the family can also change the fitted mean coefficients: the likelihood equations use variance weights as well as the link.{{cite:nelder_wedderburn1972}} (§2.1, pp. 372–374) For example, a mean of $50$ seconds and dispersion $0.00213$ imply variance $5.325$ seconds squared. This is a model calculation, not a new laboratory observation.{{cite:dodge2008}} (p. 216, Gamma Distribution)

## Worked example — Comparing lots at ten percent
Using the displayed inverse-link coefficients at $c=10$ gives
$$
\widehat\mu_1=\frac{1}{-0.01655+0.01534\log10}=53.2718,\qquad
\widehat\mu_2=\frac{1}{-0.0239+0.0236\log10}=32.8504
$$
seconds. The second mean is lower at this concentration. An intercept comparison alone would miss the effect of the slope and the reciprocal transformation. Refitting the nine observations for each lot rather than rounding the coefficients gives $53.2639$ and $32.8615$ seconds.

**Your turn.** Under the log-link model $\log\mu=a+b\log c$, what is the ratio of the means after doubling concentration?

::: {.callout-tip collapse="true" title="Answer"}
The ratio is $e^{b\log 2}=2^b$. It is independent of the starting concentration.
:::

## Check yourself

Use the definitions and calculations above to work through these questions.

### Gamma means and variances {#self-check-q-45}

[Gamma means and variances](../questions/q-45.qmd). Work parts (b), (c) and (e).

::: {.callout-tip collapse="true" title="Answer"}
The mean is $\mu_i$, the variance is $\mu_i^2/k$, and a unit covariate increase multiplies the mean by $e^{\beta_1}$. A Gamma model for $Y_i$ does not make $\log Y_i$ normal.
:::

### Reaction times on a log link {#self-check-q-55}

[Reaction times on a log link](../questions/q-55.qmd). Interpret the coefficient in part (f).

::: {.callout-tip collapse="true" title="Answer"}
A one-unit temperature increase multiplies the mean by $e^{-0.08}=0.9231$, a decrease of about $7.69\%$. The variance remains proportional to the square of that mean.
:::
