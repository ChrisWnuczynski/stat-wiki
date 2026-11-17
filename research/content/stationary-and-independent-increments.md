## Lead context
Stationary increments mean that a change over an interval depends on the interval's length and not on when it starts; independent increments mean that changes over intervals that do not overlap are independent.

## Motivating example
A Poisson process of rate 2 counts events per hour. The number of events in any half hour has mean $2\times1/2=1$, whether the half hour is the first half hour or the half hour starting at time 10. That is stationarity of increments. The counts in two half hours that do not overlap are independent, so the probability that both are empty is $e^{-1}\times e^{-1}=e^{-2}=0.1353$. A time-varying rate keeps the independence, if the rate is a fixed function of time, and loses the stationarity, because a busy half hour is not distributed as a quiet half hour of the same length.{{cite:durrett2019}} (pp. 353–354, increments whose law depends on length)

## Intuition
The level of the process at time $t$ can spread out as $t$ grows. Stationary increments do not say that $X_t$ has a distribution free of $t$. They say that the difference $X_{t+h}-X_t$ has a distribution free of $t$. A Poisson count has mean $\lambda t$, which grows, while an increment of length $h$ has mean $\lambda h$, which does not depend on where the window sits. Independent increments are a different sentence. They say that knowing the change on one window tells you nothing about the change on a window that does not touch it. A process can have either property without the other.

## Definition
The process has stationary increments when, for every $h>0$, the law of $X_{t+h}-X_t$ does not depend on $t$. It has independent increments when, for every $t_0<\cdots<t_n$, the differences $X_{t_1}-X_{t_0},\ldots,X_{t_n}-X_{t_{n-1}}$ are independent. Durrett's Brownian motion is defined by three properties, and the first two are exactly these: the increments over successive intervals are independent, and $B(s+t)-B(s)$ is normal with mean 0 and variance $t$, a law that depends on the length $t$ and not on the start $s$. Continuity of paths is the third property and is not an increment property.{{cite:durrett2019}} (pp. 353–354, independent increments and the $N(0,t)$ law of an increment of length $t$)

## Interpretation — Levels versus changes
Let $N(t)$ be a Poisson process of rate $\lambda$. Then $N(t+h)-N(t)$ is Poisson with mean $\lambda h$. The level $N(t)$ is Poisson with mean $\lambda t$. The level's law changes with $t$. The increment's law does not. For standard Brownian motion, $B(t)$ is normal with variance $t$, so the level spreads, and $B(t+h)-B(t)$ is normal with variance $h$, so the increment does not remember $t$. In both processes the two properties hold together. They come apart as soon as the rate, or the variance per unit time, is allowed to depend on the clock.

## Properties — A constant rate, and a rate that changes
For the rate-2 Poisson process, a window of length $1/2$ is Poisson with mean 1. Then $\Pr(N(t+1/2)-N(t)=0)=e^{-1}=0.3679$ for every $t$. For two disjoint windows the joint probability of two zeros is $e^{-2}=0.1353$, the product, because the increments are independent. For Brownian motion, $\Var(B(4)-B(3))=1$ and $\Var(B(1)-B(0))=1$. The covariance identity $\E B_s B_t=s\wedge t$ for $s<t$ is the same fact in another form: $\Var(B_t-B_s)=\E(B_t-B_s)^2=t-s$.

If the intensity is the deterministic function that equals 1 on $[0,1]$ and 4 on $(1,2]$, an increment construction that puts independent Poisson counts on those two intervals, with those means, has independent increments and does not have stationary increments. Both intervals have length 1. Their laws are Poisson(1) and Poisson(4).{{cite:durrett2019}} (pp. 353–354, the increment law depends on length alone)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For standard Brownian motion, property (b) in Durrett's definition says that $B(s+t)-B(s)$ has density $(2\pi t)^{-1/2}\exp(-x^2/(2t))$. The density depends on $t$ and not on $s$, which is stationary increments. Property (a) says that increments over successive intervals are independent. For $s<t$,
$$
\E B_s B_t=\E B_s\bigl(B_s+(B_t-B_s)\bigr)=\E B_s^2+\E B_s\,\E(B_t-B_s)=s,
$$
using independence of $B_s=B_s-B_0$ and $B_t-B_s$, and $\E(B_t-B_s)=0$. Thus $\E B_s B_t=\min(s,t)$.

For a homogeneous Poisson process the increment over an interval of length $h$ is Poisson($\lambda h$) by the stationary-increments assumption, and disjoint intervals are independent by the independent-increments assumption. The empty probability $e^{-\lambda h}$ follows from the Poisson(mean $\lambda h$) formula at 0. The product for two intervals is independence.{{cite:durrett2019}} (pp. 353–355, definition and the covariance $\E B_s B_t=\min(s,t)$)
:::
:::

## Statistical use — Which theorem the property unlocks
Name the state and the clock before using either property. A generation in a branching process is not a time increment of fixed length, and the next generation's law depends on how many individuals are alive, so the increments of $Z_n$ are neither stationary nor independent of the level. A Poisson process theorem that adds rates, or that conditions on the count and gets uniform event times, uses both properties. Dropping stationarity and keeping independence is the inhomogeneous Poisson process: disjoint windows are still independent, and the mean of a window is the integral of the intensity over that window rather than $\lambda$ times length.{{cite:durrett2019}} (pp. 353–354, length, not location, enters the increment law)

## Worked example
Rate $\lambda=2$. For a half hour, the mean increment is 1 and $\Pr(0)=e^{-1}=0.3679$. For the hour made of two specific disjoint half hours, independence gives $\Pr(\text{both empty})=0.1353$, and the hour itself is Poisson with mean 2, so $\Pr(N(t+1)-N(t)=0)=e^{-2}=0.1353$ as well. The two calculations agree. They agree because the sum of two independent Poisson(1) variables is Poisson(2).

For Brownian motion, $\Var(B(10)-B(9))=1$, the same as $\Var(B(1))$. The level $B(10)$ has variance 10. Stationary increments have not made the level stationary.

**Your turn.** An inhomogeneous Poisson process has intensity 1 on $[0,1]$ and intensity 4 on $(1,2]$, with independent increments. Find the mean and the variance of the increment on $[0,1]$, on $(1,2]$, and on $[0,2]$.

::: {.callout-tip collapse="true" title="Answer"}
The increment on $[0,1]$ is Poisson(1), mean 1 and variance 1. The increment on $(1,2]$ is Poisson(4), mean 4 and variance 4. Independence adds the means and the variances, so the increment on $[0,2]$ has mean 5 and variance 5. The two unit-length increments are not equally distributed, so the increments are not stationary.
:::

## Common misconceptions
Stationary increments do not mean a stationary process. Brownian motion and the Poisson process both fail to have a distribution for $X_t$ that is free of $t$. Independent increments do not mean independent levels. The levels overlap: $N(2)=N(1)+(N(2)-N(1))$, so the level at time 2 shares the first hour with the level at time 1. And a deterministic path $X(t)=3t$ has increments $X(t+h)-X(t)=3h$, which depend only on $h$. The increments are stationary. They are also degenerate random variables, hence independent. The interesting content of the two definitions starts when the increments are genuinely random.

## Assumptions and limits — Shared shocks and a random rate
If one shock creates several events at once, the counts in nearby windows share that shock and the independent-increments property fails. If the rate is itself random, as in a Poisson process with a random $\lambda$ drawn once and then held fixed, disjoint increments are independent given $\lambda$ and are dependent unconditionally: a busy first hour raises the posterior on $\lambda$ and raises the predictive mean of the next hour. The unconditional increments are stationary, because the random $\lambda$ does not prefer a clock time, and they are not independent. The two properties have come apart in the other direction from the inhomogeneous example.{{cite:durrett2019}} (pp. 353–354, the increment law is a property of the process, not of one path)

## Connections
Durrett's Brownian motion is the continuous process with both properties. A [Poisson process](homogeneous-poisson-process.qmd) is the counting process with both properties and unit jumps. A [Galton–Watson process](galton-watson-process.qmd) has neither: the next generation depends on the current population. [Independent random variables](independent-random-variables.qmd) are the increment statement when the windows are fixed and disjoint.{{cite:durrett2019}} (pp. 353–354, Brownian motion as the continuous example)

## Check yourself

### Increments and levels {#self-check-ex-sp-increments-and-levels}

For standard Brownian motion, what is $\Var(B(6)-B(4))$, and what is $\Var(B(6))$? Why are they different?

[Exercise](../questions/ex-sp-increments-and-levels.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The increment has length 2, so its variance is 2. The level $B(6)$ has variance 6. Stationary increments fix the variance of a change of a given length. They do not stop the level from accumulating variance as time passes.
:::

### A half-hour count {#self-check-ex-sp-poisson-half-hour}

A Poisson process has rate 3 per hour. What is the probability of no events in a 20-minute window, and does the answer depend on when the window starts?

[Exercise](../questions/ex-sp-poisson-half-hour.qmd)

::: {.callout-tip collapse="true" title="Answer"}
Twenty minutes is $1/3$ hour, so the mean count is $3\times1/3=1$. The probability of zero is $e^{-1}=0.3679$. Stationary increments make the answer the same for every window of that length.
:::

## History
Durrett defines one-dimensional Brownian motion by independent increments, by a normal increment whose variance equals the length of the interval, and by continuous paths. The first two of those are the independent-increments property and the stationary-increments property. He notes that the process arose as a model of Brown's 1828 observation of pollen and of Bachelier's 1900 model of the stock market. The Poisson calculation on this page is the counting-process version of the same two properties, with a Poisson increment in place of a normal one.{{cite:durrett2019}} (pp. 353–354, definition and the historical remark on Brown and Bachelier)
