## Motivating example

Two populations differ in several measurements, some noisy and some precise. Projecting along their raw mean difference treats those measurements as if their scales and within-group associations were comparable. Fisher's criterion instead rewards a projected mean gap relative to projected within-group variation.{{cite:witten_tibshirani2011_fisher}} (§2.1)

## Statement

Let $S$ be positive definite and $d=\mu_1-\mu_2$. For nonzero $a$, define
$$J(a)=\frac{(a^Td)^2}{2a^TSa}.$$
If $d\ne0$, its maximum is $d^TS^{-1}d/2$, attained exactly by nonzero multiples of $S^{-1}d$. The factor $1/2$ corresponds to adding the squared deviations of the two projected means from their midpoint. Changing that convention multiplies all criterion values by a constant without changing the maximizing direction.{{cite:witten_tibshirani2011_fisher}} (§2.1)

## Proof

Set $u=S^{1/2}a$ and $v=S^{-1/2}d$. The Cauchy–Schwarz inequality gives $(a^Td)^2=(u^Tv)^2\le(u^Tu)(v^Tv)=(a^TSa)(d^TS^{-1}d)$. Equality holds exactly when $u$ and $v$ are parallel, giving the stated direction. If $d=0$, every numerator is zero and every nonzero direction attains the same value zero.{{cite:deisenroth_faisal_ong2020}} (§3.3, p.75, Eq.3.17)

## Intuition — Whitening before measuring the gap

The transformation $S^{-1/2}$ makes within-group covariance the identity. In those coordinates the best projection points along the transformed mean difference. Returning to the measurement coordinates gives the inverse-covariance weighting. This explains why correlated measurements should not simply count the same shared information twice.{{cite:deisenroth_faisal_ong2020}} (§3.2, pp.73–74; §3.3, p.75)

## Worked example

For $S=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)$ and $d=(2,1)^T$, solving $Sa=d$ gives $a=(1,0)^T$. Its criterion is $J=1$. The raw mean-difference direction has $(d^Td)^2=25$ and $d^TSd=14$, giving $25/28\approx0.892857$. The second coordinate adds no further mean separation once its covariance with the first has been accounted for.{{cite:witten_tibshirani2011_fisher}} (§2.1)

**Your turn.** For $S=\operatorname{diag}(2,1)$ and $d=(2,2)^T$, compare the optimum with the raw difference direction.

::: {.callout-tip collapse="true" title="Answer"}
The optimum is proportional to $(1,2)^T$ and attains $d^TS^{-1}d/2=3$. The raw difference gives $64/(2\cdot12)=8/3$, which is smaller.
:::

## Related concepts — Classification needs a threshold

The direction alone does not choose an intercept or classification threshold. Under a common-covariance normal model, the log posterior odds are linear with coefficient $\Sigma^{-1}(\mu_1-\mu_0)$ and an intercept involving the class priors and the two means. Fisher's projection criterion itself needs means and a within-group covariance, rather than a normal distribution assumption. High-dimensional estimation is more delicate when the estimated within-group covariance is singular; regularisation changes the optimization problem.{{cite:witten_tibshirani2011_fisher}} (§§1–2.1)
