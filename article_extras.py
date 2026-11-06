"""Hand-chosen material for the article pages.

build_wiki.py reads these tables. Each name is an article slug (the file name
in articles/ without .qmd), a question id (q-06, c-03, ex-norm-mean,
ex-applied-geometric, ...), a book example box id (exm-...), or a figure file
in figures/. The build stops with a message if a name does not exist.

Properties: results (theorems, propositions, corollaries, remarks) about the
object. Each is shown with its full statement and a link to its own article.

Examples: worked problems, shown with the question and its answer folded
away. Only questions with a worked answer are used.

Figures: the first figure also goes in the infobox and the hover preview.
"""

PROPERTIES = {
    # Distributions
    "beta-distribution": [
        "beta-binomial-conjugacy",
        "the-beta-distribution-is-the-two-category-dirichlet",
        "beta-binomial-posterior-prediction",
        "two-pseudo-count-conventions",
    ],
    "dirichlet-distribution": [
        "dirichlet-moments",
        "interior-dirichlet-mode",
        "dirichlet-multinomial-conjugacy",
        "the-beta-distribution-is-the-two-category-dirichlet",
    ],
    "multinomial-distribution": ["multinomial-central-limit-theorem", "dirichlet-multinomial-conjugacy"],
    "binomial-distribution": ["beta-binomial-conjugacy", "beta-binomial-posterior-prediction"],
    "normal-distribution": [
        "normal-normal-conjugacy",
        "normal-inverse-gamma-variance-update",
        "full-conditionals-under-independent-priors",
        "precision-weighting",
    ],
    "inverse-gamma-distribution": [
        "normal-inverse-gamma-variance-update",
        "normal-inverse-gamma-conjugacy",
        "marginal-variance-posterior",
    ],
    "gamma-distribution": ["generic-exponential-family-conjugate-update"],
    "poisson-distribution": ["generic-exponential-family-conjugate-update"],
    # Bayesian foundations
    "prior-and-posterior-predictive-distributions": [
        "predictive-variance-decomposition",
        "beta-binomial-posterior-prediction",
        "posterior-prediction-under-the-reference-prior",
    ],
    "posterior-point-summaries": ["posterior-summaries-from-draws"],
    "bayesian-credible-interval": ["posterior-summaries-from-draws"],
    "credible-region-constructions": ["posterior-summaries-from-draws"],
    "proper-prior-and-proper-posterior": ["a-proper-approximation-to-the-flat-prior"],
    # Normal models
    "normal-normal-model": ["normal-normal-conjugacy", "precision-weighting"],
    # MCMC
    "markov-chain": ["detailed-balance-implies-stationarity", "metropolis-hastings-invariance"],
    "stationarity-and-detailed-balance": ["detailed-balance-implies-stationarity"],
    "metropolis-hastings-update": ["metropolis-hastings-invariance", "warm-up-is-not-a-convergence-proof"],
    "systematic-scan-gibbs-sampler": ["full-conditionals-under-independent-priors", "warm-up-is-not-a-convergence-proof"],
    # Categorical
    "categorical-and-multinomial-models": ["multinomial-central-limit-theorem", "dirichlet-multinomial-conjugacy"],
    # Testing
    "marginal-likelihood-and-bayes-factor": ["posterior-odds-factorisation", "a-hypothesis-region-is-not-a-separate-model"],
    "posterior-hypothesis-probability": ["bayes-action-for-two-hypotheses", "posterior-odds-factorisation"],
    # Exponential families and sufficiency
    "sufficient-statistic": ["fisher-neyman-factorisation", "basu-s-theorem", "pitman-koopman-darmois-informal-form"],
    "complete-statistic": ["basu-s-theorem"],
    "ancillary-statistic": ["basu-s-theorem"],
    "exponential-family": [
        "mean-and-variance-of-an-exponential-family",
        "log-partition-moment-identities",
        "generic-exponential-family-conjugate-update",
        "pitman-koopman-darmois-informal-form",
    ],
    "natural-exponential-family": [
        "log-partition-moment-identities",
        "generic-exponential-family-conjugate-update",
        "pitman-koopman-darmois-informal-form",
    ],
    "generalised-linear-model": ["mean-and-variance-of-an-exponential-family"],
    # Hierarchies
    "hierarchical-bayesian-model": ["normal-hierarchical-shrinkage", "marginal-hyperposterior", "study-rate-full-conditional"],
    "hyperparameter": ["marginal-hyperposterior"],
    "empirical-bayes": ["normal-hierarchical-shrinkage"],
    # Regression
    "gaussian-linear-model": [
        "ordinary-least-squares",
        "sampling-distribution-of-the-ols-estimator",
        "least-squares-decomposition",
        "marginal-student-posterior",
        "posterior-prediction-under-the-reference-prior",
    ],
    "normal-inverse-gamma-prior": [
        "normal-inverse-gamma-conjugacy",
        "conditional-coefficient-posterior",
        "marginal-variance-posterior",
        "marginal-student-posterior",
    ],
    "ordinary-least-squares": ["sampling-distribution-of-the-ols-estimator", "studentised-coefficient-pivot", "least-squares-decomposition"],
}

EXAMPLES = {
    # Distributions
    "beta-distribution": ["q-06", "q-23"],
    "binomial-distribution": ["q-06", "q-44"],
    "geometric-distribution": ["ex-geom-beta", "ex-applied-geometric"],
    "multinomial-distribution": ["q-22", "ex-applied-restaurant"],
    "poisson-distribution": ["q-53", "q-32"],
    "exponential-distribution": ["ex-applied-exp-rate", "ex-device-bf"],
    "gamma-distribution": ["q-48", "q-29"],
    "normal-distribution": ["q-07", "ex-norm-mean"],
    "dirichlet-distribution": ["q-22", "ex-applied-restaurant"],
    "inverse-gamma-distribution": ["ex-norm-var", "ex-mammal-ig"],
    # GLMs
    "generalised-linear-model": ["q-30", "ex-fish-poisson", "c-16"],
    "canonical-link": ["q-57", "c-17"],
    "exponential-family": ["q-45", "c-04"],
    "mean-and-variance-of-an-exponential-family": ["q-45"],
    "quasi-score-and-quasi-likelihood": ["q-47", "c-27"],
    "baseline-category-logit-model": ["q-46", "c-24"],
    "proportional-odds-model": ["c-25"],
    "marginal-model": ["c-38", "c-40"],
    # Bayesian foundations
    "bayes-rule": ["q-15"],
    "bayesian-credible-interval": ["q-03", "q-16"],
    "credible-region-constructions": ["q-08", "q-13"],
    "posterior-point-summaries": ["ex-applied-mmse", "c-07"],
    "posterior-summaries-from-draws": ["q-25", "c-11"],
    "predictive-variance-decomposition": ["q-20"],
    "prior-and-posterior-predictive-distributions": ["q-07", "q-20"],
    "proper-prior-and-proper-posterior": ["ex-improper-normal", "q-43"],
    # Beta-Binomial
    "beta-binomial-conjugacy": ["q-06", "q-17"],
    "conjugacy-is-optional": ["q-42", "ex-applied-logitnormal-prior"],
    # Normal models
    "normal-normal-model": ["ex-norm-mean", "q-07"],
    "normal-normal-conjugacy": ["ex-norm-mean"],
    "precision-weighting": ["ex-norm-mean"],
    "normal-inverse-gamma-variance-update": ["ex-norm-var", "q-28"],
    "full-conditionals-under-independent-priors": ["q-49", "ex-norm-both"],
    # MCMC
    "markov-chain": ["q-18", "c-12"],
    "stationarity-and-detailed-balance": ["c-12"],
    "metropolis-hastings-update": ["q-05", "q-10", "ex-applied-logitnormal-mh"],
    "metropolis-hastings-invariance": ["c-14"],
    "systematic-scan-gibbs-sampler": ["q-04", "q-09", "ex-gibbs-geom"],
    "warm-up-is-not-a-convergence-proof": ["c-15", "q-19"],
    # Categorical
    "categorical-and-multinomial-models": ["q-22"],
    "dirichlet-multinomial-conjugacy": ["q-22", "ex-applied-restaurant"],
    "dirichlet-moments": ["q-22"],
    "interior-dirichlet-mode": ["q-22"],
    # Testing
    "marginal-likelihood-and-bayes-factor": ["q-11", "ex-battery-bf"],
    "posterior-hypothesis-probability": ["q-21", "c-08"],
    "posterior-odds-factorisation": ["q-21", "ex-applied-iq"],
    # Exponential families and sufficiency
    "sufficient-statistic": ["ex-applied-sufficiency-posterior", "c-03"],
    "fisher-neyman-factorisation": ["ex-applied-sufficiency-posterior"],
    "generic-exponential-family-conjugate-update": ["q-01", "q-12"],
    "natural-exponential-family": ["c-04", "q-57"],
    # Hierarchies
    "hierarchical-bayesian-model": ["q-23", "ex-pois-hier"],
    "hyperparameter": ["q-23"],
    "exchangeability": ["c-09"],
    "normal-hierarchical-shrinkage": ["q-23"],
    # Regression
    "gaussian-linear-model": ["q-24", "ex-reg-nichisq"],
    "ordinary-least-squares": ["q-24"],
    "normal-inverse-gamma-conjugacy": ["ex-reg-nichisq", "q-58"],
    "normal-inverse-gamma-prior": ["ex-norm-nig", "ex-reg-nichisq"],
    "marginal-student-posterior": ["q-24", "q-43"],
    "marginal-variance-posterior": ["q-24"],
    "posterior-prediction-under-the-reference-prior": ["q-24"],
    "posterior-predictive-target": ["q-24"],
    "conditional-coefficient-posterior": ["q-24"],
    "direct-posterior-simulation": ["q-58"],
}

# The book's own worked example boxes, and the articles they illustrate.
BOOK_EXAMPLES = {
    "exm-five-future-tosses": ["beta-binomial-posterior-prediction", "binomial-distribution"],
    "exm-four-state-random-walk": ["markov-chain", "stationarity-and-detailed-balance"],
    "exm-bivariate-exponential-target": ["systematic-scan-gibbs-sampler"],
    "exm-normal-mean-and-variance": ["full-conditionals-under-independent-priors", "systematic-scan-gibbs-sampler"],
    "exm-advertising-responses": ["dirichlet-multinomial-conjugacy", "dirichlet-distribution"],
    "exm-imperfect-fruit-decision": ["bayes-action-for-two-hypotheses", "posterior-hypothesis-probability"],
    "exm-sufficiency-for-a-normal-mean": ["sufficient-statistic", "fisher-neyman-factorisation"],
    "exm-poisson-natural-form-and-gamma-conjugacy": [
        "natural-exponential-family",
        "generic-exponential-family-conjugate-update",
        "poisson-distribution",
        "gamma-distribution",
    ],
    "exm-large-and-small-tutorial-classes": ["normal-hierarchical-shrinkage", "empirical-bayes"],
    "exm-tg5-cattle-hierarchy": ["hierarchical-bayesian-model"],
    "exm-rat-tumour-hierarchy": ["hierarchical-bayesian-model", "exchangeability", "hyperparameter"],
    "exm-eight-point-regression": ["gaussian-linear-model", "ordinary-least-squares"],
}

FIGURES = {
    "beta-distribution": ["part1-fig-02-prior-sensitivity.png", "part1-fig-01-credible-regions.png"],
    "beta-binomial-conjugacy": ["part1-fig-02-prior-sensitivity.png"],
    "dirichlet-distribution": ["part1-fig-05-dirichlet-simplex.png", "part1-inline-simplex.png"],
    "categorical-and-multinomial-models": ["part1-inline-simplex.png"],
    "multinomial-distribution": ["part1-inline-simplex.png"],
    "gamma-distribution": ["part1-fig-06-fruit-posterior.png"],
    "bayesian-credible-interval": ["part1-fig-01-credible-regions.png"],
    "credible-region-constructions": ["part1-fig-01-credible-regions.png"],
    "systematic-scan-gibbs-sampler": ["part1-fig-04-gibbs-staircase.png"],
    "metropolis-hastings-update": ["part1-fig-04-proposal-scale.png"],
    "warm-up-is-not-a-convergence-proof": ["part1-fig-04-proposal-scale.png"],
    "bayes-action-for-two-hypotheses": ["part1-fig-06-fruit-posterior.png"],
    "posterior-hypothesis-probability": ["part1-fig-06-fruit-posterior.png"],
    "normal-hierarchical-shrinkage": ["part1-fig-08-shrinkage.png"],
    "hierarchical-bayesian-model": ["part1-fig-08-shrinkage.png", "part1-fig-08-hyperposterior-grid.png"],
    "marginal-hyperposterior": ["part1-fig-08-hyperposterior-grid.png"],
    "grid-monte-carlo-approximation": ["part1-fig-08-hyperposterior-grid.png"],
    "gaussian-linear-model": ["part1-fig-09-regression-bands.png"],
    "posterior-prediction-under-the-reference-prior": ["part1-fig-09-regression-bands.png"],
    "posterior-predictive-target": ["part1-fig-09-regression-bands.png"],
    "generalised-linear-model": ["links.png"],
    "canonical-link": ["links.png"],
    "marginal-model": ["marginal-schematic.png", "burn-ellipse.png"],
    "proportional-odds-model": ["pneumonia.png"],
    "quasi-score-and-quasi-likelihood": ["variance.png", "leaf-residuals.png"],
    "mean-and-variance-of-an-exponential-family": ["variance.png"],
    "wold-decomposition": ["ar-paths.png"],
}

# A chapter's infobox shows its first figure unless another is named here.
CHAPTER_FIGURES = {
    "bayes-05-categorical.qmd": "part1-fig-05-dirichlet-simplex.png",
}
