## Motivating example

Calls to a service centre become more frequent through the morning. A constant-rate arrival model assigns the same expected count to every interval of equal length, which misses that pattern. A deterministic time-varying rate changes the expected count without introducing dependence between counts in disjoint intervals.{{cite:pishro_nik2014}} (§11.1.4)

## Definition — Counts on the cumulative-intensity clock

For a nonnegative locally integrable function $\lambda$, define $\Lambda(t)=\int_0^t\lambda(u)\,du$. The counting process starts at zero, has independent increments, and satisfies
$$
P\{N(t)-N(s)=k\}=e^{-m}\frac{m^k}{k!},\qquad
m=\Lambda(t)-\Lambda(s),\quad 0\le s<t.
$$
In particular, the increment mean and variance both equal $m$. Equal calendar lengths can have different integrated intensities; equal integrated intensities have the same count law. Changes in $\lambda$ on sets of Lebesgue measure zero do not change this model.{{cite:siegrist_nhpp2022}} (§ “Definition and Basic Properties”){{cite:pishro_nik2014}} (§11.1.4)

## Properties — First waits and transformed arrivals

No arrival between $s$ and $s+w$ has probability $\exp[-\Lambda(s+w)+\Lambda(s)]$. Independence of future increments means the same expression describes the wait after a deterministic time $s$ given the history up to $s$. Calendar-time waits generally depend on the current time and are not identically distributed exponentials.{{cite:siegrist_nhpp2022}} (§ “Arrival Times and Time Change”)

If $\Lambda$ is continuous, strictly increasing and unbounded, a unit-rate Poisson process $M$ gives the construction $N(t)=M(\Lambda(t))$. Let $E_j$ be independent unit-rate exponentials and $S_k=\sum_{j=1}^kE_j$. The arrival times are $T_k=\Lambda^{-1}(S_k)$. The inverse requires care on flat intervals; the counting-process construction remains valid there. If $\Lambda(\infty)$ is finite, the total number of arrivals is finite almost surely, with a Poisson distribution of that finite mean.{{cite:siegrist_nhpp2022}} (§ “Arrival Times and Time Change”)

## Worked example

Take $\lambda(t)=2+t$ events per hour. Then $\Lambda(t)=2t+t^2/2$. The first hour has mean $2.5$ events and the second has mean $3.5$ events, even though both last one hour. The two-hour count is Poisson with mean six, and the probability of no events is $e^{-6}\approx0.002479$.

If the first exponential draw on the intensity clock is $E_1=1$, the first arrival is
$$
T_1=-2+\sqrt{4+2E_1}=\sqrt6-2\approx0.449490\text{ hours}.
$$
For successive draws $E_1=E_2=1$, the second arrival is $T_2=\sqrt8-2\approx0.828427$ hours. Its calendar gap from the first is about $0.378937$ hours, shorter than the first gap despite equal intensity-clock gaps. The growing rate explains the direction of that difference. The calculation uses the time-change construction.{{cite:siegrist_nhpp2022}} (§ “Arrival Times and Time Change”)

**Your turn.** Find the probability of no arrivals in the second hour alone.

::: {.callout-tip collapse="true" title="Answer"}
It is $e^{-3.5}\approx0.030197$. Using $e^{-2.5}$ would use the integrated intensity of the first hour.
:::

## Connections — Independent increments and changing rates

The rate here is deterministic. Independent increments do not require equal expected counts in equal-length intervals. Conversely, observing a varying expected count does not establish independent increments: that is a separate modelling assumption in the definition. Counts on overlapping intervals are dependent through their shared events even under the nonhomogeneous Poisson model.{{cite:pishro_nik2014}} (§11.1.4, definition)

## Check yourself

### [Counts and a first wait](../questions/ex-sp-poisson-half-hour.qmd) {#self-check-ex-sp-poisson-half-hour}

For a constant rate of three per hour, find two events in half an hour and no event in the first third of an hour.

::: {.callout-tip collapse="true" title="Answer"}
The count probability is $e^{-1.5}1.5^2/2\approx0.251021$. The first-wait survival probability is $e^{-1}\approx0.367879$.
:::

### [Three events in two hours](../questions/ex-sp-conditional-times.qmd) {#self-check-ex-sp-conditional-times}

Under a homogeneous process, conditional on three events in two hours, what is the probability all occurred in the first hour?

::: {.callout-tip collapse="true" title="Answer"}
The three unordered event locations are independent uniforms on the two-hour interval, so the probability is $(1/2)^3=1/8$. For a time-varying rate it becomes $[\Lambda(1)/\Lambda(2)]^3$.
:::
