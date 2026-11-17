## Lead context
Two measurements can rise together because one produces the other, because the other produces the first, or because a third factor produces both. The warning that correlation does not imply causation is the rule that an observed association, however strong, is not by itself a causal effect.{{cite:openintro2019}} (Ch. 1, §1.2.5) {{cite:hernan_robins2020}} (Ch. 1, §1.5, pp. 11–12)

## Motivating example
In a population of 20 people, 13 receive a treatment and 7 do not. Among the treated, 7 die, so the mortality risk is \(7/13\). Among the untreated, 3 die, so the risk is \(3/7\). The treated risk is higher. If instead every one of the 20 had been treated, 10 would have died, and if every one had been untreated, 10 would have died. The two counterfactual risks are equal. The association is real, and the causal effect on the risk is zero. A physician who withholds the treatment because the treated patients died more often is reading the association as if it were the effect.{{cite:hernan_robins2020}} (Ch. 1, §1.5, pp. 11–12)

## Intuition
Association compares the people who actually received one exposure with the people who actually received another. Causation compares the same people under two exposures, only one of which can be observed. Those are different splits of the population. The first split follows how treatment was handed out. The second split is the contrast a decision needs: what the risk would be if the exposure were changed. When the people who receive the exposure were already at higher risk, the first split and the second split disagree.{{cite:hernan_robins2020}} (Ch. 1, §1.5, pp. 11–12)

A randomised experiment is the design that makes the two splits answer the same question. Assignment by a coin, or by another mechanism that ignores prognosis, puts comparable people in each group. An observational comparison leaves the assignment as it was. In general, association does not imply causation, and a causal reading is the one a randomised experiment is built to support.{{cite:openintro2019}} (Ch. 1, §1.2.5; §1.4)

## Definition
For a binary exposure \(A\) and a binary outcome \(Y\), association means that the risk in the people who received treatment differs from the risk in the people who did not: \(\Pr(Y=1\mid A=1)\neq \Pr(Y=1\mid A=0)\). For a continuous outcome the same idea is a difference of conditional means. Causation is a contrast of the risks that would be seen if the whole population were treated and if the whole population were untreated. Equality of those two counterfactual risks is the absence of a causal effect, even when the conditional risks differ.{{cite:hernan_robins2020}} (Ch. 1, §1.5, pp. 11–12)

The same gap appears for a [correlation](correlation.qmd). A large Pearson correlation says that a straight-line summary of the pairs is steep relative to the noise. It does not say which variable would move if the other were changed. An observational study can provide evidence of a naturally occurring association. It does not, by itself, show a causal connection.{{cite:openintro2019}} (Ch. 1, §1.2.5)

In epidemiology the strength of an association is one piece of a causal argument, and it is not sufficient. The exposure has to precede the outcome, and the analyst has to deal with a factor that is tied to both and is not itself the cause being claimed. The absolute effect is the risk in the exposed minus the risk in the unexposed. The relative effect is their ratio. A risk of \(0.2\%\) among the exposed and \(0.1\%\) among the unexposed has the same ratio as a risk of \(20\%\) and \(10\%\), and the number of cases removed by taking the exposure away is far larger in the second population.{{cite:dodge2008}} (pp. 62–63)

## Statistical use
Report the association with a [scatterplot](scatterplot.qmd), a difference of risks, an [odds ratio](odds-ratio.qmd), or a regression coefficient, and say which comparison it is. If the claim is causal, say how the exposure was assigned. A [randomised controlled trial](randomised-controlled-trial.qmd) or another [designed experiment](designed-experiment.qmd) is the direct way to make the groups exchangeable. In an [observational study](observational-study.qmd), stratification or a regression that holds the common causes fixed is an attempt to reconstruct the contrast that randomisation would have given. The attempt stands or falls with the claim that the measured variables are the right ones.{{cite:openintro2019}} (Ch. 1, §1.2.5; §1.3.4) {{cite:dodge2008}} (p. 62)

A [confounding variable](confounding-variable.qmd) is one route to the disagreement: a common cause of exposure and outcome. Other routes exist. The outcome can influence the exposure. The sample can be selected on a variable related to both. None of these is repaired by a smaller [p-value](p-value.qmd) or a larger sample. A large sample makes a real association more precisely estimated. It does not turn the association into a causal effect.{{cite:hernan_robins2020}} (Ch. 1, §1.5, pp. 11–12) {{cite:openintro2019}} (Ch. 1, §1.3.4)

The counterfactual contrast assumes a well-defined intervention. "Being the sort of person who takes the treatment" is not an intervention. The randomised comparison assumes the assignment mechanism ignored prognosis. The observational adjustment assumes that the measured covariates block the common causes. None of these is a property of the correlation coefficient. Time order is a separate requirement: a factor that is measured after the outcome cannot be the cause of that outcome.{{cite:dodge2008}} (p. 62) {{cite:openintro2019}} (Ch. 1, §1.2.5)

## Worked example
Take the 20 people above. Treated mortality is \(7/13\). Untreated mortality is \(3/7\). Cross-multiplying, \(7\times 7=49\) and \(3\times 13=39\), so \(7/13>3/7\). The associational risk difference is
\[
\frac{7}{13}-\frac{3}{7}=\frac{49-39}{91}=\frac{10}{91}.
\]
The causal risks are \(10/20\) and \(10/20\), so the causal risk difference is \(0\). The associational difference is \(10/91\) on the risk scale, and the causal difference is zero.{{cite:hernan_robins2020}} (Ch. 1, §1.5, pp. 11–12)

**Your turn.** Suppose instead that 8 of the 20 would die if everyone were treated and 12 of the 20 would die if everyone were untreated. What is the causal risk difference, treated minus untreated?

::: {.callout-tip collapse="true" title="Answer"}
The causal risks are \(8/20\) and \(12/20\). The difference is \(8/20-12/20=-4/20=-1/5\).
:::

## Common misconceptions
A correlation of \(0.9\) is still an association. Magnitude is not a substitute for design. A non-significant association is not evidence that there is no causal effect; the study may be small, or the effect may be present and the association cancelled by confounding. A significant association in a huge observational file is still an association. Randomisation answers the effect of the assigned treatment in the people who were randomised.{{cite:openintro2019}} (Ch. 1, §1.2.5; §1.4) {{cite:hernan_robins2020}} (Ch. 1, §1.5, pp. 11–12)

## Connections
The [correlation](correlation.qmd) and the [sample correlation coefficient](sample-correlation-coefficient.qmd) measure linear association. The [confounding variable](confounding-variable.qmd) is one reason the association and the causal effect differ. [Epidemiology](epidemiology.qmd) uses the same distinction when it separates a relative risk from a claim that removing the exposure would remove the cases. The separation is old there: a cause is an agent that changes health, and the effect is the change in risk. Writers on the subject have long required more than a large ratio.{{cite:dodge2008}} (pp. 62–63) [Econometrics](econometrics.qmd) meets the identical gap when schooling and wages move together. The modern formulation writes the two risks, associational and counterfactual, as different mathematical objects.{{cite:hernan_robins2020}} (Ch. 1, §1.5, pp. 11–12)
