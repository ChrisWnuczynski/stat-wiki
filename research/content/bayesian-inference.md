## Lead context

Bayesian inference is the step that takes a joint probability model for data and unknowns and returns a probability distribution for the unknowns once the data are known. The distribution covers parameters and any observations that have not yet been seen. Gelman and coauthors open with that description: fit a probability model, then summarise the result by a probability distribution on the parameters and on unobserved quantities.{{cite:gelman_bda2013}} (p. 1)

## Motivating example

A woman has an affected brother, so her mother carries an X-linked hemophilia gene, and an unaffected father, so before any information about her own children she is a carrier with probability \(1/2\) and a non-carrier with probability \(1/2\). She then has two sons, neither affected. Each son would have had probability \(1/2\) of being affected if she were a carrier, and probability essentially \(1\) of being unaffected if she were not. The mutation rate is small enough, in this example, to ignore. The inference is the probability, after those two sons, that she is a carrier.{{cite:gelman_bda2013}} (p. 9, §1.4)

## Definition

Let \(\theta\) denote the unknowns and \(y\) the observed data. A joint distribution is required first,
\[
p(\theta,y)=p(\theta)\,p(y\mid\theta),
\]
with \(p(\theta)\) the prior distribution and \(p(y\mid\theta)\) the sampling distribution. Conditioning on the observed data gives the posterior
\[
p(\theta\mid y)=\frac{p(\theta)\,p(y\mid\theta)}{p(y)},
\]
wherever the marginal \(p(y)=\int p(\theta)\,p(y\mid\theta)\,d\theta\) is positive and finite. A discrete unknown replaces the integral by a sum. Dropping the factor \(p(y)\), which does not depend on \(\theta\), leaves the unnormalised posterior \(p(\theta\mid y)\propto p(\theta)\,p(y\mid\theta)\). The data enter this product only through the likelihood, the sampling distribution read as a function of \(\theta\) at the observed \(y\).{{cite:gelman_bda2013}} (pp. 6–7)

The same conditioning produces a distribution for a new observation \(\tilde y\). The posterior predictive distribution averages the sampling distribution of \(\tilde y\) over the posterior of \(\theta\), when \(y\) and \(\tilde y\) are conditionally independent given \(\theta\). Dodge writes the same step for a new observation \(x_{n+1}\): its density given the data is the sampling density averaged against the posterior of the parameter.{{cite:gelman_bda2013}} (p. 7){{cite:dodge2008}} (p. 33)

## Properties

Posterior odds between two values \(\theta_1\) and \(\theta_2\) equal prior odds times the likelihood ratio \(p(y\mid\theta_1)/p(y\mid\theta_2)\). Gelman and coauthors record the identity as equation (1.5). The marginal \(p(y)\) cancels, so the comparison of two point values does not need the normalising integral.{{cite:gelman_bda2013}} (p. 8, (1.5))

If a new observation arrives, the current posterior may be used as the prior for that observation. The result matches the posterior that would have been obtained by conditioning on the combined sample in one step. Gelman and coauthors call this the ease of a sequential analysis: the previous posterior is the new prior.{{cite:gelman_bda2013}} (p. 9)

On the carrier example the arithmetic is small enough to see both forms. The likelihood of two unaffected sons is \(0.25\) if she is a carrier and \(1\) if she is not. The prior probabilities are \(1/2\) and \(1/2\). The unnormalised posterior weights are \(0.25\times 0.5=0.125\) and \(1\times 0.5=0.5\). Their sum is \(0.625\), and
\[
\Pr(\text{carrier}\mid y)=\frac{0.125}{0.625}=0.2=\frac15.
\]
The prior odds are \(1\), the likelihood ratio is \(0.25\), and the posterior odds are \(0.25\), which converts back by \(0.25/(1+0.25)=0.2\).{{cite:gelman_bda2013}} (p. 9)

## Statistical use

The input is a [Bayesian model](bayesian-model.qmd): an explicit prior and a sampling distribution. The output used in a report is a posterior probability for a set of parameter values, a [posterior mean](posterior-mean.qmd) or another [posterior point summary](posterior-point-summaries.qmd), a [Bayesian credible interval](bayesian-credible-interval.qmd), or a [posterior predictive distribution](prior-and-posterior-predictive-distributions.qmd). Within one chosen model, the data affect these summaries only through the [likelihood function](likelihood-function.qmd). Checking whether that model is adequate is a later part of [Bayesian statistics](bayesian-statistics.qmd). Gelman and coauthors separate that check from the conditioning step: the three-step outline is to write the joint model, condition on the data, and then evaluate the fit.{{cite:gelman_bda2013}} (pp. 3, 7, §1.1)

Dodge lists the same practical products once the posterior density is in hand: a point summary such as the mean under squared error, a region that holds a stated posterior probability, and a test of a hypothesis about the parameter, tied to a loss function. The region that holds posterior probability \(\alpha\) is what replaces, in that account, the confidence interval of the sampling theory.{{cite:dodge2008}} (pp. 33–34)

## Worked example

The carrier probability starts at \(1/2\). The likelihood of two unaffected sons is \(1/4\) if she is a carrier and \(1\) if she is not. The unnormalised posterior weights are
\[
\tfrac14\cdot\tfrac12=\tfrac18, \qquad 1\cdot\tfrac12=\tfrac12.
\]
Their sum is \(5/8\), so the posterior probability that she is a carrier is \((1/8)/(5/8)=1/5\). That is the same number as \(0.125/0.625=0.2\).{{cite:gelman_bda2013}} (p. 9)

**Your turn.** A third son is also unaffected. Using the posterior above as the new prior, what is the probability that she is a carrier?

::: {.callout-tip collapse="true" title="Answer"}
The new unnormalised weights are \((1/2)\cdot(1/5)=1/10\) for the carrier and \(1\cdot(4/5)=4/5\) for the non-carrier. The probability is \((1/10)/(1/10+4/5)=1/9\).
:::

## Common misconceptions

The likelihood at a parameter value is the probability of the observed data given that value. A posterior probability is the probability of the parameter value given the data, after the prior has reweighted every value and the weights have been made to sum to one. A posterior probability for a parameter is also a different object from the long-run error rate of a procedure. A Bayesian interval is read as a probability that the unknown lies in the interval. A confidence interval, as Gelman and coauthors contrast it, is read in relation to a sequence of similar inferences in repeated practice.{{cite:gelman_bda2013}} (p. 3)

The identities assume a joint distribution in which the prior does not depend on the data and the marginal probability of the observed sample is positive and finite. The likelihood principle, that the data enter only through \(p(y\mid\theta)\), is a fact inside the model that was chosen. It does not say that the model is adequate. The third step of the analysis is the check of that model.{{cite:gelman_bda2013}} (pp. 3, 7, §1.1)

## History

The first published analysis of this form is Bayes's 1763 solution for an unknown binomial probability. Laplace developed the same reversal for counts. Dodge dates the inferential tradition that includes this reversal to Bayes (1763), de Moivre (1718), Gauss (1809), and Laplace (1812). The calculation above, updating a carrier probability from the sons' affection status, is the same conditioning step applied to a two-point unknown, as set out by Gelman and coauthors.{{cite:gelman_bda2013}} (p. 9){{cite:dodge2008}} (pp. 32, 263)

## Connections

The arithmetic identity is [Bayes' rule](bayes-rule.qmd). The probability attached to a set of unknowns after conditioning is a [posterior probability](posterior-probability.qmd). The proportionality \(p(\theta\mid y)\propto p(\theta)\,p(y\mid\theta)\) is the [kernel of a density](kernel-of-a-density.qmd) in the parameter, and \(p(y)\) is its [normalizing constant](normalizing-constant.qmd). The historical name for reading probability from the data back to the unknown is [inverse probability](inverse-probability.qmd). The joint specification that the conditioning step takes as given is a [Bayesian model](bayesian-model.qmd).{{cite:gelman_bda2013}} (pp. 6–7){{cite:dodge2008}} (p. 33)
