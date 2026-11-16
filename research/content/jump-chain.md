## Lead context
The jump chain is the sequence of states a continuous-time Markov chain visits, with the waiting times left out.

## Motivating example
A machine is either running, waiting for a part, or under repair. It stays in the current state for an exponential time and then moves. A description that only lists the successive states, and not how long each visit lasted, is a discrete-time chain. That chain is the jump chain. The holding times are a separate collection of exponential clocks.{{cite:pishro_nik2014}} (§11.3, jump chain and holding times)

## Intuition — A race of exponential clocks
From state $i$, start an independent exponential clock of rate $q_{ij}$ for each possible destination $j\neq i$. The machine leaves $i$ when the first clock rings, and it goes to the state whose clock rang. The minimum of independent exponential clocks is exponential with rate equal to the sum of the rates, so the holding time in $i$ is exponential with rate $\nu_i=\sum_{j\neq i} q_{ij}$. The probability that clock $j$ rings first is $q_{ij}/\nu_i$. Those probabilities are the transitions of the jump chain. They do not depend on how long the hold happened to be, which is the memoryless property of the exponential clocks.{{cite:pishro_nik2014}} (§11.3, generator and jump chain)

## Definition — Embedded transitions
Let $q_{ij}\ge 0$ for $j\neq i$ be the transition rate from $i$ to $j$, and set $q_{ii}=-\nu_i$ with $\nu_i=\sum_{j\neq i} q_{ij}$. If $\nu_i>0$, the jump-chain probability is
$$
k_{ij}=\Pr(\text{next state is }j\mid\text{current state is }i)=\frac{q_{ij}}{\nu_i},\qquad j\neq i,
$$
and $k_{ii}=0$. If $\nu_i=0$, state $i$ is absorbing and the chain never jumps. The matrix $K=(k_{ij})$ is a discrete-time transition matrix. The continuous-time process is recovered by attaching an independent $\mathrm{Exp}(\nu_i)$ holding time to each visit to $i$.{{cite:pishro_nik2014}} (§11.3, eq. for $g_{ij}=\lambda_i p_{ij}$)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $T_j\sim\mathrm{Exp}(q_{ij})$ be independent for $j\neq i$, and let $T=\min_j T_j$. For two destinations with rates $a$ and $b$,
$$
\Pr(T_1<T_2)=\int_0^{\infty} a e^{-a t} e^{-b t}\,dt=\frac{a}{a+b}.
$$
The same comparison of one clock against the sum of the others gives $q_{ij}/\nu_i$ when there are more than two destinations. The holding time is the minimum, which is exponential at rate $\nu_i$, and it is independent of which clock wins.{{cite:pishro_nik2014}} (§11.3, holding time and jump probabilities)
:::
:::

## Worked example
From state $1$ the rates are $q_{12}=2$ and $q_{13}=4$. Then $\nu_1=6$, $k_{12}=2/6=1/3$ and $k_{13}=4/6=2/3$. The mean holding time is $1/6$. The probability that the hold lasts longer than $0.5$ is $e^{-6\times 0.5}=e^{-3}=0.04979$. A rate may exceed $1$. The jump probability may not: $4/6$ is less than $1$, even though the rate $4$ is greater than $1$.

**Your turn.** Add a third destination with $q_{14}=6$, and recompute $\nu_1$ and $k_{13}$.

::: {.callout-tip collapse="true" title="Answer"}
The exit rate is $2+4+6=12$. The probability of jumping to state $3$ falls from $4/6$ to $4/12=1/3$, because the new clock takes a share of the race. The rate $q_{13}$ itself is unchanged.
:::

## Connections — Generators, holding times, and periodicity
The [holding time](holding-time.qmd) is the exponential wait that the jump chain ignores. The generator stores the rates $q_{ij}$, including the negative diagonal $-\nu_i$, and its rows sum to $0$. A transition matrix of the jump chain has rows that sum to $1$. A two-state jump chain that always switches is periodic as a discrete-time chain. The continuous-time process is not forced to switch at integer times, so the random holds destroy that clockwork.{{cite:pishro_nik2014}} (§11.3, embedded chain)

## Check yourself

### An absorbing state
All rates out of state $0$ are $0$. What is the jump chain's behaviour at $0$?

::: {.callout-tip collapse="true" title="Answer"}
$\nu_0=0$, so there is no next state. The holding time is infinite and the jump chain stays at $0$.
:::

### Two equal rates
$q_{12}=q_{13}=5$. Find the jump probabilities and the mean hold.

::: {.callout-tip collapse="true" title="Answer"}
$\nu_1=10$, so each destination has probability $5/10=1/2$. The mean holding time is $1/10$.
:::
