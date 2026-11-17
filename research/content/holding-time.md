## Lead context
A holding time is the random wait a continuous-time chain spends in its current state before it jumps.

## Motivating example
A state with exit rates $4$ and $6$ per hour has total exit rate $10$, so the mean hold is $0.1$ hour. After $0.3$ hour the chance of still being there is $e^{-3}\approx 0.0498$. The faster exit is chosen with probability $0.6$.

## Intuition — The wait must forget its age
If the time already spent in the state told you anything about the time still to come, the present state would not be a sufficient summary of the past. The wait therefore has to be memoryless, which for a positive continuous time is the exponential law. Several exits from the same state are a race of independent exponential clocks. The first clock to ring decides both how long the hold lasted and which state comes next.{{cite:nist_weibull_handbook}} (§8.1.6.2, the exponential case of the Weibull)

## Definition — An exponential wait at the exit rate
From state $i$, let $q_{ij}\ge 0$ be the rate of jumping to $j\neq i$, and write $\nu_i=\sum_{j\neq i}q_{ij}$ for the total exit rate. The holding time $H_i$ is exponential with rate $\nu_i$, so $\Pr(H_i>t)=e^{-\nu_i t}$ for $t\ge 0$. When $\nu_i>0$ the mean hold is $1/\nu_i$. The probability that the jump goes to $j$ is $q_{ij}/\nu_i$, and that choice is independent of the length of the hold. If $\nu_i=0$ the state is absorbing and the hold does not end.{{cite:nist_weibull_handbook}} (§8.1.6.2, reliability and mean of the exponential case)

## Properties — The minimum of independent exponential clocks
Start an independent exponential clock of rate $q_{ij}$ for each $j\neq i$. The minimum of those clocks is exponential with rate $\nu_i$, and the probability that clock $j$ rings first is $q_{ij}/\nu_i$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
An exponential clock of rate $q$ has survival function $e^{-qt}$. Independent clocks survive past $t$ together with probability $\prod_j e^{-q_{ij}t}=e^{-\nu_i t}$, which is the exponential survival function of rate $\nu_i$. The probability that clock $j$ is first equals its share of the total rate, $q_{ij}/\nu_i$, because the same product calculation with one clock singled out leaves that ratio. The identity does not depend on $t$, so the destination is independent of the holding time.{{cite:nist_weibull_handbook}} (§8.1.6.2, exponential reliability)
:::
:::

## Worked example
Suppose state $i$ has two exits, at rates $4$ and $6$ per hour. The exit rate is $\nu_i=10$ per hour, so the mean hold is $0.1$ hour. The chance of still being in $i$ after $0.3$ hour is $e^{-3}\approx 0.0498$. The faster exit is chosen with probability $6/10=0.6$, whether the hold was short or long.{{cite:nist_weibull_handbook}} (§8.1.6.2, exponential mean and reliability)

**Your turn.** Three exits have rates $1$, $1$ and $2$ per hour. Find the mean hold, the probability that the hold exceeds half an hour, and the probability that the rate-$2$ exit wins the race.

::: {.callout-tip collapse="true" title="Answer"}
The exit rate is $4$ per hour, so the mean hold is $1/4=0.25$ hour. The survival probability at half an hour is $e^{-2}\approx 0.1353$. The rate-$2$ exit wins with probability $2/4=0.5$.
:::

## Connections
The holding time uses the [memoryless property](memoryless-property.qmd) of the [exponential distribution](exponential-distribution.qmd). The probabilities $q_{ij}/\nu_i$ are the transitions of the embedded jump chain, a discrete-time [Markov chain](discrete-time-markov-chain.qmd) that records the sequence of states and forgets the clock. The shape-$1$ [Weibull distribution](weibull-distribution.qmd) is this exponential lifetime.{{cite:nist_weibull_handbook}} (§8.1.6.2, shape equal to one)

## Check yourself
**1.** An exit rate of $2$ per hour has already lasted $1$ hour. What is the probability that it lasts at least one further hour?

::: {.callout-tip collapse="true" title="Answer"}
Memorylessness makes the remaining wait a fresh exponential of rate $2$, so the probability is $e^{-2}\approx 0.1353$. The hour already spent does not appear in the answer.
:::

**2.** Exit rates $3$ and $1$ leave a state. What is the probability that the rate-$3$ clock rings first, and what is the mean hold?

::: {.callout-tip collapse="true" title="Answer"}
The total rate is $4$, so the rate-$3$ clock wins with probability $3/4=0.75$. The mean hold is $1/4=0.25$ time unit.
:::
