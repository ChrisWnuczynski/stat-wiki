## Lead context
Cross-validation uses each observation for assessment while keeping it out of the fit that predicts it. It is useful when a permanent test set would leave too little data for training, and it evaluates a training procedure at the size of the folds' training portions. Choosing a model with those scores requires a separate assessment of the choice itself.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 241–244) {{cite:cawley_talbot2010}} (§1, pp. 2079–2081)

## Motivating example
A prediction rule can look accurate on observations used to fit it. To estimate how it might perform on new observations, divide the available data into folds, fit without one fold, and score predictions on that held-out fold. Repeating this over folds gives each observation a prediction from a fit that did not use its response.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 242–243)

## Intuition
Imagine five piles of labelled observations. Fit on four piles, predict the fifth, and rotate the held-out pile until each has been predicted. Each prediction is made without its own observation in the fit. A score computed from those predictions answers how the fitting recipe performs with roughly four-fifths of the available data; a final fit on all five piles is a different fitted rule.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 241–244)

## Definition
For independent pairs \((X_i,Y_i)\), partition the indices \(1,\ldots,n\) into \(K\) disjoint folds \(F_1,\ldots,F_K\), each nonempty. Write \(\widehat f_{-k}\) for the rule fitted without cases in \(F_k\), and let \(L(y,\widehat y)\) be the chosen prediction loss. The pooled \(K\)-fold score is
\[
\widehat R_{\mathrm{CV}}=\frac1n\sum_{k=1}^{K}\sum_{i\in F_k}L\bigl(Y_i,\widehat f_{-k}(X_i)\bigr).
\]
For classification, \(L\) may be one for a wrong label and zero for a correct one; for numerical prediction, it may be squared error. When \(K=n\), each fold has one case and the formula is leave-one-out cross-validation. All preprocessing and tuning that affect \(\widehat f_{-k}\) must use the training cases for that fold.{{cite:hastie_esl2009}} (Ch. 7, §§7.10.1–7.10.2, pp. 241–246)

## Interpretation
The score averages predictions from \(K\) fitted rules, each trained on approximately \(n(K-1)/K\) cases when the folds are balanced. It is commonly used to compare fitting procedures or tuning values on the same partition. It does not directly estimate the conditional prediction error of the one final rule fitted on all \(n\) cases; its usual target is the expected error of the training procedure at the fold training size.{{cite:hastie_esl2009}} (Ch. 7, §§7.10.1, 7.12, pp. 241–244, 255–257)

If \(e_k\) is the mean loss in fold \(k\), then \(\widehat R_{\mathrm{CV}}=\sum_k(|F_k|/n)e_k\). An unweighted mean of the fold means gives small folds the same weight as large ones. The two calculations coincide when all folds have the same size. This distinction matters for small samples whose fold sizes cannot be equal.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 242–243)

## Properties
Leave-one-out makes \(n\) fits, each with \(n-1\) training cases. Ordinary \(K\)-fold validation makes \(K\) fits, each with \(n-|F_k|\) cases. A larger \(K\) therefore uses more training cases per fit but requires more fits. The held-out losses are dependent because their fitted rules share training observations.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 242–244)

Selecting the smallest of several noisy validation scores changes the assessment problem. Even when candidates have the same true risk and each score is unbiased, the expected minimum score is no larger than that common risk. A fresh outer test fold evaluates the entire selection procedure, including its inner tuning, without letting its test cases choose the winner.{{cite:stone1974}} (pp. 112–115) {{cite:cawley_talbot2010}} (§§1, 5.3, pp. 2079–2081, 2102)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For each fold define \(e_k=|F_k|^{-1}\sum_{i\in F_k}L(Y_i,\widehat f_{-k}(X_i))\). Since the folds partition the \(n\) indices, grouping the pooled sum by fold gives \(\widehat R_{\mathrm{CV}}=\sum_k(|F_k|/n)e_k\). If all \(|F_k|=n/K\), every coefficient is \(1/K\), so the pooled score equals the ordinary average of fold means.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 242–243)

For the selection statement, let \(\widehat R_1,\ldots,\widehat R_m\) be integrable validation scores for candidates with the same true risk \(R\), and suppose each \(\mathbb E\widehat R_j=R\). Pointwise, \(\min_j\widehat R_j\le\widehat R_1\). Taking expectations gives \(\mathbb E[\min_j\widehat R_j]\le R\). Equality can occur when the same candidate always has the smallest score. The inequality shows the direction of selection bias in this equal-risk setting; the outer-fold procedure avoids using the selected inner minimum as its assessment.{{cite:cawley_talbot2010}} (§§1, 5.3, pp. 2079–2081, 2102)
:::
:::

## Statistical use
Choose folds according to the unit that a later prediction will encounter. Observations from one person should stay together when the goal is a prediction for a new person. For a future-time prediction, train on earlier observations and assess later ones rather than shuffling future information into training. Within each training fold, redo scaling, feature selection, and any other data-dependent preprocessing.{{cite:hastie_esl2009}} (Ch. 7, §7.10.2, pp. 245–246)

For a fixed tuning value, a cross-validation score can compare candidate procedures. If tuning values are selected by that score, assess the whole selection rule with an outer loop or a truly unused test set. Report the number and construction of folds, the loss, the amount of data used for fitting in each fold, and whether preprocessing was repeated. This lets a reader tell what prediction problem the score addresses.{{cite:stone1974}} (pp. 111–115) {{cite:cawley_talbot2010}} (§5.3, p. 2102)

## Worked example
Suppose a classifier is assessed on eleven observations in three folds of sizes four, four, and three. It makes one error in the first fold, none in the second, and one in the third. The pooled error is \(2/11\approx0.1818\). Averaging the three fold rates without weighting gives \((1/4+0+1/3)/3=7/36\approx0.1944\). The pooled value answers the error per held-out observation; the unweighted value answers the error per fold.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 242–243)

**Your turn.** Keep fold sizes $4,4,3$, but suppose the error counts are $1,1,0$. Compute the pooled error and the unweighted average of fold rates.

::: {.callout-tip collapse="true" title="Answer"}
The pooled error is $2/11\approx0.1818$. The fold rates are $1/4,1/4,0$, whose unweighted average is $1/6\approx0.1667$. Unequal fold sizes make the two summaries differ.
:::

## Common misconceptions
A held-out observation must be absent from every part of the fit that predicts it. Scaling on all observations before splitting lets the held-out values influence the transformation, and selecting features on all cases can make performance look better than a genuinely new sample would allow. Different folds share training cases, so their scores do not amount to independent replications of the whole study.{{cite:hastie_esl2009}} (Ch. 7, §§7.10.1–7.10.2, pp. 242–246)

## Connections
[Leave-one-out cross-validation](leave-one-out-cross-validation.qmd) is the \(K=n\) case; [K-fold cross-validation](fold-cross-validation.qmd) uses a smaller number of held-out blocks. [Nested cross-validation](nested-cross-validation.qmd) repeats tuning inside each outer training portion so the outer score assesses the selection procedure. A [held-out test set](a-held-out-test-set.qmd) instead reserves a single independent block for assessment.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 241–244) {{cite:stone1974}} (pp. 111–115)

## History
In his 1974 paper, Mervyn Stone studied two distinct uses of resampling: choosing among predictive rules and assessing how well the choice predicts. The paper describes a “two-deep” cross-validatory assessment in which selection is repeated after an observation is omitted for assessment.{{cite:stone1974}} (pp. 111–115)

Gavin Cawley and Nicola Talbot revisited this issue in 2010 with empirical studies of model selection by cross-validation. They showed that tuning can overfit the selection criterion and that evaluating the selected model with the same criterion can bias comparisons. Their assessment protocol treats selection as part of fitting and repeats it within each outer training sample.{{cite:cawley_talbot2010}} (§§1, 5.3, pp. 2079–2081, 2102)
