

## Lead context

A measurement or an estimator can miss in the same direction every time the procedure is repeated. That persistent miss is systematic error. Averaging repeats does not remove it.{{cite:dodge2008}} (p. 183, systematic error){{cite:nist_type_a2002}} (§2.5.3, biases can be corrected and are not removed by treating them as scatter)

## Motivating example

A balance reads $1.5$ mg high on every weighing, and the random flutter around that offset is only a few tenths of a milligram. Four weighings of a $20$ mg standard might be $21.4$, $21.7$, $21.2$ and $21.5$. Their average, $21.45$, is still about $1.45$ mg high. The gaps from the average are a few tenths and sum to zero. The gap from the standard does not. More weighings shrink the flutter and leave the offset.{{cite:dodge2008}} (p. 183, a consistent cause, always in the same direction)

## Definition

Systematic error is the error that comes from consistent causes and falls in the same direction whenever the measurement is repeated. Improper calibration of an instrument is the standard example. In statistics, the bias of an estimator is one case: if $\hat\theta$ estimates $\theta$, the bias is $\mathbb E(\hat\theta)-\theta$.{{cite:dodge2008}} (pp. 41 and 183)

For a reported measurement, a component is analysed as bias rather than as random error when the report is about one specific instrument, operator, or method, and the offset of that one member from a reference or from a group is what matters. The same physical differences can be random error if the report is instead about a member drawn at random from the group. The classification follows the scope of the reported value.{{cite:nist_type_a2002}} (§2.5.3)

Accuracy of a measurement covers both the random scatter, often called precision, and this systematic offset between the average of the measured values and the true value. A small scatter alone is not accuracy.{{cite:nist_glossary2002}} (Glossary, "accuracy")

Random error is a scatter. Systematic error is a shift. The shift has a cause that stays put: a calibration that is off, a zero that was set wrong, a procedure that always forgets the same correction. Because the cause is common to the whole series, the readings move together. Their average moves with them. A correction is possible in principle once the shift can be estimated from a reference, and the correction is uncertain to the extent that the estimate of the shift is uncertain. Subtracting a made-up constant is not that correction.{{cite:nist_type_a2002}} (§2.5.3, correction of bias, and the uncertainty of the correction){{cite:nist_glossary2002}} (Glossary, "accuracy", the systematic offset beside precision)

The same idea appears in estimation. The bias of an estimator is the difference between its expected value and the parameter. It is the systematic error of that estimator: repeat the sampling procedure and the long-run average of the estimates sits away from the target by that amount.{{cite:dodge2008}} (p. 41, bias as systematic error of an estimator; p. 183, bias as a particular systematic error)

Let each reading be $Y_i=\theta+b+\varepsilon_i$, with a constant $b$ and uncorrelated mean-zero errors of variance $\sigma^2$. Then $\mathbb E(\bar Y)=\theta+b$, so the bias of the average is $b$, however large $n$ is. $\mathrm{Var}(\bar Y)=\sigma^2/n$ still falls. On the balance, $b$ is about $1.45$ mg in the four weighings, and the deviations from $21.45$ are $-0.05$, $0.25$, $-0.25$ and $0.05$. Their sum of squares is $0.13$, a small random scale next to a shift of $1.45$.

A correction subtracts an estimate of $b$. If the estimate is the average minus a known standard, the corrected average equals the standard on these four weighings, and the uncertainty that remains is the uncertainty of that estimated shift. The corrected average matches the standard on these four weighings only after the estimated shift is subtracted. Guidelines that assume every bias has been corrected still keep the uncertainty of the correction in the reported uncertainty.{{cite:nist_type_a2002}} (§2.5.3){{cite:dodge2008}} (p. 41)

An estimator can be repeatedly precise and still systematically wrong. Dodge's illustration is the divide-by-$n$ variance
\[
S^2=\frac1n\sum_{i=1}^n(x_i-\bar x)^2,
\]
whose expectation is not the population variance. The bias is a property of the procedure, visible in the expectation, not a property of one unlucky sample.{{cite:dodge2008}} (p. 41, bias of $S^2$)

If a reference standard is available, estimate the offset by the average reading minus the standard, subtract it, and keep a standard error for that offset. If no reference is available, do not invent a correction from the scatter of the readings. The scatter estimates $\sigma$, not $b$. In a sampling problem, state the bias of the estimator beside its variance. An unbiased estimator and a robust estimator solve different problems: unbiasedness removes a systematic error of expectation, and robustness limits the pull of a few wild points.{{cite:dodge2008}} (pp. 41 and 183){{cite:nist_type_a2002}} (§2.5.3)

Systematic error is not a residual that happens to be positive. A residual changes sign across a fitted line by construction of least squares, whenever the line has an intercept. A systematic error keeps its sign across repetitions of the same measurement.{{cite:dodge2008}} (p. 183, systematic error contrasted with the residual)

Taking more observations does not drive a constant bias to zero. It drives the variance of the average to zero, so the average settles on the wrong value more firmly.{{cite:nist_type_a2002}} (§2.5.3){{cite:dodge2008}} (p. 41)

Bias of an estimator is not the same object as a miscalibrated instrument, even though both are systematic errors. The first is an expectation under a sampling model. The second is a property of a measurement procedure. The shared word is justified by the shared structure, a shift that repetition does not average away, and the remedies differ.{{cite:dodge2008}} (pp. 41 and 183)

The split into a constant $b$ and a mean-zero $\varepsilon$ is an assumption. A drift that grows through the series is not a constant systematic error, and a shift that appears only for large true values is not either. Estimating $b$ from the same readings that are being corrected, without a standard, is impossible: the deviations from the mean sum to zero and say nothing about $b$. Randomisation in an experiment is aimed at a different systematic error, the confounding of a treatment with a persistent nuisance. It does not calibrate a balance.{{cite:dodge2008}} (p. 447, randomisation against a systematic error from noncontrollable factors; p. 183){{cite:nist_type_a2002}} (§2.5.3)

## Worked example

The standard is $20$ mg. The readings are $21.4$, $21.7$, $21.2$, $21.5$.

The mean is $(21.4+21.7+21.2+21.5)/4=21.45$. The estimated systematic error is $21.45-20=1.45$ mg. Deviations from the mean are $-0.05$, $0.25$, $-0.25$, $0.05$, and the sum of their squares is $0.005+0.0625+0.0625+0.0025=0.13$. The sample variance is $0.13/3\approx 0.0433$, so the estimated standard deviation of the mean is $\sqrt{0.13/12}\approx 0.104$ mg.

Subtracting $1.45$ from the mean lands on $20$, the standard, because the offset was computed from that standard. The $0.104$ mg is the estimated random uncertainty of the mean, and it is also the uncertainty of this particular estimate of the offset. A later weighing, corrected by subtracting $1.45$, still carries that uncertainty. It does not carry a remaining bias of $1.45$.{{cite:nist_type_a2002}} (§2.5.3, uncertainty of the correction){{cite:dodge2008}} (p. 183)

**Your turn.** A $10$ cm gauge is read as $12$, $11$ and $13$. Find the mean, the estimated systematic error, and the mean after subtracting that error.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $12$. The estimated systematic error is $12-10=2$ cm. Subtracting it leaves $10$ cm.
:::

## Connections

[Random error](random-error.qmd) is the scatter around the shifted mean. The [bias of an estimator](bias-of-an-estimator.qmd) is the sampling version of a systematic error. [Measurement error](measurement-error.qmd) includes both the shift and the scatter, and a constant calibration shift is the case that averaging does not fix. An [unbiased estimator](unbiased-estimator.qmd) is one whose systematic error of expectation is zero.{{cite:dodge2008}} (pp. 41 and 183){{cite:nist_glossary2002}} (Glossary, "accuracy")

## History

The probability distributions used to describe measurement error were developed from the middle of the eighteenth century, so that the value of taking a mean could be argued. Simpson's discrete laws and Gauss's normal law of 1809 belong to that development. The bias of an estimator, as a systematic error of expectation, was formulated by Gauss in 1821 in the course of comparing unbiased estimation with the method of least squares. Calibration error, as a metrological shift, is the laboratory form of the same idea: a cause that repeats, as distinct from a chance error that scatters.{{cite:dodge2008}} (pp. 41 and 182–183)
