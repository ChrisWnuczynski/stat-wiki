## Lead context
The partial autocorrelation at a lag is the correlation between a series and that lag after the linear effect of the lags in between has been removed.

## Motivating example
An autoregression $X_t=0.5 X_{t-1}+\varepsilon_t$ has autocorrelations $0.5$, $0.25$ and $0.125$ at lags $1$, $2$ and $3$. The partial autocorrelations are $0.5$, $0$ and $0$. The lag-$2$ association runs through lag $1$.

## Intuition — Take out the path through the intermediate times
The ordinary autocorrelation at lag \(2\) includes the route \(X_t\leftarrow X_{t-1}\leftarrow X_{t-2}\). An autoregression of order \(1\) uses exactly that route, so once \(X_{t-1}\) is accounted for, lag \(2\) has nothing left to explain. The partial autocorrelation is the correlation of the two residuals from regressing \(X_t\) and \(X_{t-k}\) on the intermediate lags. At lag \(1\) there is no intermediate time, so the partial autocorrelation equals the lag-\(1\) autocorrelation.{{cite:hyndman_athanasopoulos2021}} (§9.5, ACF and PACF plots){{cite:dodge2008}} (p. 412)

## Definition — The last autoregressive coefficient
For a weakly stationary series, the lag-\(k\) partial autocorrelation \(\phi_{kk}\) is the coefficient of \(X_{t-k}\) in the best linear predictor of \(X_t\) from \(X_{t-1},\ldots,X_{t-k}\). Equivalently, it is the correlation of those two residuals. Hyndman and Athanasopoulos estimate it as the last coefficient in an autoregression of order \(k\). An autoregression of order \(p\) has \(\phi_{kk}=0\) for every \(k>p\).{{cite:hyndman_athanasopoulos2021}} (§9.5, ACF and PACF plots)

## Properties — An autoregression of order \(1\) cuts off after lag \(1\)
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let \(X_t=\phi X_{t-1}+\varepsilon_t\) with \(|\phi|<1\) and \(\varepsilon_t\) uncorrelated with the past, mean zero, and variance constant. Then \(\rho_1=\phi\) and \(\rho_2=\phi^2\). Regress \(X_t\) and \(X_{t-2}\) on \(X_{t-1}\). The residuals are \(X_t-\phi X_{t-1}=\varepsilon_t\) and \(X_{t-2}-\phi X_{t-1}\). Their covariance is
\[
\mathrm{E}(\varepsilon_t X_{t-2})-\phi\,\mathrm{E}(\varepsilon_t X_{t-1})=0,
\]
because \(\varepsilon_t\) is uncorrelated with both earlier values. The residual correlation is \(0\), so \(\phi_{22}=0\). The same cancellation applies at every lag beyond \(1\).
:::
:::

The population formula that agrees with this regression at lag \(2\) is
\[
\phi_{22}=\frac{\rho_2-\rho_1^2}{1-\rho_1^2}
\]
when \(|\rho_1|<1\). For the autoregression, the numerator is \(\phi^2-\phi^2=0\).

## Worked example — Autoregression \(0.5\), and a moving average
For \(X_t=0.5 X_{t-1}+\varepsilon_t\), the autocorrelations are \(0.5\), \(0.25\) and \(0.125\) at lags \(1\), \(2\) and \(3\). The partial autocorrelations are \(0.5\), \(0\) and \(0\). The lag-\(2\) formula gives \((0.25-0.25)/(1-0.25)=0\).

A moving average \(X_t=\varepsilon_t+0.6\varepsilon_{t-1}\) does the opposite. Its lag-\(1\) autocorrelation is
\[
\rho_1=\frac{0.6}{1+0.6^2}=\frac{0.6}{1.36}=\frac{15}{34}\approx 0.4412,
\]
and \(\rho_k=0\) for \(k>1\). The lag-\(2\) partial autocorrelation is not zero:
\[
\phi_{22}=\frac{0-(15/34)^2}{1-(15/34)^2}=-\frac{225}{931}\approx -0.2417.
\]
The autocorrelation has cut off, and the partial autocorrelation has not.

**Your turn.** For the autoregression with coefficient \(0.5\), compute \(\phi_{22}\) from \(\rho_1=0.5\) and \(\rho_2=0.25\) again, and state \(\phi_{33}\).

::: {.callout-tip collapse="true" title="Answer"}
\((0.25-0.5^2)/(1-0.5^2)=0/0.75=0\). Every partial autocorrelation beyond lag \(1\) is \(0\), so \(\phi_{33}=0\).
:::

## Connections — Order, the autocorrelation, and a cutoff in the other direction
The [autocorrelation function](autocorrelation-function.qmd) of an autoregression decays and does not cut off. The partial autocorrelation is the plot that cuts off, which is why it suggests the order of an [autoregression](autoregression-and-moving-averages.qmd). A moving average cuts the autocorrelation off and leaves a tail in the partial autocorrelation, as the coefficient \(0.6\) did. Both descriptions need [weak stationarity](weak-stationarity.qmd), so that the correlations depend on the lag alone.{{cite:hyndman_athanasopoulos2021}} (§9.5, ACF and PACF plots){{cite:dodge2008}} (p. 412)

