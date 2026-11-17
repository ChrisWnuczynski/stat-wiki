## Motivating example
A count of three successes prompts several different questions: the probability of exactly three, the probability of at most three, a cutoff leaving 90% of counts below it, or a simulated sample of counts. These questions use a mass function, distribution function, quantile function and random generator respectively. R assigns a common naming convention to them.{{cite:r_stats_distributions2026}} (“Details”)

## Definition
For any real random variable, the cumulative distribution function is $F(x)=P(X\le x)$. For a discrete variable, the mass at $x$ is $P(X=x)$; for a continuous density, the mass at one point is zero and interval probabilities come from integration. A density can exceed one because its units are reciprocal measurement units. Probability is an area or a summed mass, not a density height.{{cite:grinstead_snell1997}} (§2.2, continuous density functions)

## Properties — Inverse probabilities need an inequality
For $0<u<1$, define a quantile as $q(u)=\inf\{x:F(x)\ge u\}$. When $F$ is continuous and strictly increasing, $F(q(u))=u$. A discrete CDF has jumps, so equality need not hold: $F(q(u))$ can be greater than $u$. R's binomial quantile uses the smallest integer reaching the requested cumulative probability.{{cite:r_stats_distributions2026}} (“Details”, distribution-function families)

The identity $P(a<X\le b)=F(b)-F(a)$ follows because $\{X\le b\}$ is the disjoint union of $\{X\le a\}$ and $\{a<X\le b\}$. For integer-valued $X$, an inclusive lower bound needs the previous integer: $P(a\le X\le b)=F(b)-F(a-1)$. This is why `pbinom(5,10,0.4)-pbinom(2,10,0.4)` covers counts three through five.{{cite:openintro2019}} (§4.3.1, binomial probability model)

## Worked example — A binomial lookup chain
For $X\sim\operatorname{Bin}(10,0.4)$, direct summation gives $P(X=3)=0.21499$ and $P(X\le3)=0.38228$. The 90th percentile is 6: $P(X\le5)=0.83376<0.9$, while $P(X\le6)=0.94524\ge0.9$. These values distinguish mass, accumulated mass and a count-valued quantile. The binomial formula follows from counting which trials succeed and multiplying their independent probabilities.{{cite:openintro2019}} (§4.3.1)

**Your turn.** For a fair die, find the mass at 4, the CDF at 4, and the 75th percentile under the smallest-value convention.

::: {.callout-tip collapse="true" title="Answer"}
The mass is $1/6$, the cumulative probability is $4/6=2/3$, and the 75th percentile is 5, because $4/6<0.75\le5/6$.
:::

## Statistical use — Simulation and parameterization
Simulation approximates a distribution by repeated draws from a specified model. It can check a tail probability, but its Monte Carlo error must be distinguished from the model probability. The binomial output length is set by the first argument to `rbinom`; its `size` argument sets trials per draw. A seed controls the pseudorandom sequence and supports reproducibility within a specified generator configuration. These are software behaviors rather than probabilistic definitions.{{cite:r_stats_distributions2026}} (“Details” and “See Also”, random number generation)

For a gamma variable, rate $\lambda$ and scale $1/\lambda$ describe the same law. Mean equals shape divided by rate. A named argument is useful when distributions use several parameterizations. For a normal variable R's `sd` is a standard deviation, while the mathematical notation $N(\mu,\sigma^2)$ uses a variance in its second slot. Confusing these slots can yield plausible but incorrect answers.{{cite:grinstead_snell1997}} (§5.2, normal and gamma densities)
