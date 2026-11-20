## Lead context
The third symbol is an infinite number of servers: every arrival starts its own service immediately.

## Motivating example
A model of files downloading simultaneously might treat each file's completion time as independent of the others. The quantity of interest is then the number of active files, rather than a waiting line for one server. The infinite-server idealisation removes congestion delays by assuming service capacity expands with the number present. It is appropriate only when that independence is a useful approximation.{{cite:shortle2018_queueing}} (Ch. 1, pp. 7–8, Tbl. 1.1)

## Definition — Constant arrivals and proportional departures
Let arrivals form a Poisson process of rate $\lambda>0$, and let service times be independent exponential variables of rate $\mu>0$, independent of arrivals. With infinitely many servers, $N(t)$ is a birth–death process with rates
$$
q_{n,n+1}=\lambda,\qquad q_{n,n-1}=n\mu\quad(n\ge1).
$$
The departure rate is $n\mu$, rather than $\mu$: the first completion among $n$ independent exponential services has that rate. The memoryless property means the number present suffices to specify the future transition rates.{{cite:durrett2012_essentials}} (§4.1, Ex. 4.3, p. 121)

The process cannot make infinitely many transitions in a finite interval when started with finitely many customers. Poisson arrivals are finite on that interval, and departures cannot exceed the initial population plus arrivals. Thus there is no finite-time explosion despite the unbounded departure rates.{{cite:durrett2012_essentials}} (§4.1, queue construction)

## Properties — The factorial makes every positive load admissible
Put $\rho=\lambda/\mu$. Neighbouring stationary flows balance when
$$
\pi_n\lambda=\pi_{n+1}(n+1)\mu.
$$
Iterating gives $\pi_n=\pi_0\rho^n/n!$. The exponential series has finite sum $e^\rho$ for every finite $\rho$, so
$$
\pi_n=e^{-\rho}\frac{\rho^n}{n!},\qquad n=0,1,\ldots.
$$
These probabilities satisfy detailed balance and sum to one, establishing the Poisson stationary law. Its mean and variance are both $\rho$. Increasing arrivals increases the mean number of busy servers, but never creates a finite overload threshold in this model.{{cite:durrett2012_essentials}} (§4.3, Ex. 4.16, p. 132; Thm. 4.5, p. 130)

For a single server, by contrast, the total departure rate stops growing once the server is busy; the corresponding stationary weights are geometric and need $\lambda<\mu$. An infinite waiting room and infinitely many servers describe different capacities.{{cite:durrett2012_essentials}} (§4.5, M/M/1 queue)

## Interpretation — Service without waiting
The waiting time before service is exactly zero. A customer's sojourn time therefore has the service distribution, with mean $1/\mu$. In equilibrium, Little's law agrees:
$$
L=\lambda W=\lambda/\mu.
$$
Little's law uses a long-run arrival rate and a mean time in the system. Its general statement does not require exponential service or Poisson arrivals; those assumptions are what gave this particular Markov occupancy process and its rates.{{cite:shortle2018_queueing}} (Ch. 1, Thm. 1.1, pp. 11–13)

## Worked example
Suppose $\lambda=12$ customers per hour and each service has rate $\mu=4$ per hour. A mean service lasts $1/4$ hour and the equilibrium occupancy is Poisson with mean $3$. Consequently,
$$
P(N=0)=e^{-3}\approx0.049787,\qquad
P(N\ge5)=1-e^{-3}\sum_{k=0}^4\frac{3^k}{k!}\approx0.184737.
$$
The system has at least five simultaneous services about $18.47\%$ of equilibrium time. These probabilities describe occupancy, not the probability of having to wait, which remains zero. The mean time in the system is $3/12=1/4$ hour.{{cite:durrett2012_essentials}} (§4.3, Ex. 4.16, p. 132){{cite:shortle2018_queueing}} (Ch. 1, Thm. 1.1)

**Your turn.** Double the arrival rate while leaving each service rate unchanged. Find mean occupancy, empty probability and mean sojourn.

::: {.callout-tip collapse="true" title="Answer"}
The mean occupancy becomes $24/4=6$ and the empty probability is $e^{-6}\approx0.002479$. The mean sojourn stays $1/4$ hour: extra customers receive extra servers rather than joining a queue.
:::

## Check yourself
### Infinite servers {#self-check-ex-sp-mminf-numbers}
[An M/M/∞ system](../questions/ex-sp-mminf-numbers.qmd): calculate its occupancy and sojourn measures.

::: {.callout-tip collapse="true" title="Answer"}
With $\lambda=6$ and $\mu=2$, $N$ is Poisson with mean $3$. Thus $P(N=0)=e^{-3}\approx0.049787$, $P(N\ge4)=1-e^{-3}(1+3+9/2+27/6)\approx0.352768$, and $W=1/2$ hour. There is no waiting before service.
:::

### Balancing neighbouring states {#self-check-ex-sp-birth-death-pi}
[Birth–death balance on three states](../questions/ex-sp-birth-death-pi.qmd): normalise the local-balance weights.

::: {.callout-tip collapse="true" title="Answer"}
The equations are $\pi_0=\pi_1/3$ and $(2/3)\pi_1=\pi_2$. Weights $(1,3,2)$ solve them and sum to six, giving $(1/6,1/2,1/3)$. The same flow idea yields factorial weights in the infinite-server process, where the downward rate changes with state.
:::
