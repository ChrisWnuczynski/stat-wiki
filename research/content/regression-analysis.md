## Lead context
Regression analysis estimates how a response moves with one or more predictors, and it attaches a measure of reliability to that estimate and to the predictions that follow from it.

The estimated variable is the response, often written \(Y\). The variables used to explain it are the predictors, often written \(X\). The estimate is a mathematical relation fitted to a sample. The reliability is a separate question: how far that relation would move if the sample were drawn again, and how far a new response could sit from the fitted value. The relation by itself does not answer the reliability question, and a reliable fit inside the observed range of the predictors does not, by the algebra alone, say what would happen if a predictor were set to a new value by an intervention.{{cite:dodge2008}} (pp. 450–452){{cite:james_islr2013}} (pp. 59–60, Ch. 3)

## Motivating example
A product's sales are recorded against the budgets spent on television, radio, and newspapers. A consultant is asked what marketing plan would raise sales next year. Before any coefficient is quoted, the data have to answer a short list of questions. Is there an association between budget and sales at all? If the evidence is weak, spending more is not supported by these records. If there is an association, how tight is the prediction: given a budget, are sales predictable, or only slightly better than a guess? Which of the three media contribute, once money has been spent on all three? How precisely is each medium's contribution estimated? How precisely can a future sales figure be predicted? Is a straight line enough, or does the relation bend? Do the media interact, so that money split across television and radio sells more than the same money spent on one of them? Linear regression is the tool James, Witten, Hastie, and Tibshirani use to organise those questions. The fitted line, or the fitted plane, is the estimate. The standard errors, the residual scale, and the checks on the shape of the residuals are the reliability.{{cite:james_islr2013}} (pp. 59–60, Ch. 3)

A smaller version of the same problem uses one predictor and three points, so that every sum can be written by hand. The inputs are \(x=0, 1, 2\) and the responses are \(y=1, 3, 3\). A line is wanted for how \(y\) moves with \(x\) inside this sample. The line will be a summary of the three points. It will not, by being a line, be a causal effect of setting \(x\).

## Definition
A regression analysis starts from a sample of joint observations and estimates a relation that predicts the response from the predictors. When the response depends on a single predictor the analysis is simple. When several predictors enter, it is multiple. When the relation is linear in the unknown coefficients, it is linear regression, whether the picture against one raw predictor is a straight line or a curve. Dodge's statement of the scope is that simple regression is the case of one predictor, multiple regression is the case of more than one, and linear regression is the case in which the relation between response and predictors is linear.{{cite:dodge2008}} (p. 450)

The working model for a straight line is
\[
Y=\beta_0+\beta_1 x+\varepsilon.
\]
The coefficients are unknown. The line people overlay on a scatterplot is an estimate of that relation, not the relation itself. The estimate is exact only in constructed cases, such as a price computed from a formula. In data, the points form a cloud around the line. OpenIntro's illustration is a share price that sits on a perfect line, set against family income and financial aid, where income is useful and the prediction is far from perfect.{{cite:openintro2019}} (Ch. 8, §8.1.1){{cite:james_islr2013}} (p. 61, §3.1)

[Simple linear regression](simple-linear-regression.qmd) is the one-predictor straight line. [Multiple linear regression](multiple-linear-regression.qmd) keeps a mean that is linear in the coefficients and adds predictors. Both are usually fitted by [ordinary least squares](ordinary-least-squares.qmd), the minimiser of the sum of squared residuals. [Polynomial least squares](polynomial-least-squares.qmd) stays inside that class and lets the mean bend by adding powers of a predictor: the mean is curved in \(x\) and linear in the coefficients. [Nonlinear regression](nonlinear-regression.qmd) is the step outside the class, when a coefficient sits inside the mean function, the normal equations are not linear, and the least-squares solution is iterative. Dodge's example of that step is a mean in which two rate coefficients sit inside exponentials.{{cite:james_islr2013}} (p. 266, §7.1){{cite:dodge2008}} (p. 373)

## Properties
For fixed inputs \(x_1,\ldots,x_n\), not all equal, and responses \(y_1,\ldots,y_n\), the least-squares slope and intercept minimise \(\sum_i(y_i-b_0-b_1 x_i)^2\). The minimiser is
\[
\hat\beta_1=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}{\sum_i(x_i-\bar x)^2},\qquad
\hat\beta_0=\bar y-\hat\beta_1\bar x.
\]
The fitted line passes through \((\bar x,\bar y)\). That identity is the first normal equation. It is not a statement that the mean response equals the sample mean of \(y\) at every \(x\).

On the three-point sample, \(\bar x=1\) and \(\bar y=7/3\). The centred sum of squares of \(x\) is
\[
S_{xx}=(0-1)^2+(1-1)^2+(2-1)^2=2,
\]
and the centred sum of products is
\[
S_{xy}=(0-1)\bigl(1-\tfrac73\bigr)+(2-1)\bigl(3-\tfrac73\bigr)=\tfrac43+\tfrac23=2.
\]
The slope is \(2/2=1\). The intercept is \(7/3-1\cdot 1=4/3\). The fitted values are \(4/3\), \(7/3\), and \(10/3\). The residuals are \(-1/3\), \(2/3\), and \(-1/3\), and the residual sum of squares is
\[
\bigl(-\tfrac13\bigr)^2+\bigl(\tfrac23\bigr)^2+\bigl(-\tfrac13\bigr)^2=\tfrac{1}{9}+\tfrac{4}{9}+\tfrac{1}{9}=\tfrac{2}{3}.
\]
The horizontal line at the mean \(7/3\) has residual sum of squares \(8/3\). The fitted slope removes \(2\) from that sum, from \(8/3\) down to \(2/3\). The fraction removed is \((8/3-2/3)/(8/3)=3/4\). That fraction is a description of these three points. It is not a probability, and it is not a licence to extend the line past \(x=2\).{{cite:openintro2019}} (Ch. 8, §8.2.2){{cite:dodge2008}} (p. 304)

Squared error charges a residual of \(4\) sixteen times as heavily as a residual of \(1\), and four times as heavily as a residual of \(2\). Absolute error would charge the residual of \(4\) only four times the residual of \(1\), and twice the residual of \(2\). The two criteria fit different lines. Least squares is the usual choice because a residual twice as large is treated as more than twice as serious, and because the resulting line is the one statistical software returns by default.{{cite:openintro2019}} (Ch. 8, §8.2.2)

## Statistical use
The questions that organise a regression are the advertising questions: whether a relation is visible, how tightly it predicts, which predictors contribute, how precisely each contribution is estimated, how precisely a new response can be predicted, and whether a straight line is enough. A weak association is a reason to doubt that changing a budget will move the response in the way a fitted slope suggests. A strong association is still an association in the sample. Reading it as the effect of an intervention requires a design that supports the intervention.{{cite:james_islr2013}} (pp. 59–60, Ch. 3)

Quote a slope as a change in fitted height per unit of the predictor inside the observed range. The intercept is the fitted height at \(x=0\). If \(x=0\) is far from the values that were used, that intercept is an extrapolation. A prediction for a new response at a new \(x\) is a different object from an estimate of the mean response: the new response adds one error on top of the uncertainty in the fitted line. Outside the observed range the same algebra still prints a number. OpenIntro's warning is that a linear model is a modelling framework, and the behaviour outside the window of the data is not supplied by the fit.{{cite:openintro2019}} (Ch. 8, §8.1.1 and §8.2.6){{cite:james_islr2013}} (pp. 59–60, Ch. 3)

The conditions collected for a least-squares line are a linear trend, residuals whose shape is not dominated by a few points, a spread that does not trend with the fit, and observations that are not a time series in disguise. Those conditions are checks on the summary. They are not a proof of cause. A nonlinear trend is a reason to leave the straight line, for a polynomial in the predictor or for a mean that is nonlinear in the coefficients, rather than a reason to quote the straight slope as if the bend were not there.{{cite:openintro2019}} (Ch. 8, §8.2.3){{cite:dodge2008}} (p. 452)

Whatever the variant, a [generalised linear model](generalised-linear-model.qmd) changes the response distribution and the link, and [ridge regression](ridge-regression.qmd) keeps a linear mean while shrinking coefficients when the predictors are many or nearly redundant. The reliability question remains: residual analysis is the usual check that the fitted relation is not an artefact of one or two points.{{cite:dodge2008}} (p. 452)

## Worked example
For \(x=0, 1, 2\) and \(y=1, 3, 3\), the least-squares line is \(\hat y=4/3+x\). The fitted values are \(4/3\), \(7/3\), and \(10/3\). The residual sum of squares is \(2/3\). The line passes through the mean point \((1, 7/3)\). At \(x=1\), which is inside the observed inputs, the fitted mean is \(7/3\). At \(x=4\), which is outside the observed inputs, the same formula prints \(4/3+4=16/3\). That number is an extrapolation. Nothing in the three points says the mean is still linear there.

The absolute residuals are \(1/3\), \(2/3\), and \(1/3\), and they sum to \(4/3\). The squared residuals sum to \(2/3\). The largest residual, \(2/3\), contributes \(4/9\) of the squared sum and only \(2/3\) of the absolute sum. Squaring is what makes that middle point the expensive one.{{cite:openintro2019}} (Ch. 8, §8.2.2){{cite:james_islr2013}} (p. 61, §3.1)

**Your turn.** Fit a least-squares line to the two points \((1, 2)\) and \((3, 6)\). Give the slope, the intercept, and the residual sum of squares.

::: {.callout-tip collapse="true" title="Answer"}
The mean of \(x\) is \(2\) and the mean of \(y\) is \(4\). The centred sum of squares of \(x\) is \(2\), and the centred sum of products is \(4\), so the slope is \(2\) and the intercept is \(0\). Both points lie on \(y=2x\), and the residual sum of squares is \(0\).
:::

## Common misconceptions
The slope is not a causal effect of changing the predictor. The advertising budgets were chosen, and even then unmeasured differences can sit in the errors. In an observational series the same algebra produces a slope and does not produce an intervention. OpenIntro's observational studies make the same point for a different design: an association, such as sunscreen use with skin cancer, can run through a confounder, and the fitted slope does not name it.{{cite:openintro2019}} (Ch. 1, §1.3.4){{cite:james_islr2013}} (pp. 59–60, Ch. 3)

Least squares minimises vertical squared gaps, not absolute gaps and not horizontal gaps. Predicting \(x\) from \(y\) swaps the roles and produces a different line. A model such as \(\beta_1/(\beta_1-\beta_2)\) times a difference of exponentials is a curve in \(x\) and is not linear in the parameters, so the closed form above does not apply. Calling that curve a polynomial, or calling a polynomial nonlinear least squares, swaps the two neighbouring fits.{{cite:dodge2008}} (p. 373){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1)

A high fraction of residual sum of squares removed, such as the \(3/4\) on the three-point line, is not a high probability that the line is the population mean. It is the fraction of the sample's squared variation about \(\bar y\) that the line captured. Three points can be captured tightly by a line that is the wrong shape one step past the largest \(x\).

## History
Determining a line through inconsistent observations was an astronomical problem in the eighteenth century. Boscovich, around 1755–1757, asked for a line whose residuals sum to zero and whose absolute residuals have the smallest possible sum, and he applied a geometric solution to the lengths of five meridians. Laplace, in 1789, gave an algebraic form of those two conditions. Gauss and Legendre, working separately, developed least squares, the squared-error criterion that became the standard fit. Legendre published it in 1805. Gauss had been using it earlier and a dispute over priority followed in 1809. An American, Robert Adrain, was working with the same criterion without knowledge of either. The word regression, in the linear sense used now, comes from Galton's studies of heredity. In 1875 he sorted sweet-pea seeds into seven groups by weight, grew them, and found each group of offspring centred near a value pulled toward the population mean. From 1885 he used the word regression for that linear return.{{cite:dodge2008}} (pp. 450–451){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1)

## Connections
A regression line is a summary of association in the sample that produced it. Neighbouring tools that answer different questions are a [confidence interval](confidence-interval.qmd) for a coefficient or a mean, a [prediction interval](prediction-interval.qmd) for a new response, and the [sampling distribution](sampling-distribution.qmd) of the coefficient estimators. [Polynomial least squares](polynomial-least-squares.qmd) is the linear fit that adds powers. [Nonlinear regression](nonlinear-regression.qmd) is the iterative fit that does not. [Ordinary least squares](ordinary-least-squares.qmd) is the criterion shared by the linear cases, simple or multiple. The conditions on the residuals remain the check that the summary is worth reporting.{{cite:openintro2019}} (Ch. 8, §8.2.3){{cite:james_islr2013}} (pp. 59–61, Ch. 3)
