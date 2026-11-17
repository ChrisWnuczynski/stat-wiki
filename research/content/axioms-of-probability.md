## Lead context
The axioms specify a nonnegative countably additive measure with total mass one on a sigma-algebra of events. Countability is essential: the sum rule is not a rule for arbitrary uncountable unions.{{cite:dodge2008}} (p. 430){{cite:durrett2019}} (§1.1, pp. 1–2)

## Motivating example
A fair die assigns probability $1/6$ to each of six faces. A uniform draw on $[0,1]$ assigns probability zero to each individual point. Both obey the same axioms because the die is a finite union of singletons, while an interval is an uncountable union. Countable additivity does not sum the interval's singleton probabilities.{{cite:durrett2019}} (§1.1, measure examples; §1.2, ex. 1.2.3)

## Properties — Derive finite rules from countable additivity
The axioms apply to events in $\mathcal F$, a collection closed under complements and countable unions. Substituting a disjoint union of an event and its complement proves the complement rule. If $A\subseteq B$, write $B=A\cup(B\setminus A)$ disjointly; nonnegativity gives $P(A)\le P(B)$. Partitioning $A\cup B$ into $A\setminus B$, $A\cap B$ and $B\setminus A$ proves inclusion–exclusion. These familiar finite rules are consequences, not separate probability assignments.{{cite:durrett2019}} (§1.1, thm. 1.1.1)

For increasing events $A_n\uparrow A$, set $B_1=A_1$ and $B_n=A_n\setminus A_{n-1}$. The $B_n$ are disjoint and their union is $A$. Countable additivity yields $P(A)=\sum_nP(B_n)=\lim_nP(A_n)$. Applying this to complements also gives continuity from above for decreasing events. These limit properties let finite approximations determine probabilities of infinite constructions.{{cite:durrett2019}} (§1.1, thm. 1.1.1)

## Worked example
On outcomes $\{1,2,3,4\}$ put weights $(0.1,0.2,0.3,0.4)$. Let $A=\{1,2\}$ and $B=\{2,3\}$. Then $P(A)=0.3$, $P(B)=0.5$, $P(A\cap B)=0.2$ and $P(A\cup B)=0.6$. Direct summation agrees with $0.3+0.5-0.2=0.6$. Also $P(A^c)=0.7$. The weights need not be equal for the axioms to hold.{{cite:dodge2008}} (p. 430)

On the positive integers, weights $P(\{k\})=2^{-k}$ sum to one, since $\sum_{k=1}^N2^{-k}=1-2^{-N}$. Thus the tail event $\{N+1,N+2,\ldots\}$ has probability $2^{-N}$; at $N=3$ it is $1/8$. The limiting tail is empty and its probability tends to zero, illustrating continuity from above.

**Your turn.** With the four-outcome weights above, find the probability that exactly one of $A$ and $B$ occurs.

::: {.callout-tip collapse="true" title="Answer"}
The event is $\{1,3\}$ and has probability $0.4$. Equivalently, $P(A)+P(B)-2P(A\cap B)=0.3+0.5-0.4=0.4$.
:::

## Assumptions and limits
An uncountable sample space may carry atoms: for example, on $[0,1]$ assign half the mass to $0$ and half to a uniform draw. Then $P(\{0\})=1/2$ and $P((0,1])=1/2$. A zero probability for every point is a feature of an atomless law, not a consequence of the cardinality of the space. All sets discussed must still belong to the chosen sigma-algebra.{{cite:durrett2019}} (§1.1, measure and sigma-field; §1.2, exs. 1.2.3 and 1.2.8)
