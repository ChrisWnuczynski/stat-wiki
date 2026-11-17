

## Lead context

A response sometimes bends, levels off, or decays in a way no straight line, and no polynomial in the predictors with fixed powers, can represent by coefficients that enter the mean only through sums and products. The curve is then nonlinear in the unknown coefficients, and the fit that minimises the sum of squared vertical gaps is nonlinear least squares.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, definition of a nonlinear regression model){{cite:dodge2008}} (p. 372, not linear in the parameters)

## Motivating example

Concrete gains strength quickly at first and then approaches a ceiling as it cures. A straight line in time has no horizontal asymptote, so it keeps rising or falling at the extremes of the time axis. A mean such as $\beta_0+\beta_1\exp(-\beta_2 t)$ can rise fast and then flatten, because the rate $\beta_2$ sits inside the exponential. The three coefficients cannot be recovered by the closed-form slope formula for a straight line. They are chosen by searching for the values that make the squared gaps between measured strength and the curve as small as possible.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, concrete strength and iterative fitting)

## Definition

Observations $(x_i,y_i)$ are modelled as
\[
y_i=f(x_i;\beta)+\varepsilon_i,
\]
where $f$ is a known function that is not linear in the coefficient vector $\beta$. Nonlinear least squares chooses $\hat\beta$ to minimise
\[
S(\beta)=\sum_i\bigl(y_i-f(x_i;\beta)\bigr)^2.
\]
The same criterion defines the procedure: a regression is called nonlinear when the mean is not linear in the coefficients, and the coefficients are estimated by least squares. Smoothness of $f$ and a unique minimum make the search practical, but they are not required for the definition.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, definition and the two practical criteria){{cite:dodge2008}} (pp. 372–373, model and the sum of squared errors)

Setting the derivatives of $S$ to zero produces one equation for each coefficient,
\[
\sum_i\bigl(y_i-f(x_i;\beta)\bigr)\frac{\partial f(x_i;\beta)}{\partial\beta_j}=0.
\]
Those equations are themselves nonlinear when $f$ is nonlinear in $\beta$, so they are solved by iteration. Gauss–Newton linearises $f$ in the coefficients at the current guess and solves the resulting linear least-squares step; Levenberg–Marquardt mixes that step with a move that only shrinks $S$.{{cite:dodge2008}} (pp. 373–374, normal equations, Gauss–Newton, and Levenberg–Marquardt)

A function that is nonlinear in $x$ can still be linear in $\beta$. The mean $\beta_0+\beta_1 x+\beta_2 x^2$ is a polynomial curve and is estimated by ordinary linear least squares. The mean $\beta_0\exp(-\beta_1 x)$ is not.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, a quadratic in $x$ is linear in the parameters){{cite:dodge2008}} (p. 372, linearity judged in the parameters)

Squaring the gaps still means what it means for a line: large misses cost more than small ones, and positive and negative misses do not cancel. What changes is the shape of that sum as a function of the coefficients. For a mean that is linear in the coefficients the sum of squares is a bowl with one bottom, and calculus gives the bottom in closed form. For a mean such as $\beta_0\exp(-\beta_1 x)$ the sum of squares can bend, and the bottom is found by starting at a guess and stepping downhill. A guess that is far from the data can stop in a shallow local dip, or fail to move at all.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, starting values and local minima){{cite:dodge2008}} (p. 373, iterative minimisation of $S$)

Write the mean as a function suggested by the mechanism, with coefficients in the positions the mechanism requires, and minimise $S$. Report the minimised $S$ together with the start that was used, and compare it with the $S$ of a straight line on the same points so the gain from the curve is visible. Treat a confidence interval from the final linearisation as an approximation, and do not extend the curve past the observed $x$ values merely because the formula still returns a number.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, approximate intervals and the range of functions){{cite:dodge2008}} (p. 373, minimising $S$)

A curve on the scatterplot is not, by itself, a nonlinear regression. Polynomial least squares draws a curve and still uses the linear normal equations, because each power of $x$ is just another column and the coefficients stand in front of those columns. Nonlinear regression begins when a coefficient appears inside a function that cannot be rewritten as such a column.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, linear in the parameters){{cite:dodge2008}} (p. 372)

Taking logarithms and then using ordinary least squares is a different fit. It minimises squared error on the log scale. The minimiser of $S$ on the original scale is the nonlinear least-squares fit, and the two answers agree only when the logged model happens to be exact.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, least squares on the stated function)

Convergence of the iteration is not evidence that the curve is the right mechanism. A smooth wrong function can still possess a unique minimum of $S$.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, a unique solution is a practical convenience)

[Ordinary least squares](ordinary-least-squares.qmd) and the [least-squares line](least-squares-line.qmd) are the same criterion in the special case where $f$ is linear in the coefficients. [Polynomial least squares](polynomial-least-squares.qmd) stays in that special case while allowing a curved mean. A [generalised linear model](generalised-linear-model.qmd) also leaves the straight line, but it does so by choosing a distribution and a link, and the coefficients of the linear predictor are estimated from a likelihood rather than from $S$ alone. [Poisson regression](poisson-regression.qmd) is one such model.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, extension of linear least squares){{cite:dodge2008}} (p. 373, comparison with multiple linear regression)

## Properties

The fitted coefficients minimise squared vertical error for the function that was written down. They are not, in general, available from a matrix formula, and a second start can finish at a different value of $S$ when the surface has more than one dip. When a minimum has been reached, intervals for the coefficients and for the mean are available from the same linearisation used in the last step, and those intervals are approximate.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, approximate confidence, prediction, and calibration intervals)

Small samples can still identify a nonlinear mean when the curve is a good description of the process, because the criterion uses every observation. One or two wild responses can move the curve a long way, for the same reason they move a least-squares line: the criterion squares their gaps, and nonlinear fits have fewer routine diagnostics for that movement than linear fits do.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, small samples and sensitivity to outliers)

## Worked example

Three measurements follow a decay: $(x,y)=(0,4)$, $(1,2)$, $(2,1.2)$. The mean $\beta_0\exp(-\beta_1 x)$ is nonlinear in $\beta_1$. At the start $(\beta_0,\beta_1)=(4,0.7)$ the fitted values are $4$, $4e^{-0.7}\approx 1.9863$ and $4e^{-1.4}\approx 0.9864$, and
\[
S(4,0.7)\approx 0+0.0137^2+0.2136^2\approx 0.0458.
\]
A numerical minimiser moves to $\beta_0=3.9742$, $\beta_1=0.6389$, with fitted values about $3.9742$, $2.0979$ and $1.1074$, and $S\approx 0.0188$. Shifting only the rate back to $0.7$ raises $S$ to about $0.0498$, and shifting only the scale to $4.2$ raises $S$ to about $0.0880$, so this pair is a local improvement on those neighbours.

The straight line fitted to the same three points has intercept $3.8$ and slope $-1.4$, fitted values $3.8$, $2.4$ and $1.0$, and residual sum of squares $0.24$. The exponential uses the same squared-error criterion and cuts that sum by a factor of about thirteen, because the drops from $4$ to $2$ to $1.2$ slow down rather than stay constant.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, least squares for a nonlinear mean){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, the straight line as the statistically linear case)

**Your turn.** The curve $y=\beta_0 e^{-\beta_1 x}$ is required to pass through $(0,5)$ and $(1,1)$. Find $\beta_0$, $\beta_1$, and the residual sum of squares.

::: {.callout-tip collapse="true" title="Answer"}
The point at $x=0$ forces $\beta_0=5$. Then $5e^{-\beta_1}=1$, so $\beta_1=\ln 5\approx 1.6094$. Both residuals are zero, and the residual sum of squares is $0$.
:::

## Assumptions and limits

The procedure assumes that the function $f$ was chosen before looking at the size of $S$, that the gaps are the right scale on which to measure miss, and that a start near the minimiser is available. A bad start can stop at a local minimum. Outliers pull the fit because they are squared. Approximate intervals inherit the usual least-squares story of comparable, weakly dependent errors, and they remain approximations even then. A process that truly levels off is a reason to leave the straight line; it is not a reason to trust an exponential outside the times that were measured.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, starting values, outliers, and approximate intervals){{cite:dodge2008}} (p. 374, a distance function that cannot be linearised by a transform)

## History

The early published uses of a regression mean that is nonlinear in its coefficients date from the 1920s, including work by Fisher and Mackenzie. Routine fitting waited on automatic calculation in the 1970s, because each fit is an iterative minimisation of $S$ rather than one pass through the normal equations. The steps in common use linearise the mean at the current coefficients, in the manner of Gauss–Newton, or combine that linearisation with a ridge-like damper, as in Levenberg–Marquardt.{{cite:dodge2008}} (pp. 372–374, history and the iterative methods)
