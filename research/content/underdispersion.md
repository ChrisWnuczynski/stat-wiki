## Motivating example

Suppose a count model predicts an average of two bids for each comparable firm. A Poisson model then assigns conditional variance two as well. If the observed counts stay tightly around two even after the relevant firm characteristics have been accounted for, the Poisson variance may be too large. This is underdispersion: a comparison between residual variation and a model's variance prediction, not simply a statement that a histogram looks narrow.

## Intuition — When counts vary less than Poisson

A mean tells where a count distribution is centred; a variance tells how widely it spreads. Poisson regression locks those two numbers together at each covariate setting. Real count processes need not obey that lock. A fixed small number of opportunities can cap variability, while constraints or regular scheduling can make counts more predictable than independent arrivals. A centre alone is inadequate for describing data and decisions; a separate spread measure is needed.{{cite:dodge2008}} (p. 341, “Measure of Dispersion”)

Underdispersion is conditional on the proposed mean model. A group of counts that looks variable in aggregate can be tightly bunched once distinct groups have different fitted means. Conversely, a badly specified mean can make an otherwise suitable variance model appear overdispersed. Diagnose the residual pattern before changing the response family.

## Definition

Relative to a reference count model with conditional mean $\mu_i$ and variance function $V(\mu_i)$, underdispersion means that the conditional variance is smaller than $V(\mu_i)$ in the relevant range. For a Poisson reference, $V(\mu_i)=\mu_i$. A quasi-Poisson description writes $\operatorname{Var}(Y_i\mid x_i)=\phi\mu_i$; $0<\phi<1$ indicates underdispersion, $\phi=1$ the Poisson variance and $\phi>1$ overdispersion. This $\phi$ is a variance multiplier, not a mean parameter.

An estimated Pearson dispersion is $\widehat\phi=X_P^2/(n-p)$, where $X_P^2=\sum_i(y_i-\widehat\mu_i)^2/\widehat\mu_i$ and $p$ fitted mean parameters. Values below one suggest underdispersion, but sampling noise, leverage, dependence, and poor mean fit complicate interpretation. The ratio is a diagnostic, not by itself a proof that a particular alternative distribution is correct.

## Properties

A binomial count supplies a simple structural counterexample to Poisson equality. If $Y\sim\operatorname{Binomial}(m,q)$, then $\mathbb E Y=mq$ and $\operatorname{Var}(Y)=mq(1-q)$, so its variance-to-mean ratio is $1-q$ when $q>0$. It is below one for $0<q\leq1$. A bounded number of trials can therefore produce underdispersed counts naturally, although a binomial model requires a meaningful trial count $m$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $Y=\sum_{j=1}^{m}B_j$ for independent Bernoulli$(q)$ variables. Linearity gives $\mathbb E Y=mq$, and independence gives $\operatorname{Var}(Y)=\sum_jq(1-q)=mq(1-q)$. Division by the positive mean yields $1-q<1$ for $q>0$. For a Poisson model with fitted intercept only, $\widehat\mu$ is the sample mean. Substituting it into the Pearson statistic gives the stated sum of squared residuals divided by that mean; dividing by its residual degrees of freedom yields the conventional dispersion estimate. These calculations establish the example and diagnostic formula, not the validity of a chi-square approximation in a small sample.
:::
:::

## Interpretation

The sign of a dispersion parameter depends on its model convention. The mean-parameterized Conway–Maxwell–Poisson model used for the bankruptcy bids example has a shape parameter $\nu$, with $\nu=1$ at the Poisson case and $\nu>1$ in its underdispersed regime. This runs in the opposite numerical direction from the quasi-Poisson variance multiplier $\phi<1$. Reporting “dispersion 1.75” without naming the model can therefore mislead. The two parameters also have different inferential meanings: quasi-Poisson specifies a mean–variance relationship without a full probability mass function, while the Conway–Maxwell–Poisson is a count distribution.

A low Pearson ratio affects uncertainty estimates. If the assumed Poisson variance is too large, standard errors based strictly on it can be unnecessarily conservative for a correctly specified mean model; however, automatically shrinking all standard errors from a single low ratio can be unsafe when dependence or a wrong mean model is responsible. The fitted mean, residual diagnostics, study design, and plausible count mechanism should be considered together.

## Statistical use

First fit a scientifically sensible mean model and plot residuals against fitted means and important covariates. Estimate the Pearson dispersion with appropriate residual degrees of freedom. If it is materially below one and the pattern persists across groups, consider whether the response is bounded by a number of opportunities, whether a quasi-likelihood variance adjustment is adequate, or whether a flexible count distribution is needed. A standard negative-binomial count model has variance greater than its mean and cannot be the direct remedy for genuine Poisson underdispersion.

The ten-count example assumes comparable units and no hidden group shifts. If eight units come from one group and two from another with different means, an intercept-only comparison mixes mean structure with dispersion. A sample of ten identical twos yields a zero Pearson statistic, but that alone does not imply a population variance of zero. Correlated repeated counts can also invalidate the usual independent-observation dispersion estimate. If a trial count is unknown or varies by unit, the simple binomial explanation may not be a usable model even when the observed ratio is low.
## Worked example

Ten comparable units produce counts $1,3,2,2,2,2,2,2,2,2$. The fitted Poisson intercept gives $\widehat\mu=2$ and expected variance $2$. The sum of squared residuals is $(1-2)^2+(3-2)^2=2$, so the sample variance is $2/9\approx0.2222$ and its ratio to the mean is $1/9\approx0.1111$. Equivalently, $X_P^2=2/2=1$ and with one fitted parameter $\widehat\phi=1/(10-1)=1/9$. These numbers show a tightly concentrated sample relative to Poisson, but ten observations alone do not establish the mechanism or validate an asymptotic test.

**Your turn.** A response counts successes in four independent trials, each with success probability $0.5$. Find its mean, variance and variance-to-mean ratio. Would a Poisson law with the same mean match its spread?

::: {.callout-tip collapse="true" title="Answer"}
For $Y\sim\operatorname{Binomial}(4,0.5)$, the mean is $4(0.5)=2$ and variance is $4(0.5)(0.5)=1$, so the ratio is $1/2=0.5$. A Poisson variable with mean $2$ has variance $2$, twice as large, and also lacks the binomial upper bound of four.
:::

## Common misconceptions

Underdispersion does not mean a small mean; a count can have a large mean and a variance smaller than that mean. It is not diagnosed by comparing raw variance and raw mean when covariates change the conditional mean across observations. A quasi-Poisson multiplier below one and a Conway–Maxwell–Poisson parameter above one indicate the same direction of spread under different conventions. Finally, replacing Poisson with a negative binomial does not fix underdispersion, because its usual variance is at least its mean.

## Connections

The [Poisson distribution](poisson-distribution.qmd) sets the reference equality of mean and variance. [Overdispersion](overdispersion.qmd) is the opposite direction relative to that reference. A [quasi-Poisson model](quasi-poisson.qmd) changes the variance scale without supplying a full likelihood, while the [Conway–Maxwell–Poisson distribution](conway-maxwell-poisson-distribution.qmd) can represent narrower counts in a fully specified family. The broader idea of [variance](variance.qmd) as a necessary companion to a centre appears in Dodge's description of dispersion.{{cite:dodge2008}} (p. 341, “Measure of Dispersion”)

## History

Descriptions of data long treated centre and spread as separate summaries; Dodge's encyclopedia explicitly presents dispersion as completing the information supplied by central tendency.{{cite:dodge2008}} (p. 341, “Measure of Dispersion”) In a count regression, the comparison becomes conditional: spread is judged against what a fitted mean model predicts at each covariate setting.
