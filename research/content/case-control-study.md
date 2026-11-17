## Lead context
When the outcome is rare, following everyone until it occurs can be a poor use of a study. A case-control study starts from the outcome: people who already have it are sampled more readily than people who do not, and the exposure is then compared. {{cite:hernan_robins2020}} (p. 112)

## Motivating example
An investigator wants the effect of postmenopausal estrogen on coronary heart disease. The source population is a cohort of women. Cases of heart disease are taken into the study more often than women without heart disease. That preferential sampling of cases is what makes the design a case-control study. If the controls are then further restricted, for example to women with a hip fracture, the exposure comparison is no longer the comparison in the source population. {{cite:hernan_robins2020}} (p. 112)

## Intuition
Imagine a room that is filled by first inviting nearly every person who became ill, and only a fraction of those who stayed well. Exposure will look more common among the ill if it truly raises risk, because the invitation rule favoured the ill. The sample percentages are not the population risks. A comparison that respects the invitation rule, usually an odds ratio, can still say something about the source population. {{cite:hernan_robins2020}} (p. 112) {{cite:openintro2019}} (p. 25)

## Definition
In a case-control study, selection into the sample depends on the outcome. Cases, the people with the outcome, are more likely to be included than non-cases. The source population from which both are drawn is the underlying cohort. {{cite:hernan_robins2020}} (p. 112) The association reported from the sample is conditional on having been selected. {{cite:hernan_robins2020}} (p. 112)

The design is retrospective in the ordinary sense that the outcome has already occurred and past exposure is then ascertained, as when past events are read from records. {{cite:openintro2019}} (p. 25) It is not a [cohort study](cohort-study.qmd), which follows people identified before the outcomes are compared.

## Properties
The sample proportion with the outcome is fixed by the design, not estimated from the population. Risks and risk differences in the sample therefore do not estimate population risks. The odds ratio of exposure, cases versus controls, is the contrast the design supports when controls represent the source population's exposure distribution. {{cite:hernan_robins2020}} (p. 112)

Control selection is part of the design. Choosing controls because of a condition that the exposure itself causes opens a path from exposure to selection. Among the selected, the exposure odds ratio is then pulled away from the causal odds ratio in the population. {{cite:hernan_robins2020}} (p. 112)

## Statistical use
The study is observational: the investigator does not assign the exposure. An association is the direct product. A causal reading needs the same extra argument that any observational comparison needs, and it also needs the control group to stand in for the source population rather than for a selected slice of it. {{cite:openintro2019}} (p. 25) {{cite:hernan_robins2020}} (p. 112) The absolute effect in epidemiology is a difference of risks, which this design does not deliver without information on how the sampling fractions differ. {{cite:dodge2008}} (p. 62)

## Worked example
Forty cases and forty controls are interviewed. Among the cases, 24 were exposed and 16 were not. Among the controls, 10 were exposed and 30 were not. The odds of exposure are \(24/16 = 1.5\) in the cases and \(10/30 = 1/3\) in the controls. The odds ratio is \(1.5 / (1/3) = 4.5\), which is the same as \((24 \times 30)/(16 \times 10) = 720/160 = 4.5\). The proportion of cases in the study is \(40/80 = 0.5\) because the design chose equal numbers, not because half the population is a case. {{cite:hernan_robins2020}} (p. 112)

**Your turn.** Four more unexposed controls are added, so the controls are 10 exposed and 34 unexposed. What is the odds ratio?

::: {.callout-tip collapse="true" title="Answer"}
The odds ratio is \((24 \times 34)/(16 \times 10) = 816/160 = 5.1\).
:::

## Common misconceptions
The fraction of the sample that has the disease is not the population risk. It was set by how many cases and controls were invited. {{cite:hernan_robins2020}} (p. 112)

A case-control study is not a defective cohort study. Sampling on the outcome is the design, and it is useful precisely when waiting for cases in a follow-up would be inefficient. The defect is a control group chosen for a reason that is itself an effect of the exposure. {{cite:hernan_robins2020}} (p. 112) {{cite:openintro2019}} (p. 25)

## Assumptions and limits
The exposure odds ratio estimates the corresponding population contrast when the controls are drawn from the same source as the cases and inclusion depends on the outcome in a way that is the same within exposure groups. Preferential selection of controls who have a condition caused by the exposure biases that odds ratio. {{cite:hernan_robins2020}} (p. 112) A causal interpretation still requires that exposure and outcome do not share an uncontrolled common cause. {{cite:openintro2019}} (p. 25) {{cite:dodge2008}} (p. 62)

## Connections
The source population is a [cohort study](cohort-study.qmd) that might have been followed instead. The [control group](control-group.qmd) here is the sample of non-cases, not an experimentally untreated arm. [Causality](causality.qmd) is a further claim about the odds ratio, not a property of the sampling rule. [Sampling bias](sampling-bias.qmd) includes the bias that comes from the wrong controls.

## History
Selecting on a common effect of exposure and outcome, of which a badly chosen case-control sample is one form, was described as a structure of bias by Berkson in 1946. {{cite:hernan_robins2020}} (p. 112) Retrospective reading of records is the older practical pattern of asking about events that have already happened. {{cite:openintro2019}} (p. 25)
