

## Lead context

A measurement is an attempt at a quantity. The true value is that quantity: the reference the measurement is compared with when one says the measurement was high, low, or close. {{cite:dodge2008}} (p. 182) {{cite:nist_glossary2002}} (Glossary, "accuracy")

## Motivating example

A gauge block is manufactured to be 20 millimetres. Four readings from a caliper are 22, 23, 21, and 22. Their mean is 22. The 20 millimetres is the reference the caliper was supposed to recover. The 2-millimetre gap is not a property of the block. It is the gap between the readings and the true value. {{cite:nist_glossary2002}} (Glossary, "bias") {{cite:dodge2008}} (p. 182)

## Definition

The true value, also called the reference value, is the quantity of which an observation or an estimate is an imperfect report. The error is the difference between the estimated value and that reference. {{cite:dodge2008}} (p. 182)

Accuracy includes the systematic offset between the average of the measured values and the true value, as well as the precision of the measurements around their own average. {{cite:nist_glossary2002}} (Glossary, "accuracy") Bias is the difference between the average or expected value of a distribution and the true value. {{cite:nist_glossary2002}} (Glossary, "bias")

For an estimator \(T\) of a parameter \(\theta\), the parallel statement is \(\mathrm{E}[T] = \theta + b(\theta)\). The true value of the parameter is \(\theta\), and \(b(\theta)\) is the bias. If \(b(\theta) = 0\), then \(T\) is unbiased for \(\theta\). {{cite:dodge2008}} (p. 41)

Repeat a measurement and the results scatter. The centre of that scatter is the procedure's own average. The true value is a different point: the quantity itself. If the centre of the scatter is not the true value, the procedure is biased, however tight the scatter is. {{cite:nist_glossary2002}} (Glossary, "precision") {{cite:nist_glossary2002}} (Glossary, "accuracy")

The arithmetic mean of repeated measurements was introduced as an approximation to the reference value when the errors are of the random kind that an error distribution describes. {{cite:dodge2008}} (p. 182) An unbiased estimator is one whose expected value equals the true value of the parameter, so that the average of many such estimates lands on \(\theta\). {{cite:dodge2008}} (p. 41) In a sample, the sample proportion estimates a population probability and need not equal it. The population probability is the true value of that proportion. The sample proportion is the report. {{cite:hernan_robins2020}} (p. 8)

The average of the measurements is not the true value. It is an estimate of it, and it equals the true value only if the errors that remain happen to cancel, or if one is speaking of the expected value of an unbiased procedure. {{cite:dodge2008}} (p. 182) {{cite:dodge2008}} (p. 41)

A very small scatter does not mean the true value has been hit. Scatter is precision. The offset from the reference is a separate part of accuracy. {{cite:nist_glossary2002}} (Glossary, "precision") {{cite:nist_glossary2002}} (Glossary, "accuracy")

[Measurement](measurement.qmd) is the procedure aimed at the true value. [Measurement error](measurement-error.qmd) is the difference it leaves. The [bias of an estimator](bias-of-an-estimator.qmd) is \(b(\theta)\) in the parameter case. [Data quality](data-quality.qmd) gets worse as the offset from the true value grows. [Uncertainty](uncertainty.qmd) is what remains once the true value is admitted to be unknown.

## Properties

Absolute error is the absolute difference between the observed value and the reference. Relative error is that absolute error divided by the size of the quantity. {{cite:dodge2008}} (p. 183)

A systematic error keeps a direction, as when a miscalibrated instrument is always high. It is an error relative to the true value, not relative to the average of the faulty readings. Bias in the statistical sense is one example. {{cite:dodge2008}} (p. 183) A random error scatters about the procedure's average and is the part that averaging is meant to shrink. {{cite:dodge2008}} (p. 183) {{cite:dodge2008}} (p. 182)

Precision is variability around the measurement process's average. It is distinguished from accuracy, which is variability around the true value. A precise procedure can still miss the true value by a constant. {{cite:nist_glossary2002}} (Glossary, "precision")

## Worked example

The true mass is 50 grams. Three estimates are 48, 53, and 51. Their sum is 152 and their mean is \(152/3\). The error of the mean is \(152/3 - 50 = 2/3\) grams. The absolute errors of the three estimates are 2, 3, and 1, summing to 6. {{cite:dodge2008}} (p. 182) {{cite:dodge2008}} (p. 183)

**Your turn.** A fourth estimate is 48 grams. What are the new mean and the new error of the mean?

::: {.callout-tip collapse="true" title="Answer"}
The sum is \(152 + 48 = 200\), so the mean is \(200/4 = 50\). The error of the mean is \(50 - 50 = 0\).
:::

## Assumptions and limits

Calling a number the true value assumes a quantity that the procedure is trying to recover. A code for a category does not have a true value in the metrological sense. {{cite:dodge2008}} (p. 182) {{cite:dodge2008}} (p. 439) For a parameter, the true value is a feature of the model. If the model is wrong, an unbiased estimator of its parameter is unbiased for the wrong target. {{cite:nist_glossary2002}} (Glossary, "uncertainty") {{cite:dodge2008}} (p. 41)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 15. Their total is 120, so their mean is 8.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 6.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. True value has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 8.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [Measurement](measurement.qmd), [Measurement error](measurement-error.qmd), [bias of an estimator](bias-of-an-estimator.qmd), [Data quality](data-quality.qmd).

Two further limits are algebraic. The sum of deviations from the mean 8.0 is zero, so the mean is the least-squares centre of these 15 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 8.0.

## History

The reference value, and the idea that an arithmetic mean approximates it, belong to the eighteenth-century theory of errors. Simpson wrote in 1756 on the probability of an error of observation. Gauss gave the normal distribution as an error distribution in 1809. {{cite:dodge2008}} (p. 182) {{cite:dodge2008}} (p. 183) The definition of the bias of an estimator as a gap between an expected value and the true parameter is the form Gauss's unbiasedness took in least squares. {{cite:dodge2008}} (p. 41)
