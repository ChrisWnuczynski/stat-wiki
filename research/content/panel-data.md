## Lead context

A household that is interviewed once can be compared with other households. A household that is interviewed every quarter can also be compared with itself. Panel data are the second arrangement: the same units, observed at more than one time, so that each record carries a unit label and a time label. The statistical point of the second label is dependence. Two observations on the same person can be correlated even when two people are not.{{cite:cameron_miller2015}} (§I, p. 2){{cite:dodge2008}} (p. 410, Panel)

## Motivating example

Three people are weighed at the start of a year and again at the end. The pairs are \((2,4)\), \((5,5)\), and \((3,6)\). Each person has a change, \(+2\), \(0\), and \(+3\). The average change is \(5/3\). The cross-sectional means are \(10/3\) at the start and \(5\) at the end, and the difference of those means is the same \(5/3\). The equality is a property of a complete panel. Drop one of the later weights and it disappears. A fresh sample of different people at the second date would not have produced within-person changes at all.{{cite:dodge2008}} (p. 410, Panel){{cite:cameron_miller2015}} (§I, p. 2)

## Definition

Panel data are repeated observations on a fixed or slowly changing collection of units, indexed by unit and by time. In the survey tradition a panel is a census-like inquiry that is repeated, built on a permanent or semipermanent sample of people or households who are questioned on a schedule. The sample may be held fixed when the aim is to follow individuals, and that case is a longitudinal inquiry. It may be partly renewed when the aim is to estimate population characteristics at successive dates, and that case is a changing panel. Either way the file has an individual dimension and a time dimension at once.{{cite:dodge2008}} (p. 410, Panel)

In the regression tradition the same layout is the second leading example of clustered errors, after a single cross-section clustered by region. Errors in different periods for one person, firm, or region may be correlated. Errors for different individuals are treated as uncorrelated. The cluster is the individual, and the observations inside the cluster are the times. Default standard errors that treat every row as an independent residual overstate the precision of a coefficient when that within-person correlation is present.{{cite:cameron_miller2015}} (§I, pp. 1–2)

Longitudinal data, in the sense of several observations on the same subject, include this layout. Repeated measures in biology and medicine, and panel studies in the social sciences, are the usual examples. A general linear model for subject \(i\) is \(y_i=X_i\beta+W_i\gamma_i+\varepsilon_i\), with \(\beta\) common and \(\gamma_i\) a subject effect. The simplest version drops \(\gamma_i\) and keeps only a time or group mean. When individuals differ, the subject effect goes back in, and the covariance of \(\gamma_i\) and \(\varepsilon_i\) becomes part of the model.{{cite:dodge2008}} (pp. 322–323, Longitudinal data)

## Interpretation

Write \(Y_{it}\) for unit \(i=1,\ldots,N\) at time \(t=1,\ldots,T\), and write \(\Delta_i=Y_{iT}-Y_{i1}\) when only the first and last times are compared. If every unit is observed at both times,
\[
\frac{1}{N}\sum_{i=1}^N \Delta_i
=
\left(\frac{1}{N}\sum_{i=1}^N Y_{iT}\right)
-
\left(\frac{1}{N}\sum_{i=1}^N Y_{i1}\right).
\]
The average change equals the change in the average. In the three-person panel the changes are \(2\), \(0\), and \(3\), their mean is \(5/3\), and the means \(5\) and \(10/3\) differ by \(5/3\). The identity uses the same set of units at both times. It is an algebraic fact about a complete rectangle, not a fact about a changing population.{{cite:dodge2008}} (p. 410, Panel)

Suppose the third person's second weight is missing. The two observed changes average \((2+0)/2=1\). The first-wave mean of all three people is \(10/3\), and the second-wave mean of the two people who remain is \((4+5)/2=9/2\). The difference of those means is
\[
\frac{9}{2}-\frac{10}{3}=\frac{7}{6},
\]
which is not \(1\). A comparison of whoever is present at each date is not the average of the observed individual changes. Missing times change the contrast.{{cite:cameron_miller2015}} (§I, p. 2){{cite:dodge2008}} (p. 323, missing data)

Observations on one unit are dependent, so the sample size for a within-unit question is \(N\), the number of units, rather than \(NT\), the number of rows. A panel of \(20\) people observed at \(10\) dates has \(200\) rows and \(20\) independent personal histories. Standard errors that count \(200\) independent residuals are too small when the personal errors persist. If the number of clusters is large, inference after least squares can use cluster-robust standard errors at the person level. A short panel, large \(N\) and small \(T\), is the setting those standard errors were built for. A long panel on a few units is closer to a set of time series.{{cite:cameron_miller2015}} (§I, pp. 2–3)

## Worked example

The complete panel \((2,4)\), \((5,5)\), \((3,6)\) has first-wave mean \(10/3\), second-wave mean \(5\), and mean change \(5/3\). The three changes sum to \(5\), and \(5/3\) equals \(5-10/3\). With the third second-wave value removed, the mean of the two observed changes is \(1\) and the difference of the available wave means is \(7/6\). The two summaries, \(1\) and \(7/6\), describe different sets of people.{{cite:dodge2008}} (p. 410, Panel){{cite:cameron_miller2015}} (§I, p. 2)

**Your turn.** Two units are observed at both times, with values \(1\) then \(4\), and \(6\) then \(6\). Find the mean change and the difference between the second-wave mean and the first-wave mean.

::: {.callout-tip collapse="true" title="Answer"}
The changes are \(3\) and \(0\), so the mean change is \(1.5\). The wave means are \((1+6)/2=3.5\) and \((4+6)/2=5\), and their difference is \(5-3.5=1.5\).
:::

## Connections

One wave of a panel is [cross-sectional data](cross-sectional-data.qmd). Many waves on one aggregate, without a cross-section of units, are a [time series](time-series.qmd). [Repeated measures](repeated-measures.qmd) are the same idea in experimental and clinical language. A unit intercept shared by the times is a [random-intercept model](random-intercept-model.qmd) inside a [linear mixed model](linear-mixed-model.qmd), and a non-Gaussian response uses a [generalised linear mixed model](generalised-linear-mixed-model.qmd). Those models are [multilevel models](multilevel-model.qmd) when the unit effects are one level and, for example, clinics containing the units are another. A population-average analysis that keeps the times correlated only through a working matrix uses [generalised estimating equations](generalised-estimating-equations.qmd). Cluster-robust standard errors leave the dependence unspecified and require many units. Those are different uses of the same rectangular file.{{cite:cameron_miller2015}} (§I, pp. 2–3){{cite:dodge2008}} (pp. 322–323)

## History

Repeated measurement of the same people is older than the modern survey panel. In 1759 Philibert Guéneau de Montbeillard began recording his son's stature every six months from birth to age 18. That series has the repeated-observation idea and little else in common with a national panel. The current notion of panel research took shape in the growth studies of the 1920s and 1930s. From the middle of the twentieth century the design spread through the social sciences. In the United States, public funding in the 1960s and 1970s supported the National Longitudinal Surveys from 1966 and the Panel Study of Income Dynamics from 1968, the latter beginning with 4,802 families. The same decades produced the methods for correlated longitudinal observations that made the large files usable rather than merely large.{{cite:dodge2008}} (pp. 322 and 410–411)

Survey panels have their own failures, and they are part of the history of the method rather than an afterthought. Some kinds of respondent are hard to recruit. Respondents tire, and non-response grows. The population changes, so a sample that was representative drifts. Dating of events is pulled toward the interview, the telescope effect, especially among new panellists. People who are asked repeatedly about a purchase or a symptom can change what they do because they were asked, which is panel conditioning. A changing panel is often used because a strict permanent sample deforms.{{cite:dodge2008}} (p. 411, Domains and limitations)
