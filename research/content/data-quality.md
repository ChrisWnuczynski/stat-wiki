

## Lead context

A file can be large and still be unfit for the conclusion someone wants to draw from it. Data quality is the match between the recorded values and that use: how far they sit from the quantities they name, and how far the recorded units sit from the population they are supposed to represent. {{cite:nist_glossary2002}} (Glossary, "accuracy") {{cite:nist_glossary2002}} (Glossary, "coverage error")

## Motivating example

Four readings of a 20-millimetre gauge block come back as 22, 23, 21, and 22 millimetres. Their mean is \(88/4 = 22\). The instrument is precise enough to agree with itself within a couple of millimetres, and it is high by 2 millimetres. A later analysis that treats 22 as if it were 20 has imported that offset. Separately, a survey frame that lists 800 of 1000 graduates cannot be repaired by weighing the 800 more carefully. The missing 200 are a coverage failure, not a measurement failure. {{cite:nist_glossary2002}} (Glossary, "bias") {{cite:nist_glossary2002}} (Glossary, "coverage error")

## Definition

Data quality is the extent to which the observations are accurate for the quantities they record and representative for the population they are used to describe.

Accuracy, in metrology, is the total measurement variation: precision, the scatter around the average of the measurements, together with the systematic offset between that average and the true value. {{cite:nist_glossary2002}} (Glossary, "accuracy") {{cite:nist_glossary2002}} (Glossary, "precision") Bias is the difference between the average or expected value and the true value. Precision is not affected by bias. Accuracy gets worse as bias grows. {{cite:nist_glossary2002}} (Glossary, "bias")

For a survey, the representational side splits into coverage error, sampling error, measurement error, and non-response error. {{cite:nist_glossary2002}} (Glossary, "survey errors")

Two questions are easy to collapse into "is the data good?". One asks whether a recorded number is near the true quantity. The other asks whether the records cover the people or items the sentence is about. Accuracy is the first question, and it includes both the scatter of repeated measurements and the systematic offset from the true value. Coverage, sampling, and non-response are the second question, for a survey. {{cite:nist_glossary2002}} (Glossary, "accuracy") {{cite:nist_glossary2002}} (Glossary, "survey errors")

The true value has to be meaningful for the bias to be meaningful. A quantity with no reference, or a category that was only coded, does not have a metrological bias of this kind. {{cite:nist_glossary2002}} (Glossary, "bias") {{cite:dodge2008}} (p. 182) Survey error classes can overlap in practice: a badly worded question is a measurement problem even when the sample was drawn well. {{cite:nist_glossary2002}} (Glossary, "questionnaire error") The judgement is relative to a use. A file that is good enough to describe respondents may be unfit for a sentence about non-respondents. {{cite:nist_glossary2002}} (Glossary, "nonresponse error")

## Properties

An absolute error is the absolute difference between an observed value and the reference value. A relative error divides that absolute error by the size of the quantity, and it is one way to describe the accuracy of a physical measurement. A systematic error comes from a consistent cause, such as a miscalibrated instrument, and it points the same way on repetition. Bias is a statistical form of that systematic error. A random error is the chance contribution of instrument and user. {{cite:dodge2008}} (p. 183) {{cite:dodge2008}} (p. 182)

A large sample from a frame that omits a class of units reproduces the omission. Coverage error is a property of the frame, not of the sample size. {{cite:nist_glossary2002}} (Glossary, "coverage error") {{cite:nist_glossary2002}} (Glossary, "sample frame")

## Statistical use

A mean of repeated measurements is used because, under a random error, it approximates the reference value. It does not remove a systematic offset: averaging four readings that are each high by about 2 millimetres produces a mean that is still high. {{cite:dodge2008}} (p. 182) {{cite:nist_glossary2002}} (Glossary, "bias") Before a survey estimate is treated as a population quantity, the frame, the selection, the answers, and the refusals each have to be considered. A sampling-error formula does not budget the other three. {{cite:nist_glossary2002}} (Glossary, "survey errors") {{cite:dodge2008}} (p. 533)

## Worked example

The true length is 20 millimetres. The readings are 22, 23, 21, and 22. Their sum is 88 and their mean is 22. The bias of the mean, mean minus true value, is \(22 - 20 = 2\). The absolute errors are 2, 3, 1, and 2, and they sum to 8. The mean absolute error is \(8/4 = 2\), the same 2 millimetres, because every reading was on the same side of 20. {{cite:nist_glossary2002}} (Glossary, "bias") {{cite:dodge2008}} (p. 183)

**Your turn.** A fifth reading is 24 millimetres. What are the new mean and the new bias of the mean?

::: {.callout-tip collapse="true" title="Answer"}
The readings sum to 112 over 5 observations, so the mean is \(112/5 = 22.4\). The bias is \(22.4 - 20 = 2.4\).
:::

## Common misconceptions

A data set is not high quality because it has many rows. A long series from a miscalibrated instrument is a long biased series. {{cite:nist_glossary2002}} (Glossary, "accuracy") {{cite:dodge2008}} (p. 183)

Precision is not accuracy. Readings that agree with each other can all be wrong by the same offset, and then precision is fine and accuracy is not. {{cite:nist_glossary2002}} (Glossary, "precision") {{cite:nist_glossary2002}} (Glossary, "bias")

## History

Describing the error of a repeated measurement by a probability distribution, and using the arithmetic mean as an approximation to the reference value, was already a programme in the second half of the eighteenth century. Simpson proposed discrete error distributions in 1756, and Gauss proposed the normal error distribution in 1809. {{cite:dodge2008}} (p. 182) {{cite:dodge2008}} (p. 183) The survey classification into coverage, sampling, measurement, and non-response is the later, administrative half of the same concern. {{cite:nist_glossary2002}} (Glossary, "survey errors")

## Connections

The [true value](true-value.qmd) is the reference the offset is measured from. [Measurement](measurement.qmd) is the process that produces the readings. [Measurement error](measurement-error.qmd) is the difference between a measured value and the quantity. [Uncertainty](uncertainty.qmd) is the quantitative caution attached to what the readings support. [Survey methodology](survey-methodology.qmd) is where coverage and non-response are designed for. The [bias of an estimator](bias-of-an-estimator.qmd) is the parallel idea for a statistic and a parameter.
