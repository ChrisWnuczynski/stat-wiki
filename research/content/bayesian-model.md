## Lead context
A Bayesian model is a joint probability specification for the observations and the unknowns. It states what the data would do if the unknowns were fixed, and it states how sure one is about the unknowns before those data are used.{{cite:gelman_bda2013}} (pp. 6–7)

## Motivating example
A coin lands heads or tails once. Two explanations are on the table: the heads probability is \(0.2\), or it is \(0.8\), and before the toss those two explanations are equally serious. The model is the pair of explanations together with the chance of heads under each of them. The single toss has not yet been seen, so the model is not yet a statement about which explanation the toss will favour.{{cite:gelman_bda2013}} (pp. 6–7){{cite:dodge2008}} (p. 33)

## Intuition
Two pieces have to be written down, and they do different jobs. The sampling distribution says how the observations arise once the unknown is given. The prior distribution says which values of the unknown are entertained, and with what weight, before the sample is consulted. Their product is the joint distribution. Anything called a posterior is computed from that joint distribution; it is a result, not a third ingredient of the model.{{cite:gelman_bda2013}} (pp. 6–7)

## Definition
Let \(y\) be the observations and \(\theta\) the unknowns. The model is a joint distribution that factors as
\[
p(\theta,y)=p(\theta)\,p(y\mid\theta).
\]
Here \(p(\theta)\) is the prior and \(p(y\mid\theta)\) is the sampling distribution, also called the data distribution. When \(y\) is held at the observed value and the product is read as a function of \(\theta\), the sampling factor is the likelihood. A model for several exchangeable observations often takes those observations as independent given \(\theta\), with a common distribution \(p(y_i\mid\theta)\). Explanatory variables that are conditioned on and not modelled as random may sit inside that sampling distribution.{{cite:gelman_bda2013}} (pp. 5–7)

Writing the model is the first of the three parts of a Bayesian analysis: the joint distribution has to be consistent with what is known about the phenomenon and about the way the data were collected. Specifying a parametric family for the observations, and specifying a distribution for its parameter, are the two modelling choices that the later conditioning step takes as given.{{cite:dodge2008}} (p. 33){{cite:gelman_bda2013}} (p. 3)

## Properties
The joint distribution determines the marginal distribution of the data,
\[
p(y)=\int p(\theta)\,p(y\mid\theta)\,d\theta,
\]
and the posterior \(p(\theta\mid y)=p(\theta)\,p(y\mid\theta)/p(y)\) wherever that marginal is positive and finite. Changing the prior changes the joint distribution even when the sampling distribution is held fixed, and so it changes the posterior. A prior that integrates to one, and does not depend on \(y\), is a proper prior. A function of \(\theta\) with an infinite integral does not complete a joint probability model, even if the formal product \(p(y\mid\theta)p(\theta)\) happens to have a finite integral in \(\theta\).{{cite:gelman_bda2013}} (pp. 7, 51–52)

If the same experimental conditions are judged exchangeable, the joint distribution of the observations is invariant to permuting their labels. The independent-and-identical sampling model given \(\theta\) is the usual way of writing that judgement. A hierarchical model adds a further distribution for the parameters of the prior, so that several related groups share a model while keeping their own parameters.{{cite:gelman_bda2013}} (pp. 5–6, 24)

## Statistical use
The sampling piece is the [likelihood function](likelihood-function.qmd) once the data are inserted. The prior piece may be a named distribution, a weakly informative distribution, or, with the warning above, an [improper prior](improper-prior.qmd). Conditioning the joint distribution on \(y\) is [Bayesian inference](bayesian-inference.qmd). The marginal \(p(y)\) is the [normalizing constant](normalizing-constant.qmd) of the unnormalised posterior and, when two models are compared, the central ingredient of the [marginal likelihood and Bayes factor](marginal-likelihood-and-bayes-factor.qmd). A model that gives the parameters of the prior their own distribution is a [hierarchical Bayesian model](hierarchical-bayesian-model.qmd).{{cite:gelman_bda2013}} (pp. 7, 24){{cite:dodge2008}} (p. 33)

## Worked example
Take \(\theta\in\{0.2,0.8\}\) with prior probability \(1/2\) each, and let \(y\) be a single Bernoulli trial with success probability \(\theta\). The model assigns the joint probabilities
\[
\begin{align*}
P(\theta=0.2,\, y=1)&=(1/2)\cdot 0.2=0.1,\\
P(\theta=0.8,\, y=1)&=(1/2)\cdot 0.8=0.4.
\end{align*}
\]
Those two numbers are the model at the observed success. They sum to \(P(y=1)=0.5\). Dividing by that marginal produces posterior probabilities \(0.2\) and \(0.8\). The division is inference from the model; it is not part of writing the model down.{{cite:gelman_bda2013}} (pp. 6–7)

**Your turn.** Under the same model, the trial is a failure, \(y=0\). Find the joint probability of \(\{\theta=0.2,\, y=0\}\) and the posterior probability of \(\theta=0.2\).

::: {.callout-tip collapse="true" title="Answer"}
The joint probability is \((1/2)\cdot 0.8=0.4\). The marginal probability of failure is \(0.4+0.1=0.5\), so the posterior probability of \(\theta=0.2\) is \(0.4/0.5=0.8\).
:::

## Common misconceptions
A likelihood, by itself, is not a Bayesian model: it lacks a distribution for the unknown. A prior, by itself, is not a Bayesian model: it lacks a distribution for the data. The posterior is the conditional distribution computed from the model after \(y\) is observed, so quoting a posterior without the prior and the sampling distribution leaves the model unnamed. A fitted sampling model whose parameters were estimated by maximum likelihood is still only the sampling piece.{{cite:gelman_bda2013}} (pp. 6–7){{cite:dodge2008}} (pp. 32–33)

## Assumptions and limits
The factorisation treats the prior as chosen without using the data that later appear in the likelihood. A prior fitted to the same \(y\) that enters \(p(y\mid\theta)\) is a different analysis. Independence of the observations is conditional on \(\theta\); unconditionally, observations that share an unknown parameter are dependent. An improper prior function leaves the joint distribution undefined, and the posterior then needs a separate check that its integral is finite.{{cite:gelman_bda2013}} (pp. 5–7, 51–52)

## Connections
[Exchangeability](exchangeability.qmd) is the judgement that usually justifies the conditionally independent sampling piece. The passage from the joint distribution to \(p(\theta\mid y)\) is [Bayes' rule](bayes-rule.qmd). The whole discipline that builds, conditions, and checks such models is [Bayesian statistics](bayesian-statistics.qmd). The probability assigned to the unknown before the data arrive is an instance of [Bayesian probability](bayesian-probability.qmd).{{cite:gelman_bda2013}} (pp. 5–7, 11)

## History
Bayes's 1763 analysis of an unknown binomial probability used a uniform distribution on that probability as the first piece and the binomial sampling probabilities as the second. Laplace used the same pair, a uniform distribution and a binomial likelihood, for the proportion of girls among births. The two-piece description, a distribution for the parameter and a parametric family for the data, is the form in which the model is stated now.{{cite:gelman_bda2013}} (pp. 29–31){{cite:dodge2008}} (pp. 32–33)
