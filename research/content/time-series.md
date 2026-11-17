## Lead context
A time series keeps the order of the measurements, because a later value can still carry the shock that moved an earlier one.{{cite:hyndman_athanasopoulos2021}} (§2.1, index and observations)

## Motivating example
The numbers $123$, $39$, $78$, $52$ and $110$ can be stored as a list. Once they are tied to the years $2015$ through $2019$, in that order, they are a time series: each figure has a time, and the times have an order.{{cite:hyndman_athanasopoulos2021}} (§2.1, yearly index) The same five numbers sorted by size, $39$, $52$, $78$, $110$, $123$, are a different series. The average is $80.4$ either way. The lag-$1$ sample correlation is not. Order is part of the data, not a label added after the mean has been computed.{{cite:dodge2008}} (p. 536, sequence of observations)

## Intuition
Independent draws from one distribution can be shuffled without changing the joint law. A series usually cannot. Neighbouring times share a season, a slow level, or a shock that has not died out. The sample then contains one stretch of dependent values, and the usual $1/T$ formula for the variance of a mean counts those values as if the shared shocks were new information.{{cite:hyndman_athanasopoulos2021}} (§9.1, stationarity){{cite:dodge2008}} (p. 536, dependence through time)

Weak stationarity is the restriction that makes repetition available inside one stretch: a mean that does not depend on time, and a covariance that depends on two times only through the lag between them. A trend, or a seasonal pattern of fixed length, moves the mean with the calendar and fails that restriction. A white-noise series, whose values are uncorrelated with mean zero and one variance, passes it. A cycle whose length is not fixed in advance can also pass it, because the timing of the next peak is not a function of the date.{{cite:hyndman_athanasopoulos2021}} (§9.1, stationarity, white noise and cycles)

## Definition
A time series is a sequence of observations indexed by time. The index may be a year, a month, a day or an hour; what matters is that the order is part of the observation.{{cite:hyndman_athanasopoulos2021}} (§2.1, list of numbers and an index){{cite:dodge2008}} (p. 536, successive times)

Write the series as $X_1,\ldots,X_T$. An autoregression of order $1$ with no constant is $X_t=\phi X_{t-1}+\varepsilon_t$, where $\varepsilon_t$ is white noise. Hyndman and Athanasopoulos require $-1<\phi<1$ for that model to be used as a stationary series. At $\phi=0$ the series is the white noise itself. At $\phi=1$ it is a random walk, and the mean and variance then depend on time.{{cite:hyndman_athanasopoulos2021}} (§9.3, AR(1) and the boundary cases)

## Interpretation
A descriptive series is often split into a secular trend, a seasonal component, a cyclical component and an irregular component. Those names are a reading of a plot. They become a probability model only after the irregular piece is given a joint distribution and the other pieces are stated as functions of time or as further stochastic terms. A random walk has no fixed trend line: its level is the sum of every shock so far, and the forecast of every future value is the last observation.{{cite:dodge2008}} (p. 536, four components){{cite:hyndman_athanasopoulos2021}} (§9.1, random-walk forecast)

Differencing is the operation $X_t-X_{t-1}$. It removes a one-step change in level. A seasonal difference $X_t-X_{t-m}$ removes a change at lag $m$. Differencing a series that was already white noise manufactures a moving-average dependence that the shocks did not have. The smallest number of differences that produces a series without a wandering level is the one to keep.{{cite:hyndman_athanasopoulos2021}} (§9.1, differencing and extra differences)

## Properties
For a stationary AR(1) with white-noise variance $\sigma^2$ and $|\phi|<1$, the marginal variance is $\gamma_0=\sigma^2/(1-\phi^2)$, and the lag-$h$ covariance is $\gamma_h=\phi^{|h|}\gamma_0$. The variance of the sample mean of $T$ consecutive values is
\[
\operatorname{Var}(\bar X)=\frac1T\sum_{h=-(T-1)}^{T-1}\Bigl(1-\frac{|h|}{T}\Bigr)\gamma_h.
\]
Independent data with the same marginal variance would have given $\gamma_0/T$. Positive $\phi$ makes the mean less precise than that benchmark, because successive values repeat the same shock.{{cite:hyndman_athanasopoulos2021}} (§9.3, stationary AR(1))

At $\phi=1/2$ and $\sigma^2=1$, $\gamma_0=4/3$. The large-sample multiplier $(1+\phi)/(1-\phi)$ equals $3$. For $T=4$ the exact multiplier is $2.0625$, and $\operatorname{Var}(\bar X)=0.6875$, against the independent-data value $1/3\approx 0.3333$. The limit $3$ is the right long-series factor and the wrong factor for these four observations.{{cite:hyndman_athanasopoulos2021}} (§9.3, AR(1) stationarity condition)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $X_t=\phi X_{t-1}+\varepsilon_t$ with $|\phi|<1$, $\mathbb E(\varepsilon_t)=0$, $\operatorname{Var}(\varepsilon_t)=\sigma^2$, and $\varepsilon_t$ uncorrelated with $X_{t-1}$. Stationarity gives $\operatorname{Var}(X_t)=\operatorname{Var}(X_{t-1})$, so $\gamma_0=\phi^2\gamma_0+\sigma^2$ and $\gamma_0=\sigma^2/(1-\phi^2)$. The lag-$1$ covariance is $\mathbb E(X_t X_{t-1})=\phi\gamma_0$. The same step at lag $h$ gives $\gamma_h=\phi\gamma_{h-1}$, hence $\gamma_h=\phi^{|h|}\gamma_0$.{{cite:hyndman_athanasopoulos2021}} (§9.3, AR(1) equation)

For any weakly stationary series, expand $\operatorname{Var}(\sum_{t=1}^T X_t)=\sum_{t=1}^T\sum_{s=1}^T\gamma_{t-s}$. Each lag $h$ with $|h|<T$ occurs $T-|h|$ times. Dividing by $T^2$ produces the displayed formula for $\operatorname{Var}(\bar X)$. Insert $\gamma_h=\phi^{|h|}\gamma_0$. At $\phi=1/2$, $\sigma^2=1$ and $T=4$ the lags $1,2,3$ contribute
\[
\tfrac34\cdot\tfrac12+\tfrac12\cdot\tfrac14+\tfrac14\cdot\tfrac18=\tfrac{3}{8}+\tfrac18+\tfrac1{32}=\tfrac{17}{32}=0.53125.
\]
The two-sided sum is $1+2\times 0.53125=2.0625$. Then $\operatorname{Var}(\bar X)=(4/3)/4\times 2.0625=0.6875$.{{cite:hyndman_athanasopoulos2021}} (§9.1, covariance depending only on lag)
:::
:::

## Statistical use — One forecast, with a horizon
A point forecast is a single number for a stated horizon. For the random walk, that number is the last observation at every horizon, and the error variance grows like the horizon times $\sigma^2$. For a stationary autoregression the forecast is pulled toward the unconditional mean as the horizon grows, and the error variance rises toward $\gamma_0$ rather than without bound. Quoting one standard error for both series treats a wandering level as if it had a fixed mean.{{cite:hyndman_athanasopoulos2021}} (§9.1, random-walk forecast; §9.3, stationary AR)

## Worked example
Take the recorded order $123,39,78,52,110$. The mean is $(123+39+78+52+110)/5=402/5=80.4$. Centred at $80.4$, the lag-$1$ sum of products is $-2436.76$ and the sum of squares is $5217.2$, so the lag-$1$ correlation is $-2436.76/5217.2\approx -0.4671$. The same numbers in increasing order, $39,52,78,110,123$, have lag-$1$ correlation $2433.84/5217.2\approx 0.4665$. The mean did not change. The time order did, and the lag-$1$ correlation changed sign.{{cite:hyndman_athanasopoulos2021}} (§2.1, observations and their index)

Separately, let $\varepsilon_t$ be white noise of variance $1$ and set $X_t=X_{t-1}+\varepsilon_t$ with $X_0=0$ and innovations $1,-1,0,2$. The path is $1,0,0,2$. The forecast of $X_5$, and of every later value, is $2$, the last observation. The variance of the position at step $4$ is $4$, not $1$, because four uncorrelated innovations have been added. A stationary AR(1) with $\phi=1/2$ and the same innovation variance has marginal variance $4/3\approx 1.3333$, and the variance of a mean of four consecutive values is $0.6875$ rather than $4/3$ divided by $4$.{{cite:hyndman_athanasopoulos2021}} (§9.1, random walk; §9.3, AR(1))

**Your turn.** For the stationary AR(1) with $\phi=1/2$ and innovation variance $1$, find the marginal variance and the large-sample multiplier $(1+\phi)/(1-\phi)$ of the mean's variance relative to independent data.

::: {.callout-tip collapse="true" title="Answer"}
The marginal variance is $1/(1-(1/2)^2)=4/3\approx 1.3333$. The multiplier is $(1+1/2)/(1-1/2)=3$. A very long mean is three times as variable as the independent-data formula. The exact multiplier at $T=4$ is $2.0625$, which is smaller than this limit.)
:::

## Common misconceptions
A time plot that slopes is not evidence that the trend is a fixed function of time. A random walk produces long runs that look like trends, and its forecast stays at the last observation instead of extending a fitted line.{{cite:hyndman_athanasopoulos2021}} (§9.1, random-walk paths)

The sample size $T$ is not the number of independent pieces of information about the mean. At $\phi=1/2$ the variance of a four-term mean is $0.6875$, a bit more than twice the independent-data value $0.3333$. Using $\gamma_0/T$ reports a standard error that is too small.{{cite:hyndman_athanasopoulos2021}} (§9.3, positive autocorrelation)

Shuffling the series to "check the mean" keeps the mean and destroys the lags. The five yearly figures have mean $80.4$ in every order and lag-$1$ correlation $-0.4671$ in the recorded order, against $0.4665$ when sorted.{{cite:hyndman_athanasopoulos2021}} (§2.1, the index is part of the series)

## Assumptions and limits — When one stretch is not many draws
Stationarity was used to treat every lag as a repeat of the same covariance. A series with a trend, a fixed seasonal spike, or a variance that grows with time does not offer that repeat. Differencing can remove a unit root and can also invent autocorrelation. If $\varepsilon_t$ is white noise of variance $\sigma^2$, then $D_t=\varepsilon_t-\varepsilon_{t-1}$ has variance $2\sigma^2$ and lag-$1$ covariance $-\sigma^2$, so the lag-$1$ correlation is $-1/2$. The shocks were uncorrelated; the difference is not.{{cite:hyndman_athanasopoulos2021}} (§9.1, do not over-difference)

Forecasts that change the thing being forecast are a different failure. A widely believed forecast that an exchange rate will rise can move the rate at once, so the forecast is no longer a spectator. Hyndman and Athanasopoulos put day-ahead exchange rates in that class: with a liquid market, calling the direction is about as sharp as a coin toss. The arithmetic of a fitted autoregression does not repair that loop.{{cite:hyndman_athanasopoulos2021}} (§1.1, exchange rates and self-fulfilling forecasts)

## Connections
[White noise](white-noise.qmd) is the innovation sequence inside the autoregression, and the series itself when $\phi=0$. [Weak stationarity](weak-stationarity.qmd) is the moment restriction used for the covariance formula. A [simple linear regression](simple-linear-regression.qmd) of one series on time estimates a fixed line; it is the wrong mean for a random walk, whose level is not a function of the date.{{cite:hyndman_athanasopoulos2021}} (§9.1, random walk; §9.3, white-noise boundary)

## Check yourself

1. The path of a random walk is $1,0,0,2$. What is the point forecast of the next value?

::: {.callout-tip collapse="true" title="Answer"}
The forecast is $2$ at every horizon. Future increments have mean zero, so they do not move the point forecast off the last observation.
:::

2. For $\phi=1/2$ and $T=4$, is the variance of the sample mean equal to $(4/3)/4=1/3$?

::: {.callout-tip collapse="true" title="Answer"}
No. That is the variance for four uncorrelated draws with variance $4/3$. The exact autoregressive variance is $0.6875$, and $0.6875/(1/3)=2.0625$.)
:::

3. Does sorting $123,39,78,52,110$ into increasing order keep the lag-$1$ correlation?

::: {.callout-tip collapse="true" title="Answer"}
No. The recorded order has lag-$1$ correlation about $-0.4671$. The sorted order has about $0.4665$. The mean $80.4$ is the same.
:::

## History
A time series is a sequence of observations measured at successive times, from hourly traffic counts to annual records, and the analysis is a route to prediction. The movement splits into trend, seasonal variation, cyclical fluctuation and irregular variation. W. M. Persons proposed that four-part decomposition in 1919.{{cite:dodge2008}} (p. 536, definition, components and Persons)

Hyndman and Athanasopoulos separate that descriptive split from the autocorrelation models used for forecasting. A stationary series has statistical properties that do not depend on the time of observation. White noise is their basic stationary series. A random walk, written $X_t=X_{t-1}+\varepsilon_t$, is their basic non-stationary series, and its forecasts sit at the last observation.{{cite:hyndman_athanasopoulos2021}} (§9.1, stationarity and the random walk)
