## Lead context

In ordinary survival analysis each subject is followed until a single kind of event, or until censoring. In many studies that picture is too simple: a subject may experience one of several different kinds of event, and whichever happens first rules out the others. A patient followed for death from cancer may die of heart disease first; a patient followed for relapse after a transplant may die without relapsing first; a kidney-transplant recipient may experience graft failure, or may die with a functioning graft. The events *compete*: at most one of them can be the first event for a given subject. A competing event is an event whose occurrence precludes the occurrence of the primary event of interest {{cite:austin_lee_fine2016}} (Abstract). Treating a competing event as if it were merely censoring — as if the event of interest might still happen later — is the central error this article is about: it overstates the risk of the event of interest, and the remedy is to estimate cumulative incidence directly.

## Motivating example: cardiovascular death after heart failure

**Example (labelled).** Austin, Lee and Fine follow patients hospitalised with heart failure for five years, with two causes of death: cardiovascular death, the event of interest, and noncardiovascular death, the competing event. A patient who dies of a noncardiovascular cause cannot later die of a cardiovascular cause, so the two causes compete. Estimating the five-year incidence of cardiovascular death with the complement of the Kaplan–Meier survival function gives 43.0%, while the cumulative incidence function, which accounts for the competing deaths, gives 36.8% — 6.2 percentage points lower {{cite:austin_lee_fine2016}} (§ "Estimating Crude Incidence"). The Kaplan–Meier figure is not a small rounding difference from the right answer; it answers a different, hypothetical question, namely what the risk would be in a world in which noncardiovascular death did not occur. For a clinician or patient asking "what is the chance that this patient dies of cardiovascular causes within five years, given that other causes of death are also in play?", 36.8% is the relevant number.

## What counts as a competing risk: one first event, several possible kinds

Let $T$ be the time from a well-defined origin (for example, hospital admission, transplantation, or randomisation) to the *first* event experienced by a subject, and let $D$ be the kind, or cause, of that first event. Suppose there are $K$ possible kinds, so $D$ takes values in $\{1, 2, \dots, K\}$, and let $k$ denote one particular kind, the event of interest. The other kinds, $D \ne k$, are the competing events for cause $k$.

The defining property is preclusion, not delay. If $D = 2$ and $T = t$, then the subject does not experience cause $1$ at any later time: the event of interest is not merely unobserved after $t$, it is impossible after $t$. In clinical oncology, for example, cancer-related mortality may be of primary interest, but deaths from other causes can prevent its occurrence {{cite:zhang2017}} (§ "Introduction"). This is what distinguishes a competing event from right-censoring. A censored subject is one whose event time is unknown but who, in the usual modelling, is treated as if the event could still occur after the censoring time; a subject who has had a competing event is known never to experience the event of interest. Censoring can still occur alongside competing risks — a subject may be lost to follow-up, or the study may end, before any event — and that ordinary censoring is a separate matter from the competing events themselves.

Two consequences follow at once. First, the probability that cause $k$ has occurred by time $t$ depends on the hazards of *all* the causes, not only on the hazard of cause $k$, because subjects are removed from the event-free pool by competing events as well. Second, there is no single survival function $S(t) = P(T > t)$ for cause $k$ alone that plays the role it plays when there is only one kind of event: $S(t)$ is the probability of being free of *every* event by time $t$, and $1 - S(t)$ is the probability of having had *any* event by time $t$, not the probability of having had cause $k$.

## Why 1 − Kaplan–Meier is wrong here

The Kaplan–Meier estimator estimates a survival function from right-censored data by multiplying, at each event time, by one minus the fraction of subjects at risk who have the event. Applied to cause $k$ alone, it treats every subject who experiences a competing event as censored at that time: the subject leaves the risk set, and the calculation proceeds as if that subject's future risk of cause $k$ were the same as the risk of the subjects who remain under observation. That is exactly the non-informative-censoring assumption, and for a competing event it is false as a description of the world: a subject who has died of another cause has future risk zero, not the average risk of the survivors.

The result is an estimate of the risk of cause $k$ in a hypothetical population in which the competing events do not occur. Censoring competing events is only justified if interest is in such a hypothetical population and if the event of interest and the competing events are independent {{cite:coemans2022}} (Abstract). In every other case the traditional estimator of the cumulative incidence tends to be biased upward, sometimes even producing probabilities above one when the naive estimates for the separate causes are added {{cite:coemans2022}} (Abstract). The upward bias holds regardless of whether the competing events are independent of one another {{cite:austin_lee_fine2016}} (Abstract): independence would make the hypothetical-world quantity well-defined, but it would not make it the actual risk in the presence of the competing events. The bias grows with time and with the incidence of the competing event, so it is largest precisely where the competing event is common — for example, in older populations, where death from other causes is frequent.

A useful diagnostic follows. If 1 − Kaplan–Meier is computed separately for each cause, treating the other causes as censored, the resulting "incidences" can sum to more than the incidence of the composite event (any event), and can sum to more than one. A genuine set of cause-specific probabilities cannot do that: the probabilities of the mutually exclusive first events, plus the probability of no event yet, must sum to one. When the naive figures violate that bookkeeping, the method, not the data, is at fault.

## Cumulative incidence and Aalen–Johansen

The quantity that replaces $1 - S(t)$ when events compete is the cumulative incidence function (CIF). For cause $k$, the CIF, written $F_k(t)$, is the probability that the first event has occurred by time $t$ *and* that it was of kind $k$:

$$F_k(t) = P(T \le t, D = k).$$

The CIF is a probability, so $0 \le F_k(t) \le 1$, it is non-decreasing in $t$, and unlike a distribution function it need not approach $1$ as $t$ grows: if competing events claim a substantial share of subjects, $F_k(t)$ plateaus below $1$, because those subjects can never experience cause $k$.

The CIFs for the different causes add up exactly to the cumulative incidence of *any* event. Writing $S(t) = P(T > t)$ for the probability of remaining free of every event,

$$\sum_{k=1}^{K} F_k(t) = 1 - S(t),$$

so the CIFs partition the overall risk among the causes. Reporting all of them — or at least the CIF for the event of interest together with the CIF for the competing events — is part of reporting the analysis honestly: a single CIF without its competitors hides how much of the total risk belongs to each cause.

To see how the CIF depends on the hazards, define the cause-specific hazard $h_k(t)$ below. Then the CIF for cause $k$ can be written as an integral over time of the probability of still being event-free multiplied by the cause-$k$ hazard at that moment:

$$F_k(t) = \int_0^t S(s) \, h_k(s) \, ds.$$

Here $S(s)$ is determined by *all* the causes together, so there is no one-to-one correspondence between the cumulative incidence $F_k(t)$ and the cause-specific hazard $h_k(s)$: the same cause-$k$ hazard produces a smaller CIF when the competing hazards are large, because fewer subjects survive event-free long enough to experience cause $k$ {{cite:zhang2017}} (§ "Key concepts in survival analysis with and without competing risks"). This integral is the reason a covariate can raise the rate of cause $k$ among the event-free while barely changing, or even lowering, its cumulative incidence.

The standard nonparametric estimator of the CIF is the Aalen–Johansen estimator {{cite:aalen_johansen1978}} (pp. 141–150), also described as the nonparametric competing-risks method to be preferred above the Kaplan–Meier method {{cite:coemans2022}} (Abstract). Let the distinct event times (of any cause) up to time $t$ be $u_1 < u_2 < \dots < u_m \le t$. At event time $u_j$, let $n(u_j)$ be the number of subjects at risk just before $u_j$ — event-free and still under observation — and let $d_k(u_j)$ be the number who experience cause $k$ at $u_j$. Let $\hat{S}(t)$ be the ordinary Kaplan–Meier estimator of overall survival, treating *any* event as an event and only genuine censoring as censoring, and let $\hat{S}(u_j-)$ be its value just before $u_j$. Then

$$\hat{F}_k(t) = \sum_{j: u_j \le t} \hat{S}(u_j-) \, \frac{d_k(u_j)}{n(u_j)}.$$

Each term is the estimated probability of surviving event-free up to $u_j$, multiplied by the estimated conditional probability of experiencing cause $k$ at $u_j$ given survival to $u_j$. Censored subjects contribute by leaving the risk sets $n(u_j)$ after their censoring time, exactly as in Kaplan–Meier estimation, and the estimator requires the same non-informative-censoring assumption for genuine censoring. When there is only one cause ($K = 1$), the Aalen–Johansen estimator reduces exactly to $1 - \hat{S}(t)$; with competing causes it is strictly the correct generalisation, and the estimated CIFs sum exactly to $1 - \hat{S}(t)$. In practice the CIF is estimated by software for competing risks (for example the `cuminc` function in R), and CIF curves for different groups can be plotted and compared with a test designed for CIFs rather than with the log-rank test, which compares survival curves.

## Cause-specific hazard versus subdistribution hazard

Regression in the presence of competing risks comes in two families, because there are two different hazards to model. They answer different questions, and choosing between them is a choice about the question, not about which is "correct" in the abstract.

The **cause-specific hazard** for cause $k$, written $h_k(t)$, is the instantaneous rate of cause $k$ among subjects who are currently event-free:

$$h_k(t) = \lim_{dt \to 0} \frac{P(t \le T < t + dt, D = k \mid T \ge t)}{dt}.$$

The conditioning event $T \ge t$ means "has experienced no event of any kind before $t$". A cause-specific hazard model — most commonly a Cox proportional hazards model fitted by treating failures from other causes as censored at their event times — estimates how covariates change this rate {{cite:zhang2017}} (§ "Cause-specific hazard regression"). Its coefficients are log hazard ratios among the event-free. Because the CIF depends on all the cause-specific hazards through the integral above, a covariate's effect on the cause-specific hazard does not translate directly into an effect on the CIF: a treatment that lowers the competing hazard, for example, leaves more subjects alive to experience the event of interest, and can raise its CIF while leaving its cause-specific hazard unchanged. Cause-specific models are therefore suited to aetiological questions — "does this factor change the rate at which cause $k$ strikes, among those still free of all events?" — as Austin, Lee and Fine put it, the cause-specific family estimates the effect of covariates on the rate of occurrence in subjects who are currently event free, and may be better suited to aetiologic questions {{cite:austin_lee_fine2016}} (Abstract).

The **subdistribution hazard** for cause $k$, written $\tilde{h}_k(t)$, is defined from the CIF itself:

$$\tilde{h}_k(t) = -\frac{d}{dt} \log(1 - F_k(t)) = \frac{f_k(t)}{1 - F_k(t)},$$

where $f_k(t)$ is the density corresponding to $F_k(t)$, when it exists. Equivalently, it is the instantaneous rate of cause $k$ among subjects who have *not yet experienced cause $k$* — a risk set that includes both subjects who are still event-free and subjects who have already experienced a competing event {{cite:austin_lee_fine2016}} (§ "Hazard Function Regression"). Those subjects are retained in the risk set, in a mathematical sense, even though they can never in fact experience cause $k$; the construction is what makes the subdistribution hazard stand in a one-to-one relation with the CIF, in the same way the ordinary hazard stands in a one-to-one relation with the ordinary survival function in the absence of competing risks.

The **Fine–Gray model** is a proportional hazards model for the subdistribution hazard {{cite:fine_gray1999}} (Abstract). For a vector $z$ of covariates, it specifies

$$\tilde{h}_k(t \mid z) = \tilde{h}_{k0}(t) \exp(z^T \beta),$$

where $\tilde{h}_{k0}(t)$ is an unspecified baseline subdistribution hazard and $\beta$ is a vector of coefficients. The quantity $\exp(\beta_j)$ is the subdistribution hazard ratio (SHR) for a one-unit increase in covariate $z_j$. The model is fitted as a weighted Cox regression, with weights that handle the censoring of the retained competing-event subjects, and it allows direct prediction of the CIF: under the model, $F_k(t \mid z) = 1 - \exp(-\tilde{H}_{k0}(t) \exp(z^T \beta))$, where $\tilde{H}_{k0}(t)$ is the cumulative baseline subdistribution hazard. The SHR, however, has no simple interpretation as an ordinary hazard ratio: it provides information on the ordering of CIF curves at different levels of covariates, but no practical interpretation as a hazard ratio in the absence of competing risks {{cite:zhang2017}} (Abstract). A subdistribution hazard ratio above one means the CIF is higher, not that the rate among the event-free is higher.

|  | Cause-specific hazard model | Fine–Gray (subdistribution hazard) model |
|---|---|---|
| Risk set at time $t$ | Subjects still free of *all* events | Subjects not yet having had cause $k$, including those who already had a competing event |
| Quantity modelled | $h_k(t)$, the rate of cause $k$ among the event-free | $\tilde{h}_k(t)$, the hazard corresponding to the CIF $F_k(t)$ |
| Question answered | How does a covariate change the *rate* of cause $k$? (aetiology) | How does a covariate change the *absolute risk* (CIF) of cause $k$? (prognosis, prediction) |
| Fitting | Ordinary Cox model, competing events treated as censored {{cite:cox1972}} (pp. 187–220) | Weighted Cox model on the subdistribution hazard {{cite:fine_gray1999}} (Abstract) |
| Effect measure | Cause-specific hazard ratio | Subdistribution hazard ratio (SHR) |

The two models can disagree, and the disagreement is informative rather than a contradiction. In the heart-failure case study, cancer was associated with a substantial decrease in the incidence of cardiac death (subdistribution hazard ratio 0.82), whereas it had essentially no association with the rate of cardiac death among subjects still alive (cause-specific hazard ratio 0.96) {{cite:austin_lee_fine2016}} (§ "Hazard Function Regression"). Cancer kills by other causes first, so fewer patients with cancer live long enough to die of cardiac causes: the absolute risk falls even though the rate among the living does not. Reporting both models side by side, as Zhang recommends, is often the most informative analysis {{cite:zhang2017}} (§ "Key concepts in survival analysis with and without competing risks"). The textbook treatment of competing risks, including the cause-specific hazards and the multistate view, is in Kalbfleisch and Prentice {{cite:kalbfleisch_prentice2002}} (Ch. 8, pp. 247–248).

## Worked example: relapse versus death without relapse

**Example (labelled).** Ten patients are followed after bone-marrow transplantation, with time measured in months from transplantation. The event of interest is relapse (cause 1); the competing event is death without relapse (cause 2). A patient who dies without relapsing can never relapse afterwards. Two patients are right-censored (lost to follow-up or still event-free when observation ends).

| Patient | Time (months) | Outcome |
|---|---|---|
| A | 2 | Relapse (cause 1) |
| B | 3 | Death without relapse (cause 2) |
| C | 4 | Relapse (cause 1) |
| D | 5 | Censored |
| E | 6 | Death without relapse (cause 2) |
| F | 7 | Relapse (cause 1) |
| G | 8 | Censored |
| H | 9 | Relapse (cause 1) |
| I | 10 | Death without relapse (cause 2) |
| J | 12 | Censored |

First, the naive Kaplan–Meier calculation for relapse alone, treating deaths without relapse as censoring. Let $\hat{S}_1(t)$ be this Kaplan–Meier estimate and $n(u)$ the number at risk just before time $u$. Only relapse times change $\hat{S}_1(t)$:

- At $u = 2$: $n = 10$, one relapse, so $\hat{S}_1(2) = 9/10 = 0.90$.
- At $u = 4$: $n = 8$ (one relapse and one competing death have removed two patients), one relapse, so $\hat{S}_1(4) = (9/10)(7/8) = 63/80 = 0.7875$.
- At $u = 7$: $n = 5$, one relapse, so $\hat{S}_1(7) = (63/80)(4/5) = 63/100 = 0.63$.
- At $u = 9$: $n = 3$, one relapse, so $\hat{S}_1(9) = (63/100)(2/3) = 21/50 = 0.42$.

The naive risks of relapse are therefore $1 - \hat{S}_1(7) = 0.37$ at 7 months and $1 - \hat{S}_1(9) = 0.58$ at 9 months.

Now the Aalen–Johansen calculation. Let $\hat{S}(t)$ be overall survival (any event counts). The table shows, at each event time $u$, the number at risk $n(u)$, the overall survival just before $u$, denoted $\hat{S}(u-)$, the increment added to the CIF of the cause that occurred, and the running CIFs.

| $u$ | $n(u)$ | $\hat{S}(u-)$ | Event | Increment | $\hat{F}_1(u)$ | $\hat{F}_2(u)$ |
|---|---|---|---|---|---|---|
| 2 | 10 | $1$ | Cause 1 | $1 \times 1/10 = 1/10$ | $1/10 = 0.10$ | $0$ |
| 3 | 9 | $9/10$ | Cause 2 | $(9/10) \times 1/9 = 1/10$ | $0.10$ | $1/10 = 0.10$ |
| 4 | 8 | $4/5$ | Cause 1 | $(4/5) \times 1/8 = 1/10$ | $1/5 = 0.20$ | $0.10$ |
| 6 | 6 | $7/10$ | Cause 2 | $(7/10) \times 1/6 = 7/60$ | $0.20$ | $13/60 \approx 0.2167$ |
| 7 | 5 | $7/12$ | Cause 1 | $(7/12) \times 1/5 = 7/60$ | $19/60 \approx 0.3167$ | $0.2167$ |
| 9 | 3 | $7/15$ | Cause 1 | $(7/15) \times 1/3 = 7/45$ | $17/36 \approx 0.4722$ | $0.2167$ |

For example, at $u = 7$ the overall survival just before 7 months is $\hat{S}(7-) = 7/15 \approx 0.4667$, and the increment to the relapse CIF is $(7/15)(1/5) = 7/60$, giving $\hat{F}_1(7) = 1/5 + 7/60 = 19/60 \approx 0.317$. At 9 months, $\hat{F}_1(9) = 19/60 + 7/45 = 17/36 \approx 0.472$.

Comparison at the two evaluation times:

| Time | Naive 1 − Kaplan–Meier risk of relapse | Aalen–Johansen $\hat{F}_1(t)$ | Difference |
|---|---|---|---|
| 7 months | $0.37$ | $19/60 \approx 0.317$ | $0.053$ |
| 9 months | $0.58$ | $17/36 \approx 0.472$ | $0.108$ |

The naive figure is larger at both times, and the gap widens as competing deaths accumulate. At 2 months the two agree ($0.10$), because no competing event has yet occurred; the overstatement appears only once competing events have removed subjects who can never relapse. As a check on the bookkeeping, at 9 months $\hat{F}_1(9) + \hat{F}_2(9) = 17/36 + 13/60 = 31/45 \approx 0.689$, and $1 - \hat{S}(9) = 1 - 14/45 = 31/45$: the two CIFs sum exactly to the overall cumulative incidence of any event. All arithmetic in this example was verified by exact rational computation; see the accompanying check script.

## Your turn

Eight patients are followed after surgery. The event of interest is local recurrence (cause 1); the competing event is death without recurrence (cause 2). Times are in months.

| Patient | Time (months) | Outcome |
|---|---|---|
| A | 1 | Recurrence (cause 1) |
| B | 2 | Death without recurrence (cause 2) |
| C | 3 | Censored |
| D | 4 | Recurrence (cause 1) |
| E | 5 | Death without recurrence (cause 2) |
| F | 6 | Recurrence (cause 1) |
| G | 7 | Censored |
| H | 8 | Death without recurrence (cause 2) |

Compute, at $t = 6$ months, (a) the naive risk of recurrence $1 - \hat{S}_1(6)$, where $\hat{S}_1$ is the Kaplan–Meier estimate for recurrence alone with deaths without recurrence treated as censoring, and (b) the Aalen–Johansen estimate $\hat{F}_1(6)$ of the cumulative incidence of recurrence. Which is larger, and by how much?

::: {.callout-tip collapse="true" title="Answer"}
(a) Kaplan–Meier for recurrence alone: at 1 month, $\hat{S}_1 = 7/8$; at 4 months, with 5 at risk, $\hat{S}_1 = (7/8)(4/5) = 7/10$; at 6 months, with 3 at risk, $\hat{S}_1 = (7/10)(2/3) = 7/15 \approx 0.467$. The naive risk is $1 - 7/15 = 8/15 \approx 0.533$.

(b) Aalen–Johansen: the increments to $\hat{F}_1$ are $1/8 = 0.125$ at 1 month, $(3/4)(1/5) = 0.15$ at 4 months (overall survival just before 4 months is $3/4$), and $(9/20)(1/3) = 0.15$ at 6 months (overall survival just before 6 months is $9/20$). So $\hat{F}_1(6) = 0.125 + 0.15 + 0.15 = 0.425 = 17/40$.

The naive figure is larger, by $8/15 - 17/40 = 13/120 \approx 0.108$. As a check, $\hat{F}_2(6) = 0.275$ and $\hat{F}_1(6) + \hat{F}_2(6) = 0.70 = 1 - \hat{S}(6)$, since overall survival at 6 months is $0.30$.
:::

## Statistical use / Assumptions and limits

**Use.** Report the CIF, estimated by Aalen–Johansen, whenever the question is about absolute risk: "what proportion of patients will have experienced the event of interest by time $t$, in the presence of the competing events?" Use cause-specific hazard models when the question is aetiological, about rates among the event-free, and use the Fine–Gray model when the question is prognostic, about predicting a patient's absolute risk or comparing CIFs between groups. In a clinical prediction model, the Fine–Gray model (or a combination of cause-specific models) is the appropriate tool, because a prediction must be a probability in the real world where competing events occur {{cite:austin_lee_fine2016}} (§ "Hazard Function Regression").

**Assumptions.** The Aalen–Johansen estimator and the cause-specific models assume that genuine right-censoring is non-informative: at any time, subjects who are censored have the same future risk as subjects who remain under observation. They do *not* assume that the competing events are independent of the event of interest: the methods described here apply equally whether competing risks are independent or not {{cite:austin_lee_fine2016}} (§ "Introduction"). What they do require is a well-defined time origin, a well-defined first event, and causes recorded correctly — misclassifying the cause of an event misallocates probability between the CIFs. The Fine–Gray model additionally assumes proportional subdistribution hazards: the ratio of subdistribution hazards between covariate levels is constant over time, an assumption that can be checked with Schoenfeld-type residuals or by adding an interaction with time {{cite:zhang2017}} (§ "Model diagnostic").

**Limits.** The Aalen–Johansen estimator is nonparametric and unadjusted: it describes one group at a time and does not adjust for covariates. Adjusted CIFs require a regression model. Estimates are unstable when the number of events of a given cause is small, and a CIF estimated over a short follow-up says nothing about the eventual split between causes beyond that horizon. Finally, a competing-risks analysis is an analysis of the *first* event only. If the scientific question concerns events after the first — for example, death after relapse — that is a multistate problem, not a competing-risks problem, and the competing-risks CIF is the wrong tool for it.

## Common misconceptions

1. **"A competing event is just another form of censoring."** No. Censoring means the event time is unknown but the event could still occur; a competing event means the event of interest can never occur. Treating the second like the first is the error that produces the upward bias in 1 − Kaplan–Meier.
2. **"If I compute 1 − Kaplan–Meier for each cause, the figures add up to the overall risk."** No. The naive figures can sum to more than the incidence of the composite event and more than one; only the CIFs sum correctly, to $1 - S(t)$.
3. **"A cause-specific hazard ratio tells me how much a covariate changes the absolute risk."** No. The CIF depends on every cause-specific hazard, so a covariate can raise the cause-specific hazard of the event of interest while lowering its CIF (if it raises the competing hazard even more), or vice versa.
4. **"The Fine–Gray subdistribution hazard ratio is an ordinary hazard ratio."** No. It is a ratio of subdistribution hazards, whose risk set artificially retains subjects who have already had a competing event. It orders CIF curves; it does not describe the rate of the event among subjects still alive and event-free.
5. **"If the competing events are independent, 1 − Kaplan–Meier is fine for absolute risk."** No. The Kaplan–Meier estimate is biased upward regardless of whether the competing events are independent {{cite:austin_lee_fine2016}} (Abstract). Independence would only make the hypothetical world without competing events a well-defined target — it would not make that target the actual risk.
6. **"Competing risks only matter when the competing event is common."** The bias grows with the incidence of the competing event, but the conceptual point does not depend on size: even a rare competing event means 1 − Kaplan–Meier is estimating a hypothetical risk, and the CIF is the quantity that matches the question actually asked.

## History

The product-limit (Kaplan–Meier) estimator of 1958 was built for a single kind of event, with other occurrences treated as "losses" that prevent observation of the event of interest {{cite:kaplan_meier1958}} (pp. 457–481). That framing — losses as censoring — is exactly what breaks down when the "loss" is itself an event of interest that precludes the first. The general nonparametric estimator for transition probabilities in a multistate setting, which specialises to the competing-risks CIF estimator, was given by Aalen and Johansen in 1978 {{cite:aalen_johansen1978}} (pp. 141–150). For regression, the cause-specific Cox model, fitted by treating competing events as censored, was available from Cox's 1972 paper onwards {{cite:cox1972}} (pp. 187–220), but it models rates, not cumulative incidence. Fine and Gray's 1999 paper supplied the missing regression tool: a proportional hazards model for the subdistribution, which models the CIF directly {{cite:fine_gray1999}} (Abstract). The modern guidance — use the CIF rather than the complement of Kaplan–Meier for crude incidence, and choose between cause-specific and subdistribution models according to whether the question is aetiological or prognostic — was set out in the widely read tutorial by Austin, Lee and Fine in 2016 {{cite:austin_lee_fine2016}} (Abstract), and the warning against censoring competing events was restated forcefully for medical researchers by Coemans and colleagues in 2022 {{cite:coemans2022}} (Abstract).

## Connections

- [Kaplan–Meier estimator](kaplan-meier-estimator.qmd) — the product-limit estimator of the survival function; its complement $1 - \hat{S}(t)$ is the right estimate of cumulative incidence only when there are no competing events.
- [Cox proportional hazards model](cox-proportional-hazards-model.qmd) — the model fitted for cause-specific hazards by treating competing events as censored, and the weighted Cox fit used by the Fine–Gray model.
- [Survival function](survival-function.qmd) — $S(t) = P(T > t)$, the probability of being free of every event; the CIFs sum to $1 - S(t)$.
- [Hazard rate](hazard-rate.qmd) — the instantaneous rate whose cause-specific versions $h_k(t)$ drive the CIF through the integral $F_k(t) = \int_0^t S(s) h_k(s) \, ds$.
- [Censoring statistics](censoring-statistics.qmd) — right-censoring and the non-informative-censoring assumption; a competing event is not censoring, and the passing remark there that competing failure modes are handled by treating a failure from another mode as a censoring time is the naive analysis this article warns against.
- [Survival analysis](survival-analysis.qmd) — the wider setting: time-to-event data, censoring, and regression, of which competing risks is the case with several mutually exclusive first events.

## Check yourself

1. A study follows patients for death from stroke, with death from other causes as a competing event. The Kaplan–Meier estimate of stroke-free survival at 5 years is 0.80. A colleague reports the 5-year risk of death from stroke as $1 - 0.80 = 0.20$. What is wrong with this figure, and what should be reported instead?

::: {.callout-tip collapse="true" title="Answer"}
The figure 0.20 is the risk of stroke death in a hypothetical world in which death from other causes does not occur, because the Kaplan–Meier calculation treats deaths from other causes as censoring. In the real world those patients can never die of stroke, so 0.20 overstates the actual risk. What should be reported is the cumulative incidence function for stroke death at 5 years, estimated by the Aalen–Johansen estimator, together with the cumulative incidence of death from other causes.
:::

2. A drug halves the cause-specific hazard of relapse (cause-specific hazard ratio 0.5) but also halves the cause-specific hazard of death without relapse. Must the 5-year cumulative incidence of relapse also be halved? Why or why not?

::: {.callout-tip collapse="true" title="Answer"}
No. The cumulative incidence of relapse depends on all the cause-specific hazards, not only its own, through the integral of overall survival times the relapse hazard. Halving the competing hazard leaves more patients alive and event-free, hence more patients available to relapse later, which offsets the lower relapse rate. The CIF could fall by less than half, stay roughly the same, or in principle rise; the cause-specific hazard ratio alone does not determine it.
:::

3. In a Fine–Gray model, a covariate has a subdistribution hazard ratio of 1.4 for the event of interest. A reader interprets this as "among patients still alive and event-free, the covariate raises the rate of the event by 40%". Is that interpretation correct? What does 1.4 mean?

::: {.callout-tip collapse="true" title="Answer"}
No, that interpretation describes a cause-specific hazard ratio, not a subdistribution hazard ratio. The subdistribution hazard ratio of 1.4 means the subdistribution hazard is 40% higher, which corresponds to a higher cumulative incidence function for the event of interest — the covariate is associated with higher absolute risk over time. The subdistribution risk set includes patients who have already had a competing event, so the ratio says nothing directly about the rate among patients still alive and event-free.
:::
