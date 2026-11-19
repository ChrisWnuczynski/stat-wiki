## Lead context

A forecast error of 10 means something different for a series whose values are near 100 and for a series whose values are near 10,000. The mean absolute percentage error puts each error on the scale of the observation it misses, so two series in different units can be compared by one average. The price of that comparison is a list of conditions: the observations must be nonzero, the zero of the measurement must be a real absence, and a symmetric-looking variant is not a repair.{{cite:hyndman_athanasopoulos2021}} (§5.8, Percentage errors){{cite:hyndman_koehler2006}} (p. 8, §2.2)

## Motivating example

Four simple methods were scored on Australian quarterly beer production for 2008–2010, after fitting through 2007. The seasonal naïve method had a mean absolute percentage error of 3.17, the historical mean 8.28, the naïve method 14.18 and the drift method 14.58. On that series every one of those scores picked the same winner. The percentage scale is what made a megalitre error readable as a share of the beer production being forecast. The same ordering is a fact about those four columns on that series. It is not a theorem that the mean absolute percentage error and the mean absolute error must rank methods alike.{{cite:hyndman_athanasopoulos2021}} (§5.8, beer accuracy table)

A second table, the Google closing prices for January 2016, shows the same kind of score on a different unit. The naïve method had MAPE 5.67, the drift method 6.99 and the historical mean 16.24. Again the ordering agreed with the other accuracy columns of that table. Agreement in two examples is still two examples.{{cite:hyndman_athanasopoulos2021}} (§5.8, Google accuracy table)

## Intuition

Divide the error by the observation and multiply by 100. An error of 10 on an observation of 100 is 10 percent, and an error of 10 on an observation of 50 is 20 percent. Averaging the absolute percentages keeps over-forecasts and under-forecasts from cancelling. The divisor is the observation, so the same absolute miss is a larger percentage when the observation is smaller. A forecast that sits below a small observation is penalised more, as a percentage, than a forecast that sits the same distance above a large one. That asymmetry is a property of the ratio, not a defect in the arithmetic that computes it.{{cite:hyndman_koehler2006}} (p. 8, §2.2){{cite:hyndman_athanasopoulos2021}} (§5.8, Percentage errors)

## Definition

Write the forecast error as $e_t=y_t-\hat y_t$. The percentage error is $p_t=100\,e_t/y_t$, and

$$
\mathrm{MAPE}=\operatorname{mean}(|p_t|).
$$


The mean is taken over the period on which accuracy is being scored. Forecast errors in that period are computed from observations that were not used to form the forecasts. Residuals, by contrast, are one-step errors on the training data. The same definition is the mean of $|p_t|$ with $p_t=100 e_t/Y_t$, used to compare methods across series.{{cite:hyndman_athanasopoulos2021}} (§5.8, Forecast errors and Percentage errors){{cite:hyndman_koehler2006}} (p. 8, §2.2)

A symmetric variant used in forecasting competitions replaces the denominator. One common form is

$$
\mathrm{sMAPE}=\operatorname{mean}\left(\frac{200|y_t-\hat y_t|}{y_t+\hat y_t}\right).
$$


That form can be negative, and it is still unstable when both the observation and the forecast are near zero. Makridakis, Spiliotis and Assimakopoulos write a related score with absolute values in the denominator,

$$
\mathrm{sMAPE}=\frac{2}{k}\sum_{t=1}^{k}\frac{|Y_t-\hat Y_t|}{|Y_t|+|\hat Y_t|}\times 100\%,
$$


and use it, together with the mean absolute scaled error, as the accuracy measure on a large subset of the monthly M3 series. The absolute values keep their version from changing sign. They do not remove the heavier penalty on large positive errors that percentage scores are known for, which is why those authors also report a scaled error.{{cite:hyndman_athanasopoulos2021}} (§5.8, symmetric MAPE){{cite:makridakis_spiliotis_assimakopoulos2018}} (§3.1, pp. 5–6, equation 1)

## Properties

The MAPE is undefined or infinite if any observation in the scoring period is zero, and it becomes extreme when an observation is close to zero. A percentage also requires a meaningful zero. Temperature in degrees Celsius or Fahrenheit has an arbitrary zero, so a percentage error in those units does not measure forecast accuracy.{{cite:hyndman_athanasopoulos2021}} (§5.8, Percentage errors){{cite:hyndman_koehler2006}} (pp. 8–9, §2.2)

On series that do hit zero, the in-sample and out-of-sample MAPE can be infinite for every simple method under comparison, as happened for a lubricant series whose sales included zeros. A series of monthly log returns that contains zeros and negative values produced an infinite MAPE for the historical mean, the random walk, exponential smoothing and Holt’s method on the fitting period. The M3 competition avoided infinite MAPEs by keeping only positive series, which removes the problem from the contest and leaves it in place for any series that actually hits zero.{{cite:hyndman_koehler2006}} (pp. 5 and 8, Tables 2 and 3 and §2.2)

The symmetric form with a signed denominator can be negative even though it is described as an absolute percentage error. The form with absolute values in the denominator, as in the 2018 comparison of statistical and machine-learning forecasts, stays non-negative and still penalises large positive errors more than negative ones. Neither form is the MAPE. Substituting one for the other changes the ranking question.{{cite:hyndman_koehler2006}} (p. 9, §2.2){{cite:makridakis_spiliotis_assimakopoulos2018}} (§3.1, pp. 5–6)

## Worked example

Suppose the observations are 100, 200 and 50 and the forecasts are 110, 160 and 80. The errors are $-10$, $40$ and $-30$. The absolute percentage errors are

$$
100\cdot\frac{10}{100}=10,\qquad 100\cdot\frac{40}{200}=20,\qquad 100\cdot\frac{30}{50}=60.
$$


The MAPE is $(10+20+60)/3=30$. The mean absolute error on the original scale is $(10+40+30)/3=80/3\approx 26.667$, a different number because it is not a percentage. If the third observation had been 0, the third percentage error would have required division by zero and the MAPE would not have been a real number.{{cite:hyndman_athanasopoulos2021}} (§5.8, Percentage errors)

**Your turn.** Observations 80 and 120 are forecast as 100 and 90. Compute the two absolute percentage errors and their mean.

::: {.callout-tip collapse="true" title="Answer"}
The absolute percentage errors are $100\cdot 20/80=25$ and $100\cdot 30/120=25$. The MAPE is 25.
:::

## Assumptions and limits

Every observation in the average must be nonzero, and the zero of the measurement must be a real absence rather than an arbitrary origin. Values close to zero dominate the average even when they are genuine. Negative observations make a percentage hard to read as an absolute share of a level. Across series with very different scales, including zeros and negatives, a scaled error is the measure that stays finite whenever the historical series is not constant. The mean absolute scaled error compares each error with the average size of a naïve change on the training data, which is why it is reported beside sMAPE when the percentage score is the quantity a competition made familiar.{{cite:hyndman_koehler2006}} (pp. 8–9, §2.2){{cite:makridakis_spiliotis_assimakopoulos2018}} (§3.1, pp. 5–6){{cite:hyndman_athanasopoulos2021}} (§5.8, Scaled errors)

Scoring the same one-step errors that were used to fit the model answers a different question from scoring a held-out period. The beer and Google tables are held-out scores. An in-sample MAPE can be small because the method was allowed to fit the points it is then praised for hitting.{{cite:hyndman_athanasopoulos2021}} (§5.8, Forecast errors)

## Connections

The [mean squared error](mean-squared-error.qmd) averages squared discrepancies and stays in the squared units of the series. A [time series](time-series.qmd) is the ordered sample on which a forecast error is defined. Percentage errors are one summary of those errors. The mean absolute error stays on the original scale and is the natural comparison when every series shares a unit. The mean absolute scaled error is the scale-free alternative when a percentage is undefined. On one series the beer table’s MAPE of 3.17 and the Google table’s MAPE of 5.67 are both percentages, and they are not percentages of the same thing. Comparing them with each other, rather than comparing methods inside each table, drops the series that gave the percentage its meaning.{{cite:hyndman_athanasopoulos2021}} (§5.8, beer and Google tables){{cite:hyndman_koehler2006}} (p. 8, §2.2)
