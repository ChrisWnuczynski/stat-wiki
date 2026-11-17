## Lead context
A point mass is visible as a jump of the distribution function, even when the same law also has a continuous component.

## Motivating example
An insurance payment can be exactly zero when no claim occurs and positive when a claim is paid. A density for positive payments alone cannot account for the positive probability of paying nothing. The distribution function can describe both features by combining a jump at zero with a smooth increase above zero.{{cite:durrett2019}} (§1.2, distributions)

## Definition — Reading mass from a jump
For a real random variable $X$, define $F(x)=\Pr(X\le x)$ and $F(x-)=\Pr(X<x)$. A point $x$ is an atom when $\Pr(X=x)>0$, and
$$
\Pr(X=x)=F(x)-F(x-).
$$
This follows by subtracting the probabilities of the disjoint events $\{X<x\}$ and $\{X=x\}$ that form $\{X\le x\}$. Right-continuity determines which side of the step includes its endpoint.{{cite:durrett2019}} (§1.2, Thm. 1.2.1, p. 10) For an ordered discrete law, the CDF is a step function whose jumps collect the successive point probabilities.{{cite:dodge2008}} (p. 165, Discrete Distribution Function)

A density value $f(x)$ is not a point probability. An absolutely continuous law has $\Pr(X=x)=0$ for every $x$, even where its density is large. The probability of an interval is an integral of the density, while the probability of an atom must be counted separately.{{cite:durrett2019}} (§1.2, density representation, pp. 12–14)

## Properties — How many atoms can there be?
There can be only countably many atoms. For each positive integer $k$, there are at most $k$ points with mass at least $1/k$; otherwise their probabilities would sum to more than one. Every positive mass exceeds $1/k$ for some $k$, so all atoms lie in a countable union of finite sets. The remaining part of a distribution need not have a density: an atom-free law has a continuous CDF, and some continuous laws are singular.{{cite:durrett2019}} (§1.2, continuous and singular distributions, pp. 13–14)

## Worked example
Let $X$ equal zero with probability $0.3$, and otherwise draw an exponential variable of rate two. Its CDF is
$$
F(x)=\begin{cases}0,&x<0,\\
0.3+0.7(1-e^{-2x}),&x\ge0.
\end{cases}
$$
The atom at zero has mass $F(0)-F(0-)=0.3$. For $x>0$ the continuous part has density $1.4e^{-2x}$, whose integral is $0.7$. The total probability at or below one is $F(1)=0.905265$. The mean is $0.7(1/2)=0.35$; the second moment is $0.7(2/2^2)=0.35$, giving variance $0.35-0.35^2=0.2275$.

The probability of an exact positive value, such as $\Pr(X=1)$, is zero. The positive CDF value at one includes the atom at zero and all continuous mass between zero and one; it is not the mass of a single payment. This uses the same cumulative-probability definition for both components.{{cite:dodge2008}} (p. 172, Distribution Function)

**Your turn.** Find $\Pr(0<X\le1)$ for this mixture.

::: {.callout-tip collapse="true" title="Answer"}
Subtract the mass at zero: $F(1)-F(0)=0.7(1-e^{-2})=0.605265$. Including zero would add $0.3$.
:::

## Interpretation — Recording and rounding
An atom can be a feature of the model or of a recording rule. For example, rounding a continuous measurement to a finite precision creates positive probabilities at the recorded values. Whether zero means no event, censoring or a rounded small measurement changes the appropriate model. The mathematical description concerns the law of the recorded random variable, so that variable must be specified.{{cite:durrett2019}} (§1.3, random variables as measurable functions)

