

## Lead context

Probability theory is the mathematical study of outcomes, of the events built from them, and of the random quantities and limits that follow once probabilities have been assigned. It supplies the language in which a statistical model says what a sample can do.{{cite:durrett2019}} (Ch. 1, §1.1, pp. 1–2){{cite:dodge2008}} (pp. 431–432)

## Motivating example

A fair die has six faces. The probability of a face is 1/6, and the probabilities of the six faces sum to 1. The probability of an even face is 3/6 = 1/2, which is the sum of the probabilities of the faces 2, 4, and 6. That additivity is the content of the theory for a finite set of exclusive outcomes. A continuous measurement replaces the list of faces by intervals, and the probability of an interval is an integral rather than a sum of six numbers. The theory is the bookkeeping that makes those two calculations the same kind of object.

## Definition

A model begins with a set of outcomes, a family of events closed under complements and countable unions, and a probability assignment on those events. The triple is a [probability space](probability-space.qmd). The assignment is a [probability measure](probability-measure.qmd): nonnegative, equal to one on the whole outcome set, and countably additive on disjoint events. The [axioms of probability](axioms-of-probability.qmd) are those requirements read as rules for calculation. On a finite set the assignment can be a list of nonnegative weights, one per outcome, that add to one; the probability of an event is the sum of the weights of its outcomes. Equal weights are one choice.{{cite:durrett2019}} (Ch. 1, §1.1, pp. 1–2){{cite:dodge2008}} (pp. 432–433)

A [random variable](random-variable.qmd) is a measurable numerical function of the outcome, and its distribution is the probability measure it induces on the line. [Expectation](expectation.qmd) is the integral of that function. [Conditional probability](conditional-probability.qmd) is the restriction of the assignment to the outcomes inside a conditioning event of positive probability. From these ingredients the subject proves limit theorems for averages, studies dependence through martingales and Markov processes, and constructs continuous-time processes such as Brownian motion. The measure-theoretic form is this same subject, not a second one: the definition of the measure is already the content of the probability-measure article, and Durrett's development of the subject opens by taking that definition as the starting point.{{cite:durrett2019}} (Contents, pp. v–vii; Ch. 1, §§1.1 and 1.3, pp. 1, 15)

## Statistical use

A statistical model is a family of probability measures for the observations, one measure for each parameter value. Calculations that a procedure will use — tail probabilities, sampling distributions of estimators, coverage events — are probabilities in that family. The [strong law](strong-law.qmd) and the [central limit theorem](central-limit-theorem.qmd) are the limit results that say what sample averages do as the sample grows. A [stochastic process](stochastic-process.qmd) is the same theory with the random variables indexed by time or space: Markov chains, martingales, and processes with independent increments are distinguished by the extra conditions imposed on that family. Dependence across time is still probability theory; the index is what makes it a process.{{cite:durrett2019}} (Contents, pp. v–vii){{cite:dodge2008}} (pp. 521–522)

The theorems give consequences of a stated assignment. They do not choose the assignment. A model can satisfy the axioms and still be a poor description of the experiment that produced the data. Checking a fitted model is a statistical question that uses probability theory and is not settled by it.{{cite:dodge2008}} (pp. 432–433, 522)


## Worked example

A fair die has six faces. The probability of a face is 1/6, and the probabilities of the six faces sum to 1. The probability of an even face is 3/6 = 1/2, which is the sum of the probabilities of the faces 2, 4, and 6. That additivity is the content of the theory for a finite set of exclusive outcomes. A continuous measurement replaces the list of faces by intervals, and the probability of an interval is an integral rather than a sum of six numbers. The theory is the bookkeeping that makes those two calculations the same kind of object.

**Your turn.** Using the same records, recompute the featured summary and state which population quantity it estimates.

::: {.callout-tip collapse="true" title="Answer"}
Recompute the displayed summary from the same records. It estimates the quantity named in the example, for these records only.
:::



The integer list used above is a device for keeping the target fixed. With 20 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.

That integer list used above is a device for keeping the target fixed. With 20 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.
## History

Games of chance are the early source. Counting problems for dice were written on by Cardano and Galileo; Huygens's treatise on games of chance appeared in 1657; Pascal and Fermat, in correspondence, solved the division of stakes when a game stops early. Jakob Bernoulli and Abraham de Moivre then built a body of theorems about repeated trials. Alongside the counting arguments, an axiomatic description required only nonnegative weights summing to one, and the complement, union, and empty-event rules that follow. In the twentieth century the subject was reorganised as measure theory: a probability is a measure of total mass one on a sigma-algebra, which is the language that covers finite games and continuous distributions in one set of rules, and that makes limit events legitimate.{{cite:dodge2008}} (pp. 431–433){{cite:durrett2019}} (Ch. 1, opening and §1.1, p. 1)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 20. Their total is 210, so their mean is 10.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 8.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Probability theory has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 10.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [probability space](probability-space.qmd), [probability measure](probability-measure.qmd), [axioms of probability](axioms-of-probability.qmd), [random variable](random-variable.qmd).

Two further limits are algebraic. The sum of deviations from the mean 10.5 is zero, so the mean is the least-squares centre of these 20 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 10.5.

## Connections

What the number assigned to an event is supposed to mean — a ratio of cases, a long-run frequency, or a degree of uncertainty — is a matter of [probability interpretations](probability-interpretations.qmd). The uncertainty reading, used for parameters as well as for events, is [Bayesian probability](bayesian-probability.qmd), and the statistical discipline built on it is [Bayesian statistics](bayesian-statistics.qmd). A real function on the outcome space is eligible for probability calculations when it is a [measurable function](measurable-function.qmd). The events themselves form a [sigma-algebra](sigma-algebra.qmd), and the outcome set is the [sample space](sample-space.qmd).{{cite:gelman_bda2013}} (pp. 11–13){{cite:durrett2019}} (Ch. 1, §§1.1 and 1.3, pp. 1, 15)
