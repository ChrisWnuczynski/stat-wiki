## Motivating example
A series of monthly demand figures may have a large value this month because last month was large, because the same month last year was large, or because the entire series has risen over time. A single ordinary correlation cannot separate these explanations. By comparing the series with copies shifted by one month, two months, and so on, the autocorrelation function (ACF) makes the relevant time gap visible. The resulting plot, also called a *correlogram*, is a diagnostic: a high seasonal-lag value suggests a repeated pattern, while a slow decay can indicate a trend that should be addressed before fitting a stationary model.{{cite:hyndman_athanasopoulos2021}} (§2.8, trend and seasonality in ACF plots; §9.1, differencing)

## Intuition
At lag $k$, pair the value now with the value $k$ time steps earlier. Positive correlation means high values tend to follow high values at that separation; negative correlation means high values tend to pair with low values. The zero-lag value equals one because every observation is perfectly correlated with itself. A plot across many lags is more informative than one coefficient: alternating signs, recurring peaks, and rapid or slow decay describe different kinds of serial structure. These are *linear* summaries; even a zero ACF at every nonzero lag need not rule out nonlinear dependence.{{cite:hyndman_athanasopoulos2021}} (§2.8, Autocorrelation)

The population ACF describes a process, whereas the sample ACF is calculated from a finite observed series. A short sample can show spikes even when its process has zero population autocorrelation, and its estimated mean affects every lagged product. The pattern is therefore evidence to investigate, not a certificate of a particular model order.{{cite:hyndman_athanasopoulos2021}} (§2.8, Autocorrelation; §9.5, ACF and PACF plots)

## Definition
For a weakly stationary process $\{X_t\}$ with positive finite variance, write $\mu=\mathbb E X_t$ and $\gamma(k)=\operatorname{Cov}(X_t,X_{t-k})$. Weak stationarity makes $\mu$ independent of $t$ and $\gamma(k)$ dependent only on the lag. The **population ACF** is
$$
\rho(k)=\frac{\gamma(k)}{\gamma(0)}
=\operatorname{Corr}(X_t,X_{t-k}).
$$
It has $\rho(0)=1$, $\rho(-k)=\rho(k)$, and $|\rho(k)|\le1$. Without constant variance and lag-only covariance, a single function of $k$ is not in general the correlation of every pair separated by $k$.{{cite:hyndman_athanasopoulos2021}} (§2.8, Autocorrelation)

For observations $y_1,\ldots,y_T$ with mean $\bar y$, a common **sample ACF** convention is
$$
r_k=\frac{\sum_{t=k+1}^{T}(y_t-\bar y)(y_{t-k}-\bar y)}
{\sum_{t=1}^{T}(y_t-\bar y)^2},\qquad 0\le k<T.
$$
This uses all $T$ observations in the denominator and $T-k$ lagged pairs in the numerator. Other normalisations exist, so small numerical differences between software packages can reflect a convention rather than a disagreement about the data.{{cite:hyndman_athanasopoulos2021}} (§2.8, sample autocorrelation formula)

The formula centres every observation at the single overall mean $\bar y$, and two different conditions hide in that centring. The sample itself must be nonconstant — if every observation were equal, the denominator would be zero and no $r_k$ would exist — but that is only a computational requirement on the data in hand. The population ACF being estimated is a separate matter: it belongs to a process whose mean does not change over time, and a level that drifts or shifts breaks that premise. A changing level does not, however, push every $r_k$ in the same direction. The four values $0,0,1,1$ contain a single level shift and no stochastic dependence at all, yet this formula gives $r_1=1/4$ and $r_2=-1/2$: the sign of the distortion depends on the lag. What trending data do show is a tendency rather than a law — the autocorrelations at small lags tend to be large and positive, because observations nearby in time are also nearby in value — not a general inflation across lags.{{cite:hyndman_athanasopoulos2021}} (§2.8, trend and seasonality in ACF plots; §9.1, differencing) So plot the series first, and diagnose a trend or a shift before deciding how to model it; only then read the sample ACF as an estimate of a population ACF.

## Interpretation
For stationary white noise with positive variance, $\rho(k)=0$ at every nonzero lag. For a stationary autoregression of order one, $X_t=\phi X_{t-1}+\varepsilon_t$ with $|\phi|<1$ and innovations uncorrelated with the past, $\rho(k)=\phi^k$ for positive $k$. Positive $\phi$ gives a geometric decay, whereas negative $\phi$ gives alternating signs. A moving average of finite order $q$ has no population autocorrelation beyond lag $q$, because observations more than $q$ steps apart have no shared innovations. These clean patterns describe population models; a finite sample ACF will rarely become exactly zero after a cutoff.{{cite:hyndman_athanasopoulos2021}} (§9.5, ACF and PACF plots)

The ACF does not say whether a lag association is direct. If $X_t$ is related to $X_{t-1}$ and $X_{t-1}$ to $X_{t-2}$, the lag-two correlation may be carried through the intervening observation. The [partial autocorrelation function](partial-autocorrelation.qmd) removes linear effects of intervening lags for that comparison. Looking at both functions helps distinguish candidate AR and MA patterns, but fitted residuals and out-of-sample behaviour must still be checked.{{cite:hyndman_athanasopoulos2021}} (§9.5, ACF and PACF plots; §9.7, modelling procedure)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Stationarity and covariance symmetry give $\gamma(-k)=\gamma(k)$, hence $\rho(-k)=\rho(k)$; $\rho(0)=1$ follows from $\gamma(0)=\operatorname{Var}(X_t)>0$. Cauchy–Schwarz gives $|\gamma(k)|\le\sqrt{\operatorname{Var}(X_t)\operatorname{Var}(X_{t-k})}=\gamma(0)$, so $|\rho(k)|\le1$.

For $X_t=\phi X_{t-1}+\varepsilon_t$ with a stationary solution and innovations uncorrelated with the past, taking covariance with $X_{t-k}$ for $k\ge1$ yields $\gamma(k)=\phi\gamma(k-1)$. Iteration gives $\rho(k)=\phi^k$. For an MA($q$), write $X_t-\mu=\sum_{j=0}^{q}\theta_j\varepsilon_{t-j}$ with mutually uncorrelated innovations. When $k>q$, the innovations in $X_t$ and $X_{t-k}$ have disjoint time indices, so their covariance, and therefore $\rho(k)$, is zero. These calculations establish the stated model patterns under their respective conditions.{{cite:hyndman_athanasopoulos2021}} (§§9.3–9.4, autoregressive and moving-average models)

For the nonlinear example below, $Y_t=\varepsilon_t\varepsilon_{t-1}$ has mean zero and unit variance. Distinct products have zero covariance because at least one independent centred normal factor appears only once. But $\mathbb E(Y_t^2Y_{t-1}^2)=\mathbb E(\varepsilon_t^2)\mathbb E(\varepsilon_{t-1}^4)\mathbb E(\varepsilon_{t-2}^2)=3$, whereas $\mathbb E(Y_t^2)\mathbb E(Y_{t-1}^2)=1$. Their squared values, and hence the observations themselves, are dependent.
:::
:::

## Statistical use — Reading a correlogram
Plot the series first, then its ACF. A large lag-one coefficient on a series with an upward trend may reflect the changing level rather than a stable stationary relation; differencing can help expose the dependence of the changes. Peaks at a seasonal period and its multiples suggest repeated calendar structure. After fitting a forecasting model, inspect the *residual* ACF for remaining serial correlation: a model may fit the level while leaving predictable patterns behind. An isolated sample spike should be judged in the context of the number of lags examined and the sample length, rather than declared a law of the process.{{cite:hyndman_athanasopoulos2021}} (§2.8; §4.2; §9.7, modelling procedure)

## Worked example
Suppose six successive readings are $4,7,5,8,6,9$. Their mean is $\bar y=13/2=6.5$, and the denominator of the sample ACF is
$$
\sum_{t=1}^{6}(y_t-\bar y)^2=35/2=17.5.
$$
At lag one the numerator is $-25/4=-6.25$, so $r_1=(-25/4)/(35/2)=-5/14\approx-0.3571$. At lag two the numerator is $9$, giving $r_2=9/(35/2)=18/35\approx0.5143$. The alternating high-low pattern is reflected by a negative adjacent association and a positive two-step association. The readings also rise overall, so six points are too few to treat these descriptive values as proof of a stationary seasonal process.{{cite:hyndman_athanasopoulos2021}} (§2.8, sample ACF and seasonality)

**Your turn.** Using the same six readings and the same denominator, calculate the lag-three sample autocorrelation. Would a value at this one lag establish a population three-step cycle?

::: {.callout-tip collapse="true" title="Answer"}
The lag-three numerator is $(8-6.5)(4-6.5)+(6-6.5)(7-6.5)+(9-6.5)(5-6.5)=-31/4$. Therefore $r_3=(-31/4)/(35/2)=-31/70\approx-0.4429$. This is one descriptive coefficient from only three lagged pairs; it does not establish a population cycle.
:::

## Common misconceptions
Autocorrelation is not a correlation between two different variables; it compares one series at different times. A small sample $r_k$ is not proof that the population $\rho(k)$ is zero, and an apparently sharp cutoff is not by itself proof of an MA order. A large positive ACF in levels does not necessarily mean a stable AR process: a deterministic trend can produce a similar plot. Zero autocorrelation is also weaker than independence; nonlinear functions of consecutive observations can remain dependent while every nonzero-lag covariance vanishes.{{cite:hyndman_athanasopoulos2021}} (§2.8, trend; §9.5, order identification from ACF and PACF plots)

## Assumptions and limits — What an ACF can miss
For a random walk, the variance changes with time, so one population $\rho(k)$ defined through a constant $\gamma(0)$ is not available even though a plotted sample ACF may decay slowly. If a series jumps from one constant level to another, its long run of similar values around each level can also create sample autocorrelation without a stationary mechanism. Conversely, let $\varepsilon_t$ be independent standard normal variables and $Y_t=\varepsilon_t\varepsilon_{t-1}$. The $Y_t$ have zero autocovariance at every nonzero lag, yet adjacent squared values share $\varepsilon_{t-1}^2$ and are dependent. An ACF is therefore a diagnostic of linear serial association under an appropriate process model, not a complete map of dependence.{{cite:hyndman_athanasopoulos2021}} (§2.8, interpretation; §9.1, non-stationarity and differencing)

## Connections
[Weak stationarity](weak-stationarity.qmd) is what makes the population ACF a function of lag alone. [White noise](white-noise.qmd) has zero nonzero-lag autocorrelation, while [autoregression and moving averages](autoregression-and-moving-averages.qmd) create characteristic population patterns. [Partial autocorrelation](partial-autocorrelation.qmd) asks what remains after the intervening linear lags are accounted for. [Effective sample size](effective-sample-size.qmd) uses serial correlation to explain why many closely related observations can carry less information than the same number of independent ones.{{cite:hyndman_athanasopoulos2021}} (§2.8; §§9.1–9.5)

## History
The study of correlation across a series grew with early twentieth-century attempts to understand apparent cycles in observed processes. George Udny Yule's work in the 1920s and 1930s developed autocorrelation, partial autocorrelation, the correlogram and autoregressive processes. The autocorrelation function still serves that diagnostic purpose, now serving both model identification and residual checking in forecasting.{{cite:dodge2008}} (p. 24, “Autocorrelation”){{cite:hyndman_athanasopoulos2021}} (§2.8; §§9.1–9.5)
