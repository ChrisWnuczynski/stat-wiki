## Lead context
Maximum likelihood in a GLM solves a weighted score equation, and the usual solver repeats a weighted least-squares step until the coefficients stop moving.

## Motivating example
One Poisson count equals $2$, and the mean is $e^{\beta}$ for an intercept-only log link. The likelihood equation is $2-e^{\beta}=0$, so $\beta=\log 2$. A tangent step from $\beta=0$ does not land on $\log 2$, but the next step is closer. That is the iteration a GLM uses when the score is not linear.

## Intuition — Reweight the residual and repeat
For an exponential-family GLM the score for $\beta$ has one summand per observation,
$$
\frac{y_i-\mu_i}{V_i}\frac{d\mu_i}{d\eta_i}x_i,
$$
where $V_i$ is the variance function at the current mean and $d\mu_i/d\eta_i$ is the slope of the inverse link. The weights depend on $\beta$, so the equation is not the ordinary normal equation. {{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374) Fisher scoring freezes those weights, replaces the mean by its tangent, and solves a weighted least-squares problem for the step. R’s `glm.fit` is that iteration.{{cite:rstats_glm2026}} (§ `glm.fit`, iteratively reweighted least squares)

## Definition — Poisson log link, one count
For $Y\sim\mathrm{Poisson}(e^{\beta})$, the log-likelihood is $\ell(\beta)=y\beta-e^{\beta}$ up to a constant. The score and Hessian are
$$
U(\beta)=y-e^{\beta},\qquad H(\beta)=-e^{\beta}.
$$
The Newton update, which here equals Fisher scoring, is $\beta-U(\beta)/H(\beta)$. {{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Differentiate $\ell$: the derivative of $y\beta-e^{\beta}$ is $y-e^{\beta}$, and the second derivative is $-e^{\beta}$. The mean $\mu=e^{\beta}$ equals the variance, and $d\mu/d\beta=\mu$, so the general GLM score $(y-\mu)/V\cdot d\mu/d\eta$ reduces to $y-\mu$. The observed Hessian does not contain $y$ except through $\mu(\beta)$, so it equals the expected information.
:::
:::

## Worked example
Take $y=2$ and start at $\beta^{(0)}=0$. Then $\mu=1$, $U=1$, and $H=-1$, so $\beta^{(1)}=1$. At $\beta=1$ the mean is $e\approx 2.718282$ and
$$
\beta^{(2)}=1-\frac{2-e}{-e}=\frac{2}{e}\approx 0.735759.
$$
The maximiser is $\log 2\approx 0.693147$. One further step from $2/e$ is not required to see the direction: the score $2-e^{2/e}$ is negative because $e^{2/e}>2$, so the next move decreases $\beta$ toward $\log 2$.

**Your turn.** Start at $\beta=\log 2$ and compute the score. What is the next Newton value?

::: {.callout-tip collapse="true" title="Answer"}
$U(\log 2)=2-e^{\log 2}=0$, so the update stays at $\log 2$.
:::

## Connections — When the step is exact
An [identity link](identity-link.qmd) with constant variance makes the score linear, so one step finishes the fit. A [logit link](logit-link.qmd) keeps the same weighted iteration and, for Bernoulli data, has observed Hessian equal to expected information. [Complete separation](complete-separation.qmd) is the case with no finite root for that iteration to find. [Newton’s method](newton-raphson-method.qmd) is the tangent step written above.

