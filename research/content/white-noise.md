## Lead context
White noise is a sequence of uncorrelated shocks with mean zero and one common variance, so a linear forecast that uses only the past of the sequence has nothing to add.{{cite:hyndman_athanasopoulos2021}} (§9.3, the white-noise boundary of an autoregression){{cite:dodge2008}} (p. 20, weak white noise)

## Motivating example
A stationary autoregression with coefficient zero is the innovation sequence itself. Hyndman and Athanasopoulos take that boundary as white noise, and their simulated paths use a normal version with mean zero and variance one. The one-step linear forecast is then zero at every time, and the forecast-error variance stays equal to the innovation variance. There is no carry-over to estimate.{{cite:hyndman_athanasopoulos2021}} (§9.1, white noise is stationary; §9.3, $\phi_1=0$ and a normal innovation of variance one)

## Intuition
Uncorrelated means each lag covariance is zero. It does not mean that a nonlinear function of the past is useless, and it does not mean the variables are independent. One description of white noise asks for mutually independent and identically distributed terms, and the ARMA equation also uses a weak white noise. The weak version is the second-moment definition. The independent version is stronger, and for jointly normal variables the two agree.{{cite:dodge2008}} (p. 20, independent white noise and weak white noise)

## Definition
A weak white noise is a sequence $\varepsilon_t$ with $\mathbb E(\varepsilon_t)=0$, $\operatorname{Var}(\varepsilon_t)=\sigma^2$ finite and constant, and $\operatorname{Cov}(\varepsilon_t,\varepsilon_{t-h})=0$ for every lag $h\neq 0$. The autocovariance is a spike of height $\sigma^2$ at lag zero. An independent white noise has independent identically distributed terms, which implies the weak properties when the variance is finite. A normal white noise is the independent case, because uncorrelated jointly normal variables are independent.{{cite:dodge2008}} (p. 20){{cite:hyndman_athanasopoulos2021}} (§9.3, normally distributed white noise)

## Interpretation
The sample mean of $T$ weak-white-noise terms has variance $\sigma^2/T$. There is no extra factor from lagged covariance, because those covariances are zero. A series with positive autocorrelation does not get this variance. Differencing a white noise does not preserve it. If $D_t=\varepsilon_t-\varepsilon_{t-1}$, then $\operatorname{Var}(D_t)=2\sigma^2$ and $\operatorname{Cov}(D_t,D_{t-1})=-\sigma^2$, so the lag-$1$ correlation is $-1/2$. The shocks were uncorrelated. The differences are a moving average.{{cite:hyndman_athanasopoulos2021}} (§9.1, over-differencing)

## Properties
The best linear predictor of $\varepsilon_{t}$ given the earlier terms is $0$, and the mean squared error of that predictor is $\sigma^2$. Any linear combination of the past has covariance zero with $\varepsilon_t$, so it cannot reduce the mean squared error below the marginal variance. A nonlinear function can do better when the noise is only weak. Let $Z$ be standard normal and set $U=Z$ and $V=Z^2-1$. Then $\mathbb E(U)=\mathbb E(V)=0$, $\mathbb E(UV)=\mathbb E(Z^3)-\mathbb E(Z)=0$, and $\operatorname{Var}(V)=2$. The pair is uncorrelated. It is not independent: if $U=0$, then $V=-1$ with probability one.{{cite:dodge2008}} (p. 20, the gap between the independent phrase and weak white noise)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a standard normal $Z$, symmetry gives $\mathbb E(Z)=\mathbb E(Z^3)=0$, so $\mathbb E\bigl(Z(Z^2-1)\bigr)=0$. Also $\mathbb E(Z^2-1)=0$. Integration by parts on the standard normal density gives $\mathbb E(Z^4)=3\mathbb E(Z^2)=3$, so $\mathbb E(Z^2-1)^2=3-1=2$. Thus $U$ and $V$ are uncorrelated, mean zero, with variances $1$ and $2$. The conditional law of $V$ given $U=0$ is a point mass at $-1$, which is not the marginal law of $V$. Uncorrelated does not imply independent.{{cite:dodge2008}} (p. 20, weak white noise)

For the difference, expand $\operatorname{Cov}(\varepsilon_t-\varepsilon_{t-1},\varepsilon_{t-1}-\varepsilon_{t-2})=-\operatorname{Var}(\varepsilon_{t-1})=-\sigma^2$ when distinct times are uncorrelated, and $\operatorname{Var}(\varepsilon_t-\varepsilon_{t-1})=2\sigma^2$. The correlation is $-\sigma^2/(2\sigma^2)=-1/2$.{{cite:hyndman_athanasopoulos2021}} (§9.1, differences of a series)
:::
:::

## Statistical use — What a residual check can see
Residual autocorrelation is a check against weak white noise. A lag that is large compared with the null fluctuation of an uncorrelated series is evidence that a linear function of the past still predicts. A lag inside that fluctuation does not prove independence. The pair $(Z,Z^2-1)$ would pass a correlation check and fail a check that looks at $V$ given $U$. Volatility clustering is that second failure along a sequence: squares can be dependent while the series itself is weak white noise.{{cite:dodge2008}} (p. 20){{cite:hyndman_athanasopoulos2021}} (§9.3, innovation white noise)

The variance formula $\sigma^2/T$ uses a common finite variance and zero lag covariances. Infinite variance, as in a stable law with no second moment, is not weak white noise. A mean that drifts is not white noise either: Hyndman and Athanasopoulos require the white-noise boundary of the autoregression to have no constant and coefficient zero. Adding a nonzero mean produces a sequence of uncorrelated variables that is not centred, and the forecast of the next term is that mean rather than zero.{{cite:hyndman_athanasopoulos2021}} (§9.3, $c=0$ and $\phi_1=0$){{cite:dodge2008}} (p. 20)

## Worked example
Let $\sigma^2=4$ and $T=4$. The variance of the sample mean of a weak white noise is $4/4=1$, so the standard error is $1$. Four independent draws with variance $4$ are the same calculation, because uncorrelated mean-zero variables with equal variance have the same mean variance as independent ones. The difference series has variance $8$ and lag-$1$ correlation $-1/2$. A residual check that differences a series which was already white noise will see that spurious correlation of $-1/2$.{{cite:hyndman_athanasopoulos2021}} (§9.1, white noise and differencing)

For the pair, $\operatorname{Var}(Z^2-1)=2$ and the covariance with $Z$ is $0$. Observing $Z=0$ tells you $Z^2-1=-1$ exactly. The correlation, which is zero, did not carry that information.{{cite:dodge2008}} (p. 20, weak white noise)

**Your turn.** A weak white noise has variance $9$. What is the variance of the mean of $9$ terms, and what is the lag-$1$ correlation of its first differences?

::: {.callout-tip collapse="true" title="Answer"}
The mean has variance $9/9=1$. The differences have lag-$1$ correlation $-1/2$, whatever the variance is, because $\sigma^2$ cancels in the ratio.
:::

## Common misconceptions
White noise is not a statement that the histogram is bell-shaped. The weak definition constrains means, variances and lag covariances. A normal white noise adds joint normality, which is what upgrades uncorrelated to independent.{{cite:hyndman_athanasopoulos2021}} (§9.3, the normal paths in the figures){{cite:dodge2008}} (p. 20)

A flat autocorrelation plot is not a proof of independence. The pair $Z$ and $Z^2-1$ has correlation zero and is a function of one variable.{{cite:dodge2008}} (p. 20, weak versus independent)

Differencing is not a harmless tidy-up. Applied to white noise it manufactures correlation $-1/2$.{{cite:hyndman_athanasopoulos2021}} (§9.1, do not over-difference)

## Connections
[Time series](time-series.qmd) models are built by passing white noise through an autoregression or a moving average. [Weak stationarity](weak-stationarity.qmd) is automatic for weak white noise, because the mean and the lag covariances do not depend on time. A [random walk](unit-root.qmd) is the partial sum of white noise, and it is not white noise: its variance grows with time.{{cite:hyndman_athanasopoulos2021}} (§9.1, random walk; §9.3, white noise)

## Check yourself

1. If $Z$ is standard normal, what is $\operatorname{Cov}(Z,Z^2-1)$?

::: {.callout-tip collapse="true" title="Answer"}
Zero. $\mathbb E(Z^3)=\mathbb E(Z)=0$, so the covariance is zero. The variables are still dependent, because $Z=0$ forces $Z^2-1=-1$.
:::

2. A white noise of variance $4$ is differenced. What is the lag-$1$ correlation of the differences?

::: {.callout-tip collapse="true" title="Answer"}
$-1/2$. The variance $4$ cancels: the lag covariance is $-4$ and the difference variance is $8$.
:::

3. Is an AR(1) with coefficient $0$ and constant $0$ white noise?

::: {.callout-tip collapse="true" title="Answer"}
Yes. That boundary is the innovation sequence. A coefficient $1$ is a random walk instead, and is not white noise.
:::

## History
An ARMA moving-average piece is a combination of a white noise. One parenthetical definition asks for mutually independent and identically distributed variables, and the combined ARMA equation is also written with a weak white noise. Hyndman and Athanasopoulos use white noise as the stationary innovation of an autoregression, with normal mean-zero variance-one paths in their figures, and they single out coefficient zero and constant zero as the white-noise model itself.{{cite:dodge2008}} (p. 20){{cite:hyndman_athanasopoulos2021}} (§9.1, §9.3)
