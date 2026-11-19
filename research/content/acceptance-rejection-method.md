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

**A further exercise.** For the beta target with the tight bound $M=3/2$, what is the probability that the first proposal is accepted, and what is the probability that the first acceptance needs more than two proposals?

::: {.callout-tip collapse="true" title="Answer"}
The acceptance probability is $1/M=2/3$, so the first proposal is accepted with probability $2/3$. The number of proposals is geometric, and $P(N>2)=(1-2/3)^2=1/9$.
:::

## Assumptions and limits — Tail control comes before tuning
For an unnormalised target $h$, a known bound $h\le Cg$ is enough to implement the acceptance decision. Its acceptance probability becomes $Z/C$, where $Z=\int h$; the sampler need not know $Z$, although a finite positive $Z$ is needed for a target probability law. Multiplying many one-dimensional envelopes in a high-dimensional problem can make the total acceptance probability very small. This concerns efficiency, whereas using an invalid envelope concerns the probability law itself. A transformation method is often preferable when a tractable inverse distribution function is available.{{cite:downey2014_thinkstats2}} (Ch. 5, “Generating random numbers”)

## Intuition
The proposal draws candidates from a distribution one already knows how to sample. The acceptance step thins those candidates. Where the target density is small relative to the envelope $Mg$, most candidates are rejected. Where the target nearly touches the envelope, most candidates are kept. The conditional law of the survivors is the target, because the thinning probability was chosen to be exactly the ratio of the two densities. The argument is an integral identity. It does not say that any particular accepted coordinate was likely as a point. A continuous density assigns probability zero to every single point. The threshold at that point is a conditional acceptance probability.

In the beta example, $f(x)=6x(1-x)$ on the unit interval has maximum $3/2$ at $x=1/2$. A uniform proposal and $M=3/2$ give an envelope that touches the target at the mode and lies above it elsewhere. The acceptance probability is $1/M=2/3$. A proposal at $x=1/4$ has height $f(1/4)=6\cdot(1/4)\cdot(3/4)=9/8$, so the threshold is $(9/8)/(3/2)=3/4$. A uniform $U=1/2$ falls below that threshold and is accepted. A uniform $U=0.8$ falls above it and is rejected. The same comparison with a looser envelope changes the threshold and the cost together.

### Properties — Cost is a geometric waiting time
Let $N$ be the number of proposals until, and including, the first acceptance. Then $P(N=n)=(1-1/M)^{n-1}(1/M)$ for $n=1,2,\ldots$, the geometric law that counts the successful trial. The mean is $M$ and the variance is $M(M-1)$. For $M=3/2$ the mean is $3/2$ and the variance is $(3/2)(1/2)=3/4$. If each proposal spends two uniform draws, one for the candidate and one for the accept–reject decision, the expected number of uniforms per output is $2M$. At the tight bound this is $3$. At the looser bound $M=2$ it is $4$. At $M=4$ the expected number of proposals is $4$ and the expected number of uniforms is $8$.

An invalid envelope is not a special case of a loose one. If $f(x)>Mg(x)$ on a set of positive probability, the ratio $f/(Mg)$ exceeds one there. Replacing the ratio by one in the code accepts too rarely in that region, relative to the proof, and the output density is no longer $f$. A target that equals $2$ on $[0,1/2]$ and equals $0$ elsewhere cannot use a uniform proposal on $[0,1]$ with $M=1$: on $(0,1/2)$ the target height $2$ exceeds the envelope height $1$. The integral test catches this before any draw is generated. The supremum of $f/g$ is $2$, so $M=2$ is a valid envelope and the acceptance probability is $1/2$.

## Common misconceptions
A high acceptance rate is evidence that the envelope is tight. It is not evidence that the program sampled the intended distribution. A bug that accepts every proposal returns the proposal law and has acceptance rate one. The check is the inequality $f\le Mg$ everywhere on the support, together with a correct uniform comparison. Histogram resemblance after a few hundred draws is a weak check of the tails and a non-check of independence across draws.

The method also does not require the target to be normalised, provided an envelope for the unnormalised function is known. The acceptance probability is then $Z/C$ rather than $1/M$, and $Z$ may be unknown. What the method cannot skip is finiteness of $Z$. An unnormalised function with an infinite integral is not a probability density, and rejection sampling against a probability proposal cannot create one. High dimension makes a different practical failure: a product of coordinate-wise factors can drive $M$ up exponentially in the dimension even when each factor looks mild. The output law remains correct while the waiting time becomes unusable. A transformation with an explicit inverse distribution function avoids the waiting time when one is available.{{cite:von_neumann1951_random_digits}} (pp. 37–38, nonuniform sampling)

## Connections
Inversion, the Box–Muller transformation, and acceptance–rejection are three ways of turning uniform random numbers into a named law. Inversion needs a tractable quantile function. Box–Muller uses two uniforms and trigonometric or logarithmic functions to produce a pair of normal draws. Acceptance–rejection needs an envelope and pays for it with rejected proposals. Mixtures can be sampled by first drawing a component label and then drawing from that component, which is inversion or rejection inside the component. The beta density $6x(1-x)$ happens to have both a simple shape and a polynomial distribution function, so inversion is available as well. The rejection calculation remains useful as a check that the envelope arithmetic, the mean number of proposals $3/2$, and the threshold $3/4$ agree with the density.
