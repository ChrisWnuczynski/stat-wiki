## Motivating example
A clinic has several service stations and room for only a fixed number of patients. Adding a server changes how quickly customers leave when the clinic is busy; adding waiting space changes how often arrivals are rejected. These choices affect different parts of the queue model. An unlimited waiting room needs a stability condition, whereas a finite room can have a stationary distribution even when it blocks many arrivals.{{cite:durrett2012_essentials}} (§4.3, Lem. 4.3, p. 128; §4.5, Ex. 4.24, pp. 138–140)

## Intuition — Count customers in service as well as waiting
In an M/M/$c$ queue, arrivals form a Poisson process of rate $\lambda$, service times are independent exponential variables of rate $\mu$ per busy server, and one queue feeds $c$ parallel servers. With $n$ customers present, $\min(n,c)$ servers are busy, so the total completion rate is $\min(n,c)\mu$. The customer count includes both service and waiting. In M/M/$c$/$K$, the capacity $K\ge c$ is the total number in the system, and an arrival at state $K$ is blocked.

## Properties — Stationary weights and flow
Put $a=\lambda/\mu$ and $\rho=\lambda/(c\mu)$. Neighbor balance gives weights
$$w_n=\frac{a^n}{n!}\quad(0\le n\le c),\qquad
w_n=\frac{a^c}{c!}\rho^{n-c}\quad(n\ge c).$$
For an unlimited queue their sum is finite exactly when $\rho<1$. At finite capacity, normalize only over $0\le n\le K$, so every positive finite load is allowed. These formulas follow by multiplying $\pi_{n+1}/\pi_n=\lambda/\{\min(n+1,c)\mu\}$; substitution verifies each neighboring balance equation. A finite irreducible birth-death chain has a stationary distribution for every positive $\lambda$ and $\mu$, including $\lambda>c\mu$. The unlimited chain needs $\rho<1$ because its state space is infinite.{{cite:durrett2012_essentials}} (§4.3, Lem. 4.3, p. 128; §4.5, Ex. 4.24, pp. 138–140)

The stationary probability $\pi_K$ is the blocking probability seen by independent Poisson arrivals. The arrival stream has no dependence on the present state, so its expected blocked rate is $\lambda P(N=K)$; dividing by its rate gives $\pi_K$. Accepted throughput is $\lambda_{\mathrm{eff}}=\lambda(1-\pi_K)$. Balance also gives $\lambda_{\mathrm{eff}}=\mu E\min(N,c)$, the average completion rate. This equality can be verified by summing neighboring flows. It is a useful numerical check on any finite-capacity calculation.{{cite:durrett2012_essentials}} (§3.2.3, Thm. 3.7, p. 108; §4.5, Ex. 4.24, pp. 138–140)

For an unlimited stable queue, the probability that all servers are busy is
$$P(N\ge c)=\pi_0\frac{a^c}{c!}\frac1{1-\rho}.$$
The expected queue length follows from the geometric tail:
$$L_q=\pi_0\frac{a^c}{c!}\frac{\rho}{(1-\rho)^2}.$$
Summing $k\rho^k$ proves the second expression. Mean waiting before service is $L_q/\lambda$ under the stationary flow version of Little's law. At finite capacity, use accepted throughput in that law for admitted customers.{{cite:durrett2012_essentials}} (§3.2.2, Thm. 3.6, p. 107; §4.3, Lem. 4.3, p. 128)

## Worked example — Two servers with and without a capacity limit
Let $\lambda=2$ and $\mu=2$ per hour, with two servers. Then $a=1$, $\rho=1/2$, and the unlimited normalizer is $1+1+(1/2)/(1/2)=3$. Thus $\pi_0=1/3$, probability of waiting is $1/3$, mean queue length is $1/3$, and mean waiting is $1/6$ hour, or ten minutes.

Limit capacity to $K=3$. The weights are $1,1,1/2,1/4$, giving $\pi=(4,4,2,1)/11$. Blocking probability is $1/11$ and throughput is $20/11$ per hour. Mean customers present is $\{4+4+3\}/11=1$. Mean time in the system for admitted customers is therefore $1/(20/11)=11/20$ hour. The average busy-server count is $10/11$, yielding the same throughput $2(10/11)$. A finite room limits delay by rejecting work, which is a service tradeoff rather than unlimited capacity at no cost.{{cite:durrett2012_essentials}} (§4.3, Lem. 4.3, p. 128; §4.5, Ex. 4.24, pp. 138–140)

**Your turn.** For M/M/1/2 with $\lambda=\mu$, find the blocking probability and throughput.

::: {.callout-tip collapse="true" title="Answer"}
The three stationary weights are equal, so $\pi_2=1/3$. Throughput is $\lambda(1-1/3)=2\lambda/3$, equal to $\mu P(N>0)$.
:::

## Assumptions and limits
Memoryless service is what allows the customer count alone to determine departure rates. Correlated arrivals, priorities, abandonment and general service-time distributions can require richer states or other queue models. A stable unlimited queue can still have a large waiting time near saturation. A finite queue's stationary existence says nothing by itself about whether blocking or delay meets a service target.{{cite:durrett2012_essentials}} (§4.3, Lem. 4.3, p. 128; §4.5, Ex. 4.24, pp. 138–140)

## Interpretation — Capacity counts everyone in the system
The symbol M/M/$c$/$K$ fixes four modelling choices: Poisson arrivals, exponential service, $c$ servers, and a maximum of $K$ customers present. The $K$ customers include those in service. In an M/M/2/5 system, a full system has two customers in service and three waiting. An arrival that finds five customers present is blocked. An arrival that finds four present enters and waits. Reading $K$ as the number of waiting seats would invent a sixth place in the system and a different birth-death chain. The worked M/M/2/3 system has one waiting seat: states $0,1,2,3$, with state $3$ meaning both servers busy and one customer waiting.{{cite:durrett2012_essentials}} (§4.3, Lem. 4.3, p. 128; §4.5, Ex. 4.24, pp. 138–140)

The load $\rho=\lambda/(c\mu)$ compares the offered arrival rate with the completion rate when every server is busy. For the worked rates $\lambda=\mu=2$ and $c=2$, $\rho=1/2$. The unlimited queue is stable, $\pi_0=1/3$, the probability of waiting is $1/3$, and the mean wait before service is $1/6$ hour. The four weights $1,1,1/2,1/4$ sum to $11/4$. The unlimited normalizer is $3$, so the unlimited chain puts probability $(11/4)/3=11/12$ on $\{0,1,2,3\}$. Conditioning that unlimited stationary law on $N\le3$ divides the weights by $11/4$ and recovers the finite-capacity probabilities $(4,4,2,1)/11$. The stationary laws agree for that reason. The processes do not: an arrival that finds three customers present is lost in the finite system and moves the unlimited system to state $4$. Blocking, throughput, and the time spent in the room are properties of the finite transition rates. The conditional unlimited probabilities describe only the occupied states under the infinite-room stationary law.{{cite:durrett2012_essentials}} (§4.3, Lem. 4.3, p. 128; §4.5, Ex. 4.24, pp. 138–140)

## Common misconceptions
The inequality $\lambda>c\mu$ prevents a stationary distribution for the unlimited M/M/$c$ queue, because the weights then grow geometrically and cannot be normalized. It does not prevent a stationary distribution for M/M/$c$/$K$. The state space is finite, every rate that should be positive is positive, and the chain is irreducible. High offered load raises the blocking probability $\pi_K$. The chain still has a unique stationary law. Treating "overloaded" as a synonym for "no steady state" imports the infinite-room theorem into a finite room.{{cite:durrett2012_essentials}} (§4.3, Lem. 4.3, p. 128; §4.5, Ex. 4.24, pp. 138–140)

Little's relation for admitted customers uses the throughput $\lambda(1-\pi_K)$, not the offered rate $\lambda$. In the worked finite system the mean number present is $1$ and the throughput is $20/11$ per hour, so the mean time in system for an admitted customer is $11/20$ hour. Dividing by the offered rate $2$ would give $1/2$ hour and would count blocked arrivals as if they had entered. The identity $\lambda(1-\pi_K)=\mu E\min(N,c)$ is the balance check. Here $\min(N,2)$ has mean $10/11$ and $\mu=2$, and $2\times10/11=20/11$. A numerical solution that violates this identity has a normalization or a rate error.{{cite:durrett2012_essentials}} (§3.2.2, Thm. 3.6, p. 107; §4.3, Lem. 4.3, p. 128)

An M/M/1/2 queue with $\lambda=\mu$ has equal stationary weights on states $0,1,2$, so the blocking probability is $1/3$ and the throughput is $2\lambda/3$. The single server is busy with probability $2/3$, and $\mu$ times that probability recovers the same throughput. Adding a second server, or a third place in the system, changes both the service rate in the busy states and the set of weights. The one-server calculation is not a bound that automatically applies to the two-server clinic.{{cite:durrett2012_essentials}} (§4.3, Lem. 4.3, p. 128; §4.5, Ex. 4.24, pp. 138–140)
