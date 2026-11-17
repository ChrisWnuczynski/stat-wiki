## Lead context

Parametric statistics studies procedures that begin by writing a model with a finite list of unknown constants, and that then use the data only to estimate or test those constants. The shape of the model is assumed. It is not left free to be whatever the sample suggests. The gain is that an arbitrary function of several predictors is replaced by a short vector of numbers. The cost is that the assumed form may be unlike the function that generated the data, in which case the estimate of that function is poor even if the constants are estimated precisely.{{cite:james_islr2013}} (pp. 21–22, §2.1.2){{cite:dodge2008}} (p. 375, Nonparametric statistics)

## Intuition

Suppose income depends on education and seniority, and the surface that relates them is unknown. One way to proceed is to declare that the surface is a plane, so that three numbers determine it, and then to choose those numbers so that the plane sits close to the observed incomes. Another way is to let the surface bend toward the points, with a penalty that stops it from threading every point exactly. The first way is parametric: the unknown object has been reduced to a parameter vector. The second way is nonparametric: no finite list was written down in advance, and the price is that many more observations are needed before the surface is stable.{{cite:james_islr2013}} (pp. 21–24, §2.1.2)

The same split appears in testing. A test that assumes each population has a named shape, for example a normal distribution, and then tests a parameter of that shape, is a parametric test. A test that refuses to name the distribution, and that uses ranks or signs instead, is the nonparametric counterpart. The parametric test is more powerful when its shape is right, and more fragile when the shape is wrong.{{cite:dodge2008}} (p. 251, Parametric tests; p. 375, Nonparametric statistics)

## Definition

A parametric method has two steps. First the analyst assumes a form for the unknown function or distribution. A linear mean
\[
f(X)=\beta_0+\beta_1 X_1+\cdots+\beta_p X_p
\]
is the simplest common assumption: the whole function is then determined by \(p+1\) coefficients. Second, the data are used to estimate those coefficients. Ordinary least squares is one way to do that step. It is not the only way. The model-based approach is called parametric because it reduces the problem of estimating \(f\) to the problem of estimating a set of parameters.{{cite:james_islr2013}} (pp. 21–22, §2.1.2)

A parametric test is a hypothesis test that presupposes a particular form for the distributions of the underlying populations. The Student test for a difference of means, under normal populations, is the usual example, and the Fisher test of variances is another. The form is part of the hypothesis, even when the parameter being tested is the only number that appears in the conclusion.{{cite:dodge2008}} (p. 251, Parametric tests)

The contrasting nonparametric methods do not write the form in advance. They look for a fit that stays close to the observations without becoming arbitrarily rough, and they are sometimes called parameter-free or distribution-free when the object is a test that avoids specifying the population distribution. They can follow shapes a parametric model would miss, and they generally need many more observations to do it. The term nonparametric was used by Wolfowitz in 1942. A histogram, and a kernel smooth built from a histogram, are simple nonparametric estimates of a density.{{cite:james_islr2013}} (pp. 23–24, §2.1.2){{cite:dodge2008}} (pp. 375–376, Nonparametric statistics)

Parametric does not mean a straight line. A nonlinear regression mean \(\beta_0\exp(-\beta_1 x)\) has a finite parameter vector and is a parametric model. It fails to be linear in the parameters, which is a different distinction, drawn in the entry for nonlinear regression: the mean is nonlinear when it is not linear in \(\beta\). A rank test that does not name the distribution of the observations is the nonparametric object set against a parametric test.{{cite:dodge2008}} (p. 372, Nonlinear regression; p. 376, Nonparametric test)

## Statistical use

[Simple linear regression](simple-linear-regression.qmd) and [ordinary least squares](ordinary-least-squares.qmd) are the parametric pattern in its most familiar form: assume a straight mean, then estimate two coefficients. On the income surface, the fit
\[
\text{income}\approx\beta_0+\beta_1\times\text{education}+\beta_2\times\text{seniority}
\]
reduces the whole problem to three numbers. The plane can miss curvature that is really there and still capture the direction of the association. That is the typical bargain. [Maximum likelihood](maximum-likelihood.qmd) is the general second step once the observations are given a distribution that depends on a finite parameter. A [generalised linear model](generalised-linear-model.qmd) keeps that structure and changes the distribution and the link. An [estimator](estimator.qmd) in this setting is a function of the sample aimed at one of those parameters, or at a function of them.{{cite:james_islr2013}} (pp. 22–23, §2.1.2){{cite:dodge2008}} (pp. 184–185, Estimation)

Making the parametric form more flexible, by adding coefficients, reduces the chance that the form is simply wrong and raises the chance that the fit follows the noise in the sample. That second failure is [overfitting](overfitting.qmd). A thin-plate spline with a roughness penalty is the nonparametric illustration: a smooth penalty can recover a curved surface, and a penalty that is too weak fits the training points exactly and misses new ones. The practical choice is not a slogan for one side. It is a choice of how many constants to estimate, given how many observations are in hand.{{cite:james_islr2013}} (pp. 22–24, §2.1.2)

Nonparametric tests are used when the distribution really is unspecified, and when the measurements are only ordered rather than numerical. Anderson–Darling, chi-squared, Kendall, Kolmogorov–Smirnov, Kruskal–Wallis, Wilcoxon, and Spearman procedures are the list usually named. They have less power than the appropriate parametric test when the parametric assumptions hold, and they are more robust when those assumptions fail. They are not a correction to apply after a parametric model has already been seen to fit.{{cite:dodge2008}} (pp. 375–376)

## Assumptions and limits

The parametric estimate of \(f\) is only as good as the form. If the chosen model is far from the true function, the estimate is poor even when each coefficient has a small standard error. Standard errors describe uncertainty inside the assumed form. They do not describe the distance from that form to the function that generated the data. A linear plane on a curved income surface can have tight coefficients and a systematic miss.{{cite:james_islr2013}} (pp. 22–23, §2.1.2)

A parametric test adds a distributional assumption to the form of the parameter. The Student test compares means of normal populations. When the populations are not normal, the nominal type I error need not be the error the test actually has. Nonparametric tests relax that assumption and pay for the relaxation in power, and in the class of alternatives they can see. A short sample makes the parametric assumption both more tempting, because there is little information with which to check it, and more dangerous, because a wrong shape moves the critical value.{{cite:dodge2008}} (pp. 251, 375–376)

Adding parameters until the training fit is perfect is not a way out. The extra constants estimate noise. Prediction on new observations then deteriorates, which is the overfitting the nonparametric roughness penalty was invented to control, and which a parametric model controls by refusing to add constants it cannot support.{{cite:james_islr2013}} (p. 24, §2.1.2)

## History

The division of labour, a specified family of distributions and then an estimate of its parameters, is the programme of the theory of estimation as it was formulated in the early twentieth century. Pearson's method of moments and Fisher's 1912 likelihood both take a parametric family as given and differ in how they use the sample. Fisher's 1922 and 1925 papers then gave bias, efficiency, and sufficiency a precise meaning inside that programme. The word nonparametric came into use for the procedures that refuse the first step; Wolfowitz used it in 1942. Linear and nonlinear parametric regressions developed alongside, sharing the finite parameter list and differing in how the parameters enter the mean. Introductions to statistical learning still open with the two-step reduction, because almost every later method is either a parametric model, a more flexible parametric model, or a nonparametric alternative that declines the reduction.{{cite:dodge2008}} (pp. 184–185 and 375){{cite:james_islr2013}} (pp. 21–24, §2.1.2)
