## Lead context
Probability theory is the mathematical study of outcomes, events, and the limit behaviour of random quantities. It starts from a set of outcomes, a collection of events closed under the operations the theory uses, and a probability that assigns each event a number. The number is constrained by axioms. The axioms do not say whether the number was justified by symmetry, by a long-run frequency, or by a degree of belief. That justification is an interpretation. The theory is the arithmetic and the limit laws that follow once an assignment has been made.{{cite:durrett2019}} (Ch. 1, §1.1, pp. 1–2){{cite:dodge2008}} (pp. 430–432)

## Motivating example
Two fair coins are tossed. The outcomes are HH, HT, TH, and TT. If the coins are judged exchangeable and independent, each outcome receives probability $1/4$. The event "at least one head" contains three of the four outcomes and receives probability $3/4$. The event "no heads" is the complement and receives probability $1/4$. Nothing in the arithmetic says the coins are fair. The fairness is the assignment. The arithmetic says what that assignment implies for every event built from the four outcomes, including events that were not the ones used to write the four probabilities down.

A second question uses the same space and is easy to get wrong. The event "the first coin is heads" has probability $1/2$. Its overlap with "at least one head" is itself. Adding the two probabilities, $3/4+1/2$, double-counts the overlap and exceeds $1$. The union rule subtracts the overlap once. The theory is the discipline that makes that subtraction compulsory.

## Definition
A probability space is a triple $(\Omega, \mathcal F, \mathbb{P})$. The set $\Omega$ contains the outcomes. The collection $\mathcal F$ contains the events, which are subsets of $\Omega$. The function $\mathbb{P}$ assigns each event a number in $[0, 1]$.

Durrett requires $\mathcal F$ to be a $\sigma$-field: it is nonempty, the complement of an event is an event, and the union of a countable sequence of events is an event. The intersection of a countable sequence is then an event as well, because the intersection of the $A_i$ is the complement of the union of the complements. A measure is a nonnegative countably additive set function with $\mu(\emptyset)=0$. A probability measure is a measure with $\mu(\Omega)=1$. Countable additivity says that if the $A_i$ are disjoint events, the probability of their union is the sum of their probabilities.{{cite:durrett2019}} (Ch. 1, §1.1, pp. 1–2)

Dodge gives the same skeleton for a finite space $\Omega=\{x_1,\ldots,x_n\}$ in three clauses. The probability of each outcome is nonnegative. The probabilities of the outcomes sum to $1$. The probability is a function from the outcomes into $[0, 1]$. The frequency route to the same function repeats an experiment and sets

$$
\mathbb{P}(A)=\lim_{n\to\infty}\frac{n_A}{n},
$$


when the limit exists. The axiomatic route simply requires the three properties and then derives the rest.{{cite:dodge2008}} (pp. 430–432)

The consequences used in every calculation are short. The probability of the sample space is $1$. The probability of the empty event is $0$. The probability of a complement is one minus the probability of the event. Incompatible events add. For any two events,

$$
\mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B).
$$


These are theorems of the axioms, not extra axioms. A classical assignment on a finite set of equally likely atoms produces them by counting. A frequency in a finite record produces them by counting occurrences. A coherent betting assignment produces them because a violation would allow a sure loss. The theory does not mind which story was used. It minds that the numbers obey the rules.{{cite:dodge2008}} (p. 432)

A random variable is a function from the outcomes to the numbers, measurable in the sense that the set of outcomes on which it falls in a given interval is an event. Its distribution is the probability that function assigns to intervals. Expectation, variance, and the laws of large numbers are properties of that distribution. They are not part of the definition of the probability space, and they are not available until a random variable has been named.

## Interpretation
The probability of an event is the number $\mathbb{P}$ assigns to that set. It is not a property of a single outcome inside the set, and it is not a frequency that has already been observed, unless the assignment was built from that frequency. In the two-coin space, $3/4$ is the probability of a set of three outcomes. It is not the probability of HH, which is $1/4$, and it does not say that three out of the next four tosses will show a head.

Conditional probability is a second assignment on a smaller space. If $\mathbb{P}(B)>0$,

$$
\mathbb{P}(A\mid B)=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(B)}.
$$


In the two-coin space, the conditional probability of two heads, given at least one head, is $(1/4)/(3/4)=1/3$. The conditioning event has removed TT and renormalised the remaining three outcomes. The conditional probability is not the original probability of HH, and it is not the probability of the conditioning event.

Independence is a restriction on the assignment: $\mathbb{P}(A\cap B)=\mathbb{P}(A)\mathbb{P}(B)$. For the two coins, "first coin heads" and "second coin heads" each have probability $1/2$, and their intersection HH has probability $1/4$, which equals the product. Independence was put in by the assignment. It is not a consequence of the axioms for an arbitrary pair of events. "At least one head" and "first coin heads" are not independent: the intersection has probability $1/2$, and the product of the probabilities is $(3/4)\cdot(1/2)=3/8$.

A discrete probability space may be infinite, provided the outcomes are countable and the weights are nonnegative and sum to $1$. The probability of an event is the sum of the weights of the outcomes it contains. An uncountable space, such as the real line, cannot put equal positive weight on every point, because a sum of uncountably many equal positive numbers is not a probability. The probability then lives on intervals, through a density or a more general measure. A continuous distribution assigns probability $0$ to every single point and positive probability to intervals. That is a theorem about the assignment. The point can still be the outcome that occurs.{{cite:durrett2019}} (Ch. 1, §1.1, pp. 1–2)

The interpretation of the number, as a symmetry, a frequency, or a degree of belief, is settled outside the axioms. Gelman's account of the mathematical definition is the one the theory uses: nonnegative, additive over mutually exclusive outcomes, and summing to $1$. Which story justified the number is a separate paragraph. Probability theory proceeds with the number.{{cite:gelman_bda2013}} (pp. 11–12)

## Worked example
Take $\Omega=\{\mathrm{HH}, \mathrm{HT}, \mathrm{TH}, \mathrm{TT}\}$ with $\mathbb{P}=1/4$ on each outcome. Let $A$ be "at least one head," so $A=\{\mathrm{HH}, \mathrm{HT}, \mathrm{TH}\}$ and $\mathbb{P}(A)=3/4$. Let $B$ be "the first coin is heads," so $B=\{\mathrm{HH}, \mathrm{HT}\}$ and $\mathbb{P}(B)=1/2$. Then $A\cap B=B$, and

$$
\mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B)=\tfrac34+\tfrac12-\tfrac12=\tfrac34.
$$


The union is $A$, which is why the probability comes back to $3/4$. The complement of $A$ is $\{\mathrm{TT}\}$, with probability $1-3/4=1/4$. The conditional probability $\mathbb{P}(B\mid A)=(1/2)/(3/4)=2/3$: given at least one head, the first coin is heads in two of the three remaining outcomes.

The empty event has probability $0$. One way to see it from the axioms is that $\Omega$ and $\emptyset$ are disjoint and their union is $\Omega$, so $\mathbb{P}(\Omega)=\mathbb{P}(\Omega)+\mathbb{P}(\emptyset)$, hence $\mathbb{P}(\emptyset)=0$. Adding a nonempty event's probability to $0$ does not change it. That is the calculation the union rule uses when the intersection is empty.{{cite:dodge2008}} (p. 432){{cite:durrett2019}} (Ch. 1, §1.1, p. 1)

**Your turn.** In the same two-coin space, let $C$ be "the two coins agree," so $C=\{\mathrm{HH}, \mathrm{TT}\}$. Find $\mathbb{P}(C)$ and $\mathbb{P}(A\cap C)$.

::: {.callout-tip collapse="true" title="Answer"}
$C$ contains two of the four outcomes, so $\mathbb{P}(C)=1/2$. The intersection $A\cap C$ is $\{\mathrm{HH}\}$, so $\mathbb{P}(A\cap C)=1/4$.
:::

## Connections
The set function $\mathbb{P}$ is a [probability measure](probability-measure.qmd). The stories that justify a particular $\mathbb{P}$, and the fact that the stories can disagree about which number to write, are the [probability interpretations](probability-interpretations.qmd). A conditional probability computed after data, for a set of parameter values, is a [posterior probability](posterior-probability.qmd). The sampling model that sits inside that calculation is an ordinary probability space for the observations given the parameter. The long-run frequency of an estimator across repeated samples is a probability in the frequency reading of this theory. It is not, by that fact, the posterior probability of a parameter.

Countable additivity is what lets a probability be assigned to a union of disjoint events by summing, including a countably infinite union. Finite additivity is the special case of two events, which is the union rule used in the coin example. A space that is only finitely additive can still compute $\mathbb{P}(A\cup B)$. It cannot, by that finite rule alone, pass from a sequence of disjoint events to the probability of all of them together. The $\sigma$-field is the matching restriction on which sets are events, so that the union being measured is a set $\mathbb{P}$ is allowed to see.{{cite:durrett2019}} (Ch. 1, §1.1, pp. 1–2){{cite:dodge2008}} (pp. 430–432)

## History
Games of chance are the early source of the calculations. Dodge traces dice and astragals to antiquity, and cards to the late medieval West. The mathematical development in Europe is marked by Cardano, Galileo's use of equiprobability for dice, Huygens's 1657 treatise, and the correspondence of Pascal and Fermat on the problem of points: how to divide the stake when a game is interrupted with $n$ and $p$ plays already won. Pascal found a recurrence that matches Fermat's count. The frequency definition, as a limit of relative frequencies in repeated trials, and the axiomatic definition, as a nonnegative countably additive set function with total mass $1$, are two routes for turning that history into a calculus. The measure-theoretic form, with an explicit $\sigma$-field so that every set the theory mentions is an event, is the form in which Durrett starts the subject: outcomes, events, and a probability measure of total mass $1$.{{cite:dodge2008}} (pp. 430–432){{cite:durrett2019}} (Ch. 1, §1.1, pp. 1–2)
