## Motivating example — Is an estimated slope large relative to its noise?
A fitted line can rise sharply because of a strong trend or because a small sample happened to align. The slope estimate needs its sampling standard error before its magnitude can be interpreted as statistical evidence. When the straight-line error model is Gaussian, dividing a centred slope by its estimated standard error gives an exact Student pivot.{{cite:openintro2019}} (§8.4, inference for linear regression)

## Statement
Let $Y_i=\beta_0+\beta_1x_i+\varepsilon_i$, with fixed predictors, independent $N(0,\sigma^2)$ errors, $n>2$ and $S_{xx}>0$. Define $S^2=\mathrm{SSE}/(n-2)$ and $\operatorname{SE}(\hat\beta_1)=S/\sqrt{S_{xx}}$. Then
$$T=\frac{\hat\beta_1-\beta_1}{S/\sqrt{S_{xx}}}\sim t_{n-2}.$$
The pivot is centred at the true slope. For a test of $\beta_1=\beta_{10}$, replace that centring by the hypothesised value and use the central law under that null.{{cite:openintro2019}} (§8.4.2–8.4.3, slope tests and confidence intervals)

## Proof
The slope error is a weighted sum $\sum_i(x_i-\bar x)\varepsilon_i/S_{xx}$ and is therefore $N(0,\sigma^2/S_{xx})$. Its normalised version is standard normal. The residual vector is the projection of the error vector onto the complement of the two-dimensional span of an intercept and a slope. It is independent of both coefficient estimators because the projection is orthogonal and the joint vector is normal. Its squared length divided by $\sigma^2$ is chi-squared on $n-2$ degrees of freedom.{{cite:siegrist_multinormal2022}} (“The General Multivariate Normal Distribution”, “Transformations”; normal linear transformations and independence)

Consequently the displayed statistic is $Z/\sqrt{V/(n-2)}$, with independent $Z\sim N(0,1)$ and $V\sim\chi^2_{n-2}$. This is the defining Student ratio. Both independence and the residual degrees of freedom are essential; dividing a normal-looking estimate by an arbitrary random scale does not establish a Student distribution.{{cite:dodge2008}} (p. 526, Student ratio construction)

## Statistical use — Confidence limits transform the same inequality
Let $c=t_{n-2;1-\alpha/2}$. Inverting $P(-c\le T\le c)=1-\alpha$ gives $\hat\beta_1\pm cS/\sqrt{S_{xx}}$. A two-sided level-$\alpha$ test rejects a specified slope precisely when this interval omits it. Changing the predictor unit rescales both the slope estimate and its standard error inversely, leaving the statistic for an equivalent scientific null unchanged.{{cite:openintro2019}} (§8.4.3, confidence interval for a coefficient)

The formula also distinguishes an uncertainty about the slope from an uncertainty about a future response. The former measures variability across fitted trends at a fixed design. A prediction interval for an individual response also includes its new error and uncertainty about the regression mean at the predictor value of interest. The slope standard error alone cannot supply that prediction interval.{{cite:nist_ls_straight2002}} (§4.4.3.1, parameter estimates and residual standard deviation)

## Worked example — A six-point calibration slope
Suppose $n=6$, the centred design has $S_{xx}=17.5$, the fitted slope is $1.2$ and $S=0.7$. The slope standard error is $0.167332$ and the statistic against zero is $7.171372$ on four degrees of freedom. With critical value $2.776445$, the 95% interval is $(0.735412,1.664588)$. The two-sided $p$-value is $0.002002$.

The estimated mean change across a predictor increment of three is $3(1.2)=3.600$, and its confidence interval is $(2.206236,4.993764)$ because multiplication by a positive known constant maps the same interval event. No extra factor of $\sqrt n$ is needed: the sample's predictor information is already in $S_{xx}$.{{cite:openintro2019}} (§8.4.3)

**Your turn.** Test a slope of $1$ using the same estimates. What statistic is compared with $t_4$?

::: {.callout-tip collapse="true" title="Answer"}
The statistic is $(1.2-1)/(0.7/\sqrt{17.5})=1.195229$. It is much smaller than the statistic against zero because the hypothesised slope is closer to the estimate.
:::

## Common misconceptions — Changing the origin does not change a slope test
Replace $x_i$ by $u_i=x_i-a$. Then $u_i-\bar u=x_i-\bar x$, so $S_{uu}=S_{xx}$ and the fitted slope and its standard error are unchanged. The intercept changes because it describes a different predictor origin. A correctly implemented slope test cannot change merely because kilometres are measured from a different reference point.{{cite:nist_ls_straight2002}} (§4.4.3.1, centred slope formula)

If all predictors coincide, $S_{xx}=0$ and the slope is unidentified; no Student pivot results. Non-normal errors can preserve unbiasedness and the variance formula but change finite-sample tail probabilities. Dependence and unequal variances similarly require a different covariance calculation before selecting a test reference. The exact result belongs to the stated Gaussian model, rather than to every line produced by a least-squares algorithm.{{cite:dodge2008}} (p. 492, normality and equal-variance assumptions for regression inference)
