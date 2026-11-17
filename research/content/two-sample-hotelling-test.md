## Motivating example
Two groups may differ across several correlated measurements without any single coordinate showing a decisive univariate difference. Hotelling's two-sample statistic measures the joint mean difference relative to a pooled covariance, accounting for the scale and correlation of those measurements.{{cite:garthwaite_koch2016_quadratic}} (§5.1(b), eq. 9)

## Statement
Let the two independent random samples have sizes $n_1,n_2\ge2$ and distributions $N_p(\mu_1,\Sigma)$ and $N_p(\mu_2,\Sigma)$, with a common positive-definite covariance. Put $N=n_1+n_2$, assume $N>p+1$, and use unbiased within-group covariance estimates $S_1,S_2$. Define
$$
S_p=\frac{(n_1-1)S_1+(n_2-1)S_2}{N-2},\qquad
T^2=\frac{n_1n_2}{N}(\overline X_1-\overline X_2)^\top S_p^{-1}(\overline X_1-\overline X_2).
$$
Under the normal model $S_p$ is invertible with probability one at the stated dimension bound. The pooling uses variation around each group's own mean, not around the grand mean.{{cite:garthwaite_koch2016_quadratic}} (§5.1(b), eq. 9)

Under $H_0:\mu_1=\mu_2$,
$$
F=\frac{N-p-1}{p(N-2)}T^2\sim F_{p,N-p-1}.
$$
Thus the exact level-$\alpha$ rule rejects for an $F$ value above its lower-tail $1-\alpha$ quantile. The $F$ distribution applies to the scaled statistic; $T^2$ itself has a different scale. []{#property-hotelling-f-calibration} The general finite-sample calibration uses the normal sample mean and covariance distribution.{{cite:ackermann_strimmer2009_genesets}} (§ “Hotelling's T²-test and related methods”, Appendix)

## Proof
For an invertible linear transformation $A$, the mean difference becomes $Ad$ and the covariance becomes $AS_pA^\top$. Since $(AS_pA^\top)^{-1}=A^{-\top}S_p^{-1}A^{-1}$, the quadratic form is unchanged. Translations cancel in the mean difference. Consequently changing units or rotating all measurements consistently does not change the statistic. Its covariance adjustment measures the difference in a common multivariate geometry.{{cite:garthwaite_koch2016_quadratic}} (§5.1, quadratic forms)

When $p=1$, $T^2$ is exactly the squared equal-variance two-sample $t$ statistic. The multiplier becomes one, so the stated $F$ law reduces to $t_{N-2}^2\sim F_{1,N-2}$. The pooled scalar residual sum is chi-square with $N-2$ degrees of freedom and independent of the mean difference, supplying a direct proof of this special case.{{cite:siegrist2022_normals}} (§ “The T Variable”)

## Worked example
Let $n_1=n_2=10$, $p=2$, mean difference $d=(1.5,1)^\top$, and pooled covariance $S_p=\begin{pmatrix}2&1\\1&2\end{pmatrix}$. Solving $S_pv=d$ gives $d^\top v=7/6$. Hence $T^2=35/6=5.833333$ and $F=(17/36)T^2=2.754630$. The $0.95$ quantile of $F_{2,17}$ is $3.591531$, and the upper-tail probability is $0.091991$. The joint test therefore does not reject at level $0.05$.

**Your turn.** In the same example, double the first coordinate of every measurement. Find the new mean difference and pooled covariance, and determine whether the test changes.

::: {.callout-tip collapse="true" title="Answer"}
The difference becomes $(3,1)^\top$ and the covariance becomes $\begin{pmatrix}8&2\\2&2\end{pmatrix}$. Their quadratic form remains $7/6$, so $T^2$, the $F$ value and the decision are unchanged.
:::

## Common misconceptions — Regularisation changes the test
If the covariance estimate is singular, substituting a pseudoinverse or a shrinkage estimate defines a different statistic. Its calibration requires its own argument. Similarly, unequal population covariances break the common-covariance model underlying pooling; equal sample sizes do not by themselves restore that assumption. High-dimensional applications therefore need a procedure whose covariance estimation and null calibration are designed together.{{cite:ackermann_strimmer2009_genesets}} (§ “Hotelling's T²-test and related methods”, Appendix)
