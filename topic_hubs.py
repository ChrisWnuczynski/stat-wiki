"""Curated topic hubs for the homepage library, the topic index, and the sidebar.

Fundamentals is the on-ramp. Probability distributions collects every
distribution article. Standalone fundamentals are articles whose whole text
lives in research/content; they are not copied out of a chapter.
"""

from __future__ import annotations

# Learning order. Existing articles are included; only STANDALONE slugs are new pages.
FUNDAMENTALS_ORDER: list[str] = [
    "data",
    "dataset",
    "variable",
    "levels-of-measurement",
    "population",
    "census",
    "sample",
    "simple-random-sample",
    "designed-experiment",
    "observational-study",
    "summary-statistics",
    "statistic",
    "parameter",
    "estimator",
    "sample-space",
    "event",
    "axioms-of-probability",
    "random-variable",
    "expectation",
    "variance",
    "random-sample",
    "ingredients-of-a-hypothesis-test",
    "confidence-interval",
]

FUNDAMENTALS_GROUPS: list[tuple[str, list[str]]] = [
    ("What is recorded", ["data", "dataset", "variable", "levels-of-measurement"]),
    ("Where the records come from", ["population", "census", "sample", "simple-random-sample", "designed-experiment", "observational-study"]),
    ("Description and a first inference", ["summary-statistics", "statistic", "parameter", "estimator", "ingredients-of-a-hypothesis-test", "confidence-interval"]),
    ("The probability language underneath", ["sample-space", "event", "axioms-of-probability", "random-variable", "expectation", "variance", "random-sample"]),
]

FUNDAMENTALS_INTRO = """
Statistics begins with a record and a question about a larger collection than the record itself. The pages in this topic follow that order. They start from what a measurement is, then from how a collection of measurements is chosen, then from the summaries and the models that turn those measurements into a claim, and only then from the probability that makes the claim precise.

A reader who is new to the subject can follow the groups from top to bottom. Each later page uses the words of the earlier ones. The same pages also sit in the chapters that develop them further: a definition here is the start of an argument, not the whole argument.
""".strip()

DISTRIBUTIONS_INTRO = """
A probability distribution is a rule that assigns chances to the values of a random variable. The cards below are the named families used on this site, grouped by the kind of value they describe. Discrete families put their chance on a list of points. Continuous families spread chance along an interval. Multivariate families describe several values at once. The last group collects the relationships that turn one family into another.

Each card links to the article. The articles keep their place in the chapter that derives them. Their primary listing is this topic. A laboratory draws the mass or density and the distribution function for the univariate families whose formulas are short enough to compute in the browser.
""".strip()

# Distribution articles that are not rows of distributions.json.
DISTRIBUTION_CONCEPTS: list[str] = [
    "discrete-distribution",
    "continuous-distribution",
    "conditional-distribution",
    "sampling-distribution",
    "fat-tails",
    "tail",
    "pearson-distribution",
]

# Related pages listed with the families, without taking the distribution breadcrumb.
DISTRIBUTION_RELATIONS: list[str] = [
    "exponential-family",
    "natural-exponential-family",
    "poisson-limit-of-the-binomial",
    "memoryless-property",
    "the-beta-distribution-is-the-two-category-dirichlet",
    "central-limit-theorem",
]

MULTIVARIATE: set[str] = {
    "dirichlet-distribution",
    "multinomial-distribution",
    "multivariate-normal-distribution",
    "wishart-distribution",
}

# Univariate families the distribution laboratory can draw.
EXPLORER_SLUGS: list[str] = [
    "bernoulli-distribution",
    "binomial-distribution",
    "poisson-distribution",
    "geometric-distribution",
    "uniform-distribution",
    "exponential-distribution",
    "normal-distribution",
    "gamma-distribution",
    "beta-distribution",
    "chi-squared-distribution",
    "student-t-distribution",
    "cauchy-distribution",
    "lognormal-distribution",
    "pareto-distribution",
    "weibull-distribution",
    "f-distribution",
]

STANDALONE: list[dict[str, str]] = [
    {"slug": "data", "term": "Data", "field": "statistics", "article": "", "verb": "are", "description": "measurements or observations collected as a source of information"},
    {"slug": "dataset", "term": "Dataset", "field": "statistics", "article": "a", "verb": "is", "description": "a collection of observations organised so that they can be analysed together"},
    {"slug": "variable", "term": "Variable", "field": "statistics", "article": "a", "verb": "is", "description": "a characteristic that is measured or counted on each unit"},
    {"slug": "levels-of-measurement", "term": "Levels of measurement", "field": "statistics", "article": "", "verb": "are", "description": "the distinctions among names, ranks, and numerical measurements that decide which summaries are meaningful"},
    {"slug": "population", "term": "Population", "field": "statistics", "article": "a", "verb": "is", "description": "the complete collection of units about which a study wants to learn"},
    {"slug": "census", "term": "Census", "field": "statistics", "article": "a", "verb": "is", "description": "a study that observes every unit in a population"},
    {"slug": "sample", "term": "Sample", "field": "statistics", "article": "a", "verb": "is", "description": "a subset of a population, studied in order to say something about the population"},
    {"slug": "parameter", "term": "Parameter", "field": "statistics", "article": "a", "verb": "is", "description": "a numerical feature of a population, as distinct from a statistic computed from a sample"},
    {"slug": "sampling-distribution", "term": "Sampling distribution", "field": "statistical inference", "article": "a", "verb": "is", "description": "the distribution of a statistic across repeated samples from the same population", "topic": "Probability distributions"},
    {"slug": "line-chart", "term": "Line chart", "field": "data analysis", "article": "a", "verb": "is", "description": "a frequency graph that draws a line of height equal to the frequency at each value of a discrete variable", "topic": "Data analysis"},
    {"slug": "abundance-estimation", "term": "Abundance estimation", "field": "ecology", "article": "", "verb": "is", "description": "the estimation of population size from marked and recaptured samples, or from overlapping lists", "topic": "Applications"},
    {"slug": "actuarial-science", "term": "Actuarial science", "field": "insurance and pensions", "article": "", "verb": "is", "description": "the practice of pricing and reserving for uncertain future events, especially lifetimes", "topic": "Applications"},
    {"slug": "apriori-algorithm", "term": "Apriori algorithm", "field": "statistical learning", "article": "the", "verb": "is", "description": "a level-by-level listing of frequent item sets that skips any set with an infrequent subset", "topic": "Statistical learning"},
    {"slug": "astrostatistics", "term": "Astrostatistics", "field": "astronomy", "article": "", "verb": "is", "description": "the statistical reduction of astronomical observations and their comparison with astrophysical models", "topic": "Applications"},
    {"slug": "asymptotic-analysis", "term": "Asymptotic analysis", "field": "statistical inference", "article": "", "verb": "is", "description": "the use of large-sample limits as working approximations to sampling distributions and posteriors", "topic": "Statistical inference"},
    {"slug": "average-treatment-effect", "term": "Average treatment effect", "field": "study design", "article": "an", "verb": "is", "description": "a contrast of mean outcomes under two treatments in a stated population", "topic": "Statistical inference"},
    {"slug": "base-rate", "term": "Base rate", "field": "statistical inference", "article": "the", "verb": "is", "description": "the probability of a condition in the population before a test result is taken into account", "topic": "Statistical inference"},
    {"slug": "bayesian-inference", "term": "Bayesian inference", "field": "Bayesian statistics", "article": "", "verb": "is", "description": "the derivation of a probability distribution for unknowns from a joint model and the observed data", "topic": "Bayesian statistics"},
    {"slug": "bayesian-model", "term": "Bayesian model", "field": "Bayesian statistics", "article": "a", "verb": "is", "description": "a joint probability specification for the observations and the unknowns", "topic": "Bayesian statistics"},
    {"slug": "bayesian-probability", "term": "Bayesian probability", "field": "Bayesian statistics", "article": "", "verb": "is", "description": "probability used as a numerical measure of uncertainty, including uncertainty about single cases and parameters", "topic": "Bayesian statistics"},
    {"slug": "bayesian-statistics", "term": "Bayesian statistics", "field": "statistics", "article": "", "verb": "is", "description": "the discipline that states uncertainty about unknowns as probability and revises it with data", "topic": "Bayesian statistics"},
    {"slug": "biostatistics", "term": "Biostatistics", "field": "medicine", "article": "", "verb": "is", "description": "the application of statistical design and analysis to biological and medical questions", "topic": "Applications"},
    {"slug": "business-analytics", "term": "Business analytics", "field": "management", "article": "", "verb": "is", "description": "the use of data and statistical models to describe, predict, and choose actions in an organisation", "topic": "Applications"},
    {"slug": "case-control-study", "term": "Case-control study", "field": "study design", "article": "a", "verb": "is", "description": "a sample in which people who already have the outcome are included more readily than people who do not", "topic": "Statistical inference"},
    {"slug": "causality", "term": "Causality", "field": "study design", "article": "", "verb": "is", "description": "a contrast between the outcomes of the same units under two actions", "topic": "Statistical inference"},
    {"slug": "censoring-statistics", "term": "Censoring", "field": "survival analysis", "article": "", "verb": "is", "description": "a record in which a lifetime is known only to exceed a time, or to fall inside an interval, rather than known exactly", "topic": "Applications"},
    {"slug": "chemometrics", "term": "Chemometrics", "field": "analytical chemistry", "article": "", "verb": "is", "description": "the use of mathematical and statistical methods to design chemical measurements and to extract chemical information from them", "topic": "Applications"},
    {"slug": "classification", "term": "Classification", "field": "statistical learning", "article": "", "verb": "is", "description": "the prediction of a qualitative response from features, by assigning each case to a class", "topic": "Statistical learning"},
    {"slug": "cluster-analysis", "term": "Cluster analysis", "field": "statistical learning", "article": "", "verb": "is", "description": "the grouping of observations so that members of one group are closer to each other than to members of another group", "topic": "Statistical learning"},
    {"slug": "cohort-study", "term": "Cohort study", "field": "study design", "article": "a", "verb": "is", "description": "a follow-up of a defined group in which exposure is recorded and later outcomes are counted", "topic": "Statistical inference"},
    {"slug": "computational-biology", "term": "Computational biology", "field": "biology", "article": "", "verb": "is", "description": "the development and use of data-analytic, theoretical, and simulation methods to study biological systems", "topic": "Applications"},
    {"slug": "conjoint-analysis", "term": "Conjoint Analysis", "field": "survey measurement", "article": "a", "verb": "is", "description": "a decomposition of overall preference ratings into the contribution of each attribute level", "topic": "Applications"},
    {"slug": "control-group", "term": "Control group", "field": "study design", "article": "a", "verb": "is", "description": "the set of observations that do not receive the experimental treatment", "topic": "Statistical inference"},
    {"slug": "correlation-does-not-imply-causation", "term": "Correlation does not imply causation", "field": "causal inference", "article": "", "verb": "is", "description": "a warning that an observed association is not, by itself, a causal effect", "topic": "Statistical inference"},
    {"slug": "cross-sectional-data", "term": "Cross-sectional data", "field": "correlated data", "article": "", "verb": "are", "description": "observations on many units taken at one time, so each unit contributes a single record", "topic": "Correlated data"},
    {"slug": "data-analysis", "term": "Data analysis", "field": "statistics", "article": "", "verb": "is", "description": "the extraction of structure, summaries and comparisons from observations once they have been arranged in a table", "topic": "Data analysis"},
    {"slug": "data-collection", "term": "Data collection", "field": "statistics", "article": "", "verb": "is", "description": "the decision of which observations are needed and the work of obtaining them", "topic": "Data analysis"},
    {"slug": "data-mining", "term": "Data mining", "field": "statistical learning", "article": "", "verb": "is", "description": "the algorithmic extraction of patterns from large collections of records, as one step in turning those records into usable knowledge", "topic": "Statistical learning"},
    {"slug": "data-quality", "term": "Data quality", "field": "statistics", "article": "", "verb": "is", "description": "the extent to which observations are accurate for the quantities they record and representative for the population they describe", "topic": "Data analysis"},
    {"slug": "data-science", "term": "Data science", "field": "data analysis", "article": "", "verb": "is", "description": "the technical work of learning from data, from preparation and computing through models and the evaluation of tools", "topic": "Applications"},
    {"slug": "data-sharing", "term": "Data sharing", "field": "scientific practice", "article": "", "verb": "is", "description": "the preservation of recorded observations, with the information needed to find and reuse them", "topic": "Applications"},
    {"slug": "decision-problem", "term": "Decision problem", "field": "statistical inference", "article": "a", "verb": "is", "description": "a choice among actions whose uncertain outcomes are scored by a utility or a loss", "topic": "Statistical inference"},
    {"slug": "demography", "term": "Demography", "field": "population studies", "article": "", "verb": "is", "description": "the statistical study of human populations through births, deaths, and migration", "topic": "Applications"},
    {"slug": "difference-in-differences", "term": "Difference in differences", "field": "study design", "article": "", "verb": "are", "description": "a treated group's before-and-after change minus the same change in a comparison group", "topic": "Statistical inference"},
    {"slug": "differential-privacy", "term": "Differential privacy", "field": "privacy", "article": "", "verb": "is", "description": "a promise that the distribution of a released analysis barely changes when one person's data are added or removed", "topic": "Applications"},
    {"slug": "dimensionality-reduction", "term": "Dimensionality reduction", "field": "statistical learning", "article": "", "verb": "is", "description": "the replacement of a long list of measurements by a short list of coordinates that keeps most of their variation or their shape", "topic": "Statistical learning"},
    {"slug": "diversity-index", "term": "Diversity index", "field": "ecology", "article": "a", "verb": "is", "description": "a summary of how individuals are divided among classes, using both the number of classes and their relative sizes", "topic": "Applications"},
    {"slug": "econometrics", "term": "Econometrics", "field": "economics", "article": "", "verb": "is", "description": "the joint study of economic models, statistical methods, and economic data", "topic": "Applications"},
    {"slug": "effect-size", "term": "Effect size", "field": "statistical inference", "article": "an", "verb": "is", "description": "the magnitude of a departure from a null value, kept separate from the probability of detecting it", "topic": "Statistical inference"},
    {"slug": "engineering-statistics", "term": "Engineering statistics", "field": "engineering", "article": "", "verb": "is", "description": "the use of designed experiments, process comparisons, and lifetime data to decide how a product or process should be changed", "topic": "Applications"},
    {"slug": "environmental-statistics", "term": "Environmental statistics", "field": "official statistics", "article": "", "verb": "is", "description": "statistics that describe the state of the environment, the pressures on it, and the responses to those pressures", "topic": "Applications"},
    {"slug": "epidemiology", "term": "Epidemiology", "field": "public health", "article": "", "verb": "is", "description": "the study of how health events are distributed in populations and of what determines that distribution", "topic": "Applications"},
    {"slug": "estimating-equations", "term": "Estimating equations", "field": "statistical inference", "article": "", "verb": "are", "description": "mean-zero restrictions on the data and a parameter, solved in the sample to produce an estimator", "topic": "Statistical inference"},
    {"slug": "estimation-theory", "term": "Estimation theory", "field": "statistical inference", "article": "", "verb": "is", "description": "the study of how a sample is converted into a point or an interval for an unknown population parameter", "topic": "Statistical inference"},
    {"slug": "expected-loss", "term": "Expected loss", "field": "statistical inference", "article": "the", "verb": "is", "description": "the probability-weighted average of a loss, used to rank actions", "topic": "Statistical inference"},
    {"slug": "experimental-error", "term": "Experimental error", "field": "statistical inference", "article": "", "verb": "is", "description": "the part of a measured response traced to influences the experimenter did not control", "topic": "Statistical inference"},
    {"slug": "extrapolation", "term": "Extrapolation", "field": "statistical inference", "article": "an", "verb": "is", "description": "an estimate of a response at an explanatory value outside the observed set", "topic": "Statistical inference"},
    {"slug": "fat-tails", "term": "Fat tails", "field": "probability", "article": "", "verb": "are", "description": "probability farther from the centre than a normal curve places there, as in a kurtosis above 3", "topic": "Probability distributions"},
    {"slug": "feature-selection", "term": "Feature selection", "field": "statistical learning", "article": "", "verb": "is", "description": "the choice of which measured predictors enter a fitted model, with the others left out", "topic": "Statistical learning"},
    {"slug": "federated-learning", "term": "Federated learning", "field": "statistical learning", "article": "", "verb": "is", "description": "training a shared model from records that stay on the devices or at the sites that collected them", "topic": "Statistical learning"},
    {"slug": "first-international-statistical-congress", "term": "First International Statistical Congress", "field": "history of statistics", "article": "the", "verb": "is", "description": "the 1853 Brussels meeting that opened a series of attempts to make national statistics comparable", "topic": "History"},
    {"slug": "foundations-of-statistics", "term": "Foundations of statistics", "field": "statistics", "article": "", "verb": "are", "description": "the ideas that turn incomplete numerical observations into statements about a wider collection of units", "topic": "Applications"},
    {"slug": "frequentist-inference", "term": "Frequentist inference", "field": "statistical inference", "article": "", "verb": "is", "description": "the judging of statistical procedures by how often they succeed across repeated samples", "topic": "Statistical inference"},
    {"slug": "game-of-chance", "term": "Game of chance", "field": "probability", "article": "a", "verb": "is", "description": "a repeatable play with listed outcomes, probabilities, and a numerical payoff", "topic": "History"},
    {"slug": "geostatistics", "term": "Geostatistics", "field": "spatial statistics", "article": "", "verb": "is", "description": "the analysis of measurements that come with locations, used to describe and predict a quantity across space", "topic": "Applications"},
    {"slug": "harking", "term": "HARKing", "field": "study reporting", "article": "", "verb": "is", "description": "the practice of presenting a hypothesis suggested by the results as if it had been stated in advance", "topic": "Statistical inference"},
    {"slug": "harmonic-mean", "term": "Harmonic mean", "field": "data analysis", "article": "the", "verb": "is", "description": "the average that replaces each observation by its reciprocal, then takes the reciprocal of the arithmetic mean of those reciprocals", "topic": "Data analysis"},
    {"slug": "hawthorne-effect", "term": "Hawthorne effect", "field": "study design", "article": "the", "verb": "is", "description": "a change in behaviour that comes from being studied rather than from the condition under test", "topic": "Statistical inference"},
    {"slug": "inference", "term": "Inference", "field": "statistical inference", "article": "", "verb": "is", "description": "reasoning from an observed sample to a quantity that was not measured on the whole population", "topic": "Statistical inference"},
    {"slug": "instrumental-variable", "term": "Instrumental variable", "field": "study design", "article": "an", "verb": "is", "description": "a variable associated with treatment that affects the outcome only through that treatment and shares no causes with the outcome", "topic": "Statistical inference"},
    {"slug": "inverse-probability", "term": "Inverse probability", "field": "probability", "article": "", "verb": "is", "description": "the historical practice of assigning a probability to an unknown given the observations", "topic": "Probability"},
    {"slug": "k-anonymity", "term": "K-anonymity", "field": "privacy", "article": "", "verb": "is", "description": "a requirement that every combination of quasi-identifiers in a released table appears at least k times", "topic": "Applications"},
    {"slug": "kruskal-wallis-test", "term": "Kruskal-Wallis test", "field": "statistical inference", "article": "the", "verb": "is", "description": "a rank test of whether several samples could come from the same continuous distribution", "topic": "Statistical inference"},
    {"slug": "kurtosis", "term": "Kurtosis", "field": "data analysis", "article": "", "verb": "is", "description": "a moment comparison of how much probability sits in the extremes, benchmarked against a normal curve", "topic": "Data analysis"},
    {"slug": "lady-tasting-tea", "term": "Lady tasting tea", "field": "experimental design", "article": "the", "verb": "is", "description": "Fisher's cup experiment for testing a claim to tell whether milk or tea was poured first", "topic": "History"},
    {"slug": "least-absolute-deviations", "term": "Least absolute deviations", "field": "statistical inference", "article": "", "verb": "are", "description": "a regression fit that minimises the sum of absolute residuals and tracks a conditional median", "topic": "Statistical inference"},
    {"slug": "likelihood-ratios-in-diagnostic-testing", "term": "Likelihood ratios in diagnostic testing", "field": "statistical inference", "article": "", "verb": "are", "description": "factors that convert the prior odds of a condition into posterior odds after a test result", "topic": "Statistical inference"},
    {"slug": "machine-learning", "term": "Machine learning", "field": "statistical learning", "article": "", "verb": "is", "description": "the estimation of a prediction or description rule from data, separating error a better rule could remove from error the measured features cannot remove", "topic": "Statistical learning"},
    {"slug": "mathematical-statistics", "term": "Mathematical statistics", "field": "statistical inference", "article": "", "verb": "is", "description": "the mathematical theory of estimating population quantities and of testing claims about them", "topic": "Statistical inference"},
    {"slug": "mean-absolute-percentage-error", "term": "Mean absolute percentage error", "field": "forecasting", "article": "the", "verb": "is", "description": "the average of absolute forecast errors after each error is expressed as a percentage of the observed value", "topic": "Data analysis"},
    {"slug": "measurable-function", "term": "Measurable function", "field": "probability", "article": "a", "verb": "is", "description": "a function for which questions about its values correspond to events, so that expectation is defined", "topic": "Probability"},
    {"slug": "measurement", "term": "Measurement", "field": "statistics", "article": "", "verb": "is", "description": "assignment of a numerical value by a procedure that has a scatter and may sit off the quantity it aims at", "topic": "Data analysis"},
    {"slug": "medical-statistics", "term": "Medical statistics", "field": "medicine", "article": "", "verb": "is", "description": "the application of statistical design and inference to human biology, clinical trials, and medical measurement", "topic": "Applications"},
    {"slug": "misuse-of-statistics", "term": "Misuse of statistics", "field": "statistical interpretation", "article": "", "verb": "is", "description": "a conclusion that the design or the analysis does not support, including selective reporting and over-strong causal readings", "topic": "Applications"},
    {"slug": "morans-i", "term": "Moran's I", "field": "spatial statistics", "article": "", "verb": "is", "description": "an index of whether neighbouring areas have more similar values than a random reassignment of those values", "topic": "Applications"},
    {"slug": "multilevel-model", "term": "Multilevel model", "field": "correlated data", "article": "a", "verb": "is", "description": "a regression that lets coefficients vary across groups, including groups that sit inside other groups", "topic": "Correlated data"},
    {"slug": "multivariate-statistics", "term": "Multivariate statistics", "field": "multivariate data", "article": "", "verb": "is", "description": "the analysis of observations that are vectors of measurements, jointly rather than one coordinate at a time", "topic": "Statistical inference"},
    {"slug": "natural-experiment", "term": "Natural experiment", "field": "study design", "article": "a", "verb": "is", "description": "a comparison that uses a treatment contrast generated outside the study", "topic": "Statistical inference"},
    {"slug": "nonlinear-regression", "term": "Nonlinear regression", "field": "regression", "article": "a", "verb": "is", "description": "a least-squares fit of a mean that is not linear in its unknown coefficients", "topic": "Statistical inference"},
    {"slug": "normalizing-constant", "term": "Normalizing constant", "field": "probability", "article": "a", "verb": "is", "description": "the factor that makes a nonnegative function integrate or sum to one", "topic": "Probability"},
    {"slug": "official-statistics", "term": "Official statistics", "field": "public statistics", "article": "", "verb": "is", "description": "statistics compiled and published by a state statistical agency about the population, the economy, and society", "topic": "Applications"},
    {"slug": "open-science", "term": "Open science", "field": "scientific method", "article": "", "verb": "is", "description": "the practice of making data, code, materials, and study plans available so that results can be checked and repeated", "topic": "Applications"},
    {"slug": "panel-data", "term": "Panel data", "field": "correlated data", "article": "", "verb": "are", "description": "repeated observations of the same units, so each record has both a unit and a time", "topic": "Correlated data"},
    {"slug": "parametric-statistics", "term": "Parametric statistics", "field": "statistical inference", "article": "", "verb": "are", "description": "procedures that assume a model with a finite list of unknown constants and then estimate those constants from the sample", "topic": "Statistical inference"},
    {"slug": "pattern-recognition", "term": "Pattern recognition", "field": "classification", "article": "", "verb": "is", "description": "the construction of rules that assign feature vectors to classes, or that describe those vectors when no class is given", "topic": "Applications"},
    {"slug": "pearson-distribution", "term": "Pearson distribution", "field": "probability", "article": "a", "verb": "is", "description": "a frequency curve whose logarithmic slope, at the mode, is minus the abscissa divided by a quadratic", "topic": "Probability distributions"},
    {"slug": "philosophy-of-statistics", "term": "Philosophy of statistics", "field": "statistics", "article": "", "verb": "are", "description": "questions about what a statistical conclusion assumes and what it is entitled to mean", "topic": "Applications"},
    {"slug": "polynomial-least-squares", "term": "Polynomial least squares", "field": "regression", "article": "", "verb": "are", "description": "estimates of a polynomial mean obtained by minimising squared residuals", "topic": "Statistical inference"},
    {"slug": "posterior-probability", "term": "Posterior probability", "field": "Bayesian statistics", "article": "a", "verb": "is", "description": "the probability of an event about an unknown after the data have been taken into account", "topic": "Bayesian statistics"},
    {"slug": "probability-interpretations", "term": "Probability interpretations", "field": "probability", "article": "", "verb": "are", "description": "accounts of what a probability number means, among ratios of cases, long-run frequencies, and degrees of uncertainty", "topic": "Probability"},
    {"slug": "probability-theory", "term": "Probability theory", "field": "mathematics", "article": "", "verb": "is", "description": "the mathematical study of outcomes, events, and the limit behaviour of random quantities", "topic": "Probability"},
    {"slug": "psychological-statistics", "term": "Psychological statistics", "field": "psychology", "article": "", "verb": "is", "description": "the design and analysis of studies of behaviour, perception, and mental measurement", "topic": "Applications"},
    {"slug": "public-health", "term": "Public health", "field": "population health", "article": "", "verb": "is", "description": "the study of how illness and its exposures are distributed in populations, and of the rates used to describe them", "topic": "Applications"},
    {"slug": "quality-control", "term": "Quality control", "field": "industrial statistics", "article": "", "verb": "is", "description": "the use of sampling, control charts, and experiments to keep a product or process within its specification", "topic": "Applications"},
    {"slug": "random-error", "term": "Random error", "field": "measurement", "article": "a", "verb": "is", "description": "a chance deviation that scatters from one repeated measurement to the next", "topic": "Statistical inference"},
    {"slug": "ranking", "term": "Ranking", "field": "data analysis", "article": "", "verb": "is", "description": "the replacement of each observation by its place in the ordered sample, with average places for ties", "topic": "Data analysis"},
    {"slug": "raw-data", "term": "Raw data", "field": "statistics", "article": "", "verb": "is", "description": "observations as recorded, before they are replaced by fewer summary numbers", "topic": "Data analysis"},
    {"slug": "regression-analysis", "term": "Regression analysis", "field": "regression", "article": "", "verb": "is", "description": "the estimation of how a response moves with one or more predictors, together with the reliability of that estimate", "topic": "Statistical inference"},
    {"slug": "replication-crisis", "term": "Replication crisis", "field": "scientific method", "article": "the", "verb": "is", "description": "the recognition that many published findings do not reappear when a study is repeated with new data", "topic": "Applications"},
    {"slug": "reproducibility", "term": "Reproducibility", "field": "scientific method", "article": "", "verb": "is", "description": "the property that a result can be regenerated from the same data and code, or, in another usage, recovered in a new study", "topic": "Applications"},
    {"slug": "resampling-statistics", "term": "Resampling (statistics)", "field": "statistical inference", "article": "", "verb": "is", "description": "the practice of drawing further samples from the observed sample and refitting a statistic on each draw", "topic": "Statistical inference"},
    {"slug": "risk-assessment", "term": "Risk assessment", "field": "applied probability", "article": "", "verb": "is", "description": "the estimation of the probability of a harmful event, such as disease in a population or a false alarm on a control chart", "topic": "Applications"},
    {"slug": "robust-statistics", "term": "Robust statistics", "field": "statistical inference", "article": "", "verb": "are", "description": "summaries and fits that barely move when a small fraction of the data is moved a long way", "topic": "Statistical inference"},
    {"slug": "rounding", "term": "Rounding", "field": "data analysis", "article": "", "verb": "is", "description": "the replacement of a calculated value by a nearby multiple of a reporting unit, such as the nearest integer", "topic": "Data analysis"},
    {"slug": "sampling", "term": "Sampling", "field": "study design", "article": "", "verb": "is", "description": "selection of part of a population, study of that part, and inference back to the population", "topic": "Data analysis"},
    {"slug": "scientific-control", "term": "Scientific control", "field": "study design", "article": "", "verb": "is", "description": "the practice of assigning treatments, holding other conditions fixed, and keeping an untreated comparison", "topic": "Statistical inference"},
    {"slug": "secondary-data", "term": "Secondary data", "field": "statistics", "article": "", "verb": "is", "description": "records made for another purpose and later used again", "topic": "Data analysis"},
    {"slug": "social-statistics", "term": "Social statistics", "field": "social science", "article": "", "verb": "is", "description": "the measurement of social structure and behaviour, from employment and education to households and participation", "topic": "Applications"},
    {"slug": "spatial-analysis", "term": "Spatial analysis", "field": "spatial data", "article": "", "verb": "is", "description": "the statistical treatment of observations that carry locations and of the dependence between neighbours", "topic": "Applications"},
    {"slug": "spearman-s-rank-correlation-coefficient", "term": "Spearman's rank correlation coefficient", "field": "statistics", "article": "the", "verb": "is", "description": "a measure of agreement between two rankings, on a scale from -1 to +1", "topic": "Data analysis"},
    {"slug": "statistical-consultant", "term": "Statistical consultant", "field": "statistical practice", "article": "a", "verb": "is", "description": "a practitioner who advises a client on the design, analysis, or interpretation of data", "topic": "Applications"},
    {"slug": "statistical-dispersion", "term": "Statistical dispersion", "field": "data analysis", "article": "", "verb": "is", "description": "the family of summaries that measure how far observations sit from a centre, or how far the extremes sit from each other", "topic": "Data analysis"},
    {"slug": "statistical-graphics", "term": "Statistical graphics", "field": "data analysis", "article": "", "verb": "are", "description": "plots that show the shape, the spread and the unusual points of a data set", "topic": "Data analysis"},
    {"slug": "statistical-learning-theory", "term": "Statistical learning theory", "field": "statistical learning", "article": "", "verb": "is", "description": "the study of how well a rule fitted on one sample predicts a new case, including the role of the richness of the class of rules", "topic": "Statistical inference"},
    {"slug": "statistical-literacy", "term": "Statistical literacy", "field": "statistics education", "article": "", "verb": "is", "description": "the ability to judge whether a published statistical claim follows from the study and the analysis that produced it", "topic": "Applications"},
    {"slug": "statistical-mechanics", "term": "Statistical mechanics", "field": "statistical physics", "article": "", "verb": "describe", "description": "the macroscopic behaviour of many-particle systems by probability distributions on their microscopic states", "topic": "Applications"},
    {"slug": "statistical-model", "term": "Statistical model", "field": "statistics", "article": "a", "verb": "is", "description": "a mathematical statement relating variables, usually with a random remainder", "topic": "Statistical inference"},
    {"slug": "statistical-process-control", "term": "Statistical process control", "field": "industrial statistics", "article": "", "verb": "is", "description": "the monitoring of a process with control charts so that a real change is distinguished from ordinary variation", "topic": "Applications"},
    {"slug": "statistical-survey", "term": "Statistical survey", "field": "study design", "article": "a", "verb": "is", "description": "an inquiry that puts the same questions to a selected part of a population and generalises", "topic": "Data analysis"},
    {"slug": "statistical-theory", "term": "Statistical theory", "field": "statistical inference", "article": "", "verb": "is", "description": "the mathematical account of how estimators, tests, and prediction rules behave when the data are random", "topic": "Statistical inference"},
    {"slug": "statistician", "term": "Statistician", "field": "history of statistics", "article": "a", "verb": "is", "description": "a person who collects numerical data and turns them into summaries and inferences other people can use", "topic": "Applications"},
    {"slug": "statistics-education", "term": "Statistics education", "field": "teaching", "article": "", "verb": "is", "description": "the design and teaching of statistical thinking, from school courses through the first university course in statistics", "topic": "Applications"},
    {"slug": "structural-equation-modelling", "term": "Structural equation modelling", "field": "multivariate models", "article": "", "verb": "is", "description": "a family of models that combine directed relations among variables with latent variables measured by observed indicators", "topic": "Statistical inference"},
    {"slug": "supervised-learning", "term": "Supervised learning", "field": "statistical learning", "article": "", "verb": "is", "description": "the fitting of a rule that predicts an observed outcome from features, using cases in which both were recorded", "topic": "Statistical learning"},
    {"slug": "survey-methodology", "term": "Survey methodology", "field": "study design", "article": "", "verb": "is", "description": "the design of questions, selection, and follow-up for an inquiry addressed to selected people", "topic": "Data analysis"},
    {"slug": "survival-analysis", "term": "Survival analysis", "field": "event times", "article": "", "verb": "is", "description": "the analysis of the time until an event when some times are only known to exceed the last observation", "topic": "Statistical inference"},
    {"slug": "system-of-national-accounts", "term": "System of national accounts", "field": "economic statistics", "article": "the", "verb": "describe", "description": "an agreed set of macroeconomic accounts for production, income, and transactions", "topic": "Applications"},
    {"slug": "systematic-error", "term": "Systematic error", "field": "measurement", "article": "a", "verb": "is", "description": "a shift, from a consistent cause, that falls in the same direction on every repeat", "topic": "Statistical inference"},
    {"slug": "systematic-sampling", "term": "Systematic sampling", "field": "study design", "article": "", "verb": "is", "description": "selection at a fixed interval through an ordered list, after a random start", "topic": "Data analysis"},
    {"slug": "tail", "term": "Tail", "field": "probability", "article": "a", "verb": "is", "description": "the probability beyond a cutoff, or the direction in which a histogram decays slowly", "topic": "Probability distributions"},
    {"slug": "true-value", "term": "True value", "field": "statistics", "article": "the", "verb": "is", "description": "the quantity that a measurement or an estimate is trying to recover", "topic": "Data analysis"},
    {"slug": "uncertainty", "term": "Uncertainty", "field": "statistics", "article": "", "verb": "is", "description": "a quantitative account of what remains unknown after the observations and the model are taken into account", "topic": "Statistical inference"},
    {"slug": "unsupervised-learning", "term": "Unsupervised learning", "field": "statistical learning", "article": "", "verb": "is", "description": "the description of how features are arranged when no outcome was recorded to score a prediction", "topic": "Statistical learning"},
    {"slug": "standard-score", "term": "Standard score", "field": "data analysis", "article": "a", "verb": "is", "description": "an observation recentred by a mean and scaled by a standard deviation", "topic": "Data analysis"},
    {"slug": "test-statistic", "term": "Test statistic", "field": "statistical inference", "article": "a", "verb": "is", "description": "a function of the sample used to decide whether a stated hypothesis is rejected", "topic": "Statistical inference"},
]


def standalone_slugs() -> set[str]:
    return {row["slug"] for row in STANDALONE}


def distribution_page_slugs(distribution_keys: list[str]) -> list[str]:
    """Every distribution article, in catalogue order, then the concept pages."""
    return list(distribution_keys) + [slug for slug in DISTRIBUTION_CONCEPTS if slug not in distribution_keys]


def is_distribution_page(slug: str, distribution_keys) -> bool:
    return slug in set(distribution_keys) or slug in DISTRIBUTION_CONCEPTS


def distribution_groups(distribution_items: list[tuple[str, dict]]) -> list[tuple[str, list[str]]]:
    discrete, continuous, multivariate = [], [], []
    for slug, facts in distribution_items:
        if slug in MULTIVARIATE:
            multivariate.append(slug)
        elif facts.get("kind") == "discrete":
            discrete.append(slug)
        else:
            continuous.append(slug)
    return [
        ("Discrete distributions", discrete),
        ("Continuous distributions", continuous),
        ("Multivariate distributions", multivariate),
        ("What a distribution is", list(DISTRIBUTION_CONCEPTS)),
        ("Families and relationships", list(DISTRIBUTION_RELATIONS)),
    ]
