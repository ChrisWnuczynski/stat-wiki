

## Lead context

A laboratory repeats an assay. A survey organisation redraws a sample. A machine fills another shift of cartons. Frequentist inference reads a statistical procedure by what would happen across such repetitions, with the unknown quantity held fixed and the data allowed to vary. The reported interval or test is one draw from that procedure. Its advertised reliability is a property of the procedure, not a probability attached to the parameter after the data are seen.{{cite:gelman_bda2013}} (Ch. 1, §1.1, p. 3; §1.5, p. 12){{cite:openintro2019}} (Ch. 5)

## Definition

Frequentist inference evaluates statistical methods by their operating characteristics in a sequence of repeated samples. A confidence interval is the clearest case. The interval computed from one sample is a fixed set of numbers once the data are in. The 95% attached to it is the proportion of intervals, from the same method applied to repeated samples from the same population, that would cover the target. It is not, on this reading, the probability that the target lies in the interval already computed.{{cite:gelman_bda2013}} (Ch. 1, §1.1, p. 3){{cite:openintro2019}} (Ch. 5)

The same frequency idea is one of the ordinary meanings of probability itself: the relative frequency in a long sequence of trials performed in the same way and physically independent of one another. Applied to inference, the “trial” is the whole study. Coverage, the type I error rate of a test, and power are frequencies of that kind. They are defined before the data arrive, as properties of a rule.{{cite:gelman_bda2013}} (Ch. 1, §1.5, p. 12; Ch. 4, §4.4, p. 91)

Inferential statistics, in the sampling tradition, formulates hypotheses about population parameters and assesses them on a representative sample. The calculations that carry out that programme — point estimates, intervals, and tests — are the procedures whose long-run success rates frequentist inference reports. Bayesian statements put probability on the parameter. Frequentist statements put probability on the data-generating step.{{cite:dodge2008}} (pp. 263–264){{cite:gelman_bda2013}} (Ch. 1, §1.1, p. 3)

[Inference](inference.qmd) is the broader task of passing from sample to unobserved quantity. [Estimation theory](estimation-theory.qmd) builds the point and interval rules. [Asymptotic analysis](asymptotic-analysis.qmd) supplies the normal approximations that justify many large-sample standard errors and tests. A [decision problem](decision-problem.qmd) can use a frequentist error rate as one ingredient and still need a loss to choose an action. The [p-value](p-value.qmd) is a tail probability computed inside the null sampling distribution, which is a frequentist summary of surprise, not a probability that the null is true.

## Statistical use

A point estimate is frequentist when one studies its sampling distribution: bias, variance, and the probability that it falls near the target. A [confidence interval](confidence-interval.qmd) is frequentist by the coverage calculation just described. A test is frequentist when its critical region is chosen so that, if the null hypothesis is true, the probability of landing in that region equals a pre-set level, and when power is computed as the probability of landing there if a stated alternative is true.{{cite:openintro2019}} (Ch. 5){{cite:dodge2008}} (p. 264)

Large-sample frequentist calculations often coincide numerically with a Bayesian summary that uses a flat prior. A normal approximation to a posterior, centred at the posterior mode with variance from the observed information, has the same limit as the repeated-sampling distribution of that mode when the model contains the distribution that generated the data. In that limit a 95% central posterior interval covers the true value in 95% of repeated samples. The numerical agreement does not make the two interpretations the same sentence. One is a probability for the parameter given these data. The other is a success rate of a method.{{cite:gelman_bda2013}} (Ch. 4, §4.1, pp. 84–85; §4.4, pp. 91–92)

Consistency and asymptotic unbiasedness are frequentist properties of a point estimate: as samples grow, the estimate’s sampling distribution concentrates at the value it is said to estimate, or its bias becomes negligible beside its standard deviation. Those properties can be checked for an estimate whether or not the estimate was derived from a posterior.{{cite:gelman_bda2013}} (Ch. 4, §4.4, p. 92)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 9. Their total is 45, so their mean is 5.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 3.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Frequentist inference has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 5.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [Inference](inference.qmd), [Estimation theory](estimation-theory.qmd), [Asymptotic analysis](asymptotic-analysis.qmd), [decision problem](decision-problem.qmd).

Two further limits are algebraic. The sum of deviations from the mean 5.0 is zero, so the mean is the least-squares centre of these 9 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 5.0.

## History

The frequency reading of probability was already available in eighteenth-century work on games and errors, the setting in which de Moivre, Bayes, Gauss, and Laplace connected observations with unknown quantities. The twentieth-century shape of frequentist inference is later. Pearson’s 1900 criterion asked whether deviations could reasonably have arisen by random sampling. Gosset’s 1908 paper gave the mean of a small normal sample a reference distribution. Neyman and Pearson’s 1928 papers organised the use and interpretation of test criteria. Fisher’s programme of estimation, likelihood, and experimental design supplied the procedures whose repeated-sampling behaviour those tests and intervals summarise.{{cite:dodge2008}} (pp. 263–264)

Comparisons between this programme and probability statements about parameters have been continuous since. Frequency calculations remain the usual way to say what a published interval or test does under repetition, including as a check on Bayesian procedures treated as rules.{{cite:gelman_bda2013}} (Ch. 4, §4.4, p. 91; §4.6, pp. 97–98)
