

## Lead context

Parametric statistics studies procedures that begin by writing a model with a finite list of unknown constants, and that then use the data only to estimate or test those constants. The shape of the model is assumed. It is not left free to be whatever the sample suggests.{{cite:james_islr2013}} (pp. 21–22, §2.1.2){{cite:dodge2008}} (p. 375, parametric structure specified in advance)

## Definition

A parametric method has two steps. First the analyst assumes a form for the unknown function or distribution. A linear mean
\[
f(X)=\beta_0+\beta_1 X_1+\cdots+\beta_p X_p
\]
is the simplest common assumption: the whole function is then determined by $p+1$ coefficients. Second, the data are used to estimate those coefficients. Ordinary least squares is one way to do that step. It is not the only way. The gain is that an arbitrary function of several predictors has been replaced by a short vector of numbers. The cost is that the assumed form may be unlike the function that generated the data, in which case the estimate of that function is poor even if the coefficients are estimated precisely.{{cite:james_islr2013}} (pp. 21–22, §2.1.2)

The contrasting nonparametric methods do not write the form in advance. They look for a fit that stays close to the observations without becoming arbitrarily rough, and they are sometimes called distribution-free when the object is a test that avoids specifying the population distribution. They can follow shapes a parametric model would miss, and they generally need many more observations to do it.{{cite:james_islr2013}} (pp. 22–23, §2.1.2){{cite:dodge2008}} (pp. 375–376, parameter-free and distribution-free methods)

"Parametric" does not mean "straight line." A nonlinear regression mean $\beta_0\exp(-\beta_1 x)$ has a finite parameter vector and is a parametric model. It fails to be linear in the parameters, which is a different distinction. A rank test that does not name the distribution of the observations is the nonparametric object Dodge sets against a parametric test.{{cite:dodge2008}} (p. 372, nonlinear in the parameters; p. 376, a test without a specified distribution)

A parametric model is the setting in which a [sufficient statistic](sufficient-statistic.qmd) can replace the whole sample for inference about the parameter, and in which the [bias of an estimator](bias-of-an-estimator.qmd) is a statement about one finite-dimensional target. [Polynomial least squares](polynomial-least-squares.qmd) is parametric and linear in its coefficients. [Nonlinear regression](nonlinear-regression.qmd) is parametric and not linear in its coefficients. A nonparametric regression, which does not commit to a finite coefficient list, sits on the other side of the distinction drawn in the estimation of $f$.{{cite:james_islr2013}} (pp. 21–23, §2.1.2){{cite:dodge2008}} (pp. 372 and 375)

## Statistical use

[Simple linear regression](simple-linear-regression.qmd) and [ordinary least squares](ordinary-least-squares.qmd) are the parametric pattern in its most familiar form: assume a straight mean, then estimate two coefficients. [Maximum likelihood](maximum-likelihood.qmd) is the general second step once the observations are given a distribution that depends on a finite parameter. A [generalised linear model](generalised-linear-model.qmd) keeps that structure and changes the distribution and the link. An [estimator](estimator.qmd) in this setting is a function of the sample aimed at one of those parameters, or at a function of them.

Making the parametric form more flexible, by adding coefficients, reduces the chance that the form is simply wrong and raises the chance that the fit follows the noise in the sample. That second failure is [overfitting](overfitting.qmd). The practical choice is not between a one-line slogan for parametric work and a slogan for nonparametric work. It is a choice of how many constants to estimate, given how many observations are in hand.{{cite:james_islr2013}} (pp. 21–23, §2.1.2){{cite:dodge2008}} (p. 375)

Nonparametric tests are used when the distribution really is unspecified, and when the measurements are only ordered rather than numerical. They are not a correction to apply after a parametric model has already been seen to fit.{{cite:dodge2008}} (p. 376, ordinal scales and the cost in efficiency)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 19. Their total is 190, so their mean is 10.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 8.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Parametric statistics has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 10.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [sufficient statistic](sufficient-statistic.qmd), [bias of an estimator](bias-of-an-estimator.qmd), [Polynomial least squares](polynomial-least-squares.qmd), [Nonlinear regression](nonlinear-regression.qmd).

Two further limits are algebraic. The sum of deviations from the mean 10.0 is zero, so the mean is the least-squares centre of these 19 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 10.0.

## History

The division of labour, a specified family of distributions and then an estimate of its parameters, is the programme of the theory of estimation as it was formulated in the early twentieth century. Pearson's method of moments and Fisher's likelihood both take a parametric family as given and differ in how they use the sample. The word nonparametric came into use for the procedures that refuse that first step; Wolfowitz used it in 1942. The linear and nonlinear parametric regressions developed alongside, sharing the finite parameter list and differing in how the parameters enter the mean.{{cite:dodge2008}} (pp. 184 and 375, estimation and the nonparametric term){{cite:james_islr2013}} (p. 21, §2.1.2, the parametric reduction)
