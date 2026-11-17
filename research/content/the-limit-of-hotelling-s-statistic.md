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
A singular population covariance has fewer variable directions than the stated dimension, so the inverse and a $p$-degree calibration are replaced by a reduction to the positive-eigenvalue subspace. Heavy tails without a finite second-moment matrix fall outside the hypotheses of the vector central limit theorem used above. Correlated observations are handled by inserting a consistent estimator of the covariance of $\sqrt n(\bar X-\mu_0)$, which need not be the usual matrix $S_n$ built from independent copies. Each of these changes replaces an ingredient of the quadratic form before a critical value is read.{{cite:durrett2019}} (§3.10, pp. 200–201)

## Definition — Two reference distributions for one quadratic form
For a fixed dimension $p$ and a positive definite covariance, the large-sample null statement is $T_n^2\Rightarrow\chi_p^2$ when $S_n$ is a consistent estimator of $\Sigma$. Under iid normal sampling with $n>p$ there is also an exact law,
$$
\frac{(n-p)}{p(n-1)}T^2\sim F_{p,n-p},
$$
where $T^2=n(\bar X-\mu_0)^\top S^{-1}(\bar X-\mu_0)$ and $S$ is the corrected sample covariance with divisor $n-1$. The chi-squared statement is the limit of this $F$ law as $n\to\infty$ with $p$ fixed, and it is also the limit obtained from the central limit theorem plus Slutsky's lemma when normality is dropped and second moments exist. The exact $F$ law uses normality of the observations, independence of the sample mean and the scatter matrix, and invertibility of $S$.{{cite:nist_hotelling2002}} (§6.5.4.3, displayed $F$ law)

The numerical gap between the two references is visible at a fixed statistic. For $p=2$ the $95\%$ chi-squared quantile is $5.991465$. The value $T^2=6$ therefore sits just beyond the limiting $5\%$ cutoff, with upper tail $e^{-3}=0.04979$. The exact normal-sample transform at $n=20$ is $F=(18/38)\times6=2.8421$, and the $95\%$ quantile of $F_{2,18}$ is $3.554557$. Because $2.8421<3.554557$, the exact test at level $5\%$ accepts the null. Its upper tail is $0.08459$. At $n=200$ the exact tail falls to $0.05282$, closer to $0.04979$, as the covariance estimate concentrates.{{cite:nist_hotelling2002}} (§6.5.4.3, one-sample $F$ transformation)

## Intuition — Replace the estimated metric by the true metric
The statistic $T_n^2$ is a squared length. The matrix $S_n^{-1}$ supplies the metric. Consistency says that this metric converges to $\Sigma^{-1}$. The vector central limit theorem says that $\sqrt n(\bar X-\mu_0)$ is approximately $N_p(0,\Sigma)$ in the large-sample sense of convergence in distribution. A continuous function of a convergent sequence and a sequence that settles at a constant settles at the function of the limit. Matrix inversion is continuous at $\Sigma$, which is why positive definiteness of the limit is part of the argument. The squared length in the limiting metric is the sum of squares of $p$ independent standard normals.

Independence of $\bar X$ and $S_n$ is not required for that sentence. Convergence in probability of $S_n$ is a statement about the joint behaviour with $\bar X$ only through Slutsky's lemma: a factor that converges in probability to a constant can be multiplied by a factor that converges in distribution. Finite-sample independence is the stronger normal-theory fact used to name the $F$ law for every $n>p$.

## Statistical use — Match the critical value to the sampling model
A normal sample with a small $n-p$ leaves a noisy $S$. The exact $F$ critical value accounts for that noise by widening the acceptance region relative to the chi-squared cutoff. With $p=2$ and $n=20$, the $5\%$ $F$ cutoff on the $T^2$ scale is $3.554557\times(2\times19)/18=7.504065$. The chi-squared cutoff on the same scale is $5.991465$. The statistic $T^2=6$ falls between them, which is why the two procedures disagree at this sample size. As $n$ grows with $p$ fixed, $(n-p)/(n-1)\to1$ and $p F_{p,n-p}$ converges in distribution to $\chi_p^2$, so the two cutoffs approach each other.{{cite:nist_hotelling2002}} (§6.5.4.3)

For a single coordinate the same arithmetic specialises to the square of a one-sample $t$ statistic. Then $T^2=t^2$, the exact law is $F_{1,n-1}$, and the limit is $\chi_1^2$. Reporting a chi-squared tail for a one-coordinate statistic is the large-sample reading of a Student tail. The degrees of freedom $n-1$ remain in the exact comparison.

## Common misconceptions
The limit does not assign a chi-squared distribution to $T^2$ for every normal sample size. At $n=20$ and $p=2$ the exact tail at $T^2=6$ is $0.08459$ and the chi-squared tail is $0.04979$. Both numbers are correct for their reference distributions. The modelling choice is which reference the sampling design supports.

A consistent covariance estimator can be dependent on the sample mean and still deliver the chi-squared limit. The proof tracks convergence in probability of the matrix factor and convergence in distribution of the normalised mean. Gaussian independence is a convenient sufficient condition for the exact finite-sample law, and the limit argument uses the weaker convergence.{{cite:durrett2019}} (§3.10, pp. 196–201, weak convergence and Gaussian vector limit)

## Connections
The vector central limit theorem is the source of the normal approximation to $\sqrt n(\bar X-\mu_0)$. The Wishart law of the centred scatter, and its independence from the sample mean, are the normal-sample facts that upgrade the approximation to an exact $F$ ratio. Whitening by $\Sigma^{-1/2}$ converts the limiting normal vector to standard normal coordinates so that the squared length has a parameter-free chi-squared law. The same whitening, applied to the Wishart matrix, is the first step in the exact derivation that reduces $T^2$ to a multiple of an $F$ variable.{{cite:durrett2019}} (§3.10, pp. 200–201, vector central limit theorem){{cite:nist_hotelling2002}} (§6.5.4.3, exact calibration)
