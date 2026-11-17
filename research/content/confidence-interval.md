## Lead context
It reports uncertainty about a population quantity through the performance of a repeatable sampling method. The stated confidence describes how often that method covers the quantity across repeated samples.{{cite:neyman1937}} (pp. 347–350, 378–379) {{cite:nist_mean_limits2002}} (§1.3.5.2)

## Motivating example
Suppose a factory weighs a random sample of tablets to estimate their production mean. A sample mean gives one number; an interval gives lower and upper limits that account for sampling variation. The calculation must also say which model and confidence level were used, because a numerical pair of limits alone has no coverage guarantee.{{cite:nist_mean_limits2002}} (§1.3.5.2)

## Intuition
Imagine drawing a fresh sample and drawing its interval, again and again. The interval moves with the sample while the population mean stays fixed. A 95% procedure is calibrated to include that fixed mean in 95% of repetitions under its assumptions. The forty intervals in the figure above are one simulation of this experiment; a particular interval either includes the mean or misses it.{{cite:neyman1937}} (pp. 347–350) {{cite:nist_mean_limits2002}} (§1.3.5.2)

## Definition
The confidence level in the displayed definition is $1-\alpha$, with $0<\alpha<1$ chosen before looking at the sample; $L$ and $U$ are lower and upper functions of the random data, and $\mathbb P_\theta$ denotes probability when the true parameter is $\theta$. Equality gives *exact* coverage at every parameter value. A procedure is *conservative* at nominal level $1-\alpha$ if its coverage is at least $1-\alpha$ for every value; this distinction matters for discrete data, where the attainable coverage probabilities can jump. Once a sample is observed, its endpoints $l$ and $u$ are numbers.{{cite:neyman1937}} (pp. 347–350, 378–379) {{cite:nist_mean_limits2002}} (§1.3.5.2)

A [pivot](pivot.qmd) is a statistic involving the data and candidate parameter whose sampling law is known without any unknown model parameters. Quantiles of that law define a probability statement about the pivot; solving the inequalities for the parameter gives the interval. For a normal mean with unknown variance, the sample standard deviation replaces the unknown population standard deviation and the pivot has a Student $t$ law.{{cite:siegrist2022_normals}} (§6.08, “The T Variable”) {{cite:nist_mean_limits2002}} (§1.3.5.2)

## Properties
For $n\ge2$ independent normal observations $X_1,\ldots,X_n$ with common mean $\mu$ and variance $\sigma^2>0$, the one-sample $t$ pivot in this section yields the interval $\overline X\pm t_{n-1;1-\alpha/2}s/\sqrt n$ for $\mu$. Here $\overline X$ is the sample mean, $s$ is the bias-corrected sample standard deviation, and $t_{m;q}$ is the $q$ quantile of Student's $t$ distribution with $m$ degrees of freedom. Its exact coverage follows from normal sampling, including the independence of $\overline X$ and $s^2$.{{cite:siegrist2022_normals}} (§6.08, “The T Variable”) {{cite:nist_mean_limits2002}} (§1.3.5.2)

The two-sample $t$ pivot below compares independent normal-sample means of sizes $n_1,n_2\ge2$ when the two populations share one positive variance; it uses the pooled variance and $n_1+n_2-2$ degrees of freedom. The $F$ pivot compares sample variances from independent normal populations and has numerator and denominator degrees of freedom $n_1-1$ and $n_2-1$. Both statements depend on the assumptions printed with their formulas.{{cite:siegrist2022_normals}} (§6.08, “The Two Sample Model”)

For a fixed-design simple regression with $n\ge3$, distinct input values, and independent normal errors of common positive variance, the slope pivot uses the residual standard error and $n-2$ degrees of freedom. It gives a confidence interval for the slope $\beta_1$; a two-sided test of a proposed slope rejects at level $\alpha$ exactly when that value lies outside the corresponding interval. The same inversion connects a two-sided $t$ test of a normal mean with its $t$ interval.{{cite:fox2016_regression}} (Ch. 6, §6.1.3, pp. 111–112) {{cite:nist_mean_limits2002}} (§1.3.5.2)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
**Coverage and one sample.** Under the stated normal model, $Z=(\overline X-\mu)/(\sigma/\sqrt n)$ is standard normal, $V=(n-1)s^2/\sigma^2$ is chi-squared with $n-1$ degrees of freedom, and $Z$ and $V$ are independent. Hence $T=Z/\sqrt{V/(n-1)}=(\overline X-\mu)/(s/\sqrt n)$ has the $t_{n-1}$ law. The event $-t_{n-1;1-\alpha/2}\le T\le t_{n-1;1-\alpha/2}$ is algebraically the event that $\mu$ lies between $\overline X\pm t_{n-1;1-\alpha/2}s/\sqrt n$. Its probability is $1-\alpha$.{{cite:siegrist2022_normals}} (§6.08, “The T Variable”) {{cite:nist_mean_limits2002}} (§1.3.5.2)

**Two samples and variance ratio.** Under the equal-variance two-sample model, the standardized difference of sample means is normal. Each sample's scaled residual sum of squares is an independent chi-squared variable with $n_j-1$ degrees of freedom, independent of both means. Adding the two residual sums gives a chi-squared variable with $n_1+n_2-2$ degrees of freedom; dividing the normal score by its square-root scale gives the displayed pooled $t$ pivot. Separately, dividing each scaled sample variance by its degrees of freedom and taking their ratio gives the displayed $F_{n_1-1,n_2-1}$ pivot, without assuming equal population variances for that ratio.{{cite:siegrist2022_normals}} (§6.08, “The Two Sample Model”)

**Regression slope.** Let $S_{xx}=\sum_i(x_i-\overline x)^2>0$ for fixed inputs $x_i$. The fitted slope error is $\widehat\beta_1-\beta_1=\sum_i(x_i-\overline x)\varepsilon_i/S_{xx}$, so its standard-normal score is $Z=(\widehat\beta_1-\beta_1)/(\sigma/\sqrt{S_{xx}})$. Orthogonal projection of the normal error vector onto the span of the intercept and centred input leaves an independent residual with squared length $V=\mathrm{RSS}/\sigma^2\sim\chi^2_{n-2}$. With $S^2=\mathrm{RSS}/(n-2)$ and $S_1=S/\sqrt{S_{xx}}$, the printed slope pivot is $Z/\sqrt{V/(n-2)}\sim t_{n-2}$. Inverting its central probability event gives the slope interval and the stated test equivalence.{{cite:fox2016_regression}} (Ch. 6, §6.1.3, pp. 111–112)
:::
:::

## Statistical use
Choose the target parameter and sampling procedure first, then check how the data were selected and whether the proposed model can justify the interval. A wider confidence level requires a more extreme quantile and, with the same data, a wider usual mean interval; increasing sample size usually narrows it. For a normal mean with unknown variance, the $t$ interval also widens when the observed sample standard deviation grows. Report the interval with its target, units, confidence level, and method.{{cite:nist_mean_limits2002}} (§1.3.5.2)

The normal-variance interval in the worked examples uses chi-squared quantiles, while the difference-of-means interval uses a pooled $t$ law only when the equal-variance model is appropriate. These are distinct sampling questions. The [interval-coverage laboratory](../labs/ci-coverage.qmd) draws repeated samples so that the coverage rate can be seen rather than inferred from one observed interval.{{cite:siegrist2022_normals}} (§6.08, “The Two Sample Model”) {{cite:nist_mean_limits2002}} (§1.3.5.2)

## Worked example
Suppose twenty independent repetitions each produce a 95% confidence interval by a correctly calibrated procedure. If $C_j$ is one when repetition $j$ covers the true parameter and zero otherwise, then $\mathbb E\sum_{j=1}^{20}C_j=20(0.95)=19$. The count need not equal 19: independence would make the probability that *all* twenty cover $0.95^{20}\approx0.3585$. A run with two misses does not, by itself, change the procedure's 95% coverage claim.{{cite:neyman1937}} (pp. 347–350, 378–379) {{cite:nist_mean_limits2002}} (§1.3.5.2)

**Your turn.** If the same independent 95% procedure is repeated ten times, what is the expected number of intervals that cover, and what is the probability that all ten cover?

::: {.callout-tip collapse="true" title="Answer"}
The expected count is $10(0.95)=9.5$. Under independence, the probability that all ten cover is $0.95^{10}\approx0.5987$. An expected count need not be an integer.
:::

## Common misconceptions
After observing $(l,u)$, a frequentist confidence statement does not assign a 95% probability to the fixed parameter being inside these fixed endpoints. The probability statement concerns the random endpoints before sampling. A 95% interval also does not say that 95% of future observations fall inside it; a [prediction interval](prediction-interval.qmd) has a different target. Narrowness alone is no proof of good calibration: an interval method must still attain its promised coverage under the stated model.{{cite:neyman1937}} (pp. 347–350, 378–379) {{cite:nist_mean_limits2002}} (§1.3.5.2)

## Assumptions and limits
The exact $t$, chi-squared, and $F$ intervals here use independent normal observations and the variance conditions specified for each pivot. Repeated observations from one dependent time series, a heavily skewed small sample, or unequal variances in the pooled two-sample interval can invalidate the quoted exact coverage. Large-sample approximations and resampling methods need their own calibration checks; the confidence level is always a claim about a particular method under particular conditions.{{cite:siegrist2022_normals}} (§6.08, “The One Sample Model”; “The Two Sample Model”) {{cite:nist_mean_limits2002}} (§1.3.5.2)

## Connections
A [standard error](standard-error.qmd) estimates the sampling spread of an estimator and sets the scale of many confidence intervals. A [pivot](pivot.qmd) supplies a distribution whose quantiles determine exact model-based limits; a [two-sided hypothesis test](tests-and-confidence-intervals.qmd) and an interval can be obtained by inverting the same acceptance rule. A [Bayesian credible interval](bayesian-credible-interval.qmd) instead states posterior probability for the parameter given observed data, under a specified prior and likelihood.{{cite:neyman1937}} (pp. 347–350, 378–379) {{cite:nist_mean_limits2002}} (§1.3.5.2)

## History
Jerzy Neyman's 1937 paper began with the practical problem of estimating an unknown feature of a population or repeatable experiment from a sample. He distinguished a single numerical estimate from two sample-based limits and asked for a precise probability guarantee on the interval method. The paper's second part formulates lower and upper functions of the data that cover a fixed parameter at a specified long-run rate.{{cite:neyman1937}} (pp. 333–334, 346–350)

Neyman also treated one-sided limits and the problem of choosing among procedures with the same coverage but different lengths. His summary distinguishes the randomness of the limits from the fixed value of the parameter. The modern normal-mean $t$ interval is a familiar application of that framework: its level follows from a pivot's sampling distribution.{{cite:neyman1937}} (pp. 370–379) {{cite:nist_mean_limits2002}} (§1.3.5.2)
