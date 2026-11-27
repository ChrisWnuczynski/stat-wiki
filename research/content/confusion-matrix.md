## Lead context
Its row and column totals answer different conditional questions, so the orientation of the table is part of its definition.

## Motivating example
An alert system may identify most events correctly but still generate many false alarms when events are uncommon. One overall accuracy percentage cannot show which errors occur. A table crossing a reference classification with the predicted classification separates missed events from false alarms. The reference classification itself also needs scrutiny: an imperfect reference can make agreement with it a misleading measure of performance.{{cite:yerushalmy1947}} (pp. 1433–1435)

## Definition — Counts before percentages
Use rows for actual classes and columns for predictions, and write $C_{ij}$ for the count in row $i$, column $j$. For $N$ evaluated observations, $C_{ij}/N$ is the empirical joint probability of the two labels. Summing a row or a column gives the corresponding marginal probability. Dividing a cell by its row total conditions on the actual class; dividing by its column total conditions on the predicted class. These are direct applications of the ratio defining a conditional probability.{{cite:grinstead_snell1997}} (§4.1, pp. 133–135, 143)

For two classes, label the event of interest positive. Its actual-positive row contains true positives $TP$ and false negatives $FN$; the actual-negative row contains false positives $FP$ and true negatives $TN$. Then
$$
\mathrm{sensitivity}=\frac{TP}{TP+FN},\qquad
\mathrm{specificity}=\frac{TN}{TN+FP}.
$$
Both describe performance conditional on the actual state. A zero denominator means the relevant rate cannot be estimated from that evaluation sample.{{cite:yerushalmy1947}} (p. 1435)

## Interpretation — Changing the denominator changes the question
Positive predictive value, also called precision in classification, is $TP/(TP+FP)$. This ratio is defined only when the predicted-positive column total $TP+FP$ is positive. It conditions on a positive prediction. Sensitivity conditions on an actual positive instead. Their numerators agree, but their denominators count different groups. Reversing a conditional probability requires the marginal frequencies as well as the conditional rates.{{cite:grinstead_snell1997}} (§4.1, Bayes' formula)

Let $\pi$ be the population prevalence of the positive class, with sensitivity $s$ and specificity $c$. The positive predictive value is
$$
\frac{s\pi}{s\pi+(1-c)(1-\pi)}.
$$
This follows by dividing the positive-and-predicted-positive probability by the total predicted-positive probability. Consequently, transporting sensitivity and specificity to a population with a different prevalence generally changes predictive value. Transporting the rates themselves also requires that performance within each class remains applicable.{{cite:grinstead_snell1997}} (§4.1, conditional probability and medical testing examples)

The overall error is the sum of off-diagonal counts divided by $N$. Equivalently it is the weighted average of class-specific errors, weighted by the actual-class proportions in the evaluation sample. If the study deliberately balances classes, those weights describe the balanced sample. Deployment error requires deployment class proportions.{{cite:grinstead_snell1997}} (§4.1, joint distributions and total probability)

## Worked example
Consider this evaluation of an alert rule:

| Actual class | Predicted positive | Predicted negative | Total |
|:--|--:|--:|--:|
| Positive | 72 | 8 | 80 |
| Negative | 12 | 108 | 120 |
| Total | 84 | 116 | 200 |

The sensitivity is $72/80=0.9$, specificity is $108/120=0.9$, and accuracy is $(72+108)/200=0.9$. Positive predictive value is $72/84=6/7\approx0.8571$. The false negative and false positive counts differ even though the two conditional error rates both equal $0.1$; their class totals differ. The overall error is $0.4(0.1)+0.6(0.1)=0.1$.{{cite:yerushalmy1947}} (p. 1435);{{cite:grinstead_snell1997}} (§4.1)

If sensitivity and specificity remain $0.9$ in a population with prevalence $0.05$, the predictive value is
$$
\frac{0.9(0.05)}{0.9(0.05)+0.1(0.95)}
=\frac9{28}\approx0.3214.
$$
The rule catches the same fraction of positives in this calculation, while the far larger negative group supplies most positive alerts.{{cite:grinstead_snell1997}} (§4.1, Bayes' formula)

**Your turn.** In the displayed evaluation table, compute the probability of an actual negative conditional on a negative prediction.

::: {.callout-tip collapse="true" title="Answer"}
There are $116$ negative predictions, of which $108$ are actual negatives. The negative predictive value is $108/116=27/29\approx0.9310$.
:::

## Statistical use — Evaluation depends on the reference labels
The table measures agreement with the supplied reference labels. If those labels make mistakes, the table combines the classifier's errors with errors in the reference. Blinded assessment, careful outcome definitions, and an evaluation design representing the intended population determine what its entries mean. Agreement between two procedures alone cannot establish that either procedure always identifies the underlying state correctly.{{cite:yerushalmy1947}} (pp. 1434–1438)

## Check yourself
State the denominator before calculating each error rate.

### Weighting the class errors {#self-check-ex-sl-09-1}
[A confusion matrix](../questions/ex-sl-09-1.qmd): compute the overall and class-specific errors for the table in the question.

::: {.callout-tip collapse="true" title="Answer"}
The off-diagonal count is $12+16=28$, so the overall error is $28/200=0.14$. The row-specific errors are $12/120=0.1$ and $16/80=0.2$. Weighting them by the observed class proportions gives $0.6(0.1)+0.4(0.2)=0.14$.
:::

### A majority-class rule {#self-check-ex-sl-11-8}
[What an accuracy table does and does not say](../questions/ex-sl-11-8.qmd): compare its test accuracy with always predicting class 2.

::: {.callout-tip collapse="true" title="Answer"}
The classifier has accuracy $(18+32)/60=5/6$ and class errors $2/20=0.1$ and $8/40=0.2$. Always predicting class 2 has accuracy $40/60=2/3$, but misses every class-1 observation. Overall accuracy therefore needs the class-specific rates to show the pattern of errors.
:::
