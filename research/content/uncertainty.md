

## Lead context

A conclusion from data is not a single number with nothing left to say. Uncertainty is the quantitative account of what is still unknown: the part that comes from the observations, and the part that comes from using a model that is not exactly right. {{cite:nist_glossary2002}} (Glossary, "uncertainty")

## Motivating example

Four timings of one reaction are 5, 7, 6, and 6 seconds. Their mean is 6. The readings are not identical, so a second set of four would not have to average to 6. That scatter is one uncertainty. A second uncertainty sits in the description: if the reaction's duration also depends on a temperature nobody recorded, the mean of 6 is the mean of a model that omitted temperature. {{cite:nist_glossary2002}} (Glossary, "uncertainty") {{cite:dodge2008}} (p. 183)

## Intuition

Imagine reporting not only the mean but a honest width around it. The width grows when the observations disagree, and it grows again when the equation used to interpret them leaves something out. Precision, in the loose sense, is the shrinking of that width as more data arrive. It is not the same as having the right target. {{cite:nist_glossary2002}} (Glossary, "precision") {{cite:nist_glossary2002}} (Glossary, "uncertainty")

## Definition

Uncertainty is the quantitative qualification of what is known or concluded, expressed with probabilities. It has two aspects: the experimental or observational error that comes with taking the observations, and the further doubt that comes from using imperfect models. {{cite:nist_glossary2002}} (Glossary, "uncertainty")

The observational piece is the error of measurement, the difference between the reported value and the reference value, including random error and systematic error. {{cite:dodge2008}} (p. 182) {{cite:dodge2008}} (p. 183) The model piece is the fact that a statistical model predicts a measured quantity only under the relation it states. {{cite:nist_glossary2002}} (Glossary, "model")

Random error scatters and is the part whose contribution shrinks, in expectation, as repeated observations are averaged. Systematic error keeps its direction and is not removed by that averaging. Both contribute to how far a report can be from the reference. {{cite:dodge2008}} (p. 183) {{cite:dodge2008}} (p. 182)

In a sample, the sample proportion is a consistent estimator of a population probability when the difference between them is expected to shrink as the sample grows. The finite-sample gap is sampling variability, a source of uncertainty even when every sampled outcome was observed without measurement error. {{cite:hernan_robins2020}} (p. 8)

A weak association used as the denominator of a ratio is a practical warning. An instrumental-variable estimate of 2.4 kilograms, from a numerator 0.1503 and a denominator 0.0627, came with an interval from \(-36.5\) to \(41.3\). The point estimate was not the uncertainty. The interval was. {{cite:hernan_robins2020}} (p. 213)

A probabilistic uncertainty statement assumes a probability model for the observational error, or for the sampling. Without a known selection probability, the usual sampling-error formula does not apply. {{cite:dodge2008}} (p. 152) {{cite:hernan_robins2020}} (p. 8) Model uncertainty is only partly visible. A residual plot can show that a line was wrong. It cannot list the variables nobody thought to record. {{cite:openintro2019}} {{cite:nist_glossary2002}} (Glossary, "uncertainty")

Quantifying the error of an observation by a probability distribution is an eighteenth-century project, from Simpson's discrete distributions in 1756 through Gauss's normal law in 1809. The mean was the device offered for approaching the reference value. {{cite:dodge2008}} (p. 182) {{cite:dodge2008}} (p. 183) Treating an imperfect model as a second, separate contribution to uncertainty is the later caution that a fitted equation is not the phenomenon. {{cite:nist_glossary2002}} (Glossary, "uncertainty") {{cite:nist_glossary2002}} (Glossary, "model")

## Statistical use

An analysis reports an estimate and a statement of how wide the set of plausible values still is. More data shorten that statement when the extra data are of the same kind, which is the loose sense of precision. {{cite:nist_glossary2002}} (Glossary, "precision") The statement is incomplete if it counts only the observational scatter and ignores an omitted factor or a curve fitted by a straight line. Residual pattern is one sign of that second contribution. {{cite:openintro2019}} {{cite:nist_glossary2002}} (Glossary, "uncertainty")

Bias and precision are different. The distance from the true value and the scatter around the estimator's own mean answer different questions, and an uncertainty that quotes only the scatter has left out the bias. {{cite:dodge2008}} (p. 41) {{cite:nist_glossary2002}} (Glossary, "bias")

## Worked example

The timings 5, 7, 6, and 6 sum to 24. The mean is \(24/4 = 6\). The absolute deviations from 6 are 1, 1, 0, and 0, summing to 2. The mean absolute deviation is \(2/4 = 0.5\) seconds. That 0.5 describes the scatter of these four readings about their mean. It does not describe a systematic offset, and it does not describe an omitted variable. {{cite:nist_glossary2002}} (Glossary, "uncertainty") {{cite:dodge2008}} (p. 183)

**Your turn.** A fifth timing of 8 seconds is included. What are the new mean and the new mean absolute deviation?

::: {.callout-tip collapse="true" title="Answer"}
The sum is 32 and the mean is \(32/5 = 6.4\). The absolute deviations from 6.4 are 1.4, 0.6, 0.4, 0.4, and 1.6, which sum to 4.4. The mean absolute deviation is \(4.4/5 = 0.88\).
:::

## Common misconceptions

A small standard error is not a demonstration that the target is the right one. It is a statement about scatter under the sampling scheme and the model that were used. A biased procedure can be very precise about the wrong number. {{cite:dodge2008}} (p. 41) {{cite:nist_glossary2002}} (Glossary, "precision")

The point estimate is not a substitute for the uncertainty. The instrumental-variable figure of 2.4 kilograms and the interval from \(-36.5\) to \(41.3\) are different objects. {{cite:hernan_robins2020}} (p. 213)

## Connections

The [true value](true-value.qmd) is what the observational error is measured against. [Measurement](measurement.qmd) produces that error. A [statistical model](statistical-model.qmd) is the second source of uncertainty when it is wrong or incomplete. [Sampling](sampling.qmd) contributes the gap between a sample summary and the population quantity. The [bias of an estimator](bias-of-an-estimator.qmd) is the systematic part that a scatter-only uncertainty misses.
