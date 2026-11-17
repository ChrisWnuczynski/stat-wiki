## Motivating example
Soil measurements close together may resemble one another more than measurements far apart. A variogram describes variability of differences at a given separation. Unlike a map of observed levels, it summarises a relation between pairs. The spatial separation, direction and measurement process all matter when deciding which pairs should be compared. Spatial analysis expressly accounts for dependence associated with location.{{cite:dodge2008}} (p. 501, Spatial Statistics)

## Definition — Make the factor of two explicit
Assume a constant mean and that increment variance depends only on displacement $h$, rather than the base location $t$. Define the variogram as
$$V(h)=\operatorname{Var}\{X(t+h)-X(t)\}.$$
The semivariogram is $\gamma(h)=V(h)/2$. Some geostatistical usage calls $\gamma$ the variogram. Therefore compare formulas before comparing numerical values. Under zero-mean increments, variance of an increment also equals its expected squared value. With a nonzero mean increment, the expected squared increment includes an additional squared-mean term.{{cite:maelicke2022_variogram}} (§3.1, variogram terminology and estimator)

## Properties — Covariance and increment variability
If a process is weakly stationary with variance $C(0)$ and covariance $C(h)$, expansion gives
$$V(h)=C(0)+C(0)-2C(h).$$
No independence assumption is needed for this identity. If $C(h)$ tends to zero as lag grows, $V(h)$ tends to $2C(0)$. That limiting behaviour follows from the additional covariance-decay condition, rather than stationarity alone. A stationary process with persistent or oscillating covariance need not have a monotone variogram or that particular long-lag plateau. This distinction matters when using a fitted spatial covariance model.{{cite:maelicke2022_variogram}} (§§3.1–3.3, variogram modelling and directional dependence)

Increment stationarity is weaker than stationarity of the levels. A random walk with uncorrelated zero-mean innovations of variance $\sigma^2$ has $V(h)=|h|\sigma^2$, even though its level variance depends on time. Its increments over a fixed lag have a stable variance. Thus a useful variogram can exist without a stationary covariance function for the levels. Pair comparisons require a model for how increment behaviour repeats across the domain.{{cite:dodge2008}} (p. 501, spatial dependence and modelling context)

## Worked example — Empirical pair differences
At equally spaced locations $0,1,2,3$, suppose observations are $1,2,4,3$. At lag one the squared pair differences are $1,4,1$. Their average is two, so the empirical semivariance is one. At lag two the squared differences are nine and one. Their average is five, so the empirical semivariance is $2.5$. At lag three there is one squared difference, four, and semivariance two. The empirical values need not increase at every lag, and estimates at different lags have different numbers of contributing pairs.{{cite:maelicke2022_variogram}} (§3.1, empirical variogram and lag classes)

For a model example, let a stationary AR(1) process have coefficient $0.5$ and variance four. Its lag-one covariance is two, giving $V(1)=4$. Its semivariogram is $\gamma(1)=2$, and its variogram approaches eight as its covariance decays. The factor-of-two convention changes these numerical values while leaving the model unchanged.

**Your turn.** A random walk has innovation variance three. Find its variogram and semivariogram at lag four.

::: {.callout-tip collapse="true" title="Answer"}
The increment sums four uncorrelated innovations. Its variance is $4\times3=12$, and its semivariance is six.
:::

## Statistical use — Binning and direction are modelling choices
Irregularly located observations rarely give many pairs at exactly the same separation. Empirical spatial variograms therefore group pairs into lag classes, and directional versions also restrict orientation. Bin boundaries, sparse distant pairs and anisotropy can change the estimate. A fitted smooth model is a further step beyond calculating empirical pair differences. Those choices affect interpolation because the resulting dependence model determines its weights.{{cite:maelicke2022_variogram}} (§§3.1–3.3)

## Assumptions and limits — A plateau does not establish stationarity
A flat empirical curve can arise from limited separation, noise or a poor binning choice. A visible trend in the levels can contribute deterministic mean differences to a squared-increment calculation. Inspect the spatial setting and the mean structure alongside the variogram. Distinguishing a model's assumptions from a finite plot prevents a descriptive pair summary from being treated as proof of stationary levels.{{cite:dodge2008}} (p. 501); {{cite:maelicke2022_variogram}} (§3.1)

## Interpretation — The factor of one half is the only difference between the two names
If the variance of an increment is $10$, the semivariogram is $5$ and the variogram in the variance convention is $10$. Halving is the whole conversion. For a weakly stationary process with variance $9$ and lag-two covariance $4$, the expansion $V(h)=2(C(0)-C(h))$ gives $V(2)=2(9-4)=10$, so the semivariogram is $5$. No independence assumption entered that expansion: it is the variance of a difference of two random variables with equal variance and covariance $C(h)$. A random walk with uncorrelated innovations of variance $1$ has increment variance equal to the lag. At lag $10$ the variogram is $10$ and the semivariogram is $5$. The level variance of the walk still grows with time. The variogram can be stable while the levels are not.{{cite:maelicke2022_variogram}} (§3.1, variogram terminology and estimator){{cite:dodge2008}} (p. 501, spatial dependence and modelling context)

The stationary AR(1) illustration has variance $4$ and lag-one covariance $2$, so $V(1)=4$ and $\gamma(1)=2$. If the covariance decays to zero, $V(h)$ approaches $8$, twice the level variance. A covariance that oscillates need not produce a monotone approach to that plateau. The identity $V(h)=2(C(0)-C(h))$ remains available at every lag for which the stationary covariance exists. It does not by itself force $C(h)$ to decay.{{cite:maelicke2022_variogram}} (§§3.1–3.3, variogram modelling and directional dependence)

### Worked example — Pair counts fall as the lag grows
The series $1,2,4,3$ has lag-one squared differences $1,4,1$, average $2$, and empirical semivariance $1$. Lag two has squared differences $9$ and $1$, average $5$, semivariance $2.5$. Lag three has one squared difference, $4$, and semivariance $2$. The empirical semivariogram is not monotone: it falls from $2.5$ to $2$ at the longest lag, where a single pair determines the value. An estimator that bins several separations together can hide or create that dip, depending on the bin edges. Directional bins add a further restriction, and a pair that is far apart along one axis and close along another may leave the bin.{{cite:maelicke2022_variogram}} (§3.1, empirical variogram and lag classes)

## Connections
A time-series autocovariance $C(h)$ and a spatial covariance are the same second-moment object when the displacement is a scalar lag. The variogram rewrites that object as an increment variance. A [random walk with drift](random-walk-with-drift.qmd), when the innovations are uncorrelated and have constant variance, is the nonstationary example whose variogram is linear in the lag and whose level variance is not constant. Fitting a covariance model with a finite plateau to that walk describes a different process.{{cite:dodge2008}} (p. 501, Spatial Statistics){{cite:maelicke2022_variogram}} (§§3.1–3.3)
