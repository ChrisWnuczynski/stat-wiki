## Motivating example
A survey can spend its budget either visiting many locations briefly or measuring many units in a few locations. It can also guarantee observations from regions whose means may differ. Stratification and clustering organise these choices in different ways. Stratification samples from every declared stratum, while cluster sampling selects groups and observes units within the selected groups. Both can use random selection, but the dependence and precision of their resulting estimators differ.{{cite:statistics_canada2003_survey}} (§§6.2.5–6.2.6)

## Definition — Which groups are all represented?
Strata form a mutually exclusive, exhaustive partition of the population. In stratified simple random sampling, an independent SRS is drawn within each stratum. If stratum $h$ contains $N_h$ units and receives sample size $n_h$, every unit in that stratum has inclusion probability $n_h/N_h$. Proportional allocation sets these sampling fractions approximately equal, subject to integer sample sizes and other design constraints.{{cite:dodge2008}} (Stratified Sampling, pp. 523–524)

Clusters also partition the population, but only some are selected. A one-stage design measures all units in the selected clusters. A two-stage design samples units within those clusters as a second randomisation. Sampling one part of every stratum and sampling all units in a few clusters are different mechanisms, even when they have the same total number of observations. A design can combine stratification at one stage with clustering at another.{{cite:statistics_canada2003_survey}} (§§6.2.5–6.2.7)

## Properties — Weights and precision follow the design
With independent SRS draws within strata, the weighted estimator of the population mean is
$$\widehat{\bar Y}_{\rm st}=\sum_hW_h\bar y_h,\qquad W_h=N_h/N.$$
Its variance is $\sum_hW_h^2(1-n_h/N_h)S_h^2/n_h$, where $S_h^2$ uses the finite-population divisor $N_h-1$ within stratum $h$. The weights are population shares, not automatically sample shares. Disproportionate allocation can be useful, but an unweighted mean may then target the wrong population average.{{cite:statistics_canada2003_survey}} (§7.3.2.4, stratified SRS estimation)

Clustering can save travel or setup costs while increasing variance when units within a selected cluster are very similar. Equal unit inclusion probabilities do not remove that correlation. Precision depends on how many independent clusters are sampled, their sizes, their within-cluster variation and the estimator's weights. A cluster design can also perform well when clusters are internally diverse and similar to one another; the effect is a property of the population and design together.{{cite:statistics_canada2003_survey}} (§6.2.5, advantages and disadvantages of cluster sampling)

## Worked example — Guarantee regional representation
Suppose a population has 40 eastern and 60 western units, with region means 10 and 20. A sample of 10 using proportional allocation takes four eastern and six western units. If the sample region means are 12 and 18, the population-mean estimate is $0.4(12)+0.6(18)=15.6$. An alternative allocation of five from each region still uses the population weights 0.4 and 0.6; simply averaging the two region means would give 15, which targets equal region weighting instead.

For a separate illustration of clustering, consider four clusters of four units each. Two clusters contain only zeros and two contain only tens. An SRS of two clusters produces possible overall means $0,5,5,5,5,10$ from six equally likely cluster pairs. The design variance is $25/3=8.333333$. An SRS of eight units from the same 16-unit population has variance $5/3=1.666667$. The cluster design has five times the variance, despite observing the same eight units in total. This difference comes entirely from which combinations can be selected.

**Your turn.** In the regional example, sample sizes are five in each region. What are the two individual inclusion probabilities?

::: {.callout-tip collapse="true" title="Answer"}
They are 5/40=0.125 in the east and 5/60=1/12 in the west. The sampling fractions are different, so population weighting matters.
:::

## Statistical use — Choose groups using useful design information
Stratification is attractive when a frame identifies meaningful groups before selection and the design needs representation or precision within them. Cluster sampling is attractive when obtaining a unit list across the entire population is costly or when measurement has a large location-specific setup cost. The choice should compare attainable precision at a stated cost, rather than comparing only nominal sample sizes.{{cite:statistics_canada2003_survey}} (§§6.2.5–6.2.6 and Chapter 8, sample allocation)

The selection probabilities from every stage should accompany the observed data. Sampling a fixed number of units within unequal-sized selected clusters can produce unequal unit inclusion probabilities. Estimation and uncertainty calculations must follow that mechanism, including any stratification, stages, finite-population corrections and nonresponse adjustments. Treating all observed units as independent SRS observations can understate uncertainty even when the weighted point estimate is sensible.{{cite:statistics_canada2003_survey}} (§§6.2.7 and 7.3.3, multistage designs and design effects)

## Common misconceptions — A balanced-looking sample need not be random
Filling a quota from each region without a random selection rule is not stratified probability sampling. Conversely, random selection does not guarantee that every realised sample resembles the population on every characteristic. A design specifies probabilities over possible samples, and its inferential properties follow from that mechanism rather than from a visual impression of representativeness.{{cite:dodge2008}} (Stratified Sampling, pp. 523–524){{cite:statistics_canada2003_survey}} (§6.1.4, quota sampling)
