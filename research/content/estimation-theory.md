

## Lead context

A population parameter is not observed. A sample is. Estimation theory is the account of how a function of the sample is made to stand for the parameter, and of what can be said about the error. It splits into producing a single number and producing a set of plausible numbers. The theory then asks which functions are worth using.{{cite:dodge2008}} (pp. 184–185){{cite:openintro2019}} (Ch. 5, §5.1.1)

## Motivating example

A sample of four measurements is 2, 4, 4, 6. The sample mean is 16/4 = 4. The sum of squared deviations from 4 is 0+0+0+4 wait: (2-4)^2+(4-4)^2+(4-4)^2+(6-4)^2 = 4+0+0+4 = 8. The unbiased sample variance uses the divisor 3, so s^2 = 8/3. Estimation theory asks which function of the sample is being used, what population quantity it is aimed at, and how that function varies across samples. The number 4 estimates a mean. The number 8/3 estimates a variance. Reporting either number without the target confuses the estimator with the parameter.

## Definition

Estimation is the procedure that determines the value of a parameter associated with a population. A sample is drawn, and an estimator — a function of the sample that does not require the unknown parameter — is evaluated. The number it returns in the sample actually drawn is the estimate. The theory of that procedure is estimation theory.{{cite:dodge2008}} (pp. 184–185)

The theory is divided into two large parts. Point estimation returns one value. Interval estimation returns a range. A confidence interval is the usual interval procedure: at a stated confidence level, the proportion of repeated intervals that cover the parameter is the advertised level, when the sampling model is right. For a normal mean with known variance the interval is the sample mean plus and minus a normal critical value times $\sigma/\sqrt{N}$. When the variance is estimated, the interval is wider, because the estimated scale is itself uncertain.{{cite:dodge2008}} (p. 184){{cite:nist_confidence2002}} (§7.1.4)

An estimator is any statistical function of the sample used for this purpose. The estimate is the value the function takes on the observed sample. Keeping the two words apart is the theory’s first distinction: properties such as bias belong to the function, considered before the sample is drawn, not to the single number written in a report.{{cite:dodge2008}} (p. 185)

## Statistical use

Sampling runs from the population to the sample. Estimation runs back. For a proportion, the sample proportion $\hat p$ estimates the population proportion $p$, and $\hat p-p$ is the error of that estimate. The error has a sampling piece, which is studied by the distribution of $\hat p$, and a bias piece, which comes from systematic features of the design or the measurement. Much of elementary estimation theory is the sampling piece: standard errors, intervals, and the conditions under which a normal approximation applies.{{cite:openintro2019}} (Ch. 5, §5.1.1; §5.1.3)

Two classical constructions organise a large part of the theory. Least squares estimates the parameters of a linear model by minimising the sum of squared deviations between the data and the fitted values. Pearson’s method of moments matches sample moments to population moments. Maximum likelihood, introduced by Fisher as a fitting criterion, chooses the parameter that makes the observed sample as probable as the model allows. Fisher’s later vocabulary then compares constructions: an estimator may be called biased, efficient, or sufficient, and those words are claims about its sampling behaviour.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1){{cite:dodge2008}} (pp. 184–185)

Interval estimates are reported with the point because a point without a scale of error invites a reading the theory does not license. A 95% interval for a normal mean is not a list of values that each have probability 95%. It is the output of a method that covers in 95% of repeated samples. Estimation theory is responsible for both the point and that sentence about the method.{{cite:nist_confidence2002}} (§7.1.4){{cite:openintro2019}} (Ch. 5)


## Worked example

A sample of four measurements is 2, 4, 4, 6. The sample mean is 16/4 = 4. The sum of squared deviations from 4 is 0+0+0+4 wait: (2-4)^2+(4-4)^2+(4-4)^2+(6-4)^2 = 4+0+0+4 = 8. The unbiased sample variance uses the divisor 3, so s^2 = 8/3. Estimation theory asks which function of the sample is being used, what population quantity it is aimed at, and how that function varies across samples. The number 4 estimates a mean. The number 8/3 estimates a variance. Reporting either number without the target confuses the estimator with the parameter.

**Your turn.** Using the same records, recompute the featured summary and state which population quantity it estimates.

::: {.callout-tip collapse="true" title="Answer"}
Recompute the displayed summary from the same records. It estimates the quantity named in the example, for these records only.
:::



The integer list used above is a device for keeping the target fixed. With 11 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.
## History

The concept is traced to the first mathematical work on estimation: Jacob Bernoulli in 1713, Laplace in 1774, and Daniel Bernoulli in 1778. Least squares, in the late eighteenth and early nineteenth centuries, was the next large advance. Pearson’s method of moments, in papers of 1894 and 1898, gave a general matching rule. The foundations of the theory, in the usual historical judgement, are Fisher’s. A 1912 paper introduced maximum likelihood as a fitting criterion. The 1922 paper on the mathematical foundations of theoretical statistics set out what estimation is. The 1925 paper on the theory of statistical estimation introduced the definitions — biased, efficient, sufficient — that became the subject’s ordinary language.{{cite:dodge2008}} (pp. 184–185)

Gauss’s theory of errors had already treated the mean of repeated measurements as an approximation to a reference value, with a probability distribution for the error. Interval statements grew up beside the point theory, and by the time of modern handbooks a confidence interval was a standard companion of an estimated mean, with an explicit warning that an unknown standard deviation widens the interval.{{cite:dodge2008}} (p. 183){{cite:nist_confidence2002}} (§7.1.4)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 11. Their total is 66, so their mean is 6.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 4.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Estimation theory has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 6.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [estimator](estimator.qmd), [Bias of an estimator](bias-of-an-estimator.qmd), [mean squared error](mean-squared-error.qmd), [consistency](consistent-estimator.qmd).

Two further limits are algebraic. The sum of deviations from the mean 6.0 is zero, so the mean is the least-squares centre of these 11 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 6.0.

## Connections

An [estimator](estimator.qmd) is the function the theory studies. [Bias of an estimator](bias-of-an-estimator.qmd), [mean squared error](mean-squared-error.qmd), and [consistency](consistent-estimator.qmd) are the usual scores. [Maximum likelihood](maximum-likelihood.qmd) and the [method of moments](method-of-moments.qmd) are constructions. [Frequentist inference](frequentist-inference.qmd) is the interpretation of the coverage and error probabilities. [Mathematical statistics](mathematical-statistics.qmd) is the larger subject in which this theory sits. [Asymptotic analysis](asymptotic-analysis.qmd) is how the theory proceeds when the exact distribution of the estimator is unknown.
