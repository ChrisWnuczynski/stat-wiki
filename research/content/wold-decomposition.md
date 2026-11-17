## Motivating example
A stationary series may contain short-term random disturbances as well as a component predictable from arbitrarily remote history. A noisy measurement of a random-phase harmonic illustrates both: the harmonic evolves by a deterministic recurrence, while each new noise term contributes an unpredictable innovation. Orthogonal projection separates these forms of linear predictability.{{cite:horak_muller_vrbova1987}} (§1, pp. 337–339)

## Statement
[]{#property-representation}

For a zero-mean covariance-stationary series, let $H_{t-1}$ be the closed linear span in $L^2$ of its observations up to time $t-1$. The innovation is $\varepsilon_t=X_t-\operatorname{proj}_{H_{t-1}}X_t$. When its variance is positive, the Wold representation takes the form
$$
X_t=\sum_{j=0}^{\infty}a_j\varepsilon_{t-j}+\nu_t,
\qquad a_0=1,\quad\sum_{j\ge0}a_j^2<\infty.
$$
The series converges in mean square. Innovations are uncorrelated across time and orthogonal to the deterministic component. Here deterministic means linearly predictable from the entire past, rather than a nonrandom constant. A purely deterministic series has zero innovation variance and consists entirely of the predictable component.{{cite:horak_muller_vrbova1987}} (§1, pp. 337–339)

## Intuition — New information and the remote past
Prediction errors from orthogonal projection are orthogonal to earlier observations. Earlier innovations are themselves linear combinations or mean-square limits of those observations, so successive innovations are uncorrelated. Orthogonality describes second moments; it does not by itself imply independent innovations or normally distributed observations.{{cite:horak_muller_vrbova1987}} (§1, pp. 338–339)

A linear moving-average representation characterises second-order structure without identifying a unique physical mechanism for a series. Covariance patterns alone do not establish that a measured system has linear internal dynamics.{{cite:scargle2020_wold}} (§§3.1 and 4)

## Key results — Forecast uncertainty from the innovation coefficients
For the purely nondeterministic component, suppose innovations through time $T$ are available from the infinite observation history. Its $h$-step linear prediction error is
$$
\sum_{j=0}^{h-1}a_j\varepsilon_{T+h-j}.
$$
Uncorrelatedness gives error variance $\sigma^2\sum_{j=0}^{h-1}a_j^2$. This calculation explains why long-horizon uncertainty approaches the variance of the nondeterministic component when the coefficients are square summable. The predictable component contributes no error under the stated information set.{{cite:scargle2020_wold}} (§4, moving-average representation)

## Worked example — One lag of memory
Let $X_t=\varepsilon_t+0.4\varepsilon_{t-1}$, with innovation variance $4$. Then $\operatorname{Var}(X_t)=4(1+0.4^2)=4.64$, lag-one covariance is $4(0.4)=1.6$, and lag-one correlation is $1.6/4.64=0.34483$. All larger-lag covariances vanish. These quantities follow by expanding the products and dropping cross-products of uncorrelated innovations.{{cite:scargle2020_wold}} (§4)

If the latest innovation is $\varepsilon_T=5$, the one-step forecast is $2$, with error variance $4$. The two-step forecast is zero, with error variance $4.64$. A separate random-phase harmonic of period $12$ obeys $\nu_t=2\cos(2\pi/12)\nu_{t-1}-\nu_{t-2}$ and illustrates the predictable component when its sine and cosine amplitudes have equal variance and zero covariance.{{cite:horak_muller_vrbova1987}} (§1, stationary processes and orthogonal decomposition)

**Your turn.** Replace the coefficient $0.4$ by $0$ in the moving average. What are its variance, lag-one correlation and one-step forecast?

::: {.callout-tip collapse="true" title="Answer"}
The series is the innovation sequence itself. Its variance is $4$, lag-one correlation is zero, and its linear forecast from the past is zero.
:::
