## Lead context

A Bayesian model is a joint probability specification for the observations and the unknowns. It states what the data would do if the unknowns were fixed, and it states a distribution for the unknowns before those data are used. Anything called a posterior is computed from that joint distribution. It is a result, not a third ingredient that has to be written down separately.{{cite:gelman_bda2013}} (pp. 6–7)

## Motivating example

A coin lands heads or tails once. Two explanations are on the table: the heads probability is $0.2$, or it is $0.8$, and before the toss those two explanations are equally serious. The model is the pair of explanations together with the chance of heads under each of them. The single toss has not yet been seen, so the model is a distribution over explanations and outcomes together, not yet a statement about which explanation the toss will favour. The sampling piece is a Bernoulli trial. The prior piece is the weight $1/2$ on each explanation. Dodge describes those two choices, a parametric family for the data and an initial distribution for the parameter, as the modelling steps a Bayesian procedure takes as given.{{cite:gelman_bda2013}} (pp. 6–7){{cite:dodge2008}} (p. 33)

## Definition

Let $y$ be the observations and $\theta$ the unknowns. The model is a joint distribution that factors as

$$
p(\theta,y)=p(\theta)\,p(y\mid\theta).
$$


Here $p(\theta)$ is the prior and $p(y\mid\theta)$ is the sampling distribution, also called the data distribution. When $y$ is held at the observed value and the product is read as a function of $\theta$, the sampling factor is the likelihood. A model for several exchangeable observations often takes those observations as independent given $\theta$, with a common distribution $p(y_i\mid\theta)$. Explanatory variables that are conditioned on, and not modelled as random, may sit inside that sampling distribution.{{cite:gelman_bda2013}} (pp. 5–7)

Writing the model is the first of the three parts of a Bayesian analysis. The joint distribution has to be consistent with what is known about the scientific problem and about the way the data were collected. Specifying a parametric family $f(x\mid\theta)$ for the observations, and specifying a distribution $f(\theta)$ for its parameter, are the two modelling choices Dodge lists before Bayes' theorem is applied.{{cite:dodge2008}} (p. 33){{cite:gelman_bda2013}} (p. 3, §1.1)

## Properties

The joint distribution determines the marginal distribution of the data,

$$
p(y)=\int p(\theta)\,p(y\mid\theta)\,d\theta,
$$


and the posterior $p(\theta\mid y)=p(\theta)\,p(y\mid\theta)/p(y)$ wherever that marginal is positive and finite. Changing the prior changes the joint distribution even when the sampling distribution is held fixed, and so it changes the posterior. A prior that integrates to one, and does not depend on $y$, is a probability distribution for the unknown. A function of $\theta$ with an infinite integral does not complete a joint probability model.{{cite:gelman_bda2013}} (p. 7)

If the same experimental conditions are judged exchangeable, the joint distribution of the observations is invariant to permuting their labels. The independent-and-identical sampling model given $\theta$ is the usual way of writing that judgement. A hierarchical model adds a further distribution for the parameters of the prior, so that several related groups share a model while keeping their own parameters. The posterior and the posterior predictive distribution are functionals of the joint model. They are not extra pieces supplied from outside it.{{cite:gelman_bda2013}} (pp. 5–7)

For the two-point coin, the joint probabilities of a success are

$$
\mathbb{P}(\theta=0.2,\, y=1)=\tfrac12\cdot 0.2=0.1, \qquad \mathbb{P}(\theta=0.8,\, y=1)=\tfrac12\cdot 0.8=0.4.
$$


They sum to $\mathbb{P}(y=1)=0.5$. The posterior probabilities are $0.1/0.5=1/5$ and $0.4/0.5=4/5$. The division uses the marginal probability of the data. It is not part of writing the joint distribution down.{{cite:gelman_bda2013}} (pp. 6–7)

## Worked example

Take $\theta\in\{0.2,0.8\}$ with prior probability $1/2$ each, and let $y$ be a single Bernoulli trial with success probability $\theta$. The model assigns the joint probabilities $0.1$ and $0.4$ to a success under the two explanations, as above. Those two numbers are the model at the observed success.

**Your turn.** Under the same model, the trial is a failure, $y=0$. Find the joint probability of $\{\theta=0.2,\, y=0\}$ and the posterior probability of $\theta=0.2$.

::: {.callout-tip collapse="true" title="Answer"}
The joint probability is $(1/2)\cdot 0.8=0.4$. The marginal probability of failure is $0.4+0.1=0.5$, so the posterior probability of $\theta=0.2$ is $0.4/0.5=0.8$.
:::

## Assumptions and limits

The factorisation treats the prior as chosen without using the data that later appear in the likelihood. A prior fitted to the same $y$ that enters $p(y\mid\theta)$ is a different analysis from the one the factorisation describes. Independence of the observations is conditional on $\theta$. Unconditionally, observations that share an unknown parameter are dependent, because they inform the same $\theta$.{{cite:gelman_bda2013}} (pp. 5–7)

An improper prior function, one whose integral diverges, leaves the joint distribution undefined as a probability distribution. The formal product with the likelihood can still be studied, and it yields a posterior only when that product has a finite integral in $\theta$. Dodge's account of the initial distribution assumes a distribution function $f(\theta)$, which is a probability distribution, before the posterior is calculated. A likelihood, by itself, is not this model: it lacks a distribution for the unknown. A prior, by itself, is not this model: it lacks a distribution for the data.{{cite:gelman_bda2013}} (p. 7){{cite:dodge2008}} (p. 33)

## History

Bayes's 1763 analysis of an unknown binomial probability used a uniform distribution on that probability as the first piece and the binomial sampling probabilities as the second. Laplace used a distribution for an unknown proportion together with a sampling model for the observed count. Dodge places that pair, an initial distribution and a parametric family, at the start of the procedure, and dates the wider inferential tradition to Bayes (1763), de Moivre (1718), Gauss (1809), and Laplace (1812). The two-piece description, a distribution for the parameter and a parametric family for the data, is the form in which the model is stated now.{{cite:gelman_bda2013}} (p. 3, §1.1){{cite:dodge2008}} (pp. 32–33, 263)
