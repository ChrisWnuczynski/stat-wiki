## Motivating example
A temporary disturbance to a stationary autoregression has an effect that decays over time. In a random walk, that disturbance becomes part of every later level. This persistence changes both long-run variation and forecasting uncertainty. Differencing a random walk isolates its increments, which can be stationary even though the level is not.{{cite:hyndman_athanasopoulos2021}} (§9.1, “Stationarity and differencing”, random walk model)

## Definition — The ordinary root at one
For an autoregression written $\phi(B)X_t=\varepsilon_t$, a root of $\phi(z)$ on the unit circle is a unit root. The common nonseasonal case is a root at $z=1$, so $\phi(B)$ contains a factor $(1-B)$. If that factor occurs once and the remaining factors describe a stable stationary process, one ordinary difference removes that root. Seasonal or repeated unit roots require the corresponding factors to be addressed as well. For the AR(1) polynomial $1-\varphi z$, a root at one means $\varphi=1$.{{cite:hyndman_athanasopoulos2021}} (§§9.1–9.3, differencing, backshift notation and autoregressive models)

Autocorrelation compares values of a time series separated by a lag. It therefore summarises a different object from the level variance at a particular time. The covariance calculations below show explicitly why a random-walk level cannot be summarised by a stationary lag-only covariance.{{cite:dodge2008}} (p. 24, Autocorrelation)

## Properties — Accumulated innovations determine variance
Let $X_t=X_{t-1}+\varepsilon_t$, with fixed $X_0$, zero-mean uncorrelated innovations and positive common innovation variance $\sigma^2$. Iteration gives $X_t=X_0+\sum_{j=1}^t\varepsilon_j$. Variances therefore add to $t\sigma^2$. For $s\le t$, the covariance is $s\sigma^2$, which depends on both times rather than just their lag. This directly rules out weak stationarity of the levels. The first difference equals $\varepsilon_t$, so it has the stable innovation variance. The random-walk representation makes the distinction between levels and changes explicit.{{cite:hyndman_athanasopoulos2021}} (§9.1, random walk model)

For the linear $h$-step forecast using the most recent observation, the error is a sum of $h$ future innovations, with unconditional variance $h\sigma^2$ under the stated assumptions. If innovations are independent of the observed past, the same expression is the conditional forecast-error variance. A drift term adds $h$ times the drift to the point forecast but does not remove the accumulation of innovation variance. Forecast uncertainty widens with horizon even when the increment model is simple.{{cite:hyndman_athanasopoulos2021}} (§9.8, “Forecasting”)

## Worked example — A series with stable changes and unstable levels
Take innovation variance four and $X_0=0$. The level variances at times one, five and twenty are $4,20,80$. The variance of each one-step increment is four. A five-step forecast error has standard deviation $\sqrt{20}\approx4.472136$, while a twenty-step error has standard deviation $\sqrt{80}\approx8.944272$. Four times the forecast horizon doubles the standard deviation.

A stationary AR(1) with coefficient $0.8$ and the same innovation variance has stationary variance $4/(1-0.8^2)=100/9\approx11.111111$. Its finite variance illustrates the discontinuity at coefficient one: substituting one into that stationary formula does not yield a finite stationary variance.

**Your turn.** If the random walk has drift $0.5$ and its latest value is ten, what is the three-step point forecast and forecast-error variance?

::: {.callout-tip collapse="true" title="Answer"}
The forecast is $10+3(0.5)=11.5$. With innovation variance four, the forecast-error variance is twelve.
:::

## Statistical use — Test the assumption that matters
A slow-decaying sample autocorrelation can motivate a stationarity investigation, but it is not a proof of a unit root. Unit-root and stationarity tests have different null hypotheses and nonstandard or model-specific calibrations. For example, the KPSS test uses stationarity as its null. Always state the deterministic terms, differencing convention and null being tested before interpreting its p-value.{{cite:hyndman_athanasopoulos2021}} (§9.1, “Unit root tests”)

## Assumptions and limits — Level regressions can be misleading
Independent persistent series can yield apparently strong fitted relationships and ordinary t statistics whose usual stationary regression interpretation is invalid. A fitted line through their levels does not establish a shared generating mechanism. Inspecting residual dependence and considering a suitable model for differences are part of the analysis; genuine long-run relations require their own conditions. The spurious-regression issue is documented in the econometric literature.{{cite:hyndman_athanasopoulos2021}} (§10.1, “Estimation”, spurious regression)
