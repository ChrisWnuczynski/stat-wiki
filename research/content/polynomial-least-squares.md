## Lead context
Polynomial least squares estimates the coefficients of a polynomial mean by minimising the sum of squared residuals. The mean is a curve in the predictor and a straight line in the coefficients. The fit is therefore ordinary linear least squares on the powers of the predictor, not a nonlinear search.{{cite:james_islr2013}} (pp. 266–267, §7.1){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1)

## Motivating example
Wage plotted against age rises and then flattens. A straight line in age cannot follow that bend. A polynomial in age can: each extra power is another column, and least squares estimates the columns together. A degree-4 polynomial is the curve James, Witten, Hastie, and Tibshirani fit to the Wage data, and it is still linear in its five coefficients. The bend is in age. The estimation is the linear one.{{cite:james_islr2013}} (p. 267, §7.1)

## Definition
For a single predictor $x$ and a chosen degree $d$, the mean is

$$
y_i=\beta_0+\beta_1 x_i+\beta_2 x_i^2+\cdots+\beta_d x_i^d+\varepsilon_i.
$$


The coefficients minimise

$$
\sum_{i=1}^n\bigl(y_i-\beta_0-\beta_1 x_i-\cdots-\beta_d x_i^d\bigr)^2.
$$


The powers $1, x, x^2, \ldots, x^d$ are known once $x$ is known, so the normal equations are linear in $\beta_0,\ldots,\beta_d$. A function is statistically linear when the unknown coefficients sit outside known functions of the predictors. A quadratic in $x$ meets that test. A mean such as $\beta_0\exp(-\beta_1 x)$ does not, because $\beta_1$ sits inside the function.{{cite:james_islr2013}} (p. 266, §7.1){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1){{cite:dodge2008}} (p. 373)

## Properties
The fitted polynomial $\hat f(x)$ is a linear combination of the estimated coefficients. Under an additive error model with fixed $x$ and uncorrelated errors of variance $\sigma^2$, the variance of $\hat f(x_0)$ at a chosen $x_0$ is $\sigma^2$ times a quadratic form in the powers of $x_0$. That variance is a pointwise scale. A band drawn at each $x_0$ from the pointwise standard error does not, by that construction, cover the whole curve at once.{{cite:james_islr2013}} (pp. 267–268, §7.1)

Adding a power cannot raise the residual sum of squares on the data used to fit the curve. The degree-$d$ polynomial includes the degree-$(d-1)$ polynomial as the case $\beta_d=0$, so the minimiser is at least as close, in squared error, as the lower degree. The drop is the price of one more free coefficient. It is evidence of curvature only together with the plot.{{cite:james_islr2013}} (pp. 266–267, §7.1)

On four points the algebra is small enough to see. For $(x,y)=(0,1)$, $(1,2)$, $(2,2)$, and $(3,5)$, the power sums are $n=4$, $\sum x=6$, $\sum x^2=14$, $\sum x^3=36$, $\sum x^4=98$, $\sum y=10$, $\sum xy=21$, and $\sum x^2 y=55$. The normal equations have the unique solution $\hat\beta_0=1.2$, $\hat\beta_1=-0.3$, $\hat\beta_2=0.5$. The fitted values are $1.2$, $1.4$, $2.6$, and $4.8$. The residuals are $-0.2$, $0.6$, $-0.6$, and $0.2$, and the residual sum of squares is $0.8$. The straight line on the same points has intercept $0.7$ and slope $1.2$, and its residual sum of squares is $1.8$. The quadratic spends one extra coefficient and removes $1.0$ from that sum.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1)

## Statistical use
Choose a small degree, fit the powers by [ordinary least squares](ordinary-least-squares.qmd), and plot $\hat f(x)$ on the range of $x$ that was observed. James and coauthors warn against a degree above 3 or 4: for large $d$ the polynomial can take strange shapes, especially near the boundary of the observed $x$. Compare the residual sum of squares with that of the straight line on the same points. A smaller sum is expected once extra coefficients are free. It becomes a reason to keep the bend when the plot shows the bend inside the range, not only at the two ends.{{cite:james_islr2013}} (pp. 266–268, §7.1)

The coefficients themselves are a poor summary of a high-degree fit. The fitted value at one age depends on all of them at once. Report $\hat f(x)$ at ages inside the sample, not a list of powers as if each were a separate slope.{{cite:james_islr2013}} (p. 266, §7.1)

## Worked example
The four-point quadratic above has coefficients $1.2$, $-0.3$, and $0.5$, and residual sum of squares $0.8$. The straight line on the same points has residual sum of squares $1.8$. The fitted curve falls slightly from $x=0$ to $x=1$, because the linear coefficient is negative, and then rises, because the square coefficient is positive. Both statements are readings of one fitted function. Neither coefficient is the change in $y$ per unit $x$.{{cite:james_islr2013}} (p. 266, §7.1){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1)

**Your turn.** Fit $y=\beta_0+\beta_1 x+\beta_2 x^2$ to $(0,1)$, $(1,0)$, and $(2,1)$. Give the three coefficients and the residual sum of squares.

::: {.callout-tip collapse="true" title="Answer"}
The three points lie on $(x-1)^2=1-2x+x^2$, so the coefficients are $1$, $-2$, and $1$. Every residual is $0$, and the residual sum of squares is $0$.
:::

## Common misconceptions
Polynomial least squares is not [nonlinear regression](nonlinear-regression.qmd). The mean is nonlinear as a function of $x$ and linear as a function of $\beta$. The test is whether the coefficients can be moved outside known functions of the data. If they can, the fit is the linear one, extra columns and all. Dodge's nonlinear example, a mean in which two coefficients sit inside exponentials, fails that test and is solved iteratively. A quadratic does not.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1){{cite:dodge2008}} (p. 373)

A large degree is not a closer look at the same curve. It is a more flexible function, and near the ends of the age range the extra flexibility is where a polynomial is least trustworthy. The pointwise band at twice the standard error is not a statement that the whole curve lies inside the band with the same coverage. Each $x_0$ has its own interval.{{cite:james_islr2013}} (pp. 266–268, §7.1)

## History
Least squares, as a way to combine inconsistent observations, was published by Legendre in 1805, and Gauss and Adrain were working with the same squared-error criterion in the same period. The extension from a straight line to a polynomial keeps that criterion and adds powers as further predictors. The modern warning about high degree is the same warning as for any flexible linear model: the fit can follow the sample near the edge of the observed range.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1){{cite:james_islr2013}} (p. 266, §7.1)

## Connections
The one-predictor case of [ordinary least squares](ordinary-least-squares.qmd) is the degree-1 polynomial. [Multiple linear regression](multiple-linear-regression.qmd) is the same algebra with columns that need not be powers of a single $x$. [Nonlinear regression](nonlinear-regression.qmd) begins when a coefficient moves inside the function and the normal equations stop being linear. A degree so high that the curve follows the sample is the overfitting problem for this particular linear model.{{cite:james_islr2013}} (pp. 266–267, §7.1){{cite:dodge2008}} (p. 304)
