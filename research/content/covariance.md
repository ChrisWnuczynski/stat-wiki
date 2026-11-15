## Lead context
Its sign distinguishes variables that tend to rise together from variables that tend to move in opposite directions. It also tells us how much dependence changes the spread of a sum, which matters when combining measurements, risks, or prediction errors.{{cite:nist_error_propagation2002}} (§3.1.3.3)

## Motivating example
Two stages of a job may both run late on difficult days. Adding their separate delay variances would understate the uncertainty in total completion time if large delays tend to occur together. Covariance records that shared movement, so it enters the variance of the combined delay.{{cite:nist_error_propagation2002}} (§3.1.3.3)

## Intuition
For each joint outcome, compare each variable with its own mean and multiply the two deviations. The product is positive when both are above their means or both are below; it is negative when one is above and the other below. Averaging the products gives covariance. Its units are the product of the variables' units: two delays measured in hours give square hours. [Correlation](correlation.qmd) divides out the standard deviations to provide a scale-free comparison.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20) {{cite:nist_covariance2002}} (§6.5.4.1)

## Definition
In the displayed definition, $X$ and $Y$ are random variables with means $\mu_X=\mathbb E X$ and $\mu_Y=\mathbb E Y$. Their covariance is finite when they have finite second moments; then their centred product is integrable by Cauchy–Schwarz. For a discrete pair with joint mass $p(x,y)$, the expectation is $\sum_{x,y}(x-\mu_X)(y-\mu_Y)p(x,y)$; for a pair with joint density $f(x,y)$, replace the sum by a double integral against $f$. The equivalent $\mathbb E(XY)-\mu_X\mu_Y$ form follows by expanding the product.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20)

## Properties
Covariance is symmetric and bilinear: $\operatorname{Cov}(X,Y)=\operatorname{Cov}(Y,X)$ and $\operatorname{Cov}(aX+bY,Z)=a\operatorname{Cov}(X,Z)+b\operatorname{Cov}(Y,Z)$ for constants $a,b$ and finite-second-moment variables. In particular, $\operatorname{Cov}(X,X)=\operatorname{Var}(X)$ and $\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)$. The last term explains why adding component variances works only when their covariance is zero.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20) {{cite:nist_error_propagation2002}} (§3.1.3.3)

Independence makes covariance zero, but zero covariance need not mean independence: the $Y=X^2$ example below shows the distinction. If both variances are positive, [correlation](correlation.qmd) is $\rho=\operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)$, where $\sigma_X$ and $\sigma_Y$ are the standard deviations. It lies between $-1$ and $1$, with equality in magnitude exactly when $Y$ is an affine function of $X$ almost surely with a nonzero slope.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20)

Normality is preserved under linear combinations of jointly normal variables. For independent normal components, the covariance matrix is diagonal and the variance of $a+\sum_i b_iX_i$ is $\sum_i b_i^2\sigma_i^2$. For jointly normal components with covariance matrix $\Sigma$, it is $\mathbf b^\top\Sigma\mathbf b$, where $\mathbf b$ is the column vector of coefficients.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20)

Proof idea: expand centred products and use linearity of expectation; the normal result follows by multiplying characteristic functions or by the linear-combination definition of a jointly normal vector.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Put $X'=X-\mu_X$ and $Y'=Y-\mu_Y$. Expanding $\mathbb E(X'Y')$ gives $\mathbb E(XY)-\mu_X\mu_Y$. Commutativity of multiplication gives symmetry, and linearity of expectation gives bilinearity. Taking $Y=X$ gives variance; expanding $\mathbb E(X'+Y')^2$ gives the sum-variance identity. Under independence, $\mathbb E(XY)=\mathbb E X\,\mathbb E Y$, so covariance vanishes. The case $Y=X^2$ shows that zero covariance does not imply independence. Cauchy–Schwarz gives $|\mathbb E(X'Y')|\leq(\mathbb E X'^2\,\mathbb E Y'^2)^{1/2}=\sigma_X\sigma_Y$, proving the correlation bound. Equality holds exactly when $Y'=cX'$ almost surely for some nonzero constant $c$; this is the asserted affine relation.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20)

For independent normal components, the characteristic function of $a+\sum_i b_iX_i$ the product of the component normal characteristic functions. The product is $\exp\{it(a+\sum_i b_i\mu_i)-t^2(\sum_i b_i^2\sigma_i^2)/2\}$, the characteristic function of the normal law with the stated mean and variance. Every linear combination of a jointly normal vector is normal by definition. Bilinearity gives $\operatorname{Var}(\mathbf b^\top\mathbf X)=\sum_{i,j}b_ib_j\operatorname{Cov}(X_i,X_j)=\mathbf b^\top\Sigma\mathbf b$, proving its variance expression.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20)

For independent identically distributed pairs, expand $\sum_i(X_i-\overline X)(Y_i-\overline Y)$ around the population means. It equals $\sum_i(X_i-\mu_X)(Y_i-\mu_Y)-n(\overline X-\mu_X)(\overline Y-\mu_Y)$. The first sum has expectation $n\operatorname{Cov}(X,Y)$, and independence across pairs makes the expectation of the second term $\operatorname{Cov}(X,Y)$. Thus division by $n-1$ makes the sample covariance unbiased.{{cite:nist_covariance2002}} (§6.5.4.1)
:::
:::

## Statistical use
A sample covariance estimates the population quantity from paired observations. With $n$ independent, identically distributed pairs $(X_i,Y_i)$, its usual estimate is $s_{XY}=\sum_i(x_i-\overline x)(y_i-\overline y)/(n-1)$, where $x_i,y_i$ are realised observations and $\overline x,\overline y$ their sample means. The same calculation fills the off-diagonal entries of a [sample covariance matrix](mean-vector-and-covariance-matrix.qmd); its diagonal entries are sample variances. In error propagation, the covariance term in a sum's variance prevents shared process or measurement errors from being counted as if they were independent.{{cite:nist_covariance2002}} (§6.5.4.1) {{cite:nist_error_propagation2002}} (§3.1.3.3)

## Worked example
Three equally likely workday scenarios produce stage delays $(X,Y)$ of $(1,3)$, $(2,4)$, and $(3,8)$ hours. The means are $\mathbb E X=2$ and $\mathbb E Y=5$. The centred products are $(-1)(-2)=2$, $0(-1)=0$, and $(1)(3)=3$, so $\operatorname{Cov}(X,Y)=(2+0+3)/3=5/3$ square hours. The individual variances are $\operatorname{Var}(X)=2/3$ and $\operatorname{Var}(Y)=14/3$ square hours. Therefore the total delay has variance $2/3+14/3+2(5/3)=26/3$ square hours. Ignoring the positive covariance would give $16/3$ and understate variability.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20)

**Your turn.** Keep the three equally likely values $X=1,2,3$, but let the paired stage-$Y$ delays be $8,4,3$ hours. Find the covariance and the variance of the total delay.

::: {.callout-tip collapse="true" title="Answer"}
Now $\mathbb E Y=5$, and the centred products are $(-1)(3)=-3$, $0(-1)=0$, and $(1)(-2)=-2$. Hence $\operatorname{Cov}(X,Y)=-5/3$ square hours. The separate variances are still $2/3$ and $14/3$, so $\operatorname{Var}(X+Y)=2/3+14/3-10/3=2$ square hours.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20)
:::

The [sample-covariance divisor exercise](../questions/ex-sl-02-1.qmd) applies the same variance expansion to explain the denominator $n-1$.{{cite:nist_covariance2002}} (§6.5.4.1)

Try [signs and their sum](../questions/ex-prob-sign-covariance.qmd), then [where the $n-1$ comes from](../questions/ex-sl-02-1.qmd). The first asks for a joint law before computing covariance; the second extends the centred-product calculation to a covariance matrix.

::: {.callout-tip collapse="true" title="Answers"}
For the sign question, $\mathbb E X=1/4$, $\mathbb E Y=-1$, and $\mathbb E(XY)=-1$, so $\operatorname{Cov}(X,Y)=-3/4$. For uncorrelated random vectors with common covariance matrix $\Sigma$, expanding deviations from the population mean gives expected centred scatter $(n-1)\Sigma$. Normality is not needed.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20)
:::

## Common misconceptions
A covariance of zero means no linear association as measured by centred products; it does not rule out nonlinear dependence. A positive covariance also does not say that both variables are positive: it says their *deviations from their own means* tend to share a sign. Raw covariance magnitudes cannot be compared across different measurement scales; multiplying $X$ by ten multiplies its covariance with $Y$ by ten.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20)

## Assumptions and limits
The familiar finite covariance requires sufficient integrability. Finite second moments guarantee it, but a heavy-tailed pair need not have a finite covariance. Sample covariance can be sensitive to a single extreme pair. Its sign and size summarize linear co-movement, so inspect the joint pattern, not just one number. Even a reliable positive covariance in observational data does not establish that changing one variable would cause the other to change.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20) {{cite:nist_covariance2002}} (§6.5.4.1) {{cite:dicker2025_cdc}} (Ch. “Analyzing and Interpreting Data”)

## Connections
[Variance](variance.qmd) is covariance with both arguments the same. [Correlation](correlation.qmd) divides covariance by two standard deviations; it keeps the sign while removing units. The [covariance matrix](mean-vector-and-covariance-matrix.qmd) collects pairwise covariances for a random vector, and the variance of a linear combination is its quadratic form. Independent variables have zero covariance, while the $Y=X^2$ example shows that the converse fails.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.2.23, 6.3.17–20) {{cite:nist_covariance2002}} (§6.5.4.1)

## History
Pearson's 1896 paper on regression, heredity and panmixia studied joint variation in family measurements. Its published abstract describes the effort to analyse hereditary patterns mathematically.{{cite:pearson1896}} (Abstract)
