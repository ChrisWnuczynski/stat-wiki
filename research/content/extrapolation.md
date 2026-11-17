

## Lead context

A line fitted on family incomes between a few thousand dollars and about a quarter of a million dollars will produce a number if one plugs in an income of a million. Extrapolation is that step: using the fitted relation at an explanatory value outside the set of values that were observed. The arithmetic is the same as interpolation. The justification is not, because nothing in the sample showed that the relation still holds out there.{{cite:dodge2008}} (p. 195){{cite:openintro2019}} (Ch. 8, §8.2.6)

## Motivating example

Elmhurst College’s aid to a sample of freshmen is summarised by $\widehat{\mathrm{aid}}=24319-0.0431\times\text{family income}$, with incomes in the scatter running up to roughly $\$250{,}000$. Substituting a family income of $\$1{,}000{,}000$ gives $24319-0.0431\times 1{,}000{,}000=-18781$. The formula says the student would receive negative aid. The college does not bill a negative grant. The line was a local description of aid against income inside the observed window. Outside that window it is an extrapolation, and the extrapolation has left the process the data were able to describe.{{cite:openintro2019}} (Ch. 8, §8.2.6)

## Definition

An extrapolation is an estimate of the dependent variable at values of the independent variable that lie outside the set of observed values. A simple linear regression fitted to pairs $(X_i,Y_i)$ can be evaluated at an $X$ beyond the smallest and largest sample $X_i$, and a multiple regression can be evaluated at a covariate vector outside the observed cloud. In a time series, extrapolation is the use of a model determined from values at times $t_1<\cdots<t_n$ to produce a value at a later time.{{cite:dodge2008}} (p. 195)

The operation is distinguished from evaluation inside the observed range. Inside the range, the data have at least had a chance to contradict the fitted shape. Outside it, the fit is being trusted on the hypothesis that the model does not change for the new explanatory values. That hypothesis is not checked by the residual sum of squares of the original fit.{{cite:dodge2008}} (p. 195){{cite:openintro2019}} (Ch. 8, §8.2.6)

A fitted line is an approximation on the range where the points sit. The slope is an average tilt over that range. Beyond the last point, the tilt can change, flatten, or hit a boundary the linear formula cannot represent, such as aid that cannot be negative. Time series make the same bet one step past the last time index: the model fitted on $t_1<\cdots<t_n$ is asked for time $t_{n+1}$. The forecast exists as a number whenever the formula can be evaluated. Its claim to be a description of the series is the claim that the mechanism has not changed.{{cite:dodge2008}} (p. 195){{cite:openintro2019}} (Ch. 8, §8.2.6)

Smooth curves can fail more sharply than straight lines. A polynomial, or a spline beyond its boundary knots, is free to bend in a region where there are no observations to restrain it. The pointwise variance of a least-squares spline fit shows the uncertainty blowing up past the boundary, and the point estimate itself can swing more wildly than the global polynomial of the same degree.{{cite:hastie_esl2009}} (Ch. 5, §5.2.1, p. 144)

Before reporting a fitted value, compare the requested explanatory point with the observed range of each covariate, not only with the range of the response. If the point is outside, say so, and treat the number as an extrapolation whose validity is the claim that the fitted mechanism persists. In forecasting, the same discipline applies one step ahead and becomes stricter several steps ahead, where the path depends on the fitted dynamics remaining stable. Multiple regression does not remove the issue: a point can lie inside every one-dimensional range and still sit outside the observed joint cloud.{{cite:dodge2008}} (p. 195)

Prefer a summary that is honest about the edge when the edge is the scientific question. For a smooth regression, a local linear fit is the more reliable default if the analysis must approach the boundary. A natural constraint, such as aid that cannot be negative, is a change of model, not a property that least squares will discover from interior points.{{cite:hastie_esl2009}} (Ch. 6, §6.1.2, p. 198){{cite:openintro2019}} (Ch. 8, §8.2.6)

A high $R^2$ on the observed sample does not validate an extrapolation. The coefficient of determination summarises residuals inside the fit. Extrapolation fails when the mean function changes outside the sample, which those residuals do not see. A prediction interval at a remote $x$ is not a remedy for a wrong mean function. Polynomials and splines are not safer than lines at the edge; past the boundary knots they are often less safe. Multiple regression is not exempt.{{cite:openintro2019}} (Ch. 8, §8.2.6){{cite:hastie_esl2009}} (Ch. 5, §5.2.1, p. 144){{cite:dodge2008}} (p. 195)

[Ordinary least squares](ordinary-least-squares.qmd) produces the line that is so often evaluated past the data. A [prediction interval](prediction-interval.qmd) widens with leverage but stays inside the fitted model. Forecasting in a time series is extrapolation along the time index. [Asymptotic analysis](asymptotic-analysis.qmd) of local polynomials is one place the boundary, where extrapolation begins, changes the preferred degree of fit.

## Properties

The formula used to extrapolate is whatever formula was fitted. For the Elmhurst line the extrapolated aid is the same linear expression, and it decreases by $0.0431$ dollars of aid per extra dollar of income without a floor. Nothing in the least-squares algebra inserts a warning when $X$ leaves the sample. The warning is a property of the scientific claim, not of the minimiser.{{cite:openintro2019}} (Ch. 8, §8.2.6){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1)

For kernel and local-polynomial smoothers, boundary behaviour is an asymptotic question as well as a practical one. Asymptotic mean-squared-error comparisons favour local linear fits over local quadratic fits when the interest is the boundary, because the boundary is where extrapolation, or near-extrapolation, is most sensitive to the degree of the local polynomial. A global cubic polynomial fitted to the interior is already a poor guide past the last observation; a spline that continues as a polynomial beyond the outer knots exaggerates the problem.{{cite:hastie_esl2009}} (Ch. 5, §5.2.1, p. 144; Ch. 6, §6.1.2, p. 198)

A prediction interval computed from a linear model at an extrapolated $x$ widens because the leverage of a remote $x$ is large. The widening accounts for sampling uncertainty in the fitted mean and, in a prediction interval, for a new residual. It does not account for a change in the form of the mean. Coverage statements for the interval are statements inside the model that was fitted.{{cite:openintro2019}} (Ch. 8, §8.2.6)

## Worked example

The Elmhurst line gives, at a family income of $\$1{,}000{,}000$,

$$
24319-0.0431\times 1{,}000{,}000=24319-43100=-18781.
$$

The extrapolated aid is $-\$18{,}781$. At an income of $\$200{,}000$, which the scatter still reaches, the same line gives $24319-0.0431\times 200000=24319-8620=15699$, an ordinary fitted value inside the window. The two evaluations use one formula. Only the first is an extrapolation. The sign change is the model leaving the region where aid grants, in this college’s practice, live.{{cite:openintro2019}} (Ch. 8, §8.2.6){{cite:dodge2008}} (p. 195)

**Your turn.** Using $\widehat{\mathrm{aid}}=24319-0.0431\times\text{income}$, compute the fitted aid at a family income of $\$400{,}000$.

::: {.callout-tip collapse="true" title="Answer"}
$24319-0.0431\times 400000=24319-17240=7079$. The fitted aid is $\$7{,}079$. Whether $\$400{,}000$ is inside the original sample’s income range decides whether this number is an interpolation or an extrapolation. The arithmetic does not decide that.
:::

## Assumptions and limits

The fitted model is being assumed to persist at the new explanatory value. That assumption is extra. Least squares, as a numerical method, only minimises squared error on the points it was given. Time-series extrapolation adds the assumption that the temporal structure estimated up to $t_n$ still governs $t_{n+1}$. If a constraint such as non-negativity binds outside the sample, the unconstrained fit will not respect it. Checking a few points near the edge of the sample is a sensitivity check, not a proof that the next point beyond the edge obeys the same line.{{cite:dodge2008}} (p. 195){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1)

## History

The operation is as old as using a fitted relationship to fill a value that was not measured. Encyclopedic usage defines it as estimation of the dependent variable off the observed set of the independent variable, and notes the standard setting in time series, where a model on times $t_1<\cdots<t_n$ is asked for $t_{n+1}$. The caution attached to that definition is unchanged in modern regression teaching: the number is computed from the hypothesis that the model does not change, and a linear formula will happily produce a negative grant, or a temperature no climate produces, once the explanatory value leaves the window that was studied. Spline and kernel methods made the boundary problem quantitative, by showing how fast variance grows and how local polynomial degree changes the bias just where the data stop.{{cite:dodge2008}} (p. 195){{cite:openintro2019}} (Ch. 8, §8.2.6){{cite:hastie_esl2009}} (Ch. 5, §5.2.1, p. 144; Ch. 6, §6.1.2, p. 198)
