## Motivating example — Transform an estimate and its uncertainty
A Poisson rate estimate may be useful mainly because it determines a probability of zero events. Transforming the rate estimate gives the desired probability estimate, but its standard error does not stay on the rate scale. The delta method locally replaces a differentiable transformation by a line. Linear variance propagation then explains why its derivative multiplies a standard error. Covariance terms also enter when several estimated inputs are transformed together.{{cite:nist_error_propagation2002}} (§3.1.3.3, linear variance propagation)

## Definition — A limiting law for a smooth transformation
Assume $\sqrt n(T_n-\theta)\Rightarrow N(0,\xi^2)$ and that $h$ is differentiable at $\theta$. The first-order transformed limit is normal with variance $\xi^2h'(\theta)^2$. If the derivative is zero, that first-order limit is degenerate at zero. A nondegenerate approximation then requires a suitable higher-order term and a possibly different scaling. Convergence in distribution specifies the law at continuity points of the limiting distribution function, rather than convergence of every possible moment.{{cite:siegrist_convergence_dist}} (“Distributions on R”, definition and continuous transformations)

## Properties — The remainder is small on the right scale
Differentiability gives $h(\theta+u)-h(\theta)=h'(\theta)u+u r(u)$ with $r(u)\to0$ as $u\to0$. The assumed root-$n$ limit makes $\sqrt n(T_n-\theta)$ bounded in probability, and also gives $T_n\to\theta$ in probability. Hence $r(T_n-\theta)\to0$ in probability. Their product tends to zero in probability: choose a large fixed bound for the first factor and then use convergence of the second. The leading term therefore supplies the transformed limit. This argument identifies the differentiability and convergence conditions that justify the linear approximation.{{cite:siegrist_convergence_dist}} (“Distributions on R”, “Convergence in Probability”)

Under a multivariate root-$n$ normal limit with covariance matrix $\Sigma$, the first-order scalar limiting variance becomes $\nabla h(\theta)^\top\Sigma\nabla h(\theta)$. Each cross covariance matters. This is the variance of the local linear form; ignoring off-diagonal terms assumes away covariance rather than removing it by transformation.{{cite:nist_error_propagation2002}} (§3.1.3.3)

## Worked example — A Poisson zero-event probability
Suppose the rate estimate is $\widehat\lambda=2$ based on $n=100$ independent Poisson observations. For $h(\lambda)=e^{-\lambda}$, the derivative is $-e^{-\lambda}$ and the sample mean has variance $\lambda/n$. Plugging the estimate into the delta standard error gives
$$e^{-2}\sqrt{2/100}\approx0.019139.$$
The probability estimate is $e^{-2}\approx0.135335$. The derivative's sign determines the direction of the change, while its square determines the variance. A large rate corresponds to a smaller zero-event probability.

**Your turn.** At the same rate estimate, increase the sample size to four hundred. What happens to that standard error?

::: {.callout-tip collapse="true" title="Answer"}
It is halved, becoming approximately $0.009570$, because the sample size appears under a square root in the denominator.
:::

## Interpretation — A zero derivative requires another calculation
Consider iid $N(0,\sigma^2)$ observations and $h(\mu)=\mu^2$. At zero, $h'(0)=0$, so the first-order normal limit contains no variation. In fact $\sqrt n\bar X/\sigma$ is exactly standard normal, and $n\bar X^2/\sigma^2$ is exactly chi-squared with one degree of freedom. That establishes the $n$ scale for this example. A constant transformation, by contrast, has no nonzero higher-order term at all, so a zero first derivative alone does not guarantee a particular alternative rate.{{cite:siegrist2022_normals}} (§6.8, sample mean and chi-square construction)

## Assumptions and limits — Local normality does not settle every tail
A smooth local approximation can perform poorly near a support boundary, under a strongly curved transformation, or in small samples. A consistent plug-in standard error requires continuity of its estimated ingredients. Convergence in law of the scaled error alone does not prove convergence of its variance; that additionally needs moment control. Keep the claimed limiting normal variance separate from an exact finite-sample variance formula.{{cite:siegrist_convergence_dist}} (“Distributions on R”, “Definition”); {{cite:nist_error_propagation2002}} (§3.1.3.3)

A confidence interval gives another way to separate a transformation from its linear approximation. If an interval $[L,U]$ covers a parameter and $h$ is strictly increasing on that interval and the parameter space, its transformed interval is $[h(L),h(U)]$. If $h$ is decreasing, the endpoints reverse. This transformation preserves the coverage event exactly; it need not produce a symmetric interval around $h(T_n)$. The delta interval instead approximates the transformed sampling law by a normal law and usually reports a symmetric error bar on that scale. Strong curvature can therefore produce visibly different endpoints even when both calculations start from the same estimate and uncertainty. The variance-propagation formula describes the local calculation, rather than choosing between interval constructions.{{cite:nist_error_propagation2002}} (§3.1.3.3)
