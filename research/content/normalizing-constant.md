## Lead context
A normalizing constant is the factor that turns a nonnegative function into a probability density or a probability mass function. In a Bayesian calculation it is often the marginal probability of the observed data, the denominator of Bayes' rule.{{cite:gelman_bda2013}} (pp. 7, 42)

## Motivating example
After a binomial sample, the product of a uniform prior and the likelihood is a power of the unknown probability times a power of its complement. That product shows where the posterior is high and where it is low, and it does not integrate to one. Multiplying by one fixed number makes the area equal to one. The number is determined by the data and the prior; it is not a further modelling choice.{{cite:gelman_bda2013}} (pp. 30–31, 42)

## Intuition
Relative heights are fixed by the unnormalised function. The constant lifts or lowers the whole graph until the total probability is one. Any question that depends only on ratios at different parameter values can ignore the constant, because it cancels. Any question that asks for a probability, a density height, or the marginal probability of the data has to put the constant back.{{cite:gelman_bda2013}} (pp. 7, 30)

## Definition
A nonnegative function \(f\) on the line determines a distribution function by integration only when its integral over the line equals one. Suppose \(g(\theta)\) is nonnegative and not identically zero, and \(Z=\int g(\theta)\,d\theta\) is positive and finite. Then \(g(\theta)/Z\) is a probability density, and \(Z\) is its normalizing constant. A discrete nonnegative function uses a sum in place of the integral. If the integral is infinite, no positive finite constant makes the function a probability density.{{cite:durrett2019}} (Ch. 1, §1.2, p. 12){{cite:gelman_bda2013}} (pp. 42, 51–52)

In the posterior formula
\[
p(\theta\mid y)=\frac{p(\theta)\,p(y\mid\theta)}{p(y)},
\]
the marginal
\[
p(y)=\int p(\theta)\,p(y\mid\theta)\,d\theta
\]
does not depend on \(\theta\). It is the normalizing constant of the unnormalised posterior \(p(\theta)\,p(y\mid\theta)\). Equivalently one writes \(p(\theta\mid y)\propto p(\theta)\,p(y\mid\theta)\) and restores the constant when a numerical probability is required. The part that still depends on \(\theta\) is the [kernel of a density](kernel-of-a-density.qmd).{{cite:gelman_bda2013}} (p. 7)

## Properties
For a uniform prior on a binomial probability \(\theta\) and \(y\) successes in \(n\) trials, the marginal probability of the count is \(p(y)=1/(n+1)\) for each \(y=0,\ldots,n\). The unnormalised posterior may be taken as the kernel \(\theta^{y}(1-\theta)^{n-y}\), since the binomial coefficient does not depend on \(\theta\). The constant that turns that kernel into a density is
\[
\frac{(n+1)!}{y!\,(n-y)!}=(n+1)\binom{n}{y},
\]
and the density is the beta density with parameters \(y+1\) and \(n-y+1\). The two expressions agree: dividing the joint contribution \(\binom{n}{y}\theta^{y}(1-\theta)^{n-y}\) by the marginal \(1/(n+1)\) produces the same beta density.{{cite:gelman_bda2013}} (pp. 30–31)

A prior density that integrates to one can be rescaled if it was written without its constant. A prior function that integrates to infinity is improper: it has no normalizing constant. The formal product of that function with a likelihood may still have a finite integral, in which case the posterior has a normalizing constant even though the prior does not. That posterior has to be checked, not assumed.{{cite:gelman_bda2013}} (pp. 51–52)

## Statistical use
Recognising a kernel as an unnormalised beta, gamma, or normal density identifies the posterior family and reads the normalizing constant off the known formula for that family. When the kernel is not a known family, \(p(y)\) is an integral in as many dimensions as \(\theta\) has, and it is often the expensive part of the calculation. Posterior probabilities, posterior densities, and the [marginal likelihood and Bayes factor](marginal-likelihood-and-bayes-factor.qmd) all require it. Draws from the posterior can be used to compute posterior means and posterior probabilities of regions without ever printing the constant, provided the draws already come from the normalised distribution.{{cite:gelman_bda2013}} (pp. 7, 42)

## Worked example
Let \(n=2\) and \(y=2\), with \(\theta\) uniform on \([0,1]\). The kernel is \(k(\theta)=\theta^2\). Its integral is
\[
\int_0^1\theta^2\,d\theta=\frac13,
\]
so the normalizing constant is \(3\) and the posterior density is \(3\theta^2\). The binomial coefficient \(\binom{2}{2}\) equals \(1\), and the marginal probability of \(y=2\) is \(1/3\), so dividing the joint factor \(1\cdot\theta^2\) by \(1/3\) gives the same density.{{cite:gelman_bda2013}} (pp. 30–31)

**Your turn.** Now \(n=2\) and \(y=1\), so the kernel is \(\theta(1-\theta)\). Find its integral on \([0,1]\) and the normalizing constant of the posterior density.

::: {.callout-tip collapse="true" title="Answer"}
The integral is \(\int_0^1(\theta-\theta^2)\,d\theta=1/2-1/3=1/6\). The normalizing constant is \(6\), and the density is \(6\theta(1-\theta)\).
:::

## Common misconceptions
The kernel and the density are different functions whenever the constant is not \(1\). A likelihood is not a density in the parameter, so the binomial coefficient, or any other factor free of \(\theta\), is not the normalizing constant of the posterior. The marginal probability \(p(y)\) normalises the product of prior and likelihood; the constant of a kernel that has already dropped factors free of \(\theta\) is a different number, and the worked example is the case where those bookkeeping choices are easy to compare.{{cite:gelman_bda2013}} (pp. 7, 30–31)

## Assumptions and limits
A finite positive integral is required. An improper prior has none, and the posterior integral is a separate fact about the likelihood. In several parameters the integral that defines \(p(y)\) may have no closed form even when the unnormalised posterior is easy to write. A factor that depends on \(\theta\) cannot be absorbed into the constant; dropping it changes the posterior.{{cite:gelman_bda2013}} (pp. 42, 51–52)

## Connections
The unnormalised function, with the constant removed, is the [kernel of a density](kernel-of-a-density.qmd). The identity that places \(p(y)\) in the denominator is [Bayes' rule](bayes-rule.qmd). A prior with a finite integral is a [proper prior](proper-prior-and-proper-posterior.qmd); a prior function with an infinite integral is an [improper prior](improper-prior.qmd). For the uniform-binomial model the normalised posterior is a [beta distribution](beta-distribution.qmd).{{cite:gelman_bda2013}} (pp. 30–31, 51–52)

## History
Bayes's 1763 evaluation of the binomial marginal probability, \(1/(n+1)\) under a uniform prior, is an evaluation of this constant. The numerator he wanted, the probability of an interval for the unknown chance, still required an incomplete beta integral. Laplace's later analytic approximations were methods for that integral. Modern calculations either recognise the normalised family or compute the constant numerically, but the constant remains the marginal probability of the data in the posterior formula.{{cite:gelman_bda2013}} (pp. 30–31, 42)
