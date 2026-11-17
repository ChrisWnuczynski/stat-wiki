## Lead context
Listing a population in order and then taking every \(r\)th unit is a draw that a person can carry out with a single random start. That design is systematic sampling. It is one of the random sampling methods, and it is not the same draw as a simple random sample. {{cite:dodge2008}} (p. 533) {{cite:dodge2008}} (p. 152)

## Motivating example
Six hundred students are listed alphabetically and a sample of 30 is required. The interval is \(600/30 = 20\). A start is drawn at random between 1 and 20. If the start is 17, the sample is the students numbered 17, 37, 57, and so on up to 597. One random number selected the whole sample. {{cite:dodge2008}} (p. 533)

## Intuition
Imagine walking a list and marking every twentieth line after a randomly chosen first line. The start is random, so the sample is a random sample of a particular kind. Neighbouring units in the list are not independent in the way two separately drawn names are: once the start is chosen, the rest of the sample is determined. {{cite:dodge2008}} (p. 533) {{cite:dodge2008}} (p. 497)

## Definition
Systematic sampling takes individuals from a population at fixed intervals in time, space, or the order of a list. The first individual is drawn at random. {{cite:dodge2008}} (p. 533)

For a population of \(N\) units and a sample of size \(n\), with \(r = N/n\), a start \(b\) is chosen at random from \(1, 2, \ldots, r\). The selected labels are
\[
b,\; b+r,\; b+2r,\; \ldots,\; b+(n-1)r.
\]
{{cite:dodge2008}} (p. 533) The units have to be arranged in some order before this rule can be applied. {{cite:dodge2008}} (p. 533)

## Properties
There are \(r\) possible samples, one for each start, not \(\binom{N}{n}\). Each of those \(r\) samples is a rigid pattern through the list. Simple random sampling gives every subset of size \(n\) the same probability. Systematic sampling gives equal probability only to the subsets that form an arithmetic progression with difference \(r\). {{cite:dodge2008}} (p. 533) {{cite:dodge2008}} (p. 497)

The design is cheap because the field work is a regular step through an ordered frame. The cost of that regularity appears when the trait being measured itself repeats every \(r\) units, or at a divisor of \(r\). The sample can then land on the same phase of the cycle every time. {{cite:dodge2008}} (p. 533)

A systematic rule is also distinct from scientific randomisation in experiments. Assigning treatment A to units 1–12 and treatment B to units 13–24 is a systematic assignment, not a random one. {{cite:nist_glossary2002}} (Glossary, "randomization, scientific")

## Statistical use
Systematic sampling is listed with simple random sampling and stratified sampling among the random methods of [data collection](data-collection.qmd), the methods for which a selection probability can be stated. {{cite:dodge2008}} (p. 152) It is used when a complete ordered list, a time sequence, or a spatial sequence already exists and drawing a fresh random number for every unit is unnecessary. The estimate that is computed from the sample is then referred to the population, as with any other probability sample, provided the periodic trap has been considered. {{cite:dodge2008}} (p. 533) {{cite:dodge2008}} (p. 468)

## Worked example
A street has \(N = 40\) houses and a sample of \(n = 8\) is required. The interval is \(r = 40/8 = 5\). The possible starts are 1, 2, 3, 4, and 5, so there are 5 possible samples. If the random start is \(b = 3\), the labels are \(3, 8, 13, 18, 23, 28, 33, 38\). The last label is \(3 + (8-1)\times 5 = 38\). There are 8 labels. {{cite:dodge2008}} (p. 533)

**Your turn.** The start is \(b = 1\) instead, with the same \(N\), \(n\), and \(r\). What is the last label, and how many houses are selected?

::: {.callout-tip collapse="true" title="Answer"}
The last label is \(1 + (8-1)\times 5 = 36\). The sample still contains 8 houses.
:::

## Common misconceptions
A systematic sample is not a simple random sample that happened to look evenly spaced. Most subsets of size \(n\) cannot occur at all. {{cite:dodge2008}} (p. 497) {{cite:dodge2008}} (p. 533)

Taking every \(r\)th unit with a start that was not random, or that was chosen because it looked convenient, drops the design out of the random methods. The interval alone is not the randomisation. {{cite:dodge2008}} (p. 533) {{cite:nist_glossary2002}} (Glossary, "randomization, scientific")

## Assumptions and limits
The list order has to be available, and \(n\) has to divide \(N\) in the simple form \(r = N/n\) used here. {{cite:dodge2008}} (p. 533) If the characteristic cycles along the list with a period that divides \(r\), the sample can be badly wrong in a way that a simple random sample of the same size would not systematically repeat. {{cite:dodge2008}} (p. 533) The design does not correct coverage error in the list itself. {{cite:nist_glossary2002}} (Glossary, "coverage error")

## Connections
[Sampling](sampling.qmd) is the general operation of selecting a part and inferring back. [Stratified and cluster sampling](stratified-and-cluster-sampling.qmd) are the other classical departures from a simple random draw. The [sample](sample.qmd) is still a subset, and the [population](population.qmd) is still the list the interval walks through. A [statistical survey](statistical-survey.qmd) is a common reason to prefer a design this easy to field.

## History
Systematic sampling is treated as one of the random methods that became part of survey practice once the argument had moved from "whether to sample" to "how to sample". Its history is the history of that sampling development, from representative samples in the 1890s through the probabilistic designs of the twentieth century. {{cite:dodge2008}} (p. 533) {{cite:dodge2008}} (p. 468) {{cite:dodge2008}} (p. 469)
