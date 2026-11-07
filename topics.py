"""Topic pages, other names, and extra term links.

Every heading in a chapter gets a page of its own: build_wiki.py copies the
section's text onto it and puts a "Main article" line under the heading. This
file holds what the build cannot work out for itself.

TITLES    A page title for a heading whose own words need its chapter to make
          sense ("The ingredients" becomes "Ingredients of a hypothesis test").
          Two headings given the same title share one page, with both texts.
SAME_AS   Headings that are the same idea as an existing article. They get a
          "Main article" line pointing there instead of a page of their own.
TOPICS    Ideas the chapters name inside a paragraph. Each gets a page with a
          short lead and the paragraphs that discuss it. A topic with the same
          title as a heading's page adds its lead and links to that page.
ALIASES   Other names for an existing page. Each becomes a redirect.
RELATED   Pages on one idea in different parts, listed under each other's
          See also.
LINKS     Phrases to link beyond the topic names, tried in this order before
          the build's own term list (LINKS_LAST after it).

A place in a chapter is written "file#anchor" for a heading, or
"file: phrase" for the paragraph that first contains the phrase.
"""

import re

# Part names, as in build_wiki.PARTS.
P, SP, I, D = "Probability", "Stochastic processes", "Statistical inference", "Data analysis"
B, G, S, L = "Bayesian statistics", "Generalised linear models", "Smoothing", "Statistical learning"
C, T = "Correlated data", "Time series"


def phrase_regex(phrase: str) -> str:
    """A plain phrase as a pattern: either dash or a space between words, either
    apostrophe, and an optional plural. A phrase that starts "re:" is a pattern."""
    if phrase.startswith("re:"):
        return phrase[3:]
    if re.search(r"[\[\]()?|\\*+]", phrase):
        return phrase  # already a pattern, such as "Wald tests?"
    out = re.escape(phrase)
    out = out.replace(r"\ ", "[- ]").replace(r"\-", "[- ]?").replace("–", "(?:--|–|-)").replace("'", "['’]?")
    if not re.search(r"(s|[A-Z])$", phrase) and phrase[-1].isalpha():
        out += "(?:s|es)?"
    return out


def link(phrases, target, scope=None, exclude=()):
    """A term link. target is "slug" (an article or topic page), "CODE" (a
    chapter), or "CODE#Heading text" (a heading in a chapter)."""
    pattern = "|".join(phrase_regex(p) for p in ([phrases] if isinstance(phrases, str) else phrases))
    if "#" in target:
        code, key = target.split("#", 1)
    elif re.fullmatch(r"[A-Z]+\d+", target):
        code, key = target, ""
    else:
        code, key = "ART", target
    return (pattern, code, key, set(scope) if scope else None, set(exclude))


def topic(term, home, lead, also=(), links=(), scope=None, exclude=(), late=False):
    return {
        "term": term,
        "home": home,
        "lead": lead.strip(),
        "also": list(also),
        "links": list(links),
        "scope": set(scope) if scope else None,
        "exclude": set(exclude),
        "late": late,
    }



# ---------------------------------------------------------------------------
# Titles for headings that need their chapter to make sense. Headings given
# the same title share a page.
# ---------------------------------------------------------------------------

_TITLES = """
01-introduction-to-glms.qmd#s-binary-responses | Binary responses in a GLM
01-introduction-to-glms.qmd#s-clotting-times | Clotting-time data
01-introduction-to-glms.qmd#s-disease-and-cholesterol | Cholesterol and heart disease
01-introduction-to-glms.qmd#s-the-cholesterol-fit | Cholesterol and heart disease
01-introduction-to-glms.qmd#s-maximum-likelihood-and-fisher-scoring | Maximum likelihood in a GLM
01-introduction-to-glms.qmd#s-three-links | Logit, probit and complementary log-log links
01-introduction-to-glms.qmd#s-what-the-software-prints | Reading glm output in R
01-introduction-to-glms.qmd#s-the-normal-distribution | Normal distribution as an exponential family
01-introduction-to-glms.qmd#s-the-poisson-distribution | Poisson distribution as an exponential family
01-introduction-to-glms.qmd#s-the-binomial-distribution | Binomial distribution as an exponential family
02-inference-and-counts.qmd#s-binomial-counts | Binomial counts in a GLM
02-inference-and-counts.qmd#s-cholesterol-with-standard-errors | Cholesterol and heart disease
02-inference-and-counts.qmd#s-counts | Count responses
02-inference-and-counts.qmd#s-mine-injuries | Mine-injury data
02-inference-and-counts.qmd#s-two-models-with-a-real-distribution | Count models beyond the Poisson
03-gamma-and-quasi.qmd#s-clotting-times-three-ways | Clotting-time data
03-gamma-and-quasi.qmd#s-leaf-blotch | Leaf-blotch data
03-gamma-and-quasi.qmd#s-positive-continuous-responses | Positive continuous responses
04-categorical-responses.qmd#s-addiction-categories | Addiction data
04-categorical-responses.qmd#s-nominal-categories | Nominal responses
04-categorical-responses.qmd#s-ordinal-data-built-from-binary-splits | Ordinal responses
05-comparisons-and-deviance.qmd#s-reading-the-addiction-model | Addiction data
05-comparisons-and-deviance.qmd#s-bradley-terry | Bradley–Terry model
05-comparisons-and-deviance.qmd#s-residuals-are-not | Residuals in a GLM
06-smooth-means.qmd#s-a-roughness-penalty | Roughness penalty
06-smooth-means.qmd#s-kyphosis-and-age | Kyphosis data
06-smooth-means.qmd#s-lidar | Lidar data
08-random-intercepts.qmd#s-a-random-intercept | Random intercept model
08-random-intercepts.qmd#s-what-is-fixed-and-what-is-random | Fixed and random effects
08-slopes-and-glmms.qmd#s-a-bernoulli-response | Generalised linear mixed model
08-slopes-and-glmms.qmd#s-a-slope-that-belongs-to-the-block | Random slopes
08-slopes-and-glmms.qmd#s-sleep-deprivation | Sleep-deprivation data
09-marginal-models.qmd#s-the-average-and-the-person | Marginal and conditional effects
09-marginal-models.qmd#s-warp-breaks | Warp-breaks data
11-forecasting.qmd#s-accidental-deaths | Accidental-deaths data
11-forecasting.qmd#s-a-hundred-minutes-of-traffic | Traffic data
12-time-series.qmd#s-stationarity | Stationarity of a time series
bayes-01-foundations.qmd#s-what-is-random | What is random in Bayesian inference
bayes-02-beta-binomial.qmd#s-conjugate-update-with-every-constant-shown | Beta–Binomial conjugate update
bayes-02-beta-binomial.qmd#s-numerical-example-five-future-tosses | Five future tosses
bayes-02-beta-binomial.qmd#s-worked-prior-sensitivity-calculation | Prior sensitivity
bayes-03-normal-models.qmd#s-unknown-mean-known-variance | Normal mean with known variance
bayes-03-normal-models.qmd#s-unknown-variance-known-mean | Normal variance with known mean
bayes-04-mcmc.qmd#s-metropolis-hastings | Metropolis–Hastings algorithm
bayes-04-mcmc.qmd#s-normal-mean-and-variance-example | Gibbs sampler for a normal mean and variance
bayes-04-mcmc.qmd#s-a-four-state-random-walk | Four-state random walk
bayes-05-categorical.qmd#s-moments-and-the-mode | Moments and mode of the Dirichlet
bayes-06-testing.qmd#s-posterior-odds-and-bayes-factors | Bayes factors and posterior odds
bayes-08-hierarchy.qmd#s-a-first-hierarchy-tg5-cattle-studies | TG5 cattle studies
bayes-08-hierarchy.qmd#s-rat-tumours-why-a-hierarchy | Rat-tumour data
bayes-09-linear-regression.qmd#s-worked-regression-example | Eight-point Bayesian regression
da-02-descriptive-statistics.qmd#s-the-table | Data table
da-02-descriptive-statistics.qmd#s-transformations | Transformations of data
da-08-linear-model-examples.qmd#s-transformations | Transformations of data
da-03-using-r.qmd#s-data-frames | Data frames in R
da-03-using-r.qmd#s-values-vectors-and-assignment | Vectors and assignment in R
da-03-using-r.qmd#s-plots-and-model-fits | Plots and model fits in R
da-04-estimation-examples.qmd#s-large-samples | Large-sample intervals
da-04-estimation-examples.qmd#s-proportions | Intervals for proportions
da-06-anova-examples.qmd#s-checking-the-model | Checking an analysis-of-variance model
da-06-anova-examples.qmd#s-two-factors | Two-factor analysis of variance
da-06-anova-examples.qmd#s-one-factor | One-factor analysis of variance
da-07-regression-examples.qmd#s-checking-the-assumptions | Checking regression assumptions
da-07-regression-examples.qmd#s-one-explanatory-variable | Regression with one explanatory variable
da-07-regression-examples.qmd#s-several-explanatory-variables | Regression with several explanatory variables
da-08-linear-model-examples.qmd#s-birth-weight | Birth-weight data
da-08-linear-model-examples.qmd#s-checking-the-final-model | Checking a linear model
da-09-chi-square-examples.qmd#s-seeing-the-approximation | Seeing the chi-squared approximation
inf-01-statistical-inference.qmd#s-a-running-example-milk-cartons | Milk-carton example
inf-01-statistical-inference.qmd#s-what-the-rest-of-this-section-does | Overview of statistical inference
inf-02-estimation.qmd#s-binomial | Maximum likelihood for a binomial proportion
inf-02-estimation.qmd#s-normal | Maximum likelihood for a normal sample
inf-03-confidence-intervals.qmd#s-a-difference-of-means | Interval for a difference of means
inf-03-confidence-intervals.qmd#s-a-proportion | Interval for a proportion
inf-03-confidence-intervals.qmd#s-a-ratio-of-variances | Interval for a ratio of variances
inf-03-confidence-intervals.qmd#s-a-variance | Interval for a normal variance
inf-03-confidence-intervals.qmd#s-coverage | Coverage
inf-03-confidence-intervals.qmd#s-how-large-a-sample | Sample size for a confidence interval
inf-03-confidence-intervals.qmd#s-one-normal-sample | Intervals for one normal sample
inf-03-confidence-intervals.qmd#s-two-normal-samples | Intervals for two normal samples
inf-04-hypothesis-tests.qmd#s-one-proportion | Test for one proportion
inf-04-hypothesis-tests.qmd#s-tests-and-intervals | Tests and confidence intervals
inf-04-hypothesis-tests.qmd#s-the-eight-steps | Eight steps of a hypothesis test
inf-04-hypothesis-tests.qmd#s-the-ingredients | Ingredients of a hypothesis test
inf-04-hypothesis-tests.qmd#s-two-samples | Two-sample tests
inf-05-chi-square.qmd#s-estimated-parameters | Chi-squared test with estimated parameters
inf-05-chi-square.qmd#s-known-cell-probabilities | Chi-squared test with known cell probabilities
inf-06-regression.qmd#s-a-bivariate-normal-sample | Correlation in a bivariate normal sample
inf-07-anova.qmd#s-blocks | Blocks in analysis of variance
inf-07-anova.qmd#s-one-factor | One-factor analysis of variance
inf-07-anova.qmd#s-two-treatments-the-paired-t-test | Paired t test as a block design
prob-01-experiments.qmd#s-probability | Axioms of probability
prob-02-random-variables.qmd#s-bernoulli-and-binomial | Bernoulli and binomial distributions
prob-02-random-variables.qmd#s-gamma-and-chi-squared | Gamma and chi-squared distributions
prob-02-random-variables.qmd#s-transforms | Generating functions
prob-05-transforms-and-limits.qmd#s-one-variable-and-a-sum | Distribution of a function or a sum
prob-06-markov-chains.qmd#s-simulation | Simulating a Markov chain
prob-07-reliability.qmd#s-lifetimes | Lifetimes of systems
prob-07-reliability.qmd#s-structure | Structure of a system
sl-01-multivariate-normal.qmd#s-one-species-or-three | Iris: one species or three
sl-01-multivariate-normal.qmd#s-the-normal-density | Multivariate normal density
sl-02-normal-inference.qmd#s-a-confidence-region-for-the-mean | Confidence region for a normal mean vector
sl-02-normal-inference.qmd#s-a-joint-mean-test-for-setosa | Joint mean test for setosa
sl-02-normal-inference.qmd#s-confidence-statements | Simultaneous confidence statements
sl-02-normal-inference.qmd#s-the-mean | Maximum likelihood for a normal mean vector
sl-02-normal-inference.qmd#s-the-covariance-and-the-invariance-lemma | Maximum likelihood for a covariance matrix
sl-02-normal-inference.qmd#s-the-likelihood-of-a-normal-sample | Likelihood of a multivariate normal sample
sl-02-normal-inference.qmd#s-hypotheses-and-the-likelihood-ratio | Hotelling's T² as a likelihood-ratio test
sl-02-normal-inference.qmd#s-the-two-sample-test | Two-sample Hotelling T² test
sl-02-normal-inference.qmd#s-the-univariate-test-as-a-template | Univariate t test as a template for T²
sl-03-principal-components.qmd#s-choosing-components | Choosing the number of principal components
sl-03-principal-components.qmd#s-derivation-by-lagrange-multipliers | Principal components by Lagrange multipliers
sl-03-principal-components.qmd#s-reconstruction | Reconstruction from principal components
sl-04-kmeans.qmd#s-initialisation-and-restarts | Initialising k-means
sl-04-kmeans.qmd#s-the-criterion | K-means criterion
sl-04-kmeans.qmd#s-voronoi-geometry | Voronoi tessellation
sl-05-mixtures-em.qmd#s-iris-membership | Iris mixture membership
sl-05-mixtures-em.qmd#s-pathologies-and-practical-advice | Pathologies of mixture likelihoods
sl-05-mixtures-em.qmd#s-uncertainty-about-the-parameters | Uncertainty about mixture parameters
sl-06-model-selection.qmd#s-bayes-factors-and-posterior-odds | Bayes factors and posterior odds
sl-06-model-selection.qmd#s-laplace-approximation-of-the-integral | Laplace approximation
sl-06-model-selection.qmd#s-make-the-bic-convention-explicit | BIC sign conventions
sl-06-model-selection.qmd#s-reading-the-criterion | Reading the BIC
sl-06-model-selection.qmd#s-the-kullback-leibler-connection | Kullback–Leibler divergence
sl-08-discriminant-analysis.qmd#s-posterior-probabilities-and-the-bayes-rule | Bayes classifier
sl-08-discriminant-analysis.qmd#s-the-discriminant-boundary | LDA decision boundary
sl-08-discriminant-analysis.qmd#s-unequal-costs | Classification with unequal costs
sl-09-error-rates.qmd#s-choosing-an-estimator | Choosing an error-rate estimator
sl-10-logistic-regression.qmd#s-logistic-and-probit | Logistic and probit models
sl-10-logistic-regression.qmd#s-more-than-two-classes | Multinomial logistic regression
sl-10-logistic-regression.qmd#s-score-and-hessian | Score and Hessian of logistic regression
sl-11-nearest-neighbours.qmd#s-distance-and-scale | Distance and scale in nearest neighbours
sl-12-classification-trees.qmd#s-building-a-tree | Building a classification tree
sl-12-classification-trees.qmd#s-controlling-the-size | Tree size and pruning
sl-13-ensembles.qmd#s-an-error-decomposition-for-regression | Ensemble error decomposition
sl-13-ensembles.qmd#s-the-three-free-quantities | Random-forest tuning parameters
sl-13-ensembles.qmd#s-the-weight-update-is-a-stagewise-step | AdaBoost as forward stagewise fitting
sl-14-neural-units.qmd#s-a-hidden-layer | Hidden layer
sl-14-neural-units.qmd#s-approximation-on-a-cube | Universal approximation
sl-14-neural-units.qmd#s-names-used-from-here-on | Neural-network terminology
sl-14-neural-units.qmd#s-the-unit | Neural unit
sl-14-neural-units.qmd#s-what-one-threshold-unit-can-separate | Linear separability
sl-14-neural-units.qmd#s-what-still-has-to-be-chosen | Choices in a neural network
sl-14-neural-units.qmd#s-where-the-calculation-came-from | History of the neural unit
sl-14-neural-units.qmd#s-why-a-single-unit-cannot-compute-xor | XOR problem
sl-14-neural-units.qmd#s-with-a-bias | Threshold unit with a bias
sl-14-neural-units.qmd#s-without-a-bias | Threshold unit without a bias
sl-15-backpropagation.qmd#s-the-error | Training error of a network
sl-15-backpropagation.qmd#s-the-delta-form | Delta rule
sl-15-backpropagation.qmd#s-behaviour-on-xor | Backpropagation on XOR
sl-16-networks-in-practice.qmd#s-applications | Applications of neural networks
sl-16-networks-in-practice.qmd#s-a-variance-argument | Variance argument for weight initialisation
sl-16-networks-in-practice.qmd#s-generalisation | Generalisation of a network
sl-16-networks-in-practice.qmd#s-preparing-the-data | Preparing data for a network
sl-17-support-vectors.qmd#s-the-hard-margin-quadratic-programme | Hard-margin support vector machine
sl-17-support-vectors.qmd#s-the-nonlinear-programme | Kernel support vector machine
sl-17-support-vectors.qmd#s-what-the-multipliers-say | Support vectors and their multipliers
sl-18-high-dimensional.qmd#s-choosing | Choosing the lasso penalty
sl-18-high-dimensional.qmd#s-extensions | Extensions of the lasso
sl-18-high-dimensional.qmd#s-principal-components-of-the-matrix | Principal components of the colon-cancer matrix
sl-18-high-dimensional.qmd#s-regression | Regression when p > n
sl-18-high-dimensional.qmd#s-the-alon-colon-cancer-matrix | Alon colon-cancer data
sl-18-high-dimensional.qmd#s-what-the-question-is | Questions to ask of high-dimensional data
sl-18-high-dimensional.qmd#s-where-the-columns-come-from | Where high-dimensional columns come from
sl-19-graphical-models.qmd#s-choosing-edges | Choosing graph edges
sl-19-graphical-models.qmd#s-the-constrained-likelihood | Constrained likelihood for a graph
sl-19-graphical-models.qmd#s-the-log-density | Log density of a Gaussian graphical model
sl-19-graphical-models.qmd#s-solving-by-regression | Fitting a graph by regression
sp-01-stochastic-processes.qmd#s-a-modelling-checklist | Modelling checklist for a stochastic process
sp-01-stochastic-processes.qmd#s-a-small-toolkit | Toolkit for stochastic processes
sp-01-stochastic-processes.qmd#s-the-object-being-modelled | What a stochastic process models
sp-02-branching.qmd#s-definition-and-the-probability-generating-function | Galton–Watson process
sp-02-branching.qmd#s-extinction-as-a-fixed-point | Extinction probability
sp-03-random-walks.qmd#s-accumulation-and-scale | Drift and scale of a random walk
sp-03-random-walks.qmd#s-expected-duration | Expected duration of a random walk
sp-04-discrete-markov.qmd#s-hitting-questions-use-the-same-principle | Hitting probabilities
sp-04-discrete-markov.qmd#s-transition-rules | Transition matrix
sp-05-classes-and-reversibility.qmd#s-communication-and-closed-classes | Communicating classes
sp-06-poisson-processes.qmd#s-a-poisson-process-in-the-plane | Spatial Poisson process
sp-06-poisson-processes.qmd#s-changing-rates | Nonhomogeneous Poisson process
sp-06-poisson-processes.qmd#s-forward-equations-and-a-rare-event-limit | Forward equations of the Poisson process
sp-06-poisson-processes.qmd#s-homogeneous-counts-and-waiting-times | Counts and waiting times of a Poisson process
sp-07-continuous-markov.qmd#s-building-a-sample-path | Simulating a continuous-time Markov chain
sp-07-continuous-markov.qmd#s-evolution-equations | Kolmogorov forward and backward equations
sp-07-continuous-markov.qmd#s-stationarity-balance-and-recurrence | Stationarity in continuous time
sp-07-continuous-markov.qmd#s-the-two-state-chain | Two-state continuous-time chain
sp-08-queues.qmd#s-a-repair-model | Machine-repair model
sp-08-queues.qmd#s-one-server-m-m-1 | M/M/1 queue
sp-08-queues.qmd#s-several-servers-and-a-finite-waiting-room | Multi-server and finite-capacity queues
sp-08-queues.qmd#s-unlimited-servers-m-m | M/M/∞ queue
sp-09-probability-spaces.qmd#s-countable-operations-on-a-sequence-of-events | Limits of sequences of events
sp-11-convergence.qmd#s-four-modes | Four modes of convergence
sp-11-convergence.qmd#s-inequalities-and-passing-a-limit-inside-the-expectation | Inequalities and limits under the expectation
sp-12-extremes.qmd#s-three-tails | Three tail types for maxima
sp-12-extremes.qmd#s-what-the-classification-says | Extreme-value classification
"""
TITLES = dict(tuple(x.strip() for x in line.split("|")) for line in _TITLES.strip().splitlines())

# Headings that are an existing article under another name.
SAME_AS = {
    "01-introduction-to-glms.qmd#s-mean-and-variance": "mean-and-variance-of-an-exponential-family",
    "bayes-01-foundations.qmd#s-prior-predictive-and-posterior-predictive-distributions": "prior-and-posterior-predictive-distributions",
    "prob-01-experiments.qmd#s-independence": "independent-events",
    "prob-02-random-variables.qmd#s-exponential": "exponential-distribution",
    "prob-02-random-variables.qmd#s-geometric": "geometric-distribution",
    "prob-02-random-variables.qmd#s-hypergeometric": "hypergeometric-distribution",
    "prob-02-random-variables.qmd#s-normal": "normal-distribution",
    "prob-02-random-variables.qmd#s-poisson": "poisson-distribution",
    "prob-02-random-variables.qmd#s-uniform": "uniform-distribution",
    "prob-03-simulation.qmd#s-acceptance-and-rejection": "acceptance-rejection-method",
    "prob-03-simulation.qmd#s-inverse-transform": "inverse-transform-method",
    "sl-02-normal-inference.qmd#s-the-null-distribution": "null-distribution-of-hotelling-s",
    "sl-03-principal-components.qmd#s-directions-and-scores": "principal-component-directions-and-scores",
    "sl-04-kmeans.qmd#s-lloyd-s-algorithm": "lloyd-s-k-means-algorithm",
    "sl-09-error-rates.qmd#s-a-confusion-matrix": "confusion-matrix",
    "sl-09-error-rates.qmd#s-fold-cross-validation": "fold-cross-validation",
    "sl-09-error-rates.qmd#s-leave-one-out": "leave-one-out-cross-validation",
    "sl-09-error-rates.qmd#s-the-error-of-a-fixed-rule": "fixed-rule-error",
    "sl-11-nearest-neighbours.qmd#s-a-rank-distance": "rank-distance",
    "sl-17-support-vectors.qmd#s-the-dual": "hard-margin-dual",
    "sp-09-probability-spaces.qmd#s-borel-cantelli": "borel-cantelli-lemmas",
}
TOPICS: list[dict] = []
ALIASES: dict[str, str] = {}
RELATED: list[tuple[str, ...]] = []
LINKS: list[tuple] = []
LINKS_LAST: list[tuple] = []


# ---------------------------------------------------------------------------
# Named topics: Probability and Stochastic processes
# ---------------------------------------------------------------------------

TOPICS += [
    topic("Markov's inequality", "sp-01-stochastic-processes.qmd: Markov's inequality is the comparison",
          r"For a non-negative random variable $X$ and $a>0$, $\mathbb{P}(X\ge a)\le\mathbb{E}X/a$. It needs nothing but the mean, and applied to $(X-\mathbb{E}X)^2$ it gives Chebyshev's inequality.",
          also=["prob-05-transforms-and-limits.qmd: Markov's inequality is"],
          links=["Markov's inequality", "Markov inequality"]),
    topic("Chebyshev's inequality", "sp-01-stochastic-processes.qmd: That is Chebyshev's inequality",
          r"For a random variable with finite variance and $\varepsilon>0$, $\mathbb{P}(|X-\mathbb{E}X|\ge\varepsilon)\le\operatorname{Var}(X)/\varepsilon^2$. It is Markov's inequality applied to $(X-\mathbb{E}X)^2$, and it proves the weak law of large numbers and the consistency of an estimator whose mean squared error tends to zero.",
          also=["prob-05-transforms-and-limits.qmd: follows from Chebyshev's inequality", "inf-02-estimation.qmd: Chebyshev"],
          links=["Chebyshev's inequality", "Chebyshev inequality"]),
    topic("Jensen's inequality", "sp-11-convergence.qmd: Jensen's inequality says",
          r"If $\varphi$ is convex and $X$ and $\varphi(X)$ are integrable, then $\varphi(\mathbb{E}X)\le\mathbb{E}\varphi(X)$; for concave $\varphi$ the inequality reverses. With $\varphi(x)=x^2$ it says $\operatorname{Var}(X)\ge0$.",
          also=["sl-11-nearest-neighbours.qmd: Jensen's inequality", "sl-12-classification-trees.qmd: Jensen", "12-time-series.qmd: Jensen"],
          links=["Jensen's inequality"]),
    topic("Cauchy–Schwarz inequality", "prob-04-joint-distributions.qmd: Cauchy–Schwarz inequality applied",
          r"For random variables with finite second moments, $(\mathbb{E}XY)^2\le\mathbb{E}X^2\,\mathbb{E}Y^2$, with equality only when one is a constant multiple of the other. Applied to centred variables it gives $|\rho(X,Y)|\le1$.",
          also=["inf-02-estimation.qmd: Cauchy", "sl-08-discriminant-analysis.qmd: Cauchy"],
          links=["Cauchy–Schwarz inequality", "Cauchy–Schwarz"]),
    topic("Chapman–Kolmogorov equations", "prob-06-markov-chains.qmd: The Chapman–Kolmogorov equations are",
          r"For a time-homogeneous Markov chain the transition probabilities compose: $P^{m+n}=P^mP^n$ in discrete time, and $P(s+t)=P(s)P(t)$ in continuous time. To be at $j$ after the longer interval, the chain must be somewhere at the intermediate time.",
          also=["sp-07-continuous-markov.qmd: The Chapman–Kolmogorov identity"],
          links=["Chapman–Kolmogorov equations", "Chapman–Kolmogorov identity", "Chapman–Kolmogorov product", "Chapman–Kolmogorov"]),
    topic("First-passage time", "sp-03-random-walks.qmd: A first-passage event",
          r"The first time $T_A=\inf\{n\ge0:X_n\in A\}$ that a process enters a set $A$, with $T_A=\infty$ if it never does. Its law depends on the whole path, not on the state at one fixed time. Gambler's ruin and hitting probabilities are questions about it.",
          also=["sp-04-discrete-markov.qmd#s-hitting-questions-use-the-same-principle"],
          links=["first[- ]passage times?", "re:hitting times?", "first passage"]),
    topic("Irreducible Markov chain", "sp-05-classes-and-reversibility.qmd: States $i$ and $j$ communicate",
          r"A chain is irreducible when every state can be reached from every other, so that all states form one communicating class. A finite irreducible chain has a unique stationary distribution; with aperiodicity added, $P^n$ converges to it from any start.",
          also=["prob-06-markov-chains.qmd#s-the-limiting-distribution"],
          links=["irreducible", "irreducibility"]),
    topic("Aperiodic Markov chain", "sp-05-classes-and-reversibility.qmd: Period $1$ means aperiodic",
          r"The period of a state $i$ is $d(i)=\gcd\{n\ge1:p_{ii}^{(n)}>0\}$, and the state is aperiodic when $d(i)=1$. States in one communicating class share a period. A periodic chain can have a stationary law and still never converge to it, as the two-state alternation shows.",
          links=["aperiodic", "aperiodicity", "periodic chains?", "re:period of (?:a|the) (?:state|chain)"]),
    topic("Transient and recurrent states", "sp-05-classes-and-reversibility.qmd: State $i$ is recurrent when",
          r"State $i$ is recurrent when a chain started there returns with probability one, and transient otherwise. A recurrent state is positive recurrent when the expected return time is finite and null recurrent when it is infinite. In a finite chain every state of a closed class is positive recurrent.",
          links=["transient states?", "recurrent states?", "positive recurrent", "null recurrent", "recurrence", "transience"], scope=[SP]),
    topic("Doubly stochastic matrix", "sp-04-discrete-markov.qmd: If $P$ is doubly stochastic",
          r"A transition matrix whose columns, as well as its rows, sum to $1$. On $m$ states the uniform distribution $(1/m,\ldots,1/m)$ is then stationary. The condition is sufficient for a uniform stationary law, not necessary for a stationary law to exist.",
          links=["doubly stochastic"]),
    topic("Intensity function", "sp-06-poisson-processes.qmd: The cumulative intensity is",
          r"The rate $\lambda(t)\ge0$ of a non-homogeneous Poisson process, and its integral $\Lambda(t)=\int_0^t\lambda(u)\,du$, the cumulative intensity. The count in $(s,t]$ is Poisson with mean $\Lambda(t)-\Lambda(s)$. A constant intensity gives the homogeneous process.",
          links=["intensity functions?", "cumulative intensity", "rate functions?"], scope=[SP]),
    topic("Interarrival time", "sp-06-poisson-processes.qmd: Independent increments make the later interarrival times",
          r"The wait $W_n=T_n-T_{n-1}$ between successive events of a counting process. For a homogeneous Poisson process of rate $\lambda$ the interarrival times are independent exponentials with mean $1/\lambda$, and the arrival times $T_n$ are their partial sums; the converse construction gives a Poisson process too.",
          links=["interarrival times?", "inter-arrival times?"]),
    topic("Jump chain", "sp-07-continuous-markov.qmd#s-holding-times-the-jump-chain-and-the-generator",
          r"The discrete-time chain of states that a continuous-time Markov chain visits, ignoring how long it stays in each. From state $i$ it moves to $j\ne i$ with probability $q_{ij}/q_i$, where $q_i=-q_{ii}$ is the total rate of leaving $i$.",
          links=["jump chains?", "embedded chains?"]),
    topic("Holding time", "sp-07-continuous-markov.qmd#s-holding-times-the-jump-chain-and-the-generator",
          r"The time a continuous-time Markov chain stays in a state before it jumps. From state $i$ it is exponential with rate $q_i=-q_{ii}$ and independent of the past, which is what the memoryless property requires of a Markov process in continuous time.",
          links=["holding times?", "sojourn times?"]),
    topic("Local balance", "sp-08-queues.qmd: Local balance equates the flow",
          r"For a birth–death chain the stationary flow across each cut between neighbouring states balances: $\pi_n\lambda_n=\pi_{n+1}\mu_{n+1}$. It is detailed balance for a chain that moves one step at a time, and it gives the stationary law as a product of birth rates over death rates.",
          links=["local balance"]),
    topic("Blocking probability", r"sp-08-queues.qmd: Blocking probability $\pi_K$",
          r"In a queue with room for at most $K$ customers, the long-run fraction of arrivals turned away, which under Poisson arrivals is the stationary probability $\pi_K$ that the system is full. It rises with the load $\rho$, and it is the price a finite queue pays for having a stationary law at every load.",
          links=["blocking probabilit(?:y|ies)", "re:blocked arrivals?"]),
    topic("Throughput", "sp-08-queues.qmd: Throughput, the long-run rate of accepted arrivals",
          r"The long-run rate at which customers are accepted, and in equilibrium also served. For a queue that refuses arrivals when full it is $\lambda(1-\pi_K)$, below the offered rate $\lambda$. Little's law must use this rate, not the offered one.",
          links=["throughput"], scope=[SP]),
    topic("Sigma-algebra", r"sp-09-probability-spaces.qmd: A sigma-algebra $\mathcal{F}$ on",
          r"A collection $\mathcal{F}$ of subsets of $\Omega$ that contains $\Omega$ and is closed under complements and countable unions, and hence under countable intersections. The events of a probability space are the members of a sigma-algebra, so that the countable operations used for limits of events stay inside the collection.",
          also=["sp-09-probability-spaces.qmd: a sigma-algebra is a collection large enough"],
          links=["sigma-algebras?", "σ-algebras?", "sigma-fields?", "σ-fields?"]),
    topic("Countable additivity", "sp-09-probability-spaces.qmd: is countably additive",
          r"The axiom that probability adds over countably many disjoint events: $\mathrm{P}(\bigcup_n A_n)=\sum_n\mathrm{P}(A_n)$. Finite additivity is not enough for limits of events; countable additivity gives continuity along monotone sequences and the Borel–Cantelli lemmas.",
          links=["countable additivity", "countably additive"]),
    topic("Lebesgue decomposition", "sp-10-random-variables.qmd: The Lebesgue decomposition splits",
          r"Every distribution on the real line is uniquely a mixture of a discrete part (atoms), an absolutely continuous part (with a density) and a singular continuous part. The distribution function correspondingly has jumps, a differentiable part, and a part that increases on a set of length zero.",
          links=["Lebesgue decomposition"]),
    topic("Kolmogorov extension theorem", "sp-10-random-variables.qmd: Kolmogorov extension theorem",
          r"A consistent family of finite-dimensional distributions determines a stochastic process on the product space. It is an existence result: it does not give continuous sample paths or any other regularity a model may need.",
          links=["Kolmogorov extension theorem", "Kolmogorov('s)? extension"]),
    topic("Atom of a distribution", "sp-10-random-variables.qmd: The jump at $x$ equals that atom",
          r"A point $x$ with $\mathrm{P}(X=x)>0$. The distribution function jumps there by exactly that probability, $F_X(x)-F_X(x-)$, and right-continuity puts the atom in $F_X(x)=\mathrm{P}(X\le x)$.",
          links=["re:atoms?(?= (?:at|of) )"], scope=[SP, P]),
    topic("Lévy's continuity theorem", "sp-11-convergence.qmd: Lévy's continuity theorem says",
          r"If the characteristic functions $\varphi_{X_n}(t)$ converge for every $t$ to a function $\varphi$ that is continuous at $0$, then $X_n$ converges in distribution to the law with characteristic function $\varphi$. It is one route to the central limit theorem.",
          links=["Lévy's continuity theorem", "continuity theorem"]),
    topic("Pareto distribution", "sp-12-extremes.qmd: a Pareto tail",
          r"A law with power-law tail $\mathrm{P}(X>x)=x^{-\alpha}$ for $x\ge1$, with $\alpha>0$. Its mean is finite only when $\alpha>1$ and its variance only when $\alpha>2$. The maximum of $n$ draws, divided by $n^{1/\alpha}$, converges to the Fréchet law.",
          links=["Pareto distributions?", "Pareto tails?", "Pareto laws?", "Pareto"]),
    topic("State space", "sp-01-stochastic-processes.qmd: with state space $S$ and index set $T$",
          r"The set $S$ of values a stochastic process can take, such as $\{0,1,2,\ldots\}$ for a count or a finite set of weather types. Together with the index set $T$ (discrete or continuous time) it fixes what kind of process a model is, and a Markov model is only as good as the choice of state.",
          also=["sp-04-discrete-markov.qmd#s-the-markov-assumption-as-a-chosen-state"],
          links=["state spaces?"]),
    topic("Fubini's theorem", "prob-07-reliability.qmd: Fubini's theorem applied",
          r"For a non-negative function, or one whose absolute value is integrable, a double integral or a double sum may be computed in either order. Applied to $\mathbb{E}T=\mathbb{E}\int_0^T1\,dt$ it gives $\mathbb{E}T=\int_0^\infty\mathbb{P}(T>t)\,dt$ for a non-negative $T$.",
          links=["Fubini's theorem", "Fubini"]),
    topic("Birthday problem", "prob-01-experiments.qmd#exm-the-birthday-problem",
          r"With $n$ people and $365$ equally likely, independent birthdays, the probability that at least two share a birthday is $1-\prod_{k=0}^{n-1}(365-k)/365$. It first exceeds $1/2$ at $n=23$: there are $\binom{23}{2}=253$ pairs, each a chance of a match.",
          links=["birthday problem", "birthday paradox"]),
    topic("Monty Hall problem", "prob-01-experiments.qmd#exm-the-monty-hall-problem",
          r"A prize is behind one of three doors. You pick a door; the host, who knows where the prize is, opens one of the other doors to show no prize and offers a switch. Switching wins with probability $2/3$, because it wins exactly when the first pick was wrong.",
          links=["Monty Hall"]),
    topic("Box–Muller method", "prob-03-simulation.qmd: by the Box–Muller map",
          r"Two independent uniforms $U,V$ on $(0,1)$ give two independent standard normals, $Z_1=\sqrt{-2\log U}\cos(2\pi V)$ and $Z_2=\sqrt{-2\log U}\sin(2\pi V)$. The polar coordinates of a standard bivariate normal are an exponential squared radius and a uniform angle, which is why it works.",
          links=["Box–Muller method", "Box–Muller transform", "Box–Muller map", "Box–Muller"]),
    topic("Cauchy distribution", "prob-03-simulation.qmd: Cauchy distribution functions invert",
          r"The law with density $1/\{\pi(1+x^2)\}$ on the real line. It has no mean, so averages of Cauchy draws never settle down, and the law of large numbers does not apply. Its distribution function $\tfrac12+\arctan(x)/\pi$ inverts in closed form, so it is easy to simulate.",
          links=["Cauchy distributions?", "Cauchy laws?"]),
    topic("Random seed", "prob-03-simulation.qmd: starting from a seed",
          r"The starting value $X_0$ of a pseudorandom number generator. The same seed reproduces the same sequence of draws, which is why a simulation records it, with `set.seed` in R.",
          links=["random seeds?", "re:set\\.seed"]),
    topic("Conditional expectation", "prob-04-joint-distributions.qmd: The conditional expectation",
          r"$\mathbb{E}(Y\mid X=x)$ is the mean of $Y$ under its conditional distribution given $X=x$. As a function of $X$ it is the random variable $\mathbb{E}(Y\mid X)$, whose average is $\mathbb{E}Y$ by the tower property. Among functions of $X$ it is the best predictor of $Y$ in mean squared error, and for a jointly normal pair it is linear in $x$.",
          also=["sl-01-multivariate-normal.qmd#s-the-conditional-mean-line-and-least-squares"],
          links=["conditional expectations?", "conditional means?"]),
    topic("Convolution", "prob-05-transforms-and-limits.qmd: the convolution",
          r"The distribution of a sum of independent random variables. For densities, $f_{X+Y}(z)=\int f_X(x)f_Y(z-x)\,dx$; for mass functions the integral is a sum. Generating functions turn a convolution into a product.",
          links=["convolutions?"]),
    topic("Jacobian", "prob-05-transforms-and-limits.qmd#s-the-transformation-rule",
          r"The determinant of the matrix of partial derivatives of a change of variables. In the transformation rule it rescales a density: if $\mathbf{Y}=g(\mathbf{X})$ with $g$ one-to-one and differentiable, $f_{\mathbf{Y}}(\mathbf{y})=f_{\mathbf{X}}(g^{-1}(\mathbf{y}))\,|\det J_{g^{-1}}(\mathbf{y})|$.",
          links=["Jacobians?", "Jacobian determinants?"]),
    topic("Random walk with drift", "12-time-series.qmd: A random walk is the case",
          r"A random walk whose increments have non-zero mean $\mu$: $S_n=S_0+\sum_{i\le n}Y_i$ with $\mathbb{E}Y_i=\mu$. Its mean moves like $n\mu$ while its spread grows like $\sqrt n$, so in the long run the drift dominates.",
          also=["sp-03-random-walks.qmd: Drift accumulates like $n$"],
          links=["random walks? with drift"], scope=[T, SP]),
]

ALIASES.update({
    "Monotone convergence theorem": "monotone-convergence-fatou-and-dominated-convergence",
    "Fatou's lemma": "monotone-convergence-fatou-and-dominated-convergence",
    "Dominated convergence theorem": "monotone-convergence-fatou-and-dominated-convergence",
    "Convergence in probability": "modes-of-convergence",
    "Convergence in distribution": "modes-of-convergence",
    "Almost sure convergence": "modes-of-convergence",
    "Convergence in mean": "modes-of-convergence",
    "Weak law of large numbers": "law-of-large-numbers",
    "Strong law of large numbers": "strong-law",
    "Recurrence (Markov chain)": "recurrence-and-period",
    "Period of a state": "recurrence-and-period",
    "Gumbel distribution": "exponential-tails-and-the-gumbel-law",
    "Fréchet distribution": "power-law-tails-and-the-frechet-law",
    "Borel sigma-algebra": "generated-and-borel-sigma-algebras",
    "Simple random variable": "simple-variables-and-expectation",
    "Reversible Markov chain": "detailed-balance",
    "Q-matrix": "generator",
    "Birth–death process": "birth-death-balance",
    "Superposition of Poisson processes": "superposition-and-thinning",
    "Thinning of a Poisson process": "superposition-and-thinning",
    "Galton–Watson branching process": "galton-watson-process",
    "Inverse-transform sampling": "inverse-transform-method",
    "Probability mass function": "discrete-distribution",
    "Probability density function": "continuous-distribution",
})


# ---------------------------------------------------------------------------
# Named topics: Statistical inference, Data analysis, Bayesian statistics
# ---------------------------------------------------------------------------

TOPICS += [
    topic("Standard error", "inf-03-confidence-intervals.qmd#s-from-a-standard-error-to-an-interval",
          r"The standard deviation of an estimator's sampling distribution, or an estimate of it. For a sample mean it is $\sigma/\sqrt n$, estimated by $s/\sqrt n$. An approximate 95% interval is the estimate plus or minus about two standard errors, and a $z$ or $t$ statistic is an estimate measured in standard errors.",
          also=["02-inference-and-counts.qmd#s-standard-errors-in-a-glm"],
          links=["standard errors?", "standard error of the mean"]),
    topic("Bias of an estimator", "inf-02-estimation.qmd: The split is the variance–bias tradeoff",
          r"$\operatorname{bias}(\hat\theta)=\mathbb{E}\hat\theta-\theta$, the average amount by which an estimator misses its target. An estimator with zero bias is unbiased. The mean squared error is the variance plus the squared bias, so a small bias can be worth accepting for a larger drop in variance.",
          links=["bias–variance trade-?off", "variance–bias trade-?off", "biased estimators?"]),
    topic("Sampling bias", "da-01-studies-and-data.qmd: Many data are collected in ways far from random",
          r"A systematic difference between a sample and the population it is meant to represent, caused by the way units were chosen. Convenience and self-selected samples are the usual sources. A larger biased sample is not a better one: the bias does not shrink with $n$.",
          links=["sampling bias", "selection bias", "convenience samples?", "self-selected samples?"]),
    topic("Measurement error", "da-01-studies-and-data.qmd: Measurements vary for more than one reason",
          r"Variation in recorded values that comes from the measuring process rather than from the units measured. It adds to the residual variability a model cannot explain, and in an explanatory variable it biases a fitted slope toward zero.",
          also=["01-introduction-to-glms.qmd: measurement error"],
          links=["measurement errors?"]),
    topic("Treatment", "da-01-studies-and-data.qmd: In a designed experiment some columns are controlled",
          r"The condition an experimenter assigns to a unit: a drug, a dose, a fertiliser, a teaching method. Comparing responses across treatments, with the assignment randomised, is what lets a designed experiment support a causal conclusion that an observational study cannot.",
          links=["treatment groups?", "treatments?"], scope=[D, I], late=True),
    topic("Significance level", "inf-04-hypothesis-tests.qmd: The size, or significance level",
          r"The probability $\alpha$ of a type I error that a test allows: the null hypothesis is rejected when the test statistic falls in a critical region of probability $\alpha$ under the null. It is chosen before the data are seen, conventionally $\alpha=0.05$.",
          links=["significance levels?", "levels? of significance", "size of (?:a|the) test"]),
    topic("Degrees of freedom", "inf-01-statistical-inference.qmd: has the chi-squared distribution with $m$ degrees of freedom",
          r"The parameter of the chi-squared, $t$ and $F$ families, and the number of independent pieces of information behind a variance estimate: $n-1$ for a sample variance, $n-p$ for a regression with $p$ coefficients, $(r-1)(c-1)$ for a test of independence in an $r\times c$ table.",
          links=["degrees? of freedom"], late=True),
    topic("Observed and expected counts", "inf-05-chi-square.qmd: is the observed count and",
          r"In a chi-squared test the count $O_i$ observed in each category is set against the count $E_i=n\pi_i$ expected under the null hypothesis. Pearson's statistic is $\sum_i(O_i-E_i)^2/E_i$; the chi-squared approximation is trusted when the expected counts are not too small, a usual rule being all $E_i\ge5$.",
          also=["da-09-chi-square-examples.qmd#s-seeing-the-approximation"],
          links=["expected counts?", "observed counts?", "expected frequenc(?:y|ies)", "expected cell counts?"]),
    topic("Explanatory variable", "inf-06-regression.qmd: Regression analysis explains a response variable",
          r"A variable $x$ used to explain or predict a response $y$; also called a covariate or predictor. In a designed experiment it is set by the experimenter, in an observational study it is only recorded, and a fitted association with it is not by itself causal.",
          also=["da-07-regression-examples.qmd#s-one-explanatory-variable"],
          links=["explanatory variables?", "covariates?"], late=True),
    topic("Response variable", "inf-06-regression.qmd: Regression analysis explains a response variable",
          r"The variable $y$ a model describes or predicts from explanatory variables; also called the dependent variable or outcome. A regression models its conditional distribution, or at least its conditional mean, given the explanatory variables.",
          links=["response variables?", "dependent variables?"]),
    topic("Regression slope", "inf-06-regression.qmd#s-least-squares",
          r"In the regression line $y=\beta_0+\beta_1x$, the slope $\beta_1$ is the change in mean response per unit increase in $x$. Its least-squares estimate is $\widehat\beta_1=S_{xY}/S_{xx}$, and under the normal linear model the slope $t$ pivot gives tests and intervals for it.",
          links=["regression slopes?", "fitted slopes?"]),
    topic("Wald test", "sl-10-logistic-regression.qmd: The Wald statistic divides",
          r"A test built from an estimate and its standard error: $z=(\hat\theta-\theta_0)/\widehat{\operatorname{se}}(\hat\theta)$, referred to $\mathrm{N}(0,1)$. Inverting it gives the Wald interval $\hat\theta\pm z_{\alpha/2}\,\widehat{\operatorname{se}}(\hat\theta)$. It is the $z$ value that R prints beside each GLM coefficient.",
          also=["inf-03-confidence-intervals.qmd#s-a-proportion"],
          links=["Wald tests?", "Wald statistics?", "Wald z"]),
    topic("Likelihood-ratio test", "sl-02-normal-inference.qmd#s-hypotheses-and-the-likelihood-ratio",
          r"A test of a model against a nested submodel that compares their maximised likelihoods. Under regularity conditions $2\{\ell(\hat\theta)-\ell(\hat\theta_0)\}$ is approximately chi-squared, with degrees of freedom equal to the number of restrictions. A difference in deviances is this statistic.",
          also=["05-comparisons-and-deviance.qmd: The deviance is twice the drop in log-likelihood"],
          links=["likelihood[- ]ratio tests?", "likelihood[- ]ratio statistics?"]),
    topic("Multiple testing", "sl-18-high-dimensional.qmd#s-why-a-fixed-threshold-fails",
          r"Running many tests at level $\alpha$ makes false rejections likely: with $m$ independent true null hypotheses, the chance of at least one is $1-(1-\alpha)^m$. Corrections control either the family-wise error rate, as Bonferroni's and Tukey's methods do, or the false discovery rate, as Benjamini–Hochberg does.",
          also=["inf-07-anova.qmd#s-multiple-comparisons", "da-06-anova-examples.qmd#s-which-groups-differ"],
          links=["multiple testing", "multiple tests", "multiplicity"]),
    topic("Family-wise error rate", "sl-18-high-dimensional.qmd: The family-wise error rate is controlled",
          r"The probability of at least one false rejection among a family of tests. Bonferroni's correction and Tukey's intervals control it. It is stricter than the false discovery rate, and with thousands of tests it leaves almost no power.",
          also=["inf-07-anova.qmd: at familywise level"],
          links=["family-wise error rates?", "family-wise level", "family-wise", "FWER"]),
    topic("Wilcoxon rank-sum test", "da-04-estimation-examples.qmd: such as the Wilcoxon rank-sum test",
          r"A test for a shift between two independent samples that uses only the ranks of the pooled observations, so it does not need normality. It is the safer choice than a two-sample $t$ procedure for small, skewed samples.",
          links=["Wilcoxon rank-sum tests?", "Wilcoxon tests?", "rank-sum tests?", "Mann–Whitney"]),
    topic("Histogram", "da-02-descriptive-statistics.qmd: A histogram counts the data",
          r"A plot that counts the observations in adjacent bins and draws a bar for each. Its look depends on the bin width and starting point, which is why a kernel density estimate is often drawn alongside it.",
          links=["histograms?"]),
    topic("Outlier", "da-02-descriptive-statistics.qmd: Points beyond the whiskers",
          r"An observation far from the bulk of the data. A boxplot flags points more than $1.5$ interquartile ranges beyond the quartiles. An outlier may be an error, or the most informative point in the sample; it is checked, not deleted by rule.",
          links=["outliers?", "outlying"]),
    topic("Skewness", "da-02-descriptive-statistics.qmd: the skewness, a measure of asymmetry",
          r"A measure of asymmetry, zero for symmetric data, positive when the right tail is longer. Strongly right-skewed positive data are often summarised and modelled better after a log transformation.",
          links=["skewness", "skewed", "right-skewed", "left-skewed"]),
    topic("Median", "da-02-descriptive-statistics.qmd: the sample median is the middle value",
          r"The middle value of the ordered sample, or the average of the two middle values when $n$ is even: the $0.5$ sample quantile. Unlike the mean it barely moves when one value is wild, which makes it the robust summary of location. For a distribution it is any point $m$ with $\mathbb{P}(X\le m)\ge\tfrac12$ and $\mathbb{P}(X\ge m)\ge\tfrac12$.",
          links=["medians?", "sample medians?"], late=True),
    topic("Range", "da-02-descriptive-statistics.qmd: The five-number summary of a sample is its minimum",
          r"The largest observation minus the smallest. It uses only the two extremes, so one outlier changes it completely; the interquartile range is the robust measure of spread.",
          links=["sample range"]),
    topic("Scatterplot", "da-02-descriptive-statistics.qmd: Two quantitative variables are plotted against each other",
          r"A plot of one quantitative variable against another, one point per unit. It shows the form, direction and strength of a relationship, and outliers, before any correlation or regression line summarises it.",
          also=["da-02-descriptive-statistics.qmd#s-two-quantitative-variables"],
          links=["scatterplots?", "scatter plots?", "scatter ?diagrams?"]),
    topic("Main effect", "da-06-anova-examples.qmd: are the main effects of the two factors",
          r"In a factorial design, the effect of one factor averaged over the levels of the others. When the factors interact, a main effect alone can mislead, because the effect of one factor then depends on the level of the other.",
          links=["main effects?"]),
    topic("Improper prior", "bayes-01-foundations.qmd: An improper prior may sometimes produce a proper posterior",
          r"A prior density whose integral is infinite, such as a flat density on the whole real line. It is not a probability distribution, and it is usable only when the posterior it produces is proper, which has to be checked rather than assumed.",
          links=["improper priors?"]),
    topic("Flat prior", "bayes-03-normal-models.qmd: flat prior",
          r"A prior density that is constant in the parameter. On an unbounded parameter it is improper. The posterior is then proportional to the likelihood, so its mode is the maximum likelihood estimate; a flat prior is flat only on the scale chosen, not on transformations of it.",
          links=["flat priors?", "uniform priors?"]),
    topic("Precision", "bayes-03-normal-models.qmd: It is often convenient to work in precisions",
          r"The reciprocal of a variance, $\tau=1/\sigma^2$. In normal models precisions add: the posterior precision of a normal mean is the prior precision plus $n/\sigma^2$, and the posterior mean is the precision-weighted average of the prior mean and the sample mean.",
          links=["precisions?"], scope=[B], late=True),
    topic("Maximum a posteriori estimate", "bayes-09-linear-regression.qmd: A centred normal prior also explains ridge regularisation",
          r"The posterior mode, $\arg\max_\theta p(\theta\mid y)$. With a flat prior it is the maximum likelihood estimate. In regression a normal prior on the coefficients makes it ridge regression and a Laplace prior makes it the lasso; it keeps none of the posterior's uncertainty.",
          also=["bayes-01-foundations.qmd#s-posterior-summaries"],
          links=["MAP estimat(?:e|es|ion|or)", "maximum a posteriori", "MAP"]),
    topic("Monte Carlo method", "bayes-04-mcmc.qmd: MCMC is not intrinsically Bayesian",
          r"Approximating an expectation by an average over simulated draws, $\mathbb{E}g(\theta)\approx\frac1M\sum_{m=1}^Mg(\theta^{(m)})$. For independent draws the Monte Carlo error shrinks like $1/\sqrt M$; correlated MCMC draws carry less information per draw.",
          also=["bayes-08-hierarchy.qmd#s-grid-approximation-and-posterior-simulation"],
          links=["Monte Carlo methods?", "Monte Carlo simulation", "Monte Carlo"], late=True),
    topic("Metropolis algorithm", "bayes-04-mcmc.qmd: The original Metropolis algorithm used symmetric proposals",
          r"The Metropolis–Hastings sampler with a symmetric proposal, $q(\theta'\mid\theta)=q(\theta\mid\theta')$, for which the acceptance probability reduces to $\min\{1,\pi(\theta')/\pi(\theta)\}$. A random-walk proposal is the usual example.",
          links=["Metropolis algorithms?", "Metropolis sampler"]),
    topic("Ising model", "bayes-04-mcmc.qmd: An Ising model on $m$ binary sites",
          r"A model for binary spins on a lattice, $x_i\in\{-1,+1\}$, whose joint law favours neighbouring sites that agree, $p(\mathbf{x})\propto\exp(\beta\sum_{i\sim j}x_ix_j)$. Its normalising constant sums over $2^m$ configurations, but ratios of unnormalised weights are easy, which is why Metropolis methods came from statistical physics.",
          links=["Ising models?"]),
    topic("Hastings correction", "bayes-04-mcmc.qmd: The Hastings correction guarantees the right equilibrium",
          r"The factor $q(\theta\mid\theta')/q(\theta'\mid\theta)$ in the Metropolis–Hastings acceptance probability. It corrects for a proposal that is more likely in one direction than the other, and equals $1$ for a symmetric proposal.",
          links=["Hastings corrections?", "Hastings ratio"]),
    topic("Burn-in", "bayes-04-mcmc.qmd: Discarding early draws is called warm-up or burn-in",
          r"The initial stretch of a Markov chain Monte Carlo run that is discarded because the chain may not yet have forgotten its starting value; the course also calls it warm-up. Discarding it limits dependence on the start. It does not prove that the rest of the run has converged.",
          also=["bayes-09-linear-regression.qmd: burn-in"],
          links=["burn-in", "warm-up"]),
    topic("Thinning a Markov chain", "bayes-04-mcmc.qmd: Thinning by retaining every",
          r"Keeping only every $k$th draw of an MCMC run. It reduces storage and visible autocorrelation, but it throws information away: the full chain gives a Monte Carlo average at least as precise, so thinning is justified only by storage or by an expensive later calculation.",
          links=["thinning", "thinned chains?"], scope=[B]),
    topic("Effective sample size", "bayes-04-mcmc.qmd: effective sample size are therefore part of a serious analysis",
          r"The number of independent draws that would give the same Monte Carlo precision as $M$ correlated MCMC draws, roughly $M/(1+2\sum_{k\ge1}\rho_k)$ for lag-$k$ autocorrelations $\rho_k$. Strong autocorrelation makes it much smaller than $M$.",
          links=["effective sample sizes?"], scope=[B]),
    topic("Trace plot", "bayes-04-mcmc.qmd: The trace plot and autocorrelation function are not substitutes",
          r"A plot of the sampled values of a parameter against iteration number. A chain that drifts, sticks, or disagrees with other chains shows a problem; a tidy plot is evidence of mixing, not a proof of convergence.",
          links=["trace plots?"]),
    topic("Full conditional distribution", "bayes-04-mcmc.qmd: while every full conditional is available",
          r"The distribution of one parameter given the data and all the other parameters, $\pi(x_j\mid x_{-j})$. A Gibbs sampler draws from each full conditional in turn. Up to a constant it is the joint density read as a function of $x_j$ alone, which is how it is found.",
          also=["bayes-03-normal-models.qmd#s-both-normal-parameters-unknown"],
          links=["full conditionals?(?: distributions?)?", "full conditional densit(?:y|ies)"]),
    topic("Lehmann–Scheffé theorem", "bayes-07-exponential-families.qmd: The Lehmann--Scheffé theorem further says",
          r"An unbiased estimator that is a function of a complete sufficient statistic is the unique uniformly minimum-variance unbiased estimator of its expectation.",
          links=["Lehmann–Scheffé theorem", "Lehmann–Scheffé", "UMVUE", "minimum-variance unbiased"]),
    topic("Natural parameter", "01-introduction-to-glms.qmd: Two reductions have names",
          r"The parameter that multiplies the data, or the sufficient statistic, in the exponent of an exponential-family density. For the Poisson it is $\log\lambda$, for the Bernoulli the log-odds $\log\{p/(1-p)\}$. A canonical link sets it equal to the linear predictor.",
          also=["bayes-07-exponential-families.qmd: whose natural parameter space contains"],
          links=["natural parameters?", "canonical parameters?"]),
    topic("Prior odds", "bayes-06-testing.qmd#s-posterior-odds-and-bayes-factors",
          r"The ratio $\mathbb{P}(H_1)/\mathbb{P}(H_2)$ of prior probabilities of two hypotheses or models. Bayes' rule turns it into the posterior odds by multiplying by the Bayes factor.",
          links=["prior odds"]),
    topic("Posterior mean", "bayes-01-foundations.qmd#s-posterior-summaries",
          r"The mean $\mathbb{E}(\theta\mid y)$ of the posterior distribution. It is the Bayes estimate under squared-error loss, and in conjugate models it is a weighted average of the prior mean and a data summary.",
          links=["posterior means?", "posterior expectations?"]),
    topic("Posterior median", "bayes-01-foundations.qmd#s-posterior-summaries",
          r"The median of the posterior distribution, the Bayes estimate under absolute-error loss. Unlike the mode and the mean it is unchanged by monotone reparameterisation.",
          links=["posterior medians?"]),
]

ALIASES.update({
    "Credible interval": "bayesian-credible-interval",
    "Posterior mode": "posterior-point-summaries",
    "Marginal likelihood": "marginal-likelihood-and-bayes-factor",
    "Null hypothesis": "null-and-alternative-hypotheses",
    "Alternative hypothesis": "null-and-alternative-hypotheses",
    "t distribution": "student-t-distribution",
    "Pitman–Koopman–Darmois theorem": "pitman-koopman-darmois-informal-form",
    "Confounding": "confounding-variable",
    "Stratified sampling": "stratified-and-cluster-sampling",
    "Cluster sampling": "stratified-and-cluster-sampling",
    "Boxplot": "five-number-summary-and-boxplot",
    "Quartile": "sample-quantile",
    "Percentile": "sample-quantile",
    "Quantile": "sample-quantile",
    "Standard deviation": "sample-variance-and-standard-deviation",
    "R-squared": "coefficient-of-determination",
    "Dummy variable": "dummy-variable-coding",
    "Power of a test": "power-function",
    "Paired t test": "paired-samples",
    "Covariate": "explanatory-variable",
    "Predictor variable": "explanatory-variable",
    "Warm-up": "burn-in",
    "MCMC thinning": "thinning-a-markov-chain",
    "Partial pooling": "complete-pooling-no-pooling-and-partial-pooling",
    "Gibbs sampler": "gibbs-sampling",
})


# ---------------------------------------------------------------------------
# Named topics: GLMs, smoothing, correlated data, time series
# ---------------------------------------------------------------------------

TOPICS += [
    topic("Link function", "01-introduction-to-glms.qmd#s-the-three-components-of-a-glm",
          r"The function $g$ that ties the mean of a GLM to its linear predictor, $g(\mu_i)=\mathbf{X}_i^\top\boldsymbol{\beta}$. It is chosen so that every value of the linear predictor gives a legal mean: the logit keeps a probability in $(0,1)$, the log keeps a count's mean positive.",
          also=["01-introduction-to-glms.qmd#s-three-links", "03-gamma-and-quasi.qmd: Three links are in ordinary use"],
          links=["link functions?"]),
    topic("Linear predictor", "01-introduction-to-glms.qmd#s-the-three-components-of-a-glm",
          r"The linear part of a generalised linear model, $\eta_i=\mathbf{X}_i^\top\boldsymbol{\beta}$, which the link function connects to the mean. It is where covariates, factors and interactions enter, exactly as in a linear model.",
          links=["linear predictors?"]),
    topic("Random component", "01-introduction-to-glms.qmd#s-the-three-components-of-a-glm",
          r"The distribution assumed for the response given the covariates in a GLM, a member of an exponential family such as the normal, Poisson, binomial or gamma. It fixes the mean–variance relationship, $\operatorname{Var}(Y)=\phi V(\mu)$.",
          links=["random components?", "response distributions?"]),
    topic("Logit link", "01-introduction-to-glms.qmd: Dividing by one plus itself fixes that",
          r"$g(p)=\log\{p/(1-p)\}$, the log-odds. It maps $(0,1)$ onto the whole real line, it is the canonical link for binomial responses, and it makes each coefficient a log odds ratio.",
          links=["logit links?", "logits?", "log[- ]odds"]),
    topic("Probit link", "01-introduction-to-glms.qmd: The probit link replaces the logistic curve",
          r"$g(p)=\Phi^{-1}(p)$, the standard normal quantile function. It fits binary data much like the logit, with coefficients smaller by a factor of about $1.6$ to $1.8$, but it has no odds-ratio reading.",
          also=["sl-10-logistic-regression.qmd#s-logistic-and-probit"],
          links=["probit links?", "probit models?", "probit regressions?", "probit"]),
    topic("Complementary log-log link", "01-introduction-to-glms.qmd: The complementary log-log link is",
          r"$g(p)=\log\{-\log(1-p)\}$. Unlike the logit and probit it is not symmetric about $p=1/2$. It arises when a binary response records whether a Poisson count is positive, since then $\log\{-\log(1-p)\}=\log\lambda$, and in ordinal regression it gives a proportional-hazards model.",
          links=["complementary log-log(?: links?)?", "cloglog"]),
    topic("Identity link", "01-introduction-to-glms.qmd: The normal linear model is the GLM with identity link",
          r"$g(\mu)=\mu$, the canonical link for normal responses: the mean is the linear predictor itself. With a normal random component the GLM is the normal linear model.",
          links=["identity links?"]),
    topic("Log link", "03-gamma-and-quasi.qmd: Three links are in ordinary use",
          r"$g(\mu)=\log\mu$. It keeps the mean positive for any linear predictor and makes coefficients multiplicative: $e^{\beta_j}$ is the factor by which the mean changes per unit of $x_j$. It is the canonical link for Poisson counts and the usual choice for gamma responses.",
          also=["02-inference-and-counts.qmd#s-reading-a-log-linear-coefficient"],
          links=["log links?"]),
    topic("Inverse link", "03-gamma-and-quasi.qmd: Three links are in ordinary use",
          r"$g(\mu)=1/\mu$, the canonical link for gamma responses, up to sign. It needs the linear predictor to stay positive, which the data do not guarantee, so it can fail where the log link does not.",
          links=["inverse links?", "reciprocal links?"]),
    topic("Odds", "01-introduction-to-glms.qmd#s-interpreting-a-logistic-regression",
          r"The ratio $p/(1-p)$ of the probability of an event to the probability that it does not happen. Probability $0.8$ is odds $4$. Logistic regression models the log-odds as a linear function of the covariates.",
          links=["odds"], late=True),
    topic("Odds ratio", "01-introduction-to-glms.qmd#s-interpreting-a-logistic-regression",
          r"The ratio of the odds of an event in two groups. In a logistic regression $e^{\beta_j}$ is the odds ratio for a one-unit increase in $x_j$, the same at every value of the other covariates when $x_j$ has no interaction terms. An odds ratio of $1$ means no association.",
          also=["10-plants-and-series.qmd: The working association between each pair is a log odds ratio", "04-categorical-responses.qmd: We can say what an odds ratio is"],
          links=["odds ratios?", "log odds ratios?"]),
    topic("Fisher information", "01-introduction-to-glms.qmd: which is the Fisher information",
          r"The expected curvature of the log-likelihood, $\mathcal{I}(\theta)=-\mathbb{E}\,\partial^2\ell/\partial\theta\,\partial\theta^\top$, which is also the variance of the score. Its inverse approximates the variance of the maximum likelihood estimator, and that is where the standard errors of a GLM come from.",
          also=["02-inference-and-counts.qmd#s-standard-errors-in-a-glm"],
          links=["Fisher information", "information matri(?:x|ces)", "expected information"]),
    topic("Score function", "01-introduction-to-glms.qmd: Differentiate with respect to",
          r"The gradient of the log-likelihood, $U(\theta)=\partial\ell/\partial\theta$. The maximum likelihood estimate solves $U(\hat\theta)=0$. At the true parameter the score has mean zero and variance equal to the Fisher information.",
          also=["sl-10-logistic-regression.qmd#s-score-and-hessian"],
          links=["score functions?", "score vectors?", "score equations?"]),
    topic("Newton–Raphson method", "sl-10-logistic-regression.qmd: Newton–Raphson updates",
          r"An iteration for solving $U(\theta)=0$: $\theta^{(k+1)}=\theta^{(k)}-H(\theta^{(k)})^{-1}U(\theta^{(k)})$, with $H$ the Hessian of the log-likelihood. Fisher scoring replaces $H$ by minus the expected information. For a canonical link the two coincide, and either one is iteratively reweighted least squares.",
          also=["01-introduction-to-glms.qmd: which is the Fisher information"],
          links=["Newton–Raphson", "Newton's method"]),
    topic("Overdispersion", "02-inference-and-counts.qmd: Here $\\phi>1$ is overdispersion",
          r"Count data are overdispersed when their variance exceeds what the model allows, usually a Poisson variance equal to the mean. Ignoring it makes standard errors too small. A quasi-Poisson dispersion or a negative binomial model allows for it.",
          also=["prob-02-random-variables.qmd: overdispersed"],
          links=["over-?dispersion", "over-?dispersed"]),
    topic("Underdispersion", "02-inference-and-counts.qmd: Here $\\phi>1$ is overdispersion",
          r"Variance smaller than the model implies, for counts a variance below the mean. It is rarer than overdispersion. A quasi-Poisson model with $\phi<1$ or a Conway–Maxwell–Poisson model can describe it; a negative binomial cannot.",
          also=["03-gamma-and-quasi.qmd#s-bids-for-a-bankrupt-firm"],
          links=["under-?dispersion", "under-?dispersed"]),
    topic("Dispersion parameter", "01-introduction-to-glms.qmd: a dispersion, which plays the role",
          r"The parameter $\phi$ that scales the variance of a GLM, $\operatorname{Var}(Y)=\phi V(\mu)$. It is $\sigma^2$ for the normal and $1/\alpha$ for a gamma with shape $\alpha$; it is fixed at $1$ for the Poisson and binomial unless a quasi-likelihood frees it.",
          links=["dispersion parameters?", "dispersions?"], scope=[G, S, C]),
    topic("Variance function", "03-gamma-and-quasi.qmd#s-quasi-likelihood",
          r"The function $V(\mu)$ in $\operatorname{Var}(Y)=\phi V(\mu)$: $1$ for the normal, $\mu$ for the Poisson, $\mu(1-\mu)$ for the Bernoulli, $\mu^2$ for the gamma, $\mu^3$ for the inverse Gaussian. Quasi-likelihood needs only a mean and a variance function, not a full distribution.",
          links=["variance functions?"]),
    topic("Negative binomial distribution", "02-inference-and-counts.qmd: the usual next model is the negative binomial",
          r"A count distribution with mean $\mu$ and variance $\mu+\mu^2/\nu$, built as a gamma mixture of Poisson counts: draw a rate from a gamma law, then a Poisson count at that rate. It allows overdispersion, never underdispersion, and approaches the Poisson as $\nu\to\infty$.",
          links=["negative binomial(?: distributions?| models?| regressions?)?", "gamma mixtures? of Poissons?"]),
    topic("Conway–Maxwell–Poisson distribution", "02-inference-and-counts.qmd: The Conway–Maxwell–Poisson distribution has been available",
          r"A count distribution with probability function proportional to $\lambda^y/(y!)^\nu$. The extra parameter allows overdispersion ($\nu<1$), the Poisson ($\nu=1$) and underdispersion ($\nu>1$); reparameterised by its mean it can be fitted as a GLM-like model.",
          also=["03-gamma-and-quasi.qmd#s-bids-for-a-bankrupt-firm"],
          links=["Conway–Maxwell–Poisson(?: distributions?| models?)?", "COM-Poisson"]),
    topic("Poisson regression", "02-inference-and-counts.qmd#s-counts",
          r"A generalised linear model for counts with a Poisson random component and, usually, the log link: $\log\mu_i=\mathbf{X}_i^\top\boldsymbol{\beta}$, so $e^{\beta_j}$ multiplies the expected count per unit of $x_j$. It assumes the variance equals the mean, which overdispersion breaks.",
          also=["02-inference-and-counts.qmd#s-reading-a-log-linear-coefficient"],
          links=["Poisson regressions?", "Poisson GLMs?", "log-linear models?"]),
    topic("Gamma regression", "03-gamma-and-quasi.qmd#s-positive-continuous-responses",
          r"A GLM for positive continuous responses with a gamma random component, so that the standard deviation is proportional to the mean. The log link is the usual choice; the canonical inverse link can fail when the linear predictor goes negative.",
          also=["01-introduction-to-glms.qmd#s-clotting-times"],
          links=["gamma regressions?", "gamma GLMs?"]),
    topic("Inverse Gaussian distribution", "03-gamma-and-quasi.qmd: a mystery of the inverse Gaussian",
          r"A distribution on $(0,\infty)$ whose variance is proportional to the cube of its mean. In a GLM its canonical link is $\mu^{-2}$, the inverse quadratic, which needs the linear predictor to stay positive.",
          links=["inverse Gaussian(?: distributions?| models?)?"]),
    topic("Lognormal distribution", "03-gamma-and-quasi.qmd: inverse gamma, lognormal",
          r"The law of $e^Z$ when $Z$ is normal. Its variance is $(e^{\sigma^2}-1)\mu^2$, proportional to the square of its mean as for the gamma, so for positive responses a lognormal model and a gamma GLM with log link often agree.",
          links=["log-?normal(?: distributions?| priors?)?"]),
    topic("Saturated model", "05-comparisons-and-deviance.qmd: The saturated fit is the baseline",
          r"A model with one parameter per observation, so that its fitted means equal the data. It fits perfectly and predicts nothing; the deviance of any other model is measured from it.",
          links=["saturated models?", "saturated fits?"]),
    topic("Residual deviance", "05-comparisons-and-deviance.qmd: The deviance is twice the drop in log-likelihood",
          r"The deviance of a fitted model, $D=2\{\ell(\mathbf{y};\mathbf{y})-\ell(\hat{\boldsymbol\mu};\mathbf{y})\}$, printed by R with its residual degrees of freedom. The difference in residual deviance between nested models is a likelihood-ratio statistic.",
          also=["05-comparisons-and-deviance.qmd: The three-factor model has residual deviance"],
          links=["residual deviances?"]),
    topic("Null deviance", "05-comparisons-and-deviance.qmd#s-three-links-one-cholesterol-slope",
          r"The deviance of the intercept-only model. The drop from the null deviance to the residual deviance measures how much the covariates explain, and is tested on the difference in degrees of freedom.",
          links=["null deviances?"]),
    topic("Scaled deviance", "05-comparisons-and-deviance.qmd: the difference in scaled deviance",
          r"The deviance divided by the dispersion $\phi$. A difference in scaled deviance between nested models is referred to a chi-squared law when $\phi$ is known, and to an $F$ law when $\phi$ is estimated from the same data.",
          links=["scaled deviances?"]),
    topic("Deviance residual", "05-comparisons-and-deviance.qmd: The deviance residual takes",
          r"$r_D=\operatorname{sign}(y_i-\hat\mu_i)\sqrt{d_i}$, where $d_i$ is observation $i$'s contribution to the deviance, so the squared deviance residuals add up to the deviance. It measures misfit on the likelihood's own scale.",
          links=["deviance residuals?"]),
    topic("Pearson residual", "05-comparisons-and-deviance.qmd: The Pearson residual divides",
          r"$r_P=(y-\hat\mu)/\sqrt{\hat\phi V(\hat\mu)}$, the raw residual divided by its estimated standard deviation under the model. For binary or count data a plot of Pearson residuals is striped, because the response takes only a few values at each fitted mean; probability-integral residuals remove the stripes.",
          also=["06-pit-residuals.qmd: A Pearson plot of a binary or a count fit is striped"],
          links=["Pearson residuals?", "Pearson plots?"]),
    topic("Paired comparison", "05-comparisons-and-deviance.qmd#s-bradley-terry",
          r"Data in which items are compared two at a time, each comparison recording which one is preferred or wins. The Bradley–Terry model gives each item a strength and makes the log odds that $i$ beats $j$ the difference of their strengths.",
          links=["paired comparisons?"]),
    topic("Proportional-hazards model", "04-categorical-responses.qmd: gives a proportional-hazards model",
          r"A model in which covariates multiply the hazard by a constant factor at every time. In ordinal regression, replacing the logit by the complementary log-log in the cumulative model gives this form, and the coefficients are log hazard ratios, not log odds ratios.",
          links=["proportional[- ]hazards?(?: models?)?"]),
    topic("Vector-response regression", "10-plants-and-series.qmd: This chapter stays with a vector response",
          r"A regression in which each unit contributes a vector of responses, such as several species recorded at one site or two measurements on one patient. It needs a mean model for each component and a description of how the components are associated.",
          also=["09-marginal-models.qmd#s-two-responses-one-person"],
          links=["vector responses?", "multivariate responses?"]),
    topic("Cubic smoothing spline", "06-smooth-means.qmd: is a cubic spline with a knot at each distinct",
          r"The function that maximises a log-likelihood penalised by $\lambda\int g''(x)^2\,dx$. It is a piecewise cubic with a knot at every distinct $x_i$, with the function and its first two derivatives continuous at each knot. $\lambda=0$ interpolates; $\lambda\to\infty$ gives the straight line.",
          links=["cubic smoothing splines?", "smoothing splines?", "cubic splines?"]),
    topic("Spline", "06-smooth-means.qmd: is a cubic spline with a knot at each distinct",
          r"A piecewise polynomial whose pieces join smoothly at points called knots. A cubic spline has continuous first and second derivatives at each knot. Regression splines use a fixed, smaller set of knots and estimate their coefficients like any linear model.",
          also=["06-smooth-means.qmd: we use a smaller set of knots"],
          links=["splines?", "regression splines?", "penali[sz]ed splines?"], late=True),
    topic("Knot", "06-smooth-means.qmd: we use a smaller set of knots",
          r"A point where the pieces of a spline join. A smoothing spline puts a knot at every distinct $x$; in practice a smaller set, often ten equally spaced points or the deciles of $x$, is used.",
          links=["knots?"], scope=[S, G]),
    topic("Partially linear model", "07-additive-and-mixed.qmd: The compromise is a partially linear model",
          r"A regression with ordinary coefficients for the terms you want to interpret and smooth functions for the terms you only adjust for: $g(\mu)=\mathbf{x}^\top\boldsymbol\beta+f(z)$.",
          links=["partially linear models?", "semiparametric models?"]),
    topic("Effective degrees of freedom", "07-additive-and-mixed.qmd#s-sums-of-smooth-functions",
          r"The trace of the matrix that maps the responses to the fitted values of a penalised fit: the number of parameters a fitted smooth behaves as if it had. It falls as the smoothing parameter grows. Concept check [C33](../questions/c-33.qmd) asks about it.",
          also=["06-smooth-means.qmd: The software reports"],
          links=["effective degrees? of freedom", "effective number of parameters"]),
    topic("Restricted maximum likelihood", "08-random-intercepts.qmd: Restricted maximum likelihood, which removes the fixed mean",
          r"REML estimates variance components from the likelihood of contrasts that do not involve the fixed effects. It corrects the downward bias of maximum likelihood for variances, as the divisor $n-1$ does for a sample variance, and it is the default for linear mixed models.",
          links=["restricted maximum likelihood", "REML"]),
    topic("Intraclass correlation", "08-random-intercepts.qmd: Two people in the same block share",
          r"In a random-intercept model, the correlation between two responses in the same block, $\sigma_A^2/(\sigma_A^2+\sigma^2)$: the share of the total variance that lies between blocks. It is $0$ when blocks do not differ and near $1$ when the block effect swamps the rest.",
          links=["intra-?class correlations?", "within-block correlations?"]),
    topic("Linear mixed model", "08-random-intercepts.qmd: We generate the dependence with a mixed model",
          r"A linear model with fixed effects, shared across all the data, and random effects drawn afresh for each block, so that observations in one block are correlated: $\mathbf{y}=\mathbf{X}\boldsymbol\beta+\mathbf{Z}\mathbf{b}+\boldsymbol\varepsilon$. The random intercept is the simplest case.",
          also=["08-random-intercepts.qmd#s-a-random-intercept"],
          links=["linear mixed models?", "mixed models?", "mixed-effects models?"]),
    topic("Repeated measures", "08-random-intercepts.qmd: repeated measures on the same person",
          r"Several measurements on the same unit, over time or under different conditions. They are correlated within the unit, so they are not an independent sample; mixed models and marginal models describe that dependence.",
          links=["repeated measures", "repeated measurements", "longitudinal data"]),
    topic("Sandwich estimator", "09-marginal-models.qmd: a sandwich estimator replaces the model-based variance",
          r"A variance estimate for $\hat{\boldsymbol\beta}$ of the form $A^{-1}BA^{-1}$: model-based bread $A$ around an empirical meat $B$ built from the residuals. It stays consistent when the working variance is wrong, provided the mean model is right.",
          also=["09-marginal-models.qmd: The estimator solves the generalised estimating equations"],
          links=["sandwich (?:estimators?|variances?|standard errors?)", "robust standard errors?", "sandwich"]),
    topic("Generalised estimating equations", "09-marginal-models.qmd: The estimator solves the generalised estimating equations",
          r"Estimating equations $\sum_iD_i^\top V_i^{-1}(\mathbf{y}_i-\boldsymbol\mu_i)=\mathbf{0}$ for a marginal mean model, with a working covariance $V_i$ within each cluster. They are the quasi-score for dependent data; inference uses the sandwich variance, so the working correlation need not be right.",
          links=["generali[sz]ed estimating equations?", "GEEs?", "marginal estimating equations?"]),
    topic("Working correlation", "09-marginal-models.qmd: The working association does not have to be right",
          r"The correlation structure assumed within a cluster when fitting generalised estimating equations, such as independence or exchangeable. It need not be correct: the sandwich variance protects the standard errors, though a closer working correlation gives more efficient estimates.",
          links=["working correlations?", "working association", "working covariances?"]),
    topic("White noise", "12-time-series.qmd: White noise is the building block",
          r"A sequence of uncorrelated innovations with mean zero and constant variance. It is the building block of autoregressive and moving-average models, and a series that is white noise has no autocorrelation to exploit for forecasting.",
          links=["white noise"]),
    topic("Variogram", "12-time-series.qmd: The variogram looks at the change",
          r"$\operatorname{Var}(X_s-X_t)$ as a function of the times, equal to $2(\gamma_0-\gamma_{t-s})$ for a weakly stationary process. It can exist when the covariance function does not, because a difference can be well behaved when the level is not.",
          links=["variograms?"]),
    topic("Gaussian process", "12-time-series.qmd: If every finite subcollection is multivariate normal",
          r"A process whose every finite collection of values is multivariate normal, so that it is fixed by a mean function and a covariance function. A covariance that favours smooth paths acts like the roughness penalty of a smoothing spline.",
          links=["Gaussian process(?:es)?"]),
    topic("Autocorrelation function", "12-time-series.qmd: Weak stationarity asks only for two moments",
          r"For a weakly stationary series, $\rho_k=\gamma_k/\gamma_0$, the correlation between observations $k$ steps apart, plotted against $k$ as the ACF. A moving average of order $q$ has $\rho_k=0$ beyond lag $q$; an autoregression's autocorrelation decays instead.",
          also=["11-forecasting.qmd: The autocorrelation and the partial autocorrelation"],
          links=["autocorrelation functions?", "autocorrelations?", "ACF"]),
    topic("Partial autocorrelation", "11-forecasting.qmd: The autocorrelation and the partial autocorrelation",
          r"The correlation between $X_t$ and $X_{t-k}$ after removing the linear effect of the observations in between. An autoregression of order $p$ has partial autocorrelation zero beyond lag $p$, which is how the PACF suggests an order.",
          links=["partial autocorrelations?(?: functions?)?", "PACF"]),
    topic("Strict stationarity", "12-time-series.qmd: Strict stationarity says",
          r"A series is strictly stationary when every block of observations has the same joint distribution as the same block shifted in time. The path changes; the distribution does not.",
          links=["strict(?:ly)? stationar(?:y|ity)"]),
    topic("Weak stationarity", "12-time-series.qmd: Weak stationarity asks only for two moments",
          r"A series is weakly, or second-order, stationary when its mean is constant and $\operatorname{Cov}(X_s,X_t)$ depends only on $t-s$. A Gaussian series that is weakly stationary is strictly stationary.",
          links=["weak(?:ly)? stationar(?:y|ity)", "second-order stationar(?:y|ity)", "covariance stationar(?:y|ity)"]),
    topic("Time series", "12-time-series.qmd: A time series is dependent because",
          r"Observations of one quantity in time order, $X_1,X_2,\ldots,X_T$. Neighbouring values are dependent, so a series is one realisation of a process, not an independent sample, and stationarity is what makes the dependence estimable.",
          links=["time series"], late=True),
    topic("ARIMA model", "11-forecasting.qmd: auto.arima",
          r"An autoregressive integrated moving-average model: an ARMA model fitted to a series after differencing it $d$ times. A seasonal ARIMA also differences, and models, at a seasonal lag such as $12$ for monthly data. Concept check [C47](../questions/c-47.qmd) asks about unit roots and ARIMA.",
          links=["ARIMA(?: models?)?", "auto\\.arima", "seasonal ARIMA"]),
    topic("Unit root", "11-forecasting.qmd:",
          r"An autoregression has a unit root when its characteristic polynomial has a root at $1$, as the random walk $X_t=X_{t-1}+\varepsilon_t$ does. The series is then not stationary, its variance grows with time, and differencing it once removes the root. Concept check [C47](../questions/c-47.qmd) asks about it.",
          links=["unit roots?"]),
    topic("Seasonality", "11-forecasting.qmd: That is the seasonality",
          r"A pattern that repeats with a fixed period, such as twelve months. It shows as oscillation of the autocorrelation at multiples of the period, and it is removed by seasonal differencing or modelled at the seasonal lag.",
          links=["seasonality", "seasonal effects?", "seasonal patterns?"]),
    topic("Trend", "11-forecasting.qmd: The overall level is not a straight trend",
          r"Slow change in the level of a series. A deterministic trend is a fixed function of time; a stochastic trend, as in a random walk, wanders and is removed by differencing rather than by subtracting a line.",
          links=["trends?"], scope=[T], late=True),
    topic("Cycle", "11-forecasting.qmd: A twelve-month cycle is the obvious feature",
          r"A repeating rise and fall in a series. A cycle of fixed period, such as twelve months, is seasonality; cycles of varying length, such as business cycles, are not, and a seasonal model does not capture them.",
          links=["cycles?"], scope=[T], late=True),
    topic("Point forecast", "11-forecasting.qmd: returns a point forecast and a prediction interval",
          r"A single predicted value of a future observation, usually the conditional mean given the series so far. It should be reported with a prediction interval, which widens with the forecast horizon.",
          links=["point forecasts?", "forecasts?", "forecast horizons?"], scope=[T, B]),
    topic("ARCH and GARCH models", "11-forecasting.qmd: Autoregressive conditional heteroscedasticity",
          r"Autoregressive conditional heteroscedasticity: models in which the variance of today's innovation depends on yesterday's squared innovations (ARCH) and, in GARCH, also on yesterday's conditional variance. They describe volatility clustering in financial returns. The course names them and does not develop them; concept check [C50](../questions/c-50.qmd) asks about them.",
          links=["ARCH", "GARCH", "autoregressive conditional heterosc[a-z]+"]),
]

ALIASES.update({
    "AIC": "akaike-information-criterion",
    "BIC": "bayesian-information-criterion",
    "Quasi-score": "quasi-score-and-quasi-likelihood",
    "Generalised additive model": "sums-of-smooth-functions",
    "Additive model": "sums-of-smooth-functions",
    "Random effect": "fixed-and-random-effects",
    "Fixed effect": "fixed-and-random-effects",
    "Random slope": "random-slopes",
    "Robust standard error": "sandwich-estimator",
    "Autocorrelation": "autocorrelation-function",
    "Log-odds": "logit-link",
    "Probit regression": "probit-link",
    "Mixed model": "linear-mixed-model",
    "Burn data": "two-responses-one-person",
    "Unit roots": "unit-root",
})


# ---------------------------------------------------------------------------
# Named topics: Statistical learning
# ---------------------------------------------------------------------------

TOPICS += [
    topic("Dendrogram", "sl-07-linkage-and-density.qmd: A height in a dendrogram is the linkage dissimilarity",
          r"The tree diagram of a hierarchical clustering: leaves are observations, and each join is drawn at the dissimilarity at which two clusters merged. Cutting it at one height gives a partition. The heights belong to the linkage rule and the sample, not to any probability model.",
          also=["sl-07-linkage-and-density.qmd#s-agglomerative-and-divisive-clustering"],
          links=["dendrograms?"]),
    topic("Single linkage", "sl-07-linkage-and-density.qmd#s-properties-of-the-linkages",
          r"In hierarchical clustering, the dissimilarity between two clusters is the smallest dissimilarity between a member of one and a member of the other. It follows long, thin clusters and is prone to chaining, where a string of close points joins two distant groups.",
          also=["sl-07-linkage-and-density.qmd: Single linkage and complete linkage, defined below"],
          links=["single[- ]linkage", "nearest-neighbour linkage", "chaining"]),
    topic("Complete linkage", "sl-07-linkage-and-density.qmd#s-properties-of-the-linkages",
          r"In hierarchical clustering, the dissimilarity between two clusters is the largest dissimilarity between a member of one and a member of the other. It favours compact clusters of similar diameter and resists chaining.",
          links=["complete[- ]linkage", "furthest-neighbour linkage"]),
    topic("Average linkage", "sl-07-linkage-and-density.qmd: Average linkage, in the group-average sense",
          r"In hierarchical clustering, the dissimilarity between two clusters is the average of all dissimilarities between a member of one and a member of the other, $d_A(D_1,D_2)=\frac{1}{|D_1||D_2|}\sum_{x\in D_1}\sum_{y\in D_2}d(x,y)$. It is a compromise between single and complete linkage.",
          links=["average[- ]linkage", "group[- ]average linkage"]),
    topic("Ward's method", "sl-07-linkage-and-density.qmd#s-linkage-and-bandwidth-are-part-of-the-analysis",
          r"Agglomerative clustering that at each step merges the two clusters whose union least increases the total within-cluster sum of squares, the criterion k-means minimises. In R it is `hclust(..., method = \"ward.D2\")`.",
          links=["Ward's method", "Ward's linkage", "ward\\.D2"]),
    topic("Epanechnikov kernel", "sl-07-linkage-and-density.qmd: The Epanechnikov kernel has bounded support",
          r"The kernel $K(u)=\tfrac34(1-u^2)$ on $[-1,1]$, which has bounded support, so a point contributes nothing beyond a finite radius. It minimises asymptotic mean integrated squared error among kernels, though the bandwidth matters far more than the kernel.",
          links=["Epanechnikov(?: kernels?)?"]),
    topic("Gaussian kernel", "sl-07-linkage-and-density.qmd: The normal kernel is the usual multivariate default",
          r"In density estimation, the standard normal density used as the kernel, with support the whole space. In a support vector machine, the radial basis kernel $k(\mathbf{x},\mathbf{x}')=\exp\{-\|\mathbf{x}-\mathbf{x}'\|^2/(2\sigma^2)\}$.",
          also=["sl-17-support-vectors.qmd#s-common-kernels"],
          links=["Gaussian kernels?", "normal kernels?"]),
    topic("Radial basis function kernel", "sl-17-support-vectors.qmd#s-common-kernels",
          r"$k(\mathbf{x},\mathbf{x}')=\exp\{-\|\mathbf{x}-\mathbf{x}'\|^2/(2\sigma^2)\}$, the default kernel of a support vector machine. Its feature space is infinite-dimensional. The width $\sigma$ (or $\gamma=1/(2\sigma^2)$) sets how local the boundary is and is tuned inside the training data.",
          also=["sl-17-support-vectors.qmd#s-tune-a-radial-kernel-inside-the-training-data"],
          links=["radial basis (?:function )?kernels?", "radial kernels?", "RBF kernels?"]),
    topic("Polynomial kernel", "sl-17-support-vectors.qmd#s-common-kernels",
          r"$K(\mathbf{x}_i,\mathbf{x}_j)=(1+\mathbf{x}_i^\top\mathbf{x}_j)^d$, the inner product of a feature map containing all monomials up to degree $d$, of dimension $\binom{p+d}{d}$. The quadratic kernel, $d=2$, separates XOR.",
          also=["sl-17-support-vectors.qmd#exm-sl-17-quadratic-kernel"],
          links=["polynomial kernels?", "quadratic kernels?"]),
    topic("Gram matrix", "sl-17-support-vectors.qmd: The necessary and sufficient condition is symmetry",
          r"The $n\times n$ matrix of kernel values $K_{ij}=K(\mathbf{x}_i,\mathbf{x}_j)$ on a sample. A function is a valid kernel exactly when every such matrix is symmetric and positive semi-definite, which is what keeps the support vector dual convex.",
          links=["Gram matri(?:x|ces)"]),
    topic("Dual problem", "sl-17-support-vectors.qmd: The dual problem is identical to the separable case",
          r"The optimisation over Lagrange multipliers obtained from a constrained primal problem. For the support vector machine the dual depends on the data only through inner products $\mathbf{x}_i^\top\mathbf{x}_j$, which is what lets a kernel replace them.",
          also=["sl-17-support-vectors.qmd#s-the-dual"],
          links=["dual problems?", "Lagrangian dual", "duality"], scope=[L]),
    topic("Gradient boosting", "sl-13-ensembles.qmd: gradient boosting",
          r"Boosting seen as gradient descent in function space: each new base learner is fitted to the negative gradient of the loss at the current fit and added with a small step. AdaBoost is the case of exponential loss; other losses give boosting for regression or for logistic loss.",
          also=["sl-13-ensembles.qmd#s-the-weight-update-is-a-stagewise-step"],
          links=["gradient boosting", "boosted trees?"]),
    topic("Bagging", "sl-13-ensembles.qmd#s-bagging-and-random-forests",
          r"Bootstrap aggregating: fit the same learner to many bootstrap resamples of the training data and average the predictions, or take a vote. It reduces variance, most for unstable learners such as deep trees, and leaves the bias as it was.",
          also=["sl-13-ensembles.qmd: Bagging creates those versions by bootstrap resampling"],
          links=["bagging", "bagged", "bootstrap aggregat(?:ion|ing)"]),
    topic("Ensemble method", "sl-13-ensembles.qmd: combine their predictions",
          r"A predictor that combines many fitted models by averaging or voting. It helps when the members are individually reasonable and their errors disagree; bagging, random forests and boosting are the main constructions.",
          also=["sl-13-ensembles.qmd#s-why-averaging-helps"],
          links=["ensembles?", "ensemble methods?", "committees?"], scope=[L], late=True),
    topic("Variable importance", "sl-13-ensembles.qmd#s-out-of-bag-estimation-and-variable-importance",
          r"A random-forest summary of how much each predictor contributes, such as the rise in out-of-bag error when that predictor's values are randomly permuted. It describes the fitted forest's use of a variable, not a causal effect.",
          links=["variable importances?", "importance measures?"]),
    topic("Decision stump", "sl-13-ensembles.qmd#exm-sl-13-stumps",
          r"A classification tree with a single split: a threshold on one variable and a sign. A stump is a weak learner, only a little better than chance, which is what boosting combines into a strong one.",
          links=["decision stumps?", "stumps?"], scope=[L]),
    topic("Decision tree", "sl-12-classification-trees.qmd#s-building-a-tree",
          r"A predictor that partitions the input space by a sequence of binary splits on single variables and predicts a constant in each final region: a class for a classification tree, a mean for a regression tree. It is grown greedily, one split at a time, and then pruned.",
          links=["decision trees?", "classification trees?", "CART"]),
    topic("Regression tree", "sl-12-classification-trees.qmd: The price of the readable partition",
          r"A tree whose leaves predict a numerical response by the mean of the training responses in the leaf. It is grown by choosing at each node the split that most reduces the residual sum of squares, and pruned like a classification tree.",
          links=["regression trees?"]),
    topic("Gini index", "sl-12-classification-trees.qmd: Gini index",
          r"A node impurity, $I_G(m)=\sum_g\hat p_{mg}(1-\hat p_{mg})=1-\sum_g\hat p_{mg}^2$: the probability that two cases drawn at random from the node fall in different classes. It is $0$ for a pure node and largest when the classes are equally represented.",
          links=["Gini (?:index|impurity|indices)"]),
    topic("Cross-entropy", "sl-12-classification-trees.qmd: Gini index",
          r"For class proportions $\hat p_g$, the impurity $-\sum_g\hat p_g\log\hat p_g$ (the entropy of the node). As a loss for predicted probabilities $s_k$ and a one-hot target it is $-\sum_ky_k\log s_k$, which with a softmax output is the multinomial negative log-likelihood.",
          also=["sl-16-networks-in-practice.qmd#s-output-coding-softmax-and-cross-entropy"],
          links=["cross-entropy(?: loss)?", "entropy impurity", "deviance impurity"]),
    topic("Cost-complexity pruning", "sl-12-classification-trees.qmd: The CART cost-complexity criterion",
          r"Pruning a large tree by minimising the sample-weighted leaf impurity plus $\alpha$ times the number of leaves. Each $\alpha$ selects a subtree, the subtrees are nested as $\alpha$ grows, and $\alpha$ is chosen by cross-validation.",
          also=["sl-12-classification-trees.qmd#s-laboratory-prune-using-training-cross-validation"],
          links=["cost-complexity(?: pruning| criterion)?", "complexity parameter"]),
    topic("Surrogate split", "sl-12-classification-trees.qmd: CART can use surrogate splits",
          r"A split on another observed variable chosen to mimic the left–right allocation of a node's primary split. CART uses surrogates to send a case whose primary variable is missing down the tree.",
          links=["surrogate splits?"]),
    topic("Training set", "sl-09-error-rates.qmd: Scoring the training sample is easy",
          r"The data used to fit a model. Error measured on the same data, the apparent error, is optimistic because those cases helped choose the rule. An honest assessment uses cases excluded from every decision that built the predictor, including preprocessing and tuning.",
          also=["sl-16-networks-in-practice.qmd#s-training-validation-and-test-sets"],
          links=["training sets?", "training samples?", "training data"]),
    topic("Validation set", "sl-16-networks-in-practice.qmd: divided into a training set, a validation set, and a test set",
          r"Data held out from fitting and used to choose tuning parameters or to decide when to stop training. Because it is used for choices, it is not an honest estimate of final performance; a separate test set, untouched until the end, is.",
          also=["sl-09-error-rates.qmd#s-nested-cross-validation"],
          links=["validation sets?", "validation data"]),
    topic("Sensitivity and specificity", "sl-09-error-rates.qmd#s-a-confusion-matrix",
          r"Sensitivity is the proportion of truly positive cases that a classifier labels positive; specificity is the proportion of truly negative cases it labels negative. Both are read off a confusion matrix, and moving a decision threshold trades one against the other.",
          links=["sensitivity and specificity", "specificity", "true positive rates?", "false positive rates?"], scope=[L]),
    topic("Classification accuracy", "sl-09-error-rates.qmd: If one cross-validation error both picks the best",
          r"The proportion of cases classified correctly, one minus the error rate. With unbalanced classes it can be high for a rule that never predicts the rare class, and the accuracy of a model chosen as the best of many is optimistic unless it is assessed on separate data.",
          links=["classification accuracy", "accuracy"], scope=[L], late=True),
    topic("Overfitting", "sl-16-networks-in-practice.qmd: **Overfitting.**",
          r"Fitting the training data so closely that noise is learned as if it were structure: the training error keeps falling while the error on new data rises. Regularisation, early stopping and tuning on held-out data guard against it.",
          also=["sl-09-error-rates.qmd#s-the-apparent-error"],
          links=["over-?fitting", "over-?fit", "over-?fitted"]),
    topic("Underfitting", "sl-16-networks-in-practice.qmd: **Underfitting.**",
          r"A model too simple, trained too little, or given too little data to capture the structure, so that the error is high on the training data and on new data alike.",
          links=["under-?fitting", "under-?fit"]),
    topic("Early stopping", "sl-16-networks-in-practice.qmd: Validation, early stopping, and weight decay",
          r"Stopping gradient-descent training when the error on a validation set stops falling, before the training error reaches its minimum. It acts as a regulariser, much like weight decay.",
          also=["sl-16-networks-in-practice.qmd#s-generalisation"],
          links=["early stopping", "stopping rules?"]),
    topic("One-hot encoding", "sl-16-networks-in-practice.qmd: Let the target be a one-hot vector",
          r"Coding a categorical variable with $K$ levels as $K$ indicator variables, exactly one of which is $1$. A network with a softmax output is trained against this coding; for predictors in a linear model one level is usually dropped to avoid redundancy.",
          links=["one-hot(?: encoding| vectors?| coding)?"]),
    topic("Stochastic gradient descent", "sl-16-networks-in-practice.qmd: Online stochastic gradient descent samples",
          r"Gradient descent that updates the weights using the gradient of one observation's loss, or of a small batch, chosen at random. Each step is cheap and noisy but unbiased for the full gradient; with a decreasing learning rate it converges under conditions.",
          also=["sl-16-networks-in-practice.qmd#s-batch-and-online-learning"],
          links=["stochastic gradient descent", "SGD", "online learning", "online gradient descent"]),
    topic("Epoch", "sl-16-networks-in-practice.qmd: whether to update after every pattern or after every epoch",
          r"One pass through the whole training set in iterative training. Batch learning updates the weights once per epoch; online learning updates after every pattern, many times per epoch.",
          also=["sl-15-backpropagation.qmd: epoch"],
          links=["epochs?"]),
    topic("Mini-batch", "sl-16-networks-in-practice.qmd: A mini-batch shares this benefit",
          r"A small random subset of the training data whose average gradient is used for one weight update. It sits between full-batch and one-observation online learning: cheaper than a full pass, less noisy than a single case.",
          links=["mini-?batch(?:es)?"]),
    topic("Learning rate", "sl-15-backpropagation.qmd#s-gradient-descent",
          r"The step size $\eta$ in a gradient-descent update $\mathbf{w}\leftarrow\mathbf{w}-\eta\,\nabla E(\mathbf{w})$. Too large and the error oscillates or diverges; too small and training crawls. A fixed rate leaves stochastic gradient descent fluctuating near a solution.",
          links=["learning rates?", "step sizes?"], scope=[L]),
    topic("Activation function", "sl-14-neural-units.qmd: Two activations are used here",
          r"The fixed function a neural unit applies to its weighted input: the step function of the threshold unit, or the logistic sigmoid used when the weights are trained by gradient descent. A non-linear activation is what lets a hidden layer represent functions a single linear score cannot.",
          also=["sl-14-neural-units.qmd: An artificial neuron is that hyperplane followed by an activation"],
          links=["activation functions?", "activations?"], scope=[L]),
    topic("Sigmoid function", "sl-14-neural-units.qmd: Two activations are used here",
          r"The logistic function $g(z)=1/(1+e^{-z})$, which maps the real line onto $(0,1)$. It is a smooth stand-in for a threshold, its derivative is $g(z)\{1-g(z)\}$, and a sigmoid output with no hidden layer is a logistic regression.",
          links=["sigmoids?", "sigmoid functions?", "logistic functions?", "expit"]),
    topic("Factor analysis", "sl-03-principal-components.qmd: Factor analysis",
          r"A probability model that writes the observed variables as linear combinations of a few unobserved factors plus independent variable-specific noise. Unlike principal components it models the covariance, not just the variance directions; the course names it as a relative of PCA and does not develop it.",
          links=["factor analys[ie]s"], scope=[L]),
    topic("Non-negative matrix factorisation", "sl-03-principal-components.qmd: Factor analysis",
          r"Approximating a non-negative data matrix by the product of two low-rank non-negative matrices, so that components add up parts rather than cancel. It is named in the course as an alternative to principal components.",
          links=["non-?negative matrix factori[sz]ations?", "NMF"]),
    topic("Loadings", "sl-03-principal-components.qmd: The leading two correlation loadings",
          r"The coefficients of the variables in a principal component, the entries of its unit direction vector. A large loading means the variable carries weight in that component; signs are arbitrary, since a direction and its negative describe the same component.",
          links=["loadings?", "component loadings?"], scope=[L]),
    topic("Scree plot", "sl-03-principal-components.qmd: A scree plot offers a visual heuristic",
          r"A plot of the eigenvalues, the component variances, in decreasing order. A bend after which they level off is an informal guide to how many principal components to keep; it can be ambiguous, and it does not validate a predictive model.",
          links=["scree plots?", "scree"]),
    topic("Eigenvalues and eigenvectors", "sl-03-principal-components.qmd: The stationary points are the eigenvectors of",
          r"For a symmetric matrix $S$, $S\mathbf{a}=\lambda\mathbf{a}$ with $\mathbf{a}\ne\mathbf{0}$. The eigenvalues are real and the eigenvectors can be chosen orthonormal. For a covariance matrix the eigenvectors are the principal component directions and the eigenvalues the variances along them.",
          also=["sl-01-multivariate-normal.qmd#s-level-sets-are-ellipsoids"],
          links=["eigenvalues?", "eigenvectors?", "spectral decompositions?", "eigen-?decompositions?"]),
    topic("Adjusted Rand index", "sl-04-kmeans.qmd: The adjusted Rand index compares the clustering",
          r"A measure of agreement between two partitions of the same items, built from the pairs placed together or apart in both and corrected for chance, so that identical partitions score $1$ and random labelling scores about $0$. It does not need cluster $1$ to mean class $1$.",
          also=["sl-07-linkage-and-density.qmd#s-linkage-and-bandwidth-are-part-of-the-analysis"],
          links=["adjusted Rand(?: index)?", "Rand index"]),
    topic("Hartigan–Wong algorithm", "sl-04-kmeans.qmd: The default `kmeans` uses the Hartigan–Wong algorithm",
          r"The default k-means algorithm in R. It targets the same within-cluster sum of squares as Lloyd's algorithm but moves single points between clusters whenever that lowers the criterion, which lets it escape some of Lloyd's local optima.",
          links=["Hartigan–Wong(?: algorithm)?"]),
    topic("Label switching", "sl-05-mixtures-em.qmd: **Label switching.**",
          r"Renaming the components of a mixture changes the parameter vector and leaves the density unchanged, so a fitted mixture is identified only up to a permutation of labels. Comparing component parameters across fits, or across MCMC draws, needs a rule for matching labels.",
          links=["label[- ]switching"]),
    topic("EM algorithm", "sl-05-mixtures-em.qmd#s-the-e-and-m-steps",
          r"An iterative method for maximum likelihood with missing or latent data. The E step computes the expected complete-data log-likelihood given the current parameters; the M step maximises it. No iteration decreases the observed-data likelihood, but the limit can be a local maximum, so several starts are used.",
          also=["sl-05-mixtures-em.qmd#s-why-the-likelihood-never-decreases"],
          links=["EM algorithms?", "expectation[–-]maximi[sz]ation", "EM"]),
    topic("Missing data", "sl-05-mixtures-em.qmd: The equation does identify the missing data",
          r"Values that were meant to be observed and were not. The EM algorithm treats a mixture's component labels as missing data: with them the complete-data likelihood is easy to maximise, and the E step replaces them by their conditional probabilities.",
          links=["missing data", "missing values?", "latent variables?"]),
    topic("Identifiability", "sl-05-mixtures-em.qmd: Finite Gaussian mixtures with distinct components",
          r"A parameter is identifiable when different values give different distributions of the data. A mixture's labels, the effects of every level of a factor alongside an intercept, and the hidden units of a network are unidentified until a constraint fixes them.",
          also=["da-06-anova-examples.qmd: The parameters are not all identifiable as written"],
          links=["identifiab(?:le|ility)", "non-?identifiab(?:le|ility)", "unidentified"]),
    topic("Gibbs' inequality", "sl-05-mixtures-em.qmd: Gibbs' inequality is nonnegativity",
          r"For probability vectors $p$ and $q$, $\sum_ip_i\log p_i\ge\sum_ip_i\log q_i$, with equality only when $p=q$: the Kullback–Leibler divergence is never negative. It is the step in the proof that an EM iteration never decreases the likelihood.",
          links=["Gibbs' inequality"]),
    topic("Cholesky decomposition", "sl-02-normal-inference.qmd: and the Cholesky factor",
          r"The factorisation $\Sigma=LL^\top$ of a positive-definite matrix with $L$ lower triangular. If $\mathbf{Z}\sim\mathrm{N}_p(\mathbf{0},I)$ then $\boldsymbol\mu+L\mathbf{Z}\sim\mathrm{N}_p(\boldsymbol\mu,\Sigma)$, which is how correlated normal vectors are drawn.",
          links=["Cholesky(?: decompositions?| factori[sz]ations?| factors?)?"]),
    topic("Sylvester's criterion", "sl-01-multivariate-normal.qmd: Sylvester's criterion turns the quadratic-form condition",
          r"A symmetric matrix is positive definite exactly when all its leading principal minors are positive. Positive semi-definiteness needs every principal minor non-negative, not only the leading ones.",
          links=["Sylvester's criterion"]),
    topic("Positive definite matrix", "sl-01-multivariate-normal.qmd: Sylvester's criterion turns the quadratic-form condition",
          r"A symmetric matrix $\Sigma$ with $\mathbf{a}^\top\Sigma\mathbf{a}>0$ for every non-zero $\mathbf{a}$; positive semi-definite when $\ge0$. Every covariance matrix is positive semi-definite, because $\mathbf{a}^\top\Sigma\mathbf{a}$ is the variance of $\mathbf{a}^\top\mathbf{X}$.",
          links=["positive[- ]definite", "positive semi-?definite", "non-?negative definite"]),
    topic("Behrens–Fisher problem", "sl-02-normal-inference.qmd: the multivariate Behrens–Fisher problem",
          r"Comparing two normal means when the two variances are unknown and not assumed equal. There is no exact pivot; Welch's approximation is the usual univariate answer, and the same difficulty returns for two mean vectors with unequal covariance matrices.",
          also=["da-04-estimation-examples.qmd#s-two-samples-with-unequal-variances"],
          links=["Behrens–Fisher(?: problem)?"]),
    topic("Cover–Hart bound", "sl-11-nearest-neighbours.qmd: gives the sharper Cover–Hart bound",
          r"As the training sample grows, the error rate $R$ of the one-nearest-neighbour rule satisfies $R^*\le R\le2R^*(1-R^*)$ for two classes, where $R^*$ is the Bayes error: at most twice the best achievable.",
          links=["Cover–Hart(?: bound)?"]),
    topic("Complete separation", "sl-10-logistic-regression.qmd: Complete separation is a concrete failure",
          r"When a hyperplane separates the two classes perfectly, the logistic log-likelihood has no maximum: it keeps rising toward $0$ as the coefficients grow without bound, and fitted probabilities approach $0$ and $1$. Software reports huge coefficients and standard errors.",
          links=["complete separation", "quasi-complete separation", "perfect separation"], scope=[L, G]),
    topic("Brier score", "sl-10-logistic-regression.qmd: The Brier score below scores the probabilities",
          r"The mean squared difference between predicted probabilities and the $0$–$1$ outcomes, $\frac1n\sum_i(\hat p_i-y_i)^2$. It rewards calibrated probabilities, not just correct classifications.",
          links=["Brier scores?"]),
    topic("Precision matrix", "sl-19-graphical-models.qmd: corresponds to a zero off-diagonal entry of the precision matrix",
          r"The inverse $K=\Sigma^{-1}$ of a covariance matrix. For a multivariate normal, $K_{ij}=0$ exactly when variables $i$ and $j$ are conditionally independent given the rest, and $-K_{ij}/\sqrt{K_{ii}K_{jj}}$ is their partial correlation.",
          links=["precision matri(?:x|ces)", "concentration matri(?:x|ces)", "inverse covariance"]),
    topic("Clique", "sl-19-graphical-models.qmd: A complete subset that is maximal",
          r"A complete subset of a graph's vertices, every pair joined by an edge, that cannot be enlarged. By the Hammersley–Clifford theorem a positive density is Markov with respect to a graph exactly when it factorises into functions of the cliques.",
          links=["cliques?"]),
    topic("Separating set", "sl-19-graphical-models.qmd#s-graph-terminology",
          r"A set $S$ of vertices separates $A$ from $B$ in a graph when every path from $A$ to $B$ passes through $S$. The global Markov property says that then $X_A$ and $X_B$ are conditionally independent given $X_S$.",
          also=["sl-19-graphical-models.qmd#s-markov-properties-and-factorisation"],
          links=["separating sets?", "re:separates (?=\\$)"], scope=[L]),
    topic("Markov random field", "sl-19-graphical-models.qmd: also known as Markov random fields",
          r"Another name for an undirected graphical model: random variables whose joint law satisfies the Markov properties of a graph, so that a missing edge means conditional independence given the rest.",
          links=["Markov random fields?", "undirected graphical models?"]),
    topic("Multicollinearity", "sl-18-high-dimensional.qmd: substantial multicollinearity",
          r"Strong linear dependence among predictors. It makes $\mathbf{X}^\top\mathbf{X}$ nearly singular, so least-squares coefficients become unstable with large standard errors; when $p>n$ the matrix is exactly singular. Ridge regression was introduced for it.",
          links=["multi-?collinearity", "collinearity", "collinear"]),
    topic("Sparsity", "sl-18-high-dimensional.qmd#s-why-the-penalty-gives-zeros",
          r"A model is sparse when only a few of its parameters are non-zero. Sparsity is what makes estimation possible when $p>n$; the lasso and the graphical lasso exploit it by setting coefficients exactly to zero.",
          also=["sl-18-high-dimensional.qmd#s-a-sparse-simulation-where-the-truth-is-known"],
          links=["sparsity", "sparse"], scope=[L]),
    topic("Regularisation", "sl-18-high-dimensional.qmd: Regularisation adds a preference among competing fits",
          r"Adding a penalty on the size or roughness of the parameters to the fitting criterion, so that the fit trades goodness of fit against complexity: ridge ($L^2$), the lasso ($L^1$), weight decay in networks, the roughness penalty of a smoothing spline. A Bayesian prior has the same effect, with the MAP estimate as the penalised fit.",
          also=["sl-16-networks-in-practice.qmd#s-regularisation-and-weight-decay", "bayes-09-linear-regression.qmd#s-informative-priors-and-regularisation"],
          links=["regulari[sz]ation", "regulari[sz]ed", "penali[sz]ation", "penali[sz]ed"]),
    topic("Ridge regression", "sl-18-high-dimensional.qmd#s-least-squares-ridge-and-the-lasso-objective",
          r"Least squares with an $L^2$ penalty, $\hat{\boldsymbol\beta}=\arg\min\|\mathbf{y}-\mathbf{X}\boldsymbol\beta\|^2+\lambda\|\boldsymbol\beta\|^2=(\mathbf{X}^\top\mathbf{X}+\lambda I)^{-1}\mathbf{X}^\top\mathbf{y}$. It shrinks coefficients toward zero without setting any to zero, works when $p>n$, and is the posterior mode under a centred normal prior.",
          also=["bayes-09-linear-regression.qmd: A centred normal prior also explains ridge regularisation", "sl-16-networks-in-practice.qmd: just as ridge regression does"],
          links=["ridge regressions?", "ridge regulari[sz]ation", "ridge penalt(?:y|ies)", "ridge"]),
    topic("High-dimensional data", "sl-18-high-dimensional.qmd#s-why-classical-methods-fail-when",
          r"Data with more variables than observations, $p>n$, or $p$ close to $n$: thousands of gene-expression values on a few dozen tissue samples. The sample covariance is singular, least squares has no unique solution, and testing every variable creates a multiple-testing problem.",
          links=["high-dimensional (?:data|statistics|analysis|problems?|settings?)", "p *> *n"]),
    topic("Iris data", "sl-01-multivariate-normal.qmd#s-one-species-or-three",
          r"Measurements of sepal length, sepal width, petal length and petal width, in centimetres, on 150 iris flowers, 50 from each of three species: setosa, versicolor and virginica. Edgar Anderson collected them; Fisher's 1936 paper on discriminant analysis made them famous. The statistical-learning chapters use it throughout, from the multivariate normal and Hotelling's test to clustering, discriminant analysis, logistic regression and a small network.",
          also=["sl-02-normal-inference.qmd#s-a-joint-mean-test-for-setosa", "sl-03-principal-components.qmd#s-iris-with-and-without-scaling",
                "sl-04-kmeans.qmd#s-do-three-clusters-recover-three-species", "sl-05-mixtures-em.qmd#s-iris-membership",
                "sl-08-discriminant-analysis.qmd#s-lda-and-qda-on-held-out-iris-flowers", "sl-10-logistic-regression.qmd#s-laboratory-odds-and-probabilities-for-two-iris-species",
                "sl-16-networks-in-practice.qmd#s-a-small-softmax-network-for-iris"],
          links=["iris data(?: ?sets?)?", "iris flowers?", "Fisher's iris"]),
    topic("Heart-failure data", "da-02-descriptive-statistics.qmd: The running example is a study of 299 patients",
          r"Records of 299 patients after heart failure, all with severe weakness of the left ventricle, admitted to one hospital and followed for up to a year, with 13 measurements each, among them age, anaemia, serum creatinine and the ejection fraction. It runs through the descriptive-statistics chapter and returns in logistic regression.",
          also=["sl-10-logistic-regression.qmd#exm-sl-10-heart"],
          links=["heart[- ]failure (?:data|patients|study)"]),
]

ALIASES.update({
    "Mahalanobis distance": "squared-mahalanobis-distance",
    "Multinomial logit": "multinomial-logistic-regression",
    "Pruning": "tree-size-and-pruning",
    "Impurity": "node-impurity",
    "Gini impurity": "gini-index",
    "Entropy impurity": "cross-entropy",
    "Mercer's condition": "which-functions-are-kernels",
    "Hotelling's T-squared test": "hotelling-s-t2-test",
    "K-nearest neighbours": "nearest-neighbours",
    "Classification tree": "decision-tree",
    "Out-of-bag error": "out-of-bag-estimation-and-variable-importance",
    "Test set": "a-held-out-test-set",
    "Logistic sigmoid": "sigmoid-function",
    "Eigenvalue": "eigenvalues-and-eigenvectors",
    "Eigenvector": "eigenvalues-and-eigenvectors",
    "ACF": "autocorrelation-function",
    "Expectation–maximisation algorithm": "em-algorithm",
})


TOPICS += [
    topic("Kernel of a density", "bayes-01-foundations.qmd: recognition of a known density kernel",
          r"The part of a density that depends on the variable, with every constant factor dropped. A posterior is computed as a kernel, $p(\theta\mid y)\propto p(y\mid\theta)\,p(\theta)$, and recognising the kernel of a named family, such as $\theta^{a-1}(1-\theta)^{b-1}$ for a Beta, identifies the posterior without computing its normalising constant.",
          also=["bayes-03-normal-models.qmd#s-finding-the-conjugate-family-by-inspection"],
          links=["density kernels?", "likelihood kernels?", "posterior kernels?", "kernels?"], scope=[B], late=True),
]


# ---------------------------------------------------------------------------
# Links between pages that already exist. LINKS are tried before the build's
# own term list, so they hold long or part-specific phrases; LINKS_LAST hold
# single words that would otherwise steal a longer phrase.
# ---------------------------------------------------------------------------

LINKS += [
    link(["re:Pearson(?:['’]s)? (?:chi-squared )?statistics?", "Pearson's chi-squared"], "pearson-statistic"),
    # Cursor's list: phrases that name another chapter's idea.
    link("pure Poisson process", "poisson-distribution", scope=[G]),
    link("smoothing chapters", "S1", scope=[T]),
    link("clustered data", "C1"),
    link("proximity in space or time", "T1", scope=[C]),
    link("Poisson observation", "count-responses", scope=[T]),
    link("separate intercept for each block", "blocks-in-analysis-of-variance", scope=[C]),
    link("patients in different hospitals", "C1", scope=[D, I]),
    link("gamma clotting fit", "clotting-time-data", scope=[G]),
    link("burn data", "two-responses-one-person"),
    link("re:shape you are willing to write down", "S1", scope=[G]),
    link("re:Markov chains?", "discrete-time-markov-chain", scope=[T]),
    link("Markov chain Monte Carlo", "B4"),
    link("transition kernels?", "markov-chain", scope=[B]),
    # Model selection.
    link(["extended information criterion", "extended BIC", "EBIC"], "extended-information-criterion"),
    link(["AIC", "Akaike information criterion", "Akaike's criterion", "Akaike's information criterion"], "akaike-information-criterion"),
    link(["BIC", "Bayesian information criterion", "Schwarz criterion"], "bayesian-information-criterion"),
    link(["Kullback–Leibler divergence", "Kullback–Leibler", "KL divergence"], "kullback-leibler-divergence"),
    link(["Laplace approximation", "Laplace's method"], "laplace-approximation"),
    # Error rates and resampling.
    link(["re:[Kk][- ]fold(?: cross[- ]validation)?"], "fold-cross-validation"),
    link(["leave-one-out cross-validation", "leave-one-out", "LOOCV"], "leave-one-out-cross-validation"),
    link("nested cross-validation", "nested-cross-validation"),
    link(["cross-validation of the likelihood", "likelihood cross-validation"], "cross-validation-of-the-likelihood"),
    link(["cross-validation", "cross-validated", "cross-validate"], "cross-validation"),
    link(["apparent error", "apparent error rates?", "resubstitution error"], "apparent-error"),
    link(["confusion matrix", "re:confusion matrices"], "confusion-matrix"),
    link(["re:held[- ]out (?:test )?(?:sets?|data|samples?)", "test sets?", "test data"], "a-held-out-test-set", scope=[L]),
    link(["re:\\.632(?: correction| estimator)?"], "bootstrap-error-and-the-correction"),
    link(["bootstrap samples?", "bootstrap resamples?", "bootstrap estimates?", "bootstrapping", "bootstrapped"], "bootstrap"),
    link("jackknife", "jackknife"),
    link(["zero–one loss", "0–1 loss"], "zero-one-loss-and-risk"),
    # Classifiers.
    link(["Bayes classifier", "Bayes-optimal rule", "Bayes-optimal classifier", "Bayes error", "Bayes risk"], "bayes-classifier"),
    link(["Bayes rule"], "bayes-classifier", scope=[L], exclude=["sl-05-mixtures-em", "sl-06-model-selection"]),
    link(["linear discriminant analysis", "LDA"], "linear-discriminant-analysis"),
    link(["quadratic discriminant analysis", "QDA"], "quadratic-discriminant-analysis"),
    link(["re:Fisher['’]?s (?:linear )?discriminant(?: analysis)?", "Fisher's direction"], "fisher-s-linear-discriminant-analysis"),
    link("mixture discriminant analysis", "mixture-discriminant-analysis"),
    link("kernel density discriminant analysis", "kernel-density-discriminant-analysis"),
    link(["re:posterior class probabilit(?:y|ies)"], "posterior-class-probability"),
    link(["logistic regression"], "binary-logistic-regression", scope=[L]),
    link(["multinomial logistic regression", "multinomial logit"], "multinomial-logistic-regression", scope=[L]),
    link(["iteratively reweighted least squares", "IRLS"], "iteratively-reweighted-least-squares", scope=[L]),
    link(["decision boundary", "re:decision boundaries"], "interpretation-and-the-decision-boundary"),
    link(["rank distance"], "rank-distance"),
    link(["node impurity", "re:node impurities"], "node-impurity"),
    link(["random forest"], "random-forest"),
    link(["AdaBoost", "Real AdaBoost"], "adaboost"),
    link(["out-of-bag", "OOB"], "out-of-bag-estimation-and-variable-importance"),
    link("exponential loss", "exponential-loss"),
    link("hinge loss", "hinge-loss"),
    link(["squared error of an average", "ambiguity decomposition"], "squared-error-of-an-average"),
    link(["support vector machine", "SVM"], "L17"),
    link(["support vector", "re:support vectors"], "support-vectors-and-their-multipliers"),
    link(["slack variable"], "soft-margin-slack-variables"),
    link(["hard margin", "hard-margin"], "hard-margin-support-vector-machine"),
    link(["soft margin", "soft-margin"], "soft-margin-primal"),
    link(["kernel trick"], "kernel-trick"),
    link(["re:kernel density estimat(?:e|es|ion|or|ors)", "KDE"], "kernel-density-estimator"),
    link(["re:Vapnik['’]?s?(?: radius[–-]margin)?(?: bound)?"], "vapnik-s-radius-margin-bound"),
    link(["signed distance", "distance to a hyperplane"], "distance-to-a-hyperplane"),
    link(["perceptron learning rule", "perceptron rule"], "perceptron-learning-rule"),
    link(["perceptron"], "perceptron"),
    link(["neural network", "neural net", "multilayer perceptron", "feed-forward network", "feedforward network"], "L14"),
    link(["artificial neuron", "threshold unit", "neural unit", "McCulloch–Pitts"], "artificial-neuron"),
    link(["XOR", "exclusive or", "exclusive-or"], "xor-problem"),
    link(["hidden layer", "hidden unit"], "hidden-layer"),
    link(["universal approximation", "universal approximator"], "universal-approximation"),
    link(["backpropagation", "back-propagation", "backprop"], "L15"),
    link(["delta rule", "re:deltas?"], "delta-rule", scope=[L]),
    link(["weight decay"], "regularisation-and-weight-decay"),
    link(["weight initialisation", "weight initialization", "initial weights"], "weight-initialisation"),
    link(["softmax"], "output-coding-softmax-and-cross-entropy"),
    link(["local minima", "plateaus?"], "local-minima-plateaus-and-symmetry", scope=[L]),
    # Unsupervised learning.
    link(["principal component directions?", "principal component scores?"], "principal-component-directions-and-scores"),
    link(["principal components analysis", "principal component analysis", "PCA"], "L3"),
    link(["singular value decomposition", "SVD"], "singular-value-decomposition"),
    link(["Lloyd's algorithm", "Lloyd's k-means algorithm", "re:Lloyd['’]?s"], "lloyd-s-k-means-algorithm"),
    link(["gap statistic"], "choosing-k-the-gap-statistic"),
    link(["Voronoi", "Voronoi tessellation", "Voronoi cell"], "voronoi-tessellation"),
    link(["within-cluster sum of squares", "within-cluster scatter", "within-cluster variation"], "within-cluster-scatter"),
    link(["k-means"], "L4"),
    link(["hierarchical clustering", "agglomerative clustering"], "hierarchical-clustering"),
    link(["agglomerative", "divisive"], "agglomerative-and-divisive-clustering", scope=[L]),
    link(["finite mixture model", "finite mixture", "mixture model", "normal mixture", "Gaussian mixture"], "finite-mixture-model"),
    link(["complete-data likelihood", "complete-data log-likelihood"], "complete-data-likelihood"),
    link(["posterior membership", "re:responsibilit(?:y|ies)"], "posterior-membership"),
    link(["E step", "E-step"], "e-step"),
    link(["M step", "M-step"], "m-step"),
    # The multivariate normal and its tests.
    link(["multivariate central limit theorem"], "multivariate-central-limit-theorem"),
    link(["multinomial central limit theorem"], "multinomial-central-limit-theorem"),
    link(["re:multivariate normal(?: distributions?)?", "re:jointly normal", "re:bivariate normal(?: distributions?)?", "re:multivariate Gaussian"], "multivariate-normal-distribution-sl-01-multivariate-normal", scope=[L]),
    link(["Mahalanobis distance", "Mahalanobis"], "squared-mahalanobis-distance"),
    link(["Wishart distribution", "Wishart"], "wishart-distribution"),
    link(["two-sample Hotelling", "two-sample T² test"], "two-sample-hotelling-t2-test"),
    link(["re:Hotelling['’]?s(?: T(?:\\^2|²|-squared))?(?: tests?| statistics?)?"], "hotelling-s-t2-test"),
    link(["pooled covariance", "pooled covariance matrix"], "pooled-covariance"),
    link(["partial correlation"], "partial-correlation"),
    link(["re:conditional(?:ly)? independen(?:t|ce)"], "conditional-independence"),
    link(["Gaussian graphical model"], "gaussian-graphical-models"),
    link(["graphical lasso", "glasso"], "graphical-lasso"),
    link(["Hammersley–Clifford theorem", "Hammersley–Clifford"], "hammersley-clifford"),
    link(["undirected graph"], "undirected-graph"),
    link(["re:(?:pairwise|local|global) Markov propert(?:y|ies)"], "markov-properties-and-factorisation"),
    link(["Markov property", "re:Markov properties", "memoryless future"], "markov-property"),
    # High dimensions.
    link(["rank bound"], "rank-bound"),
    link(["Benjamini–Hochberg procedure", "Benjamini–Hochberg", "BH procedure", "step-up procedure"], "benjamini-hochberg"),
    link(["false discovery rate", "FDR"], "false-discovery-rate"),
    link(["logistic lasso"], "logistic-lasso"),
    link(["soft-thresholding", "soft thresholding"], "soft-thresholding-for-orthonormal-predictors"),
    link(["subset selection", "best subset"], "subset-selection-and-shrinkage"),
    # Stochastic processes.
    link(["continuous-time Markov chain", "continuous-time chain", "CTMC"], "SP7"),
    link(["discrete-time Markov chain"], "discrete-time-markov-chain"),
    link(["Little's law"], "little-s-law"),
    link(["re:generator matri(?:x|ces)", "infinitesimal generator", "generator"], "generator", scope=[SP]),
    link(["extinction probability", "re:extinction probabilities"], "extinction-probability"),
    link(["extinction criterion"], "extinction-criterion"),
    link(["offspring distribution", "offspring law", "offspring probability generating function"], "offspring-probability-generating-function"),
    link(["Galton–Watson process", "Galton–Watson branching", "branching process", "Galton–Watson"], "galton-watson-process"),
    link(["gambler's ruin"], "gambler-s-ruin"),
    link(["expected duration"], "expected-duration-of-a-random-walk"),
    link(["hitting probability", "re:hitting probabilities", "absorption probability", "re:absorption probabilities"], "hitting-probabilities"),
    link(["transition matrix", "re:transition matrices", "transition probability matrix"], "transition-matrix"),
    link(["communicating class", "closed class", "re:communicat(?:e|es|ion)"], "communicating-classes", scope=[SP, P]),
    link(["global balance"], "global-balance-and-detailed-balance"),
    link(["re:M/M/1/K", "re:M/M/c(?:/K)?", "re:M/M/2"], "multi-server-and-finite-capacity-queues"),
    link(["re:M/M/1"], "m-m-1-queue"),
    link(["re:M/M/∞"], "m-m-queue"),
    link(["re:birth[–-]death (?:chains?|process(?:es)?)"], "birth-death-balance"),
    link(["uniformisation", "uniformization"], "uniformisation"),
    link(["re:Kolmogorov['’]?s? (?:forward|backward)(?: and backward)? equations?", "re:Kolmogorov['’]?s equations", "forward equation", "backward equation"], "kolmogorov-forward-and-backward-equations", scope=[SP]),
    link(["superposition"], "superposition-and-thinning"),
    link(["thinning", "thinned"], "superposition-and-thinning", scope=[SP]),
    link(["spatial Poisson process", "re:Poisson process(?:es)? in the plane"], "spatial-poisson-process"),
    link(["re:non-?homogeneous Poisson process(?:es)?", "inhomogeneous Poisson process"], "nonhomogeneous-poisson-process"),
    link(["stochastic process"], "stochastic-process"),
    link(["probability space"], "probability-space"),
    link(["re:measurable (?:random variables?|functions?|maps?)", "measurability"], "measurable-random-variable"),
    link(["modes of convergence", "re:converg(?:es|ence) in probability", "re:converg(?:es|ence) in distribution",
          "re:almost sure(?:ly)? convergen(?:t|ce)", "re:converg(?:es|ence) almost surely", "re:converg(?:es|ence) in L\\^?p", "re:in mean square"], "modes-of-convergence"),
    link(["monotone convergence", "dominated convergence", "Fatou's lemma"], "monotone-convergence-fatou-and-dominated-convergence"),
    link(["strong law of large numbers", "strong law", "re:strong laws"], "strong-law"),
    link(["weak law of large numbers", "weak law"], "law-of-large-numbers"),
    link(["characteristic function"], "characteristic-functions"),
    link(["re:(?:stationary (?:and )?)?independent increments", "stationary increments"], "stationary-and-independent-increments"),
    link(["recurrence and period"], "recurrence-and-period"),
    link(["re:extreme[- ]value(?: theory| distributions?| laws?| classification)?"], "extreme-value-classification"),
    # Inference, Bayes, linear models.
    link(["normal linear model"], "normal-linear-model"),
    link(["simple linear regression"], "simple-linear-regression"),
    link(["confidence region"], "confidence-region-for-a-normal-mean-vector", scope=[L]),
    link(["Gibbs sampler", "Gibbs sampling", "Gibbs samplers"], "gibbs-sampling"),
    link(["systematic-scan", "systematic scan"], "systematic-scan-gibbs-sampler"),
    link(["Metropolis–Hastings algorithm", "Metropolis–Hastings sampler", "Metropolis–Hastings"], "metropolis-hastings-algorithm"),
    link(["grid approximation", "grid Monte Carlo"], "grid-monte-carlo-approximation"),
    link(["partial pooling", "complete pooling", "no pooling", "borrowing strength", "borrow strength"], "complete-pooling-no-pooling-and-partial-pooling"),
    link(["prior sensitivity", "sensitivity to the prior"], "prior-sensitivity"),
    link(["Bayes factors and posterior odds"], "bayes-factors-and-posterior-odds"),
    # GLMs and models for dependence.
    link(["re:ordinal (?:responses?|data|regressions?|categories|outcomes?)"], "ordinal-responses"),
    link(["re:nominal (?:responses?|categories|data|outcomes?)"], "nominal-responses"),
    link(["binary response"], "binary-responses-in-a-glm", scope=[G, C]),
    link(["re:count (?:data|responses?)"], "count-responses", scope=[G, C, T]),
    link(["positive continuous response"], "positive-continuous-responses"),
    link(["re:marginal and conditional effects?", "population-averaged", "population average", "subject-specific"], "marginal-and-conditional-effects"),
    link(["two-factor analysis of variance", "two-way analysis of variance", "two-way ANOVA"], "two-factor-analysis-of-variance"),
    link(["one-factor analysis of variance", "one-way analysis of variance", "one-way ANOVA"], "one-factor-analysis-of-variance"),
    link(["multiple comparisons"], "multiple-comparisons"),
    # Datasets that run through several chapters.
    link(["re:cholesterol (?:data|fit|example)"], "cholesterol-and-heart-disease"),
    link(["re:clotting(?:[- ]time)? (?:data|times|fit)"], "clotting-time-data"),
    link(["re:lidar(?: data)?"], "lidar-data"),
    link(["re:kyphosis(?: data)?"], "kyphosis-data"),
    link(["re:mine[- ]injur(?:y|ies)"], "mine-injury-data"),
    link(["re:leaf[- ]blotch"], "leaf-blotch-data"),
    link(["re:warp[- ]breaks"], "warp-breaks-data"),
    link(["re:sleep[- ]deprivation", "sleepstudy"], "sleep-deprivation-data"),
    link(["re:accidental[- ]deaths", "USAccDeaths"], "accidental-deaths-data"),
    link(["re:rat[- ]tumou?rs?"], "rat-tumour-data"),
    link(["re:TG5"], "tg5-cattle-studies"),
    link(["birthwt", "re:birth[- ]weight data"], "birth-weight-data"),
    link(["re:Alon(?: et al\\.?)?(?: colon[- ]cancer)?(?: data| matrix)?", "re:colon[- ]cancer (?:data|matrix|screen)"], "alon-colon-cancer-data"),
    link(["re:addiction (?:data|model|categories)"], "addiction-data"),
    link(["re:milk cartons?"], "milk-carton-example"),
    link(["NETtalk"], "nettalk"),
]

LINKS_LAST += [
    link(["boosting", "boosted"], "boosting", scope=[L]),
    link(["gradient descent"], "gradient-descent"),
    link(["lasso", "L1 penalty"], "lasso"),
    link(["bootstrap"], "bootstrap"),
    link(["re:kernels?"], "kernel", scope=[L], exclude=["sl-07-linkage-and-density"]),
    link(["re:kernels?"], "kernel-density-estimator", scope=[L, D]),
    link(["re:linkages?"], "single-complete-and-average-linkage", scope=[L]),
    link(["re:bandwidths?"], "choosing-the-bandwidth", scope=[L, D]),
    link(["re:margins?"], "linear-separators-and-the-margin", scope=[L], exclude=["sl-13-ensembles"]),
    link(["re:mixtures?"], "finite-mixture-model", scope=[L]),
    link(["re:principal components?"], "L3"),
    link(["re:discriminant analysis"], "L8"),
    link(["re:graphical models?"], "L19"),
    link(["re:nearest[- ]neighbou?rs?", "k-NN", "kNN"], "nearest-neighbours"),
    link(["re:impurit(?:y|ies)"], "node-impurity", scope=[L]),
    link(["re:random walks?"], "SP3"),
    link(["re:queues?|queueing|queuing"], "SP8"),
    link(["re:Poisson process(?:es)?"], "homogeneous-poisson-process"),
    link(["re:Borel[–-]Cantelli(?: lemmas?)?"], "borel-cantelli-lemmas"),
    link(["re:uniform(?:ly)? integrab(?:le|ility)"], "uniform-integrability"),
    link(["re:recurren(?:t|ce)"], "recurrence-and-period", scope=[SP]),
    link(["re:smoothing"], "S1", scope=[T, G, C, L, B]),
    link(["re:linear regressions?"], "I6"),
    link(["re:linear models?"], "I6", scope=[G, S, C, T, D, L, B]),
    link(["re:hypothesis tests?", "re:significance tests?"], "I4"),
    link(["re:chi-squared tests?"], "I5"),
    link(["re:statistical inference"], "I1"),
    link(["re:least squares"], "least-squares"),
    link(["re:maximum likelihood"], "maximum-likelihood"),
    link(["re:log-likelihoods?", "re:likelihoods?"], "likelihood-function"),
    link(["re:unbiased(?: estimators?)?"], "unbiased-estimator"),
    link(["re:p-values?"], "p-value"),
    link(["re:pivots?|pivotal quantit(?:y|ies)"], "pivot"),
    link(["re:null hypothes[ie]s|alternative hypothes[ie]s"], "null-and-alternative-hypotheses"),
    link(["re:interactions?"], "interaction", scope=[G, S, C, T, B, L]),
    link(["re:random samples?"], "random-sample"),
    link(["re:sample quantiles?|percentiles?|quartiles?"], "sample-quantile"),
    link(["re:conditional probabilit(?:y|ies)"], "conditional-probability"),
    link(["re:conditional distributions?|conditional densit(?:y|ies)"], "conditional-distribution"),
    link(["re:likelihood functions?"], "likelihood-function"),
    link(["re:covariance matri(?:x|ces)", "re:covariances?"], "mean-vector-and-covariance-matrix", scope=[L]),
    link(["re:covariances?"], "covariance"),
    link(["re:correlations?"], "correlation"),
    link(["re:random variables?"], "measurable-random-variable", scope=[SP]),
    link(["re:random variables?"], "random-variable"),
    link(["re:expectations?|expected values?"], "expectation"),
    link(["re:variances?"], "variance"),
    link(["re:estimators?"], "estimator"),
    link(["re:statistic"], "statistic"),
    link(["re:events?"], "event", scope=[P, SP, I, D, B]),
    link(["re:proposals?(?: distributions?| densit(?:y|ies))?"], "random-walk-and-independent-proposals", scope=[B]),
    link(["re:cholesterol"], "cholesterol-and-heart-disease", scope=[G]),
    link(["re:iris"], "iris-data", scope=[L]),
    link(["re:addiction"], "addiction-data", scope=[G]),
]

RELATED += [
    ("markov-chain", "finite-state-markov-chain", "discrete-time-markov-chain", "markov-property"),
    ("stationary-distribution", "stationarity-and-detailed-balance", "limiting-distribution", "stationarity-of-a-time-series"),
    ("detailed-balance", "stationarity-and-detailed-balance", "detailed-balance-implies-stationarity", "local-balance"),
    ("multivariate-normal-distribution", "multivariate-normal-distribution-sl-01-multivariate-normal"),
    ("affine-images-of-normal-vectors", "linear-images-of-a-normal-vector"),
    ("expectation-vector-and-covariance-matrix", "mean-vector-and-covariance-matrix", "covariance"),
    ("joint-probability-density", "joint-distribution-and-density"),
    ("correlation", "sample-correlation-coefficient", "partial-correlation"),
    ("probability-space", "probability-measure", "sigma-algebra"),
    ("random-variable", "measurable-random-variable"),
    ("law-of-large-numbers", "strong-law"),
    ("central-limit-theorem", "multivariate-central-limit-theorem", "multinomial-central-limit-theorem"),
    ("invariance-of-maximum-likelihood", "invariance-of-the-maximum-likelihood-estimator"),
    ("bayes-rule", "posterior-class-probability", "posterior-membership", "bayes-classifier"),
    ("bayes-optimal-rule", "bayes-action-for-two-hypotheses", "bayes-classifier"),
    ("binary-logistic-regression", "interpreting-a-logistic-regression", "logit-link", "odds-ratio"),
    ("marginal-likelihood-and-bayes-factor", "bayes-factors-and-posterior-odds", "bayesian-information-criterion"),
    ("bonferroni-correction", "family-wise-error-rate", "multiple-testing", "false-discovery-rate", "benjamini-hochberg", "tukey-intervals"),
    ("kernel", "kernel-density-estimator", "kernel-of-a-density", "gaussian-kernel"),
    ("ordinary-least-squares", "least-squares-line", "least-squares", "simple-linear-regression", "multiple-linear-regression", "gaussian-linear-model", "normal-linear-model"),
    ("normal-hierarchical-shrinkage", "ridge-regression", "regularisation", "maximum-a-posteriori-estimate"),
    ("quasi-score-and-quasi-likelihood", "quasi-likelihood", "variance-function"),
    ("em-algorithm", "em-for-a-normal-mixture", "monotonicity-of-em", "complete-data-likelihood"),
    ("lloyd-s-k-means-algorithm", "k-means-as-a-limiting-case", "hartigan-wong-algorithm"),
    ("one-sample-t-test", "hotelling-s-t2-test", "univariate-t-test-as-a-template-for-t2"),
    ("two-sample-t-test", "two-sample-hotelling-test", "two-sample-hotelling-t2-test"),
    ("welch-interval", "behrens-fisher-problem"),
    ("burn-in", "warm-up-is-not-a-convergence-proof"),
    ("metropolis-hastings-algorithm", "metropolis-hastings-update", "metropolis-hastings-invariance", "metropolis-algorithm", "hastings-correction"),
    ("gibbs-sampling", "systematic-scan-gibbs-sampler", "full-conditional-distribution"),
    ("random-walk-with-drift", "drift-and-scale-of-a-random-walk", "gambler-s-ruin", "four-state-random-walk"),
    ("poisson-distribution", "homogeneous-poisson-process", "poisson-regression"),
    ("exponential-family", "natural-exponential-family", "natural-parameter", "canonical-link"),
    ("deviance", "residual-deviance", "null-deviance", "scaled-deviance", "saturated-model", "deviance-residual"),
    ("hazard-rate", "proportional-hazards-model", "survival-function"),
    ("weibull-distribution", "a-finite-endpoint-and-a-weibull-extreme-value-law"),
    ("principal-component-directions-and-scores", "principal-component-directions", "eigenvalues-and-eigenvectors", "singular-value-decomposition"),
    ("cross-validation", "fold-cross-validation", "leave-one-out-cross-validation", "nested-cross-validation", "cross-validation-of-the-likelihood"),
    ("akaike-information-criterion", "bayesian-information-criterion", "extended-information-criterion"),
    ("roughness-penalty", "cubic-smoothing-spline", "gaussian-process"),
    ("random-intercept-model", "hierarchical-bayesian-model", "blocks-in-analysis-of-variance", "randomised-block-design"),
    ("softmax-is-multinomial-logistic-regression", "multinomial-logistic-regression", "baseline-category-logit-model"),
    ("generalised-estimating-equations", "marginal-model", "sandwich-estimator", "working-correlation"),
    ("autocorrelation-function", "partial-autocorrelation", "autoregression-and-moving-averages"),
    ("artificial-neuron", "perceptron", "sigmoid-function", "activation-function"),
    ("logit-link", "probit-link", "complementary-log-log-link", "identity-link", "log-link", "inverse-link", "canonical-link"),
    ("overdispersion", "underdispersion", "quasi-poisson", "negative-binomial-distribution", "conway-maxwell-poisson-distribution"),
    ("markov-s-inequality", "chebyshev-s-inequality", "jensen-s-inequality", "cauchy-schwarz-inequality"),
]

LINKS_LAST += [
    link(["re:cumulative distribution functions?|distribution functions?|cdfs?"], "cumulative-distribution-function"),
    link(["re:continuous distributions?"], "continuous-distribution"),
    link(["re:discrete distributions?"], "discrete-distribution"),
    link(["re:sample spaces?"], "sample-space"),
    link(["re:probability measures?"], "probability-measure"),
    link(["re:Markov chains?"], "markov-chain", scope=[L, I, D]),
    link(["re:detailed balance"], "detailed-balance", scope=[L, I, D, P]),
    link(["re:stationary distributions?"], "stationary-distribution", scope=[L, I, D, P, T]),
    link(["re:transformation rule|change of variables"], "transformation-rule"),
    link(["re:observational studies?"], "observational-study"),
]

RELATED += [
    ("akaike-information-criterion", "deviance", "analysis-of-deviance"),
]
