## Motivating example
The US accidental-deaths series records monthly totals. Its annual seasonal pattern makes it useful for comparing seasonal forecasts with simpler benchmarks, while also illustrating the distinction between a time-series pattern and an explanation of that pattern. A change in a count can reflect exposure, population size, event frequency or recording, so the count series alone does not identify a mechanism. Seasonality and movement in level should first be described as properties of the observed series.{{cite:hyndman_athanasopoulos2021}} (§2.3, time-series patterns)

## Definition — Preserve the calendar index
The R dataset `USAccDeaths` contains 72 observations from January 1973 through December 1978, with time-series frequency 12. That frequency records twelve observations per year; it is part of the series metadata supplied to modelling functions. It is different from estimating an unknown seasonal period from an unindexed vector. The data values, start, end and frequency can be inspected directly with R's dataset and time-series operations.{{cite:r_usaccdeaths_ah}} (datasets, `USAccDeaths`, description and source data)

Time indexing is essential when comparing a forecast with a later observation. A one-step forecast after December refers to January, and a twelve-month forecast sum refers to the following calendar year only when no months have been dropped. Aggregating monthly means gives an annual forecast mean by linearity, but summing individual prediction-interval endpoints does not generally give a calibrated annual interval. Dependence among monthly forecast errors contributes to the uncertainty of the total.{{cite:hyndman_athanasopoulos2021}} (§§5.4–5.5, residual diagnostics and prediction intervals)

## Interpretation — Difference a seasonal pattern carefully
A seasonal difference is $W_t=Y_t-Y_{t-12}$. A further ordinary difference is
$$\Delta W_t=Y_t-Y_{t-1}-Y_{t-12}+Y_{t-13}.$$
A deterministic pattern repeating exactly each year cancels in the seasonal difference. A linear trend becomes a constant after a seasonal difference, and an additional ordinary difference removes that constant. A quadratic trend becomes a line after the seasonal difference and a constant after both differences. These are algebraic properties, rather than a proof that an observed dataset has a particular deterministic trend.{{cite:hyndman_athanasopoulos2021}} (§9.1, seasonal and second-order differencing)

The transformed series and its residual autocorrelations should guide model checking. Applying too many differences can introduce avoidable dependence. An MA coefficient describes how model innovations enter the observation equation; its sign by itself does not establish a behavioural response by people to earlier deaths. Forecast interpretation should distinguish the fitted stochastic structure from a causal account.{{cite:hyndman_athanasopoulos2021}} (§§9.1, 9.4, 9.7)

## Worked example — Recompute the first annual differences
The observed January values for 1973 and 1974 are $9007$ and $7750$, giving seasonal difference $-1257$. The February values are $8106$ and $6981$, giving seasonal difference $-1125$. Their ordinary difference is $132$, also obtained directly as $6981-7750-8106+9007$. The first twelve observations sum to $115821$. These calculations use the recorded integer counts and their calendar order, without fitting a forecast model.{{cite:r_usaccdeaths_ah}} (`USAccDeaths`, 1973–1974 source values)

**Your turn.** What is the ordinary February-minus-January change within 1973, and how does it differ from a seasonal difference?

::: {.callout-tip collapse="true" title="Answer"}
It is $8106-9007=-901$. It compares adjacent months, whereas a seasonal difference compares a month with the same month one year earlier.
:::

## Statistical use — Assess forecasts beyond the fitted sample
A seasonal naive forecast uses the most recent observed value from the same month, providing a useful benchmark. More elaborate seasonal ARIMA models should be compared with such benchmarks on a common forecast horizon and data window. Selection criteria and test-set comparisons address different questions. Residual diagnostics can reveal model inadequacy even when an automatic selection algorithm returns a fitted model successfully.{{cite:hyndman_athanasopoulos2021}} (§5.2, seasonal naive forecasts; §§9.7, 9.9)

## Assumptions and limits — Validation needs dated observations
The 72-month dataset ends in December 1978. Assessing later forecasts requires a separately verified continuation on the same count definition and calendar. A forecast interval describes uncertainty under the fitted model and its assumptions; it does not resolve changes in the event definition or exposure. Long-range extrapolation of an integrated model should be inspected in light of the trend implied by its differencing and constant terms.{{cite:hyndman_athanasopoulos2021}} (§§9.5, 9.8)


Forecast uncertainty has several components. Parameter estimates vary across samples, future observations fluctuate even when parameters are known, and the model itself can become unsuitable when the process changes. An interval that represents the first two components can therefore miss changes in exposure, recording or the trend. Comparing fits across observation windows helps reveal sensitivity to the chosen period; a narrow conditional interval alone does not establish stable long-range prediction.{{cite:downey2014_thinkstats2}} (Ch. 12, “Prediction”)
