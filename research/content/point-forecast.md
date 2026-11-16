## Motivating example
A city wants one number for next month's electricity demand so that it can schedule generation. The last observed month is informative, but it does not determine the next one: weather and exceptional events remain unknown. A point forecast gives the scheduling calculation a centre. The city also needs a range of plausible outcomes when deciding how much reserve to hold. These are different questions, so a forecast should name its target, its horizon, and the loss attached to a wrong prediction.

## Intuition
Think of a forecasting model as a collection of possible futures after the present. A point forecast compresses their conditional distribution to one number. Under squared error, large misses receive disproportionate weight and the appropriate centre is the conditional mean. Under absolute error, the conditional median is appropriate; under an asymmetric cost, a suitable conditional quantile can be preferable. The word *best* therefore requires a loss function. A forecast is also conditional on the information actually available at the time it is issued. Information acquired after the forecast origin cannot honestly be used to assess a historical forecasting rule.

The horizon matters even if the same number is reported twice. In a stationary autoregression, today's deviation from the long-run mean is gradually forgotten. In a random walk, today's level persists as the forecast but uncertainty accumulates. A plotted line of point forecasts alone can conceal that difference. Dodge's forecasting entry distinguishes trend, cyclical, seasonal and irregular components and notes that the horizons at which these matter differ.{{cite:dodge2008}} (pp. 206–207, “Forecasting”)

## Definition
Write $\mathcal F_T$ for the information available at forecast origin $T$ and $Y_{T+h}$ for the future quantity of interest, with $h\geq1$. A point forecast $a_{T,h}$ is an $\mathcal F_T$-measurable single-valued prediction of $Y_{T+h}$. If the relevant conditional expectation exists and loss is $(Y_{T+h}-a)^2$, the optimal forecast is $a_{T,h}=\mathbb E(Y_{T+h}\mid\mathcal F_T)$. The condition means that the rule may use past observations and known covariates but cannot depend on the future observation itself.

The target must be stated carefully. A forecast of the next noisy observation differs from a forecast of its latent conditional mean, even when both have the same numerical centre. A forecast for next month's total also differs from one for next month's average daily demand. Aggregation changes the target and generally its uncertainty.

## Properties
Let $m=\mathbb E(Y\mid\mathcal F)$ and suppose the relevant second moments are finite. The conditional mean-squared error of any $\mathcal F$-measurable action $a$ is
$$
\mathbb E[(Y-a)^2\mid\mathcal F]
=\operatorname{Var}(Y\mid\mathcal F)+(a-m)^2.
$$
The first term is uncertainty left after conditioning; the second is the avoidable cost of moving away from the conditional mean. This identity also explains why an estimated forecasting model cannot eliminate the random variation of a future observation. Parameter estimation can add further uncertainty beyond the displayed expression when the fitted parameters are treated as uncertain.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $Y-a=(Y-m)+(m-a)$ and expand its square. Conditional on $\mathcal F$, $m-a$ is fixed and $\mathbb E(Y-m\mid\mathcal F)=0$, so the cross-term vanishes and the first identity follows. For absolute-error loss, the one-sided derivatives of $\mathbb E(|Y-a|\mid\mathcal F)$ are controlled by the conditional probabilities below and above $a$; zero lies between them exactly when $a$ is a conditional median. For a stationary AR(1), iterating $X_{t}-\mu=\phi(X_{t-1}-\mu)+\varepsilon_t$ with independent mean-zero innovations gives $\mathbb E(X_{T+h}\mid\mathcal F_T)=\mu+\phi^h(X_T-\mu)$ and forecast error $\sum_{j=0}^{h-1}\phi^j\varepsilon_{T+h-j}$. Independence gives its variance $\sigma^2\sum_{j=0}^{h-1}\phi^{2j}$. At $\phi=1$ the same iteration yields the random-walk forecast $X_T$ and variance $h\sigma^2$.
:::
:::

## Interpretation
For $|\phi|<1$, the AR(1) formula $\mu+\phi^h(X_T-\mu)$ approaches $\mu$. A positive $\phi$ preserves the direction of the latest deviation while a negative $\phi$ alternates it. The corresponding forecast-error variance approaches $\sigma^2/(1-\phi^2)$, the stationary marginal variance. This limiting behaviour does not mean the series becomes exactly equal to its mean; it says that the distant future is no longer strongly predictable from the current level under this model.

A prediction interval combines the forecast centre with a model for the forecast error. If that error is conditionally normal with standard deviation $s_h$, a nominal 95% interval using known model parameters is $a_{T,h}\pm1.96s_h$. The same arithmetic is not automatically an exact 95% interval after parameters have been estimated or when the errors are skewed or heavy-tailed. Coverage should be evaluated at the stated horizon and for the stated target.

## Statistical use
Choose a forecast origin, then record what was known there. Fit the model using only that information, calculate the point forecast at each needed horizon, and evaluate forecasts against observations that arrived later. Repeating this exercise over successive origins measures actual out-of-sample performance. A small training residual is not a substitute: a flexible model can fit the observed series closely while predicting new observations poorly.

Under squared error, a mean-squared forecast error compares forecast rules in the units squared of the target. Under absolute error, mean absolute error is in the original units and is less dominated by occasional large misses. These scores need the same target, horizons and evaluation periods to be comparable. A forecast may also be deliberately biased if operational costs are asymmetric: scheduling too little capacity can be much costlier than scheduling too much. In that case report the relevant quantile and the cost rule, rather than calling it a conditional-mean forecast.

## Worked example
Suppose a stationary series follows $X_t=0.5X_{t-1}+\varepsilon_t$, with independent, mean-zero innovations of variance $4$, and the last observation is $X_T=10$. At horizons one, two and three, the squared-error point forecasts are $5$, $2.5$ and $1.25$. Their forecast-error variances are $4$, $4(1+0.5^2)=5$, and $4(1+0.5^2+0.5^4)=5.25$. The stationary variance is $4/(1-0.5^2)=16/3\approx5.3333$. The third forecast is closer to the long-run mean zero than the first, while its uncertainty is larger. If the innovations are Gaussian and the parameters are known, the one-step 95% prediction interval is $5\pm1.96(2)=(1.08,8.92)$. The observed next value can fall outside it without contradicting the model.

**Your turn.** For the same series and last observation, find the four-step conditional-mean forecast and its forecast-error variance. Then explain what would change if the autoregressive coefficient were one.

::: {.callout-tip collapse="true" title="Answer"}
The four-step forecast is $0.5^4(10)=0.625$. The error variance is $4(1+0.5^2+0.5^4+0.5^6)=5.3125$. With coefficient one the process is a random walk: its four-step point forecast would remain $10$, while its error variance would be $4(4)=16$. Its level would not revert to zero.
:::

## Common misconceptions
A point forecast is not necessarily the most probable exact outcome. For a continuous distribution, any exact value has probability zero; even the density mode can differ from the mean. Nor is the conditional mean always the right decision: absolute and asymmetric losses favour other summaries. A narrow point-forecast line does not imply a narrow distribution of future outcomes. Finally, a forecast computed with data that became available after its purported origin is a hindsight calculation, not a genuine advance prediction.

## Assumptions and limits
The AR(1) calculations assume a fixed coefficient, independent mean-zero innovations and, for the stationary limit, $|\phi|<1$. A structural break in electricity demand after a major tariff change can move the conditional distribution so that a model fitted to earlier years misses systematically. A random walk with coefficient one has no stationary variance ceiling, so the stationary long-horizon formula fails. If forecast errors have a strongly asymmetric distribution, a symmetric normal interval can have poor coverage even when its centre is sensible. These failures concern model stability, dependence and distributional shape separately.

## Connections
The [conditional expectation](conditional-expectation.qmd) supplies the squared-error target; the [posterior predictive distribution](prior-and-posterior-predictive-distributions.qmd) adds parameter uncertainty in a Bayesian analysis. [Prediction intervals](prediction-interval.qmd) describe uncertainty around a future observation, while [ARIMA](arima-model.qmd) is one family of models that can produce the forecasts. A [time series](time-series.qmd) with trend or seasonality needs those features represented before a simple stationary AR(1) interpretation is used.{{cite:dodge2008}} (pp. 206–207, trend and seasonal components)

## History
Dodge's account records the classical decomposition of a forecast into secular trend, cyclical fluctuation, seasonal variation and irregular variation. Its different short-, medium- and long-horizon constructions show why the horizon was explicit in forecasting practice before modern automated fitting routines.{{cite:dodge2008}} (pp. 206–207, “Forecasting”)
