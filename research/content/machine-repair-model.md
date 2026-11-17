## Motivating example
A small workshop has two identical machines but only one repair station. A failure reduces production and also reduces the number of operating machines exposed to another failure. The repair queue therefore differs from a queue fed by an unlimited external arrival stream. Counting failed machines captures that feedback in a finite continuous-time Markov chain.{{cite:durrett2012_essentials}} (§4.1, continuous-time chains; §4.8, exs. 4.14–4.15, printer repairs)

## Intuition — Competing exponential clocks
Assume each operating machine has an independent exponential failure time with rate $\lambda>0$. A repair has independent exponential duration with rate $\mu>0$, and the repairer works whenever any machine is down. With $N(t)$ machines failed, failures arrive at rate $(2-N(t))\lambda$ and repairs complete at rate $\mu$ when $N(t)>0$. Exponential memorylessness permits the count alone to be Markov. For general lifetimes or repair times, remaining durations or ages may have to enter the state.{{cite:durrett2012_essentials}} (§4.1, definitions and exponential holding times){{cite:siegrist_birthdeath2022}} (Basic Theory, Introduction)

## Properties — Balance, availability and completed repairs
In state order $0,1,2$, the generator is
$$Q=\begin{pmatrix}-2\lambda&2\lambda&0\\\mu&-(\mu+\lambda)&\lambda\\0&\mu&-\mu\end{pmatrix}.$$
Let $r=\lambda/\mu$. Neighbor balance gives weights $w_0=1,w_1=2r,w_2=2r^2$ and normalizer $Z=1+2r+2r^2$. Their normalized vector satisfies $\pi Q=0$: each state's inflow equals its outflow after the two neighboring balance equations are substituted. Finite irreducibility gives the unique stationary law. Scaling both rates by a common factor leaves $r$ and the stationary probabilities unchanged while changing the speed at which transitions occur.{{cite:siegrist_birthdeath2022}} (Limiting Behavior and Stationary Distributions){{cite:durrett2012_essentials}} (§4.3, limiting behavior)

Mean failed machines is $E_\pi N=(2r+4r^2)/Z$, so mean operating machines is $2-E_\pi N$. The repairer is busy with probability $1-\pi_0$. Long-run repair throughput is $\mu(1-\pi_0)$ and must equal the failure throughput $\lambda E_\pi(2-N)$. This identity follows algebraically from $\pi_1\mu=2\lambda\pi_0$ and $\pi_2\mu=\lambda\pi_1$. It is a useful check on units and stationary calculations. Availability of a uniformly chosen machine is $E_\pi(2-N)/2$ by symmetry. Probability that both machines operate is instead $\pi_0$; these are different performance measures.{{cite:siegrist_birthdeath2022}} (Limiting Behavior and Stationary Distributions; Time Reversal)

## Worked example — Repair capacity and downtime
Take failure rate $\lambda=1$ per day and repair rate $\mu=2$ per day. Then $r=1/2$, the weights are $1,1,1/2$, and $\pi=(2/5,2/5,1/5)$. The workshop has on average $4/5$ failed machines and $6/5$ operating machines. A randomly chosen machine is available $3/5$ of the time, while both work together only $2/5$ of the time. The repairer is busy $3/5$ of the time, producing repairs at rate $2(3/5)=6/5$ per day, exactly the mean failure rate $1(6/5)$. The probability of total shutdown is $1/5$.

If two repairers can work independently, the death rate at state two becomes $2\mu$. The stationary weights become $1,1,1/4$, with probabilities $(4/9,4/9,1/9)$. The shutdown probability falls from $1/5$ to $1/9$. This calculation changes the service mechanism; merely doubling a single repairer's speed would also change the rate at state one and give a different comparison.{{cite:siegrist_birthdeath2022}} (Basic Theory, Introduction)

**Your turn.** With one repairer and equal failure and repair rates, find the stationary probabilities and mean operating machines.

::: {.callout-tip collapse="true" title="Answer"}
The weights are $1,2,2$, so the probabilities are $1/5,2/5,2/5$. Mean failed machines is $6/5$, hence mean operating machines is $4/5$.
:::

## Connections — A finite source queue
For $M$ machines and $c$ independent repairers, the count model has birth rate $(M-n)\lambda$ and death rate $\min(n,c)\mu$. Multiplying neighbor-rate ratios gives
$$w_n=\prod_{j=0}^{n-1}\frac{(M-j)\lambda}{\min(j+1,c)\mu}.$$
All $M+1$ weights can be normalized for positive rates. There is no unlimited-population stability threshold, but severe congestion can still mean that most machines are down. Stationarity guarantees a probability law, not acceptable performance.{{cite:durrett2012_essentials}} (§4.5, Markovian queues){{cite:siegrist_birthdeath2022}} (Limiting Behavior and Stationary Distributions)

## Statistical use — Time until a total shutdown
Stationary shutdown probability and the first time both machines fail are different questions. Let $t_i$ be the mean time to hit state two starting at $i$. Exponential holding times and the jump probabilities give
$$t_0=\frac1{2\lambda}+t_1,\qquad
 t_1=\frac1{\lambda+\mu}+\frac\mu{\lambda+\mu}t_0.$$
A repair from state one returns to zero; a failure reaches the target and contributes no further time. Solving the two equations gives $t_0=(3\lambda+\mu)/(2\lambda^2)$ and $t_1=t_0-1/(2\lambda)$. For the worked rates $\lambda=1,\mu=2$, these means are $2.5$ days and two days. A stationary probability such as $1/5$ cannot replace this duration. The first-passage calculation depends on the initial state, while the stationary percentage averages a long run of repeated shutdowns and recoveries. Both can matter for maintenance planning.{{cite:durrett2012_essentials}} (§4.4, exit distributions and hitting times)
