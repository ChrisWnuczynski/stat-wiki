## Motivating example

A server receives more requests than it can keep, and requests arriving to a full buffer are discarded. Measuring attempted requests overstates the rate of completed work. The customer population counted in mean queue length and mean time in the system consists of admitted requests, so those summaries must use the admitted rate.{{cite:durrett2012_essentials}} (§3.2.2, Thm. 3.6, p. 107)

## Definition — Offered, admitted and completed rates

For a finite-capacity queue with Poisson offered arrivals of rate $\lambda$, let $\pi_K$ be the stationary probability of its full state. Poisson arrivals see the stationary state proportions, so the admitted rate is
$$
\lambda_{\mathrm{eff}}=\lambda(1-\pi_K).
$$
When every admitted customer eventually departs, this is the stationary throughput. A finite-capacity model can have a stationary law even when the offered rate exceeds maximum service capacity: the excess offered work is refused.{{cite:durrett2012_essentials}} (§3.2.3, Thm. 3.7, p. 108; §4.5, Ex. 4.24, pp. 138–140)

For birth and death rates $\lambda_n,\mu_n$, the stationary upward and downward flows are $\sum_n\pi_n\lambda_n$ and $\sum_n\pi_n\mu_n$. Local balance equates each neighbouring pair of flows and hence their totals. For an M/M/1/$K$ queue, they reduce to $\lambda(1-\pi_K)$ and $\mu(1-\pi_0)$. The second expression is service capacity multiplied by the busy fraction.{{cite:siegrist_birthdeath2022}} (§ “Limiting Behavior and Stationary Distributions”)

## Properties — Conservation of customers

Let $A(t)$ and $D(t)$ count admissions and departures. Pathwise,
$$
N(t)-N(0)=A(t)-D(t).
$$
For bounded capacity, dividing by $t$ makes the left side tend to zero. Whenever the two rates have limits, those limits agree. This argument explains flow conservation without assuming that departure times form a Poisson process. Relating mean occupancy to mean sojourn additionally uses Little's formula with the admitted customer rate.{{cite:durrett2012_essentials}} (§3.2.2, Thm. 3.6, p. 107; §4.3, Lem. 4.3, p. 128)

## Worked example

Take $\lambda=4$ per hour, $\mu=2$ per hour and capacity two, including the customer in service. The stationary weights are $1,2,4$, giving $\pi=(1,2,4)/7$. The admitted rate is $4(1-4/7)=12/7$ per hour; independently, the completed rate is $2(1-1/7)=12/7$ per hour. The mean occupancy is $10/7$, so mean sojourn of admitted customers is $(10/7)/(12/7)=5/6$ hours.

Conditioning on admission gives another check. An admitted arrival finds zero customers with probability $(1/7)/(3/7)=1/3$ and one customer with probability $2/3$. Under first-come-first-served exponential service, its mean time is therefore $(1/3)(1/2)+(2/3)(2/2)=5/6$ hours. The admission condition is essential to the weights.{{cite:durrett2012_essentials}} (§4.5, Ex. 4.24, pp. 139–140)

**Your turn.** Keep capacity two but set both rates to two per hour. What are the full-state probability and throughput?

::: {.callout-tip collapse="true" title="Answer"}
The three stationary weights are equal, so $\pi_2=1/3$ and throughput is $2(1-1/3)=4/3$ per hour. The queue is full one third of the time, despite equal offered and service rates.
:::

## Connections — State-dependent service

With $c$ identical servers, the departure intensity in state $n$ is $\mu\min(n,c)$. Thus the average completion rate is $\sum_n\pi_n\mu\min(n,c)$, bounded by $c\mu$. That average, rather than the service rate of a permanently busy server, is the quantity that must balance admissions.{{cite:siegrist_queuing2022}} (§ “Infinitesimal Generator”)
