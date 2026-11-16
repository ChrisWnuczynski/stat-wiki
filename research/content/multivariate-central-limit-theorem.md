## Lead context
The multivariate central limit theorem says that a centred sample mean of random vectors, scaled by the square root of the sample size, settles toward a normal cloud with the population covariance.

## Statement
**A normal limit for the vector average.** Let $X_1,\ldots,X_n$ be independent and identically distributed random vectors in $\mathbb{R}^p$ with mean $\mu$ and covariance $\Sigma$, and write $\overline X_n$ for their sample mean. Then $\sqrt n\,(\overline X_n-\mu)$ converges in distribution to $\operatorname{N}_p(0,\Sigma)$. Equivalently, every fixed non-zero contrast $\lambda^\top\overline X_n$ obeys a scalar central limit theorem, and the Cramér–Wold device turns those scalar limits into the vector limit. Finite variances are enough for this independent identically distributed case. They do not supply a moment-generating function, and they do not cover a dimension $p$ that grows with $n$.{{cite:cameron2004_asymptotic}} (§7, pp. 10–11, multivariate central limit theorem and the Cramér–Wold device)

## Intuition — One normal approximation in every direction
The sample mean is unbiased for $\mu$ and has covariance $\Sigma/n$ whenever the vectors are independent with that covariance, whether or not they are Gaussian. The theorem adds a shape: after multiplication by $\sqrt n$, the cloud of centred means looks normal. A quadratic form in that centred mean is then approximately chi-squared on $p$ degrees of freedom when $\Sigma$ is invertible. Replacing $\Sigma$ by a consistent estimator does not change the limit.{{cite:cameron2004_asymptotic}} (§7, pp. 10–11, the normal limit and a consistent variance)

## Worked example
Take $p=2$, $\Sigma=I_2$, $n=80$, $\mu=0$ and $\overline X_n=(0.2,0.1)^\top$. The quadratic form is
$$
n\,\overline X_n^\top\overline X_n=80(0.04+0.01)=4.
$$
A chi-squared law on two degrees of freedom has survival function $e^{-x/2}$, so it exceeds $4$ with probability $e^{-2}\approx 0.1353$. The number $4$ is a calculation from this observed mean. It is not a certificate that $n=80$ is large enough for a skewed or heavy-tailed coordinate.{{cite:cameron2004_asymptotic}} (§7, pp. 10–11, the normal limit)

**Your turn.** Keep $\Sigma=I_2$ and $\mu=0$, and take $n=20$ with $\overline X_n=(0.5,0)^\top$. Find the same quadratic form and the chi-squared tail probability on $2$ degrees of freedom.

::: {.callout-tip collapse="true" title="Answer"}
The quadratic form is $20(0.25+0)=5$. The tail probability is $e^{-2.5}\approx 0.0821$.{{cite:cameron2004_asymptotic}} (§7, pp. 10–11)
:::

**Check yourself.** A contrast $\lambda=(1,-1)^\top$ and $\Sigma=I_2$ give the scalar average variance $\lambda^\top\Sigma\lambda/n$. What is that variance when $n=80$?

::: {.callout-tip collapse="true" title="Answer"}
$\lambda^\top\Sigma\lambda=1+1=2$, so the variance of the contrast of the sample mean is $2/80=0.025$. The square root of the sample size in the theorem cancels the $n$ in this denominator.{{cite:cameron2004_asymptotic}} (§7, pp. 10–11, scalar projections)
:::

**Check yourself.** Why does the quadratic form $n(\overline X_n-\mu)^\top\Sigma^{-1}(\overline X_n-\mu)$ become undefined if the sample covariance used in place of $\Sigma$ is singular?

::: {.callout-tip collapse="true" title="Answer"}
A singular matrix has no inverse, so the displayed quadratic form cannot be computed. Consistency of a covariance estimator is a separate requirement from invertibility at a finite $n$.{{cite:cameron2004_asymptotic}} (§7, pp. 10–11, positive definite variance)
:::

## Related concepts
The one-coordinate case is the [central limit theorem](central-limit-theorem.qmd). The limiting cloud is a [multivariate normal distribution](multivariate-normal-distribution.qmd). The chi-squared tail used above is the squared length of a standard bivariate normal vector, a [chi-squared distribution](chi-squared-distribution.qmd) on two degrees of freedom. Replacing $\Sigma$ by a consistent estimator leaves that limiting chi-squared law unchanged.{{cite:cameron2004_asymptotic}} (§7, pp. 10–11)
