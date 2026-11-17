## Lead context
Global balance says the probability arriving at a state equals the probability sitting there; detailed balance says the flow on every edge equals the flow on its reverse.

## Motivating example
The deterministic cycle $1\to 2\to 3\to 1$ has a uniform stationary distribution $(1/3,1/3,1/3)$. At each state, mass $1/3$ arrives and mass $1/3$ leaves, so global balance holds. The reverse edges do not exist. The flow from 1 to 2 is $1/3$ and the flow from 2 to 1 is 0. Detailed balance fails. A chain can be stationary and still have a net circulation.{{cite:durrett2019}} (pp. 300–301, detailed balance is stronger than stationarity)

## Intuition
Global balance is a conservation statement at each state: what flows in equals what is already there, once the distribution is $\pi$. It is one equation per state. Detailed balance is one equation per ordered pair. There are more equations, so fewer chains satisfy them. The reward is time symmetry. Started from $\pi$, a chain in detailed balance has the same law run backwards. A chain in global balance only has the same marginal at every time. Its paths can prefer a direction.{{cite:durrett2019}} (p. 300, equal flows on an edge and its reverse)

## Definition
Global balance for a transition matrix $P$ and a probability row $\pi$ is $\pi=\pi P$, or coordinatewise $\pi_j=\sum_i\pi_i p_{ij}$. Detailed balance is $\pi_i p_{ij}=\pi_j p_{ji}$ for all $i,j$. Summing the pairwise equations on $i$ produces global balance, because $\sum_i p_{ji}=1$. The continuous version is $\pi(dx)P(x,dy)=\pi(dy)P(y,dx)$, and the same integration in $x$ returns $\pi P=\pi$.{{cite:durrett2019}} (pp. 300–301, summing the pairwise identity)

## Interpretation — Circulation
On the three-cycle the net flow around the cycle is $1/3$ per step and the net flow on each reverse edge is 0. Global balance cannot see that, because at each vertex the incoming $1/3$ equals the outgoing $1/3$. Detailed balance sees it immediately. On a birth–death chain the state graph is a path. The only way to balance an edge is to match it with its reverse, so the local equations are detailed balance, and solving them solves global balance at the same time.{{cite:durrett2019}} (p. 301, birth–death chains)

## Properties — What each equation guarantees
Detailed balance implies global balance, and global balance is stationarity. Global balance does not imply detailed balance, by the cycle. If $\pi_i>0$ for every $i$ that the chain can sit on, detailed balance forces every positive edge to have a positive reverse edge. A doubly stochastic matrix has the uniform vector as a stationary distribution, because each column sums to 1. Doubly stochastic is not detailed balance. The cycle matrix is a permutation matrix, hence doubly stochastic, and it is not reversible.{{cite:durrett2019}} (p. 300, a stationary measure need not be reversible)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Start from $\pi_i p_{ij}=\pi_j p_{ji}$ and sum on $i$. The right-hand side factors as $\pi_j\sum_i p_{ji}=\pi_j$. The left-hand side is $(\pi P)_j$. So $\pi P=\pi$.

For the cycle let $P$ send 1 to 2, 2 to 3 and 3 to 1 with probability 1. For $\pi=(1/3,1/3,1/3)$, each coordinate of $\pi P$ is $1/3$, so global balance holds. For the pair $(1,2)$, $\pi_1 p_{12}=1/3$ and $\pi_2 p_{21}=0$.

Conversely, a two-state chain with $p_{01}=a\in(0,1]$ and $p_{10}=b\in(0,1]$ has the unique stationary distribution $\pi_0=b/(a+b)$, $\pi_1=a/(a+b)$, and $\pi_0 a=\pi_1 b$. On two states the stationary distribution automatically satisfies detailed balance. The gap between the two notions needs at least three states, or a one-way edge.{{cite:durrett2019}} (pp. 300–301)
:::
:::

## Statistical use — Which equation to verify
If the goal is to confirm a guessed $\pi$, global balance is the equation $\pi P=\pi$. If the goal is to build $P$ from a known $\pi$, detailed balance is the easier symmetry to impose, which is why Metropolis–Hastings targets it. After the kernel is built, global balance is then a consequence rather than a separate search. A numerical check that a long run's histogram is close to $\pi$ is not a proof of either equation. It is a check on one path.{{cite:durrett2019}} (pp. 300–301, detailed balance is stronger than stationarity)

Summing the pairwise equations proves $\pi P=\pi$ only when the sums exist. A birth–death product that grows so fast that $\sum_n\pi_n=\infty$ satisfies the edge equations and is not a probability distribution, so it is not a stationary distribution of a probability chain. If the chain has two closed classes, global balance can hold for every mixture of the two class-wise stationary distributions. Detailed balance has to be checked inside each class. A mixture does not create balance on an edge that is not there.{{cite:durrett2019}} (p. 301, the weights need a finite sum before they are a probability)

## Worked example
Take $a=1/5$ and $b=1/2$ on two states. Then $\pi=(5/7,\ 2/7)=(0.7143,\ 0.2857)$. The global-balance residual at state 0 is
$$
\pi_0(1-a)+\pi_1 b-\pi_0=\frac57\cdot\frac45+\frac27\cdot\frac12-\frac57=0.
$$
The detailed-balance residual on the off-diagonal is $(5/7)(1/5)-(2/7)(1/2)=0$. Both residuals vanish. On the cycle the global-balance residual at each state is 0 and the detailed-balance residual on each forward edge is $1/3-0=1/3$.

**Your turn.** A doubly stochastic matrix on two states has $p_{01}=p_{10}=c$. Find the uniform stationary distribution's detailed-balance residual.

::: {.callout-tip collapse="true" title="Answer"}
The uniform vector is $(1/2,1/2)$. The two products are $(1/2)c$ and $(1/2)c$. The residual is 0 for every $c$. On two states, doubly stochastic and detailed balance agree for the uniform distribution. The three-cycle is the smallest permutation that separates them.
:::

## Common misconceptions
"Stationary" does not mean "reversible". The cycle is stationary and not reversible. "Doubly stochastic" does not mean "detailed balance" either, for the same chain. And satisfying detailed balance on the edges that were checked is not enough if some other edge has a one-way transition with positive stationary mass. The identity is required for every pair, including the pairs one hopes are zero.

## Connections
[Detailed balance](detailed-balance.qmd) is the pairwise equation. [Stationarity and detailed balance](stationarity-and-detailed-balance.qmd) is the sampler's reading of the same pair of conditions. A [Metropolis–Hastings](metropolis-hastings-algorithm.qmd) kernel is built to satisfy the pairwise equation for a target known up to scale. Adding the pairwise equations is what produces the single-state conservation law.{{cite:durrett2019}} (pp. 300–301)

## Check yourself

### A deterministic cycle {#self-check-ex-sp-deterministic-cycle}

For the cycle $1\to 2\to 3\to 1$ and $\pi=(1/3,1/3,1/3)$, compute one global-balance residual and one detailed-balance residual.

[Exercise](../questions/ex-sp-deterministic-cycle.qmd)

::: {.callout-tip collapse="true" title="Answer"}
At state 1 the incoming mass is $\pi_3 p_{31}=1/3$ and $\pi_1=1/3$, so the global residual is 0. On the edge from 1 to 2 the products are $1/3$ and 0, so the detailed residual is $1/3$.
:::

### Doubly stochastic matrices {#self-check-ex-sp-doubly-stochastic}

Why does every doubly stochastic matrix have the uniform distribution as a stationary distribution, and why is that not detailed balance?

[Exercise](../questions/ex-sp-doubly-stochastic.qmd)

::: {.callout-tip collapse="true" title="Answer"}
If every column sums to 1 and $\pi_i=1/m$ for $m$ states, then $(\pi P)_j=(1/m)\sum_i p_{ij}=1/m$. That is global balance. Detailed balance also needs $p_{ij}=p_{ji}$ when $\pi$ is uniform. A permutation cycle has $p_{ij}\neq p_{ji}$ and is still doubly stochastic.
:::

## History
Durrett separates a stationary measure from a reversible measure and shows the summation that makes the second notion imply the first. The same implication holds for a general kernel, and the symmetry is the condition one checks when constructing a Markov-chain sampler. The three-cycle is the small example in which the summation has something to cancel and the pairwise products do not match.{{cite:durrett2019}} (pp. 300–301)
