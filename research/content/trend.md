## Motivating example
An organisation's monthly total can rise even when each January is below the previous December. The long-term direction and the repeating calendar pattern answer different questions. A trend describes movement in the underlying level over an extended interval and need not follow a straight line.{{cite:dodge2008}} (p. 480)

## Definition — Movement in the level over time
A trend is a sustained change in the level of a time series on the time scale of interest. It can increase, decrease or change direction. Whether a movement looks like a trend depends partly on the length of the observation window: one portion of a long cycle can appear to have a persistent direction.{{cite:hyndman_athanasopoulos2021}} (§2.3)

One description separates $Y_t=T_t+S_t+R_t$. Here $T_t$ is the smoother trend-cycle component; subtracting $S_t$ alone gives seasonally adjusted data, which still contain the remainder. Thus seasonal adjustment and trend estimation are distinct operations.{{cite:hyndman_athanasopoulos2021}} (§3.2)

## Properties — Detrending and differencing answer different questions
For the deterministic trend model $Y_t=a+bt+\varepsilon_t$, subtracting $a+bt$ leaves $\varepsilon_t$. First differencing instead gives $Y_t-Y_{t-1}=b+\varepsilon_t-\varepsilon_{t-1}$. Even independent errors become dependent after differencing: consecutive differences share one error with opposite signs. The choice of transformation therefore affects the stochastic model.{{cite:hyndman_athanasopoulos2021}} (§9.1)

For a random walk with drift, $Y_t=Y_{t-1}+b+\varepsilon_t$, a difference gives $b+\varepsilon_t$. Subtracting a fitted straight line does not remove accumulated random shocks in this model. A smooth-looking path therefore does not establish whether deterministic detrending or differencing is appropriate.{{cite:hyndman_athanasopoulos2021}} (§9.1)

## Worked example — A fitted line and its differences
For times $t=1,2,3,4,5$, let the observed values be $(3,5,7,9,11)$. The least-squares trend is $\widehat T_t=1+2t$. All detrended values are zero, while all first differences are $2$. Both computations express the same straight-line movement, but on different scales. Estimating a linear secular trend by least squares fits the intercept and slope to all observations simultaneously.{{cite:dodge2008}} (p. 480)

Now suppose independent noise with variance $4$ is added to that trend. Subtracting the known trend leaves variance $4$. Differencing gives noise variance $8$ and covariance $-4$ between consecutive differences, hence lag-one correlation $-1/2$. The negative correlation is introduced by the transformation; it does not require a negative relationship between consecutive measurement errors.{{cite:hyndman_athanasopoulos2021}} (§9.1)

**Your turn.** What is the lag-$4$ difference of the trend $1+2t$? Does it have a trend?

::: {.callout-tip collapse="true" title="Answer"}
It is $(1+2t)-[1+2(t-4)]=8$ at every eligible time. It is constant, so its straight-line slope is zero.
:::
