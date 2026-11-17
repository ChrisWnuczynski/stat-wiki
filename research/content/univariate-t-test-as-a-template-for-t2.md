## Motivating example
A sample mean two units from its target can be a large discrepancy or a small one, depending on the variability and number of measurements. The Student statistic measures that discrepancy in estimated standard-error units. Squaring it removes its direction and reveals the quadratic form that extends to several response variables.{{cite:nist_handbook2002}} (§6.5.4.3, univariate calculation)

## Definition — The one-dimensional pivot
For $n>1$ independent normal observations with positive variance, the Student statistic is
$$t=\frac{\bar X-\mu_0}{s/\sqrt n}.$$
Under the null, the standardised mean $Z=\sqrt n(\bar X-\mu_0)/\sigma$ is standard normal, while $W=(n-1)s^2/\sigma^2$ is chi-squared on $n-1$ degrees of freedom and independent of $Z$. Thus $t=Z/\sqrt{W/(n-1)}$ has the Student distribution. Orthogonal projection of the Gaussian observation vector onto the constant-vector direction and its perpendicular residual space explains the independence: the mean uses one coordinate and residual sum of squares uses the other $n-1$.{{cite:openintro2019}} (§7.1, “One-sample means with the t-distribution”)

This exact calibration assumes normal observations. In large samples a normal or Student approximation can sometimes be justified under weaker conditions, but the estimated standard error still needs to reflect the sampling design. Repeated observations on the same person do not supply $n$ independent pieces of information simply by being arranged in $n$ rows.

## Properties — From a signed discrepancy to a quadratic form
Squaring the statistic gives
$$t^2=n(\bar X-\mu_0)(s^2)^{-1}(\bar X-\mu_0).$$
The factors are a difference, an inverse variance and the difference again. Under the null, $Z^2$ is chi-squared on one degree of freedom, so $t^2$ has an $F_{1,n-1}$ distribution. Hence a two-sided Student cutoff satisfies $t_{n-1;1-\alpha/2}^2=F_{1,n-1;1-\alpha}$.{{cite:nist_handbook2002}} (§6.5.4.3, square of Student's statistic)

For a $p$-dimensional mean, replace the scalar squared difference by
$$T^2=n(\bar{\boldsymbol X}-\boldsymbol\mu_0)^TS^{-1}(\bar{\boldsymbol X}-\boldsymbol\mu_0).$$
Off-diagonal covariances rotate and rescale the discrepancy. The statistic is a squared Mahalanobis distance, so it loses the simple sign of the univariate $t$. Its exact normal-model calibration is $\frac{n-p}{p(n-1)}T^2\sim F_{p,n-p}$ when $n>p$ and the population covariance is positive definite. At $p=1$, the multiplier is one and $T^2=t^2$ exactly.{{cite:nist_handbook2002}} (§6.5.4.3, multivariate statistic and distribution)

## Worked example — Check the reduction numerically
The observations $8,9,10,11,12$ have mean $10$ and sample variance $2.5$. Testing $\mu_0=8$ gives standard error $\sqrt{2.5/5}=\sqrt{0.5}$ and $t=2\sqrt2\approx2.828427$. Squaring gives $8$. The direct one-dimensional Hotelling calculation is also $5(10-8)^2/2.5=8$.

The two-sided $5\%$ Student critical value is approximately $2.776445$ on four degrees of freedom. Its square is approximately $7.708647$, equal to the $95\%$ quantile of $F_{1,4}$. The two-sided $p$-value is approximately $0.047421$ by either the Student tail or the upper $F$ tail. The calculation demonstrates equivalence of the two procedures under a common sampling model and tail allocation.{{cite:openintro2019}} (§7.1, Student inference)

**Your turn.** A sample of $n=9$ has mean $3$, sample variance $4$ and null mean $1$. Compute $t$, $t^2$ and the direct $p=1$ Hotelling statistic.

::: {.callout-tip collapse="true" title="Answer"}
The standard error is $2/3$, so $t=(3-1)/(2/3)=3$. Both squared statistics are $9$, since $9(3-1)^2/4=9$. The null $F$ distribution has degrees of freedom $(1,8)$.
:::

## Connections — The two-sample template
For two independent groups with a common variance, replace $s^2/n$ by $s_p^2(1/n_1+1/n_2)$. Squaring again produces a pooled two-sample quadratic form. In several dimensions replace the pooled variance by the pooled covariance matrix and use the inverse covariance of the mean difference. This is the two-sample Hotelling statistic, with its own dimension-adjusted $F$ multiplier.

The template also identifies where analogy ends. A singular sample covariance cannot be inverted in the classical statistic. Replacing it by a pseudoinverse or a regularised estimator defines another procedure; its null law requires separate calibration. The number of coordinates changes the reference distribution as well as the algebraic shape of the distance. (Appendix, dimension reduction and covariance regularisation)

## Assumptions and limits
Student's exact law needs a nondegenerate normal model and a nonzero observed sample standard deviation. A constant observed sample does not permit division by zero; it is a boundary case requiring a separate model assessment. Squaring is appropriate for a two-sided discrepancy but discards direction, so it cannot reproduce a one-sided Student test without keeping the sign as additional information.

Squaring a two-sided t statistic produces the matching one-numerator F statistic, and the tail probabilities agree once the two-sided t event is written as an upper tail for that square.
