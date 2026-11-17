## Motivating example
A clinician might want to describe how a patient's age changes the chance of an event coded one rather than zero. A straight-line probability model can fall below zero or above one; binary logistic regression instead fits a straight line to *log odds* and transforms it back to a probability. The result can be used for probability forecasts or, after a decision threshold is chosen, classifications.{{cite:dodge2008}} (p. 319, “Logistic Regression”)

## Intuition
For probability $p$ between zero and one, the odds $p/(1-p)$ run from zero to infinity, and their logarithm runs over all real values. A linear predictor can therefore change freely while the inverse-logit keeps the fitted probability inside $(0,1)$. A slope adds to log odds; exponentiating it gives a multiplicative change in odds at fixed values of the other predictors. This is not generally the same as a risk ratio or a fixed change in probability.{{cite:dodge2008}} (pp. 319–320, model and odds ratio)

## Definition
For independent binary responses $Y_i\in\{0,1\}$ and observed predictor rows $x_i$ that include an intercept coordinate, put $p_i=\Pr(Y_i=1\mid x_i)$ and $\log\{p_i/(1-p_i)\}=x_i^\top\beta$. Thus $p_i=\operatorname{expit}(x_i^\top\beta)=e^{x_i^\top\beta}/(1+e^{x_i^\top\beta})$. Maximum likelihood chooses $\beta$ to maximise $\ell(\beta)=\sum_i[Y_i\log p_i+(1-Y_i)\log(1-p_i)]$. The design and binary coding must be stated, since reversing zero and one reverses the sign of every coefficient.{{cite:dodge2008}} (p. 319, model and log likelihood)

## Interpretation
If a slope is $\beta_j$, increasing $x_j$ by one unit while other predictors stay fixed multiplies the event odds by $e^{\beta_j}$. The probability change depends on the starting point: an odds multiplier of two raises probability from $0.1$ to $2/11\approx0.182$, but from $0.5$ to $2/3\approx0.667$. A threshold such as $0.5$ converts probabilities into labels; it does not change how the likelihood was fitted, and a different cost balance can justify a different threshold.{{cite:dodge2008}} (pp. 319–320, interpretation)

## Properties
The Bernoulli variance is $p_i(1-p_i)$, so uncertainty is greatest near $p_i=1/2$. In the linear predictor $\eta_i=x_i^\top\beta$, the log likelihood contribution equals $y_i\eta_i-\log(1+e^{\eta_i})$; its score is $\sum_i x_i(y_i-p_i)$ and Hessian is $-\sum_i p_i(1-p_i)x_ix_i^\top$. The negative semidefinite Hessian makes the likelihood concave, but does not guarantee a *finite* maximum: separated classes can push some coefficients indefinitely.{{cite:dodge2008}} (p. 319, model and log likelihood)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Writing $p_i=e^{\eta_i}/(1+e^{\eta_i})$ in the Bernoulli likelihood yields $\ell_i=y_i\eta_i-\log(1+e^{\eta_i})$. Since $dp_i/d\eta_i=p_i(1-p_i)$, differentiating gives $\partial\ell/\partial\beta=\sum_i x_i(y_i-p_i)$ and $\partial^2\ell/\partial\beta\partial\beta^\top=-\sum_i p_i(1-p_i)x_ix_i^\top$. For any vector $v$, its quadratic form is $-\sum_i p_i(1-p_i)(v^\top x_i)^2\leq0$. For a one-unit change in coordinate $j$, subtracting the two log-odds equations gives $\beta_j$, hence the odds multiplier $e^{\beta_j}$.{{cite:dodge2008}} (p. 319, model and log likelihood)
:::
:::

## Statistical use — A yes-or-no probability
Inspect the response coding, predictor ranges, missingness and class frequencies before fitting. Compare predicted probabilities with observed event rates on fresh or properly held-out cases, and choose a classification threshold according to the decision cost. If predictors are screened using outcome labels, that screening belongs inside each training fold of cross-validation. A very large coefficient or standard error may reflect separation rather than a strong, precisely measured effect.{{cite:dodge2008}} (pp. 319–320, interpretation and use)

If every observed success has $x>0$ and every failure has $x<0$, increasing a positive slope can drive all fitted probabilities toward their observed labels without producing a finite unpenalised estimate. If repeated patients are treated as independent, standard errors based on independent Bernoulli trials can be too small. If an important curved age effect is forced into one linear log-odds slope, the fitted probabilities can be miscalibrated even though they remain between zero and one. And a model evaluated only after selecting predictors on the full dataset leaks outcome information into its validation folds.{{cite:dodge2008}} (p. 319, model conditions)

## Worked example
Suppose $\log\{p/(1-p)\}=-3+0.8x_1-0.4x_2$. At $x=(4,2)$ the linear predictor is $-3+3.2-0.8=-0.6$, so $p=1/(1+e^{0.6})\approx0.3543$. A $0.5$ threshold predicts class zero. At the same $x_2$, one more unit of $x_1$ multiplies the odds by $e^{0.8}\approx2.2255$; it does not add $0.8$ to probability. The decision boundary solves $-3+0.8x_1-0.4x_2=0$.{{cite:dodge2008}} (p. 319, probability and logit formulas)

**Your turn.** In this fitted model, find the probability at $x=(5,2)$ and decide its class at threshold $0.5$.

::: {.callout-tip collapse="true" title="Answer"}
The predictor is $-3+0.8(5)-0.4(2)=0.2$, giving $p=1/(1+e^{-0.2})\approx0.5498$. The predicted class is one at a $0.5$ threshold. The change from $0.3543$ to $0.5498$ is about $0.1955$, specific to these starting predictors; the odds multiplier stays $e^{0.8}$.
:::

## Common misconceptions
A slope is a log-odds change, not a probability increase. Its exponent is an odds ratio, not generally a relative risk. Logistic regression can output probabilities without making any classification decision; the threshold is a separate choice. A concave log likelihood does not mean a finite maximum always exists when the classes separate.{{cite:dodge2008}} (pp. 319–320, model and odds interpretation)

## Connections
The [logit link](logit-link.qmd) is the probability transformation used here; [complete separation](complete-separation.qmd) explains the nonfinite maximum. The [logistic-rule question](../questions/ex-sl-10-7.qmd) exercises probabilities, odds and a decision boundary. The [screening question](../questions/ex-sl-18-6.qmd) tests whether validation includes the full model-building procedure.{{cite:dodge2008}} (pp. 319–320, model and odds interpretation)

## History
Berkson's 1944 paper used the logistic function for bioassay, where a dose is related to the frequency of an all-or-none response. The model later became a general regression tool for binary outcomes, read through the logit, the Bernoulli likelihood and an odds ratio.{{cite:dodge2008}} (pp. 319–320, “Logistic Regression”, bioassay setting and model)
