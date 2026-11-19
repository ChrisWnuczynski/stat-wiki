## Lead context
A random error is a chance deviation that scatters from one repeated measurement of the same quantity to the next. The error of a single reading is the difference between the estimated value and the reference value. The random part of that error is the part whose statistical properties are studied with probabilities, as distinct from a systematic shift that always runs in the same direction.{{cite:dodge2008}} (pp. 182–183)

## Motivating example
A rod whose reference length is $10$ cm is read four times: $9.7$, $10.2$, $9.9$, and $10.4$. The four numbers are not the same, and none of them has to equal $10$. The scatter among them is the random error of this series. Their average can sit close to $10$ while each reading sits away from it. A correction that shifts every reading by the same amount would move the average. It would not make the four readings equal.{{cite:dodge2008}} (p. 183){{cite:nist_type_a2002}} (§2.5.3)

## Intuition
Imagine the same measurement repeated under the same conditions. If the only disturbances are small and change direction from trial to trial, the readings form a cloud around the reference. The width of the cloud is the scale of the random error. A disturbance that pushes every reading high, such as a mis-calibrated zero, moves the whole cloud. That shift is systematic. The cloud's width is still the random error. Probability is the language for the cloud, because the next reading is not fixed by the previous one.{{cite:dodge2008}} (pp. 182–183){{cite:nist_type_a2002}} (§2.5.3)

## Definition
Dodge distinguishes the absolute error, the absolute difference between the observed value and the reference value, from the relative error, that absolute difference divided by the value of the quantity. The random error is the chance error resulting from a combination of errors due to the instrument and the user. Its statistical properties and its estimation are studied using probabilities. The systematic error comes from consistent causes, for example an improper calibration, and always happens in the same direction. Bias in statistics is a particular example of that systematic error. The residual error is a third object: the difference between an estimated value and the observed value, as when a fitted mean is subtracted from a point.{{cite:dodge2008}} (p. 183)

A Type A evaluation of uncertainty is a statistical analysis of data. It can be applied to random error or to bias. The distinction that the evaluation has to keep is that random errors cannot be corrected, while biases can, at least in principle, be corrected or eliminated from the result. The ISO guidelines used in that handbook section assume that biases have been corrected, so that the uncertainty left from a bias is the uncertainty of the correction.{{cite:nist_type_a2002}} (§2.5.3)

## Properties
For the four rod readings the mean is

$$
\frac{9.7+10.2+9.9+10.4}{4}=\frac{40.2}{4}=10.05.
$$


The deviations from the mean are $-0.35$, $0.15$, $-0.15$, and $0.35$. The sum of their squares is

$$
0.35^2+0.15^2+0.15^2+0.35^2=0.1225+0.0225+0.0225+0.1225=0.29.
$$


The error of the mean against the reference $10$ is $10.05-10=0.05$ cm. The sum of squared deviations, $0.29$, describes the scatter of the readings about their own mean. The $0.05$ describes where that mean sits relative to the reference. Those are different summaries. A large scatter can coexist with a small error of the mean, and a small scatter can coexist with a mean that is far from the reference if the shift is shared by every reading.{{cite:dodge2008}} (p. 183){{cite:nist_type_a2002}} (§2.5.3)

The same differences among instruments can be a random effect or a bias, according to the uncertainty statement. If several instruments are treated as a draw from a batch, and the statement is meant to cover an instrument selected at random from that batch, the differences are a random effect. If the statement is meant to cover one named instrument, the difference of that instrument from the batch is the bias of interest.{{cite:nist_type_a2002}} (§2.5.3)

## Worked example
The rod series has mean $10.05$, sum of squared deviations $0.29$, and error of the mean $0.05$ cm against the reference $10$. The largest absolute deviation from the mean is $0.35$ cm, on both the low reading $9.7$ and the high reading $10.4$. The random error of this short series is visible in that $0.35$ cm and in the sum $0.29$. It is not visible in the $0.05$ cm, which is the shift of the average.{{cite:dodge2008}} (p. 183)

**Your turn.** Three readings of a $10$ cm rod are $8$, $10$, and $12$. Find the mean, the sum of squared deviations from the mean, and the error of the mean against the reference.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $10$. The deviations are $-2$, $0$, and $2$, and the sum of squared deviations is $8$. The error of the mean against $10$ is $0$.
:::

## Assumptions and limits
Further readings shrink the error of the mean when the disturbances really do change direction from trial to trial and share a common centre. They do not shrink a systematic shift. If every reading is $0.2$ cm high because the zero is wrong, the mean of more readings is still about $0.2$ cm high. The sum of squared deviations can be small in that case. Small scatter is not evidence that the mean equals the reference.{{cite:nist_type_a2002}} (§2.5.3){{cite:dodge2008}} (p. 183)

A residual from a fitted curve is not the random error of a repeated measurement of a fixed reference. The residual uses an estimate in place of the reference, and the estimate was computed from the same observations. Quoting the residual sum of squares as if it were the scatter of repeated measurements of one standard mixes those two differences.{{cite:dodge2008}} (p. 183)

## Connections
[Systematic error](systematic-error.qmd) is the shift that a correction is aimed at. [Measurement error](measurement-error.qmd) is the broader difference between a recorded value and the quantity being measured, of which the random error is the chance part. The [standard error](standard-error.qmd) of a mean is the scale of the mean's sampling variability, which is the random-error scale divided by a function of the number of readings when the readings are uncorrelated. Accuracy, in the metrology glossary, includes both the precision of the scatter and the systematic offset of the average from the reference. Precision alone leaves the offset out.{{cite:nist_glossary2002}} (Glossary, "accuracy"){{cite:dodge2008}} (p. 183)
