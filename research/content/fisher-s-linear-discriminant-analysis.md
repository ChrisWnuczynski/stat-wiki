## Lead context
The direction separates projected class centres relative to variation within the classes; choosing a decision threshold is a further step.

## Motivating example
Two measurements may both distinguish two species, yet contain nearly the same information. Adding their raw differences can overemphasise a noisy common direction. A projection can instead reward a large difference between class means while penalising its within-class variation. This is the central criterion of Fisher's discriminant construction.{{cite:fisher1936}} (§§I–II, p. 179)

## Definition — Separation after accounting for covariance
Let $d=\mu_1-\mu_2$ and let $S$ be a positive-definite within-class covariance matrix. For a nonzero direction $a$, use
$$
J(a)=\frac{(a^\top d)^2}{2a^\top Sa}.
$$
The factor two corresponds to adding the projected variances of two classes sharing covariance $S$; omitting it changes the criterion's value but not its maximising direction. Multiplying $a$ by any nonzero scalar also leaves $J$ unchanged. The optimisation is a statement about means and covariances and does not require normal class distributions.{{cite:fisher1936}} (§II, p. 179)

## Properties — Whitening the within-class variation
Set $u=S^{1/2}a$ and $v=S^{-1/2}d$. Then
$$
J(a)=\frac{(u^\top v)^2}{2\|u\|^2}\le\frac{\|v\|^2}{2}
=\frac12d^\top S^{-1}d.
$$
Cauchy–Schwarz gives equality precisely when $u$ is parallel to $v$, for $d\ne0$. Hence $a\propto S^{-1}d$. Covariance weighting rescales and rotates the contrast before projecting it; it is more than dividing each coordinate by a separate variance when predictors are correlated.{{cite:fisher1936}} (§II, p. 179){{cite:boyd_vandenberghe2004}} (§A.5.2, symmetric eigenvalue decomposition)

If $d=0$, every nonzero direction has criterion zero. If $S$ is singular, the inverse expression is unavailable. A direction in the null space with $a^\top d\ne0$ has zero within-class variation and nonzero separation, so its ratio has no finite bound. A pseudoinverse alone does not resolve that case. If $d$ lies in the range of $S$, the same proof can be applied on that range, with null directions leaving the projection criterion unchanged.{{cite:boyd_vandenberghe2004}} (§§A.5.1–A.5.2)

## Interpretation — A direction is not a complete rule
Under a Gaussian class model with a common covariance matrix, the log posterior odds are affine in $x$, with coefficient $\Sigma^{-1}(\mu_1-\mu_0)$. This supplies a probabilistic interpretation of the Fisher direction. Class priors and error costs affect the threshold; the direction alone does not specify those quantities. Different covariance estimates, class weights, and regularisation choices can therefore produce different fitted classifiers.{{cite:lindholm2022_ml}} (§10.1, pp. 248–252)

Estimating a separate covariance for each class gives quadratic discriminant analysis. Sharing a covariance reduces the number of fitted covariance parameters, but also imposes a substantive model restriction. Positive definiteness requires enough observations spanning the predictor space, not merely a sufficiently large total sample count.{{cite:lindholm2022_ml}} (§10.1, pp. 250–252)

## Worked example
Take class means $\mu_0=(0,0)^\top$, $\mu_1=(2,1)^\top$ and
$$
S=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
$$
Then $S^{-1}d=(1,0)^\top$ and $J_{\max}=1$. Projecting in the raw mean-difference direction $d=(2,1)^\top$ gives
$$
J(d)=\frac{25}{28}\approx0.892857.
$$
The second coordinate's mean difference is redundant for the optimal linear contrast in this example: its correlation with the first coordinate changes the covariance-adjusted direction. With equal Gaussian priors and equal error costs, the optimal boundary is $x_1=1$, the midpoint of the projected class centres.{{cite:lindholm2022_ml}} (§10.1, linear discriminant analysis)

**Your turn.** What happens to the maximum separation if both covariance eigenvalues are doubled while the means stay fixed?

::: {.callout-tip collapse="true" title="Answer"}
Replacing $S$ by $2S$ halves every value of $J(a)$. The optimal direction is proportional to $(2S)^{-1}d=(1/2,0)^\top$, the same projection direction, and the maximum becomes $1/2$.
:::
