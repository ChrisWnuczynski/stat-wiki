## Motivating example
Daily demand is often close to yesterday's demand, but a surprise yesterday can also affect today's orders. Those are two different ways for a series to remember the past. An autoregression (AR) relates a value to earlier *values*; a moving-average (MA) model relates it to current and earlier *innovations*, the unpredictable shocks left after past information has been used. Both turn serial dependence into a forecasting rule.{{cite:hyndman_athanasopoulos2021}} (§§9.3–9.4)

## Intuition
In an AR model, a high observation can carry forward and gradually lose influence. In an MA model, a shock enters for a fixed number of time steps and then disappears. This difference gives characteristic autocorrelation patterns: a stable AR(1) has correlations that decay by powers of its coefficient, whereas an MA(1) has no population correlation beyond lag one. The patterns are guides to modelling, not guarantees that a short noisy series reveals its true order.{{cite:hyndman_athanasopoulos2021}} (§§9.3–9.5, ACF and PACF plots)

## Definition
Let $\varepsilon_t$ be zero-mean, uncorrelated innovations with common variance $\sigma^2$. A mean-centred AR($p$) model uses past values,
$$
X_t-\mu=\sum_{j=1}^{p}\phi_j(X_{t-j}-\mu)+\varepsilon_t.
$$
An MA($q$) model uses past shocks,
$$
X_t=\mu+\varepsilon_t+\sum_{j=1}^{q}\theta_j\varepsilon_{t-j}.
$$
An ARMA model includes both terms. The *model* called MA($q$) must be distinguished from a rolling arithmetic average of the latest $q$ observations. The latter is a smoothing calculation on observed values; its weights often sum to one, while the innovation coefficients of an MA model need not.{{cite:hyndman_athanasopoulos2021}} (§§9.3–9.5)

## Properties — Persistence and short memory
For an AR(1), $X_t-\mu=\phi(X_{t-1}-\mu)+\varepsilon_t$. If $|\phi|<1$ and the innovations have finite variance, the stationary variance is $\sigma^2/(1-\phi^2)$ and the lag-$h$ autocorrelation is $\phi^{|h|}$. A positive coefficient preserves the direction of a departure from the mean; a negative one tends to alternate it. If $\phi=1$, the model is a random walk, whose variance grows with time rather than remaining stationary.{{cite:hyndman_athanasopoulos2021}} (§9.3)

For an MA(1), $X_t=\mu+\varepsilon_t+\theta\varepsilon_{t-1}$, the variance is $\sigma^2(1+\theta^2)$ and the lag-one covariance is $\theta\sigma^2$. All covariances beyond lag one are zero because the two observations share no innovation. This finite *linear* memory does not mean the observations are independent unless stronger assumptions, such as independent innovations, are imposed. The usual invertibility restriction $|\theta|<1$ chooses a representation whose innovations can be recovered stably from the observed past; an MA(1) remains stationary even when this restriction fails.{{cite:hyndman_athanasopoulos2021}} (§9.4)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $Z_t=X_t-\mu$ for the AR(1). Under a stationary causal solution with $|\phi|<1$, repeated substitution gives $Z_t=\sum_{j=0}^{\infty}\phi^j\varepsilon_{t-j}$. Uncorrelated innovations then give
$\operatorname{Var}(Z_t)=\sigma^2\sum_{j=0}^{\infty}\phi^{2j}=\sigma^2/(1-\phi^2)$.
For $h\ge0$, only shared innovation terms survive in $\operatorname{Cov}(Z_t,Z_{t-h})$, giving $\phi^h\sigma^2/(1-\phi^2)$ and hence correlation $\phi^h$; covariance symmetry handles negative lags. When $\phi=1$, $Z_t=Z_0+\sum_{j=1}^t\varepsilon_j$ and, if $Z_0$ is independent of the innovations, its variance is $\operatorname{Var}(Z_0)+t\sigma^2$.

For the MA(1), multiplying $(\varepsilon_t+\theta\varepsilon_{t-1})(\varepsilon_{t-h}+\theta\varepsilon_{t-h-1})$ and taking expectations leaves two squared terms at $h=0$, one shared term at $|h|=1$, and none at larger lags. Thus $\gamma_0=\sigma^2(1+\theta^2)$, $\gamma_1=\theta\sigma^2$, and $\gamma_h=0$ for $|h|>1$.{{cite:hyndman_athanasopoulos2021}} (§§9.3–9.4)
:::
:::

## Statistical use — Choosing and checking a model
First inspect the series for trend or seasonality, because a changing mean can produce apparent persistence that a stationary ARMA model cannot explain. On a suitably stable series, the sample autocorrelation and partial autocorrelation help suggest orders, and fitted residuals should be checked for remaining serial structure. An AR term lets a departure in the observed level affect several forecasts; an MA term lets an estimated past forecast error affect the near future. ARIMA models add differencing when a series needs it before these dependence terms are applied.{{cite:hyndman_athanasopoulos2021}} (§§9.1, 9.5–9.7)

With $\phi=1$ and nonzero innovation variance, an AR(1) becomes a random walk; its variance increases each step, so stationary AR formulas such as $\sigma^2/(1-\phi^2)$ are invalid. A series whose mean rises through a season cannot be described adequately by one stationary mean without accounting for that trend or seasonality. If residuals retain strong correlation after fitting, the chosen lag orders have left dependence unexplained. And if innovations are merely uncorrelated rather than independent, the covariance calculations above still work, but stronger claims about independent distant observations do not follow.{{cite:hyndman_athanasopoulos2021}} (§§9.1, 9.3–9.7)

## Worked example
Suppose demand has long-run mean $\mu=10$, follows a stationary AR(1) with $\phi=3/5=0.6$, and has innovation variance $\sigma^2=4$. If today's value is $X_t=12$, the one-step conditional forecast is
$$
\widehat X_{t+1\mid t}=10+(3/5)(12-10)=56/5=11.2.
$$
One more step with no new shock gives $\widehat X_{t+2\mid t}=10+(3/5)^2(12-10)=268/25=10.72$. The forecast moves toward ten, and the stationary variance is $4/[1-(3/5)^2]=25/4=6.25$.

For comparison, give an MA(1) the same mean and innovation variance but set $\theta=1/2$. Its variance is $4[1+(1/2)^2]=5$, lag-one covariance is $(1/2)4=2$, and lag-one correlation is $2/5=0.4$. If the latest estimated innovation is $\varepsilon_t=2$, the one-step forecast is $10+(1/2)2=11$; with no later information, the two-step forecast is already $10$. The AR level deviation fades geometrically, while the MA shock expires after one more observation.{{cite:hyndman_athanasopoulos2021}} (§§9.3–9.4, model-based calculations)

**Your turn.** In the MA(1) example, change $\theta$ to $-1/2$ while keeping $\mu=10$, $\sigma^2=4$, and the latest innovation $\varepsilon_t=2$. Find the next forecast, the forecast two steps ahead, and the lag-one correlation.

::: {.callout-tip collapse="true" title="Answer"}
The next forecast is $10+(-1/2)2=9$; the two-step forecast is $10$. The variance remains $4[1+(-1/2)^2]=5$, but lag-one covariance becomes $(-1/2)4=-2$, so the correlation is $-2/5=-0.4$. A negative MA coefficient reverses the immediate effect of a shock without making it persist indefinitely.
:::

## Common misconceptions
The MA($q$) in an ARMA model does not mean averaging the last $q$ observed values; it combines latent shocks. Zero population autocorrelation beyond lag one for an MA(1) is not the claim that a finite sample ACF must be exactly zero there. A positive fitted AR coefficient below one describes decay toward a stable mean, not a deterministic upward trend. Finally, stationarity and invertibility answer different questions: an MA(1) is stationary for every finite coefficient, but the conventional invertible representation restricts its magnitude below one.{{cite:hyndman_athanasopoulos2021}} (§§9.3–9.5)

## Connections
[Autocorrelation](autocorrelation-function.qmd) measures the lag pattern these models imply. [Weak stationarity](weak-stationarity.qmd) supplies the constant-mean and lag-only covariance setting for the formulas, while [white noise](white-noise.qmd) supplies the innovations. [ARIMA](arima-model.qmd) adds differencing; the three-series figure above contrasts a stable AR(1), an MA(1), and the nonstationary random walk.{{cite:hyndman_athanasopoulos2021}} (ch. 9)

## History
Early time-series work asked how to describe changing levels and apparent cycles rather than treating observations as unrelated; Astronomical records, trend fitting and seasonal decomposition were part of that work. The later ARIMA forecasting framework put AR and MA components side by side. Rolling smoothing is an older and still useful meaning of “moving average,” and it is not the innovation model. The distinction matters whenever a forecasting equation is interpreted.{{cite:dodge2008}} (p. 360, “Moving Average”; p. 536, “Time Series”){{cite:hyndman_athanasopoulos2021}} (§§9.3–9.5)
