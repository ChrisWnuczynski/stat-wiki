## Lead context

A household that is interviewed once can be compared with other households. A household that is interviewed every quarter can also be compared with itself. Panel data are the second arrangement: the same units, observed at more than one time, so that each record carries a unit label and a time label.

## Motivating example

Three people are weighed at the start of a year and again at the end. The pairs are \((2,4)\), \((5,5)\), and \((3,6)\). Each person has a change, \(+2\), \(0\), and \(+3\). The average change is \(5/3\). The cross-sectional means are \(10/3\) at the start and \(5\) at the end, and the difference of those means is the same \(5/3\). The equality is a property of a complete panel. Drop one of the later weights and it disappears.{{cite:cameron_miller2015}} (§I, p. 2){{cite:dodge2008}} (p. 410)

## Intuition

A [cross-sectional data](cross-sectional-data.qmd) set has one row per unit. A [time series](time-series.qmd) has one row per time for a single series. A panel stacks several series that share a calendar, with a column that says which series is which. The statistical point of the stack is that two observations on the same person can be dependent even when two people are not. Analysing the stack as if every row were a new person treats that dependence as if it were not there.{{cite:cameron_miller2015}} (§I, p. 2)

Following the same people is also why a panel is more than a repeated census of a changing population. A census can be taken every decade on whoever is present. A panel tries to keep a sample and return to it.{{cite:dodge2008}} (p. 410)

## Definition

Panel data are repeated observations on a fixed or slowly changing collection of units, indexed by unit and by time. In the survey tradition a panel is a census-like inquiry that is repeated, built on a permanent or semipermanent sample of people or households who are questioned on a schedule. The sample may be held fixed when the aim is to follow individuals, and that case is a longitudinal inquiry. It may be partly renewed when the aim is to estimate population characteristics at successive dates, and that case is a changing panel. Either way the file has an individual dimension and a time dimension at once.{{cite:dodge2008}} (p. 410)

In the regression tradition the same layout is the second leading example of clustered errors, after a single cross-section clustered by region. Errors in different periods for one person, firm, or region may be correlated. Errors for different individuals are treated as uncorrelated. The cluster is the individual, and the observations inside the cluster are the times.{{cite:cameron_miller2015}} (§I, p. 2)

Longitudinal data, in the sense of several observations on the same subject, include this layout. Repeated measures in biology and medicine, and panel studies in the social sciences, are the usual examples.{{cite:dodge2008}} (p. 322)

## Properties

Write \(Y_{it}\) for unit \(i=1,\ldots,N\) at time \(t=1,\ldots,T\), and write \(\Delta_i=Y_{iT}-Y_{i1}\) when only the first and last times are compared. If every unit is observed at both times,
\[
\frac{1}{N}\sum_{i=1}^N \Delta_i
=
\left(\frac{1}{N}\sum_{i=1}^N Y_{iT}\right)
-
\left(\frac{1}{N}\sum_{i=1}^N Y_{i1}\right).
\]
The average change equals the change in the average. In the three-person panel the changes are \(2\), \(0\), and \(3\), their mean is \(5/3\), and the means \(5\) and \(10/3\) differ by \(5/3\).{{cite:dodge2008}} (p. 410)

The identity uses the same set of units at both times. Suppose the third person's second weight is missing. The two observed changes average \((2+0)/2=1\). The first-wave mean of all three people is \(10/3\), and the second-wave mean of the two people who remain is \((4+5)/2=9/2\). The difference of those means is
\[
\frac{9}{2}-\frac{10}{3}=\frac{7}{6}\neq 1.
\]
A comparison of whoever is present at each date is not the average of the observed individual changes.{{cite:cameron_miller2015}} (§I, p. 2)

Observations on one unit are dependent, so the sample size for a within-unit question is \(N\), the number of units, rather than \(NT\), the number of rows. A panel of \(20\) people observed at \(10\) dates has \(200\) rows and \(20\) independent personal histories. Standard errors that count \(200\) independent residuals are too small when the personal errors persist.{{cite:cameron_miller2015}} (§I, pp. 2–3)

## Statistical use

The design answers questions a single cross-section cannot. A change in a person's own spending, after a change in that person's own circumstances, uses the within-person contrast \(\Delta_i\). A comparison of different people at one date uses only one time slice and is again a cross-section. Studies that want both, a within contrast and a between contrast, keep the full \(Y_{it}\) and model the dependence.{{cite:dodge2008}} (p. 410){{cite:cameron_miller2015}} (§I, p. 2)

A [linear mixed model](linear-mixed-model.qmd) can give each unit an intercept, so that the shared level induces the within-unit correlation. A [marginal model](marginal-model.qmd) states the average at each time and uses a [working correlation](working-correlation.qmd) only to estimate that average. Cluster-robust standard errors after a regression leave the dependence unspecified and require many units rather than many time points. Those are different uses of the same rectangular file.{{cite:cameron_miller2015}} (§I, pp. 2–3)

Survey panels are also used to estimate a population total at several dates. Renewal of part of the sample is then deliberate: a sample that never changes slowly ceases to represent a population that does. The price of renewal is that some within-unit changes are no longer observed.{{cite:dodge2008}} (pp. 410–411)

## Worked example

The complete panel \((2,4)\), \((5,5)\), \((3,6)\) has first-wave mean \(10/3\), second-wave mean \(5\), and mean change \(5/3\). The three changes sum to \(5\), and \(5/3\) equals \(5-10/3\). With the third second-wave value removed, the mean of the two observed changes is \(1\) and the difference of the available wave means is \(7/6\). The two summaries, \(1\) and \(7/6\), describe different sets of people.{{cite:dodge2008}} (p. 410){{cite:cameron_miller2015}} (§I, p. 2)

**Your turn.** Two units are observed at both times, with values \(1\) then \(4\), and \(6\) then \(6\). Find the mean change and the difference between the second-wave mean and the first-wave mean.

::: {.callout-tip collapse="true" title="Answer"}
The changes are \(3\) and \(0\), so the mean change is \(1.5\). The wave means are \((1+6)/2=3.5\) and \((4+6)/2=5\), and their difference is \(5-3.5=1.5\).
:::

## Common misconceptions

A panel is not just any table with a date column. A fresh cross-section every year, on a new sample, has dates and does not have repeated units. Pasting those cross-sections into one file does not create within-unit changes.{{cite:dodge2008}} (p. 410)

The number of rows is not the number of independent observations for a question about people. Twenty people measured ten times are twenty clusters of correlated rows. A [time series](time-series.qmd) on one country is the opposite extreme: one unit, many times, and no cross-person contrast at all.{{cite:cameron_miller2015}} (§I, p. 2)

Returning to the same respondents does not leave their behaviour untouched. People who are asked repeatedly about a purchase or a symptom can change what they do because they were asked. That panel conditioning is a property of the measurement, not a property of the world the survey hoped to watch.{{cite:dodge2008}} (p. 411)

## Assumptions and limits

The uncorrelated-units assumption is the one the standard errors rely on. If neighbouring regions share a shock, clustering only on person is not enough; the cluster has to be wide enough to contain the dependence. A short panel, with large \(N\) and small \(T\), supports that person-level clustering. A long panel on a few units is closer to a set of time series, and person-level asymptotics in \(N\) do not apply.{{cite:cameron_miller2015}} (§I, pp. 2–3)

Survey panels have their own failures. Some kinds of respondent are hard to recruit. Respondents tire, and non-response grows. The population changes, so a sample that was representative drifts. Dating of events is pulled toward the interview, the telescope effect, especially among new panellists. A changing panel is often used precisely because a strict permanent sample deforms.{{cite:dodge2008}} (p. 411)

Missing times are not a cosmetic gap. The three-person calculation shows a difference of means, \(7/6\), that is not the mean of the observed changes, \(1\). An analysis that ignores the missingness pattern is describing a different contrast from the one the complete-panel identity names.{{cite:dodge2008}} (p. 322)

## Connections

One wave of a panel is [cross-sectional data](cross-sectional-data.qmd). Many waves on one aggregate, without a cross-section of units, are a [time series](time-series.qmd). [Repeated measures](repeated-measures.qmd) are the same idea in experimental and clinical language. A unit intercept shared by the times is a [random-intercept model](random-intercept-model.qmd) inside a [linear mixed model](linear-mixed-model.qmd), and a non-Gaussian response uses a [generalised linear mixed model](generalised-linear-mixed-model.qmd). Those models are [multilevel models](multilevel-model.qmd) when the unit effects are one level and, for example, clinics containing the units are another. A population-average analysis that keeps the times correlated only through a working matrix uses [generalised estimating equations](generalised-estimating-equations.qmd).

## History

Repeated measurement of the same people is older than the modern survey panel. In 1759 Philibert Guéneau de Montbeillard began recording his son's stature every six months from birth to age 18. That series has the repeated-observation idea and little else in common with a national panel. The current notion of panel research took shape in the growth studies of the 1920s and 1930s. From the middle of the twentieth century the design spread through the social sciences. In the United States, public funding in the 1960s and 1970s supported the National Longitudinal Surveys from 1966 and the Panel Study of Income Dynamics from 1968, the latter beginning with 4,802 families. The same decades produced the methods, for correlated longitudinal observations, that made the large files usable rather than merely large.{{cite:dodge2008}} (pp. 322, 410–411)
