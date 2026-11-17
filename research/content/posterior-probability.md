

## Lead context
A posterior probability is the probability a model assigns to a set of parameter values after the data are included. A [posterior hypothesis probability](posterior-hypothesis-probability.qmd) is that probability when the set is a named hypothesis. One question is about a region of a parameter. The other is about a hypothesis written as such a region.

A posterior probability is the probability of an event about an unknown after the data have been taken into account. It is computed from a prior distribution and a sampling model, not from the sample alone.{{cite:gelman_bda2013}} (pp. 6–7)

## Motivating example

Two explanations of a binary outcome are open: explanation \(A\) with prior probability \(1/4\), and explanation \(B\) with prior probability \(3/4\). The observed sample has probability \(1/2\) under \(A\) and probability \(1/6\) under \(B\). The question the posterior answers is how probable \(A\) is once that sample has been seen. The prior probabilities and the two sampling probabilities are the ingredients; neither ingredient is already the answer.{{cite:gelman_bda2013}} (pp. 6–9)

## Definition

For a discrete unknown \(\theta\) and observed data \(y\),
\[
P(\theta=\theta_j\mid y)
=\frac{p(y\mid\theta_j)\,P(\theta=\theta_j)}{\sum_i p(y\mid\theta_i)\,P(\theta=\theta_i)},
\]
provided the denominator is positive. For a continuous parameter with prior density \(p(\theta)\) and sampling density \(p(y\mid\theta)\), the posterior density is
\[
p(\theta\mid y)=\frac{p(\theta)\,p(y\mid\theta)}{p(y)},
\qquad
p(y)=\int p(\theta)\,p(y\mid\theta)\,d\theta.
\]
The posterior probability of a set \(A\) of parameter values is the integral of that density over \(A\), or the sum of the point masses in \(A\). The whole function \(p(\theta\mid y)\) is the posterior distribution; a posterior probability is the mass it assigns to a specified set.{{cite:gelman_bda2013}} (pp. 6–7)

In the carrier example, the set has one point, "she is a carrier", the prior probability is \(1/2\), and the likelihood of two unaffected sons is \(1/4\) against \(1\). The posterior probability of that point is \(1/5\).{{cite:gelman_bda2013}} (p. 9)

Each explanation is first given its prior weight, then multiplied by the probability of the data under that explanation. Explanations that make the sample surprising are scaled down; explanations that make the sample expected are scaled up. Dividing by the sum of the weighted values turns the list into probabilities. The number on one explanation is then the share of the total weight that explanation still holds.{{cite:gelman_bda2013}} (pp. 7–8)

Posterior probabilities are the numbers reported for parameter regions, for model indicators, and for events defined from future observations. A [Bayesian credible interval](bayesian-credible-interval.qmd) is an interval whose posterior probability equals a chosen level. The [posterior mean](posterior-mean.qmd) is the mean of the same distribution, not a substitute for the probability of a region. When the unknown is a model index, the posterior probability of a model is prior odds times a Bayes factor, converted back from odds, as in the [marginal likelihood and Bayes factor](marginal-likelihood-and-bayes-factor.qmd).{{cite:gelman_bda2013}} (pp. 7–8, 32–33)

A likelihood value \(p(y\mid\theta)\) is not a posterior probability: the likelihoods at different parameter values need not add to one. A prior probability is the assignment before \(y\) is used. A long-run coverage probability of a confidence procedure is a property of the procedure across repeated samples, not the posterior probability that the parameter lies in one computed interval.{{cite:gelman_bda2013}} (pp. 3–4, 7–8)

The operation that produces the posterior distribution is [Bayesian inference](bayesian-inference.qmd), and the identity is [Bayes' rule](bayes-rule.qmd). The joint specification required before any posterior probability can be computed is a [Bayesian model](bayesian-model.qmd). The probability calculus being used is [Bayesian probability](bayesian-probability.qmd). The factor \(p(y)\) in the denominator is the [normalizing constant](normalizing-constant.qmd).{{cite:gelman_bda2013}} (pp. 6–7, 42)

## Properties

The ratio of two posterior probabilities equals the prior odds times the likelihood ratio. The marginal probability of the data cancels, so
\[
\frac{P(\theta=\theta_1\mid y)}{P(\theta=\theta_2\mid y)}
=\frac{P(\theta=\theta_1)}{P(\theta=\theta_2)}\cdot\frac{p(y\mid\theta_1)}{p(y\mid\theta_2)}.
\]
If the prior probability of a region is zero, the posterior probability of that region remains zero whenever the posterior is defined. Multiplying by a likelihood cannot create mass outside the prior's support.{{cite:gelman_bda2013}} (pp. 7–8)

A continuous posterior assigns probability zero to any single point. The posterior probability of a hypothesis that names a region is the mass of that region, which is a [posterior hypothesis probability](posterior-hypothesis-probability.qmd). An equal-tailed posterior interval and the probability of a fixed region such as \(\{\theta\le 1/2\}\) answer different questions: the interval chooses its endpoints to put a stated mass in the tails, while the hypothesis fixes the region and reads off the mass.{{cite:gelman_bda2013}} (pp. 32–33){{cite:dodge2008}} (pp. 33–34)

## Worked example

Prior probabilities are \(P(A)=1/4\) and \(P(B)=3/4\). The sampling probabilities of the observed sample are \(1/2\) under \(A\) and \(1/6\) under \(B\). The unnormalised weights are
\[
\tfrac14\cdot\tfrac12=\tfrac18, \qquad \tfrac34\cdot\tfrac16=\tfrac18.
\]
The marginal probability of the sample is \(1/8+1/8=1/4\). The posterior probability of \(A\) is \((1/8)/(1/4)=1/2\). The likelihood ratio in favour of \(A\) is \((1/2)/(1/6)=3\), and the prior odds of \(A\) against \(B\) are \((1/4)/(3/4)=1/3\), so the posterior odds are \(1\), which is the same probability \(1/2\).{{cite:gelman_bda2013}} (pp. 7–8)

**Your turn.** Keep the sampling probabilities \(1/2\) and \(1/6\), and replace the prior by \(P(A)=P(B)=1/2\). What is the posterior probability of \(A\)?

::: {.callout-tip collapse="true" title="Answer"}
The unnormalised weights are \((1/2)\cdot(1/2)=1/4\) and \((1/2)\cdot(1/6)=1/12\). Their sum is \(1/3\), so the posterior probability of \(A\) is \((1/4)/(1/3)=3/4\).
:::

## Assumptions and limits

The denominator must be positive and finite. If the prior is an improper function, there is no prior probability to start from, and a posterior probability is available only after the product of that function and the likelihood has been checked to have a finite integral. The numerical value depends on the whole prior, not only on the maximum of the likelihood. A posterior probability computed under one model is conditional on that model.{{cite:gelman_bda2013}} (pp. 7, 51–52)

## History

Bayes's 1763 essay asked for the probability that an unknown chance lies between two bounds, given the number of successes in a fixed number of trials. That is a posterior probability for an interval of the unknown. Laplace computed the same kind of probability for the proportion of female births, under a uniform prior, and treated a tiny probability for the proportion being at least one half as decisive. The name used for this reversal, before "posterior" became standard, was inverse probability.{{cite:gelman_bda2013}} (pp. 31, 56){{cite:dodge2008}} (pp. 32–33)
