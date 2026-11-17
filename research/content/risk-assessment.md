## Lead context

A health department wants the chance that a person in a stated group becomes ill this year. A factory wants the chance that a control chart will send someone looking for a fault that is not there. Both are risk assessments: a probability attached to a harmful or costly event, computed under a stated model, and compared with an alternative. The number is not a decision. It becomes one only when someone says which risks are worth acting on.

## Definition — Scope

In epidemiology, risk is the probability that a disease appears in a population, or in a homogeneous subgroup, during a given time interval. The subgroup is homogeneous in the limited sense that its members share an exposure suspected of causing the disease. Incidence is the related frequency. Risk assessment, in this setting, is the estimation of that probability and of the contrasts that give it a meaning: the difference and the ratio of risks for exposed and unexposed people. The absolute effect is the exposed risk minus the unexposed risk. The relative effect is their ratio, reported as a relative risk or an [odds ratio](odds-ratio.qmd). A large ratio can accompany a small difference. An assessment that quotes only one of them is incomplete.{{cite:dodge2008}} (pp. 62, 461)

A second, industrial meaning is the probability of a false signal. On a control chart, the control limits determine the risk of searching for an assignable cause when the process has not changed. Three-sigma limits put that risk near 0.0027 for a normal statistic, about 0.00135 in each tail. Moving the limits moves the risk. This is not a disease probability. It is the operating characteristic of a monitoring rule.{{cite:nist_pmc31_2002}} (§6.3.1)

## Statistical use

Epidemiological assessment starts from a defined population and an interval of time. A follow-up study estimates the risks directly. A case-control study often estimates an odds ratio instead, which approximates the relative risk when the disease is rare. The comparison is not yet causal. The exposure has to come first, and a [confounding variable](confounding-variable.qmd) can create the association. Sun exposure, in a study of sunscreen and skin cancer, is the usual confounder: it tracks both the exposure and the outcome. An assessment that stops at the crude ratio has not finished.{{cite:dodge2008}} (p. 62){{cite:openintro2019}} (Ch. 1, §1.3.4, p. 25)

Industrial assessment states the in-control distribution and the limit, then computes the probability of a point outside the limit. If the distribution is skewed, or Poisson, the three-sigma shortcut does not preserve the nominal probability. For a Poisson mean of 0.8 the upper three-sigma limit is $0.8+3\sqrt{0.8}=3.48$, and the chance of a count above 3 is about 0.009. The assessed false-alarm risk is then larger than the normal calculation suggests.{{cite:nist_pmc31_2002}} (§6.3.1)

## History

Cornfield, in 1951, set out risk as a comparison of follow-up groups, one of people with the disease and one without, and the notion spread through epidemiological studies as a measure of association between disease and exposure. The older tradition is the life table and the cause-of-death tally, which already asked how probability of death varied. Control-chart risks are younger: they date from the choice, in the 1920s and 1930s, to replace inspection of every item with a limit that has a known chance of a false alarm.{{cite:dodge2008}} (p. 461){{cite:nist_pmc31_2002}} (§6.3.1)

## Connections

Risk assessment in health is the quantitative centre of [public health](public-health.qmd) and a standard output of [medical statistics](medical-statistics.qmd). The false-alarm version is part of [statistical process control](statistical-process-control.qmd). [Loss and risk](loss-and-risk.qmd) in decision theory names a further quantity, the expected cost of a decision, which is neither a disease probability nor a false-alarm rate. A relative risk, a risk difference, and a false-alarm probability can all be called "the risk" in a meeting. They answer three questions. An assessment names the event, the interval, the population, and the model, and it reports the contrast that the decision actually uses.{{cite:dodge2008}} (pp. 62, 461){{cite:nist_pmc31_2002}} (§6.3.1)
