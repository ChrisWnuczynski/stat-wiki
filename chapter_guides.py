"""Plain-language guide and level for each chapter.

Level rule
----------
A chapter is beginner when it uses only events, variables, samples, and tables,
including the R that holds those objects.
A chapter is intermediate when it adds one method on that base: several
variables at once, a limit or a chain, estimation or a test, regression, a
generalised linear model, a conjugate prior, or a standard classifier.
A chapter is advanced when one of those methods is already assumed: measure
and stochastic processes, optimality and finer asymptotics, MCMC and
hierarchical models, dependence across time or repeated measures, or
ensemble, network, and high-dimensional learning.
A question takes the level of the chapter it is filed under. There is no
separate label on the question.
"""

from __future__ import annotations

LEVELS = ("beginner", "intermediate", "advanced")

LEVEL_RULE = (
    "A chapter is beginner when it uses only events, variables, samples, and tables. "
    "It is intermediate when it adds one method, such as estimation, regression, a prior, or a standard classifier. "
    "It is advanced when that method is already assumed. A question has the level of its chapter."
)

# The five chapters in the starter path, in reading order.
STARTER = (
    "prob-01-experiments.qmd",
    "prob-02-random-variables.qmd",
    "da-01-studies-and-data.qmd",
    "da-02-descriptive-statistics.qmd",
    "da-03-using-r.qmd",
)


def _g(level: str, summary: str, needs: tuple[str, ...] = (), note: str = "") -> dict:
    return {"level": level, "summary": summary, "needs": list(needs), "note": note}


GUIDES: dict[str, dict] = {
    "prob-01-experiments.qmd": _g(
        "beginner",
        "A random experiment is a procedure whose outcome is not fixed in advance, but which can still be described exactly. This chapter builds the outcomes, the events, and a probability for each event.",
        note=(
            "Nothing else comes first. This is the chapter to open first. "
            "The second paragraph names densities, a prior, and Bayes' rule. "
            "Those words point at later chapters. You do not need them to read this one. "
            "Stay with events and conditional probability here, then go on to random variables."
        ),
    ),
    "prob-02-random-variables.qmd": _g(
        "beginner",
        "A random variable turns the outcome of an experiment into a number. This chapter is the distribution of that number: the chance of each value, the mean, and the spread.",
        ("prob-01-experiments.qmd",),
    ),
    "prob-03-simulation.qmd": _g(
        "beginner",
        "Simulation turns uniform random numbers into draws from a distribution you have already specified. The two constructions are inverting a distribution function and rejecting draws that miss a target shape.",
        ("prob-02-random-variables.qmd",),
    ),
    "prob-04-joint-distributions.qmd": _g(
        "intermediate",
        "Two or more numbers from the same experiment have a joint distribution. That joint distribution fixes the separate distributions, the chance of a region, and what one variable does when the other is known.",
        ("prob-02-random-variables.qmd",),
    ),
    "prob-05-transforms-and-limits.qmd": _g(
        "intermediate",
        "A function of a random variable is another random variable, and its distribution can be read from the original one. The limit theorems say what happens to an average as the sample grows.",
        ("prob-04-joint-distributions.qmd",),
    ),
    "prob-06-markov-chains.qmd": _g(
        "intermediate",
        "A Markov chain is a process with a short memory: the next state depends on the past only through the present. On a finite set of states the whole process is a transition matrix.",
        ("prob-02-random-variables.qmd",),
    ),
    "prob-07-reliability.qmd": _g(
        "intermediate",
        "Reliability is the probability that a system of unreliable parts is working. The structure says which patterns of working parts make the system work, and independence turns that structure into a probability.",
        ("prob-01-experiments.qmd",),
    ),
    "sp-01-stochastic-processes.qmd": _g(
        "advanced",
        "A stochastic process is a collection of random variables indexed by time. This chapter sets the vocabulary: paths, finite-dimensional distributions, and what it means for the future to depend on the present.",
        ("prob-06-markov-chains.qmd", "prob-05-transforms-and-limits.qmd"),
    ),
    "sp-02-branching.qmd": _g(
        "advanced",
        "A branching process counts a population in which each individual independently produces offspring. The mean number of offspring decides whether the line dies out or grows without bound.",
        ("sp-01-stochastic-processes.qmd", "prob-02-random-variables.qmd"),
    ),
    "sp-03-random-walks.qmd": _g(
        "advanced",
        "A random walk adds independent steps. This chapter is the position after many steps, the chance of hitting a barrier, and how long that hit takes.",
        ("sp-01-stochastic-processes.qmd",),
    ),
    "sp-04-discrete-markov.qmd": _g(
        "advanced",
        "This chapter returns to Markov chains with the tools for a long-run distribution, a first hit, and a calculation that conditions on the first step. The finite-state picture from the probability chapter is the starting point.",
        ("prob-06-markov-chains.qmd", "sp-01-stochastic-processes.qmd"),
    ),
    "sp-05-classes-and-reversibility.qmd": _g(
        "advanced",
        "States of a chain fall into classes that can or cannot reach one another. Reversibility is the extra balance that makes the long-run distribution easy to write down.",
        ("sp-04-discrete-markov.qmd",),
    ),
    "sp-06-poisson-processes.qmd": _g(
        "advanced",
        "A Poisson process counts events that arrive one by one, with no memory of when the last one came. The counts in an interval and the gaps between arrivals are two views of the same process.",
        ("prob-02-random-variables.qmd", "sp-01-stochastic-processes.qmd"),
    ),
    "sp-07-continuous-markov.qmd": _g(
        "advanced",
        "A continuous-time Markov chain waits an exponential time and then jumps. The rate matrix replaces the one-step transition matrix, and the long-run distribution solves a balance of rates.",
        ("sp-04-discrete-markov.qmd", "sp-06-poisson-processes.qmd"),
    ),
    "sp-08-queues.qmd": _g(
        "advanced",
        "A queue is a birth-death chain: arrivals increase the number present and departures decrease it. This chapter reads the long-run chance of each length and the mean time in the system.",
        ("sp-07-continuous-markov.qmd",),
    ),
    "sp-09-probability-spaces.qmd": _g(
        "advanced",
        "On a finite set every subset can be an event. On an uncountable set a sigma-algebra says which subsets are events, so that probability is defined where it needs to be and not asked to do the impossible.",
        ("prob-01-experiments.qmd", "prob-05-transforms-and-limits.qmd"),
    ),
    "sp-10-random-variables.qmd": _g(
        "advanced",
        "A random variable here is a measurable map from outcomes to numbers, and its law is the probability it pushes forward onto the line. Two variables can share a law without living on the same outcomes.",
        ("sp-09-probability-spaces.qmd", "prob-02-random-variables.qmd"),
    ),
    "sp-11-convergence.qmd": _g(
        "advanced",
        "A sequence of random variables can settle in several different senses. A rare huge value can vanish from a probability statement and still dominate an expectation, which is why the senses are not the same.",
        ("sp-10-random-variables.qmd", "prob-05-transforms-and-limits.qmd"),
    ),
    "sp-12-extremes.qmd": _g(
        "advanced",
        "An average is pulled by many observations, and a maximum is pulled by the upper tail. The scaling that gives a usable limit for the maximum is not the scaling used for an average.",
        ("sp-11-convergence.qmd", "prob-05-transforms-and-limits.qmd"),
    ),
    "inf-01-statistical-inference.qmd": _g(
        "intermediate",
        "A probability model says what a sample would look like if the parameters were known. Inference runs the other way: the sample is in hand and the parameter is not.",
        ("prob-02-random-variables.qmd", "da-02-descriptive-statistics.qmd"),
    ),
    "inf-02-estimation.qmd": _g(
        "intermediate",
        "An estimator is a function of the sample used as a guess at a parameter, and the number it produces on the data in hand is the estimate. This chapter is bias, variance, and the likelihood as a way to choose the guess.",
        ("inf-01-statistical-inference.qmd",),
    ),
    "inf-03-confidence-intervals.qmd": _g(
        "intermediate",
        "A point estimate does not say how far it might fall from the parameter. A confidence interval is a random interval whose long-run coverage is the stated probability, computed before the sample is seen.",
        ("inf-02-estimation.qmd",),
    ),
    "inf-04-hypothesis-tests.qmd": _g(
        "intermediate",
        "A test asks whether the data would be surprising if a stated hypothesis were true. The probability in that question is computed under the hypothesis, not as a probability that the hypothesis itself is true.",
        ("inf-02-estimation.qmd",),
    ),
    "inf-05-chi-square.qmd": _g(
        "intermediate",
        "A chi-squared statistic compares observed counts with the counts a model expected. It is the large-sample test for a fully specified discrete distribution and for independence in a table of counts.",
        ("inf-04-hypothesis-tests.qmd",),
    ),
    "inf-06-regression.qmd": _g(
        "intermediate",
        "Regression fits a line and then gives that line a probability model, so a slope, a mean response, and a new observation can have standard errors. The fit is a statement about the mean, not a causal effect of setting the predictor.",
        ("inf-02-estimation.qmd", "prob-02-random-variables.qmd"),
    ),
    "inf-07-anova.qmd": _g(
        "intermediate",
        "Analysis of variance compares several means by splitting the total sum of squares into a part between groups and a part within groups. With two groups the resulting comparison is the two-sample comparison of means.",
        ("inf-06-regression.qmd",),
    ),
    "inf-08-information-and-bounds.qmd": _g(
        "advanced",
        "Mean squared error compares estimators one already has. It does not say whether a better unbiased estimator is still possible. This chapter builds that bound from the information in the sample.",
        ("inf-02-estimation.qmd",),
    ),
    "inf-09-rao-blackwell.qmd": _g(
        "advanced",
        "The information bound is attained only in special families. This chapter shows how conditioning on a sufficient statistic improves an unbiased estimator, and when that improvement is the best unbiased estimator there is.",
        ("inf-08-information-and-bounds.qmd",),
    ),
    "inf-10-large-sample-estimation.qmd": _g(
        "advanced",
        "Unbiasedness and the information bound are finite-sample statements, and they often have no solution. This chapter is what maximum likelihood does as the sample grows, when an exact unbiased estimator is not available.",
        ("inf-02-estimation.qmd", "prob-05-transforms-and-limits.qmd"),
    ),
    "inf-11-most-powerful-tests.qmd": _g(
        "advanced",
        "A test fixes a null hypothesis and a type I error, and then looks for the critical region with the smallest type II error. For two simple hypotheses the most powerful test rejects for a large likelihood ratio.",
        ("inf-04-hypothesis-tests.qmd",),
    ),
    "inf-12-generalised-likelihood-ratio.qmd": _g(
        "advanced",
        "Most hypotheses leave parameters free, so the comparison is no longer between two completely specified distributions. The generalised likelihood ratio compares the best fit inside the null with the best fit overall.",
        ("inf-11-most-powerful-tests.qmd",),
    ),
    "inf-13-exact-tests.qmd": _g(
        "advanced",
        "The chi-squared approximation needs expected counts that are not tiny. An exact test for a table uses the probability of the observed table and of tables at least as extreme, under the null, without that approximation.",
        ("inf-05-chi-square.qmd",),
    ),
    "inf-14-linear-hypotheses.qmd": _g(
        "advanced",
        "One-way analysis of variance, two-way analysis of variance, and a polynomial regression are the same normal linear model with different columns. A hypothesis about several coefficients is one linear restriction on that model.",
        ("inf-06-regression.qmd", "inf-07-anova.qmd"),
    ),
    "inf-15-two-factor-anova.qmd": _g(
        "intermediate",
        "One factor splits a sample into groups. Two factors cross those groups, and the mean may depend on each factor separately or on their combination.",
        ("inf-07-anova.qmd",),
    ),
    "inf-16-predictive-values.qmd": _g(
        "intermediate",
        "Sensitivity and specificity describe a test conditional on the truth. The predictive values run the other way: the chance the condition is present given the test result, which depends on how common the condition is.",
        ("inf-04-hypothesis-tests.qmd", "da-01-studies-and-data.qmd"),
    ),
    "da-01-studies-and-data.qmd": _g(
        "beginner",
        "A study turns a question about the world into data and a conclusion. What the design can support, and what it cannot, is fixed by how the data were collected, before any model is fit.",
        ("prob-01-experiments.qmd", "prob-02-random-variables.qmd"),
    ),
    "da-02-descriptive-statistics.qmd": _g(
        "beginner",
        "Descriptive statistics summarise a sample before a model is fitted. The sample mean is the average, and the median, the spread, and a plot show shape and odd points that the average hides.",
        ("da-01-studies-and-data.qmd", "prob-02-random-variables.qmd"),
    ),
    "da-03-using-r.qmd": _g(
        "beginner",
        "This chapter is the language used to hold a table, summarise it, draw it, and fit a model that has already been defined. A command is useful only when the rows, the assumption, and the scale of the printed number match the question.",
        ("da-02-descriptive-statistics.qmd",),
    ),
    "da-04-estimation-examples.qmd": _g(
        "intermediate",
        "These examples compute an estimate and an interval on particular samples. The definitions of an estimator, likelihood, bias, and a confidence interval sit on the estimation and interval chapters.",
        ("inf-02-estimation.qmd", "inf-03-confidence-intervals.qmd"),
    ),
    "da-05-testing-examples.qmd": _g(
        "intermediate",
        "These examples carry a stated hypothesis through a test statistic and a p-value on particular samples. The probability is still the one computed under the hypothesis.",
        ("inf-04-hypothesis-tests.qmd",),
    ),
    "da-06-anova-examples.qmd": _g(
        "intermediate",
        "These examples compare means of a quantitative response across the levels of a factor. The sum-of-squares split and the F comparison are the ones derived for the analysis of variance.",
        ("inf-07-anova.qmd",),
    ),
    "da-07-regression-examples.qmd": _g(
        "intermediate",
        "These examples fit a line, read a coefficient, and form an interval for a mean response or a new response. The model is the normal linear model, not a new one.",
        ("inf-06-regression.qmd",),
    ),
    "da-08-linear-model-examples.qmd": _g(
        "intermediate",
        "Simple regression, multiple regression, and the analysis of variance are one normal linear model with different columns. These examples show that shared form on particular tables.",
        ("inf-06-regression.qmd", "inf-07-anova.qmd"),
    ),
    "da-09-chi-square-examples.qmd": _g(
        "intermediate",
        "These examples compare observed counts with expected counts, including independence in a two-way table. Each estimated parameter spends a degree of freedom in the reference distribution.",
        ("inf-05-chi-square.qmd",),
    ),
    "ur-01-exploratory-data-analysis.qmd": _g(
        "beginner",
        "Look at the table before fitting a model. The point is to learn what a row is, which values are missing, how each variable is shaped, and which patterns survive a split into groups.",
        ("da-03-using-r.qmd", "da-02-descriptive-statistics.qmd"),
    ),
    "ur-02-probability-and-simulation.qmd": _g(
        "beginner",
        "This chapter is the command for a density, a cumulative probability, a quantile, and a draw. A permutation test and an empirical distribution are included as experiments rather than as fitted models.",
        ("da-03-using-r.qmd", "prob-02-random-variables.qmd"),
    ),
    "ur-03-bootstrap-and-numerical.qmd": _g(
        "intermediate",
        "The bootstrap replaces an unknown sampling distribution by redrawing the observed units. One-dimensional integration and optimisation are the numerical checks for a density whose integral or mode can also be written down.",
        ("ur-02-probability-and-simulation.qmd", "inf-03-confidence-intervals.qmd"),
    ),
    "ur-04-mixtures-and-clustering.qmd": _g(
        "intermediate",
        "A mixture asks whether one observed distribution could be several latent groups, and clustering asks how to group rows that are described by many measurements. The commands here are those two fits, and the label that was held out of them.",
        ("ur-02-probability-and-simulation.qmd",),
    ),
    "ur-05-bayesian-computation.qmd": _g(
        "advanced",
        "This chapter computes a conjugate update, a Bayes factor, and two samplers. The draws are a stand-in for a posterior that has already been defined, and a Monte Carlo average is not a substitute for the wrong target.",
        ("bayes-02-beta-binomial.qmd", "ur-02-probability-and-simulation.qmd"),
    ),
    "ur-06-model-objects.qmd": _g(
        "intermediate",
        "A fitted model is an object with several views, and the printed summary is only one of them. Coefficients, the covariance, the rows used, and an interval for the mean or for a new observation are different extractions.",
        ("da-03-using-r.qmd", "inf-06-regression.qmd"),
    ),
    "ur-07-glms-in-r.qmd": _g(
        "intermediate",
        "A generalised linear model specifies a mean, a variance function, and a link from the mean to the predictors. This chapter is the command and the scale of each printed number, for binary data, counts, and positive responses.",
        ("ur-06-model-objects.qmd", "01-introduction-to-glms.qmd"),
    ),
    "ur-08-additive-models.qmd": _g(
        "intermediate",
        "An additive model keeps the response family and lets a predictor act through a smooth curve rather than a straight line. The basis dimension is an upper bound on the wiggles, not the complexity of the curve that is returned.",
        ("ur-07-glms-in-r.qmd", "06-smooth-means.qmd"),
    ),
    "ur-09-repeated-measures.qmd": _g(
        "advanced",
        "Each row of a repeated-measures table is a visit, and the independent unit is the person. A random intercept and a marginal model are two commands for that dependence, and they answer different questions when the link is not the identity.",
        ("08-random-intercepts.qmd", "ur-06-model-objects.qmd"),
    ),
    "ur-10-time-series.qmd": _g(
        "advanced",
        "Consecutive times are not interchangeable rows. This chapter fits on a past stretch only, scores a later stretch, and reads the sign in front of a lagged term.",
        ("12-time-series.qmd", "ur-06-model-objects.qmd"),
    ),
    "ur-11-checking-a-fit.qmd": _g(
        "intermediate",
        "A surprising number is usually a row, a scale, or a unit, not a deep property of the estimator. A check that changes two of those at once cannot say which one moved the answer.",
        ("ur-06-model-objects.qmd", "ur-01-exploratory-data-analysis.qmd"),
    ),
    "bayes-01-foundations.qmd": _g(
        "intermediate",
        "A prior is a probability distribution for an unknown quantity before the data arrive. Bayes' rule combines that prior with the likelihood and returns the distribution after the data, the posterior.",
        ("prob-02-random-variables.qmd", "inf-01-statistical-inference.qmd"),
        "The pointer in the opening probability chapter is not this argument. Read the event form of conditional probability there, and the distribution of a random variable, before this page.",
    ),
    "bayes-02-beta-binomial.qmd": _g(
        "intermediate",
        "A beta prior on a coin's heads probability, updated by binomial data, is another beta distribution. The posterior mean is pulled from the observed rate toward the prior mean by the pseudo-counts in the prior.",
        ("bayes-01-foundations.qmd", "prob-02-random-variables.qmd"),
    ),
    "bayes-03-normal-models.qmd": _g(
        "intermediate",
        "A normal sample with a normal prior for the mean has a normal posterior, and an unknown variance brings an inverse-gamma or a related partner. Conjugacy here is the same pattern as the beta–binomial update, for a different sampling model.",
        ("bayes-01-foundations.qmd", "prob-02-random-variables.qmd"),
    ),
    "bayes-04-mcmc.qmd": _g(
        "advanced",
        "When a posterior cannot be written in closed form, a Markov chain can be built whose long-run distribution is that posterior. Gibbs sampling and Metropolis–Hastings are two ways to take the steps.",
        ("bayes-01-foundations.qmd", "prob-06-markov-chains.qmd"),
    ),
    "bayes-05-categorical.qmd": _g(
        "intermediate",
        "Several categories replace the two outcomes of a coin, and a Dirichlet prior is the partner of a multinomial likelihood. The update adds the observed counts to the prior pseudo-counts, one category at a time.",
        ("bayes-02-beta-binomial.qmd",),
    ),
    "bayes-06-testing.qmd": _g(
        "advanced",
        "A Bayes factor compares two models by the probability each gives to the observed data, averaging over its prior. It updates the odds of the models. It is not itself the posterior probability of either model.",
        ("bayes-01-foundations.qmd", "inf-04-hypothesis-tests.qmd"),
    ),
    "bayes-07-exponential-families.qmd": _g(
        "advanced",
        "The conjugate updates for a coin, a normal mean, and a Poisson rate are one pattern. In an exponential family the prior that stays in the same family adds its natural statistic to the statistic from the sample.",
        ("bayes-02-beta-binomial.qmd", "bayes-03-normal-models.qmd"),
    ),
    "bayes-08-hierarchy.qmd": _g(
        "advanced",
        "Related groups can share a distribution for their parameters instead of being pooled into one group or left completely separate. That shared distribution is the hierarchy, and it can be conjugate or not.",
        ("bayes-03-normal-models.qmd",),
    ),
    "bayes-09-linear-regression.qmd": _g(
        "advanced",
        "Bayesian linear regression gives each observation its own mean, linear in the predictors, and puts a prior on the coefficients and the variance. The posterior is the normal–inverse-gamma update when the prior is chosen to match.",
        ("bayes-03-normal-models.qmd", "inf-06-regression.qmd"),
    ),
    "01-introduction-to-glms.qmd": _g(
        "intermediate",
        "A generalised linear model keeps a linear predictor and replaces the normal response with a distribution whose mean is a function of that predictor. The link is applied to the mean, not to each observed response.",
        ("inf-06-regression.qmd", "da-02-descriptive-statistics.qmd"),
    ),
    "02-inference-and-counts.qmd": _g(
        "intermediate",
        "This chapter is the precision of a generalised-linear fit, and the model for counts whose variance equals the mean. Overdispersion is what happens when the counts vary more than that mean allows.",
        ("01-introduction-to-glms.qmd",),
    ),
    "03-gamma-and-quasi.qmd": _g(
        "intermediate",
        "Positive continuous responses need a variance that grows with the mean, and a quasi-likelihood specifies that variance without a full distribution. This chapter is those two extensions of the count models.",
        ("02-inference-and-counts.qmd",),
    ),
    "04-categorical-responses.qmd": _g(
        "intermediate",
        "A response that lands in one of several categories has no mean of the labels worth interpreting. The models here are for the probabilities of the categories, ordered or unordered.",
        ("01-introduction-to-glms.qmd",),
    ),
    "05-comparisons-and-deviance.qmd": _g(
        "intermediate",
        "Deviance measures how far a fit is from a saturated description of the same data. Paired comparisons use the same binary building block when the response is which of two items wins.",
        ("04-categorical-responses.qmd",),
    ),
    "06-pit-residuals.qmd": _g(
        "advanced",
        "A plot of ordinary residuals from a binary or a count fit is striped, because the response can take only a few values. A probability-integral residual compares each observation with the fitted distribution instead of with a single fitted mean.",
        ("02-inference-and-counts.qmd", "04-categorical-responses.qmd"),
    ),
    "06-smooth-means.qmd": _g(
        "intermediate",
        "A coefficient is worth having when a unit change has a meaning. A smooth mean lets the curve bend, with a penalty on wiggliness so the fit is not a curve through every point.",
        ("inf-06-regression.qmd",),
    ),
    "07-additive-and-mixed.qmd": _g(
        "advanced",
        "One smooth covariate is enough for a curve against a single predictor. This chapter puts more than one covariate into that smooth, and then lets a block carry its own curve.",
        ("06-smooth-means.qmd",),
    ),
    "08-random-intercepts.qmd": _g(
        "advanced",
        "Responses that share a person, a place, or a time are not independent. A random intercept gives each block its own level, drawn from a common distribution, and that shared level is the dependence.",
        ("inf-06-regression.qmd",),
    ),
    "08-slopes-and-glmms.qmd": _g(
        "advanced",
        "Blocks can differ in slope as well as in level. This chapter fits that richer random effect, and then replaces the normal residual by a binary response inside the same block structure.",
        ("08-random-intercepts.qmd",),
    ),
    "09-marginal-models.qmd": _g(
        "advanced",
        "A mixed model explains the correlation with a shared random effect. A marginal model does not. It describes the average curve in the population and uses a working correlation only to estimate that curve.",
        ("08-random-intercepts.qmd",),
    ),
    "10-plants-and-series.qmd": _g(
        "advanced",
        "A vector response has several measurements on the same unit. This chapter stays with that vector when every component is binary, so the dependence is among categories rather than among repeated continuous visits.",
        ("09-marginal-models.qmd",),
    ),
    "12-time-series.qmd": _g(
        "advanced",
        "A time series is dependent because it is ordered: today can depend on yesterday. Stationarity is what makes that dependence estimable from a single stretch of time.",
        ("prob-06-markov-chains.qmd", "inf-06-regression.qmd"),
    ),
    "11-forecasting.qmd": _g(
        "advanced",
        "A forecast is a statement about a future stretch that was not used to fit the model. This chapter is the point forecast, the interval around it, and why a seasonal pattern is not the same thing as a trend.",
        ("12-time-series.qmd",),
    ),
    "sl-01-multivariate-normal.qmd": _g(
        "intermediate",
        "Several measurements on the same unit move together, and the covariance says how. The multivariate normal is the distribution fixed by that mean vector and that covariance.",
        ("prob-04-joint-distributions.qmd", "prob-02-random-variables.qmd"),
    ),
    "sl-02-normal-inference.qmd": _g(
        "intermediate",
        "When the population mean and covariance are not given, they are estimated from the sample. This chapter is that estimate and the uncertainty around a normal mean vector.",
        ("sl-01-multivariate-normal.qmd", "inf-02-estimation.qmd"),
    ),
    "sl-03-principal-components.qmd": _g(
        "intermediate",
        "A display in two dimensions has to choose two directions. Principal components choose the directions that keep as much of the sample's variation as possible.",
        ("sl-01-multivariate-normal.qmd",),
    ),
    "sl-04-kmeans.qmd": _g(
        "intermediate",
        "Clustering looks for groups when the group label is hidden. K-means places centres so that each point is near the centre of its own group, and the centres are means of the points assigned to them.",
        ("sl-01-multivariate-normal.qmd",),
    ),
    "sl-05-mixtures-em.qmd": _g(
        "intermediate",
        "A point near a boundary need not belong entirely to one group. A mixture draws a hidden component and then draws the measurements from that component, and EM alternates between those two steps.",
        ("sl-01-multivariate-normal.qmd", "prob-04-joint-distributions.qmd"),
    ),
    "sl-06-model-selection.qmd": _g(
        "intermediate",
        "Training likelihood alone rewards a more flexible model, so the largest model that was tried wins that comparison. This chapter is a penalty, or a held-out check, that can prefer a smaller one.",
        ("sl-05-mixtures-em.qmd",),
    ),
    "sl-07-linkage-and-density.qmd": _g(
        "intermediate",
        "Hierarchical clustering records which groups merge first, instead of forcing one partition. A kernel density estimate turns the same points into a smooth picture of where the sample sits.",
        ("sl-04-kmeans.qmd",),
    ),
    "sl-08-discriminant-analysis.qmd": _g(
        "intermediate",
        "A new unit arrives without a label, and labelled units are available. Discriminant analysis models the measurements inside each class and turns those models into a predicted class.",
        ("sl-01-multivariate-normal.qmd", "sl-02-normal-inference.qmd"),
    ),
    "sl-09-error-rates.qmd": _g(
        "intermediate",
        "The question after a classifier is fit is how often it fails on a new observation. Scoring the same sample that chose the classifier answers a different, easier question.",
        ("sl-08-discriminant-analysis.qmd",),
    ),
    "sl-10-logistic-regression.qmd": _g(
        "intermediate",
        "Logistic regression models the probability of a label given the measurements, instead of modelling the measurements inside each class. A coefficient is a change in log odds, not a change in the probability itself.",
        ("inf-06-regression.qmd", "01-introduction-to-glms.qmd"),
    ),
    "sl-11-nearest-neighbours.qmd": _g(
        "intermediate",
        "Instead of a global boundary, look near the point to be classified and use the labels found there. How many neighbours, and how distance is measured, are the choices that change the rule.",
        ("sl-08-discriminant-analysis.qmd",),
    ),
    "sl-12-classification-trees.qmd": _g(
        "intermediate",
        "A classification tree asks a sequence of questions and sends each unit to a leaf. The questions are chosen to make the leaves purer, and a tree that fits the training sample too closely is then cut back.",
        ("sl-08-discriminant-analysis.qmd",),
    ),
    "sl-13-ensembles.qmd": _g(
        "advanced",
        "If one tree changes when the training sample is perturbed, fit many perturbed trees and combine them. Bagging, random forests, and boosting are three ways to build and combine those trees.",
        ("sl-12-classification-trees.qmd",),
    ),
    "sl-14-neural-units.qmd": _g(
        "advanced",
        "One linear score cannot separate every labelling of a few points. A neural unit passes a linear score through a nonlinear function, and a layer of those units can build a boundary a line cannot.",
        ("sl-10-logistic-regression.qmd",),
    ),
    "sl-15-backpropagation.qmd": _g(
        "advanced",
        "Learning a network means changing the weights to reduce a loss. Backpropagation computes that gradient by the chain rule, from the output back to the earliest weights.",
        ("sl-14-neural-units.qmd",),
    ),
    "sl-16-networks-in-practice.qmd": _g(
        "advanced",
        "The gradient says how to take a step. It does not say which fitted network to keep, how long to train, or how a choice made on the training sample should be scored.",
        ("sl-15-backpropagation.qmd",),
    ),
    "sl-17-support-vectors.qmd": _g(
        "advanced",
        "Several lines can separate two classes perfectly, so training error cannot choose among them. A support vector machine prefers the line with the widest margin, and only the points on that margin determine it.",
        ("sl-08-discriminant-analysis.qmd",),
    ),
    "sl-18-high-dimensional.qmd": _g(
        "advanced",
        "A covariance of four measurements is manageable. Thousands of measurements on a few dozen units is a different problem, because there are more parameters than observations.",
        ("sl-01-multivariate-normal.qmd", "inf-02-estimation.qmd"),
    ),
    "sl-19-graphical-models.qmd": _g(
        "advanced",
        "Two measurements can move together because both track a third. A graph asks which dependences remain after conditioning, and an edge means a dependence that conditioning on the other variables does not remove.",
        ("sl-01-multivariate-normal.qmd", "prob-04-joint-distributions.qmd"),
    ),
}


def validate(filenames: list[str]) -> None:
    """Every chapter has one guide, every prerequisite is a chapter, and the starter path is beginner."""
    missing = [name for name in filenames if name not in GUIDES]
    extra = sorted(name for name in GUIDES if name not in filenames)
    problems: list[str] = []
    if missing:
        problems.append("missing guides: " + ", ".join(missing))
    if extra:
        problems.append("guides for unknown chapters: " + ", ".join(extra))
    for name, guide in GUIDES.items():
        if guide["level"] not in LEVELS:
            problems.append(f"{name}: bad level {guide['level']}")
        summary = guide["summary"].strip()
        if summary.count(".") < 2:
            problems.append(f"{name}: summary should be two sentences")
        if name in guide["needs"]:
            problems.append(f"{name}: lists itself as a prerequisite")
        for need in guide["needs"]:
            if need not in GUIDES:
                problems.append(f"{name}: unknown prerequisite {need}")
    for name in STARTER:
        if name not in GUIDES:
            problems.append(f"starter chapter missing: {name}")
        elif GUIDES[name]["level"] != "beginner":
            problems.append(f"starter chapter {name} is not beginner")
    opening = GUIDES.get("prob-01-experiments.qmd", {})
    note = opening.get("note", "")
    for word in ("densit", "prior", "Bayes"):
        if word not in note:
            problems.append(f"opening chapter note does not mention {word}")
    seen: set[str] = set()

    def walk(name: str, stack: list[str]) -> None:
        if name in stack:
            problems.append("prerequisite cycle: " + " -> ".join(stack + [name]))
            return
        if name in seen or name not in GUIDES:
            return
        seen.add(name)
        for need in GUIDES[name]["needs"]:
            walk(need, stack + [name])

    for name in list(GUIDES):
        walk(name, [])
    if problems:
        raise SystemExit("chapter guides: " + "; ".join(problems[:12]))
