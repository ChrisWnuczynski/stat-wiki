## Lead context
Knowing that an event occurred changes which outcomes are still possible. Conditional probability gives the probability of another event within that restricted set, while preserving the original relative weights of the outcomes that remain. It underlies sequential sampling, diagnostic calculations, independence, and Bayes' rule. The event after the bar must have positive probability for the elementary quotient to be defined.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 133–135)

## Motivating example
In Dodge's table of 100 cars, 40 are both fast and comfortable, 10 are comfortable but slow, 20 are fast but uncomfortable, and 30 are neither. Among the 50 comfortable cars, 40 are fast, so the fast proportion *given comfort* is $40/50=4/5$. Among the 60 fast cars, 40 are comfortable, so the comfortable proportion *given speed* is $40/60=2/3$. The same intersection sits in both numerators, but the questions select different denominators. A statement such as “40 cars have both traits” is a joint count and does not answer either conditional question by itself.{{cite:dodge2008}} (pp. 105–106)

## Intuition
Conditioning is a change of reference population. First restrict attention to the outcomes satisfying $B$; then ask what fraction of their probability mass also satisfies $A$. If all elementary outcomes have equal probability, counting within $B$ works. If they have unequal probabilities, count *mass* instead of outcomes. This is why merely removing impossible outcomes and declaring the rest equally likely can fail in the Monty Hall example: the host's rule gives the remaining paths different weights.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 134–135, 137–139)

The vertical bar reads “given.” It does not say that $B$ caused $A$, that $B$ happened earlier, or that one has learned $B$ through a perfectly reliable measurement. The probability law and the definition of $B$ must already specify what is being conditioned on. In an observational table, a change from $\mathbb P(A)$ to $\mathbb P(A\mid B)$ is a change in subgroup, not automatically a causal effect.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 133–135)

## Definition
For events $A$ and $B$ with $\mathbb P(B)>0$, set $\mathbb P(A\mid B)=\mathbb P(A\cap B)/\mathbb P(B)$. For fixed $B$, this defines a probability law on events: $\mathbb P(\Omega\mid B)=1$, it is nonnegative, and it is additive over disjoint events. In particular, $\mathbb P(B\mid B)=1$ and $\mathbb P(B^c\mid B)=0$. The quotient is a property of the joint law of $A$ and $B$; neither marginal probability alone determines it.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 134–135)

For a finite sample space with atom masses $p(\omega)$, the conditional mass is $p(\omega\mid B)=p(\omega)/\mathbb P(B)$ for $\omega\in B$ and zero otherwise. The masses over $B$ sum to one. In a continuous sample space, the analogous density restriction and renormalisation apply when $B$ has positive probability. Conditioning on a particular value of a continuous random variable, which often has probability zero, instead requires a conditional distribution; the event quotient does not assign it a value.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, p. 134; §4.2, pp. 162–163){{cite:durrett2019}} (Ch. 4, §4.1)

## Properties
The two-event product rule is $\mathbb P(A\cap B)=\mathbb P(A\mid B)\mathbb P(B)$ when $\mathbb P(B)>0$. Repeated use gives the chain rule for several events, with each conditioning intersection required to have positive probability. This is the right calculation for draws without replacement: the composition of an urn changes after each draw. The three-black-ball calculation uses exactly these changing denominators.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 135–136)

For a disjoint exhaustive partition $B_1,\ldots,B_k$, the law of total probability adds $\mathbb P(A\cap B_i)$ across the cells. Each positive-probability cell contributes $\mathbb P(A\mid B_i)\mathbb P(B_i)$; a zero-probability cell contributes zero without needing an undefined conditional. Bayes' rule reverses the conditioning by dividing one cell contribution by that total. These are bookkeeping identities for the same joint probabilities, not three unrelated formulas.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 135–137)

Events $A$ and $B$ are independent precisely when their joint probability factors as $\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)$. If $\mathbb P(B)>0$, this is equivalent to $\mathbb P(A\mid B)=\mathbb P(A)$. Conditioning then leaves the probability of $A$ unchanged. A large or small unconditional probability of $B$ says nothing by itself about whether independence holds.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 139–140)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For fixed $B$ with positive mass, nonnegativity follows from nonnegativity of $\mathbb P(A\cap B)$. Also $\mathbb P(\Omega\mid B)=\mathbb P(B)/\mathbb P(B)=1$. If $A_1,A_2,\ldots$ are disjoint, then the events $A_i\cap B$ are disjoint, so countable additivity of the original law gives $\mathbb P(\bigcup_i A_i\mid B)=\sum_i\mathbb P(A_i\mid B)$. This also proves the complement rule $\mathbb P(A^c\mid B)=1-\mathbb P(A\mid B)$.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 134–135){{cite:durrett2019}} (Ch. 1, §1.1)

Multiplying the defining quotient by $\mathbb P(B)$ gives the two-event product rule. Apply that rule successively to $A_1$, $A_1\cap A_2$, and so on; the intermediate intersection probabilities cancel, leaving the chain product. For the partition, $A$ is the disjoint union of $A\cap B_i$, hence $\mathbb P(A)=\sum_i\mathbb P(A\cap B_i)$. Replacing each nonzero term by the product rule gives total probability. Dividing the joint term for $B_j$ by $\mathbb P(A)>0$ gives Bayes' rule. Finally, substituting the definition into $\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)$ proves the independence equivalence.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 135–140)
:::
:::

## Statistical use
In a two-way frequency table, identify the condition before taking a ratio. To estimate a conditional proportion for $A$ given $B$, divide the count in $A\cap B$ by the count in the $B$ row or column. Dividing by the grand total estimates a *joint* proportion; dividing by the $A$ margin answers the reversed question. The table alone supports a descriptive conditional proportion. Generalising it to a population probability requires a sampling model, and causal interpretation requires further assumptions about how the groups were formed.{{cite:dodge2008}} (pp. 105–106){{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 133–135)

In a multistage model, draw a probability tree with the condition at each branch. Multiply along a path to obtain a joint probability, sum paths to obtain an event probability, then divide only if a reverse conditional is requested. This makes the denominator visible in diagnostic, mixture, and reliability calculations. It also exposes missing assumptions: a host's choice rule, a sampling design, or the distribution of the first stage cannot be silently supplied after the calculation.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 135–139)

## Worked example
Consider a hypothetical record of 200 journeys. It rained on 40, 30 journeys were late, and 18 were both rainy and late. The four cell counts are therefore 18 rainy-and-late, 22 rainy-and-on-time, 12 dry-and-late, and 148 dry-and-on-time. They sum to 200. Among rainy journeys, the late proportion is $18/40=0.45$. Among late journeys, the rainy proportion is $18/30=0.60$. The joint proportion is $18/200=0.09$, and the late proportion among dry journeys is $12/160=0.075$. Thus the two conditionals, the joint probability, and the dry subgroup probability all answer different questions. No causal effect of rain follows from these counts alone.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 134–135)

**Your turn.** In another hypothetical table of 120 journeys, 45 are rainy, 30 are late, and 15 are both. Find the late proportion given rain, the rainy proportion given lateness, and the late proportion given a dry journey. First fill in the fourth cell so that your denominators can be checked.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 134–135)

::: {.callout-tip collapse="true" title="Answer"}
The rainy-and-on-time count is $45-15=30$; the dry-and-late count is $30-15=15$; the dry-and-on-time count is $120-15-30-15=60$. Hence $\mathbb P(\text{late}\mid\text{rain})=15/45=1/3$, $\mathbb P(\text{rain}\mid\text{late})=15/30=1/2$, and $\mathbb P(\text{late}\mid\text{dry})=15/75=1/5$ in this empirical table. The denominators are the sizes of the rain, late, and dry subgroups respectively.
:::

**A further exercise.** In Dodge's table of 100 cars, 40 are both fast and comfortable, 10 are comfortable but slow, 20 are fast but uncomfortable, and 30 are neither. What is the probability a car is comfortable, given that it is slow?

::: {.callout-tip collapse="true" title="Answer"}
The slow cars are the 10 comfortable slow cars and the 30 that are neither, so there are 40 slow cars. Among them, 10 are comfortable, and $10/40=1/4$.
:::

## Common misconceptions
The joint probability $\mathbb P(A\cap B)$ is not generally the conditional probability $\mathbb P(A\mid B)$; the latter divides by $\mathbb P(B)$. Reversing the bar also changes the denominator. In Dodge's car table, $4/5$ and $2/3$ arise from the same 40 cars, but neither ratio can be substituted for the other. Conditioning also does not force the remaining outcomes to be equiprobable: that shortcut is valid only when their original masses agree.{{cite:dodge2008}} (pp. 105–106){{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 134–135)

## Assumptions and limits
The event formula requires $\mathbb P(B)>0$. When $\mathbb P(B)=0$, the ratio is $0/0$ because $A\cap B\subseteq B$; it gives no conditional probability. A model may still specify a conditional law at a continuously valued observation through densities or a regular conditional distribution, but that is an additional construction and may be unique only outside a null set of conditioning values. Independence does not rescue division by zero; use the factorisation definition instead.{{cite:grinstead_snell1997}} (Ch. 4, §4.1, pp. 134, 139–140; §4.2, pp. 162–163){{cite:durrett2019}} (Ch. 4, §4.1)

## Connections
The [product rule](product-rule.qmd) reconstructs a joint probability from a conditional and a marginal. The [law of total probability](law-of-total-probability.qmd) combines conditional probabilities across a partition, and [Bayes' rule](bayes-rule.qmd) reverses their direction. [Conditional distributions](conditional-distribution.qmd) extend the idea to random variables; [conditional expectation](conditional-expectation.qmd) averages under such a distribution. [Independent events](independent-events.qmd) are the special case in which conditioning on one positive-probability event does not change the other event's probability.{{cite:grinstead_snell1997}} (Ch. 4, §§4.1–4.2, pp. 134–140, 162–163)
