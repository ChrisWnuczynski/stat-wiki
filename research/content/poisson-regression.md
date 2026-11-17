## Lead context
Poisson regression gives a count a positive mean that depends on covariates, usually through a logarithm, so the mean cannot become negative when a covariate changes.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

## Motivating example
One ward records $4$ infections in $2$ years. Another records $9$ infections in $3$ years. The counts are $4$ and $9$. The rates are $2$ and $3$ per year. A regression that treats the counts as comparable without the years of observation pretends the wards were watched for the same time. The offset $\log t$ puts the years into the mean before any coefficient is interpreted as a rate.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

## Intuition
A Poisson count has variance equal to its mean. The log link writes $\log\mu_i=\mathbf{x}_i^\top\boldsymbol{\beta}$, so $\mu_i=\exp(\mathbf{x}_i^\top\boldsymbol{\beta})$ stays positive. A coefficient is then a difference of log means. Exponentiating it gives a multiplicative change in the mean count, the other covariates held fixed. An offset is a covariate whose coefficient is fixed at $1$, used for the log of an exposure.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

## Definition
The Poisson log-linear model for independent counts is $Y_i\sim\mathrm{Poisson}(\mu_i)$ with $\log\mu_i=\mathbf{x}_i^\top\boldsymbol{\beta}$, or $\log\mu_i=\mathbf{x}_i^\top\boldsymbol{\beta}+\log t_i$ when observation $i$ has exposure $t_i$. The dispersion is fixed at $1$: R's `glm` uses that convention for the Poisson family when it forms the AIC, and it does not estimate a second scale from the residual deviance.{{cite:rstats_glm2026}} (Value, binomial and Poisson dispersion fixed at one)

## Interpretation
With a single binary covariate and an offset, two groups have saturated rates $y_1/t_1$ and $y_2/t_2$. The intercept is the log rate in the reference group and the slope is the log ratio of the two rates. In the wards, those rates are $4/2=2$ and $9/3=3$, so the intercept is $\log 2\approx 0.6931$ and the slope is $\log(3/2)\approx 0.4055$. The fitted means are the counts themselves. A model with only an intercept and the offset pools the rate: $(4+9)/(2+3)=13/5=2.6$ per year, and the fitted means are $2.6\times 2=5.2$ and $2.6\times 3=7.8$.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

## Properties
The Poisson score for the log link is $\mathbf{X}^\top(\mathbf{y}-\boldsymbol{\mu})$. At the saturated rates the residuals are zero, so the score is zero and those rates are the maximum-likelihood fit of the two-group model. At the pooled rate the residuals are $4-5.2=-1.2$ and $9-7.8=1.2$. The Pearson statistic is
\[
\frac{(-1.2)^2}{5.2}+\frac{1.2^2}{7.8}=\frac{6}{13}\approx 0.4615.
\]
With one parameter and two observations the residual degrees of freedom are $1$. The statistic is not large, but it is not zero: the pooled rate does not reproduce both counts. Omitting the offset and fitting a common mean to the raw counts gives mean $6.5$ and Pearson statistic $25/13\approx 1.9231$, and it answers a question about counts rather than rates.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The log-likelihood contribution $y\log\mu-\mu$ has derivative $(y-\mu)/\mu$ in $\log\mu$. The chain rule multiplies by the covariate row, and for the log link that factor is $1$ on the $\eta$ scale, leaving the score contribution $y-\mu$. Summing gives $\mathbf{X}^\top(\mathbf{y}-\boldsymbol{\mu})$. Setting the score to zero with an intercept and an offset $\log t$, and with no other covariate, forces $\sum_i(y_i-e^{\beta}t_i)=0$, hence $e^{\beta}=\sum y_i/\sum t_i$. That is the pooled rate $13/5=2.6$. With a group indicator the two blocks of the score vanish separately and the rates are the group ratios $2$ and $3$.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)
:::
:::

## Statistical use — Quote a rate, and name the exposure
A slope on the log-rate scale is a rate ratio only when the offset is the log exposure and the coefficient is a contrast of groups observed on that exposure scale. The wards' slope $0.4055$ multiplies the infection rate by $1.5$ for the second ward relative to the first. It does not say the second ward had $1.5$ times as many infections: the counts are $9$ and $4$, a ratio of $2.25$, because the second ward was observed for $3$ years rather than $2$.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

The score derivation used $\operatorname{Var}(Y_i)=\mu_i$. If the wards' infections cluster, the variance exceeds the mean and the Poisson standard errors are too small, even when the log-rate point estimates stay the same, because a dispersion factor that does not depend on $\boldsymbol{\beta}$ drops out of the score and stays in the variance. A ratio of exposures that was recorded wrongly moves the offset and changes the rates themselves. And a mean that is not log-linear in the covariates is not repaired by a correct offset.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

## Worked example
Exposures $t=(2,3)$, counts $y=(4,9)$.

Saturated log-rate model: rates $2$ and $3$, coefficients $\log 2\approx 0.6931$ and $\log(1.5)\approx 0.4055$, fitted means $4$ and $9$, Pearson statistic $0$.

Pooled rate with the offset included: rate $2.6$, fitted means $5.2$ and $7.8$, Pearson statistic $6/13\approx 0.4615$.

Offset dropped, common mean fitted to the counts: fitted values $6.5$ and $6.5$, Pearson statistic $25/13\approx 1.9231$. Dividing those fitted counts by the exposures after the fact gives $3.25$ and $6.5/3\approx 2.1667$, neither of which is the pooled rate $2.6$. The division cannot repair a likelihood that ignored $t$.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

**Your turn.** One ward records $8$ infections in $4$ years. Under the log link with offset $\log 4$ and a single rate parameter, what rate and what mean count does maximum likelihood give?

::: {.callout-tip collapse="true" title="Answer"}
The rate is $8/4=2$ per year and the mean count is $2\times 4=8$. The residual is zero. The log rate is $\log 2\approx 0.6931$.
:::

## Common misconceptions
A coefficient is not a change in the count. It is a change in the log mean. The wards' rate ratio is $1.5$ and their count ratio is $2.25$. Those are different quotients because the exposures differ.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

Poisson regression does not estimate a dispersion. The Poisson dispersion is fixed at one. A Pearson statistic of $0.4615$ on one degree of freedom is a check on that assumption, not a second parameter the Poisson likelihood has estimated.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

Prior weights are not the exposure. Prior weights are rarely the way to encode Poisson exposure; the offset is.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

## Connections
[Fisher scoring](fisher-scoring.qmd) is the iteration that solves the score when the linear predictor is not saturated. The [log link](log-link.qmd) is the map from the coefficient vector to a positive mean. A [baseline-category logit](baseline-category-logit-model.qmd) is a different likelihood: one category out of several, not an unbounded count.{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–380)

## Check yourself

1. What is the pooled infection rate for counts $4$ and $9$ over $2$ and $3$ years?

::: {.callout-tip collapse="true" title="Answer"}
$13/5=2.6$ per year. The fitted means are $5.2$ and $7.8$.
:::

2. What is $\log(3/2)$ to four decimals, and what rate ratio does it represent?

::: {.callout-tip collapse="true" title="Answer"}
$\log(1.5)\approx 0.4055$. It is the log of the rate ratio $3/2=1.5$, not the log of the count ratio $9/4=2.25$.
:::

3. Is the Pearson statistic $6/13$ equal to zero?

::: {.callout-tip collapse="true" title="Answer"}
No. It is about $0.4615$. It is zero only for the saturated rates $2$ and $3$, whose fitted means are the counts.
:::

## History
`glm` fits this mean by iteratively reweighted least squares, fixes the Poisson dispersion at one, and provides an offset for a term whose coefficient is not estimated. Exposure enters the wards' model as that offset. The saturated two-group fit and the pooled-rate fit are then the zeros of the same score, with and without a group coefficient.{{cite:rstats_glm2026}} (Details and Arguments)
