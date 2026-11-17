## Motivating example
A risk register lists several possible faults in a machine. The chance of at least one fault cannot generally be found by adding their probabilities: two faults may occur together. Basic probability properties turn such statements into coherent calculations. They distinguish mutually exclusive events, overlapping events and independent events, while requiring all probabilities to belong to one specified experiment and sample space.{{cite:openintro2019}} (Chapter 3, “Defining probability”, disjoint and non-disjoint events)

## Statement

**Begin with a probability measure.**
On a sample space $\Omega$ with a sigma-algebra $\mathcal F$, a probability measure $P$ is nonnegative, satisfies $P(\Omega)=1$, and is countably additive on pairwise disjoint measurable events. From these axioms follow
$$P(\varnothing)=0,\qquad P(A^c)=1-P(A),\qquad 0\le P(A)\le1.$$
If $A\subseteq B$, then $P(A)\le P(B)$. For any two events,
$$P(A\cup B)=P(A)+P(B)-P(A\cap B).$$
These facts are constraints on a single probability assignment, rather than separate assumptions to be selected independently.{{cite:dodge2008}} (Probability, pp. 430–432)

## Proof
Since $\Omega=\Omega\mathbin{\dot\cup}\varnothing$, finite additivity gives $1=1+P(\varnothing)$, proving the empty-set formula. The disjoint union $\Omega=A\mathbin{\dot\cup}A^c$ gives the complement rule. Nonnegativity then bounds $P(A)$ above by one. If $A\subseteq B$, decompose $B=A\mathbin{\dot\cup}(B\setminus A)$; subtracting gives $P(B)-P(A)=P(B\setminus A)\ge0$.

For inclusion–exclusion, decompose $A\cup B$ into the disjoint events $A\setminus B$, $A\cap B$ and $B\setminus A$. Adding their probabilities counts the intersection once. Adding $P(A)+P(B)$ counts it twice, so subtracting $P(A\cap B)$ gives the displayed formula. Dropping this nonnegative intersection term yields $P(A\cup B)\le P(A)+P(B)$, the two-event union bound.{{cite:openintro2019}} (Chapter 3, “Probabilities when events are not disjoint” and “Complement of an event”)

## Intuition — Complements and unions express different questions
A complement asks whether an event fails to occur, so it refers to all outcomes outside that event. A union asks whether at least one of several events occurs. The phrase “either A or B” must be interpreted carefully, because an inclusive union permits both. If exactly one is intended, the event is the symmetric difference, with probability $P(A)+P(B)-2P(A\cap B)$. These are set operations before they are numerical formulas.{{cite:openintro2019}} (Chapter 3, “Defining probability”, disjoint and non-disjoint events)

Independence is another distinct relationship. It means $P(A\cap B)=P(A)P(B)$, whereas disjointness means the intersection is empty. Two disjoint events with positive probabilities cannot be independent, because their intersection probability is zero while their product is positive. Confusing these conditions gives a wrong probability even when each marginal probability has been estimated well.{{cite:openintro2019}} (Chapter 3, “Independence”)

## Worked example — Overlapping machine faults
Suppose a temperature fault has probability $0.3$, a pressure fault has probability $0.4$, and both occur with probability $0.1$. The chance of at least one is $0.3+0.4-0.1=0.6$, so the chance of neither is $0.4$. The chance of exactly one is $0.3+0.4-2(0.1)=0.5$. The four disjoint outcomes have probabilities $0.1$ for both, $0.2$ for temperature only, $0.3$ for pressure only and $0.4$ for neither; they sum to one.

These faults are not independent, since $0.1\ne0.3\times0.4=0.12$. Their marginal probabilities alone would not determine the probability of a union: an intersection probability is also required, or an assumption that determines it. Without that information, inclusion–exclusion gives the bounds $0.4\le P(A\cup B)\le0.7$.

**Your turn.** If the two faults were independent with the same marginal probabilities, what would be the probability of neither?

::: {.callout-tip collapse="true" title="Answer"}
The intersection would have probability 0.12, so the union would have probability 0.58. Its complement would have probability 0.42, also equal to (1−0.3)(1−0.4).
:::

## Generalizations — Countable bounds and limiting events
For events $A_1,A_2,\ldots$, define disjoint pieces $B_1=A_1$ and $B_j=A_j\setminus\bigcup_{i<j}A_i$. Their union is the same as the union of the $A_j$, and $B_j\subseteq A_j$. Countable additivity and monotonicity give $P(\bigcup_j A_j)\le\sum_j P(A_j)$. This union bound needs no independence assumption.{{cite:dodge2008}} (Probability, pp. 430–432, countable additivity)

If $A_n$ increases to $A$, the differences $A_n\setminus A_{n-1}$ form a disjoint decomposition of $A$. Partial sums of their probabilities equal $P(A_n)$, so $P(A_n)\to P(A)$. Applying this to complements gives continuity for decreasing event sequences too. These limiting properties follow from countable additivity and justify passing from finite event approximations to their countable limit.

## Common misconceptions — Zero probability need not mean an empty event
The axiom $P(\varnothing)=0$ does not assert the converse. In a continuous uniform model on [0,1], any specified singleton has probability zero while still containing an outcome. Conversely, a probability-one event can omit a null set. Statements about almost-sure behaviour should therefore distinguish measure from set equality.{{cite:openintro2019}} (Chapter 3, “Continuous distributions”, probabilities as areas)

## Statistical use — Express risks as events before adding them
For a collection of risks, specify the sample space and the event corresponding to each reported number before combining them. The union bound gives a conservative upper bound on the probability of at least one event without requiring independence; inclusion–exclusion gives an exact calculation when intersections are known. These choices make clear which information is supplied by data and which comes from assumptions about how events overlap.{{cite:openintro2019}} (Chapter 3, “Probabilities when events are not disjoint”)
