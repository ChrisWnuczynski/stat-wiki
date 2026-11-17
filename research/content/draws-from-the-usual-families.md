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

## Intuition
A uniform random number $U$ on $(0,1)$ is a position along the probability scale. Inversion asks which point on the outcome scale sits at that position in the target distribution function. If $F$ is continuous and strictly increasing, the ordinary inverse $F^{-1}(U)$ has distribution function $F$, because $F^{-1}(U)\le x$ is the same event as $U\le F(x)$, up to endpoints of probability zero. Jumps and flat stretches use the generalised inverse $\inf\{x:F(x)\ge u\}$. The definition looks technical. The picture is the same: read across from $u$ until the distribution function has risen at least that high, and report the outcome there.

Discrete distributions make the picture a partition of the unit interval. Masses $(1/5,1/2,3/10)$ at $(0,1,2)$ have cumulative thresholds $1/5$, $7/10$, and $1$. A draw $U=1/4$ falls between $1/5$ and $7/10$, so the outcome is $1$. A draw $U=9/10$ falls in the last interval, so the outcome is $2$. A draw $U=4/5=0.8$ also falls between $7/10$ and $1$, and the outcome is again $2$. The length of each interval equals the probability of the outcome it labels.

### Properties — Rate, scale, and the geometric convention
An exponential rate $\lambda$ appears in the denominator of the inverse transform $X=-\log(U)/\lambda$. Doubling $\lambda$ halves $X$ for a fixed $U$. With $U=1/4$, the rate-$2$ draw is $-\log(1/4)/2=\log 2\approx 0.693147$, and the rate-$4$ draw is half of that, $(\log 2)/2\approx 0.346574$. A scale parameterisation that multiplies $-\log(U)$ by $\lambda$ runs in the opposite direction. Code that documents the symbol and not the formula can silently turn a rate into a scale. The survival function $e^{-\lambda x}$ is the check: it belongs to the rate parameterisation, and its mean is $1/\lambda$.

The geometric formula $N=\lfloor\log(U)/\log(1-p)\rfloor+1$ counts trials until the first success. With $p=1/2$ and $U=1/4$, $\log(1/4)/\log(1/2)=2$, and the floor expression returns $3$. With $p=1/4$ and $U=1/2$, $\log(1/2)/\log(3/4)\approx 2.409421$, the floor is $2$, and $N=3$. The number of failures before the first success is $N-1$, which is $2$ in both of these draws. A function named at random in a library may return either convention. The survival identity $P(N>n)=(1-p)^n$ identifies the trials-until-success convention. A library that instead returns the failure count satisfies $P(M\ge n)=(1-p)^n$. The two statements differ by one in the random variable.

An affine map $a+(b-a)U$ is uniform on $[a,b]$. With $U=1/4$, $a=2$ and $b=6$ the draw is $3$. The same $U$ is an input, not a sample, in every one of these checks. Reusing one uniform stream for two coordinates of a joint draw, without a transformation that restores independence, produces a curve of outcomes rather than a sample from the product law. Box–Muller uses two independent uniforms to produce two independent standard normals. Feeding it the same uniform twice does not.{{cite:grinstead_snell1997}} (§5.2, p. 213)

## Common misconceptions
A histogram that looks roughly exponential does not identify the rate, and it does not test independence of successive draws. The deterministic checks above are sharper for implementation errors: a rate treated as a scale fails the numerical value $0.693147$ immediately. Tail behaviour needs either a much larger experiment or a direct comparison of the implemented quantile function with the formula. Pseudorandom generators also have a finite state. A short simulation will not reveal the period. Recording the generator, the seed, and the parameter convention makes a later disagreement diagnosable.

Exact ties at a cumulative boundary have probability zero for a continuous uniform and probability one for some floating-point values. The worked geometric draw with $U=1/4$ and $p=1/2$ lands on the boundary $\log(1/4)/\log(1/2)=2$. The floor convention has to be applied consistently. Switching to a strict inequality in the discrete inversion moves that single point into a neighbouring bin and does not change the distribution of an ideal continuous $U$. It can change a unit test that uses that exact input.

## Connections
Acceptance–rejection is the alternative when the quantile function is unavailable and an envelope is. Inversion is exact in exact arithmetic and uses one uniform per draw, apart from the cost of evaluating the quantile. The families treated here, uniform, exponential, geometric, Bernoulli, and normal via Box–Muller, all have explicit transformations. A gamma draw with a noninteger shape, or a normal draw in a library routine, may use rejection internally. The user's responsibility is then the parameterisation the library expects and the independence of the calls. The mathematical responsibility of the formula is the distributional identity, which the unit-interval argument proves once and which the numerical checks above instantiate.
