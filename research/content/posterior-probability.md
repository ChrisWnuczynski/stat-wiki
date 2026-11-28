## Lead context
A posterior probability is the probability of a set of parameter values after the data have been taken into account.

It is computed from a prior distribution and a sampling model, not from the sample alone. A [posterior hypothesis probability](posterior-hypothesis-probability.qmd) is that probability when the set is the region a named hypothesis picks out, such as "the heads probability is at most one half." The integral is the same kind of object. The report is not: one number is the mass of whatever set is asked for, and the other is the mass attached to a hypothesis that has been named in advance. The distribution that supplies both, and the arithmetic that turns a prior and a likelihood into a probability, are the subject here. The comparison of a named hypothesis with a $p$-value, and the decision that uses a loss, belong with the hypothesis probability.{{cite:gelman_bda2013}} (pp. 7–8)

## Motivating example
Two explanations of a binary outcome are open: explanation $A$ with prior probability $1/4$, and explanation $B$ with prior probability $3/4$. The observed sample has probability $1/2$ under $A$ and probability $1/6$ under $B$. The question the posterior answers is how probable the set $\{A\}$ is once that sample has been seen. The prior probabilities and the two sampling probabilities are the ingredients. Neither ingredient is already the answer, and neither is a hypothesis probability until someone names $A$ or $B$ as the hypothesis under test.{{cite:gelman_bda2013}} (pp. 7–8)

## Definition
For a discrete unknown $\theta$ and observed data $y$,

$$
\mathbb{P}(\theta=\theta_j\mid y)
=\frac{p(y\mid\theta_j)\,\mathbb{P}(\theta=\theta_j)}{\sum_i p(y\mid\theta_i)\,\mathbb{P}(\theta=\theta_i)},
$$


provided the denominator is positive. For a continuous parameter with prior density $p(\theta)$ and sampling density $p(y\mid\theta)$, the posterior density is

$$
p(\theta\mid y)=\frac{p(\theta)\,p(y\mid\theta)}{p(y)},
\qquad
p(y)=\int p(\theta)\,p(y\mid\theta)\,d\theta.
$$


The posterior probability of a set $A$ of parameter values is the integral of that density over $A$, or the sum of the point masses in $A$. The whole function $p(\theta\mid y)$ is the posterior distribution. A posterior probability is the mass it assigns to a specified set. When that set is the region named by a hypothesis, the mass is a [posterior hypothesis probability](posterior-hypothesis-probability.qmd). The set can also be an interval chosen to hold a stated mass, or a single point of a discrete parameter.{{cite:gelman_bda2013}} (p. 7){{cite:dodge2008}} (p. 33)

In the carrier calculation, the set has one point, "she is a carrier." The prior probability is $1/2$. Two unaffected sons have likelihood $1/4$ if she is a carrier and likelihood $1$ if she is not. The posterior probability of that point is

$$
\frac{(1/4)\cdot(1/2)}{(1/4)\cdot(1/2)+1\cdot(1/2)}=\frac{1}{5}=0.2.
$$


That number is the posterior probability of one point in a two-point parameter. It is not, by itself, a test of a scientific hypothesis about haemophilia beyond the model that was written down.{{cite:gelman_bda2013}} (p. 9)

## Properties
The ratio of two posterior probabilities equals the prior odds times the likelihood ratio. The marginal probability of the data cancels, so

$$
\frac{\mathbb{P}(\theta=\theta_1\mid y)}{\mathbb{P}(\theta=\theta_2\mid y)}
=\frac{\mathbb{P}(\theta=\theta_1)}{\mathbb{P}(\theta=\theta_2)}\cdot\frac{p(y\mid\theta_1)}{p(y\mid\theta_2)}.
$$


If the prior probability of a region is zero, the posterior probability of that region remains zero whenever the posterior is defined. Multiplying by a likelihood cannot create mass outside the prior's support.{{cite:gelman_bda2013}} (pp. 7–8)

A continuous posterior assigns probability zero to any single point, even at a point where the density is positive. The probability of a set with positive length can still be large. An equal-tailed posterior interval chooses its endpoints so that the tails hold a stated mass. A fixed region such as $\{\theta\le 1/2\}$ does the opposite: the region is chosen first and the mass is read off. Those two summaries answer different questions, and only the second is a hypothesis probability.{{cite:gelman_bda2013}} (pp. 7–8){{cite:dodge2008}} (p. 33)

## Worked example
Prior probabilities are $\mathbb{P}(A)=1/4$ and $\mathbb{P}(B)=3/4$. The sampling probabilities of the observed sample are $1/2$ under $A$ and $1/6$ under $B$. The unnormalised weights are

$$
\tfrac14\cdot\tfrac12=\tfrac18, \qquad \tfrac34\cdot\tfrac16=\tfrac18.
$$


The marginal probability of the sample is $1/8+1/8=1/4$. The posterior probability of $A$ is $(1/8)/(1/4)=1/2$. The likelihood ratio in favour of $A$ is $(1/2)/(1/6)=3$, and the prior odds of $A$ against $B$ are $(1/4)/(3/4)=1/3$, so the posterior odds are $1$, which is the same probability $1/2$. The data have moved the probability of $\{A\}$ from $1/4$ to $1/2$. Naming $A$ as a hypothesis would then call $1/2$ a posterior hypothesis probability. Without that naming, $1/2$ is only the posterior probability of the set.{{cite:gelman_bda2013}} (pp. 7–8)

**Your turn.** Keep the sampling probabilities $1/2$ and $1/6$, and replace the prior by $\mathbb{P}(A)=\mathbb{P}(B)=1/2$. What is the posterior probability of $A$?

::: {.callout-tip collapse="true" title="Answer"}
The unnormalised weights are $(1/2)\cdot(1/2)=1/4$ and $(1/2)\cdot(1/6)=1/12$. Their sum is $1/3$, so the posterior probability of $A$ is $(1/4)/(1/3)=3/4$.
:::

## Assumptions and limits
The denominator must be positive and finite. If the prior is an improper function, there is no prior probability to start from, and a posterior probability is available only after the product of that function and the likelihood has been checked to have a finite integral. The numerical value depends on the whole prior, not only on the maximum of the likelihood. A posterior probability computed under one model is conditional on that model. A dispute about the number is a dispute about the prior, the sampling model, or both.{{cite:gelman_bda2013}} (pp. 7–8){{cite:dodge2008}} (p. 31)

The carrier probability $1/5$ used the likelihoods $1/4$ and $1$, and it ignored mutation. A different sampling story for the sons produces a different posterior probability of the same point. The arithmetic does not supply the story.{{cite:gelman_bda2013}} (p. 9)

## History
Bayes's 1763 essay asked for the probability that an unknown chance lies between two bounds, given the number of successes in a fixed number of trials. That is a posterior probability for an interval of the unknown. The continuous form used now writes the posterior density as the prior density times the likelihood, divided by the marginal probability of the data. Once that density is in hand, a mean, a median, an interval, or the probability of a named region can be computed from it. The probability of a named region is the hypothesis probability. The interval probability Bayes asked for is the set probability, whether or not anyone has called the interval a hypothesis.{{cite:dodge2008}} (pp. 31, 33){{cite:gelman_bda2013}} (p. 7)
