## Motivating example
A repairable device alternates between working, state $0$, and failed, state $1$. Its failure clock runs at rate $\alpha$ while it works, and its repair clock runs at rate $\beta$ while it is failed. Counting transitions gives an alternating sequence, but observing the device at a fixed elapsed time weights states by how long the device spends in them. The transition probabilities combine these random holding times with the alternating moves.{{cite:siegrist2022_ctmc_transition}} (§15.16, “The Two-State Chain”)

## Definition
For positive rates, the mean working spell is $1/\alpha$ and the mean failed spell is $1/\beta$. A rate has inverse-time units. It gives $P(X(h)=1\mid X(0)=0)=\alpha h+o(h)$ as $h\downarrow0$, rather than a finite-time probability equal to $\alpha$. The generator has rows summing to zero because the short-time probabilities in each row must sum to one.{{cite:siegrist2022_ctmc_transition}} (§15.16, “The Generator Matrix”)

## Properties — Solve both rows of the transition matrix
Put $c=\alpha+\beta$. The forward equation for the probability of state $1$ is $u'=\alpha-cu$. For any initial probability $u(0)=u_0$, multiplying by the integrating factor $e^{ct}$ gives
$$u(t)=\frac\alpha c+\left(u_0-\frac\alpha c\right)e^{-ct}.$$
Taking $u_0=0$ and $u_0=1$ and using complementary probabilities gives
$$P(t)=\frac1c\begin{pmatrix}\beta+\alpha e^{-ct}&\alpha(1-e^{-ct})\\\beta(1-e^{-ct})&\alpha+\beta e^{-ct}\end{pmatrix}.$$
Every row sums to one, $P(0)=I$, and differentiating at zero returns $Q$. The transient part decays at rate $c$, while the limit has each row equal to $\pi=(\beta/c,\alpha/c)$.{{cite:siegrist2022_ctmc_transition}} (§15.16, “The Two-State Chain”, transition-matrix formula)

For another verification, write $\Pi$ for the matrix whose rows are $\pi$. Direct multiplication gives $\Pi^2=\Pi$ and $Q=-c(I-\Pi)$, so $P(t)=\Pi+e^{-ct}(I-\Pi)$. The identities $\Pi(I-\Pi)=(I-\Pi)\Pi=0$ give $P(s)P(t)=P(s+t)$. It also shows that multiplying both rates by a constant changes the speed of approach but leaves the stationary proportions alone.

## Worked example — Failure probability after one hour
Let $\alpha=2$ per hour and $\beta=3$ per hour. The mean working and failed spells are $0.5$ and $1/3$ hours, and the stationary failure probability is $2/5=0.4$. Starting in working order,
$$P_{01}(1)=0.4(1-e^{-5})\approx0.397305.$$
The full one-hour transition matrix is approximately
$$\begin{pmatrix}0.602695&0.397305\\0.595957&0.404043\end{pmatrix}.$$
Starting failed gives a slightly larger one-hour failure probability, although the initial-state difference has already fallen to $e^{-5}\approx0.006738$.

The probability of at least one failure during that hour is instead $1-e^{-2}\approx0.864665$. This is much larger than the probability of being failed at the end, because a device can fail and then be repaired within the hour. “Ever failed” and “failed at observation” are different events. The exponential no-event calculation uses the same waiting-time principle as a Poisson clock.{{cite:durrett2019}} (§3.7, pp. 174–175, exponential waiting times and Poisson processes)

**Your turn.** If $\alpha=1$ and $\beta=4$ per day, find the stationary failure probability. Starting working, find the failure probability after $t=(\log2)/5$ days.

::: {.callout-tip collapse="true" title="Answer"}
The stationary probability is $1/(1+4)=0.2$. At the specified time, $e^{-5t}=1/2$, so the failure probability is $0.2(1-1/2)=0.1$.
:::

## Interpretation — Why alternating jumps do not create periodic observations
The embedded jump chain moves to the other state at every jump, so it alternates deterministically. When $\alpha=\beta=r$, the jump times form a rate-$r$ Poisson process. Starting at zero, state one means an odd number of jumps. The Poisson generating function gives
$$P\{N(t)\text{ odd}\}=\tfrac12(1-e^{-2rt}),$$
which approaches one half smoothly. For unequal rates the jump count is no longer a single homogeneous Poisson count, but the solved matrix still approaches its stationary law. Random time, rather than an alternating jump index, determines the observation.{{cite:durrett2019}} (§3.7, Poisson-process counting law)

## Assumptions and limits
The exponential spell distributions encode memorylessness: a working device's instantaneous failure rate does not depend on its age. Wear, repair quality and time-varying conditions can violate that assumption. If one rate vanishes, the destination state is absorbing and the limiting formula can be read directly with $c>0$. If both vanish, the process never moves, $Q=0$, and every initial distribution is stationary; the positive-rate stationary formula then has no meaning.

Memorylessness is a property of the exponential holding time. A different holding-time law would make the chance of leaving depend on the time already spent in the state.
