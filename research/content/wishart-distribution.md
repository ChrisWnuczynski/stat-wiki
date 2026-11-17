## Lead context
A Wishart matrix is the sum of outer products of independent normal vectors, the matrix analogue of a sum of squared normal observations.

## Motivating example
Five independent measurements of two correlated traits produce a $2\times 2$ matrix of corrected cross-products. The mean of that matrix is $4$ times the population covariance, because one degree of freedom is spent on the sample mean. Knowing only that mean does not say whether a particular sample matrix is a typical scatter or an unusually large one. The Wishart law is the distribution of the scatter. Its one-dimensional case is a scaled chi-squared variable, which is why a normal sample variance has a chi-squared law.{{cite:wishart1928}} (pp. 32–52) The mean of a sum of outer products is a separate fact, from linearity of expectation.{{cite:durrett2019}} (Thm. 1.6.1, p. 29)

## Intuition
Each centred normal vector $\mathbf{U}$ contributes the rank-one matrix $\mathbf{U}\mathbf{U}^\top$. The $(i,j)$ entry of that matrix is the product $U_i U_j$. Adding $\nu$ independent copies gives a scatter whose mean is $\nu\Sigma$ whenever $\mathrm{E}(\mathbf{U}\mathbf{U}^\top)=\Sigma$, and that mean calculation uses linearity rather than the Wishart density.{{cite:durrett2019}} (Thm. 1.6.1, p. 29) Normality is what makes the whole matrix Wishart, and what makes the sample mean independent of the scatter.{{cite:wishart1928}} (pp. 32–52)

## Definition
For integer $\nu\ge p$ the construction is $W=\sum_{m=1}^{\nu}\mathbf{U}_m\mathbf{U}_m^\top$ with the $\mathbf{U}_m$ independent $\mathrm{N}_p(0,\Sigma)$. The density on positive-definite matrices is the one displayed above. At $p=1$ and $\Sigma=1$ the sum of squares is $\chi^2_\nu$. At $p=1$ and scale $\sigma^2$ the same sum is $\sigma^2\chi^2_\nu$, with mean $\nu\sigma^2$ and variance $2\nu\sigma^4$.

The entry covariances
$$
\mathrm{Cov}(W_{ij},W_{kl})=\nu(\Sigma_{ik}\Sigma_{jl}+\Sigma_{il}\Sigma_{jk})
$$
are the multivariate form of that variance. They remain meaningful as moments even when one is not using the density.

## Properties
The mean and the Gaussian fourth-moment identity that feeds the variance are elementary.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $W=\sum_{m=1}^{\nu}\mathbf{U}_m\mathbf{U}_m^\top$ with $\mathrm{E}(\mathbf{U}_m\mathbf{U}_m^\top)=\Sigma$. Linearity of expectation, applied entrywise, gives $\mathrm{E} W=\nu\Sigma$. No normality was used.{{cite:durrett2019}} (Thm. 1.6.1, p. 29)

For a standard normal density, $\varphi'(z)=-z\varphi(z)$. For $k\ge 1$, integration by parts with vanishing boundary terms gives
$$
\mathrm{E} Z^{k+1}=\int z^{k}(- \varphi'(z))\,\mathrm{d}z=k\,\mathrm{E} Z^{k-1}.
$$
Thus $\mathrm{E} Z^2=1$ and $\mathrm{E} Z^4=3\,\mathrm{E} Z^2=3$. If $U=\sigma Z$, then $\mathrm{E} U^2=\sigma^2$ and $\mathrm{E} U^4=3\sigma^4$, so $\mathrm{Var}(U^2)=2\sigma^4$.

A sum of $\nu$ independent copies has variance $2\nu\sigma^4$. That is the scalar case of the entry formula: with $p=1$ and $\Sigma=\sigma^2$,
$$
\mathrm{Var}(W)=\nu(\sigma^2\cdot\sigma^2+\sigma^2\cdot\sigma^2)=2\nu\sigma^4.
$$
For $\sigma^2=2$ and $\nu=4$ the mean is $8$ and the variance is $32$. The mean is $\nu\sigma^2$ by linearity.{{cite:durrett2019}} (Thm. 1.6.1, p. 29) The variance $2\nu\sigma^4$ is the one-dimensional Wishart moment.{{cite:wishart1928}} (pp. 32–52)
:::
:::

## Related distributions
A chi-squared law on $\nu$ degrees of freedom is $W_1(1,\nu)$. A sample variance from $\mathrm{N}(\mu,\sigma^2)$ satisfies $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$, which is the case $\nu=n-1$ and $p=1$. The sample covariance matrix of a $\mathrm{N}_p(\boldsymbol{\mu},\Sigma)$ sample is $A/(n-1)$ with $A\sim W_p(\Sigma,n-1)$, so the Wishart degrees of freedom are one less than the sample size. The multivariate normal law of the sample mean is a different distribution, independent of $A$ under normal sampling.

## Statistical inference
**Scatter, mean, and degrees of freedom.** Hotelling's $T^2$ compares a normal mean vector with a hypothesised value by using a Wishart matrix as the estimated scatter. The null calibration is an $F$ law because a normal vector and an independent Wishart matrix produce the same ratio that, in one dimension, is a normal variable over an independent root-chi-squared variable. The degrees of freedom in the denominator fall by the dimension: $n-1$ becomes $n-p$ in the one-sample $F$. Using $n$ instead of $n-1$ as the Wishart degrees of freedom assigns the scatter the wrong mean, $(n)\Sigma$ rather than $(n-1)\Sigma$.

## Generating random samples
For integer $\nu\ge p$, draw $\nu$ independent $\mathrm{N}_p(0,\Sigma)$ vectors and add their outer products. A non-integer $\nu$ is a different analytic continuation of the density and is not a count of vectors. Software that simulates a Wishart matrix must be told whether the scale argument is $\Sigma$ or $\Sigma^{-1}$. Passing the precision matrix in place of $\Sigma$ simulates the scatter for the inverse covariance.

## Worked example
Let $\nu=3$ and
$$
\Sigma=\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}.
$$
The mean matrix is $3\Sigma$, that is
$$
\mathrm{E} W=\begin{pmatrix} 6 & 3 \\ 3 & 6 \end{pmatrix}.
$$
The entry formula gives
$$
\mathrm{Var}(W_{11})=3(2\cdot 2+2\cdot 2)=24,
$$
$$
\mathrm{Cov}(W_{11},W_{22})=3(1\cdot 1+1\cdot 1)=6,
$$
$$
\mathrm{Var}(W_{12})=3(2\cdot 2+1\cdot 1)=15.
$$
The diagonal entries have mean $6$ and standard deviation $\sqrt{24}\approx 4.899$. A single realised matrix can easily sit several units away from $3\Sigma$. The covariance $6$ between $W_{11}$ and $W_{22}$ equals $2\nu\sigma_{12}^{2}$. The diagonal sums of squares move together because the coordinates inside each vector are correlated.{{cite:wishart1928}} (pp. 32–52)

**Your turn.** Take $\nu=5$ and $\Sigma=\mathrm{diag}(1,4)$. Find $\mathrm{E} W$ and $\mathrm{Var}(W_{22})$.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $\mathrm{diag}(5,20)$. The variance of the second diagonal entry is $5(4\cdot 4+4\cdot 4)=160$. The off-diagonal mean is $0$, and $\mathrm{Cov}(W_{11},W_{22})=5(0+0)=0$, so the two diagonal entries are uncorrelated when $\Sigma$ is diagonal.
:::

**Check yourself.** For $p=1$, $\Sigma=2$ and $\nu=4$, the mean and variance are $8$ and $32$. What changes if the four normal squares are replaced by four independent copies of a variable that has mean $0$ and variance $2$ but is not normal?

::: {.callout-tip collapse="true" title="Answer"}
The mean of the sum of squares remains $4\cdot 2=8$, by linearity. The variance need not be $32$, because that number uses $\mathrm{E} Z^4=3$. The sum is not chi-squared, and it is not a one-dimensional Wishart matrix, because the Wishart density asks for normal vectors.
:::

A corrected cross-product matrix from $n=6$ bivariate normal observations is assigned $\nu=5$. Why not $\nu=6$?

::: {.callout-tip collapse="true" title="Answer"}
The six outer products of the raw observations have mean $6\Sigma$ only after the population mean is removed. Centring at the sample mean spends one dimension and leaves $n-1=5$ degrees of freedom, with mean $5\Sigma$.
:::

## Common misconceptions
The Wishart law is the law of a scatter matrix, not the law of the observations. The observations are multivariate normal. Calling the data Wishart because a Gaussian graphical model was fitted confuses the sample with the population.

The scale $\Sigma$ in $W_p(\Sigma,\nu)$ is not always the covariance of one observation. In the construction used here it is: each vector has covariance $\Sigma$, and the mean of $W$ is $\nu\Sigma$. A parametrisation that puts $\Sigma^{-1}$ in the exponent and calls $\Sigma$ a precision will move the mean. The density displayed above has $\Sigma^{-1}$ in the trace and mean $\nu\Sigma$, so $\Sigma$ is the covariance scale.

Integer $\nu$ in the outer-product story is a count of vectors. The density formula can be read at non-integer $\nu$ large enough for the multivariate gamma function to be finite, and that extension is not a sum of $\nu$ outer products.

## Assumptions and limits — When the matrix is not Wishart
If the vectors are independent with mean zero and covariance $\Sigma$ but are not normal, the mean $\mathrm{E} W=\nu\Sigma$ survives and the Wishart density does not. Heavy-tailed coordinates inflate $\mathrm{Var}(U_i^2)$ above $2\sigma^4$, so the entry-variance formula, which is a Gaussian moment, fails with the density.

If $\nu<p$, a sum of $\nu$ outer products in $p$ dimensions is singular. The density displayed for positive-definite matrices does not apply. A sample covariance from fewer observations than variables is the practical version of that singularity.

Centring at a sample mean and then still using $\nu=n$ double-counts the observations. The mean of the corrected matrix is $(n-1)\Sigma$, not $n\Sigma$.

## Connections
The [multivariate normal distribution](multivariate-normal-distribution.qmd) supplies the vectors inside the outer products. A [chi-squared distribution](chi-squared-distribution.qmd) is the scalar Wishart law. The sample mean's normal law and its independence from the scatter are the two companions of $A\sim W_p(\Sigma,n-1)$ in a normal sample. Hotelling's $T^2$ is the test that spends those three facts together.

## History
The scalar reduction to a sum of normal squares is the one-dimensional case of the same outer-product construction. John Wishart edited Student's collected papers with E. S. Pearson, and Allan and Wishart's 1930 note treated a missing field plot.{{cite:dodge2008}} (pp. 235 and 350) The mean formula $\nu\Sigma$ used here follows from linearity of expectation applied to the outer products.{{cite:durrett2019}} (Thm. 1.6.1, p. 29)
