## Lead context
Detailed balance means that, in the stationary chain, the probability flow from one state to another equals the flow in the opposite direction.

## Motivating example
A two-state chain steps from 0 to 1 with probability $a=1/5$ and from 1 to 0 with probability $b=1/2$. The weights $\pi_0=b/(a+b)=5/7$ and $\pi_1=a/(a+b)=2/7$ make the two directed flows equal: $(5/7)\times(1/5)=1/7$ and $(2/7)\times(1/2)=1/7$. Every departure toward 1 is matched by a return toward 0. That pairwise match is detailed balance. Global balance only asks that the total probability arriving at a state equal the probability sitting there. The pairwise match is stronger, and it is the one a sampler is usually built to satisfy.{{cite:durrett2019}} (pp. 300–301, detailed balance and reversible measures){{cite:geyer2005_markov_chain}} (pp. 9–10, reversibility implies invariance)

## Intuition
Picture probability as mass sitting on the states. In one step, mass moves along the arrows. Detailed balance says each arrow carries the same mass as its reverse arrow. There is no net circulation. Geyer's reading is time symmetry: if the chain is started in $\pi$, the pair $(X_n,X_{n+1})$ has the same distribution as $(X_{n+1},X_n)$. A chain that only satisfies global balance can still have a whirlpool. Mass leaves each state at the right total rate, but it travels around a cycle instead of back along the same edge.{{cite:geyer2005_markov_chain}} (pp. 10–11, time reversal){{cite:durrett2019}} (p. 300, the flow from $x$ to $y$ equals the flow from $y$ to $x$)

## Definition
A probability $\pi$ and a transition matrix $P$ satisfy detailed balance when $\pi_i p_{ij}=\pi_j p_{ji}$ for every pair of states. Durrett writes the same identity as $\mu(x)p(x,y)=\mu(y)p(y,x)$ and calls $\mu$ a reversible measure. Summing on $i$ collapses the identity to $\sum_i\pi_i p_{ij}=\pi_j$, which is global balance, so $\pi$ is stationary. The converse is false. Stationarity does not force the pairwise products to match.{{cite:durrett2019}} (pp. 300–301, summing the pairwise equations){{cite:geyer2005_markov_chain}} (p. 10, reversibility implies $\pi P=\pi$)

## Interpretation — Flows, not just a fixed point
On the two-state chain the common flow is $1/7$. An observer who only checks $\pi P=\pi$ learns that the distribution does not change. An observer who checks the two products learns that the chain looks the same run backwards. For a birth–death chain the graph is a path, so the only cycles are immediate reversals. Local balance $\pi_i p_i=\pi_{i+1} q_{i+1}$ determines the whole distribution up to a constant, and that constant is fixed by making the weights sum to 1 when the sum is finite. A formal product that sums to infinity is an invariant measure, not a probability.{{cite:durrett2019}} (p. 301, birth–death chains and the product formula)

## Properties — Two states, and a cycle that fails
Every irreducible two-state chain satisfies detailed balance. The equations $\pi_0 a=\pi_1 b$ and $\pi_0+\pi_1=1$ have the unique solution above, and both directed products equal $ab/(a+b)$. A deterministic cycle $1\to 2\to 3\to 1$ does not. The uniform vector $(1/3,1/3,1/3)$ is stationary, because each row is a permutation of a point mass and the chain merely rotates. The reverse edges have probability 0, so $\pi_i p_{ij}=\pi_j p_{ji}$ fails whenever $p_{ij}=1$. Probability circulates. Global balance holds at every state: mass $1/3$ arrives and mass $1/3$ leaves. The circulation is invisible to that check.{{cite:durrett2019}} (p. 300, detailed balance is stronger than stationarity){{cite:geyer2005_markov_chain}} (p. 10, a reversible stationary chain looks the same forwards and backwards)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Sum $\pi_i p_{ij}=\pi_j p_{ji}$ over $i$. The right-hand side is $\pi_j\sum_i p_{ji}=\pi_j$, because row $j$ of $P$ sums to 1. The left-hand side is $\sum_i\pi_i p_{ij}$. Therefore $\pi P=\pi$.

For the two-state chain set $\pi_0=b/(a+b)$ and $\pi_1=a/(a+b)$. Then $\pi_0 a=ab/(a+b)=\pi_1 b$. The diagonal equations are identities. Hence detailed balance holds, and the previous paragraph gives stationarity.

For the cycle, $P$ is the permutation matrix of $1\to 2\to 3\to 1$. Then $\pi P=\pi$ for $\pi=(1/3,1/3,1/3)$, since $P$ is doubly stochastic. For the edge $1\to 2$, $\pi_1 p_{12}=(1/3)\cdot 1$ and $\pi_2 p_{21}=(1/3)\cdot 0$. The products differ.{{cite:durrett2019}} (pp. 300–301, summing gives stationarity){{cite:geyer2005_markov_chain}} (p. 10, the integral form of the same cancellation)
:::
:::

## Statistical use — Building a sampler
Geyer's practical point is that $\pi P=\pi$ is a hard equation to solve for $P$ given $\pi$, while the symmetry $\pi(dx)P(x,dy)=\pi(dy)P(y,dx)$ is easy to check. A Metropolis update is built so that the symmetry holds for a target known only up to a constant. The sampler is then stationary because detailed balance has been checked. Irreducibility is a separate requirement. A transition can satisfy detailed balance on a subset it cannot leave, and then the chain preserves the wrong conditional distribution.{{cite:geyer2005_markov_chain}} (pp. 10–11, reversibility is easier to arrange than invariance alone)

## Worked example
With $a=1/5$ and $b=1/2$, $\pi_0=5/7=0.7143$ and $\pi_1=2/7=0.2857$. Both flows equal $1/7=0.1429$. The one-step balance at state 0 is $\pi_0 p_{00}+\pi_1 p_{10}$. Here $p_{00}=1-a=4/5$ and $p_{10}=b=1/2$, so
$$
\frac57\cdot\frac45+\frac27\cdot\frac12=\frac{4}{7}+\frac{1}{7}=\frac57=\pi_0.
$$
The same arithmetic at state 1 returns $2/7$. Stationarity holds because the pairwise flows match, not because the chain is unable to move.

**Your turn.** Keep $b=1/2$ and change $a$ to $1/2$. Find $\pi$ and the common flow.

::: {.callout-tip collapse="true" title="Answer"}
Now $a=b=1/2$, so $\pi_0=\pi_1=1/2$. The common flow is $(1/2)\times(1/2)=1/4$. The chain is symmetric and the stationary distribution is uniform. Detailed balance still holds. It does not require the two transition probabilities to differ.{{cite:durrett2019}} (p. 300, the pairwise identity)
:::

## Common misconceptions
Detailed balance is not the same statement as $\pi P=\pi$. The cycle is a counterexample with a stationary distribution and no detailed balance. It is also not a property of one simulated path. A trace can look calm while the transition kernel circulates, and a short path can look restless while the kernel satisfies the identity. The identity is a fact about $\pi$ and $P$. And a reversible kernel started away from $\pi$ does not look the same forwards and backwards. Geyer notes that the time-reversal reading uses $\pi$ as the initial distribution.{{cite:geyer2005_markov_chain}} (p. 10, the chain must be started in $\pi$)

## Assumptions and limits — Subsets the chain cannot leave
If $p_{ij}>0$ and $\pi_i>0$ and $\pi_j>0$, detailed balance forces $p_{ji}>0$. A one-way edge with positive stationary mass on both ends cannot be balanced. The deterministic cycle is that obstruction. On a graph that is a tree, there is no longer cycle to carry a current, and the edge equations determine $\pi$. If the state space is infinite and the birth–death product has infinite total mass, there is no stationary probability even though the local balance equations have a solution. The solution is an invariant measure. Sampling from it is not a probability calculation.{{cite:durrett2019}} (p. 301, the product may fail to be summable)

## Connections
[Global balance](global-balance-and-detailed-balance.qmd) is the summed form. [Stationarity](stationarity-and-detailed-balance.qmd) is $\pi P=\pi$. A [Metropolis–Hastings update](metropolis-hastings-algorithm.qmd) is one construction that enforces the pairwise identity. The cycle $1\to 2\to 3\to 1$ is a stationary chain that fails the pairwise identity.{{cite:durrett2019}} (pp. 300–301){{cite:geyer2005_markov_chain}} (pp. 9–11)

## Check yourself

### Birth–death stationary weights {#self-check-ex-sp-birth-death-pi}

A birth–death chain on $\{0,1,2\}$ has $p_0=1$, $q_1=1/3$, $p_1=2/3$ and $q_2=1$. Using $\pi_i p_i=\pi_{i+1} q_{i+1}$, find $\pi$.

[Question-bank page](../questions/ex-sp-birth-death-pi.qmd)

::: {.callout-tip collapse="true" title="Answer"}
$\pi_0\cdot 1=\pi_1\cdot(1/3)$, so $\pi_1=3\pi_0$. Then $\pi_1\cdot(2/3)=\pi_2\cdot 1$, so $\pi_2=(2/3)\cdot 3\pi_0=2\pi_0$. The sum is $\pi_0(1+3+2)=6\pi_0=1$, hence $\pi=(1/6,\ 1/2,\ 1/3)$. Each edge flow matches by construction.{{cite:durrett2019}} (p. 301, birth–death product)
:::

### A path graph {#self-check-ex-sp-path-graph}

Why does the deterministic three-cycle fail detailed balance even though $(1/3,1/3,1/3)$ is stationary?

[Question-bank page](../questions/ex-sp-path-graph.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The forward edge has probability 1 and the reverse edge has probability 0, so the products $(1/3)\cdot 1$ and $(1/3)\cdot 0$ differ. Stationarity only asks that the total mass into each state equal $1/3$. It does not ask the mass to return along the same edge.{{cite:durrett2019}} (p. 300, detailed balance is stronger than a stationary distribution)
:::

## History
Durrett introduces detailed balance as the condition stronger than stationarity, with the Ehrenfest chain and birth–death chains as the cases where the pairwise equations are easy to solve, and he then explains reversibility by running the stationary chain backwards. Geyer's notes make the same implication in integral notation and emphasise why the symmetry is the practical way to build a Markov chain with a prescribed stationary distribution.{{cite:durrett2019}} (pp. 300–301, reversible measures){{cite:geyer2005_markov_chain}} (pp. 9–11, reversible Markov chains)
