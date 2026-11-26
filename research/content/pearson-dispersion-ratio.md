## Motivating example
Four counts can have a plausible fitted mean yet vary far more than a Poisson model permits. A residual diagnostic should compare their scatter with the variance implied by that mean, rather than comparing counts directly across observations with very different expected sizes. Pearson scaling performs that comparison before a degrees-of-freedom adjustment.{{cite:wuthrich_merz2022_glm}} (§5.3.1, ex. 5.16 and eq. 5.30)

## Definition — Divide by the fitted residual dimension
For independent responses with variance $\operatorname{Var}(Y_i)=\phi V(\mu_i)$ and unit prior weights, define
$$X_P^2=\sum_{i=1}^n\frac{(Y_i-\hat\mu_i)^2}{V(\hat\mu_i)},\qquad\hat\phi_P=\frac{X_P^2}{n-p},$$
where $p$ is the rank of the fitted mean model, including its intercept, and $n>p$. This convention leaves $\phi$ out of each residual's denominator because the purpose is to estimate it. In a Poisson model $V(\mu)=\mu$ and the model dispersion is fixed at one. The ratio is therefore a diagnostic against that model's variance restriction.{{cite:wuthrich_merz2022_glm}} (§5.3.1, eq. 5.30)

Variance functions distinguish response models sharing a link. For a normal response with unit weights, $V(\mu)=1$, so the ratio is a residual mean square with the units of the squared response. For a gamma mean parameterisation $V(\mu)=\mu^2$, so the ratio is dimensionless. These scales must be specified before interpreting a numerical value. The exponential-family mean–variance relationship supplies the variance function; the link describes how the mean changes with predictors.{{cite:nelder_wedderburn1972}} (§1.1, p. 371, eqs. 3–6)

## Interpretation — Why a value near one is only a diagnostic
If the means were known, each summand would have expectation $\phi$, because $\E[(Y_i-\mu_i)^2]=\operatorname{Var}(Y_i)$. Fitting the means uses information from the same data and reduces residual variation. In a Gaussian linear model, an orthogonal projection leaves exactly $n-p$ independent normal residual directions, giving $\E(X_P^2)=(n-p)\phi$ and exact unbiasedness. For other GLMs this degrees-of-freedom correction is motivated by approximation rather than by the same exact finite-sample projection law.

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

A useful report gives the fitted mean structure, variance function, residual degrees of freedom and the ratio together. Where the ratio is far from the model's dispersion, residual plots against predictors and fitted values show whether the mean curve or the variance function is the part under strain. The unit-weight formula changes when observations represent unequal exposures or precision weights: each squared residual is then multiplied by its weight before it is divided by $V(\hat\mu_i)$.{{cite:wuthrich_merz2022_glm}} (§5.3.1, eq. 5.30, exposure weights)

## Intuition — Compare residual scatter with the variance the mean implies
A Poisson count with mean $5$ has variance $5$. The counts $1,2,8,9$ have squared deviations $16,9,9,16$, summing to $50$. Dividing by the Poisson variance $5$ gives $X_P^2=10.000$. The same squared deviations divided by a gamma-style variance $\mu^2=25$ give $50/25=2.000$. With three residual degrees of freedom the Poisson ratio is $3.333333$ and the gamma-style ratio is $0.666667$. The observations did not change. The variance function changed, and with it the scale on which scatter is judged large.{{cite:nelder_wedderburn1972}} (§1.1, p. 371, eqs. 3–6)

The degrees-of-freedom divisor is a second, separate choice. If the four means were known to be $5$ and the Pearson sum remained $10$, each known-mean term would have expectation $\phi$ and the average $10/4=2.500$ would estimate $\phi$. Fitting an intercept spends one dimension and the usual divisor becomes $3$, giving $3.333333$ for the same sum. The worked example keeps the sum fixed when it imagines a second mean parameter and obtains $10/2=5.000$. In a real refit the sum would move as well, because the fitted means would move.

## Common misconceptions
A ratio near one is sometimes treated as a certificate that the Poisson likelihood is the right sampling model. The ratio compares a weighted residual sum of squares with a degrees-of-freedom benchmark. Dependence, a missing covariate and a single large count can all inflate it, and an overfit mean can shrink it. The quasi-Poisson adjustment multiplies coefficient variances by $\hat\phi_P$ and standard errors by its square root. In the first worked fit that factor is $1.825742$, and a unit-dispersion statistic of $2.4$ becomes $2.4/1.825742=1.314534$. The fitted means stay where the score equation put them, because a common positive dispersion cancels from the quasi-score.{{cite:wuthrich_merz2022_glm}} (§§5.3.1–5.3.2, dispersion estimation and Wald statistics)

The Gaussian linear model is the case in which the benchmark is exact: an orthogonal projection leaves $n-p$ independent residual directions and $\E(X_P^2)=(n-p)\phi$. For a Poisson or gamma GLM the same divisor is an approximation motivated by that geometry. A ratio of $3.333333$ on three degrees of freedom is a serious discrepancy with the Poisson variance function in this tiny sample, and it is still a diagnostic rather than a formal likelihood-ratio test against a named larger family.

## Connections
The Pearson residual for one observation is $(y_i-\hat\mu_i)/\sqrt{V(\hat\mu_i)}$, and $X_P^2$ is the sum of its squares. Deviance residuals come from the likelihood contribution of each observation and need a full probability model. Quasi-likelihood needs the mean and the variance function, which is why the Pearson ratio is the dispersion estimator that matches the quasi-score's working variance. Software that fixes the Poisson dispersion at one can still print the Pearson sum; dividing by $n-p$ is then an extra step the analyst takes when the variance assumption is under review.{{cite:rstats_summary_glm2026}} (§Details, dispersion){{cite:wuthrich_merz2022_glm}} (§5.3.1, residuals and dispersion)
