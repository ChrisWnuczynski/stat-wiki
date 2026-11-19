## Motivating example
A service system's customer count changes one person at a time. In stationarity, customers cannot cross the boundary between counts $n$ and $n+1$ persistently faster in one direction than the other. That single-boundary observation turns a large system of balance equations into a recurrence for the stationary weights.{{cite:pishro_nik2014}} (§11.3.2)

## Definition — Rates and flows across a boundary
Consider a nonexplosive birth–death process on the nonnegative integers, with positive upward rates $\lambda_n$ and positive downward rates $\mu_n$ for $n\ge1$. The downward rate at zero is zero. In a stationary law, probability flow upward through a boundary is $\pi_n\lambda_n$, and flow downward through the same boundary is $\pi_{n+1}\mu_{n+1}$. Their equality gives
$$
\pi_{n+1}=\pi_n\frac{\lambda_n}{\mu_{n+1}}.
$$
The discrete-time analogue replaces rates by adjacent-state transition probabilities. In both settings, repeatedly applying adjacent balance gives product-form weights.{{cite:durrett2019}} (§5.5, Ex. 5.5.4, p. 301)

## Properties — Normalisation is an existence question
Starting with weight $w_0=1$, define $w_n=\prod_{j=0}^{n-1}\lambda_j/\mu_{j+1}$. A stationary probability constructed from these weights requires $\sum_{n\ge0}w_n<\infty$; its normalising constant is then the reciprocal of that sum. Formal balance equations alone do not turn an infinite total weight into a probability law. For infinite-state processes, nonexplosion is a separate requirement concerning the number of jumps in finite time.{{cite:siegrist_birthdeath2022}} (§15.21, “Limiting Behavior and Stationary Distributions”)

In a finite chain, the implication from adjacent balance to global balance is direct. For an interior state, incoming flow is
$$
\pi_{n-1}\lambda_{n-1}+\pi_{n+1}\mu_{n+1}
=\pi_n\mu_n+\pi_n\lambda_n,
$$
which equals outgoing flow. The boundary equations follow from their sole adjacent edge. Thus the vector solves $\pi Q=0$ for the generator $Q$.{{cite:pishro_nik2014}} (§11.3.2)

## Worked example — A three-state system
Take upward rates $\lambda_0=2$, $\lambda_1=3$ and downward rates $\mu_1=4$, $\mu_2=6$, with no transition above state $2$. Adjacent balance gives weights $1$, $2/4=1/2$, and $(1/2)(3/6)=1/4$. They sum to $7/4$, so
$$
\pi=(4/7,2/7,1/7),\qquad
Q=\begin{pmatrix}-2&2&0\\4&-7&3\\0&6&-6\end{pmatrix}.
$$
Multiplication verifies $\pi Q=0$. The stationary mean count is $0(4/7)+1(2/7)+2(1/7)=4/7$. This checks both the normalisation and the two separate flow equations.{{cite:pishro_nik2014}} (§11.3.2)

For constant upward rate $\lambda$ and constant downward rate $\mu$ on the infinite state space, the weights become $\rho^n$ with $\rho=\lambda/\mu$. Their sum is finite precisely when $\rho<1$, giving $\pi_n=(1-\rho)\rho^n$. At $\lambda=2$, $\mu=4$, the first three masses are $1/2,1/4,1/8$, and the mean is $1$.{{cite:siegrist_birthdeath2022}} (§15.21, constant birth and death rates)

**Your turn.** Multiply all four rates of the three-state system by $10$. What happens to the stationary law?

::: {.callout-tip collapse="true" title="Answer"}
Every adjacent-rate ratio is unchanged, so the stationary probabilities remain $(4/7,2/7,1/7)$. Holding times are divided by $10$; the stationary state proportions do not change.
:::
