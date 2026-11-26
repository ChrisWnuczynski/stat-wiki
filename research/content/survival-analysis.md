## Lead context

Patients leave a study, machines are taken off test, and a report is due before every unit has failed. Survival analysis is the set of methods for event times under that kind of incomplete observation. The quantity being estimated is often a probability of still being free of the event, or a rate among those still at risk. The subject is wider than any one formula for that probability. It includes how the times were cut short, how groups are compared, and how covariates enter the rate. A complete sample of failure times can be summarised by an ordinary empirical distribution. The subject becomes survival analysis when some times are incomplete, or when the interest is the risk among those still surviving.{{cite:kaplan_meier1958}} (p. 457){{cite:james_islr2021}} (Ch. 11, §11.1, pp. 462–463)

## Motivating example

A clinic follows four patients and must report before every history is finished. One dies at 2 months. One is lost at 4 months, still alive at the last visit. One dies at 5 months. One dies at 8 months. The lost patient contributes a fact: the event time was greater than 4 months. Treating 4 as if it were a death answers a different question, the question of when contact stopped. The [survival function](survival-function.qmd) $S(t)=\Pr(T>t)$ is the probability the event time exceeds $t$. The four records are used to estimate that probability, not to pretend that every patient was watched until death.{{cite:james_islr2021}} (Ch. 11, §11.1, (11.1)–(11.2), pp. 462–465){{cite:kaplan_meier1958}} (p. 457)

The same shape of problem appears in a life test. A tube breaks for a reason the test was not about, the rig is needed for something else, or the report cannot wait. Each of those records says that the failure time exceeded the time last seen. Kaplan and Meier called that earlier event a loss, accidental or the result of a decision to stop observation, and they wanted the proportion of lifetimes that would have exceeded $t$ had the losses not occurred.{{cite:kaplan_meier1958}} (p. 457)

## Definition

For each individual there is a survival time $T$, also called the failure time or the event time, and a censoring time $C$. What is recorded is $Y=\min(T,C)$, together with a status indicator $\delta$ that equals 1 when the event is seen ($T\le C$) and 0 when the censoring time is seen instead. Right censoring is the case $T\ge Y$: the event is at least as late as the recorded time. Left censoring is the opposite inequality, as when a survey at day 250 finds that a pregnancy has already ended and the duration is known only to be at most 250 days. Interval censoring places the event inside a window, as when patients are contacted once a week. The development below is for right censoring.{{cite:james_islr2021}} (Ch. 11, §11.1–§11.2, pp. 462–464)

The [survival function](survival-function.qmd) is $S(t)=\Pr(T>t)$. In reliability work the same function is called the reliability function $R(t)$, and $R(t)=1-F(t)$ because a unit has either failed by $t$ or it has not. The hazard, or force of mortality, is the instantaneous risk among those still event-free,

$$
h(t)=\lim_{\Delta t\to 0}\frac{\Pr(t<T\le t+\Delta t\mid T>t)}{\Delta t}=\frac{f(t)}{S(t)}.
$$


The division by $\Delta t$ makes $h(t)$ a rate, not a probability. A hazard of 2 per year can exceed 1. It says that the conditional chance of an event in a short interval is about $2$ times the length of the interval.{{cite:nist_reliability2002}} (§8.1.2.2){{cite:james_islr2021}} (Ch. 11, §11.5.1, (11.9)–(11.10), pp. 469–470)

The product-limit estimator updates $S(t)$ only at observed event times, and only among those still under observation. Let $d_1<\cdots<d_K$ be the distinct death times, let $q_j$ be the number of deaths at $d_j$, and let $r_j$ be the number alive and still in the study just before $d_j$, the risk set. Then

$$
\widehat S(d_k)=\prod_{j=1}^{k}\frac{r_j-q_j}{r_j}.
$$


Between death times the estimate stays flat. When no losses occur before $t$, the product reduces to the ordinary proportion of survivors.{{cite:james_islr2021}} (Ch. 11, §11.3, (11.3), pp. 464–466){{cite:kaplan_meier1958}} (p. 457)

## Properties

The estimator is a product because survival past $d_k$ factors into survival past each earlier death, conditional on having reached it. It is impossible to survive past $d_k$ without having survived past $d_{k-1}$, so

$$
S(d_k)=\Pr(T>d_k\mid T>d_{k-1})\,S(d_{k-1}).
$$


The fraction $(r_j-q_j)/r_j$ estimates the conditional probability. A person censored before $d_j$ is not in $r_j$. A person censored at a later time still is. That is why a censoring at 4 months changes the risk set at 5 months and does not change the risk set at 2 months.{{cite:james_islr2021}} (Ch. 11, §11.3, pp. 464–466)

Independent components combine by multiplication when all of them must survive. If each microprocessor has reliability $R_m(t)$ and the processor uses two that must both work, the pair has reliability $R_m(t)^2$. The general rule is to multiply the reliability functions of independent components. The rule fails when the components share a cause of failure. Two patients in the same ward during an outbreak are the medical analogue: their event times are not independent just because a curve was drawn as if they were.{{cite:nist_reliability2002}} (§8.1.2.2)

The likelihood of one record is the density $f(y_i)$ if the event was seen and the survival probability $S(y_i)$ if the record was censored. For independent records the likelihood is $\prod_i h(y_i)^{\delta_i}S(y_i)$. An exponential model puts a constant hazard on that likelihood. A Weibull model lets the hazard rise or fall as a power of time. The proportional-hazards model leaves a baseline hazard $h_0(t)$ unspecified and multiplies it by $\exp(x_i^\top\beta)$, a factor that does not change with time. The name records the assumption: two people with different covariates have hazards in a constant ratio.{{cite:james_islr2021}} (Ch. 11, §11.5.1–§11.5.2, (11.12)–(11.14), pp. 470–471)

For the four clinic records the arithmetic is small enough to check by hand. At 2 months everyone is at risk, one death occurs, and $(4-1)/4=3/4$. At 5 months the patient lost at 4 months is gone, two patients remain, one dies, and the factor is $1/2$. The product is $(3/4)\times(1/2)=3/8$. At 8 months one patient is left and dies, and the estimate drops to 0. A naive proportion of known survivors past 5 months would have used a different denominator and a different meaning.

## Statistical use

Use a survival method when the outcome is a time and some times are cut short. Comparing two groups with a rank test is the analogue of a two-sample test when the outcome is a censored time. A covariate model is the analogue of a regression. In a brain-tumour series of 88 patients, of whom 53 were still alive at the end of follow-up, the proportion known to have survived past 20 months was $48/88$, about 55 percent. That figure treats every censored patient who had not reached 20 months as if the event had occurred by then. Seventeen of the forty patients who were not known to have reached 20 months were in fact censored. Restricting the denominator to the 71 patients not censored by 20 months gives $48/71$, about 68 percent, and that figure throws away the censored histories entirely, including a patient last seen at 19.9 months who very likely would have passed 20. The product-limit curve is the estimate that uses both the deaths and the censoring times.{{cite:james_islr2021}} (Ch. 11, §11.3, pp. 464–465)

For the ordinary pooled Kaplan–Meier curve over times with follow-up support, marginal independent censoring is the standard sufficient censoring condition: $T$ is independent of $C$ in the population being estimated.{{cite:kaplan_meier1958}} (pp. 457–458) Independence only within baseline strata does not by itself justify pooling; see the [Kaplan–Meier assumptions discussion](kaplan-meier-estimator.qmd#assumptions-and-limits). If independence holds only within strata, one option is to estimate survival within each stratum with follow-up support at the times of interest, then standardize by averaging those curves using the target population's stratum weights. The strata must be mutually exclusive and cover the target population: by the [law of total probability](law-of-total-probability.qmd), population survival is the weighted average of stratum survival probabilities.{{cite:pishro_nik2014}} (§1.4.2) The observed data alone cannot establish independent censoring; its plausibility depends on how the study was run. If the sickest patients leave a cancer study early, an analysis that ignores the reason will tend to overestimate the average survival time. If sick men leave more often than sick women, a comparison of men and women can make the men look longer-lived.{{cite:james_islr2021}} (Ch. 11, §11.2, pp. 463–464)

Parametric models use the [exponential distribution](exponential-distribution.qmd) or the [Weibull distribution](weibull-distribution.qmd) when a simple shape for the hazard is plausible. The [proportional-hazards model](proportional-hazards-model.qmd) is the regression that multiplies a baseline hazard by a covariate factor. A life-test engineer who needs the reliability of a subsystem of independent parts multiplies the component reliabilities instead of fitting a regression at all. If each of two processors has reliability $0.9$ at the horizon of interest, the pair that must both work has reliability $0.9^2=0.81$.{{cite:nist_reliability2002}} (§8.1.2.2){{cite:james_islr2021}} (Ch. 11, §11.5.2, p. 471)

## Worked example

Four records, in months: a death at 2, a censoring at 4, a death at 5, and a death at 8.

At the first death the risk set has size 4 and there is 1 death, so the factor is $(4-1)/4=3/4$. The estimated survival just after 2 months is $3/4$.

At 5 months the patient censored at 4 months is no longer at risk. The risk set has size 2 and there is 1 death, so the factor is $1/2$. The estimated survival just after 5 months is

$$
\frac34\times\frac12=\frac38.
$$


At 8 months the last patient dies and the estimate is 0. The curve is flat between the death times. The censoring at 4 months does not draw a drop. It only removes one person from the later risk sets.

A separate reliability calculation uses the product rule for independent components. Two components, each with reliability $0.9$, both required, have reliability $0.81$.

**Your turn.** Three patients: a death at 1 month, a censoring at 3 months, and a death at 6 months. What is the product-limit estimate of survival just after 1 month?

::: {.callout-tip collapse="true" title="Answer"}
All three patients are at risk at 1 month and one dies, so the estimate is $(3-1)/3=2/3$.
:::

## Common misconceptions

The recorded time is not the event time whenever $\delta=0$. Putting the censoring times into an ordinary average of "lifetimes" treats losses as deaths. The product-limit estimate drops only at deaths.{{cite:kaplan_meier1958}} (p. 457){{cite:james_islr2021}} (Ch. 11, §11.1, p. 462)

The hazard is not a probability and need not be smaller than one. It is a conditional rate per unit time. Reading $h(t)=2$ as "a 200 percent chance of death" confuses the rate with the probability of an event in one whole year.{{cite:james_islr2021}} (Ch. 11, §11.5.1, pp. 469–470)

Multiplying component reliabilities is valid for independent components that must all survive. Shared shocks, a common power supply, or two patients exposed to the same outbreak violate the product. The curve for a system is then not the square of the curve for one part.{{cite:nist_reliability2002}} (§8.1.2.2)

A proportional-hazards coefficient is a multiplier of the hazard, constant in time, under the assumption that the hazards do not cross. It is not a difference in mean survival, and it is not evidence that censoring was independent.{{cite:james_islr2021}} (Ch. 11, §11.5.2, (11.14), p. 471)

## History

Life tables and actuarial estimates are the older technology for the same probability. Kaplan and Meier, in 1958, treated the estimation problem directly: incomplete measurements on a sample, with life testing and medical follow-up as the leading examples, and with the empirical proportion of survivors as the answer when there are no losses. They also set the actuarial estimates, which group time and shorten the product, beside the product-limit estimate, which keeps a factor at each observed death. The independence of lifetime and potential loss time is assumed in that paper, and the authors say the assumption deserves scrutiny in careful practice.{{cite:kaplan_meier1958}} (p. 457)

Engineering reliability calculations use the same $S(t)$ for systems of components, under the name reliability function, with the product rule for independent parts. Clinical research adopted the product-limit curve as a standard display and then added regression on covariates through the hazard. The proportional-hazards form leaves the baseline hazard free and estimates only the covariate multipliers. The field's later textbooks put censoring, the product-limit curve, the log-rank comparison, and the proportional-hazards regression in one chapter, because the data are censored more often than they are complete.{{cite:nist_reliability2002}} (§8.1.2.2){{cite:james_islr2021}} (Ch. 11, §11.3 and §11.5.2, pp. 464–466 and 471)

## Connections

Survival analysis borrows the [survival function](survival-function.qmd) from probability and returns it as an estimand under censoring. The [hazard rate](hazard-rate.qmd) is the instantaneous risk among those still event-free. [Censoring](censoring-statistics.qmd) is the pattern in which one end of a duration is unobserved. The subject is a central part of [medical statistics](medical-statistics.qmd) and of reliability as a branch of [quality control](quality-control.qmd). A Kaplan–Meier curve that drops only at deaths, a hazard that is a rate per unit time, and a covariate model that multiplies that hazard are three different summaries. Reading the curve as if every patient had been observed until death, or reading the hazard as a probability, confuses the summary with the design that made the times incomplete.{{cite:kaplan_meier1958}} (p. 457){{cite:nist_reliability2002}} (§8.1.2.2){{cite:james_islr2021}} (Ch. 11, §11.5.1, pp. 469–470)
