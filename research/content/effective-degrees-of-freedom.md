## Motivating example

A straight line and a wiggly curve can both be built from ten basis functions, yet the fitted curves need not have the same freedom to follow the observed responses. A penalty suppresses the curved directions by different amounts. Effective degrees of freedom, or edf, summarise the response sensitivity that survives: it counts a fully retained direction as one and a partly suppressed direction as a fraction. This gives a common scale for comparing a smooth with an unpenalised regression fit.{{cite:efron2004_prediction_error}} (§2, equations (2.11)–(2.12))

## Intuition — Flexibility measured by influence

In ordinary least squares, one observation can influence several fitted values, but the sum of its influence on its own fit is the number of independent regression coefficients. A penalised smooth still maps observations to fits; the diagonal elements of this map measure each observation's self-influence. Adding those elements yields an effective parameter count even when no coefficient is simply kept or discarded. A basis dimension limits which shapes are available, whereas edf measures how freely the *fitted* curve uses those shapes after penalisation.{{cite:efron2004_prediction_error}} (§2, projection-matrix comparison)

## Definition

For a fixed linear smoother $\hat{\boldsymbol y}=S_\lambda\boldsymbol y$, define $\operatorname{edf}(\lambda)=\operatorname{tr}(S_\lambda)=\sum_i(S_\lambda)_{ii}$. If the observations have independent errors with common variance $\sigma^2$ and the smoother matrix is fixed independently of their realised values, the same number is $\sum_i\operatorname{Cov}(\hat y_i,Y_i)/\sigma^2$. For a least-squares projection this equals the dimension of the fitted subspace. For a smoother it can be fractional. The residual degrees of freedom used by a GAM summary are $n-\operatorname{tr}(S_\lambda)$ under that summary's convention.{{cite:efron2004_prediction_error}} (§2, equations (2.11)–(2.12)){{cite:wood2025_mgcv_docs}} (“summary.gam,” Details)

## Properties

For a full-rank spline basis $B$ and a positive-semidefinite roughness penalty $\Omega$, the penalised least-squares solution is $\hat{\boldsymbol y}=S_\lambda\boldsymbol y$ with $S_\lambda=B(B^\top B+\lambda\Omega)^{-1}B^\top$. Diagonalising the penalty relative to $B^\top B$ gives $\operatorname{edf}(\lambda)=\sum_{j=1}^K(1+\lambda d_j)^{-1}$, where each $d_j\geq0$. Unpenalised directions have $d_j=0$ and keep one degree each; penalised directions gradually lose influence as $\lambda$ grows. Thus edf falls from $K$ at zero penalty to the dimension of the penalty's null space at infinite penalty. For a cubic-spline second-derivative penalty, that null space comprises constants and straight lines, so the full fit approaches two edf; a centred smooth term reported separately approaches one.{{cite:efron2004_prediction_error}} (§2, linear smoother trace)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Minimising $\|\boldsymbol y-B\beta\|^2+\lambda\beta^\top\Omega\beta$ gives $(B^\top B+\lambda\Omega)\hat\beta=B^\top\boldsymbol y$, hence the stated $S_\lambda$. Put $G=B^\top B$ and $C=G^{-1/2}\Omega G^{-1/2}$. Because $G$ is positive definite and $C$ symmetric positive semidefinite, its eigenvalues $d_j$ are nonnegative. Cyclic invariance of trace gives $\operatorname{tr}(S_\lambda)=\operatorname{tr}[(G+\lambda\Omega)^{-1}G]=\operatorname{tr}[(I+\lambda C)^{-1}]=\sum_j(1+\lambda d_j)^{-1}$. For fixed $S_\lambda$, $\operatorname{Cov}(\hat y_i,Y_i)=\sum_j(S_\lambda)_{ij}\operatorname{Cov}(Y_j,Y_i)=\sigma^2(S_\lambda)_{ii}$ under independent equal-variance errors; summing proves the covariance identity.{{cite:efron2004_prediction_error}} (§2, equations (2.9)–(2.12))
:::
:::

## Worked example

Consider four orthogonal basis directions, two unpenalised and two with penalty eigenvalues $d_3=2$ and $d_4=6$. At $\lambda=1/2$, their response multipliers are $1$, $1$, $1/(1+1)=1/2$, and $1/(1+3)=1/4$. The edf is therefore $1+1+1/2+1/4=2.75$, although the basis contains four directions. If the response has coordinates $(2,1,4,-4)$ in this orthogonal basis, the fitted coordinates are $(2,1,2,-1)$: the last, most heavily penalised direction contributes less. At $\lambda=0$ all four directions remain and edf is $4$; at very large $\lambda$ only the first two remain and edf approaches $2$. The number $2.75$ describes fitted flexibility, not a fractional polynomial degree.{{cite:efron2004_prediction_error}} (§2, linear smoother trace)

**Your turn.** Keep the same four penalty eigenvalues $0,0,2,6$, but set $\lambda=1$. What are the four multipliers and the edf?

::: {.callout-tip collapse="true" title="Answer"}
The multipliers are $1$, $1$, $1/3$, and $1/7$. Their sum is $2+1/3+1/7=52/21\approx2.4762$. More smoothing has reduced the edf from $2.75$ toward the two unpenalised directions.
:::

## Statistical use — Comparing smoothers on one flexibility scale

In a GAM summary, edf near one for an ordinary centred univariate smooth suggests a nearly linear effect on the link scale; a larger value indicates curvature retained after the penalty. It does not test *whether* the effect is present, nor does it directly supply a test for departure from linearity. A latitude smooth with edf $8.881$ is more flexible than a straight slope. A cholesterol smooth with edf $2.011$ is nearly linear, which is a different question from whether an effect is present. Both examples require reading the curve and its uncertainty alongside edf.{{cite:wood2025_mgcv_docs}} (“summary.gam,” Details, term edf and approximate p-values)

The term edf values in a GAM add to the model edf under the software's influence-matrix decomposition. For prediction-error calculations, the covariance definition shows why fitted flexibility costs optimism: a fit that follows its own noisy responses too closely will look better in-sample than on fresh data. Efron's covariance penalty makes this link explicit. {{cite:wood2025_mgcv_docs}} (“summary.gam,” Details){{cite:efron2004_prediction_error}} (§2, equations (2.8)–(2.12))

## Common misconceptions

The basis dimension $K$ is an upper bound on flexibility, not the edf actually used after penalisation. An edf of $2.75$ does not mean the fitted curve is a polynomial of degree $2.75$: a spline is piecewise polynomial and its edf measures sensitivity to data. An edf near one for a centred smooth means an approximately straight fitted contribution, not a one-parameter *whole model*; an intercept and other terms contribute separately. Finally, two fits with the same edf can have different shapes and predictive errors because edf compresses a whole influence matrix into one number.{{cite:efron2004_prediction_error}} (§2, covariance definition)

## Assumptions and limits — When the trace misreads the fit

The trace formula describes a *fixed* linear smoother. If the data also select a knot set, a smoothing parameter, or a model, the complete fitting rule can be nonlinear; the covariance degrees of freedom then need not equal the trace of a matrix computed after selection. For two responses, consider a rule that fits both values separately when their difference exceeds $2$ and otherwise replaces both by their mean. It gives $(0,3)$ two separate fits but pools $(0,1)$ at $(0.5,0.5)$; the abrupt choice is part of the fitting rule, beyond the trace of either selected matrix. Likewise, if a three-column basis contains two identical columns and $\lambda=0$, then $B^\top B$ is singular and the displayed inverse formula is unavailable without a generalised inverse or a different parameterisation. With a full-rank penalty, every direction is penalised and edf can approach zero, so the two-edf limit belongs specifically to a penalty that leaves constants and straight lines free.{{cite:efron2004_prediction_error}} (§2, general covariance degrees of freedom)

## Connections

[Roughness penalties](roughness-penalty.qmd) determine which directions are suppressed. [Sums of smooth functions](sums-of-smooth-functions.qmd) assemble term-wise edf in an additive model. [Cubic smoothing splines](cubic-smoothing-spline.qmd) leave the linear null space unpenalised, while [ridge regression](ridge-regression.qmd) uses the same shrinkage geometry with coefficient penalties. [Cross-validation](cross-validation.qmd) and marginal likelihood can choose smoothing strength; the reported edf then describes the selected fit's influence under the software convention.{{cite:wood2025_mgcv_docs}} (“gam,” Description; “summary.gam,” Details)

## History

Fisher's 1925 work introduced the classical “degree of freedom” language for counting independent deviations left after constraints. Smoothers extended that count: Efron's account relates the trace of a linear fitting rule to the dimension of an ordinary least-squares projection, and then gives a covariance-based definition that also covers nonlinear fitting rules. This extension explains why a penalty can spend a fraction of a degree of freedom on a curved direction.{{cite:dodge2008}} (p. 155, “Degree of Freedom,” History and Mathematical Aspects){{cite:efron2004_prediction_error}} (§2, equations (2.11)–(2.12) and discussion of earlier work)
