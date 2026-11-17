## Motivating example
A daily balance changes by an average gain plus an unpredictable shock. Even when the shocks have no trend, their cumulative sum produces persistent movements in the balance. A random walk with drift separates the expected accumulated change from this growing uncertainty. A steady positive average does not mean that every realized step, or every finite-horizon change, is positive.{{cite:hyndman_athanasopoulos2021}} (§5.2, Drift method; §9.1, random walk models)

## Definition — Independent increments and a deterministic start
Let $S_n=s_0+\sum_{i=1}^nY_i$, where the increments are iid with mean $\mu\ne0$ and finite variance $\sigma^2$. Equivalently, write $S_n=S_{n-1}+\mu+\varepsilon_n$, with $E\varepsilon_n=0$. The coefficient of $S_{n-1}$ is one. A coefficient larger than one instead creates an explosive autoregression, while an intercept in a stationary autoregression produces a long-run mean rather than a linearly accumulating drift.{{cite:hyndman_athanasopoulos2021}} (§§9.1, 9.3, autoregressive models)

## Properties — Drift, fluctuations and correlation
Linearity and independence give $E(S_n)=s_0+n\mu$ and $\operatorname{Var}(S_n)=n\sigma^2$. For $m\le n$, the two sums share their first $m$ increments, giving $\operatorname{Cov}(S_m,S_n)=m\sigma^2$ and correlation $\sqrt{m/n}$ when $m>0,\sigma^2>0$. The process is therefore not covariance-stationary: its variance changes with time. The first difference $S_n-S_{n-1}=Y_n$ is stationary under the iid assumption.{{cite:grinstead_snell1997}} (§§6.2, 7.1, variances and sums){{cite:hyndman_athanasopoulos2021}} (§9.1, differencing)

The weak or strong law gives $(S_n-s_0)/n\to\mu$ in the corresponding mode, while the central limit theorem gives
$$\frac{S_n-s_0-n\mu}{\sigma\sqrt n}\Rightarrow N(0,1)\quad(\sigma^2>0).$$
Thus drift is order $n$ and standard deviation order $\sqrt n$. Their ratio $|\mu|\sqrt n/\sigma$ grows, but an event about crossing a barrier at any time depends on the whole path, rather than on a one-time normal approximation. For positive drift, the strong law does imply $S_n\to+\infty$ almost surely under integrable iid increments; it does not imply monotonicity.{{cite:durrett2019}} (§§2.4, 3.4.1)

## Worked example — Forecasting with known drift
Let $s_0=100$, $\mu=0.5$ and $\sigma=2$. After sixteen steps, the mean is $108$, variance is $64$ and standard deviation is eight. If increments are normal, the endpoint distribution is exactly $N(108,64)$ and $P(S_{16}>100)=\Phi(1)\approx0.841345$. For other iid finite-variance increments this is a normal approximation whose quality depends on their distribution and the horizon.

Given observations through time $T$, a known-drift forecast is $S_T+h\mu$. Its error is the sum of $h$ independent future centered increments and has variance $h\sigma^2$. For $h=9$ and $S_T=120$, the forecast is $124.5$ with standard deviation six. These are forecast uncertainties for a future level, rather than standard errors for estimating the drift.{{cite:hyndman_athanasopoulos2021}} (§5.5, prediction intervals; §9.1, random walk)

**Your turn.** For $s_0=0$, drift $-0.2$ and increment variance $0.64$, find the mean and standard deviation at step $25$.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $25(-0.2)=-5$. The variance is $25(0.64)=16$, so the standard deviation is four.
:::

## Statistical use — Estimating a drift from observed differences
With $T$ observed levels, the average of the $T-1$ increments is $\widehat\mu=(S_T-S_1)/(T-1)$. It gives the drift forecast $S_T+h\widehat\mu$. If the increment variance is known and future increments are independent of the observed ones, the unconditional forecast-error variance is
$$h\sigma^2+\frac{h^2\sigma^2}{T-1}.$$
The first term is future shock uncertainty and the second is drift estimation uncertainty. The cross term is zero by independence. Treating the fitted drift as known drops the second term, especially consequential at long horizons.{{cite:hyndman_athanasopoulos2021}} (§§5.2, 5.5, drift forecasts and forecast distributions)

Seasonality, changing drift and dependent shocks require a different model. Differencing can expose their structure, but it does not prove the increments are independent. A fitted positive trend is also not a guarantee of profit or safety; these are probability models whose assumptions need to match the measurement process.{{cite:hyndman_athanasopoulos2021}} (§9.1){{cite:durrett2019}} (§2.4, assumptions of laws of large numbers)
