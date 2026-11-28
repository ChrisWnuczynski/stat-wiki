## Motivating example

A deep tree fitted to a small training sample can change its first split after only a few observations change. That makes one tree's prediction sensitive to sample accidents. An ensemble combines several fitted predictors so their individual fluctuations may offset one another. The combination has to specify both how the members are made different and how their predictions are combined. Bagging uses bootstrap samples; a random forest also varies the candidate predictors at splits; boosting trains later members to address earlier mistakes. These are distinct ways to build an ensemble, with distinct sources of dependence between members. {{cite:breiman1996_bagging}} (§1, pp. 123–124){{cite:breiman2001_rf}} (§§1, 5){{cite:freund_schapire1997}} (§4.1, pp. 125–127)

## Intuition — Agreement and disagreement

Several models are useful together when they are each informative and their errors do not always point in the same direction. If every member makes the same numerical error, its average makes exactly that error. If errors vary independently around zero, averaging makes their mean less variable. Deliberately adding random noise to predictions creates disagreement but also damages individual accuracy, so diversity is a means rather than an end. For class labels, a majority or plurality vote can cancel some mistakes, but a vote has different mathematics from a mean of numerical errors. An ensemble has no automatic advantage over its strongest member on every future observation. {{cite:breiman1996_bagging}} (§§1, 4, pp. 123–124, 131–132)

## Definition — Members and aggregation rule

Let $f_1,\ldots,f_T$ be predictors fitted using a specified training procedure. For a numerical response, the simple ensemble is $\bar f(x)=T^{-1}\sum_{t=1}^{T} f_t(x)$. For categorical labels, a plurality vote chooses the class receiving most member votes; a tie needs a prespecified rule. Averaging estimated class probabilities and then choosing the largest average is another possible rule and need not agree with a vote of hard labels. The term *ensemble method* names this fitted collection together with its aggregation rule, not a particular training algorithm. Bagging, random forests, and boosting differ principally in how they construct the collection. {{cite:breiman1996_bagging}} (§1, pp. 123–124){{cite:freund_schapire1997}} (§4.1, pp. 125–127)

## Properties — How correlation limits averaging

Suppose, at a fixed $x$, the $T$ members have errors with common variance $\sigma^2$ and common pairwise correlation $\rho$. Their mean error has variance

$$
\operatorname{Var}(\bar f(x)-\E\bar f(x))
=\sigma^2\left[\rho+\frac{1-\rho}{T}\right].
$$

With independent errors ($\rho=0$), the variance is $\sigma^2/T$. With perfectly correlated errors ($\rho=1$), it stays $\sigma^2$ regardless of how many identical members are added. If $\rho>0$, the limiting variance as $T$ grows is $\rho\sigma^2$. This stylized calculation explains why a random forest tries to keep individual trees useful while reducing their correlation. It does not describe the zero-one loss of a classification vote or remove bias shared by all members. {{cite:breiman1996_bagging}} (§4, pp. 131–132){{cite:breiman2001_rf}} (§§2, 6, strength and correlation)

::: {.callout-note collapse="true" title="Proof"}
Write $E_t=f_t(x)-\E f_t(x)$. Then $\operatorname{Var}(T^{-1}\sum_tE_t)=T^{-2}[\sum_t\operatorname{Var}(E_t)+2\sum_{s<t}\operatorname{Cov}(E_s,E_t)]$. There are $T$ variance terms, each $\sigma^2$, and $T(T-1)/2$ covariance pairs, each $\rho\sigma^2$. Hence the variance is $T^{-2}[T\sigma^2+T(T-1)\rho\sigma^2]=\sigma^2[\rho+(1-\rho)/T]$. This is an identity under the stated equal-variance, equal-correlation assumptions; it makes no claim about bias or classification error.
:::

## Interpretation — A change of scale, not a guarantee

For $T=5$ predictors with individual error variance $1$ and pairwise correlation $0.3$, the formula gives $0.3+0.7/5=0.44$. If those same errors were uncorrelated, it would give $0.20$. More members can reduce the independent part of variation, but cannot remove the common part. Breiman's population aggregation argument compares expected squared error of an averaged predictor with that of a random member; an implemented bagged predictor uses the empirical bootstrap distribution instead, so that idealized comparison does not guarantee improvement on every dataset. For stable base procedures, his examples and discussion explicitly warn that bagging can fail to help. {{cite:breiman1996_bagging}} (§4, pp. 131–132)

## Statistical use — Three routes to different members

In bagging, each member is fitted to a bootstrap sample of the training cases. Their regression predictions are averaged or their class predictions voted. This is most useful when a small change in the sample would otherwise alter the fitted predictor substantially. Random forests retain the tree ensemble but also randomize which variables are available at each split, limiting the tendency of strong predictors to make every tree similar. In AdaBoost, the sequence is adaptive: examples that have been difficult for earlier learners get more weight, and the final classification uses a weighted combination. Therefore the correlation calculation is a useful guide for averages, but it is not a proof about boosting's sequential objective. {{cite:breiman1996_bagging}} (§§1, 4, pp. 123–124, 131–132){{cite:breiman2001_rf}} (§§1, 5–6){{cite:freund_schapire1997}} (§4.1, pp. 125–127)

Assess the whole recipe on observations not used to choose it. A bootstrap out-of-bag estimate can be useful for a bagged or forest predictor, but selecting its tuning settings by the smallest out-of-bag error also selects noise in that estimate. The evaluation target is the performance of the chosen, trained procedure on future cases; member agreement on training cases is not that target. {{cite:breiman2001_rf}} (§3, out-of-bag estimation)

## Worked example — Predictions and shared errors

Three regression members predict $2$, $4$, and $6$ for a new case. Their mean predicts $(2+4+6)/3=4$. If the observed response is $5$, their squared errors are $9$, $1$, and $1$, averaging to $11/3\approx3.6667$, while the ensemble squared error is $1$. The difference, $8/3\approx2.6667$, is exactly the variance of the three predictions about their mean using divisor $3$. This arithmetic illustrates why disagreement can help *when the members are individually plausible*; it is not a promise that the mean beats the best member, whose squared error here is also $1$. For a separate five-member setting with variance $1$ and correlation $0.3$, the predicted variance of the mean is $0.44$, not $0.20$. {{cite:breiman1996_bagging}} (§4, pp. 131–132)

**Your turn.** Four numerical predictors each have error variance $1$ and pairwise error correlation $0.5$ at a fixed input. What is the variance of their average? What would it be if their errors were independent?

::: {.callout-tip collapse="true" title="Answer"}
The correlated case gives $0.5+(1-0.5)/4=0.625$. Independence gives $1/4=0.25$. The first value retains a common-error component even after averaging.
:::

## Common misconceptions

“More models” is not itself a diversity mechanism: repeated copies of one deterministic fit give the same answer. A majority vote does not inherit a squared-error identity for averaged numerical predictions. Bagging and boosting are not synonyms; one resamples training sets to fit members in parallel, while the other changes the training emphasis sequentially. A low training error from a large ensemble is not evidence of low future error. Finally, different predictions are not necessarily complementary errors; the members can disagree because some are badly biased. {{cite:breiman1996_bagging}} (§§1, 4, pp. 123–124, 131–132){{cite:freund_schapire1997}} (§4.1, pp. 125–127)

## Assumptions and limits — Cases that do not improve

If the same deterministic tree is trained $500$ times on unchanged data with unchanged settings, the “ensemble” is only that one tree repeated. If every model omits an important predictor and underpredicts high values, their common bias survives averaging. Bagging a very stable fitting rule can leave its prediction nearly unchanged and, as Breiman noted, can sometimes degrade it. Boosting can concentrate weight on mislabeled or intrinsically ambiguous training cases; a tiny training error then need not transfer to test data. When a class is rare, hard-label voting can also conceal poor probability calibration, even if accuracy appears high. These counterexamples call for out-of-sample assessment of the particular procedure and loss. {{cite:breiman1996_bagging}} (§§4, 6, pp. 131–132, 138–140){{cite:freund_schapire1997}} (§4.2, pp. 127–129)

## Connections

[Bagging](bagging.qmd) and [random forests](random-forest.qmd) supply resampling and randomized splitting recipes. [Boosting](boosting.qmd) and [AdaBoost](adaboost.qmd) use sequentially adapted learners. The [squared error of an average](squared-error-of-an-average.qmd) gives a realized-prediction identity, while the variance formula here describes variation across hypothetical fits. [Out-of-bag estimation](out-of-bag-estimation-and-variable-importance.qmd) assesses some resampling ensembles without a separate test set, subject to the evaluation design. {{cite:breiman1996_bagging}} (§§1, 4, pp. 123–124, 131–132){{cite:breiman2001_rf}} (§§1, 3, 5)

### Guided practice

**1. Diversity alone.** Can adding a member that makes wildly different but inaccurate predictions be justified by the variance reduction formula?

::: {.callout-tip collapse="true" title="Answer"}
No. The formula concerns the variance of an average under specified error moments. Large bias or a much larger individual error variance can overwhelm a gain from lower correlation. Member quality and dependence both matter.
:::

**2. Vote versus mean.** Three classifiers vote for classes A, A, and B. What is the plurality prediction, and why is this not a numerical mean of class labels?

::: {.callout-tip collapse="true" title="Answer"}
The plurality prediction is A with two votes. Category names have no numerical spacing to average, and an algebraic squared-error guarantee for numerical predictions does not apply directly to the vote.
:::

## History

Breiman's 1996 bagging paper made bootstrap aggregation a concrete procedure for unstable learners and separated averaging of numerical predictions from voting on classes. Freund and Schapire's 1997 AdaBoost paper developed a sequential weighted-learner route to a combined classifier. Breiman's 2001 random-forest paper used randomized trees and examined how strength and correlation affect generalization. Together these papers show why the broad term *ensemble* covers several training mechanisms rather than one algorithm. {{cite:breiman1996_bagging}} (§§1, 4, pp. 123–124, 131–132){{cite:freund_schapire1997}} (§4, pp. 125–129){{cite:breiman2001_rf}} (§§1, 5–6)
