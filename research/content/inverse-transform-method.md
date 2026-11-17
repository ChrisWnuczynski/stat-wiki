## Lead context
A quantile function turns the uniform distribution into a chosen probability law, including laws with jumps.

## Motivating example
A simulation supplies uniform random numbers, while a queueing model requires exponential waiting times. The problem is to transform the numbers without changing the requested probabilities. More generally, a single rule should handle both a smooth waiting-time distribution and a discrete choice between several outcomes. Quantiles provide that rule.{{cite:durrett2019}} (§1.2, Thm. 1.2.2, p. 11)

## Definition — Generalised quantiles
For a cumulative distribution function $F$, define
$$
Q(u)=\inf\{x\in\mathbb R:F(x)\ge u\},\qquad 0<u<1.
$$
If $U$ is uniform on $(0,1)$, the inverse-transform method returns $X=Q(U)$. A strictly increasing continuous $F$ has its ordinary inverse. The infimum definition also handles flat sections and jumps. At a jump of size $p$, a whole interval of uniform inputs of length $p$ maps to the same value.{{cite:durrett2019}} (§1.2, Thm. 1.2.2, pp. 10–12)

For a finite discrete law on ordered values $x_1<\cdots<x_k$ with probabilities $p_j$, put $c_j=\sum_{i\le j}p_i$. Return $x_j$ when $c_{j-1}<U\le c_j$, with $c_0=0$. The interval lengths are the desired probabilities.{{cite:grinstead_snell1997}} (§1.1, simulation of discrete probabilities)

## Properties — Why the probabilities match
The defining equivalence is
$$
Q(u)\le x\quad\Longleftrightarrow\quad u\le F(x).
$$
Consequently $\Pr\{Q(U)\le x\}=\Pr\{U\le F(x)\}=F(x)$. Right-continuity is what lets the infimum select the appropriate boundary at jumps. The output law is determined by these probabilities, so no differentiability of $F$ is needed.{{cite:durrett2019}} (§1.2, proof of Thm. 1.2.2, p. 11)

An exponential law of rate $\lambda$ has $F(x)=1-e^{-\lambda x}$ for $x\ge0$. Solving $u=F(x)$ gives $Q(u)=-\log(1-u)/\lambda$. Replacing $1-U$ by $U$ gives another uniform input and the equally valid formula $-\log U/\lambda$. The two formulas produce the same distribution, but different outputs for a particular input number.{{cite:grinstead_snell1997}} (§2.1, simulation of continuous probabilities)

## Worked example
For rate $\lambda=2$ and input $u=0.8$,
$$
Q(0.8)=-\frac{\log(0.2)}2=0.804719.
$$
Substitution into $F$ gives $1-e^{-2(0.804719)}\approx0.8$. The median corresponds to $u=0.5$ and equals $\log2/2=0.346574$. Its value is below the mean $1/2$, which is consistent with the long right tail.

For a discrete distribution with values $0,2,5$ and probabilities $0.2,0.5,0.3$, the cumulative thresholds are $0.2,0.7,1$. Inputs $0.1,0.6,0.9$ return $0,2,5$. The interval $(0.2,0.7]$ has length $0.5$ and therefore produces the atom at two with the required probability.

**Your turn.** A distribution has $F(x)=x^3$ on $[0,1]$. Find its quantile at $u=1/8$.

::: {.callout-tip collapse="true" title="Answer"}
The quantile is $Q(u)=u^{1/3}$. Thus $Q(1/8)=1/2$, and the CDF at that point is $(1/2)^3=1/8$.
:::

## Connections — Shared uniforms and monotone outputs
The quantile function is nondecreasing. Two simulations driven by the same uniform numbers can therefore be compared point by point when their quantile functions are ordered. This construction couples the variables; it does not make them independent. Independent output draws require independent uniform inputs. When a quantile has no closed form, solving $F(x)=u$ numerically still implements the same idea.{{cite:durrett2019}} (§1.2, inverse distribution construction)

