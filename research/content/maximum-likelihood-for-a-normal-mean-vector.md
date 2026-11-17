## Motivating example
A laboratory measures two chemical concentrations on each specimen and wants their common mean vector. The measurement coordinates may be strongly correlated. Under independent multivariate normal sampling with one common covariance, maximizing the likelihood still gives the coordinatewise sample means. Correlation affects the uncertainty ellipse, even though it does not change that maximizing vector.

## Definition — The sampling model and the target
Let $X_1,\ldots,X_n$ be independent $N_p(\mu,\Sigma)$ vectors, with the same positive definite covariance $\Sigma$. For any fixed admissible $\Sigma$, the unique mean maximizer is $\widehat\mu=\overline X=n^{-1}\sum_iX_i$. It is a vector statement: maximizing each coordinate separately without respecting the joint quadratic form happens to produce the same answer because all observations share the same covariance. If different observations have different known covariance matrices, that cancellation changes.

## Properties — Sampling uncertainty and transformations
Linearity of expectation gives $E(\overline X)=\mu$. Independence makes all between-observation covariance terms zero, yielding $\operatorname{Cov}(\overline X)=\Sigma/n$. A linear combination of independent normal vectors is normal, so $\overline X\sim N_p(\mu,\Sigma/n)$ exactly. For any fixed vector $a$, the estimated contrast $a^\top\overline X$ has variance $a^\top\Sigma a/n$. Covariance matters whenever the target combines coordinates.

If $Y_i=BX_i+c$ for a fixed matrix and vector, then $\overline Y=B\overline X+c$. This affine equivariance follows by distributing the average over the transformation. It allows units and coordinate systems to change coherently. In the likelihood, the quadratic decomposition in the sample mean proves global optimality because its additional term is nonnegative and zero only at the mean. The existence of this conditional mean maximizer does not ensure that a joint unrestricted covariance maximizer exists: singular centered scatter can still make the joint likelihood unbounded.{{cite:goodfellow_bengio_courville2016}} (§5.5, maximum likelihood)

## Worked example — A mean and a contrast
For vectors $(1,2),(3,2),(2,5)$, $\widehat\mu=(2,3)$. If the common covariance is known to be
$$\Sigma=\begin{pmatrix}4&1\\1&9\end{pmatrix},$$
the estimated difference between mean coordinates is $2-3=-1$. Its variance is $(4+9-2)/3=11/3$, giving standard error $\sqrt{11/3}\approx1.914854$. Ignoring covariance would give $\sqrt{13/3}\approx2.081666$, a larger value in this example because the positive covariance cancels in a difference. For a sum, the same positive covariance adds instead.

For a candidate mean $\mu=(0,0)$, the quadratic loss in the likelihood exceeds its value at $(2,3)$ by $n(\overline x-\mu)^\top\Sigma^{-1}(\overline x-\mu)$. This is $36/7\approx5.142857$, so the likelihood ratio of the candidate to the fitted mean is $e^{-18/7}\approx0.076426$. This comparison uses known covariance and holds the observed vectors fixed.

**Your turn.** Two independent vector observations are $(0,1)$ and $(4,5)$, with common covariance $I_2$. Find the MLE and the standard error of the sum of its coordinates.

::: {.callout-tip collapse="true" title="Answer"}
The MLE is $(2,3)$. The sum has variance $(1+1)/2=1$, so its standard error is one.
:::

## Statistical use — Unequal known covariances
For independent $X_i\sim N_p(\mu,\Sigma_i)$ with known positive definite matrices, differentiation gives
$$\widehat\mu=\left(\sum_i\Sigma_i^{-1}\right)^{-1}\sum_i\Sigma_i^{-1}X_i.$$
To verify the maximum, the Hessian of the log-likelihood is $-\sum_i\Sigma_i^{-1}$, which is negative definite. Equal covariance reduces this expression to the ordinary mean; unequal precision gives more influence to more informative observations and directions. This is a different model from common-covariance sampling.{{cite:goodfellow_bengio_courville2016}} (§5.5, likelihood maximization)

## Connections — A joint confidence region with known covariance
When $\Sigma$ is known, whitening gives $Z=\sqrt n\Sigma^{-1/2}(\overline X-\mu)\sim N_p(0,I)$. Therefore $Z^\top Z=n(\overline X-\mu)^\top\Sigma^{-1}(\overline X-\mu)$ is chi-squared with $p$ degrees of freedom. Inverting the central probability statement gives an exact ellipsoidal confidence region for the whole vector. This has joint coverage for a candidate vector and is different from placing separate unadjusted intervals on its coordinates.

For two coordinates, the 95% chi-squared cutoff is approximately $5.991465$. The candidate zero vector in the worked example has quadratic statistic $36/7\approx5.142857$, so it lies inside this known-covariance confidence ellipse. Changing the sample size, the covariance or the candidate mean changes that comparison. If covariance is estimated from the same sample, this chi-squared calibration is replaced by an appropriate estimated-covariance procedure; simply substituting an estimate does not preserve exact small-sample coverage.

## Interpretation — Precision weights and a contrast
When every observation has the same known covariance, the likelihood score for $\mu$ is proportional to $\Sigma^{-1}$ times the sum of $(x_i-\mu)$. The unique root is the sample mean. Correlation changes the quadratic form and cancels out of the location of the root. It does not cancel out of a contrast. In the worked sample the difference of coordinates has estimated value $-1$ and variance $(4+9-2)/3=11/3$, so the standard error is about $1.914854$. Dropping the covariance $1$ replaces $11/3$ by $13/3$ and the standard error by about $2.081666$. The same covariance added to a sum of coordinates would enlarge the variance. The mean vector can be reported coordinatewise. A scientific comparison that adds or subtracts coordinates needs the off-diagonal entries.

Unequal known covariances change the root itself. Two scalar observations $0$ and $10$ with variances $1$ and $4$ have precisions $1$ and $1/4$. The common-mean maximum likelihood estimate is $(0\cdot1+10\cdot1/4)/(1+1/4)=2$. The ordinary average $5$ would maximise the likelihood only if the variances were equal. In vector form the same weights are the inverses $\Sigma_i^{-1}$, and the Hessian $-\sum_i\Sigma_i^{-1}$ is negative definite when each $\Sigma_i$ is positive definite and at least one observation is present. The formula is the Gauss–Markov weighted mean for known Gaussian covariances. It is not the estimator for a shared unknown covariance, which returns to the unweighted mean.{{cite:goodfellow_bengio_courville2016}} (§5.5, likelihood maximization)

For $n=8$ independent copies with $\Sigma=\operatorname{diag}(4,16)$, the covariance of the sample mean is $\operatorname{diag}(4,16)/8=\operatorname{diag}(1/2,2)$. Each coordinate's variance is divided by the sample size. The correlation is zero in this $\Sigma$, so the covariance of the mean stays diagonal. A nondiagonal $\Sigma$ divided by $n$ keeps its correlations and shrinks every entry by $n$. Affine equivariance says that if the laboratory rescales the measurements by a fixed matrix $B$ and then adds a fixed offset $c$, the maximum likelihood estimate transforms by the same $B$ and $c$. Units can be changed after averaging or before averaging, with the same vector at the end.

## Common misconceptions
The ellipsoidal region $\{ \mu: n(\overline x-\mu)^\top\Sigma^{-1}(\overline x-\mu)\le \chi^2_{p,1-\alpha}\}$ covers the true mean with probability $1-\alpha$ when $\Sigma$ is known and the vectors are independent and normal. It is a joint statement. Two separate intervals, one per coordinate, each with marginal coverage $0.95$, do not automatically have joint coverage $0.95$, and their rectangle is a different shape from the ellipse. In the worked example the origin is inside the $95\%$ ellipse because $5.142857<5.991465$. A coordinatewise reading of the estimates $(2,3)$ does not by itself produce that comparison. The quadratic form uses $\Sigma^{-1}$.

The sample mean maximises the Gaussian likelihood for any fixed positive definite $\Sigma$. It does not guarantee that a joint maximizer over $(\mu,\Sigma)$ exists. If the centered scatter is singular, the likelihood can be driven to infinity by a covariance that collapses in the null direction, even though the mean profile at each fixed $\Sigma$ is perfectly well behaved. Reporting $\overline x$ as the mean estimate and $A/n$ as a covariance estimate is the joint maximum likelihood estimate only when $A/n$ is positive definite. Otherwise $\overline x$ is still the conditional maximizer for each fixed $\Sigma$, and the joint problem has no maximizer in the positive definite cone.{{cite:goodfellow_bengio_courville2016}} (§5.5, maximum likelihood)
