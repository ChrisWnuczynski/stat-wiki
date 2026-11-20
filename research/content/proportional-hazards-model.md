## Lead context
Proportionality concerns instantaneous event rates among subjects still at risk. It does not require a constant baseline hazard or a constant difference between survival probabilities.

## Motivating example
A study follows two groups until an event occurs. Their event rates may both rise with time, while one group's rate is always a fixed multiple of the other's. A proportional-hazards model expresses that comparison without prescribing the time pattern of the baseline rate. It is useful when follow-up lengths differ and some event times are right censored.{{cite:cox1972}} (§§1–3, pp. 187–189)

## Definition — A multiplier on the instantaneous rate
For a nonnegative event time $T$, let $h(t\mid\mathbf{x})$ denote the conditional hazard. With covariates fixed over follow-up, the log-linear proportional-hazards model is
$$
h(t\mid\mathbf{x})=h_0(t)\exp(\mathbf{x}^{\mathsf T}\boldsymbol\beta).
$$
For two covariate vectors, division cancels $h_0(t)$ and gives the time-independent hazard ratio $\exp\{(\mathbf{x}_1-\mathbf{x}_0)^{\mathsf T}\boldsymbol\beta\}$. A unit increase in a covariate has ratio $e^{\beta_j}$ when its effect enters additively without an interaction.{{cite:cox1972}} (§3, eq. 9, p. 189)

The baseline may increase, decrease, or change direction. Proportionality restricts the ratio of hazards, rather than either hazard separately. With right censoring, inference also requires a suitable independence assumption for censoring conditional on the covariates; informative loss to follow-up can distort the comparison.{{cite:deo2021_cox}} (§§“What is CPH?” and “Assumptions for CPH”)

## Properties — From hazards to survival curves
Write $H_0(t)=\int_0^t h_0(u)\,du$ and $S_0(t)=e^{-H_0(t)}$. Integrating the hazard gives
$$
H(t\mid\mathbf{x})=H_0(t)e^{\mathbf{x}^{\mathsf T}\boldsymbol\beta},\qquad
S(t\mid\mathbf{x})=S_0(t)^{\exp(\mathbf{x}^{\mathsf T}\boldsymbol\beta)}.
$$
Thus a constant hazard ratio generally gives a time-varying probability ratio. Comparing event probabilities at one follow-up time asks a different question from comparing instantaneous rates throughout follow-up.{{cite:cox1972}} (§3, pp. 189–190)

For a binary event probability $p$ over a specified interval, a complementary log-log predictor makes $-\log(1-p)$ multiplicative. Calling this quantity a cumulative hazard requires the event-time interpretation. With ordered categories, the same transformation can instead act on cumulative category probabilities; the direction used to define the cumulative event determines the signs and intercept ordering.{{cite:mccullagh1980}} (§3.1, pp. 113–114)

## Worked example — One coefficient, two probability scales
Let $\beta=0.5$ for a binary covariate. The hazard ratio is $e^{0.5}=1.6487$. If baseline survival at a chosen time is $0.8$, survival in the other group is
$$
0.8^{e^{0.5}}=0.6922.
$$
The event probabilities are $0.2$ and $0.3078$, giving a probability ratio about $1.5391$, rather than $1.6487$. The calculation follows by integrating the multiplicative hazard model.{{cite:cox1972}} (§3, pp. 189–190)

For cumulative category predictors $0.3$ and $-0.5$, the inverse link $g^{-1}(\eta)=1-e^{-e^\eta}$ gives $0.7407$ and $0.4548$. The probabilities decrease with the category threshold when the intercepts decrease under the upper-tail convention.{{cite:mccullagh1980}} (§3.1, pp. 113–114)

**Your turn.** If the hazard ratio is $2$ and baseline survival is $0.8$, find survival and event probability in the other group.

::: {.callout-tip collapse="true" title="Answer"}
Survival is $0.8^2=0.64$, and event probability is $1-0.64=0.36$. The event probability ratio is $0.36/0.2=1.8$.
:::

## Check yourself

### Reading a coefficient {#self-check-depth-cloglog-interpretation}
[Reading a complementary log-log coefficient](../questions/depth-cloglog-interpretation.qmd): which quantity is multiplied when the coefficient is $\log 3$?

::: {.callout-tip collapse="true" title="Answer"}
The quantity $-\log(1-p)$ triples. An interpretation as a hazard ratio additionally requires an event-time model with proportional hazards.
:::

### Reversing the event {#self-check-depth-cloglog-reversal}
[Reversing the event in a cloglog model](../questions/depth-cloglog-reversal.qmd): does negating every coefficient model $1-p$ with the same link?

::: {.callout-tip collapse="true" title="Answer"}
No. The inverse complementary log-log curve is asymmetric. Reversing the event changes the transformation to its log-log counterpart; coefficient sign reversal alone does not perform that transformation.
:::
