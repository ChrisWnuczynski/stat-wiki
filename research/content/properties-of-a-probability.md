## Motivating example
A risk register lists several possible faults in a machine. The chance of at least one fault cannot generally be found by adding their probabilities: two faults may occur together. Basic probability properties turn such statements into coherent calculations. They distinguish mutually exclusive events, overlapping events and independent events, while requiring all probabilities to belong to one specified experiment and sample space.{{cite:openintro2019}} (§3.1, pp. 84–86, disjoint and general addition rules)

## Statement

**Begin with a probability measure.**
On a sample space $\Omega$ with a sigma-algebra $\mathcal F$, a probability measure $P$ is nonnegative, satisfies $P(\Omega)=1$, and is countably additive on pairwise disjoint measurable events. From these axioms follow
$$P(\varnothing)=0,\qquad P(A^c)=1-P(A),\qquad 0\le P(A)\le1.$$
If $A\subseteq B$, then $P(A)\le P(B)$. For any two events,
$$P(A\cup B)=P(A)+P(B)-P(A\cap B).$$
These facts are constraints on a single probability assignment, rather than separate assumptions to be selected independently.{{cite:dodge2008}} (Probability, pp. 430–432)

## Proof
Since $\Omega=\Omega\mathbin{\dot\cup}\varnothing$, finite additivity gives $1=1+P(\varnothing)$, proving the empty-set formula. The disjoint union $\Omega=A\mathbin{\dot\cup}A^c$ gives the complement rule. Nonnegativity then bounds $P(A)$ above by one. If $A\subseteq B$, decompose $B=A\mathbin{\dot\cup}(B\setminus A)$; subtracting gives $P(B)-P(A)=P(B\setminus A)\ge0$.

For inclusion–exclusion, decompose $A\cup B$ into the disjoint events $A\setminus B$, $A\cap B$ and $B\setminus A$. Adding their probabilities counts the intersection once. Adding $P(A)+P(B)$ counts it twice, so subtracting $P(A\cap B)$ gives the displayed formula. Dropping this nonnegative intersection term yields $P(A\cup B)\le P(A)+P(B)$, the two-event union bound.{{cite:openintro2019}} (§3.1.4, pp. 85–86, general addition rule)

## Intuition — Complements and unions express different questions
A complement asks whether an event fails to occur, so it refers to all outcomes outside that event. A union asks whether at least one of several events occurs. The phrase “either A or B” must be interpreted carefully, because an inclusive union permits both. If exactly one is intended, the event is the symmetric difference, with probability $P(A)+P(B)-2P(A\cap B)$. These are set operations before they are numerical formulas.{{cite:openintro2019}} (§3.1.4, pp. 85–86; §3.1.6, p. 89, inclusive union and complement)

Independence is another distinct relationship. It means $P(A\cap B)=P(A)P(B)$, whereas disjointness means the intersection is empty. Two disjoint events with positive probabilities cannot be independent, because their intersection probability is zero while their product is positive. Confusing these conditions gives a wrong probability even when each marginal probability has been estimated well.{{cite:openintro2019}} (§3.1.7, p. 91, product formula for independent events)

## Worked example
### Overlapping machine faults
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
The axiom $P(\varnothing)=0$ does not assert the converse. In a continuous uniform model on [0,1], any specified singleton has probability zero while still containing an outcome. Conversely, a probability-one event can omit a null set. Statements about almost-sure behaviour should therefore distinguish measure from set equality.{{cite:openintro2019}} (§3.5.2, p. 127, continuous probability as area)

## Key results — Three events need every intersection that the formula names
Apply the two-event identity to $A\cup B$ and then to $(A\cup B)\cup C$. The intersections that appear are the three pairwise intersections and the triple intersection. The resulting expansion is
$$P(A\cup B\cup C)=P(A)+P(B)+P(C)-P(A\cap B)-P(A\cap C)-P(B\cap C)+P(A\cap B\cap C).$$
Suppose the three probabilities are $1/2$, $2/5$ and $3/10$, the pairwise intersections are $1/5$, $1/10$ and $1/10$, and the triple intersection is $1/20$. The union probability is $17/20=0.85$. Dropping the triple term would leave $0.80$, and dropping every intersection would leave the sum $1.2$, which is not a probability. The same expansion shows why a reported list of marginal fault probabilities is not yet a probability for “at least one fault.”{{cite:dodge2008}} (Probability, pp. 430–432)

The union bound iterates without those intersections. For events of probabilities $0.2$, $0.25$ and $0.4$, the probability of the union is at most $0.85$, whether or not the events are independent. Equality holds when the events are pairwise disjoint, because every subtracted intersection is then zero. If the events can overlap, $0.85$ remains an upper bound and the marginal probabilities alone do not identify the union. This is the same nonnegativity argument used for two events, applied to the disjoint pieces of a finite union.{{cite:dodge2008}} (Probability, pp. 430–432, countable additivity)

## History — The axioms fix one assignment before any sampling story
The nonnegativity, total-mass and countable-additivity requirements are properties of one set function on one collection of events. Finite additivity for two disjoint events is the special case used to prove the complement rule and the two-event union formula. Countable additivity is the further requirement that turns a sequence of disjoint pieces into a convergent series of probabilities, which is what justifies the continuity statement for an increasing sequence of events. A sampling design, a long-run frequency and a stated degree of belief are interpretations of a probability once such an assignment has been specified. They do not license adding marginal probabilities that refer to different experiments.{{cite:dodge2008}} (Probability, pp. 430–432)

## Related concepts
Independence of two events is the product rule for their intersection. A [simple random sample](simple-random-sample.qmd) makes a stronger uniformity statement: every subset of a fixed size receives the same probability, which determines the inclusion probabilities and their dependence. Disjointness, independence and equal inclusion are three different constraints. Two of them can fail while the third holds, as when every unit has the same chance of entering a sample but some pairs of units can never enter together.{{cite:dodge2008}} (Simple Random Sampling, pp. 497–498){{cite:dodge2008}} (Probability, pp. 430–432)

## Statistical use — Express risks as events before adding them
For a collection of risks, specify the sample space and the event corresponding to each reported number before combining them. The union bound gives a conservative upper bound on the probability of at least one event without requiring independence; inclusion–exclusion gives an exact calculation when intersections are known. These choices make clear which information is supplied by data and which comes from assumptions about how events overlap.{{cite:openintro2019}} (§3.1.4, pp. 85–86, general addition rule)
