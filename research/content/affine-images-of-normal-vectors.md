## Motivating example
A device reports the sum and a contrast of two noisy measurements. Separate normal marginal distributions do not suffice to determine the joint law of those reports. Joint normality does: every affine transformation is again Gaussian, with its covariance determined by the whole covariance matrix, including cross terms.{{cite:pishro_nik2014}} (§6.1.5, normal random vectors)

## Statement
Let $X\sim N_p(\mu,\Sigma)$, allowing a positive semidefinite covariance matrix. For a fixed $q\times p$ matrix $A$ and fixed vector $b$,
$$
AX+b\sim N_q(A\mu+b,A\Sigma A^\top).
$$
This includes constant coordinates and singular image distributions. In one dimension, independent $X_i\sim N(\mu_i,\sigma_i^2)$ give $a+\sum_i b_iX_i\sim N(a+\sum_i b_i\mu_i,\sum_i b_i^2\sigma_i^2)$. With correlated jointly normal inputs, the variance is instead $b^\top\Sigma b$.{{cite:durrett2019}} (§3.10, pp. 201–203){{cite:pishro_nik2014}} (§6.1.5)

## Proof
For any $c\in\mathbb R^q$, $c^\top(AX+b)=(A^\top c)^\top X+c^\top b$ is normal by the linear-combination definition of a Gaussian vector. Its mean is $c^\top(A\mu+b)$ and variance $c^\top A\Sigma A^\top c$. These are exactly the one-dimensional projections of the asserted Gaussian law. The argument also covers a projection with variance zero, interpreted as a constant.{{cite:pishro_nik2014}} (§6.1.5)

## Generalizations — Singular images and normal marginals
If $A$ has deficient row rank, a Gaussian image can lie on a lower-dimensional affine subspace. For example, $(Z,2Z)$ with $Z\sim N(0,1)$ has covariance $\left(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\right)$ and no two-dimensional density. An invertible transformation permits a density change of variables; the linear-combination proof does not require invertibility.{{cite:durrett2019}} (§3.10, pp. 201–202)

Joint normality is stronger than normality of each coordinate. Let an independent fair sign $S$ multiply $Z\sim N(0,1)$. Both $Z$ and $SZ$ are standard normal, but their sum is exactly zero with probability $1/2$ and has a continuous normal component otherwise. It is neither a nondegenerate normal variable nor a constant. This supplies a direct counterexample to inferring affine Gaussian closure from marginal normality alone.{{cite:pishro_nik2014}} (§6.1.5, linear-combination definition)

## Worked example

### A sum and a contrast
Let $\mu=(1,2)^\top$, $\Sigma=\left(\begin{smallmatrix}4&1\\1&9\end{smallmatrix}\right)$, and define $U=X_1+X_2-1$, $V=2X_1-X_2+3$. Then
$$
\begin{pmatrix}U\\V\end{pmatrix}\sim
N_2\!\left[\begin{pmatrix}2\\3\end{pmatrix},
\begin{pmatrix}15&0\\0&21\end{pmatrix}\right].
$$
For instance, $\operatorname{Cov}(U,V)=2(4)+(2-1)(1)-9=0$. The transformed pair is jointly Gaussian and its diagonal quadratic density factors into one-dimensional normal densities, so $U$ and $V$ are independent. Independence of the inputs was unnecessary; their covariance was used explicitly.{{cite:durrett2019}} (§3.10, pp. 201–203)

The scalar manufacturing calculations use the same rule. Independent measurements with variances $0.01$ and $0.04$ and means $1$ and $1.1$ have difference $N(0.1,0.05)$, giving probability $0.67264$ of a positive difference. A single board thickness $N(0.151,0.003^2)$ lies between $0.146$ and $0.154$ with probability $0.79355$. For the mean of $25$ independent boards the standard deviation is $0.0006$ and that probability becomes $0.9999997133$.{{cite:pishro_nik2014}} (§6.1.5)

**Your turn.** What are the mean and variance of $2U-V$ in the bivariate example?

::: {.callout-tip collapse="true" title="Answer"}
Its mean is $2(2)-3=1$ and its variance is $4(15)+21=81$. The covariance term vanishes, so $2U-V\sim N(1,81)$.
:::
