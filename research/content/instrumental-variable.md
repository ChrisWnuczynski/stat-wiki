

## Lead context

When people do not take the treatment they were assigned, or when the treatment was never assigned at all, the comparison of those who took it with those who did not mixes the effect with the reasons they took it. An instrumental variable is a third variable that moves the treatment and, under stated conditions, does not move the outcome any other way. {{cite:hernan_robins2020}} (p. 209)

## Motivating example

In a double-blind trial, \(Z\) is the randomised assignment and \(A\) is the treatment actually received. Some participants do not adhere. Factors \(U\) that affect both adherence and the outcome confound a comparison of \(A\) with the outcome. The assignment \(Z\) is still associated with the treatment received, it is not expected to change the outcome except through that treatment, and it was randomised so that it shares no causes with the outcome. Those are the three instrumental conditions, and \(Z\) is an instrument. {{cite:hernan_robins2020}} (p. 209)

## Definition

A variable \(Z\) is an instrument for the effect of treatment \(A\) on outcome \(Y\) when three conditions hold. First, \(Z\) is associated with \(A\). Second, \(Z\) does not affect \(Y\) except through \(A\), the exclusion restriction. Third, \(Z\) and \(Y\) share no causes. {{cite:hernan_robins2020}} (p. 209) Only the first condition can be checked in the data. The other two are assumptions. {{cite:hernan_robins2020}} (p. 211)

For a binary instrument, when a fourth condition also holds, the average causal effect on the additive scale equals the usual instrumental-variable estimand
\[
\frac{\mathrm{E}[Y\mid Z=1]-\mathrm{E}[Y\mid Z=0]}{\mathrm{E}[A\mid Z=1]-\mathrm{E}[A\mid Z=0]}.
\]
{{cite:hernan_robins2020}} (p. 213) The numerator is the effect of assignment on \(Y\). The denominator is the effect of assignment on \(A\). {{cite:hernan_robins2020}} (p. 213)

Assignment changes the outcome only to the extent that it changes the treatment received. The effect of assignment on the outcome, divided by the effect of assignment on the treatment received, inflates the assignment effect back up to the effect of the treatment. If everyone adheres, the denominator is 1 and the two effects match. If few people adhere, the denominator shrinks and the treatment effect is larger than the assignment effect. {{cite:hernan_robins2020}} (p. 213)

Conditions two and three are not verified by conditioning on the treatment. Treatment is a collider on some of the paths that would be used in that check, so the check can show an association even when the exclusion restriction holds. {{cite:hernan_robins2020}} (p. 211) A weak denominator makes the ratio, and its interval, too wide to be informative, as in the estimate \(2.4\) whose interval ran from \(-36.5\) to \(41.3\). {{cite:hernan_robins2020}} (p. 213) Without the fourth condition the three instrumental conditions do not identify the average effect. {{cite:hernan_robins2020}} (p. 213)

## Properties

In a randomised experiment the numerator and the denominator can each be estimated without adjustment, because \(Z\) was randomised. The ratio is the Wald estimator. {{cite:hernan_robins2020}} (p. 213) Randomised assignment, as against an arbitrary or systematic split, is what makes that lack of adjustment reasonable: the investigator assigns treatments by a random mechanism. {{cite:openintro2019}} {{cite:nist_glossary2002}} (Glossary, "randomization, scientific")

The same ratio is obtained by two-stage least squares. Fit \(\mathrm{E}[A\mid Z] = \alpha_0 + \alpha_1 Z\), replace \(A\) by its prediction, and fit the outcome on that prediction. The slope equals the ratio of the two differences. {{cite:hernan_robins2020}} (p. 213)

A weak instrument, one for which the denominator is close to zero, produces an unstable ratio. A rule of thumb treats the instrument as weak when the first-stage \(F\) statistic is under 10. In one smoking-cessation example the numerator was \(2.686 - 2.536 = 0.1503\), the denominator was \(0.2578 - 0.1951 = 0.0627\), and the ratio was \(0.1503/0.0627 = 2.4\) kilograms, with a confidence interval from \(-36.5\) to \(41.3\) and a first-stage \(F\) of \(0.8\). {{cite:hernan_robins2020}} (p. 213)

## Statistical use

The instrument is the assignment indicator in a trial with non-adherence. In an observational study a candidate instrument might be a price, a distance to a facility, a physician's preference, or a genetic variant. Whether it meets the exclusion restriction and shares no causes with the outcome is a subject-matter argument, not a test that the data can settle. {{cite:hernan_robins2020}} (p. 211) {{cite:hernan_robins2020}} (p. 209) The three conditions alone do not make the ratio equal to the average treatment effect. A fourth condition, discussed after the estimand is defined, is required for that reading. {{cite:hernan_robins2020}} (p. 213)

## Worked example

Among people with \(Z = 1\), the mean outcome is 11 and the proportion treated is \(0.75\). Among people with \(Z = 0\), the mean outcome is 7 and the proportion treated is \(0.25\). The numerator is \(11 - 7 = 4\). The denominator is \(0.75 - 0.25 = 0.5\). The instrumental-variable estimand is \(4/0.5 = 8\). {{cite:hernan_robins2020}} (p. 213)

**Your turn.** The proportion treated when \(Z = 1\) is \(0.65\) instead of \(0.75\), and the other three numbers stay the same. What is the estimand?

::: {.callout-tip collapse="true" title="Answer"}
The numerator is still \(4\). The denominator is \(0.65 - 0.25 = 0.4\). The estimand is \(4/0.4 = 10\).
:::

## Common misconceptions

Any variable associated with treatment is not an instrument. Association is the first condition. The variable must also have no path to the outcome except through treatment, and no common cause with the outcome. A price that changes treatment and also changes the outcome directly fails the second condition. {{cite:hernan_robins2020}} (p. 209) {{cite:hernan_robins2020}} (p. 211)

The ratio is not the average causal effect merely because the arithmetic was done. The fourth condition has to be added to the three instrumental conditions. {{cite:hernan_robins2020}} (p. 213)

## History

The ratio of the two assignment effects is the Wald estimator. {{cite:hernan_robins2020}} (p. 213) Using a genetic variant as the instrument is the later pattern called Mendelian randomisation. Preference of a physician, and access measured by distance or by calendar time, are the other families of candidate instruments used when no one randomised the treatment. {{cite:hernan_robins2020}} (p. 211)

## Connections

The target, when the fourth condition holds, is the [average treatment effect](average-treatment-effect.qmd). [Causality](causality.qmd) is the contrast of potential outcomes inside that effect. A [natural experiment](natural-experiment.qmd) is a setting in which a candidate instrument was produced outside the study. [Difference in differences](difference-in-differences.qmd) is the alternative that uses a pre-treatment outcome instead of an instrument. [Blinding and placebos](blinding-and-placebo.qmd) are what make the exclusion restriction plausible for a randomised assignment. {{cite:hernan_robins2020}} (p. 209)
