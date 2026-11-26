## Motivating example
A company wants a straight line relating monthly advertising spending to sales. No line passes through all ten observed points, so a rule is needed to trade one discrepancy against another. Least squares chooses the line with the smallest sum of squared *vertical* discrepancies. Squaring prevents positive and negative discrepancies from cancelling and penalises one large miss more heavily than several small ones. The resulting fit summarises association in the observed months; whether it predicts future months accurately depends on whether the underlying relationship remains stable.{{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion and LS for Straight Line)

## Intuition
For a proposed model $f(x_i;\beta)$, each residual $e_i=y_i-f(x_i;\beta)$ is an observed response minus its fitted value. Least squares adjusts $\beta$ until the residual vector $(e_1,\ldots,e_n)^\top$ has minimum Euclidean length. When $f(x_i;\beta)$ is linear in $\beta$, that minimum is the orthogonal projection of the response vector onto the subspace spanned by the predictor columns, and the normal equations express the orthogonality of the optimal residual vector to every predictor column. The criterion is purely algebraic and requires no probability model for the responses or errors; the [normal linear model](normal-linear-model.qmd) and [Gaussian linear model](gaussian-linear-model.qmd) supply the sampling assumptions needed for standard errors, confidence intervals, and tests.{{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion and LS for Straight Line){{cite:dodge2008}} (pp. 304–305, Least-Squares Method)

## Definition
Given responses $y_1,\ldots,y_n$ and candidate predictions $f(x_i;\beta)$, **least squares** chooses $\widehat\beta$ to minimize the residual sum of squares

$$Q(\beta)=\sum_{i=1}^n\{y_i-f(x_i;\beta)\}^2.$$

For the two-parameter [least-squares line](least-squares-line.qmd) $f(x_i;b_0,b_1)=b_0+b_1x_i$, with the $x_i$ not all equal, the unique minimizer is

$$b_1=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}{\sum_i(x_i-\bar x)^2},\qquad b_0=\bar y-b_1\bar x,$$

so the fitted line passes through $(\bar x,\bar y)$. Restricting the candidate family to lines $bx$ through the origin yields $b=\sum_i x_iy_i/\sum_i x_i^2$ when $\sum_i x_i^2>0$; omitting the intercept is a substantive restriction on the model, not an algebraic simplification.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line){{cite:dodge2008}} (p. 305, normal equations)

For a design matrix $X$ and response vector $y$, [ordinary least squares](ordinary-least-squares.qmd) minimizes $\|y-X\beta\|^2$ via the normal equations $X^\top X\widehat\beta=X^\top y$. When $X$ has full column rank, $\widehat\beta=(X^\top X)^{-1}X^\top y$; when columns are linearly dependent, the orthogonal projection $X\widehat\beta$ remains unique even though $\widehat\beta$ is not. Polynomial models using columns such as $x$ and $x^2$ remain linear least-squares problems because $\beta$ enters $X\beta$ linearly.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Definition of a Linear Least Squares Model and Examples of Linear Functions){{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion)

## Properties
For a straight line with an intercept, the normal equations require $\sum_i e_i=0$ and $\sum_i x_i e_i=0$: the fitted line passes through $(\bar x,\bar y)$ and leaves no sample linear association between the [residuals](error-and-residual.qmd) and $x$. Both identities come from differentiating $Q$ rather than from properties of the unobservable errors, and $\sum_i e_i=0$ need not hold when the intercept is omitted.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line){{cite:dodge2008}} (p. 305, normal equations)

The quadratic objective determines which discrepancies govern the fit. Under independent normal errors with common variance in the [normal linear model](normal-linear-model.qmd), minimizing $Q(\beta)$ coincides with maximizing the Gaussian likelihood in $\beta$. When observations have unequal variances, weighted least squares rescales squared discrepancies by precision; when heavy-tailed errors or gross outliers occur, absolute-error or Huber-type objectives limit the pull of single points.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Modeling Workhorse and Disadvantages of Linear Least Squares){{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion)

Curved relationships can still be fitted by linear least squares when the unknown coefficients enter linearly, as in $b_0+b_1x+b_2x^2$. Transforming the response changes the loss function itself: fitting $\log y=\log a+bx$ to positive responses minimizes *squared log-scale residuals*, with $e^b$ giving the fitted multiplicative factor per unit increase in $x$. Log–log and logit-transformed fits likewise alter the error scale and therefore change which observations carry the most weight.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Examples of Linear Functions){{cite:nist_nonnormal_errors_pmd2002}} (§4.4.5.3, transformations)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For the straight line, differentiating $Q=\sum_i(y_i-b_0-b_1x_i)^2$ gives $\partial Q/\partial b_0=-2\sum_i e_i$ and $\partial Q/\partial b_1=-2\sum_i x_i e_i$. Setting the first derivative to zero gives $b_0=\bar y-b_1\bar x$, and substituting into the second gives $\sum_i(x_i-\bar x)(y_i-\bar y)=b_1\sum_i(x_i-\bar x)^2$. Any nonzero perturbation $(u,v)$ adds $\sum_i(u+vx_i)^2>0$ whenever the $x_i$ are not all equal, establishing a unique global minimum. Differentiating $\sum_i(y_i-bx_i)^2$ yields $b\sum_i x_i^2=\sum_i x_iy_i$.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line)

In matrix form, the [least-squares decomposition](least-squares-decomposition.qmd) writes $\|y-X(\widehat\beta+h)\|^2=\|y-X\widehat\beta\|^2-2h^\top X^\top(y-X\widehat\beta)+\|Xh\|^2$. At any solution of $X^\top X\widehat\beta=X^\top y$ the cross term vanishes, leaving $\|y-X\widehat\beta\|^2+\|Xh\|^2\ge\|y-X\widehat\beta\|^2$. Equality holds if and only if $Xh=0$, which shows both global optimality and why dependent columns admit multiple coefficient vectors with the same fitted projection. Under iid $N(0,\sigma^2)$ errors, the log-likelihood in $\beta$ up to additive constants in $\sigma^2$ is $-Q(\beta)/(2\sigma^2)$, maximized by the same $\widehat\beta$.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Why "Least Squares"?){{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion)
:::
:::

## Worked example — Advertising and sales
A company records monthly advertising spending $x$ and sales $y$, both in units of $10\,000$ dollars:

| Month | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Spending $x$ | 1.2 | 0.8 | 1.0 | 1.3 | 0.7 | 0.8 | 1.0 | 0.6 | 0.9 | 1.1 |
| Sales $y$ | 101 | 92 | 110 | 120 | 90 | 82 | 93 | 75 | 91 | 105 |

The sample summaries are $\bar x=0.94$, $\bar y=95.9$, $\sum(x_i-\bar x)^2=0.444$, and $\sum(x_i-\bar x)(y_i-\bar y)=23.34$. Hence $b_1=23.34/0.444\approx52.6$ and $b_0=95.9-52.6(0.94)\approx46.5$, giving $\widehat y=46.5+52.6x$ at the displayed precision: $10\,000$ dollars more spending corresponds to about $526\,000$ dollars higher fitted sales across these ten months. That summary describes observed co-movement; attributing sales changes causally to spending would require a study design that rules out common drivers such as seasonal demand.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line)

### A curved example — Melanoma and latitude
Melanoma rates per $100\,000$ white males at nine US locations show how the response scale changes the optimization target:

| Latitude | 32.8 | 33.9 | 34.1 | 37.9 | 40.0 | 40.8 | 41.7 | 42.2 | 45.0 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rate | 9.0 | 5.9 | 6.6 | 5.8 | 5.5 | 3.0 | 3.4 | 3.1 | 3.8 |

A straight-line fit rounds to $\widehat y=20.6-0.399x$, leaving the southernmost location far above that line. Adding $x^2$ gives $\widehat y=66.4-2.81x+0.0314x^2$, which tracks the bend on the rate scale. Fitting $\log y$ instead gives $\widehat{\log y}=4.51-0.0761x$, where each degree further north multiplies the fitted rate by $e^{-0.0761}\approx0.93$, a decline of about $7\%$. The quadratic fit minimizes squared rate errors, whereas the log-linear fit minimizes squared log-rate errors; neither establishes a direct causal effect of latitude.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Examples of Linear Functions){{cite:nist_nonnormal_errors_pmd2002}} (§4.4.5.3, transformations)

**Your turn.** Fit a line with an intercept to $(x,y)=(1,2),(2,3),(3,5)$. Find its slope and intercept, and explain why fitting a line through the origin would solve a different problem.

::: {.callout-tip collapse="true" title="Answer"}
Here $\bar x=2$ and $\bar y=10/3$. The centered cross-product is $3$ and the centered $x$ sum of squares is $2$, so $b_1=3/2=1.5$ and $b_0=10/3-(3/2)2=1/3$. The fitted line is $\widehat y=1/3+1.5x$. A line forced through the origin must have zero intercept; it minimizes squared errors over a smaller set of candidate lines and generally has another slope.
:::

## Common misconceptions
“Best-fitting” is defined only relative to a loss and a direction: vertical least squares minimizes squared discrepancies in $y$, whereas regressing $x$ on $y$ minimizes horizontal squared discrepancies and produces a different line unless the points are already collinear. A polynomial $b_0+b_1x+b_2x^2$ is curved in $x$ yet linear in $(b_0,b_1,b_2)$, whereas $\beta_0+\beta_0\beta_1 x$ is a straight line in $x$ yet nonlinear in its parameters. Finally, a least-squares slope summarises conditional association in the sample rather than the effect of an external intervention on $x$.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Definition of a Linear Least Squares Model and Nonlinear Model Example){{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion)

## Assumptions and limits
Squared loss gives extreme observations high leverage on the fit: for $x=(0,1,2)$ and $y=(0,1,2)$ the slope is $1$, whereas replacing the third response by $100$ pulls the slope to $50$. If all $x_i$ coincide, slope and intercept are not separately identifiable; more generally, duplicated or collinear columns in $X$ leave individual slopes nonunique even while the projected vector $X\widehat\beta$ stays unique. An unconstrained straight line can also predict negative values for positive rates or mislead severely when extrapolated beyond the observed $x$ range.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Disadvantages of Linear Least Squares)

## Connections
The [least-squares line](least-squares-line.qmd) treats the two-parameter straight-line fit, while [ordinary least squares](ordinary-least-squares.qmd) establishes the matrix estimator and its moment properties within [regression analysis](regression-analysis.qmd). Adding normal-error assumptions leads to the [normal linear model](normal-linear-model.qmd) and small-sample $t$ inference in the [Gaussian linear model](gaussian-linear-model.qmd). [Ridge regression](ridge-regression.qmd) adds an $\ell_2$ penalty to restore uniqueness and reduce variance under collinearity, as illustrated in the [ridge question](../questions/ex-sl-18-2.qmd), alongside the [normal-equations question](../questions/ex-inf-normal-equations.qmd) and [through-origin question](../questions/ex-inf-line-through-origin.qmd). In a [generalised linear model](generalised-linear-model.qmd), maximum likelihood solves iteratively reweighted least-squares subproblems rather than a single unweighted sum of squares.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Modeling Workhorse)

## History
Legendre's 1805 appendix introduced the method of least squares to reconcile overdetermined systems of astronomical equations by minimizing the sum of squared errors, noting the sample mean as the special case when repeated measurements estimate a single quantity. Gauss reported earlier independent use in orbital calculations, and the later probabilistic theory of error distributions grew around Legendre's algebraic criterion.{{cite:legendre1805}} (pp. 72–75, appendix “Sur la Méthode des moindres quarrés”){{cite:dodge2008}} (p. 304, Least-Squares Method){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Why "Least Squares"?)
