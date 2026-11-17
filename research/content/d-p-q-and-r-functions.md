## Motivating example
A count of three successes prompts several different questions: the probability of exactly three, the probability of at most three, a cutoff leaving 90% of counts below it, or a simulated sample of counts. These questions use a mass function, distribution function, quantile function and random generator respectively. R assigns a common naming convention to them.

## Definition
For any real random variable, the cumulative distribution function is $F(x)=P(X\le x)$. For a discrete variable, the mass at $x$ is $P(X=x)$; for a continuous density, the mass at one point is zero and interval probabilities come from integration. A density can exceed one because its units are reciprocal measurement units. Probability is an area or a summed mass, not a density height.{{cite:grinstead_snell1997}} (§2.2, continuous density functions)

## Properties — Inverse probabilities need an inequality
For $0<u<1$, define a quantile as $q(u)=\inf\{x:F(x)\ge u\}$. When $F$ is continuous and strictly increasing, $F(q(u))=u$. A discrete CDF has jumps, so equality need not hold: $F(q(u))$ can be greater than $u$. R's binomial quantile uses the smallest integer reaching the requested cumulative probability.

The identity $P(a<X\le b)=F(b)-F(a)$ follows because $\{X\le b\}$ is the disjoint union of $\{X\le a\}$ and $\{a<X\le b\}$. For integer-valued $X$, an inclusive lower bound needs the previous integer: $P(a\le X\le b)=F(b)-F(a-1)$. This is why `pbinom(5,10,0.4)-pbinom(2,10,0.4)` covers counts three through five.{{cite:openintro2019}} (§4.3.1, binomial probability model)

## Worked example — A binomial lookup chain
For $X\sim\operatorname{Bin}(10,0.4)$, direct summation gives $P(X=3)=0.21499$ and $P(X\le3)=0.38228$. The 90th percentile is 6: $P(X\le5)=0.83376<0.9$, while $P(X\le6)=0.94524\ge0.9$. These values distinguish mass, accumulated mass and a count-valued quantile. The binomial formula follows from counting which trials succeed and multiplying their independent probabilities.{{cite:openintro2019}} (§4.3.1)

**Your turn.** For a fair die, find the mass at 4, the CDF at 4, and the 75th percentile under the smallest-value convention.

::: {.callout-tip collapse="true" title="Answer"}
The mass is $1/6$, the cumulative probability is $4/6=2/3$, and the 75th percentile is 5, because $4/6<0.75\le5/6$.
:::

## Statistical use — Simulation and parameterization
Simulation approximates a distribution by repeated draws from a specified model. It can check a tail probability, but its Monte Carlo error must be distinguished from the model probability. The binomial output length is set by the first argument to `rbinom`; its `size` argument sets trials per draw. A seed controls the pseudorandom sequence and supports reproducibility within a specified generator configuration. These are software behaviors rather than probabilistic definitions.

For a gamma variable, rate $\lambda$ and scale $1/\lambda$ describe the same law. Mean equals shape divided by rate. A named argument is useful when distributions use several parameterizations. For a normal variable R's `sd` is a standard deviation, while the mathematical notation $N(\mu,\sigma^2)$ uses a variance in its second slot. Confusing these slots can yield plausible but incorrect answers.{{cite:grinstead_snell1997}} (§5.2, normal and gamma densities)

## Lead context
The four letters name four questions one can ask of the same distribution. A density or mass function gives the height at a point. A distribution function gives the probability at or below a point. A quantile function inverts that distribution function. A random-number generator draws values. For a discrete distribution the inverse is a step: the smallest integer whose distribution function is at least the requested probability. For a continuous distribution the inverse is usually one-to-one on the interior of the range.

## Intuition
For $\mathrm{Binomial}(10,0.4)$, the mass at $3$ is about $0.21499$ and the distribution function at $3$ is about $0.38228$. The $0.90$ quantile is $6$, because the distribution function at $5$ is about $0.83376$ and at $6$ is about $0.94524$. Asking for the probability of the values $3,4,5$ is the difference of distribution functions at $5$ and at $2$, not the mass at $5$ minus the mass at $2$. A standard normal density at zero is about $0.399$, and the $0.975$ quantile is about $1.96$. Those two numbers answer different questions: one is a height and one is a point on the axis.{{cite:openintro2019}} (§4.3.1, binomial probability model)

## Interpretation
A gamma law with shape $3$ and rate $2$ has mean $3/2$ and variance $3/4$. The same law has scale $1/2$, because the rate is the reciprocal of the scale. An exponential law of rate $2$ is the gamma law with shape $1$ and that rate. Its density at zero is $2$, its distribution function at $1$ is $1-e^{-2}\approx 0.8647$, and its median is $-\log(0.5)/2\approx 0.3466$. A fair die has mass $1/6$ at each face. Its distribution function at $4$ is $4/6=2/3$, and its $0.75$ quantile is $5$, because the distribution function first reaches $0.75$ at $5$. Software that asks for a lower-tail probability and software that asks for an upper-tail probability are reading the same distribution function from opposite ends.{{cite:grinstead_snell1997}} (§5.2, normal and gamma densities)

## Common misconceptions
A density value is not a probability. The standard normal density can be about $0.399$ at zero, and the probability of any single point is zero. A mass function does give probabilities, so the binomial mass $0.21499$ can be read as a probability and the normal density cannot. A second confusion is to treat the quantile function of a discrete law as if it were continuous. There is no integer whose binomial distribution function equals $0.90$ exactly in the example above. The quantile returns $6$ because that is the first integer at which the distribution function has crossed $0.90$. A third confusion is to mix the random-number generator with the quantile function. One draw from the generator is a random outcome. The quantile of a fixed probability is a constant.{{cite:grinstead_snell1997}} (§2.2, continuous density functions)

## Assumptions and limits
The four functions are four questions about one law, and the parameterisation has to be the one the function expects. A gamma law with shape $3$ and rate $2$ has mean $3/2$ and variance $3/4$. The same law has scale $1/2$, the reciprocal of the rate. An exponential law of rate $2$ is that gamma law with shape $1$. Its density at zero is $2$, its distribution function at $1$ is $1-e^{-2}\approx 0.8647$, and its median is $-\log(0.5)/2\approx 0.3466$. Feeding the rate into a scale argument, or the scale into a rate argument, answers a different law.

A discrete quantile has an inequality built in. For the binomial example the distribution function at $5$ is about $0.83376$ and at $6$ is about $0.94524$, so the $0.90$ quantile is $6$. There is no integer whose distribution function equals $0.90$ exactly. A density height is not a probability: the standard normal density at zero is about $0.399$, while the probability of any single point is zero. A random draw and a quantile are different objects as well. One is an outcome of the generator. The other is a fixed point on the axis for a stated probability.{{cite:grinstead_snell1997}} (§5.2, normal and gamma densities)
