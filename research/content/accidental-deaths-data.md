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

## Intuition
A monthly count series carries two clocks. One clock is the calendar month, which repeats every twelve observations. The other is the year-to-year level. A plot of the seventy-two USAccDeaths values shows both: winters differ from summers, and the level is not the same in 1973 as in 1978. Frequency $12$ in the time-series object is the statement that the seasonal clock has already been supplied. It is not a period estimated from an unordered list of seventy-two numbers. Dropping the index and sorting the counts would destroy both clocks.

Seasonal differencing subtracts each month from the same month a year later. The January 1974 value $7750$ minus the January 1973 value $9007$ is $-1257$. The February difference is $6981-8106=-1125$. The ordinary change from the January 1974 seasonal difference to the February 1974 seasonal difference is $-1125-(-1257)=132$. That second difference is what an additional first difference of the seasonally differenced series computes. The within-year change from January 1973 to February 1973 is $8106-9007=-901$, a comparison of adjacent months rather than of matched months.

## Properties — Polynomial trends after seasonal differencing
Let $Y_t=100+2t+t^2$, a deterministic quadratic, and let $W_t=Y_t-Y_{t-12}$. Expanding the square gives
$$t^2-(t-12)^2=24t-144,\qquad 2t-2(t-12)=24,$$
so $W_t=24t-120$. The seasonal difference of a quadratic is a straight line, not a constant. One further ordinary difference removes that line: $W_t-W_{t-1}=24$. A linear trend $a+bt$ becomes the constant $12b$ after a seasonal difference at lag $12$, and a further ordinary difference turns the constant into zero. These identities are algebra. They describe what the operators do to a polynomial. They do not say that the accidental-death counts were generated by a quadratic.

The first twelve observations sum to $115821$. Dividing by twelve gives the 1973 monthly mean $9651.75$. A later forecast of an annual total is a sum of monthly forecasts only when the months are the twelve months of that year and no observation has been dropped from the window. Adding the endpoints of twelve marginal prediction intervals does not produce an interval for the sum. The variance of a sum includes twelve variances and the covariances between every pair of monthly forecast errors. Those covariances are part of a joint forecast distribution. They are not visible in twelve separate bands.{{cite:hyndman_athanasopoulos2021}} (§§5.4–5.5, residual diagnostics and prediction intervals)

## Common misconceptions
A negative seasonal difference in January is a drop from the previous January. It is not, by itself, a statement that deaths became rarer per person, because the series records counts. Population, exposure, reporting rules, and the mix of causes can move a count while a rate moves differently. The time-series model describes the counts that were stored in `USAccDeaths`. A causal reading needs measurements the series does not contain.

Automatic order selection can return a seasonal ARIMA model whose residuals look respectable and whose point forecasts track the seasonal naive forecast closely. The seasonal naive forecast, which copies last year's same month, is the benchmark those more elaborate forecasts have to beat on a window that was not used to choose the orders. Fitting success on 1973–1978 does not answer how the same specification would have scored on a later decade. The published series stops in December 1978. Any later score needs a continuation with the same definition of a counted death.{{cite:hyndman_athanasopoulos2021}} (§5.2, seasonal naive forecasts; §§9.7, 9.9)

## Connections
The random-walk and unit-root calculations are the nonseasonal version of the differencing used here. A seasonal unit root is the statement that the seasonal difference, rather than only the first difference, is what renders the series stationary. The accidental-death series is a single realised path of seventy-two months. It can illustrate the operators, the role of frequency, and the difference between a count and a rate. It cannot illustrate the sampling distribution of a forecast error, because that distribution is a property of a model and of repeated paths. Residual checks on the one observed path remain useful as diagnostics of the fitted model. They are one path's residuals, not a Monte Carlo estimate of coverage.
