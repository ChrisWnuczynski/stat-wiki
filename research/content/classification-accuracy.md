## Motivating example
A classifier that labels almost every transaction legitimate can be right on most transactions and still miss nearly every fraudulent one. Accuracy tells how often its labels match the truth in an assessment set, but the class mix and the kinds of mistakes determine whether that fraction is useful. The first question is therefore whose cases were assessed and what a missed case costs.{{cite:bacallado_taylor2022_stats202}} (“Evaluating a classification method”, confusion matrix and threshold sections)

## Intuition
Each prediction is either correct or incorrect under zero–one loss. Accuracy averages the correct indicators; the error rate averages their complements. That simplicity makes accuracy easy to communicate and compare, but it compresses all off-diagonal cells of a confusion matrix into one number. If one class is rare, a rule that never predicts it can achieve a high score just by following prevalence. A confusion matrix shows where the successes and failures came from.{{cite:bacallado_taylor2022_stats202}} (“Evaluating a classification method”, 0–1 loss and confusion matrix)

## Definition
For labelled assessment cases $(x_i,y_i)$ and a fitted classifier $\widehat g$, empirical classification accuracy is
$$
\widehat A=\frac1n\sum_{i=1}^n\mathbf1\{\widehat g(x_i)=y_i\}=1-\widehat{\mathrm{Err}}.
$$
For a binary outcome, write TP, FN, FP and TN for true positives, false negatives, false positives and true negatives. Then $\widehat A=(\mathrm{TP}+\mathrm{TN})/n$, sensitivity is $\mathrm{TP}/(\mathrm{TP}+\mathrm{FN})$, and specificity is $\mathrm{TN}/(\mathrm{TN}+\mathrm{FP})$, when their denominators are positive. Accuracy does not require probability forecasts, only class labels, so it cannot tell whether those forecasts were well calibrated.{{cite:bacallado_taylor2022_stats202}} (“Evaluating a classification method”, 0–1 loss and confusion matrix)

## Properties — How prevalence enters
Let $\pi=\Pr(Y=1)$ in the population being predicted, $s=\Pr(\widehat g(X)=1\mid Y=1)$ be sensitivity, and $c=\Pr(\widehat g(X)=0\mid Y=0)$ be specificity. The population accuracy is
$$
A=\pi s+(1-\pi)c.
$$
Thus two populations can give different overall accuracies for the same conditional performance. In particular, the rule that always predicts negative has sensitivity zero, specificity one, and accuracy $1-\pi$. This is a useful baseline, not evidence that the rule detects positives. Balanced accuracy, $(s+c)/2$, gives the two classes equal weight when that comparison is desired, though it too does not encode unequal mistake costs.{{cite:bacallado_taylor2022_stats202}} (“Evaluating a classification method”, class-specific errors)

Under equal costs for every wrong label, the ideal population classifier at a feature value $x$ predicts a class with largest conditional probability $\Pr(Y=k\mid X=x)$. The result depends on the loss rule: if missing a positive is more costly than a false alarm, the optimal probability threshold can fall below one half. A higher accuracy at one threshold can therefore be the wrong operational choice.{{cite:bacallado_taylor2022_stats202}} (“Basic approach”, Bayes classifier; “Evaluating a classification method”, changing decision rule)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For each labelled case, $\mathbf1\{\widehat g(x_i)=y_i\}+\mathbf1\{\widehat g(x_i)\ne y_i\}=1$. Averaging proves $\widehat A=1-\widehat{\mathrm{Err}}$; counting correct cells gives $(\mathrm{TP}+\mathrm{TN})/n$. For a fresh case, partition the event “correct” by true class:
$$
\Pr(\widehat g(X)=Y)=\Pr(Y=1)\Pr(\widehat g(X)=1\mid Y=1)+\Pr(Y=0)\Pr(\widehat g(X)=0\mid Y=0),
$$
which is $\pi s+(1-\pi)c$.

At fixed $x$, predicting class $k$ under zero–one loss has conditional error $1-\Pr(Y=k\mid X=x)$. Minimizing it chooses a largest conditional class probability. For binary classes, if a false negative costs $C_{\mathrm{FN}}$ and a false positive costs $C_{\mathrm{FP}}$, predicting positive costs $C_{\mathrm{FP}}(1-p)$ and predicting negative costs $C_{\mathrm{FN}}p$, where $p=\Pr(Y=1\mid X=x)$. Predict positive when $p>C_{\mathrm{FP}}/(C_{\mathrm{FP}}+C_{\mathrm{FN}})$, with either decision permitted at equality.{{cite:bacallado_taylor2022_stats202}} (“Basic approach”, Bayes classifier; “Evaluating a classification method”, threshold)
:::
:::

## Statistical use — Assessing a fitted rule
Accuracy is most informative on cases that were not used to fit, preprocess, tune, or select the classifier. Training accuracy describes fit to known cases and can be optimistic about future predictions. A held-out test set estimates the accuracy of the already fitted rule for cases drawn from the same target population; cross-validation repeats fitting and assessment across folds when test data are scarce. Keep every selection step inside the training folds, or the reported score benefits from information that would not be available at deployment.{{cite:bacallado_taylor2022_stats202}} (“Validation”, validation set and cross-validation sections)

Report the confusion matrix and the class mix beside overall accuracy. If the action depends on false negatives or false positives, examine sensitivity, specificity, precision, and the relevant decision threshold. The Stanford teaching example of credit default shows that lowering a classification threshold reduces false negatives while increasing false positives; one overall number does not reveal that exchange.{{cite:bacallado_taylor2022_stats202}} (“Evaluating a classification method”, default example and changing decision rule)

## Worked example
Suppose an untouched test set has 200 cases: 20 truly positive and 180 truly negative. An always-negative rule is correct for all 180 negatives, so its accuracy is $180/200=0.90$ even though its sensitivity is $0/20=0$. A second classifier gives this confusion matrix:

| True class | Predicted positive | Predicted negative | Total |
|:--|--:|--:|--:|
| Positive | 15 | 5 | 20 |
| Negative | 20 | 160 | 180 |

Its accuracy is $(15+160)/200=175/200=0.875$. Sensitivity is $15/20=0.75$; specificity is $160/180=8/9\approx0.8889$; precision is $15/(15+20)=3/7\approx0.4286$. The second rule's overall accuracy is lower, yet it identifies three quarters of positive cases. If missed positives matter, that trade-off may be worthwhile. Which rule is preferable depends on the decision costs and the target population, not only on the ordering of $0.90$ and $0.875$.{{cite:bacallado_taylor2022_stats202}} (“Evaluating a classification method”, confusion matrix and threshold trade-off)

**Your turn.** A lower threshold on the same 200 cases produces TP $=18$, FN $=2$, FP $=36$, and TN $=144$. Find accuracy, sensitivity, specificity, and precision. Compare the change with the worked classifier.

::: {.callout-tip collapse="true" title="Answer"}
Accuracy is $(18+144)/200=162/200=0.81$. Sensitivity rises to $18/20=0.90$, specificity falls to $144/180=0.80$, and precision is $18/(18+36)=1/3\approx0.3333$. The lower threshold catches three additional positives but creates sixteen additional false positives, so accuracy falls while sensitivity rises. The confusion matrix shows the exchange that the single accuracy number conceals.
:::

## Common misconceptions
An accuracy of $0.90$ does not mean 90% of positive cases are found: the always-negative rule has that accuracy and zero sensitivity in the example. Training accuracy is not an unbiased estimate of accuracy on new cases that did not help build the classifier. Accuracy does not assess the numerical quality of predicted probabilities; two rules can assign different probabilities yet make identical labels. Nor does maximizing accuracy automatically minimize expected harm when the two error types have different costs.{{cite:bacallado_taylor2022_stats202}} (“Evaluating a classification method”; “Validation”)

## Assumptions and limits — When accuracy misleads
If positive prevalence drops or rises, $A=\pi s+(1-\pi)c$ changes even when sensitivity and specificity stay fixed. If the test set deliberately oversamples one class, its raw accuracy represents that artificial mix unless results are reweighted to the target population. If test labels leaked into feature selection, tuning, or threshold choice, the score is no longer an untouched assessment. And when a false negative is much more costly than a false positive, a rule with fewer total mistakes can still be the worse decision. These are distinct failures of class mix, assessment design, and loss specification.{{cite:bacallado_taylor2022_stats202}} (“Evaluating a classification method”; “Validation”)

## Connections
[Confusion matrices](confusion-matrix.qmd) retain the error types hidden by overall accuracy; [sensitivity and specificity](sensitivity-and-specificity.qmd) condition on the true class. [Apparent error](apparent-error.qmd) scores training cases, whereas a [held-out test set](a-held-out-test-set.qmd) evaluates a fitted rule on fresh cases. [Cross-validation](cross-validation.qmd) estimates the performance of a fitting procedure through repeated splits.{{cite:bacallado_taylor2022_stats202}} (“Evaluating a classification method”; “Validation”)

## History
“Accuracy” has a broader statistical meaning: Dodge describes the closeness of an estimator to its target and discusses squared deviation. In classification, the term denotes a direct count of correct labels, the complement of zero–one error. This narrower usage is useful for comparing prediction rules, while a confusion matrix keeps the kinds of mistakes visible.{{cite:dodge2008}} (p. 1, “Accuracy”){{cite:bacallado_taylor2022_stats202}} (“Evaluating a classification method”, 0–1 loss and confusion matrix)
