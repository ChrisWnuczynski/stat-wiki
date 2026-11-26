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
A directional alternative should be selected before observing the sign count. A difference in either direction calls for a two-sided rule. A nonrejection with few untied pairs may reflect limited information rather than a demonstration of equal direction probabilities. Recording the initial sample size, number of ties and final positive count makes the exact calculation reproducible.{{cite:openintro2019}} (§4.3, “Binomial distribution”); {{cite:dodge2008}} (p. 486)

## Intuition
Each untied pair contributes one bit: the second measurement is higher, or it is lower. The sign test adds those bits and compares the total with a fair coin. A difference of $0.01$ and a difference of $1000$ are the same bit. That is the source of the procedure's resistance to a single huge observation, and it is the source of its silence about magnitudes. If the scientific question is whether the typical size of the change is large, the sign count is the wrong summary. If the question is whether positive and negative changes are equally likely, the magnitudes are a distraction, and the sign count matches the question.

Ties are pairs that contribute neither bit. Conditioning on the untied pairs treats those ties as removed from the denominator. In the worked numbers, fourteen pairs with two ties leave twelve trials, and ten positive signs among those twelve give the one-sided probability $79/4096\approx 0.019287$. Replacing the denominator by fourteen would answer a different question, one that scores the ties as if they were negative. The write-up has to say which question was asked.

### Properties — The null mean and the discrete tail
Under independent fair signs, $N_+$ is binomial with mean $m/2$ and variance $m/4$. For $m=12$ the mean is $6$ and the variance is $3$. Ten positive signs sit $(10-6)/\sqrt 3\approx 2.309$ null standard deviations above the mean. The exact upper tail is still the binomial sum, not the normal approximation to that sum. The normal figure is a description of where the observation sits. The reported probability $0.019287$ comes from $\binom{12}{10}+\binom{12}{11}+\binom{12}{12}=66+12+1=79$ favourable outcomes out of $4096$.

For a smaller count, five untied pairs and a positive-direction alternative, $P(N_+\ge 4)=(5+1)/32=3/16=0.1875$. The attainable one-sided probabilities on five trials are the partial binomial sums divided by $32$. They jump. A nominal $5\%$ test cannot have type I error exactly $0.05$ unless randomisation is added on the boundary. Doubling a one-sided tail for a two-sided report has to be capped at one, because the two tails of a discrete symmetric law can overlap at the centre.

## Common misconceptions
A nonrejection is sometimes read as evidence that the median difference is zero. With few untied pairs the null distribution is wide: eight positive signs out of twelve still have one-sided tail $794/4096\approx 0.193848$. Failing to reject at a conventional level is what that wide distribution does with a moderate count. It is not a measurement of how close the median is to zero. A confidence set for a shift, or a report of the observed differences themselves, carries the magnitude information the test discarded.

Dependence among pairs breaks the binomial count even when each separate sign is fair. Two measurements on the same person, repeated across people, can be paired within person. The pairs are the independent trials only if the people are independent. A cluster of people who share a ward, a household, or a day can move together. The binomial variance $m/4$ is then the wrong variance for the sum of signs. Pairing fixes how each difference is formed. It does not create independence across pairs.{{cite:dodge2008}} (pp. 485–486)

## Connections
The [Wilcoxon signed-rank procedure](wilcoxon-signed-rank-test.qmd) uses the ranks of the absolute within-pair differences as well as their signs. A larger absolute difference then counts for more than a smaller one. The sign test is a paired comparison that keeps only the sign of each untied within-pair difference, giving each the same weight. The two-sample rank-sum test instead ranks pooled observations from independent samples; it does not start from pairs. Choosing the sign test because its $p$-value is smaller than a $t$ test on the same differences confuses a selection step with a calibrated test. The $t$ test targets a mean, under moment and error assumptions the sign test does not use. The sign test targets a sign probability. The two hypotheses can disagree in a single sample when a few large differences pull the mean off zero while the signs stay balanced.{{cite:openintro2019}} (§4.3, binomial conditions)
