## Motivating example
For a training set of five cases, each bootstrap draw misses a fixed case with probability $4/5$. The chance that one case is absent from a sample of five draws is $(4/5)^5=0.3277$ to four decimal places.

## Intuition — The trees that never saw this case
Each tree in a forest is grown on a bootstrap sample, so some training cases are left out of that tree. Those left-out cases are a ready-made check on the tree that did not use them. Averaging, over only the trees that missed a given case, gives that case a prediction. Comparing the prediction with the label estimates the error of the forest without a separate cross-validation loop. Permuting one predictor in those left-out cases, and watching the accuracy fall, ranks how much that predictor was doing inside the fitted forest.{{cite:hastie_esl2009}} (Ch. 15, §15.3.1–15.3.2, pp. 592–593)

## Definition — Omission, error, and a permutation drop
A bootstrap sample of size $n$ includes each draw independently. A fixed training case is missed by one draw with probability $1-1/n$, and missed by the whole sample with probability $(1-1/n)^n$. The out-of-bag prediction of that case averages the trees whose samples missed it. Hastie, Tibshirani and Friedman note that the resulting error estimate is almost the same thing as $n$-fold cross-validation.{{cite:hastie_esl2009}} (Ch. 15, §15.3.1, pp. 592–593)

Permutation importance, for predictor $j$, passes the out-of-bag cases down each tree, records the accuracy, then randomly permutes predictor $j$ in those cases and records the accuracy again. The importance is the average, over trees, of the drop in accuracy. It describes the fitted forest. It is not the change one would see if the forest were grown again without predictor $j$, because a refit could replace $j$ by a correlated predictor.{{cite:hastie_esl2009}} (Ch. 15, §15.3.2, pp. 593–594)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
A bootstrap sample of size $n$ is drawn with replacement.{{cite:hastie_esl2009}} (Ch. 8, §8.2, p. 264) Each draw then matches a fixed case with probability $1/n$, so the case is missed by one draw with probability $1-1/n$ and missed by all $n$ draws with probability $(1-1/n)^n$. For the limit, set $u=1/n$. Then $n\log(1-1/n)=\log(1-u)/u$. The derivative of $\log$ at $1$ is $1$, so $\log(1-u)=-u+o(u)$ and the ratio tends to $-1$. Therefore $(1-1/n)^n\to e^{-1}$.
:::
:::

## Worked example — Five draws, and three drops
For $n=5$, the omission probability is $(4/5)^5=1024/3125=0.3277$ to four decimal places. The large-sample limit $e^{-1}$ is $0.3679$ to four decimal places. At $n=5$ the limit is not a substitute for the exact probability: the case is omitted from about $32.8\%$ of trees, not $36.8\%$.

Suppose three trees record out-of-bag accuracies $0.80$, $0.70$ and $0.90$ before a permutation of predictor $j$, and $0.60$, $0.60$ and $0.90$ after it. The drops are $0.20$, $0.10$ and $0.00$. Their average is $0.10$. That average is the permutation importance of $j$ in this three-tree illustration.{{cite:hastie_esl2009}} (Ch. 15, §15.3.2, p. 593)

**Your turn.** For $n=2$, compute $(1-1/2)^2$. For the same three trees, what is the average drop if the third tree's accuracy falls from $0.90$ to $0.75$ and the first two drops stay $0.20$ and $0.10$?

::: {.callout-tip collapse="true" title="Answer"}
$(1/2)^2=0.25$, so a given case is omitted from a quarter of the two-draw bootstrap samples. The new drops are $0.20$, $0.10$ and $0.15$, and the average is $0.45/3=0.15$.
:::

## Check yourself
### A case in every sample
If a case appears in every bootstrap sample, how many trees vote in its out-of-bag prediction?

::: {.callout-tip collapse="true" title="Answer"}
None. The out-of-bag prediction uses only trees that missed the case. If there are no such trees, that case contributes no out-of-bag prediction.
:::

### A zero drop
The accuracy after permuting predictor $j$ equals the accuracy before it, in every tree. What is the permutation importance of $j$?

::: {.callout-tip collapse="true" title="Answer"}
The average drop is $0$. Inside this fit, shuffling $j$ in the out-of-bag cases did not change the accuracy. A later refit that deleted $j$ could still change, if another predictor took its place.
:::

## Connections — Error and rank from the same leftovers
The trees are a [random forest](random-forest.qmd). The samples are the [bootstrap](bootstrap.qmd) draws inside [bagging](bagging.qmd). The split criterion whose total decrease is the other importance summary is often the [Gini index](gini-index.qmd). An out-of-bag error that has been used to choose among forests is no longer an untouched assessment; that choice needs a separate [held-out test set](a-held-out-test-set.qmd).{{cite:hastie_esl2009}} (Ch. 15, §§15.3.1–15.3.2, pp. 592–594)
