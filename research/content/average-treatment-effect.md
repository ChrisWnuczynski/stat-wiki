## Lead context
A treatment contrast is an average when the question is about a population rather than about one person. The same drug can help one patient and harm another, and the quantity used to summarise that mixture is the average treatment effect. {{cite:hernan_robins2020}} (p. 5)

## Motivating example
Twenty patients can each be imagined under a heart transplant and under no transplant. In one such list, ten would die within five days either way, so the proportion who die is \(10/20 = 0.5\) under both actions. The average effect in that population is zero even though some individuals are helped and some are harmed. {{cite:hernan_robins2020}} (p. 5) {{cite:hernan_robins2020}} (p. 4)

## Intuition
For each person write the outcome that would be seen if everyone received the treatment, and the outcome that would be seen if everyone received the comparison. Average each column. The difference of those two averages is the average treatment effect. Only one of the two outcomes is observed for any real person, so the average is a target, not a column that can be computed by subtraction inside the data set. {{cite:hernan_robins2020}} (p. 4) {{cite:hernan_robins2020}} (p. 5)

## Definition
Let \(Y^{a=1}\) be the outcome that would be seen under treatment and \(Y^{a=0}\) the outcome under the comparison. An average causal effect is present when the population means differ, \(\mathrm{E}[Y^{a=1}] \neq \mathrm{E}[Y^{a=0}]\). {{cite:hernan_robins2020}} (p. 5) For a binary outcome the mean is the risk, so the same contrast is \(\Pr(Y^{a=1}=1) - \Pr(Y^{a=0}=1)\). {{cite:hernan_robins2020}} (p. 5) {{cite:hernan_robins2020}} (p. 7)

The actions being compared have to be stated. "Transplant" against "no transplant" is one contrast. A different comparison, such as transplant against a named alternative procedure, is a different average effect. {{cite:hernan_robins2020}} (p. 5)

## Properties
The average can be zero while individual effects are not. In the twenty-patient transplant list the risks match, so the average effect is null, and the null hypothesis of no average causal effect is the statement that those two risks are equal. {{cite:hernan_robins2020}} (p. 5)

On the additive scale the effect counts extra cases. A risk of \(0.2\) under treatment and \(0.3\) under no treatment is a risk difference of \(0.2 - 0.3 = -0.1\): ten fewer deaths per hundred people. The same pair of risks has ratio \(0.2/0.3\). Which summary is used depends on whether the question is about the number of cases or about the fold change. {{cite:hernan_robins2020}} (p. 7) {{cite:dodge2008}} (p. 62)

The definition assumes that one person's treatment does not change another person's outcome. When it does, the counterfactual for a single person is not fixed until everyone else's treatment is fixed as well. {{cite:hernan_robins2020}} (p. 5)

## Statistical use
A randomised experiment estimates the average by comparing the treated group with the [control group](control-group.qmd), because random assignment makes the two groups exchangeable in expectation. {{cite:openintro2019}} (p. 32) {{cite:hernan_robins2020}} (p. 5) In an observational study the same contrast is the target only after the identifying conditions are stated. A sample proportion estimates the population risk, and sampling variability means the sample contrast is not the population average itself. {{cite:hernan_robins2020}} (p. 8) {{cite:openintro2019}} (p. 25)

## Worked example
Eight patients have potential outcomes under treatment \(1, 0, 1, 0, 1, 0, 0, 1\) and under no treatment \(1, 1, 0, 0, 1, 1, 0, 0\), where \(1\) is death. The mean under treatment is \(4/8 = 0.5\). The mean under no treatment is \(4/8 = 0.5\). The average treatment effect on the risk difference is \(0.5 - 0.5 = 0\). Three patients have different outcomes under the two actions, so individual effects exist in a population whose average effect is zero. {{cite:hernan_robins2020}} (p. 5)

**Your turn.** Change the last patient's outcome under treatment from \(1\) to \(0\). What are the new mean under treatment and the average treatment effect?

::: {.callout-tip collapse="true" title="Answer"}
The treatment outcomes sum to 3, so the mean is \(3/8\). The average treatment effect is \(3/8 - 4/8 = -1/8\).
:::

## Common misconceptions
The average treatment effect is not the difference of outcomes for the people who happened to be treated and the people who happened not to be. That difference mixes the effect with whatever else differs between those people, unless the groups were formed so that the mixture cancels. {{cite:openintro2019}} (p. 25) {{cite:hernan_robins2020}} (p. 4)

A null average does not mean the treatment does nothing to every person. It means the population means match. {{cite:hernan_robins2020}} (p. 5)

## Assumptions and limits
The contrast is for one population and one pair of actions, over the time window in which the outcome is defined. Interference, in which one person's treatment changes another's outcome, makes a single \(Y^{a}\) undefined until the whole allocation is specified. {{cite:hernan_robins2020}} (p. 5) {{cite:hernan_robins2020}} (p. 7) Individual effects are not identified from the observed data, because one of the two potential outcomes is missing for each person. {{cite:hernan_robins2020}} (p. 4)

## Connections
[Causality](causality.qmd) is the contrast of potential outcomes of which the average treatment effect is the population summary. A [designed experiment](designed-experiment.qmd) is one way to estimate it. An [instrumental variable](instrumental-variable.qmd) is another route when adherence is incomplete, and it estimates this average only under a further condition. {{cite:hernan_robins2020}} (p. 213) {{cite:openintro2019}} (p. 32)

## History
Comparing what would have happened under two actions is the ordinary reasoning the notation makes precise. The population average, rather than the individual contrast, is the version that can be tied to observed frequencies. {{cite:hernan_robins2020}} (p. 3) {{cite:hernan_robins2020}} (p. 5) In epidemiology the same idea appears as an absolute effect, the risk in the exposed minus the risk in the unexposed. {{cite:dodge2008}} (p. 62)
