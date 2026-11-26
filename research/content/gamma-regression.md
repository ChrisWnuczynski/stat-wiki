## Lead context
Gamma regression describes a positive response whose variability grows with its mean, with a separate choice of link for that mean.

## Motivating example
An insurer may need the expected size of a positive claim at several vehicle ages. A model with a common response variance treats variation at small and large means alike. A gamma GLM instead permits the standard deviation to grow in proportion to the conditional mean. Zero claims require a different response model or a separate frequency component.{{cite:wuthrich_merz2022_glm}} (§5.3.7, pp. 167–169)

## Definition — Mean, shape and dispersion
For independent positive responses, write
$$
Y_i\sim\operatorname{Gamma}\left(\text{shape}=\phi^{-1},\ \text{scale}=\phi\mu_i\right),\qquad\phi>0.
$$
Then $\E(Y_i)=\mu_i$ and $\operatorname{Var}(Y_i)=\phi\mu_i^2$. A common dispersion gives a common coefficient of variation $\sqrt\phi$. This uses the scale convention; the corresponding rate is $1/(\phi\mu_i)$. Stating the convention prevents a reciprocal parameter from changing the model.{{cite:wuthrich_merz2022_glm}} (§5.3.7, pp. 168–169, eqs. 5.43–5.44)

The gamma exponential-family canonical parameter is $-1/\mu$. An inverse link $1/\mu$ is often described as canonical after absorbing its constant sign into the coefficients. The log link, $\log\mu_i=x_i^\top\beta$, is not canonical, but automatically ensures a positive fitted mean for every finite predictor vector. Neither choice asserts that $\log Y_i$ is normally distributed.{{cite:nelder_wedderburn1972}} (§3.4, p. 380){{cite:wuthrich_merz2022_glm}} (§5.3.7, p. 167)

## Properties — The log link simplifies the information
Ignoring terms independent of $\beta$, the log-link gamma log-likelihood is
$$
\ell(\beta)=-\phi^{-1}\sum_i\left(y_i e^{-x_i^\top\beta}+x_i^\top\beta\right)+C.
$$
Differentiation gives
$$
U(\beta)=\phi^{-1}X^\top(y/\mu-\mathbf1),\qquad
\nabla^2\ell=-\phi^{-1}X^\top\operatorname{diag}(y_i/\mu_i)X.
$$
All divisions are coordinatewise. For strictly positive observations and a full-column-rank $X$, this Hessian is negative definite at every finite $\beta$. Taking expectations replaces $y_i/\mu_i$ by one, so the expected information is $X^\top X/\phi$, for unit observation weights. This differs from claiming that the realised Hessian is constant.{{cite:nelder_wedderburn1972}} (§2.1, pp. 372–374){{cite:wuthrich_merz2022_glm}} (§5.3.7, p. 169)

The coefficient score does not involve an unknown common $\phi$ after multiplying through by it. Dispersion still matters for standard errors and predictive variation. One Pearson estimate is
$$
\widehat\phi_P=\frac1{n-p}\sum_i\frac{(y_i-\widehat\mu_i)^2}{\widehat\mu_i^2},
$$
where $p$ is the fitted design rank and $n>p$. Likelihood estimation of shape is a different procedure. Wald intervals from inverse information are large-sample approximations rather than exact gamma-regression confidence intervals.{{cite:wuthrich_merz2022_glm}} (§5.3.1, p. 143, eq. 5.30; §5.3.7, p. 173)

## Interpretation — Relative errors on a positive scale
For fixed dispersion, twice the log-likelihood difference from the saturated fit is $D/\phi$, where the unit-weight unscaled deviance is
$$
D=2\sum_i\left[\frac{y_i-\widehat\mu_i}{\widehat\mu_i}-\log\frac{y_i}{\widehat\mu_i}\right].
$$
Each summand is nonnegative, by $r-1-\log r\ge0$ for $r>0$, with equality at $r=1$. A proportionate error, rather than an absolute error, determines each contribution.{{cite:nelder_wedderburn1972}} (§2.3, p. 375)

## Worked example
For an intercept-only fit to $(2,4,6)$, the score equation gives $\widehat\mu=4$ and $\widehat\beta_0=\log4\approx1.386294$. The Pearson estimate is
$$
\widehat\phi_P=\frac{(2-4)^2+(4-4)^2+(6-4)^2}{(3-1)4^2}=\frac14.
$$
At this fitted dispersion the shape is $4$, scale is $1$, and fitted standard deviation is $2$. The unscaled deviance is $-2\log(3/4)\approx0.575364$, giving scaled deviance $2.301457$. This calculation specifies the fit and its dispersion estimator; it does not provide an exact chi-square test for three observations.{{cite:wuthrich_merz2022_glm}} (§5.3.1, pp. 143–144)

**Your turn.** At a covariate value whose fitted mean is twice as large, what are the fitted standard deviation and change in log-link predictor?

::: {.callout-tip collapse="true" title="Answer"}
The mean is $8$. Keeping $\phi=1/4$ gives standard deviation $\sqrt\phi\mu=4$. The linear predictor increases by $\log2\approx0.693147$.
:::

## Check yourself
### Differentiating a link {#self-check-ex-sl-10-1}
[The logistic derivative](../questions/ex-sl-10-1.qmd): practise the link differentiation used in GLM scores.

::: {.callout-tip collapse="true" title="Answer"}
For $\sigma(\eta)=(1+e^{-\eta})^{-1}$, differentiation gives $\sigma'(\eta)=e^{-\eta}/(1+e^{-\eta})^2=\sigma(\eta)(1-\sigma(\eta))$. Also $\sigma(-\eta)=1-\sigma(\eta)$. Thus a Bernoulli logit model has Hessian $-X^\top\operatorname{diag}(p_i(1-p_i))X$; the gamma log-link Hessian uses different weights.
:::

### Interpreting a variance divisor {#self-check-ex-inf-variance-bias}
[The biased variance estimator](../questions/ex-inf-variance-bias.qmd): distinguish an estimator's scale from its bias.

::: {.callout-tip collapse="true" title="Answer"}
Since $\E(s^2)=\sigma^2$, $\E(((n-1)/n)s^2)=(n-1)\sigma^2/n$. Its bias is $-\sigma^2/n$. Changing a residual divisor affects estimation of dispersion, even when the fitted mean coefficients stay the same.
:::
