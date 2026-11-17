## Motivating example — A Poisson mean does not determine a good fit
Four counts can have a plausible fitted mean yet vary far more than a Poisson model permits. A residual diagnostic should compare their scatter with the variance implied by that mean, rather than comparing counts directly across observations with very different expected sizes. Pearson scaling performs that comparison before a degrees-of-freedom adjustment.{{cite:wuthrich_merz2022_glm}} (§5.3.1, ex. 5.16 and eq. 5.30)

## Definition — Divide by the fitted residual dimension
For independent responses with variance $\operatorname{Var}(Y_i)=\phi V(\mu_i)$ and unit prior weights, define
$$X_P^2=\sum_{i=1}^n\frac{(Y_i-\hat\mu_i)^2}{V(\hat\mu_i)},\qquad\hat\phi_P=\frac{X_P^2}{n-p},$$
where $p$ is the rank of the fitted mean model, including its intercept, and $n>p$. This convention leaves $\phi$ out of each residual's denominator because the purpose is to estimate it. In a Poisson model $V(\mu)=\mu$ and the model dispersion is fixed at one. The ratio is therefore a diagnostic against that model's variance restriction.{{cite:wuthrich_merz2022_glm}} (§5.3.1, eq. 5.30)

Variance functions distinguish response models sharing a link. For a normal response with unit weights, $V(\mu)=1$, so the ratio is a residual mean square with the units of the squared response. For a gamma mean parameterisation $V(\mu)=\mu^2$, so the ratio is dimensionless. These scales must be specified before interpreting a numerical value. The exponential-family mean–variance relationship supplies the variance function; the link describes how the mean changes with predictors.{{cite:nelder_wedderburn1972}} (§1.1, p. 371, eqs. 3–6)

## Interpretation — Why a value near one is only a diagnostic
If the means were known, each summand would have expectation $\phi$, because $E[(Y_i-\mu_i)^2]=\operatorname{Var}(Y_i)$. Fitting the means uses information from the same data and reduces residual variation. In a Gaussian linear model, an orthogonal projection leaves exactly $n-p$ independent normal residual directions, giving $E(X_P^2)=(n-p)\phi$ and exact unbiasedness. For other GLMs this degrees-of-freedom correction is motivated by approximation rather than by the same exact finite-sample projection law.{{cite:siegrist2022_normals}} (§6.08, normal-sample residual sums of squares)

An unusually large ratio can reflect a variance model that is too narrow, a missing mean covariate, a few outliers or dependence among observations. Changing only $\phi$ cannot repair a systematically wrong mean curve. Conversely, a small ratio can arise from underdispersion, overfitting or a feature of how the responses were collected. Neither direction identifies the mechanism by itself. Small fitted Poisson means can also give strongly skewed Pearson residuals and unstable denominators.{{cite:wuthrich_merz2022_glm}} (§5.3.1, residuals and dispersion)

## Worked example — The same mean, contrasting residual scatter
For counts $1,2,8,9$, an intercept-only Poisson fit has $\hat\mu=5$. Thus $X_P^2=(16+9+9+16)/5=10.000$ and $n-p=3$, yielding $\hat\phi_P=3.333333$. Replacing the counts by $4,5,5,6$ leaves their mean at five but gives $X_P^2=(1+0+0+1)/5=0.400$ and ratio $0.133333$. The contrast separates mean level from residual scatter.

If a quasi-Poisson analysis holds the fitted mean fixed and estimates a common dispersion, its model-based coefficient covariance is multiplied by $\hat\phi_P$. The corresponding standard errors are multiplied by $\sqrt{\hat\phi_P}=1.825742$ in the first example. A statistic that used a unit-dispersion standard error and equalled $2.4$ would become $1.314534$ after this scaling. This is a variance adjustment, rather than a likelihood comparison between fully specified probability laws.{{cite:wuthrich_merz2022_glm}} (§§5.3.1–5.3.2, dispersion estimation and Wald statistics)

**Your turn.** For the hypothetical first dataset, suppose two independent mean parameters rather than one have been fitted and the Pearson sum stays ten. What dispersion estimate follows?

::: {.callout-tip collapse="true" title="Answer"}
The residual degrees of freedom are $4-2=2$, so the ratio is $10/2=5.000$. The premise keeps the Pearson sum fixed; fitting another parameter would generally also change that sum.
:::

## Statistical use — Separate software defaults from model assessment
R's `summary.glm` fixes the dispersion at one for its Poisson and binomial families and estimates it for families where dispersion is free. Its reported convention is software behaviour. It does not prevent calculating the Pearson ratio as a diagnostic for a Poisson fit, nor imply that a quasi-family defines a full response distribution for prediction.{{cite:rstats_summary_glm2026}} (§Details, dispersion)

A useful report gives the fitted mean structure, variance function, residual degrees of freedom and the ratio together. Where the ratio suggests a problem, inspect residual patterns against predictors and fitted values before choosing an alternative variance model. The unit-weight formula should also be adapted explicitly when observations represent unequal exposures or precision weights.{{cite:wuthrich_merz2022_glm}} (§5.3.1, eq. 5.30, exposure weights)
