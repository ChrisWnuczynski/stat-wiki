## Motivating example

A fitted classifier can be assessed on observations withheld from its training. When data are limited, one split leaves either a small training set or a small assessment set. K-fold cross-validation rotates the held-out role through disjoint subsets so every observation is assessed once.{{cite:deisenroth_faisal_ong2020}} (§8.2.4, pp.263–264)

## Definition — Fit without the assessed fold

Partition the indices into nonempty disjoint folds $I_1,\ldots,I_K$, $2\le K\le n$. Fit $\widehat f^{(-k)}$ using all observations outside $I_k$. The per-observation loss estimate is
$$\widehat R_{CV}=\frac1n\sum_{k=1}^K\sum_{i\in I_k}L(Y_i,\widehat f^{(-k)}(X_i)).$$
For equal fold sizes, this is the unweighted mean of the fold-average losses. For unequal sizes, per-observation weighting requires weights $|I_k|/n$. Training includes every data-dependent preprocessing operation; a transform fitted on the whole dataset would expose held-out information.{{cite:deisenroth_faisal_ong2020}} (§8.2.4, pp.263–264)

## Worked example — Unequal folds

Suppose folds of sizes ten and thirty contain two and three classification errors. The per-observation estimate is $(2+3)/40=0.125$. An unweighted mean of the two fold rates gives $(0.2+0.1)/2=0.15$, which describes an equally weighted random choice of folds instead of an equally weighted random choice of assessed observations. Both calculations have well-defined weights, but answer different averaging questions.{{cite:bengio_grandvalet2004}} (§2.3, pp.1092–1093)

**Your turn.** Two regression folds have sizes two and three, with squared-error sums four and nine. Find the per-observation squared error and the unweighted average of fold mean squared errors.

::: {.callout-tip collapse="true" title="Answer"}
The per-observation value is $(4+9)/5=2.6$. The unweighted fold average is $(4/2+9/3)/2=2.5$.
:::

## Properties — Which training size is being evaluated?

With equal folds, each fit uses $n(1-1/K)$ observations. For iid sampling and a fixed learning procedure, averaging held-out losses estimates expected prediction loss at that training size. It need not equal the prediction loss of a particular final fit on all $n$ observations. Changing $K$ changes both the training size and the dependence between fitted models. A universal monotone relationship between $K$ and prediction error does not follow from the definition.{{cite:bengio_grandvalet2004}} (§2.3, p.1093)

Fold scores can be dependent because their training sets overlap. Treating them as independent replicates in a standard error calculation ignores that structure. Repeated random partitions measure sensitivity to the partition but do not create independent datasets.{{cite:bengio_grandvalet2004}} (§§2.3–3, pp.1093–1095)

## Statistical use — Selection inside assessment

If cross-validation selects a tuning parameter, reporting the best score as an independent assessment uses the same noisy scores twice. An external test set or outer cross-validation loop can assess the complete selection procedure. In a nested loop, every outer training set repeats the inner choices. Once selection is complete, the chosen procedure can be refitted to all the available development data.{{cite:deisenroth_faisal_ong2020}} (§8.6.1, pp.284–285)

For twelve observations, ordinary three-fold cross-validation fits three models on eight observations each; every observation is assessed once and appears in two training sets. Leave-one-out instead fits twelve models on eleven observations each. These are fit counts before any final all-data refit.{{cite:deisenroth_faisal_ong2020}} (§8.2.4, pp.263–264)


## Check yourself

### [Costs of cross-validation](../questions/ex-sl-09-5.qmd) {#self-check-ex-sl-09-5}

::: {.callout-tip collapse="true" title="Answer"}
For $n=1000$, leave-one-out needs $1000$ fold fits and ten-fold needs ten. Adding one final all-data fit gives $1001$ and $11$, respectively. With ten outer folds, nine inner folds and five candidates, inner selection plus one outer refit costs $10(9\cdot5+1)=460$. The stated final ten-fold selection and refit add $10\cdot5+1=51$, giving $511$.
:::

### [Separate tuning from evaluation](../questions/ex-sl-09-7.qmd) {#self-check-ex-sl-09-7}

::: {.callout-tip collapse="true" title="Answer"}
Choosing the highest validation accuracy among twenty candidates selects favourable sampling noise as well as good performance. Fit preprocessing inside training, select on validation data, freeze the choices, refit if desired, and assess on an independent test set. If cross-validation tunes the models, an external test set or an outer loop must assess that tuning procedure.
:::
