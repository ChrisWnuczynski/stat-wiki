## Motivating example
Knowing the expected offspring count describes average population growth, but does not determine extinction probability. The complete offspring distribution is needed. Its probability generating function packages that distribution so that moving from one generation to the next becomes function composition.{{cite:grinstead_snell1997}} (§10.2, branching processes)

## Definition — A transform on the unit interval
For a nonnegative integer offspring count $\xi$ with probabilities $p_k$, define
$$
f(s)=\mathbb E[s^\xi]=\sum_{k=0}^{\infty}p_ks^k,\qquad0\le s\le1.
$$
Then $f(0)=p_0$, $f(1)=1$, and $f$ is increasing and convex. Its left derivative at one is the mean, including the possibility of an infinite mean. If the second factorial moment is finite, $f''(1-)=\mathbb E[\xi(\xi-1)]$ and $\operatorname{Var}(\xi)=f''(1-)+f'(1-)-f'(1-)^2$.{{cite:grinstead_snell1997}} (§§10.1–10.2)

## Properties — Why the transforms compose
For a Galton–Watson process started at $Z_0=1$, independent reproduction gives $\mathbb E[s^{Z_{n+1}}\mid Z_n]=f(s)^{Z_n}$. Therefore $f_{n+1}(s)=f_n(f(s))$, where $f_n(s)=\mathbb E[s^{Z_n}]$. Starting with $f_0(s)=s$ makes $f_n$ the $n$-fold composition of $f$. A fixed number of independent offspring counts would multiply their transforms; a random generation size introduces composition.{{cite:durrett2019}} (§4.3.4)

Putting $s=0$ yields $q_{n+1}=f(q_n)$ with $q_0=0$, the probability of extinction by generation $n+1$. The sequence increases to the smallest fixed point of $f$ in $[0,1]$: if $a=f(a)$, induction gives $q_n\le a$, while continuity gives $q=f(q)$ at the limit. This argument also distinguishes extinction by a given generation from eventual extinction.{{cite:grinstead_snell1997}} (§10.2)

## Worked example — A quadratic offspring transform
Let $p_0=1/4$, $p_1=1/4$ and $p_2=1/2$. Then
$$
f(s)=\tfrac14+\tfrac14s+\tfrac12s^2,
\qquad m=\tfrac54,\qquad\operatorname{Var}(\xi)=\tfrac{11}{16}.
$$
The fixed-point equation factors as $(2s-1)(s-1)=0$ after multiplication by four, so eventual extinction has probability $1/2$. The first four extinction-by-generation probabilities are $0.25$, $0.34375$, $0.39502$ and $0.42678$. Their increase illustrates convergence to the smaller fixed point.{{cite:durrett2019}} (§4.3.4, offspring generating functions and extinction)

For Poisson offspring with mean $1.5$, $f(s)=e^{1.5(s-1)}$. Extinction in the first generation has probability $e^{-1.5}=0.22313$, while the smaller fixed point is approximately $0.417188$. For the geometric law $p_k=(1-r)r^k$, the transform is $(1-r)/(1-rs)$ and its mean is $r/(1-r)$. The fixed-point roots are $1$ and $(1-r)/r$ when $0<r<1$; the extinction probability is the smaller root in the unit interval.{{cite:grinstead_snell1997}} (§10.2)

**Your turn.** If $p_0=1/4$ and $p_2=3/4$, find $f$, its mean and the eventual extinction probability.

::: {.callout-tip collapse="true" title="Answer"}
The transform is $f(s)=1/4+3s^2/4$, its mean is $3/2$, and $f(s)=s$ factors as $(3s-1)(s-1)=0$. The smallest root is $1/3$, giving survival probability $2/3$.
:::

## Connections — Criticality and several ancestors
With positive probability of zero offspring, a non-degenerate law of mean at most one becomes extinct almost surely. Mean greater than one permits a smaller fixed point and positive survival probability. The deterministic one-child law has $f(s)=s$ and never dies out, showing why the critical case requires attention to degeneracy. With $r$ independent ancestors, every lineage must die out for total extinction, giving probability $q^r$.{{cite:durrett2019}} (§4.3.4)
