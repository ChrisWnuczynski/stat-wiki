## Lead context
The sign indicates which side of the fitted mean an observation occupies; the squared magnitude records its contribution to the likelihood discrepancy.

## Motivating example
An observed count of zero is a very different departure from a fitted mean of one than from a fitted mean of twenty. Raw residuals alone use the response's scale, while deviance residuals use the model's likelihood scale. Their squares decompose the discrepancy between the fitted and saturated mean models into individual observations.{{cite:dunn_smyth1996}} (§2)

## Definition — A signed square root of unit deviance
For independent exponential-family observations with a common dispersion $\phi$, let $d(y_i,\hat\mu_i)$ be an observation's unit deviance. Define
$$
r_{D,i}=\operatorname{sign}(y_i-\hat\mu_i)
\sqrt{d(y_i,\hat\mu_i)}.
$$
With the convention $\operatorname{sign}(0)=0$, a perfectly fitted observation has residual zero. The unscaled deviance is $D=\sum_i d(y_i,\hat\mu_i)=\sum_i r_{D,i}^2$. Dividing residuals by $\sqrt\phi$ makes their squared sum the scaled deviance $D/\phi$.{{cite:dunn_smyth1996}} (§2, unit deviance and deviance residual)

For a Poisson mean $\mu>0$,
$$
d(y,\mu)=2\{y\log(y/\mu)-(y-\mu)\},
$$
using $0\log0=0$ by continuity. In particular $d(0,\mu)=2\mu$, so a zero count has residual $-\sqrt{2\mu}$. The linear term in $y-\mu$ is part of each contribution, even in models where its sum over observations happens to vanish.{{cite:nelder_wedderburn1972}} (§2.3, p. 375)

## Properties — The Poisson formula from its log likelihood
The Poisson log likelihood for one observation is $\ell(\mu;y)=y\log\mu-\mu-\log(y!)$. Its saturated mean is $y$, with zero handled as a boundary limit. Subtracting the fitted log likelihood from the saturated one cancels the factorial term and gives $d/2$. This derivation explains why an arbitrary squared raw residual is not the same contribution.{{cite:nelder_wedderburn1972}} (§2.3, p. 375)

The signed root preserves the direction that squaring discards. A large positive residual indicates a count above the fitted mean; a large negative residual indicates a count below it. Its distribution still depends on the response family and fitted mean. For discrete observations, deviance residuals may form separate curves corresponding to distinct response values, and normal-looking residuals are not guaranteed.{{cite:dunn_smyth1996}} (§§1–2)

## Worked example
For observed counts $(0,2,5)$ and predicted means $(1,2,3)$, the unit deviances are
$$
d_1=2,\qquad d_2=0,\qquad
d_3=2\{5\log(5/3)-2\}\approx1.108256.
$$
The deviance residuals are approximately $(-1.414214,0,1.052737)$, and their squared sum is $D\approx3.108256$. The first and third counts lie on different sides of their predictions; their signed residuals preserve that difference.{{cite:nelder_wedderburn1972}} (§2.3);{{cite:dunn_smyth1996}} (§2)

The Pearson residuals for the same Poisson means are $(y_i-\mu_i)/\sqrt{\mu_i}$, giving $(-1,0,2/\sqrt3)$. They use the variance function rather than the exact unit-deviance difference, so they need not match the deviance residuals away from a close fit.{{cite:dunn_smyth1996}} (§2)

**Your turn.** If the zero count in the first observation instead has predicted mean four, find its deviance and deviance residual.

::: {.callout-tip collapse="true" title="Answer"}
For a zero count, $d=2\mu=8$ and the sign is negative. The deviance residual is $-\sqrt8=-2\sqrt2\approx-2.828427$.
:::

## Interpretation — Local agreement with Pearson residuals
Let $y=\mu+\delta$ with $|\delta|/\mu$ small. Expanding the logarithm gives
$$
d(y,\mu)=\delta^2/\mu+O(\delta^3/\mu^2).
$$
Thus $r_D$ is approximately $\delta/\sqrt\mu$ near a close fit, agreeing to first order with the Poisson Pearson residual. The expansion is local; zero counts at small means and large deviations can show substantial differences.{{cite:dunn_smyth1996}} (§2, comparison of Pearson and deviance residuals)

## Check yourself
Keep unscaled deviance distinct from its dispersion-scaled likelihood ratio.

### The saturated comparison {#self-check-c-29}
[Saturated model and deviance](../questions/c-29.qmd): which squared residual sum corresponds to $D$, and which to $D/\phi$?

::: {.callout-tip collapse="true" title="Answer"}
The unit-deviance residuals satisfy $\sum_i r_{D,i}^2=D$. Their dispersion-scaled versions $r_{D,i}/\sqrt\phi$ satisfy a squared sum of $D/\phi$, the scaled likelihood-ratio discrepancy at the common dispersion.
:::

### Comparing fitted models {#self-check-ex-sl-10-6}
[Reading the deviance](../questions/ex-sl-10-6.qmd): use the stated Wald approximation to predict the reduced-model deviance.

::: {.callout-tip collapse="true" title="Answer"}
The approximate increase is $1.016^2=1.032256$, giving $354.97+1.032256\approx356.0023$ on $297$ residual degrees of freedom. The actual observed likelihood-ratio difference requires refitting the reduced model. The approximation is below the supplied one-degree-of-freedom critical value $3.84$.
:::
