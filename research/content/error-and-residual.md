## Motivating example
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

## Intuition
The error $\varepsilon_i=Y_i-x_i^\top\beta$ compares the response with the conditional mean the model declares. That mean is unknown, so the error is unknown. The residual $e_i=y_i-x_i^\top\widehat\beta$ compares the response with a fitted mean. The fit is a function of the whole sample, including $y_i$ itself, so the residual is a function of the errors rather than a copy of one error. In matrix form, $e=(I-H)\varepsilon$ when the model includes the column space that $H$ projects onto. Fitting has imposed $X^\top e=0$. With an intercept, the residuals sum to zero even if the errors do not.

The intercept-only example makes the dependence numerical. Responses $(1,2,6)$ have mean $3$ and residuals $(-2,-1,3)$. The residual sum of squares is $4+1+9=14$. Every entry of $H$ is $1/3$. If the errors are uncorrelated with variance $9$, each residual has variance $9(1-1/3)=6$, and each pair has covariance $-9\cdot(1/3)=-3$. The correlation is $-3/6=-1/2$. Independent errors have produced dependent residuals, because the three residuals are forced to sum to zero. Two negative residuals make the third positive more often than independent noise would.

### Properties — Leverage rescales residual variance
The general identity $\operatorname{Var}(e_i\mid X)=\sigma^2(1-h_{ii})$ says that a point with large leverage has a residual that is pulled toward zero. The response helped place the fitted surface, so the gap between the response and the surface understates the gap between the response and the true mean. An error variance of $16$ and a diagonal leverage of $1/8$ give residual variance $16(1-1/8)=14$. Standardising every residual by one common root-mean-square value ignores that factor. A studentised residual divides by a scale that includes $(1-h_{ii})$. The ordinary residual plot does not.

Adding five to every response in the intercept-only example moves the fitted mean from $3$ to $8$ and leaves the residuals $(-2,-1,3)$. An additive shift in the response is absorbed by the intercept. The residual vector is invariant to that shift, and the error vector is not, unless the true mean shifts by the same constant. A response of $15$ with fitted conditional mean $11$ has residual $4$. The error could be $4$ only if the true conditional mean equals the fitted value. In general the true mean differs from the fit, and the error differs from the residual by that amount, $x_i^\top(\widehat\beta-\beta)$, up to sign.

The residual sum of squares in the example estimates $\sigma^2$ through $14/(3-1)=7$. The divisor is the rank of $I-H$, which is $n$ minus the number of fitted independent columns. Using $n$ in the divisor estimates a smaller target than $\sigma^2$ under the model. The moment identities $E(e\mid X)=0$ and $\operatorname{Cov}(e\mid X)=\sigma^2(I-H)$ do not need normal errors. Normality of the errors makes the residual vector normal, with a singular covariance. A test that treats the residuals as $n$ independent normal draws contradicts that singularity.{{cite:nist_model_fit2002}} (§4.4.4, constraints caused by parameter estimation)

## Common misconceptions
A residual of zero means the fitted mean matches the observation. It does not mean the model mean matches the observation, and it does not mean the observation was unimportant. A high-leverage point can have a small residual and a large influence on $\widehat\beta$. Cook's distance and related measures combine the residual with the leverage. Either ingredient alone can miss the point that moves the fit.

A patternless residual plot supports the mean function and the variance function that were plotted. It does not prove independence of the observations. Independence is a property of the sampling mechanism. Two measurements on one person can have residuals that look unstructured in a small sample and still be dependent. Conversely, a curved plot of residuals against a predictor is evidence about the conditional mean, worth examining before any $p$-value attached to a coefficient in the current design is treated as final.{{cite:nist_model_fit2002}} (§4.4.4, graphical residual analysis)

## Connections
The one-way within-group sum of squares is the residual sum of squares for a model whose fitted values are the group means. The hat diagonal $1/n_i$ reproduces the residual variance $\sigma^2(1-1/n_i)$ of a deviation from a group mean. Deviance residuals in a generalised linear model replace the raw residual $y-\widehat\mu$ by a signed contribution to the likelihood-ratio comparison with a saturated fit. They reduce to a scaled version of $y-\widehat y$ in the Gaussian linear model. The distinction between error and residual remains. The deviance residual is still computed from the fitted mean, and the true error still requires the unknown mean.{{cite:dodge2008}} (p. 457, Residual)
