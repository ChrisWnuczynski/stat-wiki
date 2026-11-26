## Motivating example

Three measured responses at predictor values $-1,0,1$ are $0,1,0$. The quadratic curve $\hat f(x)=1-x^2$ passes through all three points, so its training squared error is zero. If the underlying response pattern is in fact flat near zero and the middle measurement was raised by noise, extrapolating the quadratic to $x=2$ gives $-3$. A constant fit of $1/3$ misses the training data but stays much closer to the underlying zero there. Perfect interpolation is a statement about the observed points, not a guarantee about a new one.{{cite:james_islr2013}} (Ch. 2, §2.2.1, pp. 31–33)

## Definition

Let a learning procedure fit a prediction rule $\hat f_D$ from training data $D$. For squared-error regression, its training error averages $\{y_i-\hat f_D(x_i)\}^2$ over the same observations used for fitting; its prediction error averages $\{Y_0-\hat f_D(X_0)\}^2$ over a fresh observation from the target population. Overfitting means that flexibility or tuning has captured sample-specific noise enough to make the latter error worse than it would be under a suitable simpler or more regularized procedure. A gap between training and test error is common even without overfitting; the comparison with alternatives and the target population matter.{{cite:james_islr2013}} (Ch. 2, §2.2.1, pp. 30–33)

The definition applies beyond squared error. A classifier can memorize training labels and still misclassify new cases. In a likelihood model, adding parameters often improves the maximized training likelihood, but the fitted parameters can vary so much across samples that predictive log loss deteriorates. An observed validation curve that turns upward while training loss keeps falling is evidence of overfitting, although finite validation samples also fluctuate{{cite:james_islr2013}} (Ch. 5, §5.1).

## Interpretation

Training loss is *apparent* performance because the data have already influenced the fitted rule. Test loss evaluates the whole fitted rule on observations kept out of training. For nested model classes fit by minimizing the same training loss, the best achievable training loss cannot increase as the class grows: the larger class contains the smaller one. That monotonic relation does not carry over to future loss. A richer class may represent a genuine nonlinear signal better, or it may follow random deviations that will not recur.{{cite:james_islr2013}} (Ch. 2, §2.2.1, pp. 31–34)

The bias–variance decomposition makes the tension precise for squared error. At a fixed new predictor value, expected prediction error is squared bias plus variation of the fitted prediction across possible training sets plus irreducible response noise. Greater flexibility can lower bias while increasing variance. The resulting test-error curve need not always have a tidy U shape in a finite dataset, but the decomposition explains why zero training error alone settles nothing about generalization. {{cite:james_islr2013}} (Ch. 2, §2.2.2, pp. 34–36)

## Properties

Suppose models $\mathcal F_1\subseteq\mathcal F_2$ are fitted by global minimization of one training loss. Then $\min_{f\in\mathcal F_2}L_D(f)\le\min_{f\in\mathcal F_1}L_D(f)$. The larger search can imitate every smaller-model fit. This result says nothing about which model wins on unseen data, and it can fail for a particular training *algorithm* that does not reach either minimum.{{cite:james_islr2013}} (Ch. 2, §2.2.1, pp. 31–33)

For squared error, if $Y_0=f(x_0)+\varepsilon_0$ with mean-zero new noise independent of the training data, then $\E\{Y_0-\hat f_D(x_0)\}^2=\{f(x_0)-\E\hat f_D(x_0)\}^2+\operatorname{Var}\{\hat f_D(x_0)\}+\operatorname{Var}(\varepsilon_0)$. The expectation is over both training samples and the fresh response at $x_0$. A single observed train–test gap is not itself this expectation. {{cite:james_islr2013}} (Ch. 2, §2.2.2, pp. 34–35, equation 2.7)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Set inclusion gives $\min_{f\in\mathcal F_2}L_D(f)\le L_D(g)$ for every $g\in\mathcal F_1$; taking the minimum over $g$ proves the training-loss inequality. For prediction error, write $m=\E_D\hat f_D(x_0)$ and decompose
$$
Y_0-\hat f_D(x_0)=\{f(x_0)-m\}+\{m-\hat f_D(x_0)\}+\varepsilon_0.
$$
The last two terms have mean zero and are independent, so their cross-products have expectation zero. Squaring and averaging yields squared bias plus fitted-prediction variance plus noise variance. The independence condition concerns the new error and the training set; without it an additional covariance term appears.{{cite:james_islr2013}} (Ch. 2, §2.2.2, pp. 34–35, equation 2.7)
:::
:::

## Statistical use — Keeping evaluation independent

Compare candidate complexity using a validation set or cross-validation folds whose outcomes were not used to fit each candidate. Put all preprocessing, feature selection and parameter tuning inside each training fold. Once a candidate is chosen, evaluate the *chosen procedure* on a separate test set or outer cross-validation folds. The minimum validation error among many candidates is itself selected and can be optimistic as a performance estimate; an independent evaluation must replay the selection process without seeing the evaluation outcomes.{{cite:james_islr2013}} (Ch. 5, §5.1, cross-validation for test error)

Regularization penalizes large or complicated fits; early stopping ends iterative fitting before it follows residual training noise; fewer basis terms or hidden units constrain what can be represented. Each changes the fitting procedure and needs its own tuning. These controls address sample-specific fitting, but no split scheme can make future data exchangeable with training data when there is a genuine time trend, a new population, or data leakage{{cite:james_islr2013}} (Ch. 5, §5.1).

Randomly splitting repeated records from the same patient can put nearly identical observations in training and validation sets, making validation accuracy look strong even when predictions fail on a new patient. A random split of a time series can let future observations influence a model assessed on earlier ones. A penalty chosen by repeatedly checking one test set uses that set for tuning. And strong regularization can underfit a real interaction, increasing both training and future error. Splitting by patient or time, reserving independent evaluation data, and checking the target population address these concrete failures.{{cite:james_islr2013}} (Ch. 5, §5.1)
## Worked example

For the three pairs $(-1,0),(0,1),(1,0)$, the quadratic $1-x^2$ has training mean squared error $0$. The best constant predictor is their mean $1/3$, with training squared-error sum $2/3$ and mean squared error $2/9\approx0.222$. Now suppose one independent test case at $x=2$ has response $0$. The quadratic predicts $-3$ and has squared error $9$; the constant predicts $1/3$ and has squared error $1/9\approx0.111$. This one held-out case illustrates how the training ranking can reverse. It is not a precise estimate of the two procedures' population risks.{{cite:james_islr2013}} (Ch. 2, §2.2.1, pp. 31–33)

The same logic explains the training-loss example: a fit can show $0.02$ training error and $0.18$ held-out error. Those figures describe one split. Reusing that held-out set repeatedly to choose the best architecture makes it part of the tuning process, so its best score no longer serves as an independent check. {{cite:james_islr2013}} (Ch. 2, §2.2.1, pp. 31–33; Ch. 5, §5.1)

**Your turn.** The training responses at $x=-1,0,1$ are $0,2,0$. Compare the training mean squared error of the interpolating quadratic $2-2x^2$ with that of the best constant predictor. If a held-out response at $x=2$ is $0$, compare their squared errors there.

::: {.callout-tip collapse="true" title="Answer"}
The quadratic fits all three training values exactly, so its training MSE is $0$. The best constant is the mean $2/3$; its training squared-error sum is $8/3$ and MSE is $8/9\approx0.889$. At $x=2$ the quadratic predicts $-6$ and incurs squared error $36$, while the constant predicts $2/3$ and incurs $4/9\approx0.444$. The held-out case favors the less flexible predictor, without proving that it always will.
:::

## Common misconceptions

A higher test error than training error is not by itself proof of overfitting; fitting on the training sample normally makes its apparent error optimistic. A flexible model is not automatically overfit: when the underlying relationship is genuinely curved and enough data support it, flexibility can improve predictions. A zero training error is not evidence of a zero irreducible error. Finally, the lowest validation score after trying many settings is not an unbiased test score for the selected setting, because validation outcomes helped select it.{{cite:james_islr2013}} (Ch. 2, §2.2.1, pp. 31–34; Ch. 5, §5.1)

## Connections

[Apparent error](apparent-error.qmd) is measured on fitted observations, while [cross-validation](cross-validation.qmd) uses held-out folds to estimate predictive performance. [Regularisation](regularisation.qmd) and [early stopping](early-stopping.qmd) reduce effective fitting flexibility. [Underfitting](underfitting.qmd) describes a different failure: even the training pattern is poorly captured. The bias–variance trade-off explains one mechanism by which a better training fit can have worse expected prediction error.{{cite:james_islr2013}} (Ch. 2, §§2.2.1–2.2.2; Ch. 5, §5.1)

## History

The distinction between fitting observed data and predicting fresh data became a central organizing theme of statistical learning. A 2013 account by James and colleagues used train-versus-test error curves to explain overfitting and cross-validation to estimate test error when a separate test sample is unavailable. Later educational treatments also use paired training and validation loss curves to show how iterative fitting can begin to follow sample-specific noise.{{cite:james_islr2013}} (Ch. 2, §2.2.1, pp. 31–34; Ch. 5, §5.1)
