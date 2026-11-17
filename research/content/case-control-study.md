## Lead context

When the outcome is rare, following everyone until it occurs can be a poor use of a study. A case-control study starts from the outcome. People who already have it are sampled more readily than people who do not, and the exposure is then compared. The sample percentages are not the population risks. A comparison that respects the sampling rule can still say something about the source population.{{cite:hernan_robins2020}} (p. 112)

## Motivating example

An investigator wants the effect of postmenopausal estrogen on coronary heart disease. The source population is a cohort of women. Cases of heart disease are taken into the study more often than women without heart disease. That preferential sampling of cases is what makes the design a case-control study. If the controls are then further restricted, for example to women with a hip fracture, the exposure comparison is no longer the comparison in the source population. Estrogen lowers the incidence of hip fracture, so controls chosen because they have a hip fracture are less likely to have taken estrogen than cases are. The odds ratio in the selected sample is then pulled away from the odds ratio in the population.{{cite:hernan_robins2020}} (p. 112)

## Intuition

Imagine a room that is filled by first inviting nearly every person who became ill, and only a fraction of those who stayed well. Exposure will look more common among the ill if it truly raises risk, because the invitation rule favoured the ill. The fraction of the room that is ill was set by the invitations. It is not the risk of illness in the population the invitations were drawn from. A comparison that uses the exposure odds among the invited ill and the exposure odds among the invited well can still track the population contrast, provided the invitation probabilities depend on the outcome in the same way inside each exposure group.{{cite:hernan_robins2020}} (p. 112){{cite:openintro2019}} (Ch. 1, §1.3.4)

## Definition

In a case-control study, selection into the sample depends on the outcome. Cases, the people with the outcome, are more likely to be included than non-cases. The source population from which both are drawn is the underlying cohort. The association reported from the sample is conditional on having been selected. Hernán and Robins represent that selection by a variable \(C\): an arrow from disease status to selection is the defining feature, because cases are more likely to be selected than non-cases.{{cite:hernan_robins2020}} (p. 112)

The design is retrospective in the ordinary sense that the outcome has already occurred and past exposure is then ascertained, as when past events are read from records. OpenIntro distinguishes prospective and retrospective collection of observational data on that basis. The design is not a [cohort study](cohort-study.qmd), which follows people identified before the outcomes are compared.{{cite:openintro2019}} (Ch. 1, §1.3.4)

## Properties

The sample proportion with the outcome is fixed by the design, not estimated from the population. Risks and risk differences in the sample therefore do not estimate population risks. The odds ratio of exposure, cases versus controls, is the contrast the design supports when controls represent the source population's exposure distribution.{{cite:hernan_robins2020}} (p. 112)

Control selection is part of the design. Choosing controls because of a condition that the exposure itself causes opens a path from exposure to selection. Among the selected, the exposure odds ratio is then pulled away from the causal odds ratio in the population. In the estrogen example the path runs through hip fracture: treatment affects hip fracture, hip fracture affects who is chosen as a control, and conditioning on having been selected induces a non-causal association. Hernán and Robins note that some of the biases Berkson described in 1946, and incidence-prevalence bias, have this structure.{{cite:hernan_robins2020}} (p. 112)

Forty cases and forty controls make the arithmetic concrete. Among the cases, 24 were exposed and 16 were not. Among the controls, 10 were exposed and 30 were not. The odds of exposure are \(24/16=1.5\) in the cases and \(10/30=1/3\) in the controls. The odds ratio is
\[
\frac{1.5}{1/3}=4.5=\frac{24\times 30}{16\times 10}.
\]
The proportion of cases in the study is \(40/80=0.5\) because the design chose equal numbers, not because half the population is a case. Adding four unexposed controls changes the control counts to 10 and 34 and the odds ratio to \((24\times 34)/(16\times 10)=5.1\). The population risk is still unidentified from these counts alone.{{cite:hernan_robins2020}} (p. 112)

## Worked example

Forty cases and forty controls are interviewed. Among the cases, 24 were exposed and 16 were not. Among the controls, 10 were exposed and 30 were not. The exposure odds ratio is \((24\times 30)/(16\times 10)=720/160=4.5\).

**Your turn.** Four more unexposed controls are added, so the controls are 10 exposed and 34 unexposed. The cases stay 24 exposed and 16 unexposed. What is the odds ratio?

::: {.callout-tip collapse="true" title="Answer"}
The odds ratio is \((24\times 34)/(16\times 10)=816/160=5.1\).
:::

## Assumptions and limits

The exposure odds ratio estimates the corresponding population contrast when the controls are drawn from the same source as the cases and inclusion depends on the outcome in a way that is the same within exposure groups. Preferential selection of controls who have a condition caused by the exposure biases that odds ratio, in the direction the estrogen and hip-fracture path illustrates.{{cite:hernan_robins2020}} (p. 112)

A causal reading needs the same extra argument that any observational comparison needs. OpenIntro's statement of that limit is that causal conclusions from observational data are not the conclusions an experiment is designed to support, and that searching for confounders does not guarantee that every confounder was measured. The absolute effect in epidemiology is a difference of risks. This design does not deliver that difference without information on how the sampling fractions differ, because the sample fraction who are cases was set by the investigator.{{cite:openintro2019}} (Ch. 1, §1.3.4){{cite:dodge2008}} (p. 62)

## Connections

The source population is a [cohort study](cohort-study.qmd) that might have been followed instead. The [control group](control-group.qmd) here is the sample of non-cases, not an experimentally untreated arm. [Causality](causality.qmd) is a further claim about the odds ratio, not a property of the sampling rule. [Sampling bias](sampling-bias.qmd) includes the bias that comes from the wrong controls. The absolute effect, a difference of risks, is the summary this design does not estimate from the sample counts alone.{{cite:hernan_robins2020}} (p. 112){{cite:dodge2008}} (p. 62)
