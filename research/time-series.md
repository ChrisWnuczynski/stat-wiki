# Time series

Type: Concept. Rank 220. Tier: full.

## Material checked

- **Checked:** Baseline 506 words and no figures. The source note on one ordered stretch and the autoregressive variance factor stays in the generated page. The added example uses a different coefficient, $\phi=1/2$, and an exact factor at $T=4$.
- **Checked:** Hyndman and Athanasopoulos, *Forecasting: Principles and Practice*, 3rd edition, §1.1 (exchange-rate forecasts that move the rate), §2.1 (a series is observations plus a time index; the yearly list $123,39,78,52,110$), §9.1 (stationarity, white noise, differencing, random-walk forecast equal to the last observation) and §9.3 (AR(1), the condition $-1<\phi<1$, and the white-noise and random-walk boundaries).
- **Checked:** Dodge printed p. 536: a series is observations at successive times; the four components are trend, seasonal variation, cyclical fluctuation and irregular variation; Persons (1919) is credited with that split.
- **Checked by code:** mean $80.4$; lag-$1$ correlations $-0.4671$ and $0.4665$; $\gamma_0=4/3$; exact mean variance $0.6875$; multiplier $2.0625$; random-walk path $1,0,0,2$; difference correlation $-1/2$.
- **Assumed:** White noise in the variance proof means mean zero, constant variance, and no correlation with the current state or across time. Hyndman's figure captions use normal white noise; the covariance algebra does not need normality.
- **Disputed:** Nothing. Dodge's four-component description and Hyndman's autocorrelation account are different organisations of the same subject, and both are reported.

## Sources opened and used

1. Rob J. Hyndman and George Athanasopoulos, *Forecasting: Principles and Practice*, 3rd ed., OTexts, 2021, §§1.1, 2.1, 9.1 and 9.3, `https://otexts.com/fpp3/`. Existing key `hyndman_athanasopoulos2021`.
2. Yadolah Dodge, *The Concise Encyclopedia of Statistics*, 2008, printed p. 536. Existing key `dodge2008`.

## Skipped

The Google-stock KPSS statistics printed in §9.1 were not copied, because the underlying series was not recomputed. The large-sample mean-variance factor $(1+\phi)/(1-\phi)$ is derived in the proof for the AR(1); the source note's numerical case $\phi=0.9$ was left as it stands.
