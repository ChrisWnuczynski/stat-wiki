## Lead context

A regression that is handed every recorded measurement will give each of them a coefficient. Some of those measurements have nothing to do with the response. Feature selection, also called variable selection, is the decision to leave those measurements out, so that the fitted model uses only a subset of the predictors.{{cite:james_islr2021}} (Ch. 6, pp. 225–226) {{cite:hastie_esl2009}} (p. 57, §3.3)

## Motivating example

Three cases have predictors $(x,z)$ and response $y$ equal to $(0,0,1)$, $(1,0,1)$ and $(2,1,3)$. An intercept-only fit predicts the mean $5/3$ every time, and its residual sum of squares is $8/3$. A straight line in $x$ alone, still with an intercept, has residual sum of squares $2/3$. The line $1+2z$ passes through all three points, so the residual sum of squares for $z$ alone is $0$. The variable that earns its place is $z$. Keeping $x$ as well cannot make the training residual sum of squares smaller than $0$, and it adds a coefficient that the three points do not need.{{cite:james_islr2021}} (Ch. 6, pp. 227–228)

## Definition

For the linear model
\[
Y=\beta_0+\beta_1 X_1+\cdots+\beta_p X_p+\varepsilon,
\]
feature selection means choosing a subset of $\{X_1,\ldots,X_p\}$ and fitting the model on that subset. The excluded predictors are absent. Their coefficients are not estimated, which is the same end state as a coefficient fixed at zero.{{cite:james_islr2021}} (Ch. 6, pp. 225–226) {{cite:hastie_esl2009}} (p. 57, §3.3)

Subset selection does the choice first and then applies least squares to the survivors. Best-subset selection, for each size $k$, finds the subset of $k$ predictors with the smallest residual sum of squares. Forward stepwise selection starts from the intercept and adds, one predictor at a time, the variable that most improves the fit. Backward stepwise selection starts from the full model and deletes the predictor with the least effect on the fit. Shrinkage can do the same job inside one fit: an $\ell_1$ penalty, as in the [lasso](lasso.qmd), drives some coefficients to exact zeros when the penalty is large enough, and those zeros are the excluded variables.{{cite:james_islr2021}} (Ch. 6, pp. 226–231, 241–242) {{cite:hastie_esl2009}} (pp. 57–59, §3.3; p. 661, §18.4)

The same idea is not limited to least squares. For logistic regression the residual sum of squares is replaced by the deviance, and an $\ell_1$ penalty on the logistic coefficients again sets some of them to zero. A quadratic penalty does not. Linear discriminant analysis, ordinary logistic regression, and the support-vector classifier, regularised by a square penalty, give every feature a nonzero weight.{{cite:james_islr2021}} (Ch. 6, p. 228) {{cite:hastie_esl2009}} (p. 658, §18.3.4; p. 661, §18.4)

## Interpretation

Least squares with many predictors has two familiar failures. When the number of predictors is not small relative to the sample, the fitted coefficients move a lot from sample to sample, and predictions on new cases suffer. And a coefficient that is only a little different from zero is still a number one has to explain. Setting the useless coefficients to zero, or never estimating them, buys a simpler equation. The price is bias: a predictor that was wrongly dropped cannot help. The useful procedures are the ones that make that exchange on purpose, and that do not decide it by training error alone.{{cite:james_islr2021}} (Ch. 6, pp. 225–226) {{cite:hastie_esl2009}} (p. 57, §3.3)

Training residual sum of squares for the best subset of each size cannot rise as the size increases: the larger search includes every smaller subset. On the three cases above, the best residual sums of squares are $8/3$ at size $0$, $0$ at size $1$, and $0$ at size $2$. Training $R^2$ moves the other way. A rule that picks the subset with the smallest training residual sum of squares therefore has no reason to stop before every predictor is available, and here it cannot prefer $\{z\}$ to $\{x,z\}$.{{cite:james_islr2021}} (Ch. 6, pp. 227–228) {{cite:hastie_esl2009}} (p. 57, §3.3.1)

The search itself has a cost that grows with $p$. Best subset selection considers $2^p$ subsets. At $p=20$ that is $1{,}048{,}576$ fits. Forward stepwise fits the null model and then $p-k$ candidates at step $k$, which is $1+p(p+1)/2$ models in all, or $211$ models when $p=20$. Forward stepwise can still miss the best subset of a given size. If the best single predictor is $X_1$ and the best pair is $\{X_2,X_3\}$, the forward path has already committed to $X_1$ and cannot reach that pair. The narrower path is also the statistical point of the shortcut: a search through every subset pays in variance for the subset that looked best on the training sample.{{cite:james_islr2021}} (Ch. 6, pp. 228–231) {{cite:hastie_esl2009}} (pp. 58–59, §3.3.2)

[Ridge regression](ridge-regression.qmd) shrinks coefficients and does not set them to zero, except in the limit of an infinite penalty, where every coefficient is zero. The lasso penalty $\lambda\sum_j|\beta_j|$ does set coefficients to zero for large enough $\lambda$, so the fitted equation names the variables it kept. When there are more predictors than observations, a lasso solution has at most as many nonzero coefficients as there are observations.{{cite:james_islr2021}} (Ch. 6, pp. 241–242) {{cite:hastie_esl2009}} (p. 661, §18.4, (18.18))

Use a selection procedure when the scientific or practical product is a short list of predictors, or when $p$ is large enough that an unpenalised least-squares fit is noisy. Best subset selection is feasible for $p$ up to about $30$ or $40$. Beyond that, forward stepwise, or the lasso, is the computation one can actually run. Backward stepwise needs more observations than predictors, because it starts from the full least-squares fit. Forward stepwise does not.{{cite:hastie_esl2009}} (pp. 57–59, §3.3) {{cite:james_islr2021}} (Ch. 6, pp. 228–231)

The size of the subset, or the lasso penalty, is not chosen by the training residual sum of squares. Validation error, [cross-validation](cross-validation.qmd), $C_p$, AIC, BIC, or adjusted $R^2$ compare models that have different numbers of coefficients. For a least-squares fit with $d$ predictors, one estimate of test mean squared error is $C_p=(\mathrm{RSS}+2d\hat\sigma^2)/n$. The penalty term is what can make a larger subset look worse.{{cite:james_islr2021}} (Ch. 6, pp. 227–228, 233, (6.2))

[Subset selection and shrinkage](subset-selection-and-shrinkage.qmd) are the two standard organisations of this idea in linear regression. [Dimensionality reduction](dimensionality-reduction.qmd) is the third organisation in the same chapter, and it is not feature selection: every original predictor can still appear inside a principal component. The component may be a useful summary, but it does not drop a named variable from the equation.{{cite:james_islr2021}} (Ch. 6, p. 226)

A smaller training residual sum of squares does not mean a better selected model. On the three cases, $\{z\}$ and $\{x,z\}$ both have training residual sum of squares $0$. The second model is not more accurate on new cases merely because it contains an extra predictor. Training error is why the size of the subset is chosen by a validation score or by a penalty such as $C_p$, not by residual sum of squares itself.{{cite:james_islr2021}} (Ch. 6, pp. 227–228)

Forward stepwise is not best subset selection on a budget that happens to reach the same answer. It is a nested search. The three-case example happens to agree at size $1$. The search disagrees as soon as the best pair does not contain the best single predictor.{{cite:james_islr2021}} (Ch. 6, pp. 230–231) {{cite:hastie_esl2009}} (pp. 58–59)

[Ridge regression](ridge-regression.qmd) is not a feature-selection method. Shrinking a coefficient is not the same as removing the predictor. The square penalty leaves every coefficient nonzero for any finite penalty. The [lasso](lasso.qmd) is the penalty that removes predictors.{{cite:james_islr2021}} (Ch. 6, pp. 241–242) {{cite:hastie_esl2009}} (pp. 658, 661)

The comparisons above use squared error, an intercept, and predictors that enter as they are. A monotone transformation of $z$, or a penalty on coefficients that have not been put on a common scale, changes which variable looks useful. Best subset and stepwise selection, followed by ordinary least squares on the chosen subset, treat the selected variables as if they had been named in advance. The selection search is part of the fitting, and a later standard error that ignores the search is too small.{{cite:james_islr2021}} (Ch. 6, pp. 229–231) {{cite:hastie_esl2009}} (pp. 58–59)

A large search overfits. With enough candidate predictors, some subset will look good on the [training set](training-set.qmd) and fail on new cases. That is why $p=20$ is already described as a statistical problem for best subset selection, not only a computational one. Forward stepwise reduces the number of subsets, and it can still overfit the order in which variables were added.{{cite:james_islr2021}} (Ch. 6, p. 229) {{cite:hastie_esl2009}} (pp. 58–59)

Quadratic regularisation does not become feature selection by discarding small weights after the fit and refitting. That backward trick has been tried on a support-vector classifier with thousands of genes and a few hundred samples, and the accuracy fell as genes were removed. An $\ell_1$ penalty builds the zeros into the fit instead.{{cite:hastie_esl2009}} (p. 658, §18.3.4; p. 661, §18.4)

## Worked example

Take the three cases $(x,z,y)=(0,0,1)$, $(1,0,1)$, $(2,1,3)$.

The sample mean of $y$ is $(1+1+3)/3=5/3$. The intercept-only residual sum of squares is
\[
2\left(1-\frac53\right)^2+\left(3-\frac53\right)^2=\frac{8}{3}.
\]
The least-squares line in $x$ is $2/3+x$. Its fitted values are $2/3$, $5/3$ and $8/3$, and the residual sum of squares is
\[
\left(\frac13\right)^2+\left(-\frac23\right)^2+\left(\frac13\right)^2=\frac{2}{3}.
\]
The line $1+2z$ fits all three points, so its residual sum of squares is $0$.

Best subset selection of size $1$ therefore returns $\{z\}$. Forward stepwise starts from the intercept, compares the drop from $8/3$ to $2/3$ against the drop from $8/3$ to $0$, and adds $z$. The two-predictor fit also has residual sum of squares $0$, because it can set the coefficient of $x$ to zero and keep $1+2z$. Training residual sum of squares does not prefer the one-predictor model.

For a separate count, $p=20$ predictors give $2^{20}=1{,}048{,}576$ best-subset models and $1+20\cdot 21/2=211$ forward-stepwise models.

**Your turn.** On these three cases, what is the training residual sum of squares of the intercept-only model, and of the least-squares model that uses only $x$?

::: {.callout-tip collapse="true" title="Answer"}
The intercept-only residual sum of squares is $8/3$. The model that uses only $x$ has residual sum of squares $2/3$.
:::

## Connections

[Subset selection and shrinkage](subset-selection-and-shrinkage.qmd) are the paired tools. The [lasso](lasso.qmd) and the [logistic lasso](logistic-lasso.qmd) are the shrinkage versions that set coefficients to zero. [Ridge regression](ridge-regression.qmd) shrinks without selection. [Dimensionality reduction](dimensionality-reduction.qmd) replaces predictors by a few combinations rather than by a subset. [Cross-validation](cross-validation.qmd) is the usual way to choose how many variables, or how large a penalty, to keep. [Overfitting](overfitting.qmd) is what a selection rule is trying not to do when it refuses the subset with the smallest training error.{{cite:james_islr2021}} (Ch. 6, pp. 226–228, 241–242) {{cite:hastie_esl2009}} (pp. 57–59, 658, 661)

## History

Subset search is the older organisation: all subsets of each size when $p$ is moderate, and a forward or backward path when it is not. The leaps-and-bounds algorithm made an exhaustive subset search practical for a few dozen predictors. Forward stepwise, a greedy nested path, and backward deletion of the weakest coefficient were the practical substitutes, with the warning that the path need not contain the best subset of each size.{{cite:hastie_esl2009}} (pp. 57–59, §3.3) {{cite:james_islr2021}} (Ch. 6, pp. 227–231)

The lasso made selection a property of one convex penalty rather than of a search over subsets. In high-dimensional classification the distinction became sharp: square penalties on discriminant analysis, logistic regression, and support-vector machines keep every feature, while an absolute penalty sets some coefficients to zero and so selects.{{cite:james_islr2021}} (Ch. 6, pp. 241–242) {{cite:hastie_esl2009}} (p. 658, §18.3.4; p. 661, §18.4)
