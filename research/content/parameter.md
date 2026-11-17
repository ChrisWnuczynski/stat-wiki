## Lead context
A sample produces numbers. A population has features those numbers are meant to describe. The feature is a parameter. The number computed from the sample is a statistic. {{cite:dodge2008}} (p. 412) {{cite:abs_glossary2023}} (Glossary, “Statistic”)

## Motivating example
Five workshops produce 10, 12, 14, 16, and 18 tonnes a day. Their mean output, 14 tonnes, is a feature of that whole set. If only two workshops are observed, the mean of those two is a statistic. It estimates the 14, and it is not the 14 unless the two workshops happen to average to it. {{cite:dodge2008}} (p. 412) {{cite:abs_glossary2023}} (Glossary, “Estimate”)

## Intuition
A parameter is a fact about the collection named in the question. It does not change when a different subset is drawn. A statistic is recomputed every time the subset changes. Greek letters are the usual names for the parameter, and Roman letters for the statistic, so that the sentence cannot confuse the target with the estimate. {{cite:dodge2008}} (p. 412) {{cite:nist_glossary2002}} (Glossary, “statistic”)

## Definition
A parameter characterises a quantitative aspect of a population. The mean, the standard deviation, and a proportion in the population are parameters. They are often unknown. A statistic calculated from a sample estimates a parameter. {{cite:dodge2008}} (p. 412) The statistic is a value produced from the collected data. {{cite:abs_glossary2023}} (Glossary, “Statistic”) An estimate is a value inferred for the population from the sample. {{cite:abs_glossary2023}} (Glossary, “Estimate”)

The same contrast appears when the population is described as the entire set of potential observations one wants to learn about, and the statistic as a value calculated from the observations actually in hand. {{cite:nist_glossary2002}} (Glossary, “population”) {{cite:nist_glossary2002}} (Glossary, “statistic”)

## Properties
A parameter is fixed for a stated population. A statistic is a function of the sample, so it varies across samples. For a population with values $x_1,\ldots,x_N$, the mean $\mu = N^{-1}\sum_{i=1}^{N} x_i$ does not depend on which subset is later drawn. The sample mean $\bar x = n^{-1}\sum_{j=1}^{n} x_{i_j}$ does. {{cite:dodge2008}} (p. 412) {{cite:abs_glossary2023}} (Glossary, “Mean”)

Equality of one realised statistic and the parameter is possible and uninformative. It does not make them the same object. {{cite:dodge2008}} (p. 412)

## Statistical use
Estimation is the production of a statistic aimed at a parameter. A confidence interval is a range offered for the unknown parameter, not for the statistic, which is known once the sample is in hand. A test is a rule for a claim about the parameter. {{cite:abs_glossary2023}} (Glossary, “Estimate”) {{cite:abs_glossary2023}} (Glossary, “Confidence interval”) {{cite:dodge2008}} (p. 518)

## Worked example
The population values are 2, 4, 6, 8, and 10. Then $\mu = (2+4+6+8+10)/5 = 6$. The sample 2, 6, 10 has $\bar x = 6$. The sample 2, 4, 6 has $\bar x = 4$. The parameter is 6 in both cases. The statistics are 6 and 4. {{cite:dodge2008}} (p. 412) {{cite:abs_glossary2023}} (Glossary, “Sample (partial enumeration)”)

**Your turn.** The population gains a sixth value, 16. What is the new parameter $\mu$? If the sample stays 2, 4, 6, what is the statistic?

::: {.callout-tip collapse="true" title="Answer"}
The population total is 2+4+6+8+10+16 = 46, so $\mu = 46/6 = 23/3$. The sample mean stays (2+4+6)/3 = 4.
:::

## Common misconceptions
The sample mean is not a parameter of the sample. The sample has a mean, and that mean is a statistic. The parameter is the corresponding mean in the population. Writing \(\bar x\) where the question asked for \(\mu\) answers a different question. {{cite:dodge2008}} (p. 412) {{cite:nist_glossary2002}} (Glossary, “statistic”)

A symbol does not settle the distinction. If a formula can be computed from the sample alone, it is a statistic even when a Greek letter was used by habit. {{cite:abs_glossary2023}} (Glossary, “Statistic”)

## Assumptions and limits
The distinction assumes a named population. If the study never says which units the parameter refers to, the estimate has no target. A census with no measurement error would reveal a finite-population parameter directly. A sample, and any measurement error, leaves the parameter unknown. {{cite:dodge2008}} (p. 64) {{cite:dodge2008}} (p. 191) {{cite:abs_glossary2023}} (Glossary, “Sampling error”)

## Connections
The [statistic](statistic.qmd) is the sample quantity. The [population](population.qmd) is what the parameter describes. The [sample](sample.qmd) is where the statistic is computed. An [estimator](estimator.qmd) is a statistic used for a particular parameter. A [confidence interval](confidence-interval.qmd) is one way to report the remaining uncertainty about the parameter. {{cite:dodge2008}} (p. 412) {{cite:dodge2008}} (p. 518)

## History
The separation of a population feature from a quantity computed on observations is the move from a complete count to an inference. Descriptive summaries report the observations. Inferential methods treat those summaries as evidence about the population feature. {{cite:dodge2008}} (p. 518) {{cite:abs_glossary2023}} (Glossary, “Inferential statistics”)
