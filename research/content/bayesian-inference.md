

## Lead context

Bayesian inference is the step that takes a joint probability model for data and unknowns and returns a probability distribution for the unknowns once the data are known. The distribution covers parameters and any observations that have not yet been seen.{{cite:gelman_bda2013}} (p. 1)

## Motivating example

A woman has an affected brother and an unaffected father, so before any information about her own children she is a carrier of an X-linked gene with probability \(1/2\) and a non-carrier with probability \(1/2\). She then has two sons, neither affected. Each son would have had probability \(1/2\) of being affected if she were a carrier, and probability essentially \(0\) of being affected if she were not. The inference is the probability, after those two sons, that she is a carrier.{{cite:gelman_bda2013}} (p. 9)

## Definition

Let \(\theta\) denote the unknowns and \(y\) the observed data. A joint distribution is required first,
\[
p(\theta,y)=p(\theta)\,p(y\mid\theta),
\]
with \(p(\theta)\) the prior distribution and \(p(y\mid\theta)\) the sampling distribution. [Bayes' rule](bayes-rule.qmd) then gives the posterior distribution
\[
p(\theta\mid y)=\frac{p(\theta)\,p(y\mid\theta)}{p(y)},
\]
wherever the marginal \(p(y)=\int p(\theta)\,p(y\mid\theta)\,d\theta\) is positive and finite. A discrete unknown replaces the integral by a sum. Dropping the factor \(p(y)\), which does not depend on \(\theta\), leaves the unnormalised posterior \(p(\theta\mid y)\propto p(\theta)\,p(y\mid\theta)\). The data enter this product only through the likelihood, the sampling distribution read as a function of \(\theta\) at the observed \(y\).{{cite:gelman_bda2013}} (pp. 6–7)

The same conditioning produces a distribution for a new observation \(\tilde y\). The posterior predictive distribution averages the sampling distribution of \(\tilde y\) over the posterior of \(\theta\), under the assumption that \(y\) and \(\tilde y\) are conditionally independent given \(\theta\).{{cite:gelman_bda2013}} (p. 7)

The sampling model runs from the unknown to the data: it says how the observations would behave if the unknown were fixed at a particular value. Inference runs the other way. It keeps every value of the unknown that the model allows, reweights each value by how probable the observed data are there, and scales the weights so that they add to one. The result is a probability statement about the unknown given the data that actually occurred, rather than a summary of how an estimator would behave across data sets that did not occur.{{cite:gelman_bda2013}} (pp. 6–7)

The identities assume a joint distribution in which the prior does not depend on the data and the marginal probability of the observed sample is positive and finite. An improper prior function has no finite integral, so it does not by itself define that joint distribution; the formal product with the likelihood is usable only when the resulting posterior integral is finite. The likelihood principle, that the data enter only through \(p(y\mid\theta)\), is a fact inside the model that was chosen. It does not say that the model is adequate.{{cite:gelman_bda2013}} (pp. 7–8, 51–52)

## Properties

Posterior odds between two values \(\theta_1\) and \(\theta_2\) equal prior odds times the likelihood ratio \(p(y\mid\theta_1)/p(y\mid\theta_2)\). The marginal \(p(y)\) cancels, so the comparison of two point values does not need the normalising integral.{{cite:gelman_bda2013}} (p. 8)

On average over data sets drawn from the joint model, the posterior variance of a parameter is smaller than the prior variance, by the variance of the posterior mean across those data sets. A particular sample can still leave the posterior as spread out as the prior, or more so, when the sample and the prior conflict. The posterior mean is a compromise between the prior mean and the information in the sample; as the sample grows, the sample dominates.{{cite:gelman_bda2013}} (pp. 32–33)

If a new observation arrives, the current posterior may be used as the prior for that observation. The result matches the posterior that would have been obtained by conditioning on the combined sample in one step.{{cite:gelman_bda2013}} (p. 9)

## Statistical use

The input is a [Bayesian model](bayesian-model.qmd): an explicit prior and a sampling distribution. The output used in a report is a posterior probability for a set of parameter values, a [posterior mean](posterior-mean.qmd) or another [posterior point summary](posterior-point-summaries.qmd), a [Bayesian credible interval](bayesian-credible-interval.qmd), or a [posterior predictive distribution](prior-and-posterior-predictive-distributions.qmd). Within one chosen model, the data affect these summaries only through the [likelihood function](likelihood-function.qmd). Checking whether that model is adequate is a later part of [Bayesian statistics](bayesian-statistics.qmd), and it can use the sampling distribution of hypothetical repetitions.{{cite:gelman_bda2013}} (pp. 7–8, 24)

## Worked example

The carrier probability starts at \(1/2\). The likelihood of two unaffected sons is \(1/4\) if she is a carrier and \(1\) if she is not. The unnormalised posterior weights are
\[
\tfrac14\cdot\tfrac12=\tfrac18, \qquad 1\cdot\tfrac12=\tfrac12.
\]
Their sum is \(5/8\), so the posterior probability that she is a carrier is \((1/8)/(5/8)=1/5\). The prior odds are \(1\), the likelihood ratio is \(1/4\), and the posterior odds are \(1/4\), which is the same probability: \((1/4)/(1+1/4)=1/5\).{{cite:gelman_bda2013}} (p. 9)

**Your turn.** A third son is also unaffected. Using the posterior above as the new prior, what is the probability that she is a carrier?

::: {.callout-tip collapse="true" title="Answer"}
The new unnormalised weights are \((1/2)\cdot(1/5)=1/10\) and \(1\cdot(4/5)=4/5\). The probability is \((1/10)/(1/10+4/5)=1/9\).
:::

## Common misconceptions

The likelihood at a parameter value is the probability of the observed data given that value. A posterior probability is the probability of the parameter value given the data, after the prior has reweighted every value and the weights have been made to sum to one. A posterior probability for a parameter is also a different object from the long-run error rate of a procedure that rejects or accepts a hypothesis.{{cite:gelman_bda2013}} (pp. 3–4, 7–8)

## History

The first published analysis of this form is Bayes's 1763 solution for an unknown binomial probability, using a uniform distribution on that probability before the trials. Laplace developed the same reversal for the proportion of female births and for other counts. The calculation above, updating a carrier probability from the sons' affection status, is the same conditioning step applied to a two-point unknown.{{cite:gelman_bda2013}} (pp. 9, 31){{cite:dodge2008}} (p. 32)

## Connections

The arithmetic identity is [Bayes' rule](bayes-rule.qmd). The probability attached to a set of unknowns after conditioning is a [posterior probability](posterior-probability.qmd). The proportionality \(p(\theta\mid y)\propto p(\theta)\,p(y\mid\theta)\) is the [kernel of a density](kernel-of-a-density.qmd) in the parameter, and \(p(y)\) is its [normalizing constant](normalizing-constant.qmd). The historical name for reading probability from the data back to the unknown is [inverse probability](inverse-probability.qmd).{{cite:gelman_bda2013}} (pp. 7, 56)
