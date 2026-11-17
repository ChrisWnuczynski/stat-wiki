## Motivating example
An optimisation routine has returned a coefficient vector, and a second analyst proposes a different value. The least-squares decomposition calculates exactly how much residual sum of squares the proposal adds. It also isolates the quadratic coefficient penalty in a Gaussian likelihood. The identity is deterministic geometry: normal errors become relevant when the same quadratic is interpreted probabilistically.{{cite:prado_ferreira_west2021}} (§1.5.2, pp. 19–20)

## Key results — Orthogonality controls the extra cost
For a response $y\in\mathbb R^n$ and design $X\in\mathbb R^{n\times p}$, let $\widehat\beta$ solve the normal equations $X^\top(y-X\widehat\beta)=0$. Then, for any $\beta$,
$$\|y-X\beta\|^2=\|y-X\widehat\beta\|^2+\|X(\beta-\widehat\beta)\|^2.$$
The residual minimum and the extra cost are both nonnegative. Full column rank makes the coefficient minimiser unique, because $X\delta=0$ then forces $\delta=0$. Without full column rank, every minimiser still gives the same fitted vector and residual minimum, but different coefficient vectors can represent that same fit.{{cite:dodge2008}} (pp. 304–305, Least-Squares Method)

## Proof
Write $r=y-X\widehat\beta$ and $d=\beta-\widehat\beta$. Expanding $\|r-Xd\|^2$ gives $r^\top r-2d^\top X^\top r+d^\top X^\top Xd$. The middle term is zero by the normal equations. This proves the identity. It also proves sufficiency of the normal equations for a global minimum: the remaining difference is a squared norm. Conversely, differentiating the quadratic objective gives $-2X^\top(y-X\beta)$, so every unconstrained minimiser satisfies those equations.{{cite:prado_ferreira_west2021}} (§1.5.2, pp. 19–20)

The geometric interpretation is a right triangle in observation space. The fitted residual is perpendicular to every vector in the column space of $X$, while the change in fitted values $Xd$ lies in that space. Coefficient space acquires the quadratic form $d^\top X^\top Xd$ from this observation-space distance. In the rank-deficient case this is a seminorm, because a nonzero null-space direction can have zero fitted-value cost.

## Statistical use — Separate centre and scale in a Gaussian model
Under $Y\mid\beta,v\sim N(X\beta,vI)$, the likelihood is proportional to $v^{-n/2}\exp[-\|y-X\beta\|^2/(2v)]$. Substituting the decomposition separates it into an SSE factor and a quadratic centred at $\widehat\beta$. With a flat coefficient prior, full column rank and fixed $v>0$, this yields a normal conditional posterior with covariance $v(X^\top X)^{-1}$. Integrating over the coefficients contributes a factor proportional to $v^{p/2}$, which affects the residual degrees of freedom in a variance posterior. The value of the minimum SSE alone is therefore insufficient to reconstruct that marginal posterior; the integration volume also matters.{{cite:prado_ferreira_west2021}} (§1.5.3.1, pp. 21–22)

A proper normal coefficient prior adds a second quadratic penalty. Completing the combined square centres the posterior at a precision-weighted compromise rather than at the OLS estimate. Thus the least-squares identity remains useful in Bayesian calculations even when the posterior centre changes. The likelihood geometry and the prior contribution are distinct terms in the optimisation.{{cite:prado_ferreira_west2021}} (§1.5.3.2, p. 24, eq. 1.23)

## Worked example
### A straight line with three observations
Take $X=\left(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\right)$ and $y=(1,2,2)^\top$. Then $\widehat\beta=(7/6,1/2)^\top$, the residual is $(-1/6,1/3,-1/6)^\top$, and the fitted SSE is $1/6$. Propose $\beta=(1,1)^\top$. Its residual is $(0,0,-1)^\top$, so its SSE is one. The difference $d=(-1/6,1/2)^\top$ gives $Xd=(-1/6,1/3,5/6)^\top$, with squared norm $5/6$. Hence $1=1/6+5/6$, and the cross-product $r^\top Xd$ is zero. This verifies both the scalar identity and the orthogonality that makes it work.

**Your turn.** Increase only the fitted intercept by one, leaving the fitted slope unchanged. How much does SSE increase?

::: {.callout-tip collapse="true" title="Answer"}
The change in fitted values is the all-ones vector of length three. Its squared norm is three, so the candidate SSE is $1/6+3=19/6$.
:::

## Generalizations — Change the inner product when observations have weights
For a symmetric positive-definite weight matrix $W$, minimise $(y-X\beta)^\top W(y-X\beta)$. The normal equations become $X^\top W(y-X\widehat\beta_W)=0$, and the same expansion gives the weighted minimum plus $d^\top X^\top WXd$. This is ordinary orthogonality after transforming the observations by a square root of $W$. A covariance-weighted Gaussian likelihood uses $W$ proportional to the inverse observation covariance; arbitrary weighting changes the fitting criterion and needs its own statistical interpretation.{{cite:dodge2008}} (pp. 219–220, generalised regression with known error covariance)

## Related concepts — Extra cost is a length in the column space

The residual at a least-squares coefficient is orthogonal to every column of the design. Another coefficient differs by a vector $d$, and the change in the fitted vector is $Xd$, which lies in the column space. The cross term between an orthogonal residual and a column-space vector vanishes, so the increase in residual sum of squares is exactly the squared length of $Xd$. If that length is zero, the fitted vector does not move and the residual sum of squares does not change, even though the numerical coefficient did. Full column rank is what turns a unique fitted vector into a unique coefficient. [Ordinary least squares](ordinary-least-squares.qmd) is this minimisation. [Least squares estimators are unbiased](least-squares-estimators-are-unbiased.qmd) adds a probability model with mean-zero errors. The geometric identity does not need that model. [Sampling distribution of the OLS estimator](sampling-distribution-of-the-ols-estimator.qmd) describes the coefficient when the response is redrawn.

A spherical Gaussian likelihood puts the residual sum of squares in the exponent. The decomposition splits that exponent into the minimum, which depends on the response only through the residual, and a quadratic penalty for leaving the least-squares coefficient. A known positive-definite weight matrix replaces ordinary length by $(y-X\beta)^\top W(y-X\beta)$. The same expansion holds in that inner product, and the normal equations become $X^\top W(y-X\widehat\beta)=0$. Estimating the weights from the same residuals is a different algorithm from treating $W$ as known.{{cite:prado_ferreira_west2021}} (§1.5.2, pp. 19–20){{cite:dodge2008}} (pp. 219–220, generalised regression with known error covariance)
