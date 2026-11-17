## Lead context
Some data sets are a single snapshot. Each person, firm, or plot appears once, and the differences of interest are differences between those units. Cross-sectional data are that snapshot. They support comparisons across units, and they do not by themselves show how any one unit changed.{{cite:hyndman_athanasopoulos2021}} (Ch. 1, §1.4)

## Motivating example
Five households are interviewed in the same week and report weekly incomes 2, 4, 4, 6, and 9, in the same currency units. The mean income in this cross-section is 5. Nothing in the table says whether the household that reported 9 earned 9 last year as well. A question about change needs a second observation on the same household. A question about the distribution this week can be answered from the five numbers alone.{{cite:hyndman_athanasopoulos2021}} (Ch. 1, §1.4)

## Definition
Cross-sectional data are observations collected at a single point in time, on many units. Most quantitative prediction problems use either time series data, collected at regular intervals over time, or cross-sectional data, collected at a single point in time. The forecasting problem concentrates on the series. The cross-section is the case in which the analysis compares units rather than dates.{{cite:hyndman_athanasopoulos2021}} (Ch. 1, §1.4)

Lay the data out as one row per unit. Columns are variables measured on that unit: income, age, region. Time does not vary inside the table, or it varies so little that the study treats the rows as contemporaneous. The sample size that matches this layout is the number of units, not the number of occasions. A [time series](time-series.qmd) turns the layout the other way: one unit, or one aggregate, observed in time order.{{cite:hyndman_athanasopoulos2021}} (Ch. 1, §1.4)

A regression on such data can still have errors that are correlated inside a cluster. One leading example is an individual-level cross-section in which the cluster is a village, a state, or another region. Errors for individuals in the same region may be correlated. Errors for individuals in different regions are the ones the model treats as uncorrelated. The data remain cross-sectional: each individual contributes one record. The dependence is across records that share a place, not across times.{{cite:cameron_miller2015}} (§I, p. 2)

## Interpretation
Let unit \(i=1,\ldots,n\) contribute a single response \(Y_i\). The sample mean \(\bar Y=n^{-1}\sum_i Y_i\) estimates the mean across units at that time. There is no within-unit difference \(Y_{i2}-Y_{i1}\) to compute, because the second index does not exist. For the five incomes,
\[
2+4+4+6+9=25, \qquad \bar y=25/5=5.
\]
The deviations from 5 are \(-3,-1,-1,1,4\), and the sum of squared deviations is \(9+1+1+1+16=28\). The sample variance with divisor \(n-1=4\) is \(28/4=7\). That variance is a spread across households. It is not a variance of changes.{{cite:hyndman_athanasopoulos2021}} (Ch. 1, §1.4)

If the \(n\) units fall into \(G\) regions and the errors are correlated inside a region, the number of independent pieces of information for a regional contrast is closer to \(G\) than to \(n\). Default standard errors that assume independent units then overstate precision. It is not unusual for standard errors that respect the cluster to be several times the default. The need grows with the within-cluster correlation of the errors, with the within-cluster correlation of the regressors, and with the number of observations inside a cluster. A leading case is a policy, or another regressor, that takes the same value for every observation in a cluster.{{cite:cameron_miller2015}} (§I, p. 2)

A cross-section can be repeated on a fresh sample at a later date. The two samples support a comparison of two population snapshots. They do not follow the same units, so a change in the snapshot mean is not an average of individual changes. That distinction is the reason a later study may keep the same units and become [panel data](panel-data.qmd) instead. Cameron and Miller treat the panel, in which the same individual appears at several dates, as its own design rather than as a tall cross-section.{{cite:cameron_miller2015}} (§I, p. 2)

The usual summaries are means, rates, and regressions in which the unit of analysis is the row. An [observational study](observational-study.qmd) that records exposure and outcome once per person is the typical scientific setting. Forecasting from the past of a single series is not: that problem asks for a time series, and a cross-section taken today has no past inside it.{{cite:hyndman_athanasopoulos2021}} (Ch. 1, §1.4)

Three annual totals for one country are a time series of length three. Three countries in one year are a cross-section of size three. The file can look the same in a spreadsheet and still answer different questions. Independence is not part of the definition. Individual-level cross-sections are often clustered by geography or by industry. A cross-section also does not become a panel because the questionnaire asks people to remember last year. The study still has one interview.{{cite:hyndman_athanasopoulos2021}} (Ch. 1, §1.4) {{cite:cameron_miller2015}} (§I, p. 2)

The phrase "a single point in time" is an idealisation. A survey taken over a month is called a cross-section when the analysis does not use the interview date as a time index. If the phenomenon moves during fieldwork, that idealisation is a source of error. Cross-sectional comparisons mix stable differences between units with temporary ones. Holding age or region fixed in a regression removes only the differences that were measured. The cluster-robust correction assumes many clusters. A cross-section with a handful of regions can have a large sample of people and still have little information about a region-level regressor.{{cite:cameron_miller2015}} (§I, p. 2) {{cite:hyndman_athanasopoulos2021}} (Ch. 1, §1.4)

## Worked example
The incomes \(2,4,4,6,9\) are one cross-section. Their mean is \(5\). The deviations from the mean are \(-3,-1,-1,1,4\), and the sum of squared deviations is \(9+1+1+1+16=28\). The sample variance with divisor \(n-1=4\) is \(28/4=7\). No within-household change is defined. A second cross-section, on five different households, could have the same mean and a different variance; it would still not say which of the original households had moved.{{cite:hyndman_athanasopoulos2021}} (Ch. 1, §1.4)

**Your turn.** A cross-section of three units has values \(3, 5, 7\). Find the mean and the range. Why is a within-unit change unavailable?

::: {.callout-tip collapse="true" title="Answer"}
The mean is \((3+5+7)/3=5\). The range is \(7-3=4\). Each unit was measured once, so there is no second measurement to subtract from the first.
:::

## Connections
A [time series](time-series.qmd) follows order in time; a cross-section follows differences across units. [Panel data](panel-data.qmd) keep both indices, unit and time. [Repeated measures](repeated-measures.qmd) are the case in which the same unit is observed more than once, often on a short schedule. Dependence inside a region of a cross-section is handled by a [multilevel model](multilevel-model.qmd) when the region effect is given a distribution, or by [generalised estimating equations](generalised-estimating-equations.qmd) when the target is a population-average association and the [working correlation](working-correlation.qmd) is only a device for estimation. An [observational study](observational-study.qmd) is the usual scientific frame for a cross-section that does not assign treatments.{{cite:cameron_miller2015}} (§I, p. 2)

## History
The contrast between a snapshot and a series is as old as the two kinds of table: a census of a country at one date, and a run of harvests or prices. Forecasting practice now states the split in those words. Most quantitative prediction uses either a time series, collected at regular intervals, or a cross-section, collected at one time, and the forecasting problem concentrates on the series.{{cite:hyndman_athanasopoulos2021}} (Ch. 1, §1.4) Econometric practice states a further split inside the cross-section itself. An individual-level survey is often clustered, and the standard errors have to respect the cluster, while a panel is treated as its own design.{{cite:cameron_miller2015}} (§I, p. 2)
