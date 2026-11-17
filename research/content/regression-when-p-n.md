## Motivating example
A study can measure thousands of gene-expression variables on a few dozen people. Fitting a coefficient for every variable creates more unknowns than observed responses. The difficulty is already visible in a tiny system with two observations and three coefficients: several distinct coefficient vectors can produce the same predictions on the observed rows. A calculation that returns a fitted vector has not necessarily identified individual effects.{{cite:zhang_d2l2023}} (section “Linear Regression”, “Analytic Solution”)

## Definition — Count coefficients, then inspect rank
Use $d$ for the total number of columns of $X$, including an intercept if present. Then $\operatorname{rank}(X)\le\min(n,d)$. If $d>n$, the null space has positive dimension, so $X^TX$ is singular. The normal equations $X^TX\hat\beta=X^Ty$ still characterise least-squares minima, but the expression using an ordinary inverse is unavailable. Even when $d\le n$, duplicated or linearly dependent columns can cause the same singularity.{{cite:zhang_d2l2023}} (section “Linear Regression”, “Analytic Solution”)

An intercept changes the count by one: $p$ measured predictors normally give $d=p+1$. More predictors than observations is a sufficient obstruction to full column rank, not a complete description of the geometry. Exact interpolation requires $y\in\operatorname{col}(X)$; all possible response vectors can be interpolated precisely when $X$ has full row rank.

## Properties — Fitted values and coefficient ambiguity
Let $\hat y$ be the orthogonal projection of $y$ onto $\operatorname{col}(X)$. Every least-squares minimiser satisfies $X\hat\beta=\hat y$. Indeed, write $y-X\beta=(y-\hat y)+(\hat y-X\beta)$; the two terms are orthogonal, so their squared norms add. The first is fixed and the second is minimised at zero. Thus fitted values are unique, while all coefficient solutions are $\hat\beta+v$ with $v\in\ker X$.

A new prediction $x_*^T\beta$ is unique across those solutions exactly when $x_*^Tv=0$ for every $v\in\ker X$, equivalently when $x_*$ lies in the row space of $X$. Uniqueness on the training rows therefore does not guarantee uniqueness away from them. This distinction is central when interpreting a large collection of coefficients as separately measured effects.

## Statistical use — What a ridge penalty supplies
Ridge regression minimises $\|y-X\beta\|^2+\lambda\|\beta\|^2$, with $\lambda>0$. Its unique solution is
$$\hat\beta_\lambda=(X^TX+\lambda I)^{-1}X^Ty.$$
For every nonzero vector $v$, $v^T(X^TX+\lambda I)v=\|Xv\|^2+\lambda\|v\|^2>0$, which proves invertibility. The penalty resolves ambiguity by adding a preference for small coefficients; the observations alone have not provided new equations.{{cite:dodge2008}} (pp. 458–459, “Ridge Regression”){{cite:zhang_d2l2023}} (section “Weight Decay”, “Norms and Weight Decay”)

In usual regression practice the intercept is separated and left unpenalised after centring the response and predictors. Penalising all coefficients, as in the displayed formula, is a specific convention. Column scaling also matters: changing the units of a predictor changes the meaning of the same quadratic coefficient penalty. Choose preprocessing and the tuning parameter using training and validation data, and assess prediction on data that did not select those choices.{{cite:zhang_d2l2023}} (section “Weight Decay”, regularisation constant and validation)

## Worked example — Interpolation without identified effects
Take
$$X=\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix},\qquad y=\binom12.$$
Every vector $\beta=(1-t,2-t,t)^T$ interpolates both observations. Its squared norm is $(1-t)^2+(2-t)^2+t^2=3(t-1)^2+2$, minimised at $t=1$. The minimum-norm solution is therefore $(0,1,1)^T$.

At the new row $x_*=(1,1,0)^T$, prediction is $3-2t$, which changes with the arbitrary coefficient representation. At row $(1,1,2)^T$, prediction is always $3$, because that row is the sum of the two training rows. The difference is exactly the row-space condition above.

With $\lambda=1$, the ridge solution is $(0.125,0.625,0.75)^T$, giving fitted values $(0.875,1.375)^T$ and residual sum of squares $0.40625$. Positive regularisation sacrifices interpolation in exchange for a unique penalised solution.{{cite:dodge2008}} (p. 459, ridge normal equations)

**Your turn.** A design matrix has two identical columns $u,u$. Show which combination of their coefficients is estimable. If their fitted sum is $6$, which pair minimises their squared norm?

::: {.callout-tip collapse="true" title="Answer"}
The contribution is $u(\beta_1+\beta_2)$, so only the sum is identified from these columns. Given sum $6$, write the pair as $3+a,3-a$; the squared norm is $18+2a^2$, minimised at $(3,3)$.
:::

## Assumptions and limits
A unique penalised estimate does not make unpenalised standard errors or classical coefficient tests valid. With exact interpolation the residual sum of squares can vanish while prediction error remains substantial. Validation must include the entire feature-selection and tuning process. High dimensionality also makes scientific interpretation depend heavily on structural assumptions such as sparsity, smoothness or small coefficient norm. Those assumptions should be stated with the model rather than hidden behind a successful numerical solve.
