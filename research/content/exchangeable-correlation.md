## Motivating example

Four measurements from one child share a subject and may be correlated. An exchangeable working correlation assigns the same association to every pair, even when the visits occur at different times. This is useful when the common subject effect matters more than lag, but it does not encode a decay of association with time separation.{{cite:liang_zeger1986}} (§4, p.18, Ex.3)

## Definition — One correlation for every pair

For $K\ge2$ standardised measurements, the correlation matrix is
$$R(\rho)=(1-\rho)I_K+\rho\mathbf1\mathbf1^T.$$
Its diagonal entries are one and every off-diagonal entry is $\rho$. Exchangeable correlation specifies second moments; it does not by itself assert that the entire joint distribution is invariant under permutations.{{cite:liang_zeger1986}} (§3.1, pp.15–16; §4, p.18, Ex.3)

## Properties — The admissible range

The all-ones vector has eigenvalue $1+(K-1)\rho$, while every vector orthogonal to it has eigenvalue $1-\rho$. Positive semidefiniteness therefore holds exactly when
$$-\frac1{K-1}\le\rho\le1.$$
Strict inequalities give a positive definite matrix. At the lower boundary the sum of the standardised measurements has zero variance. At the upper boundary every pair of standardised measurements agrees almost surely. Distinct raw means or scales can still give different raw values. This follows from the covariance identity $\operatorname{Var}(a^TX)=a^T\Sigma a$.{{cite:deisenroth_faisal_ong2020}} (§6.4.4, pp.194–195)

In the interior,
$$R^{-1}=\frac1{1-\rho}\left[I_K-\frac{\rho}{1+(K-1)\rho}\mathbf1\mathbf1^T\right],\qquad
\det R=(1-\rho)^{K-1}[1+(K-1)\rho].$$
Multiplying the proposed inverse by $R$ proves the identity. The spectral decomposition explains both singular boundaries.{{cite:deisenroth_faisal_ong2020}} (§4.4, “Eigendecomposition and Diagonalization”)

## Worked example

For four measurements and $\rho=0.3$, the eigenvalues are $0.7$ three times and $1.9$ once; the determinant is $0.6517$. If each raw measurement has variance $\sigma^2$, their mean has variance
$$\operatorname{Var}(\bar X)=\frac{\sigma^2}{4}(1+3\rho)=0.475\sigma^2.$$
An independence calculation would give $0.25\sigma^2$. A proposal $\rho=-0.5$ instead gives eigenvalue $-0.5$ in the mean direction and cannot be a correlation matrix.{{cite:deisenroth_faisal_ong2020}} (§6.4.4, pp.194–195)

**Your turn.** Can five measurements have exchangeable correlation $-0.3$?

::: {.callout-tip collapse="true" title="Answer"}
No. The lower bound is $-1/(5-1)=-0.25$; the eigenvalue along the all-ones vector would be $1+4(-0.3)=-0.2$.
:::

## Interpretation — A random intercept and a working matrix

With $X_{ij}=\mu_{ij}+U_i+\epsilon_{ij}$, independent mean-zero subject effects of variance three and errors of variance seven give total variance ten and correlation $0.3$. Such a random-intercept construction produces nonnegative correlation. Negative exchangeable correlation can be valid for a fixed cluster size, but cannot be obtained by giving a random-intercept variance a negative value.{{cite:liang_zeger1986}} (§4, p.18, Ex.3)

GEE uses this matrix as a working association model. With correctly specified marginal means, many independent clusters, regularity, suitable nuisance estimation and the stated missingness assumptions, the regression estimator remains consistent when the working correlation is wrong. A cluster sandwich covariance addresses coefficient uncertainty; it does not correct a wrong mean model.{{cite:liang_zeger1986}} (§3.1, pp.15–16)


## Check yourself

### [A correlation four visits cannot have](../questions/ex-ur-exchangeable-bound.qmd) {#self-check-ex-ur-exchangeable-bound}

::: {.callout-tip collapse="true" title="Answer"}
Four visits require $\rho\ge-1/3$. At $-0.5$ the mean-direction eigenvalue is negative, so the proposed matrix is impossible.
:::

### [Working correlation and mean validity](../questions/depth-marginal-working-covariance.qmd) {#self-check-depth-marginal-working-covariance}

::: {.callout-tip collapse="true" title="Answer"}
With many independent clusters, regularity and suitable missingness, the analyst with the correct marginal mean has the usual GEE consistency argument even with a wrong working correlation. A sandwich estimates uncertainty about that estimating equation. It cannot repair an omitted mean covariate.
:::
