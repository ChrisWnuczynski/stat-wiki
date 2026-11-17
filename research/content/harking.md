## Lead context
A laboratory set out to test whether a new teaching method raises the average score. The planned comparison is flat. One of twenty other splits, chosen after the sheets were scored, is sharp. HARKing is the practice of writing that after-the-fact comparison into the report as if it had been the hypothesis from the start.

## Motivating example
The pre-specified contrast of method against control has a two-sided \(p\)-value of \(0.40\). After looking at the scores, the authors notice that among the eight students older than 30 the method looks better, with \(p=0.04\). The published introduction states the hypothesis as an effect in older students. A reader who trusts the introduction thinks the study was built to test that claim, and reads \(0.04\) as the confirmation of a prediction. The \(0.04\) was the best of a search.{{cite:kerr1998}} (p. 196){{cite:ioannidis2005}} (section "Bias")

## Intuition
A hypothesis that is fixed before the data arrive can be wrong, and the data can show that it is wrong. A hypothesis that is chosen because the data favour it has already used the surprise. Writing it as a prediction spends the surprise twice: once to choose the claim, and again to test it. Induction, noticing a pattern and saying so, uses the data once and labels the pattern as something the data suggested. HARKing uses the data to choose the claim and then describes the claim as prior.{{cite:kerr1998}} (p. 196)

## Definition
HARKing is hypothesizing after the results are known: presenting a post hoc hypothesis, one based on or informed by the results, in the research report as if it were an a priori hypothesis. The narrower form Kerr isolates is the appearance of that hypothesis in the introduction, as the thing the study was designed to test.{{cite:kerr1998}} (p. 196)

Several versions sit under the name. One version reports only the post hoc hypothesis and drops the prediction that failed. Another keeps the original prediction and adds a new one that the data made plausible. The common feature is that the reader cannot tell which sentences were fixed before the outcome was seen. Post hoc subgroup analyses, changes in who counts as a case, and contrasts that were not in the study plan are the same family of moves when they are reported as the original question.{{cite:kerr1998}} (p. 196){{cite:ioannidis2005}} (section "Bias")

## Properties
Under a true global null, a single pre-specified test at level \(0.05\) rejects with probability \(0.05\). Twenty independent tests of true nulls reject once in expectation, because \(20\times 0.05=1\). Selecting the smallest \(p\)-value and presenting it as the pre-specified test reports a procedure whose error rate is the error rate of the search, not the error rate printed next to the winner. The published \(p\)-value is then the tail probability of a statistic that was not the statistic the introduction describes.{{cite:ioannidis2005}} (section "Bias")

HARKing also changes what a failed study looks like. Predictions that the data contradicted disappear from the introduction, so a literature of positive findings accumulates. A later reader who tries to replicate the stated hypothesis is replicating the winner of a search, which is a different experiment from the one that was run.{{cite:kerr1998}} (p. 196){{cite:ioannidis2005}} (Summary)

## Statistical use
The remedy is a record of what was specified. A protocol or a pre-analysis plan lists the outcome, the comparison, and the subgroups before the outcomes are inspected. Results that were not on the list can still be reported, labelled as exploratory. [Cross-validation](cross-validation.qmd) and a [held-out test set](a-held-out-test-set.qmd) do a related job for a model chosen from many candidates: the selection happens on one part of the data, and the reported error is computed on a part the selection did not see. [Multiple comparison](family-wise-error-rate.qmd) procedures keep the type I error of a declared family; they do not repair a family that was hidden.{{cite:ioannidis2005}} (section "Bias")

## Worked example
Twenty outcomes are examined. Each test is independent, and each null hypothesis is true. The chance that a given test produces \(p<0.05\) is \(0.05\). The expected number of such results is
\[
20\times 0.05=1.
\]
The pre-specified primary outcome has \(p=0.40\). The smallest of the other nineteen has \(p=0.04\). Reporting the \(p=0.04\) comparison as the hypothesis of the study presents one expected false alarm as a confirmation.{{cite:ioannidis2005}} (section "Bias"){{cite:kerr1998}} (p. 196)

**Your turn.** If the same twenty true nulls are each tested at level \(0.01\), what is the expected number of tests with \(p<0.01\)?

::: {.callout-tip collapse="true" title="Answer"}
The expected number is \(20\times 0.01=0.2\).
:::

## Common misconceptions
HARKing is not the same as exploratory analysis. Exploration that is labelled as exploration tells the reader the hypothesis came from these data. HARKing is the relabelling. It is also not the same as a genuine replication. A second sample, collected after the hypothesis was formed on the first sample, is a new test. Rewriting the introduction of the first paper does not create that second sample. A small \(p\)-value on a chosen subgroup is not, by itself, evidence that the subgroup was the target.{{cite:kerr1998}} (p. 196)

## Assumptions and limits
The expectation \(20\times 0.05=1\) assumes independent tests and true nulls. Dependent outcomes share a smaller set of surprises, so the expected count of false alarms is lower, and it is not zero. A pre-specified hypothesis can still be wrong, and a post hoc hypothesis can still be true. The damage is to the calibration of the report, not a proof that every surprising pattern is noise. Kerr treated the balance of costs and benefits as something to be studied, not as a slogan that closes the question.{{cite:kerr1998}} (p. 196){{cite:ioannidis2005}} (section "Bias")

## Connections
The [p-value](p-value.qmd) is the tail probability of a pre-specified statistic. [Family-wise error](family-wise-error-rate.qmd) and the [false discovery rate](false-discovery-rate.qmd) control searches that are declared. [Cross-validation](cross-validation.qmd) separates selection from assessment. A [randomised controlled trial](randomised-controlled-trial.qmd) is one setting in which a protocol already states the comparison before outcomes are seen. HARKing is what it looks like when that statement is rewritten after the table is filled in.

## History
Norbert Kerr named the practice in 1998, in a survey of how research reports in his field were written. He defined it, distinguished it from ordinary induction, and argued that some forms were common and widely regarded as inappropriate. The costs he listed include a distorted literature of confirmed predictions. Later work on false findings put the same moves, under names such as selective reporting and post hoc subgroups, among the biases that make a published claim less likely to be true than its \(p\)-value suggests.{{cite:kerr1998}} (p. 196){{cite:ioannidis2005}} (Summary; section "Bias")
