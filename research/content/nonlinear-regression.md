## Lead context

A response sometimes bends, levels off, or decays in a way no straight line, and no polynomial in the predictors with fixed powers, can represent by coefficients that enter the mean only through sums and products. The curve is then nonlinear in the unknown coefficients, and the fit that minimises the sum of squared vertical gaps is nonlinear least squares. A mean is a nonlinear regression when it is not linear in the parameters. The same squared-error criterion is used as in a linear fit. What changes is that the minimiser is found by iteration.{{cite:dodge2008}} (p. 372, Nonlinear regression){{cite:nist_nonlinear_ls2002}} (§4.1.4.2, Definition of a nonlinear regression model)

## Motivating example

Concrete gains strength quickly at first and then approaches a ceiling as it cures. A straight line in time has no horizontal asymptote, so it keeps rising or falling at the extremes of the time axis. A mean such as \(\beta_0+\beta_1\exp(-\beta_2 t)\) can rise fast and then flatten, because the rate \(\beta_2\) sits inside the exponential. The three coefficients cannot be recovered by the closed-form slope formula for a straight line. They are chosen by searching for the values that make the squared gaps between measured strength and the curve as small as possible. The way the parameters are estimated is conceptually the same least-squares idea as in a linear model. The search is what the nonlinearity forces.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, Examples of nonlinear models)

## Definition

Observations \((x_i,y_i)\) are modelled as
\[
y_i=f(x_i;\beta)+\varepsilon_i,
\]
where \(f\) is a known function that is not linear in the coefficient vector \(\beta\). Nonlinear least squares chooses \(\hat\beta\) to minimise
\[
S(\beta)=\sum_i\bigl(y_i-f(x_i;\beta)\bigr)^2.
\]
The same criterion defines the procedure: a regression is called nonlinear when the mean is not linear in the coefficients, and the coefficients are estimated by least squares. Smoothness of \(f\) and a unique minimum make the search practical, but they are not required for the definition.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, Definition of a nonlinear regression model){{cite:dodge2008}} (pp. 372–373, Mathematical aspects)

Setting the derivatives of \(S\) to zero produces one equation for each coefficient,
\[
\sum_i\bigl(y_i-f(x_i;\beta)\bigr)\frac{\partial f(x_i;\beta)}{\partial\beta_j}=0.
\]
Those normal equations are themselves nonlinear when \(f\) is nonlinear in \(\beta\), so they need not have a solution, or they may have more than one. They are solved by iteration. Gauss–Newton linearises \(f\) in the coefficients at the current guess, by a Taylor expansion, and solves the resulting linear least-squares step. Levenberg–Marquardt mixes that step with a move that only shrinks \(S\).{{cite:dodge2008}} (p. 373, Mathematical aspects)

A function that is nonlinear in \(x\) can still be linear in \(\beta\). The mean \(\beta_0+\beta_1 x+\beta_2 x^2\) is a polynomial curve and is estimated by ordinary linear least squares, because each term is a coefficient times a known function of \(x\). In that statistical sense the model is linear in the parameters even though the graph is curved. The mean \(\beta_0\exp(-\beta_1 x)\) is not. A function that is not linear in the parameters can sometimes be rewritten, by a transformation of the response, as a function that is. When no such transformation exists, the fit stays in the nonlinear iteration.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Definition of a linear least squares model){{cite:dodge2008}} (p. 373, Domains and limitations)

## Properties

The fitted coefficients minimise squared vertical error for the function that was written down. They are not, in general, available from a matrix formula. A second start can finish at a different value of \(S\) when the surface has more than one dip. When a minimum has been reached, intervals for the coefficients and for the mean are available from the same linearisation used in the last step, and those intervals are approximate. The probabilistic reading of the interval is only approximately correct, and the approximation is still the interval that is used in practice.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, Advantages of nonlinear least squares)

Small samples can still identify a nonlinear mean when the curve is a good description of the process, because the criterion uses every observation. One or two wild responses can move the curve a long way, for the same reason they move a least-squares line: the criterion squares their gaps. Nonlinear fits have fewer routine diagnostics for that movement than linear fits do.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, Disadvantages of nonlinear least squares)

## Worked example

Three measurements follow a decay: \((x,y)=(0,4)\), \((1,2)\), \((2,1.2)\). The mean \(\beta_0\exp(-\beta_1 x)\) is nonlinear in \(\beta_1\). At the start \((\beta_0,\beta_1)=(4,0.7)\) the fitted values are \(4\), \(4e^{-0.7}\approx 1.9863\) and \(4e^{-1.4}\approx 0.9864\), and
\[
S(4,0.7)=(4-4)^2+(2-1.986341)^2+(1.2-0.986388)^2=0.045817.
\]
A numerical minimiser moves to \(\beta_0=3.9742\), \(\beta_1=0.6389\). The fitted values are \(3.9742\), \(2.097872\) and \(1.107409\), and
\[
S(3.9742,0.6389)=0.018818.
\]
Shifting only the rate back to \(0.7\), with the scale held at \(3.9742\), raises \(S\) to \(0.049755\). Shifting only the scale to \(4.2\), with the rate held at \(0.6389\), raises \(S\) to \(0.087998\). This pair is a local improvement on those two neighbours. It is the minimiser along the profile that, for each rate, chooses the best scale: the profiled minimum is at rate \(0.63892\) and scale \(3.97418\), and rounding to four decimals does not change \(S\) at the reported precision.

The straight line fitted to the same three points has mean \(x\) equal to \(1\), mean \(y\) equal to \(2.4\), \(\sum(x_i-\bar x)^2=2\) and \(\sum(x_i-\bar x)(y_i-\bar y)=-2.8\), so the slope is \(-2.8/2=-1.4\) and the intercept is \(2.4-(-1.4)(1)=3.8\). The fitted values are \(3.8\), \(2.4\) and \(1.0\), and the residual sum of squares is \(0.24\). The exponential uses the same squared-error criterion and cuts that sum from \(0.24\) to \(0.018818\), because the drops from \(4\) to \(2\) to \(1.2\) slow down rather than stay constant.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, least squares for a nonlinear mean){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, the straight line as the statistically linear case)

**Your turn.** The curve \(y=\beta_0 e^{-\beta_1 x}\) is required to pass through \((0,5)\) and \((1,1)\). Find \(\beta_0\), \(\beta_1\), and the residual sum of squares.

::: {.callout-tip collapse="true" title="Answer"}
The point at \(x=0\) forces \(\beta_0=5\). Then \(5e^{-\beta_1}=1\), so \(\beta_1=\ln 5\approx 1.6094\). Both residuals are zero, and the residual sum of squares is \(0\).
:::

## Assumptions and limits

The procedure assumes that the function \(f\) was chosen before looking at the size of \(S\), that the gaps are the right scale on which to measure miss, and that a start near the minimiser is available. A bad start can stop at a local minimum, or the iteration can fail to move. Outliers pull the fit because they are squared. Approximate intervals inherit the usual least-squares story of comparable, weakly dependent errors, and they remain approximations even then. A process that truly levels off is a reason to leave the straight line. The formula still returns a number outside the times that were measured, and that number is an extrapolation of the fitted function, not a new observation.{{cite:nist_nonlinear_ls2002}} (§4.1.4.2, starting values, outliers, and approximate intervals){{cite:dodge2008}} (p. 373, Domains and limitations)

Taking logarithms and then using ordinary least squares minimises squared error on the log scale. The minimiser of \(S\) on the original scale is the nonlinear least-squares fit. The two answers agree only when the logged model happens to match the criterion that was declared. A curve on the scatterplot is not, by itself, a nonlinear regression. Polynomial least squares draws a curve and still uses the linear normal equations.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, linear in the parameters){{cite:dodge2008}} (p. 372, Nonlinear regression)

## History

The early published uses of a regression mean that is nonlinear in its coefficients date from the 1920s, including work by Fisher and Mackenzie on the manurial response of potato varieties. Routine fitting waited on automatic calculation in the 1970s, because each fit is an iterative minimisation of \(S\) rather than one pass through the normal equations. The steps in common use linearise the mean at the current coefficients, in the manner of Gauss–Newton, or combine that linearisation with a damper, as in Levenberg–Marquardt. The least-squares criterion itself is older: Gauss, Legendre, and possibly Adrain developed it around the turn of the nineteenth century for problems that were linear in the parameters. Nonlinear regression is that criterion applied where the parameters sit inside the function.{{cite:dodge2008}} (pp. 372–373, History and Mathematical aspects){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Why least squares)
