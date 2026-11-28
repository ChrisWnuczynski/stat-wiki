## Lead context

A treatment contrast is an average when the question is about a population rather than about one person. The same intervention can help one person and harm another. The quantity used to summarise that mixture is the average treatment effect: a contrast of mean outcomes under two stated actions in a stated population.{{cite:hernan_robins2020}} (pp. 4–5)

## Motivating example

Twenty members of one family can each be imagined under a heart transplant and under no transplant. In Hernán and Robins's table, 10 of the 20 would die if everyone received the transplant, and 10 of the 20 would die if no one did. The risks are

$$
\Pr(Y^{a=1}=1)=\frac{10}{20}=0.5, \qquad \Pr(Y^{a=0}=1)=\frac{10}{20}=0.5.
$$


The average effect in that population is zero. The null hypothesis of no average causal effect is the statement that those two risks are equal. The table is not a list of identical pairs: individual counterfactual outcomes differ, and the average of the differences is still zero because the two column means match.{{cite:hernan_robins2020}} (pp. 4–5)

## Definition

For a binary treatment, write $Y^{a=1}$ for the outcome that would be seen under treatment and $Y^{a=0}$ for the outcome under the comparison. An average causal effect is present when the population means differ,

$$
\E[Y^{a=1}] \neq \E[Y^{a=0}].
$$


For a binary outcome the mean is the risk, so the same contrast is $\Pr(Y^{a=1}=1)-\Pr(Y^{a=0}=1)$. The actions being compared have to be stated. "Transplant" against "no transplant" is one contrast. A different comparison is a different average effect.{{cite:hernan_robins2020}} (p. 5)

The definition uses one person's outcome under an action that does not depend on other people's actions. If one person's treatment changes another's outcome, the counterfactual $Y^{a}$ for a single person is not fixed until the whole allocation is specified. Hernán and Robins record that restriction as the assumption of no interference, the condition Cox called no interaction between units and that sits inside the stable-unit-treatment-value assumption.{{cite:hernan_robins2020}} (p. 5)

Only one of the two potential outcomes is observed for any real person. If the person received treatment $A=a$, the observed outcome equals $Y^{a}$. The other potential outcome is missing. The average is a target defined on the full table of potential outcomes. It is not a column that can be computed by subtraction inside the observed data set. Individual effects are not identified from the observed data for that reason.{{cite:hernan_robins2020}} (p. 4)

## Interpretation

On the additive scale the effect counts extra cases. A risk of $0.2$ under treatment and $0.3$ under the comparison is a risk difference of $0.2-0.3=-0.1$: ten fewer outcome events per hundred people. The same pair of risks has ratio $0.2/0.3$. In epidemiology the absolute effect is the risk in the exposed minus the risk in the unexposed, and the relative effect is the ratio of those risks. Which summary is used depends on whether the question is about the number of cases or about the fold change.{{cite:hernan_robins2020}} (p. 7){{cite:dodge2008}} (p. 62)

Dodge's numerical comparison makes the distinction sharp. In a population of $100000$, risks of $0.2\%$ exposed and $0.1\%$ unexposed give a relative effect of $0.2/0.1=2$ and an absolute effect of $0.1$ percentage points, hence $0.001\times 100000=100$ avoidable cases. Risks of $20\%$ and $10\%$ give the same relative effect of $2$ and an absolute effect of $10$ percentage points, hence $10000$ avoidable cases. The ratio does not say how many people are affected. The difference does.{{cite:dodge2008}} (p. 63)

A null average does not mean the treatment does nothing to every person. It means the population means match. In the twenty-person transplant population both risks are $0.5$, so the average effect is null, while the rows of the table are not all ties. A randomised experiment estimates the average by comparing the treated group with the [control group](control-group.qmd), because random assignment is designed to make the groups exchangeable in expectation. In an observational study the same contrast is the target only after the identifying conditions are stated. A sample proportion estimates the population risk, and the sample contrast is not the population average itself.{{cite:hernan_robins2020}} (pp. 5, 8){{cite:openintro2019}} (Ch. 1, §1.4)

## Worked example

Eight patients have potential outcomes under treatment $1, 0, 1, 0, 1, 0, 0, 1$ and under no treatment $1, 1, 0, 0, 1, 1, 0, 0$, where $1$ is the outcome event. The treatment outcomes sum to $4$, so the mean is $4/8=0.5$. The comparison outcomes also sum to $4$, so the mean is $4/8=0.5$. The average treatment effect on the risk difference is $0.5-0.5=0$.

Compare the two outcomes person by person. They differ in the second position ($0$ against $1$), the third ($1$ against $0$), the sixth ($0$ against $1$), and the eighth ($1$ against $0$). They agree in the other four positions. Four of the eight patients have different outcomes under the two actions, in a population whose average effect is zero.{{cite:hernan_robins2020}} (p. 5)

**Your turn.** Change the last patient's outcome under treatment from $1$ to $0$, and leave the comparison outcomes unchanged. What are the new mean under treatment and the average treatment effect?

::: {.callout-tip collapse="true" title="Answer"}
The treatment outcomes sum to 3, so the mean is $3/8$. The average treatment effect is $3/8 - 4/8 = -1/8$.
:::

## Connections

[Causality](causality.qmd) is the contrast of potential outcomes of which the average treatment effect is the population summary. A [designed experiment](designed-experiment.qmd) assigns the action and is the design OpenIntro describes for a causal connection between two variables. An [instrumental variable](instrumental-variable.qmd) is another route when adherence is incomplete. The absolute and relative effects in epidemiology are the risk difference and the risk ratio for the same pair of population risks.{{cite:hernan_robins2020}} (pp. 5, 7){{cite:openintro2019}} (Ch. 1, §1.4){{cite:dodge2008}} (p. 62)

## History

Comparing what would have happened under two actions is the reasoning the potential-outcome notation writes down so that an average over a population is a defined number. Hernán and Robins take the population average, rather than the individual contrast, as the version that can be tied to observed frequencies, because one of the two potential outcomes is missing for each person. In epidemiology the same contrast has been described as a risk comparison since the seventeenth-century origins of the subject: an absolute effect is a difference of risks, and a relative effect is their ratio. The twenty-person transplant table is a modern statement of the case in which those two risks match and the average effect is null.{{cite:hernan_robins2020}} (pp. 3–5){{cite:dodge2008}} (p. 62)
