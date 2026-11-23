## Lead context

The Kaplan–Meier estimator, also called the product-limit estimator, is the
standard nonparametric estimate of a survival function from right-censored
time-to-event data. It estimates, at each time $t$, the probability of
remaining event-free beyond $t$, using every subject for exactly as long as
that subject was observed — no longer. A subject censored at 4 months
contributes the information that they survived at least 4 months, and nothing
about what happened afterwards. The estimator was introduced by Kaplan and
Meier in 1958 as the distribution, unrestricted as to form, that maximises
the likelihood of the incomplete observations {{cite:kaplan_meier1958}}
(pp. 457–458).

## The problem: follow-up ends before the event

Let $T$ be the true event time — the time of death, relapse, failure, or
whatever event is of interest — and let $C$ be the censoring time, the time
at which observation would end for a reason other than the event, such as the
end of the study or loss to follow-up. What is observed for each subject is
$Y = \min(T, C)$, together with an indicator $\delta$ that records whether
the event was observed ($\delta = 1$ when $T \le C$) or the observation was
censored ($\delta = 0$ when $T > C$) {{cite:james_islr2021}} (eq. 11.1).
The target is the [survival function](survival-function.qmd)
$S(t) = P(T > t)$, the probability of surviving beyond time $t$
{{cite:james_islr2021}} (eq. 11.2).

The difficulty is that a censored observation is not an event time and not
a survival time: it is a lower bound on $T$. Discarding censored subjects
throws away the information that they survived at least until censoring,
while treating a censoring time as if it were the event time understates
survival. The Kaplan–Meier estimator avoids both errors by working with
conditional probabilities among the subjects still at risk.

## Two naive proportions, and why both fail

James and colleagues motivate the estimator with the BrainCancer data, and
the example is worked in full in [survival-analysis](survival-analysis.qmd):
in a series of 88 patients, the proportion known to have survived past 20
months is $48/88$, about $55\%$, while restricting to the 71 patients not
censored by 20 months gives $48/71$, about $68\%$. The first figure
implicitly assumes every censored patient had the event before 20 months;
the second discards the censored patients entirely. The Kaplan–Meier
estimate is $71\%$, higher than either naive figure, because it credits
each censored patient with survival up to their censoring time and no
further {{cite:james_islr2021}} (§11.3, pp. 464–465). The rest of this
article is the machinery behind that correction.

## The product-limit construction

Order the distinct event times as $t_1 < t_2 < \dots < t_K$. At event time
$t_j$, let $n_j$ be the number of subjects at risk just before $t_j$ — those
whose observed time $Y$ is at least $t_j$, so they are known to be alive and
under observation immediately before $t_j$ — and let $d_j$ be the number of
events at $t_j$. The set of subjects at risk at $t_j$ is the risk set.
Survival beyond $t_j$ factorises, by the law of total probability, into
survival beyond $t_{j-1}$ and then survival from $t_{j-1}$ to $t_j$ given
survival to $t_{j-1}$. Estimating each conditional survival probability by
the fraction of the risk set that survives the moment, $(n_j - d_j)/n_j$,
and multiplying gives the Kaplan–Meier estimator

$$\widehat{S}(t) = \prod_{j: t_j \le t} \left(1 - \frac{d_j}{n_j}\right),$$

with $\widehat{S}(t) = 1$ for $t < t_1$ {{cite:james_islr2021}} (eq. 11.3).
Equivalently, $\widehat{S}(t_j) = \widehat{S}(t_{j-1}) (1 - d_j/n_j)$: each
event time multiplies the previous estimate by the fraction of those at risk
who did not have the event. This is the product-limit formula of Kaplan and
Meier {{cite:kaplan_meier1958}} (pp. 462–464). It is also the nonparametric
maximum likelihood estimator of $S$: among all distributions, with no
assumed shape, it is the one that maximises the likelihood of the observed
data {{cite:kaplan_meier1958}} (pp. 457–458).

Three features of the construction deserve attention. First, censoring
never causes a step: a censored subject simply leaves the risk set, so later
factors $(1 - d_j/n_j)$ are computed over fewer subjects, and each later
event therefore produces a larger drop. Second, ties are handled by counting
all $d_j$ events at $t_j$ together in a single factor $(1 - d_j/n_j)$; the
formula does not split tied event times into separate factors. Third, when
an event time and a censoring time coincide, the convention is to treat the
deaths as occurring slightly before the losses at that time, so the censored
subjects are still counted in $n_j$ for the events at $t_j$ and leave the
risk set only afterwards {{cite:kaplan_meier1958}} (pp. 461–462).

No shape is assumed for $S$: the estimator is nonparametric, giving
estimates of the reliability (survival) function from complete or censored
data without assuming a particular distribution model such as Weibull or
lognormal {{cite:nist_kaplan2002}} (§8.2.1.5). Exact event times are
required; grouped data need the actuarial (life-table) approximation instead.

## What the steps mean

$\widehat{S}$ is a step function: it is constant between event times and
drops only at event times, by an amount that depends on how many subjects
are still at risk. A drop of $d_j/n_j$ times the current level is large when
the risk set is small, which is why Kaplan–Meier curves often look alarming
in their right-hand tail, where few subjects remain. The curve is usually
drawn with tick marks at censoring times; the ticks mark information
exhausted, not events {{cite:bland_altman1998}} (pp. 1572–1580).

The estimate at a time $t$ is a statement about the population from which
the sample was drawn, not a description of the sample alone: $\widehat{S}(t)$
estimates the probability that a member of that population survives beyond
$t$. That interpretation is exactly what the non-informative-censoring
assumption buys, and it is what fails when the assumption fails (see
Statistical use, assumptions and limits below).

Because the estimator is a product of conditional probabilities, its
sampling behaviour is governed by the risk sets, not by the total sample
size alone. Two studies with the same number of subjects can have very
different precision at late times if one of them has much heavier censoring.

## Greenwood's formula and confidence intervals

A point estimate without a measure of uncertainty is of limited use, and
the uncertainty in $\widehat{S}(t)$ grows as the risk sets shrink. Greenwood's
formula estimates the variance of the Kaplan–Meier estimator as

$$\widehat{\text{Var}}\{\widehat{S}(t)\} = \widehat{S}(t)^2 \sum_{j: t_j \le t} \frac{d_j}{n_j (n_j - d_j)},$$

a formula derived by Greenwood for life tables in 1926 and given in its
Kaplan–Meier form by Kaplan and Meier {{cite:kaplan_meier1958}}
(pp. 465–466). The sum accumulates one term per event time up to $t$; each
term grows as $n_j$ falls, so the variance accumulates fastest late in
follow-up. The estimated standard error is
$\widehat{\text{SE}}\{\widehat{S}(t)\} = \widehat{S}(t) \sqrt{\widehat{G}(t)}$,
where $\widehat{G}(t)$ denotes the sum above. Kaplan and Meier stress that
this is an asymptotic expression for the variance, so intervals built from
it are approximate, not exact {{cite:kaplan_meier1958}} (pp. 465–466).

A direct normal interval, $\widehat{S}(t) \pm z_{1-\alpha/2}\,
\widehat{\text{SE}}\{\widehat{S}(t)\}$, is easy to compute but can extend
below 0 or above 1, which is impossible for a probability. The standard
remedy is to build the interval on the log-log scale and transform back.
Write $\theta(t) = \log[-\log S(t)]$, defined when $0 < S(t) < 1$. By the
delta method, the standard error of $\widehat{\theta}(t) =
\log[-\log \widehat{S}(t)]$ is approximately
$\sqrt{\widehat{G}(t)} / |\log \widehat{S}(t)|$, and the log-log
transformation has variance
$\text{Var}(\log[-\log \widehat{S}(t)]) =
\text{Var}(\log \widehat{S}(t)) / (\log \widehat{S}(t))^2$
{{cite:rodriguez2018}} (slide 5). An approximate $100(1-\alpha)\%$ interval
for $S(t)$ is therefore

$$\left[\exp\left\{-\exp\left(\widehat{\theta}(t) + z_{1-\alpha/2}
\frac{\sqrt{\widehat{G}(t)}}{|\log \widehat{S}(t)|}\right)\right\},\
\exp\left\{-\exp\left(\widehat{\theta}(t) - z_{1-\alpha/2}
\frac{\sqrt{\widehat{G}(t)}}{|\log \widehat{S}(t)|}\right)\right\}\right],$$

where $z_{1-\alpha/2}$ is the corresponding standard normal quantile
($1.96$ for a 95% interval). Note the reversal: because
$s \mapsto \exp\{-\exp(s)\}$ is decreasing, the upper end of the
$\theta$-interval gives the lower end of the $S$-interval. The resulting
interval lies inside $(0, 1)$ and is asymmetric, stretching further on the
side towards which the estimate is less precisely determined. It is a
pointwise interval — valid, approximately, at the single time $t$ — not a
simultaneous band for the whole curve. Standard errors and confidence
intervals for the estimated survival probabilities are found by Greenwood's
method {{cite:bland_altman1998}} (pp. 1572–1580).

Greenwood's formula needs $d_j < n_j$ at every event time included in the
sum. If the last subject at risk has the event, so $d_j = n_j$ and
$\widehat{S}$ drops to zero, the corresponding term is undefined; the
variance estimate is then not defined at or beyond that time. This is one
more reason to report Greenwood intervals only where the risk set is not
degenerate.

## Median survival and restricted mean

Two summaries are read off the curve more often than any single value
$\widehat{S}(t)$. The median survival time is the smallest time $t$ at which
$\widehat{S}(t) \le 0.5$ — the time by which half the population is estimated
to have had the event. It is a property of the curve, not of the observed
event times: a median computed from the observed events alone, ignoring
censoring, is biased. If the curve never falls to $0.5$ within follow-up,
the median is not reached and should be reported as not estimable, not
extrapolated; Rich and colleagues' small example illustrates the reporting,
with median survival of 3 years in one group and 1 year in the other
{{cite:rich2010}} (pp. 331–336).

The mean survival time is the area under the survival curve, but the
unrestricted mean is not estimable when follow-up ends before the curve
reaches zero — which is the usual case. Kaplan and Meier instead define the
mean life limited to a time $L$: the mean of $\min(T, L)$, estimated as the
area under $\widehat{S}$ up to $L$ {{cite:kaplan_meier1958}} (pp. 467–468).
This is now usually called the restricted mean survival time,
$\text{RMST}(L) = \int_0^L \widehat{S}(t)\, dt$. It is the average event-free
time over the window $[0, L]$, and it is defined even when the median is not
reached. The horizon $L$ must be stated alongside the number; an RMST
without its $L$ is uninterpretable, and RMSTs with different horizons are
not comparable.

## Large-sample behaviour

Kaplan and Meier show that the product-limit estimate is consistent and of
negligible bias: $\widehat{S}(t)$ converges in probability to $S(t)$ provided
only that the number of items observable to $t$ grows without bound
{{cite:kaplan_meier1958}} (p. 479). Consistency is therefore a statement
about the risk set at $t$, not about the initial sample size: a study can
start with many subjects and still estimate late survival badly if almost
all of them are censored early. The effective sample size — the size of an
uncensored sample that would give the same variance — is nonincreasing in
$t$ and falls as censoring accumulates {{cite:kaplan_meier1958}}
(pp. 467–468). In small samples, and especially in the tail, the Greenwood
standard error and the log-log interval are approximations whose coverage
can be poor; the log-log transformation improves the normal approximation
but does not remove the small-sample problem {{cite:rodriguez2018}}
(slide 5).

## No censoring, heavy censoring, and the end of follow-up

If there is no censoring, the product telescopes: every factor
$(n_j - d_j)/n_j$ cancels with its neighbours except for the first
denominator and the last numerator, and the estimator reduces to the usual
empirical survival function, the observed proportion surviving beyond $t$
{{cite:kaplan_meier1958}} (p. 464). The Kaplan–Meier estimator is therefore
a genuine generalisation of the empirical survivor function, not a different
kind of object. Greenwood's formula likewise reduces to the ordinary
binomial variance in that case {{cite:rodriguez2018}} (slide 5).

Heavy censoring does the opposite. Each censoring shrinks the risk set
without adding an event, so later factors are computed over fewer subjects,
later drops are larger, and Greenwood's sum accumulates larger terms. The
curve becomes coarser and its intervals wider, and both effects accelerate
in the tail. A curve whose risk set has fallen to a handful of subjects
should not be read at face value at late times, however smooth it looks.

What happens after the last observation matters too. If the largest observed
time is an event, the curve may drop to zero and stay there. If the largest
observed time is a censoring, the estimate is undefined beyond it: the curve
is conventionally drawn flat at its last value, but that flat line is a
plotting convention, not an estimate. Kaplan and Meier state the point
explicitly — beyond the greatest observed lifetime, when that lifetime is a
loss, the estimate "can be regarded as lying between $0$ and"
$\widehat{S}$ at that time, "but is not more closely defined"
{{cite:kaplan_meier1958}} (p. 463). Nothing in the data distinguishes
"everyone died the next day" from "everyone lived for years", and the
estimator does not pretend otherwise.

## Worked example: eight patients, four events

Eight patients are followed after treatment, with times in months and
$1 =$ event, $0 =$ censored:

| Patient | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Time (months) | 2 | 3 | 4 | 6 | 6 | 7 | 9 | 12 |
| Event ($1$) / censored ($0$) | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |

There is a tie at 6 months (two events) and censorings at 4, 7 and 12 months.
The distinct event times are 2, 3, 6 and 9.

| Event time $t_j$ | At risk $n_j$ | Events $d_j$ | Factor $1 - d_j/n_j$ | $\widehat{S}(t_j)$ | Greenwood term $d_j / (n_j(n_j - d_j))$ |
|---:|---:|---:|---:|---:|---:|
| 2 | 8 | 1 | $7/8$ | $7/8 = 0.875$ | $1/56$ |
| 3 | 7 | 1 | $6/7$ | $3/4 = 0.750$ | $1/42$ |
| 6 | 5 | 2 | $3/5$ | $9/20 = 0.450$ | $2/15$ |
| 9 | 2 | 1 | $1/2$ | $9/40 = 0.225$ | $1/2$ |

At 6 months the risk set is 5, not 6: the patient censored at 4 months has
left it. The two events at 6 months enter as a single factor $3/5$, giving
$\widehat{S}(6) = (3/4) \times (3/5) = 9/20 = 0.45$. The curve is flat at
$0.75$ from 3 months up to (but not including) 6 months, so
$\widehat{S}(5) = 0.75$; the censoring at 4 months changes no value of
$\widehat{S}$, only the risk set for later times. After 9 months the curve
stays at $0.225$ until the last observation, a censoring at 12 months,
beyond which it is undefined.

**Greenwood standard error and 95% interval at 6 months.** The Greenwood
sum through 6 months is

$$\widehat{G}(6) = \frac{1}{56} + \frac{1}{42} + \frac{2}{15}
= \frac{15 + 20 + 112}{840} = \frac{147}{840} = \frac{7}{40} = 0.175.$$

Hence the estimated variance is
$\widehat{\text{Var}}\{\widehat{S}(6)\} = (9/20)^2 \times (7/40) =
567/16000 = 0.0354375$, and the standard error is
$\widehat{\text{SE}}\{\widehat{S}(6)\} = 0.45 \times \sqrt{0.175} \approx 0.188$.
For the log-log interval: $\log \widehat{S}(6) = \log 0.45 \approx -0.799$,
$\widehat{\theta}(6) = \log(0.799) \approx -0.225$, and
$\widehat{\text{SE}}\{\widehat{\theta}(6)\} = \sqrt{0.175}/0.799 \approx 0.524$.
With $z_{0.975} = 1.96$, the $\theta$-interval is
$-0.225 \pm 1.96 \times 0.524 = (-1.252,\ 0.802)$, which transforms back to

$$[\exp\{-\exp(0.802)\},\ \exp\{-\exp(-1.252)\}] \approx (0.108,\ 0.751).$$

So a 95% log-log interval for $S(6)$ is approximately $(0.108,\ 0.751)$.
For comparison, the plain normal interval $0.45 \pm 1.96 \times 0.188$ is
$(0.081,\ 0.819)$: wider on the upper side and symmetric by construction,
while the log-log interval is asymmetric about $0.45$, as it should be for
a quantity bounded between 0 and 1. Both are wide — with only 8 patients,
a survival probability of $0.45$ is compatible with a wide range of true
values — and both are approximate.

**Median and restricted mean.** The curve first falls to $0.5$ or below at
6 months ($\widehat{S}(6) = 0.45$), so the median survival time is 6 months.
The restricted mean to 9 months is the area under the curve to 9 months:

$$\text{RMST}(9) = 1 \times 2 + 0.875 \times 1 + 0.75 \times 3 + 0.45 \times 3
= 2 + 0.875 + 2.25 + 1.35 = 6.475\ \text{months}.$$

That is the average event-free time over the first 9 months, not an estimate
of mean lifetime: the curve is still at $0.225$ at 9 months, so the
unrestricted mean is not estimable from these data.

## Your turn

Six further patients are followed, with times in months and $1 =$ event,
$0 =$ censored:

| Patient | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| Time (months) | 1 | 2 | 4 | 4 | 5 | 8 |
| Event ($1$) / censored ($0$) | 1 | 0 | 1 | 1 | 0 | 1 |

Compute the Kaplan–Meier estimate at 1, 4 and 8 months, the median survival
time, and the Greenwood standard error and log-log 95% confidence interval
for $S(4)$.

::: {.callout-tip collapse="true" title="Answer"}

The distinct event times are 1, 4 and 8. At 1 month, $n_1 = 6$ and $d_1 = 1$,
so $\widehat{S}(1) = 5/6 \approx 0.833$. The censoring at 2 months leaves a
risk set of 4 at 4 months, where $d = 2$, so
$\widehat{S}(4) = (5/6) \times (2/4) = 5/12 \approx 0.417$. The censoring at
5 months leaves a risk set of 1 at 8 months, where the last patient has the
event, so $\widehat{S}(8) = 0$.

The median survival time is 4 months, the first time at which
$\widehat{S}$ falls to $0.5$ or below ($\widehat{S}(4) = 5/12 \approx 0.417$).

Greenwood's sum through 4 months is
$\widehat{G}(4) = 1/(6 \times 5) + 2/(4 \times 2) = 1/30 + 1/4 = 17/60
\approx 0.2833$. The estimated variance is
$(5/12)^2 \times (17/60) = 85/1728 \approx 0.0492$, so the standard error is
approximately $0.222$. For the log-log interval,
$\log \widehat{S}(4) \approx -0.875$, $\widehat{\theta}(4) \approx -0.133$,
and $\widehat{\text{SE}}\{\widehat{\theta}(4)\} = \sqrt{17/60}/0.875
\approx 0.608$. The interval is approximately $(0.056,\ 0.767)$. The plain
normal interval, $0.417 \pm 1.96 \times 0.222 \approx (-0.018,\ 0.851)$,
crosses below zero — one reason to prefer the log-log interval. Note also
that Greenwood's formula cannot be used at 8 months: there $n = d = 1$, so
the term $d/(n(n-d))$ is undefined.

:::

## Statistical use, assumptions and limits

The Kaplan–Meier estimator is the default first step in a survival analysis:
it describes one group's survival over time, supplies the curve that the
[log-rank test](log-rank-test.qmd) compares between groups, and provides the
nonparametric baseline against which model-based estimates are checked. It
is used wherever the question is "what fraction survive, and for how long?",
from clinical trials to reliability testing to customer churn, and it is the
right tool whenever the data are right-censored and no distributional shape
is to be assumed.

Its validity rests on the censoring being non-informative: the lifetime $T$
must be independent of the potential censoring time $C$, at least given any
features being conditioned on. Kaplan and Meier assume the lifetime to be
independent of the potential loss time, and warn that "in practice this
assumption deserves careful scrutiny" {{cite:kaplan_meier1958}}
(pp. 457–458). James and colleagues make the same point: the censoring
mechanism must be independent, in the sense that, conditional on the
features, the event time carries no information about the censoring time,
and whether that holds "is not possible to determine from the data itself"
{{cite:james_islr2021}} (§11.2). Bland and Altman list it as the first of
three assumptions behind the method: at any time, patients who are censored
must have the same survival prospects as those who continue to be followed
{{cite:bland_altman1998}} (pp. 1572–1580). If sicker patients drop out early, the
curve overestimates survival; if healthier patients are the ones lost, it
underestimates it. Administrative censoring at a fixed end of study is the
least worrying case; dropout related to prognosis is the most worrying, and
no calculation on the observed data can detect it.

Two further assumptions are easily overlooked. The survival probabilities
must be the same for subjects recruited early and late in the study — a
condition that fails if the case mix or ancillary treatment changes over a
long recruitment period — and the event must genuinely occur at the recorded
time, which fails when events are only detected at periodic examinations
(interval censoring) {{cite:bland_altman1998}} (pp. 1572–1580).

The estimator's limits are the limits of a single-sample description. It
does not adjust for covariates, so it cannot separate a treatment effect
from a difference in case mix; it does not compare groups, so a visual gap
between two curves is not a test (that is the log-rank test's job); it says
nothing beyond the last observation; and with competing events it answers
the wrong question if competing events are treated as censoring — see
[competing-risks](competing-risks.qmd). Its intervals are pointwise and
approximate, and in small samples or heavy censoring they can be wide
enough to be uninformative, which is itself a finding worth reporting.

## Common misconceptions

**"The curve shows the proportion of the original sample still alive."**
Only if there is no censoring. With censoring, $\widehat{S}(t)$ is a
product of conditional fractions over changing risk sets, not a count
divided by the initial $n$. In the worked example, 3 of 8 patients are
known alive at 9 months, yet $\widehat{S}(9) = 0.225$, not $3/8 = 0.375$:
the two patients censored before 9 months are not counted as survivors.

**"A censored patient counts as a survivor (or as a death)."** Neither. A
censored patient contributes survival up to the censoring time and then
leaves the risk set. Counting them as survivors understates risk; counting
them as events overstates it; dropping them entirely discards the survival
they are known to have had.

**"The median is the average survival time."** The median is the time at
which the curve crosses $0.5$; the mean is the area under the curve, and it
is not estimable at all when follow-up ends with the curve above zero. With
skewed survival times the two can differ greatly, and the median may not
exist while a restricted mean does.

**"If the curve never reaches zero, survival is good."** A curve that ends
high may simply reflect heavy censoring or short follow-up. The height of
the curve at the end of follow-up, the size of the risk set there, and the
width of the interval all have to be read together.

**"Non-overlapping confidence intervals at one time point mean the groups
differ."** Pointwise intervals at a single time are not a comparison of
curves. Comparing whole curves needs a test that uses the entire follow-up,
such as the log-rank test, and even then the comparison is of survival
distributions, not of survival at one chosen time. Rich and colleagues make
the same point about their small example: despite apparently very different
curves, the log-rank test was not significant, because the method's "main
focus is on the entire curve" rather than on isolated points
{{cite:rich2010}} (pp. 331–336).

**"The flat tail after the last observation is an estimate."** It is a
plotting convention. Beyond the largest observed time, if that time is a
censoring, the estimator is undefined, and extrapolating the flat line is
unjustified.

## History

The product-limit estimator was published by Edward L. Kaplan and Paul
Meier in 1958, in "Nonparametric estimation from incomplete observations",
in the *Journal of the American Statistical Association*
{{cite:kaplan_meier1958}} (pp. 457–458). The name "product-limit" was
adopted because the estimate is a limiting case of the older actuarial
(life-table) estimates, with the intervals made so short that each contains
at most one death; the idea had in fact been proposed as early as 1912 by
Bohmer, but "seems to have been lost sight of by later writers and not
further investigated" {{cite:kaplan_meier1958}} (p. 463). The variance
formula used with it goes back further still: a very similar formula had
been derived by Greenwood in 1926 for life tables {{cite:kaplan_meier1958}}
(p. 466). Kaplan and Meier's paper also gave the mean and variance of the
estimate, the mean lifetime and its restricted version, and a consistency
argument {{cite:kaplan_meier1958}} (pp. 465–468, 479). The estimator became
the standard nonparametric summary of survival data, and the paper one of
the most cited in statistics. Later work refined its asymptotic theory, but
the estimator itself, and Greenwood's formula for its variance, are still
used in essentially their 1958 form.

## Connections

- [Survival function](survival-function.qmd) — the target $S(t) = P(T > t)$
  that the Kaplan–Meier estimator estimates.
- [Hazard rate](hazard-rate.qmd) — the instantaneous event rate; the
  Kaplan–Meier curve and the Nelson–Aalen cumulative hazard estimate are two
  views of the same risk-set information, related by
  $\widehat{\Lambda}(t) = -\log \widehat{S}(t)$ approximately.
- [Censoring statistics](censoring-statistics.qmd) — the censoring
  mechanisms (right, left, interval) that make the estimator necessary, and
  the non-informative-censoring assumption it relies on.
- [Survival analysis](survival-analysis.qmd) — the broader setting: the
  product-limit formula is the nonparametric core of survival analysis, and
  the worked examples there use the same risk-set arithmetic.
- [Log-rank test](log-rank-test.qmd) — the test that compares two or more
  Kaplan–Meier curves, built from the same event-time tables.
- [Competing risks](competing-risks.qmd) — the setting where treating a
  competing event as censoring, and reading $1 - \widehat{S}(t)$ as the
  probability of the event of interest, overstates the risk; the cumulative
  incidence function is needed instead.

## Check yourself

1. In the worked example, what is $\widehat{S}(5)$, and why is it the same
as $\widehat{S}(3)$ even though a patient was censored at 4 months?

::: {.callout-tip collapse="true" title="Answer"}

$\widehat{S}(5) = 0.75$. The Kaplan–Meier estimate changes only at event
times, and there is no event between 3 and 5 months. The censoring at 4
months does not change any value of $\widehat{S}$; it only removes that
patient from the risk set, so the next event, at 6 months, is divided by 5
rather than 6.

:::

2. In the worked example, the log-log 95% interval for $S(6)$ is
approximately $(0.108,\ 0.751)$, while the plain normal interval is
approximately $(0.081,\ 0.819)$. Why is the log-log interval asymmetric
about $0.45$, and why is it preferred?

::: {.callout-tip collapse="true" title="Answer"}

The log-log interval is built on the transformed scale
$\theta = \log[-\log S]$ and then transformed back with the decreasing
function $s \mapsto \exp\{-\exp(s)\}$, so equal steps on the
$\theta$-scale become unequal steps on the survival scale. It is preferred
because it always lies inside $(0, 1)$: a plain normal interval can extend
below 0 or above 1, which is impossible for a probability. In this example
both intervals stay inside $(0, 1)$, but the log-log interval is the one
whose asymmetry reflects the bounded scale.

:::

3. A study reports a Kaplan–Meier curve that stays above $0.6$ for the whole
follow-up period, with only 3 patients still at risk at the end. What can
be said about the median survival time, and what should be reported
instead?

::: {.callout-tip collapse="true" title="Answer"}

Nothing can be said about the median: it is not reached, because the curve
never falls to $0.5$, and it should be reported as not estimable rather than
extrapolated. Report instead the estimated survival at a stated horizon
with its confidence interval, and the restricted mean survival time to a
stated horizon — for example, the area under the curve to the end of
follow-up. The small risk set at the end also means late estimates are very
imprecise, so the interval width and the numbers at risk should be shown
alongside the curve.

:::
