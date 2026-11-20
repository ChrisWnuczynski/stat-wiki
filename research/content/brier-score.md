## Motivating example
Two forecasters both classify an event as likely, with probabilities $0.51$ and $0.99$. A classification threshold treats their decisions alike, but a probability score should distinguish their confidence. The Brier loss does this by measuring squared distance from the observed binary outcome.{{cite:gneiting_raftery2007_scoring}} (§3, Ex. 1, p. 363)

## Properties — Why truthful probabilities minimise expected loss
For $Y\sim\operatorname{Bernoulli}(p)$ and forecast $q\in[0,1]$,
$$
E(q-Y)^2=p(1-q)^2+(1-p)q^2=p(1-p)+(q-p)^2.
$$
The first term is outcome variation; the second is the excess loss from an inaccurate probability. It vanishes only at $q=p$. Thus the Brier loss is strictly proper: the unique probability forecast minimising expected loss is the true event probability. This is also the conditional-mean principle for squared-error prediction applied to an indicator.{{cite:gneiting_raftery2007_scoring}} (§3, Ex. 1, p. 363){{cite:pishro_nik2014}} (§9.1.5)

Condition on available information $X$. The same calculation gives
$E[(q(X)-Y)^2\mid X]=p(X)(1-p(X))+(q(X)-p(X))^2$.
Averaging proves that correct conditional probabilities minimise population Brier loss. A finite realised sample can still favour a less accurate forecaster through sampling variation. Strict propriety is an expected-loss property, rather than a guarantee about every short sequence of outcomes.{{cite:pishro_nik2014}} (§9.1.5, minimum mean squared error)

For binary outcomes, $0\le(q-y)^2\le1$. Hard forecasts in $\{0,1\}$ have Brier loss equal to their misclassification indicator. Constant probability $1/2$ has loss $1/4$ on every case. The categorical version sums squared differences over all class indicators; with two classes that sum is twice the single-event binary convention. Scores must use the same convention for numerical comparison.{{cite:gneiting_raftery2007_scoring}} (§3, Ex. 1, p. 363)

## Interpretation — Calibration and useful discrimination
A constant base-rate forecast can be calibrated yet fail to distinguish high-risk from low-risk cases. Its expected loss is $\bar p(1-\bar p)$. Conditioning on useful information replaces this by $E[p(X)(1-p(X))]$, reducing expected loss by $\operatorname{Var}(p(X))$. This follows from total variance for the binary outcome. Reporting inaccurate conditional probabilities adds $E[(q(X)-p(X))^2]$. The score therefore reflects both probability accuracy and the information used to separate risks.{{cite:pishro_nik2014}} (§9.1.5, variance decomposition)

For a rare event, a low average loss may result from forecasting a low base rate on every case. Compare forecasts against a relevant baseline on the same evaluation population. A probabilistic score and a cost-sensitive action address different targets: a change in action costs need not change the best probability report.{{cite:gneiting_raftery2007_scoring}} (§§2.2–2.3, pp. 361–362)

## Worked example — Realised losses and expected losses
For forecasts $(0.9,0.2,0.6)$ and outcomes $(1,0,1)$, the losses are $(0.01,0.04,0.16)$ and their average is $0.07$. Forecasting $1/2$ on all three cases gives $0.25$. These are observed scores, computed without estimating a data-generating probability.{{cite:gneiting_raftery2007_scoring}} (§3, Ex. 1, p. 363)

For an expected-loss comparison, suppose two equally common groups have true event probabilities $0.2$ and $0.8$. Forecasts $0.3$ and $0.7$ have expected Brier loss $0.17$: outcome variation contributes $0.16$ and probability error contributes $0.01$. Accurate group forecasts achieve $0.16$; the constant population base-rate forecast $0.5$ achieves $0.25$. Both accuracy and use of informative groups matter.{{cite:pishro_nik2014}} (§9.1.5)

**Your turn.** When the true event probability is $0.2$, compare expected losses for forecasts $0.2$ and $0$.

::: {.callout-tip collapse="true" title="Answer"}
Forecast $0.2$ has expected loss $0.2(0.8)=0.16$. Forecast zero has loss $0.16+(0-0.2)^2=0.20$. The extra $0.04$ is its squared probability error.
:::

## Check yourself
### Convert odds to a probability {#self-check-ex-sl-10-2}
[Odds ratios](../questions/ex-sl-10-2.qmd) supplies the transformation needed before scoring probabilities.

::: {.callout-tip collapse="true" title="Answer"}
Ten years multiplies the fitted odds by $e^{10(0.04618)}=1.58693$, with interval $(e^{0.2484},e^{0.6851})=(1.28197,1.98397)$. Without high blood pressure, the fitted probabilities at ages $60$ and $70$ are $0.281936$ and $0.383888$, an increase of $0.101952$. Their probability ratio differs from their odds ratio.
:::

### Separate scoring from action {#self-check-ex-sl-08-2}
[Unequal costs](../questions/ex-sl-08-2.qmd) asks which action follows from disease probability $0.3$.

::: {.callout-tip collapse="true" title="Answer"}
A false alarm costs $1$ and a miss costs $5$, giving risks $0.7$ for declaring disease and $1.5$ for declaring no disease. Declare disease above probability $1/6$. The probability supplied for Brier scoring remains $0.3$.
:::
