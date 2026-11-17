## Motivating example
Suppose a sensor is observed at a few locations and a prediction is needed between them. A model for a whole random function can specify how strongly nearby readings should be related before a finite set of observation locations is chosen. A Gaussian process makes every finite prediction problem a multivariate-normal calculation.{{cite:rasmussen_williams2006}} (§2.2, Def. 2.1, p. 13)

## Definition — Consistent finite Gaussian vectors
A process $f(x)$ is Gaussian if every finite vector $(f(x_1),\ldots,f(x_n))$ is jointly normal, allowing singular covariance matrices. Its mean function $m(x)$ and covariance function $k(x,x')$ determine these finite laws. Marginalising a finite vector must agree with the law specified directly for its subset of inputs.{{cite:rasmussen_williams2006}} (§2.2, pp. 13–14)

For every finite set of inputs, the matrix $K_{ij}=k(x_i,x_j)$ must be symmetric and positive semidefinite. This condition follows from $a^\top Ka=\operatorname{Var}(\sum_i a_if(x_i))\ge0$. A matrix of appealing pairwise similarities can fail this joint requirement.{{cite:rasmussen_williams2006}} (§4.1, pp. 79–80)

## Properties — Conditioning and observation noise
With independent normal observation noise of variance $\sigma^2>0$, let $K$ be the training covariance matrix, $k_*$ the covariance vector between the prediction location and training inputs, and $k_{**}$ its prior variance. For a zero mean prior,
$$
\mathbb E(f_*\mid y)=k_*^\top(K+\sigma^2I)^{-1}y,\qquad
\operatorname{Var}(f_*\mid y)=k_{**}-k_*^\top(K+\sigma^2I)^{-1}k_*.
$$
A prediction of a new noisy reading adds $\sigma^2$ to this latent-function variance. The two predictive variances answer different questions.{{cite:rasmussen_williams2006}} (§2.2, eqs. 2.23–2.24, p. 16)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $A=K+\sigma^2I$ be positive definite, and define the linear residual $R=f_*-k_*^\top A^{-1}y$. Its covariance with $y$ is $k_*^\top-k_*^\top A^{-1}A=0$, and its variance is $k_{**}-k_*^\top A^{-1}k_*$. The vector $(y,R)$ is jointly normal because it is a linear transformation of $(y,f_*)$. Its block-diagonal covariance makes its normal density factor into a function of $y$ and a function of $R$, so the two are independent. Thus conditioning on $y$ only adds the known term $k_*^\top A^{-1}y$ to $R$, giving the stated mean and variance. If the residual variance is zero, $R$ is deterministic and the same formulas hold.{{cite:rasmussen_williams2006}} (§2.2, eqs. 2.23–2.24, p. 16)
:::
:::

## Worked example — Learning from one noisy reading
Use $k(x,x')=\exp\{-(x-x')^2/2\}$, prior mean zero, noise variance $0.25$, and one reading $y=2$ at $x=0$. At $x_*=1$, $k_*=e^{-1/2}=0.606531$. The posterior latent mean is $2e^{-1/2}/1.25=0.970449$ and its variance is $1-e^{-1}/1.25=0.705696$. The reading shifts the mean, while its distance and noise leave substantial uncertainty.

**Your turn.** What variance should be reported for a new noisy reading at $x_*=1$ under this same model?

::: {.callout-tip collapse="true" title="Answer"}
Add the observation-noise variance to the latent variance: $0.705696+0.25=0.955696$.
:::

## Connections — Gaussian does not mean smooth or stationary
Brownian motion is a Gaussian process with covariance $k(s,t)=\min(s,t)$ for nonnegative times. Its increments can be stationary even though its levels have variance $t$ and hence are not stationary. A smooth covariance and Brownian covariance therefore encode quite different path behaviour; Gaussian finite laws alone do not choose one.{{cite:durrett2019}} (§7.1, Gaussian-process characterisation, p. 355)

## Check yourself

Use the definitions and calculations above to work through these questions.

### Check a proposed covariance {#self-check-ex-sl-01-1}

[Check a proposed covariance](../questions/ex-sl-01-1.qmd). Apply the nonnegative-variance condition.

::: {.callout-tip collapse="true" title="Answer"}
For any coefficient vector $a$, $a^\top\Sigma a$ is a variance. The displayed candidate correlation matrix has determinant $-2.888$, so it cannot be a covariance matrix.
:::

### Uncorrelated coordinates need a joint assumption {#self-check-ex-sl-01-3}

[Uncorrelated coordinates need a joint assumption](../questions/ex-sl-01-3.qmd). Explain the dependence in the example.

::: {.callout-tip collapse="true" title="Answer"}
For a centred standard normal $X$, $\operatorname{Cov}(X,X^2)=\mathbb E(X^3)=0$, but the second coordinate is determined by the first. This vector is not jointly Gaussian.
:::
