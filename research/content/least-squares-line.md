## Lead context
The least-squares line is the straight line whose vertical squared gaps, added over the observed points, are as small as that sum can be.{{cite:nist_ls_straight2002}} (§4.4.3.1, straight-line criterion){{cite:dodge2008}} (p. 304, sum of squared residuals)

## Motivating example
The points $(0,1)$, $(1,1)$ and $(2,4)$ are not collinear. A freehand line can pass through two of them and miss the third by a wide margin. The least-squares choice balances all three vertical gaps after squaring, and it is required to pass through the average point $(1,2)$. That requirement decides the intercept once the slope is known.{{cite:nist_ls_straight2002}} (§4.4.3.1, the line passes through the mean when the intercept formula is used){{cite:dodge2008}} (p. 305, first normal equation)

## Intuition
Squaring stops a point above the line from cancelling a point below it, and it charges the point at height $4$ more than a point that misses by a fraction. Among straight lines, the sum of those squares is a bowl in the intercept and the slope. The bottom of the bowl is the least-squares line. A line forced through the origin is the bottom of a different bowl, with the intercept fixed at zero, and it is not the same line.{{cite:dodge2008}} (p. 305, partial derivatives set to zero){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, least squares)

## Definition
For points $(x_i,y_i)$ with the $x_i$ not all equal, the least-squares line $y=b_0+b_1 x$ minimises $\sum_i(y_i-b_0-b_1 x_i)^2$. The slope and intercept are

$$
b_1=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}{\sum_i(x_i-\bar x)^2},\qquad b_0=\bar y-b_1\bar x.
$$


The normal equations are $\sum_i(y_i-b_0-b_1 x_i)=0$ and $\sum_i x_i(y_i-b_0-b_1 x_i)=0$.{{cite:nist_ls_straight2002}} (§4.4.3.1){{cite:dodge2008}} (p. 305, normal equations)

## Interpretation
The slope is the change in fitted height per unit change in $x$, inside the range of the observed $x$ values. The intercept is the fitted height at $x=0$. If the data do not contain an $x$ near zero, that height is an extrapolation. The line of the points above is $y=0.5+1.5x$, so the fitted height at $x=0$ is $0.5$, and the observed point there is $1$. The residual $0.5$ is part of the fit, not a failure of the formula.{{cite:nist_ls_straight2002}} (§4.4.3.1, intercept depends on the slope){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, extrapolation)

## Properties
The fitted line passes through $(\bar x,\bar y)$. The residuals sum to zero. If a line is required to pass through the origin, the slope that minimises $\sum_i(y_i-b x_i)^2$ is $\sum_i x_i y_i/\sum_i x_i^2$, and the residuals need not sum to zero. For the three points that origin slope is $9/5=1.8$, and the residual sum of squares is $1.8$, larger than the $1.5$ achieved by the line with a free intercept. Forcing the intercept is a different problem.{{cite:dodge2008}} (p. 305, the intercept equation){{cite:nist_ls_straight2002}} (§4.4.3.1)

Under a straight mean and fixed $x_i$, the slope and intercept are unbiased for the mean line. With uncorrelated equal-variance errors the slope has variance $\sigma^2/S_{xx}$. Neither claim needs normal errors. Normality is what supplies a $t$ reference law for the slope.{{cite:nist_ls_straight2002}} (§4.4.3.1, residual scale $\sqrt{Q/(n-p)}$)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Set the derivatives of $Q(b_0,b_1)=\sum_i(y_i-b_0-b_1 x_i)^2$ to zero. The intercept equation says the residuals sum to zero, so $b_0=\bar y-b_1\bar x$ and the line passes through the sample mean. Substitution produces the slope formula. For the origin-constrained line, set $b_0=0$ before differentiating. The single equation $\sum_i x_i(y_i-b x_i)=0$ gives $b=\sum_i x_i y_i/\sum_i x_i^2$.{{cite:dodge2008}} (p. 305){{cite:nist_ls_straight2002}} (§4.4.3.1)

For the three points, $\bar x=1$, $\bar y=2$, $S_{xx}=2$ and $S_{xy}=3$, so $b_1=3/2$ and $b_0=1/2$. The fitted values are $0.5$, $2$ and $3.5$, the residuals are $0.5$, $-1$ and $0.5$, and the residual sum of squares is $1.5$. The origin slope is $(0\cdot 1+1\cdot 1+2\cdot 4)/(0+1+4)=9/5$. Its residual sum of squares is $1^2+(1-1.8)^2+(4-3.6)^2=1.8$.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, the criterion)
:::
:::

## Statistical use — Say which gaps were squared
Report the line as a fit to vertical squared gaps. If the scientific line must go through the origin, say so and use $\sum x_i y_i/\sum x_i^2$; do not quote the free-intercept slope as if the constraint had been imposed. A prediction beyond the largest $x$ is an extrapolation of a line that was only scored inside the sample.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, extrapolation){{cite:dodge2008}} (p. 304)

If every $x_i$ is equal, $S_{xx}=0$ and the slope formula divides by zero. Many horizontal lines share the same vertical gaps, and the criterion does not choose among their intercepts once the height is fixed at $\bar y$; the slope is simply unidentified. One wild $y$ moves the line sharply because the gap is squared. And a curve scored only by a line can have a small residual sum of squares on three points and still be the wrong shape on a fourth $x$.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, outliers and long ranges){{cite:nist_ls_straight2002}} (§4.4.3.1, the denominator)

## Worked example
The points $(0,1)$, $(1,1)$, $(2,4)$ have $\bar x=1$, $\bar y=2$, $S_{xx}=2$ and $S_{xy}=3$. The least-squares line is $y=0.5+1.5x$. Fitted heights are $0.5$, $2$ and $3.5$. Residuals are $0.5$, $-1$ and $0.5$, and $Q=1.5$. With $n-2=1$, the residual standard deviation is $\sqrt{1.5}\approx 1.2247$. The origin-constrained slope is $1.8$, with $Q=1.8$. The free line fits better on its own criterion, and it does so by using an intercept the constrained line is not allowed.{{cite:nist_ls_straight2002}} (§4.4.3.1, $n-p$ with $p=2$)

**Your turn.** For the same three $x$ values and responses $(0,0,3)$, find the free-intercept slope.

::: {.callout-tip collapse="true" title="Answer"}
The response mean is $1$. Then $S_{xy}=(-1)(-1)+(0)(-1)+(1)(2)=3$, so the slope is $3/2=1.5$ again, and the intercept is $1-1.5\cdot 1=-0.5$. The line is $y=-0.5+1.5x$.
:::

## Common misconceptions
The line does not minimise absolute vertical gaps, and it does not minimise horizontal gaps. Predicting $x$ from $y$ swaps the axes and produces another line.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, vertical least squares)

Passing through $(\bar x,\bar y)$ is not the same as passing through the origin. The worked line has fitted height $2$ at $x=1$ and fitted height $0.5$ at $x=0$.{{cite:dodge2008}} (p. 305)

The residual sum of squares of the origin line, $1.8$, is not a worse value of the free-intercept criterion in a comparison that ignores the constraint. It is the minimum of a smaller family. The free line's $1.5$ is smaller because the family is larger.{{cite:nist_ls_straight2002}} (§4.4.3.1)

## Connections
[Simple linear regression](simple-linear-regression.qmd) is this line together with a sampling model for the responses. [Multicollinearity](multicollinearity.qmd) appears when a second predictor nearly copies $x$ and the analogue of $S_{xx}$ shrinks. The origin-constrained slope is least squares with one parameter removed, not a different loss.{{cite:dodge2008}} (p. 304){{cite:nist_ls_straight2002}} (§4.4.3.1)

## Check yourself

1. For $(0,1)$, $(1,1)$, $(2,4)$, what is the fitted height at $x=1$?

::: {.callout-tip collapse="true" title="Answer"}
$2$, the mean of $y$. The arithmetic is $0.5+1.5\cdot 1=2$.
:::

2. What is the origin-constrained slope for these three points?

::: {.callout-tip collapse="true" title="Answer"}
$9/5=1.8$. The products $x_i y_i$ sum to $9$ and the squares $x_i^2$ sum to $5$.
:::

3. Why is the origin line's residual sum of squares $1.8$ rather than $1.5$?

::: {.callout-tip collapse="true" title="Answer"}
The origin line is not allowed an intercept. The free line reaches $1.5$ by using intercept $0.5$. Inside the origin-only family, $1.8$ is the minimum.
:::

## History
Least squares minimises the sum of squared residuals, and Legendre introduced the method in 1805. Gauss, Legendre and possibly Adrain developed it independently in the late eighteenth and early nineteenth centuries. The straight-line estimators come from setting the two partial derivatives to zero, and the normal equations are that same critical-point system.{{cite:dodge2008}} (pp. 304–305){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1){{cite:nist_ls_straight2002}} (§4.4.3.1)
