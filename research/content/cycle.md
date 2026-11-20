## Motivating example
A business activity index may rise, fall and rise again without its peaks arriving in the same month or even after the same number of years. Forecasting that movement by copying last year's calendar can put the next peak at the wrong time. A cycle describes a recurring swing; seasonality adds a fixed calendar rhythm.{{cite:hyndman_athanasopoulos2021}} (§2.3, Time series patterns)

## Definition — Repetition and the calendar
Trend, seasonal variation, cyclical movement and irregular variation are distinct ways to describe a time series. A decomposition is a model of those movements, and the components depend on its assumptions.{{cite:dodge2008}} (p. 536, Time Series) In many forecasting decompositions, trend and cycle are combined into one trend-cycle component instead of being estimated separately.{{cite:hyndman_athanasopoulos2021}} (§3.2, Time series components)

A calendar period is known before observing the next data value. An irregular cycle has no such fixed return date. Finding several alternating peaks does not establish a stable oscillation: random disturbances and slowly changing levels can produce similar plots over a short record. Describing the movement and forecasting its timing are separate tasks.{{cite:hyndman_athanasopoulos2021}} (§2.3, Time series patterns)

## Interpretation — What seasonal differencing removes
A seasonal difference $(1-B^s)X_t=X_t-X_{t-s}$ subtracts the value one seasonal period earlier. A component that repeats exactly after $s$ observations cancels. Other frequencies need not shrink. For a complex sinusoid $e^{i\omega t}$, differencing multiplies it by $1-e^{-i\omega s}$, whose magnitude can range from zero to two. This calculation explains why differencing chosen for one calendar pattern can amplify another oscillation. The algebra assumes a fixed deterministic sinusoid; an irregular business cycle need not obey that model.{{cite:hyndman_athanasopoulos2021}} (§9.1, Stationarity and differencing)

## Worked example — Two frequencies under a yearly difference
For a monthly index let $X_t=\cos(2\pi t/12)+\cos(2\pi t/8)$. Subtract $X_{t-12}$. The first term cancels. The second shifts by $3\pi$, changing its sign, so
$$
X_t-X_{t-12}=2\cos(2\pi t/8).
$$
The eight-month oscillation doubles in amplitude. Both components in this example have fixed mathematical periods; the example isolates what a filter does and does not model irregular cycle lengths. The joint deterministic series repeats after $24$ months, the least common multiple of its component periods.

**Your turn.** What would differencing the same series at lag $24$ do?

::: {.callout-tip collapse="true" title="Answer"}
Both components cancel, since $24/12=2$ and $24/8=3$ are integers.
:::

## Connections — A component need not be an explanation
A trend-cycle estimate smooths short-scale variation. Choosing the smoothing span changes which swings appear in it. A seasonal adjustment removes an estimated calendar component, while its remainder can still contain irregular changes and measurement noise. Neither operation by itself identifies the scientific cause of a turning point.{{cite:hyndman_athanasopoulos2021}} (§3.2, Seasonally adjusted data)

## Check yourself

Use the definitions and calculations above to work through these questions.

### A stable dependence pattern {#self-check-depth-weak-stationarity-ar}

[A stable dependence pattern](../questions/depth-weak-stationarity-ar.qmd). Calculate the three requested AR(1) summaries.

::: {.callout-tip collapse="true" title="Answer"}
$\gamma(0)=9/(1-0.4^2)=75/7$, $\gamma(1)=30/7$, and $\rho(2)=0.16$. Stable covariances alone do not supply a calendar season.
:::

### A forecast depends on its target {#self-check-depth-point-forecast-loss}

[A forecast depends on its target](../questions/depth-point-forecast-loss.qmd). Choose the squared-error and absolute-error forecasts.

::: {.callout-tip collapse="true" title="Answer"}
The conditional mean is $0.8(10)+0.2(30)=14$, which minimises squared error. The conditional median is $10$, which minimises absolute error.
:::
