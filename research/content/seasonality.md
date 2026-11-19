## Motivating example
A shop sells more in the same quarter of each year. Comparing consecutive quarters mixes the recurring quarterly effect with growth in the shop's overall business. Comparing the same quarter across years can help separate those two patterns. Seasonal variation refers to recurrence associated with a calendar or other fixed observation period.{{cite:dodge2008}} (p. 479)

## Definition — Repetition tied to an observation period
A seasonal pattern repeats at a known period: quarterly observations can have annual period $4$, and monthly observations annual period $12$. Data collected more frequently can contain multiple seasonal periods, such as daily and weekly patterns in hourly demand. A cycle whose length varies does not have the same fixed-period structure.{{cite:hyndman_athanasopoulos2021}} (§§2.1 and 2.3)

An additive description is $Y_t=T_t+S_t+R_t$, with trend-cycle $T_t$, seasonal component $S_t$ and remainder $R_t$. A multiplicative description uses $Y_t=T_tS_tR_t$ when seasonal amplitude scales with the level and the observations permit that representation. These are modelling descriptions, rather than unique decompositions of arbitrary data.{{cite:hyndman_athanasopoulos2021}} (§3.2)

## Interpretation — What seasonal differencing removes
The lag-$m$ seasonal difference is $(1-B^m)Y_t=Y_t-Y_{t-m}$. If $S_t=S_{t-m}$ exactly, this operation cancels $S_t$. It does not necessarily remove changing seasonal effects, and it adds the two remainder terms as $R_t-R_{t-m}$. Differencing therefore changes the noise structure as well as removing a periodic mean.{{cite:hyndman_athanasopoulos2021}} (§9.1)

For a linear trend $a+bt$, the seasonal difference is $mb$, a constant. For a harmonic with period $m$, both sine and cosine terms cancel exactly. An ordinary first difference generally leaves that periodic pattern, because adjacent seasonal positions need not have the same effect. These identities explain the different roles of ordinary and seasonal differencing.{{cite:hyndman_athanasopoulos2021}} (§9.1)

## Worked example — Quarterly effects and annual growth
Consider two years of quarterly values:
$$
(80,100,120,100),\qquad(90,110,130,110).
$$
Their year means are $100$ and $110$. Subtracting each year's mean gives the same quarterly effects $(-20,0,20,0)$ in both years. The average of each quarterly position across years is $(85,105,125,105)$; subtracting their overall mean $105$ gives those same effects. Normalising the seasonal effects to sum to zero separates the annual level from seasonal offsets.{{cite:hyndman_athanasopoulos2021}} (§3.4)

The lag-$4$ differences are $(10,10,10,10)$: each quarter has grown by the same amount. The within-year changes $20,20,-20$ still depend on seasonal position. A large change between adjacent quarters therefore need not indicate a change in the annual growth rate.

**Your turn.** A third year is $(100,120,140,120)$. Find the seasonal differences and the sum of its mean-adjusted quarterly values.

::: {.callout-tip collapse="true" title="Answer"}
Subtracting the second year gives $(10,10,10,10)$. The third-year mean is $120$, giving offsets $(-20,0,20,0)$, whose sum is zero.
:::

## Connections — Seasonal patterns and serial dependence
Autocorrelations at multiples of the seasonal lag can reveal a repeating pattern. They do not by themselves identify its cause or establish a seasonal unit root. A seasonal plot aligns observations by their position within a period, while a subseries plot follows one seasonal position over successive periods. Both help distinguish changing seasonal amplitude from changes in the overall level.{{cite:hyndman_athanasopoulos2021}} (§§2.4–2.5 and 2.8)
