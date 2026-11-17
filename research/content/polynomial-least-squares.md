## Lead context
A curved mean can still be linear in its unknown coefficients. Polynomial least squares replaces the single predictor by its powers and then minimises the usual sum of squared residuals, so the arithmetic is the linear normal equations with extra columns.{{cite:james_islr2013}} (pp. 266–267, §7.1){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, a quadratic in the predictor is linear in the parameters)

## Motivating example
Wage tends to rise with age and then flatten. A straight line in age forces a constant increase per year. Replacing age by age, age squared, age cubed, and age to the fourth produces a curve that can bend, and the four coefficients, plus an intercept, are still estimated by least squares because each power is just another predictor. The plot people read is the whole curve, not any one coefficient.{{cite:james_islr2013}} (p. 267, §7.1, degree-4 polynomial for wage against age)

## Intuition
Each extra power is a new direction in which the fitted mean can move. The intercept and the linear term make a straight line. The square lets the slope change at a steady rate. Higher powers add more wiggles. Least squares picks the combination of those columns that makes the squared vertical gaps smallest. Because the columns enter only through coefficients that stand in front of them, the sum of squares is a quadratic bowl in those coefficients, and the bottom is a linear system.{{cite:james_islr2013}} (p. 266, §7.1, equation (7.1)){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, statistically linear functions)

The price of the extra wiggles shows up at the edge of the data. A high power grows quickly once $x$ leaves the middle of the sample, so a polynomial that looks smooth through the cloud can swing sharply near the smallest and largest $x$.{{cite:james_islr2013}} (p. 266, §7.1, behaviour for large degree and near the boundary)

## Definition
For observations $(x_i,y_i)$ and a chosen degree $d$, polynomial least squares minimises
\[
S(b_0,\ldots,b_d)=\sum_{i=1}^n\Bigl(y_i-b_0-b_1 x_i-b_2 x_i^2-\cdots-b_d x_i^d\Bigr)^2.
\]
The minimiser satisfies the normal equations obtained by differentiating $S$. In matrix form the design has a column of ones and columns $x$, $x^2$, through $x^d$, and the coefficient vector $\hat\beta$ solves that linear least-squares problem. The fitted value at a chosen $x_0$ is
\[
\hat f(x_0)=\hat\beta_0+\hat\beta_1 x_0+\cdots+\hat\beta_d x_0^d.
\]
Its estimated variance uses the estimated covariance matrix of $\hat\beta$ and the row $(1,x_0,\ldots,x_0^d)$.{{cite:james_islr2013}} (pp. 266–267, §7.1, equations (7.1) and (7.2))

The same construction is linear in the statistical sense even though $\hat f(x)$ is not a straight line. A model is linear here when the coefficients appear as multipliers of known functions of $x$. A quadratic $\beta_0+\beta_1 x+\beta_2 x^2$ meets that test. A mean $\beta_0\exp(-\beta_1 x)$ does not, and is left to nonlinear least squares.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, polynomial and other statistically linear examples){{cite:dodge2008}} (p. 372, linearity judged in the parameters)

## Properties
The fit reproduces the linear least-squares properties that follow from a mean which really is that polynomial and from errors with mean zero. The coefficients are linear functions of the responses, so their variances and covariances are determined by the design of the powers and by the error variance. The estimated pointwise standard error of $\hat f(x_0)$ is the square root of the quadratic form in that covariance. Bands drawn at twice that standard error are a pointwise summary under a normal error model; they are not a simultaneous band for the whole curve.{{cite:james_islr2013}} (pp. 267–268, §7.1, variance of the fitted polynomial)

Degrees above three or four are rarely useful for a single predictor. The column of a high power is nearly a linear combination of the lower powers on a short interval of $x$, and the curve between the observed points can oscillate. The individual coefficients then become hard to read, which is why the object of interest is $\hat f(x)$ across a grid of $x$ values rather than $\hat\beta_3$ or $\hat\beta_4$ alone.{{cite:james_islr2013}} (pp. 266–267, §7.1)

## Statistical use — A curve with ordinary least squares
Choose a small degree, fit the powers by least squares, and plot $\hat f(x)$ on the range of $x$ that was observed, with the pointwise standard-error curves if a normal-error reading is wanted. Compare the residual sum of squares with that of the straight line on the same points. A smaller sum is expected once extra coefficients are free; it becomes evidence of curvature only together with the plot and with a check that the extra bends are not confined to one or two edges.{{cite:james_islr2013}} (pp. 266–268, §7.1){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, least squares for a statistically linear mean)

## Worked example
Four points $(x,y)=(0,1)$, $(1,2)$, $(2,2)$, $(3,5)$ are fitted by $\beta_0+\beta_1 x+\beta_2 x^2$. The sums that enter the normal equations are $n=4$, $\sum x=6$, $\sum x^2=14$, $\sum x^3=36$, $\sum x^4=98$, $\sum y=10$, $\sum xy=21$ and $\sum x^2 y=55$. The unique solution is
\[
\hat\beta_0=1.2,\qquad \hat\beta_1=-0.3,\qquad \hat\beta_2=0.5.
\]
The fitted values are $1.2$, $1.4$, $2.6$ and $4.8$. The residuals are $-0.2$, $0.6$, $-0.6$ and $0.2$, and the residual sum of squares is $0.8$.

The straight line on the same points has intercept $0.7$ and slope $1.2$, and its residual sum of squares is $1.8$. The quadratic spends one extra coefficient and removes $1.0$ from that sum. The fitted curve falls slightly from $x=0$ to $x=1$ and then rises, which is what a negative linear coefficient and a positive square produce together.{{cite:james_islr2013}} (p. 266, §7.1, least squares on the powers){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, quadratic model)

**Your turn.** Fit $y=\beta_0+\beta_1 x+\beta_2 x^2$ to $(0,1)$, $(1,0)$ and $(2,1)$. Give the three coefficients and the residual sum of squares.

::: {.callout-tip collapse="true" title="Answer"}
The three points lie on $(x-1)^2=1-2x+x^2$, so the coefficients are $1$, $-2$ and $1$. Every residual is $0$, and the residual sum of squares is $0$.
:::

## Common misconceptions
Polynomial least squares is not nonlinear least squares. The mean is nonlinear as a function of $x$ and linear as a function of $\beta$. The test is whether the coefficients can be moved outside known functions of the data. If they can, the fit is the linear one, extra columns and all.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1){{cite:dodge2008}} (p. 354, a model nonlinear in a parameter contrasted with $Y=\beta_0+\beta_1 X$)

A large degree is not a closer look at the same curve. It is a more flexible function, and near the ends of the age range in the wage example the extra flexibility is exactly where a polynomial is least trustworthy. The coefficients of a degree-4 fit are also a poor summary: the fitted wage at a given age depends on all of them at once.{{cite:james_islr2013}} (pp. 266–267, §7.1)

The pointwise band at twice the standard error is not a statement that the whole curve lies inside the band with the same coverage. Each $x_0$ has its own interval, built from $\mathrm{Var}\,\hat f(x_0)$.{{cite:james_islr2013}} (pp. 267–268, §7.1)

## Assumptions and limits — Where a global polynomial misleads
The normal equations assume the degree was chosen and the powers are not perfectly collinear. On a very short span of $x$, high powers are nearly collinear and the coefficients become unstable even when $\hat f(x)$ in the middle is calm. A polynomial has no horizontal asymptote, so it is a poor description of a process that flattens for good, such as strength approaching a limit. Squared error still chases outliers. And a residual sum of squares that falls from $1.8$ to $0.8$ on four points does not, by itself, say that the quadratic is the population mean.{{cite:james_islr2013}} (p. 266, §7.1, strange shapes near the boundary){{cite:nist_nonlinear_ls2002}} (§4.1.4.2, linear models and asymptotes)

## Connections
The one-predictor case of [ordinary least squares](ordinary-least-squares.qmd) is the degree-1 polynomial. [Multiple linear regression](multiple-linear-regression.qmd) is the same algebra with columns that need not be powers of a single $x$. [Nonlinear regression](nonlinear-regression.qmd) is the neighbouring fit once a coefficient moves inside the function. [Overfitting](overfitting.qmd) is the name for a degree so high that the curve follows the sample rather than the mean one would see on new $x$ values.{{cite:james_islr2013}} (pp. 266–267, §7.1){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1)

## History
Extending a straight regression by adding powers of the predictor is an old device for a curved mean, and it remains the usual first step before splines and other local curves. The coefficients are estimated by the least-squares method developed in the late eighteenth and early nineteenth centuries by Gauss, Legendre, and possibly Adrain. What the polynomial changes is the list of predictors, not that criterion.{{cite:james_islr2013}} (p. 266, §7.1, the historical extension of the linear model){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Gauss, Legendre, and Adrain)
