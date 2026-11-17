

## Lead context
A percentage error can be computed inside the range of the observed predictor. Extrapolation is a different operation: it estimates a response outside that range. {{cite:dodge2008}} (p. 195)

A forecast error of 10 means something different for a series whose values are near 100 and for a series whose values are near 10,000. The mean absolute percentage error puts each error on the scale of the observation it misses, so two series in different units can be compared by one average.{{cite:hyndman_athanasopoulos2021}} (§5.8, “Percentage errors”)

## Motivating example

Four simple methods were scored on Australian quarterly beer production for 2008–2010, after fitting through 2007. The seasonal naïve method had a mean absolute percentage error of 3.17, the historical mean 8.28, the naïve method 14.18 and the drift method 14.58. On that series every one of those scores picked the same winner. The percentage scale is what made a megalitre error readable as a share of the beer production being forecast.{{cite:hyndman_athanasopoulos2021}} (§5.8, beer example and the accuracy table)

## Intuition

Divide the error by the observation and multiply by 100. An error of 10 on an observation of 100 is 10%, and an error of 10 on an observation of 50 is 20%. Averaging the absolute percentages keeps over-forecasts and under-forecasts from cancelling. The price of that cancellation is a heavier penalty when the forecast is below the observation than when it is the same distance above it, because the divisor is the observation rather than the forecast.{{cite:hyndman_athanasopoulos2021}} (§5.8, “Percentage errors”){{cite:hyndman_koehler2006}} (preprint PDF p. 8, §2.2)

## Definition

Write the forecast error as \(e_t=y_t-\hat y_t\). The percentage error is \(p_t=100\,e_t/y_t\), and
\[
\mathrm{MAPE}=\operatorname{mean}(|p_t|).
\]
The mean is taken over the period on which accuracy is being scored. Forecast errors in that period are computed from observations that were not used to form the forecasts. Residuals, by contrast, are one-step errors on the training data.{{cite:hyndman_athanasopoulos2021}} (§5.8, “Forecast errors” and “Percentage errors”) The same definition is the mean absolute percentage error used to compare methods across series: the mean of \(|p_t|\), with \(p_t=100e_t/Y_t\).{{cite:hyndman_koehler2006}} (preprint PDF p. 8, §2.2)

Use the MAPE when several positive series on different scales need a shared accuracy number, and the observations are comfortably away from zero. On one series, or on several series that share a unit, the mean absolute error and the root mean squared error stay on the scale of the data and are easier to explain. The mean absolute scaled error is the scale-free alternative when zeros, small values or an arbitrary origin make percentages the wrong language.{{cite:hyndman_athanasopoulos2021}} (§5.8, scale-dependent errors, percentage errors and scaled errors){{cite:hyndman_koehler2006}} (preprint PDF p. 8, §2.2)

On the Google closing prices for January 2016 the naïve method had MAPE 5.67, the drift method 6.99 and the historical mean 16.24. The same ordering appeared in the other accuracy columns of that table. The beer table happened to agree across columns as well. Agreement is a property of those two examples, not a theorem about the MAPE.{{cite:hyndman_athanasopoulos2021}} (§5.8, Google and beer tables)

A smaller MAPE is a comparison of absolute percentage errors on the observations that were scored. It is not a statement that the method minimises squared error, and it is not defined for a series that contains a zero. The symmetric MAPE is not a repair: it can be negative, and a pair of values near zero still makes the ratio unstable. Scoring the same one-step errors that were used to fit the model answers a different question from scoring a held-out period.{{cite:hyndman_athanasopoulos2021}} (§5.8, forecast errors and symmetric MAPE){{cite:hyndman_koehler2006}} (preprint PDF p. 8, §2.2)

Percentage errors were already the usual way to compare forecast methods across series in the M-competition and the M3-competition. The case against relying on them was set out by showing series for which the MAPE is infinite, including zeros and negative returns, and by proposing the mean absolute scaled error as the measure that remains defined in those cases. The symmetric MAPE used in the M3-competition is part of that record, together with the advice to stop using it.{{cite:hyndman_koehler2006}} (preprint PDF p. 3, §1; p. 8, §2.2){{cite:hyndman_athanasopoulos2021}} (§5.8, symmetric MAPE)

## Properties

The MAPE is undefined or infinite if any observation in the scoring period is zero, and it becomes extreme when an observation is close to zero. A percentage also requires a meaningful zero. Temperature in degrees Celsius or Fahrenheit has an arbitrary zero, so a percentage error in those units does not measure forecast accuracy.{{cite:hyndman_athanasopoulos2021}} (§5.8, “Percentage errors”) On series that do hit zero, the in-sample and out-of-sample MAPE can be infinite for every simple method under comparison, as happened for a lubricant series whose sales included zeros. A Disney monthly log-return series, which contains zeros and negative values, produced an infinite MAPE for the historical mean, the random walk, exponential smoothing and Holt’s method on the fitting period.{{cite:hyndman_koehler2006}} (preprint PDF p. 5, Tables 2 and 3; p. 8, §2.2)

A symmetric variant replaces the denominator \(y_t\) by \((y_t+\hat y_t)/2\),
\[
\mathrm{sMAPE}=\operatorname{mean}\left(\frac{200|y_t-\hat y_t|}{y_t+\hat y_t}\right).
\]
That form can be negative, and it is still unstable when both the observation and the forecast are near zero. It is recorded because competitions have used it, and the recommendation is to avoid it.{{cite:hyndman_athanasopoulos2021}} (§5.8, symmetric MAPE)

## Worked example

Suppose the observations are 100, 200 and 50 and the forecasts are 110, 160 and 80. The errors are \(-10\), \(40\) and \(-30\). The absolute percentage errors are
\[
100\cdot\frac{10}{100}=10,\qquad 100\cdot\frac{40}{200}=20,\qquad 100\cdot\frac{30}{50}=60.
\]
The MAPE is \((10+20+60)/3=30\). The mean absolute error on the original scale is \((10+40+30)/3=80/3\approx 26.667\), a different number because it is not a percentage. If the third observation had been 0, the third percentage error would have required division by zero and the MAPE would not have been a real number.{{cite:hyndman_athanasopoulos2021}} (§5.8, “Percentage errors”)

**Your turn.** Observations 80 and 120 are forecast as 100 and 90. Compute the two absolute percentage errors and their mean.

::: {.callout-tip collapse="true" title="Answer"}
The absolute percentage errors are \(100\cdot 20/80=25\) and \(100\cdot 30/120=25\). The MAPE is 25.
:::

## Assumptions and limits

Every observation in the average must be nonzero, and the zero of the measurement must be a real absence rather than an arbitrary origin. Values close to zero dominate the average even when they are genuine. Negative observations make a percentage hard to read as an absolute share of a level. Across series with very different scales, including zeros and negatives, a scaled error is the measure that stays finite whenever the historical series is not constant.{{cite:hyndman_koehler2006}} (preprint PDF p. 8, §2.2){{cite:hyndman_athanasopoulos2021}} (§5.8, “Percentage errors” and “Scaled errors”)

## Connections

The [mean squared error](mean-squared-error.qmd) averages squared discrepancies and stays in the squared units of the series. A [time series](time-series.qmd) is the ordered sample on which a forecast error is defined. Percentage errors are one summary of those errors. The mean absolute scaled error compares them with the average size of a naïve change on the training data.{{cite:hyndman_athanasopoulos2021}} (§5.8, scaled errors)
