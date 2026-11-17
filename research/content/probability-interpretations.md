## Lead context
Probability interpretations are the accounts of what a probability number means. The axioms constrain the arithmetic. They do not choose among a ratio of cases, a long-run relative frequency, and a degree of uncertainty.{{cite:gelman_bda2013}} (pp. 11–13){{cite:dodge2008}} (p. 431)

## Motivating example
A coin can be assigned probability \(1/2\) of heads because the two faces are judged exchangeable. The same coin, tossed \(10\) times and landing heads \(3\) times, has relative frequency \(3/10\). Both numbers are probabilities under some reading: one is a judgement about the toss, and the other is a summary of a finite record. Using one of them as if it were the other answers a different question.{{cite:gelman_bda2013}} (p. 12){{cite:dodge2008}} (p. 431)

## Intuition
The number is asked to do several jobs in ordinary speech. It can report how many of a list of equally serious possibilities fall inside an event. It can report how often an event has occurred in a long run of repetitions. It can report how strongly an uncertain claim is believed, including a claim about a single case. Each job suggests a way to arrive at the number. Once the number is in hand, the addition and complement rules are common property.{{cite:gelman_bda2013}} (pp. 12–13){{cite:dodge2008}} (pp. 431–433)

## Definition
Three readings cover the uses that statistical work actually makes.

The classical, or symmetry, reading sets the probability of an event equal to the number of favourable cases divided by the number of possible cases, when the cases are judged equally likely. For a coin this is a claim about the physical toss, not a convention that every experiment has equally likely atoms.{{cite:gelman_bda2013}} (p. 12)

The frequency reading sets the probability equal to the relative frequency in a long sequence of repetitions, taken to be performed in the same way and independently. A single trial that is not thought of as one member of such a sequence has no probability under a strict form of this reading. A reference set can sometimes be constructed, for example by treating a future rocket launch as one of a class of comparable launches.{{cite:gelman_bda2013}} (p. 12)

The uncertainty reading sets the probability equal to a degree of belief about an event or an unknown, whether or not a sequence of repetitions is available. A betting version names the probability \(p\) as the price of a contract that pays \(1\) if the event occurs. This is [Bayesian probability](bayesian-probability.qmd).{{cite:gelman_bda2013}} (pp. 11–13)

An axiomatic reading does not pick one of these stories. It requires a nonnegative assignment on events that gives the whole sample space probability one and adds over incompatible events. Relative frequencies in repeated trials are one way to justify the numbers; the axioms are the other, and they are what calculations then use.{{cite:dodge2008}} (pp. 431–433)

## Properties
All three readings are asked to obey the same arithmetic. The probability of the sample space is \(1\). The probability of the empty event is \(0\). The probability of a complement is one minus the probability of the event. Incompatible events add, and for any two events the probability of the union is the sum of the probabilities minus the probability of the intersection. A classical assignment on a finite set of equally likely atoms produces these rules by counting. A frequency in a finite record produces them by counting occurrences. A coherent betting assignment produces them because a violation would allow a sure loss.{{cite:dodge2008}} (pp. 432–433){{cite:gelman_bda2013}} (pp. 11, 13)

The readings can disagree about which number to write down. Symmetry can say \(1/2\) for a coin that, in a short record, has landed heads three times in ten. The frequency \(3/10\) describes that record. Neither number corrects the other unless a further judgement says which question is being asked.{{cite:gelman_bda2013}} (p. 12)

## Statistical use
A sampling model is a probability assignment for observations given parameters, and it is often motivated by symmetry, by a frequency in a population, or by a physical story that plays the role of a reference set. A prior distribution for a parameter uses the uncertainty reading, because the parameter is not itself a draw in the sample. Reporting both, and saying which reading each number uses, is part of stating a [Bayesian model](bayesian-model.qmd). An interval procedure calibrated by the frequency of coverage across repeated samples is not, by that calibration alone, a posterior probability.{{cite:gelman_bda2013}} (pp. 3–4, 11–12){{cite:dodge2008}} (pp. 32, 431)

## Worked example
Judge a coin's two faces exchangeable. The classical probability of heads is \(1/2\), one favourable face out of two. Suppose a record of \(10\) tosses contains \(3\) heads. The relative frequency in the record is \(3/10\). The two figures answer different questions: \(1/2\) is the symmetry assignment for a single toss under that judgement, and \(3/10\) is the proportion of heads in those ten tosses. A frequency interpretation of the coin's probability would treat \(3/10\) as an estimate from a short sequence, not as a replacement for the symmetry assumption, unless the symmetry assumption is withdrawn.{{cite:gelman_bda2013}} (p. 12){{cite:dodge2008}} (p. 431)

**Your turn.** The next record has \(60\) heads in \(100\) tosses. What is the relative frequency of heads, as a fraction in lowest terms?

::: {.callout-tip collapse="true" title="Answer"}
The relative frequency is \(60/100=3/5\).
:::

## Common misconceptions
The axioms do not say that elementary outcomes are equally likely. Equal likelihood is the extra judgement in the classical reading. A relative frequency in a finite record is a property of that record; identifying it with the probability in the sampling model is a further step, and a short record can sit far from the probability that generated it. A degree of belief about a parameter is not a relative frequency of the parameter.{{cite:gelman_bda2013}} (pp. 11–12){{cite:dodge2008}} (pp. 431–432)

## Assumptions and limits
Each reading brings a substantive hypothesis: that the cases really are exchangeable, that the repetitions really are comparable, or that the betting prices really are the commitments one will live by. The axioms will not detect a bad hypothesis of that kind. They will detect an assignment that contradicts itself, for example nonnegative weights on a finite set that do not add to one. Probability theory develops the consequences of the axioms once an assignment has been made.{{cite:dodge2008}} (pp. 432–433){{cite:gelman_bda2013}} (pp. 12–13)

## Connections
The rules common to the readings are the [axioms of probability](axioms-of-probability.qmd), and the set function that satisfies them is a [probability measure](probability-measure.qmd). The mathematical development is [probability theory](probability-theory.qmd). The uncertainty reading, applied to parameters and single cases, is [Bayesian probability](bayesian-probability.qmd), and it is the reading [Bayesian statistics](bayesian-statistics.qmd) uses for unknowns.{{cite:gelman_bda2013}} (pp. 11–13){{cite:dodge2008}} (pp. 32, 432)

## History
Counting equally likely cases in games of chance is the early form: dice, cards, and the problems Pascal and Fermat solved. A frequency account, tying probability to repeated trials, runs alongside that history. The axiomatic account states the rules without choosing the story that supplied the numbers. Extending the same numbers to scientific unknowns, including an unknown chance given the data, is the step that produced inverse probability and, later, Bayesian statistics.{{cite:dodge2008}} (pp. 431–432){{cite:gelman_bda2013}} (pp. 12–13, 31)
