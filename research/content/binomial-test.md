## Lead context
Exact tail probabilities preserve the discreteness of the count, which can make an unrandomised test conservative.

## Motivating example
A claim of a success probability of one half can be tested by counting successes in repeated independent trials. Nine successes out of ten is unusual under that claim; eight out of ten is less decisive. The test compares the observed count and more extreme counts with their probabilities under the null distribution. Its assumptions include independent trials with one common success probability.{{cite:dodge2008}} (pp. 47–48)

## Definition — Choose the tail before looking at the count
For $X\sim\operatorname{Bin}(n,p)$ and null $p=p_0$, an upper-tail alternative uses the $p$-value
$$
p_{\rm upper}=\sum_{k=x}^{n}\binom nkp_0^k(1-p_0)^{n-k}.
$$
The lower-tail alternative sums from zero through $x$. The null distribution supplies the probabilities; selecting a tail after seeing which direction is favourable changes the testing procedure.{{cite:dodge2008}} (p. 47, one-sided hypotheses);{{cite:grinstead_snell1997}} (§§3.2, 5.1, binomial probabilities)

An upper-tail critical value $c$ is the smallest integer for which $P_{p_0}(X\geq c)\leq\alpha$. Reject for counts at least $c$. Because the count is discrete, the actual null rejection probability can be strictly smaller than $\alpha$. An exact binomial calculation uses the specified sampling distribution without a normal approximation; it does not mean that every attainable rejection probability equals the nominal level.{{cite:dodge2008}} (pp. 47–48)

## Properties — The rejection probability is a function of the true rate
For a fixed rejection threshold, its power at success probability $p$ is
$$
\beta(p)=\sum_{k=c}^n\binom nkp^k(1-p)^{n-k}.
$$
The size at the boundary null is $\beta(p_0)$. Increasing $p$ increases the upper-tail probability: represent each Bernoulli success as $1\{U_i\leq p\}$ using the same independent uniforms, and every count is nondecreasing in $p$. This also establishes that an upper-tail rule calibrated at $p_0$ controls rejection throughout the composite null $p\leq p_0$.{{cite:grinstead_snell1997}} (§§1.1, 5.1, Bernoulli simulation and binomial distribution)

For the symmetric null $p_0=1/2$, an equal-tail two-sided test pairs a large count with its equally probable small-count counterpart. Away from the centre, the two-sided tail probability is twice the smaller one-sided tail. The calculation below uses this explicit convention.{{cite:dodge2008}} (p. 47, two-sided case)

## Worked example
Let $n=10$, $p_0=1/2$, and test against $p>1/2$. For nine observed successes,
$$
P_{1/2}(X\geq9)=\frac{\binom{10}{9}+\binom{10}{10}}{2^{10}}
=\frac{11}{1024}=0.0107421875.
$$
For eight successes the tail is $56/1024=0.0546875$. Thus the five-percent upper-tail test rejects from nine onwards, and its actual size is only $11/1024$. The jump across the requested level comes from the mass at eight.{{cite:grinstead_snell1997}} (§5.1);{{cite:dodge2008}} (pp. 47–48)

Under a two-sided doubled-tail convention, nine successes gives $22/1024=0.021484375$. This doubles a null tail probability, rather than giving the posterior probability that the null is true. A posterior probability for a point null requires a separate model and prior probability assigned to that null.{{cite:grinstead_snell1997}} (§4.1, Bayes' formula)

**Your turn.** For the same ten trials, calculate the lower-tail $p$-value when one success is observed.

::: {.callout-tip collapse="true" title="Answer"}
Symmetry under $p_0=1/2$ gives $P(X\leq1)=P(X\geq9)=11/1024$. The matched two-sided value is $22/1024$.
:::
