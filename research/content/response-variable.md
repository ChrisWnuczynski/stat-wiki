## Motivating example
Suppose a model predicts a baby's birth weight from the mother's age. Birth weight is the response, while age is the predictor. Reversing the roles asks a different question: the typical mother's age among babies of a given weight. A response is identified by the question and model, rather than being an intrinsic property of a column.{{cite:dodge2008}} (p. 161)

## Definition — The outcome conditional on the predictors
In a model for $Y$ given $X=x$, the response is $Y$. Upper-case notation distinguishes the random outcome from an observed value $y$. A fitted value $\widehat y$ is a prediction, and the residual $y-\widehat y$ is the difference between observation and prediction. A least-squares regression fits a line by minimising squared residuals in the response direction.{{cite:cetinkaya_hardin2024}} (§7.1, “Fitting a line to data” and “Residuals”)

The response need not be continuous. A count, an event indicator or an ordered category can also be an outcome. Its possible values help determine a suitable conditional distribution; a numerical coding alone does not make a categorical outcome a continuous measurement. The response/predictor distinction specifies the direction of the analysis, while the measurement scale specifies what an observation means.{{cite:dodge2008}} (p. 161)

## Properties — Why reversing the axes changes the fit
For paired measurements with nonzero sample variances, the two least-squares slopes satisfy
$$
\widehat\beta_{Y\mid X}=r\frac{s_Y}{s_X},\qquad
\widehat\beta_{X\mid Y}=r\frac{s_X}{s_Y}.
$$
Their product is $r^2$, so they are reciprocals only when $|r|=1$. Reversing the regression changes which squared vertical distances are minimised.{{cite:cetinkaya_hardin2024}} (§7.2, “Finding and interpreting the least squares line”)

A change of response units changes its fitted coefficients and residuals. If $Y^*=a+bY$, with $b\ne0$, fitting the same predictor columns gives $\widehat Y^*=a+b\widehat Y$ and residuals $b(Y-\widehat Y)$. This follows by transforming the squared-error criterion. A nonlinear transformation such as a logarithm generally changes the conditional-mean target as well as its units.{{cite:cetinkaya_hardin2024}} (§7.2, “An objective measure for finding the best line”)

## Worked example — Two regressions through three points
Take the observations $(x,y)=(0,0),(1,0),(2,1)$. Their centred sums are $S_{xx}=2$, $S_{yy}=2/3$ and $S_{xy}=1$. Therefore the fit of $y$ on $x$ is
$$
\widehat y=-\frac16+\frac12x,
$$
whereas fitting $x$ on $y$ gives $\widehat x=1/2+(3/2)y$. The slopes have product $3/4$, equal to the squared sample correlation. Neither regression can be obtained by algebraically reversing the other. The least-squares line passes through the two sample means, which determine the intercepts.{{cite:cetinkaya_hardin2024}} (§7.2, “Finding and interpreting the least squares line”)

**Your turn.** Replace $y$ by $y^*=10+2y$ while leaving $x$ unchanged. Find the new regression line.

::: {.callout-tip collapse="true" title="Answer"}
Transform the fitted values: $\widehat y^*=10+2(-1/6+x/2)=29/3+x$. The new slope is $1$, and the intercept is $29/3$.
:::

