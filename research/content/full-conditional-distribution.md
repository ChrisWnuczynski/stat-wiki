## Lead context
It makes a joint posterior usable one coordinate at a time: hold the other parameter values fixed, derive a distribution for the remaining coordinate, and draw from it. This is the step that connects a posterior model to a Gibbs sampler when direct joint sampling is difficult.{{cite:gelfand_smith1990}} (§§1, 2.3, pp. 398–401){{cite:geyer2005_markov_chain}} (§§10.1, 10.5, pp. 27–29)

## Motivating example
In a model with an unknown mean and variance, the posterior couples the two parameters. Fixing the variance leaves a normal distribution for the mean; fixing the mean leaves a gamma distribution for the precision, or equivalently an inverse-gamma distribution for the variance. Sampling those easier conditional laws alternately builds draws from the joint posterior.{{cite:geyer2005_markov_chain}} (§10.6, pp. 29–30)

## Definition
Let $Y=y$ denote observed data and $X=(X_1,\ldots,X_p)$ a random vector of parameters with posterior density $\pi(x_1,\ldots,x_p\mid y)$. The **full conditional** of coordinate $j$ conditions on every other coordinate $X_{-j}$ as well as on $y$. For a realised vector $x_{-j}$ whose posterior marginal density is positive, it is
$$
\pi(x_j\mid x_{-j},y)=\frac{\pi(x_j,x_{-j}\mid y)}{\int\pi(u,x_{-j}\mid y)\,\mathrm du},
$$
where $u$ ranges over possible values of $X_j$ and the denominator normalises the density in $x_j$. For a discrete coordinate, replace the integral by a sum. If the joint posterior is known only up to a positive constant, that constant cancels between numerator and denominator.{{cite:gelfand_smith1990}} (§2, pp. 398–400){{cite:geyer2005_markov_chain}} (§§10.1, 10.6, pp. 27–29)

At a given Gibbs step, the values of $x_{-j}$ are the most recent values of the other coordinates, not a fresh sample from their separate marginal distributions. Thus the order shown above uses the updated $X_1^{(t+1)}$ when drawing $X_2^{(t+1)}$. A complete sweep changes every coordinate once; the full conditional is the distribution used for just one of those changes.{{cite:geman_geman1984}} (§XI, pp. 731–733){{cite:gelfand_smith1990}} (§2.3, pp. 400–401)

## Interpretation
The conditioning bar changes the question. $\pi(x_j\mid y)$ averages over uncertainty in the other parameters, whereas $\pi(x_j\mid x_{-j},y)$ fixes their values. A full conditional can be a familiar distribution even when the marginal posterior of $X_j$ requires integration that cannot be done in closed form. A value at a conditioning point with zero posterior marginal density is not fixed by the quotient; the Gibbs chain must be specified on a state space where its updates are defined.{{cite:gelfand_smith1990}} (§§1–2.3, pp. 398–401){{cite:geyer2005_markov_chain}} (§10.6, pp. 29–30)

## Properties
The denominator in the definition makes each full conditional integrate or sum to one. Any factor in the joint posterior that depends only on $x_{-j}$ or on the observed data cancels, while a factor involving $x_j$ must remain. This is the practical rule for deriving a Gibbs update from a posterior kernel.{{cite:geyer2005_markov_chain}} (§10.6, p. 29)

Drawing one coordinate from its exact full conditional leaves the joint posterior invariant. A sweep composed of such coordinate updates also leaves it invariant, regardless of the chosen fixed order. For a finite product state space on which the joint mass is strictly positive, the systematic-scan chain can reach every state in a sweep and converges to that posterior from any starting state. The positive finite-state assumption gives the needed irreducibility and aperiodicity; general continuous-state convergence needs its own conditions.{{cite:geman_geman1984}} (§XII, Theorem A, p. 733){{cite:geyer2005_markov_chain}} (§§10.4–10.5, pp. 28–29)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Fix $x_{-j}$ with a positive denominator. Dividing the joint density by its integral over $u$ gives a density whose integral over $x_j$ is one. If the joint density is $c h(x_j,x_{-j})$ for constant $c>0$, the same factor $c$ appears in the integral and cancels. A factor depending only on $x_{-j}$ cancels in exactly the same way.{{cite:geyer2005_markov_chain}} (§10.6, p. 29)

For the invariant-distribution claim, suppose the current vector has joint law $\pi$. Its unchanged coordinates then have marginal law $\pi_{-j}$. Replacing coordinate $j$ from $\pi(\cdot\mid x_{-j})$ produces joint law $\pi_{-j}(x_{-j})\pi(x_j\mid x_{-j})=\pi(x_j,x_{-j})$. Applying this identity successively proves invariance of the full sweep. In a finite product state space with positive mass at every state, each required conditional probability is positive. Following any prescribed coordinate order therefore gives a positive one-sweep probability from any starting state to any target state, including a self-transition. The sweep chain is irreducible and aperiodic; the finite-state convergence theorem then gives convergence to its invariant law $\pi$.{{cite:geman_geman1984}} (§XII, Theorem A, p. 733){{cite:geyer2005_markov_chain}} (§§10.4–10.5, pp. 28–29)
:::
:::

## Statistical use
For a normal mean and variance with independent priors, derive each update by holding the other parameter fixed in the joint posterior kernel. The mean update is normal and the precision update is gamma. The [normal-model derivation](../notes/bayes-03-normal-models.qmd#s-both-normal-parameters-unknown) writes the same construction using variance and its inverse-gamma update. Posterior averages can then be approximated from repeated Gibbs sweeps, with dependence between successive draws taken into account when assessing simulation error.{{cite:geyer2005_markov_chain}} (§10.6, pp. 29–30){{cite:gelfand_smith1990}} (§§1, 2.3, pp. 398–401)

Before using a collection of separately supplied conditional models, check that they arise from a common joint distribution. When they are incompatible, changing the scan order can change the limiting distribution of the resulting sampler. A derivation from one proper joint posterior supplies compatibility by construction.{{cite:chen_ip2015}} (Abstract; §§1, 3, pp. 3266–3271)

## Worked example
Suppose a joint posterior for binary parameters $X$ and $Z$, after observing fixed data $y$, has masses $\pi(0,0\mid y)=2/5$, $\pi(0,1\mid y)=1/10$, $\pi(1,0\mid y)=1/5$ and $\pi(1,1\mid y)=3/10$. The four masses sum to one. Holding $Z=0$ gives $\Pr(X=0\mid Z=0,y)=(2/5)/(3/5)=2/3$ and $\Pr(X=1\mid Z=0,y)=1/3$. Holding $X=0$ gives $\Pr(Z=1\mid X=0,y)=(1/10)/(1/2)=1/5$. Starting a sweep at $(X,Z)=(1,0)$ and updating $X$ then $Z$, the chance of reaching $(0,1)$ in that sweep is $(2/3)(1/5)=2/15$. That transition probability conditions on the starting state; the posterior mass of $(0,1)$ is $\pi(0,1\mid y)=1/10$.{{cite:gelfand_smith1990}} (§2.3, pp. 400–401){{cite:geyer2005_markov_chain}} (§§10.1, 10.4, pp. 27–28)

**Your turn.** For the same four-cell posterior, find $\Pr(Z=1\mid X=1,y)$. Starting at $(1,0)$ and updating $X$ then $Z$, what is the chance of reaching $(1,1)$ in one sweep?

::: {.callout-tip collapse="true" title="Answer"}
The first probability is $(3/10)/(1/5+3/10)=3/5$. The $X$ update retains $X=1$ with probability $(1/5)/(3/5)=1/3$ while $Z=0$; the subsequent $Z$ update selects $1$ with probability $3/5$. The transition probability is $(1/3)(3/5)=1/5$.
:::

## Assumptions and limits
The displayed density quotient requires a positive, finite marginal density at the fixed conditioning value. For continuous parameters it is defined only up to choices on marginal-null sets. A Gibbs update also requires a way to sample from its full conditional; recognizing a kernel without an available sampler does not by itself produce a draw. On a finite state space, strictly positive joint mass gives the convergence result proved above. If conditionals are specified separately rather than derived from one joint law, their compatibility needs checking.{{cite:geyer2005_markov_chain}} (§§10.1, 10.6, pp. 27–30){{cite:chen_ip2015}} (§1, pp. 3266–3268)

## Connections
A [conditional distribution](conditional-distribution.qmd) conditions one variable on another; a full conditional is the special case conditioning one parameter on *all* the other parameters and the data. A [joint density](joint-probability-density.qmd) supplies its numerator, while the corresponding marginal supplies its normalising denominator. [Gibbs sampling](gibbs-sampling.qmd) chains these exact conditional draws; a [systematic-scan Gibbs sampler](systematic-scan-gibbs-sampler.qmd) fixes their order. [Metropolis–Hastings](metropolis-hastings-algorithm.qmd) instead proposes a move and may reject it. [Block Gibbs sampling](../notes/bayes-04-mcmc.qmd#s-gibbs-sampling) updates several coordinates jointly when their block conditional can be sampled.{{cite:geman_geman1984}} (§XI, pp. 731–733){{cite:gelfand_smith1990}} (§2.3, pp. 400–401){{cite:geyer2005_markov_chain}} (§§9–10.2, pp. 25–28)

## History
Stuart and Donald Geman's 1984 image-restoration paper used local conditional draws to update pixels and edge variables in a Markov random field. Its Gibbs sampler avoided computing the normalising constant of the full image distribution at each local update. The paper proved convergence for repeated site visits in its finite positive-state setting.{{cite:geman_geman1984}} (§§I, XI–XII, pp. 721–723, 731–733)

Gelfand and Smith's 1990 paper brought the same conditional-sampling idea to Bayesian marginal calculations in missing-data, hierarchical and normal models. It described how full conditionals could make simulation possible when direct evaluation of the marginals was difficult. Later work by Chen and Ip examined conditional models specified separately and showed that incompatible conditionals can make scan order affect the sampler's limit.{{cite:gelfand_smith1990}} (§§1–3, pp. 398–404){{cite:chen_ip2015}} (Abstract; §§1, 3, pp. 3266–3271)
