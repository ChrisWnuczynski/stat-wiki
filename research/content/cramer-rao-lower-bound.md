## Lead context
The Cramér–Rao lower bound is a floor under the variance of an unbiased estimator, available when the model is regular enough that the score has mean zero and finite variance.{{cite:siegrist2022_best_unbiased}} (§7.5, Cramér–Rao bounds)

## Motivating example
One Bernoulli trial has log probability \(X\log\theta+(1-X)\log(1-\theta)\). Its score is \((X-\theta)/\{\theta(1-\theta)\}\). For \(n\) independent trials the score adds, so \(S(\theta)=n(\overline X-\theta)/\{\theta(1-\theta)\}\). The variance of one score is \(1/\{\theta(1-\theta)\}\), and \(\mathcal{I}(\theta)=n/\{\theta(1-\theta)\}\). The bound for \(\theta\) is \(\theta(1-\theta)/n\). At \(\theta=1/4\) and \(n=20\),
\[
\frac{(1/4)(3/4)}{20}=0.009375.
\]
The sample proportion has variance \(\theta(1-\theta)/n\), so it meets the bound. The score is a multiple of \(\overline X-\theta\), which is the equality case.{{cite:siegrist2022_best_unbiased}} (§7.5, Cramér–Rao bounds)

## Intuition — The score limits how sharp an unbiased estimator can be
The score \(S(\theta)\) is the derivative of the log-density with respect to a scalar parameter. In a regular model its mean is zero, and its variance is the Fisher information \(\mathcal{I}(\theta)\). An unbiased estimator \(T\) of \(g(\theta)\) has to move when \(\theta\) moves. That movement shows up as a covariance with the score. Cauchy–Schwarz then stops the variance of \(T\) from being smaller than the square of that covariance divided by the information.

## Definition — The variance floor
Let \(T\) be unbiased for a differentiable target \(g(\theta)\), with finite variance. Suppose the support of the density does not depend on \(\theta\), and that both \(\mathbb{E}_\theta T=g(\theta)\) and \(\int f(x\mid\theta)\,dx=1\) may be differentiated under the integral. Then
\[
\operatorname{Var}_\theta(T)\ge\frac{\{g'(\theta)\}^2}{\mathcal{I}(\theta)},
\]
where \(\mathcal{I}(\theta)=\operatorname{Var}_\theta\{S(\theta)\}\) and \(S(\theta)=\partial\log f(X\mid\theta)/\partial\theta\). For \(g(\theta)=\theta\) the floor is \(1/\mathcal{I}(\theta)\).{{cite:siegrist2022_best_unbiased}} (§7.5, Cramér–Rao bounds)

## Properties — Cauchy–Schwarz on the score
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Differentiating \(\mathbb{E}_\theta T=g(\theta)\) under the integral gives \(\mathbb{E}_\theta\{T\,S(\theta)\}=g'(\theta)\). Differentiating the density's integral gives \(\mathbb{E}_\theta S(\theta)=0\), so the covariance of \(T\) and \(S(\theta)\) equals \(g'(\theta)\). Cauchy–Schwarz yields
\[
\{g'(\theta)\}^2=\bigl(\operatorname{Cov}_\theta(T,S(\theta))\bigr)^2
\le\operatorname{Var}_\theta(T)\,\operatorname{Var}_\theta\{S(\theta)\}
=\operatorname{Var}_\theta(T)\,\mathcal{I}(\theta).
\]
Rearrangement is the bound, provided \(\mathcal{I}(\theta)>0\). Equality holds when \(S(\theta)=k(\theta)\{T-g(\theta)\}\) for some \(k(\theta)\) free of the sample.
:::
:::

The uniform\((0,\theta)\) model is outside the argument: the upper endpoint of the integral depends on \(\theta\), so the derivative does not pass under the integral. A small variance in that model is not a counter-example, because the inequality's derivative-under-the-integral step does not apply when the support depends on the parameter.

## Worked example — A Bernoulli proportion

**Your turn.** For the same Bernoulli model with \(n=10\) and \(\theta=1/2\), give the Cramér–Rao bound for an unbiased estimator of \(\theta\), and the variance of \(\overline X\).

::: {.callout-tip collapse="true" title="Answer"}
Both equal \((1/2)(1/2)/10=0.025\). The sample proportion still meets the bound. The numerical value is larger than \(0.009375\) because the sample is smaller and the Bernoulli variance \(\theta(1-\theta)\) is larger at \(1/2\) than at \(1/4\).
:::

## Connections — Information, attainment and unbiased estimation
The denominator is the [Fisher information](fisher-information.qmd), the variance of the [score](score-function.qmd). An estimator that attains the bound at every \(\theta\) is a [uniformly minimum-variance unbiased estimator](uniformly-minimum-variance-unbiased-estimator.qmd). Attainment for every \(\theta\) forces the likelihood into a one-parameter exponential family with sufficient statistic \(T\), because the score has to be linear in \(T-g(\theta)\). A biased estimator can have smaller mean squared error; the bound does not apply to it.

