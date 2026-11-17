## Motivating example
A clinic has several service stations and room for only a fixed number of patients. Adding a server changes how quickly customers leave when the clinic is busy; adding waiting space changes how often arrivals are rejected. These choices affect different parts of the queue model. An unlimited waiting room needs a stability condition, whereas a finite room can have a stationary distribution even when it blocks many arrivals.{{cite:durrett2012_essentials}} (§4.5, Markovian Queues)

## Intuition — Count customers in service as well as waiting
In an M/M/$c$ queue, arrivals form a Poisson process of rate $\lambda$, service times are independent exponential variables of rate $\mu$ per busy server, and one queue feeds $c$ parallel servers. With $n$ customers present, $\min(n,c)$ servers are busy, so the total completion rate is $\min(n,c)\mu$. The customer count includes both service and waiting. In M/M/$c$/$K$, the capacity $K\ge c$ is the total number in the system, and an arrival at state $K$ is blocked.{{cite:siegrist_queuing2022}} (Basic Theory, Infinitesimal Generator)

## Properties — Stationary weights and flow
Put $a=\lambda/\mu$ and $\rho=\lambda/(c\mu)$. Neighbor balance gives weights
$$w_n=\frac{a^n}{n!}\quad(0\le n\le c),\qquad
w_n=\frac{a^c}{c!}\rho^{n-c}\quad(n\ge c).$$
For an unlimited queue their sum is finite exactly when $\rho<1$. At finite capacity, normalize only over $0\le n\le K$, so every positive finite load is allowed. These formulas follow by multiplying $\pi_{n+1}/\pi_n=\lambda/\{\min(n+1,c)\mu\}$; substitution verifies each neighboring balance equation.{{cite:durrett2012_essentials}} (§4.5){{cite:siegrist_birthdeath2022}} (Limiting Behavior and Stationary Distributions)

The stationary probability $\pi_K$ is the blocking probability seen by independent Poisson arrivals. The arrival stream has no dependence on the present state, so its expected blocked rate is $\lambda P(N=K)$; dividing by its rate gives $\pi_K$. Accepted throughput is $\lambda_{\mathrm{eff}}=\lambda(1-\pi_K)$. Balance also gives $\lambda_{\mathrm{eff}}=\mu E\min(N,c)$, the average completion rate. This equality can be verified by summing neighboring flows. It is a useful numerical check on any finite-capacity calculation.{{cite:durrett2012_essentials}} (§4.5, finite waiting-room examples)

For an unlimited stable queue, the probability that all servers are busy is
$$P(N\ge c)=\pi_0\frac{a^c}{c!}\frac1{1-\rho}.$$
The expected queue length follows from the geometric tail:
$$L_q=\pi_0\frac{a^c}{c!}\frac{\rho}{(1-\rho)^2}.$$
Summing $k\rho^k$ proves the second expression. Mean waiting before service is $L_q/\lambda$ under the stationary flow version of Little's law. At finite capacity, use accepted throughput in that law for admitted customers.{{cite:durrett2012_essentials}} (§§3.2, 4.5)

## Worked example — Two servers with and without a capacity limit
Let $\lambda=2$ and $\mu=2$ per hour, with two servers. Then $a=1$, $\rho=1/2$, and the unlimited normalizer is $1+1+(1/2)/(1/2)=3$. Thus $\pi_0=1/3$, probability of waiting is $1/3$, mean queue length is $1/3$, and mean waiting is $1/6$ hour, or ten minutes.

Limit capacity to $K=3$. The weights are $1,1,1/2,1/4$, giving $\pi=(4,4,2,1)/11$. Blocking probability is $1/11$ and throughput is $20/11$ per hour. Mean customers present is $\{4+4+3\}/11=1$. Mean time in the system for admitted customers is therefore $1/(20/11)=11/20$ hour. The average busy-server count is $10/11$, yielding the same throughput $2(10/11)$. A finite room limits delay by rejecting work, which is a service tradeoff rather than unlimited capacity at no cost.{{cite:durrett2012_essentials}} (§4.5)

**Your turn.** For M/M/1/2 with $\lambda=\mu$, find the blocking probability and throughput.

::: {.callout-tip collapse="true" title="Answer"}
The three stationary weights are equal, so $\pi_2=1/3$. Throughput is $\lambda(1-1/3)=2\lambda/3$, equal to $\mu P(N>0)$.
:::

## Assumptions and limits
Memoryless service is what allows the customer count alone to determine departure rates. Correlated arrivals, priorities, abandonment and general service-time distributions can require richer states or other queue models. A stable unlimited queue can still have a large waiting time near saturation. A finite queue's stationary existence says nothing by itself about whether blocking or delay meets a service target.{{cite:siegrist_queuing2022}} (Basic Theory){{cite:durrett2012_essentials}} (§4.5)
