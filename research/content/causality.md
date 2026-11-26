## Lead context

Two groups can differ because a treatment changed the outcome, or because the groups differed already. Causality, in the sense used here, is the first of those readings: a contrast between what would happen under one action and what would happen under another, for the same units. Association is the second reading, a contrast between units that already received different actions.{{cite:hernan_robins2020}} (pp. 3–4){{cite:openintro2019}} (Ch. 1, §1.4)

## Motivating example

A patient dies five days after a heart transplant. That fact alone does not say the transplant caused the death. The causal question is whether that patient would have been alive at five days without the transplant. If the answer is yes, the two potential outcomes differ and the transplant had an effect on that patient. If the patient would have died either way, the transplant had no effect on that outcome. The death certificate records the outcome that occurred. It does not record the outcome under the action that was not taken.{{cite:hernan_robins2020}} (pp. 3–4)

## Definition

For a binary treatment, write $Y^{a=1}$ for the outcome under treatment and $Y^{a=0}$ for the outcome under no treatment. The treatment has a causal effect on a person's outcome when $Y^{a=1}\neq Y^{a=0}$. In a population the average effect is present when the means differ, $\E[Y^{a=1}]\neq\E[Y^{a=0}]$. For a binary outcome the mean is a risk, so the average contrast is a difference of risks.{{cite:hernan_robins2020}} (pp. 4–5)

One of the two potential outcomes matches the outcome that was actually seen. If the person received treatment $A=a$, the observed outcome equals $Y^{a}$. The other potential outcome is not seen. Individual effects are therefore not identified from the observed data: they are not a function of the outcomes that were recorded.{{cite:hernan_robins2020}} (p. 4)

In epidemiology a cause is an agent that changes health, and the effect is a risk comparison. The absolute effect is the risk in the exposed minus the risk in the unexposed. The relative effect is the ratio of those risks. A cause that produces the effect by itself is called sufficient. The absolute effect is the summary that counts extra cases. The relative effect is the summary that describes the strength of the association between the agent and the illness.{{cite:dodge2008}} (p. 62)

The potential outcome under a treatment is defined for one person only when that person's treatment does not depend on how others are treated. Hernán and Robins state the restriction as no interference. If one person's treatment changes another's outcome, the counterfactual for a single person is not fixed until the allocation to everyone else is fixed as well.{{cite:hernan_robins2020}} (p. 5)

## Properties

Association is a contrast of observed outcomes between groups that received different treatments. Causation is a contrast of potential outcomes under the two treatments in the same people. The two contrasts agree when the groups are exchangeable, which is what random assignment is designed to produce. OpenIntro describes a randomised experiment, with the treatment assigned by the investigator, as the design used when the aim is a causal connection between two variables.{{cite:openintro2019}} (Ch. 1, §1.4){{cite:hernan_robins2020}} (p. 5)

A relative effect can be large when the baseline risk is small, and an absolute effect can be large when many people are affected. Dodge's comparison of two populations of $100000$ makes the arithmetic explicit. Risks of $0.2\%$ and $0.1\%$ give a relative effect of $2$ and $100$ avoidable cases. Risks of $20\%$ and $10\%$ give the same relative effect of $2$ and $10000$ avoidable cases. The ratio answers a different question from the difference.{{cite:dodge2008}} (p. 63){{cite:hernan_robins2020}} (p. 7)

The supposed cause has to precede the effect. A factor that is only statistically tied to the real cause is a confusion factor, and the association it produces is not the effect. Dodge lists that temporality requirement and the exclusion of a confusion factor as conditions on top of the strength of the association. An association, however large, does not by itself establish the temporal order or rule out the confusion factor.{{cite:dodge2008}} (p. 62)

## Statistical use

A randomised experiment assigns the treatment and is the standard design when the aim is a causal connection. An observational study, in which no treatment is assigned, is the design OpenIntro describes as generally sufficient to show an association or to form a hypothesis that an experiment might later check. Sun exposure can make both sunscreen use and skin cancer more common, so the association between sunscreen and cancer can point the wrong way. Searching for measured confounders can narrow the gap. It does not guarantee that every confounder was measured.{{cite:openintro2019}} (Ch. 1, §1.3.4, §1.4)

Even if every potential outcome in a sample were known, the sample proportion estimates the population risk and need not equal it. A causal conclusion from a sample is an inference about the population contrast, not a direct count of a census of counterfactuals. In the worked numbers below the five people are the population, so the means are the population means. A sample from a larger population would estimate those means.{{cite:hernan_robins2020}} (pp. 5, 8)

## Worked example

Five people have outcomes under treatment $1, 0, 1, 1, 0$ and under no treatment $0, 0, 1, 0, 0$. The individual effects, treatment minus no treatment, are $1, 0, 0, 1, 0$. Two of the five effects are nonzero. The mean under treatment is $3/5=0.6$ and the mean under no treatment is $1/5=0.2$, so the average causal effect is $0.6-0.2=0.4$.{{cite:hernan_robins2020}} (pp. 4–5)

**Your turn.** The third person's outcome under no treatment is corrected from $1$ to $0$. The treatment outcomes stay $1, 0, 1, 1, 0$. What are the new mean under no treatment and the new average causal effect?

::: {.callout-tip collapse="true" title="Answer"}
The outcomes under no treatment are $0, 0, 0, 0, 0$, so the mean is $0$. The average causal effect is $0.6-0=0.6$.
:::

## Common misconceptions

A statistically detectable association is not a cause. The strength of an association is one item in the epidemiological list. Temporality, and evidence that the factor is not standing in for another factor, are further items. A large risk ratio in a large study and a non-significant ratio in a small study of the same proportions are different statements about sampling error. Neither statement is the argument that the exposure precedes the outcome and is not a confusion factor.{{cite:dodge2008}} (pp. 61–62)

Seeing that treated patients fare worse does not establish harm. The treated patients may have been the sicker ones. The contrast of observed outcomes mixes the effect with whatever else differs between the groups, unless the groups were formed so that the mixture cancels. Random assignment is the design aimed at that cancellation.{{cite:hernan_robins2020}} (p. 3){{cite:openintro2019}} (Ch. 1, §1.4)

## History

Cause and effect, as a risk comparison, have been part of the language of epidemiology since its beginnings in the seventeenth century. The absolute effect and the relative effect are the two forms of that comparison: a difference of risks and a ratio of risks. The potential-outcome notation is a way to write the same comparison so that an average over a population is a well-defined number, including the case in which the average is zero while some individual contrasts are not.{{cite:dodge2008}} (p. 62){{cite:hernan_robins2020}} (pp. 3–5)

## Connections

The [average treatment effect](average-treatment-effect.qmd) is the population mean of the individual contrasts. A [designed experiment](designed-experiment.qmd) assigns the action. A [cohort study](cohort-study.qmd) and a [case-control study](case-control-study.qmd) record actions that were not assigned. The [response variable](response-variable.qmd) is the outcome in the contrast, and the [explanatory variable](explanatory-variable.qmd) is the action or exposure. Methods that avoid measuring every common cause, such as [difference in differences](difference-in-differences.qmd), replace that requirement with a different identifying condition.{{cite:hernan_robins2020}} (p. 5){{cite:openintro2019}} (Ch. 1, §1.4)
