## Motivating example
A monitoring system can record event counts in fixed windows or the exact gaps between events. Under a homogeneous Poisson model, the two descriptions contain compatible probability calculations: an event threshold for the count corresponds to an arrival-time threshold for a sum of waiting times.{{cite:durrett2019}} (§3.7, pp. 174–176)

## Definition — Gaps, arrival epochs and the counting path
Set $T_0=0$, let $T_n$ be the time of the $n$th event, and define $W_n=T_n-T_{n-1}$. In a homogeneous Poisson process of rate $\lambda>0$, the gaps are independent exponentials with survival $e^{-\lambda w}$ for $w\ge0$. The first gap follows from $\{W_1>w\}=\{N(w)=0\}$; successive gaps have the same law by the Poisson construction.{{cite:durrett2019}} (§3.7, pp. 175–176) Their mean is $1/\lambda$ and variance is $1/\lambda^2$.{{cite:dodge2008}} (p. 194, Exponential Distribution)

## Properties — Summing gaps and counting arrivals
The $n$th arrival time is $T_n=\sum_{j=1}^nW_j$. Its mean is $n/\lambda$. The identity $\{T_n>t\}=\{N(t)\le n-1\}$ gives
$$\Pr(T_n>t)=e^{-\lambda t}\sum_{k=0}^{n-1}\frac{(\lambda t)^k}{k!}.$$
Differentiating the complement yields the gamma density $\lambda^nt^{n-1}e^{-\lambda t}/(n-1)!$. Integer shape is often called an Erlang law.{{cite:durrett2019}} (§3.7, arrival-time construction, pp. 175–176) This agrees with the exponential distribution as the shape-one case of the Gamma family.{{cite:dodge2008}} (pp. 194, 216)

The exponential survival also gives $\Pr(W>s+t\mid W>s)=e^{-\lambda t}$. This memoryless law concerns remaining wait from a deterministic elapsed time under the homogeneous model. It does not say that a general waiting-time distribution has a constant hazard.{{cite:dodge2008}} (p. 194, Exponential Distribution)

## Worked example — Waiting for a third event
For rate four per hour, the mean gap is fifteen minutes. The probability a gap exceeds half an hour is $e^{-2}=0.135335$. The third arrival has mean $3/4$ of an hour. The probability that it occurs after one hour is the probability of at most two events by then:
$$\Pr(T_3>1)=e^{-4}(1+4+8)=0.238103.$$
The mean first wait and the mean third arrival answer different scheduling questions.

**Your turn.** What is the median first wait at this rate?

::: {.callout-tip collapse="true" title="Answer"}
Solve $e^{-4w}=1/2$, giving $w=(\log2)/4=0.173287$ hours. It is shorter than the mean first wait of one quarter of an hour.
:::

## Assumptions and limits — The clock matters when the rate changes
For a deterministic nonconstant intensity, waiting from clock time $s$ has survival $\exp\{-\int_s^{s+w}\lambda(u)\,du\}$. After an arrival, the next waiting law depends on that random arrival time; the successive gaps generally are not independent identically distributed exponentials. On the cumulative-intensity clock a Poisson construction again has unit-rate exponential spacings.{{cite:durrett2019}} (§3.7.2, nonhomogeneous Poisson processes, p. 179)

## Check yourself

Use the definitions and calculations above to work through these questions.

### A first wait and a window count {#self-check-ex-sp-poisson-half-hour}

[A first wait and a window count](../questions/ex-sp-poisson-half-hour.qmd). Work both requested probabilities.

::: {.callout-tip collapse="true" title="Answer"}
The half-hour count has mean $1.5$, giving probability $e^{-1.5}1.5^2/2$ for exactly two events. Twenty minutes is one third of an hour, so the first-wait survival is $e^{-1}$.
:::

### Conditioning changes the experiment {#self-check-ex-sp-conditional-times}

[Conditioning changes the experiment](../questions/ex-sp-conditional-times.qmd). Explain why the given count matters.

::: {.callout-tip collapse="true" title="Answer"}
Given $N(2)=3$ in a homogeneous process, the unordered arrival locations are independent uniforms over two hours. All three fall in the first hour with probability $(1/2)^3=1/8$.
:::
