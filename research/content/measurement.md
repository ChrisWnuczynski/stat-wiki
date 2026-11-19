## Lead context

A measurement assigns a number to a unit by a procedure that can be repeated. The procedure has a scatter, and it can sit systematically off the quantity it is aimed at. Both belong to the measurement. The error of a measurement is the difference between the estimated or observed value and the true or reference value. Averaging repeated readings is a way to shrink the chance part of that difference. It does not shrink a systematic part that is common to every reading.{{cite:dodge2008}} (pp. 182–183, Error){{cite:nist_glossary2002}} (Glossary, "precision")

## Motivating example

Two operators time the same chemical reaction. Operator A records 10, 12, 11, and 11 seconds. Operator B records 14, 16, 15, and 15 seconds. Each operator's readings cluster. The clusters are four seconds apart. If the reaction really lasts 12 seconds, A is slightly low on average and B is high. The procedure, not the reaction, changed. The short-term scatter inside each operator's list is one component of precision. The gap between each operator's average and 12 seconds is bias, the difference between the average of the readings and the reference value.{{cite:nist_glossary2002}} (Glossary, "bias" and "repeatability"){{cite:dodge2008}} (p. 183, systematic error)

## Definition

Measurement is the assignment of a numerical value to a characteristic by a stated procedure. A characteristic is a distinguishing feature of a process or of its output on which variables or attributes can be collected.{{cite:nist_glossary2002}} (Glossary, "characteristic")

Precision is the variability of that procedure around its own average. Accuracy is the total variation around the true value, so it includes precision and the systematic offset between the average of the measured values and the true value. Measures of precision are not affected by bias. Accuracy degrades as bias increases. The error of one reading is the difference between the observed value and the reference value. Absolute error is the absolute value of that difference. Relative error divides the absolute error by the size of the quantity.{{cite:nist_glossary2002}} (Glossary, "precision" and "accuracy"){{cite:dodge2008}} (pp. 182–183, Error)

## Properties

Random error is the chance contribution of the instrument and the user. Its statistical properties are studied with probability. Systematic error comes from consistent causes, improper calibration being the example, and it keeps its direction. The bias of a statistic is one form of systematic error. Accidental error is attributed to the experimenter rather than to the instrument, and experimental error is the contribution of uncontrolled variables. A reported error is generally a mixture of these types. Rounding adds a further error when a value is replaced by a truncated neighbour, and rounding errors accumulate in a long calculation.{{cite:dodge2008}} (p. 183, Mathematical aspects)

Repeatability is the short-term component of precision under highly controlled conditions: the same instrument, the same operator, the same setup. Reproducibility is the wider precision that includes long-term variation and the variation from one instrument to another and from one laboratory to another. A procedure can be repeatable and still fail to be reproducible. The two words answer different experiments.{{cite:nist_glossary2002}} (Glossary, "repeatability" and "reproducibility")

Error distributions were introduced to describe repeated measures of the same quantity under the same conditions, and to explain why an arithmetic mean approximates the reference when the error is the chance kind. They do not cancel a systematic error that is shared by every repetition. The mean of a biased procedure is a biased estimate of the reference, however many repetitions are averaged.{{cite:dodge2008}} (pp. 182–183, History and systematic error)

## Worked example

Operator A's times are 10, 12, 11, and 11. The sum is 44 and the mean is $44/4 = 11$. Operator B's times are 14, 16, 15, and 15. The sum is 60 and the mean is $60/4 = 15$. The true duration is 12 seconds. A's bias is $11 - 12 = -1$. B's bias is $15 - 12 = 3$. The absolute errors for A are 2, 0, 1, and 1, summing to 4, so the mean absolute error is $4/4 = 1$. A's repeatability is visible in the scatter around 11. A's accuracy is worse than that scatter alone, because the average sits 1 second off the reference.{{cite:nist_glossary2002}} (Glossary, "bias" and "accuracy"){{cite:dodge2008}} (p. 183, absolute error)

**Your turn.** Operator A records one more time, of 16 seconds. What are A's new mean and new bias?

::: {.callout-tip collapse="true" title="Answer"}
The times sum to 60 over 5 observations, so the mean is 12. The bias is $12 - 12 = 0$.
:::

## Assumptions and limits

The decomposition into random and systematic error assumes a reference value against which the direction of the systematic part can be judged. Without a reference, a shift that is common to every reading is invisible in the scatter, and precision can look excellent while the accuracy is unknown.{{cite:dodge2008}} (p. 182, Error){{cite:nist_glossary2002}} (Glossary, "accuracy")

Repeatability describes a tightly held setup. It does not describe a procedure that changes operator, instrument, or laboratory. That wider scatter is reproducibility. Quoting a repeatability standard deviation as if it were the uncertainty of a measurement made in another laboratory uses the wrong component.{{cite:nist_glossary2002}} (Glossary, "reproducibility")

A recorded length is discrete at the resolution of the instrument even when the quantity is treated as continuous. Replacing the reading by a shorter decimal is a rounding error, bounded by half a unit in the last place when the usual rounding rule is used, and those bounds add across a long calculation. The statistical error of the procedure and the rounding error of the arithmetic are different contributions to the number that is finally stored.{{cite:dodge2008}} (p. 183, rounded error)

## History

Error distributions were introduced in the second half of the eighteenth century to describe repeated measures of the same quantity under the same conditions. In a letter of 1756, Simpson suggested that the probability of obtaining a certain error during an observation can be described by a discrete distribution, and he proposed the first two error distributions. Lagrange studied further discrete distributions in 1776. Simpson also proposed continuous error distributions, as did Laplace. The normal distribution, proposed by Gauss in 1809, became the central error law for that tradition. The metrological split into absolute, relative, random, and systematic error is the later vocabulary in which those distributions are applied to a measuring procedure.{{cite:dodge2008}} (pp. 182–183, History)
