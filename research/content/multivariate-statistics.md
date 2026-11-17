

## Lead context

An observation in a medical record, a survey, or an image is rarely one number. It is a vector: several symptoms, several test scores, the intensities of many pixels. Multivariate statistics is the set of methods that keep those numbers together. Means become vectors, variances become matrices, and the scientific question is often whether the vector, not any single coordinate, differs between groups or can be compressed into fewer directions.

## Motivating example

Two measurements on three units are (1, 2), (2, 3), and (3, 4). Each margin has mean 2, 3, and the second coordinates are exactly the first plus one. The sample covariance of the two columns, with divisor 2, uses centred values (-1, -1), (0, 0), (1, 1). The cross-product sum is 1+0+1 = 2, so the covariance is 1. The two sample variances are also 1. A multivariate summary has to keep that cross-product. Analysing each column separately would report two variances and would miss that the columns move together.

## Definition

Multivariate statistics treats data in which each observation is a collection of measurements. In the language of statistical learning the measurements are inputs, predictors, or features, and there may also be a response. When there is no response, the analysis is unsupervised: the structure has to be found in the vectors themselves. When the response is a class label, the task is classification, which divides the space of vectors into regions. The field includes both, and it includes the probability models, such as the [multivariate normal distribution](multivariate-normal-distribution.qmd), that give those vectors a joint distribution. It is not a licence to run a separate one-variable test on every coordinate and ignore the rest.{{cite:hastie_esl2009}} (Ch. 2, §2.2, p. 9; Ch. 4, §4.1, p. 101){{cite:james_islr2021}} (Ch. 2, p. 26)

Multivariate analysis is one of the standard tools of biostatistics, next to regression and resampling, because a patient or an organism is measured in several ways at once. The same methods appear in psychometry when several scores define a scale, and in official statistics when several indicators describe one area.{{cite:dodge2008}} (pp. 49, 519)

## Statistical use

A mean vector and a covariance matrix replace the mean and variance. [Hotelling's T² test](hotelling-s-t2-test.qmd) compares mean vectors. [Principal component directions](principal-component-directions.qmd) replace the original coordinates with a few linear combinations that keep as much variation as possible. [Factor analysis](factor-analysis.qmd) explains the coordinates by a smaller set of latent factors. Classification uses [linear discriminant analysis](linear-discriminant-analysis.qmd), which separates classes by a linear function of the features, and tree or ensemble methods when the boundary is not linear. [Partial correlation](partial-correlation.qmd) describes the association of two coordinates after others are held fixed. With censored or binary coordinates the models become multivariate regressions rather than a single normal sample, but the object is still the vector.{{cite:hastie_esl2009}} (Ch. 4, §4.1, p. 101){{cite:james_islr2021}} (Ch. 2, p. 26)

Unsupervised methods are harder to check than supervised ones. There is no held-out response that the fitted summary must predict. A component plot or a clustering can be useful and still not be a unique description of the sample.{{cite:james_islr2021}} (Ch. 2, p. 26)


## Worked example

Two measurements on three units are (1, 2), (2, 3), and (3, 4). Each margin has mean 2, 3, and the second coordinates are exactly the first plus one. The sample covariance of the two columns, with divisor 2, uses centred values (-1, -1), (0, 0), (1, 1). The cross-product sum is 1+0+1 = 2, so the covariance is 1. The two sample variances are also 1. A multivariate summary has to keep that cross-product. Analysing each column separately would report two variances and would miss that the columns move together.

**Your turn.** Using the same records, recompute the featured summary and state which population quantity it estimates.

::: {.callout-tip collapse="true" title="Answer"}
Recompute the displayed summary from the same records. It estimates the quantity named in the example, for these records only.
:::



The integer list used above is a device for keeping the target fixed. With 11 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.

That integer list used above is a device for keeping the target fixed. With 11 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.
## History

Nineteenth-century biometry already worked with several measurements on the same person, and Galton and Pearson's correlation is the pairwise piece of that habit. Fisher's allocation of experimental units and his later discriminant methods made joint measurements a tool for classification as well as for association. The computing expansion after the middle of the twentieth century made high-dimensional versions routine: many features, sometimes more features than observations, with principal components, discriminant rules, and clustering as the standard reductions. Textbooks of statistical learning present that collection as one subject, supervised or not, rather than as a list of isolated tests.{{cite:dodge2008}} (p. 49){{cite:hastie_esl2009}} (Ch. 4, §4.1, p. 101){{cite:james_islr2021}} (Ch. 2, p. 26)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 11. Their total is 66, so their mean is 6.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 4.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Multivariate statistics has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 6.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [multivariate normal distribution](multivariate-normal-distribution.qmd), [Hotelling's T² test](hotelling-s-t2-test.qmd), [Principal component directions](principal-component-directions.qmd), [Factor analysis](factor-analysis.qmd).

Two further limits are algebraic. The sum of deviations from the mean 6.0 is zero, so the mean is the least-squares centre of these 11 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 6.0.

## Connections

Multivariate statistics supplies the joint models used in [medical statistics](medical-statistics.qmd), [psychological statistics](psychological-statistics.qmd), and [pattern recognition](pattern-recognition.qmd). [Structural equation modelling](structural-equation-modelling.qmd) is the branch that puts latent variables and directed relations on top of the covariance matrix. A significant marginal test on one coordinate can vanish, or reverse, once the other coordinates are in the model. That is not a paradox in the arithmetic. It is the reason the vector was recorded.{{cite:james_islr2021}} (Ch. 2, p. 26){{cite:dodge2008}} (p. 519)
