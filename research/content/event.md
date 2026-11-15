## Lead context
An event turns a question about an uncertain experiment into a precise collection of outcomes: it happens exactly when the observed outcome belongs to that collection. Events can be combined to describe “either,” “both,” and “not,” making them the objects to which a probability measure assigns numbers. In an infinite model, only the subsets chosen as measurable events receive probabilities.{{cite:kolmogorov1933_slln,grimmett_stirzaker2020}}

## Motivating example
For one roll of a fair die, “an even result” is the event $\{2,4,6\}$, whereas “greater than four” is $\{5,6\}$. The outcome $6$ belongs to both events. Before adding their probabilities to find the chance of either question being true, that overlap must be counted once rather than twice. Specifying events as sets makes the correction visible.{{cite:feller1968}}

## Intuition
An outcome is one possible complete result of the experiment; an event may contain many outcomes or none. A single observation either belongs to an event or does not. The sample space describes what can occur, while the event describes the question being asked of that result. Changing what is recorded can change the sample space and hence the sets available to express a question. For example, recording only the number of heads in two coin tosses cannot distinguish heads–tails from tails–heads, while recording the ordered sequence can.{{cite:kolmogorov1933_slln,feller1968}}

## Definition
Let $\Omega$ be a [sample space](sample-space.qmd), and let $\mathcal F$ be a collection of subsets of $\Omega$ closed under complements and countable unions and containing $\Omega$. Such a collection is a *sigma-algebra*. An **event** is a member $A\in\mathcal F$; it occurs if the observed outcome $\omega\in\Omega$ belongs to $A$. A [probability measure](probability-measure.qmd) $\mathbb P$ assigns a number $\mathbb P(A)$ to each $A\in\mathcal F$, with $\mathbb P(\Omega)=1$ and countable additivity for disjoint events. The triple $(\Omega,\mathcal F,\mathbb P)$ is the probability space. On a finite sample space one may take $\mathcal F$ to be all subsets; on a continuous space the choice of measurable subsets matters.{{cite:kolmogorov1933_slln,billingsley1995}}

The event $A^c=\Omega\setminus A$ occurs when $A$ does not; $A\cup B$ occurs when at least one of $A,B$ does; $A\cap B$ occurs when both do. The events are *disjoint* when $A\cap B=\varnothing$. The empty event $\varnothing$ is impossible and $\Omega$ is certain in this mathematical model. An event can nevertheless have probability zero without being empty: for a continuous uniform draw from $[0,1]$, the event $\{1/2\}$ is possible as a set of outcomes but has probability zero.{{cite:kolmogorov1933_slln,billingsley1995}}

## Properties
If $A\subseteq B$, occurrence of $A$ guarantees occurrence of $B$, and $\mathbb P(A)\le\mathbb P(B)$. Complementation gives $\mathbb P(A^c)=1-\mathbb P(A)$. For disjoint events, $\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)$; in general, subtract the overlap: $\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B)$. These identities make an event expression a calculation, once the required probabilities are supplied.{{cite:kolmogorov1933_slln,feller1968}}

De Morgan's laws express the logic of failure as set identities: $(A\cup B)^c=A^c\cap B^c$ and $(A\cap B)^c=A^c\cup B^c$. For a series system that needs both components, failure means at least one component fails. For a parallel system that needs either component, failure means both fail. These identities describe the event without assuming component independence; independence enters only if the probability of an intersection is replaced by a product.{{cite:feller1968,grimmett_stirzaker2020}}

For events $A_1,A_2,\ldots$, the union bound gives $\mathbb P(\bigcup_i A_i)\le\sum_i\mathbb P(A_i)$. Its value is that it needs no independence assumption. In particular, a small upper bound on the sum of many failure probabilities also bounds the chance of at least one failure.{{cite:billingsley1995}}

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Because $\Omega=A\sqcup A^c$ is a disjoint union, additivity and $\mathbb P(\Omega)=1$ give $\mathbb P(A^c)=1-\mathbb P(A)$. Setting $A=\Omega$ also gives $\mathbb P(\varnothing)=0$. If $A\subseteq B$, then $B=A\sqcup(B\setminus A)$, so nonnegativity yields $\mathbb P(B)\ge\mathbb P(A)$. Here $\sqcup$ marks a disjoint union.{{cite:kolmogorov1933_slln}}

The set $A\cup B$ is the disjoint union of $A$ and $B\setminus A$; $B$ is the disjoint union of $A\cap B$ and $B\setminus A$. Apply additivity to both and eliminate $\mathbb P(B\setminus A)$ to get inclusion–exclusion. If $A\cap B=\varnothing$, its final term is zero. De Morgan's first identity follows by checking an outcome $\omega$: it is outside $A\cup B$ exactly when it is outside both $A$ and $B$. The second follows by the same membership check with “both” and “either” exchanged.{{cite:kolmogorov1933_slln,feller1968}}

For a finite or countable family, put $B_1=A_1$ and $B_i=A_i\setminus\bigcup_{j<i}A_j$ for $i>1$. The $B_i$ are disjoint, have the same union as the $A_i$, and satisfy $B_i\subseteq A_i$. Countable additivity and monotonicity therefore give $\mathbb P(\bigcup_i A_i)=\sum_i\mathbb P(B_i)\le\sum_i\mathbb P(A_i)$, proving the union bound.{{cite:billingsley1995}}
:::
:::

## Statistical use
Define a rejection event before calculating a [p-value](p-value.qmd): its outcomes are the test statistics at least as extreme as the observed statistic under the stated null model. The probability of that event depends on both the statistic and the null distribution. In a reliability calculation, define “system works” as a union or intersection of component events, then apply the component failure model. In either case, writing the event first separates the question from any assumptions, such as independence, used to compute its probability.{{cite:grimmett_stirzaker2020,feller1968}}

The choice of observed information also matters for [conditional probability](conditional-probability.qmd). If $B$ is the event known to have occurred and $\mathbb P(B)>0$, then $\mathbb P(A\mid B)=\mathbb P(A\cap B)/\mathbb P(B)$. This is a probability of an intersection relative to the conditioning event, not a new definition of what outcomes constitute $A$. A zero-probability $B$ cannot be inserted into this ratio; more general conditioning on continuous observations requires conditional distributions.{{cite:kolmogorov1933_slln,billingsley1995}}

## Worked example
Roll a fair six-sided die and let $A=\{2,4,6\}$ be “even” and $B=\{4,5,6\}$ be “at least four.” The two events overlap in $A\cap B=\{4,6\}$, so $\mathbb P(A\cap B)=2/6=1/3$. Their union is $\{2,4,5,6\}$ and has probability $4/6=2/3$. Inclusion–exclusion agrees: $3/6+3/6-2/6=4/6$. Conditioning on $B$ gives $\mathbb P(A\mid B)=(2/6)/(3/6)=2/3$; two of the three outcomes in $B$ are even.{{cite:feller1968}}

**Your turn.** In the same experiment, find the event “neither even nor at least four,” and its probability.

::: {.callout-tip collapse="true" title="Answer"}
Its outcomes are $(A\cup B)^c=\{1,3\}$. There are two of the six equally likely outcomes, so its probability is $2/6=1/3$. De Morgan's law gives the same event as $A^c\cap B^c$.
:::

## Common misconceptions
An event is a set of outcomes, not its numerical probability. Disjoint events cannot occur together, whereas independent events can occur together; disjoint nonempty events of positive probability cannot be independent. A nonempty event can have probability zero in a continuous model. In a general uncountable sample space, “every subset has a probability” is too strong: the probability measure is defined on the specified sigma-algebra. Finally, an overlapping union cannot be evaluated by simply adding its two probabilities.{{cite:kolmogorov1933_slln,billingsley1995}}

## Assumptions and limits
The set identities and union bound require no independence. Calculating probabilities from equal outcome counts does require a finite space with equal probability for each elementary outcome. The aircraft example below assumes independent engine failures with a common failure probability; its event expression remains correct even if either assumption fails, but the numerical product formula would change. In a continuous model, the choice of sigma-algebra and probability measure is part of the model, and probability-zero sets need not be logically impossible.{{cite:feller1968,billingsley1995}}

## Connections
The [sample space](sample-space.qmd) supplies possible outcomes; a [probability measure](probability-measure.qmd) assigns weights to its measurable events. A [sigma-algebra](generated-and-borel-sigma-algebras.qmd) specifies which subsets stay measurable under complements and countable combinations. [Conditional probability](conditional-probability.qmd) rescales an intersection relative to a positive-probability event, while [independent events](independent-events.qmd) satisfy $\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)$. A [random variable](random-variable.qmd) links numerical statements back to events through preimages such as $\{\omega:X(\omega)\le x\}$.{{cite:kolmogorov1933_slln,billingsley1995}}

## Check yourself
[Matching faces](../questions/ex-prob-two-dice-faces.qmd) asks for a probability from an event in a two-dice experiment. [A zero received](../questions/ex-prob-channel-zero.qmd) tests conditional events in a noisy communication model. [The larger coordinate](../questions/ex-prob-unit-square-max.qmd) turns $\{\max(X,Y)\le z\}$ into a square in a continuous sample space.

## History
In *Grundbegriffe der Wahrscheinlichkeitsrechnung* (1933), Andrey Kolmogorov formulated probability using a collection of subsets he called random events and an additive probability assignment. His opening chapter treated finitely many events, separating the formal set operations from their interpretation as experimental outcomes. He illustrated this with two coin tosses, where a repeated face corresponds to two of the four ordered outcomes. This is a verified source for the event-as-set formulation, not a claim that he first used the word *event*.{{cite:kolmogorov1933_slln}}

The same work then added the countable structure needed for sequences of events. Modern probability texts formulate that structure as a sigma-algebra and a countably additive measure, so events such as a tail union or the event that infinitely many trials satisfy a condition remain within the probability model. This is the formal extension of the finite event calculations used in elementary examples.{{cite:kolmogorov1933_slln,billingsley1995,grimmett_stirzaker2020}}
