## Motivating example
A company wants a line relating advertising spending to sales across months. No straight line passes through all ten observed points, so it needs a rule for trading one prediction error against another. Least squares chooses the line with the smallest total squared *vertical* errors. Squaring stops positive and negative residuals from cancelling and makes a large miss count more heavily than several small ones. The resulting fit summarizes association in these months, while its value for future prediction depends on how stable the relationship remains.{{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion and LS for Straight Line)

## Intuition
For a proposed model $f(x_i;\beta)$, each residual $e_i=y_i-f(x_i;\beta)$ is the observed response minus its fitted response. Least squares adjusts the parameters until the residual vector is as short as possible in Euclidean distance. In a linear model this is a geometric projection of the response vector onto the space spanned by the chosen predictors. The residual at the optimum is perpendicular to that space, which is the meaning of the normal equations. This criterion defines a fit even before any probability model for the errors has been specified.{{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion and LS for Straight Line){{cite:dodge2008}} (pp. 304–305, Least-Squares Method)

## Definition
Given responses $y_1,\ldots,y_n$ and predictions $f(x_i;\beta)$, **least squares** chooses $\widehat\beta$ to minimize the residual sum of squares

$$Q(\beta)=\sum_{i=1}^n\{y_i-f(x_i;\beta)\}^2.$$

For a straight line $f(x_i;b_0,b_1)=b_0+b_1x_i$, with the $x_i$ not all equal, the minimizer is unique and has

$$b_1=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}{\sum_i(x_i-\bar x)^2},\qquad b_0=\bar y-b_1\bar x.$$

The line therefore passes through $(\bar x,\bar y)$. If an intercept is deliberately excluded and the line is $bx$, the distinct formula is $b=\sum_i x_iy_i/\sum_i x_i^2$ when the denominator is positive. The choice to force a zero intercept is a modelling restriction, not an algebraic shortcut.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line){{cite:dodge2008}} (p. 305, normal equations)

With a design matrix $X$ whose columns are predictors and a response vector $y$, linear least squares minimizes $\|y-X\beta\|^2$. Its normal equations are $X^\top X\widehat\beta=X^\top y$. If $X$ has full column rank, $\widehat\beta=(X^\top X)^{-1}X^\top y$; if columns are dependent, fitted values can still be unique even while coefficient vectors are not. Polynomial regression is linear least squares when columns such as $x$ and $x^2$ are used, because the unknown coefficients enter linearly.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Definition and Examples of Linear Functions){{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion)

## Properties
At the line fit, the normal equations say $\sum_i e_i=0$ and $\sum_i x_i e_i=0$. The first is why the line goes through the sample means; the second says the residuals have no remaining linear association with the predictor in the fitted sample. Neither identity says the true errors have mean zero or are independent. Those are separate modelling assumptions for statistical inference. For a model with no intercept, $\sum e_i=0$ need not hold.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line){{cite:dodge2008}} (p. 305, normal equations)

If the conditional errors are independent normal variables with common variance, minimizing $Q$ also maximizes their likelihood for the regression coefficients. Normality is therefore one route to likelihood-based intervals, not a requirement to calculate the minimizing line. Under unequal error variances, weighted least squares can put more weight on more precise observations; with large outliers, absolute-deviation or robust criteria can yield a quite different fit. The chosen loss function says which kinds of mistakes the method treats as costly.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, related weighted methods and outlier sensitivity){{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion)

Curved relationships can still use linear least squares if they are linear in their parameters. A quadratic $b_0+b_1x+b_2x^2$ fits by adding an $x^2$ column. For a positive response model $y=ae^{bx}$, fitting $\log y=\log a+bx$ instead minimizes *squared log-scale residuals*; $e^b$ is a multiplicative change per unit of $x$. Likewise $y=ax^b$ can be fitted on log–log axes, and a logistic-shaped response may be linearized on a logit scale when the transformed quantity is defined. These transformations change the error scale and can change which observations drive the fit.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, linear functions and transformed predictors){{cite:nist_nonnormal_errors_pmd2002}} (§4.4.5.3, transformations)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For the line, differentiating $Q=\sum_i(y_i-b_0-b_1x_i)^2$ gives $\partial Q/\partial b_0=-2\sum_i e_i$ and $\partial Q/\partial b_1=-2\sum_i x_i e_i$. The first normal equation yields $b_0=\bar y-b_1\bar x$. Substituting into the second yields $\sum_i(x_i-\bar x)(y_i-\bar y)=b_1\sum_i(x_i-\bar x)^2$, proving the stated formulas. The quadratic form in a perturbation $(u,v)$ is $\sum_i(u+vx_i)^2$, positive for every nonzero pair when not all $x_i$ coincide; hence the critical point is the unique global minimum. For a line through the origin, differentiating $\sum_i(y_i-bx_i)^2$ gives $b\sum_i x_i^2=\sum_i x_iy_i$.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line)

In matrix form, $\|y-X(\widehat\beta+h)\|^2=\|y-X\widehat\beta\|^2-2h^\top X^\top(y-X\widehat\beta)+\|Xh\|^2$. The middle term vanishes at a solution of the normal equations, leaving a nonnegative difference. This proves global optimality, explains projection, and shows why dependent columns can yield multiple coefficients with the same fitted vector. If errors are iid $N(0,\sigma^2)$, their log-likelihood in $\beta$, up to constants, is $-Q(\beta)/(2\sigma^2)$, so its maximizer is the same fit.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, linear criterion){{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion)
:::
:::

## Worked example — Advertising and sales
A company records monthly advertising spending $x$ and sales $y$, both in units of $10\,000$ dollars. The ten paired measurements are

| Month | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Spending $x$ | 1.2 | 0.8 | 1.0 | 1.3 | 0.7 | 0.8 | 1.0 | 0.6 | 0.9 | 1.1 |
| Sales $y$ | 101 | 92 | 110 | 120 | 90 | 82 | 93 | 75 | 91 | 105 |

The data give $\bar x=0.94$, $\bar y=95.9$, $\sum(x_i-\bar x)^2=0.444$, and $\sum(x_i-\bar x)(y_i-\bar y)=23.34$. Thus $b_1=23.34/0.444\approx52.6$ and $b_0=95.9-52.6(0.94)\approx46.5$, giving $\widehat y=46.5+52.6x$ at the displayed precision. An additional $10\,000$ dollars of advertising is associated with about $526\,000$ dollars more sales on this fitted scale. The line describes past months; a causal claim would need a design that rules out other reasons for spending and sales to move together.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line)

### A curved example — Melanoma and latitude
The melanoma rates per $100\,000$ white males at nine US locations illustrate how the response scale changes interpretation.

| Latitude | 32.8 | 33.9 | 34.1 | 37.9 | 40.0 | 40.8 | 41.7 | 42.2 | 45.0 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rate | 9.0 | 5.9 | 6.6 | 5.8 | 5.5 | 3.0 | 3.4 | 3.1 | 3.8 |

A straight-line fit rounds to $\widehat y=20.6-0.399x$, but the southernmost location lies high above that line. A quadratic fit rounds to $\widehat y=66.4-2.81x+0.0314x^2$ and follows the bend. Fitting the logarithm of the rate gives $\widehat{\log y}=4.51-0.0761x$; each degree further north corresponds to a fitted multiplier $e^{-0.0761}\approx0.93$, a decline of about $7\%$. The quadratic and log fit answer different questions: one minimizes squared errors in rates, the other in log rates, and neither establishes a causal effect of latitude.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, polynomial and transformed linear models){{cite:nist_nonnormal_errors_pmd2002}} (§4.4.5.3, transformations)

**Your turn.** Fit a line with an intercept to $(x,y)=(1,2),(2,3),(3,5)$. Find its slope and intercept, and explain why fitting a line through the origin would solve a different problem.

::: {.callout-tip collapse="true" title="Answer"}
Here $\bar x=2$ and $\bar y=10/3$. The centered cross-product is $3$ and the centered $x$ sum of squares is $2$, so $b_1=3/2=1.5$ and $b_0=10/3-(3/2)2=1/3$. The fitted line is $\widehat y=1/3+1.5x$. A line forced through the origin must have zero intercept; it minimizes squared errors over a smaller set of candidate lines and generally has another slope.
:::

## Common misconceptions
“Best-fitting” always needs a loss and direction: least squares minimizes vertical squared errors in $y$, whereas swapping response and predictor minimizes horizontal errors and usually gives another line. Least squares does not require normal errors to *compute* the line, though normality supports particular likelihood and interval claims. A polynomial in $x$ is not automatically nonlinear in its coefficients; $b_0+b_1x+b_2x^2$ remains a linear model for least-squares computation. Finally, a fitted slope is an association conditional on the model and sample, not evidence by itself that changing $x$ causes $y$ to change.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Definition and Examples of Linear Functions){{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion)

## Assumptions and limits
With $x=(0,1,2)$ and $y=(0,1,2)$, the least-squares slope is $1$; replacing the final response by $100$ moves it to $50$. This shows the effect a single unusual point can have under squared loss. If every $x_i$ is identical, the slope and intercept cannot be separately determined. If two design-matrix columns are duplicates, the coefficient vector is nonunique even though its fitted responses can still be determined. If the response is an exponentially growing rate, a line on the original scale can predict negative values or give a misleading additive interpretation; a transformed or appropriately constrained model may be needed. And extrapolating far beyond the observed $x$ range can magnify small model errors.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, outlier sensitivity and extrapolation)

## Connections
The [least-squares line](least-squares-line.qmd) is the two-coefficient case, while [ordinary least squares](ordinary-least-squares.qmd) develops the matrix fit. The [normal-equations question](../questions/ex-inf-normal-equations.qmd) derives the line formulas, the [through-origin question](../questions/ex-inf-line-through-origin.qmd) changes the candidate set, and the [ridge question](../questions/ex-sl-18-2.qmd) shows how a penalty selects a unique coefficient vector when two predictors coincide. In a [generalised linear model](generalised-linear-model.qmd), Fisher scoring can solve a sequence of weighted least-squares problems rather than minimize the ordinary squared response residuals once.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, related methods)

## History
Legendre's 1805 appendix presented a general method for reconciling more observational equations than unknown quantities by minimizing the sum of squared errors. He explicitly derived the arithmetic mean as the least-squares answer when several observations estimate one common value. Astronomical orbit determination motivated the work; the same principle later became a standard way to fit statistical regression models. Accounts also describe Gauss's independent earlier use, but Legendre's publication supplied an early explicit statement of the method.{{cite:legendre1805}} (pp. 72–75, appendix “Sur la Méthode des moindres quarrés”){{cite:dodge2008}} (p. 304, Least-Squares Method){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Why Least Squares?)
