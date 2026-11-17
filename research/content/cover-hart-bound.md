## Motivating example
A classifier can copy the label of the closest training observation without estimating a probability model. Even when that neighbour is extremely close, its label can differ from a new response at the same location. The Cover–Hart bound quantifies this irreducible disagreement relative to the best possible classification error.{{cite:cover_hart1967}} (§VI, pp. 24–25)

## Definition — The large-sample error of one neighbour
[]{#property-nn-limit}

Let $(X,Y)$ and the training observations be iid, with two classes $Y\in\{0,1\}$ and zero–one loss. Write $\eta(x)=\mathbb P(Y=1\mid X=x)$, $r(x)=\min\{\eta(x),1-\eta(x)\}$ and $R^*=\mathbb E[r(X)]$. Under the nearest-neighbour limit conditions, the limiting expected risk of the one-nearest-neighbour rule is
$$
R_\infty=\mathbb E[2\eta(X)(1-\eta(X))]
=\mathbb E[2r(X)(1-r(X))].
$$
For iid Euclidean features, an index-based rule for distance ties gives this limit for general feature distributions. Continuity of the conditional class probabilities supplies a simpler sufficient setting for the local argument.{{cite:devroye1981_nn_error}} (Introduction, p. 1320, eq. 2; §1, Lem. 4)

## Properties — Two conditional labels and a concave quadratic
At a continuity point, the closest feature value approaches the query. Conditional on the two feature values, the training label and the fresh response are independent. In the limit they are Bernoulli draws with the same success probability $\eta(x)$, giving disagreement probability $2\eta(x)(1-\eta(x))$. Averaging gives the displayed expression.{{cite:cover_hart1967}} (§VI, pp. 24–25)

Since $0\le r\le1/2$, $2r(1-r)\ge r$. Also,
$$
R_\infty
=2R^*(1-R^*)-2\operatorname{Var}(r(X))
\le2R^*(1-R^*)\le2R^*.
$$
The identity follows by expanding the second moment of $r(X)$; the middle inequality is equivalently Jensen's inequality for a concave quadratic. Thus $R^*\le R_\infty\le2R^*(1-R^*)$. Equality in the sharper upper bound holds precisely when the conditional Bayes error is constant almost surely.{{cite:cover_hart1967}} (§VI, pp. 24–25)

## Worked example — Equal Bayes risk, different local ambiguity
Suppose two feature regions each have probability $1/2$, with conditional Bayes errors $0.1$ and $0.3$. Then $R^*=0.2$, while
$$
R_\infty=\tfrac12(2\cdot0.1\cdot0.9+2\cdot0.3\cdot0.7)=0.30.
$$
Here $\operatorname{Var}(r(X))=0.01$, and $2(0.2)(0.8)-2(0.01)=0.30$. If the conditional error were instead $0.2$ everywhere, the same Bayes risk would give $R_\infty=0.32$, attaining the sharper upper bound. The coarser factor-two bound is $0.40$.{{cite:cover_hart1967}} (§VI, binary-class bound)

**Your turn.** At a feature value where $\eta(x)=0.9$, calculate the Bayes error, the limiting one-neighbour error and their ratio.

::: {.callout-tip collapse="true" title="Answer"}
The Bayes error is $0.1$. The one-neighbour error is $2(0.9)(0.1)=0.18$, which is $1.8$ times as large.
:::

## Statistical use — A limit does not calibrate a small sample
The bound concerns expected risk as the training size tends to infinity. At a fixed size, distant neighbours and unsuitable distance scaling can give a larger error. One-neighbour classification also need not attain Bayes risk as more data arrive: its limiting label remains noisy. For Euclidean data, a growing neighbour count with $k_n\to\infty$ and $k_n/n\to0$ yields a different consistency regime. Increasing $k$ all the way to the sample size does not meet those conditions.{{cite:devroye1981_nn_error}} (Introduction, p. 1320)

## Check yourself

### Conditional error and a comparison multiplier {#self-check-ex-sl-11-4}
[The factor of two](../questions/ex-sl-11-4.qmd): calculate the local errors and the stated multipliers.

::: {.callout-tip collapse="true" title="Answer"}
At class probability $0.9$, the Bayes error is $0.1$ and the limiting one-neighbour error is $0.18$. The arithmetic expression $1+\sqrt{2/k}$ is approximately $2.414$, $1.535$ and $1.200$ for $k=1,7,50$. The binary one-neighbour bound gives the sharper comparison in that case.
:::

### Tuning with held-out observations {#self-check-ex-sl-11-7}
[Tuning a nearest-neighbour classifier](../questions/ex-sl-11-7.qmd): describe scaling, selection and evaluation.

::: {.callout-tip collapse="true" title="Answer"}
Estimate predictor means and standard deviations using training observations and apply that transformation to held-out observations. Select candidate neighbour counts using validation accuracy, then evaluate the selected procedure on an untouched test set. Optional refitting on training plus validation fixes the selected choices before testing. Selecting the largest validation score introduces optimism across repeated splits. A tree likewise uses validation loss to select a depth limit or pruning penalty.
:::
