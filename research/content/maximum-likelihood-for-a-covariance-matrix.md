## Motivating example
Several instruments measure different coordinates on each specimen. Estimating their joint uncertainty requires a matrix of variances and covariances, rather than separate error bars alone. In a multivariate normal model, maximum likelihood fits this matrix from the centered observation cloud. The resulting divisor is the sample size, while the familiar unbiased covariance uses one fewer degree of freedom. The two estimators optimize different criteria.{{cite:goodfellow_bengio_courville2016}} (§5.4.2, bias of variance estimation)

## Intuition — Precision makes the objective concave
Assume $x_i\in\mathbb R^p$ are independent with common law $N_p(\mu,\Sigma)$ and $\Sigma$ positive definite. Put $A=\sum_i(x_i-\overline x)(x_i-\overline x)^\top$ and $S=A/n$. After maximizing the mean at $\overline x$, the precision objective is
$$\ell(\Theta)=\frac n2\{\log|\Theta|-\operatorname{tr}(S\Theta)\}+\text{constant},\quad\Theta=\Sigma^{-1}\succ0.$$
The determinant controls volume, while the trace charges for how strongly the precision penalizes the observed scatter. Both terms are needed: minimizing only the trace would send the precision toward zero.{{cite:wainwright_jordan2008}} (§3.3, Gaussian exponential-family representation)

## Properties — Existence and the divisor
If $S\succ0$, the unique maximum has $\widehat\Theta=S^{-1}$ and $\widehat\Sigma=S$. One direct proof uses $B=S^{1/2}\Theta S^{1/2}$. Relative to $\Theta=S^{-1}$ the objective difference is
$$\frac n2\{\log|B|-\operatorname{tr}(B)+p\}=\frac n2\sum_j(\log b_j-b_j+1)\le0,$$
where $b_j>0$ are its eigenvalues. The inequality follows from $\log t\le t-1$, with equality only at one. It proves the global maximum without relying solely on a zero derivative.{{cite:goodfellow_bengio_courville2016}} (§3.13, information-theoretic inequalities)

If $S$ is singular, choose a unit vector $v$ with $Sv=0$ and let $\Theta_t=I+t vv^\top$. Then $\operatorname{tr}(S\Theta_t)=\operatorname{tr}S$ but $\log|\Theta_t|=\log(1+t)\to\infty$. Thus no positive definite covariance attains a finite maximum. Since centered residuals sum to zero, $\operatorname{rank}(A)\le\min(p,n-1)$; $n>p$ is necessary but an arbitrary dataset must also span all directions after centering. Under a nonsingular normal model with $n>p$, full rank occurs with probability one.

The identity $A=\sum_i(X_i-\mu)(X_i-\mu)^\top-n(\overline X-\mu)(\overline X-\mu)^\top$ gives $\E(A)=(n-1)\Sigma$. Hence $S$ has expectation $(n-1)\Sigma/n$, while $A/(n-1)$ is unbiased. If the mean is known, centering at that fixed mean gives a different scatter with expectation $n\Sigma$ and divisor $n$.{{cite:goodfellow_bengio_courville2016}} (§5.4.2, variance estimator bias)

## Worked example — A two-coordinate cloud
For $(0,0),(2,0),(0,2),(2,2)$, the sample mean is $(1,1)$. Summing centered outer products gives $A=\operatorname{diag}(4,4)$, so the covariance MLE and precision MLE are both $I_2$. The unbiased covariance is $(4/3)I_2$. Changing the points to $(0,0),(1,1),(2,2)$ gives $A=\begin{pmatrix}2&2\\2&2\end{pmatrix}$, which has eigenvalues four and zero. The formal matrix $A/3$ is singular, and therefore is outside the positive definite parameter space.

**Your turn.** For four points $(0,0),(4,0),(0,2),(4,2)$, find the mean, covariance MLE and precision MLE.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $(2,1)$ and the scatter is $\operatorname{diag}(16,4)$. The covariance MLE is $\operatorname{diag}(4,1)$, and its inverse is $\operatorname{diag}(1/4,1)$.
:::

## Assumptions and limits
A diagonal or sparse covariance model restricts the parameter space and can have a different maximizer. Adding a penalty can produce a positive definite estimate when the unpenalized problem is singular, but it solves a different optimization problem. The unrestricted Gaussian fit is also sensitive to extreme observations because scatter uses squared deviations. A covariance matrix that can be computed algebraically is not necessarily an admissible maximum likelihood fit under the stated parameter restrictions.{{cite:wainwright_jordan2008}} (§6.1, fully observed maximum likelihood)

## Statistical use — The divisor and the rank
The unrestricted maximizer divides the centered scatter $A$ by $n$, not by $n-1$. For the four corners of the square, $A=\operatorname{diag}(4,4)$ and both the covariance and the precision maximum likelihood estimates equal $I_2$. The unbiased matrix $(4/3)I_2$ has a larger trace. It minimises mean squared error for the variance entries under a different criterion. It is not the maximizer of the Gaussian likelihood. When the mean is known and centering uses that known vector, the scatter $\sum_i(x_i-\mu)(x_i-\mu)^\top$ has expectation $n\Sigma$, and the likelihood divisor is $n$ for a different matrix. Using $n-1$ there would bias the known-mean estimator.{{cite:goodfellow_bengio_courville2016}} (§5.4.2, variance estimator bias)

The centered scatter of $n$ points in $p$ coordinates has rank at most $\min(p,n-1)$, because the residuals sum to zero. With $n=3$ and $p=4$ the rank is at most $2$, so $S$ is singular and the log-likelihood of a positive definite covariance is unbounded. The same obstruction appears in the three collinear points whose scatter has eigenvalues $4$ and $0$. A sample with $n>p$ can still be singular if the centered points lie in a lower-dimensional flat. Full rank has probability one under a nonsingular normal model when $n>p$, which is a probability statement about that model, not a property of every spreadsheet.

## Common misconceptions
The eigenvalue argument shows why $S$ is the unique maximizer when $S$ is positive definite. Set $B=S^{1/2}\Theta S^{1/2}$. The objective gap relative to $\Theta=S^{-1}$ is $(n/2)\sum_j(\log b_j-b_j+1)$, and $\log t\le t-1$ for $t>0$ with equality only at $t=1$. Every eigenvalue of $B$ must equal one, so $B=I$ and $\Theta=S^{-1}$. A critical-point calculation that stops at the derivative finds the same matrix and does not by itself show it is the only maximum. The inequality does. It requires $S$ positive definite so that $S^{1/2}$ exists inside the positive definite cone. On a singular $S$ the determinant term can be driven to infinity along $I+tvv^\top$ for a null vector $v$, and there is no maximum to find.{{cite:goodfellow_bengio_courville2016}} (§3.13, information-theoretic inequalities)

A shrinkage or graphical penalty that forces zeros, or that pulls eigenvalues away from zero, maximises a penalized objective. The four-point cloud has an unpenalized solution $I_2$, and a penalty would move that solution. Reporting the penalized matrix as the maximum likelihood estimate of an unrestricted covariance uses the likelihood name for a different function. If the scientific model really does restrict the covariance to a diagonal, the maximizer is the diagonal of $S$ in the Gaussian case with a free mean, which agrees with $I_2$ on the square example and would drop an off-diagonal entry in a different cloud. The restriction has to be stated.{{cite:wainwright_jordan2008}} (§6.1, fully observed maximum likelihood){{cite:wainwright_jordan2008}} (§3.3, Gaussian exponential-family representation)
