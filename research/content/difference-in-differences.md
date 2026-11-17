## Lead context
Sometimes the treated and the untreated already differ, and the difference was visible before anyone was treated. Difference in differences subtracts that earlier gap from the later gap, and treats what remains as the effect in the treated. {{cite:hernan_robins2020}} (p. 106)

## Motivating example
Aspirin use and blood pressure share causes, such as a history of heart disease, that were not measured. Standardisation cannot block that path. Blood pressure was also recorded before aspirin was available. That earlier measurement cannot have been caused by the later aspirin, and it can still show how large the confounding gap was. Removing that gap from the later contrast is the difference-in-differences step. {{cite:hernan_robins2020}} (p. 106)

## Intuition
Write two changes: how the outcome moved in the treated group, and how it moved in the comparison group. If the comparison group is a guide to the change the treated group would have experienced anyway, the extra change in the treated group is the effect. Equivalently, subtract the pre-treatment gap between the groups from the post-treatment gap. {{cite:hernan_robins2020}} (p. 106)

## Definition
Let \(A\) be treatment, \(Y\) the outcome after treatment is available, and \(C\) a pre-treatment measurement of the outcome, a negative outcome control. The effect of treatment on the treated, on the additive scale, is identified by
\[
\mathrm{E}[Y^{1}-Y^{0}\mid A=1]
= \bigl(\mathrm{E}[Y\mid A=1]-\mathrm{E}[Y\mid A=0]\bigr)
- \bigl(\mathrm{E}[C\mid A=1]-\mathrm{E}[C\mid A=0]\bigr)
\]
when the additive confounding is the same for \(C\) and for the untreated potential outcome \(Y^{0}\). That common confounding is the assumption of additive equi-confounding. {{cite:hernan_robins2020}} (p. 106)

The pre-treatment contrast \(\mathrm{E}[C\mid A=1]-\mathrm{E}[C\mid A=0]\) is not a causal effect of \(A\) on \(C\). It is a measure of confounding, because \(A\) does not cause a measurement taken before \(A\) existed. {{cite:hernan_robins2020}} (p. 106)

## Properties
The same number can be computed as a difference of changes. The change in the treated group is \(\mathrm{E}[Y\mid A=1]-\mathrm{E}[C\mid A=1]\). The change in the comparison group is \(\mathrm{E}[Y\mid A=0]-\mathrm{E}[C\mid A=0]\). Subtracting those changes reproduces the display above. {{cite:hernan_robins2020}} (p. 106)

The method adjusts for unmeasured confounding only under additive equi-confounding. It is more restrictive than the general idea of a negative outcome control: \(Y\) and \(C\) have to be on the same scale, and both a pre-treatment and a post-treatment measurement are required. {{cite:hernan_robins2020}} (p. 106)

Measured covariates can be adjusted for at the same time, by parametric or semiparametric versions of the same contrast. {{cite:hernan_robins2020}} (p. 106)

## Statistical use
Difference in differences is used when conditional exchangeability given the measured covariates is not believed, and a pre-treatment outcome is available to stand in for the unmeasured common causes. It sits with instrumental-variable estimation as a method that trades one unverifiable assumption for another. {{cite:hernan_robins2020}} (p. 104) {{cite:hernan_robins2020}} (p. 106) The target it identifies, under the assumption above, is the average effect in the treated, not automatically the average effect in the whole population. {{cite:hernan_robins2020}} (p. 106) {{cite:hernan_robins2020}} (p. 5)

## Worked example
Mean blood pressure, in millimetres of mercury, is 150 before and 140 after among aspirin users, and 148 before and 146 after among non-users. The post-treatment gap is \(140 - 146 = -6\). The pre-treatment gap is \(150 - 148 = 2\). The difference in differences is \(-6 - 2 = -8\). As changes: users fall by \(150 - 140 = 10\), non-users fall by \(148 - 146 = 2\), and \(10 - 2 = 8\) millimetres, with the sign recording a larger fall in the treated group. The effect in the treated is \(-8\) if additive equi-confounding holds. {{cite:hernan_robins2020}} (p. 106)

**Your turn.** The non-users' later mean is 144 instead of 146, and nothing else changes. What is the difference in differences?

::: {.callout-tip collapse="true" title="Answer"}
The post-treatment gap is \(140 - 144 = -4\). The pre-treatment gap is still \(2\). The difference in differences is \(-4 - 2 = -6\).
:::

## Common misconceptions
A larger change in the treated group is not yet an effect. It is an effect in the treated only if the comparison group's change equals the change the treated group would have had without treatment. That is the equi-confounding assumption, and it is not guaranteed by having two time points. {{cite:hernan_robins2020}} (p. 106)

The pre-treatment gap is not evidence that the treatment was already working. The treatment was not yet there. The gap is confounding, visible early. {{cite:hernan_robins2020}} (p. 106)

## Assumptions and limits
Additive equi-confounding can fail when the groups are diverging for reasons that change over time, or when \(C\) and \(Y\) are not the same measurement. The method needs both waves on a common scale. {{cite:hernan_robins2020}} (p. 106) It does not replace random assignment. It is an observational correction whose identifying assumption cannot be verified from the same contrast that it corrects. {{cite:hernan_robins2020}} (p. 104) {{cite:openintro2019}} (p. 25)

## Connections
The target is a version of the [average treatment effect](average-treatment-effect.qmd), restricted to the treated. [Causality](causality.qmd) here is the counterfactual change \(Y^{1}-Y^{0}\). An [instrumental variable](instrumental-variable.qmd) is the other standard route when a common cause is unmeasured. A [natural experiment](natural-experiment.qmd) is often analysed with this contrast when a policy arrives in one place and not another. The comparison series plays the role of a [control group](control-group.qmd) that was not assigned by the investigator.

## History
The pre-treatment outcome as a negative control, and the subtraction of the two gaps, is the construction known in economics as difference in differences. {{cite:hernan_robins2020}} (p. 106) It remains a restrictive special case of negative-outcome-control methods, which can sometimes put the two measurements on different scales. {{cite:hernan_robins2020}} (p. 106)
