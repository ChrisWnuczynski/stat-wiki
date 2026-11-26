## Lead context
One measured input is used to describe the mean of a numerical response by a straight line, with the line chosen to make the squared vertical errors as small as possible.{{cite:nist_ls_straight2002}} (§4.4.3.1, straight-line least squares)

## Motivating example
Five seedlings are grown under 2, 4, 6, 8 and 10 hours of light a day, and their growth is 3, 4, 8, 9 and 11 millimetres. A straight summary is wanted: how many extra millimetres go with one extra hour in these five pots. The hours were set by the grower, so they are treated as fixed numbers and growth is the response. Fitting a [least-squares line](least-squares-line.qmd) answers that slope question inside this sample; without randomisation and control of pot-level differences, the calculation alone does not establish that extra light caused the extra growth.{{cite:nist_ls_straight2002}} (§4.4.3.1, straight-line model){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, linear in the parameters)

## Intuition
Each candidate line produces a vertical gap between observed growth and the line's height at that input. Squaring stops positive and negative gaps from cancelling and penalises large misses more heavily than small ones; because the sum of squares is a strictly convex quadratic in the intercept and slope when inputs vary, its unique critical point is the global minimum.{{cite:nist_ls_straight2002}} (§4.4.3.1, criterion $Q$){{cite:dodge2008}} (p. 305, partial derivatives)

The sample fit $\hat y=\hat\beta_0+\hat\beta_1 x$ that minimises squared residuals is an estimate, distinct from the unknown population mean line $\E(Y_i)=\beta_0+\beta_1 x_i$. Distinct straight lines with different slopes always intersect somewhere—though not necessarily inside the observed input range; for example, the seedling fit $0.70+1.05x$ and a hypothetical mean $1+x$ cross at $x=6$ while differing at every other input—so agreement at a single $x$ does not make the fitted line equal the true mean function. Replacing $(\beta_0,\beta_1)$ by $(\hat\beta_0,\hat\beta_1)$ is estimation, and the remaining squared residuals estimate the error variance.{{cite:nist_ls_straight2002}} (§4.4.3.1, General LS Criterion and Comparison of LS Line and True Line)

## Definition
With fixed inputs $x_1,\ldots,x_n$, not all equal, and responses $y_1,\ldots,y_n$, the least-squares intercept and slope minimise

$$
Q(b_0,b_1)=\sum_{i=1}^n\bigl(y_i-b_0-b_1 x_i\bigr)^2.
$$

Setting the normal equations $\sum_i(y_i-\hat\beta_0-\hat\beta_1 x_i)=0$ and $\sum_i x_i(y_i-\hat\beta_0-\hat\beta_1 x_i)=0$ gives the centred-product ratio developed under [regression slope](regression-slope.qmd),

$$
\hat\beta_1=\frac{\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y)}{\sum_{i=1}^n(x_i-\bar x)^2},\qquad
\hat\beta_0=\bar y-\hat\beta_1\bar x.
$$

{{cite:nist_ls_straight2002}} (§4.4.3.1, straight-line estimators){{cite:dodge2008}} (p. 305, normal equations)

The regression model writes random responses as $Y_i=\beta_0+\beta_1 x_i+\varepsilon_i$ with $\E(\varepsilon_i)=0$. Least squares estimates $\beta_0$ and $\beta_1$ without assuming Gaussian errors; Gaussian errors enter when comparing a standardized estimator to a Student-$t$ reference law. With $p=2$ mean parameters, the residual standard deviation is

$$
\hat\sigma=\sqrt{\frac{Q}{n-2}}.
$$

{{cite:nist_ls_straight2002}} (§4.4.3.1, Quantifying the Quality of the Fit for Real Data){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Definition of a Linear Least Squares Model)

## Interpretation
The slope $\hat\beta_1$ is the change in fitted mean per unit increase in $x$ across the observed range of $x$, while $\hat\beta_0$ is the fitted height at $x=0$. When $x=0$ lies far outside the design, $\hat\beta_0$ is an extrapolation and is coupled to $\hat\beta_1$ whenever $\bar x\neq 0$: an estimation error in $\hat\beta_1$ shifts $\hat\beta_0=\bar y-\hat\beta_1\bar x$ in the opposite direction when $\bar x>0$. Centring the input at $x_i-\bar x$ redefines the intercept as the fitted height $\bar y$ at $\bar x$, removing the $-\hat\beta_1\bar x$ coupling.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line)

Dividing the first normal equation by $n$ shows that the fitted line always passes through $(\bar x,\bar y)$. For the seedlings, $\bar x=6$ and $\bar y=7$, so the fitted height at $6$ hours is $7$ millimetres; that algebraic constraint does not say the conditional mean equals $\bar y$ at other inputs.{{cite:dodge2008}} (p. 305, first normal equation){{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line)

## Properties
Under $\E(Y_i)=\beta_0+\beta_1 x_i$ with fixed $x_i$ not all equal, $\hat\beta_1$ and $\hat\beta_0$ are unbiased for $\beta_1$ and $\beta_0$, as proved generally in [least-squares estimators are unbiased](least-squares-estimators-are-unbiased.qmd). If the errors are also uncorrelated with common variance $\sigma^2$, then $\operatorname{Var}(\hat\beta_1)=\sigma^2/S_{xx}$ where $S_{xx}=\sum_i(x_i-\bar x)^2$: wider input spread reduces slope variance, whereas identical inputs give $S_{xx}=0$ and leave the slope undefined.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line)

Substituting $\hat\sigma^2=Q/(n-2)$ yields the estimated standard error $\hat\sigma/\sqrt{S_{xx}}$. Exact $t_{n-2}$ intervals and tests require independent, equal-variance normal errors in addition to the straight-line mean.{{cite:nist_ls_straight2002}} (§4.4.3.1, Quantifying the Quality of the Fit for Real Data)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Setting the partial derivatives $-2\sum_i(y_i-b_0-b_1 x_i)$ and $-2\sum_i x_i(y_i-b_0-b_1 x_i)$ of $Q$ to zero gives $\hat\beta_0=\bar y-\hat\beta_1\bar x$ and, via the centred-product reduction in [regression slope](regression-slope.qmd), $\hat\beta_1=S_{xy}/S_{xx}$.{{cite:dodge2008}} (p. 305, normal equations){{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line)

Because $\sum_i(x_i-\bar x)=0$ and $\sum_i(x_i-\bar x)x_i=S_{xx}$, writing $\hat\beta_1=\sum_i(x_i-\bar x)Y_i/S_{xx}$ under $\E(Y_i)=\beta_0+\beta_1 x_i$ gives

$$
\E(\hat\beta_1)=\frac{1}{S_{xx}}\sum_{i=1}^n(x_i-\bar x)(\beta_0+\beta_1 x_i)=\beta_1,
$$

and $\E(\hat\beta_0)=\E(\bar Y)-\beta_1\bar x=\beta_0$. When the $Y_i$ are uncorrelated with variance $\sigma^2$, $\operatorname{Var}(\hat\beta_1)=\sigma^2\sum_i(x_i-\bar x)^2/S_{xx}^2=\sigma^2/S_{xx}$.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line)
:::
:::

## Statistical use — Reading a slope inside the observed hours
Quote $\hat\beta_1$ as the estimated change in mean response per unit of $x$ within the observed input range, paired with $\hat\sigma/\sqrt{S_{xx}}$ when uncorrelated equal-variance errors are plausible. At any input $x$, a prediction interval for one new response $Y$ is wider than a confidence interval for $\beta_0+\beta_1 x$ because the new observation carries its own error variance $\sigma^2$ on top of estimation uncertainty in the line. Evaluating $\hat\beta_0+\hat\beta_1 x$ outside the observed inputs is an extrapolation whose bias can grow rapidly if the true conditional mean curves.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Disadvantages of Linear Least Squares){{cite:nist_ls_straight2002}} (§4.4.3.1, Quantifying the Quality of the Fit for Real Data)

## Worked example
For the five seedlings, $\bar x=6$, $\bar y=7$, $S_{xx}=40$ and $S_{xy}=42$. The slope is $42/40=1.05$ millimetres per hour, and the intercept is $7-1.05\times 6=0.70$. The fitted heights are $2.8$, $4.9$, $7.0$, $9.1$ and $11.2$. The residuals are $0.2$, $-0.9$, $1.0$, $-0.1$ and $-0.2$, and

$$
Q=0.2^2+(-0.9)^2+1^2+(-0.1)^2+(-0.2)^2=1.90.
$$

With $n-2=3$, $\hat\sigma=\sqrt{1.90/3}=\sqrt{19/30}\approx 0.7958$. The estimated standard error of the slope is $\sqrt{(19/30)/40}=\sqrt{19/1200}\approx 0.1258$. At $7$ hours, between the observed inputs, the fitted mean is $0.70+1.05\times 7=8.05$ millimetres.{{cite:nist_ls_straight2002}} (§4.4.3.1, estimators and residual standard deviation)

Replace the last growth $11$ by $20$, as if one pot had been mis-recorded. Then $S_{xy}=78$, the slope becomes $78/40=1.95$, and the intercept becomes $8.8-1.95\times 6=-2.90$. One point moved the slope from $1.05$ to $1.95$. Squared error did what the criterion asks: it chased the large gap.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, sensitivity to outliers)

**Your turn.** For the points $(0,1)$, $(1,3)$ and $(2,2)$, find the least-squares slope and intercept, and the fitted height at the mean of $x$.

::: {.callout-tip collapse="true" title="Answer"}
Here $\bar x=1$, $\bar y=2$, $S_{xx}=2$ and $S_{xy}=1$, so the slope is $1/2=0.5$ and the intercept is $2-0.5\times 1=1.5$. The fitted height at $x=1$ is $2$, the mean of $y$. The residual sum of squares is $1.5$.
:::

## Common misconceptions
A fitted slope is not automatically the causal effect of intervening on $x$: even with assigned light hours, unmeasured pot differences enter the errors, and in observational data confounding can drive $\hat\beta_1$ without any causal mechanism.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Modeling Workhorse)

Vertical least squares minimises neither absolute vertical discrepancies nor horizontal discrepancies; regressing $x$ on $y$ reverses the roles and yields a different line. Conversely, $\beta_0+\beta_0\beta_1 x$ is a straight line in $x$ yet multiplies two unknown parameters, so the linear least-squares closed form does not apply.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Nonlinear Model Example)

When $x=0$ was never observed, $\hat\beta_0$ need not represent a physically meaningful baseline, and a strong in-sample correlation does not justify extrapolating the line beyond the largest observed $x$.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Disadvantages of Linear Least Squares)

## Assumptions and limits — When the squared-error line misleads
If all inputs are identical, $S_{xx}=0$ and no slope is defined. If the conditional mean bends, the best straight line can still describe the process poorly: over a wide range a straight line with nonzero slope grows without bound at both ends and has no horizontal asymptote. That unbounded behaviour is a property of a straight line in $x$ with nonzero slope rather than of linearity in the coefficients—a model such as $\beta_0+\beta_1\exp(-x)$ is linear in $(\beta_0,\beta_1)$ yet tends to the horizontal asymptote $\beta_0$ as $x\to\infty$, whereas extrapolating a straight line past the observed inputs cannot level off. One outlier, as when the fifth seedling growth changes from $11$ to $20$, moves $\hat\beta_1$ from $1.05$ to $1.95$ because squared loss weights large residuals heavily. Serially correlated errors, such as repeated measurements on one plant, leave $\hat\beta_1$ unbiased under a straight mean while invalidating $\sigma^2/S_{xx}$.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Definition of a Linear Least Squares Model, Examples of Linear Functions, and Disadvantages of Linear Least Squares){{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line)

## Connections
The [least-squares line](least-squares-line.qmd) is the fitted sample line and [regression slope](regression-slope.qmd) develops $\hat\beta_1=S_{xy}/S_{xx}$ in detail. Adding independent normal errors embeds this specification in the [normal linear model](normal-linear-model.qmd) and supplies an exact $t_{n-2}$ [pivot](pivot.qmd) for $(\hat\beta_1-\beta_1)/(\hat\sigma/\sqrt{S_{xx}})$. Adding further covariates leads to [multiple linear regression](multiple-linear-regression.qmd), where [multicollinearity](multicollinearity.qmd) is the multi-predictor analogue of a small $S_{xx}$, while [Poisson regression](poisson-regression.qmd) replaces both the identity link and constant variance for count responses.{{cite:nist_ls_straight2002}} (§4.4.3.1, LS for Straight Line)

## History
The least-squares criterion minimises the sum of squared residuals between observed and fitted values. Legendre published the method in 1805, while historical accounts trace independent development in the late eighteenth and early nineteenth centuries to Gauss, Legendre, and possibly Adrain.{{cite:dodge2008}} (p. 304, least-squares method){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Why "Least Squares"?)
