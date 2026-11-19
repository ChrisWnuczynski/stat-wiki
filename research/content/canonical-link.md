## Motivating example — The Poisson log link matches y log μ in the likelihood
In a study of counts, a Poisson mean must be positive although a linear predictor $\eta_i=x_i^\top\beta$ can be any real number. The log link makes $\mu_i=e^{\eta_i}$ positive automatically. It is also the canonical link: the Poisson log-likelihood contains $y_i\log\mu_i$, so the coefficient of the observed count is exactly $\eta_i$. This alignment simplifies the score and information calculations. For binary outcomes the corresponding alignment uses log odds, rather than the probability itself, as the linear predictor.{{cite:nelder_wedderburn1972}} (§§1.1–1.3, 3.2–3.3, pp. 371–373, 378–380)

## Intuition — The predictor is set equal to the natural parameter
A generalised linear model has a sampling distribution for $Y_i$, a linear predictor, and a link connecting the conditional mean to that predictor. Exponential-family distributions already have a parameter that multiplies the observed response in the log-likelihood. A canonical link chooses the linear predictor to be that parameter. It does not transform each observed $Y_i$ into a straight line, and it does not assert that the mean itself is linear. The choice is mathematically convenient because differentiating the log-likelihood then leaves the simple residual $y_i-\mu_i$ multiplied by a covariate.{{cite:nelder_wedderburn1972}} (§§1.1–1.3, 2.2, pp. 371–374)

## Definition — g(μ) = θ, for the family's natural parameter θ
In the regular one-parameter exponential-family form

$$f(y_i\mid\theta_i,\phi)=\exp\!\left\{\frac{y_i\theta_i-A(\theta_i)}{a(\phi)}+c(y_i,\phi)\right\},$$

$\theta_i$ is the natural parameter and $\mu_i=A'(\theta_i)$. A link $g$ is **canonical** when $g(\mu_i)=\theta_i=\eta_i=x_i^\top\beta$.{{cite:mccullagh_nelder1989}} (§2.2.4, p. 32) With the natural-parameter convention fixed, the identity link is canonical for a normal mean, the log link for a Poisson mean, and the logit link for a Bernoulli probability. For a gamma mean the natural parameter is $-1/\mu$ in the common shape-scale exponential-family expression; a positive inverse link differs by a sign convention, and its predictor must still stay in the valid domain.{{cite:nelder_wedderburn1972}} (§§1.1–1.3, 3.1–3.4, pp. 371–372, 377–380)

## Properties — Score Xᵀ(y−μ), and observed Hessian equals expected
At fixed dispersion and design matrix $X$, a canonical-link model has score $U(\beta)=X^\top(y-\mu)/a(\phi)$.{{cite:mccullagh_nelder1989}} (§2.5.1, pp. 41–43, eq. 2.13; $W=V$ on p. 43) Its observed negative Hessian $X^\top\operatorname{diag}\{A''(\eta_i)\}X/a(\phi)$ contains no observed $y_i$, so it equals its own expectation, and Fisher scoring takes the same step as Newton–Raphson.{{cite:mccullagh_nelder1989}} (§2.5.1, p. 43) The likelihood depends on the observations through $X^\top y$ and the base factors, so $X^\top y$ is sufficient for $\beta$ when the dispersion and design are fixed.{{cite:mccullagh_nelder1989}} (§2.2.4, p. 32){{cite:geyer2022_exp_family}} (§9.3.4) These conveniences do not guarantee a unique finite estimate: the design may be rank deficient or a binary sample may be completely separated.{{cite:nelder_wedderburn1972}} (§2.2, eqs. 10–11, p. 374)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Under the stated canonical link, $\theta_i=\eta_i=x_i^\top\beta$, so the joint log-likelihood is $\ell(\beta)=\{y^\top X\beta-\sum_iA(x_i^\top\beta)\}/a(\phi)+\sum_i c(y_i,\phi)$. Differentiating gives $U(\beta)=\sum_i x_i\{y_i-A'(\eta_i)\}/a(\phi)=X^\top(y-\mu)/a(\phi)$ and $-\nabla^2\ell=X^\top\operatorname{diag}\{A''(\eta_i)\}X/a(\phi)$. The latter is free of $y$, hence equals expected information. The displayed likelihood factors into a function of $X^\top y$ and $\beta$ times a factor free of $\beta$, proving sufficiency by factorisation. For Bernoulli data, $p^y(1-p)^{1-y}=\exp\{y\log[p/(1-p)]-\log(1+e^{\log[p/(1-p)]})\}$, identifying the logit; for Poisson data, $e^{-\mu}\mu^y/y!=\exp\{y\log\mu-\mu-\log(y!)\}$, identifying the log.{{cite:nelder_wedderburn1972}} (§§1.1, 2.2, 3.2–3.3, pp. 371, 374, 378–380)
:::
:::

## Statistical use — Choosing a mean relationship
Canonical links simplify fitting, but the link also states a substantive relation between covariates and the mean. The Poisson log link says a one-unit covariate increase multiplies the mean by a constant factor; the Bernoulli logit says it multiplies the odds by a constant factor. A probit link may better describe a latent normal threshold, and a log link may be more interpretable than the gamma inverse link for positive responses. Link choice should therefore be checked against the science and the observed response pattern, not settled solely by the word “canonical.”{{cite:nelder_wedderburn1972}} (§§1.3, 3.3–3.4, pp. 372, 378–381)

For gamma responses under the natural-parameter convention $\theta=-1/\mu<0$, an unconstrained linear predictor can cross zero and imply an impossible negative or infinite mean; a log link keeps the mean positive for every real predictor. In logistic regression with a covariate that perfectly separates successes from failures, the likelihood can approach its supremum as a coefficient diverges, so the canonical logit does not yield a finite maximum likelihood estimate. With two identical design columns, $X^\top W X$ is singular and cannot identify separate coefficients. In each case the algebraic score simplification remains, while the intended fitting or uncertainty calculation fails.{{cite:nelder_wedderburn1972}} (§§2.1, 3.3–3.4, pp. 373, 378–381)

## Worked example — A logit coefficient doubles odds, not probability
Suppose a binary-response model has $\eta=\beta_0+\beta_1x$ with $\beta_0=\log(1/3)$ and $\beta_1=\log 2$. Because the Bernoulli natural parameter is log odds, the canonical link gives $p(x)=e^\eta/(1+e^\eta)$. At $x=0$ the odds are $1/3$ and $p(0)=1/4=0.25$. At $x=1$ the odds double to $2/3$ and $p(1)=2/5=0.40$. The coefficient represents an odds multiplier of $2$, while the probability rises by $0.15$ in this particular comparison. The probability change would differ at another starting probability, even with the same coefficient.{{cite:nelder_wedderburn1972}} (§3.3, logistic model, pp. 378–380)

**Your turn.** A Poisson regression uses its canonical link and has $\eta=\log3+x\log2$. Find the conditional means at $x=0,1,2$ and interpret the slope on the mean scale.

::: {.callout-tip collapse="true" title="Answer"}
Since $\mu(x)=e^\eta=3\cdot2^x$, the means are $3$, $6$ and $12$. Each one-unit increase in $x$ doubles the conditional mean. The predictor is log mean, not the count itself, and the observed count can still vary about its mean.
:::

## Common misconceptions — “Canonical” does not mean “best”
“Canonical” does not mean best fitting: a link can have simple derivatives yet imply an inappropriate covariate effect. It does not mean that observed responses are transformed to become normal; GLMs model a response distribution and link its *mean*. Nor is a canonical link universal across families: log is canonical for Poisson but logit is canonical for Bernoulli. Finally, equating observed and expected Hessians under a canonical link does not ensure finite standard errors if the design lacks rank or an estimate lies at infinity.{{cite:nelder_wedderburn1972}} (§§1.3, 2.1–2.2, 3.2–3.4)

## Connections — Natural parameter, score, and Fisher scoring
For an [exponential family](exponential-family.qmd), the canonical [link](link-function.qmd) is the one that sets the linear predictor equal to the [natural parameter](natural-parameter.qmd). In that parameterisation the [score](score-function.qmd) is $X^\top(y-\mu)/a(\phi)$. The observed Hessian does not depend on $y$, so it equals the [Fisher information](fisher-information.qmd), and [Fisher scoring](fisher-scoring.qmd) takes the same step as Newton–Raphson. The canonical link for a family is found by reading off the coefficient of $y$ and writing that coefficient as a function of $\mu$: the result is the Poisson log link, the Bernoulli logit, or a negative-binomial canonical link.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

## History — The predictor set equal to the natural parameter
Nelder and Wedderburn singled out the case in which the distribution parameter equals the linear predictor and showed that it yields sufficient statistics and matching observed and expected second derivatives. The phrase “canonical link” names that alignment within the exponential-family representation.{{cite:nelder_wedderburn1972}} (§§1.3, 2.2, 3, pp. 372, 374, 377–381)
