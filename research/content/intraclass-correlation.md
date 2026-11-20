## Motivating example
Repeated measurements on one person can resemble one another more closely than measurements from different people. A shared random intercept provides a direct model for that resemblance and distinguishes variation between people from variation within a person.{{cite:laird_ware1982}} (§2, pp. 964–965)

## Definition — A variance ratio for a shared intercept
Let $Y_{ji}=\mu+A_j+\varepsilon_{ji}$, where $A_j$ has variance $\sigma_A^2$ and the independent individual errors have variance $\sigma^2$. The random intercepts are independent across groups and independent of the errors. For distinct observations in one group,
$$\operatorname{Cov}(Y_{ji},Y_{ji'})=\sigma_A^2,\qquad
\rho=\operatorname{Corr}(Y_{ji},Y_{ji'})=\frac{\sigma_A^2}{\sigma_A^2+\sigma^2}.$$
This is the random-intercept special case of the marginal covariance $R_j+Z_jDZ_j^\top$, taking $Z_j$ to be a column of ones.{{cite:laird_ware1982}} (§2, p. 965) The same conditional and marginal distinction is central to the general linear mixed model.{{cite:bates_lme4_2015}} (§1.1, linear mixed models)

## Properties — Averaging cannot remove a shared component
For $m$ observations in a group,
$$\operatorname{Var}(\overline Y_j)=\sigma_A^2+\frac{\sigma^2}{m}
=\frac{\sigma_A^2+\sigma^2}{m}\{1+(m-1)\rho\}.$$
The first identity follows by separating the shared intercept from the average of independent errors. The second is an algebraic rearrangement. The multiplier $1+(m-1)\rho$ compares the variance with the variance under independence at the same marginal observation variance. More within-group observations reduce individual noise, while the random-intercept component remains.{{cite:laird_ware1982}} (§2, marginal covariance, p. 965)

In this model, a defined ICC lies in $[0,1]$. An unrestricted exchangeable correlation matrix on $m$ observations instead permits $-1/(m-1)\le\rho\le1$ because its eigenvalues are $1-\rho$ and $1+(m-1)\rho$. Negative exchangeable correlations therefore require another mechanism; they cannot arise from an independent additive random intercept with nonnegative variance.{{cite:bates_lme4_2015}} (§1.1, covariance parametrisation)

## Worked example — Ten observations with a common source of variation
If $\sigma_A^2=3$ and $\sigma^2=1$, each observation has variance four and the ICC is $0.75$. For ten observations from one group, the mean has variance $3+1/10=3.1$. Treating them as independent would give $4/10=0.4$. The ratio is $7.75=1+9(0.75)$. On this variance comparison, ten correlated measurements provide the same precision as $10/7.75=40/31$ independent measurements of variance four. This is a comparison for estimating a common mean; treatment contrasts and unequal groups need their own design calculation.

**Your turn.** What happens to the group mean's variance as the group size tends to infinity?

::: {.callout-tip collapse="true" title="Answer"}
It tends to $\sigma_A^2=3$. Averaging suppresses the individual errors but leaves the shared group intercept.
:::

## Connections — Correlation is conditional on the model
Adding fixed covariates changes the residual variance components whose ratio is being interpreted. A random slope can also make the correlation depend on both observations' covariate values. Reporting one ICC therefore requires specifying the response model, its grouping unit and any conditioning covariates.{{cite:laird_ware1982}} (§2, pp. 964–965)

## Check yourself

Use the definitions and calculations above to work through these questions.

### Shared intercepts and slopes {#self-check-c-35}

[Shared intercepts and slopes](../questions/c-35.qmd). Explain where each random effect enters.

::: {.callout-tip collapse="true" title="Answer"}
A random intercept shifts a group’s baseline; a random slope changes its covariate effect. In a GLMM both enter the conditional linear predictor. Their covariance can make marginal dependence vary with the covariates.
:::

### A proposed negative correlation {#self-check-ex-ur-exchangeable-bound}

[A proposed negative correlation](../questions/ex-ur-exchangeable-bound.qmd). Check the all-ones direction for four visits.

::: {.callout-tip collapse="true" title="Answer"}
The exchangeable matrix has all-ones eigenvalue $1+3\rho$. At $\rho=-0.5$ this is $-0.5$, so the matrix cannot be a correlation matrix. The lower permissible bound is $-1/3$.
:::
