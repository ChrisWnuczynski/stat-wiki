## Motivating example

Suppose a hospital has many correlated laboratory measurements but relatively few patients. An ordinary least-squares fit may give unstable coefficients, and searching every possible small set of measurements becomes impractical. The lasso fits a joint regression while charging for the total absolute size of its slopes. As the penalty grows, some slopes become exactly zero, producing a smaller predictive model whose selected measurements can be inspected. Selection by itself does not establish that those measurements caused the outcome.{{cite:friedman_glmnet2010}} (§§1–2, sparse penalty and high-dimensional regression)

## Intuition

An absolute-value penalty has a corner at zero. A coefficient whose improvement in fit is too small to overcome the penalty stays at that corner; a larger coefficient moves away from zero but is pulled back toward it. This explains the combination of selection and shrinkage. The geometry in the definition below shows the same event as a squared-error contour touching a diamond-shaped constraint. Ridge regression instead uses a smooth quadratic penalty, usually retaining every coefficient. The scientific question is not simply how many coefficients survive, but whether the selected model predicts and remains stable for the population of interest.{{cite:friedman_glmnet2010}} (§2, penalty and coordinate updates)

## Definition

For centred responses and predictors, the raw-sum-of-squares convention minimises $\lVert y-X\beta\rVert_2^2+\lambda\lVert\beta\rVert_1$, with $\lVert\beta\rVert_1=\sum_j|\beta_j|$ and $\lambda\geq0$. An unpenalised intercept can be restored for the original response scale. This objective is convex, though its coefficients need not be unique when predictors are linearly dependent. Its absolute-value penalty is the feature that permits exact zeros. Different software packages divide the loss by $n$ or $2n$, so a numerical value of $\lambda$ has meaning only with its objective's scaling.{{cite:friedman_glmnet2010}} (§2, scaled elastic-net objective and lasso special case)

## Interpretation — Selection is conditional

A nonzero slope describes a contribution conditional on the other predictors *in the fitted model*. It does not mean a variable passed a separate marginal test, and a zero slope does not prove an absence of association or importance. Two almost identical predictors can substitute for one another: the fitted predictions may barely change when the selected name changes. This matters when one wants to identify a mechanism rather than merely forecast an outcome. Good predictive loss is a different target from recovery of the true nonzero coefficients.{{cite:friedman_glmnet2010}} (§2, behaviour with highly correlated predictors)

## Properties

For an orthonormal design with $X^\top X=I$, each least-squares coefficient $b_j$ solves a separate problem $(\beta_j-b_j)^2+\lambda|\beta_j|$. The solution is the soft threshold $\operatorname{sign}(b_j)(|b_j|-\lambda/2)_+$. Thus a coefficient at magnitude exactly $\lambda/2$ is set to zero; a larger one is reduced by $\lambda/2$ in magnitude. The $1/2$ arises from the raw squared-error convention and changes under a different scaling. This one-coordinate result makes the penalty's effect visible without a full optimisation algorithm.{{cite:friedman_glmnet2010}} (§2, coordinate descent and soft threshold)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $b>0$, a negative minimiser cannot beat its positive reflection because $(\beta-b)^2$ is then larger while $|\beta|$ is unchanged. On $\beta>0$, differentiation gives $2(\beta-b)+\lambda=0$, so the interior candidate is $b-\lambda/2$; it is admissible only for $b>\lambda/2$. At $\beta=0$, the subgradient of the objective is $-2b+\lambda[-1,1]$, which contains zero precisely when $|b|\le\lambda/2$. Symmetry gives the negative-$b$ case, yielding $\operatorname{sign}(b)(|b|-\lambda/2)_+$. The objective is convex, so these conditions identify global minima.{{cite:friedman_glmnet2010}} (§2, coordinate-descent thresholding)
:::
:::

## Statistical use

Standardise predictors using training data so the penalty treats their slopes comparably, then choose the penalty with a validation plan aligned to the goal. For prediction, cross-validation can compare held-out errors across a path of penalty values. If a reported error is meant to assess the entire procedure, every selection and tuning step must be repeated inside the training portion of each outer fold. Selecting variables before the split lets outcome information from a supposedly held-out case influence its predictor. The question on a tempting wrong turn asks the reader to locate exactly that leak in a gene-screening example.{{cite:friedman_glmnet2010}} (§2–3, standardisation and path fitting)

Coefficient inference needs more care than reading an ordinary least-squares standard error beside a selected lasso coefficient. The penalty biases estimates toward zero, and the same outcomes have helped choose both the variables and the penalty. A selected variable may be useful for prediction yet have an unstable coefficient in another sample. A separate assessment sample, a prespecified model or a selection-aware inferential method is needed when uncertainty or causal interpretation is the goal. {{cite:friedman_glmnet2010}} (§§1–2, penalised estimation and shrinkage)

Take two identical predictor columns and the centred objective $(3-\beta_1-\beta_2)^2+2(|\beta_1|+|\beta_2|)$. Its optimal fitted sum is $\beta_1+\beta_2=2$, but $(2,0)$, $(1,1)$ and $(0,2)$ all attain the same objective value. Predictions agree while the reported selected variables differ. This is a concrete failure of reading a lasso coefficient list as a unique scientific explanation. A different failure occurs when a gene screen uses all labels before cross-validation: held-out labels have already shaped the feature set, making the estimated error optimistic. Both problems require attention to the design and evaluation procedure, not just a different penalty value.{{cite:friedman_glmnet2010}} (§2, identical-predictor degeneracy and correlation)
## Worked example

Suppose an orthonormal design gives least-squares slopes $b=(1.8,-0.4,0.9)$ under the raw-sum-of-squares convention. With $\lambda=1.2$, the threshold is $\lambda/2=0.6$. Soft thresholding gives $(1.2,0,0.3)$: the second predictor drops out, while the first and third remain with reduced magnitudes. Ridge under the matching objective would divide every $b_j$ by $1+\lambda=2.2$, giving approximately $(0.8182,-0.1818,0.4091)$ and retaining all three. The comparison shows exactly where sparsity enters; it does not certify that the two selected predictors are the true data-generating variables.{{cite:friedman_glmnet2010}} (§2, lasso/ridge penalties and coordinate solutions)

**Your turn.** In the same orthonormal, raw-sum-of-squares convention, let $b=(2,-0.7,0.2)$ and $\lambda=1$. Find the lasso coefficients and name the selected predictors.

::: {.callout-tip collapse="true" title="Answer"}
The threshold is $\lambda/2=0.5$. The coefficients are $(2-0.5,-0.7+0.5,0)=(1.5,-0.2,0)$. The first and second predictors remain. The second slope is small but exceeds the threshold in magnitude before penalisation.
:::

## Common misconceptions

An exact zero is a property of the fitted penalised objective, not proof that a predictor has no effect in the population. A nonzero coefficient is a conditional, penalised estimate, not an unshrunk least-squares effect. Cross-validation that tunes $\lambda$ does not also provide an unbiased assessment of the tuning procedure unless the assessment is kept outside selection. Finally, correlated predictors can yield similarly accurate fits with different chosen variables, so a selected list is not automatically stable.{{cite:friedman_glmnet2010}} (§2, correlated predictors and path fitting)

## Connections

[Ridge regression](ridge-regression.qmd) uses a smooth quadratic penalty and handles collinearity without the same sparsity mechanism. [Soft thresholding](soft-thresholding-for-orthonormal-predictors.qmd) gives the exact lasso update in the orthonormal case. [Subset selection](subset-selection-and-shrinkage.qmd) searches discrete model sets, while [cross-validation](cross-validation.qmd) assesses a tuning procedure when its folds contain every selection step. [Logistic lasso](logistic-lasso.qmd) changes the loss for binary outcomes, and [graphical lasso](graphical-lasso.qmd) applies an absolute-value penalty to a different statistical object, the precision matrix.{{cite:friedman_glmnet2010}} (§1–3, regression and GLM penalty paths)

## History

Tibshirani introduced the lasso in 1996 as a way to combine shrinkage and variable selection in regression. The method soon extended beyond ordinary linear regression. Subsequent path and coordinate-descent algorithms made it practical to fit many penalty values efficiently and extended the same penalty principle to generalised linear models. The result is a method that links a geometric corner at zero to a computationally tractable selection rule.{{cite:friedman_glmnet2010}} (§1, original attribution and later developments; §§2–3, regression and GLM algorithms)
