## Motivating example
A normalizing constant may look like a technical adjustment that merely makes a density integrate to one. In an exponential family, its logarithm contains the mean and covariance of the sufficient statistic. Differentiation therefore turns normalization into statistical information. This is useful for estimating parameters, calculating curvature and checking whether a proposed exponential-family representation is internally consistent.{{cite:wainwright_jordan2008}} (§3.5.1, prop. 3.1, pp. 61–63)

For example, the Bernoulli family can be parameterized by log odds rather than by probability. Its log normalizer is a smooth function of the log odds; its first derivative gives the success probability and its second derivative gives the Bernoulli variance. The two derivatives describe the same probability law in different statistical roles.{{cite:wainwright_jordan2008}} (§3.2, tab. 3.1, p. 42)

## Statement
Write a regular exponential-family density relative to a measure $\nu$ as
$$p_\eta(x)=h(x)\exp\{\eta^\top T(x)-A(\eta)\},\qquad A(\eta)=\log\int h(x)e^{\eta^\top T(x)}\,d\nu(x).$$
At an interior natural parameter where differentiation under the integral is valid,
$$\nabla A(\eta)=\E_\eta[T(X)],\qquad\nabla^2A(\eta)=\operatorname{Cov}_\eta[T(X)].$$
The support and base measure are fixed as $\eta$ varies. Differentiating with respect to a transformed parameter generally introduces chain-rule factors and does not give these same expressions without adjustment.{{cite:wainwright_jordan2008}} (§§3.2, 3.5.1, eqs. 3.5–3.7, 3.41)

## Proof
Put $Z(\eta)=e^{A(\eta)}$. Differentiating $Z$ gives $\partial_j Z=\int T_j(x)h(x)e^{\eta^\top T(x)}d\nu(x)$. Division by $Z$ converts that integral to an expectation under $p_\eta$. For the second derivative,
$$\partial_{jk}A=\frac{\partial_{jk}Z}{Z}-\frac{(\partial_jZ)(\partial_kZ)}{Z^2}=\E(T_jT_k)-\E(T_j)\E(T_k).$$
The quotient rule is responsible for the subtraction of the product of means. At a regular interior parameter, an exponential-moment bound from a small neighboring parameter region justifies the required differentiation and moments.{{cite:wainwright_jordan2008}} (§3.5.1, proof of prop. 3.1)

The Hessian is positive semidefinite because $a^\top\nabla^2A\,a=\operatorname{Var}(a^\top T)\ge0$. It is positive definite precisely when no nonzero linear combination of the sufficient statistics is constant almost surely. Such a minimal representation removes a parameter redundancy. A zero curvature direction can therefore reflect a redundant statistic rather than an absence of data.{{cite:wainwright_jordan2008}} (§3.5.1, prop. 3.1(b))

## Key results — Likelihood scores inherit the same geometry
For independent observations with common parameter, the log likelihood is $\eta^\top\sum_iT(x_i)-nA(\eta)$ plus a constant. Its score is $\sum_iT(x_i)-n\nabla A(\eta)$, and its Hessian is $-n\nabla^2A(\eta)$. A finite interior maximum therefore matches the modeled mean sufficient statistic to the observed average. Concavity follows from the covariance identity. Boundary samples can prevent a finite solution even though the likelihood remains concave.{{cite:wainwright_jordan2008}} (§3.4.2, eq. 3.38, pp. 60–61)

For a one-parameter exponential-dispersion model with log density $\{y\theta-b(\theta)\}/a(\phi)+c(y,\phi)$, the corresponding identities are $\E(Y)=b'(\theta)$ and $\operatorname{Var}(Y)=a(\phi)b''(\theta)$. The dispersion factor appears because the natural parameter for $Y$ is $\theta/a(\phi)$. Keeping that factor explicit avoids confusing a log-partition derivative with a response variance in a different parameterization.{{cite:nelder_wedderburn1972}} (§1.1, p. 371, eqs. 3–6)

## Worked example
### Bernoulli log odds
For $X\in\{0,1\}$ and $\eta=\log\{p/(1-p)\}$, the density is $\exp\{\eta X-\log(1+e^\eta)\}$. Thus $A(\eta)=\log(1+e^\eta)$, $A'(\eta)=e^\eta/(1+e^\eta)=p$, and $A''(\eta)=p(1-p)$. At $\eta=\log3$, the normalizer is four, the log normalizer is $\log4=1.386294$, the mean is $3/4=0.75$ and the variance is $3/16=0.1875$. Summing the two probability masses verifies the derivatives directly.{{cite:wainwright_jordan2008}} (§§3.2, 3.5.1, tab. 3.1 and prop. 3.1)

For four observations with three successes, the score is $3-4p$. It vanishes at $p=3/4$, corresponding to $\eta=\log3$. Its derivative there is $-4p(1-p)=-3/4$. If all four observations are successes, the score is positive for every finite $\eta$ and the likelihood's supremum is approached as $\eta\to\infty$. A score equation need not have a finite root.

**Your turn.** For a Poisson variable in natural parameter $\eta=\log\lambda$, the log normalizer is $A(\eta)=e^\eta$. Find the mean and variance at $\eta=\log2$.

::: {.callout-tip collapse="true" title="Answer"}
Both the first and second derivatives equal $e^\eta$. Hence the mean and variance both equal two.
:::

## Generalizations — Several statistics and a singular covariance
If $T(X)=(X,2X)^\top$ for a Bernoulli variable, then $\operatorname{Cov}(T)=p(1-p)\begin{pmatrix}1&2\\2&4\end{pmatrix}$. Its determinant is zero because $2T_1-T_2=0$ identically; the vector $(2,-1)^\top$ is a null direction. Only $\eta_1+2\eta_2$ affects the density, so separate identification of the two natural parameters is impossible. This example connects analytic curvature, statistical covariance and parameter redundancy in one calculation.{{cite:wainwright_jordan2008}} (§§3.2, 3.5.1, minimal representations)

A singular covariance means some linear combination of the statistics is constant, so that direction carries no second-moment information even though the mean identities still hold on the range of the covariance.

The Poisson check is the one-parameter case of the same derivatives. With $A(\eta)=e^\eta$ and $\eta=\log 2$, both $A'(\eta)$ and $A''(\eta)$ equal $2$, so the mean and the variance are both $2$. The Bernoulli point $\eta=\log 3$ separates them: the mean is $3/4$ and the variance is $3/16$.{{cite:wainwright_jordan2008}} (§§3.2, 3.5.1, tab. 3.1 and prop. 3.1)
