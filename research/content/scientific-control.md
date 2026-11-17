

## Lead context

A treatment contrast is readable when the groups differ in the treatment and are alike in everything else the investigator can hold still. Scientific control is that discipline: assign the treatment, pin down the other conditions, and keep a comparison that did not receive the experimental treatment. {{cite:openintro2019}} {{cite:nist_glossary2002}} (Glossary, "control group")

## Motivating example

Patients take a study pill with anything from a sip of water to a full glass. If the amount of water affects the outcome, the drug is tangled with the drink. Asking every patient to take the pill with a 12-ounce glass removes water as a difference between groups. That instruction is a control on a condition. It is not itself the control group. {{cite:openintro2019}}

## Intuition

An experiment is a programme for which conditions will vary and which will be held fixed. The factors that are meant to vary are set to chosen levels. The conditions that are not under study are kept common, so that a later difference has fewer alternative explanations. Random assignment covers the conditions that cannot be held fixed, because it balances them in expectation rather than by an instruction. {{cite:dodge2008}} (p. 162) {{cite:openintro2019}}

## Definition

Scientific control is the practice of assigning treatments and of controlling other differences among the units, together with the maintenance of a comparison set that does not receive the experimental treatment. {{cite:openintro2019}} {{cite:nist_glossary2002}} (Glossary, "control group")

An experimental design states the levels of each factor, or of each combination of factors, that the units will receive. The aim is a conclusion the experiment can actually support, reached by an economical plan. {{cite:dodge2008}} (p. 162) The plans used most often are the completely randomised design, the randomised block design, and the Latin square. {{cite:dodge2008}} (p. 163)

Four principles organise a randomised experiment: controlling other differences, randomising into groups, replicating so that the effect is estimated from enough cases, and blocking on a trait that is already known to matter. The first three belong in any such study. {{cite:openintro2019}}

Control of a condition is an instruction that applies to every unit, such as the common glass of water. The control group is a subset of units that do not receive the experimental treatment. The footnote distinction is the whole point: one is a shared protocol, the other is an arm of the comparison. {{cite:openintro2019}} {{cite:nist_glossary2002}} (Glossary, "control group")

Randomisation is the assignment of units to treatments by a random mechanism, not by an arbitrary or systematic rule such as "the first twelve get treatment A". {{cite:nist_glossary2002}} (Glossary, "randomization, scientific") Replication, in a single study, means a sample large enough to estimate the effect. A second study that repeats the first is replication of another kind. {{cite:openintro2019}}

Different designs are different mathematical models. The analysis that belongs to a completely randomised plan is not the analysis that belongs to a Latin square. {{cite:dodge2008}} (p. 163)

Conditions that are not measured and not randomised can still differ between groups. Control reduces the differences the protocol names. It does not name every cause. {{cite:openintro2019}} Human participants who know which arm they are in can still change their behaviour. Blinding is a further protection, not a consequence of having a control. {{cite:openintro2019}} The design's conclusion is only as wide as the levels that were actually used. {{cite:dodge2008}} (p. 162)

Experimental designs came into regular use in the 1920s, largely in agriculture. Ronald Fisher set out the principles in non-mathematical language in 1926. {{cite:dodge2008}} (p. 162) The four-principle account used in teaching now, control, randomisation, replication, and blocking, is the form in which that programme is stated for a first course. {{cite:openintro2019}}

## Statistical use

Scientific control is what makes a treated-minus-control contrast interpretable as a treatment effect rather than as a bundle of other differences. {{cite:openintro2019}} In agricultural and industrial experiments the design is chosen so that the planned comparison can be estimated and the unplanned differences are either held fixed or balanced. Variance analysis, covariance analysis, and regression are the analyses attached to those plans. {{cite:dodge2008}} (p. 163) A prospective study can include a comparison group without the investigator controlling the exposure. That comparison is weaker, because the exposure was not assigned. {{cite:nist_glossary2002}} (Glossary, "control group") {{cite:openintro2019}}

## Worked example

Twelve patients all drink a 12-ounce glass of water with their pill, so water volume does not differ. Six are randomised to the drug and six to a placebo pill. The outcome changes are 8, 10, 6, 12, 9, and 9 on the drug, summing to 54, with mean \(54/6 = 9\). The placebo changes are 2, 4, 3, 3, 5, and 1, summing to 18, with mean \(18/6 = 3\). The contrast is \(9 - 3 = 6\). The common water volume is the controlled condition. The placebo arm is the control group. {{cite:openintro2019}} {{cite:nist_glossary2002}} (Glossary, "control group")

**Your turn.** The placebo changes gain one more patient with change 4, and the drug mean stays 9. What are the new placebo mean and the new contrast?

::: {.callout-tip collapse="true" title="Answer"}
The placebo changes sum to 22 over 7 patients, so the mean is \(22/7\). The contrast is \(9 - 22/7\).
:::

## Common misconceptions

Scientific control is not a control group. Holding water intake fixed does not create an untreated arm, and an untreated arm does not by itself hold every other condition fixed. {{cite:openintro2019}}

A systematic assignment, first half treated and second half not, feels orderly and is not randomisation. Order in the list can line up with the outcome. {{cite:nist_glossary2002}} (Glossary, "randomization, scientific")



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 20. Their total is 210, so their mean is 10.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 8.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Scientific control has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 10.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [control group](control-group.qmd), [designed experiment](designed-experiment.qmd), [Blinding and placebos](blinding-and-placebo.qmd), [randomised controlled trial](randomised-controlled-trial.qmd).

Two further limits are algebraic. The sum of deviations from the mean 10.5 is zero, so the mean is the least-squares centre of these 20 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 10.5.

## Connections

The untreated arm is the [control group](control-group.qmd). The plan is a [designed experiment](designed-experiment.qmd). [Blinding and placebos](blinding-and-placebo.qmd) address knowledge of the assignment. A [randomised controlled trial](randomised-controlled-trial.qmd) is the medical form of the same principles. [Causality](causality.qmd) is the reading those principles are meant to support.
