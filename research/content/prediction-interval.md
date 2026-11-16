## Lead context
A prediction interval is a range for a new observation, and it stays wide even after the fitted mean is known precisely.

## Motivating example
A weather model can pin down the mean ozone at a stated temperature and still be a poor forecast of tomorrow's reading. Tomorrow adds a fresh residual on top of whatever uncertainty remains in the fitted mean. An interval for the mean answers a narrower question than an interval for that new day.{{cite:hyndman_athanasopoulos2021}} (§5.5, Prediction intervals)

## Intuition — Two layers of uncertainty
The fitted value at a chosen covariate is an estimate of a mean. A new response at that covariate equals the mean plus a new error. The interval for the mean can shrink toward a point as the sample grows. The interval for the new response cannot: the new error keeps a variance of its own, so the forecast interval levels off at a width set by that residual scale.{{cite:hyndman_athanasopoulos2021}} (§5.5, One-step prediction intervals){{cite:nist_prediction_interval}} (§4.5.1.2, prediction intervals)

## Definition — A future response on a straight line
Suppose $Y_1,\ldots,Y_n$ are independent, $Y_i=\beta_0+\beta_1 x_i+\varepsilon_i$, with fixed predictors and $\varepsilon_i\sim N(0,\sigma^2)$. Let $\widehat Y(x)$ be the least-squares fitted value at a new predictor $x$, and let $Y_{\mathrm{new}}$ be a new response at that $x$, independent of the sample and using the same line. A $100(1-\alpha)\%$ prediction interval is
$$
\widehat Y(x)\pm t_{n-2,\,1-\alpha/2}\,S\sqrt{1+\frac1n+\frac{(x-\overline x)^2}{S_{xx}}},
$$
where $S^2$ is the residual mean square on $n-2$ degrees of freedom and $S_{xx}=\sum_i(x_i-\overline x)^2$. The leading $1$ under the square root is the new residual. The other two terms are the variance of the fitted mean.{{cite:nist_prediction_interval}} (§4.5.1.2, $\hat\sigma_p=\sqrt{\hat\sigma^2+\hat\sigma_f^2}$)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $\widehat Y(x)=\overline Y+\widehat\beta_1(x-\overline x)$. For fixed predictors, $\overline Y$ and $\widehat\beta_1$ are uncorrelated, with variances $\sigma^2/n$ and $\sigma^2/S_{xx}$. Hence
$$
\operatorname{Var}\{\widehat Y(x)\}=\sigma^2\left\{\frac1n+\frac{(x-\overline x)^2}{S_{xx}}\right\}.
$$
Independence of $Y_{\mathrm{new}}$ adds $\sigma^2$, so
$$
\operatorname{Var}\{Y_{\mathrm{new}}-\widehat Y(x)\}=\sigma^2\left\{1+\frac1n+\frac{(x-\overline x)^2}{S_{xx}}\right\}.
$$
Under normal errors the studentised residual follows $t_{n-2}$, and the displayed interval is the usual inversion of that pivot.{{cite:nist_prediction_interval}} (§4.5.1.2, $t$ multiplier)
:::
:::

## Worked example
Eleven fixed predictors are $0,1,\ldots,10$, so $\overline x=5$ and $S_{xx}=110$. At $x=8$ the fit is $\widehat y=12$ and $s=1.5$. Then
$$
1+\frac1{11}+\frac{3^2}{110}=1.17273,\qquad 1.5\sqrt{1.17273}=1.62439.
$$
The $0.975$ quantile of $t_9$ is $2.26216$, and the margin is $2.26216\times 1.62439=3.67462$. The 95% prediction interval is $(8.325,15.675)$. The matching interval for the mean uses standard error $0.62341$ and margin $1.410$, which is narrower because it omits the new residual.

**Your turn.** At the same fit, move the new predictor to $x=5$, the centre of the sample. Compute the 95% prediction standard error and the margin, still with $t_{9,0.975}=2.26216$ and $s=1.5$.

::: {.callout-tip collapse="true" title="Answer"}
The leverage term vanishes, so the factor under the square root is $1+1/11=1.09091$. The prediction standard error is $1.5\sqrt{1.09091}=1.56670$, and the margin, using the unrounded $t_9$ quantile, is $3.54412$. The interval is shorter than at $x=8$ because the slope is not being extrapolated, and it is still much wider than an interval for the mean.
:::

## Connections — Means, forecasts, and coverage
A [confidence interval](confidence-interval.qmd) covers a fixed parameter. A prediction interval covers a random future response, which is why the residual variance remains after the parameter uncertainty has gone. In a time-series forecast the same idea appears as $\hat y_{T+h|T}\pm c\hat\sigma_h$, and $\hat\sigma_h$ usually grows with the horizon.{{cite:hyndman_athanasopoulos2021}} (§5.5, Multi-step prediction intervals) The straight-line case is the [pivot](pivot.qmd) $(\,Y_{\mathrm{new}}-\widehat Y(x)\,)/(\text{estimated scale})$, inverted for the unobserved $Y_{\mathrm{new}}$.

## Check yourself

### Known line, one new draw
The line is known exactly, $\sigma=2$, and a new response is normal about the line. Give a 95% prediction interval around the known mean $10$, using the normal multiplier $1.96$.

::: {.callout-tip collapse="true" title="Answer"}
There is no uncertainty in the mean, so the half-width is $1.96\times 2=3.92$. The interval is $(6.08,13.92)$.
:::

### Why the mean interval is the wrong forecast
At $x=8$ in the worked example the 95% interval for the mean runs from $12-1.410=10.590$ to $12+1.410=13.410$. Why is that range too narrow as a forecast of one new response?

::: {.callout-tip collapse="true" title="Answer"}
It accounts only for uncertainty in $\widehat Y(8)$. One new response also has variance $\sigma^2$, so the prediction margin is $3.67462$ rather than $1.410$. Quoting $(10.590,13.410)$ as a range for a single new outcome understates the residual scatter the model itself assumes.
:::
