## Lead context
A stump trades flexibility for a decision that can be described by one question about one predictor.

## Motivating example
A screening rule might ask whether a measurement exceeds a chosen cutoff. The cutoff and the prediction on each side must be learned from labelled observations. A single cutoff may work well, poorly, or perfectly; its depth alone does not determine its error.{{cite:lindholm2022_ml}} (Ch. 7, p. 175)

## Definition — One split, two terminal predictions
A classification stump is a decision tree with one internal split and two terminal nodes. For numerical predictors a split has the form $x_j<t$. Each terminal node receives a class label, usually a majority label among the training observations reaching it. Weighted training replaces counts by sums of nonnegative observation weights. For binary labels $y_i\in\{-1,+1\}$, opposite terminal labels can be represented as
$$
h_{j,t,a}(x)=\begin{cases}a,&x_j<t,\\-a,&x_j\ge t,\end{cases}\qquad a\in\{-1,+1\}.
$$
Allowing both leaves to predict the same label includes constant rules. Categorical splits require a specified division of categories rather than a numerical threshold.{{cite:lindholm2022_ml}} (§2.3; Ch. 7, p. 175)

## Interpretation — Search the distinct partitions
For weights $D_i\ge0$ with $\sum_iD_i=1$, weighted classification error is
$$
\varepsilon(h)=\sum_iD_i\mathbf1\{h(x_i)\ne y_i\}.
$$
After sorting a numerical predictor, only cuts between distinct observed values change the partition of the training data. Tied values must remain on the same side. For each partition, independently choose the lower-loss label in each leaf and compare its loss with the other partitions. Cuts outside the observed range represent constant predictions. Different thresholds producing the same training partition can still disagree on future observations.{{cite:lindholm2022_ml}} (§2.3, decision-tree construction)

This fit optimises the chosen sample criterion. It does not establish a useful population error, and it does not guarantee an error strictly below one half under every weighting. In boosting, a weak-learning assumption supplies a positive advantage over one half on the weighted problems encountered by the algorithm. The assumption concerns the learner and data distribution together.{{cite:schapire2013_explaining_adaboost}} (§2, p. 3)

## Properties — Reweighting changes the next problem
For an AdaBoost round with $0<\varepsilon<1/2$, set
$$
\alpha=\frac12\log\frac{1-\varepsilon}{\varepsilon},\qquad
D_i^{\mathrm{new}}=\frac{D_i e^{-\alpha y_i h(x_i)}}{Z},\qquad
Z=2\sqrt{\varepsilon(1-\varepsilon)}.
$$
The combined classifier uses the sign of a weighted sum of stump predictions. Increasing the weights of errors encourages a subsequent stump to repair a different part of the sample; it need not repeat the preceding threshold. The displayed finite formula excludes zero error, where the logarithm diverges and the implementation needs a stopping convention.{{cite:schapire2013_explaining_adaboost}} (§1, Fig. 1, pp. 1–2)

For $0<\varepsilon<1$, the total new weight on the preceding stump's errors is
$$
\frac{\varepsilon e^\alpha}{\varepsilon e^\alpha+(1-\varepsilon)e^{-\alpha}}=\frac12.
$$
This follows by substituting $e^{2\alpha}=(1-\varepsilon)/\varepsilon$. It describes the same stump after reweighting, rather than the newly fitted stump.{{cite:schapire2013_explaining_adaboost}} (§1, weight update)

## Worked example
For $x=1,\ldots,5$ and labels $(+,+,-,-,+)$ with equal weights, the stump predicting $+$ below $2.5$ makes one error. Exhausting the numerical partitions and both orientations gives minimum error $1/5$. Its coefficient is $\alpha=\log2\approx0.693147$ and its normaliser is $Z=0.8$. The four correctly classified points each receive new weight $1/8$; the error at $x=5$ receives weight $1/2$.

Under these new weights the threshold $4.5$ with the reverse orientation, predicting $-$ below the threshold and $+$ above it, has error $1/4$. The training problem has changed: the first stump has weighted error $1/2$, while a different partition improves it. This is the mechanism behind successive stump fits.{{cite:schapire2013_explaining_adaboost}} (§1, Fig. 1)

**Your turn.** What coefficient and normaliser correspond to a next-round weighted error of $1/4$?

::: {.callout-tip collapse="true" title="Answer"}
$\alpha=\tfrac12\log3\approx0.549306$ and $Z=2\sqrt{(1/4)(3/4)}=\sqrt3/2\approx0.866025$.
:::

## Check yourself
### Updating five weights {#self-check-ex-sl-13-4}
[One round of AdaBoost](../questions/ex-sl-13-4.qmd): calculate the new error of the same stump.

::: {.callout-tip collapse="true" title="Answer"}
Only the fifth observation is wrong. Its initial weight is $0.2$, giving $\alpha=\tfrac12\log4$. Multipliers are $1/2$ on correct points and $2$ on the error; after division by $0.8$, the weights are $(1/8,1/8,1/8,1/8,1/2)$. The same stump therefore has new error $1/2$.
:::

### Identical classifiers {#self-check-ex-sl-13-6}
[Averaging identical classifiers does not reduce variance](../questions/ex-sl-13-6.qmd): explain why replicating one deterministic rule does not improve its prediction.

::: {.callout-tip collapse="true" title="Answer"}
All member predictions coincide, so their average is the same prediction. Their diversity is zero and their pairwise correlation is one whenever the variance is positive. Random forests vary samples and candidate predictors; AdaBoost changes weights across rounds. Each approach changes the fitted members rather than merely repeating one rule.
:::
