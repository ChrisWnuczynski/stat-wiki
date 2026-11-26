## Lead context
The axioms specify a nonnegative countably additive measure with total mass one on a sigma-algebra of events. Countability is essential: the sum rule is not a rule for arbitrary uncountable unions.{{cite:dodge2008}} (p. 430){{cite:durrett2019}} (§1.1, pp. 1–2)

## Motivating example
A fair die assigns probability $1/6$ to each of six faces. A uniform draw on $[0,1]$ assigns probability zero to each individual point. Both obey the same axioms because the die is a finite union of singletons, while an interval is an uncountable union. Countable additivity does not sum the interval's singleton probabilities.{{cite:durrett2019}} (§1.1, measure examples; §1.2, ex. 1.2.3)

## Properties — Derive finite rules from countable additivity
The axioms apply to events in $\mathcal F$, a collection closed under complements and countable unions. Substituting a disjoint union of an event and its complement proves the complement rule. If $A\subseteq B$, write $B=A\cup(B\setminus A)$ disjointly; nonnegativity gives $\mathbb{P}(A)\le \mathbb{P}(B)$. Partitioning $A\cup B$ into $A\setminus B$, $A\cap B$ and $B\setminus A$ proves inclusion–exclusion. These familiar finite rules are consequences, not separate probability assignments.{{cite:durrett2019}} (§1.1, thm. 1.1.1)

For increasing events $A_n\uparrow A$, set $B_1=A_1$ and $B_n=A_n\setminus A_{n-1}$. The $B_n$ are disjoint and their union is $A$. Countable additivity yields $\mathbb{P}(A)=\sum_nP(B_n)=\lim_nP(A_n)$. Applying this to complements also gives continuity from above for decreasing events. These limit properties let finite approximations determine probabilities of infinite constructions.{{cite:durrett2019}} (§1.1, thm. 1.1.1)

## Worked example
On outcomes $\{1,2,3,4\}$ put weights $(0.1,0.2,0.3,0.4)$. Let $A=\{1,2\}$ and $B=\{2,3\}$. Then $\mathbb{P}(A)=0.3$, $\mathbb{P}(B)=0.5$, $\mathbb{P}(A\cap B)=0.2$ and $\mathbb{P}(A\cup B)=0.6$. Direct summation agrees with $0.3+0.5-0.2=0.6$. Also $\mathbb{P}(A^c)=0.7$. The weights need not be equal for the axioms to hold.{{cite:dodge2008}} (p. 430)

On the positive integers, weights $\mathbb{P}(\{k\})=2^{-k}$ sum to one, since $\sum_{k=1}^N2^{-k}=1-2^{-N}$. Thus the tail event $\{N+1,N+2,\ldots\}$ has probability $2^{-N}$; at $N=3$ it is $1/8$. The limiting tail is empty and its probability tends to zero, illustrating continuity from above.

**Your turn.** With the four-outcome weights above, find the probability that exactly one of $A$ and $B$ occurs.

::: {.callout-tip collapse="true" title="Answer"}
The event is $\{1,3\}$ and has probability $0.4$. Equivalently, $\mathbb{P}(A)+\mathbb{P}(B)-2\mathbb{P}(A\cap B)=0.3+0.5-0.4=0.4$.
:::

## Assumptions and limits
An uncountable sample space may carry atoms: for example, on $[0,1]$ assign half the mass to $0$ and half to a uniform draw. Then $\mathbb{P}(\{0\})=1/2$ and $\mathbb{P}((0,1])=1/2$. A zero probability for every point is a feature of an atomless law, not a consequence of the cardinality of the space. All sets discussed must still belong to the chosen sigma-algebra.{{cite:durrett2019}} (§1.1, measure and sigma-field; §1.2, exs. 1.2.3 and 1.2.8)

## Intuition
The axioms are a short list of properties that a probability assignment must have, not a menu of optional formulas. Nonnegativity keeps probabilities from running below zero. Total mass one fixes the scale. Countable additivity says that the probability of a countable collection of disjoint events is the sum of their probabilities. Finite rules such as complements, monotonicity, and inclusion–exclusion are theorems from that list. The restriction to countable unions is the part that lets a uniform distribution on an interval give every single point probability zero while still giving the whole interval probability one. An uncountable sum of zeros is not a sum the axiom governs.{{cite:durrett2019}} (§1.1, pp. 1–2)

## Definition
A probability space is a sample space, a sigma-algebra $\mathcal F$ of events, and a function $P$ on $\mathcal F$. The sigma-algebra contains the sample space and is closed under complements and under countable unions. The function $P$ satisfies $\mathbb{P}(A)\ge 0$, $\mathbb{P}(\Omega)=1$, and $\mathbb{P}(\bigcup_n A_n)=\sum_n \mathbb{P}(A_n)$ whenever the events $A_n$ are disjoint and belong to $\mathcal F$. From these, $\mathbb{P}(A^c)=1-\mathbb{P}(A)$. If $A\subseteq B$, then $\mathbb{P}(A)\le \mathbb{P}(B)$. For any two events, $\mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B)$, because the intersection would otherwise be counted twice. The probability that exactly one of the two events occurs is $\mathbb{P}(A)+\mathbb{P}(B)-2\mathbb{P}(A\cap B)$.{{cite:durrett2019}} (§1.1, thm. 1.1.1)

## Interpretation
On the four outcomes with weights $0.1,0.2,0.3,0.4$, the events $A=\{1,2\}$ and $B=\{2,3\}$ have probabilities $0.3$ and $0.5$, and their intersection has probability $0.2$. The union formula returns $0.6$, matching the direct sum of the weights on $\{1,2,3\}$. The exactly-one event is $\{1,3\}$, with probability $0.4$. Nothing in the arithmetic required the weights to be equal. On the positive integers the weights $2^{-k}$ sum to one. The tail beyond $N$ has probability $2^{-N}$. At $N=3$ that tail is $1/8$, and at $N=5$ it is $1/32$. The empty limiting tail has probability zero, which is continuity from above: a decreasing sequence of events shrinks to a limit whose probability is the limit of the probabilities.{{cite:dodge2008}} (p. 430)

## Common misconceptions
A probability of zero is not the same statement as an empty set. In the uniform distribution on $[0,1]$, every singleton is nonempty and still has probability zero. That does not contradict additivity, because the interval is not a countable union to which the sum rule applies. A second confusion is to treat an uncountable space as automatically atomless. Putting mass $1/2$ on the single point $0$ and spreading the rest uniformly on $(0,1]$ is a legitimate probability, and $\{0\}$ is an atom. A third confusion is to apply inclusion–exclusion to objects that are not events in $\mathcal F$. The axioms assign probabilities only to the sets the sigma-algebra contains.{{cite:durrett2019}} (§1.1, measure and sigma-field; §1.2, exs. 1.2.3 and 1.2.8)

## Statistical use
The four weights $0.1,0.2,0.3,0.4$ already show the finite rules at work. Events $A=\{1,2\}$ and $B=\{2,3\}$ have probabilities $0.3$ and $0.5$. Their intersection has probability $0.2$, so the union has probability $0.3+0.5-0.2=0.6$. The complement of that union has probability $0.4$, and the complement of $A$ has probability $0.7$. The event that exactly one of $A$ and $B$ occurs is $\{1,3\}$, with probability $0.4$. Each of these is a consequence of nonnegativity, total mass one, and additivity. None of them requires the four outcomes to be equally likely.

On the positive integers the weights $2^{-k}$ are a different assignment with the same three properties. The probability of the integers beyond $3$ is $1/8$, and the probability beyond $5$ is $1/32$. The probabilities of the tails decrease to the probability of the empty limit, which is zero. That continuity is what countable additivity adds to the finite sum rules. A uniform distribution on an interval uses the same continuity in the other direction: every singleton can have probability zero while the interval keeps probability one, because the interval is not a countable union to which the sum applies.{{cite:durrett2019}} (§1.1, thm. 1.1.1)
