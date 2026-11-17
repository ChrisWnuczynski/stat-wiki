## Motivating example

A store wants to forecast daily demand from earlier days. If the mean demand rises each month, observations from last year cannot be treated as draws from the same level as observations today. If the level and lag dependence remain stable, one set of time-series summaries can describe many time windows and support a more economical forecasting model.{{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1, Stationarity and differencing)

## Intuition

Stationarity means that moving the time origin does not change the probabilistic structure being modeled. It does not require a flat observed path: a stationary series wanders, rises for a while and falls for a while. The stability concerns the *distribution* of such behavior across possible realizations. Without it, one long series can ask for a separate mean at every date and a separate covariance for every pair of dates, too many quantities to infer reliably from one path. Stationarity lets observations at different times inform common mean and lag-covariance quantities, though a law of large numbers or ergodicity is a further question.{{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1)

## Definition

A process $\{X_t:t\in\mathbb Z\}$ is *strictly stationary* when every finite vector $(X_{t_1},\ldots,X_{t_k})$ has the same joint distribution as $(X_{t_1+h},\ldots,X_{t_k+h})$ for every integer shift $h$. A process is *weakly stationary* when it has finite second moments, $E(X_t)=\mu$ independent of $t$, and $\operatorname{Cov}(X_s,X_t)=\gamma(t-s)$ for a function of the lag alone. Thus its variance is the common lag-zero value $\gamma(0)$. Weak stationarity says less about the full distribution than strict stationarity{{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1, Stationarity and differencing).

If $\gamma(0)>0$, the autocorrelation at lag $h$ is $\rho(h)=\gamma(h)/\gamma(0)$. Covariance symmetry gives $\gamma(-h)=\gamma(h)$, and Cauchy–Schwarz gives $|\rho(h)|\le1$. The vector of covariances at several dates must also form a positive semidefinite matrix: no weighted sum of observations can have a negative variance. These restrictions help distinguish a possible stationary covariance function from an arbitrary sequence of numbers{{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1, Stationarity and differencing).

## Interpretation — Two strengths of stability

Strict stationarity with finite variance implies weak stationarity, because the one- and two-time distributions remain unchanged after a common shift. A Gaussian process goes the other way too: its finite-dimensional normal laws are determined by their mean vectors and covariance matrices, so constant mean and lag covariance make those laws shift invariant. Outside the Gaussian case, identical first two moments can hide time-varying distributional shape. An independent sequence alternating between two different zero-mean, unit-variance distributions is weakly stationary but not strictly stationary. Conversely, independent identically distributed Cauchy variables are strictly stationary yet lack the finite variance required for weak stationarity.

One must distinguish fixed seasonal movement from irregular cycles. A deterministic monthly mean pattern changes with calendar month and violates ordinary stationarity. A stationary stochastic process may still produce cycles of varying length whose phase is not tied to the calendar. Hyndman and Athanasopoulos illustrate this with aperiodic population cycles; simply seeing peaks in a plot does not settle the definition. {{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1, cyclic-series examples)

## Properties — What stable covariances allow

For a weakly stationary process, $\operatorname{Var}(X_t-X_{t-h})=2\{\gamma(0)-\gamma(h)\}$. This relates movement over a lag to the variance at one time and the persistence between times. A moving average $X_t=\varepsilon_t+\theta\varepsilon_{t-1}$ with independent mean-zero innovations of variance $\sigma^2$ has $\gamma(0)=\sigma^2(1+\theta^2)$, $\gamma(1)=\sigma^2\theta$, and $\gamma(h)=0$ for $|h|>1$. Its mean and covariance do not depend on the calendar date, making it a concrete stationary model when the innovations are identically distributed{{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1, Stationarity and differencing).

The process $S_t=\sum_{j=1}^t\varepsilon_j$, starting at zero with independent innovations of variance $\sigma^2$, is different. Its mean may stay at zero, but $\operatorname{Var}(S_t)=t\sigma^2$ grows with time. Its increment $S_t-S_{t-1}=\varepsilon_t$ is stationary when the innovations are identically distributed. Differencing can remove such a changing level; it does not guarantee that *every* trend, seasonal pattern or change in variance has been cured. {{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1, Differencing and Random walk model)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a strict-stationary process with finite second moments, the laws of $X_t$ and $(X_s,X_t)$ are invariant under common shifts. Their means and covariances are therefore invariant too, giving weak stationarity. For a Gaussian process, equal mean vectors and covariance matrices determine equal finite-dimensional laws, proving the converse under weak stationarity.

For weak stationarity, expanding the variance of a difference gives $\operatorname{Var}(X_t-X_{t-h})=\gamma(0)+\gamma(0)-2\gamma(h)$. Cauchy–Schwarz yields $|\gamma(h)|\le\sqrt{\gamma(0)\gamma(0)}=\gamma(0)$. Finally, for any coefficients $a_1,\ldots,a_k$, $\sum_{i,j}a_i a_j\gamma(t_i-t_j)=\operatorname{Var}(\sum_i a_iX_{t_i})\ge0$, proving positive semidefiniteness. For the MA(1), expansion and innovation independence leave two variance terms at lag zero, one shared innovation at lag one, and no shared term beyond that. The random walk variance is the sum of $t$ innovation variances.
:::
:::

{{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1, Differencing and Random walk model)

## Statistical use — Diagnose, transform, then check

Plot the series against time before fitting a stationary model. A rising level, fixed seasonal pattern or changing spread suggests the raw series fails the assumption. Compare early and late windows, inspect the autocorrelation function, and consider a transformation for changing variance or differencing for changes in level. A slowly decaying sample ACF can be a clue to nonstationarity, but these finite-sample displays are diagnostic evidence rather than a proof. After modeling, check whether residual dependence or changing scale remains.{{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1, time plot, ACF and Differencing)

Weak stationarity is the working assumption for many covariance and ARMA calculations; it does not by itself say sample averages converge to population quantities. Long-range dependence or a common latent random level can leave a process stationary while a single path remains uninformative about part of the ensemble law. A practitioner should separate the stationarity assumption from ergodicity and from forecast-model adequacy.

Consider independent $X_t$ that are $-1$ or $1$ with equal probability at even times, but are $0$ with probability $1/2$ and $-\sqrt2$ or $\sqrt2$ with probability $1/4$ each at odd times. Every time has mean $0$ and variance $1$, and cross-time covariance is zero, so the series is weakly stationary. Its one-time distribution alternates, so it is not strictly stationary. In another concrete failure, a random walk with innovation variance $4$ has variance $4t$: its early and late levels have different spreads even though its increments have the same distribution. These examples show why the desired level of stationarity must be stated{{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1, Differencing and Random walk model).
## Worked example

Let $X_t=\varepsilon_t+0.5\varepsilon_{t-1}$, where the innovations are independent, identically distributed, mean zero and variance $4$. Then $\gamma(0)=4(1+0.5^2)=5$, $\gamma(1)=4(0.5)=2$, and $\rho(1)=2/5=0.4$. The variance of a one-step change is $2(5-2)=6$. The same values apply at every date, so this model is weakly stationary. A plot can still show runs of large or small values by chance; those runs do not change its theoretical moments{{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1, Stationarity and differencing).

**Your turn.** Keep innovation variance $4$ but set $\theta=-0.25$. Find $\gamma(0)$, $\gamma(1)$, $\rho(1)$ and the variance of a one-step change. Does the negative adjacent correlation make the series nonstationary?

::: {.callout-tip collapse="true" title="Answer"}
The variance is $\gamma(0)=4(1+0.25^2)=4.25$, and lag-one covariance is $\gamma(1)=4(-0.25)=-1$. Thus $\rho(1)=-1/4.25\approx-0.2353$ and $\operatorname{Var}(X_t-X_{t-1})=2(4.25-(-1))=10.5$. The negative correlation describes alternating tendency at adjacent times; the mean and lag covariance remain time invariant, so the process is weakly stationary. covariance)
:::

## Common misconceptions

Stationarity does not mean the observed path is constant or has no temporary runs. A constant mean alone is insufficient: the random walk has constant mean but growing variance. Weak stationarity does not ensure an invariant full distribution outside the Gaussian case. Differencing a nonstationary series once is not a universal cure; a seasonal component or changing variance may remain. Finally, stationarity is not the same as independence or ergodicity.{{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1)

## Connections

[Strict stationarity](strict-stationarity.qmd) and [weak stationarity](weak-stationarity.qmd) develop the two definitions. The [autocorrelation function](autocorrelation-function.qmd) summarizes lag dependence, while the [variogram](variogram.qmd) describes changes over a lag. [Autoregression and moving averages](autoregression-and-moving-averages.qmd) give model examples. The [Wold decomposition](wold-decomposition.qmd) represents weakly stationary series through innovations plus a predictable component; its theorem is stronger than the elementary covariance facts proved here.{{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1)

## History

An older practice decomposes observed series into trend, seasonal, cyclical and irregular components; W. M. Persons proposed a four-part decomposition in 1919. The later mathematical language of stationarity states precisely what kind of stability is expected of the component modeled after trend or seasonality is handled. Modern forecasting texts still put stationarity and differencing before ARIMA model fitting, linking that abstract assumption to practical checks on a plotted series.{{cite:dodge2008}} (p. 536, Time Series, History){{cite:hyndman_athanasopoulos2021}} (Ch. 9 §9.1, Stationarity and differencing)
