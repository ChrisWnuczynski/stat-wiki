## Motivating example
House prices may vary with floor area, location and age at the same time. A simple plot of price against area mixes those associations because larger houses may also occupy different locations. Multiple linear regression describes a conditional mean using several predictors together. Each coefficient refers to a specified comparison that holds the other design columns fixed. This is a statement about the fitted conditional model and does not, by itself, establish a causal effect.{{cite:openintro2019}} (§9.1, “Introduction to multiple regression”)

A predictor need not be a measured continuous quantity. Indicator variables represent categories, and a product of columns represents an interaction. The model is called linear because its mean is linear in the coefficients, not because every relationship must be a straight line in an untransformed raw measurement.{{cite:dodge2008}} (pp. 364–365)

## Definition — One response and a fixed design matrix
For $n$ responses and a full-column-rank $n\times p$ design matrix $X$, write $Y=X\beta+\varepsilon$ with $E(\varepsilon\mid X)=0$. The vector $\beta$ contains $p$ unknown coefficients, including an intercept when $X$ has a column of ones. Ordinary least squares minimizes $\lVert Y-Xb\rVert^2$. Differentiating gives the normal equations $X^\top X\widehat\beta=X^\top Y$, so
$$\widehat\beta=(X^\top X)^{-1}X^\top Y.$$
Full rank makes the coefficient estimate unique. The fitted vector is the orthogonal projection of $Y$ onto the column space of $X$.{{cite:dodge2008}} (p. 365)

Several assumptions have separate roles. The zero conditional error mean identifies the conditional mean model. Constant conditional variance and uncorrelated errors give the simple covariance formula $\sigma^2(X^\top X)^{-1}$. Gaussian errors provide exact finite-sample normal, t and F sampling laws. Numerical least-squares fitting itself does not require the errors to be Gaussian.{{cite:openintro2019}} (§9.3, “Checking model conditions using graphs”)

## Properties — What the other predictors remove
The normal equations imply $X^\top e=0$ for residuals $e=Y-X\widehat\beta$. With an intercept, the residual sum is zero. Orthogonality is a consequence of the fitting procedure and is not a diagnostic proof that the population errors are independent of the predictors. A misspecified model can satisfy the normal equations exactly.

To interpret a coefficient on one predictor $x$, first remove the linear contribution of all remaining design columns from both $x$ and $Y$. The slope of the residualized response against the residualized predictor equals that coefficient. Indeed, after writing $X=[Z,x]$ and minimizing over the coefficients of $Z$, the objective in the remaining slope is $\lVert M_ZY-bM_Zx\rVert^2$, where $M_Z=I-Z(Z^\top Z)^{-1}Z^\top$. Differentiating gives $\widehat b=x^\top M_ZY/(x^\top M_Zx)$. This derivation explains the meaning of adjustment rather than treating “holding constant” as a verbal rule.{{cite:goodfellow_bengio_courville2016}} (§5.1.4, normal equations and squared-error fitting)

## Worked example — Two orthogonal comparisons
Use four observations with design rows $(1,0,0)$, $(1,1,0)$, $(1,0,1)$ and $(1,1,1)$, and responses $1,3,4,7$. The second and third columns are binary predictors. Solving the normal equations gives intercept $0.75$ and slopes $2.5$ and $3.5$. Fitted responses are $0.75,3.25,4.25,6.75$ and residuals are $0.25,-0.25,-0.25,0.25$. Their squared sum is $0.25$. All three columns are orthogonal to the residual vector, as required. The coefficient calculation uses the matrix fit above.{{cite:dodge2008}} (p. 365)

There are $n-p=1$ residual degrees of freedom, so the unbiased residual variance estimate is $s^2=0.25$. Here the inverse cross-product matrix is
$$ (X^\top X)^{-1}=\begin{pmatrix}3/4&-1/2&-1/2\\-1/2&1&0\\-1/2&0&1\end{pmatrix}.$$
Thus both slope standard errors are $0.5$ under homoscedastic uncorrelated errors. Four responses provide very little residual information; a numerically precise fit is different from precise inference about a wider population.{{cite:dodge2008}} (p. 365)

**Your turn.** Add two to all four responses without changing $X$. What happens to the coefficients and residual sum of squares?

::: {.callout-tip collapse="true" title="Answer"}
The intercept rises from $0.75$ to $2.75$. Both slopes stay at $2.5$ and $3.5$. Every fitted response rises by two, so the residuals and their squared sum $0.25$ stay the same.
:::

## Assumptions and limits — Adjustment can be fragile
If a design column is a linear combination of the others, the coefficients cannot be identified separately. Fitted values can still be uniquely defined as a projection, but an ordinary matrix inverse is unavailable. Nearly dependent columns create a related precision problem: small changes in the responses can produce large changes in individual coefficients, even when fitted values change less.{{cite:goodfellow_bengio_courville2016}} (§5.1.4, discussion of invertibility)

Diagnostics should examine residual patterns, influential observations and whether the conditional mean form is plausible. Independence concerns the observation mechanism, so a residual plot cannot by itself establish it. Extrapolating a fitted linear mean beyond observed predictor combinations also needs scientific justification. With an interaction, the coefficient of one main-effect column describes a comparison at a particular value of the interacting predictor; the comparison changes as that value changes.{{cite:openintro2019}} (§§9.1, 9.3)

A design with two identical columns, or with one column equal to the sum of two others, has no unique coefficient vector, even when the fitted mean vector itself remains unique.
