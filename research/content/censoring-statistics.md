

## Lead context

Five components are put on test for 10 hours. Three fail, at 2, 4, and 7 hours. Two are still working when the test stops. Those two are not failures at 10 hours, and they are not missing data in the ordinary sense. Censoring is the name for an observation that says a lifetime exceeds a time, or falls inside an interval, without giving the exact failure time.

## Motivating example

A clinic follows patients after treatment and records the month of relapse. Some patients move away. For a patient last seen well at month 15, the relapse time is known only to be greater than 15 months. Dropping that patient pretends the study never included them. Treating month 15 as a relapse pretends the event happened then. The record is usable as a survival past month 15, which is less information than an exact time and more information than a blank.{{cite:bonita2006}} (Ch. 2, "Incidence"){{cite:nist_censoring2002}} (§8.1.3.1, "Censoring")

## Definition

Suppose \(n\) non-repairable units are tested. In Type I censoring the stopping time \(T\) is fixed in advance. If \(r\) units fail at exact times \(t_1,\ldots,t_r\) and the other \(n-r\) are still working at \(T\), the data are right censored at \(T\). Here \(T\) is chosen and \(r\) is random. In Type II censoring the number of failures \(r\) is fixed and the test runs until the \(r\)th failure, so the stopping time is random. Interval or readout censoring replaces an exact time by a window in which the failure occurred. In the general case each unit contributes one of three things: a run time without failure, an exact failure time, or an interval known to contain the failure.{{cite:nist_censoring2002}} (§8.1.3.1, "Censoring")

The [survival function](survival-function.qmd) \(S(t)=\Pr(T>t)\) is what these records are used to estimate. A right-censored time \(c\) enters a likelihood through \(S(c)\), and a failure at \(t\) enters through the density. For a parametric model with distribution function \(F\) and density \(f\), the Type I likelihood has the form
\[
L \propto \Bigl(\prod_{i=1}^{r} f(t_i)\Bigr)\,[1-F(T)]^{n-r}.
\]
With no censoring the second factor is absent and the likelihood is the ordinary product of densities.{{cite:nist_censoring_mle2002}} (§8.4.1.2, "Maximum likelihood estimation")

A lifetime is a point on the time axis. A censored observation is an interval that is known to contain that point. Right censoring gives an interval \((c,\infty)\): the event had not happened by time \(c\). The person or the component still contributes every moment they were watched. In a person-time rate, each subject adds time to the denominator until the event or until follow-up stops, and only an event enters the numerator. The stopped follow-up is the censored piece.{{cite:bonita2006}} (Ch. 2, "Incidence")

Life tests, medical follow-up, and warranty records are the usual settings. A [Weibull](weibull-distribution.qmd) or [exponential](exponential-distribution.qmd) model is fitted by [maximum likelihood](maximum-likelihood.qmd) with the censored contribution included. A [proportional hazards model](proportional-hazards-model.qmd) compares groups without specifying the baseline hazard, and it still needs a censoring assumption: given the covariates, the censoring time should not carry extra information about the event time. Person-time incidence in [epidemiology](epidemiology.qmd) is the same bookkeeping for a rate.{{cite:bonita2006}} (Ch. 2, "Incidence"){{cite:nist_censoring_mle2002}} (§8.4.1.2)

A censored time is not a failure at the censoring time, and it is not a missing row to be deleted. Deleting the censored units estimates survival only among units that failed during the study, which is a different population. Recording the censoring time as if it were a failure pulls the estimated lifetime downward. Right censoring is also different from truncation: under truncation, units that fall outside a window may never enter the sample at all, so even the count of those units is unknown.{{cite:nist_censoring2002}} (§8.1.3.1, "Censoring")

The [survival function](survival-function.qmd) is the probability being estimated. The [hazard rate](hazard-rate.qmd) is the instantaneous risk among those still event-free. The [reliability function](reliability-function.qmd) is the same object in engineering life tests. [Missing data](missing-data.qmd) is the broader label; censoring is the special pattern in which the missing piece is one end of a duration. [Actuarial science](actuarial-science.qmd) meets the same pattern when a policy is observed only until it lapses.

## Properties

The product-limit estimator uses the failures and keeps the censored units in the risk set only while they are still under observation. At a failure time \(t_j\), if \(n_j\) units are still at risk and \(d_j\) fail, the conditional survival factor is \(1-d_j/n_j\). A unit censored at \(c\) is counted in \(n_j\) for failure times before \(c\) and is omitted afterwards. It does not create a drop of its own. The estimated survival is the product of those factors over failure times up to \(t\).{{cite:nist_kaplan2002}} (§8.2.1.5, "Empirical model fitting")

Type I and Type II censoring produce different sampling distributions because one fixes the clock and the other fixes the number of events. Both are right censoring. Competing failure modes are handled by treating a failure from a mode that is not under study as a censoring time for the mode that is, which is a modelling choice about independence of the modes.{{cite:nist_censoring2002}} (§8.1.3.1, "Censoring")

## Worked example

Five units are observed. Failures occur at times 2, 5, and 5. One unit is censored at time 3, and one is still under observation at the last failure. Order the information. At time 2 all five units are at risk and one fails, so the factor is \(1-1/5=4/5\). The censoring at time 3 removes a unit and does not multiply by a failure factor. At time 5 three units remain and two fail, so the factor is \(1-2/3=1/3\). The product-limit estimate at time 5 is
\[
\widehat S(5)=\frac{4}{5}\times\frac{1}{3}=\frac{4}{15}.
\]
{{cite:nist_kaplan2002}} (§8.2.1.5)

**Your turn.** Suppose the observation at time 3 is a failure rather than a censoring. Using the same product of conditional factors, what is \(\widehat S(5)\)?

::: {.callout-tip collapse="true" title="Answer"}
The factors are \(4/5\) at time 2, then \(3/4\) at time 3 (four units at risk, one failure), then \(1/3\) at time 5 (three units at risk, two failures). The product is \(4/5 \times 3/4 \times 1/3 = 1/5\).
:::

## Assumptions and limits

The standard product-limit and likelihood calculations assume that the censoring mechanism does not depend on the unseen failure time, at least not beyond the covariates in the model. If patients who are becoming ill are the ones who leave, the censored times are informative and the curve can be too optimistic. Type I censoring with no failures, \(r=0\), still says that all \(n\) lifetimes exceed \(T\), and a model can use that fact, but it cannot locate a failure time inside \((T,\infty)\). Interval censoring needs the window, not a substitute exact time at the middle of the window, if the likelihood is to stay honest.{{cite:nist_censoring2002}} (§8.1.3.1){{cite:bonita2006}} (Ch. 2, "Incidence")

## History

Life tables already had to cope with people who left observation. The product-limit estimator made the non-parametric version of that idea explicit for arbitrary censoring times: multiply the conditional survival fractions at the observed failure times, and let a censored unit leave the later risk sets without counting as a death. Parametric likelihoods for Type I and Type II samples do the same job inside a named distribution, by replacing the density of a censored unit with its survival probability. Both devices are now routine in medical follow-up and in reliability tests.{{cite:nist_kaplan2002}} (§8.2.1.5){{cite:nist_censoring_mle2002}} (§8.4.1.2)
