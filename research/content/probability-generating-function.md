## Motivating example
If one machine produces a random count and another independent machine produces another count, calculating the distribution of their total can require many convolution terms. A probability generating function stores the count probabilities as coefficients, so adding independent counts becomes multiplication of functions.{{cite:grinstead_snell1997}} (§10.1, pp. 369–372)

## Definition — Probabilities as coefficients
For a nonnegative integer-valued $N$, its probability generating function is
$$
G_N(z)=E(z^N)=\sum_{k=0}^\infty P(N=k)z^k,\qquad |z|\le1.
$$
The series converges absolutely on the closed unit disc. Its coefficients recover the probabilities: $P(N=k)=G_N^{(k)}(0)/k!$. For a proper distribution, $G_N(1)=1$, and $G_N(0)=P(N=0)$ with the convention $0^0=1$.{{cite:grinstead_snell1997}} (§10.1, ordinary generating functions, pp. 369–370)

## Properties — Derivatives and independent totals
Differentiation at the boundary gives factorial moments when they are finite:
$$
E(N)=G_N'(1),\quad E\{N(N-1)\}=G_N''(1),\quad
\operatorname{Var}(N)=G_N''(1)+G_N'(1)-G_N'(1)^2.
$$
A derivative at $1$ is understood as a limit from below; it can diverge. Inside the unit disc, termwise differentiation is justified by the power-series representation.{{cite:grinstead_snell1997}} (§10.1, pp. 369–371)

If $N$ and $M$ are independent, $G_{N+M}=G_NG_M$. For $N$ independent of iid counts $Y_i$, a random sum $S=\sum_{i=1}^NY_i$ has $G_S(z)=G_N\{G_Y(z)\}$ for $0\le z\le1$. Condition on $N=n$ to obtain $G_Y(z)^n$, then average over $N$. This composition is the basis of generating-function calculations in branching models.{{cite:grinstead_snell1997}} (§§10.1–10.2){{cite:durrett2019}} (§4.3.4, branching-process generating functions)

For a branching process started by one individual, let $q_j$ be the probability of extinction by generation $j$. Independent reproduction gives $q_0=0$ and $q_{j+1}=G(q_j)$. These probabilities increase to the eventual extinction probability $q$, and continuity gives $q=G(q)$. If $s\in[0,1]$ is any other fixed point, induction gives $q_j\le s$, hence $q\le s$. Thus extinction probability is the smallest fixed point in $[0,1]$.{{cite:grinstead_snell1997}} (§10.2, branching processes){{cite:durrett2019}} (§4.3.4, extinction-probability equation)

## Worked example
Suppose $N$ has probabilities $0.2,0.5,0.3$ at $0,1,2$. Then $G_N(z)=0.2+0.5z+0.3z^2$, with $E(N)=1.1$ and $\operatorname{Var}(N)=0.49$. For two independent copies the product is
$$
G_N(z)^2=0.04+0.20z+0.37z^2+0.30z^3+0.09z^4.
$$
The five coefficients are the probabilities of the total. They sum to one; differentiation gives total mean $2.2$ and variance $0.98$. Multiplication encodes precisely the convolution of the two count distributions.{{cite:grinstead_snell1997}} (§10.1, multiplication under independent addition)

The same method explains Poisson thinning. If a Poisson$(2)$ number of items are independently selected with probability $0.3$, the selected count has generating function $\exp\{2[(0.7+0.3z)-1]\}=e^{0.6(z-1)}$, hence a Poisson$(0.6)$ law.{{cite:durrett2019}} (§3.7, Poisson-process thinning)

**Your turn.** What is the probability that three independent copies of the first count all sum to zero?

::: {.callout-tip collapse="true" title="Answer"}
It is $G_N(0)^3=0.2^3=0.008$. A nonnegative sum is zero only when every summand is zero.
:::

## Check yourself

### A Bernoulli total {#self-check-depth-mgf-bernoulli-sum}

[Practice question](../questions/depth-mgf-bernoulli-sum.qmd)

Let X and Y be independent Bernoulli variables with success probability 0.4. Find the MGF of S=X+Y, its mean and variance, and P(S=2). What part fails if X=Y instead?

::: {.callout-tip collapse="true" title="Answer"}
One MGF is 0.6+0.4e^t, so independence gives M_S(t)=(0.6+0.4e^t)². The mean is 0.8, variance 2(0.4)(0.6)=0.48, and P(S=2)=0.4²=0.16. If X=Y, the sum's MGF is 0.6+0.4e^{2t}; the product rule and binomial law do not apply.
:::

### An offspring generating function {#self-check-ex-sp-critical-extinction}

[Practice question](../questions/ex-sp-critical-extinction.qmd)

For the offspring law $\mathbb{P}(\xi=0)=2/5$, $\mathbb{P}(\xi=1)=1/5$, $\mathbb{P}(\xi=2)=2/5$, find the mean, the probability generating function, and the extinction probability. Explain the result.

::: {.callout-tip collapse="true" title="Answer"}
The mean is

$$
m=0\cdot\frac{2}{5}+1\cdot\frac{1}{5}+2\cdot\frac{2}{5}=1.
$$

The probability generating function is $f(s)=2/5+s/5+2s^2/5$. The equation $f(s)=s$ is $2s^2-4s+2=0$, or $(s-1)^2=0$. The only root in $[0,1]$ is $1$, so the extinction probability is $1$. The offspring law is non-degenerate and $p_0=2/5>0$, so the critical case of the extinction criterion applies.
:::
