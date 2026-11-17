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

For the conjugate kernel $\exp\{\eta\chi-\nu A(\eta)\}$ relative to $d\eta$, multiplication by $n$ independent likelihoods changes $(\chi,\nu)$ to $(\chi+\sum x_i,\nu+n)$. This is simply collection of the coefficients of $\eta$ and $A$. A prior specified relative to $d\lambda$ requires the Jacobian $d\eta/d\lambda=1/\lambda$ when translated to the other coordinate; a change of the parameter's name leaves the underlying measure as it was.

### A symbolic translation between coordinates
Write the Poisson natural normaliser as $A(\eta)=e^{\eta}$ and the Bernoulli natural normaliser as $B(\eta)=\log(1+e^{\eta})$. Symbolic differentiation produces
$$
A'(\eta)=e^{\eta},\qquad A''(\eta)=e^{\eta},
$$
$$
B'(\eta)=\frac{e^{\eta}}{1+e^{\eta}},\qquad B''(\eta)=\frac{e^{\eta}}{(1+e^{\eta})^2}.
$$
The first pair says that a Poisson natural statistic has mean and variance $e^{\eta}$. The second pair says that a Bernoulli natural statistic has mean $p=B'(\eta)$ and variance $p(1-p)$. These are derivatives with respect to $\eta$.

Now set $\lambda>0$ and $\eta=\log\lambda$, so the composed Poisson map is $A(\log\lambda)=\lambda$. Differentiating in $\lambda$ gives a second derivative of $0$. The chain rule makes the cancellation explicit:
$$
\frac{d^2}{d\lambda^2}A(\log\lambda)
=A''(\eta)\left(\frac1\lambda\right)^2+A'(\eta)\left(-\frac1{\lambda^2}\right)
=\frac{e^{\eta}}{\lambda^2}-\frac{e^{\eta}}{\lambda^2}=0,
$$
because $e^{\eta}=\lambda$. The variance remains $A''(\eta)=\lambda$ when it is read in the natural coordinate. The zero is the second derivative of the reparameterised function $A(c(\lambda))$.

The same distinction appears for a centred normal factor. Let $L(v)=\tfrac12\log(2\pi v)$ for $v>0$. Then $L''(v)=-1/(2v^2)$. At $v=4$, $L''(4)=-1/32=-0.03125$. The value $4$ is a variance. The value $-0.03125$ is a second derivative in that variance coordinate. The two numbers come from different operations.{{cite:wainwright_jordan2008}} (§3.5.1, prop. 3.1, pp. 62–63)

**Your turn.** For Poisson mean $2$, identify $\eta$, $A$ and $P(X=0)$.

::: {.callout-tip collapse="true" title="Answer"}
$\eta=\log2$, $A=2$, and $P(X=0)=e^{-2}=0.13534$.
:::

## Definition — Match the normaliser before differentiating
One regular writing of a density on a fixed support is
$$
f(x\mid\theta)=\frac{b(x)\exp\{c(\theta)\,T(x)\}}{a(\theta)},
$$
with $a(\theta)>0$ free of $x$. The natural-parameter writing of the same density is
$$
f(x\mid\eta)=h(x)\exp\{\eta\,T(x)-A(\eta)\},
$$
with $\eta=c(\theta)$ and $h=b$. Equating exponents gives the translation
$$
A\bigl(c(\theta)\bigr)=\log a(\theta).
$$
Division by $a(\theta)$ becomes subtraction of $\log a(\theta)$ once the factor sits in the exponent. For the Poisson probabilities, $a(\lambda)=e^{\lambda}$ and $c(\lambda)=\log\lambda$, so $\log a(\lambda)=\lambda$ and $A(\log\lambda)=\lambda$. For a Bernoulli success probability $p$, take $a(p)=1/(1-p)$ and $c(p)=\log\{p/(1-p)\}$. Then $\log a(p)=-\log(1-p)$. At $p=3/4$ this equals $\log4$, the same number as $B(\log3)$. The base measures still differ: the Poisson factor carries $1/x!$, while the Bernoulli factor is $1$ on $\{0,1\}$.{{cite:wainwright_jordan2008}} (§3.2, eqs. 3.5–3.7, pp. 39–40){{cite:wainwright_jordan2008}} (p. 42, tab. 3.1)

A conjugate kernel $\exp\{\eta\chi-\nu A(\eta)\}$, taken relative to $d\eta$, collects coefficients when independent copies are multiplied. After $n$ observations the updated pair is $(\chi+\sum_i T(x_i),\,\nu+n)$. That arithmetic is the translation of Bayes' rule inside the natural coordinate. A density written relative to $d\lambda$ still needs the Jacobian of $\eta=c(\lambda)$ before it can be compared with a density relative to $d\eta$. For the Poisson mean that Jacobian is $1/\lambda$.{{cite:wainwright_jordan2008}} (§3.2 and §3.5.1)

## Interpretation — The mean and variance have a coordinate
Where differentiation under the integral is justified, $\nabla A(\eta)$ is the mean of $T(X)$ and $\nabla^2 A(\eta)$ is its covariance. The gradient and Hessian are partial derivatives in $\eta$. A smooth reparameterisation $\eta=c(\theta)$ changes both of them by the chain rule. In one dimension the first derivative of the composed map is $A'(c(\theta))c'(\theta)$. The second derivative adds the further term $A'(c(\theta))c''(\theta)$. That extra term is why a variance formula copied from the natural coordinate can fail after a routine substitution of $\theta$ for $\eta$.

The Poisson calculation is small enough to check by hand and by symbolic differentiation. Both give $A''(\eta)=e^{\eta}$ and a vanishing second derivative for $\lambda\mapsto A(\log\lambda)$. The Bernoulli calculation gives $B''(\eta)=p(1-p)$ with $p=e^{\eta}/(1+e^{\eta})$. At $\eta=\log3$, $p=3/4$ and $B''(\log3)=(3/4)(1/4)=0.1875$. The same natural-parameter value $\log3$ occurs for a Poisson mean of $3$, where the variance is $3$, and for this Bernoulli law, where the variance is $0.1875$. Equal natural parameters leave the families distinct because $h$ and $A$ differ.{{cite:wainwright_jordan2008}} (§3.5.1, prop. 3.1, pp. 62–63)

The centred normal expression $L(v)=\tfrac12\log(2\pi v)$ is a log normaliser contribution in the variance coordinate. Its second derivative $-1/(2v^2)$ is negative. Convexity of a log partition function is a property of $A$ on its natural domain, after the representation has been reduced to a minimal natural statistic. A negative second derivative in $v$ is compatible with that convexity because $v$ is a different coordinate.{{cite:wainwright_jordan2008}} (§3.5.1, prop. 3.1, pp. 62–63)

## Intuition — Translate the exponent, then differentiate
Start from a density that is already written as an exponential of a linear function of $T(x)$. Read off $\eta$, $T$, $h$ and $A$ as the coefficient of $T$, the statistic, the factor free of $\eta$, and the term free of $x$. Differentiate $A$ only after that reading is fixed. If the scientifically convenient parameter is a mean, a probability or a variance, compose $A$ with the map from that parameter to $\eta$ and keep every factor the chain rule produces.

The Poisson mean makes the bookkeeping visible. The map $\lambda\mapsto\log\lambda$ has first derivative $1/\lambda$ and second derivative $-1/\lambda^2$. Multiplying the natural variance $e^{\eta}$ by $(1/\lambda)^2$ produces $1/\lambda$. Adding the natural mean times the second derivative of the map produces $-1/\lambda$. The sum is zero, which is the second derivative of the identity function $\lambda$. Nothing in that arithmetic sets the Poisson variance to zero.

## Common misconceptions
A large value of $A''(\eta)$ is a variance of $T$ in the natural coordinate. It becomes a curvature for a different parameter only after multiplication by the squared derivative of the reparameterisation, together with the first-derivative term when the map is curved. Reporting $A''$ beside a mean, a probability or a variance label mixes those coordinates.

Two families can share a numerical value of $\eta$ and still assign different probabilities. The Poisson probability of $2$ at mean $3$ is $0.22404$. A Bernoulli trial with the same natural parameter $\log3$ has success probability $3/4$ and variance $0.1875$. The shared symbol is a coefficient in an exponent, and the sample spaces remain different.{{cite:dodge2008}} (p. 425){{cite:wainwright_jordan2008}} (p. 42, tab. 3.1)

Changing the symbol that denotes the argument of a density is a notation edit. A Jacobian appears when the underlying measure changes, as in the passage between $d\eta$ and $d\lambda$. The conjugate update $(\chi,\nu)\mapsto(\chi+\sum T(x_i),\nu+n)$ is stated for the natural coordinate and its dominating measure $d\eta$.

## Assumptions and limits
The derivative identities use a representation in which the support does not depend on $\eta$, together with enough smoothness to differentiate under the integral. A minimal representation is what turns positive semidefinite curvature into strict convexity. A curved exponential family can still have a natural sufficient statistic of higher dimension than the parameter of interest; the map $\eta(\theta)$ then traces a curve, and derivatives along that curve are directional derivatives of $A$. The table of standard families fixes $h$, $T$ and $A$ one row at a time, which is the practical check that a translation has kept the same density.{{cite:wainwright_jordan2008}} (§3.2, eqs. 3.5–3.7, pp. 39–40){{cite:wainwright_jordan2008}} (p. 42, tab. 3.1)

## Connections
The same derivatives specialise to the variance functions used in a generalised linear model. In the Poisson row, mean and variance are both $e^{\eta}$, hence both $\lambda$ after returning to the mean. In the Bernoulli row, the variance is $p(1-p)$. A log-linear coefficient later translates a change in a linear predictor into a multiplicative change in a mean. That last step is a contrast on the scale of $\eta$ or of $\log\mu$, and it stays consistent when $A$ has been differentiated in the coordinate the contrast actually uses.{{cite:wainwright_jordan2008}} (§3.5.1, prop. 3.1, pp. 62–63)
