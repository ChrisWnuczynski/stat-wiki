## Lead context
Hotelling's T-squared test asks whether a sample of vector measurements is centred at a proposed mean, using the sample covariance so that correlated coordinates are not treated as separate one-coordinate tests.{{cite:hotelling1931}} (pp. 360–378)

## Motivating example
Five paired measurements have sample mean $(2,0)$ and a sample covariance that is the identity. Looked at alone, the first coordinate has mean difference $2$ and the second has mean difference $0$. A joint test has to say whether the pair $(2,0)$ is far from $(0,0)$ in the metric of that covariance. With the identity covariance the squared distance is $2^2+0^2=4$, and $T^2=n\times 4=20$.{{cite:hotelling1931}} (pp. 360–378) The same number is the square of the ordinary one-sample $t$ on the first coordinate, because the second coordinate contributes nothing and the coordinates are uncorrelated in this covariance.

## Intuition
The one-sample $t$ statistic is a mean difference divided by an estimated standard error. Squaring it produces a one-dimensional $T^2$. In several dimensions the standard error becomes a covariance matrix. Multiplying by the inverse covariance is the squared Mahalanobis distance of the sample mean from the proposed mean, scaled by the sample size. Large values say the mean is far from the proposal in a direction where the sample does not vary much. A direction in which the sample varies a great deal can absorb a numerically larger raw difference.

## Definition
For an independent sample of size $n>p$ from a $p$-dimensional distribution with mean $\boldsymbol{\mu}$ and a nonsingular sample covariance $S$,

$$
T^2=n(\bar{\mathbf{x}}-\boldsymbol{\mu}_0)^\top S^{-1}(\bar{\mathbf{x}}-\boldsymbol{\mu}_0)
$$

tests $\boldsymbol{\mu}=\boldsymbol{\mu}_0$.{{cite:hotelling1931}} (pp. 360–378) When $p=1$, $S=s^2$ and $T^2=t^2$, where $t=\sqrt n(\bar x-\mu_0)/s$ is the ordinary one-sample statistic. For normal data the null calibration used with this statistic is

$$
\frac{n-p}{(n-1)p}T^2\sim F_{p,\,n-p}.
$$

The 0.95 quantile of $F_{2,4}$ is $6.944$. A transformed value below that quantile is not a $5\%$ rejection under this calibration.

## Interpretation
The statistic is zero only when $\bar{\mathbf{x}}=\boldsymbol{\mu}_0$. It grows when the mean moves away from $\boldsymbol{\mu}_0$ along a short axis of $S$. Replacing $S$ by the identity ignores the sample correlations and the coordinate scales. In the identity example that replacement happens to be correct, because $S=I$. If $S=\bigl(\begin{smallmatrix}2&0\\0&2\end{smallmatrix}\bigr)$ and the mean is $(1,1)$, then $S^{-1}$ halves each squared coordinate and

$$
T^2=6\cdot(1,1)S^{-1}(1,1)^\top=6\cdot 1=6
$$

for $n=6$. The transformed value is $(6-2)/((6-1)\cdot 2)\cdot 6=2.4$. The $0.95$ quantile of $F_{2,4}$ is $6.944$, and the upper tail probability of $2.4$ is $0.2066$. The mean is one unit from the origin on each axis, and the test does not reject at $5\%$.

## Properties
$T^2$ is unchanged by a common shift of the data and the proposed mean, and it scales in the natural way under a common nonsingular linear transformation of the coordinates: the inverse covariance transforms by the inverse congruence, and the quadratic form is invariant. When $p=1$ the $F$ factor equals $1$, so the transformed statistic equals $T^2$. For $n=5$, $\bar x=2$, $\mu_0=0$ and $s=1$, $t=\sqrt5\cdot 2\approx 4.4721$ and $t^2=20$, which is also $T^2$. SciPy defines an $F$ law as a ratio of independent chi-squared variables after rescaling by the degrees of freedom. A squared standard normal is chi-squared on one degree of freedom, and dividing by an independent chi-squared scale with $\nu$ degrees of freedom produces $F_{1,\nu}$. That is why a squared $t_{n-1}$ statistic and this one-dimensional transform refer to the same critical value.

A singular $S$ makes $S^{-1}$ undefined. That happens automatically if $n\le p$, because the centred data matrix has rank at most $n-1$. The test as written then has no value.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $p=1$, $S^{-1}=1/s^2$ and $T^2=n(\bar x-\mu_0)^2/s^2=t^2$. The factor $(n-1)/((n-1)\cdot 1)$ equals $1$, so the $F$ transform equals $T^2$. For the numbers $n=5$, $\bar x=2$, $s=1$, $t^2=5\cdot 4=20$. SciPy's $F$ law is a rescaled ratio of independent chi-squared variables, so the square of a $t_{n-1}$ variable, a normal squared over an independent chi-squared scale, is $F_{1,n-1}$.{{cite:scipy_f2026}} (§ Notes, ratio of independent chi-squared variables)

For the two-dimensional example, $S=2I_2$ so $S^{-1}=\tfrac12 I_2$ and $(\bar{\mathbf{x}})^\top S^{-1}\bar{\mathbf{x}}=1/2+1/2=1$. Thus $T^2=6$. The $F$ factor is $(4)/(5\cdot 2)=0.4$, and $0.4\cdot 6=2.4$. The upper tail $\Pr(F_{2,4}\ge 2.4)=0.2066$, and $F_{2,4;\,0.95}=6.944$.
:::
:::

## Statistical use — One quadratic form, not two separate tests
Use $T^2$ when the scientific question is about the mean vector. Two separate $t$ tests answer two coordinate questions and do not control the joint error in the same way, and they ignore covariance off the diagonal. The identity example is the special case in which the coordinates are uncorrelated and on the same scale, so the joint statistic splits into a sum of squares of $t$ statistics. With a nonzero covariance that split fails. Report $n$, $p$, and whether $S$ divides by $n-1$. The calibration above uses that divisor.

## Worked example
Sample size $n=6$, dimension $p=2$, sample mean $(1,1)$, $S=2I_2$, proposed mean $\mathbf{0}$. Then $T^2=6$ and the transformed statistic is $2.4$. Since $2.4<6.944$, the $5\%$ test does not reject. The upper tail probability is $0.2066$.

One-dimensional check: $n=5$, $\bar x=2$, $s=1$, proposed mean $0$. Then $T^2=t^2=20$. The transformed statistic is also $20$, now on $F_{1,4}$.

**Your turn.** Keep $n=6$, $p=2$ and $S=2I_2$, and move the sample mean to $(2,0)$. Find $T^2$.

::: {.callout-tip collapse="true" title="Answer"}
$S^{-1}$ still multiplies the squared length by $1/2$, and the squared length is $4$, so $(\bar{\mathbf{x}})^\top S^{-1}\bar{\mathbf{x}}=2$. Then $T^2=6\cdot 2=12$.
:::

## Common misconceptions
$T^2$ is not the squared Euclidean distance. In the worked example the Euclidean squared length of the mean is $2$, while $T^2=6$ after the covariance scaling and the factor $n$.

A nonsignificant coordinate test is not a nonsignificant $T^2$. The tests use different covariances when the coordinates are correlated. The identity case hides that difference.

The $F$ quantile is not $T^2$ itself. The comparison is between $2.4$ and $6.944$, not between $6$ and $6.944$. Forgetting the factor $(n-p)/((n-1)p)$ compares the statistic with the wrong scale.

## Assumptions and limits — When the covariance inverse is the wrong metric
The $F$ calibration is a normal-sample result. A long-tailed vector sample can have a mean and a covariance and still not have this null distribution. A singular $S$, including every case $n\le p$, leaves $T^2$ undefined. Dividing the cross-product matrix by $n$ instead of $n-1$ changes $S$ and changes $T^2$ by the factor $(n-1)/n$; the $F$ quantile above is for the $n-1$ divisor. And a proposed mean that is not the scientific target produces a precise answer to the wrong question: $T^2=6$ is the distance from $(1,1)$ to the origin, not the distance to some other point.

## Connections
The [one-sample $t$ test](one-sample-t-test.qmd) is the case $p=1$, with $T^2=t^2$. The [$F$ distribution](f-distribution.qmd) supplies the critical value after the factor $(n-p)/((n-1)p)$. A [sample covariance](mean-vector-and-covariance-matrix.qmd) that is not invertible is the case the statistic does not cover.

## History
The one-dimensional reduction shows why the statistic carries Student's name into several dimensions: $T^2$ is $t^2$ when $p=1$. The $F$ quantiles used for the two-dimensional numerical comparison are the $0.95$ point $6.944$ of $F_{2,4}$ and the tail probability $0.2066$ at $2.4$. Those are properties of the $F$ family. The normal-sample argument that the transformed $T^2$ follows that family is the content of the multivariate derivation; the algebra checked here is the quadratic form and the one-dimensional identity.
