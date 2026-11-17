## Motivating example
A diagnostic study measures many genes on each patient but has far fewer patients than candidate coefficients. An unrestricted logistic fit can be unstable or separated. The logistic lasso charges for coefficient magnitude while fitting binary outcomes, allowing some coefficients to be exactly zero. Prediction, gene prioritization and causal explanation remain different goals even when the same fitted vector is useful for all three discussions.{{cite:holmes_huber2019_msmb}} (§12.6.1, Penalization)

## Definition — Binary likelihood with an absolute penalty
For independent responses $y_i\in\{0,1\}$, let $\eta_i=\beta_0+x_i^\top\beta$ and $p_i=(1+e^{-\eta_i})^{-1}$. One common normalization minimizes
$$F(\beta_0,\beta)=\frac1n\sum_i\{\log(1+e^{\eta_i})-y_i\eta_i\}+\lambda\sum_j|\beta_j|,$$
where $\lambda\ge0$ and the intercept is unpenalized. The first term is average negative binomial log-likelihood, apart from constants. Reporting the normalization matters: multiplying the likelihood term by $n$ also requires multiplying the penalty by $n$ to obtain the same fit.{{cite:friedman_glmnet2010}} (§3, Logistic Regression)

## Properties — Why zero coefficients are possible
Write $g_j=n^{-1}\sum_i x_{ij}(p_i-y_i)$ for the derivative of the smooth loss. The optimality conditions are
$$g_j=-\lambda\operatorname{sign}(\beta_j)\quad(\beta_j\ne0),\qquad |g_j|\le\lambda\quad(\beta_j=0).$$
At zero, the absolute value has every subgradient in $[-1,1]$; a range of likelihood gradients can therefore be balanced without moving the coefficient away from zero. The intercept condition is $\sum_i(p_i-y_i)=0$ at a finite optimum. The Hessian of the smooth term is $X^\top W X/n$, with diagonal weights $p_i(1-p_i)\ge0$, proving convexity. The absolute penalty is also convex, so these conditions characterize global minima. Coefficients may be nonunique with dependent columns even when fitted linear predictors are unique.{{cite:friedman_glmnet2010}} (§3, quadratic approximation and coordinate descent)

With both outcome classes present, the intercept-only optimum is $\beta_0=\operatorname{logit}(\overline y)$. At that fit, all slopes can stay zero whenever
$$\lambda\ge\lambda_{\max}=\max_j\left|n^{-1}\sum_i x_{ij}(y_i-\overline y)\right|.$$
This follows immediately from the zero-coordinate conditions. A coefficient's size depends on predictor units, so standardization and the intercept convention belong in any reproducible specification.{{cite:friedman_glmnet2010}} (§§2–3, standardization and regularization paths)

## Worked example — A complete one-predictor path
Take two observations $(x,y)=(-1,0),(1,1)$. Symmetry gives intercept zero. For a nonnegative slope $\beta$, the objective is $\log(1+e^{-\beta})+\lambda\beta$. Its derivative is $-1/(1+e^\beta)+\lambda$. Thus the solution is zero when $\lambda\ge1/2$ and $\widehat\beta=\log\{(1-\lambda)/\lambda\}$ for $0<\lambda<1/2$. At $\lambda=1/4$, $\widehat\beta=\log3\approx1.098612$ and the fitted probabilities are $1/4$ and $3/4$. At $\lambda=0$, the likelihood supremum is approached as the slope tends to infinity, illustrating separation and the stabilizing effect of a positive penalty.

**Your turn.** Use the two-observation example with $\lambda=0.1$. Find the slope and probabilities, then compare with $\lambda=0.6$.

::: {.callout-tip collapse="true" title="Answer"}
The slope is $\log9\approx2.197225$ and the probabilities are $0.1,0.9$. At $\lambda=0.6$, the slope is zero and both probabilities are $1/2$.
:::

## Statistical use — Selection is part of the fitting procedure
Cross-validation chooses a penalty for a specified prediction objective, such as binomial deviance. Feature filtering and standardization must be learned within each training split. If many penalty values or methods are compared, a separate test sample or nested validation is needed for an honest final assessment. A selected coefficient is evidence that the variable helps that fitted predictor under those choices; a zero does not establish absence of a biological association, especially when genes are strongly correlated.{{cite:holmes_huber2019_msmb}} (§§12.4, 12.6.2)

The fourteen-gene coefficient table describes one specified high-dimensional fit. Its counts, overlaps and coefficient comparisons can be checked directly; reproducing its selected penalty requires the exact preprocessing, folds and tuning choices. Those details determine which of correlated genes enters. Fitting principal components instead changes the scientific target from individual gene coefficients to combinations of genes.{{cite:friedman_glmnet2010}} (§2, correlated predictors){{cite:holmes_huber2019_msmb}} (§12.6.1)
