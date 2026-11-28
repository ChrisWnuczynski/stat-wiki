## Motivating example
A detector counts arrivals over time. Rather than specifying only the total count in one fixed interval, a process model must explain how probabilities evolve when the observation window grows. The forward equations express incoming probability from count $n-1$ and outgoing probability from count $n$. A homogeneous Poisson process has a constant rate and independent increments.{{cite:durrett2012_essentials}} (§2.2, pp. 80–83)

## Properties — A complete short-interval argument
Put $\Delta_h=N(t+h)-N(t)$. Independence and stationarity of increments give
$$p_n(t+h)=\sum_{j=0}^np_{n-j}(t)\mathbb{P}(\Delta_h=j).$$
For fixed $n$, substitute $\mathbb{P}(\Delta_h=0)=1-\lambda h+o(h)$, $\mathbb{P}(\Delta_h=1)=\lambda h+o(h)$ and $\mathbb{P}(\Delta_h\ge2)=o(h)$. The sum has finitely many terms, so after subtracting $p_n(t)$, dividing by $h$ and taking the limit, only the terms for zero and one new arrivals survive. This yields $p_n'=\lambda p_{n-1}-\lambda p_n$, with $p_{-1}=0$. The construction is a pure-birth specialization of the Kolmogorov forward equation.{{cite:durrett2012_essentials}} (§4.2, eq. 4.9–4.11, pp. 124–125)

Multiplying by $e^{\lambda t}$ gives $(e^{\lambda t}p_n(t))'=\lambda e^{\lambda t}p_{n-1}(t)$. Starting with $p_0=e^{-\lambda t}$ and integrating inductively from zero gives
$$p_n(t)=e^{-\lambda t}\frac{(\lambda t)^n}{n!}.$$
These probabilities sum to one by the exponential series, so the solution loses no probability mass. The recursion uniquely determines each coordinate from the preceding one and its initial value. The count and interarrival descriptions are related by $\{N(t)\ge n\}=\{T_n\le t\}$.

## Worked example — Probability can be flowing out
At rate two arrivals per hour and time one hour, $(p_0,p_1,p_2)=(e^{-2},2e^{-2},2e^{-2})\approx(0.13534,0.27067,0.27067)$. Their instantaneous derivatives are $p_0'=-0.27067$, $p_1'=-0.27067$ and $p_2'=0$. The probability of exactly two arrivals is at its peak at this time: incoming and outgoing rates balance. This does not mean the count stops increasing; counts only jump upward while probability moves among count states.{{cite:durrett2012_essentials}} (§4.2, ex. 4.7, p. 125)

**Your turn.** For rate three per hour, find the probability of exactly one arrival by half an hour and its derivative with respect to time at that instant.

::: {.callout-tip collapse="true" title="Answer"}
Here $\lambda t=1.5$, so $p_1=1.5e^{-1.5}=0.33470$. Its derivative is $3(p_0-p_1)=-1.5e^{-1.5}=-0.33470$ per hour.
:::

### A generating function solves the entire system
For $0\le z\le1$, define $G(z,t)=\sum_{n\ge0}p_n(t)z^n$. Substituting the Poisson solution gives $G(z,t)=e^{\lambda t(z-1)}$. It also satisfies $\partial G/\partial t=\lambda(z-1)G$ with $G(z,0)=1$, combining the forward equations into a single differential equation. Differentiating in $z$ at one gives $\E\{N(t)\}=\lambda t$ and $\E\{N(t)(N(t)-1)\}=(\lambda t)^2$. Since $N^2=N(N-1)+N$, the variance is also $\lambda t$. These moments are consequences of the full distribution; equality of the mean and variance alone does not establish independent increments. The factorial-moment identities are useful diagnostics for the Poisson count law.{{cite:durrett2012_essentials}} (§2.2, thm. 2.3, p. 81)

## Connections — Counts and waiting times
The no-arrival probability $p_0(t)=e^{-\lambda t}$ is also the survival probability of the first waiting time. Independent exponential interarrival times reconstruct the Poisson count process. Their sums give the arrival epochs, so distributional statements about counts can be converted into statements about waiting times. The rate has units of events per time and $\lambda t$ is dimensionless.{{cite:durrett2012_essentials}} (§2.2, lem. 2.2, pp. 80–81)

## Assumptions and limits
A constant mean rate by itself does not establish a Poisson process. Bursty arrivals can violate the short-interval multiple-arrival condition or independent increments. A deterministic time-varying rate replaces $\lambda$ by $\lambda(t)$ in the forward equations and its cumulative integral in the Poisson mean; a rate depending on the current state describes a different birth process. The displayed system concerns the homogeneous unit-jump model.{{cite:durrett2012_essentials}} (§2.2, definition of the Poisson process)

## Lead context
A Poisson process is a counting model with a constant rate and independent increments. The forward equations describe how the probability of each count changes as the observation window grows.

Probability of count $n$ increases when an arrival occurs in count $n-1$, and it decreases when an arrival occurs in count $n$. Solving the system recovers the familiar Poisson probabilities, and those probabilities can be read either as statements about counts or as statements about waiting times.{{cite:durrett2012_essentials}} (§2.2, pp. 80–83)

## Intuition
Fix a short extra interval of length $h$. The chance of no arrival in that interval is about $1-\lambda h$, the chance of one arrival is about $\lambda h$, and the chance of two or more is much smaller than $h$. Count $n$ at the later time is therefore reached in two ordinary ways: the process was already at $n$ and nothing arrived, or it was at $n-1$ and one arrival occurred. Subtracting the probability at the earlier time, dividing by $h$, and letting $h$ shrink leaves the derivative $\lambda p_{n-1}-\lambda p_n$. The index $n-1$ appears because the process only jumps upward. A term in $p_{n+1}$ would describe a downward jump, which this model does not have.{{cite:durrett2012_essentials}} (§4.2, eq. 4.9–4.11, pp. 124–125)

## Definition
Let $p_n(t)=\mathbb{P}\{N(t)=n\}$ for $n=0,1,2,\ldots$, with $p_{-1}=0$. The homogeneous Poisson process of rate $\lambda>0$ satisfies
$$
p_0'(t)=-\lambda p_0(t),\qquad p_n'(t)=\lambda p_{n-1}(t)-\lambda p_n(t)\quad(n\ge 1),
$$
together with $p_0(0)=1$ and $p_n(0)=0$ for $n\ge 1$. The unique solution is $p_n(t)=e^{-\lambda t}(\lambda t)^n/n!$. At rate one and time one, $p_0=p_1=e^{-1}\approx 0.36788$. Their derivatives are $p_0'=-e^{-1}$ and $p_1'=0$. The probability of exactly one arrival is instantaneously flat, while the probability of zero arrivals is still falling. Flatness of one coordinate is a balance of flows, not a frozen sample path.{{cite:durrett2012_essentials}} (§2.2, thm. 2.3, p. 81)

## Interpretation
The equation $p_n'=\lambda(p_{n-1}-p_n)$ separates an inflow from the count below and an outflow to the count above. If $p_n$ is larger than $p_{n-1}$, the derivative is negative and probability is leaving $n$. If $p_n$ is smaller, probability is arriving. At rate two and time one, $p_2'=0$ because $p_1=p_2$, so the two flows match at that instant. Individual paths still jump from $2$ to $3$ at rate two; other paths jump from $1$ to $2$ at the same total rate of probability. The generating function $G(z,t)=e^{\lambda t(z-1)}$ packages every coordinate. Differentiating it at $z=1$ gives mean $\lambda t$ and second factorial moment $(\lambda t)^2$, hence variance $\lambda t$. Equal mean and variance are consequences of this solution. They do not, by themselves, prove independent increments.{{cite:durrett2012_essentials}} (§4.2, ex. 4.7, p. 125)

## Statistical use
The forward equations are a way to derive the sampling distribution used for a Poisson count. If a desk has rate four arrivals per hour, a fifteen-minute window has mean one, and the probability of an empty window is $e^{-1}$. That numerical probability is $p_0(1/4)$ for rate four, or equivalently $p_0(1)$ for rate one on a rescaled clock. The same solution converts a waiting-time question into a count question: the first arrival is later than $t$ exactly when $N(t)=0$, so its survival probability is $e^{-\lambda t}$. A rate estimated from several windows should be paired with the exposure that the equations use. Changing the window changes $\lambda t$ even when the underlying rate is constant.{{cite:durrett2012_essentials}} (§2.2, lem. 2.2, pp. 80–81)
