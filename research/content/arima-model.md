## Lead context
An ARIMA model differences a wandering series until the changes look stationary, then fits a short autoregression and moving average to those changes.

## Motivating example
A random walk observed at $12$ has point forecasts equal to $12$ at every horizon when there is no drift. Differencing white noise of variance $4$ produces a series of variance $8$ and lag-$1$ autocorrelation $-1/2$.

## Intuition — Integration is the undo button for differencing
A series with a trend or a changing level does not have one fixed mean, so a stationary autoregression is the wrong model for the levels. First differencing, $y'_t=y_t-y_{t-1}$, passes from levels to consecutive changes to help stabilise the mean, though it turns a permanent step shift in level into a one-time pulse rather than removing it. An ARIMA model then puts an autoregressive moving-average structure on the differenced series. The word integrated means that the forecast of the differences is added back up to a forecast of the level.{{cite:hyndman_athanasopoulos2021}} (§9.1, differencing; §9.5, the meaning of integrated)

## Definition — Orders for autoregression, differences and moving average
An ARIMA$(p,d,q)$ model differences the series $d$ times and then uses $p$ autoregressive terms and $q$ moving-average terms. With $y'_t$ the differenced series,
$$
y'_t=c+\phi_1 y'_{t-1}+\cdots+\phi_p y'_{t-p}+\varepsilon_t+\theta_1\varepsilon_{t-1}+\cdots+\theta_q\varepsilon_{t-q}.
$$
White noise is ARIMA$(0,0,0)$ with no constant. A random walk $y_t=y_{t-1}+\varepsilon_t$ is ARIMA$(0,1,0)$ with no constant. A random walk with drift is the same orders with a constant. An ordinary autoregression is ARIMA$(p,0,0)$.{{cite:hyndman_athanasopoulos2021}} (§9.5, equation (9.1) and the table of special cases){{cite:dodge2008}} (p. 20, the ARMA combination)

## Properties — One difference too many plants a negative spike
If $y_t$ is already white noise with variance $\sigma^2$, the first difference $\varepsilon_t-\varepsilon_{t-1}$ has variance $2\sigma^2$ and lag-$1$ autocorrelation $-1/2$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let the innovations be uncorrelated with mean $0$ and variance $\sigma^2$. Then $\operatorname{Var}(\varepsilon_t-\varepsilon_{t-1})=2\sigma^2$. The lag-$1$ covariance is
$$
\operatorname{Cov}(\varepsilon_t-\varepsilon_{t-1},\varepsilon_{t-1}-\varepsilon_{t-2})=-\operatorname{Var}(\varepsilon_{t-1})=-\sigma^2,
$$
because every other product has mean zero. The autocorrelation is $-\sigma^2/(2\sigma^2)=-1/2$. Differencing a series that is already a change is what plants this spike.{{cite:hyndman_athanasopoulos2021}} (§9.1, differencing)
:::
:::

## Worked example
A random walk observed at $12$ has point forecasts equal to $12$ at every horizon, because each future change has mean zero when there is no drift. If instead the levels are white noise with variance $4$, one unnecessary difference has variance $8$ and lag-$1$ autocorrelation $-1/2$. That spike is produced by the differencing, not by a moving-average term that was in the levels.{{cite:hyndman_athanasopoulos2021}} (§9.1, random-walk forecasts){{cite:dodge2008}} (p. 20, white-noise errors)

**Your turn.** An ARIMA$(1,0,0)$ model with no extra constant is $y_t=0.5 y_{t-1}+\varepsilon_t$. The last observation is $4$. Find the one-step and two-step point forecasts.

::: {.callout-tip collapse="true" title="Answer"}
The one-step forecast is $0.5\times 4=2$. The two-step forecast replaces the unknown next level by that forecast, giving $0.5\times 2=1$.
:::

## Connections
The autoregressive and moving-average pieces are the stationary ARMA model; the extra order $d$ is what ARIMA adds when the levels wander. A seasonal difference $y_t-y_{t-m}$ is the same idea at lag $m$. Forecasting then rebuilds the level from the differenced forecast, and the prediction variance grows with the horizon because each new step adds innovation variance.{{cite:hyndman_athanasopoulos2021}} (§9.1, seasonal differencing; §9.5){{cite:dodge2008}} (p. 20, AR and MA)
