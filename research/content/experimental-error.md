## Lead context

A resistor is baked at a set temperature and measured again. Two resistors at the same temperature do not change by the same amount. The gap, after the temperature effect is accounted for, is experimental error: the piece of the response traced to influences the experimenter did not control. It is the noise against which a treatment difference has to stand, and it is not the same thing as a mistake in arithmetic or a hypothesis-testing error.{{cite:dodge2008}} (p. 183){{cite:nist_anova2002}} (§7.4.3.1)

## Motivating example

Three ovens are set to three temperatures, with several resistors in each. The analysis asks whether temperature shifted the resistance. Even within one oven the changes differ. That within-oven scatter is what an analysis of variance calls error: the sum of squares left after the treatment means have been fitted. If the ovens had been run with repeated centre points of a designed experiment, those repeated points would have been a direct reading of how large this uncontrolled scatter is. Without some such reading, a temperature difference cannot be compared with the variation the experiment itself produces.{{cite:nist_anova2002}} (§7.4.3.1){{cite:nist_glossary2002}} (Glossary, "centerpoint")

## Definition

Experimental error is the error due to uncontrolled variables. In the older classification of measurement errors it sits beside absolute and relative error, accidental error attributed to the experimenter, random error with a probability description, residual error as the gap between a fitted value and an observation, and systematic error that repeats in the same direction. A statistical analysis sees a combination of these, not a pure specimen of one of them.{{cite:dodge2008}} (p. 183)

In a one-way layout the same idea is operational. The corrected total sum of squares of the responses splits as

$$
\sum_i\sum_j(y_{ij}-\bar y_{\cdot\cdot})^2
=\sum_i n_i(\bar y_{i\cdot}-\bar y_{\cdot\cdot})^2
+\sum_i\sum_j(y_{ij}-\bar y_{i\cdot})^2,
$$

treatment sum of squares plus error sum of squares. The second term is the residual variation within treatments. Divided by its degrees of freedom it estimates the variance of the uncontrolled scatter, on the assumption that this variance is the same in each group.{{cite:nist_anova2002}} (§7.4.3.1)

Repeated centre points of a factorial design, where every factor is held at its midpoint, estimate the magnitude of that scatter directly, because the controlled factors are not changing.{{cite:nist_glossary2002}} (Glossary, "centerpoint")

Control a factor and the response still moves. The movement comes from variables that were not set: small differences in the resistors, placement in the oven, timing, the measuring instrument, the person using it. Some of those influences behave like chance from run to run. Some are systematic and repeat whenever the same slip in procedure is repeated. Experimental error, in the narrow metrological list, is the part due to the uncontrolled variables. In a comparative experiment it is estimated by the scatter among units that saw the same treatment.{{cite:dodge2008}} (p. 183){{cite:nist_anova2002}} (§7.4.3.1)

## Properties

The split of sums of squares is an identity. It does not by itself say that the error term is normal, independent, or free of missed factors. Those are extra assumptions that let a mean square for error become the denominator of an $F$ statistic. If a factor that affects the response was left out of the model and is entangled with the treatment, its contribution is inside the residual and the residual no longer estimates pure uncontrolled noise.{{cite:nist_anova2002}} (§7.4.3.1)

Random error, in the measurement classification, is the chance combination of instrument and user contributions, and it is the part whose statistical properties are studied with probability. Systematic error repeats. Experimental error as “uncontrolled variables” can include either, until the design separates them. Randomisation and replication are the design tools that give the uncontrolled piece a distribution one can estimate. A single run at each treatment has no within-treatment scatter to estimate.{{cite:dodge2008}} (p. 183){{cite:nist_glossary2002}} (Glossary, "centerpoint")

Type I and type II errors are different uses of the word. They are wrong decisions in a test: rejecting a true null, or failing to reject a false one. They are probabilities computed from a model. They are not the residual of a measurement.{{cite:dodge2008}} (p. 183)

## Statistical use

Estimate experimental error from replicates that share the same controlled conditions, or from the residual mean square after the controlled factors are fitted, and use that estimate as the scale for treatment contrasts. In a designed experiment, repeated centre points are a planned version of the same estimate. Report the error mean square, or the residual standard deviation, beside any treatment effect, so the effect is seen in units of the scatter the experiment actually produced.{{cite:nist_anova2002}} (§7.4.3.1){{cite:nist_glossary2002}} (Glossary, "centerpoint")

Do not treat a [type I error](type-i-and-type-ii-errors.qmd) rate as a substitute for this scale. The test uses the estimated experimental error. It is not the error. An [effect size](effect-size.qmd) that is large beside the residual standard deviation is a different statement from an effect size that is large in the original units and small beside a noisy measurement.

## Worked example

Two treatments have observations $(3,5)$ and $(8,10)$. The treatment means are $4$ and $9$, and the grand mean is $6.5$. The treatment sum of squares is

$$
2(4-6.5)^2+2(9-6.5)^2=2(6.25)+2(6.25)=25.
$$

The error sum of squares is

$$
(3-4)^2+(5-4)^2+(8-9)^2+(10-9)^2=4.
$$

The total sum of squares is $25+4=29$. Of the variation in the four numbers, 4 is the within-treatment piece that estimates experimental error, and 25 is the piece associated with the treatment means. With two observations per treatment the error sum of squares has $4-2=2$ degrees of freedom, so the error mean square is $4/2=2$.{{cite:nist_anova2002}} (§7.4.3.1)

**Your turn.** Treatments $(1,3)$ and $(5,7)$ have means $2$ and $6$ and grand mean $4$. Compute the treatment sum of squares and the error sum of squares.

::: {.callout-tip collapse="true" title="Answer"}
The treatment sum of squares is $2(2-4)^2+2(6-4)^2=16$. The error sum of squares is $(1-2)^2+(3-2)^2+(5-6)^2+(7-6)^2=4$. The within-treatment piece is again $4$, on $2$ degrees of freedom.
:::

## Common misconceptions

Experimental error is not a blunder and not a rounding error, though both can hide inside a residual. It is not the [bias of an estimator](bias-of-an-estimator.qmd), which is a property of a rule under repeated sampling. It is not a type I or type II error. A residual of a fitted model estimates experimental error only when the mean structure is right. A significant $F$ statistic does not mean the experimental error was small in any absolute sense. It means the treatment sum of squares was large relative to the error sum of squares.{{cite:dodge2008}} (p. 183){{cite:nist_anova2002}} (§7.4.3.1)

The sum-of-squares split is algebraic. Interpreting the error mean square as the variance of uncontrolled noise assumes independent observations, a common variance, and a mean model that has not left systematic structure in the residual. Centre-point replicates estimate that variance at the centre of the design, not automatically at every corner. Uncontrolled variables that are constant across the whole experiment are invisible to the residual and can still shift every treatment together.{{cite:nist_anova2002}} (§7.4.3.1){{cite:nist_glossary2002}} (Glossary, "centerpoint"){{cite:dodge2008}} (p. 183)

## History

Eighteenth-century writers on the errors of repeated measurements — Simpson, Lagrange, Laplace, and Gauss — built probability distributions for the discrepancy between an observation and a reference value, and used the mean of several observations as the approximation to that value. Later metrology separated the discrepancy into absolute, relative, accidental, experimental, random, residual, systematic, and rounding contributions, with experimental error reserved for uncontrolled variables. Comparative experiments turned the same idea into a sum of squares. Analysis of variance partitions the response into a part associated with the factors the experimenter set and a part left inside the treatments, and designed experiments use repeated centre points when a direct estimate of that leftover scatter is wanted.{{cite:dodge2008}} (p. 183){{cite:nist_anova2002}} (§7.4.3.1){{cite:nist_glossary2002}} (Glossary, "centerpoint")

## Connections

[One-way analysis of variance](one-way-analysis-of-variance.qmd) is the decomposition that isolates the error sum of squares. [Type I and type II errors](type-i-and-type-ii-errors.qmd) are decision errors in a test. A residual is the observation-level version of the error term. [Effect size](effect-size.qmd) is the treatment contrast that the error scale is used to judge.
