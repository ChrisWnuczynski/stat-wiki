## Motivating example
When two measurements are naturally paired, ask whether positive and negative differences occur with equal probability. The sign test uses only their directions. A very large positive difference contributes the same positive sign as a small positive difference. This makes its target and its sensitivity different from a procedure that averages the differences. The paired sign construction and its binomial reference law are explicit parts of the test.{{cite:dodge2008}} (pp. 485–486)

## Definition — Count untied positive differences
For independent pairs, define $D_i=Y_i-X_i$. Remove exact ties and let $m$ be the number of untied pairs. Conditional on being untied, the null requires equal probabilities of positive and negative differences. If these signs are independent and fair, their positive count $N_+$ is binomial with parameters $m$ and $1/2$. The relevant denominator is the number of untied pairs, rather than the number initially recorded.{{cite:dodge2008}} (p. 486); {{cite:openintro2019}} (§4.3, “Binomial distribution”)

With iid continuous differences, zero is a median under a balanced-sign null. With discrete data and ties, an unconditional median statement alone can be insufficient for a fair conditional sign probability. For example, positive and negative masses can differ while a sufficiently large atom at zero makes zero a median. State the sign null directly when ties occur, and explain how ties are handled. The binomial calculation follows from its independent-trial model.{{cite:openintro2019}} (§4.3, binomial conditions); {{cite:dodge2008}} (p. 486, equality signs)

## Properties — A probability calculation without magnitude information
Under the null, the chance of exactly $k$ positive signs is $\binom{m}{k}2^{-m}$. For a positive-direction alternative, sum this over counts at least as large as observed. A symmetric two-sided test can double the smaller tail and cap it at one. Because the reference law is discrete, attainable p-values and rejection probabilities occur in steps. Nominal significance levels therefore need not be attained exactly without randomisation.{{cite:dodge2008}} (p. 486, decision rules); {{cite:openintro2019}} (§4.3)

Discarding magnitudes protects the sign count from a single arbitrarily large observation's size. It also gives away information that a correctly specified magnitude model could use. Dependence between pairs can invalidate the binomial count even when each individual sign is fair. Pairing identifies how a difference is formed; it does not establish independence across the pairs.{{cite:dodge2008}} (pp. 485–486)

## Worked example — Ten increases among twelve untied pairs
Suppose ten of twelve differences are positive. The one-sided null tail is
$$P(N_+\ge10)=\frac{\binom{12}{10}+\binom{12}{11}+\binom{12}{12}}{2^{12}}=\frac{79}{4096}\approx0.019287.$$
The symmetric two-sided probability is $158/4096\approx0.038574$. These compare the count of increases with its balanced-sign reference. They do not quantify the typical size of an increase.

If the same twelve untied pairs came from fourteen recorded pairs with two exact ties, the calculations still use twelve. Replacing twelve by fourteen would treat the discarded ties as random negative outcomes and answer a different question.

**Your turn.** With eight positive signs out of twelve, compute the one-sided probability for a positive-direction alternative.

::: {.callout-tip collapse="true" title="Answer"}
The tail numerator is $495+220+66+12+1=794$. The probability is $794/4096\approx0.193848$, which rounds to $0.194$.
:::

## Interpretation — Median and mean are different targets
The mean of the differences can be positive even if half the differences are negative, for example because a few positive magnitudes are large. A test based only on signs responds to direction probabilities. It cannot distinguish two data sets that have the same signs but very different magnitudes. Report a magnitude summary separately when the scientific question requires one, with assumptions appropriate to that summary.{{cite:dodge2008}} (pp. 485–486)

## Statistical use — Match the direction to the question
A directional alternative should be selected before observing the sign count. A difference in either direction calls for a two-sided rule. A nonrejection with few untied pairs may reflect limited information rather than a demonstration of equal direction probabilities. Recording the initial sample size, number of ties and final positive count makes the exact calculation reproducible.{{cite:openintro2019}} (§4.3); {{cite:dodge2008}} (p. 486)
