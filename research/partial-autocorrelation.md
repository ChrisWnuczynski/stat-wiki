# Partial autocorrelation

Rank 352. Lighter tier. Concept page.

## Facts checked

- Hyndman and Athanasopoulos, *Forecasting: Principles and Practice*, 3rd ed., §9.5 “ACF and PACF plots”: partial autocorrelations remove lags \(1,\ldots,k-1\); the lag-\(k\) coefficient equals the last coefficient in an autoregression of order \(k\); the first partial autocorrelation equals the first autocorrelation.
- Dodge, printed p. 412: the partial autocorrelation at lag \(k\) is the autocorrelation between \(Y_t\) and \(Y_{t-k}\) not accounted for by lags \(1\) through \(k-1\).
- AR(1) with \(\phi=0.5\): autocorrelations \(0.5\), \(0.25\), \(0.125\); partial autocorrelations \(0.5,0,0\). Residual covariance with \(\varepsilon_t\) is \(0\).
- MA(1) with coefficient \(0.6\): \(\rho_1=0.6/1.36=15/34\approx 0.441176\), printed \(0.4412\). \(\phi_{22}=-225/931\approx -0.241676\), printed \(-0.2417\).
- Check: \(\phi=0.8\) gives \(\rho_2=0.64\) and \(\phi_{22}=0\). \(\rho_1=0.5\), \(\rho_2=0.1\) gives \(\phi_{22}=-0.2\).

## Assumed

- The lag-\(2\) population formula is the normal equation for the two-lag regression. It was checked against the AR(1) residual argument, where both give \(0\).

## Disputed

- None.

## Not opened

- Box and Jenkins (1970) and Brockwell and Davis (1991), cited on the page, were not reopened. The Egyptian-exports figure in Hyndman and Athanasopoulos was not recomputed.
