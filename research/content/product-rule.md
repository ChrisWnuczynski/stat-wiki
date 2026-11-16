## Lead context
The product rule prices a chain of events by multiplying the probability of the first by each later conditional probability.

## Intuition — Each factor is the chance of the next step given the steps so far
The two-event identity \(\mathrm{P}(A\cap B)=\mathrm{P}(A)\,\mathrm{P}(B\mid A)\) is the definition of conditional probability, rearranged. A third event multiplies by one more conditional probability, given both of the earlier events. The intermediate intersections cancel, so the joint probability is a product and not a sum. Independence is the special case in which every conditional probability equals the matching marginal. Using a marginal in place of a conditional that is smaller is how the product overstates a joint event.

## Statement
**The chain for n events.** If \(\mathrm{P}(A_1\cap\cdots\cap A_{n-1})>0\), then
\[
\mathrm{P}(A_1\cap\cdots\cap A_n)
=\mathrm{P}(A_1)\,\mathrm{P}(A_2\mid A_1)\cdots\mathrm{P}(A_n\mid A_1\cap\cdots\cap A_{n-1}).
\]
Grinstead and Snell ask for the three-event case as an exercise: whenever \(A\), \(B\) and \(A\cap B\) have positive probability,
\[
\mathrm{P}(A\cap B\cap C)=\mathrm{P}(A)\,\mathrm{P}(B\mid A)\,\mathrm{P}(C\mid A\cap B).
\]
{{cite:grinstead_snell1997}} (p. 152, Exercise 16)

## Worked example — Three black balls drawn without replacement
An urn holds \(5\) black balls and \(5\) white balls. Three black balls are drawn in order, without replacement. The conditional probabilities are \(5/10\), \(4/9\) and \(3/8\), so
\[
\frac{5}{10}\times\frac{4}{9}\times\frac{3}{8}=\frac{1}{12}.
\]
The first factor is a marginal. The second and third are conditional on the black balls already removed. Replacing them by \(5/10\) again would give \((1/2)^3=1/8\), which is the probability for sampling with replacement, a different experiment.{{cite:grinstead_snell1997}} (p. 152, Exercise 16)

**Your turn.** An urn holds \(4\) black balls and \(2\) white balls. Two black balls are drawn without replacement. Find the probability.

::: {.callout-tip collapse="true" title="Answer"}
\(\frac{4}{6}\times\frac{3}{5}=\frac{2}{5}\). The second factor is \(3/5\), not \(4/6\), because one black ball has been removed.
:::

**Check yourself.** In the ten-ball urn, what is the probability that the first ball is black and the second is white?

::: {.callout-tip collapse="true" title="Answer"}
\(\frac{5}{10}\times\frac{5}{9}=\frac{5}{18}\). After a black draw, five of the nine remaining balls are white.
:::

Three independent events each have probability \(1/2\). What does the product rule return, and which conditional probabilities were used?

::: {.callout-tip collapse="true" title="Answer"}
Independence sets each conditional probability equal to \(1/2\), so the joint probability is \(1/8\). The rule itself did not require independence; independence was what justified replacing the conditionals by \(1/2\).
:::

## Related concepts — Total probability and sampling without replacement
The [law of total probability](law-of-total-probability.qmd) sums the product rule over a partition. [Independent events](independent-events.qmd) are the case of constant conditional probabilities. Sampling without replacement, as in the urn, is the case where each conditional probability changes because the composition of the urn changes.
