## Lead context
Probability interpretations are the accounts of what a probability number means. The axioms constrain the arithmetic. They do not choose among a ratio of equally likely cases, a long-run relative frequency, and a degree of uncertainty about a single event. A statistical argument that treats one of those readings as if it were another answers a different question from the one that was asked.{{cite:gelman_bda2013}} (pp. 11–12){{cite:dodge2008}} (pp. 430–431)

## Motivating example
A coin can be assigned probability $1/2$ of heads because the two faces are judged exchangeable. The same coin, tossed $10$ times and landing heads $3$ times, has relative frequency $3/10$. Both numbers are probabilities under some reading: one is a judgement about the toss, and the other is a summary of a finite record. Using $3/10$ as the symmetry assignment, or using $1/2$ as a description of those ten tosses, mixes the two jobs.{{cite:gelman_bda2013}} (p. 12){{cite:dodge2008}} (p. 430)

## Intuition
The number is asked to do several jobs in ordinary speech. It can report how many of a list of equally serious possibilities fall inside an event. It can report how often an event has occurred in a long run of repetitions. It can report how strongly an uncertain claim is believed, including a claim about a single case that will not be repeated. Each job suggests a way to arrive at the number. Once the number is in hand, the addition and complement rules are common property. The interpretation is the story that justified writing the number down.{{cite:gelman_bda2013}} (pp. 11–12){{cite:dodge2008}} (pp. 430–432)

## Definition
Three readings cover the uses that statistical work actually makes.

The classical, or symmetry, reading sets the probability of an event equal to the number of favourable cases divided by the number of possible cases, when the cases are judged equally likely. For a coin this is a claim about the physical toss, not a convention that every experiment has equally likely atoms. Galileo's writings on dice already use that equiprobability.{{cite:gelman_bda2013}} (p. 12){{cite:dodge2008}} (p. 431)

The frequency reading sets the probability equal to the limit of the relative frequency in a sequence of repetitions, taken to be performed in the same way and independently. If $n_A$ is the number of times event $A$ occurs in the first $n$ repetitions, the probability is $\lim n_A/n$. A single trial that is not thought of as one member of such a sequence has no probability under a strict form of this reading. A reference set can sometimes be constructed, for example by treating a future rocket launch as one of a class of comparable launches.{{cite:gelman_bda2013}} (p. 12){{cite:dodge2008}} (p. 430)

The uncertainty reading sets the probability equal to a degree of belief about an event or an unknown, whether or not a sequence of repetitions is available. It is equally available for "rain tomorrow" and for the chance that a coin lands heads. This is [Bayesian probability](bayesian-probability.qmd).{{cite:gelman_bda2013}} (pp. 11–12)

An axiomatic reading does not pick one of these stories. It requires a nonnegative assignment on events that gives the whole sample space probability one and adds over incompatible events. The frequency limit is one way to justify the numbers. The axioms are what calculations then use.{{cite:dodge2008}} (pp. 430–432)

## Statistical use
A sampling model is a probability assignment for observations given parameters. It is often motivated by symmetry, by a frequency in a population, or by a physical story that plays the role of a reference set. A prior distribution for a parameter uses the uncertainty reading, because the parameter is not itself a draw in the sample. Reporting both, and saying which reading each number uses, is part of stating a [Bayesian model](bayesian-model.qmd). An interval procedure calibrated by the frequency of coverage across repeated samples is not, by that calibration alone, a posterior probability that the parameter lies in one computed interval.{{cite:gelman_bda2013}} (pp. 11–12){{cite:dodge2008}} (p. 430)

[Bayesian statistics](bayesian-statistics.qmd) uses the uncertainty reading for unknowns and, typically, a frequency or symmetry reading for the sampling model given the unknowns. Keeping those two readings labelled is what stops a coverage frequency from being quoted as the probability of a parameter.{{cite:gelman_bda2013}} (pp. 11–12)

## Worked example
Judge a coin's two faces exchangeable. The classical probability of heads is $1/2$, one favourable face out of two. Suppose a record of $10$ tosses contains $3$ heads. The relative frequency in the record is $3/10$. The two figures answer different questions: $1/2$ is the symmetry assignment for a single toss under that judgement, and $3/10$ is the proportion of heads in those ten tosses. A frequency interpretation of the coin's probability would treat $3/10$ as an estimate from a short sequence, not as a replacement for the symmetry assumption, unless the symmetry assumption is withdrawn.{{cite:gelman_bda2013}} (p. 12){{cite:dodge2008}} (p. 430)

**Your turn.** The next record has $60$ heads in $100$ tosses. What is the relative frequency of heads, as a fraction in lowest terms?

::: {.callout-tip collapse="true" title="Answer"}
The relative frequency is $60/100=3/5$.
:::

## Common misconceptions
The axioms do not say that elementary outcomes are equally likely. Equal likelihood is the extra judgement in the classical reading. A relative frequency in a finite record is a property of that record. Identifying it with the probability in the sampling model is a further step, and a short record can sit far from the probability that generated it. A degree of belief about a parameter is not a relative frequency of the parameter. Both the symmetry argument and the frequency argument still require a judgement, about the coin and about the tossing procedure. Neither is a report that has been read off the axioms alone.{{cite:gelman_bda2013}} (pp. 11–12){{cite:dodge2008}} (pp. 430–432)

## Connections
The rules common to the readings are developed in [probability theory](probability-theory.qmd), and the set function that satisfies them is a [probability measure](probability-measure.qmd). The uncertainty reading, applied to parameters and single cases, is [Bayesian probability](bayesian-probability.qmd). The early history of the numbers is the history of games of chance: dice, cards, and the problems Pascal and Fermat solved for a gambler who asked how the stake should be divided. A frequency account, tying probability to repeated trials, runs alongside that history. Extending the same numbers to an unknown chance given the data is the step that produced inverse probability.{{cite:dodge2008}} (pp. 431–432){{cite:gelman_bda2013}} (pp. 11–12)
