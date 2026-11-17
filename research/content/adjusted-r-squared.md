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
