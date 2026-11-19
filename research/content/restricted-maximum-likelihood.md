## Lead context
Restricted maximum likelihood estimates a variance from the residuals after the fixed mean has been removed, which is why a normal sample variance divides by one less than the sample size.

## Motivating example
Five measurements $1,2,3,4,10$ have mean $4$ and residual sum of squares $50$. Dividing by $5$ gives $10$. Dividing by $4$ gives $12.5$. The second divisor is what remains after the mean has used one direction in the sample.

## Intuition — The mean is not part of the variance likelihood
The ordinary normal likelihood treats $\mu$ and $\sigma^2$ together. Its maximiser for $\sigma^2$ is the residual sum of squares divided by $n$, and that estimator is biased downward. Once $\mu$ is unknown, the deviations $X_i-\overline X$ live in an $(n-1)$-dimensional subspace. Restricted maximum likelihood uses the likelihood of those contrasts. For a single normal sample that likelihood is the chi-squared law of $(n-1)S^2/\sigma^2$, and its maximiser is $S^2$.{{cite:siegrist2022_normals}} (§6.08, chi-square law of $V$)

## Definition — The chi-squared likelihood of the residual sum
Let $Q=\sum_{i=1}^n(X_i-\overline X)^2$ for an iid normal sample, so $Q/\sigma^2$ is chi-squared on $\nu=n-1$ degrees of freedom. The log-likelihood in $\sigma^2$ based on $Q$ is, up to a constant,
$$
\ell(\sigma^2)=-\frac{\nu}{2}\log\sigma^2-\frac{Q}{2\sigma^2}.
$$
The maximiser is $\hat\sigma^2=Q/\nu=S^2$. {{cite:siegrist2022_normals}} (§6.08, chi-square law of $V$) The ordinary maximum-likelihood estimator is $Q/n$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Differentiate with respect to $\sigma^2$: $\partial\ell/\partial\sigma^2=-\nu/(2\sigma^2)+Q/(2\sigma^4)$. Setting the derivative to zero gives $\sigma^2=Q/\nu$. As $\sigma^2\to 0$ or $\sigma^2\to\infty$, $\ell\to-\infty$, so this positive critical point is the maximum. Siegrist’s chi-squared law is the density whose logarithm is $\ell$.{{cite:siegrist2022_normals}} (§6.08, The Sample Variance)
:::
:::

## Worked example
For $1,2,3,4,10$ the mean is $4$ and $Q=50$. The ordinary maximum-likelihood estimate is $50/5=10$. The restricted estimate is $50/4=12.5$. The same five numbers cannot support both divisors as the same estimator: $n$ counts observations, and $n-1$ counts residual degrees of freedom.

**Your turn.** For $2,2,2,6$, compute the ordinary maximum-likelihood estimate of $\sigma^2$ and the restricted estimate.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $3$ and $Q=12$. The ordinary estimate is $12/4=3$. The restricted estimate is $12/3=4$.
:::

## Connections — Fixed effects and variance components
The [sample variance](variance.qmd) $S^2$ is this one-sample restricted estimator. A [linear mixed model](linear-mixed-model.qmd) has several variance components, and the same idea removes the fixed effects before estimating those components. Comparing two models that differ in their fixed effects should use the ordinary likelihood of both fits: the restricted likelihoods are likelihoods of different sets of contrasts. A test of a variance component against zero also sits on the boundary of the parameter space, so a naive chi-squared reference from a likelihood-ratio statistic is not automatic.
