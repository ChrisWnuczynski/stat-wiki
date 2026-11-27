## Motivating example

A count model predicts one case for a site that reports two, and one case for a site that reports none. The raw errors have equal magnitude, but their likelihood contributions depend on the count distribution and its fitted means. Residual deviance measures the total loss of log-likelihood compared with a model that can match every observation exactly. It helps describe fit and compare appropriate nested models, provided the reference distribution and dispersion are handled carefully.

## Intuition — Why fit is measured against saturation

Imagine fitting a separate mean to every observation. This *saturated model* is flexible enough to reproduce the data, so its likelihood sets a benchmark. The fitted regression uses far fewer parameters and generally has lower maximized likelihood. Residual deviance doubles the gap on the log scale. Zero means the fitted model achieves the saturated likelihood; larger values mean a greater likelihood loss. A larger number is not, by itself, a verdict of poor fit, because it also depends on sample size, family and how many parameters were fitted.

## Definition

For a fitted GLM with log-likelihood $\ell(\hat\mu;y)$ and saturated log-likelihood $\ell(y;y)$, the residual deviance is

$$
D_{\mathrm{res}}=2\{\ell(y;y)-\ell(\hat\mu;y)\}
$$

under a unit-dispersion convention.{{cite:nelder_wedderburn1972}} (§2.3, pp. 375–376) Where a dispersion parameter $\phi$ is separated from the likelihood, software commonly reports an unscaled $D$ whose likelihood-ratio scale is $D/\phi$. The associated residual degrees of freedom are usually $n-p$ for $n$ independent observations and a full-rank design with $p$ estimated regression coefficients. “Usually” matters: weights, grouped observations, smoothers and rank deficiency change the accounting.

The *null deviance* uses a baseline fit without fitted covariate effects in place of the stated predictor model. In R's `glm`, that baseline retains any offsets and includes an intercept only if the original model has one, reducing to an intercept-only fit when an intercept and no varying offsets are present.{{cite:rstats_glm2026}} (Sec. Value, null.deviance) Residual deviance uses the actual fitted model. They share the saturated reference when fitted to the same responses under the same family and likelihood convention. These names specify two comparisons with the same saturated benchmark, not two unrelated diagnostics.

## Properties

The saturated fit maximizes the likelihood over a model containing the fitted model, so $D_{\mathrm{res}}\geq0$ when the likelihoods and data are comparable.{{cite:nelder_wedderburn1972}} (§2.3, pp. 375–376) For nested fits on the same data, if model $0$ is contained in model $1$, then

$$
D_0-D_1=2(\ell_1-\ell_0)\geq0
$$

on the unit-dispersion scale. Thus a larger nested model cannot have greater *training* deviance at its true maximum-likelihood fit. The identity is algebraic; a chi-squared reference for the difference needs regularity conditions, and its degrees of freedom are the difference in effective parameter dimensions. It does not license a likelihood-ratio test between a logit and a probit model merely because both were fitted to binary data: they are generally non-nested.

For Poisson counts with fitted means $\hat\mu_i>0$,

$$
D_{\mathrm{res}}=2\sum_i\left[y_i\log\left(\frac{y_i}{\hat\mu_i}\right)-(y_i-\hat\mu_i)\right],
$$

where $0\log(0/\hat\mu_i)$ is defined by its limit as zero. For Bernoulli responses, a success contributes $-2\log\hat p_i$ and a failure contributes $-2\log(1-\hat p_i)$. For a binomial observation with $y_i$ successes in $m_i$ trials, the corresponding contribution is

$$
d_i=2\left\{y_i\log\frac{y_i}{m_i\hat p_i}+(m_i-y_i)\log\frac{m_i-y_i}{m_i(1-\hat p_i)}\right\},
$$

again taking a zero-times-log term as zero. This expression compares the fitted probability with the observed proportion $y_i/m_i$, and reduces to the Bernoulli contributions when $m_i=1$. Grouping independent trials with the same covariates changes the data representation and residual degrees of freedom, so the binomial trial counts should be reported. The contributions are nonnegative and depend on the fitted probability or mean, rather than only on the raw difference $y_i-\hat\mu_i$. With a Gaussian model and common variance $\sigma^2$, the likelihood-ratio scale is $\sum_i(y_i-\hat\mu_i)^2/\sigma^2$; the commonly reported unscaled deviance is the residual sum of squares.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For Poisson $Y_i=y_i$, the log-likelihood at mean $\mu_i$ is $y_i\log\mu_i-\mu_i-\log(y_i!)$. The saturated mean is $y_i$ for positive counts; at zero, take the boundary limit. Subtracting the fitted log-likelihood from the saturated one, canceling $\log(y_i!)$, and doubling gives $2\{y_i\log(y_i/\hat\mu_i)-(y_i-\hat\mu_i)\}$. Its nonnegativity follows from $t\log t-t+1\geq0$ for $t=y_i/\hat\mu_i$, with equality at $t=1$; the zero-count limit gives $2\hat\mu_i$. For Bernoulli data, the saturated success probability is $y_i\in\{0,1\}$. Its log-likelihood is zero, so a success contributes $-2\log\hat p_i$ and a failure $-2\log(1-\hat p_i)$. For a binomial count, the log-likelihood is $\log\binom{m_i}{y_i}+y_i\log p_i+(m_i-y_i)\log(1-p_i)$. The saturated probability is $y_i/m_i$, and subtracting the fitted log-likelihood cancels the binomial coefficient and gives the displayed $d_i$. For Gaussian observations of common known variance, $\ell(\mu;y)$ differs from $-\sum_i(y_i-\mu_i)^2/(2\sigma^2)$ only by a constant, giving the stated scaled sum of squares. Finally, subtracting $D_1=2(\ell_{\rm sat}-\ell_1)$ from $D_0=2(\ell_{\rm sat}-\ell_0)$ cancels the saturated likelihood and yields $2(\ell_1-\ell_0)$.
:::
:::

## Interpretation

An individual deviance contribution can be attached to the sign of $y_i-\hat\mu_i$ to form a deviance residual, $r_{D,i}=\operatorname{sign}(y_i-\hat\mu_i)\sqrt{d_i}$, where $D=\sum_i d_i$. The signs show whether observations exceed their fitted means, while the squares add back to total deviance. A large contribution identifies an observation to investigate; it does not establish that it is erroneous or influential, since influence also depends on leverage and how refitting would change the model.

Residual deviance and residual degrees of freedom appear together in GLM output because the latter give context for the former. A deviance near its degrees of freedom can be a useful rough diagnostic for some count models with suitable asymptotics, but there is no universal rule that $D/(n-p)$ must be one. Sparse binary data, overdispersion, dependence, boundary parameters and estimated dispersion can invalidate a naive chi-squared goodness-of-fit calibration. A model can have much smaller residual deviance than an intercept-only model yet still miss a systematic pattern or understate uncertainty.

The distinction between a fitted model and a saturated benchmark is especially sharp for individual binary responses. A Bernoulli observation is either zero or one, so its saturated probability sits on a boundary and describes that one observation perfectly. Even a well-specified stochastic model ordinarily assigns a probability strictly between zero and one and pays positive deviance for each realized outcome. Summing many such terms does not automatically produce the same simple chi-squared goodness-of-fit law as a table of binomial groups with large counts per group. The design and the amount of replication matter to calibration.

## Statistical use

First identify the response family, its dispersion convention and the model whose deviance is printed. Compare residual and null deviance only when the fits use the same observations and likelihood. For a nested comparison, refit both models, subtract their deviances, state the difference in dimensions and choose a reference distribution justified by the design and sample size. Use held-out prediction or an information criterion to compare non-nested models; training deviance alone rewards extra flexibility.

Inspect residuals against fitted means and important covariates. In a Poisson model, a large deviance relative to its degrees of freedom can point toward missing structure or overdispersion, but it cannot tell which without further checks. In a Gaussian model, a residual sum of squares must be interpreted with its error variance. In a quasi-likelihood model without a full likelihood, a reported deviance analogue should not automatically be called a likelihood-ratio statistic.

For a Poisson fit to counts whose variance is several times their mean, the ordinary Poisson deviance can be large even if the mean trend is reasonable; its nominal chi-squared calibration then fails. With one binary response per unique covariate vector, the saturated model assigns probabilities zero or one, and sparse-data goodness-of-fit tests based directly on residual deviance can be unreliable. If one candidate model silently drops observations with missing predictors, subtracting its deviance from a model fitted to all observations no longer cancels the same saturated likelihood. Complete separation can prevent a finite Bernoulli maximum-likelihood estimate, undermining an ordinary deviance comparison. Boundary or small-sample cases require more careful reference distributions.
## Worked example

Three sites report Poisson counts $y=(2,0,3)$. Sites one and two form group A, whose fitted mean is their average $1$; site three is group B, whose fitted mean is $3$. The group model has fitted vector $(1,1,3)$ and $p=2$ mean parameters, leaving $n-p=1$ residual degree of freedom. The third count matches exactly. The first contributes $2\{2\log 2-(2-1)\}=4\log2-2\approx0.77259$, and the zero count contributes $2(1)=2$. Thus $D_{\mathrm{res}}=4\log2\approx2.77259$.

The intercept-only model predicts the overall mean $5/3$ for all three sites. Its deviance is $2\{2\log(6/5)+3\log(9/5)\}\approx4.25601$. The nested difference is $4.25601-2.77259\approx1.48342$ on one extra model parameter. The group fit improves the training likelihood, yet three observations are far too few for an automatic large-sample chi-squared conclusion about a group effect.

**Your turn.** Two independent Bernoulli outcomes are $y=(1,0)$, with fitted probabilities $(0.8,0.3)$. Compute their individual deviance contributions and total residual deviance. Which observation contributes more, and why?

::: {.callout-tip collapse="true" title="Answer"}
The success contributes $-2\log(0.8)\approx0.44629$ and the failure contributes $-2\log(1-0.3)=-2\log(0.7)\approx0.71335$. The total is about $1.15964$. The failure contributes more because, under its fitted probability, the observed outcome has probability $0.7$, smaller than the success probability $0.8$ assigned to the first observation.
:::

## Common misconceptions

Residual deviance is not the sum of raw residuals, which can cancel, nor is it always the residual sum of squares outside the Gaussian case. A large number is not a calibrated lack-of-fit test without its family, degrees of freedom and assumptions. A small training deviance does not guarantee good prediction on new data. A difference in deviances is an ordinary likelihood-ratio statistic only for comparable nested likelihood fits; dividing by a dispersion estimate or using a quasi-family changes the inferential procedure.

## Connections

[Null deviance](null-deviance.qmd) uses a baseline fit without fitted covariate effects, retaining any offsets and including an intercept only if the model has one, while [scaled deviance](scaled-deviance.qmd) accounts for dispersion. A [deviance residual](deviance-residual.qmd) attributes signed contributions to observations. [Analysis of deviance](analysis-of-deviance.qmd) organizes nested-model differences, and a [likelihood-ratio test](likelihood-ratio-test.qmd) supplies a reference distribution when its assumptions apply. An [Akaike information criterion](akaike-information-criterion.qmd) adds a complexity charge for comparing fitted likelihood models.

## History

Neyman and Pearson's 1928 work treated hypothesis tests by comparing maximized likelihoods under competing parameter spaces.{{cite:dodge2008}} (pp. 309–310, “Likelihood Ratio Test”) Residual deviance uses the same log-likelihood contrast with a saturated fit as its reference; subtracting deviances between nested models removes that reference and recovers a likelihood-ratio comparison.
