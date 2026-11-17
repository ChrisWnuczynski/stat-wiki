## Lead context
Bayesian probability is probability used as a numerical measure of uncertainty, including uncertainty about a parameter, a single future event, or any other unknown. The same axioms govern these assignments as govern probabilities of ordinary random outcomes.{{cite:gelman_bda2013}} (pp. 11–13)

## Motivating example
A fair coin is assigned probability \(1/2\) of landing heads. The same numerical language is used for the probability that a specified rocket launch fails, or that a team wins a match, even though those events are not embedded in a long sequence of identical repetitions. Once that use is allowed, the probability that an unknown parameter lies in an interval is the same kind of number.{{cite:gelman_bda2013}} (pp. 11–12)

## Intuition
Uncertainty comes in degrees, and probability is the scale on which those degrees are written. A probability near one is a strong commitment that the event obtains; a probability near one half is a refusal to favour either side. The scale is useful because it already has addition and conditioning rules, so uncertainty about a parameter can be updated when data arrive without inventing a second calculus.{{cite:gelman_bda2013}} (pp. 11–13)

## Definition
In this use, a probability is a number attached to an event or to a set of values of an unknown. The numbers are nonnegative, additive over mutually exclusive events, and sum to one over a partition of the possibilities. The event may be "the parameter is greater than one half" or "it rains tomorrow" as well as "the next toss is heads". The distribution of an unknown parameter, before or after the data, is a Bayesian probability assignment of this kind.{{cite:gelman_bda2013}} (pp. 11–12){{cite:dodge2008}} (pp. 32–33)

One operational reading fixes the number by a bet. The probability \(p\) that you attach to an event \(E\) is the price at which you will exchange \(p\) units for a payout of \(1\) unit if \(E\) occurs. Coherence requires that the whole assignment leave no combination of bets that wins from you for sure. Assignments that meet that requirement obey the axioms of probability.{{cite:gelman_bda2013}} (p. 13)

## Properties
A symmetry judgement and a frequency judgement are two ways of arriving at the number. For a coin regarded as balanced, symmetry of the two faces gives \(1/2\). A long sequence of tosses, treated as identical and independent, gives a relative frequency. Both judgements are substantive claims about the coin and the tossing, and both are then expressed as probabilities. A single case that is not plausibly one draw from a sequence of repetitions still receives a probability; the frequency story is then a constructed reference set, not a prerequisite.{{cite:gelman_bda2013}} (pp. 12–13)

If you will bet \(1\) unit to win \(10\) on an event, the corresponding probability is at least \(1/11\): the stake \(1\) and the profit \(10\) are the two sides of a price \(p\) with \((1-p)/p=10\). The axioms then force the probabilities of a partition to add to one, so a coherent assignment cannot price every member of a partition above its share.{{cite:gelman_bda2013}} (p. 13)

The prior distribution of a parameter and the posterior distribution after conditioning on data are both assignments of this sort. The posterior is the prior reweighted by the likelihood. Scientific judgement enters both the likelihood and the prior; replication of exchangeable units is what allows features of either distribution to be estimated from data.{{cite:gelman_bda2013}} (pp. 11–13)

## Statistical use
A [Bayesian model](bayesian-model.qmd) records the assignment for the unknowns in the prior and the assignment for the data, given the unknowns, in the sampling distribution. [Bayesian inference](bayesian-inference.qmd) replaces the prior assignment by the conditional assignment given the sample. An interval with a stated posterior probability is then read directly as a probability that the unknown lies in the interval, which is the sense in which a [Bayesian credible interval](bayesian-credible-interval.qmd) is used.{{cite:gelman_bda2013}} (pp. 3–4, 11)

## Worked example
A price of \(1/11\) against a payout of \(1\) corresponds to odds of \(10\) to \(1\): if the event occurs the net gain is \(10/11\), and if it fails the loss is \(1/11\). The ratio of net gain to loss is \(10\). Someone willing to take the favourable side of a \(10\) to \(1\) bet is therefore assigning the event a probability of at least \(1/11\).{{cite:gelman_bda2013}} (p. 13)

**Your turn.** A bet of \(1\) unit in order to win \(3\) more units is odds of \(3\) to \(1\). What probability does taking the favourable side of that bet commit you to, at minimum?

::: {.callout-tip collapse="true" title="Answer"}
The stake is \(1\) and the profit is \(3\), so the price \(p\) satisfies \((1-p)/p=3\), hence \(p=1/4\).
:::

## Common misconceptions
A Bayesian probability for a parameter is not a claim that the parameter is a random draw from a population, unless the model really is a hierarchical model of that population. It is also not a relative frequency of the parameter, which is a fixed unknown in the sampling story. Calling the assignment subjective does not separate it from the rest of a statistical model: the sampling distribution is a judgement as well.{{cite:gelman_bda2013}} (pp. 11–13){{cite:dodge2008}} (p. 32)

## Assumptions and limits
The betting story asks for a two-sided price and ignores the possibility that the person on the other side of the bet knows more. Coherence constrains assignments that have already been made; it does not by itself choose the prior. A frequency interpretation remains available whenever a genuine or carefully constructed reference set exists, and it is often the practical way to estimate a probability. The axioms are the common grammar; which events receive probabilities, and from what information, is the modelling choice.{{cite:gelman_bda2013}} (pp. 12–13)

## Connections
The several readings of the same axioms are the [probability interpretations](probability-interpretations.qmd). The mathematical rules are the [axioms of probability](axioms-of-probability.qmd) and, in the measure-theoretic form, a [probability measure](probability-measure.qmd). Using the assignment on an unknown parameter, then conditioning on data, is the defining practice of [Bayesian statistics](bayesian-statistics.qmd).{{cite:gelman_bda2013}} (pp. 11–13){{cite:dodge2008}} (pp. 32, 432)

## History
The extension of probability from games of chance to scientific unknowns is the step Bayes and Laplace took when they assigned a probability distribution to an unknown chance before any trials and then conditioned on the observed count. A later axiomatic and decision-theoretic argument treats probability as the unique scale compatible with coherent preferences. The applied literature uses the scale because posterior statements about parameters are the statements users already try to read from intervals.{{cite:gelman_bda2013}} (pp. 3–4, 12–13, 31)
