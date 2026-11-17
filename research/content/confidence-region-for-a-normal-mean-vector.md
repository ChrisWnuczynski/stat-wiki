## Lead context
The region combines uncertainty across coordinates through the inverse covariance, rather than testing each coordinate separately.

## Motivating example
A treatment study measures changes in two related scores. Reporting separate intervals for the two mean changes obscures directions in which the changes are estimated precisely or imprecisely together. A joint confidence ellipsoid uses their covariance to describe those directions and to test a proposed mean vector in one step. The same geometric idea underlies confidence ellipsoids for vectors of model parameters.{{cite:friendly_monette_fox2013}} (§§2.2, 4.6)

## Definition — Inverting the normal-mean test
Let $X_1,\ldots,X_n$ be iid $N_p(\mu,\Sigma)$, with $\Sigma$ positive definite and $n>p$. Define the unbiased sample covariance $S=(n-1)^{-1}\sum_i(X_i-\bar X)(X_i-\bar X)^\top$. A $1-\alpha$ confidence region is
$$
\left\{\mu_0:
n(\bar X-\mu_0)^\top S^{-1}(\bar X-\mu_0)
\leq\frac{p(n-1)}{n-p}F_{p,n-p;1-\alpha}\right\},
$$
where the last subscript denotes the lower-tail quantile. The finite-sample calibration comes from Hotelling's statistic and its central $F$ distribution under the true mean. Covariance-divisor conventions must be matched when converting the statistic to an $F$ variable.{{cite:pan_zhou2011_hotelling}} (§1, Remark 1, covariance divisor $n$ and corresponding $F$ scaling)

The statement of coverage is $P_\mu\{\mu\in C(X_1,\ldots,X_n)\}=1-\alpha$. The random object is the region produced by a new sample. The fixed true mean is inside or outside the particular observed region; frequentist coverage does not itself assign that fixed mean a posterior distribution.{{cite:friendly_monette_fox2013}} (§4.6, joint confidence coverage)

## Interpretation — Principal axes show joint uncertainty
Write $S=U\operatorname{diag}(\lambda_1,\ldots,\lambda_p)U^\top$ and let $c$ be the right-hand threshold for $T^2$. In principal coordinates $z=U^\top(\mu_0-\bar X)$, the region is
$$
\sum_{j=1}^p\frac{z_j^2}{c\lambda_j/n}\leq1.
$$
Its centre is $\bar X$, its axes are the eigenvectors of $S$, and its semi-axis lengths are $\sqrt{c\lambda_j/n}$. A larger variance eigenvalue corresponds to a longer uncertainty axis.{{cite:friendly_monette_fox2013}} (§§2.1–2.2, ellipsoid representations)

The confidence ellipsoid describes the mean vector. An ellipsoid for individual observations has a different scale: averaging reduces covariance from $\Sigma$ to $\Sigma/n$. Plotting a data contour and calling it a confidence region for the mean confuses these two random objects.{{cite:friendly_monette_fox2013}} (§§2.2–3, statistical and data ellipsoids)

## Worked example
Take $n=20$, $p=2$, observed mean $(1,0.5)^\top$, and
$$
S=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
$$
At $95\%$ confidence, the $F_{2,18}$ quantile is approximately $3.554557$, so $c=2(19)3.554557/18\approx7.504065$. The covariance eigenvalues are three and one, with unit eigenvectors $(1,1)^\top/\sqrt2$ and $(1,-1)^\top/\sqrt2$. The confidence semi-axes are approximately $1.06095$ and $0.61254$.{{cite:pan_zhou2011_hotelling}} (§1, Remark 1);{{cite:friendly_monette_fox2013}} (§2.2)

For the proposed mean $(0,0)^\top$, the observed quadratic statistic is $10$, exceeding $7.504065$, so that mean lies outside the region. For the proposed mean $(1,0)^\top$, the displacement is $(0,0.5)^\top$, giving $T^2=10/3$, which lies inside. The covariance affects both comparisons through $S^{-1}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$.{{cite:friendly_monette_fox2013}} (§2.2, quadratic-form geometry)

**Your turn.** At the same threshold $c$, multiply every entry of $S$ by four. How do the centre and semi-axis lengths change?

::: {.callout-tip collapse="true" title="Answer"}
The centre remains the observed mean. Every covariance eigenvalue is multiplied by four, so each semi-axis length doubles. The axis directions are unchanged.
:::

## Assumptions and limits — Rank and the dimension of the problem
The centred covariance has rank at most $n-1$. If $p\geq n$, its ordinary inverse is unavailable. Replacing it by a generalised inverse changes the statistic and requires a corresponding calibration; it cannot preserve the displayed reference law by notation alone. Large-dimensional inference is a separate setting in which the relation between dimension and sample size matters.{{cite:pan_zhou2011_hotelling}} (§1)

[]{#property-hotelling-null-calibration}

The exact normal-sample $F$ calibration relies on the Gaussian sampling law and the covariance estimate's distribution, in addition to the algebra of the ellipsoid. Those sampling assumptions should accompany a reported region.{{cite:pan_zhou2011_hotelling}} (§1, Remark 1)

