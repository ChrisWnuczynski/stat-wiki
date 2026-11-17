## Motivating example — A fitted line uses every response
A measurement may differ from its unknown true conditional mean because of random error. It also differs from an estimated line, but that second difference uses coefficients calculated from the data. Calling both differences noise hides a dependence: changing one response can move the fitted line and hence alter several residuals. The observed residual vector is useful for diagnosis precisely because it records what the chosen fitted mean failed to explain.{{cite:nist_model_fit2002}} (§4.4.4, residuals)

## Definition — Separate the model from the calculation
In the fixed-design linear model $Y=X\beta+\varepsilon$, the error vector is $\varepsilon=Y-X\beta$. The coefficient vector $\beta$ is the unknown model parameter. After fitting least squares, the residual vector is $e=y-X\widehat\beta$. It can be computed from observations and the fitted coefficients. The true errors generally cannot be recovered because their calculation would require knowing the true conditional means. This distinction applies even if the fitted line is an excellent approximation.{{cite:dodge2008}} (p. 457, Residual)

For a full-column-rank design, the hat matrix is $H=X(X^\top X)^{-1}X^\top$. It is symmetric and idempotent, and $e=(I-H)y=(I-H)\varepsilon$. Thus the residuals are projections of the errors, rather than independent copies of them. The normal equations give $X^\top e=0$. In particular, when an intercept is fitted, the residuals sum to zero. This is a constraint imposed by fitting; zero-sum errors are not an assumption of the population model.{{cite:nist_ls_straight2002}} (§4.4.3.1, least-squares criterion and normal equations)

## Properties — Fitting changes variance and dependence
Assume $E(\varepsilon\mid X)=0$ and $\operatorname{Cov}(\varepsilon\mid X)=\sigma^2I$. Then
$$E(e\mid X)=0,\qquad \operatorname{Cov}(e\mid X)=\sigma^2(I-H).$$
Multiplying out $(I-H)\sigma^2I(I-H)^\top$ proves the covariance identity. Consequently $\operatorname{Var}(e_i\mid X)=\sigma^2(1-h_{ii})$ and $\operatorname{Cov}(e_i,e_j\mid X)=-\sigma^2h_{ij}$ for distinct indices. Higher leverage reduces the marginal residual variance. Standardising only by a common residual standard deviation does not correct that leverage effect. The interpretation of residual plots should take the fitted model's constraints into account.{{cite:nist_model_fit2002}} (§4.4.4, constraints caused by parameter estimation)

Normality is unnecessary for these moment identities. If the errors are jointly normal, the residual vector is jointly normal too, but its covariance is singular whenever coefficients have been fitted. Residual normality checks concern approximate error-model adequacy, rather than a literal assertion that the fitted residuals are independent draws.{{cite:nist_model_fit2002}} (§4.4.4, model validation specifics)

## Worked example — An intercept-only model
Take responses $(1,2,6)$ and fit their common mean. The fitted value is $3$ for each observation and the residuals are $(-2,-1,3)$; their sum is zero and SSE is $14$. Here every entry of $H$ is $1/3$. If independent errors have variance $\sigma^2=9$, each residual has variance $6$ and every pair has covariance $-3$. Their correlation is $-1/2$, despite the independent errors in the model. The observed SSE estimates the error variance through $14/(3-1)=7$.{{cite:dodge2008}} (p. 457, residual definition; p. 399, within-group sum of squares)

**Your turn.** Add five to every response in this intercept-only example. What happens to the fitted values and residuals?

::: {.callout-tip collapse="true" title="Answer"}
The fitted mean rises from 3 to 8. The residuals stay $(-2,-1,3)$, so SSE stays 14.
:::

## Statistical use — Diagnose what the model leaves unexplained
Plotting residuals against fitted values, predictors and observation order targets different possible failures: curvature, nonconstant spread or temporal dependence. A small residual alone does not guarantee an unimportant observation, since leverage and influence involve the design as well. Conversely, a large residual can be an informative sign of a misspecified mean, an unusual outcome or a data error. Diagnosis should return to the measurement and scientific context before changing a model.{{cite:nist_model_fit2002}} (§4.4.4)
