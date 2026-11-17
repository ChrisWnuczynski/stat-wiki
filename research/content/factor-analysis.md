## Motivating example

Several test scores may move together through a few latent abilities while each score also has its own measurement noise. Factor analysis models the shared covariance through low-dimensional factors and separates it from coordinate-specific residual variance. It thereby asks which variation is common, rather than merely which projections have the largest total variance.{{cite:deisenroth_faisal_ong2020}} (§10.7, pp.345–346)

## Definition — Shared factors and specific variation

A Gaussian factor model is
$$X=\mu+\Lambda F+\epsilon,\qquad F\sim N_q(0,I_q),\quad
 \epsilon\sim N_p(0,\Psi),\quad F\perp\epsilon,$$
where $\Psi$ is diagonal with nonnegative entries. Hence $E(X)=\mu$ and $\Sigma=\Lambda\Lambda^T+\Psi$. Off-diagonal covariances come from the factors; the diagonal residual matrix allows different noise levels for different coordinates. Probabilistic PCA uses the more restrictive $\Psi=\sigma^2I$.{{cite:deisenroth_faisal_ong2020}} (§10.7, p.346)

## Properties — Rotation and identification

For an orthogonal $q\times q$ matrix $Q$, replacing $\Lambda$ by $\Lambda Q$ leaves $\Lambda\Lambda^T$ unchanged. With spherical Gaussian factors, rotating the latent factors correspondingly also leaves the observable distribution unchanged. The covariance alone therefore does not select unique factor axes. Sign reversals are the one-factor instance of this ambiguity.{{cite:dempster_laird_rubin1977}} (§3, p.10; §4.7, pp.20–21)

Counting free parameters is a useful necessary check on identification, though it is not a complete proof. For one factor and two observed variables, two loadings and two residual variances must describe only three distinct covariance entries. Additional constraints or information are needed. For three variables with one factor and nonzero cross-covariances, the equations imply $\lambda_1^2=\Sigma_{12}\Sigma_{13}/\Sigma_{23}$ when that quotient is positive. Residual variances must still be nonnegative.{{cite:deisenroth_faisal_ong2020}} (§10.7, p.346)

## Worked example

Take $\Lambda=(0.8,0.6,0.5)^T$ and $\Psi=\operatorname{diag}(0.36,0.64,0.75)$. Then
$$\Sigma=\begin{pmatrix}1&0.48&0.40\\0.48&1&0.30\\0.40&0.30&1\end{pmatrix}.$$
The common variance fractions are $0.64,0.36,0.25$. The first loading can be recovered up to sign from $0.48(0.40)/0.30=0.64$. Changing all loading signs preserves every covariance. The diagonal residual terms represent variation that this one-factor structure does not share across coordinates.{{cite:deisenroth_faisal_ong2020}} (§10.7, p.346)

**Your turn.** Negate every loading in the worked example. What happens to the observable covariance and to the conditional factor mean?

::: {.callout-tip collapse="true" title="Answer"}
The covariance is unchanged because $(-\Lambda)(-\Lambda)^T=\Lambda\Lambda^T$. The conditional mean changes sign, while its variance is unchanged.
:::

## Interpretation — Scores differ from factors

Even at fitted parameter values, an individual's latent factor is uncertain. Completing the Gaussian square gives
$$F\mid X=x\sim N_q\left(V\Lambda^T\Psi^{-1}(x-\mu),V\right),
\qquad V=(I+\Lambda^T\Psi^{-1}\Lambda)^{-1},$$
when $\Psi$ is positive definite. In the one-factor example with $\mu=0$ and $x=(1,0,-1)^T$, the conditional mean is $0.423440$ and variance is $0.272212$. A factor-score estimate is a summary of this conditional distribution, not a directly observed measurement.{{cite:deisenroth_faisal_ong2020}} (§6.5.2, p.201, Eqs.6.74–6.75)

## Statistical use — Likelihood and latent-variable fitting

EM can treat the factors as missing data and use their conditional first and second moments in its E-step. Estimation must account for rotation ambiguities and possible boundary solutions with zero residual variances. Interpreting fitted axes requires identifying constraints or an explicit choice of rotation.{{cite:dempster_laird_rubin1977}} (§4.7, pp.20–21; discussion, p.30)


## Check yourself

### [Two factors of one covariance](../questions/ex-sl-02-3.qmd) {#self-check-ex-sl-02-3}

::: {.callout-tip collapse="true" title="Answer"}
For $\Sigma=\left(\begin{smallmatrix}4&2\\2&3\end{smallmatrix}\right)$, the Cholesky factor is $L=\left(\begin{smallmatrix}2&0\\1&\sqrt2\end{smallmatrix}\right)$. A spectral factor also satisfies $BB^T=\Sigma$. Both transform a standard normal vector to covariance $\Sigma$, although they need not give the same transformed vector for a fixed draw.
:::

### [The effect of correlation](../questions/ex-sl-03-3.qmd) {#self-check-ex-sl-03-3}

::: {.callout-tip collapse="true" title="Answer"}
For $\left(\begin{smallmatrix}1&r\\r&1\end{smallmatrix}\right)$ with $r>0$, the eigenvalues are $1+r$ and $1-r$, along the sum and difference directions. The first principal component explains fraction $(1+r)/2$, tending to $1/2$ as $r\to0$ and to one as $r\to1$.
:::
