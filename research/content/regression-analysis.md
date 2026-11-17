

## Lead context

Regression analysis estimates how one variable moves with one or more others, and it attaches some measure of reliability to that estimate and to the predictions that follow from it. The estimated variable is the response. The variables used to explain it are the predictors.{{cite:dodge2008}} (pp. 450–452, definition and the reliability of estimates)

## Motivating example

A shop records advertising spend and weekly sales for six weeks: spends 1, 2, 3, 4, 5, 6 and sales 2, 3, 5, 6, 8, 9. The spend mean is 3.5 and the sales mean is 5.5. The slope of the least-squares line is the ratio of the centred cross-product to the centred sum of squares of spend. The centred spends are -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, with squared sum 17.5. The centred sales are -3.5, -2.5, -0.5, 0.5, 2.5, 3.5, and the cross-product is 2.5*3.5 + 1.5*2.5 + 0.5*0.5 + 0.5*0.5 + 1.5*2.5 + 2.5*3.5 = 17.5. The slope is 17.5/17.5 = 1, and the intercept is 5.5 - 1*3.5 = 2. The fitted line is sales = 2 + spend. That line is a summary of these six weeks. It does not, by the arithmetic, say what sales would be if spend were set by an intervention.

## Definition

A regression analysis starts from a sample of paired or joint observations and estimates a mathematical relation that predicts the response from the predictors. When the response depends on a single predictor the analysis is simple. When several predictors enter, it is multiple. When the relation is linear in the unknown coefficients, it is linear regression, whether the picture against one raw predictor is a straight line or a polynomial curve. The fitted relation is then used to predict, and the same fit supplies the residual scale on which the uncertainty of those predictions is judged. The predictions carry an error even when the relation is stable.{{cite:dodge2008}} (pp. 450–452){{cite:james_islr2013}} (pp. 59–60, Ch. 3)

The questions that organise the analysis are whether a relation is visible at all, how tightly it predicts, which predictors contribute, how precisely each contribution is estimated, how precisely a new response can be predicted, and whether a straight line is enough. A weak association is a reason to doubt that changing a budget, or any other predictor, will move the response in the way a fitted slope suggests.{{cite:james_islr2013}} (pp. 59–60, Ch. 3)

The working model for a straight line is $y=\beta_0+\beta_1 x+\varepsilon$, with the coefficients estimated from the sample. The line people overlay on a scatterplot is that estimate. It is exact only in constructed cases, such as a price that is computed from a formula. In data, the points form a cloud around the line.{{cite:openintro2019}} (Ch. 8, §8.1.1)

## Statistical use

[Simple linear regression](simple-linear-regression.qmd) is the one-predictor straight line. [Multiple linear regression](multiple-linear-regression.qmd) keeps a mean that is linear in the coefficients and adds predictors. Both are usually fitted by [ordinary least squares](ordinary-least-squares.qmd), the minimiser of the sum of squared residuals, which is the special case of [least squares](least-squares.qmd) used throughout linear regression. Squaring is the common choice because a residual of $4$ is treated as more than twice as serious as a residual of $2$, and because the resulting line is the one statistical software returns by default. Minimising the sum of absolute residuals is a different fit.{{cite:openintro2019}} (Ch. 8, §8.2.2){{cite:james_islr2013}} (p. 59, Ch. 3, least squares as the usual fit)

[Polynomial least squares](polynomial-least-squares.qmd) stays inside linear regression and lets the mean bend by adding powers of a predictor.{{cite:james_islr2013}} (p. 266, §7.1) [Nonlinear regression](nonlinear-regression.qmd) is the step outside that class, when a coefficient sits inside the mean function and the least-squares solution is iterative.{{cite:dodge2008}} (p. 372, nonlinear in the parameters) A [generalised linear model](generalised-linear-model.qmd) changes the response distribution and the link: [Poisson regression](poisson-regression.qmd) for counts, and [binary logistic regression](binary-logistic-regression.qmd) for a yes-or-no outcome. [Ridge regression](ridge-regression.qmd) keeps a linear mean and shrinks the coefficients when the predictors are many or nearly redundant.

Whatever the variant, a fitted coefficient is read inside the observed range of the predictors, and a prediction for a new response is a different object from an estimate of the mean response. The analysis also asks whether an apparent relation would be expected from noise alone. That question is empty if the conditions that justify the reference distribution are ignored.{{cite:dodge2008}} (p. 452, significance and prediction){{cite:openintro2019}} (Ch. 8, §8.2.3, linearity, residual shape, constant spread, and independence)


## Worked example

A shop records advertising spend and weekly sales for six weeks: spends 1, 2, 3, 4, 5, 6 and sales 2, 3, 5, 6, 8, 9. The spend mean is 3.5 and the sales mean is 5.5. The slope of the least-squares line is the ratio of the centred cross-product to the centred sum of squares of spend. The centred spends are -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, with squared sum 17.5. The centred sales are -3.5, -2.5, -0.5, 0.5, 2.5, 3.5, and the cross-product is 2.5*3.5 + 1.5*2.5 + 0.5*0.5 + 0.5*0.5 + 1.5*2.5 + 2.5*3.5 = 17.5. The slope is 17.5/17.5 = 1, and the intercept is 5.5 - 1*3.5 = 2. The fitted line is sales = 2 + spend. That line is a summary of these six weeks. It does not, by the arithmetic, say what sales would be if spend were set by an intervention.

**Your turn.** Using the same records, recompute the featured summary and state which population quantity it estimates.

::: {.callout-tip collapse="true" title="Answer"}
Recompute the displayed summary from the same records. It estimates the quantity named in the example, for these records only.
:::

## History

Determining a line through inconsistent observations was an astronomical problem in the eighteenth century. Boscovich, around 1755–1757, asked for a line whose residuals sum to zero and whose absolute residuals have the smallest possible sum, and he applied a geometric solution to lengths of a meridian. Laplace, in 1789, gave an algebraic form of those two conditions. Gauss and Legendre, working separately, developed least squares, the squared-error criterion that became the standard fit. The word regression, in the linear sense used now, comes from Galton's studies of heredity, including the 1875 experiment with sweet-pea seeds sorted by weight.{{cite:dodge2008}} (pp. 451–452)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 8. Their total is 36, so their mean is 4.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 2.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Regression analysis has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 4.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [Simple linear regression](simple-linear-regression.qmd), [Multiple linear regression](multiple-linear-regression.qmd), [ordinary least squares](ordinary-least-squares.qmd), [least squares](least-squares.qmd).

Two further limits are algebraic. The sum of deviations from the mean 4.5 is zero, so the mean is the least-squares centre of these 8 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 4.5.

## Connections

A regression line is a summary of association in the sample that produced it. It does not, by the algebra alone, say what would happen if a predictor were set to a new value by intervention. The conditions collected for a least-squares line — a linear trend, residuals whose spread does not trend with the fit, and observations that are not a time series in disguise — are checks on the summary, not a proof of cause. Neighbouring tools that answer different questions are a [confidence interval](confidence-interval.qmd) for a coefficient or a mean, a [prediction interval](prediction-interval.qmd) for a new response, and the [sampling distribution](sampling-distribution.qmd) of the coefficient estimators.{{cite:openintro2019}} (Ch. 8, §§8.1.1 and 8.2.3){{cite:james_islr2013}} (pp. 59–60, Ch. 3, prediction accuracy and linearity)
