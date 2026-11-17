## Motivating example

A sequence of daily demand measurements fluctuates around a stable level and remains similarly variable throughout the year after seasonal effects have been removed. In that setting, observations a week apart can be compared using the same lagged covariance as any other pair a week apart. Weak stationarity formalizes this repeatability of first and second moments, making one autocorrelation function meaningful across time.

## Intuition — Why stable moments matter

The series itself changes from day to day. Weak stationarity says that its mean and pairwise covariance do not change when the calendar origin is shifted. The covariance may depend on how far apart two observations are, but not on whether the pair occurred in January or October. This assumption reduces a separate mean at every date and a separate covariance for every pair to one mean and one function of lag. It is a useful modelling economy. Even so, observed segments can look quite different.

A trend violates constant mean; changing volatility violates constant variance even when the mean remains level. Seasonality in the mean also breaks weak stationarity unless the seasonal component is removed or modelled explicitly. Classical time-series descriptions have long separated trend and seasonal components. Persons's 1919 decomposition used trend, cyclical, seasonal and irregular parts. {{cite:dodge2008}} (p. 536, “Time Series”)

## Definition

A real-valued process $(X_t)$ is weakly stationary when each $X_t$ has a finite second moment, $\mathbb E X_t=\mu$ does not depend on $t$, and $\operatorname{Cov}(X_t,X_s)=\gamma(t-s)$ depends only on the lag. In particular $\gamma(0)=\operatorname{Var}(X_t)$ is constant, $\gamma(-h)=\gamma(h)$ for real-valued series, and $\rho(h)=\gamma(h)/\gamma(0)$ is the autocorrelation when $\gamma(0)>0$.

Strict stationarity is stronger in general: it requires every finite-dimensional joint distribution to be unchanged by a common time shift. Strict stationarity plus finite second moments implies weak stationarity. For a Gaussian process, the mean and covariance determine every finite-dimensional distribution, so weak stationarity also implies strict stationarity. The finite-second-moment condition cannot be skipped merely because a series looks stable in a plot.

## Properties

For any weakly stationary series, $|\gamma(h)|\leq\gamma(0)$ by Cauchy–Schwarz, so autocorrelations lie between $-1$ and $1$. The variance of a difference is $\operatorname{Var}(X_t-X_{t-h})=2\{\gamma(0)-\gamma(h)\}$. A positive autocovariance makes nearby values move together and reduces the variation of their difference; a negative one has the opposite effect.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Time-shift invariance of all joint distributions, with finite second moments, makes each one-time mean and each two-time covariance invariant under a common shift, proving strict implies weak. For a real weakly stationary process, covariance symmetry gives $\gamma(-h)=\gamma(h)$, and Cauchy–Schwarz gives $|\gamma(h)|\leq\sqrt{\operatorname{Var}(X_t)\operatorname{Var}(X_{t-h})}=\gamma(0)$. Expanding the variance of $X_t-X_{t-h}$ gives two copies of $\gamma(0)$ minus twice $\gamma(h)$. For a stationary AR(1) solution $X_t=\sum_{j=0}^{\infty}\phi^j\varepsilon_{t-j}$ with $|\phi|<1$ and independent mean-zero innovations of variance $\sigma_\varepsilon^2$, independence gives $\gamma(0)=\sigma_\varepsilon^2\sum_{j\geq0}\phi^{2j}=\sigma_\varepsilon^2/(1-\phi^2)$ and $\gamma(h)=\phi^{|h|}\gamma(0)$. Finally, independent alternating variables that have mean zero and variance one but different even- and odd-time laws have $\gamma(h)=0$ for nonzero lag yet fail strict stationarity; the construction in Interpretation supplies explicit laws.
:::
:::

## Interpretation

Weak stationarity does not force identical marginal distributions outside Gaussian models. For example, let independent even-time observations equal $-1$ or $1$ with equal probability, while odd-time observations equal $-\sqrt2,0,\sqrt2$ with probabilities $1/4,1/2,1/4$. All means are zero, all variances are one, and nonzero-lag covariances are zero, so the process is weakly stationary. Its one-time distribution changes with parity, so it is not strictly stationary. This counterexample shows exactly what the first two moments leave unidentified.

For an AR(1) with $|\phi|<1$, a stationary solution has autocovariance $\gamma(h)=\phi^{|h|}\sigma_\varepsilon^2/(1-\phi^2)$. The coefficient's sign and magnitude govern how quickly lagged information fades, while the innovation variance sets overall scale. An arbitrary initial value need not place the process in its stationary law immediately, even if $|\phi|<1$; transient startup behaviour then changes its early variances.

## Statistical use

Inspect a time plot for trend, seasonality and changing volatility before estimating a single mean and autocorrelation function. A roughly stable plot is evidence to investigate, not a mathematical proof. Differences or a model for trend and seasonality can sometimes produce a weakly stationary residual series. When modelling forecast uncertainty, use the covariance structure only over periods where its stability is defensible. Structural breaks or changing measurement rules can make historical lags poor guides to future dependence.

A random walk started at zero with independent innovations of variance $4$ has $\operatorname{Var}(X_t)=4t$, so it is not weakly stationary even though each increment has a stable distribution. A process with a stable mean but volatility that doubles after a policy change also fails constant $\gamma(0)$. Independent Cauchy observations may be strictly stationary, yet lack finite second moments and therefore are not weakly stationary under this definition. These cases separate drift, variance change and moment nonexistence.
## Worked example

Let $X_t=0.6X_{t-1}+\varepsilon_t$ be in its stationary regime, with independent innovations of mean zero and variance $4$. Then $\gamma(0)=4/(1-0.6^2)=6.25$, $\gamma(1)=0.6(6.25)=3.75$, and $\gamma(2)=0.6^2(6.25)=2.25$. The corresponding autocorrelations are $\rho(1)=0.6$ and $\rho(2)=0.36$. The variance of a one-step difference is $2(6.25-3.75)=5$. These values are the same at every time origin under the stationary model.

**Your turn.** A stationary AR(1) has coefficient $-0.5$ and independent innovations with variance $3$. Find $\gamma(0)$, $\gamma(1)$, $\gamma(2)$ and $\rho(2)$. What does the negative first-lag covariance suggest about successive deviations?

::: {.callout-tip collapse="true" title="Answer"}
The variance is $\gamma(0)=3/(1-(-0.5)^2)=4$. Thus $\gamma(1)=-0.5(4)=-2$, $\gamma(2)=(-0.5)^2(4)=1$, and $\rho(2)=1/4=0.25$. A positive deviation tends to be followed by a negative one under this linear model, though innovations prevent a deterministic alternation.
:::

## Common misconceptions

Weak stationarity does not mean the observed series is constant, only that its first two moments are time-invariant in the specified way. Constant mean and variance alone are insufficient if covariance at a fixed lag changes over time. Weak and strict stationarity are not equivalent for arbitrary non-Gaussian processes, as the alternating example shows. Finally, a stable-looking finite plot cannot establish the required population moment conditions.

## Connections

The [autocorrelation function](autocorrelation-function.qmd) is normalized from the stationary covariance function. [Stationarity of a time series](stationarity-of-a-time-series.qmd) compares weak and strict forms more broadly, while [autoregression and moving averages](autoregression-and-moving-averages.qmd) give common models with stationary parameter regimes. A [random walk](../notes/sp-03-random-walks.qmd) illustrates how constant increment behaviour can coexist with a nonstationary level.{{cite:dodge2008}} (p. 536, trend and irregular components)

## History

Time-series descriptions have long used trend, seasonal and cyclical decomposition, and Persons gave a four-part decomposition in 1919.{{cite:dodge2008}} (p. 536, “Time Series”) Weak stationarity takes a different mathematical route to repeatability: after systematic changes are accounted for, it asks that the remaining mean and lag covariance remain stable over time.
