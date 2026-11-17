## Lead context

A normalizing constant is the factor that turns a nonnegative function into a probability density or a probability mass function. In a Bayesian calculation it is often the marginal probability of the observed data, the denominator of Bayes' rule. Relative heights of an unnormalised posterior can be compared without it. A probability, a density height, or a marginal likelihood cannot.{{cite:gelman_bda2013}} (p. 7, §1.3)

## Motivating example

After a binomial sample, the product of a uniform prior and the likelihood is a power of the unknown probability times a power of its complement. Bayes evaluated the marginal probability of the count under that prior and found
\[
p(y)=\frac{1}{n+1}, \qquad y=0,\ldots,n.
\]
The product \(\theta^{y}(1-\theta)^{n-y}\) shows where the posterior is high and where it is low, and it does not integrate to one. Dividing by \(p(y)\), or equivalently multiplying by the constant that the beta integral supplies, makes the area equal to one. The number is determined by the data and the prior. It is not a further modelling choice.{{cite:gelman_bda2013}} (pp. 31–32, §2.1, equation 2.5)

## Intuition

Relative heights are fixed by the unnormalised function. The constant lifts or lowers the whole graph until the total probability is one. Any question that depends only on ratios at different parameter values can ignore the constant, because it cancels. The ratio of the posterior density at two parameter values equals the ratio of the unnormalised products of prior and likelihood at those values. Any question that asks for a probability, a density height, or the marginal probability of the data has to put the constant back.{{cite:gelman_bda2013}} (p. 7, §1.3)

## Definition

Suppose \(g(\theta)\) is nonnegative and not identically zero, and \(Z=\int g(\theta)\,d\theta\) is positive and finite. Then \(g(\theta)/Z\) is a probability density, and \(Z\) is its normalizing constant. A discrete nonnegative function uses a sum in place of the integral. If the integral is infinite, no positive finite constant makes the function a probability density. A prior density is called proper when it does not depend on the data and integrates to one. A function that integrates to a positive finite value other than one is an unnormalised density and can be multiplied by a constant to integrate to one. A prior whose integral over the parameter space is infinite is improper.{{cite:gelman_bda2013}} (p. 52, §2.8){{cite:durrett2019}} (Ch. 1, §1.2, p. 11)

In the posterior formula
\[
p(\theta\mid y)=\frac{p(\theta)\,p(y\mid\theta)}{p(y)},
\]
the marginal
\[
p(y)=\int p(\theta)\,p(y\mid\theta)\,d\theta
\]
does not depend on \(\theta\). It is the normalizing constant of the unnormalised posterior \(p(\theta)\,p(y\mid\theta)\). Equivalently one writes \(p(\theta\mid y)\propto p(\theta)\,p(y\mid\theta)\) and restores the constant when a numerical probability is required. The part that still depends on \(\theta\) is the [kernel of a density](kernel-of-a-density.qmd).{{cite:gelman_bda2013}} (p. 7, §1.3, equations 1.1 and 1.2)

## Statistical use

Recognising a kernel as an unnormalised beta, gamma, or normal density identifies the posterior family and reads the normalizing constant off the known formula for that family. For a uniform prior on a binomial probability and \(y\) successes in \(n\) trials, \(p(y)=1/(n+1)\) for each \(y=0,\ldots,n\), so every count is equally likely before the data are seen. The posterior density is the beta density with parameters \(y+1\) and \(n-y+1\). The constant that turns the kernel \(\theta^{y}(1-\theta)^{n-y}\) into that density is \((n+1)!/(y!\,(n-y)!)\). Dividing the joint contribution \(\binom{n}{y}\theta^{y}(1-\theta)^{n-y}\) by the marginal \(1/(n+1)\) produces the same beta density, because \(\binom{n}{y}(n+1)\) equals that factorial ratio.{{cite:gelman_bda2013}} (pp. 31–32, §2.1)

When the kernel is not a known family, \(p(y)\) is an integral in as many dimensions as \(\theta\) has, and it is often the expensive part of the calculation. Posterior probabilities of regions and the [marginal likelihood and Bayes factor](marginal-likelihood-and-bayes-factor.qmd) require it. Draws from the posterior can be used to compute posterior means without printing the constant, provided the draws already come from the normalised distribution. A prior that integrates to infinity has no normalizing constant. The formal product of that function with a likelihood may still have a finite integral, in which case the posterior is proper even though the prior is not. That posterior has to be checked. An improper prior is not a joint probability model for the data and the parameter.{{cite:gelman_bda2013}} (pp. 7 and 51–52, §§1.3 and 2.8)

## Worked example

Let \(n=2\) and \(y=2\), with \(\theta\) uniform on \([0,1]\). The kernel is \(k(\theta)=\theta^2\). Its integral is
\[
\int_0^1\theta^2\,d\theta=\frac13,
\]
so the normalizing constant is \(3\) and the posterior density is \(3\theta^2\). The binomial coefficient \(\binom{2}{2}\) equals \(1\), and the marginal probability of \(y=2\) is \(1/3\), so dividing the joint factor \(1\cdot\theta^2\) by \(1/3\) gives the same density.{{cite:gelman_bda2013}} (pp. 31–32, §2.1)

**Your turn.** Now \(n=2\) and \(y=1\), so the kernel is \(\theta(1-\theta)\). Find its integral on \([0,1]\) and the normalizing constant of the posterior density.

::: {.callout-tip collapse="true" title="Answer"}
The integral is \(\int_0^1(\theta-\theta^2)\,d\theta=1/2-1/3=1/6\). The normalizing constant is \(6\), and the density is \(6\theta(1-\theta)\).
:::

## Common misconceptions

The kernel and the density are different functions whenever the constant is not \(1\). A likelihood is not a density in the parameter, so the binomial coefficient, or any other factor free of \(\theta\), is not the normalizing constant of the posterior. The marginal probability \(p(y)\) normalises the product of prior and likelihood. The constant of a kernel that has already dropped factors free of \(\theta\) is a different number. In the worked example those two bookkeeping choices are easy to compare because the binomial coefficient equals \(1\).{{cite:gelman_bda2013}} (p. 7, §1.3; pp. 31–32, §2.1)

An improper prior is not repaired by writing a proportionality sign. The posterior integral is a separate fact about the likelihood. In the normal model with known variance, a flat prior is the limit of a normal prior whose variance grows, and the posterior after at least one observation is a proper normal. That check does not transfer to every flat prior. A factor that depends on \(\theta\) cannot be absorbed into the constant. Dropping it changes the posterior.{{cite:gelman_bda2013}} (pp. 51–52, §2.8)

## Connections

The unnormalised function, with the constant removed, is the [kernel of a density](kernel-of-a-density.qmd). The identity that places \(p(y)\) in the denominator is [Bayes' rule](bayes-rule.qmd). A prior with a finite integral is a [proper prior](proper-prior-and-proper-posterior.qmd). A prior function with an infinite integral is an [improper prior](improper-prior.qmd). For the uniform-binomial model the normalised posterior is a [beta distribution](beta-distribution.qmd). A distribution function on the line rises from \(0\) to \(1\), which is the same requirement that a density integrate to one, stated for the cumulative probability rather than for the height.{{cite:gelman_bda2013}} (pp. 31–32 and 51–52){{cite:durrett2019}} (Ch. 1, §1.2, p. 11, the distribution-function fact)
