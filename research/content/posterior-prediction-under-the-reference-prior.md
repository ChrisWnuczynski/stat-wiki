## Motivating example
A fitted calibration line gives a best estimate of the mean response at a new input. A future measurement also includes a fresh measurement error. These are two different targets, so they require two different uncertainty statements. In Gaussian regression, integrating the coefficient and variance uncertainty under the reference prior produces Student distributions for both targets, with an additional observation-noise term only for the future measurement.{{cite:rasmussen_williams2006}} (§2.1, Bayesian linear regression and predictive distribution)

## Statement

**Rank, residual information and the integration measure.**
Let $y\mid\beta,v\sim N_n(X\beta,vI)$, with $X$ fixed and of full column rank $p$, $v>0$ and prior density $\pi(\beta,v)\propto1/v$ relative to $d\beta\,dv$. Require $\nu=n-p>0$ and $\mathrm{SSE}=\|y-X\widehat\beta\|^2>0$. Define $C=(X^TX)^{-1}$ and $s^2=\mathrm{SSE}/\nu$. Then
$$v\mid y\sim\operatorname{InvGamma}(\nu/2,\mathrm{SSE}/2),\qquad \beta\mid v,y\sim N_p(\widehat\beta,vC).$$
The inverse-Gamma convention is $p(v)\propto v^{-a-1}e^{-b/v}$. Specifying the integration measure is essential: transforming to the standard deviation $\sigma$ introduces the Jacobian $dv=2\sigma\,d\sigma$, giving a density proportional to $1/\sigma$ relative to $d\beta\,d\sigma$. A flat density in one coordinate is generally not flat in another.{{cite:bernardo2005_reference}} (§3.12, Example 23 and equation 38)

For a new vector $x_*$, let $m_*=x_*^T\widehat\beta$ and $h_*=x_*^TCx_*$. The linear mean $x_*^T\beta$ has posterior $t_\nu(m_*,s\sqrt{h_*})$, whereas an independent new response has predictive law $t_\nu(m_*,s\sqrt{1+h_*})$. The mean-response Student statement assumes $h_*>0$; if $x_*=0$, that mean is deterministically zero. Here the second argument is a scale. Its square is a variance only after multiplying by $\nu/(\nu-2)$ when $\nu>2$. At lower degrees of freedom the predictive distribution can be proper without having a finite variance.{{cite:bernardo2005_reference}} (Example 23, equation 38, Student predictive distribution)

## Intuition — The intercept-only case exposes the extra noise
With an intercept as the only coefficient, $h_*=1/n$. The predictive scale is $s\sqrt{1+1/n}$ while the mean scale is $s/\sqrt n$. More observations reduce uncertainty in the mean, but they do not remove the variability of one future draw around that mean. The intercept-only reference predictive distribution is exactly the normal-prediction example obtained by integrating an unknown location and scale.{{cite:bernardo2005_reference}} (§3.12, Example 23)

## Proof
The least-squares normal equations imply the decomposition
$$\|y-X\beta\|^2=\mathrm{SSE}+(\beta-\widehat\beta)^TX^TX(\beta-\widehat\beta).$$
Multiplying the Gaussian likelihood by $1/v$ and integrating the $p$ coefficient coordinates contributes a factor $v^{p/2}$, giving the inverse-Gamma marginal stated above. At fixed $v$, a linear transformation of the normal coefficient posterior has mean $m_*$ and variance $vh_*$. Adding an independent new error changes that variance to $v(1+h_*)$.

To identify the mixture explicitly, let $c$ denote either $h_*$ or $1+h_*$. With $a=\nu/2$ and $b=\mathrm{SSE}/2$, integration over $v$ gives a density proportional to
$$\int_0^\infty v^{-a-3/2}\exp\left[-\frac{b+(z-m_*)^2/(2c)}v\right]dv
\ \propto\ \left[1+\frac{(z-m_*)^2}{\nu s^2c}\right]^{-(\nu+1)/2}.$$
This is the Student kernel with degrees of freedom $\nu$ and scale $s\sqrt c$. Positivity of SSE makes $b>0$, ensuring integrability at zero, and $\nu>0$ ensures integrability at infinity.

## Worked example
### An intercept with five measurements
Take measurements $(2,3,4,5,6)$. Their mean is $4$, SSE is $10$, and $s^2=10/4=2.5$. For a new measurement, $h_*=1/5=0.2$. The mean posterior is $t_4(4,\sqrt{0.5})$, whereas the predictive distribution is $t_4(4,\sqrt3)$. Using the $0.975$ Student quantile $2.776445$, the equal-tailed 95% intervals are $(2.036757,5.963243)$ for the mean and $(-0.808944,8.808944)$ for a new measurement. The centres agree, but the predictive scale is $\sqrt6$ times the mean scale.

**Your turn.** What is the variance of the new-measurement predictive distribution in this example?

::: {.callout-tip collapse="true" title="Answer"}
It is $3\times4/(4-2)=6$. The Student scale squared is 3, and the variance multiplier is 2.
:::

## Statistical use — Leverage is conditional on a valid regression model
For a general design, $h_*$ measures coefficient uncertainty in the new linear predictor. It grows when a prediction uses poorly estimated coefficient directions. However, it does not measure the error from a nonlinear mean, a changing residual variance, dependence between errors or a future population shift. A wide interval from leverage alone is still an interval under the stated linear Gaussian model.{{cite:rasmussen_williams2006}} (§2.1, predictive uncertainty conditional on the linear model)

A proper posterior from an improper reference prior also does not define a normalised prior predictive distribution or an absolute marginal likelihood. The arbitrary multiplicative constant cancels in posterior normalisation and subsequent prediction within the model; it need not cancel when comparing models with different improper priors. Prior specification and the inferential target must therefore be explicit.{{cite:bernardo2005_reference}} (§1, reference prior functions and posterior inference)

Leverage $h_*$ widens the interval when the new predictor lies in a direction the design estimates poorly. That widening is the Gaussian linear model's account of coefficient uncertainty. A curved mean, a variance that changes with the predictor, dependent errors, or a shift in the population that produces the next case are further sources of error, and $h_*$ does not record them. The interval remains the reference-prior interval for the model that was fitted.{{cite:rasmussen_williams2006}} (§2.1, predictive uncertainty conditional on the linear model)
