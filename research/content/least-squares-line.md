## Lead context
The least-squares line is the straight line whose vertical squared gaps, added over the observed points, are as small as that sum can be.{{cite:nist_ls_straight2002}} (§4.4.3.1, straight-line criterion){{cite:dodge2008}} (p. 304, sum of squared residuals)

## Motivating example
The points $(0,1)$, $(1,1)$ and $(2,4)$ are not collinear: a line through any two of them misses the third. Applying [least squares](least-squares.qmd) balances all three vertical discrepancies after squaring and forces the fitted line through the centroid $(1,2)$, which determines the intercept once the slope is fixed.{{cite:nist_ls_straight2002}} (§4.4.3.1, the line passes through the mean when the intercept formula is used){{cite:dodge2008}} (p. 305, first normal equation)

## Intuition
Squaring prevents a positive vertical gap above the line from cancelling a negative gap below it, and weights a large miss more heavily than a fractional miss. Over all candidate pairs $(b_0,b_1)$, the sum of squared vertical gaps forms a convex quadratic bowl whose unique minimum is the least-squares line. Fixing $b_0=0$ restricts minimization to a one-parameter slice of that bowl and generally produces a different line.{{cite:dodge2008}} (p. 305, partial derivatives set to zero){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, least squares)

## Definition
For pairs $(x_i,y_i)$ with the $x_i$ not all equal, the least-squares line $y=b_0+b_1 x$ minimises $\sum_i(y_i-b_0-b_1 x_i)^2$. Its [regression slope](regression-slope.qmd) and intercept are

$$
b_1=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}{\sum_i(x_i-\bar x)^2},\qquad b_0=\bar y-b_1\bar x,
$$

which solve the normal equations $\sum_i(y_i-b_0-b_1 x_i)=0$ and $\sum_i x_i(y_i-b_0-b_1 x_i)=0$.{{cite:nist_ls_straight2002}} (§4.4.3.1){{cite:dodge2008}} (p. 305, normal equations)

## Interpretation
The slope $b_1$ is the change in fitted height per unit increase in $x$ across the observed $x$ range, and $b_0$ is the fitted height at $x=0$. When the sample contains no $x$ near zero, $b_0$ extrapolates outside the data. For the three points $(0,1)$, $(1,1)$ and $(2,4)$, the least-squares line is $y=0.5+1.5x$, giving fitted height $0.5$ against observed height $1$ at $x=0$; the residual $0.5$ reflects the global trade-off across all three points rather than an arithmetic defect.{{cite:nist_ls_straight2002}} (§4.4.3.1, intercept depends on the slope){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, extrapolation)

## Properties
With a free intercept, the fitted line passes through $(\bar x,\bar y)$ and its residuals sum to zero. Requiring the line to pass through the origin instead minimises $\sum_i(y_i-b x_i)^2$ at $b=\sum_i x_i y_i/\sum_i x_i^2$, where the residuals need not sum to zero. On $(0,1)$, $(1,1)$ and $(2,4)$, the origin-constrained slope is $9/5=1.8$ with residual sum of squares $1.8$, exceeding the $1.5$ achieved when the intercept is free.{{cite:dodge2008}} (p. 305, the intercept equation){{cite:nist_ls_straight2002}} (§4.4.3.1)

When a linear mean model holds at fixed $x_i$, [least-squares estimators are unbiased](least-squares-estimators-are-unbiased.qmd) for the population intercept and slope, and uncorrelated equal-variance errors give $\operatorname{Var}(b_1)=\sigma^2/S_{xx}$. Neither property requires Gaussian errors; Gaussian errors enter through the [sampling distribution of the regression estimators](sampling-distribution-of-the-regression-estimators.qmd) to justify exact Student-$t$ inference.{{cite:nist_ls_straight2002}} (§4.4.3.1, residual scale $\sqrt{Q/(n-p)}$)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Setting the partial derivatives of $Q(b_0,b_1)=\sum_i(y_i-b_0-b_1 x_i)^2$ to zero yields the two normal equations. The intercept equation sets the residual sum to zero, giving $b_0=\bar y-b_1\bar x$ so that the line passes through $(\bar x,\bar y)$, and substituting $b_0$ into the slope equation gives $b_1=S_{xy}/S_{xx}$. Fixing $b_0=0$ before differentiating leaves $\sum_i x_i(y_i-b x_i)=0$, hence $b=\sum_i x_i y_i/\sum_i x_i^2$ when $\sum_i x_i^2>0$.{{cite:dodge2008}} (p. 305){{cite:nist_ls_straight2002}} (§4.4.3.1)

For $(0,1)$, $(1,1)$ and $(2,4)$, $\bar x=1$, $\bar y=2$, $S_{xx}=2$ and $S_{xy}=3$, so $b_1=3/2$ and $b_0=1/2$, with fitted values $(0.5,2,3.5)$, residuals $(0.5,-1,0.5)$, and residual sum of squares $1.5$. Under $b_0=0$, $b=(0\cdot 1+1\cdot 1+2\cdot 4)/(0+1+4)=9/5=1.8$ with residual sum of squares $1^2+(1-1.8)^2+(4-3.6)^2=1.8$.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, the criterion)
:::
:::

## Statistical use — Say which gaps were squared
State explicitly that the fitted line minimises vertical squared discrepancies in $y$. When physical or scientific theory fixes the intercept at zero, report that restriction and use $\sum_i x_i y_i/\sum_i x_i^2$ rather than quoting the free-intercept slope as though the origin constraint had been imposed. Evaluating $b_0+b_1 x$ outside the observed $x$ range extrapolates a line that was only fitted inside the sample.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, extrapolation){{cite:dodge2008}} (p. 304)

If every $x_i$ coincides, $S_{xx}=0$ and the slope is unidentified: every line through $(x_1,\bar y)$ achieves the same vertical gaps. Because discrepancies are squared, a single extreme $y_i$ can tilt the fitted line sharply, and a small residual sum of squares on three points does not rule out curvature elsewhere.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, outliers and long ranges){{cite:nist_ls_straight2002}} (§4.4.3.1, the denominator)

## Worked example
The points $(0,1)$, $(1,1)$, $(2,4)$ have $\bar x=1$, $\bar y=2$, $S_{xx}=2$ and $S_{xy}=3$. The least-squares line is $y=0.5+1.5x$. Fitted heights are $0.5$, $2$ and $3.5$. Residuals are $0.5$, $-1$ and $0.5$, and $Q=1.5$. With $n-2=1$, the residual standard deviation is $\sqrt{1.5}\approx 1.2247$. The origin-constrained slope is $1.8$, with $Q=1.8$. The free line fits better on its own criterion, and it does so by using an intercept the constrained line is not allowed.{{cite:nist_ls_straight2002}} (§4.4.3.1, $n-p$ with $p=2$)

**Your turn.** For the same three $x$ values and responses $(0,0,3)$, find the free-intercept slope.

::: {.callout-tip collapse="true" title="Answer"}
The response mean is $1$. Then $S_{xy}=(-1)(-1)+(0)(-1)+(1)(2)=3$, so the slope is $3/2=1.5$ again, and the intercept is $1-1.5\cdot 1=-0.5$. The line is $y=-0.5+1.5x$.
:::

## Common misconceptions
The least-squares line minimises neither absolute vertical discrepancies nor horizontal discrepancies; predicting $x$ from $y$ interchanges the axes and generally yields a distinct line.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, vertical least squares)

Passing through $(\bar x,\bar y)$ does not imply passing through $(0,0)$: on $(0,1)$, $(1,1)$ and $(2,4)$ the fitted height is $2$ at $x=1$ and $0.5$ at $x=0$.{{cite:dodge2008}} (p. 305)

The origin-constrained residual sum of squares $1.8$ is the minimum over lines through $(0,0)$; the unconstrained minimum $1.5$ is smaller because enlarging the candidate family cannot increase the minimum.{{cite:nist_ls_straight2002}} (§4.4.3.1)

## Connections
[Least squares](least-squares.qmd) states the general criterion, [regression slope](regression-slope.qmd) isolates the centred-product ratio $b_1$, and [simple linear regression](simple-linear-regression.qmd) embeds this line in a probabilistic response model. When a second predictor nearly duplicates $x$, [multicollinearity](multicollinearity.qmd) shrinks the two-predictor analogue of $S_{xx}$ and inflates slope variances.{{cite:dodge2008}} (p. 304){{cite:nist_ls_straight2002}} (§4.4.3.1)

## History
Legendre published the least-squares criterion in 1805, while historical accounts trace independent late-eighteenth- and early-nineteenth-century development to Gauss, Legendre, and possibly Adrain. Setting the partial derivatives of the straight-line sum of squares to zero yields the two normal equations still used to compute $b_0$ and $b_1$.{{cite:dodge2008}} (pp. 304–305){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1){{cite:nist_ls_straight2002}} (§4.4.3.1)
