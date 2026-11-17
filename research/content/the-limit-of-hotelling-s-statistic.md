## Lead context
The chi-squared calibration concerns fixed dimension and a consistently estimated covariance. Under multivariate normal sampling an exact finite-sample calibration based on an F distribution is available as well.{{cite:nist_hotelling2002}} (§6.5.4.3)

## Motivating example
A laboratory compares a two-component mean with a target. A measured quadratic distance $T^2=6$ lies just beyond the $5\%$ chi-squared cutoff, but a sample of twenty observations leaves substantial uncertainty in the covariance estimate. The limiting and exact normal-theory tests need not make the same decision.{{cite:nist_hotelling2002}} (§6.5.4.3, one-sample $F$ transformation)

## Properties — Whitening before squaring
Let $X_i$ be iid vectors with mean $\mu_0$, finite covariance $\Sigma\succ0$, and fixed dimension $p$. The vector central limit theorem gives $Z_n=\sqrt n\,\Sigma^{-1/2}(\bar X-\mu_0)\Rightarrow N_p(0,I_p)$.{{cite:durrett2019}} (§3.10, pp. 200–201, vector central limit theorem) Write
$$
T_n^2=Z_n^\top\{\Sigma^{1/2}S_n^{-1}\Sigma^{1/2}\}Z_n.
$$
If $S_n\to\Sigma$ in probability, continuity of matrix inversion at a positive definite matrix makes the matrix in braces converge to $I_p$. Tightness of $Z_n$ makes the difference between this form and $Z_n^\top Z_n$ vanish in probability. The continuous mapping theorem then gives the sum of squares of $p$ independent standard normals, namely $\chi_p^2$.{{cite:durrett2019}} (§3.10, pp. 196–201, weak convergence and Gaussian vector limit)

The proof needs neither independence between $\bar X$ and $S_n$ nor Gaussian observations. Those stronger normal-sample properties underlie the exact $F$ law. Dimension must stay fixed: increasing $p$ changes the limiting problem and may make $S_n$ singular.{{cite:nist_hotelling2002}} (§6.5.4.3, normality and sample-size conditions)

## Worked example
With $p=2$ and $T^2=6$, the limiting upper-tail probability is $P(\chi_2^2\ge6)=e^{-3}=0.04979$. For $n=20$, the exact normal-sample transform is $F=18\cdot6/38=2.8421$, whose $F_{2,18}$ tail is $0.08459$. With $n=200$, the corresponding exact tail is $0.05282$. Thus the limiting test rejects at $5\%$ while both finite-sample comparisons do not. The difference narrows as covariance estimation becomes more precise.{{cite:nist_hotelling2002}} (§6.5.4.3, displayed $F$ law)

**Your turn.** For one component, express $T^2$ in terms of the ordinary one-sample $t$. What is its limiting law?

::: {.callout-tip collapse="true" title="Answer"}
$T^2=n(\bar X-\mu_0)^2/s^2=t^2$. Its limit is $\chi_1^2$, the square of a standard normal variable. Under normal sampling its exact law is $F_{1,n-1}$.
:::

## Assumptions and limits
A singular population covariance has fewer variable directions than the stated dimension, so ordinary inversion and a $p$-degree calibration cannot be used as written. Heavy tails without finite second moments can invalidate the Gaussian mean limit. Correlated observations require a consistent covariance for the scaled sample mean, rather than automatically using the iid sample covariance. These are failures of the ingredients in the quadratic-form argument, not corrections supplied by a larger critical value.{{cite:durrett2019}} (§3.10, pp. 200–201)
