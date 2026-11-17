## Lead context

A laboratory set out to test whether a new teaching method raises the average score. The planned comparison is flat. One of twenty other splits, chosen after the sheets were scored, is sharp. HARKing is the practice of writing that after-the-fact comparison into the report as if it had been the hypothesis from the start.

## Motivating example

The pre-specified contrast of method against control has a two-sided \(p\)-value of \(0.40\). After looking at the scores, the authors notice that among the eight students older than 30 the method looks better, with \(p=0.04\). The published introduction states the hypothesis as an effect in older students. A reader who trusts the introduction thinks the study was built to test that claim, and reads \(0.04\) as the confirmation of a prediction. The \(0.04\) was the best of a search. {{cite:kerr1998}} (p. 197) {{cite:ioannidis2005}} (section “Bias”)

## Intuition

A hypothesis that is fixed before the data arrive can be wrong, and the data can show that it is wrong. A hypothesis that is chosen because the data favour it has already used the surprise. Writing it as a prediction spends the surprise twice: once to choose the claim, and again to test it. Induction, noticing a pattern and saying so, uses the data once and labels the pattern as something the data suggested. Kerr separates that ordinary induction from the reporting practice he named. Inferring a relation from a pattern is literally something done after the results are known. HARKing, in the sense he isolates, is the further step of presenting the post hoc hypothesis in the report as if it had been an a priori hypothesis. {{cite:kerr1998}} (p. 197)

## Definition

HARKing is hypothesizing after the results are known: presenting a post hoc hypothesis in the introduction of a research report as if it were an a priori hypothesis. The opening statement of the 1998 paper uses the same words for the report as a whole. The narrower formulation Kerr then adopts is the appearance of that hypothesis as the thing the study was designed to test. {{cite:kerr1998}} (pp. 196–197)

Several versions sit under the name. One version reports only the post hoc hypothesis and drops the prediction that failed. Another keeps a result that was anticipated and rewrites its rationale after the data have made a different story plausible. Kerr’s Table 1 cross-classifies hypotheses by whether they were anticipated and whether they looked plausible before the study, against their status once the results are known. The common feature he isolates is that knowledge of the results alters the set of hypotheses advanced in the introduction. Post hoc subgroup analyses, changes in who counts as a case, and contrasts that were not in the study plan are the same family of moves when they are reported as the original question. {{cite:kerr1998}} (pp. 197–198) {{cite:ioannidis2005}} (section “Bias”)

## Statistical use

Under a true global null, a single pre-specified test at level \(0.05\) rejects with probability \(0.05\). Twenty independent tests of true nulls reject once in expectation, because \(20\times 0.05=1\). Selecting the smallest \(p\)-value and presenting it as the pre-specified test reports a procedure whose error rate is the error rate of the search, not the error rate printed next to the winner. Ioannidis treats selective or distorted reporting as a typical form of the bias that produces research findings when the design, the data, and a complete report would not have produced them. The published \(p\)-value is then the tail probability of a statistic that was not the statistic the introduction describes. {{cite:ioannidis2005}} (sections “Bias” and “Corollaries”)

The remedy that keeps the mathematics honest is a record of what was specified. A protocol or a pre-analysis plan lists the outcome, the comparison, and the subgroups before the outcomes are inspected. Results that were not on the list can still be reported, labelled as exploratory. [Cross-validation](cross-validation.qmd) and a [held-out test set](a-held-out-test-set.qmd) do a related job for a model chosen from many candidates: the selection happens on one part of the data, and the reported error is computed on a part the selection did not see. A [family-wise error rate](family-wise-error-rate.qmd) procedure keeps the type I error of a declared family. It does not repair a family that was hidden. {{cite:ioannidis2005}} (section “Bias”)

HARKing also changes what a failed study looks like. Predictions that the data contradicted disappear from the introduction, so a literature of positive findings accumulates. A later reader who tries to replicate the stated hypothesis is replicating the winner of a search, which is a different experiment from the one that was run. Corollary 1 of Ioannidis’s accounting is the sample-size version of a related distortion: smaller studies have less power, and findings from fields of small studies are less likely to be true when the other factors are held fixed. A HARKed claim taken from a small sample stacks the selection problem on top of that one. {{cite:kerr1998}} (p. 198) {{cite:ioannidis2005}} (section “Corollaries”)

## Worked example

Twenty outcomes are examined. Each test is independent, and each null hypothesis is true. The chance that a given test produces \(p<0.05\) is \(0.05\). The expected number of such results is
\[
20\times 0.05=1.
\]
The pre-specified primary outcome has \(p=0.40\). The smallest of the other nineteen has \(p=0.04\). Reporting the \(p=0.04\) comparison as the hypothesis of the study presents one expected false alarm as a confirmation. {{cite:ioannidis2005}} (section “Bias”) {{cite:kerr1998}} (p. 197)

**Your turn.** If the same twenty true nulls are each tested at level \(0.01\), what is the expected number of tests with \(p<0.01\)?

::: {.callout-tip collapse="true" title="Answer"}
The expected number is \(20\times 0.01=0.2\).
:::

## Common misconceptions

HARKing is not the same act as noticing a pattern. Kerr says so explicitly: induction from a pattern of data is literally after the fact, and the practice he is isolating is the presentation of the new hypothesis as if it had been fixed in advance. A discussion section that says “the scores suggested an age split we had not planned” is a different document from an introduction that announces the age split as the study’s aim. {{cite:kerr1998}} (p. 197)

A small \(p\)-value on the selected comparison is not evidence that the comparison was pre-specified. The tail probability is computed for the statistic that was chosen. If the statistic was chosen because it was extreme, the reference distribution of that selection is wider than the reference distribution of any single pre-specified test. Quoting the unadjusted tail treats the search as if it had not happened. {{cite:ioannidis2005}} (section “Bias”)

Bem’s advice, which Kerr quotes, that one should write the article that makes sense after seeing the results, is a recommendation about exposition. It becomes HARKing when the rewritten story is offered as the hypothesis that organised the design. Kerr does not treat every form as equally costly, and he does not offer a definition that sorts every borderline sentence without judgment. The grey region is part of the account. {{cite:kerr1998}} (pp. 197–198)

## Connections

A test has a [null and an alternative](null-and-alternative-hypotheses.qmd), and a statistic whose null distribution was fixed with them. HARKing changes the statistic after the data and leaves the printed null distribution in place. The [p-value](p-value.qmd) is then being read as if it belonged to a different experiment. [Multiple comparisons](family-wise-error-rate.qmd) are the declared version of a search: the family is named, and the error rate is the error rate of the family. A [replication](replication-crisis.qmd) of a HARKed claim repeats the winner, not the protocol. [Ioannidis’s argument](misuse-of-statistics.qmd) that many published findings are false counts selective reporting among the biases that raise the chance a claimed finding is not a true relation. The design record is what lets a reader tell those cases apart. {{cite:kerr1998}} (p. 197) {{cite:ioannidis2005}} (section “Bias”)
