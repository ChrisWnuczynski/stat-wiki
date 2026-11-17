## Motivating example
A normal fit estimates its centre by the sample mean. Its likelihood estimate of variance divides the residual sum of squares by $n$, while the usual unbiased sample variance divides by $n-1$. Both quantities use the same residuals, but optimise different criteria: one maximises the observed-data likelihood and the other corrects a repeated-sampling expectation. Calling both a sample variance can conceal that distinction.{{cite:dodge2008}} (pp. 334–335, Maximum Likelihood)

## Properties — Profile out the centre before the variance
Put $v=\sigma^2>0$, $\bar x=n^{-1}\sum_i x_i$ and $S=\sum_i(x_i-\bar x)^2$. The sum-of-squares identity
$$\sum_i(x_i-\mu)^2=S+n(\mu-\bar x)^2$$
follows by expanding around $\bar x$ and using $\sum_i(x_i-\bar x)=0$. For each fixed positive $v$, the likelihood is uniquely maximised at $\mu=\bar x$. The profile log-likelihood is $\ell_p(v)=C-\tfrac n2\log v-S/(2v)$. Its derivative is $(S-nv)/(2v^2)$, positive below $S/n$ and negative above it when $S>0$. Therefore the stationary point is the global maximum, not merely a solution of the score equations.{{cite:dodge2008}} (pp. 334–335)

The maximum is $\widehat v=S/n$ whenever at least two observations differ. If all observations coincide, then $S=0$ and $\ell_p(v)$ increases without bound as $v\downarrow0$. Since the ordinary normal parameter space excludes zero variance, a finite maximum does not exist. Reporting a zero variance in that case describes a boundary limit rather than an attained maximum within the positive-variance normal family. The positivity requirement belongs to the distributional model itself.{{cite:nist_normal_distribution}} (§1.3.6.6.1, probability density function)

## Interpretation — Sampling properties follow the selected criterion
The identity $S=\sum_i(X_i-\mu)^2-n(\bar X-\mu)^2$ gives $\mathbb ES=n\sigma^2-n\operatorname{Var}(\bar X)=(n-1)\sigma^2$ for iid observations with finite variance. Consequently $\mathbb E\widehat v=(n-1)\sigma^2/n$ and $S/(n-1)$ is unbiased when $n>1$. Normality supplies the likelihood being optimised, but this expectation identity uses only independence, common mean and common finite variance.{{cite:dodge2008}} (p. 335, variance-estimator bias)

Taking a square root gives the MLE of the standard deviation because the mapping $v\mapsto\sqrt v$ is one-to-one on positive variances. It does not make the square root of the unbiased variance estimator unbiased for $\sigma$. Nonlinear transformations generally change bias. Meanwhile the normal model's population mean, median and mode all equal $\mu$; estimating the population centre by $\bar X$ should not be confused with claiming that a finite dataset has identical mean, median and mode.{{cite:nist_normal_distribution}} (§1.3.6.6.1, Common Statistics)

## Worked example — Four measurements
For observations $1,2,4,5$, the sample mean is $3$ and $S=4+1+1+4=10$. Hence $\widehat\mu=3$, $\widehat{\sigma^2}=10/4=2.5$, and the unbiased variance is $10/3$. The MLE standard deviation is $\sqrt{2.5}\approx1.581139$. The profile log-likelihood at $v=2.5$ exceeds its value at $v=5$ by $2\log2-1\approx0.386294$, using the same fitted mean in both evaluations. The increase is a likelihood comparison for these observations, rather than a significance probability.

**Your turn.** If the mean is known to be zero for the same measurements, what is the variance MLE?

::: {.callout-tip collapse="true" title="Answer"}
With the mean fixed at zero, the sum of squared deviations is $1+4+16+25=46$. The variance MLE is $46/4=11.5$. Estimating the mean and fixing it at a known value are different optimisation problems.
:::

## Assumptions and limits — What the normal fit does and does not assume
The product likelihood requires independent observations with a shared mean and variance. Correlated observations require their joint covariance in the likelihood; unequal known variances change the mean estimate to a precision-weighted average. If observations are normal only after a transformation, the density and any Jacobian must match the variable actually observed. A normal likelihood for raw measurements cannot automatically be used for their logarithms.{{cite:nist_normal_distribution}} (§1.3.6.6.1, density and modelling comments)

For iid data from another distribution, maximising the normal expression still returns the empirical mean and the $1/n$ empirical variance when $S>0$. Those estimates describe the fitted Gaussian approximation. Distribution-specific likelihood claims and exact Gaussian confidence statements then need separate justification. In particular, a large sample does not change skewed individual observations into normal observations; asymptotic normality of a sample mean is a statement about a sampling distribution.{{cite:dodge2008}} (pp. 334–335, scope of maximum likelihood)

## Connections

Dividing the centred sum of squares by $n$ maximises the normal likelihood. Dividing by $n-1$ removes the bias that comes from using the sample mean in place of the population mean. The two divisors answer different questions. The square root of either estimator is not automatically unbiased for the standard deviation, because a square root is nonlinear. When the mean is a known number, squared deviations are taken about that number and the likelihood divisor is still $n$. No degree of freedom is spent on estimating a centre. [Normal distribution](normal-distribution.qmd) is the sampling model. [Maximum likelihood](maximum-likelihood.qmd) maximises the joint density of the sample. [Moments of the sample mean and variance](moments-of-the-sample-mean-and-variance.qmd) record the second-moment calculation that makes $S/(n-1)$ unbiased without requiring the full normal likelihood.

If every observation equals the same number, the profile log-likelihood increases without bound as the variance decreases to zero. The positive-variance family then has no maximiser. A reported variance of zero describes that limit from outside the open parameter space. A nearly constant sample has a very small maximiser. Dependence among the observations, or a heavy-tailed error distribution, is not repaired by switching from the likelihood divisor to the unbiased divisor. Both formulas still treat the centred sum of squares as if the observations were independent with a common variance.{{cite:dodge2008}} (p. 335, variance-estimator bias){{cite:nist_normal_distribution}} (§1.3.6.6.1, density and modelling comments)
