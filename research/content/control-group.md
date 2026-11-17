## Lead context
An effect is a comparison. The control group is the set of observations that do not receive the experimental treatment, and it is the reference against which the treated observations are judged. {{cite:nist_glossary2002}} (Glossary, "control group")

## Motivating example
In a trial of a stent meant to prevent stroke, 224 patients were assigned to the stent and 227 to medical management without it. By the end of the first year, 45 of the 224 treated patients and 28 of the 227 untreated patients had had a stroke. The untreated patients are the control group: the same clinical setting, without the device under test. The proportions are \(45/224\) and \(28/227\). {{cite:openintro2019}} (p. 10) {{cite:openintro2019}} (p. 9)

## Intuition
If everyone is treated, a later improvement has nothing to be compared with. The control group holds the comparison fixed: same kind of person, same follow-up, no experimental treatment. The treated results are then read as a departure from that reference, not as a number floating on its own. {{cite:nist_glossary2002}} (Glossary, "control group") {{cite:openintro2019}} (p. 33)

## Definition
The control group is the set of observations in an experiment or a prospective study that do not receive the experimental treatment. Those observations serve as a comparison point for the size of the treatment contrast, as a check against what has been seen before, and as a source of information about the variation that is present without the treatment. {{cite:nist_glossary2002}} (Glossary, "control group")

In a human experiment the treatment group receives the drug and the control group does not. When the assignment is random, the two groups are the arms of a randomised experiment. {{cite:openintro2019}} (p. 33) {{cite:openintro2019}} (p. 32)

## Properties
The control condition has to be specified. "No drug" is one control. A placebo pill, or the prevailing medical management, is another. The stent trial's control was the same medical management without the stent, so the contrast is stent against that management, not stent against no care at all. {{cite:openintro2019}} (p. 9) {{cite:openintro2019}} (p. 10)

The group is a set of observations, not a property of a single person. A person is in it because of the assignment or the eligibility rule. Random assignment is what makes membership unpredictable from the traits that also affect the outcome. {{cite:openintro2019}} (p. 32) {{cite:nist_glossary2002}} (Glossary, "randomization, scientific")

Blocking can force the control group to contain the same mix of a known trait as the treated group. Patients are split into low-risk and high-risk blocks, and then half of each block is assigned to the control group. {{cite:openintro2019}} (p. 32)

## Statistical use
The treated mean minus the control mean is the estimate of the treatment contrast when the design supports that reading. In the stent counts the comparison is between \(45/224\) and \(28/227\). {{cite:openintro2019}} (p. 10) The control group also supplies a picture of the outcome's variation in the absence of the experimental treatment, which is part of judging whether a treated departure is large. {{cite:nist_glossary2002}} (Glossary, "control group")

In a prospective observational study the group that did not receive the exposure plays the same reference role, without the protection of assignment. {{cite:nist_glossary2002}} (Glossary, "control group") {{cite:openintro2019}} (p. 25)

## Worked example
A small trial assigns 20 patients at random, 10 to a drug and 10 to control. Deaths are 2 in the drug group and 5 in the control group. The risks are \(2/10 = 0.2\) and \(5/10 = 0.5\). The risk difference, drug minus control, is \(0.2 - 0.5 = -0.3\). {{cite:openintro2019}} (p. 33) {{cite:nist_glossary2002}} (Glossary, "control group")

**Your turn.** One further control patient is added and dies. What are the new control risk and the new risk difference, with the drug risk still \(0.2\)?

::: {.callout-tip collapse="true" title="Answer"}
The control group has 6 deaths among 11 patients, so the risk is \(6/11\). The risk difference is \(0.2 - 6/11\).
:::

## Common misconceptions
The control group is not the group that receives a worse treatment by design. It is the group that does not receive the experimental treatment. A placebo is one way to build that group so that the act of being given a pill is shared. {{cite:openintro2019}} (p. 33) {{cite:openintro2019}} (p. 32)

Controlling other conditions, such as asking every patient to drink the same amount of water with a pill, is a different precaution. It is not the same object as the control group. {{cite:openintro2019}} (p. 32)

## Assumptions and limits
A control group that was formed by offering the treatment to whoever asked for it does not, by itself, estimate the effect of the treatment. The comparison estimates an effect when assignment, or an argument that replaces assignment, makes the groups comparable. {{cite:openintro2019}} (p. 32) {{cite:openintro2019}} (p. 25) The contrast is only as sharp as the control condition. A control that quietly receives a version of the treatment answers a different question. {{cite:openintro2019}} (p. 9)

## Connections
[Scientific control](scientific-control.qmd) is the broader practice of holding conditions fixed and of providing a comparison. A [designed experiment](designed-experiment.qmd) is the plan that creates the group. [Blinding and placebos](blinding-and-placebo.qmd) keep knowledge of assignment from changing the outcome. The [average treatment effect](average-treatment-effect.qmd) is the population contrast the two groups are used to estimate. A [randomised controlled trial](randomised-controlled-trial.qmd) is the experiment in which the control group is produced by random assignment.

## History
Using an explicit comparison group, rather than a before-and-after impression, is part of what experimental design added to agricultural and later medical trials in the twentieth century. Completely randomised designs, randomised blocks, and Latin squares are the classical plans that decide who is untreated. {{cite:dodge2008}} (p. 162) {{cite:dodge2008}} (p. 163) The stent comparison is a modern medical instance of the same role: a counted untreated group against which the treated proportion is read. {{cite:openintro2019}} (p. 10)
