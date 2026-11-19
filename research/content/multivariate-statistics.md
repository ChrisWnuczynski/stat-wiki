## Lead context

An observation in a medical record, a survey, or an image is rarely one number. It is a vector: several symptoms, several test scores, the intensities of many pixels. Multivariate statistics is the set of methods that keep those numbers together. Means become vectors, variances become matrices, and the scientific question is often whether the vector, not any single coordinate, differs between groups or can be compressed into fewer directions. Analysing each coordinate by itself and then listing the significant ones answers a different question. The joint question is why the vector was recorded.{{cite:hastie_esl2009}} (p. 9, §2.2){{cite:james_islr2021}} (p. 26, §2.1.4)

## Motivating example

Three patients each have a systolic blood pressure and a resting heart rate. The pairs are $(1, 2)$, $(2, 3)$, and $(3, 1)$, written in units that have already been centred for the arithmetic below so that the story is about association rather than about the clinical scale. The blood-pressure mean is $2$ and the heart-rate mean is $2$. Each margin, looked at alone, is a short list of numbers with a mean and a spread. The pair is a different object: when blood pressure sits above its mean, heart rate in this tiny file tends to sit below its mean. A covariance records that tendency. Two separate variances do not. A clinician who reports only the two means has described the margins and has not described the joint pattern the two measurements were taken to capture.{{cite:james_islr2021}} (p. 26, §2.1.4){{cite:dodge2008}} (p. 49, Biostatistics)

The same structure appears whenever one unit contributes many numbers. A psychological scale is several items. A census tract is several indicators. An image patch is many pixels. Multivariate statistics is the decision to treat the unit as the observation and the numbers as coordinates of one vector.

## Intuition

One coordinate has a centre and a spread. Two coordinates have a centre, two spreads, and a statement about whether they move together. The statement is a sum of products of deviations. A product is positive when the two deviations have the same sign and negative when they have opposite signs. Adding the products and scaling by the spreads produces a correlation between $-1$ and $1$. The correlation is a property of the pair. It cannot be recovered from the two spreads, because the spreads throw away the sign of each product.

With more than two coordinates the same idea becomes a matrix. The diagonal holds the spreads. The off-diagonal holds the products. A linear combination of the coordinates, such as a weighted sum of test scores, has a variance that depends on the whole matrix, not on the diagonal alone. That is why a method that keeps only the separate standard deviations is not yet a multivariate method. The joint second-moment structure is the part that changes the answer.

When the scientific target is a class rather than a mean, the same matrix becomes a description of how the features scatter inside each class. A classifier that ignores the off-diagonal treats the features as unrelated. A classifier that uses it can tilt the boundary. Both are multivariate as soon as the observation is a vector. They differ in whether the response is a label or is absent.{{cite:hastie_esl2009}} (pp. 9 and 101){{cite:james_islr2021}} (p. 26, §2.1.4)

## Definition

Multivariate statistics treats data in which each observation is a collection of measurements. In the language of statistical learning the measurements are inputs, predictors, or features, and there may also be a response. When a response is present the analysis is supervised: the fit relates the response to the vector. When there is no response the analysis is unsupervised: for each observation one sees a vector and nothing to predict, and the structure has to be found in the vectors themselves. Classification is the supervised case in which the response is a class label and the rule partitions the space of vectors into regions. The field includes both, and it includes the probability models, such as the [multivariate normal distribution](multivariate-normal-distribution.qmd), that give those vectors a joint distribution.{{cite:hastie_esl2009}} (p. 9, §2.2; p. 101, §4.1){{cite:james_islr2021}} (p. 26, §2.1.4)

Write the $i$th observation as a column $X_i=(X_{i1},\ldots,X_{ip})^\top$. The sample mean vector is the coordinate-wise average

$$
\bar X=\frac1n\sum_{i=1}^n X_i.
$$


The sample covariance matrix, with divisor $n-1$, has entries

$$
s_{jk}=\frac1{n-1}\sum_{i=1}^n (X_{ij}-\bar X_j)(X_{ik}-\bar X_k).
$$


The diagonal entries are ordinary sample variances. The off-diagonal entries are sample covariances. A correlation is the covariance divided by the product of the two standard deviations. These are the descriptive summaries that replace the mean and variance of a one-variable course. Inferential procedures then treat $\bar X$ and the matrix $S=(s_{jk})$ as estimators of a population mean vector and a population covariance, under a joint model.

Multivariate analysis is one of the standard tools of biostatistics, next to regression and resampling, because a patient or an organism is measured in several ways at once. The same methods appear when several scores define a scale and when several indicators describe one area. The field is not a licence to run a separate one-variable test on every coordinate and ignore the rest.{{cite:dodge2008}} (p. 49, Biostatistics){{cite:james_islr2021}} (p. 26, §2.1.4)

## Properties

The covariance matrix is symmetric, because $s_{jk}=s_{kj}$. It is positive semidefinite: for every vector of weights $a$, the variance of the linear combination $a^\top X$ is $a^\top S a$, which cannot be negative. A correlation matrix is the covariance matrix of the standardised coordinates, so its diagonal is one. Standardising a coordinate changes the variances and the covariances by the same scale factors and leaves the correlations unchanged. Adding a constant to a coordinate leaves both the covariance and the correlation unchanged, because deviations from the mean do not see the constant.

A joint shift of the mean can be invisible in every margin and obvious in the pair, or visible in a margin and unimportant jointly. The second-moment matrix is what makes those two situations different. [Hotelling's $T^2$ test](hotelling-s-t2-test.qmd) compares mean vectors using the covariance, so that a difference aligned with a direction of small variance counts for more than the same Euclidean difference aligned with a direction of large variance. Two separate $t$ tests do not make that comparison. They also do not control the joint error rate of the two decisions.

[Principal component directions](principal-component-directions.qmd) replace the original coordinates with orthogonal linear combinations ordered by variance. The first component maximises $a^\top S a$ subject to $a^\top a=1$. Later components maximise the same quantity subject to being orthogonal to the earlier ones. The sum of the component variances equals the trace of $S$, the sum of the original variances, so the decomposition does not invent variation. It reorganises it. [Factor analysis](factor-analysis.qmd) explains the coordinates by a smaller set of latent factors plus coordinate-specific noise, which is a model for $S$, not only a rotation of it.

Classification uses the same matrix as a within-class scatter. [Linear discriminant analysis](linear-discriminant-analysis.qmd) separates classes by a linear function of the features. If class scores are linear in the features, the boundary where two scores are equal is a hyperplane. The [Bayes classifier](bayes-classifier.qmd), which assigns the class with the highest posterior probability, has the lowest possible error rate when the class-conditional distributions are correct. Estimated discriminants approximate that rule. They do not inherit the optimum merely by being called Bayes.{{cite:hastie_esl2009}} (p. 101, §4.1){{cite:james_islr2021}} (p. 142, §4.4)

Unsupervised methods are harder to check than supervised ones. There is no held-out response that the fitted summary must predict. A component plot or a clustering can be useful and still not be a unique description of the sample. With censored or binary coordinates the models become multivariate regressions rather than a single normal sample, but the object is still the vector.{{cite:james_islr2021}} (p. 26, §2.1.4)

## Worked example

Three observations on two coordinates are $(1,2)$, $(2,3)$, and $(3,1)$. The coordinate means are

$$
\bar x=\frac{1+2+3}{3}=2, \qquad \bar y=\frac{2+3+1}{3}=2.
$$


The deviations are $(-1,0)$, $(0,1)$, and $(1,-1)$. The sums of squared deviations are $1+0+1=2$ for the first coordinate and $0+1+1=2$ for the second. The sum of products is

$$
(-1)(0)+(0)(1)+(1)(-1)=-1.
$$


With divisor $n-1=2$, the sample variances are $s_{xx}=1$ and $s_{yy}=1$, and the sample covariance is $s_{xy}=-1/2$. The correlation is

$$
r=\frac{-1/2}{\sqrt{1\cdot 1}}=-\frac12.
$$


The negative sign matches the products: the third observation is high on the first coordinate and low on the second, and nothing in the other two observations cancels that product. The two variances are equal and positive, and they do not determine the sign. A report that listed $s_{xx}$ and $s_{yy}$ and omitted $s_{xy}$ would have described two margins and missed the association.{{cite:james_islr2021}} (p. 26, §2.1.4)

**Your turn.** Four observations are $(0,0)$, $(2,0)$, $(0,2)$, and $(2,2)$. Find the mean vector, the sum of products of deviations, and the correlation.

::: {.callout-tip collapse="true" title="Answer"}
The mean vector is $(1,1)$. The centred points are $(-1,-1)$, $(1,-1)$, $(-1,1)$, and $(1,1)$. The products are $1$, $-1$, $-1$, and $1$, which sum to $0$. The correlation is $0$.
:::

## Assumptions and limits

The sample covariance estimates a population covariance when the vectors are independent draws from a distribution that has second moments. A multivariate normal model adds the assumption that the mean vector and the covariance determine the whole distribution. Many procedures, including Hotelling's test and linear discriminant analysis with shared covariance, use that model for their exact null distributions. The descriptive matrix $S$ can still be computed when the vectors are not normal. The $p$-value that treats $S$ as Wishart, or the linear boundary that treats each class as normal with covariance $S$, cannot.

The divisor $n-1$ requires $n\ge 2$. A covariance matrix of $p$ coordinates has $p(p+1)/2$ free entries. When $p$ is large relative to $n$, those entries are estimated from too little information, $S$ is singular or unstable, and a method that inverts $S$ has to be replaced by a reduced-rank summary, a penalised covariance, or a method that never forms $S$ explicitly. Principal components remain defined, but the leading components can track noise.

Dependence among the units is a different failure. Repeated measures on the same patient are not $n$ independent vectors. Treating them as independent understates the variance of $\bar X$. A multilevel or longitudinal model is the remedy when the dependence has a grouping. A multivariate method that assumes independent vectors does not become valid because the coordinates inside each vector were modelled jointly.

Marginal tests are a limit of interpretation rather than of algebra. A coordinate can differ between groups in a one-variable test and not in the joint test, or the reverse, because the joint test uses the covariance. Reporting every marginal $p$-value as if it were a joint finding multiplies the error rate and ignores the reason the coordinates were collected together.{{cite:hastie_esl2009}} (p. 101, §4.1){{cite:dodge2008}} (p. 49, Biostatistics)

## Connections

Multivariate statistics supplies the joint models used in [medical statistics](medical-statistics.qmd), [psychological statistics](psychological-statistics.qmd), and [pattern recognition](pattern-recognition.qmd). [Structural equation modelling](structural-equation-modelling.qmd) is the branch that puts latent variables and directed relations on top of the covariance matrix. [Partial correlation](partial-correlation.qmd) describes the association of two coordinates after others are held fixed. [Supervised learning](supervised-learning.qmd) is the case with a response, and [unsupervised learning](unsupervised-learning.qmd) is the case without one. A significant marginal test on one coordinate can vanish, or reverse, once the other coordinates are in the model. That is a property of the joint distribution. It is the reason the vector was recorded.{{cite:james_islr2021}} (pp. 26 and 142){{cite:dodge2008}} (p. 49){{cite:hastie_esl2009}} (pp. 9 and 101)
