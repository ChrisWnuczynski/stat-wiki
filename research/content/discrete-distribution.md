## Lead context
It lets probabilities for a count or a category be calculated by adding the masses of the values of interest.{{cite:durrett2019}} (Ch. 1, §1.2, pp. 13–14)

## Motivating example
A clinic records the number of missed appointments in a day. A probability for “at least two” is found by adding the chances of two, three and every larger possible count. Treating the count as a discrete random variable makes that calculation explicit, even if no fixed upper limit on missed appointments is imposed. The same idea appears in the dice-sum example below: there are 36 equally likely *ordered pairs* of faces, but the 11 possible sums are not equally likely. Six pairs give a sum of seven and only one gives a sum of two, so their probabilities are $6/36$ and $1/36$.{{cite:grinstead_snell1997}} (Ch. 1, §1.2, pp. 26–27)

## Intuition
A mass function assigns a probability to each value, like a set of weights whose total is one. A value can have zero mass; the support can be taken to contain only values with positive mass. The cumulative distribution function adds all masses at or below a threshold. As the threshold passes a value $x$, it jumps by exactly the mass at $x$. This is why the die plot on this page has bars for its mass function and steps for its distribution function.{{cite:durrett2019}} (Ch. 1, §1.2, pp. 13–14){{cite:grinstead_snell1997}} (Ch. 1, §1.2, pp. 19–21)

The values need not be equally spaced or integer-valued. For example, a recorded dose could take one of three labelled numerical amounts. Conversely, a countable list of labels is not itself a probability model: their masses must be specified. The underlying sample space can be much larger than the range of the recorded variable, as the dice example shows.{{cite:grinstead_snell1997}} (Ch. 1, §1.2, pp. 25–27)

## Definition
More precisely, a real-valued random variable $X$ has a discrete distribution if some finite or countable set $S$ satisfies $\mathbb P(X\in S)=1$. Its probability mass function is $p_X(x)=\mathbb P(X=x)$, zero off the values with positive mass. Necessarily $p_X(x)\geq0$ and $\sum_{x\in S}p_X(x)=1$. Conversely, any nonnegative assignments with that sum define a discrete law. For any set $B$ of values, $\mathbb P(X\in B)=\sum_{x\in B\cap S}p_X(x)$. This is a statement about the *distribution* of $X$: outcomes outside $S$ may exist in a larger sample space but receive probability zero under this law.{{cite:durrett2019}} (Ch. 1, §1.2, pp. 13–14){{cite:grinstead_snell1997}} (Ch. 1, §1.2, pp. 19–21)

For a countably infinite support the sum is a convergent series, not an instruction to truncate at an arbitrary last value. A geometric waiting time, for example, takes values $1,2,\ldots$ and has mass $p(1-p)^{x-1}$ at $x$ when independent trials succeed with probability $p\in(0,1]$. The geometric-series identity makes its total mass one. A finite table is valid only when its listed masses add to one or the omitted tail is explicitly accounted for.{{cite:grinstead_snell1997}} (Ch. 5, §5.1, geometric distribution)

## Properties
The distribution function is $F_X(t)=\sum_{x\in S:x\leq t}p_X(x)$, and its jump at $x$ is $F_X(x)-F_X(x-)=p_X(x)$. It follows that $\mathbb P(a<X\leq b)=F_X(b)-F_X(a)$; the choice of strict or weak endpoint matters when an endpoint has mass. This connects the mass function directly to the staircase figure. A discrete distribution has a cumulative function with jumps, though its support may be infinite or even dense; “discrete” does not mean that every pair of support points has a gap between them.{{cite:durrett2019}} (Ch. 1, §1.2, pp. 13–14)

If $Y=g(X)$, several $x$ values may map to the same $y$. The new mass is $p_Y(y)=\sum_{x:g(x)=y}p_X(x)$, not the mass at just one preimage. In particular, the sum and minimum of two dice in the examples below are obtained by grouping ordered pairs with the same result. For a function $h$ with an absolutely convergent expectation, $\mathbb E[h(X)]=\sum_x h(x)p_X(x)$. The mean and variance then follow by taking $h(x)=x$ and $h(x)=(x-\mathbb EX)^2$.{{cite:grinstead_snell1997}} (Ch. 1, §1.2, pp. 25–27; Ch. 6, §6.1)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The events $\{X=x\}$ for distinct $x\in S$ are disjoint and their union has probability one. Countable additivity therefore gives $\sum_{x\in S}p_X(x)=1$ and, after restricting the union to $B$, the event-sum formula. Restricting it to $(-\infty,t]$ gives the formula for $F_X(t)$. The limit $F_X(x-)$ sums masses strictly below $x$, so subtracting leaves $p_X(x)$. Subtracting the sums up to $a$ and $b$ leaves precisely those masses in $(a,b]$.{{cite:durrett2019}} (Ch. 1, §§1.1–1.2, pp. 3–14)

For a transformation, $\{g(X)=y\}$ is the disjoint union of $\{X=x\}$ over all $x$ with $g(x)=y$, yielding the preimage-sum rule. Grouping the same masses by transformed value gives $\mathbb E[h(X)]=\sum_x h(x)p_X(x)$ when absolute convergence permits regrouping. For the geometric example, $\sum_{x=1}^{\infty}p(1-p)^{x-1}=p/[1-(1-p)]=1$ for $0<p\leq1$ (with the endpoint $p=1$ understood directly).{{cite:grinstead_snell1997}} (Ch. 5, §5.1; Ch. 6, §6.1)
:::
:::

## Statistical use
Discrete laws arise for event counts, categories coded numerically, waiting times recorded in trials, and bounded numbers of successes. The figure of binomial, geometric and Poisson masses illustrates different shapes and supports; a bar height is a probability of that exact value. When fitting a model, choose a family whose possible values and dependence assumptions match the measurement process. A binomial count has a fixed number of trials, whereas a Poisson count has no finite upper bound. Probabilities from either fitted law are conditional on its model assumptions.{{cite:grinstead_snell1997}} (Ch. 5, §5.1)

A mass function also supplies the likelihood for an observed value when its parameters are unknown. If independent observations $x_1,\ldots,x_n$ follow a proposed mass function $p_\theta$, their joint probability is $\prod_i p_\theta(x_i)$. The product uses independence, which is an extra assumption; the single-variable definition of a discrete distribution does not require independent observations.{{cite:durrett2019}} (Ch. 1, §§1.1–1.2, pp. 3–14)

## Worked example
Suppose three independent inspections each find a defect with probability $1/4$, and let $X$ be the number of defects. The four masses are $p_X(0)=27/64$, $p_X(1)=27/64$, $p_X(2)=9/64$ and $p_X(3)=1/64$. For example, exactly two defects can occur in three positions, each with probability $(1/4)^2(3/4)=3/64$, giving $3(3/64)=9/64$. The masses total $64/64=1$. The chance of at least two defects is $(9+1)/64=5/32$, while $F_X(1)=(27+27)/64=27/32$. The expected count is $3(1/4)=3/4$, or equivalently $(27+2\cdot9+3)/64=3/4$. Each result is a claim about a fresh set of three inspections under the stated independent-trial model.{{cite:grinstead_snell1997}} (Ch. 5, §5.1, binomial distribution; Ch. 6, §6.1)

**Your turn.** Two independent trials each succeed with probability $1/3$. Write the masses of the success count $Y$ at 0, 1 and 2. Find $\mathbb P(Y\geq1)$ and $\mathbb EY$.{{cite:grinstead_snell1997}} (Ch. 5, §5.1; Ch. 6, §6.1)

::: {.callout-tip collapse="true" title="Answer"}
The masses are $p_Y(0)=(2/3)^2=4/9$, $p_Y(1)=2(1/3)(2/3)=4/9$ and $p_Y(2)=(1/3)^2=1/9$. They add to one. Hence $\mathbb P(Y\geq1)=4/9+1/9=5/9$ and $\mathbb EY=(4+2)/9=2/3$. The middle mass counts two orders of one success and one failure.{{cite:grinstead_snell1997}} (Ch. 5, §5.1; Ch. 6, §6.1)
:::

## Common misconceptions
“Discrete” refers to concentration on a countable set, not equal probability for each listed value: the sum of two fair dice is a counterexample. A mass $p_X(x)$ *is* a probability for one value, unlike the height of a continuous density. The values in a probability table are possible outcomes, not an observed frequency table; frequencies estimate masses but do not have to equal them in a finite sample. Finally, a variable can take numerical values from a finite set without its distribution being uniform over that set.{{cite:grinstead_snell1997}} (Ch. 1, §1.2, pp. 25–27){{cite:durrett2019}} (Ch. 1, §1.2, pp. 13–14)

## Assumptions and limits
An ordinary mass function cannot describe a purely continuous uniform draw on $[0,1]$: every singleton has probability zero, and summing any countable collection of them still gives zero. A model that rounds such a draw to a fixed number of decimal places *does* produce a discrete recorded value, but its law depends on the rounding rule. A mixture that assigns half its probability to a point and half to a uniform interval is neither purely discrete nor described by a density alone; it needs both components. Durrett's Cantor example gives a further warning: a continuous distribution function need not have a density and need not be discrete.{{cite:durrett2019}} (Ch. 1, §1.2, pp. 12–14)

## Connections
The [cumulative distribution function](cumulative-distribution-function.qmd) accumulates the masses. [Expectation](expectation.qmd) weights values by those masses, and a [joint probability mass function](joint-probability-mass-function.qmd) assigns masses to pairs of values. Named [binomial](binomial-distribution.qmd), [geometric](geometric-distribution.qmd) and [Poisson](poisson-distribution.qmd) laws are particular discrete models. The [continuous distribution](continuous-distribution.qmd) page explains probabilities computed by integration instead of summation.{{cite:grinstead_snell1997}} (Ch. 5, §5.1; Ch. 6, §6.1)

## History
Probability calculations began with finite games of chance: the Grinstead–Snell historical introduction traces that tradition to Pascal and Fermat's seventeenth-century correspondence. The modern definition is broader than dice or cards; Durrett includes any law carried by a countable set, including infinitely many possible values.{{cite:grinstead_snell1997}} (Preface, p. vii){{cite:durrett2019}} (Ch. 1, §1.2, pp. 13–14)
