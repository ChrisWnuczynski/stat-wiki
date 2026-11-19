## Lead context

Squared residuals punish a wild point by the square of its distance, so one distant observation can swing a fitted line. Least absolute deviations fit the same linear summary by minimising the sum of absolute residuals instead. The criterion is an old alternative to least squares, and for a single location it picks a median. {{cite:dodge2008}} (pp. 291, 299)

## Motivating example

Three points sit at $x=0,1,2$ with responses $0,0,3$. The horizontal line $y=0$ misses the third point by 3, so the sum of absolute residuals is 3. The line $y=1.5x$ passes through $(0,0)$ and $(2,3)$ and misses $(1,0)$ by 1.5, so the sum is 1.5. The line through $(1,0)$ and $(2,3)$ misses the origin by 3. Among lines that pass through two of the points, $y=1.5x$ has the smallest absolute-residual sum. That comparison is the geometric fact Dodge isolates for simple regression: a minimising line passes through at least two observations, and the pair is the one that makes the sum smallest. {{cite:dodge2008}} (pp. 299–300)

## Definition

For the simple regression $y_i=\beta_0+\beta_1 x_i+\varepsilon_i$, least absolute deviations chooses $\hat\beta_0$ and $\hat\beta_1$ to minimise

$$
\sum_i |e_i|=\sum_i |y_i-\hat\beta_0-\hat\beta_1 x_i|.
$$


There is no closed-form expression of the least-squares type. The fit is defined as the minimiser, and it is computed by an algorithm. The algorithm Dodge describes uses the fact that the regression line always crosses at least two data points. One searches, among lines through pairs of observations, for the pair whose line has the smallest sum of absolute residuals. {{cite:dodge2008}} (pp. 299–300)

In one dimension the same criterion estimates a location $\beta_0$ in $y_i=\beta_0+\varepsilon_i$ by minimising $\sum_i |y_i-\beta_0|$. That minimiser is a median of the observations. The regression fit is the extension of that idea to a line: absolute residuals rather than squared residuals, and no explicit formula. {{cite:dodge2008}} (pp. 291, 299)

[Ordinary least squares](ordinary-least-squares.qmd) estimates the parameters by minimising the sum of squared deviations between the data and the model. NIST lists sensitivity to outliers among the disadvantages of that criterion: one or two unusual points can skew the fit. A line that minimises squared residuals and a line that minimises absolute residuals are not two attempts at one number. {{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, “Why Least Squares?” and “Disadvantages”) {{cite:dodge2008}} (p. 299)

## Properties

Two particular cases appear when the algorithm is run. The solution need not be unique: at least two lines can share the same minimal sum of absolute residuals. Degeneracy, in Dodge’s geometric account, means the minimising line passes through more than two observations. The derivative of $|e|$ does not exist at a zero residual, which is why the usual least-squares calculus does not deliver a closed equation at the solution. The algorithm searches pairs instead. {{cite:dodge2008}} (p. 300)

For a single location the three descriptions agree when the criterion has a unique minimiser: the sample median, the minimiser of $\sum |y_i-\theta|$, and a centre at which the positive and negative residuals balance in the absolute-deviation sense. Boscovich’s eighteenth-century side condition, that the sums of the positive and negative residuals be equal, is the ancestor of that balance, together with the requirement that the sum of absolute residuals be minimal. {{cite:dodge2008}} (p. 291)

A large residual still contributes to the sum, but only through its absolute value. Least squares contributes the square. That is the sense in which Dodge calls the L1 estimators less sensitive to outliers than least squares. The fit is not immune to a change of sign. A point that crosses the line changes which pair is best. {{cite:dodge2008}} (pp. 291, 299–300)

## Worked example

For the three points $(0,0)$, $(1,0)$, and $(2,3)$, the line through the first and third has slope $3/2$ and equation $y=1.5x$. Absolute residuals are $0$, $1.5$, and $0$, summing to $1.5$. The line $y=0$ has absolute residuals $0$, $0$, and $3$, summing to $3$. The line through $(1,0)$ and $(2,3)$ is $y=-3+3x$, with absolute residuals $3$, $0$, and $0$, summing to $3$. The least absolute deviations fit among these pair-lines is $y=1.5x$, with criterion value $1.5$. The mean of the three responses is $1$, and the horizontal line at that mean has absolute residual sum $|0-1|+|0-1|+|3-1|=4$, larger still. {{cite:dodge2008}} (pp. 299–300)

**Your turn.** For the points $(0,1)$, $(1,1)$, and $(2,5)$, compute the sum of absolute residuals for the line $y=1$ and for the line $y=1+2x$. Which sum is smaller?

::: {.callout-tip collapse="true" title="Answer"}
The line $y=1$ has absolute residuals $0$, $0$, and $4$, summing to $4$. The line $y=1+2x$ has residuals $0$, $-2$, and $0$, summing to $2$. The smaller sum is $2$.
:::

## Assumptions and limits

The geometric claim that a solution passes through two observations is for simple regression. Non-uniqueness and degeneracy are both possible, so “the” least absolute deviations line may be a set of lines, or a line through more than two points. With a handful of points the pair search gives the minimal sum exactly, up to ties among pairs. An asymptotic standard error is a different summary, and Dodge’s history records that asymptotic theory for the regression estimator arrived late: Bassett and Koenker developed it in 1978, after a long period in which the lack of a closed formula and the lack of that theory kept the method out of routine use. The small-sample answer is the minimal sum itself. {{cite:dodge2008}} (pp. 291, 300)

If the scientific target is the least-squares fit, absolute deviations estimate a different summary. Least squares is sensitive to unusual points; absolute deviations replace the square with the absolute value. Least absolute deviations is the estimator for that second criterion. It is not a re-expression of the least-squares coefficient. {{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, “Disadvantages of Linear Least Squares”) {{cite:dodge2008}} (p. 299)

## History

Boscovich, in 1757, proposed two criteria for a line: the positive and negative residuals should balance, and the sum of absolute residuals should be minimal. He used the idea while reconciling inconsistent measurements. Laplace gave an analytical procedure for those criteria in 1793. Least squares, associated with Legendre and Gauss, then dominated, because the squared criterion has easy calculus and a closed linear solution. Through the first half of the twentieth century the numerical difficulty and the missing asymptotic theory kept L1 regression in the background. From about 1970 the computation became routine, Bassett and Koenker gave the asymptotic theory in 1978, and a 1987 conference in Neuchâtel was devoted to L1 methods. The one-dimensional ancestor remains the centre that minimises the sum of absolute deviations. {{cite:dodge2008}} (pp. 291, 299)
