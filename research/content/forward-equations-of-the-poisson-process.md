## Motivating example
A detector counts arrivals over time. Rather than specifying only the total count in one fixed interval, a process model must explain how probabilities evolve when the observation window grows. The forward equations express incoming probability from count $n-1$ and outgoing probability from count $n$. A homogeneous Poisson process has a constant rate and independent increments.{{cite:durrett2012_essentials}} (§2.2, pp. 80–83)

## Properties — A complete short-interval argument
Put $\Delta_h=N(t+h)-N(t)$. Independence and stationarity of increments give
$$p_n(t+h)=\sum_{j=0}^np_{n-j}(t)P(\Delta_h=j).$$
For fixed $n$, substitute $P(\Delta_h=0)=1-\lambda h+o(h)$, $P(\Delta_h=1)=\lambda h+o(h)$ and $P(\Delta_h\ge2)=o(h)$. The sum has finitely many terms, so after subtracting $p_n(t)$, dividing by $h$ and taking the limit, only the terms for zero and one new arrivals survive. This yields $p_n'=\lambda p_{n-1}-\lambda p_n$, with $p_{-1}=0$. The construction is a pure-birth specialization of the Kolmogorov forward equation.{{cite:durrett2012_essentials}} (§4.2, eq. 4.9–4.11, pp. 124–125)

Multiplying by $e^{\lambda t}$ gives $(e^{\lambda t}p_n(t))'=\lambda e^{\lambda t}p_{n-1}(t)$. Starting with $p_0=e^{-\lambda t}$ and integrating inductively from zero gives
$$p_n(t)=e^{-\lambda t}\frac{(\lambda t)^n}{n!}.$$
These probabilities sum to one by the exponential series, so the solution loses no probability mass. The recursion uniquely determines each coordinate from the preceding one and its initial value. The count and interarrival descriptions are related by $\{N(t)\ge n\}=\{T_n\le t\}$.{{cite:siegrist2020_poisson_process}} (§14.1, random processes and arrival-count relationship)

## Worked example — Probability can be flowing out
At rate two arrivals per hour and time one hour, $(p_0,p_1,p_2)=(e^{-2},2e^{-2},2e^{-2})\approx(0.13534,0.27067,0.27067)$. Their instantaneous derivatives are $p_0'=-0.27067$, $p_1'=-0.27067$ and $p_2'=0$. The probability of exactly two arrivals is at its peak at this time: incoming and outgoing rates balance. This does not mean the count stops increasing; counts only jump upward while probability moves among count states.{{cite:durrett2012_essentials}} (§4.2, ex. 4.7, p. 125)

**Your turn.** For rate three per hour, find the probability of exactly one arrival by half an hour and its derivative with respect to time at that instant.

::: {.callout-tip collapse="true" title="Answer"}
Here $\lambda t=1.5$, so $p_1=1.5e^{-1.5}=0.33470$. Its derivative is $3(p_0-p_1)=-1.5e^{-1.5}=-0.33470$ per hour.
:::

### A generating function solves the entire system
For $0\le z\le1$, define $G(z,t)=\sum_{n\ge0}p_n(t)z^n$. Substituting the Poisson solution gives $G(z,t)=e^{\lambda t(z-1)}$. It also satisfies $\partial G/\partial t=\lambda(z-1)G$ with $G(z,0)=1$, combining the forward equations into a single differential equation. Differentiating in $z$ at one gives $E\{N(t)\}=\lambda t$ and $E\{N(t)(N(t)-1)\}=(\lambda t)^2$. Since $N^2=N(N-1)+N$, the variance is also $\lambda t$. These moments are consequences of the full distribution; equality of the mean and variance alone does not establish independent increments. The factorial-moment identities are useful diagnostics for the Poisson count law.{{cite:durrett2012_essentials}} (§2.2, thm. 2.3, p. 81)

## Connections — Counts and waiting times
The no-arrival probability $p_0(t)=e^{-\lambda t}$ is also the survival probability of the first waiting time. Independent exponential interarrival times reconstruct the Poisson count process. Their sums give the arrival epochs, so distributional statements about counts can be converted into statements about waiting times. The rate has units of events per time and $\lambda t$ is dimensionless.{{cite:durrett2012_essentials}} (§2.2, lem. 2.2, pp. 80–81)

## Assumptions and limits
A constant mean rate by itself does not establish a Poisson process. Bursty arrivals can violate the short-interval multiple-arrival condition or independent increments. A deterministic time-varying rate replaces $\lambda$ by $\lambda(t)$ in the forward equations and its cumulative integral in the Poisson mean; a rate depending on the current state describes a different birth process. The displayed system concerns the homogeneous unit-jump model.{{cite:durrett2012_essentials}} (§2.2, definition of the Poisson process)
