## Motivating example
Two fair steps, each $+1$ or $-1$ with probability $1/2$, start at $X_0=0$. The position at time $2$ is their sum. The value at time $1$ and the value at time $2$ are two coordinates of one path.

## Intuition — One path, many times
A single random variable is one measurement. A stochastic process is the whole list of measurements, one for each time. One outcome picks an entire path: the value at time 1, the value at time 2, and so on. Matching the distribution at each separate time does not fix how those times move together. It is a family of random variables used for temporal phenomena in which chance plays a part. Markov, martingale, stationary and independent-increment processes are distinguished by the conditions placed on that family.{{cite:dodge2008}} (pp. 521–522)

## Definition — Index, state, and path
On a probability space, a stochastic process with index set $T$ and state space $S$ is a family $\{X_t:t\in T\}$ of $S$-valued random variables. Discrete time takes $T=\{0,1,2,\ldots\}$; continuous time takes $T=[0,\infty)$. For a fixed outcome $\omega$, the map $t\mapsto X_t(\omega)$ is a trajectory. One statement of the term uses an infinite index. A finite index is also allowed: a finite family is still a collection of random variables on one probability space, and the joint distributions of those variables are what a calculation uses.{{cite:dodge2008}} (p. 522, family $(X_t)_{t\in I}$ and trajectory)

The process has independent increments when increments over disjoint intervals are independent, and stationary increments when the law of $X_{t+h}-X_t$ depends on the length $h$ and not on $t$. Neither property makes the levels $X_t$ identically distributed. The level can spread as $t$ grows while each increment of a given length keeps the same law.{{cite:dodge2008}} (p. 522, independent increments and stationary processes)

## Worked example — Two fair steps
Let $S_1$ and $S_2$ be independent steps, each equal to $+1$ or $-1$ with probability $1/2$. Set $X_0=0$, $X_1=S_1$ and $X_2=S_1+S_2$. Then
$$
\mathbb P(X_2=2)=\mathbb P(X_2=-2)=\tfrac14,\qquad \mathbb P(X_2=0)=\tfrac12.
$$
The mean is $0$. The second moment is $4\cdot\tfrac12=2$, so $\operatorname{Var}(X_2)=2$. The marginal of $X_1$ is supported on $\{-1,+1\}$, not on $\{-2,0,2\}$. The increment $X_2-X_1=S_2$ has the same law as $X_1$ and is independent of it: the increments are stationary and independent, while the position at time 2 is more spread out than the position at time 1.{{cite:dodge2008}} (p. 522, independent increments)

**Your turn.** For the same two steps, find $\mathbb P(X_1=1,X_2=0)$ and $\mathbb P(X_2=2)$.

::: {.callout-tip collapse="true" title="Answer"}
The event $\{X_1=1,X_2=0\}$ is the first step $+1$ and the second step $-1$, with probability $\tfrac14$. The event $\{X_2=2\}$ is both steps $+1$, also with probability $\tfrac14$.
:::

## Connections — The conditions that come next
A [Markov chain](markov-chain.qmd) is the discrete-time case in which the next state depends on the present state and not on the earlier path. [Stationary and independent increments](stationary-and-independent-increments.qmd) are the two clock conditions used for random walks and for the [homogeneous Poisson process](homogeneous-poisson-process.qmd). The finite-dimensional joints live on the product of the state space with itself; the [sigma-algebra](sigma-algebra.qmd) is what makes events about the whole path legitimate.{{cite:dodge2008}} (pp. 521–522, Markov process and independent increments)

## Check yourself
### A copied step
Suppose the second step is forced to equal the first, so $X_2=2X_1$. Are the increments $X_1-X_0$ and $X_2-X_1$ independent?

::: {.callout-tip collapse="true" title="Answer"}
No. Here $X_2-X_1=X_1$, so the second increment is the first increment. They are equal, not independent. The position at time 2 is then supported on $\{-2,+2\}$, each with probability $1/2$.
:::

### Adding means
Keep independent steps with mean $0$ and variance $1$, but drop the assumption that each step is $\pm 1$. What are $\mathbb E(X_2)$ and $\operatorname{Var}(X_2)$?

::: {.callout-tip collapse="true" title="Answer"}
The mean of a sum is the sum of the means, so $\mathbb E(X_2)=0$. Independence makes the variances add, so $\operatorname{Var}(X_2)=2$. The four-point distribution in the worked example is a special case of this calculation.
:::
