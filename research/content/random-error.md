

## Lead context

Repeat a measurement of the same quantity under the same conditions and the readings still differ. The part of each reading that scatters, rather than landing in the same direction every time, is random error.{{cite:dodge2008}} (p. 183, random error){{cite:nist_type_a2002}} (§2.5.3, random error is not removed by a correction)

## Motivating example

Four technicians measure a rod whose reference length is $10.00$ cm and record $9.7$, $10.2$, $9.9$ and $10.4$. The average is $10.05$. The gaps from that average are $-0.35$, $0.15$, $-0.15$ and $0.35$, and they sum to zero. No single reading is the length, and no single gap has a cause one would correct and then forget. Averaging is the relevant operation: the error of the average, $0.05$ cm against the reference, is smaller than the typical single gap.{{cite:dodge2008}} (p. 183, chance error studied with probabilities)

## Intuition

Random error is what is left when the persistent causes have been named and removed, or when they were never there. It is tied to the instrument and to the person using it, and its size is described by a distribution rather than by a single signed correction. The classical models for that distribution, from discrete laws in the eighteenth century through the normal law, were built so that an average of several readings would sit closer to the reference value than a single reading does. Squared or absolute deviations from the average estimate the scale of the scatter. They do not estimate a shift that is common to every reading.{{cite:dodge2008}} (pp. 182–183, error distributions and the average as an approximation to the reference)

## Definition

In metrology, the random error of a measurement is the chance error that comes from the instrument, the user, or both acting together. Its statistical properties are handled with probability, not with a fixed correction. It is distinct from the systematic error, which arises from a consistent cause and falls in the same direction on repetition, and from the residual in a regression, which is the gap between an observation and a fitted value rather than the gap between an observation and a reference value.{{cite:dodge2008}} (p. 183)

A component of uncertainty is treated as random error when the reported result is meant to stand for a randomly chosen member of a class, such as any instrument from a batch of similar instruments. The differences among those instruments then scatter. If instead the report is about one named instrument, that instrument's offset from the batch is a bias, and the analysis changes. Random errors are not removed by applying a correction. Biases, in principle, are.{{cite:nist_type_a2002}} (§2.5.3)

The scale is estimated from replicates, from a check standard, or from a designed comparison that covers the conditions under which the measurement will be repeated. The standard deviation of those replicates is the usual summary of the random component.{{cite:nist_type_a2002}} (§2.5.3, type A evaluation of random errors)

Quote the average as the measured value and the standard deviation of the mean, or a limit built from it, as the contribution of random error. Do not subtract an estimated random gap from a single reading and then treat the result as exact. If a reference value is available, the average minus the reference still contains the systematic error. On the rod that difference is $0.05$ cm, and it is an estimate of the shift only after the random part has been reduced by averaging. A single reading of $10.4$ cannot be split into those two parts.{{cite:nist_type_a2002}} (§2.5.3){{cite:dodge2008}} (p. 183)

Random error is not the residual from a regression. A residual is $y_i-\hat y_i$, the gap to a fitted mean that may itself be estimated from many different $x$ values. Random error, in the metrological sense, is scatter in repeated measurements of one quantity. The two can be modelled by similar probability laws, and they are still different gaps.{{cite:dodge2008}} (p. 183, residual error contrasted with random error)

Averaging does not cancel a systematic error. If every reading is long by a millimetre, the average is long by a millimetre. The $1/\sqrt{n}$ reduction applies to the random component.{{cite:nist_type_a2002}} (§2.5.3, random errors cannot be corrected; biases can)

A small random error is not the same thing as an accurate measurement. Accuracy also requires a small systematic offset. A precise instrument can be precisely wrong.{{cite:nist_glossary2002}} (Glossary, "accuracy", precision and the systematic offset)

Descriptions of the error in a repeated measurement, as a probability distribution, go back to the eighteenth century. Simpson, in a letter of 1756 to the Royal Society, treated the probability of an error of a given size as a discrete distribution, so that the advantage of taking a mean could be calculated. Laplace and others continued the discrete and continuous cases. Gauss, in 1809, put forward the normal distribution as the leading law for measurement error. The later split into random and systematic parts is a metrological classification of those errors, not a single formula from that early work.{{cite:dodge2008}} (pp. 182–183)

## Properties

On the rod, the four deviations from the sample mean sum in squares to $0.29$. Dividing by $3$, one less than the number of readings, gives $0.29/3\approx 0.0967$, and the square root is about $0.311$ cm. The square root of that quantity divided by $4$ is about $0.155$ cm, a scale for the mean rather than for a single reading. The error of the mean against the reference is $0.05$ cm, smaller than the largest single deviation, $0.35$ cm. That is the content of averaging for this series: the scatter of the mean is estimated from the scatter of the readings, and it is smaller. A further series reduces that scatter only when the new readings are fresh repeats rather than copies of the same mistake.{{cite:dodge2008}} (p. 183, estimation of random errors by probabilities)

The decomposition "error equals random error plus systematic error" is a modelling statement. In a report of uncertainty the two are easy to mix up, because a component that scatters across a batch of instruments becomes a fixed offset once the report is about one instrument. The label follows the question, not the hardware.{{cite:nist_type_a2002}} (§2.5.3, the same differences can be a random effect or a bias)

## Worked example

Reference length $10.00$ cm. Readings $9.7$, $10.2$, $9.9$, $10.4$.

The mean is $(9.7+10.2+9.9+10.4)/4=10.05$. Deviations from the mean are $-0.35$, $0.15$, $-0.15$, $0.35$. Their squares are $0.1225$, $0.0225$, $0.0225$, $0.1225$, and the sum of squares is $0.29$. With three degrees of freedom the sample variance is $0.29/3=0.096\overline{6}$, and the sample standard deviation is $\sqrt{0.29/3}\approx 0.3109$ cm. The estimated standard deviation of the mean is $\sqrt{0.29/12}\approx 0.1555$ cm.

The errors against the reference are $-0.3$, $0.2$, $-0.1$, $0.4$. They do not sum to zero. Their average, $0.05$, is the error of the mean. The deviations from the mean are the part that averaging has already centred. They are the visible random scatter in this series.{{cite:dodge2008}} (p. 183)

**Your turn.** Three readings of a $10$ cm rod are $8$, $10$ and $12$. Find the mean, the sum of squared deviations from the mean, and the error of the mean against the reference.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $10$. Squared deviations from the mean are $4$, $0$ and $4$, so the sum of squares is $8$. The error of the mean against $10$ is $0$.
:::

## Assumptions and limits

The variance formula $\sigma^2/n$ uses uncorrelated readings and a common variance. Readings taken in a hurry by the same person, or taken while the instrument drifts, are correlated, and the variance of the mean is then larger than $\sigma^2/n$. A designed comparison is needed when the random component includes day-to-day changes rather than only the scatter of repeats within a minute. And no number of repeats estimates a bias that is shared by all of them. That bias is a systematic error, estimated by comparison with a reference, not by the standard deviation of the series.{{cite:nist_type_a2002}} (§2.5.3){{cite:dodge2008}} (p. 183)

## Connections

[Systematic error](systematic-error.qmd) is the persistent companion of random error. [Measurement error](measurement-error.qmd) is the broader gap between a recorded value and the quantity, and it contains both. [Errors and residuals](error-and-residual.qmd) separate a deviation from a true mean from a deviation from a fitted value. The [standard error](standard-error.qmd) of a mean is the scale of the random component after averaging.{{cite:dodge2008}} (p. 183){{cite:nist_glossary2002}} (Glossary, "measurement error")
