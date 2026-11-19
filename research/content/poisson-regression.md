## Motivating example — Unequal observation times are not comparable counts
One ward records $4$ infections in $2$ years. Another records $9$ infections in $3$ years. The counts are $4$ and $9$. The rates are $2$ and $3$ per year. A regression that treats the counts as comparable without the years of observation pretends the wards were watched for the same time. The offset $\log t$ puts the years into the mean before any coefficient is interpreted as a rate. An offset is a term whose coefficient is fixed at $1$. The exposure multiplies the mean, and the logarithm of the exposure enters the linear predictor.{{cite:mccullagh_nelder1989}} (§6.3.2, eq. 6.5, p. 206)

## Intuition — A log mean and an exposure offset
A Poisson count has variance equal to its mean: the mean, the variance and every cumulant equal $\mu$.{{cite:mccullagh_nelder1989}} (§6.2.1, p. 195) The log link writes $\log\mu_i=\mathbf{x}_i^\top\boldsymbol{\beta}$, so $\mu_i=\exp(\mathbf{x}_i^\top\boldsymbol{\beta})$ stays positive for every finite coefficient and every covariate pattern. An identity link does not, because the linear predictor can be negative while a mean count cannot.{{cite:mccullagh_nelder1989}} (§1.2.7, p. 15; §2.2.3, p. 31) A coefficient is then a difference of log means. Exponentiating it gives a multiplicative change in the mean count, the other covariates held fixed.{{cite:mccullagh_nelder1989}} (§1.2.7, pp. 14–15) With an exposure $t_i$, the same construction is $\log\mu_i=\mathbf{x}_i^\top\boldsymbol{\beta}+\log t_i$, so $\exp(\mathbf{x}_i^\top\boldsymbol{\beta})$ is a rate per unit of exposure and the expected count is that rate times $t_i$.

## Definition — Poisson log-linear mean, with an optional offset
The Poisson log-linear model for independent counts is $Y_i\sim\mathrm{Poisson}(\mu_i)$ with $\log\mu_i=\mathbf{x}_i^\top\boldsymbol{\beta}$, or $\log\mu_i=\mathbf{x}_i^\top\boldsymbol{\beta}+\log t_i$ when observation $i$ has exposure $t_i$. In the exponential-family form the log-likelihood contribution is $y\log\mu-\mu$, the natural parameter is $\theta=\ln\mu$, and the variance function is $V=\mu$. When the linear predictor is $\ln\mu$ there are sufficient statistics.{{cite:nelder_wedderburn1972}} (§3.2, p. 378) The Poisson scale factor in that scheme is known and equal to one. An unknown scale is a different model, estimated only after an adequate mean has been fitted.{{cite:nelder_wedderburn1972}} (§2.3, p. 375) R's `glm` follows the known-scale convention for the Poisson family when it forms the AIC, and it does not estimate a second scale from the residual deviance.{{cite:rstats_glm2026}} (§ Value, binomial and Poisson dispersion fixed at one)

## Interpretation — Saturated rates and a pooled rate
With a single binary covariate and an offset, two groups have saturated rates $y_1/t_1$ and $y_2/t_2$. The intercept is the log rate in the reference group and the slope is the log ratio of the two rates. In the wards, those rates are $4/2=2$ and $9/3=3$, so the intercept is $\log 2\approx 0.6931$ and the slope is $\log(3/2)\approx 0.4055$. The fitted means are the counts themselves. A model with only an intercept and the offset pools the rate: $(4+9)/(2+3)=13/5=2.6$ per year, and the fitted means are $2.6\times 2=5.2$ and $2.6\times 3=7.8$. Those two fits are the zeros of one score, with and without a group coefficient. The identity that makes the pooled rate $\sum y_i/\sum t_i$ is the intercept-only case of $\mathbf{X}^\top(\mathbf{y}-\boldsymbol{\mu})=\mathbf{0}$.

## Properties — The score recovers rates and flags a pooled fit
The Poisson score for the log link is $\mathbf{X}^\top(\mathbf{y}-\boldsymbol{\mu})$. At the saturated rates the residuals are zero, so the score is zero and those rates are the maximum-likelihood fit of the two-group model. At the pooled rate the residuals are $4-5.2=-1.2$ and $9-7.8=1.2$. The Pearson statistic is

$$
\frac{(-1.2)^2}{5.2}+\frac{1.2^2}{7.8}=\frac{6}{13}\approx 0.4615.
$$

With one parameter and two observations the residual degrees of freedom are $1$. The statistic is not large, but it is not zero: the pooled rate does not reproduce both counts. Omitting the offset and fitting a common mean to the raw counts gives mean $6.5$ and Pearson statistic $25/13\approx 1.9231$, and it answers a question about counts rather than rates.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The Poisson log-likelihood contribution $y\log\mu-\mu$ has derivative $(y-\mu)/\mu$ in $\mu$, and therefore derivative $y-\mu$ in $\log\mu$.{{cite:nelder_wedderburn1972}} (§3.2, p. 378) The chain rule multiplies by the covariate row. For the log link that factor is $1$ on the $\eta$ scale, leaving the score contribution $y-\mu$. Summing gives $\mathbf{X}^\top(\mathbf{y}-\boldsymbol{\mu})$. Setting the score to zero with an intercept and an offset $\log t$, and with no other covariate, forces $\sum_i(y_i-e^{\beta}t_i)=0$, hence $e^{\beta}=\sum y_i/\sum t_i$. That is the pooled rate. With a group indicator the two blocks of the score vanish separately and each rate is the group ratio of count to exposure. A common positive dispersion multiplies every contribution by the same constant and does not move the root.{{cite:mccullagh_nelder1989}} (§9.2.3, eq. 9.5, p. 327)
:::
:::

## Statistical use — Quote a rate, and name the exposure
A slope on the log-rate scale is a rate ratio only when the offset is the log exposure and the coefficient is a contrast of groups observed on that exposure scale. The wards' slope $0.4055$ multiplies the infection rate by $1.5$ for the second ward relative to the first. It does not say the second ward had $1.5$ times as many infections: the counts are $9$ and $4$, a ratio of $2.25$, because the second ward was observed for $3$ years rather than $2$.

The score derivation used $\operatorname{Var}(Y_i)=\mu_i$. If the infections cluster, or if units that share a covariate still differ in rate, the variance exceeds the mean and the Poisson standard errors are too small, even when the log-rate point estimates stay the same. A dispersion factor that does not depend on $\boldsymbol{\beta}$ drops out of the score and stays in the covariance, which is the inverse of the Poisson information, multiplied by that factor.{{cite:mccullagh_nelder1989}} (§6.2.3, pp. 198–199; §9.2.3, eq. 9.6, p. 327) A ratio of exposures that was recorded wrongly moves the offset and changes the rates themselves. A mean that is not log-linear in the covariates is not repaired by a correct offset. Both parts of the log-linear specification need checking, and the mean equation is the one that matters first.{{cite:mccullagh_nelder1989}} (§6.1, p. 194)

## Worked example — Two wards, with and without the offset
Exposures $t=(2,3)$, counts $y=(4,9)$.

Saturated log-rate model: rates $2$ and $3$, coefficients $\log 2\approx 0.6931$ and $\log(1.5)\approx 0.4055$, fitted means $4$ and $9$, Pearson statistic $0$.

Pooled rate with the offset included: rate $2.6$, fitted means $5.2$ and $7.8$, Pearson statistic $6/13\approx 0.4615$.

Offset dropped, common mean fitted to the counts: fitted values $6.5$ and $6.5$, Pearson statistic $25/13\approx 1.9231$. Dividing those fitted counts by the exposures after the fact gives $3.25$ and $6.5/3\approx 2.1667$, neither of which is the pooled rate $2.6$. The division cannot repair a likelihood that ignored $t$.

**Your turn.** One ward records $8$ infections in $4$ years. Under the log link with offset $\log 4$ and a single rate parameter, what rate and what mean count does maximum likelihood give?

::: {.callout-tip collapse="true" title="Answer"}
The rate is $8/4=2$ per year and the mean count is $2\times 4=8$. The residual is zero. The log rate is $\log 2\approx 0.6931$.
:::

## Common misconceptions — Rate ratios are not count ratios
A coefficient is not a change in the count. It is a change in the log mean, and the reported effect is the factor $e^{\beta_j}$.{{cite:mccullagh_nelder1989}} (§1.2.7, pp. 14–15) The wards' rate ratio is $1.5$ and their count ratio is $2.25$. Those are different quotients because the exposures differ. The count ratio multiplies the rate ratio by the exposure ratio $3/2$.

Poisson regression does not estimate a dispersion. The Poisson scale is fixed at one.{{cite:nelder_wedderburn1972}} (§2.3, p. 375){{cite:rstats_glm2026}} (§ Value, binomial and Poisson dispersion fixed at one) A Pearson statistic of $0.4615$ on one degree of freedom is a check on that assumption, not a second parameter the Poisson likelihood has estimated. McCullagh and Nelder's estimator $X^2/(n-p)$ is available once the variance is freed; it is not a parameter of the Poisson likelihood itself.{{cite:mccullagh_nelder1989}} (§6.2.4, eq. 6.4, p. 200)

Prior weights are not the exposure. A prior weight rescales the contribution of a row to the dispersion. An offset is a covariate whose coefficient is fixed at $1$, and that is how a log exposure enters the mean.{{cite:mccullagh_nelder1989}} (§2.5, p. 42; §6.3.2, eq. 6.5, p. 206)

## Connections — Scoring, the log link, and a different likelihood
[Fisher scoring](fisher-scoring.qmd) is the iteration that solves the score when the linear predictor is not saturated. Nelder and Wedderburn wrote that step, using expected second derivatives, as iterative weighted least squares.{{cite:nelder_wedderburn1972}} (§2.1, p. 373, eq. 9) The [log link](log-link.qmd) is the map from the coefficient vector to a positive mean. A [baseline-category logit](baseline-category-logit-model.qmd) is a different likelihood: one category out of several, not an unbounded count. The same 1972 paper treats a contingency table as independent Poisson counts, following Birch, precisely because a multinomial table can be estimated that way; the likelihood is still not the likelihood of an unbounded count regression with an exposure offset.{{cite:nelder_wedderburn1972}} (§3.2, p. 378)

## Check yourself

1. One ward records $6$ infections in $1$ year and another records $6$ in $5$ years. What are the two rates, and what comparison does a model of the raw counts, with no offset, actually make?

::: {.callout-tip collapse="true" title="Answer"}
The rates are $6$ and $6/5=1.2$ per year. Without an offset the two counts are equal, so a common-mean fit treats the wards as having the same expected count and never sees that the second ward was observed five times as long.
:::

2. Why does a common dispersion $\phi>0$, multiplying every Poisson variance, leave the fitted log-rate unchanged in an intercept-only model with an offset, and where does $\phi$ still appear?

::: {.callout-tip collapse="true" title="Answer"}
The quasi-score is the Poisson score divided by $\phi$. A positive constant does not move the root, so the fitted rate remains the total count divided by the total exposure. The factor stays in the covariance, and each standard error is multiplied by $\sqrt{\phi}$.
:::

3. Suppose a second group is observed for twice as long as the first and its event rate is also twice the first group's rate. By what factor do the expected counts differ, and why is that factor not the rate ratio?

::: {.callout-tip collapse="true" title="Answer"}
The expected-count ratio is the exposure ratio times the rate ratio, here $2\times 2=4$. The rate ratio is $2$. Quoting the count ratio as if it were the group effect confounds time at risk with the rate.
:::

## History — Poisson errors on a log-linear mean
Log-linear models made multiplicative effects, with a nominal Poisson distribution for the counts, the standard replacement for additive effects and Normal errors. Writing the mean as $\mu=\exp(\eta)$ keeps it positive for every coefficient and every covariate pattern.{{cite:mccullagh_nelder1989}} (§1.2.7, pp. 14–16) Nelder and Wedderburn's 1972 paper fitted Poisson models by iterative weighted least squares, and listed “Poisson (contingency tables)” among four illustrative families. They treated a contingency table as independent Poisson counts, following Birch, with natural parameter $\theta=\ln\mu$ and sufficient statistics under the log link.{{cite:nelder_wedderburn1972}} (Summary, p. 370; §3.2, p. 378) Earlier, Fisher had estimated effects for tuberculin measurements as if the observations were Poisson, taking the variance proportional to the mean and the systematic part linear on the log scale.{{cite:nelder_wedderburn1972}} (§3.1, p. 377) The exposure offset, a covariate with coefficient fixed at $1$, is the same device as the log of aggregate months of service in the ship-damage model.{{cite:mccullagh_nelder1989}} (§6.3.2, eq. 6.5, p. 206)
