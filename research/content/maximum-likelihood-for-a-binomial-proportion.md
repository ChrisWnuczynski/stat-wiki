## Motivating example
A quality check finds seven successful items in ten independent trials. The binomial likelihood asks which success probability makes that count most plausible, with the number of trials fixed. Its answer is the observed fraction, but the uncertainty is substantial: choosing the maximum does not mean the fitted probability is known exactly. Trials with different probabilities or dependence require a different sampling model.

## Intuition — The likelihood is a function of the unknown probability
For the observed count $x$, values of $p$ compete through $p^x(1-p)^{n-x}$. The binomial coefficient is constant in $p$ and can be omitted when maximizing. Keeping it is necessary when interpreting probabilities across possible counts. A likelihood ratio between two probabilities is meaningful even when the likelihood itself is not a probability distribution over $p$.{{cite:dodge2008}} (p. 334, Maximum Likelihood)

## Properties — Interior and endpoint solutions
For $n\ge1$ and $0<x<n$, solving the score equation yields $\widehat p=x/n$. Its second derivative is strictly negative throughout the open interval, so the stationary point is the unique global maximum. When $x=0$ the likelihood $(1-p)^n$ decreases on $[0,1]$ and is maximized at zero; when $x=n$ it increases and is maximized at one. If the parameter space excludes the endpoints, those two samples have a supremum but no attained maximum. Thus the parameter space belongs in the estimator's definition.

For interior $p$, the score can be written $(X-np)/\{p(1-p)\}$. Its expectation is zero and its variance, the Fisher information, is $n/\{p(1-p)\}$ because $\operatorname{Var}(X)=np(1-p)$. The estimator has mean $p$ and variance $p(1-p)/n$. These finite-sample moments follow directly from the binomial moments. The usual asymptotic standard error replaces $p$ by $\widehat p$, and can be misleading near a boundary where it collapses.{{cite:grinstead_snell1997}} (§§5.1, 6.2, binomial distribution and variance)

## Worked example — Comparing candidate probabilities
For $n=10,x=7$, the maximizer is $0.7$. The likelihood ratio $L(0.7)/L(0.5)$ is
$$\frac{0.7^7 0.3^3}{0.5^{10}}=2.2769317.$$
The plug-in standard error is $\sqrt{0.7(0.3)/10}=0.144914$. A fitted odds parameter $p/(1-p)$ is maximized at $7/3$, because this is a one-to-one increasing reparameterization of the interior probability. The likelihood comparison gives relative support among candidate values, rather than posterior odds without a prior.

For ten failures, $L(0.1)/L(0)=0.9^{10}=0.348678$. The value $p=0.1$ is therefore far from impossible under the observation. A zero plug-in standard error reflects the fitted model at an endpoint and does not mean that ten trials identify the population probability without error. The binomial variance $p(1-p)/n$ is zero at the fitted endpoint and positive at $p=0.1$.{{cite:grinstead_snell1997}} (§§5.1, 6.2, binomial distribution and variance)

**Your turn.** Observe $x=3$ in $n=12$ trials. Find the MLE, its plug-in standard error and its estimated odds.

::: {.callout-tip collapse="true" title="Answer"}
The MLE is $1/4$. The standard error is $\sqrt{(1/4)(3/4)/12}=1/8=0.125$. The estimated odds are $1/3$.
:::

## Statistical use — Repeated binomial groups
If independent counts $X_j\sim\operatorname{Bin}(n_j,p)$ share a common probability, their product likelihood has exponents $\sum_jx_j$ and $\sum_j(n_j-x_j)$. The pooled MLE is therefore $\sum_jx_j/\sum_jn_j$. Averaging group proportions without weighting gives a different result when group sizes differ. The pooling assumption is substantive: heterogeneity in success probabilities cannot be removed by this algebra.{{cite:grinstead_snell1997}} (§5.1, binomial trials)

## Assumptions and limits — Restrictions can move the maximum
Suppose external scientific knowledge restricts $p$ to $[0,u]$ for some $u<1$. The same binomial objective has constrained maximizer $\min(x/n,u)$. For an interior unconstrained maximum above $u$, the derivative is positive throughout the admissible interval up to $u$, so the best allowed value is its upper endpoint. For the seven-success count and $u=0.2$, the constrained estimate is $0.2$, even though the observed fraction is $0.7$. The result follows from optimizing over the actual parameter space; it does not mean the count has been altered.

A binomial probability also requires a clear trial definition and a known number of trials. If the denominator itself is selected using outcomes, or trials have different success probabilities, the simple count likelihood need not describe the experiment. The estimator may still be a descriptive fraction, but its binomial variance and likelihood comparisons then require separate justification. Exact count probabilities remain discrete, whereas the fitted parameter ranges continuously. A smooth likelihood curve should therefore not be confused with an exact continuous sampling distribution for the estimator.{{cite:grinstead_snell1997}} (§5.1, Bernoulli trials and the binomial distribution)

## Interpretation — Pooling, odds, and a restricted interval
Independent groups that share one $p$ contribute a single binomial likelihood whose success count is the sum of the group counts and whose trial count is the sum of the group sizes. Counts $1$ out of $2$ and $8$ out of $10$ therefore have pooled maximum likelihood estimate $9/12=0.75$. The unweighted average of $0.5$ and $0.8$ is $0.65$, and that average does not maximise the product likelihood unless the groups happen to be the same size. The pooling step is justified when the groups really do share $p$. A mixture of two probabilities can produce the same two counts and a different target.{{cite:grinstead_snell1997}} (§5.1, binomial trials)

On the interior, the odds $\omega=p/(1-p)$ are a one-to-one increasing function of $p$. The likelihood, as a function of $\omega$, is maximised at the odds of the maximising $p$. For $7$ successes in $10$ trials that odds estimate is $7/3$. The invariance is algebraic. It does not turn the likelihood ratio $L(0.7)/L(0.5)=2.2769317$ into a posterior odds. A posterior odds statement divides that likelihood ratio by the prior odds. Leaving the prior out leaves a likelihood ratio.{{cite:dodge2008}} (p. 334, Maximum Likelihood)

If the parameter is restricted to $[0,u]$ with $u=0.2$, the seven-success likelihood is increasing on the whole restriction, and the constrained maximum is $0.2$. The unrestricted fraction $0.7$ is still the count divided by the number of trials. The estimate changed because the parameter space changed. Reporting $0.2$ without the restriction presents a boundary solution as if it had been the interior critical point. The score $(x-np)/\{p(1-p)\}$ at $p=0.2$ for $x=7$, $n=10$ equals $(7-2)/(0.2\times0.8)=31.25$, which is positive, confirming that the likelihood is still rising at the boundary.

## Common misconceptions
The maximiser is the value of $p$ that makes the observed count most likely. It is not a probability statement that $p$ equals $0.7$. For the interior binomial the estimator $X/n$ is unbiased and has variance $p(1-p)/n$, so at $p=0.7$ and $n=10$ the sampling standard deviation is $\sqrt{0.21/10}\approx0.144914$, the same number as the plug-in standard error when the estimate happens to be $0.7$. At an estimate of $0$ or $1$ the plug-in formula returns $0$ while the sampling variance at a nearby interior $p$ does not. The plug-in standard error is a function of the fitted point. The sampling variance is a function of the true $p$.{{cite:grinstead_snell1997}} (§§5.1, 6.2, binomial distribution and variance)

An open parameter space $(0,1)$ has no maximiser when $x=0$. The likelihood $(1-p)^n$ increases as $p$ decreases, and the supremum is $1$, approached as $p\downarrow0$, but $0$ is not in the space. Closing the space to $[0,1]$ puts the maximiser at $0$. Existence is a property of the likelihood and the set over which it is maximised. A numerical optimiser that stops at a tiny positive $p$ has found a feasible point near the supremum, not a critical point of an interior score equation. The score equation $(x-np)/\{p(1-p)\}=0$ has the solution $x/n$ only when that solution lies in the open interval where the derivative was formed.{{cite:dodge2008}} (p. 334, Maximum Likelihood)
