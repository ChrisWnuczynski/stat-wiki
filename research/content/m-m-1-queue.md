## Lead context
An M/M/1 queue is a single server with Poisson arrivals and exponential service, and it settles to a geometric queue length only when the server is faster than the arrivals.

## Motivating example
Customers arrive at rate $3$ per hour and each service averages $1/5$ of an hour. The server is free more often than busy, but the queue is not a fixed length: the chance of two or more people present is still large enough to matter for the mean wait.

## Intuition — Balance across each cut
Let $N$ be the number present, including the customer in service. In the long run the flow from $n$ to $n+1$ has to match the flow back. Arrivals happen at rate $\lambda$ in every state. Service happens at rate $\mu$ whenever $n\ge 1$. Writing $\pi_n$ for the stationary probability,
$$
\pi_n\lambda=\pi_{n+1}\mu.
$$
The ratios are constant, so the probabilities form a geometric sequence. They can be scaled to sum to $1$ only when $\lambda<\mu$. If arrivals are at least as fast as service, the same formal weights sum to infinity and there is no stationary distribution.

## Definition — Geometric queue length
Set $\rho=\lambda/\mu$. If $0\le\rho<1$, then
$$
\pi_n=(1-\rho)\rho^n,\qquad n\ge 0,
$$
the mean number present is $L=\rho/(1-\rho)$, and $\Pr(N\ge k)=\rho^k$. The mean time in system is $W=L/\lambda=1/(\mu-\lambda)$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The cut balance gives $\pi_n=\pi_0\rho^n$. Then $\sum_{n=0}^\infty\pi_0\rho^n=1$ forces $\pi_0=1-\rho$ when $\rho<1$, and the series diverges when $\rho\ge 1$. Also
$$
\sum_{n=1}^\infty n\rho^{n-1}=\frac{1}{(1-\rho)^2},
$$
so $L=(1-\rho)\rho/(1-\rho)^2=\rho/(1-\rho)$. The tail $\sum_{n\ge k}\pi_n=\rho^k$. Little’s relation $L=\lambda W$ then gives $W=1/(\mu-\lambda)$.
:::
:::

## Worked example
Take $\lambda=3$ and $\mu=5$ per hour. Then $\rho=3/5$, $\pi_0=2/5$, and
$$
L=\frac{3/5}{2/5}=\frac{3}{2},\qquad W=\frac{1}{5-3}=\frac{1}{2}
$$
hour. The chance of at least two customers is $\rho^2=9/25=0.36$. If instead $\lambda=5$ and $\mu=5$, then $\rho=1$ and these formulae do not give a probability distribution.

**Your turn.** For $\lambda=1$ and $\mu=4$, find $\pi_0$, $L$, and $W$.

::: {.callout-tip collapse="true" title="Answer"}
$\rho=1/4$, so $\pi_0=3/4$, $L=(1/4)/(3/4)=1/3$, and $W=1/(4-1)=1/3$.
:::

## Connections — Birth–death queues
The same cut balance is [local balance](local-balance.qmd) on a birth–death chain. [Little’s law](little-s-law.qmd) converts $L$ into $W$ once the arrival rate is the rate that actually enters. An [M/M queue](m-m-queue.qmd) with infinitely many servers has no stability threshold, because every arrival starts service at once and the stationary count is Poisson. A finite waiting room restores a stationary distribution at every load by turning arrivals away.

## Check yourself

### An M/M/1 queue {#self-check-ex-sp-mm1-numbers}

Arrivals are $2$ per hour and service is $3$ per hour. Find $\pi_0$, $\Pr(N\ge 3)$, $L$, and $W$.

[Question-bank page](../questions/ex-sp-mm1-numbers.qmd)

::: {.callout-tip collapse="true" title="Answer"}
$\rho=2/3$, so $\pi_0=1/3$ and $\Pr(N\ge 3)=(2/3)^3=8/27$. Then $L=2$ and $W=1$ hour.
:::

### An M/M/∞ system {#self-check-ex-sp-mminf-numbers}

Arrivals are $6$ per hour and each service rate is $2$ per hour, with infinitely many servers. Find the stationary mean and the probability that the system is empty.

[Question-bank page](../questions/ex-sp-mminf-numbers.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The mean is $\lambda/\mu=3$. The empty-system probability is the Poisson probability $e^{-3}$. There is no requirement that $\lambda<\mu$.
:::
