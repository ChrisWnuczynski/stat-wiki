## Lead context

Squared residuals punish a wild point by the square of its distance, so one distant observation can swing a fitted line. Least absolute deviations fit the same linear summary by minimising the sum of absolute residuals instead. For a single location parameter the minimiser is a median. For a line, the fit is a median regression: it tracks the conditional median of the response rather than the conditional mean.{{cite:hansen2010}} (Ch. 7, §7.5, pp. 110–111){{cite:dodge2008}} (pp. 299–300)

## Motivating example

Three points sit at $x=0,1,2$ with responses $0,0,3$. The horizontal line $y=0$ misses the third point by 3, so the sum of absolute residuals is 3. The line $y=1.5x$ passes through $(0,0)$ and $(2,3)$ and misses $(1,0)$ by 1.5, so the sum is 1.5. The line through $(1,0)$ and $(2,3)$ misses the origin by 3. Among lines that pass through two of the points, $y=1.5x$ has the smallest absolute-residual sum. That comparison is the whole of the simple algorithm: the fitted line passes through at least two observations, and the pair is the one that makes the sum smallest.{{cite:dodge2008}} (pp. 299–300)

## Intuition

The median of a continuous random variable is a centre in the absolute-deviation sense: it minimises $\mathbb E|Y-\theta|$. The sign of $Y-\theta$ then has expectation zero at that centre, which is a moment condition rather than a squared-error condition. Replacing the unconditional median by a linear function of covariates gives the same geometry in regression. Each residual contributes its sign, times the covariate vector, to an estimating equation. A large residual still counts, but only through its sign, not through a squared distance that grows without bound.{{cite:hansen2010}} (Ch. 7, §7.5, pp. 110–111)

## Definition

For observations $(x_i,y_i)$, the least absolute deviations estimator $\hat\beta$ minimises the average absolute residual

$$
\mathrm{LAD}_n(\beta)=\frac1n\sum_{i=1}^n\bigl|y_i-x_i^\top\beta\bigr|.
$$

Equivalently, it solves the moment condition

$$
\frac1n\sum_{i=1}^n x_i\,\mathrm{sgn}(y_i-x_i^\top\hat\beta)=0,
$$

where $\mathrm{sgn}(u)$ is $+1$ for $u\ge 0$ and $-1$ for $u<0$. In the linear median model $y_i=x_i^\top\beta+e_i$ with $\mathrm{med}(e_i\mid x_i)=0$, the linear function is the conditional median of $y$ given $x$. There is no closed-form expression of the least-squares type. The fit is defined as the minimiser.{{cite:hansen2010}} (Ch. 7, §7.5, pp. 110–111){{cite:dodge2008}} (p. 299)

For simple regression, a direct algorithm uses a geometric fact: a minimising line passes through at least two data points. One searches over pairs, or iteratively replaces the second point, and keeps the pair whose line has the smallest sum of absolute residuals. The slope through $(x_1,y_1)$ and $(x_k,y_k)$ is $(y_k-y_1)/(x_k-x_1)$, and the intercept is fixed by passage through the first point.{{cite:dodge2008}} (pp. 299–300)

## Properties

When the conditional median is linear, $\sqrt n\,(\hat\beta-\beta)$ is asymptotically normal. The asymptotic variance depends on the conditional density of the error at zero, the median of the error. A taller density at the median means more observations near the centre and a more precise fit. If the error is independent of $x$ with density $f$ at zero, the asymptotic variance simplifies to $(E\,xx^\top)^{-1}/(4f(0)^2)$. Estimating $f(0)$ is the awkward step in a standard error; kernel estimates of that height are one route.{{cite:hansen2010}} (Ch. 7, §7.5, pp. 111–112)

The criterion is not differentiable at a zero residual, so the usual derivative argument for least squares does not apply at the solution. The sign equation is the subgradient condition instead. Non-uniqueness is possible: two different lines can share the same minimal sum. Degeneracy, in the geometric account, means a minimising line passes through more than two observations.{{cite:hansen2010}} (Ch. 7, §7.5, p. 111){{cite:dodge2008}} (p. 300)

For a single location, with $x_i=1$, the three descriptions “sample median,” “minimiser of $\sum|y_i-\theta|$,” and “solution of $\sum\mathrm{sgn}(y_i-\theta)=0$” agree. The regression estimator is the conditional version of that agreement.{{cite:hansen2010}} (Ch. 7, §7.5, p. 110)

## Statistical use

Use least absolute deviations when the target is a conditional median, or when a conditional-mean fit is too easily pulled by heavy-tailed residuals. Report the fitted coefficients as a median regression, not as a mean regression that happened to be computed differently. Standard errors from the asymptotic variance need an estimate of the error density at the median, and they are large-sample statements. With a handful of points the pair-search algorithm gives the fit exactly, up to ties among pairs, and an asymptotic standard error is not the right summary.{{cite:hansen2010}} (Ch. 7, §7.5, pp. 110–112){{cite:dodge2008}} (p. 299)

[Ordinary least squares](ordinary-least-squares.qmd) remains the estimator for a conditional mean and is the easier calculation when that is the target and the errors are not extreme. The two fits answer different questions. A line that minimises squared residuals and a line that minimises absolute residuals are not two attempts at one number.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1){{cite:hansen2010}} (Ch. 7, §7.5, p. 110)

## Worked example

For the three points $(0,0)$, $(1,0)$, and $(2,3)$, the line through the first and third has slope $3/2$ and equation $y=1.5x$. Absolute residuals are $0$, $1.5$, and $0$, summing to $1.5$. The line $y=0$ has absolute residuals $0$, $0$, and $3$, summing to $3$. The line through $(1,0)$ and $(2,3)$ is $y=-3+3x$, with absolute residuals $3$, $0$, and $0$, summing to $3$. The least absolute deviations fit among these pair-lines is $y=1.5x$, with criterion value $1.5$. The mean of the three responses is $1$, and the horizontal line at that mean has absolute residual sum $|0-1|+|0-1|+|3-1|=4$, larger still.{{cite:dodge2008}} (pp. 299–300){{cite:hansen2010}} (Ch. 7, §7.5, p. 110)

**Your turn.** For the points $(0,1)$, $(1,1)$, and $(2,5)$, compute the sum of absolute residuals for the line through the first and second points and for the line through the first and third. Which sum is smaller?

::: {.callout-tip collapse="true" title="Answer"}
The line through $(0,1)$ and $(1,1)$ is $y=1$. The absolute residuals are $0$, $0$, and $4$, so the sum is $4$. The line through $(0,1)$ and $(2,5)$ is $y=1+2x$. The absolute residuals are $0$, $|1-3|=2$, and $0$, so the sum is $2$. The second sum is smaller.
:::

## Common misconceptions

Least absolute deviations is not a robust version of a mean regression that estimates the same coefficient. Under a linear median model it estimates the conditional median. It is not computed by a formula of the $(X^\top X)^{-1}X^\top y$ type. A single outlier does not have to leave the fit unchanged: a point still contributes its sign, and a change of sign changes the estimating equation. The fit is also not always unique.{{cite:hansen2010}} (Ch. 7, §7.5, pp. 110–111){{cite:dodge2008}} (pp. 299–300)

## Assumptions and limits

The asymptotic normal limit quoted above assumes a linear conditional median, and the simplified variance assumes that the error density at the median does not depend on $x$. The geometric claim that a solution passes through two observations is for simple regression with a continuous response. If the scientific target is a conditional mean, absolute deviations estimate something else. Small samples should be summarised by the minimal sum itself, not by an asymptotic standard error that needs a density estimate.{{cite:hansen2010}} (Ch. 7, §7.5, pp. 111–112){{cite:dodge2008}} (p. 300)

## Connections

[Ordinary least squares](ordinary-least-squares.qmd) minimises squared residuals and targets a conditional mean. An [estimating equation](estimating-equations.qmd) is the general device of solving a sample moment; the sign equation above is one. The median of a single sample is the location special case of the same absolute-deviation criterion.

## History

Boscovich, in 1757, fitted a line by absolute deviations while reconciling inconsistent measurements of the shape of the Earth, with side conditions on the signs of the residuals. Laplace took the idea up later in the eighteenth century. Least squares, associated with Legendre and Gauss, then dominated, partly because the squared criterion has easy calculus and a closed linear solution. Interest returned in the late twentieth century, when computation made the minimisation routine and asymptotic theory for the estimator was developed. The median characterisation — the centre that minimises expected absolute deviation — is the one-parameter ancestor of that regression criterion.{{cite:dodge2008}} (pp. 299–300){{cite:hansen2010}} (Ch. 7, §7.5, p. 110)
