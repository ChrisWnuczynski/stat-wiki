

## Lead context

Inverse probability is the historical name for the step that turns a sampling model around and states a probability for the unknown given the observations. In current vocabulary that step is Bayesian inference, and the probability it produces is a posterior probability.{{cite:gelman_bda2013}} (pp. 31, 56)

## Motivating example

A sampling calculation starts from a known chance \(\theta\) and gives the probability of each possible count \(y\). The early binomial theorems are of that kind: if \(y\) is binomial with known \(\theta\), the sample proportion settles near \(\theta\) as the number of trials grows. The inverse question fixes the observed count and asks for a probability that \(\theta\) itself lies in some interval. That is the question Bayes set, and the question Laplace answered for the proportion of girls among births.{{cite:gelman_bda2013}} (pp. 30–31)

## Definition

For binomial data, \(y\) successes in \(n\) independent trials, each with unknown probability \(\theta\), a uniform distribution on \(\theta\) in \([0,1]\) was the classical initial assignment. The inverse probability of an interval \((\theta_1,\theta_2)\) is
\[
P\bigl(\theta\in(\theta_1,\theta_2)\mid y\bigr)
=\frac{\int_{\theta_1}^{\theta_2}\theta^{y}(1-\theta)^{n-y}\,d\theta}{\int_0^1\theta^{y}(1-\theta)^{n-y}\,d\theta}.
\]
Bayes evaluated the denominator: with the uniform assignment, each count \(y=0,\ldots,n\) has marginal probability \(1/(n+1)\). The numerator is an incomplete beta integral. The same uniform-binomial pair is what Laplace used.{{cite:gelman_bda2013}} (pp. 30–31)

The unknown is treated as carrying a probability distribution because it is unknown. The distribution after the data is proportional to the initial distribution times the likelihood. That product, normalised, is the posterior distribution whose probabilities are the inverse probabilities of the older language.{{cite:dodge2008}} (pp. 32–33)

Direct probability runs from cause to effect: the unknown chance is given, and the data are random. Inverse probability runs from effect to cause: the data are now the fixed record, and the chance is what carries the probability. The arithmetic is [Bayes' rule](bayes-rule.qmd). What made the step a distinct historical topic is the willingness to put a probability distribution on the chance before any observations, and then to condition.{{cite:gelman_bda2013}} (pp. 30–31){{cite:dodge2008}} (p. 32)

The interval probability above is a [posterior probability](posterior-probability.qmd). Computing it, and summarising the resulting distribution, is [Bayesian inference](bayesian-inference.qmd). The uniform distribution together with the binomial sampling model is a [Bayesian model](bayesian-model.qmd). The beta family that falls out of the uniform-binomial pair is the [beta distribution](beta-distribution.qmd). Current practice keeps the inversion and is free to replace the uniform distribution by another prior when there is information about \(\theta\); the uniform choice is one model, not a requirement of the inversion.{{cite:gelman_bda2013}} (pp. 29–32){{cite:dodge2008}} (pp. 32–33)

The probability of the data given a fixed chance is the direct probability. Inverse probability is a probability for the chance given the data, and it depends on the distribution that was assigned to the chance before the data. With a uniform assignment, a posterior probability for an interval of \(\theta\) is not the relative frequency of that interval in repeated samples. Replacing the uniform distribution changes the inverse probability even when the observed count stays the same.{{cite:gelman_bda2013}} (pp. 30–32){{cite:dodge2008}} (pp. 32–33)

The general identity, of which the binomial formula is one case, is [Bayes' rule](bayes-rule.qmd). The discipline that now contains the method is [Bayesian statistics](bayesian-statistics.qmd). Putting a probability on the unknown chance in the first place is [Bayesian probability](bayesian-probability.qmd). The integral in the denominator is a [normalizing constant](normalizing-constant.qmd).{{cite:gelman_bda2013}} (pp. 7, 31, 42)

## Properties

Under the uniform assignment, the posterior distribution of \(\theta\) given \(y\) successes in \(n\) trials is the beta distribution with parameters \(y+1\) and \(n-y+1\). Its density on \((0,1)\) is
\[
p(\theta\mid y)=(n+1)\binom{n}{y}\theta^{y}(1-\theta)^{n-y}.
\]
The marginal probability \(1/(n+1)\) is what makes the binomial coefficient and this beta density consistent: the joint probability of \((y,\theta)\) integrates in \(\theta\) to \(1/(n+1)\).{{cite:gelman_bda2013}} (pp. 30–31)

The posterior mean is \((y+1)/(n+2)\). For a single new trial, exchangeable with the first \(n\), the probability of success is that same mean. At the extreme samples \(y=0\) and \(y=n\) the predictive probabilities are \(1/(n+2)\) and \((n+1)/(n+2)\). This is Laplace's rule of succession for the uniform prior.{{cite:gelman_bda2013}} (pp. 31–32)

## Worked example

Take one trial, \(n=1\), and suppose it is a success, \(y=1\), with \(\theta\) uniform on \([0,1]\). The kernel is \(\theta\), and \(\int_0^1\theta\,d\theta=1/2\), so the posterior density is \(2\theta\). Then
\[
P(\theta>1/2\mid y=1)=\int_{1/2}^1 2\theta\,d\theta=\bigl[\theta^2\bigr]_{1/2}^1=1-\tfrac14=\tfrac34.
\]
The direct probability of a success when \(\theta=1/2\) is \(1/2\). The inverse probability that \(\theta\) exceeds \(1/2\), after a success, is \(3/4\). The marginal probability of the success is \(1/(1+1)=1/2\).{{cite:gelman_bda2013}} (pp. 30–31)

**Your turn.** The single trial is a failure, so \(y=0\). The posterior density is \(2(1-\theta)\). Find \(P(\theta>1/2\mid y=0)\).

::: {.callout-tip collapse="true" title="Answer"}
The integral is \(\int_{1/2}^1 2(1-\theta)\,d\theta=\bigl[2\theta-\theta^2\bigr]_{1/2}^1=(2-1)-(1-1/4)=1/4\).
:::

## Assumptions and limits

The closed beta form uses a uniform distribution on a chance that lies in \([0,1]\), and independent Bernoulli trials. Another prior replaces \(y+1\) and \(n-y+1\) by different beta parameters, or leaves no beta distribution at all. Bayes's evaluation of the marginal probability as \(1/(n+1)\) is special to the uniform assignment: it says that, before the trials, every count from \(0\) to \(n\) is equally likely. The normal approximation Laplace used for the incomplete beta integral is an approximation for large counts, not an identity.{{cite:gelman_bda2013}} (pp. 30–32)

## History

Seventeenth- and early eighteenth-century probability, including Jacob Bernoulli's law of large numbers for a binomial proportion, answered the direct question. Bayes, whose essay appeared in the *Philosophical Transactions* in 1763, and Laplace, working independently, are credited with the inversion: a probability for the unknown chance given the count. Bayes's argument pictured the unknown chance as the position of a ball thrown uniformly onto a table, and the successes as further balls landing to one side of it. The phrase inverse probability is the later name for that inversion. A uniform prior remained the worked example, including Laplace's analysis of \(241{,}945\) girls and \(251{,}527\) boys born in Paris, for which the probability of a female proportion of at least one half was tiny.{{cite:gelman_bda2013}} (pp. 30–31, 56){{cite:dodge2008}} (p. 32)
