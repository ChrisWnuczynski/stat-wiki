## Motivating example
A simulation of waiting times, counts or measurements needs random draws with a specified law. Uniform random numbers provide a common starting point, but the transformation must match the desired parameterisation and support. A method that is correct for an exponential rate is different from one that treats the same argument as a scale. Documenting the formula helps expose such mistakes before a simulation is trusted.{{cite:dodge2008}} (pp. 222–223, Generation of Random Numbers)

## Definition — Inversion works for continuous and discrete laws
For a distribution function $F$, the generalised inverse is $F^{-1}(u)=\inf\{x:F(x)\ge u\}$ for $0<u<1$. If $U$ is uniform on that interval, the event $F^{-1}(U)\le x$ is equivalent, up to null boundary cases, to $U\le F(x)$. Hence $\Pr\{F^{-1}(U)\le x\}=F(x)$, proving that the transformed draw has the desired law. Flat or jumping distribution functions do not require an ordinary analytic inverse.{{cite:downey2014_thinkstats2}} (Ch. 5, “Generating random numbers”)

For a finite discrete law, form cumulative masses and return the first outcome whose cumulative probability exceeds the uniform draw. Intervals in the unit interval then have lengths equal to the requested probabilities. For a Bernoulli law this reduces to an indicator comparison with its success probability.{{cite:grinstead_snell1997}} (§1.1, simulation of discrete probabilities)

## Properties — Transformations reveal parameters and support
If $U$ is uniform, $a+(b-a)U$ is uniform on $[a,b]$. For an exponential rate $\lambda>0$, $X=-\log(U)/\lambda$ has survival probability $e^{-\lambda x}$ for $x\ge0$. For a geometric count of trials up to and including the first success, with $0<p<1$, $N=\lfloor\log(U)/\log(1-p)\rfloor+1$ has $\Pr(N>n)=(1-p)^n$ for nonnegative integers $n$. The convention matters: the number of failures before that success is $N-1$.{{cite:grinstead_snell1997}} (§§2.1, 5.1–5.2)

Two independent uniform inputs can also produce two independent standard normal draws through the Box–Muller transformation. A subsequent affine transformation gives a normal location and scale. Independence of the input uniforms is essential; using the same input twice changes the joint distribution even if some marginal expressions look familiar.{{cite:grinstead_snell1997}} (§5.2, p. 213)

## Worked example — Use specified inputs to check a sampler
Take $U=1/4$. A uniform draw on $[2,6]$ is $3$. An exponential draw with rate $2$ is $-\log(1/4)/2=\log2\approx0.693147$. A geometric draw with success probability $1/2$ is $\lfloor\log(1/4)/\log(1/2)\rfloor+1=3$. The last input lies exactly at a cumulative boundary; such boundaries have probability zero for an ideal continuous uniform, although a finite-precision implementation must choose a consistent convention.{{cite:grinstead_snell1997}} (§§2.1, 5.1)

For masses $(1/5,1/2,3/10)$ at outcomes $(0,1,2)$, the cumulative thresholds are $1/5$, $7/10$ and $1$. Thus $U=1/4$ produces outcome $1$, and $U=9/10$ produces outcome $2$. These deterministic input checks are useful complements to distributional simulation checks.{{cite:grinstead_snell1997}} (§1.1)

**Your turn.** With $U=1/4$ and exponential rate $4$, what value does the inverse-transform formula produce?

::: {.callout-tip collapse="true" title="Answer"}
It gives $-\log(1/4)/4=(\log2)/2\approx0.346574$.
:::

## Assumptions and limits — Pseudorandom arithmetic has boundaries
Ideal sampling formulas use independent continuous uniforms. Computers provide finite-precision pseudorandom outputs and can include endpoints that cause logarithms or inverses to overflow. Production implementations should use a well-tested generator and a numerically stable distribution sampler, with the seed and parameter convention recorded. A plausible histogram alone does not prove independence or accurate tail behaviour.{{cite:von_neumann1951_random_digits}} (pp. 36–38, random digits and testing)
