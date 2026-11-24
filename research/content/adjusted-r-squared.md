## Motivating example
Adding a predictor to a least-squares model cannot increase its training residual sum of squares when the smaller model is nested inside it. Even an irrelevant predictor can therefore increase ordinary $R^2$. Adjusted $R^2$ compares residual variation per residual degree of freedom with total variation per total degree of freedom. It asks whether the improvement in fit offsets the additional fitted coefficients. It remains a descriptive selection criterion; it does not directly estimate the predictive performance of a completed model-search procedure.{{cite:openintro2019}} (§9.1, adjusted R-squared; §9.2, model selection)

## Definition — Count fitted coefficients consistently
For a full-rank least-squares model with an intercept, $n$ observations and $p$ slope coefficients, write $\mathrm{SSE}=\sum_i(y_i-\widehat y_i)^2$ and $\mathrm{SST}=\sum_i(y_i-\bar y)^2$. Provided $n>p+1$ and $\mathrm{SST}>0$,
$$\overline R^2=1-\frac{\mathrm{SSE}/(n-p-1)}{\mathrm{SST}/(n-1)}.$$
This equals $1-(1-R^2)(n-1)/(n-p-1)$. Here $p$ excludes the intercept. A categorical predictor can require several columns, so counting variable names instead of independent design columns gives the wrong residual degrees of freedom. If columns are dependent, replace $p+1$ by the design rank. The positive-SST condition excludes a constant response, for which the ratio is undefined.{{cite:openintro2019}} (§9.1, adjusted R-squared)

## Properties — The improvement threshold is explicit
Consider adding $q$ independent columns to a reduced model. Let its residual degrees of freedom be $d$, its residual sum of squares be $S_R$, and let the larger model have $S_F$ and $d-q$. Comparing the two adjusted scores shows improvement precisely when
$$\frac{S_R-S_F}{q}>\frac{S_F}{d-q}.$$
The left side is the average reduction per added coefficient and the right side is the full-model mean square error. Equivalently, the usual partial $F$ statistic must exceed one. This algebraic threshold is weaker than a typical significance-test threshold. Maximising adjusted $R^2$ is therefore a different rule from retaining only predictors with small p-values.{{cite:openintro2019}} (§9.2, model selection)

Adjusted $R^2$ can be negative because the fitted residual mean square can exceed the sample variance of the response. That outcome does not mean a negative fraction of variance exists. It means the coefficient-count adjustment has outweighed the reduction in residual sum of squares. A high score can also coexist with nonlinear structure or changing residual spread, which require examination of residual plots.{{cite:nist_model_fit2002}} (§4.4.4)

## Worked example — Compare two nested fits
Suppose $n=20$, $\mathrm{SST}=100$, and a model with two slopes has $\mathrm{SSE}=40$. Then $R^2=0.6$, while $\overline R^2=1-(40/17)/(100/19)=0.552941$. A third slope that reduces SSE to $38$ raises ordinary $R^2$ to $0.62$, but adjusted $R^2$ falls to $0.54875$. The partial $F$ is $2/(38/16)=0.842105$, below one. A reduction to $37$ instead gives adjusted $R^2=0.560625$ and clears the algebraic improvement threshold. These calculations compare the same observations and response scale.{{cite:openintro2019}} (§9.2, model selection)

**Your turn.** In the two-slope model above, what is adjusted $R^2$ if SSE is $85$?

::: {.callout-tip collapse="true" title="Answer"}
The residual mean square is $85/17=5$. Hence adjusted $R^2=1-5/(100/19)=0.05$.
:::

## Assumptions and limits — Fit quality has several dimensions
The score is useful only when models use comparable data and an appropriate sum-of-squares definition. Changing observations because a new predictor has missing values changes the comparison. A response transformation changes the scale on which residual variation is measured. Without an intercept, the centred decomposition behind the usual $R^2$ interpretation can fail. Prediction should be evaluated separately on appropriate held-out observations, and residual diagnostics should investigate whether the proposed mean and error structure describe the data.{{cite:nist_model_fit2002}} (§4.4.4, graphical residual analysis)

## Intuition
Ordinary $R^2$ compares the residual sum of squares with the total sum of squares. Both sums use the same observations, and enlarging a nested linear model can only shrink the residual sum or leave it unchanged. The fraction of residual variation therefore falls, and $R^2$ rises, even when the added column is unrelated to the response in any repeatable way. Adjusted $R^2$ divides each sum by a degrees-of-freedom count before forming the ratio. The residual divisor $n-p-1$ shrinks when a slope is added. The score rises only when the drop in SSE is large enough to offset that smaller divisor.

The algebra is easiest one coefficient at a time. Let the reduced model have residual sum $S_R$ and residual degrees of freedom $d$, and let one added independent column produce $S_F$ on $d-1$ degrees of freedom. The adjusted score improves exactly when
$$\frac{S_R-S_F}{1}>\frac{S_F}{d-1},$$
which is the statement that the partial $F$ statistic exceeds one. In the worked numbers, moving from SSE $40$ on $17$ degrees of freedom to SSE $38$ on $16$ degrees of freedom gives partial $F=2/(38/16)\approx 0.842105$, below one, and adjusted $R^2$ falls from $0.552941$ to $0.54875$. A drop from $40$ to $37$ instead clears the threshold and raises the adjusted score to $0.560625$. The same arithmetic, with a different threshold, is what a significance test uses. A conventional $5\%$ $F$ critical value is larger than one, so a coefficient can raise adjusted $R^2$ while failing that test, and a coefficient can pass a tiny-sample test while the ordering of adjusted scores still has to be computed directly.

### Properties — Negative scores and the intercept
The formula $1-(1-R^2)(n-1)/(n-p-1)$ shows when the adjusted score is negative. Because $(n-1)/(n-p-1)>1$ whenever $p\ge 1$ and the residual degrees of freedom are positive, a sufficiently small positive $R^2$ is pulled below zero. With $n=8$, one slope, $\mathrm{SST}=10$ and $\mathrm{SSE}=9$, ordinary $R^2=0.1$, while
$$\overline R^2=1-\frac{9/6}{10/7}=1-\frac{1.5\times 7}{10}=-0.05.$$
The fitted line has reduced the residual sum, from $10$ to $9$, and the degrees-of-freedom adjustment has more than consumed that reduction. A negative value is a comparison of mean squares. It does not mean the response has a negative variance, and it is not a cue to report the absolute value $0.05$ in its place.

Counting coefficients is part of the definition. An intercept plus $p$ independent slopes uses residual degrees of freedom $n-p-1$. A categorical factor with $k$ levels, entered through $k-1$ independent contrasts beside an intercept, contributes $k-1$ to $p$, not one. If the columns are linearly dependent, the residual divisor is $n-r$, where $r$ is the rank of the design, rather than a count of column names. Using $n-p-1$ after two columns have been duplicated understates the residual degrees of freedom and inflates the adjusted score.

Without an intercept, the centred total sum $\sum_i(y_i-\bar y)^2$ is still the residual sum of squares of the model that contains only a constant: fitting a constant alone gives $\bar y$, so that model's SSE is exactly this sum. What changes is the nesting. The constant-only model need not be nested inside a no-intercept fit, so the identity $R^2=1-\mathrm{SSE}/\mathrm{SST}$ can compare the fitted model with a baseline that is not a special case of it. Adjusted $R^2$ inherits that comparison. A no-intercept fit therefore needs its own baseline, stated explicitly, before either score is interpreted as a fraction of centred variation. R's `summary.lm`, for example, uses the zero predictor — the uncentred sum $\sum_i y_i^2$ — as the baseline when there is no intercept.

## Common misconceptions
Maximising adjusted $R^2$ over many candidate subsets is a search. The score of the winner, computed on the same observations that chose the subset, describes that search. It does not estimate the prediction error of the selected model on new observations, and it does not carry the null distribution it would have had if the subset had been chosen before seeing the data. A held-out mean squared error answers a prediction question the adjusted score does not ask.{{cite:openintro2019}} (§9.2, model selection)

A large adjusted score can sit beside a curved residual plot or a variance that changes with the fitted mean. The score is a single comparison of two sums of squares. Residual plots examine the pattern of the summands. Both can be reported. One does not certify the other.{{cite:nist_model_fit2002}} (§4.4.4)

## Connections
The partial $F$ comparison and adjusted $R^2$ use the same residual sums and the same ranks. They impose different cutoffs. Analysis of deviance is the likelihood version of the same nested comparison when the dispersion is known or estimated. In a Gaussian linear model the deviance difference is the drop in residual sum of squares, and the $F$ statistic displayed above is the usual normal-theory calibration of that drop. Information criteria add an explicit penalty to a maximised log likelihood rather than rescaling two sums of squares. Each rule can rank the same two nested Gaussian fits differently because each rule encodes a different tradeoff. The fitted coefficients and the residual plot remain available whichever ranking is used.
