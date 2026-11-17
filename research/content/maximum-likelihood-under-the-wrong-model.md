## Motivating example
A count analyst uses a Poisson likelihood because it is easy to fit, even though observed counts vary much more than their mean. The fitted mean can still estimate a useful population quantity, but a Poisson standard error can be too small. Misspecification separates three issues: what parameter the fitting rule targets, whether the rule converges to that target, and how uncertain the estimate is.{{cite:goodfellow_bengio_courville2016}} (§5.5, expected log-likelihood and KL divergence){{cite:firth1993_quasi}} (§§1–2, quasi-likelihood equations and robust variance)

## Intuition — The population objective defines a projection
For iid data from $f_0$, define $M(\theta)=E_0\log f(X;\theta)$ when the expectation is finite. If $E_0\log f_0(X)$ is finite too, then
$$D_{KL}(f_0\|f_\theta)=E_0\log f_0(X)-M(\theta).$$
The first term is constant in $\theta$, so maximizing $M$ minimizes this divergence. The resulting $\theta^\star$ is often called the pseudo-true parameter. It depends on the chosen family and discrepancy direction. A family can match a feature such as a mean while failing badly on tail probabilities.{{cite:goodfellow_bengio_courville2016}} (§5.5, maximum likelihood as KL minimization)

Pointwise convergence of average log-likelihood at each fixed parameter is insufficient by itself to prove convergence of its maximizer. One sufficient framework is a compact parameter space, a continuous population objective with a unique maximizer, and uniform convergence $\sup_\theta|n^{-1}\ell_n(\theta)-M(\theta)|\to0$ in probability. For any neighborhood of the maximum, compactness and uniqueness give a positive objective gap outside it; uniform error less than half that gap forces the sample maximizer inside the neighborhood. This proves consistency under those stated conditions.

## Properties — The two matrices in the sandwich
Let $s(X,\theta)=\partial\log f(X;\theta)/\partial\theta$ and define at $\theta^\star$
$$A=-E_0\{\partial s/\partial\theta^\top\},\qquad B=E_0(ss^\top).$$
Assume the score has mean zero there, finite covariance, nonsingular $A$, and a valid local Taylor expansion with a consistent derivative average. Expanding the score equation gives
$$\sqrt n(\widehat\theta-\theta^\star)=A^{-1}\frac1{\sqrt n}\sum_i s(X_i,\theta^\star)+o_p(1).$$
The multivariate central limit theorem then gives asymptotic covariance $A^{-1}BA^{-\top}/n$. Equality of $A$ and $B$ is an extra model identity, rather than a consequence of fitting an objective. Misspecification can inflate, reduce or leave unchanged the variance relative to a model calculation.{{cite:durrett2019}} (§3.9, multivariate central limit theorem){{cite:firth1993_quasi}} (§1, score identities and second-moment assumptions)

## Worked example — A correct mean with an incorrect Poisson variance
Fit $Y_i\sim\operatorname{Pois}(\lambda)$ to iid nonnegative integer observations with true mean $m>0$ and variance $v<\infty$. The score is $Y_i/\lambda-1$, so its sum vanishes at $\widehat\lambda=\overline Y$. The population objective is maximized at $\lambda^\star=m$. Here $A=1/m$ and $B=v/m^2$, giving sandwich variance $v/n$. The Poisson-model variance would be $m/n$. Thus the point estimate is consistent for the mean even when the Poisson variance relation is false.{{cite:firth1993_quasi}} (§1, independent Poisson variance function){{cite:durrett2019}} (§3.4.1, iid central limit theorem)

If the true mean is four and variance twelve, $n=100$ gives actual standard deviation $\sqrt{12/100}\approx0.346410$, compared with the model standard error $\sqrt{4/100}=0.2$. The ratio is $\sqrt3$. If the variance is two instead, the actual standard deviation is $\sqrt{2/100}\approx0.141421$, smaller than the Poisson value. Both directions are possible.

**Your turn.** A working Poisson fit has sample mean $9$, sample variance $36$ and $n=400$. Compare its model and robust mean standard errors.

::: {.callout-tip collapse="true" title="Answer"}
The model standard error is $\sqrt{9/400}=0.15$. The sample-variance estimate gives $\sqrt{36/400}=0.3$, twice as large.
:::

## Assumptions and limits
A sandwich standard error addresses variability around the fitted population target; it does not make that target the scientific truth. Dependence requires long-run score covariance rather than the iid matrix $B$. Infinite variances, unidentified parameters, boundary maxima and failed optimization can invalidate the expansion. Robust mean inference also does not imply that every likelihood ratio statistic keeps its reference distribution. A procedure's efficiency within a correct model and its reliability outside that model are separate properties.{{cite:goodfellow_bengio_courville2016}} (§5.5.2, conditions for maximum likelihood properties){{cite:durrett2019}} (§3.4, moment conditions)
