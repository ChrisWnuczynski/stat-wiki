## Motivating example
A classifier labels every case in its training file correctly. That sounds promising until one learns it used each case's label while building the rule. A new patient has no known label to memorize. Apparent error records the training performance faithfully, but a prediction claim needs error measured on observations that did not participate in the fit.{{cite:james_islr2013}} (Ch. 2 §2.2.3, pp. 38–43; Ch. 5 §5.1, p. 176)

## Definition
Let $D=\{(x_i,y_i)\}_{i=1}^n$ be training data and let $\eta_D$ be the classifier fitted on *all* of $D$. For loss $Q$, the **apparent error**, also called resubstitution or training error, is $\mathrm{err}(D)=n^{-1}\sum_i Q(y_i,\eta_D(x_i))$. With zero–one loss, $Q$ is one for a wrong class and zero for a correct class, so this is the fraction of training cases misclassified. The subscript $D$ matters: changing even one training label can change both the fitted classifier and its score.{{cite:james_islr2013}} (Ch. 2 §2.2.3, training and test error rates)

For a fresh pair $(X_0,Y_0)$ drawn from the same target population, the **conditional future error** of the fitted rule is $\mathrm{Err}(D)=\mathbb E[Q(Y_0,\eta_D(X_0))\mid D]$. This is a property of the particular fitted rule, whereas $\mathbb E_D[\mathrm{err}(D)-\mathrm{Err}(D)]$ describes average bias over possible training samples. The same observations appear in the fit and apparent score, so training loss is commonly lower than future loss. There is no theorem that it must be lower for every learning algorithm and every sample.{{cite:james_islr2013}} (Ch. 2 §2.2.3, training versus test errors)

## Interpretation
The gap is clearest for one-nearest-neighbour classification. Provided training inputs are distinct and each training point is allowed to be its own neighbour, the nearest point to $x_i$ has distance zero and label $y_i$. Thus apparent zero–one error is exactly zero. A new point must borrow a *different* point's label, and closeness need not imply agreement. A fully grown classification tree can also isolate distinct training cases into pure leaves; conflicting labels at identical inputs or stopping rules can prevent purity. The conclusion is about reuse of fitted data, not about the accuracy of either procedure on future cases.{{cite:james_islr2013}} (Ch. 2 §2.2.3, KNN training/test comparison; Ch. 8 §8.1, tree fitting)

Capacity alone does not determine the gap. A regularized model may fit less closely but generalize better, while a small model can still be unstable in weak data. In cross-validation, each case is predicted by a rule fitted *without* that case; in a held-out test set, none of the test cases is used for fitting or tuning. These procedures target future prediction more directly, though cross-validation folds train on fewer cases than the final rule and test performance can shift if the deployment population differs.{{cite:james_islr2013}} (Ch. 2 §2.2.3; Ch. 5 §5.1, pp. 176–185)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For distinct $x_1,\ldots,x_n$ in a metric space, $d(x_i,x_i)=0$ and $d(x_i,x_j)>0$ for $j\ne i$. A one-nearest-neighbour rule that includes the training case itself therefore predicts $\eta_D(x_i)=y_i$ for every $i$. Under zero–one loss every summand of $\mathrm{err}(D)$ is zero, proving $\mathrm{err}(D)=0$. Its conditional future error $\mathrm{Err}(D)$ is nonnegative, so $\mathbb E_D[\mathrm{err}(D)-\mathrm{Err}(D)]=-\mathbb E_D[\mathrm{Err}(D)]\le0$. Equality is possible only if its future error vanishes almost surely. The proof concerns this interpolating rule; it does not establish negative bias for every fitting procedure.{{cite:james_islr2013}} (Ch. 2 §2.2.3, one-nearest-neighbour training error)
:::
:::

## Worked example
Four training points have positions $x=(0,2,5,9)$ and labels $y=(0,0,1,1)$. One-nearest-neighbour prediction on the training set uses each point itself, so apparent error is $0/4=0$. To leave one out, the nearest *remaining* positions are $2,0,2,5$, respectively. Their labels predict $0,0,0,1$: only the point at $5$ is wrong, giving leave-one-out error $1/4=0.25$. This does not reveal the exact future error of the final four-point rule; it shows how much the assessment can change when self-prediction is prohibited.{{cite:james_islr2013}} (Ch. 2 §2.2.3; Ch. 5 §5.1.2, leave-one-out cross-validation)

**Your turn.** Keep positions $(0,2,5,9)$, but change the labels to $(0,1,1,0)$. Find the apparent and leave-one-out zero–one errors of one-nearest-neighbour classification.

::: {.callout-tip collapse="true" title="Answer"}
Apparent error remains $0$ because every point predicts itself. Leaving each point out gives predictions $(1,0,1,1)$, so the points at $0$, $2$ and $9$ are wrong. Leave-one-out error is $3/4=0.75$. The difference comes from which labels nearby *other* points carry, information hidden by self-prediction.{{cite:james_islr2013}} (Ch. 5 §5.1.2, leave-one-out construction)
:::

## Common misconceptions
Zero apparent error does not mean zero future error; one-nearest neighbour is a counterexample whenever neighbouring labels are unreliable. Apparent error is not the same as a $p$-value, a confidence interval or a calibrated probability of a mistaken prediction. Its usual optimism is an expectation across training samples, not a guarantee that any observed test error exceeds it. Nor does leave-one-out directly score the final model fitted to all $n$ cases: it averages scores from $n$ slightly smaller fits. A test set used repeatedly to choose tuning settings is no longer an untouched final assessment.{{cite:james_islr2013}} (Ch. 2 §2.2.3; Ch. 5 §5.1, validation and CV)

## Assumptions and limits — When the comparison misleads
If training cases are replicated at identical predictor values with conflicting labels, one-nearest neighbour needs a tie rule and need not attain zero training error. If training cases come from one hospital but deployment is at another with a changed case mix, even a clean held-out split from the first hospital does not estimate error at the second. If the outcome for a given patient appears in training and their other visits appear in validation, a row-wise split leaks patient information; splitting by patient is needed for a new-patient prediction target. Finally, if one chooses among many models by the same test set's score, the reported minimum is itself selected and can be optimistic.{{cite:james_islr2013}} (Ch. 5 §5.1, validation-set purpose and split design)

## Connections
Apparent error is the baseline from which resampling corrections and optimism estimates begin. Cross-validation replaces self-predictions with out-of-fold predictions, while the bootstrap compares performance on resampled and omitted cases to estimate optimism. A held-out test set assesses a final frozen fitting procedure. Each method estimates a particular prediction target under a particular sampling scheme, so the first question is what future cases the classifier is supposed to face.{{cite:james_islr2013}} (Ch. 5 §§5.1–5.2, validation, cross-validation and bootstrap)

## History
The problem of judging a rule on the cases that built it motivated resampling approaches to prediction assessment. Cross-validation and bootstrap methods became standard ways to separate model fitting from evaluation or correct the apparent score. Modern treatments present training error beside independent test error because the gap is central to choosing model flexibility, especially for adaptive classifiers such as nearest neighbours and trees.{{cite:james_islr2013}} (Ch. 2 §2.2.3 and Ch. 5 §§5.1–5.2)
