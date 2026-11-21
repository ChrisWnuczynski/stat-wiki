## Lead context
Local balance equates the stationary probability flow up an edge of a birth–death chain with the flow back down that same edge.

## Motivating example
States $0,1,2$ have births $1,1,0$ and deaths $2,2$. The un-normalised weights are $1$, $1/2$ and $1/4$. Scaled, they are $4/7$, $2/7$ and $1/7$, and each cut carries the same flow in both directions.

## Intuition — On a path, one cut carries the whole flow
A birth–death chain moves only to a neighbour. Probability can pass the cut between $n$ and $n+1$ in just two ways: a birth in $n$, or a death in $n+1$. In stationarity those two flows match. Global balance at a state is the sum of every such cut that touches the state. On a path, writing the single-edge equation once per cut is enough, and unfolding it gives the stationary weights as a product. {{cite:durrett2019}} (p. 301, birth–death chains and the product formula)

## Definition — The cut equation and the product
With birth rate $\lambda_n$ and death rate $\mu_{n+1}>0$,

$$
\pi_n\lambda_n=\pi_{n+1}\mu_{n+1},
$$

so $\pi_{n+1}=\pi_n\lambda_n/\mu_{n+1}$. Iterating from $\pi_0$ gives

$$
\pi_n=\pi_0\prod_{k=0}^{n-1}\frac{\lambda_k}{\mu_{k+1}}.
$$

The weights are a stationary distribution when they sum to a finite number and are then scaled to sum to $1$. An infinite sum is an invariant measure that cannot be used as a probability. {{cite:durrett2019}} (p. 301, the product may fail to be summable)

## Properties — The product satisfies every cut
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Define $w_0=1$ and $w_{n+1}=w_n\lambda_n/\mu_{n+1}$. Then $w_n\lambda_n=w_{n+1}\mu_{n+1}$ by construction. If $Z=\sum_n w_n<\infty$ and $\pi_n=w_n/Z$, multiplying the cut equation by $1/Z$ leaves it true for $\pi$.
:::
:::

## Worked example — Three states, births $1,1,0$ and deaths $2,2$
States $0,1,2$ have $\lambda_0=1$, $\lambda_1=1$, $\lambda_2=0$, $\mu_1=2$ and $\mu_2=2$. The un-normalised weights are $1$, then $1/2$, then $(1/2)\cdot(1/2)=1/4$. They sum to $7/4$, so

$$
\pi=\Bigl(\frac{4}{7},\frac{2}{7},\frac{1}{7}\Bigr).
$$

The first cut: $\pi_0\lambda_0=4/7$ and $\pi_1\mu_1=(2/7)\cdot 2=4/7$. The second cut: $\pi_1\lambda_1=2/7$ and $\pi_2\mu_2=(1/7)\cdot 2=2/7$.

**Your turn.** Keep the same death rates and set $\lambda_0=2$, $\lambda_1=2$, $\lambda_2=0$. Find the stationary distribution.

::: {.callout-tip collapse="true" title="Answer"}
The weights are $1$, $2/2=1$, and $1\cdot 2/2=1$, summing to $3$. So $\pi=(1/3,1/3,1/3)$. The first cut is $(1/3)\cdot 2=(1/3)\cdot 2$.
:::

## Connections — Detailed balance on a path
[Detailed balance](detailed-balance.qmd) equates flow in both directions on every edge, not only on the edges of a path. Local balance is that equation for a [birth–death chain](birth-death-balance.qmd). {{cite:durrett2019}} (p. 301, birth–death chains) Summing the cut equations that touch one state recovers [global balance](global-balance-and-detailed-balance.qmd) at that state. A finite state space with positive rates along the path has a finite sum, so a stationary distribution exists.
