## Motivating example
A help desk receives calls throughout the day and needs a model for both the count in the next hour and the wait until the next call. If arrivals occur at a steady rate and disjoint intervals behave independently, one Poisson process supplies both answers. The model concerns the entire sequence of arrival times, not just one Poisson-distributed count.{{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2, summary pp. 47–48)

## Intuition
The rate $\lambda$ is an expected number of arrivals per unit time. A window of length $h$ has expected count $\lambda h$, whatever its starting time. Counts in nonoverlapping windows are independent, so observing several calls just now does not itself change the future count law. Equivalently, successive waits are independent exponential random variables with mean $1/\lambda$. These are strong modelling claims, not consequences of having a Poisson histogram for one chosen window size.{{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2, summary pp. 47–48)

## Definition
Let $N(t)$ count arrivals in $(0,t]$, with $N(0)=0$. A homogeneous Poisson process of rate $\lambda>0$ has independent increments and $N(t+h)-N(t)\sim\operatorname{Poisson}(\lambda h)$ for every $t,h\geq0$. The increment law depends on interval length, not its location; this is *stationary increments*. It does not mean that the level $N(t)$ is stationary: its mean rises as $\lambda t$. The equivalent small-interval description has one arrival with probability $\lambda h+o(h)$ and two or more with probability $o(h)$.{{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2, summary p. 47)

## Interpretation
For any fixed $t$, $N(t)$ is Poisson with mean and variance $\lambda t$, while the first wait $T_1$ has survival probability $\Pr(T_1>t)=e^{-\lambda t}$. Counts and waits answer different questions about the same process. The $k$th arrival time is the sum of $k$ independent exponential waits, with mean $k/\lambda$ and variance $k/\lambda^2$. Because those waits are almost surely positive and their sum diverges, a finite time contains only finitely many arrivals.{{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2, summary pp. 47–48)

## Properties
The probability of no arrivals in $(s,s+h]$ is $e^{-\lambda h}$. Counts over adjacent disjoint intervals add, so their Poisson means add; a pair of independent processes with rates $\lambda_1$ and $\lambda_2$ can be superposed to obtain rate $\lambda_1+\lambda_2$. Independent thinning, retaining each event with probability $r$, produces rate $r\lambda$. Those closure rules require independence of the processes or marks. An event that produces a simultaneous cluster is not one ordinary Poisson arrival.{{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2 and §6.3, summary pp. 47–49)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The increment law gives $\Pr\{N(t+h)-N(t)=0\}=e^{-\lambda h}$ and $E\{N(t+h)-N(t)\}=\operatorname{Var}\{N(t+h)-N(t)\}=\lambda h$. Since $T_1>t$ exactly when $N(t)=0$, $\Pr(T_1>t)=e^{-\lambda t}$; differentiating its complement gives exponential density $\lambda e^{-\lambda t}$. Independent increments restart the same waiting calculation after each arrival, giving independent exponential gaps. For independent counts $A\sim\operatorname{Poisson}(\lambda_1h)$ and $B\sim\operatorname{Poisson}(\lambda_2h)$, multiply their probability-generating functions $e^{\lambda_1h(z-1)}$ and $e^{\lambda_2h(z-1)}$ to obtain the Poisson law of $A+B$ with mean $(\lambda_1+\lambda_2)h$.{{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2–6.3, summary pp. 47–49)
:::
:::

## Statistical use
Estimate a constant rate by total observed events divided by total exposure time, provided the observation intervals and missing periods are recorded. Compare counts in disjoint windows and examine interarrival times: a changing rate, excess clusters or serial dependence contradict the simple model. An apparent quiet period after a burst may indicate a system with recovery time, while daily cycles call for a time-varying intensity. The process is a starting model whose independent-increment assumption should be checked against the event mechanism.{{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2, summary pp. 47–48)

## Worked example
Suppose calls arrive at rate $3$ per hour. In a $40$-minute window, $h=2/3$ hour and $\lambda h=2$, so the probability of exactly two calls is $e^{-2}2^2/2!=2e^{-2}\approx0.27067$. The expected count and its variance are both $2$. If the count for that window has just been observed, the next disjoint $40$-minute count still has the same distribution under the model. This last statement uses independence, not merely the Poisson formula.{{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2, summary p. 47)

**Your turn.** At the same rate, what is the probability of waiting more than ten minutes for the next call?

::: {.callout-tip collapse="true" title="Answer"}
Ten minutes is $1/6$ hour. The chance of zero calls in that time, and hence of a wait exceeding it, is $e^{-3(1/6)}=e^{-1/2}\approx0.60653$. This uses the waiting-time version of the same process, not a new rate.{{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2, summary pp. 47–48)
:::

## Common misconceptions
Stationary *increments* do not make $N(t)$ a stationary random level: $\operatorname{Poisson}(\lambda t)$ changes with $t$. A Poisson distribution for total daily counts alone does not establish independent hourly increments. The mean wait is $1/\lambda$, not $\lambda$, and a count of $\lambda h$ is an expectation, not a fixed number of events. A rate of three per hour also does not imply exactly one arrival every twenty minutes; exponential gaps vary.{{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2, summary pp. 47–48)

## Assumptions and limits — When the process fails
If a call centre has a lunch rush, equal-length windows at noon and midnight do not have the same count law, so a homogeneous rate fails. If a machine breakdown generates several alarms at once, short intervals can contain clusters with probability of first order in their length, contradicting the small-interval condition. If arrivals trigger a refractory period, nearby counts are dependent. In each case one may need a varying-rate, clustered or self-regulating point-process model instead of forcing one constant $\lambda$.{{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2, definition p. 47)

## Connections
The [Poisson distribution](poisson-distribution.qmd) describes each count, while the [exponential distribution](exponential-distribution.qmd) describes each wait. The answered [half-hour question](../questions/ex-sp-poisson-half-hour.qmd) combines a count and first wait; the [stationary-increment question](../questions/ex-sp-increments-and-levels.qmd) tests why the count level itself changes over time.{{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2, summary pp. 47–48)

## History
Poisson's 1837 work introduced the count distribution through a limiting binomial argument, as Dodge records. That historical count law is one component of the later continuous-time process model: specifying its joint independent increments and exponential waits adds information that a single count distribution cannot supply.{{cite:dodge2008}} (p. 425, “Poisson Distribution”, history){{cite:bertsekas_tsitsiklis2008_summary}} (Ch. 6, §6.2, summary pp. 47–48)
