## Lead context

A conclusion from data is not a single number with nothing left to say. Uncertainty is the quantitative account of what is still unknown: the part that comes from the observations, and the part that comes from using a model that is not exactly right.{{cite:nist_glossary2002}} (Glossary, "uncertainty")

## Motivating example

Four timings of one reaction are 5, 7, 6, and 6 seconds. Their mean is 6. The readings are not identical, so a second set of four would not have to average to 6. That scatter is one uncertainty. A second uncertainty sits in the description: if the reaction's duration also depends on a temperature nobody recorded, the mean of 6 is the mean of a model that omitted temperature.{{cite:nist_glossary2002}} (Glossary, "uncertainty"){{cite:dodge2008}} (p. 183)

## Intuition

Imagine reporting not only the mean but an honest width around it. The width grows when the observations disagree, and it grows again when the equation used to interpret them leaves something out. Precision, in the loose sense, is the shrinking of that width as more data of the same kind arrive. It is not the same as having the right target. A biased procedure can be very precise about the wrong number.{{cite:nist_glossary2002}} (Glossary, "precision"){{cite:nist_glossary2002}} (Glossary, "uncertainty")

## Definition

Uncertainty is the quantitative qualification of what is known or concluded, expressed with probabilities. It has two aspects: the experimental or observational error that comes with taking the observations, and the further doubt that comes from using imperfect models.{{cite:nist_glossary2002}} (Glossary, "uncertainty")

The observational piece is the error of measurement, the difference between the reported value and the reference value, including random error and systematic error.{{cite:dodge2008}} (pp. 182–183) The model piece is the fact that a statistical model predicts a measured quantity only under the relation it states. A model, in the glossary, is a mathematical statement of relations among variables, and a statistical model is the part that predicts a measured quantity.{{cite:nist_glossary2002}} (Glossary, "model")

## Statistical use

An analysis reports an estimate and a statement of how wide the set of plausible values still is. More data shorten that statement when the extra data are of the same kind, which is the loose sense of precision.{{cite:nist_glossary2002}} (Glossary, "precision") The statement is incomplete if it counts only the observational scatter and ignores an omitted factor or a curve fitted by a straight line. One purpose of a residual plot is to show pattern that remains after the line is fitted. Curvature in the residuals is a sign that a straight line was the wrong shape, and that leftover pattern is a contribution to uncertainty that the residual standard deviation, read as pure noise, would miss.{{cite:openintro2019}} (Ch. 8, §8.1){{cite:nist_glossary2002}} (Glossary, "uncertainty")

Random error scatters and is the part whose contribution shrinks, in expectation, as repeated observations are averaged. Systematic error keeps its direction and is not removed by that averaging. Both contribute to how far a report can be from the reference.{{cite:dodge2008}} (pp. 182–183)

Bias and precision are different. The distance from the true value and the scatter around the estimator's own mean answer different questions, and an uncertainty that quotes only the scatter has left out the bias.{{cite:dodge2008}} (p. 41){{cite:nist_glossary2002}} (Glossary, "bias")

In a sample, the sample proportion is a consistent estimator of a population probability when the difference between them is expected to shrink as the sample grows. The finite-sample gap is sampling variability, a source of uncertainty even when every sampled outcome was observed without measurement error. Without a known selection probability, the usual sampling-error formula does not apply.{{cite:hernan_robins2020}} (Ch. 1, p. 8){{cite:dodge2008}} (p. 152)

A weak association used as the denominator of a ratio is a practical warning of a different kind. In a smoking-cessation example the numerator difference of the instrumental-variable estimate is reported as $0.1503$, and the denominator is $0.2578-0.1951=0.0627$. The ratio $0.1503/0.0627$ is $2.4$ kilograms to one decimal place. The 95 percent interval ran from $-36.5$ to $41.3$. The point estimate was not the uncertainty. The interval was. The width is what a weak first stage does to the ratio.{{cite:hernan_robins2020}} (Ch. 16, §16.2, p. 213)

## Worked example

The timings 5, 7, 6, and 6 sum to 24. The mean is $24/4 = 6$. The absolute deviations from 6 are 1, 1, 0, and 0, summing to 2. The mean absolute deviation is $2/4 = 0.5$ seconds. That 0.5 describes the scatter of these four readings about their mean. It does not describe a systematic offset, and it does not describe an omitted variable.{{cite:nist_glossary2002}} (Glossary, "uncertainty"){{cite:dodge2008}} (p. 183)

**Your turn.** A fifth timing of 8 seconds is included. What are the new mean and the new mean absolute deviation?

::: {.callout-tip collapse="true" title="Answer"}
The sum is 32 and the mean is $32/5 = 6.4$. The absolute deviations from 6.4 are 1.4, 0.6, 0.4, 0.4, and 1.6, which sum to 4.4. The mean absolute deviation is $4.4/5 = 0.88$.
:::

## Common misconceptions

A small standard error is not a demonstration that the target is the right one. It is a statement about scatter under the sampling scheme and the model that were used. A biased procedure can be very precise about the wrong number. Precision, in the metrological sense, is variability around the procedure's own average. Accuracy includes the offset from the true value.{{cite:dodge2008}} (p. 41){{cite:nist_glossary2002}} (Glossary, "precision")

The point estimate is not a substitute for the uncertainty. The instrumental-variable figure of 2.4 kilograms and the interval from $-36.5$ to $41.3$ are different objects. Quoting 2.4 and omitting the interval reports the ratio and hides the weakness of the denominator.{{cite:hernan_robins2020}} (Ch. 16, §16.2, p. 213)

A residual plot can show that a line was the wrong shape. It cannot list the variables nobody thought to record. Model uncertainty is only partly visible. The glossary's second aspect of uncertainty, the doubt that comes from an imperfect model, is not exhausted by the residuals of the model that was fitted.{{cite:openintro2019}} (Ch. 8, §8.1){{cite:nist_glossary2002}} (Glossary, "uncertainty")

## Connections

The [true value](true-value.qmd) is what the observational error is measured against. [Measurement](measurement.qmd) produces that error. A [statistical model](statistical-model.qmd) is the second source of uncertainty when it is wrong or incomplete. [Sampling](sampling.qmd) contributes the gap between a sample summary and the population quantity. The [bias of an estimator](bias-of-an-estimator.qmd) is the systematic part that a scatter-only uncertainty misses.{{cite:dodge2008}} (pp. 41 and 182){{cite:nist_glossary2002}} (Glossary, "uncertainty")
