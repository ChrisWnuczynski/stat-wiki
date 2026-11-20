## Lead context
Nested cross-validation keeps the data that choose a tuning constant out of the average that reports the error of that choice.{{cite:cawley_talbot2010}} (§1, pp. 2079–2080)

## Motivating example
Three constant predictors, $0$, $1$ and $4$, are scored by squared error on the responses $0$, $1$, $0$ and $8$. Their average squared errors are $16.25$, $12.75$ and $14.25$. The search that reports $12.75$ has used the same four responses both to crown the winner and to announce how accurate the winner is. The number $12.75$ is the best of three looks at one sample. It is not an assessment of the search. An outer split that chooses the constant without the held-out response, then scores only that response, answers the second question.{{cite:cawley_talbot2010}} (§1, pp. 2079–2080){{cite:hastie_esl2009}} (Ch. 7, §7.10.2, pp. 245–246)

## Intuition — The minimum is selected for its luck
A tuning constant is a second level of fitting. The inner loop picks the constant whose cross-validated score looks best. That score is a random variable. Taking the minimum over several constants favours whichever constant happened to draw a low score on this sample, so the reported minimum sits below the score one would expect from a constant chosen in advance. Cawley and Talbot show that this second-level overfitting can be as large as the gap between learning methods, which means a comparison of methods is not interpretable until each method is paired with the selection rule that will be used on new data.{{cite:cawley_talbot2010}} (§1, pp. 2079–2080)

The same bias appears when a screen, rather than a numerical constant, sees every label before cross-validation begins. Predictors chosen on the full sample have already used the rows that the later split pretends to hold out.{{cite:hastie_esl2009}} (Ch. 7, §7.10.2, pp. 245–246)

## Definition
Split the sample into outer folds. For each outer fold, run the entire selection procedure on the remaining rows: an inner cross-validation, or any other inner criterion, chooses the tuning constant, the model is refitted on those remaining rows at the chosen constant, and only the outer fold is scored. The nested estimate is the average of the outer scores. The constant chosen in one outer fold need not match the constant chosen in another. After the nested average has been computed, a final constant is chosen by repeating the inner procedure on all the rows, and the final fit uses every row at that constant. The nested average assesses the selection-and-fit procedure. It does not assess a single frozen constant that was never re-chosen.{{cite:cawley_talbot2010}} (§1, pp. 2079–2080)

## Properties — The expected minimum cannot exceed every candidate
For scores $C_1,\ldots,C_K$ of $K$ candidates on the same sample,
$$
\mathrm{E}\bigl(\min_k C_k\bigr)\le \min_k \mathrm{E}(C_k).
$$
Reporting the minimum therefore estimates something no larger than the best candidate’s expected score, and strictly smaller unless one candidate is always the minimiser.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For each fixed index $j$, $\min_k C_k\le C_j$, so $\mathrm{E}(\min_k C_k)\le \mathrm{E}(C_j)$. The left side does not depend on $j$, and the inequality holds for every $j$, so the left side is at most the smallest of the $\mathrm{E}(C_j)$. Equality holds for all sample sizes only if a single index achieves the minimum with probability one. A search that sometimes changes its mind makes the inequality strict.{{cite:cawley_talbot2010}} (§1, pp. 2079–2080)
:::
:::

The inequality is about the selection score. It does not say that the outer nested average is unbiased for the error of the final fit on a still larger population. The outer training sets are smaller than the full sample, so a steep learning curve makes the nested average pessimistic for the final fit even while the inner minimum is optimistic for the selected constant. The two biases point in opposite directions and do not cancel by arithmetic.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 242–243){{cite:cawley_talbot2010}} (§1, pp. 2079–2080)

## Statistical use — What may enter the inner loop
Preprocessing, a penalty grid, a number of neighbours, and a variable screen all belong inside the inner procedure, rerun for every outer fold. The outer fold contributes only its loss. After the nested estimate is stored, the final deployed fit may use all the data, with the tuning constant chosen by one more inner run that no longer holds out an assessment fold. Publishing the inner minimum from that final run, instead of the nested average, returns to the optimistic report the outer loop was built to avoid.{{cite:cawley_talbot2010}} (§1, pp. 2079–2080){{cite:hastie_esl2009}} (Ch. 7, §7.10.2, pp. 245–246)

## Worked example
Responses $0$, $1$, $0$ and $8$ are scored by the constant predictors $0$, $1$ and $4$. The four-point mean squared errors are
$$
\frac{0+1+0+64}{4}=16.25,\qquad \frac{1+0+1+49}{4}=12.75,\qquad \frac{16+9+16+16}{4}=14.25.
$$
The minimum is $12.75$. Now hold out the response $8$. On the remaining responses $0$, $1$ and $0$ the mean squared errors are $1/3$, $2/3$ and $41/3$. The inner search chooses the constant $0$. Its squared error on the held-out $8$ is $64$. Holding out a response $0$ and leaving $1$, $0$ and $8$ gives inner means $65/3$, $50/3$ and $41/3$, so the inner search chooses $4$ and the outer squared error is $16$. There are two such zeros. Holding out $1$ and leaving $0$, $0$ and $8$ gives inner means $64/3$, $17$ and $16$, so the search chooses $4$ and the outer squared error is $(1-4)^{2}=9$. The nested average is
$$
\frac{16+9+16+64}{4}=26.25.
$$
The figure $12.75$ is what the un-nested search would publish. The figure $26.25$ is the average loss of the search itself, each time on a response that did not choose the constant. They are not two estimates of the same thing.{{cite:cawley_talbot2010}} (§1, pp. 2079–2080)

**Your turn.** Using only the three full-sample scores $16.25$, $12.75$ and $14.25$, which value does the inequality say an expectation of the minimum cannot exceed, and which of the three sample scores is that bound’s sample analogue?

::: {.callout-tip collapse="true" title="Answer"}
The expectation of the minimum is at most the smallest of the three expected scores. On this one sample the analogue of that comparison is the minimum itself, $12.75$, which is smaller than both $16.25$ and $14.25$. The nested average $26.25$ is a different functional: it scores the chosen constant on rows the choice did not see.
:::

## Common misconceptions
Nested cross-validation does not choose the tuning constant that will be deployed. It estimates the error of a procedure that chooses a constant. The inner winners may differ across outer folds; that disagreement is part of the procedure’s variability, not a failure to converge. A small inner score is not a licence to quote that score as the test error of the winner. And an outer average computed after the constant was chosen on all the data is ordinary cross-validation of a frozen rule, not a nested estimate of the search.{{cite:cawley_talbot2010}} (§1, pp. 2079–2080){{cite:hastie_esl2009}} (Ch. 7, §7.10.1, eq. 7.49, pp. 242–243)

## Assumptions and limits — Optimism and a short outer training set
The minimum inequality assumes that every candidate is scored on the same sample and that the reported number is the minimum of those scores. It says nothing about a candidate that was not in the list. Adding further constants can only lower the minimum, so a wider search makes the optimistic bias worse, not better.

The outer estimate has its own limit. Each outer fit trains on fewer rows than the final fit. If prediction error drops sharply with training size, the nested average overstates the error of the final deployed fit. It remains the honest estimate of a procedure trained at the outer-fold size. Treating it as if it were the error of the full-sample fit confuses those two sample sizes.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 242–243)

A screen that ranks predictors on every label, and only then starts the outer loop, breaks the construction even if the arithmetic of the folds is correct. The labels in the outer fold have already entered the ranking.{{cite:hastie_esl2009}} (Ch. 7, §7.10.2, pp. 245–246)

## Connections
[Cross-validation](cross-validation.qmd) estimates the error of a rule whose form is already fixed. [Leave-one-out cross-validation](leave-one-out-cross-validation.qmd) is the inner or the outer split in which each fold holds out one row; the nesting is the separation of the two jobs, not the fold size. A [held-out test set](a-held-out-test-set.qmd) is the single-split version of the outer loop. The [Akaike information criterion](akaike-information-criterion.qmd) is a different correction for fitting, aimed at a penalty linear in the number of parameters, and it is not a substitute for rerunning a search inside each outer fold.{{cite:cawley_talbot2010}} (§1, pp. 2079–2080){{cite:hastie_esl2009}} (Ch. 7, §7.10, pp. 241–246)

## Check yourself
### Which number is the nested one? {#self-check-nested-which}

On the responses $0$, $1$, $0$ and $8$, the best full-sample mean squared error among the constants $0$, $1$ and $4$ is $12.75$, and the average of the outer squared errors is $26.25$. Which number assesses the selection procedure?

::: {.callout-tip collapse="true" title="Answer"}
The nested average $26.25$. The value $12.75$ is the minimum of three scores on the same four responses, so it both chose a constant and graded that choice.
:::

### One outer fold {#self-check-nested-fold}

The response $8$ is held out. On $0$, $1$ and $0$, the mean squared errors of the constants $0$, $1$ and $4$ are $1/3$, $2/3$ and $41/3$. Which constant is chosen, and what squared error does it incur on $8$?

::: {.callout-tip collapse="true" title="Answer"}
The smallest inner score is $1/3$, from the constant $0$. The squared error on $8$ is $(8-0)^{2}=64$.
:::

## History
Stone’s cross-validatory framework already distinguished choosing a predictor from assessing the choice, and later writers called the two-loop version a double cross or nested cross-validation. Cawley and Talbot’s 2010 study showed that overfitting the selection criterion can be as large as typical gaps between learning algorithms, and that the bias is avoided only when selection is rerun inside every assessment sample. The wrong-way screen in Hastie, Tibshirani and Friedman is the same separation applied to variable ranking rather than to a numerical penalty.{{cite:cawley_talbot2010}} (§1, pp. 2079–2080){{cite:hastie_esl2009}} (Ch. 7, §7.10.2, pp. 245–246)
