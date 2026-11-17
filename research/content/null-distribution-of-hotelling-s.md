## Motivating example
Two measurements on the same object may move together. Testing whether their mean vector equals a target should account for that covariance: a displacement along a highly variable direction is different from the same Euclidean displacement along a stable direction. Hotelling's statistic standardizes the mean displacement using the sample covariance matrix. Its null distribution calibrates that distance under a multivariate normal sampling model.{{cite:nist_hotelling2002}} (§6.5.4.3, “Generalize to p variables”)

For one measurement, dividing the sample mean's displacement by its estimated standard error gives Student's t statistic. The multivariate result extends that idea while paying a finite-sample cost for estimating a covariance matrix. The one-dimensional reduction is a useful check of the scale factors.{{cite:dodge2008}} (pp. 528–529)

## Statement
### Exact F calibration {#exact-f-calibration}
Let $X_1,\ldots,X_n$ be independent $N_p(\mu,\Sigma)$ observations with positive-definite $\Sigma$ and $n>p$. Define $S=(n-1)^{-1}\sum_i(X_i-\overline X)(X_i-\overline X)^\top$ and $T^2=n(\overline X-\mu_0)^\top S^{-1}(\overline X-\mu_0)$. Under $H_0:\mu=\mu_0$,
$$\frac{n-p}{p(n-1)}T^2\sim F_{p,n-p}.$$
Use the upper-tail F quantile at the intended level. The covariance estimator's divisor is part of the statement; substituting a different divisor without changing the statistic's scale changes the test.{{cite:nist_hotelling2002}} (§6.5.4.3, “Distribution of T squared”)

## Intuition — Estimated geometry needs a finite-sample correction
If $\Sigma$ were known, the standardized normal mean's squared distance would have a chi-squared law. Replacing $\Sigma$ by the random estimate $S$ adds scale uncertainty and produces the F relationship. The denominator degrees of freedom are $n-p$, rather than $n-1$. The distinction matters when the dimension is not small compared with sample size.{{cite:nist_hotelling2002}} (§6.5.4.3)

The sample scatter matrix has rank at most $n-1$, since its centered rows sum to zero. Thus $p\ge n$ prevents an ordinary inverse. Exact collinearity can also cause singularity when $p<n$. A generalized inverse defines a different statistic and does not automatically inherit this F calibration.

## Proof
The statistic is unchanged by an invertible affine coordinate transformation. Write $Y_i=BX_i+c$ and transform the target in the same way. Then the displacement becomes $B(\overline X-\mu_0)$ and covariance becomes $BSB^\top$. Its inverse is $(B^\top)^{-1}S^{-1}B^{-1}$, so all B factors cancel in the quadratic form. Translation cancels from the displacement. This establishes the coordinate invariance directly.

For $p=1$, write $s^2=S$ for the scalar sample variance. Then $T^2=n(\overline X-\mu_0)^2/s^2=t^2$, and the scaling factor becomes one. A standard normal numerator squared divided by an independent chi-squared variance estimate over $n-1$ degrees of freedom gives $F_{1,n-1}$. This checks the univariate case against the t construction.{{cite:dodge2008}} (pp. 526, 528–529)

## Worked example — Twenty observations in two dimensions
With $n=20$, $p=2$ and observed $T^2=10$, the scaled statistic is $90/19=4.736842$. The 95th percentile of $F_{2,18}$ is $3.554557$, so the 5% test rejects. Its upper-tail probability is $0.0222434$. The corresponding critical value on the T-squared scale is $\{2(19)/18\}\times3.554557=7.504065$. These are the same decision written in two coordinate systems for the test statistic.{{cite:nist_hotelling2002}} (§6.5.4.3, testing a specified mean vector)

The phrase “two dimensions” describes a single joint test of the mean vector. It is not a separate 5% test for each coordinate. Covariance changes the quadratic distance, and the joint critical value is calibrated for that complete statistic.

**Your turn.** If the observed T-squared value were five with the same n and p, calculate the scaled F statistic and decide whether the 5% test rejects.

::: {.callout-tip collapse="true" title="Answer"}
The scaled value is $45/19=2.368421$, below $3.554557$. The test does not reject at 5%.
:::

## Generalizations — Exact calibration and asymptotic approximations
Under finite-dimensional regularity and suitable moment conditions, sample-mean normal approximations can motivate large-sample mean-vector tests outside the normal family. That is a different calibration argument from the exact finite-sample F law. The normal-model F threshold should not be described as exact merely because a sample is moderately large.{{cite:nist_hotelling2002}} (§6.5.4.3, scope of the normal mean test)

The one-sample test is also distinct from control-chart distances computed using the same observations that estimated the reference mean and covariance. Those statistics have different dependencies. A test calibrated for a nominated external $\mu_0$ cannot automatically be transferred to every multivariate monitoring chart.{{cite:nist_hotelling2002}} (§6.5.4.3, “Result does not apply directly to multivariate Shewhart-type charts”)
