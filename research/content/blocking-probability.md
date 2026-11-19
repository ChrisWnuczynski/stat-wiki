## Lead context
Blocking is an arrival-based probability; identifying it with a stationary occupancy probability requires an assumption about how arrivals sample the system.

## Motivating example
A service desk has a finite waiting area. It can avoid an unbounded queue by turning customers away, even when the offered work exceeds its processing capacity. Designing the waiting area therefore requires a loss probability as well as an average queue length. The fraction of time the room is full and the fraction of customers rejected answer different questions. Poisson arrivals link them under a nonanticipation condition.{{cite:wolff1982_pasta}} (§1, pp. 224–225)

## Definition — Offered arrivals and available capacity
[]{#property-pasta}

Let $N(t-)$ count customers immediately before an offered arrival, including the one in service, and let the total capacity be $K$. An arrival is blocked when $N(t-)=K$. In a stationary ergodic system with an exogenous Poisson arrival stream whose future arrivals cannot be anticipated by the occupancy process, the long-run arrival fraction blocked equals $\pi_K$. This is the Poisson-arrivals-see-time-averages principle, applied to the full state.{{cite:wolff1982_pasta}} (§1, Thm. 1, pp. 224–225)

For the finite $M/M/1/K$ model, offered arrivals have rate $\lambda$ and service completions have rate $\mu$ whenever the server is busy. An accepted arrival increments the occupancy below $K$; a blocked arrival leaves it unchanged. For $\rho=\lambda/\mu$, stationary weights satisfy $\pi_{n+1}=\rho\pi_n$, giving
$$
\pi_n=\frac{\rho^n}{\sum_{j=0}^K\rho^j},\qquad0\le n\le K.
$$
The finite normaliser works for every positive load, including loads at or above one. Stationarity is a property of the occupancy chain; Poisson sampling is the extra step that identifies its full-state probability with blocking.{{cite:durrett2019}} (§5.5, detailed balance and stationary measures){{cite:wolff1982_pasta}} (§1)

## Properties — A normalised birth–death calculation
Choose a constant $c\ge\lambda+\mu$ and form the discrete transition matrix $P=I+Q/c$ from the finite occupancy generator $Q$. Neighbouring probabilities satisfy $\pi_nP_{n,n+1}=\pi_{n+1}P_{n+1,n}$, because both sides equal $\lambda\pi_n/c$. Summing these balances proves $\pi P=\pi$, equivalently $\pi Q=0$. This gives a direct finite-state derivation of the weights.{{cite:durrett2019}} (§5.5, detailed balance)

For $\rho\ne1$, summing the geometric series yields
$$
B_K=\pi_K=\frac{(1-\rho)\rho^K}{1-\rho^{K+1}}.
$$
At $\rho=1$, the weights are all one and $B_K=1/(K+1)$. There is no singularity in the probability model at this value; only the geometric-series quotient needs its limiting interpretation. The accepted rate is $\lambda(1-B_K)$, and equilibrium flow also makes it $\mu(1-\pi_0)$.{{cite:durrett2019}} (§5.5, stationary balance equations)

For $K\ge1$, write $Z(\rho)=\sum_{j=0}^K\rho^j$. Differentiation gives $dB_K/d\rho=B_K(K-\mathbb E_\pi N)/\rho>0$. Every state below capacity has positive stationary mass, so $\mathbb E_\pi N<K$. This proves that blocking increases strictly with offered load, rather than inferring the trend from a few examples.

## Worked example
Take $\lambda=2$, $\mu=3$ and total capacity $K=2$. The weights are $1,2/3,4/9$, whose sum is $19/9$. Thus
$$
(\pi_0,\pi_1,\pi_2)=(9,6,4)/19,\qquad B_2=4/19=0.210526.
$$
The accepted rate is $2(1-4/19)=30/19=1.578947$ per unit time. The completion rate is independently $3(1-9/19)=30/19$. Counting the two customers as two waiting places would instead produce capacity three, so the capacity convention matters.

**Your turn.** Keep capacity two and set $\lambda=\mu$. Find the blocking probability and accepted fraction of arrivals.

::: {.callout-tip collapse="true" title="Answer"}
The three occupancy states are equally likely. Blocking is $1/3$, and the accepted fraction is $2/3$. Equal offered and service rates do not imply that every offered customer is accepted.
:::

## Assumptions and limits — When time averages do not describe arrivals
Ergodicity makes long-run time fractions equal the fixed stationary probabilities. Without it, a stationary process can have random limiting time fractions; PASTA relates arrival observations to the corresponding time averages under its limit conditions.

For a general arrival process, arrivals may systematically occur at times when the system is unusually empty or full. A stationary time fraction by itself then does not determine the arrival fraction blocked. PASTA also permits interaction: an arrival may change occupancy immediately after seeing its pre-arrival value. The restriction is nonanticipation of future Poisson arrivals, rather than independence of the entire occupancy path from the arrival path.{{cite:wolff1982_pasta}} (§§1–2, pp. 224–227)
