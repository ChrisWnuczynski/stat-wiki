## Lead context
The logarithm of the normalising integral is a function of the natural parameter. Identifying that parameter before differentiating prevents a change of notation from becoming a change of calculus.{{cite:wainwright_jordan2008}} (§3.2, eqs. 3.5–3.7, pp. 39–40)

## Motivating example
For a Poisson variable with mean $\lambda>0$, the density is $e^{-\lambda}\lambda^x/x!$. The natural parameter is $\eta=\log\lambda$, not $\lambda$. The form $h(x)\exp\{\eta x-A(\eta)\}$ has $h(x)=1/x!$ and $A(\eta)=e^\eta$. The mean and variance both equal $\lambda$.{{cite:dodge2008}} (p. 425){{cite:wainwright_jordan2008}} (p. 42, tab. 3.1)

## Properties — The derivative has a coordinate
Where differentiation under the integral is justified,
$$
A(\eta)=\log\int h(x)e^{\eta^\top T(x)}\,dx,
\qquad \nabla A(\eta)=E_\eta T(X),\quad
\nabla^2 A(\eta)=\operatorname{Cov}_\eta T(X).
$$
The first derivative divides the integral of $T(x)$ times the unnormalised density by its normalising integral. Differentiating again subtracts the outer product of those means, giving covariance. A covariance matrix is positive semidefinite, so $A$ is convex on its natural domain; strict convexity needs a minimal representation.{{cite:wainwright_jordan2008}} (§3.5.1, prop. 3.1, pp. 62–63)

If $\eta=c(\theta)$, the chain rule gives $d\{A(c(\theta))\}/d\theta=A'(c(\theta))c'(\theta)$ in one dimension. Its second derivative also contains $A'(c(\theta))c''(\theta)$. It therefore need not equal a variance or be nonnegative. In the Poisson mean coordinate $A(c(\lambda))=\lambda$ is linear, although $A''(\eta)=e^\eta>0$. This is a distinction between functions and the coordinates used for them.{{cite:wainwright_jordan2008}} (§3.2 and §3.5.1)

## Worked example
At $\lambda=3$, $\eta=\log3$ and $A=3$. The probability of $x=2$ is
$$
\frac12\exp\{2\log3-3\}=\frac92e^{-3}=0.22404.
$$
In normaliser notation, $a(\lambda)=e^\lambda$, $b(x)=1/x!$, $c(\lambda)=\log\lambda$ and $T(x)=x$ give exactly the same value. A Bernoulli variable with $p=3/4$ instead has $\eta=\log3$ and $A(\eta)=\log(1+e^\eta)=\log4$; sharing a natural parameter value does not make two families equal. Their base measures and log normalisers differ.{{cite:wainwright_jordan2008}} (p. 42, tab. 3.1)

For the conjugate kernel $\exp\{\eta\chi-\nu A(\eta)\}$ relative to $d\eta$, multiplication by $n$ independent likelihoods changes $(\chi,\nu)$ to $(\chi+\sum x_i,\nu+n)$. This is simply collection of the coefficients of $\eta$ and $A$. A prior specified relative to $d\lambda$ requires the Jacobian $d\eta/d\lambda=1/\lambda$ when translated to the other coordinate; changing a density's parameter label alone does not transform its underlying measure.

**Your turn.** For Poisson mean $2$, identify $\eta$, $A$ and $P(X=0)$.

::: {.callout-tip collapse="true" title="Answer"}
$\eta=\log2$, $A=2$, and $P(X=0)=e^{-2}=0.13534$.
:::
