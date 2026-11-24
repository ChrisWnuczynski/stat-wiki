## Motivating example
A positive waiting-time model may have a rate parameter but no immediate regression structure. If its mean is $1/\lambda$, the observed average suggests the equation $\bar x=1/\lambda$. Solving gives $\widetilde\lambda=1/\bar x$. The method of moments generalises this idea by matching a sufficient number of distributional moments to their empirical counterparts. It starts with selected population features, rather than maximising the probability of the observed sample.{{cite:dodge2008}} (pp. 348–349, Method of Moments)

## Definition
For a $k$-parameter family, write $m_j=n^{-1}\sum_i X_i^j$ and $\mu_j'(\theta)=\mathbb E_\theta X^j$. A basic moment estimator solves $m_j=\mu_j'(\theta)$ for $j=1,\ldots,k$, using moments that exist and identify the parameters. The prime denotes a raw moment about zero; a central moment instead measures powers of $X-\mathbb EX$. Counting equations is necessary but not sufficient: different parameter values may share the chosen moments, or sample moments may lie outside the model's feasible moment region.{{cite:dodge2008}} (pp. 348–349)

Moment matching can also use other estimating functions. In the classical construction, however, the first $k$ raw moments give a concrete default and explain the name. The resulting estimate must lie in the parameter space. Algebraically solving the equations and then ignoring a negative variance, invalid probability or noninteger count parameter would change the problem. A constrained alternative needs an explicitly stated discrepancy criterion.{{cite:nist_method_of_moments}} (§1.3.6.5.1, Method of Moments)

## Properties — Consistency needs identification and continuity
Suppose the observations are iid and $\mathbb E|X|^k<\infty$. The law of large numbers makes the first $k$ sample moments converge to their population values. If the moment map has a continuous local inverse at the true parameter and the selected solution remains on that branch, applying that inverse gives consistency. This explains both the appeal and the limitation: existence of moments supplies convergence of features, while identification and a stable inverse turn convergence of features into convergence of parameters.{{cite:durrett2019}} (§2.4, strong law of large numbers)

Moment estimates need not be unbiased or have minimum variance. In a normal family, matching $\mathbb EX=\mu$ and $\mathbb EX^2=\mu^2+\sigma^2$ gives $\widetilde\mu=m_1$ and $\widetilde{\sigma^2}=m_2-m_1^2=n^{-1}\sum_i(X_i-\bar X)^2$. Its expectation is $(n-1)\sigma^2/n$. The equality with the normal MLE is a special agreement between two methods, not a universal property of moment estimates.{{cite:dodge2008}} (p. 349, normal example and limitations)

## Worked example — Fit a Gamma law by two moments
Use a Gamma model with shape $\alpha>0$ and rate $\beta>0$, so $\mathbb EX=\alpha/\beta$ and $\operatorname{Var}(X)=\alpha/\beta^2$. Let the observations be $1,2,3,6$. Their mean is $3$, their second raw moment is $50/4=12.5$, and their empirical central second moment is $12.5-9=3.5$. Solving $m_1=\alpha/\beta$ and $m_2-m_1^2=\alpha/\beta^2$ gives
$$\widetilde\alpha=\frac{m_1^2}{m_2-m_1^2}=\frac{18}{7},\qquad \widetilde\beta=\frac{m_1}{m_2-m_1^2}=\frac{6}{7}.$$
The fitted Gamma mean is exactly $3$ and its variance is exactly $3.5$, because those are the two quantities being matched. The unbiased sample variance $14/3$ is a different empirical feature and would produce different estimates.{{cite:nist_gamma_distribution}} (§1.3.6.6.11, density, common statistics and parameter estimation)

**Your turn.** Multiply every observation by two. What happens to the fitted Gamma shape and rate?

::: {.callout-tip collapse="true" title="Answer"}
The mean doubles and the central second moment multiplies by four. The fitted shape stays $18/7$ and the fitted rate halves to $3/7$. The shape is a scale-free ratio of those two moments, while the rate has the dimension of one over the observations and therefore halves.
:::

## Assumptions and limits — When the moment equations have no admissible root
For a binomial model with unknown count $K$ and success probability $p$, let $m=\bar x>0$ and $v=n^{-1}\sum_i(x_i-m)^2$. Matching $m=Kp$ and $v=Kp(1-p)$ gives $\widetilde p=1-v/m$ and $\widetilde K=m/\widetilde p$ when the denominator is positive. If $v>m$, the implied probability is negative; if $v=m$, the solution has no finite positive count; and even a positive solution may give a noninteger $K$. Sample variation can therefore prevent an exact feasible moment solution.{{cite:dodge2008}} (p. 349, parameter constraints and existence of solutions)

Heavy-tailed models supply another limitation. A Cauchy law has no finite first moment, so matching the sample average to a theoretical mean is undefined even though the sample average can be computed for each finite dataset. Robust location or quantile-based methods may still be available. The ability to calculate a finite-sample statistic does not establish existence of the population quantity it is supposed to estimate.{{cite:durrett2019}} (§2.4, strong law and integrability assumptions)

## Connections
The [gamma distribution](gamma-distribution.qmd) is the two-moment illustration above: its mean and variance determine a shape and a rate. The [binomial distribution](binomial-distribution.qmd) is the case in which the moment map can return a probability outside $[0,1]$, so that no exact root lies in the model. [Maximum likelihood](maximum-likelihood.qmd) maximises a different function and need not solve these moment equations.

## History
In 1894 Karl Pearson set out to dissect an asymmetrical frequency curve into normal components, on the view that the measurements might mix homogeneous groups.{{cite:pearson1894_mixture}} (pp. 71–72) For two normal components that share a mean, the second, fourth and sixth moments of the observed curve determine the component parameters.{{cite:pearson1894_mixture}} (pp. 92–93)
