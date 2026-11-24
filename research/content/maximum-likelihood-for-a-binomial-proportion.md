## Motivating example
A quality check finds seven successful items in ten independent trials. The binomial likelihood asks which success probability makes that count most plausible, with the number of trials fixed. Its answer is the observed fraction, but the uncertainty is substantial: choosing the maximum does not mean the fitted probability is known exactly. Trials with different probabilities or dependence require a different sampling model.

## Intuition
For the observed count $x$, values of $p$ compete through $p^x(1-p)^{n-x}$. The binomial coefficient is constant in $p$ and can be omitted when maximizing. Keeping it is necessary when interpreting probabilities across possible counts. A likelihood ratio between two probabilities is meaningful even when the likelihood itself is not a probability distribution over $p$.{{cite:dodge2008}} (p. 334, Maximum Likelihood)

## Properties — Interior and endpoint solutions
For $n\ge1$ and $0<x<n$, the score equation of the log-likelihood yields $\widehat p=x/n$. The second derivative of the log-likelihood is $-x/p^2-(n-x)/(1-p)^2$, which is strictly negative throughout the open interval, so the stationary point is the unique global maximum. When $x=0$ the likelihood $(1-p)^n$ decreases on $[0,1]$ and is maximized at zero; when $x=n$ it increases and is maximized at one. If the parameter space excludes the endpoints, those two samples have a supremum but no attained maximum. Thus the parameter space belongs in the estimator's definition.{{cite:casella_berger2002}} (Ch. 7, §7.2.2, pp. 317–318)

For interior $p$, the score can be written $(X-np)/\{p(1-p)\}$. Its expectation is zero and its variance, the Fisher information, is $n/\{p(1-p)\}$ because $\operatorname{Var}(X)=np(1-p)$. The estimator has mean $p$ and variance $p(1-p)/n$. These finite-sample moments follow directly from the binomial moments. The usual asymptotic standard error replaces $p$ by $\widehat p$, and can be misleading near a boundary where it collapses.{{cite:grinstead_snell1997}} (§§5.1, 6.2, binomial distribution and variance)

## Worked example — Comparing candidate probabilities
For $n=10,x=7$, the maximizer is $0.7$. The likelihood ratio $L(0.7)/L(0.5)$ is
$$\frac{0.7^7 0.3^3}{0.5^{10}}=2.2769317.$$
Take a two-point prior that puts positive probability on $p=0.7$ and on $p=0.5$ and on no other value. The posterior mass at each of those points is proportional to the likelihood times the prior mass, so the posterior odds equal the likelihood ratio multiplied by the prior odds. A continuous prior would give probability zero to each exact value, and point odds would not be defined. When the prior odds are $1$, each point has prior probability $1/2$, and the posterior odds are $2.2769317\times 1=2.2769317$, which is $2.2769$ to four decimal places.{{cite:lehmann_casella1998}} (Ch. 4, §4.3, pp. 240–241) The plug-in standard error is $\sqrt{0.7(0.3)/10}=0.144914$. A fitted odds parameter $p/(1-p)$ is maximized at $7/3$, because this is a one-to-one increasing reparameterization of the interior probability.

For ten failures, $L(0.1)/L(0)=0.9^{10}=0.348678$. The value $p=0.1$ is therefore far from impossible under the observation. A zero plug-in standard error reflects the fitted model at an endpoint and does not mean that ten trials identify the population probability without error. The binomial variance $p(1-p)/n$ is zero at the fitted endpoint and positive at $p=0.1$.{{cite:grinstead_snell1997}} (§§5.1, 6.2, binomial distribution and variance)

**Your turn.** Observe $x=3$ in $n=12$ trials. Find the MLE, its plug-in standard error and its estimated odds.

::: {.callout-tip collapse="true" title="Answer"}
The MLE is $1/4$. The standard error is $\sqrt{(1/4)(3/4)/12}=1/8=0.125$. The estimated odds are $1/3$.
:::

## Statistical use — Repeated binomial groups
If independent counts $X_j\sim\operatorname{Bin}(n_j,p)$ share a common probability, their product likelihood has exponents $\sum_jx_j$ and $\sum_j(n_j-x_j)$. The pooled MLE is therefore $\sum_jx_j/\sum_jn_j$. Counts of $1$ out of $2$ and $8$ out of $10$ therefore have pooled estimate $9/12=0.75$. The unweighted average of $0.5$ and $0.8$ is $0.65$, and that average is not the maximum likelihood estimate in this example. Unequal sample sizes do not force the two averages apart in general: counts of $1$ out of $2$ and $5$ out of $10$ have pooled estimate $6/12=0.5$, the same number as the unweighted average of the two proportions. The pooling assumption is substantive: heterogeneity in success probabilities cannot be removed by this algebra.{{cite:grinstead_snell1997}} (§5.1, binomial trials)

## Assumptions and limits — Restrictions can move the maximum
Suppose external scientific knowledge restricts $p$ to $[0,u]$ for some $u<1$. The same binomial objective has constrained maximizer $\min(x/n,u)$. For an interior unconstrained maximum above $u$, the derivative is positive throughout the admissible interval up to $u$, so the best allowed value is its upper endpoint. For the seven-success count and $u=0.2$, the constrained estimate is $0.2$, even though the observed fraction is $0.7$. The score $(x-np)/\{p(1-p)\}$ at $p=0.2$ equals $(7-2)/(0.2\times 0.8)=31.25$, which is positive, so the likelihood is still rising at that endpoint. The result follows from optimizing over the actual parameter space; the maximum is taken only on the values the model allows, and the count itself has not been altered.{{cite:casella_berger2002}} (Ch. 7, §7.2.2, p. 318)

A binomial probability also requires a clear trial definition and a known number of trials. If the denominator itself is selected using outcomes, or trials have different success probabilities, the simple count likelihood need not describe the experiment. The estimator may still be a descriptive fraction, but its binomial variance and likelihood comparisons then require separate justification. Exact count probabilities remain discrete, whereas the fitted parameter ranges continuously. A smooth likelihood curve should therefore not be confused with an exact continuous sampling distribution for the estimator.{{cite:grinstead_snell1997}} (§5.1, Bernoulli trials and the binomial distribution)

## Common misconceptions
The maximiser is the value of $p$ that makes the observed count most likely. It is not a probability statement that $p$ equals $0.7$. The sampling variance of $X/n$ is $p(1-p)/n$, a function of the true probability. Substituting the fitted value produces a plug-in standard error, which describes that fitted point rather than the sampling variance.{{cite:grinstead_snell1997}} (§§5.1, 6.2, binomial distribution and variance)
