

## Lead context

A measurement assigns a number to a unit by a procedure that can be repeated. The procedure has a scatter, and it can sit systematically off the quantity it is aimed at. Both belong to the measurement, not to the arithmetic done afterwards. {{cite:nist_glossary2002}} (Glossary, "precision") {{cite:dodge2008}} (p. 183)

## Motivating example

Two operators time the same chemical reaction. Operator A records 10, 12, 11, and 11 seconds. Operator B records 14, 16, 15, and 15 seconds. Each operator's readings cluster. The clusters are four seconds apart. If the reaction really lasts 12 seconds, A is slightly low and B is high. The procedure, not the reaction, changed. {{cite:nist_glossary2002}} (Glossary, "bias") {{cite:nist_glossary2002}} (Glossary, "repeatability")

## Definition

Measurement is the assignment of a numerical value to a characteristic by a stated procedure. A characteristic is a distinguishing feature of a process or of its output on which variables or attributes can be collected. {{cite:nist_glossary2002}} (Glossary, "characteristic")

Precision is the variability of that procedure around its own average. Accuracy is the variability around the true value, so it includes precision and the systematic offset from the true value. {{cite:nist_glossary2002}} (Glossary, "precision") {{cite:nist_glossary2002}} (Glossary, "accuracy") The error of a measurement is the difference between the estimated or observed value and the true or reference value. {{cite:dodge2008}} (p. 182)

Repeat the procedure on the same quantity under tight conditions and watch the scatter. That short-term scatter is repeatability, the part of precision that shows up when the instrument, the operator, and the setup stay fixed. A shift that survives the averaging, and that has a consistent direction, is a systematic error, the kind produced by a bad calibration. {{cite:nist_glossary2002}} (Glossary, "repeatability") {{cite:dodge2008}} (p. 183)

Averaging repeated measurements is the classical way to approximate a reference value when the error is random. The average does not cancel a systematic error that is common to every repetition. {{cite:dodge2008}} (p. 182) {{cite:nist_glossary2002}} (Glossary, "bias") A quantitative [variable](variable.qmd) is what the procedure is recording when the result is a numerical modality such as a weight, a length, or a time. {{cite:dodge2008}} (p. 440) The level of that recording, and what arithmetic it will support, is a separate decision about the scale. {{cite:dodge2008}} (p. 439)

A measurement is not the same object as a [level of measurement](levels-of-measurement.qmd). The level says whether the recorded values are names, ranks, or numbers with meaningful gaps. The measurement is the procedure that produced a numerical value and the errors that procedure carries. {{cite:dodge2008}} (p. 439) {{cite:nist_glossary2002}} (Glossary, "precision")

Agreement between operators is not accuracy. A and B can each be very repeatable and still sit on opposite sides of the true duration. {{cite:nist_glossary2002}} (Glossary, "repeatability") {{cite:nist_glossary2002}} (Glossary, "accuracy")

The [true value](true-value.qmd) is the reference. [Measurement error](measurement-error.qmd) is the difference the procedure leaves. [Data quality](data-quality.qmd) asks whether the resulting file is fit to use. [Uncertainty](uncertainty.qmd) is the caution that remains after the procedure is described. The [variable](variable.qmd) is the characteristic being recorded on each unit.

## Properties

Absolute error is the absolute difference between the observed value and the reference. Relative error divides the absolute error by the size of the quantity. {{cite:dodge2008}} (p. 183)

Random error is the chance contribution of the instrument and the user. Its statistical properties are studied with probability. Systematic error comes from consistent causes, improper calibration being the example, and it keeps its direction. The bias of a statistic is one form of systematic error. {{cite:dodge2008}} (p. 183) {{cite:dodge2008}} (p. 41)

Repeatability is the short-term component under highly controlled conditions. Reproducibility brings in the long-term and between-instrument, between-laboratory components of precision. {{cite:nist_glossary2002}} (Glossary, "repeatability") {{cite:nist_glossary2002}} (Glossary, "reproducibility")

## Worked example

Operator A's times are 10, 12, 11, and 11. The sum is 44 and the mean is \(44/4 = 11\). Operator B's times are 14, 16, 15, and 15. The sum is 60 and the mean is \(60/4 = 15\). The true duration is 12 seconds. A's bias is \(11 - 12 = -1\). B's bias is \(15 - 12 = 3\). The absolute errors for A are 2, 0, 1, and 1, summing to 4, so the mean absolute error is \(4/4 = 1\). {{cite:nist_glossary2002}} (Glossary, "bias") {{cite:dodge2008}} (p. 183)

**Your turn.** Operator A records one more time, of 16 seconds. What are A's new mean and new bias?

::: {.callout-tip collapse="true" title="Answer"}
The times sum to 60 over 5 observations, so the mean is 12. The bias is \(12 - 12 = 0\).
:::

## Assumptions and limits

The decomposition into random and systematic error assumes a reference value against which the direction of the systematic part can be judged. {{cite:dodge2008}} (p. 182) Repeatability describes a tightly held setup. It does not describe a procedure that changes operator, instrument, or laboratory. That wider scatter is reproducibility. {{cite:nist_glossary2002}} (Glossary, "reproducibility") A recorded length is discrete at the resolution of the instrument even when the quantity is treated as continuous. {{cite:dodge2008}} (p. 440)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 15. Their total is 120, so their mean is 8.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 6.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Measurement has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 8.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [variable](variable.qmd), [level of measurement](levels-of-measurement.qmd), [true value](true-value.qmd), [Measurement error](measurement-error.qmd).

Two further limits are algebraic. The sum of deviations from the mean 8.0 is zero, so the mean is the least-squares centre of these 15 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 8.0.

## History

Error distributions were introduced in the second half of the eighteenth century to describe repeated measures of the same quantity under the same conditions, and to explain why an arithmetic mean approximates the reference. Simpson's discrete distributions of 1756 and Gauss's normal distribution of 1809 are the early landmarks. {{cite:dodge2008}} (p. 182) {{cite:dodge2008}} (p. 183)
