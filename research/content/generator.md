## Lead context
The generator of a continuous-time Markov chain is the matrix of instantaneous jump rates, with each row summing to zero.

## Motivating example
A machine alternates between idle and busy. It leaves idle at rate $2$ per hour and leaves busy at rate $4$ per hour. The mean idle spell is $1/2$ hour and the mean busy spell is $1/4$ hour. Over a long run the proportion of idle time is $(1/2)/(1/2+1/4)=2/3$. Those two rates, and the requirement that each row sums to zero, are the whole generator
$$
Q=\begin{pmatrix}-2&2\\ 4&-4\end{pmatrix}.
$$

## Intuition
In continuous time there is no fixed tick. A rate may exceed $1$, because it is an intensity, not a probability. From state $i$ the chain waits an exponential time with rate $\nu_i=-q_{ii}$ and then jumps to $j$ with probability $q_{ij}/\nu_i$. Those jump probabilities sum to $1$.{{cite:levin_peres2017}} (§1.1) The rates themselves sum to $0$ along a row, because the diagonal is minus the total exit rate.{{cite:nist_weibull_handbook}} (§8.1.6.2, reliability and mean of the exponential case)

Over a short interval of length $h$, the chance of a jump from $i$ to $j\neq i$ is $q_{ij}h+o(h)$, and the chance of still being in $i$ is $1-\nu_i h+o(h)$.

## Definition
On a finite state space the off-diagonal entries satisfy $q_{ij}\ge 0$ for $j\neq i$, and $q_{ii}=-\sum_{j\neq i}q_{ij}$. The matrix $Q=(q_{ij})$ is the generator. An absorbing state has a zero row.

For the two-state chain the only off-diagonal entries are the two rates, so each jump probability is $1$. The chain alternates. The randomness is in the holding times, not in the destination.

## Interpretation — Where the time is spent
The stationary row $\pi$ solves $\pi Q=0$ and $\pi_0+\pi_1=1$. For the rates $2$ and $4$,
$$
-2\pi_0+4\pi_1=0
$$
gives $\pi_0=2\pi_1$, hence $\pi=(2/3,1/3)$. The same weights come from the mean holds: a cycle is an idle spell of mean $1/2$ and a busy spell of mean $1/4$, and $(1/2)/(3/4)=2/3$.

Let $u(t)=\mathrm{P}(X(t)=1\mid X(0)=0)$. The forward equation is $u'(t)=2(1-u(t))-4u(t)=2-6u(t)$, with $u(0)=0$. The solution is
$$
u(t)=\frac13\bigl(1-e^{-6t}\bigr).
$$
At $t=1$, $u(1)=(1-e^{-6})/3\approx 0.3325$, already close to the stationary value $1/3\approx 0.3333$.

## Properties
Balance, the holding-time mean, and the explicit transition are checked by differentiation.{{cite:nist_weibull_handbook}} (§8.1.6.2, reliability and mean of the exponential case)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
With $\pi=(2/3,1/3)$ and the matrix above, the first column of $\pi Q$ is $(2/3)(-2)+(1/3)(4)=-4/3+4/3=0$. The second column is $(2/3)(2)+(1/3)(-4)=4/3-4/3=0$.

An exponential holding time of rate $\nu$ has survival $e^{-\nu t}$ and mean $\int_0^{\infty}e^{-\nu t}\,\mathrm{d}t=1/\nu$. The idle and busy means are therefore $1/2$ and $1/4$.

Differentiate $u(t)=(1/3)(1-e^{-6t})$. Then $u(0)=0$ and $u'(t)=2e^{-6t}$. The forward right-hand side is $2-6u(t)=2-2(1-e^{-6t})=2e^{-6t}$. The two sides agree. As $t\to\infty$, $u(t)\to 1/3$.
:::
:::

## Statistical use — Reading a rate diagram
A diagram labelled with rates is not a transition matrix. The number $2$ on the idle-to-busy arrow is not a probability. The jump probability is $2/2=1$, and the mean wait is $1/2$. Confusing the rate with a one-step probability produces a matrix whose rows do not sum to $1$ and whose entries can exceed $1$.

The matrix exponential $P(t)=e^{tQ}$ solves both the forward equation $P'(t)=P(t)Q$ and the backward equation $P'(t)=QP(t)$, with $P(0)=I$, because the series $\sum (tQ)^n/n!$ commutes with $Q$. For the two-state chain the $(0,1)$ entry of that exponential is the function $u(t)$ above.

## Worked example
Rates $2$ and $4$, as above. Stationary probabilities $2/3$ and $1/3$. Mean holds $0.5$ and $0.25$ hours. At time $1$, starting from idle, the probability of being busy is about $0.3325$.

The embedded jump chain is
$$
K=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}.
$$
It is periodic. The continuous-time chain is not: the exponential clocks destroy the parity, and $u(t)$ rises smoothly toward $1/3$ instead of oscillating.

**Your turn.** Change the busy-to-idle rate from $4$ to $2$, and keep the idle-to-busy rate at $2$. Find the stationary probability of idle, and the mean length of a busy spell.

::: {.callout-tip collapse="true" title="Answer"}
Now $Q$ has off-diagonal entries $2$ and $2$, so the mean holds are both $1/2$. The idle proportion is $(1/2)/(1/2+1/2)=1/2$. The stationary distribution is $(1/2,1/2)$, and a busy spell has mean $1/2$ hour.
:::

## Common misconceptions
A generator row does not sum to $1$. It sums to $0$. The jump chain is the matrix that sums to $1$.

A rate larger than $1$ is not a mistake. Rate $4$ per hour means the mean hold is $15$ minutes. The probability of a jump in a small interval of length $h$ is about $4h$, which is below $1$ when $h<1/4$.

The stationary distribution is not the jump chain's stationary distribution in every chain, but in this alternating example both put mass $1/2$ and $1/2$ on the two states only when the rates are equal. With rates $2$ and $4$ the jump chain is still alternating, so its long-run proportion of visits is $1/2$, while the time-average proportion of idle time is $2/3$. Visits and time are different.

## Assumptions and limits — Explosion and a moving rate
On a finite state space the rates are bounded, so only finitely many jumps occur in a finite time. On a countable space a pure-birth process that jumps from $n$ to $n+1$ at rate $2^n$ can make infinitely many jumps in a finite interval. The matrix exponential formula used above is a finite-state fact.

If the idle-to-busy rate depends on the clock time, the chain is no longer time-homogeneous. A single matrix $Q$ no longer describes every instant, and $u(t)=(1/3)(1-e^{-6t})$ ceases to solve the forward equation.

The exponential hold is memoryless. A holding time that is always exactly $15$ minutes is not exponential, and the state "busy" is then not enough: the elapsed busy time still matters.

## Connections
The [holding time](holding-time.qmd) is the exponential wait. The [jump chain](jump-chain.qmd) carries the probabilities $q_{ij}/\nu_i$. A [Poisson process](homogeneous-poisson-process.qmd) is the continuous-time chain that only steps upward, at a constant rate. The two-state calculation is the smallest case in which a rate diagram, a stationary distribution, and a forward equation can be written in full.

## Check yourself
### Row sums
What do the two rows of the rate-$2$ and rate-$4$ generator sum to?

::: {.callout-tip collapse="true" title="Answer"}
Each row sums to $0$: $-2+2=0$ and $4-4=0$.
:::

### Time versus visits
With those rates, what fraction of visits does the jump chain spend idle, and what fraction of time does the continuous-time chain spend idle?

::: {.callout-tip collapse="true" title="Answer"}
The jump chain alternates, so half of the visits are idle. The time average is $2/3$, because idle spells last twice as long as busy spells.
:::

### One hour
Starting idle, about how large is the probability of being busy after one hour, and what is the stationary value it is approaching?

::: {.callout-tip collapse="true" title="Answer"}
The probability is $(1-e^{-6})/3\approx 0.3325$. The stationary probability of busy is $1/3\approx 0.3333$.
:::

## History
The generator records rates rather than one-step probabilities. For the two-state machine the stationary distribution is the normalised vector of mean holding times, and the chance of being busy, starting from idle, solves a linear differential equation whose limit is that same stationary value.
