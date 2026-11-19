## Motivating example — Residuals that all pull the same way

In a binary-response model, an estimated probability can be too low for the observed successes and too high for the observed failures. The score combines those mismatches into a direction in which the log-likelihood initially rises. At a finite interior maximum, the competing contributions balance and the score is zero. This makes the score the working quantity behind maximum-likelihood estimation, while its variability describes how much information repeated data carry about the parameter.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1, pp. 371–373)

## Intuition — The slope of the log-likelihood

The likelihood grades a candidate parameter by the probability or density it assigns to the observed sample. Differentiating its logarithm asks how rapidly that grade changes for a small parameter move. A positive one-dimensional score favors an increase *locally*; a negative score favors a decrease. For a vector parameter, the score is a gradient and its components depend on how the model is parameterized. In a canonical-link GLM, each observation contributes a covariate vector multiplied by an observed-minus-fitted response. The logistic and Poisson score formulas illustrate that pattern.{{cite:nelder_wedderburn1972}} (§2.1, pp. 372–373, score equations)

## Definition — U = ∂ℓ/∂θ, and a zero at an interior maximum

For a differentiable log-likelihood $\ell(\theta;x)$, the score is $U(\theta;x)=\partial\ell(\theta;x)/\partial\theta$, or the gradient $\nabla_\theta\ell$ for a parameter vector. The observed data $x$ are held fixed in this derivative. A finite interior maximum of a smooth likelihood is a stationary point, so it satisfies $U(\hat\theta;x)=0$; the converse needs information about the likelihood's shape. A boundary maximum or a supremum reached only as coefficients diverge need not provide a finite score root.{{cite:nelder_wedderburn1972}} (§2.1, pp. 372–373){{cite:albert_anderson1984}} (§§1–2, pp. 1–3, existence of logistic estimates)

Evaluating $U(\theta;X)$ at the true parameter makes it a random variable across repeated samples. Under fixed-support differentiation and integrability conditions, $\operatorname E_\theta U=0$ and its covariance matrix is the Fisher information. The *observed* score for one sample is not generally zero at the true parameter. The observed information $-\nabla^2\ell(\theta;x)$ also differs from its expectation in general; their expectation agrees with the score covariance under the regularity conditions. {{cite:nelder_wedderburn1972}} (§1.1, equations 1–6, p. 371)

## Properties — Additivity, reparameterisation, and the logistic Hessian

Independent observations give additive log-likelihoods and hence additive scores. A reparameterization changes the score by the chain rule: if $\theta=h(\psi)$, then $U_\psi=(dh/d\psi)U_\theta$ in the scalar case. The zero-score property survives a smooth one-to-one change, but the numerical value and units of the score do not. Thus scores from differently parameterized models should not be compared by their raw magnitudes.{{cite:nelder_wedderburn1972}} (§§1.1–2.1, pp. 371–373)

For logistic regression with fixed design matrix $X$ and fitted probabilities $p$, the score $X^\top(y-p)$ asks whether response residuals still align with any model column. The Hessian $-X^\top W X$, with positive diagonal weights at finite coefficients, is negative semidefinite. Full column rank makes it negative definite, so a finite score root is the unique global maximum. The conclusion presupposes that the root exists: complete or quasi-complete separation can send coefficients to infinity. {{cite:nelder_wedderburn1972}} (§2.1, pp. 372–373){{cite:albert_anderson1984}} (§§2–4, pp. 2–7)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a density $f(x;\theta)$ on fixed support, suppose derivatives may pass through integration. Since $\int f(x;\theta)\,dx=1$ and $U=\partial_\theta\log f=(\partial_\theta f)/f$, we have $\operatorname E_\theta U=\int\partial_\theta f\,dx=0$. Differentiating this identity once more gives $0=\operatorname E_\theta(\partial_\theta U+U^2)$, hence $\operatorname{Var}_\theta(U)=\operatorname E_\theta U^2=-\operatorname E_\theta\partial_\theta^2\ell$. The vector result replaces the square by $UU^\top$ and the second derivative by a Hessian. Independence makes both log-likelihood and score sums.{{cite:nelder_wedderburn1972}} (§1.1, equations 1–6, p. 371)

For Bernoulli responses with $p_i=\{1+\exp(-x_i^\top\beta)\}^{-1}$, differentiating $\ell=\sum_i\{y_i x_i^\top\beta-\log(1+\exp(x_i^\top\beta))\}$ gives $U=X^\top(y-p)$ and $H=-X^\top W X$. For any vector $v$, $v^\top Hv=-\sum_i p_i(1-p_i)(x_i^\top v)^2\leq0$; it is strictly negative for nonzero $v$ when $X$ has full column rank. Concavity then makes every finite stationary point globally maximal and, under full rank, unique. This argument does not establish existence of a finite point, as separation demonstrates. {{cite:nelder_wedderburn1972}} (§2.1, pp. 372–373){{cite:albert_anderson1984}} (§§2–4, pp. 2–7)
:::
:::

## Statistical use — Estimation and diagnostics

Numerical maximizers use the score together with observed or expected curvature to choose parameter updates. Fisher scoring replaces the observed Hessian by expected information; for canonical-link GLMs this leads to the iteratively reweighted least-squares equations. A small computed score at a reported optimum is one convergence check, but it does not certify that the maximum exists, that the Hessian is well conditioned, or that the sampling model fits. Complete separation in a logistic sample is a reason to inspect coefficient size and data configuration as well as a numerical stopping message.{{cite:nelder_wedderburn1972}} (§2.1, pp. 372–374){{cite:albert_anderson1984}} (§§1–4, pp. 1–7)

The score also underlies score tests: evaluate it at a null-constrained estimate and scale it by information to assess whether a permitted parameter direction would improve the fit. This uses the sampling distribution under the null, so a large observed derivative has meaning only after it is put on an information scale. An information matrix with a nearly zero eigenvalue warns that some parameter combination is weakly identified. {{cite:nelder_wedderburn1972}} (§§1.1, 2.1, pp. 371–373)

## Worked example — One Newton step in an intercept-only logit

Consider an intercept-only logistic model for three independent Bernoulli outcomes $y=(1,0,1)$. At coefficient $\beta=0$ the fitted success probability is $p=1/2$, so the score is $U(0)=2-3/2=0.5$ and the Hessian is $H(0)=-3(1/2)(1/2)=-0.75$. One Newton step is $\beta_{\mathrm{new}}=0-U(0)/H(0)=2/3\approx0.6667$. The exact likelihood maximum is at $\hat p=2/3$, or $\hat\beta=\log(2)\approx0.6931$, where the score is zero. The first step moves toward the maximum but does not reach it exactly; at $2/3$ on the coefficient scale, the score remains about $0.0177$.{{cite:nelder_wedderburn1972}} (§2.1, pp. 372–373, likelihood equations)

**Your turn.** With an intercept-only logistic model and four outcomes $y=(1,0,0,0)$, calculate the score and Hessian at $\beta=0$, take one Newton step, and find the exact maximum-likelihood coefficient.

::: {.callout-tip collapse="true" title="Answer"}
At $p=1/2$, $U(0)=1-4(1/2)=-1$ and $H(0)=-4(1/2)(1/2)=-1$. The Newton step is $\beta_{\mathrm{new}}=0-(-1)/(-1)=-1$. The observed success fraction is $1/4$, so the exact coefficient is $\log\{(1/4)/(3/4)\}=\log(1/3)\approx-1.0986$. The first step is close, but the fitted probability at $\beta=-1$ is not exactly $1/4$.
:::

## Common misconceptions — A zero expected score is not a zero observed score

The score is not a goodness-of-fit score on a fixed scale: it is a derivative and changes under reparameterization. Mean-zero score is an expectation under repeated sampling at the model parameter, not a statement that every observed sample has score zero there. Setting the score to zero finds candidates for an interior maximum, not automatically an existing or unique MLE. Equality of score variance and expected curvature also requires regularity; it is not a generic identity for every moving-support model.{{cite:nelder_wedderburn1972}} (§1.1, p. 371){{cite:albert_anderson1984}} (§§1–4, pp. 1–7)

## Assumptions and limits — Moving support, separation, and rank

For one $X\sim\operatorname{Uniform}(0,\theta)$, differentiating the log density at an interior observed $x$ gives $U(\theta;x)=-1/\theta$, whose expectation is not zero; the support boundary moves with $\theta$ and supplies a missing boundary contribution. For a completely separated logistic sample, the finite-coefficient Hessian remains negative semidefinite but the likelihood may only approach its supremum as coefficients diverge. If two design columns are identical, $X^\top W X$ is singular and a unique coefficient estimate cannot be recovered even if fitted probabilities are identifiable. Each example breaks a different premise behind a routine score calculation.{{cite:nelder_wedderburn1972}} (§1.1, differentiation conditions, p. 371){{cite:albert_anderson1984}} (§§2–4, pp. 2–7)

## Connections — Likelihood, information, and Fisher scoring

[Maximum likelihood](maximum-likelihood.qmd) looks for a point at which the derivative of the [likelihood](likelihood-function.qmd) is zero. That root is an interior candidate, not a proof that a finite maximum exists. Under the regularity conditions, [Fisher information](fisher-information.qmd) is the variance of this derivative, and [Fisher scoring](fisher-scoring.qmd) uses the expected curvature rather than the observed Hessian. [Complete separation](complete-separation.qmd) is a logistic sample in which the likelihood keeps increasing as a coefficient tends to infinity, so no finite root is the maximum.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1, pp. 371–373){{cite:albert_anderson1984}} (§§2–4, pp. 2–7)

## History — Score equations, then separation

R. A. Fisher's 1922 paper is the reference for this derivative of the log-likelihood.{{cite:fisher1922}} (pp. 324, 328–329) Dodge's 2008 encyclopedia entry lists Fisher's 1922 and 1925 papers.{{cite:dodge2008}} (p. 203, Fisher entry) Nelder and Wedderburn's 1972 paper made the GLM score equations the basis of one iterative fit across response families.{{cite:nelder_wedderburn1972}} (§2.1, pp. 372–374) Albert and Anderson's 1984 study showed how separation in logistic data can prevent the finite maximum that solving $U=0$ would otherwise be taken to provide.{{cite:albert_anderson1984}} (§§1–4, pp. 1–7)
