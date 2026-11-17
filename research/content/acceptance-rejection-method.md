## Motivating example
A simulation may need values from a density whose cumulative distribution is difficult to invert. Suppose evaluating the density is easy and a familiar proposal distribution covers its support. Acceptance–rejection turns those proposal draws into draws from the desired law by accepting them at a location-dependent rate. The accepted draws favour locations where the target is high relative to the proposal; rejected proposals consume computation but contribute no output value.{{cite:von_neumann1951_random_digits}} (pp. 37–38, nonuniform sampling)

## Definition — The envelope must dominate everywhere
Let $f$ and $g$ be probability densities with respect to the same measure. Assume $f(x)\le M g(x)$ almost everywhere for a finite $M$. Generate independent proposals $X\sim g$ and uniforms $U\sim\mathrm{Uniform}(0,1)$, accepting if $U\le f(X)/(Mg(X))$. Repeat until acceptance. The support condition is indispensable: a proposal that assigns zero density where the target has positive mass cannot generate that part of the target. The bound must be a genuine upper bound, rather than the largest ratio encountered in a short simulation.{{cite:von_neumann1951_random_digits}} (p. 37)

## Properties — Why rejection gives the right law
For any measurable set $A$, the probability of both acceptance and a proposal in $A$ is
$$\int_A g(x)\frac{f(x)}{M g(x)}\,dx=\frac1M\int_A f(x)\,dx.$$
Taking $A$ to be the full support gives acceptance probability $1/M$. Dividing by that probability shows that the conditional distribution of an accepted proposal has density $f$. Independence of proposal pairs makes successive output draws independent. The proof also shows why an acceptance probability above one signals an invalid envelope; replacing it by one generally changes the output distribution.{{cite:von_neumann1951_random_digits}} (p. 37, rejection construction)

If $N$ counts proposals including the accepted one, $\Pr(N=n)=(1-1/M)^{n-1}/M$. Its mean is $M$ and its variance is $M(M-1)$. Summing the geometric series and its derivatives proves both moment formulas. The acceptance event therefore controls computational cost as well as correctness. A proposal with heavier tails can make the bound finite, while a tighter envelope reduces expected work.{{cite:grinstead_snell1997}} (§5.1, geometric distribution; §6.1, geometric waiting time)

## Worked example — A beta density under a rectangle
For $f(x)=6x(1-x)$ on the unit interval and uniform proposal $g(x)=1$, completing the square gives $f(x)=3/2-6(x-1/2)^2$. Hence $M=3/2$ is valid and tight. The acceptance probability is $2/3$, the expected number of proposals is $3/2$, and its variance is $3/4$. If every proposal uses one uniform for $X$ and another for the acceptance decision, the expected count is three uniforms per output. The rectangle construction agrees with the conditional-density derivation.{{cite:von_neumann1951_random_digits}} (p. 37)

A particular proposal $X=1/4$ has acceptance threshold $3/4$. Thus a uniform value $U=1/2$ accepts it, while $U=9/10$ rejects it. The first decision does not mean that one quarter is an especially likely exact output: a continuous distribution assigns zero probability to any exact point. It describes the conditional acceptance probability at that proposed coordinate.{{cite:grinstead_snell1997}} (§2.2, densities and interval probabilities)

**Your turn.** Keep the same target and uniform proposal, but use the looser bound $M=2$. What are the acceptance probability and expected uniforms per output?

::: {.callout-tip collapse="true" title="Answer"}
The acceptance probability is $1/2$ and the expected number of proposals is two. Two uniforms per proposal give four uniforms per output.
:::

## Assumptions and limits — Tail control comes before tuning
For an unnormalised target $h$, a known bound $h\le Cg$ is enough to implement the acceptance decision. Its acceptance probability becomes $Z/C$, where $Z=\int h$; the sampler need not know $Z$, although a finite positive $Z$ is needed for a target probability law. Multiplying many one-dimensional envelopes in a high-dimensional problem can make the total acceptance probability very small. This concerns efficiency, whereas using an invalid envelope concerns the probability law itself. A transformation method is often preferable when a tractable inverse distribution function is available.{{cite:downey2014_thinkstats2}} (Ch. 5, “Generating random numbers”)
