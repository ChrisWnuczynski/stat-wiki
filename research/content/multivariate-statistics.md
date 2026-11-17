## Lead context

An observation in a medical record, a survey, or an image is rarely one number. It is a vector: several symptoms, several test scores, the intensities of many pixels. Multivariate statistics is the set of methods that keep those numbers together. Means become vectors, variances become matrices, and the scientific question is often whether the vector, not any single coordinate, differs between groups or can be compressed into fewer directions.

## Definition — Scope

Multivariate statistics treats data in which each observation is a collection of measurements. In the language of statistical learning the measurements are inputs, predictors, or features, and there may also be a response. When there is no response, the analysis is unsupervised: the structure has to be found in the vectors themselves. When the response is a class label, the task is classification, which divides the space of vectors into regions. The field includes both, and it includes the probability models, such as the [multivariate normal distribution](multivariate-normal-distribution.qmd), that give those vectors a joint distribution. It is not a licence to run a separate one-variable test on every coordinate and ignore the rest.{{cite:hastie_esl2009}} (Ch. 2, §2.2, p. 9; Ch. 4, §4.1, p. 101){{cite:james_islr2021}} (Ch. 2, p. 26)

Multivariate analysis is one of the standard tools of biostatistics, next to regression and resampling, because a patient or an organism is measured in several ways at once. The same methods appear in psychometry when several scores define a scale, and in official statistics when several indicators describe one area.{{cite:dodge2008}} (pp. 49, 519)

## Statistical use

A mean vector and a covariance matrix replace the mean and variance. [Hotelling's T² test](hotelling-s-t2-test.qmd) compares mean vectors. [Principal component directions](principal-component-directions.qmd) replace the original coordinates with a few linear combinations that keep as much variation as possible. [Factor analysis](factor-analysis.qmd) explains the coordinates by a smaller set of latent factors. Classification uses [linear discriminant analysis](linear-discriminant-analysis.qmd), which separates classes by a linear function of the features, and tree or ensemble methods when the boundary is not linear. [Partial correlation](partial-correlation.qmd) describes the association of two coordinates after others are held fixed. With censored or binary coordinates the models become multivariate regressions rather than a single normal sample, but the object is still the vector.{{cite:hastie_esl2009}} (Ch. 4, §4.1, p. 101){{cite:james_islr2021}} (Ch. 2, p. 26)

Unsupervised methods are harder to check than supervised ones. There is no held-out response that the fitted summary must predict. A component plot or a clustering can be useful and still not be a unique description of the sample.{{cite:james_islr2021}} (Ch. 2, p. 26)

## History

Nineteenth-century biometry already worked with several measurements on the same person, and Galton and Pearson's correlation is the pairwise piece of that habit. Fisher's allocation of experimental units and his later discriminant methods made joint measurements a tool for classification as well as for association. The computing expansion after the middle of the twentieth century made high-dimensional versions routine: many features, sometimes more features than observations, with principal components, discriminant rules, and clustering as the standard reductions. Textbooks of statistical learning present that collection as one subject, supervised or not, rather than as a list of isolated tests.{{cite:dodge2008}} (p. 49){{cite:hastie_esl2009}} (Ch. 4, §4.1, p. 101){{cite:james_islr2021}} (Ch. 2, p. 26)

## Connections

Multivariate statistics supplies the joint models used in [medical statistics](medical-statistics.qmd), [psychological statistics](psychological-statistics.qmd), and [pattern recognition](pattern-recognition.qmd). [Structural equation modelling](structural-equation-modelling.qmd) is the branch that puts latent variables and directed relations on top of the covariance matrix. A significant marginal test on one coordinate can vanish, or reverse, once the other coordinates are in the model. That is not a paradox in the arithmetic. It is the reason the vector was recorded.{{cite:james_islr2021}} (Ch. 2, p. 26){{cite:dodge2008}} (p. 519)
