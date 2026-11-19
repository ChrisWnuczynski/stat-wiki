## Lead context
Each update is a weighted least-squares step that uses the expected curvature of the log-likelihood, and the step is repeated at the new coefficient vector.{{cite:nelder_wedderburn1972}} (Summary; §§1.1–2.2, pp. 370–374)

## Motivating example — The first step can overshoot the Poisson fit
A Poisson log-linear model for counts $1$ and $3$ at inputs $0$ and $1$ has a perfect fit: the means should be $1$ and $3$, so the slope on the log scale is $\log 3\approx 1.0986$ and the intercept is $0$. Starting at the zero vector, every mean is $1$. One scoring step does not land on $\log 3$. It lands on a slope of $2$, and the second count's fitted mean jumps to $e^{2}\approx 7.3891$, past the observed $3$. The algorithm is a sequence of linear steps, not a closed form.{{cite:nelder_wedderburn1972}} (Summary; §§1.1–2.2, pp. 370–374)

## Intuition — Freeze the weights, solve a linear equation, then repeat
The score equation sets a weighted sum of residuals to zero. The weights depend on the mean, and the mean depends on the coefficients, so the equation is not linear. Fix the weights and the current mean, replace the mean by its tangent in the coefficients, and the score equation becomes a linear equation for the step. That linear equation is weighted least squares. Recompute the weights at the new coefficients and repeat. R's `glm.fit` is this iteration: the returned `iter` is the number of steps, and the returned `weights` are the working weights from the last step.{{cite:rstats_glm2026}} (§ Details and Value, IWLS, `iter` and working weights)

## Definition — Expected-information update for β
For a GLM the log-likelihood score for the coefficient vector $\boldsymbol{\beta}$ has the form

$$
\mathbf{U}(\boldsymbol{\beta})=\sum_{i=1}^n\frac{y_i-\mu_i}{V_i}\,\mu'_i\,\mathbf{x}_i,
$$


where $\mu_i$ is the mean, $V_i$ its variance under the family, $\mu'_i$ the derivative of the mean with respect to the linear predictor, and $\mathbf{x}_i$ the covariate row. Fisher scoring replaces the observed Hessian by its expectation. For the Poisson log link, $V_i=\mu_i$ and $\mu'_i=\mu_i$, so the weight simplifies to $\mu_i$ and

$$
\mathbf{U}(\boldsymbol{\beta})=\mathbf{X}^\top(\mathbf{y}-\boldsymbol{\mu}),\qquad
\mathcal{I}(\boldsymbol{\beta})=\mathbf{X}^\top\mathrm{diag}(\boldsymbol{\mu})\,\mathbf{X}.
$$


The update is $\boldsymbol{\beta}^{(1)}=\boldsymbol{\beta}^{(0)}+\mathcal{I}(\boldsymbol{\beta}^{(0)})^{-1}\mathbf{U}(\boldsymbol{\beta}^{(0)})$. For this link the matrix $\mathcal{I}$ does not depend on $\mathbf{y}$ except through $\boldsymbol{\mu}$, and the observed Hessian equals $-\mathcal{I}$, so Newton–Raphson and Fisher scoring take the same step.{{cite:nelder_wedderburn1972}} (Summary; §§1.1–2.2, pp. 370–374)

## Interpretation — A tangent step is not the MLE
A single step linearises the mean at the current fit. If the current mean is far from the observations, the tangent can overshoot, as the jump from fitted mean $1$ to $7.3891$ does when the observation is $3$. Later steps pull the mean back. Convergence is a property of the sequence, reported by `glm` as the logical `converged`, not a property of the first arithmetic step. A model outside the exponential family does not hand the same weights to this update; `glm.fit` is written for a `family` object that supplies the variance and the link.{{cite:rstats_glm2026}} (§ Arguments, `family`; Value, `converged`)

## Properties — Working weights, working response, and a perfect fit
For the Poisson log link the working weight of observation $i$ is the current mean $\mu_i$. The working response that turns the step into least squares is the linearised target $z_i=\eta_i+(y_i-\mu_i)/\mu_i$. Weighted least squares of $z_i$ on $\mathbf{x}_i$ with weights $\mu_i$ is the same linear system as the scoring update. R stores those weights from the final iteration. They are not prior weights: prior weights scale the contribution of a row before the mean-dependent weight is applied.

At a perfect fit, $y_i=\mu_i$ for every $i$, the score is zero and the update stays put. For two Poisson means and two coefficients the perfect fit exists and is the interpolating log-means. With more observations than coefficients the score can be zero without every residual being zero.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $Y\sim\mathrm{Poisson}(\mu)$ and $\eta=\log\mu$, the log-likelihood contribution is $y\eta-e^{\eta}$, up to a term free of $\eta$. Its derivative in $\eta$ is $y-e^{\eta}=y-\mu$, and the chain rule through $\boldsymbol{\beta}$ multiplies by $\mathbf{x}$. Summing gives $\mathbf{U}=\mathbf{X}^\top(\mathbf{y}-\boldsymbol{\mu})$. The second derivative of the contribution in $\eta$ is $-e^{\eta}=-\mu$, which does not involve $y$. The expected negative Hessian in $\boldsymbol{\beta}$ is therefore $\mathbf{X}^\top\mathrm{diag}(\boldsymbol{\mu})\mathbf{X}$, and it equals the observed negative Hessian. The Newton step and the Fisher-scoring step coincide.{{cite:nelder_wedderburn1972}} (Summary; §§1.1–2.2, pp. 370–374)

With rows $(1,0)$ and $(1,1)$, start at $\boldsymbol{\beta}=\mathbf{0}$, so $\boldsymbol{\mu}=(1,1)$ and $\mathbf{y}-\boldsymbol{\mu}=(0,2)$. Then $\mathbf{U}=(2,2)$ and $\mathcal{I}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$, with inverse $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$. The step is $(0,2)$. The new slope is $2$ and the new means are $1$ and $e^{2}$. One further step uses $\mathcal{I}=\bigl(\begin{smallmatrix}1+e^{2}&e^{2}\\ e^{2}&e^{2}\end{smallmatrix}\bigr)$ and moves the slope from $2$ to $1+3e^{-2}\approx 1.4060$.{{cite:nelder_wedderburn1972}} (Summary; §§1.1–2.2, pp. 370–374)
:::
:::

## Statistical use — Reading an iteration, not a closed form
Report the converged coefficients, and treat `iter` as a record of how many weighted least-squares steps were taken. A large `iter` means the linearisations had far to travel or the weights were changing sharply. It is not a measure of evidence about a coefficient. The standard errors come from the inverse of the final information matrix, not from the number of steps. For a binomial or Poisson model the dispersion used in that matrix is fixed at one; a Gaussian model estimates a dispersion as well.

## Worked example — Two Poisson counts, two scoring steps
Counts $y=(1,3)$ at $x=(0,1)$, Poisson log link, start $(0,0)$.

Step 1. Means $(1,1)$. The update derived above adds $(0,2)$. The slope is $2$ and the fitted means are $1$ and $e^{2}\approx 7.3891$. The second fitted mean is larger than the count $3$.

Step 2. The slope becomes $1+3e^{-2}\approx 1.4060$. The fitted means are $1$ and $e^{1.4060}\approx 4.0796$. The second mean has moved from $7.3891$ toward $3$ and has not arrived.

The interpolating solution is intercept $0$ and slope $\log 3\approx 1.0986$, with means $1$ and $3$. The score is then zero. Two scoring steps have not reached it: $1.4060$ is still above $1.0986$, and $4.0796$ is still above $3$.{{cite:nelder_wedderburn1972}} (Summary; §§1.1–2.2, pp. 370–374)

**Your turn.** At the interpolating slope $\log 3$, what is the second fitted mean, and what is the Poisson score contribution $y-\mu$ of that observation?

::: {.callout-tip collapse="true" title="Answer"}
The second mean is $e^{\log 3}=3$, so $y-\mu=3-3=0$. The first observation already has $y-\mu=0$. The score vector is zero and the update stops.
:::

## Common misconceptions — The first step is not the estimate, and working weights are not prior weights
The first scoring step is not the maximum-likelihood estimate. Here it produced slope $2$ against the likelihood solution $\log 3\approx 1.0986$. Stopping after one step leaves a fitted mean of $7.3891$ where the observation is $3$.{{cite:nelder_wedderburn1972}} (Summary; §§1.1–2.2, pp. 370–374)

Fisher scoring is not ordinary least squares of $y$ on $x$. The response in the weighted regression is the working target $z$, rebuilt each step, and the weights are the current means. Regressing the raw counts on $x$ once does not enforce a positive mean and does not solve the Poisson score.{{cite:nelder_wedderburn1972}} (Summary; §§1.1–2.2, pp. 370–374)

The working weights are not prior weights. Prior weights are supplied in the call. Working weights are computed from the current mean and stored after the last iteration.

## Assumptions and limits — When the step is the wrong curvature
The coincidence of Newton and Fisher scoring used $V=\mu$ and $\mu'=\mu$, which is the Poisson log link. A different variance function makes the expected Hessian and the observed Hessian different matrices, and the two algorithms take different steps. A zero or negative mean cannot occur under the log link while the coefficients stay finite, but a starting value that makes a weight zero, or a design matrix that is not full rank, makes $\mathcal{I}$ singular. R treats a singular fit as an error when `singular.ok` is false. The iteration also assumes independent rows given the covariates. Dependent counts share information the working weights do not represent.

## Connections — Score, information, and IRLS
Each step inverts the expected [Fisher information](fisher-information.qmd) applied to the [score](score-function.qmd), with the weights held fixed only for that linear solve; recomputing the weights and solving again is [iteratively reweighted least squares](iteratively-reweighted-least-squares.qmd).

## Check yourself

1. For the Poisson log link, the working response is $z_i=\eta_i+(y_i-\mu_i)/\mu_i$. If observation $i$ is already fitted exactly, what is $z_i$?

::: {.callout-tip collapse="true" title="Answer"}
The correction $(y_i-\mu_i)/\mu_i$ is zero when $y_i=\mu_i$, so $z_i=\eta_i$. The working target is the current linear predictor, and that observation adds nothing to the step.
:::

2. Three Poisson counts $1,2,3$ share one intercept and a log link, and the common mean is set to $2$. What is the score, and is every residual zero?

::: {.callout-tip collapse="true" title="Answer"}
For an intercept, each row of the design is $1$, so the score is the sum of the residuals $(1-2)+(2-2)+(3-2)=0$. The residuals are $-1$, $0$ and $1$. A zero score does not require every residual to vanish when there are more observations than coefficients.
:::

## History — Iteratively reweighted least squares
`glm.fit` carries out the coefficient update by iteratively reweighted least squares. The design was inspired by the S function described by Hastie and Pregibon, and the references include McCullagh and Nelder's book on generalised linear models. The iteration count, the working weights and the convergence flag are part of the fitted object.{{cite:rstats_glm2026}} (§ Details and References; Value, IWLS, `iter` and working weights) The expected-information step is the GLM update.{{cite:nelder_wedderburn1972}} (Summary; §§1.1–2.2, pp. 370–374) In the two-count example that step can be calculated directly: the slope is $0$, then $2$, then about $1.4060$, moving toward $\log 3\approx 1.0986$ without equalling it after two steps.
