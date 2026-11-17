## Motivating example
A sample of bivariate measurements gives both a mean vector and a covariance estimate. Exact multivariate inference needs their joint behaviour, rather than two unrelated marginal approximations. Normal sampling supplies a particularly useful separation: the mean vector is independent of the centred cross-products that estimate covariance. The scalar case is the familiar independence of a normal sample mean and sample variance.

## Statement
Let $X_1,\ldots,X_n$ be independent $N_p(\mu,\Sigma)$ vectors, with $n\ge2$ and positive-definite $\Sigma$. Define $\bar X=n^{-1}\sum_iX_i$ and
$$A=\sum_i(X_i-\bar X)(X_i-\bar X)^\top.$$
Then $\bar X\sim N_p(\mu,\Sigma/n)$ and $A\sim W_p(\Sigma,n-1)$, independently. The convention $W_p(\Sigma,\nu)$ denotes the distribution of $\sum_{j=1}^\nu Z_jZ_j^\top$ for independent $Z_j\sim N_p(0,\Sigma)$. The construction, rather than the ordering of its two arguments in a particular software package, fixes the scale and degrees of freedom.{{cite:nist_multivariate_normal2002}} (§6.5.4.2, vector-normal model)

The corrected sample covariance is $S=A/(n-1)$ and satisfies $E(S)=\Sigma$. The uncorrected version $A/n$ is a different estimator and has expectation $(n-1)\Sigma/n$. Since the centred observation vectors sum to zero, $A$ has rank at most $\min(p,n-1)$. For an invertible sample covariance under a nonsingular normal population, the sample must therefore have $n>p$.

## Proof
Choose an orthogonal $n\times n$ matrix $Q$ whose first row is $n^{-1/2}\mathbf1^\top$. Transform the observation rows after subtracting $\mu$. For the transformed row vectors $Z_j$, the cross-covariance of rows $j,k$ is $\sum_iQ_{ji}Q_{ki}\Sigma=\delta_{jk}\Sigma$. Their joint distribution is normal, so the transformed rows are independent and each has covariance $\Sigma$. The first row is $Z_1=\sqrt n(\bar X-\mu)$.

Orthogonal preservation of cross-products gives $\sum_i(X_i-\mu)(X_i-\mu)^\top=\sum_jZ_jZ_j^\top$. Expanding the left side about $\bar X$ and cancelling the mixed terms yields $A=\sum_{j=2}^nZ_jZ_j^\top$. It is therefore the stipulated Wishart sum of $n-1$ independent centred normal outer products and is independent of $Z_1$. This proves all three joint sampling claims. The mechanism extends the scalar mean–variance separation, while making the matrix-valued scatter explicit.

## Key results — Mean and scatter measure different uncertainty
Taking expectations of the outer-product construction gives $E(A)=(n-1)\Sigma$. The covariance of $\bar X$ is $\Sigma/n$. These two moment identities also hold for iid observations with finite covariance without normality; expansion of centred cross-products proves the first and independence of observations proves the second. What normality adds is the exact Gaussian/Wishart shape and their independence, rather than the elementary unbiasedness identities.{{cite:dodge2008}} (pp. 559–560, variance–covariance matrix)

## Worked example
### A bivariate scale calculation
Let $n=10$ and $\Sigma=\begin{pmatrix}4&1\\1&9\end{pmatrix}$. Its determinant is $35.000>0$, so it is positive definite. The sample-mean covariance is $\begin{pmatrix}0.4&0.1\\0.1&0.9\end{pmatrix}$, while $E(A)=\begin{pmatrix}36&9\\9&81\end{pmatrix}$. The scatter has nine Wishart degrees of freedom, not ten.

For contrast vector $c=(1,-1)^\top$, $\operatorname{Var}(c^\top\bar X)=c^\top\Sigma c/10=1.100$. The expected sample variance of that contrast is $c^\top\Sigma c=11.000$. These are uncertainties of a sample mean and individual-vector contrasts respectively, and should not be interchanged.

**Your turn.** Increase the sample size to 20 while the population covariance stays fixed. Give the new mean-contrast variance and the expected scatter matrix.

::: {.callout-tip collapse="true" title="Answer"}
The mean-contrast variance becomes $11/20=0.550$. The scatter expectation is $19\Sigma=\begin{pmatrix}76&19\\19&171\end{pmatrix}$, while the expected corrected sample covariance remains $\Sigma$.
:::

## Statistical use — Exact multivariate tests spend the joint law
Hotelling's statistic compares a mean contrast with an estimated covariance matrix. Under the normal null and $n>p$, $T^2=n(\bar X-\mu_0)^\top S^{-1}(\bar X-\mu_0)$ satisfies $(n-p)T^2/[p(n-1)]\sim F_{p,n-p}$. Its exact calibration depends on the normal mean and independent covariance estimate. A central limit theorem for a non-normal population does not by itself give an exact finite-sample Wishart law for the scatter.{{cite:nist_hotelling2002}} (§6.5.4.3, distribution of T squared)


## Generalizations — Derive the Hotelling calibration from normal projections
For the stated null, put $Z=\sqrt n\Sigma^{-1/2}(\bar X-\mu_0)$ and $W=\Sigma^{-1/2}A\Sigma^{-1/2}$, with $\nu=n-1$. Then $Z\sim N_p(0,I)$, $W\sim W_p(I,\nu)$ and they are independent. Consequently $T^2=\nu Z^\top W^{-1}Z$. Orthogonal invariance of $W$ permits rotating the direction of $Z$ to the first coordinate, while its squared length remains an independent $\chi_p^2$ variable.{{cite:nist_hotelling2002}} (§6.5.4.3, exact calibration)

Write the Wishart construction as $W=B^\top B$, with $\nu$ independent standard normal rows. Partition its first column as $b_1$ and the other columns as $B_2$. The reciprocal of $(W^{-1})_{11}$ is the Schur complement $b_1^\top(I-P_{B_2})b_1$. Conditional on $B_2$, the independent standard normal $b_1$ is projected onto a subspace of dimension $\nu-p+1$. Thus this reciprocal has a $\chi^2_{\nu-p+1}$ law that is independent of the radius of $Z$. The normal-over-chi-square calculation therefore gives $Z^\top W^{-1}Z\sim[p/(\nu-p+1)]F_{p,\nu-p+1}$. Substituting $\nu=n-1$ yields the displayed calibration of $T^2$. The assumption $n>p$ ensures that these projection dimensions and inverses are valid.

## Intuition — One orthogonal transformation separates the mean
The first row of the orthogonal matrix $Q$ is the normalised constant vector, so the first transformed row is $\sqrt n(\bar X-\mu)$. Every later row is orthogonal to the constant vector and therefore has mean zero. Orthogonal rows of a spherical Gaussian array are independent, and each has covariance $\Sigma$. The scatter $A$ is the sum of the outer products of those later rows, a Wishart matrix on $n-1$ degrees of freedom, independent of $\bar X$. In the bivariate worked example, $n=10$ leaves $9$ degrees of freedom, $E(A)=9\Sigma=\begin{pmatrix}36&9\\9&81\end{pmatrix}$, and the mean vector has covariance $\Sigma/10$. Raising $n$ to $20$ changes the mean-contrast variance of $X_1-X_2$ from $1.100$ to $0.550$ and changes $E(A)$ to $19\Sigma=\begin{pmatrix}76&19\\19&171\end{pmatrix}$, while $E(S)=\Sigma$ stays fixed because the corrected covariance divides by $n-1$.

The scalar case is the same split with $p=1$. The sample mean and the sum of squared deviations are independent, the sum of squares is $\sigma^2\chi^2_{n-1}$, and the corrected variance is unbiased. The matrix $A$ is that sum of squares promoted to outer products. Unbiasedness $E(A)=(n-1)\Sigma$ holds for iid samples with finite covariance even when the coordinates are non-normal. Normality adds the Wishart shape and the independence from $\bar X$.{{cite:dodge2008}} (pp. 559–560, variance–covariance matrix)

## Common misconceptions
The divisor in $S=A/(n-1)$ matches $E(S)=\Sigma$. The divisor $n$ produces $A/n$ with expectation $(n-1)\Sigma/n$. For $n=10$ that factor is $0.9$, so a covariance estimated with divisor $10$ has expectation $0.9\Sigma$. Hotelling's statistic is usually written with the corrected $S$, and the $F$ calibration $(n-p)T^2/[p(n-1)]$ has the $n-1$ in the denominator for that reason. Swapping the divisor changes the numerical statistic and the reference degrees of freedom together.

The covariance of $\bar X$ is $\Sigma/n$, an uncertainty about the mean. The population covariance $\Sigma$ is an uncertainty about a single draw. For the contrast $c=(1,-1)$ these are $1.100$ and $11.000$ in the worked example. A prediction interval for a new vector uses both, adding $\Sigma$ to $\Sigma/n$ inside the quadratic form. An interval for the mean uses $\Sigma/n$ alone.{{cite:nist_hotelling2002}} (§6.5.4.3, distribution of T squared)
