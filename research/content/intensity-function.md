## Motivating example
A service desk may receive more requests near closing time than when it opens. Assigning one constant arrival rate to the whole day can hide that pattern. A deterministic intensity specifies how expected counts accumulate over time while retaining independence of counts on disjoint intervals.{{cite:durrett2019}} (§3.7.2, Thm. 3.7.5, p. 179)

## Definition — Rates integrate to expected counts
Let $\lambda(t)\ge0$ be locally integrable and define $\Lambda(t)=\int_0^t\lambda(u)\,du$. A nonhomogeneous Poisson process has independent increments with
$$N(t)-N(s)\sim\operatorname{Poisson}(\Lambda(t)-\Lambda(s)).$$
The integral is dimensionless when the intensity is events per unit time and integration uses that time unit. The Poisson parameter describes the expected count over the interval.{{cite:dodge2008}} (pp. 425–426, Poisson Distribution)

## Interpretation — A deterministic change of clock
Let $\widetilde N$ be a rate-one homogeneous Poisson process and put $N(t)=\widetilde N(\Lambda(t))$. Disjoint time intervals are mapped to disjoint intervals on the cumulative-intensity scale. Their increments remain independent and have means equal to their transformed lengths. This construction explains why the area under the rate, rather than its endpoint value, controls a count.{{cite:durrett2019}} (§3.7, Thm. 3.7.2, pp. 174–175)

An intensity can be zero on an interval, in which case the count is constant there almost surely. Altering the intensity on a set of time points with zero length changes none of its integrals and none of the process's finite count laws. A homogeneous rate is recovered when the cumulative intensity is linear.{{cite:durrett2019}} (§3.7.2, nonhomogeneous thinning, p. 179)

## Properties — First-event and conditional waiting probabilities
No event by time $t$ means a Poisson count of zero, so $\Pr(T_1>t)=e^{-\Lambda(t)}$. More generally, the probability of no event during $(s,s+w]$ is $e^{-[\Lambda(s+w)-\Lambda(s)]}$. This depends on the starting time unless the rate is constant. These are probabilities of zero counts; they do not replace the count mean by the instantaneous rate.{{cite:dodge2008}} (p. 425, Poisson Distribution)

## Worked example — A linearly increasing rate
Take $\lambda(t)=2t$ for $t\ge0$, so $\Lambda(t)=t^2$. The first two hours have expected count four; the following hour, from two to three, has expected count five. These counts are independent. The probability of no event in the first two hours is $e^{-4}=0.0183156$; the probability of exactly one is $4e^{-4}=0.0732626$. A one-hour interval starting at two has no event with probability $e^{-5}=0.00673795$. The equal lengths of different intervals do not force equal expected counts.

**Your turn.** From clock time two, how long must an interval be to have probability one half of containing no event?

::: {.callout-tip collapse="true" title="Answer"}
Solve $e^{-[(2+w)^2-4]}=1/2$. The nonnegative solution is $w=\sqrt{4+\log2}-2=0.166367$.
:::
