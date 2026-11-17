

## Lead context

Bayesian statistics is the part of statistics that states uncertainty about unknowns with probability, then revises that statement after data arrive. A conclusion is a probability for the unknown given the observations, together with a check that the model which produced it is still credible.{{cite:gelman_bda2013}} (pp. 3–4){{cite:dodge2008}} (pp. 32–33)

## Motivating example

A coin is tossed 10 times and shows 7 heads. A uniform prior on the heads probability is a Beta(1,1) distribution. After 7 heads and 3 tails the posterior is Beta(8,4). Its mean is 8/(8+4) = 2/3. The maximum-likelihood estimate from the same tosses is 7/10 = 0.7. The two numbers answer different questions. The posterior mean is the mean of the probability assigned to the heads probability after the tosses. The maximum-likelihood value is the heads probability that makes these 10 tosses most probable. Neither number is the fraction of heads in a future sequence until a predictive calculation is added.

## Definition

The work has three parts. First, write a joint probability model for everything that could be observed and everything that is unknown, including parameters and any missing or future observations. The model has to match what is known about the scientific question and about how the data were collected. Second, condition on the values that were actually observed and read the conditional distribution of the unknowns. Third, ask whether that distribution and the model that produced it fit the data, whether the conclusions are substantively reasonable, and whether they move when the modelling choices move. If they do not hold up, the model is changed and the three parts are repeated.{{cite:gelman_bda2013}} (pp. 3–4, 24)

The unknown parameter is given a probability distribution because it is unknown. The distribution expresses uncertainty about the parameter. It describes a draw from a super-population only when a hierarchical model says that. After the sample arrives, the conditional distribution of the parameter is proportional to the product of the initial distribution and the likelihood. From that conditional distribution one reads a point summary, a region, or the probability of a set of parameter values.{{cite:dodge2008}} (pp. 32–34)

The field includes the construction of the joint model, the calculation that conditions on the data, and the criticism of the result. The conditioning step itself is [Bayesian inference](bayesian-inference.qmd). The number attached to a set of parameter values after the data arrive is a [posterior probability](posterior-probability.qmd). The joint specification, initial distribution together with sampling distribution, is a [Bayesian model](bayesian-model.qmd).{{cite:gelman_bda2013}} (pp. 1, 6–7)

## Statistical use

The identity that converts the joint model into the conditional distribution is [Bayes' rule](bayes-rule.qmd). With a squared-error penalty the point summary is the [posterior mean](posterior-mean.qmd); other one-number summaries are collected under [posterior point summaries](posterior-point-summaries.qmd). An interval that holds a stated posterior probability is a [Bayesian credible interval](bayesian-credible-interval.qmd). The posterior probability of a named region of the parameter is a [posterior hypothesis probability](posterior-hypothesis-probability.qmd). Predictions for a new observation, averaged over the parameter, are [prior and posterior predictive distributions](prior-and-posterior-predictive-distributions.qmd).{{cite:gelman_bda2013}} (pp. 7, 32–33){{cite:dodge2008}} (pp. 33–34)

Comparing two fully specified models uses the [marginal likelihood and Bayes factor](marginal-likelihood-and-bayes-factor.qmd). When the same form of prior is used for many related units and the prior's own constants are estimated from those units, the method is [empirical Bayes](empirical-bayes.qmd); when those constants are themselves given a distribution, the model is a [hierarchical Bayesian model](hierarchical-bayesian-model.qmd). Calculations that recognise an unnormalised product of likelihood and prior use the [kernel of a density](kernel-of-a-density.qmd). The factor that restores total probability one is the [normalizing constant](normalizing-constant.qmd).{{cite:gelman_bda2013}} (pp. 7, 24){{cite:dodge2008}} (p. 33)


## Worked example

A coin is tossed 10 times and shows 7 heads. A uniform prior on the heads probability is a Beta(1,1) distribution. After 7 heads and 3 tails the posterior is Beta(8,4). Its mean is 8/(8+4) = 2/3. The maximum-likelihood estimate from the same tosses is 7/10 = 0.7. The two numbers answer different questions. The posterior mean is the mean of the probability assigned to the heads probability after the tosses. The maximum-likelihood value is the heads probability that makes these 10 tosses most probable. Neither number is the fraction of heads in a future sequence until a predictive calculation is added.

**Your turn.** Using the same records, recompute the featured summary and state which population quantity it estimates.

::: {.callout-tip collapse="true" title="Answer"}
Recompute the displayed summary from the same records. It estimates the quantity named in the example, for these records only.
:::



The integer list used above is a device for keeping the target fixed. With 20 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.

That integer list used above is a device for keeping the target fixed. With 20 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.
## History

Thomas Bayes's essay on the chance of an unknown event, given the number of successes and failures, was published in 1763 after his death, through Richard Price. Pierre-Simon Laplace independently turned sampling probabilities around and computed probability statements about an unknown proportion from observed counts. That reversal was later called inverse probability. The modern field keeps the reversal and adds an explicit joint model, a computational summary of the conditional distribution, and a check of the model against the data and against alternative specifications.{{cite:gelman_bda2013}} (pp. 31, 56){{cite:dodge2008}} (p. 32)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 20. Their total is 210, so their mean is 10.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 8.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Bayesian statistics has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 10.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [Bayesian inference](bayesian-inference.qmd), [posterior probability](posterior-probability.qmd), [Bayesian model](bayesian-model.qmd), [Bayes' rule](bayes-rule.qmd).

Two further limits are algebraic. The sum of deviations from the mean 10.5 is zero, so the mean is the least-squares centre of these 20 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 10.5.

## Connections

The probability used for an unknown parameter is [Bayesian probability](bayesian-probability.qmd): the same numerical calculus that [probability theory](probability-theory.qmd) uses for random outcomes, applied to uncertainty about a quantity that will not be sampled repeatedly. A sampling model alone, summarised by [maximum likelihood](maximum-likelihood.qmd), does not by itself supply a probability distribution for the parameter. Intervals and tests that are calibrated by the long-run behaviour of a procedure answer a different question from a posterior probability for the parameter.{{cite:gelman_bda2013}} (pp. 3–4, 11){{cite:dodge2008}} (pp. 32–34)
