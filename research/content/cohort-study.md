## Lead context
Some questions ask what happens to people after an exposure, not who among the already ill was exposed. A cohort study identifies the people first and then records the outcomes that occur as time passes, or reconstructs that follow-up from records. {{cite:openintro2019}} (p. 25)

## Motivating example
The Nurses' Health Study, begun in 1976 and expanded in 1989, recruited registered nurses and then collected data from them with questionnaires over the following years. The nurses are the cohort. Behaviour is recorded, and later illness is the outcome. Nobody assigned the behaviour. {{cite:openintro2019}} (p. 25) A factory workforce followed for mortality after a chemical exposure is the same kind of group: the cohort is the people at work, and the outcome is death. {{cite:hernan_robins2020}} (p. 111)

## Intuition
Fix a membership list at the start. Classify people by exposure. Wait, or read forward through the records, and count who develops the outcome. The counts sit on top of a denominator of people who were eligible to develop it, so the result can be a risk. That is the feature a [case-control study](case-control-study.qmd) gives up when it samples cases and non-cases in proportions the investigator chooses. {{cite:openintro2019}} (p. 25) {{cite:hernan_robins2020}} (p. 112)

## Definition
A prospective study identifies individuals and collects information as events unfold. Following a group of patients for years to relate behaviour to later cancer is the pattern, and a cohort is that group. {{cite:openintro2019}} (p. 25) A retrospective study collects data after the events, for example by reviewing medical records. A data set can mix variables collected in both ways. {{cite:openintro2019}} (p. 25)

The comparison is often with a group that did not receive the exposure. In a prospective study that untreated set is a [control group](control-group.qmd): it is the reference against which the exposed experience is judged. {{cite:nist_glossary2002}} (Glossary, "control group")

## Properties
Because membership is defined before the outcome is used to select the sample, the proportion who develop the outcome estimates a risk in that cohort, subject to losses. The risk in the exposed minus the risk in the unexposed is the absolute effect. The ratio of the risks is the relative effect. {{cite:dodge2008}} (p. 62) {{cite:openintro2019}} (p. 25)

People leave. If those who drop out differ in both exposure and prognosis, the risks among those who remain are not the risks in the cohort that was enrolled. Restricting the analysis to workers still at work, or to patients still attending, is one way that selection changes the contrast. {{cite:hernan_robins2020}} (p. 111)

## Statistical use
The design is observational when the exposure was not assigned. It can support an association, and a causal reading depends on whether the exposed and unexposed are comparable apart from the exposure. {{cite:openintro2019}} (p. 25) {{cite:openintro2019}} (p. 32) Longitudinal data, repeated observations on the same subjects, are the natural record of a cohort followed through time. {{cite:dodge2008}} (p. 322)

A randomised experiment is not a cohort study in this sense: there the investigator assigns the treatment. The follow-up of randomised groups borrows the same arithmetic of risks. {{cite:openintro2019}} (p. 32) {{cite:nist_glossary2002}} (Glossary, "control group")

## Worked example
A cohort contains 200 people, 80 exposed and 120 unexposed, all followed for the same period. The outcome occurs in 20 of the exposed and in 12 of the unexposed. The risks are \(20/80 = 0.25\) and \(12/120 = 0.10\). The risk difference is \(0.25 - 0.10 = 0.15\). The risk ratio is \(0.25/0.10 = 2.5\). {{cite:dodge2008}} (p. 62) {{cite:openintro2019}} (p. 25)

**Your turn.** Four more exposed people are enrolled, and one of them develops the outcome. What are the new exposed risk and the new risk ratio, using the same unexposed risk of \(0.10\)?

::: {.callout-tip collapse="true" title="Answer"}
The exposed count is 84 and the outcomes among them number 21, so the risk is \(21/84 = 0.25\). The risk ratio remains \(0.25/0.10 = 2.5\).
:::

## Common misconceptions
A cohort is not any large data set. It is a defined set of people in whom exposure and later outcome can both be observed. A stack of case records with no account of the people who did not become cases is not a cohort analysis. {{cite:openintro2019}} (p. 25) {{cite:hernan_robins2020}} (p. 112)

Following people forward does not by itself assign the exposure. The Nurses' Health Study collects questionnaires from nurses. It does not allocate their behaviour. {{cite:openintro2019}} (p. 25) {{cite:openintro2019}} (p. 32)

## Assumptions and limits
Everyone in the denominator has to be able to be classified for the outcome. Losses that depend on exposure and on the outcome change the risks. {{cite:hernan_robins2020}} (p. 111) A causal claim needs the exposed and unexposed to be comparable, or an explicit adjustment that is believed to make them so. Exhausting the list of measured confounders does not prove the list was complete. {{cite:openintro2019}} (p. 25)

## Connections
A [case-control study](case-control-study.qmd) samples from a cohort according to the outcome. [Causality](causality.qmd) is a reading of the risk contrast, not a synonym for follow-up. Repeated measurements on the same subjects are the record a cohort produces when units are observed more than once. The [population](population.qmd) is the wider group the cohort is meant to inform, which may be larger than the enrolled set. {{cite:openintro2019}} (p. 22)

## History
Identifying a group and watching events unfold is the prospective pattern used in studies such as the Nurses' Health Study from 1976. {{cite:openintro2019}} (p. 25) Reading the same history backwards from records is the retrospective form of the same idea. Occupational cohorts, such as factory workers followed for mortality, became a standard setting in which to see how selection out of the cohort distorts a contrast. {{cite:hernan_robins2020}} (p. 111)
