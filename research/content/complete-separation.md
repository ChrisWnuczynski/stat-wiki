## Lead context
Complete separation means a direction in the predictors sorts the two classes perfectly, so the logistic likelihood never reaches a finite maximum.

## Motivating example
Suppose every failure has a negative predictor and every success has a positive one. Pushing the slope upward makes each fitted probability closer to the observed $0$ or $1$. The log-likelihood climbs toward its upper bound and the coefficient does not settle.

## Intuition — The likelihood rises and the coefficient runs away
For a Bernoulli observation the log contribution $\log p$ or $\log(1-p)$ is at most $0$, with equality only when the fitted probability equals the observed label. If a direction $v$ has $v^{\mathsf T}x_i>0$ for every success and $v^{\mathsf T}x_i<0$ for every failure, then moving $\beta$ a long way along $v$ drives every factor toward that bound. The log-likelihood increases, but the bound $0$ is not attained at any finite $\beta$. The fit is not a large but finite slope. There is no maximizer. {{cite:albert_anderson1984}} (§2, Thm. 1, p. 3)

## Definition — A one-predictor path
Let $x_i\in\{-1,1\}$ and $y_i=(1+x_i)/2$, and fit an intercept-free logit, $p_i=e^{\beta x_i}/(1+e^{\beta x_i})$. Each observation contributes
$$
\beta-\log(1+e^{\beta})=-\log(1+e^{-\beta})
$$
to the log-likelihood, whether it is a success at $x=1$ or a failure at $x=-1$. For $n$ such observations,
$$
\ell(\beta)=n\bigl(\beta-\log(1+e^{\beta})\bigr).
$$
As $\beta\to\infty$, $\ell(\beta)\to 0$ from below, and $\ell$ has no critical point at a finite $\beta$. {{cite:albert_anderson1984}} (§§1–2, pp. 1–3, existence of logistic estimates)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $x=1$ and $y=1$, $\log p=\beta-\log(1+e^{\beta})$. For $x=-1$ and $y=0$, $p=1/(1+e^{\beta})$ and $\log(1-p)=\beta-\log(1+e^{\beta})$. The two contributions agree. Also
$$
\beta-\log(1+e^{\beta})=-\log(1+e^{-\beta}),
$$
which is negative for every finite $\beta$ and tends to $0$ as $\beta\to\infty$. The derivative of $\ell/n$ is $1-e^{\beta}/(1+e^{\beta})=1/(1+e^{\beta})>0$, so $\ell$ is strictly increasing and has no finite stationary point.
:::
:::

## Worked example
Four observations, two at $x=-1$ with $y=0$ and two at $x=1$ with $y=1$, give $\ell(\beta)=4\bigl(\beta-\log(1+e^{\beta})\bigr)$. Then
$$
\ell(0)=-4\log 2\approx -2.773,\qquad \ell(2)\approx -0.508,\qquad \ell(5)\approx -0.027.
$$
The values are increasing toward $0$. A reported slope of $5$ is not a stable estimate: $\ell(10)$ is closer to $0$ still, and so is $\ell(20)$.

**Your turn.** Using the same four observations, compute $\ell(1)$ and say whether it lies between $\ell(0)$ and $\ell(2)$.

::: {.callout-tip collapse="true" title="Answer"}
$\ell(1)=4\bigl(1-\log(1+e)\bigr)\approx -1.253$. Because the score is positive, $\ell(0)<\ell(1)<\ell(2)$.
:::

## Connections — What the software is chasing
[Maximum likelihood](maximum-likelihood.qmd) looks for a root of the score. [Newton’s method](newton-raphson-method.qmd) follows that score, and here the score never hits zero. The [logit link](logit-link.qmd) is what turns a separating direction into probabilities that can approach $0$ and $1$. A huge coefficient with a huge standard error is a prompt to look at whether the successes and failures are sorted by the predictors, not a precise finite-sample standard error. {{cite:albert_anderson1984}} (§§2–4, pp. 2–7)
