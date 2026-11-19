## Lead context

Five components are put on test for a fixed time. Some fail at recorded hours. Others are still working when the test stops. Those survivors are not failures at the stopping time, and they are not blank rows. Censoring is the name for a record that says a lifetime exceeds a time, or falls inside an interval, without giving the exact failure time. Reliability testing meets the pattern whenever not every unit on test fails. Medical follow-up meets it whenever a patient is last seen well.

## Motivating example

A clinic follows patients after treatment and records the time of relapse. Some patients move away. For a patient last seen well at month 15, the relapse time is known only to be greater than 15 months. Dropping that patient analyses only the patients who stayed. Treating month 15 as a relapse pretends the event happened then. The record is usable as a survival past month 15. That is less information than an exact time and more information than a blank. In a life test the same record appears when the clock is stopped at a pre-chosen time $T$ and some units are still working. The NIST handbook calls the resulting data censored, and it calls the fixed-time version right censoring because the failure times larger than $T$ are the ones missing.{{cite:nist_censoring2002}} (§8.1.3.1)

## Definition

Suppose $n$ non-repairable units are tested. In Type I censoring the stopping time $T$ is fixed in advance. If $r$ units fail at exact times $t_1,\ldots,t_r$ and the other $n-r$ are still working at $T$, the data are right censored at $T$. Here $T$ is chosen and $r$ is random, because the number of failures is not known until the test is run. In Type II censoring the number of failures $r$ is fixed and the test runs until the $r$th failure, so the stopping time $T=t_r$ is random. The advantage is that the number of observed failure times is known when the test is planned. An open-ended random test time is the practical cost, which is why the handbook describes Type II testing as rarely used.{{cite:nist_censoring2002}} (§8.1.3.1)

Interval or readout censoring replaces an exact time by a window in which the failure occurred. In the general, multicensored case each unit contributes one of three things: a run time without failure, an exact failure time, or an interval known to contain the failure. The units may have different run times and different windows.{{cite:nist_censoring2002}} (§8.1.3.1)

The [survival function](survival-function.qmd) is the probability being estimated. Kaplan and Meier write $P(t)$ for the probability of surviving past $t$, and they study a nonparametric estimate of that function from incomplete observations. A right-censored time enters a parametric likelihood through the probability of lasting past the censoring time. A failure at an exact time enters through the density. The NIST account of maximum likelihood defines the likelihood as the probability of the observed sample given the model, and it states that the same maximisation applies to censored and multicensored samples. For a Type I sample the observed records are $r$ exact failures and $n-r$ survivals past the fixed time $T$, so the likelihood is built from those two kinds of contribution.{{cite:kaplan_meier1958}} (p. 459, §1.2){{cite:nist_censoring_mle2002}} (§8.4.1.2){{cite:nist_censoring2002}} (§8.1.3.1)

## Properties

The product-limit estimator uses the failures and keeps the censored units in the risk set only while they are still under observation. The handbook's one-failure-at-a-time steps are: order the failure times; let $n_i$ be the number of units still operating just before the $i$th failure; estimate the reliability at the first failure by $(n_1-1)/n_1$; and multiply by $(n_i-1)/n_i$ at each later failure. A unit removed without failure counts in the $n_i$ only through the last failure time before it was removed, and not after. It does not create a drop of its own. Two failures at the same time multiply as two successive single-failure factors, which equals $(n-d)/n$ when $d$ units fail together out of $n$ at risk.{{cite:nist_kaplan2002}} (§8.2.1.5)

Kaplan and Meier describe this product-limit form as the nonparametric estimate aimed at the whole class of distributions, and as a limiting case of the actuarial, life-table estimates that group time into intervals. No Weibull or lognormal shape is assumed. Exact failure times are required for the version the handbook sets out. Interval censoring needs the window itself. A substitute exact time at the middle of the window is a different estimator.{{cite:kaplan_meier1958}} (p. 461){{cite:nist_kaplan2002}} (§8.2.1.5)

Type I and Type II censoring produce different sampling distributions because one fixes the clock and the other fixes the number of events. Both are right censoring. Competing failure modes are handled by treating a failure from a mode that is not under study as a censoring time for the mode that is. That step assumes the modes are independent in the sense the analysis uses: the time of the other mode carries no extra information about the mode under study beyond the time already recorded.{{cite:nist_censoring2002}} (§8.1.3.1)

Maximum likelihood estimates from censored samples have the large-sample properties the handbook lists: they become unbiased minimum-variance estimators as the sample grows, and they are approximately normal, so a standard error can be computed. With fewer than about five failures, and sometimes with fewer than ten, those large-sample properties do not apply and the estimates can be badly biased. The likelihood is still defined. The normal approximation to it is not.{{cite:nist_censoring_mle2002}} (§8.4.1.2)

## Worked example

Five units are observed. Failures occur at times 2, 5, and 5. One unit is censored at time 3, and one is still under observation at the last failure. Order the information. At time 2 all five units are at risk and one fails, so the factor is $(5-1)/5=4/5$. The censoring at time 3 removes a unit and does not multiply by a failure factor. At time 5 three units remain and two fail. Applying the single-failure step twice gives $(3-1)/3$ and then $(2-1)/2$, and the product of those two factors is $1/3$, the same as $(3-2)/3$. The product-limit estimate at time 5 is

$$
\widehat S(5)=\frac{4}{5}\times\frac{1}{3}=\frac{4}{15}.
$$


{{cite:nist_kaplan2002}} (§8.2.1.5)

**Your turn.** Suppose the observation at time 3 is a failure rather than a censoring. Using the same product of conditional factors, what is $\widehat S(5)$?

::: {.callout-tip collapse="true" title="Answer"}
The factors are $4/5$ at time 2, then $3/4$ at time 3 (four units at risk, one failure), then $1/3$ at time 5 (three units at risk, two failures). The product is $4/5 \times 3/4 \times 1/3 = 1/5$.
:::

## Assumptions and limits

The standard product-limit and likelihood calculations assume that the censoring mechanism does not depend on the unseen failure time, at least not beyond the covariates in the model. If the units that are about to fail are the ones removed, the censored times are informative and the reliability curve can be too high. The handbook's rule that a removed unit counts only up to the last failure before removal is the bookkeeping for non-informative removal. It is the wrong bookkeeping when removal is caused by the approach of failure.{{cite:nist_kaplan2002}} (§8.2.1.5){{cite:nist_censoring2002}} (§8.1.3.1)

Type I censoring with no failures, $r=0$, still says that all $n$ lifetimes exceed $T$. A model can use that fact through the survival probability past $T$. It cannot locate a failure time inside $(T,\infty)$. Type II censoring fixes $r$ and leaves $T$ random, so the plan knows how many failures it will see and does not know when the test will end. Interval censoring needs the window. A parametric maximum likelihood estimate with very few failures remains a maximum of the censored likelihood, and the handbook's warning is that the large-sample standard error does not apply.{{cite:nist_censoring2002}} (§8.1.3.1){{cite:nist_censoring_mle2002}} (§8.4.1.2)

## History

Life tables already grouped time and multiplied conditional survival fractions. Kaplan and Meier made the non-parametric version explicit for arbitrary censoring times: the product-limit estimate, a limiting case of those actuarial products as the intervals shrink to the observed failure times. A censored unit leaves the later risk sets without counting as a death. Parametric likelihoods for Type I and Type II samples do the same job inside a named distribution, by scoring a censored unit with the probability of surviving past its censoring time rather than with a density at a failure. Both devices are now routine in medical follow-up and in reliability tests. The handbook's sections on censoring, on the Kaplan–Meier product, and on maximum likelihood are the engineering statement of that pair of devices.{{cite:kaplan_meier1958}} (p. 461){{cite:nist_censoring2002}} (§8.1.3.1){{cite:nist_kaplan2002}} (§8.2.1.5)
