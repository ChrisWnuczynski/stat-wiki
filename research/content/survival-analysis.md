

## Lead context

Patients leave a study, machines are taken off test, and a report is due before every unit has failed. Survival analysis is the set of methods for event times under that kind of incomplete observation. The quantity being estimated is often a probability of still being free of the event, or a rate among those still at risk. The field is wider than any one formula for that probability. It includes how the times were cut short, how groups are compared, and how covariates enter the rate.

## Motivating example

Five patients are followed for a year. Their observed times, in months, are 2, 4, 6, 8, and 12, and the patient at 6 months is still alive when records stop, so that time is censored. Four of the five times are deaths. A naive mean that treats the censored 6 as a death uses (2+4+6+8+12)/5 = 6.4. That calculation ends the censored life at the last visit. The survival function at 6 months is the proportion still alive just after 6, which on these records is the two later deaths still ahead plus the person censored, counted by a method that does not pretend the censoring time is a death. The point of the analysis is to keep the censored time in the risk set until it stops, rather than to average the recorded numbers as if they were complete lifetimes.

## Definition

Survival analysis studies the time until an event: death, failure, discharge, or another defined transition. The [survival function](survival-function.qmd) $S(t)$ is the probability that the event time exceeds $t$. In reliability work the same function is called the reliability function $R(t)$, and $R(t)=1-F(t)$ because a unit has either failed by $t$ or it has not. The field covers both the biomedical follow-up study and the industrial life test. It is not only the definition of $S(t)$. A complete sample of failure times can be summarised by an ordinary empirical distribution. The subject becomes survival analysis when some times are incomplete, or when the interest is the risk among those still surviving, or when several groups or covariates are compared.{{cite:kaplan_meier1958}} (p. 458){{cite:nist_reliability2002}} (§8.1.2.2)

Censoring is the usual incompleteness. In a medical follow-up, contact is lost, or a death occurs from a cause one wishes to set aside. In a life test, a tube breaks for an irrelevant reason, or the rig is needed for something else, or the report cannot wait. Each of those records says that the event time exceeded the time last seen, not that the event happened then. Treating the recorded time as if it were the event time answers a different question.{{cite:kaplan_meier1958}} (p. 458)

## Statistical use

With a complete sample the empirical distribution puts mass $1/N$ at each observed time. With censoring, the product-limit estimator, introduced for this problem by Kaplan and Meier, updates the survival probability only at observed event times and only among those still under observation. The [hazard rate](hazard-rate.qmd) is the instantaneous risk among those who have reached that time; it is not a probability and need not be smaller than one. Parametric models use the [exponential distribution](exponential-distribution.qmd) or the [Weibull distribution](weibull-distribution.qmd) when a simple shape for the hazard is plausible. The [proportional-hazards model](proportional-hazards-model.qmd) lets covariates multiply a baseline hazard by a factor that does not change with time. Comparing two groups with a rank test is the analogue of a two-sample test when the outcome is a censored time.{{cite:kaplan_meier1958}} (p. 458){{cite:nist_reliability2002}} (§8.1.2.2)

Independent components combine by multiplication when all of them must survive. If each microprocessor has reliability $R_m(t)$ and the processor uses two that must both work, the pair has reliability $R_m(t)^2$. That rule fails when the components share a cause of failure. A medical analogue is two patients in the same ward during an outbreak: their event times are not independent just because the survival curve was drawn as if they were.{{cite:nist_reliability2002}} (§8.1.2.2)


## Worked example

Five patients are followed for a year. Their observed times, in months, are 2, 4, 6, 8, and 12, and the patient at 6 months is still alive when records stop, so that time is censored. Four of the five times are deaths. A naive mean that treats the censored 6 as a death uses (2+4+6+8+12)/5 = 6.4. That calculation ends the censored life at the last visit. The survival function at 6 months is the proportion still alive just after 6, which on these records is the two later deaths still ahead plus the person censored, counted by a method that does not pretend the censoring time is a death. The point of the analysis is to keep the censored time in the risk set until it stops, rather than to average the recorded numbers as if they were complete lifetimes.

**Your turn.** Using the same records, recompute the featured summary and state which population quantity it estimates.

::: {.callout-tip collapse="true" title="Answer"}
Recompute the displayed summary from the same records. It estimates the quantity named in the example, for these records only.
:::



The integer list used above is a device for keeping the target fixed. With 19 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.
## History

Life tables and actuarial estimates are the older technology for the same probability. The 1958 product-limit paper treated the modern estimation problem directly: incomplete measurements on a sample, with medical follow-up and equipment testing as the two leading examples, and with the empirical distribution function as the complete-data reference. Engineering reliability calculations use the same $S(t)$ for systems of components. Clinical research adopted the estimator as a standard display and then added regression on covariates. The field's journals and software followed the data, which were censored more often than they were complete.{{cite:kaplan_meier1958}} (p. 458){{cite:nist_reliability2002}} (§8.1.2.2)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 19. Their total is 190, so their mean is 10.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 8.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Survival analysis has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 10.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [survival function](survival-function.qmd), [hazard rate](hazard-rate.qmd), [exponential distribution](exponential-distribution.qmd), [Weibull distribution](weibull-distribution.qmd).

Two further limits are algebraic. The sum of deviations from the mean 10.0 is zero, so the mean is the least-squares centre of these 19 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 10.0.

## Connections

Survival analysis borrows the [survival function](survival-function.qmd) from probability and returns it as an estimand under censoring. It is a central part of [medical statistics](medical-statistics.qmd) and of reliability as a branch of [quality control](quality-control.qmd). A Kaplan–Meier curve that drops only at deaths, a hazard that is a rate per unit time, and a covariate model that multiplies that hazard are three different summaries. Reading the curve as if every patient had been observed until death, or reading the hazard as a probability, confuses the summary with the design that made the times incomplete.{{cite:kaplan_meier1958}} (p. 458){{cite:nist_reliability2002}} (§8.1.2.2)
