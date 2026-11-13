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


# ---------------------------------------------------------------------------
# Statistical inference. Kept in one block and merged into the tables above,
# so an article that already has Bayesian material keeps it.
# ---------------------------------------------------------------------------

_INFERENCE_PROPERTIES = {
    "random-sample": ["moments-of-the-sample-mean-and-variance", "normal-sample-theorem"],
    "statistic": ["moments-of-the-sample-mean-and-variance", "normal-sample-theorem"],
    "normal-distribution": ["normal-sample-theorem"],
    "chi-squared-distribution": ["normal-sample-theorem", "pearson-chi-squared-approximation", "pearson-test-with-estimated-parameters"],
    "student-t-distribution": ["one-sample-t-pivot", "two-sample-t-pivot", "slope-t-pivot"],
    "f-distribution": ["variance-ratio-f-pivot", "anova-f-distribution"],
    "likelihood-function": ["invariance-of-maximum-likelihood"],
    "maximum-likelihood": ["invariance-of-maximum-likelihood"],
    "unbiased-estimator": ["moments-of-the-sample-mean-and-variance", "least-squares-estimators-are-unbiased"],
    "confidence-interval": ["one-sample-t-pivot", "two-sample-t-pivot", "variance-ratio-f-pivot", "slope-t-pivot"],
    "pivot": ["one-sample-t-pivot", "two-sample-t-pivot", "variance-ratio-f-pivot", "slope-t-pivot"],
    "pooled-variance": ["two-sample-t-pivot"],
    "one-sample-t-test": ["one-sample-t-pivot"],
    "two-sample-t-test": ["two-sample-t-pivot"],
    "f-test-for-equal-variances": ["variance-ratio-f-pivot"],
    "pearson-statistic": ["pearson-chi-squared-approximation", "pearson-test-with-estimated-parameters"],
    "chi-squared-test-of-independence": ["pearson-test-with-estimated-parameters"],
    "simple-linear-regression": [
        "least-squares-estimators-are-unbiased",
        "sampling-distribution-of-the-regression-estimators",
        "slope-t-pivot",
    ],
    "least-squares-line": ["least-squares-estimators-are-unbiased"],
    "prediction-interval": ["sampling-distribution-of-the-regression-estimators"],
    "one-way-analysis-of-variance": ["anova-sum-of-squares-decomposition", "anova-f-distribution"],
    "randomised-block-design": ["anova-f-distribution"],
}

_INFERENCE_EXAMPLES = {
    "statistic": ["ex-inf-which-are-statistics"],
    "pivot": ["ex-inf-which-are-statistics", "ex-inf-mean-pivot"],
    "student-t-distribution": ["ex-inf-t-squared-is-f"],
    "f-distribution": ["ex-inf-t-squared-is-f", "ex-inf-variance-ratio-interval"],
    "maximum-likelihood": ["ex-inf-normal-mle", "ex-inf-exponential-mle", "ex-inf-poisson-mle"],
    "invariance-of-maximum-likelihood": ["ex-inf-exponential-mle"],
    "unbiased-estimator": ["ex-inf-variance-bias", "ex-inf-expected-sample-variance"],
    "mean-squared-error": ["ex-inf-shrunk-mean"],
    "consistent-estimator": ["ex-inf-poisson-mle"],
    "confidence-interval": ["ex-inf-two-standard-errors", "ex-inf-mean-pivot"],
    "pooled-variance": ["ex-inf-safety-interval"],
    "wald-interval": ["ex-inf-green-voters", "ex-inf-poll-size"],
    "critical-region": ["ex-inf-blood-pressure-region"],
    "power-function": ["ex-inf-serve-power", "ex-inf-fork-critical-value"],
    "one-sample-t-test": ["ex-inf-tyre-wear"],
    "sign-test": ["ex-inf-sign-test-one-sided"],
    "pearson-statistic": ["ex-inf-die-fairness"],
    "two-proportion-z-test": ["ex-inf-two-by-two"],
    "chi-squared-test-of-independence": ["ex-inf-two-by-two", "ex-inf-degrees-of-freedom"],
    "least-squares-line": ["ex-inf-normal-equations", "ex-inf-line-through-origin"],
    "coefficient-of-determination": ["ex-inf-advertising-r2"],
    "prediction-interval": ["ex-inf-prediction-width"],
    "sample-correlation-coefficient": ["ex-inf-correlation-t"],
    "one-way-analysis-of-variance": ["ex-inf-heart-rate", "ex-inf-anova-two-groups"],
    "contrast": ["ex-inf-corn-contrast"],
    "tukey-intervals": ["ex-inf-tukey-corn"],
    "randomised-block-design": ["ex-inf-hardness", "ex-inf-paired-f"],
}

_INFERENCE_BOOK_EXAMPLES = {
    "exm-ten-thermometers": ["estimator"],
    "exm-two-variance-estimators": ["mean-squared-error", "unbiased-estimator"],
    "exm-two-estimators-of-a-uniform-endpoint": ["mean-squared-error", "maximum-likelihood", "method-of-moments"],
    "exm-household-fuel-spending": ["confidence-interval", "one-sample-t-pivot"],
    "exm-aspirin-tablet-weights": ["chi-squared-distribution", "confidence-interval"],
    "exm-nightmares-in-two-groups": ["wald-interval"],
    "exm-a-gene-in-lake-fish": ["binomial-test", "p-value"],
    "exm-caffeine-in-cola": ["one-sample-t-test", "p-value", "critical-region"],
    "exm-tuning-fork-variability": ["chi-squared-distribution", "critical-region"],
    "exm-army-recruits-by-iq-class": ["multinomial-distribution"],
    "exm-frizzled-chickens": ["pearson-statistic", "pearson-chi-squared-approximation"],
    "exm-houses-on-a-village-grid": ["pearson-test-with-estimated-parameters", "poisson-distribution"],
    "exm-belief-in-esp": ["chi-squared-test-of-independence"],
    "exm-advertising-and-sales": ["least-squares-line"],
    "exm-melanoma-and-latitude": ["least-squares-line"],
    "exm-heart-rate-and-oxygen-intake": ["simple-linear-regression", "slope-t-pivot", "prediction-interval"],
    "exm-testing-a-correlation": ["sample-correlation-coefficient"],
    "exm-five-varieties-of-corn": ["one-way-analysis-of-variance", "anova-f-distribution", "tukey-intervals"],
}

_INFERENCE_FIGURES = {
    "confidence-interval": ["inf-coverage.png"],
    "student-t-distribution": ["inf-t-densities.png"],
    "one-sample-t-pivot": ["inf-t-densities.png"],
    "p-value": ["inf-p-value.png"],
    "one-sample-t-test": ["inf-p-value.png"],
    "critical-region": ["inf-p-value.png"],
    "power-function": ["inf-power-curve.png"],
    "type-i-and-type-ii-errors": ["inf-power-curve.png"],
    "neyman-pearson-approach": ["inf-power-curve.png"],
    "pearson-test-with-estimated-parameters": ["inf-houses-poisson.png"],
    "simple-linear-regression": ["inf-heart-oxygen.png", "inf-regression-effect.png"],
    "prediction-interval": ["inf-heart-oxygen.png"],
    "least-squares-line": ["inf-regression-effect.png"],
    "randomised-block-design": ["inf-hardness-blocks.png"],
    "one-way-analysis-of-variance": ["inf-corn-groups.png"],
    "tukey-intervals": ["inf-corn-groups.png"],
}

for _table, _extra in (
    (PROPERTIES, _INFERENCE_PROPERTIES),
    (EXAMPLES, _INFERENCE_EXAMPLES),
    (BOOK_EXAMPLES, _INFERENCE_BOOK_EXAMPLES),
    (FIGURES, _INFERENCE_FIGURES),
):
    for _name, _items in _extra.items():
        _table.setdefault(_name, []).extend(i for i in _items if i not in _table[_name])


# ---------------------------------------------------------------------------
# Probability. Merged into the tables above in the same way.
# ---------------------------------------------------------------------------

_PROBABILITY_PROPERTIES = {
    "probability-measure": ["properties-of-a-probability", "equally-likely-outcomes"],
    "sample-space": ["equally-likely-outcomes", "four-ways-of-counting-draws"],
    "event": ["properties-of-a-probability"],
    "conditional-probability": ["product-rule", "law-of-total-probability"],
    "independent-events": ["product-rule"],
    "random-variable": ["expectation-of-a-function"],
    "expectation": ["expectation-of-a-function", "tower-property"],
    "binomial-distribution": ["poisson-limit-of-the-binomial", "central-limit-theorem"],
    "poisson-distribution": ["poisson-limit-of-the-binomial"],
    "exponential-distribution": ["memoryless-property"],
    "geometric-distribution": ["memoryless-property"],
    "uniform-distribution": ["inverse-transform-method"],
    "cumulative-distribution-function": ["inverse-transform-method"],
    "joint-probability-mass-function": ["tower-property"],
    "joint-probability-density": ["transformation-rule"],
    "conditional-distribution": ["tower-property"],
    "covariance": ["affine-images-of-normal-vectors"],
    "multivariate-normal-distribution": ["affine-images-of-normal-vectors"],
    "finite-state-markov-chain": ["limiting-distribution"],
    "structure-function": [],
    "survival-function": [],
    "weibull-distribution": [],
}

_PROBABILITY_EXAMPLES = {
    "sample-space": ["ex-prob-three-tosses", "ex-prob-three-toss-weights"],
    "four-ways-of-counting-draws": ["ex-prob-urn-combinations", "ex-prob-three-cards", "ex-prob-ten-balls-three-boxes"],
    "equally-likely-outcomes": ["ex-prob-two-dice-faces", "ex-prob-four-honours"],
    "conditional-probability": ["ex-prob-second-die", "ex-prob-binary-channel"],
    "law-of-total-probability": ["ex-prob-channel-quarter", "ex-prob-channel-zero"],
    "independent-events": ["ex-prob-series-parallel"],
    "properties-of-a-probability": ["ex-prob-intersection-bound"],
    "discrete-distribution": ["ex-prob-dice-sum-pmf", "ex-prob-min-dice"],
    "continuous-distribution": ["ex-prob-cubic-cdf", "ex-prob-uniform-interval"],
    "cumulative-distribution-function": ["ex-prob-cubic-cdf", "ex-prob-cdf-of-maximum"],
    "expectation": ["ex-prob-three-point-expectation", "ex-prob-red-balls-expectation", "ex-prob-dice-sum-game"],
    "expectation-of-a-function": ["ex-prob-min-dice-game", "ex-prob-squared-heads"],
    "variance": ["ex-prob-uniform-variance", "ex-prob-dice-sum-game"],
    "moment-generating-function": ["ex-prob-exp-moments", "ex-prob-second-moment"],
    "binomial-distribution": ["ex-prob-twenty-heads", "ex-prob-votes"],
    "geometric-distribution": ["ex-prob-wait-for-twelve", "ex-prob-double-six-wait"],
    "poisson-distribution": ["ex-prob-radioactive"],
    "hypergeometric-distribution": ["ex-prob-five-evens-no-replace"],
    "exponential-distribution": ["ex-prob-component-five-years", "ex-prob-memoryless-component"],
    "memoryless-property": ["ex-prob-two-lifetimes", "ex-prob-memoryless-component"],
    "normal-distribution": ["ex-prob-standard-normal-probs", "ex-prob-normal-shift"],
    "gamma-distribution": ["ex-prob-ten-components"],
    "inverse-transform-method": ["ex-prob-generate-exp", "ex-prob-shifted-exp-generate"],
    "joint-probability-mass-function": ["ex-prob-joint-table", "ex-prob-sign-covariance"],
    "joint-probability-density": ["ex-prob-region-probability", "ex-prob-independent-exponentials"],
    "conditional-distribution": ["ex-prob-triangle-conditional"],
    "covariance": ["ex-prob-sign-covariance"],
    "transformation-rule": ["ex-prob-exponential-ratio", "ex-prob-quadratic-transform", "ex-prob-random-radius"],
    "affine-images-of-normal-vectors": ["ex-prob-partial-sums", "ex-prob-circuit-board"],
    "law-of-large-numbers": ["ex-prob-voltage-mean"],
    "central-limit-theorem": ["ex-prob-clt-binomial-tail", "ex-prob-blueberry-sieve", "ex-prob-lift"],
    "finite-state-markov-chain": ["ex-prob-markov-two-steps", "ex-prob-markov-random-walk"],
    "limiting-distribution": ["ex-prob-markov-limit", "ex-prob-markov-two-state", "ex-prob-markov-periodic", "ex-prob-markov-reflecting"],
    "structure-function": ["ex-prob-k-out-of-n", "ex-prob-bridge-pivot", "ex-prob-bridge-paths"],
    "reliability-function": ["ex-prob-series-parallel"],
    "survival-function": ["ex-prob-mttf-integral", "ex-prob-christmas-lights"],
    "hazard-rate": ["ex-prob-hazard-survival"],
}

_PROBABILITY_BOOK_EXAMPLES = {
    "exm-a-four-engine-aeroplane": ["independent-events", "event"],
    "exm-the-birthday-problem": ["four-ways-of-counting-draws", "equally-likely-outcomes"],
    "exm-the-monty-hall-problem": ["conditional-probability"],
    "exm-three-factories": ["law-of-total-probability", "conditional-probability"],
    "exm-defective-items-in-a-box": ["binomial-distribution"],
    "exm-a-rare-fault": ["poisson-limit-of-the-binomial", "poisson-distribution"],
    "exm-aces-in-a-hand": ["hypergeometric-distribution"],
    "exm-iq-scores": ["normal-distribution"],
    "exm-rejection-for-a-beta-density": ["acceptance-rejection-method"],
    "exm-a-box-of-three-dice": ["joint-probability-mass-function", "independent-random-variables"],
    "exm-uncorrelated-but-dependent": ["covariance", "independent-random-variables"],
    "exm-a-uniform-point-on-a-triangle": ["conditional-distribution", "tower-property"],
    "exm-a-day-of-takings": ["tower-property"],
    "exm-the-square-of-a-standard-normal": ["transformation-rule", "chi-squared-distribution"],
    "exm-a-series-of-exponential-components": ["exponential-distribution"],
    "exm-the-sum-of-two-uniforms": ["uniform-distribution"],
    "exm-ball-bearings-and-a-sieve": ["affine-images-of-normal-vectors"],
    "exm-normal-approximation-to-a-binomial": ["central-limit-theorem", "binomial-distribution"],
    "exm-six-stepping-stones": ["finite-state-markov-chain", "limiting-distribution"],
    "exm-a-two-state-weather-chain": ["limiting-distribution"],
    "exm-a-bridge-of-reliable-links": ["reliability-function", "structure-function"],
    "exm-mean-lifetimes-of-redundant-systems": ["survival-function", "reliability-function"],
}

_PROBABILITY_FIGURES = {
    "probability-measure": ["prob-coin-averages.png"],
    "law-of-large-numbers": ["prob-coin-averages.png"],
    "four-ways-of-counting-draws": ["prob-birthday.png"],
    "binomial-distribution": ["prob-discrete-pmfs.png", "prob-binomial-normal.png"],
    "geometric-distribution": ["prob-discrete-pmfs.png"],
    "poisson-distribution": ["prob-discrete-pmfs.png"],
    "discrete-distribution": ["prob-discrete-pmfs.png"],
    "exponential-distribution": ["prob-continuous-densities.png"],
    "normal-distribution": ["prob-continuous-densities.png"],
    "continuous-distribution": ["prob-continuous-densities.png"],
    "inverse-transform-method": ["prob-inverse-transform.png"],
    "cumulative-distribution-function": ["prob-inverse-transform.png"],
    "acceptance-rejection-method": ["prob-acceptance-rejection.png"],
    "covariance": ["prob-correlation.png"],
    "multivariate-normal-distribution": ["prob-correlation.png"],
    "central-limit-theorem": ["prob-clt.png", "prob-binomial-normal.png"],
    "finite-state-markov-chain": ["prob-stepping-stones.png", "prob-random-walk.png"],
    "limiting-distribution": ["prob-stepping-stones.png"],
    "structure-function": ["prob-systems.png"],
    "reliability-function": ["prob-systems.png", "prob-system-survival.png"],
    "survival-function": ["prob-system-survival.png"],
    "hazard-rate": ["prob-weibull-hazards.png"],
    "weibull-distribution": ["prob-weibull-hazards.png"],
}

for _table, _extra in (
    (PROPERTIES, _PROBABILITY_PROPERTIES),
    (EXAMPLES, _PROBABILITY_EXAMPLES),
    (BOOK_EXAMPLES, _PROBABILITY_BOOK_EXAMPLES),
    (FIGURES, _PROBABILITY_FIGURES),
):
    for _name, _items in _extra.items():
        if _items:
            _table.setdefault(_name, []).extend(i for i in _items if i not in _table[_name])


# TikZ diagrams. The first figure of an article is its infobox image, so a
# diagram that explains the idea directly goes to the front of the list.
_DIAGRAMS_FIRST = {
    "law-of-total-probability": ["prob-01-experiments-total-probability.png"],
    "cumulative-distribution-function": ["prob-02-random-variables-distribution-function.png"],
    "discrete-distribution": ["prob-02-random-variables-distribution-function.png"],
    "conditional-distribution": ["prob-04-joint-distributions-conditional-slice.png"],
    "type-i-and-type-ii-errors": ["inf-04-hypothesis-tests-errors.png"],
    "anova-sum-of-squares-decomposition": ["inf-07-anova-sums-of-squares.png"],
    "observational-study": ["da-01-studies-and-data-assignment.png"],
    "designed-experiment": ["da-01-studies-and-data-assignment.png"],
}
_DIAGRAMS_AFTER = {
    "conditional-probability": ["prob-01-experiments-total-probability.png"],
    "continuous-distribution": ["prob-02-random-variables-distribution-function.png"],
    "limiting-distribution": ["prob-06-markov-chains-reflected-walk.png"],
    "power-function": ["inf-04-hypothesis-tests-errors.png"],
    "p-value": ["inf-04-hypothesis-tests-errors.png"],
    "one-way-analysis-of-variance": ["inf-07-anova-sums-of-squares.png"],
}
for _name, _items in _DIAGRAMS_FIRST.items():
    _rest = [f for f in FIGURES.get(_name, []) if f not in _items]
    FIGURES[_name] = _items + _rest
for _name, _items in _DIAGRAMS_AFTER.items():
    FIGURES.setdefault(_name, []).extend(i for i in _items if i not in FIGURES[_name])


# ---------------------------------------------------------------------------
# Data analysis.
# ---------------------------------------------------------------------------

_DATA_EXAMPLES = {
    "observational-study": ["ex-da-alcohol-attendance", "ex-da-devil-tumours"],
    "designed-experiment": ["ex-da-motn-insomnia", "ex-da-devil-tumours"],
    "randomised-controlled-trial": ["ex-da-blood-pressure-covariates", "ex-da-random-split"],
    "confounding-variable": ["ex-da-correlation-reading"],
    "sample-correlation-coefficient": ["ex-da-correlation-reading"],
    "simple-random-sample": ["ex-da-random-split"],
    "margin-of-error": ["ex-da-pilot-width", "ex-da-sleep-sample-size"],
}

_DATA_BOOK_EXAMPLES = {
    "exm-alices-caffeine-experiment": ["designed-experiment", "randomised-controlled-trial", "blinding-and-placebo"],
    "exm-sampling-ten-villages": ["stratified-and-cluster-sampling", "simple-random-sample"],
    "exm-the-ages-of-299-patients": ["sample-quantile", "interquartile-range", "sample-variance-and-standard-deviation"],
    "exm-anaemia-and-death": ["chi-squared-test-of-independence"],
    "exm-a-biased-coin": ["wald-interval", "binomial-test"],
    "exm-ten-normal-measurements": ["one-sample-t-pivot"],
    "exm-the-volume-of-a-drop": ["one-sample-t-pivot", "student-t-distribution"],
    "exm-first-and-third-year-weights": ["welch-interval", "pooled-variance"],
    "exm-simulating-the-power-of-a-t-test": ["power-function", "one-sample-t-test"],
    "exm-a-new-sweetener": ["binomial-test"],
    "exm-alices-caffeine-test": ["two-sample-t-test", "welch-interval"],
    "exm-two-labs-on-the-same-patients": ["one-sample-t-test"],
    "exm-five-treatments-for-cold-sores": ["one-way-analysis-of-variance", "bonferroni-correction", "tukey-intervals"],
    "exm-wheat-in-four-regions": ["interaction"],
    "exm-pesticide-and-fertilizer": ["interaction"],
    "exm-height-and-shoe-size": ["simple-linear-regression", "coefficient-of-determination"],
    "exm-predicting-a-students-height": ["prediction-interval"],
    "exm-height-shoe-size-and-weight": ["multiple-linear-regression", "adjusted-r-squared"],
    "exm-explaining-birth-weight": ["dummy-variable-coding", "multiple-linear-regression"],
    "exm-age-and-smoking-interact": ["interaction", "dummy-variable-coding"],
    "exm-a-hundred-balls-in-ten-boxes": ["pearson-chi-squared-approximation"],
}

_DATA_FIGURES = {
    "randomised-controlled-trial": ["da-01-studies-and-data-assignment.png", "da-alice-strip.png"],
    "confounding-variable": ["da-01-studies-and-data-assignment.png"],
    "sample-quantile": ["da-creatinine-shape.png"],
    "five-number-summary-and-boxplot": ["da-creatinine-shape.png", "da-creatinine-by-death.png"],
    "interquartile-range": ["da-creatinine-shape.png"],
    "normal-quantile-plot": ["da-creatinine-qq.png", "da-birthwt-residuals.png"],
    "sample-correlation-coefficient": ["da-sodium-jitter.png", "da-pairs.png"],
    "power-function": ["da-power-by-n.png"],
    "one-way-analysis-of-variance": ["da-coldsore.png"],
    "bonferroni-correction": ["da-coldsore.png"],
    "interaction": ["da-interaction.png", "da-birthwt-interaction.png"],
    "dummy-variable-coding": ["da-birthwt-interaction.png"],
    "multiple-linear-regression": ["da-pairs.png", "da-birthwt-residuals.png"],
    "pearson-chi-squared-approximation": ["da-chisq-simulation.png"],
    "chi-squared-test-of-independence": ["da-anaemia-death.png"],
}

for _table, _extra in ((EXAMPLES, _DATA_EXAMPLES), (BOOK_EXAMPLES, _DATA_BOOK_EXAMPLES), (FIGURES, _DATA_FIGURES)):
    for _name, _items in _extra.items():
        _table.setdefault(_name, []).extend(i for i in _items if i not in _table[_name])


# ---------------------------------------------------------------------------
# Self-contained teaching prose for thin or non-self-contained articles.
# ---------------------------------------------------------------------------

NOTES: dict[str, str] = {
    "a-finite-endpoint-and-a-weibull-extreme-value-law": r"""
## The gap below a hard ceiling

A sample maximum pressed against a finite upper endpoint has nowhere left to travel except into a shrinking gap. The question is how to magnify that gap so the limit is a proper distribution, neither a point mass at the endpoint nor a law that escapes to infinity.

Let $X_1,X_2,\ldots$ be independent copies with distribution function $F$, and write $M_n=\max\{X_1,\ldots,X_n\}$. The upper endpoint is $x_F=\sup\{x:F(x)<1\}$. For the uniform law on $(0,1)$ one has $x_F=1$. The scaled gap $Y_n=n(1-M_n)$ then satisfies, for $y\ge 0$ and $n>y$,

$$
\mathbb{P}(Y_n>y)=\left(1-\frac{y}{n}\right)^n\to e^{-y}.
$$

So $Y_n$ converges in distribution to the exponential law of rate $1$, supported on $[0,\infty)$. Equivalently, $n(M_n-1)$ converges in distribution to the reversed exponential law on $(-\infty,0]$. Centring moves towards the endpoint, and the limit lives entirely on one side of $0$. That one-sided shape is the Weibull extreme-value type.

## A numerical gap, and the other two types

For $n=50$ and $y=2$, $\mathbb{P}(M_{50}<0.96)=(0.96)^{50}\approx 0.130$, while $e^{-2}\approx 0.135$. About $13\%$ of uniform samples of size $50$ still have their maximum below $0.96$. Fisher and Tippett (1928) and Gnedenko (1943) place this limit beside two others: a [Gumbel law](exponential-tails-and-the-gumbel-law.qmd) for light unbounded tails, and a [Fréchet law](power-law-tails-and-the-frechet-law.qmd) for heavy tails. The [extreme-value classification](extreme-value-classification.qmd) is a statement about possible limits. The name Weibull here labels the finite-endpoint shape, which is a different object from a Weibull lifetime model.
""",
    "a-finite-stationary-point-is-a-global-maximiser": r"""
## Concavity from the logistic Hessian

Binary logistic regression chooses a finite coefficient vector $\beta$ by maximising the Bernoulli log-likelihood $\ell(\beta)$. Let $X$ be the $n\times d$ design matrix, with row $x_i^\top$ containing the covariates for case $i$ and usually a leading $1$ for an intercept. The success probability is $p_i=\sigma(x_i^\top\beta)$, where $\sigma(\eta)=1/(1+e^{-\eta})$, and $y$ and $p$ are the vectors of labels and probabilities. The score is $X^\top(y-p)$. Differentiating $p_i$ brings down the factor $p_i(1-p_i)$, so the Hessian is $-X^\top W X$ with $W=\operatorname{diag}\bigl(p_i(1-p_i)\bigr)$. Every finite $\beta$ forces $0<p_i<1$, and therefore every diagonal entry of $W$ is positive. The Gram matrix $X^\top W X$ is positive semi-definite, the minus sign makes the Hessian negative semi-definite, and $\ell$ is concave. For a concave objective every stationary point, meaning every root of the score, is a global maximiser.

## When the maximiser is unique

If $X$ has full column rank, $X^\top W X$ is [positive definite](positive-definite-matrix.qmd) and the Hessian is negative definite, so $\ell$ is strictly concave and the stationary point is the only maximiser. An intercept-only sample with labels $y=(0,1)$ has score $1-2p$ and Hessian $-2p(1-p)$. The unique root is $p=1/2$, hence $\beta=0$, where the Hessian equals $-1/2$. Duplicate columns of $X$ leave $\ell$ flat along a line, so a finite maximiser, when one exists, is not unique. Perfect separation is a different failure: if some direction already matches every training label, increasing its scale pushes each $p_i$ towards $0$ or $1$ and $\ell$ keeps rising, so the supremum is not attained at any finite $\beta$.
""",
    "a-hypothesis-region-is-not-a-separate-model": r"""
## One posterior, two regions

Region probabilities and model probabilities answer different questions. Suppose twenty boxes produce independent [Poisson](poisson-distribution.qmd) counts with mean $\theta$, the prior is a [gamma distribution](gamma-distribution.qmd) with shape $12$ and rate $1$, and the counts sum to $177$. The likelihood contributes a factor $e^{-20\theta}\theta^{177}$, so the posterior is the single gamma distribution with shape $189$ and rate $21$. The hypotheses $H_0\colon \theta \le 10$ and $H_1\colon \theta > 10$ are two pieces of that same line. The posterior is continuous, so $\mathbb{P}(\theta = 10 \mid x) = 0$ and the endpoint may be assigned to either region. The posterior probability of $H_0$ is the integral of this one density up to $10$, about $0.93$. An equal-tailed credible interval for the same posterior can still reach above $10$.

## When the claim has smaller dimension

Independence in a $2\times 3$ table is not a cut of one parameter space. A saturated multinomial has five free cell probabilities. Independence forces every cell probability to be a row margin times a column margin, a lower-dimensional surface in the simplex. A continuous prior on the full simplex, such as a [Dirichlet distribution](dirichlet-distribution.qmd), assigns probability zero to that surface, so integrating the saturated posterior cannot return a positive probability of independence. Each model needs its own parameter prior. The [marginal likelihood](marginal-likelihood-and-bayes-factor.qmd) is the sampling density averaged against that prior, and the [Bayes factor](marginal-likelihood-and-bayes-factor.qmd) is the ratio of the two marginal likelihoods. [Posterior odds](posterior-odds-factorisation.qmd) equal the Bayes factor times the prior odds of the models. Those prior odds are an extra modelling choice. They are not recovered by splitting a single posterior.
""",
    "a-single-threshold-unit-cannot-compute-xor": r"""
## Four corners and one straight cut

The exclusive-or, or [XOR](xor-problem.qmd), pattern on the unit square asks for output $0,1,1,0$ at the inputs $(0,0)$, $(0,1)$, $(1,0)$ and $(1,1)$. A threshold unit returns $f(w_0+w_1 x_1+w_2 x_2)$, where $f(u)=1$ if $u\ge 0$ and $f(u)=0$ if $u<0$. The weights $(w_0,w_1,w_2)$ define a half-plane. The attempt $w=(1,1)$ and $w_0=-1/2$ already shows the obstruction: the four net inputs are $-1/2$, $1/2$, $1/2$ and $3/2$, so the outputs are $0,1,1,1$. Both mixed corners are on, but the corner $(1,1)$ is on as well. That pattern is OR, not XOR. Any cut that accepts both mixed corners also accepts their average, which is the same point $(1/2,1/2)$ lying between $(1,1)$ and the origin.

## The inequalities cannot hold together

Write the four demands as strict or weak linear inequalities. Output $0$ at the origin forces $w_0<0$. Output $1$ at $(1,0)$ and at $(0,1)$ forces $w_0+w_1\ge 0$ and $w_0+w_2\ge 0$. Output $0$ at $(1,1)$ forces $w_0+w_1+w_2<0$. Adding the two mixed-corner inequalities gives $2w_0+w_1+w_2\ge 0$, which rearranges to $w_0+(w_0+w_1+w_2)\ge 0$. The sum of two strictly negative numbers cannot be nonnegative, so no real weights meet all four conditions. The same counting shows why AND and OR are possible: each leaves one corner on the opposite side of a single line. A second unit, or a hidden layer, can build coordinates in which XOR becomes linearly separable.
""",
    "a-zero-precision-entry-is-conditional-independence": r"""
## What a precision entry measures

Let $X=(X_1,\ldots,X_p)^\top$ be multivariate normal with mean $\mu$ and a nonsingular covariance $\Sigma$, and write $K=\Sigma^{-1}=(k_{jk})$ for the precision, or concentration, matrix. Index the coordinates by $V=\{1,\ldots,p\}$. For a multivariate normal, zero covariance is independence, and the same fact applied to a conditional distribution gives a precision test. The conditional covariance of a block given the remaining coordinates is a Schur complement of $\Sigma$, and that complement is the inverse of the corresponding block of $K$. In particular the conditional variance of $X_j$ given every other coordinate is $1/k_{jj}$, and the conditional covariance of $X_j$ and $X_k$ given the rest is proportional to $-k_{jk}$. Thus $k_{jk}=0$, for $j\neq k$, if and only if that conditional covariance is zero, which for this joint normal law is the conditional independence $X_j\perp X_k\mid X_{V\setminus\{j,k\}}$.

## A three-variable precision

The covariance and precision below are a chain in which the third variable is attached to nothing.

$$
\Sigma=\begin{pmatrix}1&1/2&0\\1/2&1&0\\0&0&1\end{pmatrix},
\qquad
K=\begin{pmatrix}4/3&-2/3&0\\-2/3&4/3&0\\0&0&1\end{pmatrix}.
$$

The zeros $k_{13}=k_{23}=0$ say that $X_3$ is conditionally independent of each of $X_1$ and $X_2$ given the remaining variable; here the whole off-diagonal row is zero, so $X_3$ is independent of $(X_1,X_2)$. The entry $k_{12}=-2/3$ is not zero, so $X_1$ and $X_2$ remain dependent given $X_3$. Their partial correlation is $-k_{12}/\sqrt{k_{11}k_{22}}=(2/3)/(4/3)=1/2$. Outside the normal family a zero in an inverse covariance need not mean conditional independence: the inversion step is linear algebra, and the independence step uses joint normality.
""",
    "adaboost": r"""
## Reweighting the cases a weak learner misses

AdaBoost builds a classifier for labels $y_i\in\{-1,+1\}$ by adding weak learners one at a time (Freund and Schapire, 1997). Start with equal weights $w_{1,i}=1/n_{\mathrm{train}}$ on the $n_{\mathrm{train}}$ training pairs $(x_i,y_i)$. At round $t$ the learner $f_t$, with values in $\{-1,+1\}$, is fitted to minimise the weighted error $\varepsilon_t$. The mismatch $Q[y,f]$ equals $0$ when the label and the prediction agree and equals $1$ otherwise, so $\varepsilon_t$ is the total weight on the mistakes, divided by the total weight. The coefficient $\alpha_t=\tfrac12\log\bigl((1-\varepsilon_t)/\varepsilon_t\bigr)$ uses the natural logarithm. It is positive only when $\varepsilon_t<1/2$: a learner that is no better than a coin toss on the current weights receives no positive vote. Each weight is then multiplied by $e^{-\alpha_t y_i f_t(x_i)}$, which is $e^{-\alpha_t}$ after a correct call and $e^{\alpha_t}$ after a mistake, and $Z_t$ rescales the weights so that they sum to $1$.

## One round with error $0.2$

Suppose the weighted error is $\varepsilon_1=1/5$. Then $\alpha_1=\tfrac12\log 4=\log 2\approx 0.693$. Correct cases are multiplied by $1/2$ and mistakes by $2$, and $Z_1=2\sqrt{(1/5)(4/5)}=4/5$. One way to realise that error is a single mistake of weight $1/5$, with the other three cases sharing weight $4/5$ equally. After the update those weights are $1/2$ on the mistake and $1/6$ on each correct case. The ensemble predicts the sign of $\sum_t\alpha_t f_t(x)$. A classical bound says that its training error is at most $\prod_t 2\sqrt{\varepsilon_t(1-\varepsilon_t)}$; one round at $\varepsilon=1/5$ contributes the factor $0.8$. A round with $\varepsilon_t=0$ makes $\alpha_t$ infinite, so a perfect weak learner needs a stopping convention.
""",
    "akaike-information-criterion": r"""
## A penalty aimed at prediction

Several parametric models $M_k$ may be fitted to the same sample $X_{\mathrm{all}}$ of $n$ observations. Model $M_k$ has a parameter $\Psi_k$ of dimension $d_k$, and $\widehat\Psi_k$ is a maximiser of its log-likelihood $\ell(\Psi_k;X_{\mathrm{all}},M_k)$. The maximised value always rises, or at least does not fall, when the candidate is enlarged, so the largest model would win a raw likelihood comparison. Akaike's criterion charges two units per free parameter (Akaike, 1974),

$$
\mathrm{AIC}_k=-2\ell(\widehat\Psi_k;X_{\mathrm{all}},M_k)+2d_k,
$$

and the selected index $k^*$ minimises $\mathrm{AIC}_k$. The penalty is an asymptotic correction for using the same sample to estimate $\Psi_k$ and to score the fitted density. Up to a constant that does not depend on $k$, AIC estimates the expected Kullback–Leibler divergence from the true distribution of a new observation to the fitted distribution.

## Two candidates at the same maximised fits

Take $n=100$, with $\ell(\widehat\Psi_1)=-140$ and $d_1=2$, against $\ell(\widehat\Psi_2)=-136$ and $d_2=5$. Then $\mathrm{AIC}_1=280+4=284$ and $\mathrm{AIC}_2=272+10=282$, so AIC prefers the larger model. The extra three parameters raised the log-likelihood by $4$, and the penalty rose by only $6$, which is not enough to offset $-2\times 4$. One further parameter improves AIC only when it raises the maximised log-likelihood by more than $1$. The derivation assumes a regular interior maximum, with $d_k$ counting genuinely free and identified parameters. Label switching, a parameter on a boundary, or a variance that can collapse makes $d_k$ and the penalty harder to justify. AIC is also not constructed to recover a true model order with probability tending to one.
""",
    "ancillary-statistic": r"""
## Variation the parameter does not move

Sufficiency asks which function of the sample carries the information about a parameter $\theta$. Ancillarity asks the complementary question. A statistic $A = A(X_1,\ldots,X_n)$ is ancillary for $\theta$ when its sampling distribution is the same at every $\theta$: probabilities such as $\mathbb{P}(A \in B)$ can be computed without knowing $\theta$. The formula for $A$ uses only the data. What is free of $\theta$ is the distribution of $A$, not the expression. The property is relative to the named parameter and the model. A statistic ancillary for a normal mean, with the variance treated as known, need not be ancillary for the pair consisting of the mean and the variance.

## Residuals, and why completeness matters

Let $X_1,\ldots,X_n$ be independent and $\operatorname{N}(\mu, \sigma^2)$ with $\sigma^2$ known. Adding $\mu$ to every observation cancels in the differences, so the centred vector $(X_1 - \overline{X},\ldots,X_n - \overline{X})$ has a distribution free of $\mu$. It is ancillary for $\mu$, while $\overline{X}$ is sufficient. A pattern in those centred residuals is not evidence about $\mu$ inside this model, though it can be evidence against the model. [Basu's theorem](basu-s-theorem.qmd) upgrades the separation to independence once the [sufficient statistic](sufficient-statistic.qmd) is [complete](complete-statistic.qmd). Completeness is essential. For a uniform sample on $(\theta, \theta+1)$ the range is ancillary, yet it is a function of the minimal sufficient pair of order statistics, so that pair is not independent of every ancillary statistic.
""",
    "anova-sum-of-squares-decomposition": r"""
## An algebraic split

Comparing group means starts from an identity. Let $Y_{ij}$ be observation $i$ in group $j$, with $i=1,\ldots,n_j$ and $j=1,\ldots,k$, and set $n=\sum_j n_j$. The group mean $\overline Y_{\cdot j}$ averages over $i$, and the grand mean $\overline Y_{\cdot\cdot}$ averages all $n$ observations. Write each gap from the grand mean as a within-group gap plus a between-group gap,

$$
Y_{ij}-\overline Y_{\cdot\cdot}=(Y_{ij}-\overline Y_{\cdot j})+(\overline Y_{\cdot j}-\overline Y_{\cdot\cdot}).
$$

Squaring and summing kills the cross term: inside group $j$, $\sum_i(Y_{ij}-\overline Y_{\cdot j})=0$. What remains is $\mathrm{SS}_{\mathrm{total}}=\mathrm{SS}_{\mathrm{treatment}}+\mathrm{SS}_{\mathrm{error}}$. The treatment sum weights $(\overline Y_{\cdot j}-\overline Y_{\cdot\cdot})^2$ by the group size $n_j$. The error sum is the scatter inside groups. Unequal variances do not affect this algebra.

The $F$ reference law needs a probability model. If the $Y_{ij}$ are independent and normal, with group mean $\mu_j$ and a common variance $\sigma^2$, then $\mathrm{SS}_{\mathrm{error}}/\sigma^2$ is chi-squared on $n-k$ [degrees of freedom](degrees-of-freedom.qmd), and the mean square $\mathrm{MS}_{\mathrm{error}}=\mathrm{SS}_{\mathrm{error}}/(n-k)$ estimates $\sigma^2$ whether or not the $\mu_j$ are equal. When $\mu_1=\cdots=\mu_k$, $\mathrm{SS}_{\mathrm{treatment}}/\sigma^2$ is chi-squared on $k-1$ degrees of freedom and independent of the error sum, so the ratio of mean squares has the [ANOVA $F$ distribution](anova-f-distribution.qmd). Dependence, or a different variance in each group, leaves the split true and that $F$ law false. The chi-squared count is the [normal sample theorem](normal-sample-theorem.qmd) applied within groups and then to the group means.

## Four numbers

For the groups $(1,3)$ and $(5,7)$ the group means are $2$ and $6$ and the grand mean is $4$. Then $\mathrm{SS}_{\mathrm{treatment}}=16$, $\mathrm{SS}_{\mathrm{error}}=4$ and $\mathrm{SS}_{\mathrm{total}}=20$.
""",
    "aperiodic-markov-chain": r"""
## A clock the chain cannot forget

A chain can possess a stationary distribution and still fail to settle down to it. The obstruction is a rigid clock: returns to a state may be possible only on a lattice of times, so the distribution at time $n$ keeps oscillating.

Let $P=(p_{ij})$ be the transition matrix of a discrete-time chain, and write $p_{ii}^{(n)}$ for the $n$-step return probability. The period of state $i$ is

$$
d(i)=\gcd\{n\ge 1: p_{ii}^{(n)}>0\}.
$$

Aperiodicity means $d(i)=1$. That gcd is constant on a communicating class, so one speaks of the period of the class. A self-loop forces $d(i)=1$. A self-loop is not necessary: return lengths $2$ and $3$ already have gcd $1$, and that is enough for the whole class.

## Alternation against a chain that can wait

The deterministic alternation $0\to 1\to 0$, with $p_{01}=p_{10}=1$, has stationary row vector $\pi=(1/2,1/2)$, because each state is occupied half the time along every path. Its period is $2$: $p_{00}^{(n)}$ equals $1$ for even $n$ and $0$ for odd $n$, so $p_{00}^{(n)}$ never converges. On a finite [irreducible](irreducible-markov-chain.qmd) class, aperiodicity is exactly the extra assumption that turns the unique [stationary distribution](stationary-distribution.qmd) into a limit, $p_{ij}^{(n)}\to\pi_j$. The long-run proportion of visits still converges to $\pi_j$ when the chain is periodic. Period blocks the distribution at one distant time, not the time average. See [finite irreducible chains](finite-irreducible-chains.qmd).
""",
    "apparent-error": r"""
## Scoring a rule on the cases that built it

A classifier $\eta$ maps a feature vector to a class label. Under zero–one loss the mismatch $Q(y,\hat y)$ equals $0$ when $y=\hat y$ and equals $1$ otherwise, so an average of $Q$ is an error rate. The apparent error, or resubstitution error, plugs in the rule $\eta_{(X,y)}$ fitted to the whole observed sample $(X,y)=\{(x_i,y_i)\}_{i=1}^n$ and then averages $Q$ on those same $n$ pairs. The quantity is easy to compute and it describes the fit. It is a poor estimate of the error on a fresh draw from the same distribution, because each summand helped to choose the rule that is being scored. The dependence tends to pull the average down.

## A rule whose apparent error is exactly zero

For the one-nearest-neighbour rule with a metric and no distance ties, the nearest training point to $x_i$ is $x_i$ itself, at distance zero. Then $Q(y_i,\eta_{(X,y)}(x_i))=0$ for every $i$, and the apparent error is $0$. The same memorising rule, applied to a new point, copies the label of a neighbour that is merely close, and that prediction can be wrong. A tree grown until every leaf is pure has the same training score and the same difficulty. Holding cases out of the fit, as in [cross-validation](cross-validation.qmd), breaks the dependence between the summand and the rule. The apparent error remains useful as the optimistic end of a comparison, and as one ingredient in a bootstrap correction, but it should not be read as the error of the deployed classifier.
""",
    "arch-and-garch-models": r"""
## Volatility that clusters

Large financial returns tend to arrive in bursts. A calm stretch is followed by more calm, and a violent day is followed by another, even when the average return is close to zero. Autoregressive conditional heteroscedasticity, introduced by Engle (1982), puts a model on that changing scale rather than on the mean. Write the return as $r_t=\sigma_t\varepsilon_t$, where the innovation $\varepsilon_t$ has mean $0$ and variance $1$, is uncorrelated over time, and given the past has conditional mean $0$ and conditional variance $1$, and where $\sigma_t^2=\operatorname{Var}(r_t\mid r_{t-1},r_{t-2},\ldots)$ is the variance conditional on the past. An ARCH(1) model uses only yesterday's squared return,

$$
\sigma_t^2=\alpha_0+\alpha_1 r_{t-1}^2,
$$

with $\alpha_0>0$ and $\alpha_1\ge 0$. The generalised form of Bollerslev (1986) lets yesterday's conditional variance persist as well, $\sigma_t^2=\alpha_0+\alpha_1 r_{t-1}^2+\beta_1\sigma_{t-1}^2$, with $\beta_1\ge 0$. If $\alpha_1+\beta_1<1$, the unconditional variance is the finite value $\alpha_0/(1-\alpha_1-\beta_1)$. If that sum is $1$ or larger, the unconditional variance is not finite.

## One shock, then a slow decay

Take $\alpha_0=0.02$, $\alpha_1=0.10$ and $\beta_1=0.85$. The stationary variance is $0.02/0.05=0.4$. A return of size $2$ adds $0.10\times 4=0.4$ at the next step, so the conditional variance equals $0.42+0.85\sigma_{t-1}^2$, which is at least $0.42$. The excess over the stationary value $0.4$ then decays, in conditional expectation, by the factor $\alpha_1+\beta_1=0.95$ a day: $0.85$ carries the current conditional variance forward, and the new squared return contributes a further $0.10$ on average. The conditional mean of $r_t$ can remain $0$: the model widens a [prediction interval](prediction-interval.qmd), it does not aim the return. Because the shock enters as a square, one enormous return can dominate a short-sample estimate of $\alpha_1$. That day has to be checked before it is read as a new regime.
""",
    "arima-model": r"""
## Differencing until the changes settle

A series that wanders does not have a useful fixed mean. An autoregressive integrated moving-average model differences the series until the changes look stationary, then fits a short-memory model to those changes. Write $\nabla X_t=X_t-X_{t-1}$. An ARIMA$(p,d,q)$ model says that $\nabla^d X_t$, the series differenced $d$ times, is a stationary autoregressive moving-average process of autoregressive order $p$ and moving-average order $q$. The case $d=0$ is already stationary and is an ordinary ARMA model. A random walk $X_t=X_{t-1}+\varepsilon_t$, with innovations of mean $0$ and variance $\sigma^2$, is ARIMA$(0,1,0)$: one difference, and the difference is [white noise](white-noise.qmd).

## A seasonal lag, and one difference too many

Monthly series often need a second operator, $\nabla_{12}X_t=X_t-X_{t-12}$, as well as $\nabla$. The point forecast is then the conditional mean of the future level, rebuilt from the differenced forecast, and the prediction variance grows with the horizon because each extra step adds innovation variance. Differencing a series that was already stationary is the matching mistake. If $X_t$ itself is white noise, $\nabla X_t=\varepsilon_t-\varepsilon_{t-1}$ is a moving average of order $1$ whose lag-$1$ autocorrelation equals $-1/2$. The residual plot then shows a large negative spike that the original shocks did not have, and a further moving-average term is being asked to cancel a root that the differencing put in. The order $d$ is chosen so that this spike is not manufactured.
""",
    "artificial-neuron": r"""
## A weighted sum followed by a fixed nonlinearity

An artificial neuron is a device for a decision or a numeric feature that depends on the inputs only through one linear score. Inputs $x_1,\ldots,x_p$ are combined with weights $w_1,\ldots,w_p$ and a bias $w_0$. Setting $x_0=1$ writes the net input as $\mathrm{net}=w_0+w^\top x=\sum_{j=0}^p w_j x_j$. The output is $o=f(\mathrm{net})$ for a chosen [activation function](activation-function.qmd) $f$. The bias is not a separate kind of parameter: it is the weight on a constant input, so a derivative with respect to $w_0$ has the same product form as a derivative with respect to any other weight. With the threshold $f(u)=1$ for $u\ge 0$ and $f(u)=0$ otherwise, the unit splits the input space along the hyperplane $\mathrm{net}=0$.

## Weights that compute AND

The weights $w_0=-3/2$, $w_1=1$ and $w_2=1$ compute the AND of two binary inputs. The four net inputs are $-3/2$ at $(0,0)$, $-1/2$ at $(1,0)$ and at $(0,1)$, and $+1/2$ at $(1,1)$. The threshold therefore returns $0,0,0,1$. Replacing the threshold by the logistic $g(u)=1/(1+e^{-u})$ at those same nets returns about $0.182$, $0.378$, $0.378$ and $0.622$. The ordering is preserved, but the output is a soft score rather than a bit, and $g'(u)=g(u)\bigl(1-g(u)\bigr)$ is available for gradient training. That derivative equals $1/4$ at $u=0$ and is already small once $|u|$ is large, so a saturated unit moves its weights slowly. One threshold unit still only represents a half-space. Patterns that are not linearly separable need further units whose outputs become inputs to a later unit.
""",
    "atom-of-a-distribution": r"""
## Probability sitting on a single point

A distribution function can rise smoothly, or it can jump. An atom is a point that carries a lump of probability, and the size of the jump is that lump. Without the jump, probabilities of exact values would be invisible in $F$.

Let $X$ be a real random variable and let $F_X(x)=\mathbb{P}(X\le x)$. The left limit is $F_X(x-)=\lim_{y\uparrow x}F_X(y)=\mathbb{P}(X<x)$. The point $x$ is an atom when $\mathbb{P}(X=x)>0$, and the jump identity is

$$
\mathbb{P}(X=x)=F_X(x)-F_X(x-).
$$

Right-continuity is the convention that puts the atom into the value $F_X(x)$ rather than leaving it to the next point. A law is discrete when it is a countable sum of atoms. A law with a density has no atoms: $F_X$ is continuous and $\mathbb{P}(X=x)=0$ at every single $x$, even at points where the density is positive.

## A coin, and a mixture

A fair Bernoulli trial has atoms at $0$ and at $1$, each of mass $1/2$. Thus $F_X(0)=1/2$ and $F_X(0-)=0$. The uniform law on $(0,1)$ has $F_X(x)=0$ for $x\le 0$, $F_X(x)=x$ for $x\in(0,1)$, and $F_X(x)=1$ for $x\ge 1$, so every jump is zero. The two can be mixed. With probability $1/2$ draw the Bernoulli trial, and with probability $1/2$ draw the uniform number. Then $\mathbb{P}(X=0)=\mathbb{P}(X=1)=1/4$, while $F_X$ also increases continuously on $(0,1)$ with slope $1/2$. Atoms and a density may occupy the same [distribution function](cumulative-distribution-function.qmd). See [discrete distributions](discrete-distribution.qmd) and [continuous distributions](continuous-distribution.qmd).
""",
    "average-linkage": r"""
## The typical cross-pair, counting multiplicity

[Hierarchical clustering](hierarchical-clustering.qmd) merges groups from a matrix of dissimilarities $d(x,y)$. Single linkage uses the nearest cross-pair and can chain distant points through a bridge of neighbours. Complete linkage uses the farthest cross-pair and is driven by diameter. Average linkage answers the intermediate question: how far apart is a randomly chosen member of $D_1$ from a randomly chosen member of $D_2$? If clusters are multisets, so that a repeated point is legal, the denominator is the product of the cardinalities $|D_1|\,|D_2|$, and every copy contributes to the sum. The resulting $d_A$ depends only on the cross-pairs. It does not require the points to sit in a vector space, which matters when $d$ is an edit distance or another dissimilarity with no coordinates to average.

## Three points, and a repeated point

On the line with absolute difference as $d$, the points $0$, $1$ and $4$ first merge $\{0,1\}$ at height $1$. The average linkage from that pair to $4$ is $(|4-0|+|4-1|)/2=3.5$. The single-linkage height of the same merge would be $3$, and the complete-linkage height would be $4$, so $3.5$ sits between them. Now replace the cluster $\{0,1\}$ by the multiset $\{0,0,1\}$, cardinality $3$. The three cross-distances to $4$ are $4$, $4$ and $3$, and $d_A=(4+4+3)/3=11/3\approx 3.67$. Dropping the duplicate would have left $3.5$, so the cardinality convention is part of the definition whenever repeated points occur. Average linkage still has no guarantee of recovering spherical clusters of equal size; it only specifies which cross-pair summary is being minimised at each merge.
""",
    "backpropagation-batch-form": r"""
## Names for the forward and backward signals

Consider a network with one hidden layer, logistic activations $g(u)=1/(1+e^{-u})$, and training sum of squares $E=\sum_i\sum_k(y_{ik}-o_{ik})^2$ with no leading factor $1/2$. For pattern $i$, input coordinate $j$ (with $x_{i0}=1$), hidden unit $q$ and output unit $k$, the forward pass stores the hidden net input $u_{iq}=\sum_j w_{jq}x_{ij}$, the hidden output $h_{iq}=g(u_{iq})$, the output net input $z_{ik}=\sum_q w_{qk}h_{iq}$ (with $h_{i0}=1$), and the output $o_{ik}=g(z_{ik})$. The logistic derivative is $g'(u)=g(u)\bigl(1-g(u)\bigr)$. The output delta folds the residual together with that slope and with the factor $2$ from differentiating a square,

$$
\delta_{ik}^{(o)}=-2(y_{ik}-o_{ik})\,o_{ik}(1-o_{ik}).
$$

The hidden delta $\delta_{iq}^{(h)}$ multiplies $h_{iq}(1-h_{iq})$ by $\sum_k w_{qk}\delta_{ik}^{(o)}$, sharing the output residuals in proportion to the outgoing weights. Summing $\delta_{ik}^{(o)}h_{iq}$ over patterns produces the gradient entry $G_{qk}$ for a hidden-to-output weight, and summing $\delta_{iq}^{(h)}x_{ij}$ produces $G_{jq}$ for an input-to-hidden weight.

## One pattern and a step of size $0.1$

Take a single pattern with target $y=1$, output $o=0.6$ and a hidden signal $h=1/2$ on the weight being updated. Then $\delta^{(o)}=-2(0.4)(0.6)(0.4)=-0.192$, and $G=\delta^{(o)}h=-0.096$. The batch update $w\leftarrow w-\varepsilon G$ with learning rate $\varepsilon=0.1$ increases that weight by $0.0096$, which raises the net input and moves $o$ towards the target. If this hidden unit has slope factor $h(1-h)=1/4$ and a single outgoing weight equal to $1$, its delta is $(1/4)(-0.192)=-0.048$. An input value $x=2$ then contributes gradient $-0.096$, so the same step increases the input weight as well. The pass uses one frozen forward state: mixing new outgoing weights into old activations would not be the gradient of that $E$.
""",
    "basic-gradient-descent-learning": r"""
## Walking downhill on the training error

Training here means choosing weights to make the training sum of squares $E$ small. Squared error is differentiable, so a step can follow $-\partial E/\partial w$. Draw each initial weight independently from the uniform distribution on $[-1/2,1/2]$, a scale small enough that logistic units start near the steep part of their curve rather than already saturated. Then pass every training pattern through the current network, recompute $E$, and replace each weight by $w-\varepsilon\,\partial E/\partial w$, where the learning rate $\varepsilon>0$ is the step length. The product $\varepsilon\,\partial E/\partial w$ is the whole proposed change: a large partial derivative and a large $\varepsilon$ are interchangeable ways to take a long step. Stop when $E$ is acceptable for the task, or when successive weights barely move.

## A local slope is not a global map

Suppose one coordinate currently has $\partial E/\partial w=-4$. With $\varepsilon=0.1$ the update adds $0.4$ to that weight, a short step in the downhill direction. With $\varepsilon=2$ the same derivative proposes a jump of $8$, which can leave the region in which the derivative was about $-4$. On a multilayer network $E$ is nonconvex. Hidden units can be permuted, and a sign flip in one layer can be absorbed by the next, so many different weight vectors represent the same function. Gradient descent follows the basin of its initial draw. Repeating the random start and keeping the smallest training $E$ only compares those basins.
""",
    "basu-s-theorem": r"""
## Conditional expectation that completeness flattens

Independence of a sufficient statistic and an ancillary statistic is often wanted and rarely convenient to check from the joint density, because both are functions of one sample. Let $T$ be a [complete](complete-statistic.qmd) [sufficient statistic](sufficient-statistic.qmd) for $\theta$, and let $A$ be [ancillary](ancillary-statistic.qmd). For a bounded function $g$, ancillarity makes $c = \mathbb{E}[g(A)]$ a constant. Sufficiency makes the conditional law of the sample given $T$, and therefore $h(t) = \mathbb{E}[g(A) \mid T = t]$, free of $\theta$. Then $\mathbb{E}_{\theta}[h(T) - c] = 0$ for every $\theta$. Completeness forces $h(T) = c$ almost surely, so $\mathbb{E}[g(A) \mid T] = \mathbb{E}[g(A)]$. A random element whose conditional expectation given $T$ ignores $T$, for every bounded $g$, is independent of $T$. This is Basu's theorem (Basu, 1955).

## A location family where the hypothesis fails

The completeness hypothesis cannot be omitted. Let $X_1,\ldots,X_n$ be uniform on $(\theta, \theta+1)$. The order-statistic pair $T = (X_{(1)}, X_{(n)})$ is minimal sufficient. The range $R = X_{(n)} - X_{(1)}$ is ancillary, because a location shift cancels, and for a uniform sample on an interval of length one its expectation is $(n-1)/(n+1)$. Thus $R - (n-1)/(n+1)$ has mean zero for every $\theta$ without being almost surely zero, so $T$ is not complete. The same range is a non-degenerate function of $T$, hence not independent of $T$. In the normal model with known variance the hypotheses do hold: $\overline{X}$ is complete and sufficient for $\mu$, the centred residual vector is ancillary, and the mean used for estimation is independent of the residual pattern.
""",
    "bayes-consistency-of-nearest-neighbours": r"""
## Local votes that become exact in the limit

The $k$-nearest-neighbour rule classifies a query by the majority label among the $k$ closest points of an independent identically distributed training sample of size $n$, in Euclidean space of a fixed dimension. Let $\tau_g(x)=\mathbb{P}(Y=g\mid X=x)$ and write $R^*$ for the [Bayes risk](bayes-classifier.qmd), the smallest error achievable by any measurable rule under zero–one loss. A fixed neighbourhood size keeps a random vote: even if the neighbours sit at the query, one neighbour samples the conditional label rather than recovering $\tau_g(x)$. Letting $k=k_n$ grow washes out that voting noise. Forcing $k_n/n\to 0$ keeps the neighbourhood inside a vanishing fraction of the sample, so the neighbours approach the query and still represent the local conditional distribution. Under those two conditions, and with a fixed tie-breaking rule, the expected error of the $k$-nearest-neighbour classifier tends to $R^*$ for any joint distribution of $(X,Y)$ (Stone, 1977).

## Rates that look moderate, and limits that do not apply

For $n=1000$ and $k_n=31$, the neighbour count is already large while $k_n/n=0.031$ is small. The choice $k_n=500$ uses half the sample, so the vote is stable but not local, and $k_n/n\not\to 0$. The choice $k_n=1$ stays local but never averages out label noise; its asymptotic error is controlled by the Cover–Hart factor rather than driven all the way to $R^*$. Fixed dimension is part of the hypothesis. In a growing dimension, distances concentrate and the nearest of $n$ points need not be near the query in the sense the proof uses.
""",
    "bayes-optimal-rule": r"""
## The conditional risk decides the label

A fresh pair $(X,Y)$ is drawn, $X=x$ is observed, and the classifier must name a class in $\{1,\ldots,G\}$. Write $\tau_g(x)=\mathbb{P}(Y=g\mid X=x)$ for the posterior probability of class $g$. Under [zero–one loss](zero-one-loss-and-risk.qmd) the loss is $0$ if the predicted class equals $Y$ and $1$ otherwise, so the conditional risk of predicting $g$ is $1-\tau_g(x)$. The sum of the posterior probabilities is $1$, and nothing in the loss treats one kind of mistake as more expensive than another. The conditional risk is therefore minimised by any class of largest posterior probability,

$$
B(x)=\arg\max_{g\in\{1,\ldots,G\}}\tau_g(x).
$$

A rule that attains this minimum at every $x$ is a Bayes rule. Its overall risk $R^*=\mathbb{E}\bigl[1-\max_g\tau_g(X)\bigr]$ is the Bayes risk, a lower bound for every other measurable classifier under the same loss.

## Three posteriors and a tie

At a point with $\tau(x)=(0.20,0.55,0.25)$ the minimum conditional risk is $1-0.55=0.45$, achieved only by predicting class $2$. Predicting class $1$ instead has conditional risk $0.80$, and predicting class $3$ has conditional risk $0.75$. If the posteriors are $(0.40,0.40,0.20)$, both class $1$ and class $2$ achieve the conditional risk $0.60$, and either prediction is Bayes. The argument uses the true posteriors. A plug-in classifier that replaces $\tau_g$ by an estimate keeps the same comparison, so its risk is at least $R^*$, as is the risk of every other measurable rule. The risk equals $R^*$ when the plugged-in probabilities pick a true maximiser for almost every $x$, which can happen while the estimated probabilities are still not $\tau_g$. Unequal misclassification costs replace $1-\tau_g(x)$ by a weighted sum of the other posteriors, and the maximiser of $\tau_g$ can then cease to be optimal.
""",
    "bayesian-information-criterion": r"""
## The penalty that remains after a Laplace approximation

BIC compares models $M_k$ on one sample $X_{\mathrm{all}}$ of size $n$ by approximating a posterior probability of the model (Schwarz, 1978). Let $\Psi_k$ be the $d_k$-dimensional parameter of $M_k$, and let $\ell(\widehat\Psi_k;X_{\mathrm{all}},M_k)$ be the log-likelihood at a maximiser. A Gaussian integral around a regular interior peak has volume of order $n^{-d_k/2}$: each of the $d_k$ parameter directions is localised by an information that grows like $n$. Multiplying the marginal likelihood by $-2$ and dropping terms that stay bounded as $n$ grows leaves

$$
\mathrm{BIC}_k=-2\ell(\widehat\Psi_k;X_{\mathrm{all}},M_k)+d_k\log n.
$$

The selected index minimises $\mathrm{BIC}_k$. The logarithm is natural, as in the Laplace expansion. One extra parameter improves BIC only when it raises the maximised log-likelihood by more than $\tfrac12\log n$.

## The same two fits, scored by BIC

For $n=100$, $\log 100\approx 4.605$. Let $\ell(\widehat\Psi_1)=-140$ with $d_1=2$, and $\ell(\widehat\Psi_2)=-136$ with $d_2=5$. Then $\mathrm{BIC}_1=280+2\times 4.605=289.21$ and $\mathrm{BIC}_2=272+5\times 4.605=295.03$. BIC selects $M_1$. AIC, with penalties $4$ and $10$, selects $M_2$ on these same maximised log-likelihoods. The two criteria are answering different questions. The Laplace step needs a quadratic peak in the interior of the parameter space, with $d_k$ counting free and identified coordinates. A mixture with a vanishing weight, two components that coincide, or a covariance that can collapse onto a point, violates that geometry. Close BIC values also leave the discarded $O(1)$ terms, including the prior, able to change the ranking.
""",
    "benjamini-hochberg": r"""
## A line through the ordered $p$-values

Order the $m$ $p$-values as $P_{(1)}\le\cdots\le P_{(m)}$, and let $H_{(i)}$ be the null hypothesis attached to $P_{(i)}$. Choose a target false-discovery level $q^*\in(0,1)$. The Benjamini–Hochberg threshold at rank $i$ is $(i/m)q^*$, a straight line from $q^*/m$ up to $q^*$. Find the largest index $k$ such that $P_{(k)}$ lies on or below its own threshold, and reject $H_{(1)},\ldots,H_{(k)}$. If even $P_{(1)}$ exceeds $q^*/m$, reject nothing. The step-up form matters: rejection is not decided by checking each $p$-value against its own threshold in isolation. Once a later $p$-value crosses below the line, every hypothesis of smaller rank is rejected with it, including one whose $p$-value sits above the line at its own index.

## Four tests at level $0.20$

Take $m=4$, $q^*=0.20$ and sorted $p$-values $0.06$, $0.08$, $0.14$, $0.50$. The thresholds $(i/4)\times 0.20$ are $0.05$, $0.10$, $0.15$ and $0.20$. Then $0.06>0.05$, $0.08\le 0.10$, $0.14\le 0.15$ and $0.50>0.20$. The largest successful index is $k=3$, so the procedure rejects the three smallest $p$-values. In particular $H_{(1)}$ is rejected even though $0.06$ exceeds $0.05$. Stopping at the first failure would have rejected nothing and would be a different, more conservative rule. Bonferroni at level $0.20$ uses the single cutoff $0.20/4=0.05$ and, on these numbers, rejects nothing. The gain comes from allowing a controlled expected proportion of false discoveries rather than protecting the probability of any false discovery. The validity of that control still depends on how the $p$-values were derived.
""",
    "benjamini-hochberg-controls-the-false-discovery-rate": r"""
## The proportion of false calls among the calls that were made

Suppose $m$ hypotheses are tested, of which $m_0$ are true nulls, and let $q^*\in(0,1)$ be the target level of the Benjamini–Hochberg procedure. Let $V$ be the number of true nulls that are rejected and $R$ the number of rejections. The false-discovery proportion is $Q=V/R$ when $R>0$ and $Q=0$ when nothing is rejected, and the false-discovery rate is $\mathrm{FDR}=\mathbb{E}(Q)$. This is not the family-wise probability of at least one false rejection. It is the expected share of the rejected list that should not have been rejected. Under mutual independence of the $p$-values, and under the validity bound $\mathbb{P}(P_i\le t)\le t$ for every true null, the procedure satisfies $\mathrm{FDR}\le (m_0/m)q^*\le q^*$ (Benjamini and Hochberg, 1995). When the true-null $p$-values are exactly uniform, the first inequality is an equality.

## A numerical guarantee, and a dependence warning

With $m=1000$, $m_0=900$ and $q^*=0.05$, the theorem gives $\mathrm{FDR}\le 0.045$. The ratio $m_0/m$ is unknown at the time of testing, so the procedure is calibrated to the conservative target $q^*$. The independence hypothesis can be weakened to positive regression dependence on the true nulls, and the same $q^*$ still controls the rate (Benjamini and Yekutieli, 2001). Arbitrary dependence is not covered by that extension. A sufficient repair divides $q^*$ by the harmonic sum $c(m)=\sum_{j=1}^m 1/j$, which is about $7.49$ when $m=1000$, and then rejects on the stricter line $i q^*/\bigl(m\,c(m)\bigr)$. Invalid $p$-values, for example from a misspecified null distribution, fall outside the argument entirely, because the proof uses $\mathbb{P}(P_i\le t)\le t$.
""",
    "bernoulli-distribution": r"""
## One trial with two outcomes

A Bernoulli trial records a yes-or-no event as a number. Let $A$ be an event with probability $p\in[0,1]$, and let $X=1$ when $A$ occurs and $X=0$ otherwise. Then $\mathbb{P}(X=1)=p$ and $\mathbb{P}(X=0)=1-p$, written $X\sim\operatorname{Bern}(p)$. The same law is the distribution of a single draw that equals $1$ with probability $p$. Because the only possible values are $0$ and $1$, the square collapses: $X^2=X$. Hence $\mathbb{E} X^2=\mathbb{E} X=p$, and

$$
\operatorname{Var}(X)=\mathbb{E} X^2-(\mathbb{E} X)^2=p-p^2=p(1-p).
$$

The quadratic $p(1-p)$ is largest at $p=1/2$, where the variance is $1/4$, and it is $0$ at $p=0$ and at $p=1$, where the outcome is certain. A very rare event and a very common event are both predictable; a fair coin is the noisiest single trial.

## Adding independent copies

If $X_1,\ldots,X_n$ are independent and each is $\operatorname{Bern}(p)$, their sum is a [binomial count](binomial-distribution.qmd) with parameters $n$ and $p$. The mean adds, and independence makes the variances add, so the sum has mean $np$ and variance $np(1-p)$. For a concrete rate, take $p=1/5$. One trial has mean $1/5$ and variance $4/25$. Ten independent trials have mean $2$ and variance $8/5$. The [probability generating function](probability-generating-function.qmd) of one trial is $1-p+pz$, and the moment generating function is $1-p+pe^{s}$. Both factor across independent trials, which is another way to see the binomial sum.
""",
    "bias-of-an-estimator": r"""
## Variance plus squared bias

An [estimator](estimator.qmd) $\widehat\theta$ of a target $\theta$ is a random variable computed from the sample. Its bias is $\operatorname{bias}(\widehat\theta)=\mathbb{E}\widehat\theta-\theta$, defined whenever the expectation exists. The estimator is [unbiased](unbiased-estimator.qmd) when this difference is $0$ for every $\theta$ under consideration. Bias $0$ says the estimates are centred on the target on average. It does not say that a typical estimate is close.

Closeness is measured by the [mean squared error](mean-squared-error.qmd) $\mathbb{E}(\widehat\theta-\theta)^2$. When the variance is finite the error splits exactly as

$$
\mathbb{E}(\widehat\theta-\theta)^2=\operatorname{Var}(\widehat\theta)+\{\operatorname{bias}(\widehat\theta)\}^2.
$$

A reduction in variance can outweigh a small squared bias. Bias is also not preserved by nonlinear rewrites. If $\widehat\theta$ is unbiased for $\theta$ and $g$ is curved, $g(\widehat\theta)$ is usually biased for $g(\theta)$. In particular the square root of an unbiased variance estimator is biased for the standard deviation, because the square root is strictly concave and the estimator is not constant.

## The normal variance, divided by $n$ or by $n-1$

Let $X_1,\ldots,X_n$ be independent and $\operatorname{N}(\mu,\sigma^2)$, and let $s^2=\frac1{n-1}\sum_i(X_i-\overline X)^2$. Then $\mathbb{E} s^2=\sigma^2$, while the [normal maximum likelihood estimator](maximum-likelihood-for-a-normal-sample.qmd) $\widehat\sigma^2=\frac{n-1}{n}s^2$ has bias $-\sigma^2/n$. Normality gives $\operatorname{Var}(s^2)=2\sigma^4/(n-1)$. For $n=10$ that variance is $2\sigma^4/9$, so the unbiased estimator has mean squared error $2\sigma^4/9$. The maximum likelihood estimator has variance $0.18\sigma^4$ and squared bias $0.01\sigma^4$, hence mean squared error $0.19\sigma^4$. The biased estimator wins. Away from normality the variance of $s^2$ also depends on the fourth moment, and the comparison can reverse.
""",
    "binary-logistic-regression": r"""
## Bernoulli trials with a logistic mean

Each response $y_i$ is $0$ or $1$, with success probability $p_i$ that depends on a covariate vector $x_i$. Binary logistic regression sets $p_i=\sigma(\beta^\top x_i)$ with $\sigma(\eta)=1/(1+e^{-\eta})$ and $\beta$ an unknown coefficient vector, usually including an intercept through a coordinate $x_{i0}=1$. The observations are treated as independent Bernoulli trials, so the likelihood is the product $p_i^{y_i}(1-p_i)^{1-y_i}$ and the log-likelihood $\ell(\beta)$ is the sum of $y_i\log p_i+(1-y_i)\log(1-p_i)$. The logarithm is natural. The odds of success are $p_i/(1-p_i)=\exp(\beta^\top x_i)$, so a coefficient is a change in log-odds. If the coordinate of sepal length has coefficient $0.5$, then a one-unit increase in that coordinate, with the other coordinates held fixed, multiplies the odds by $e^{0.5}\approx 1.649$.

## A probability, a classification, and separation

The fitted probability at a new $x$ is $\sigma(\widehat\beta^\top x)$. The equal-cost classification rule predicts success when that probability is at least $1/2$, which is the same event as $\widehat\beta^\top x\ge 0$. The likelihood uses the probabilities themselves: predicting $0.99$ on a failure is a much worse contribution to $\ell$ than predicting $0.6$. A single success with an intercept only has $\ell(\beta)=\log\sigma(\beta)$, whose derivative $1-\sigma(\beta)$ is positive for every finite $\beta$. The log-likelihood rises towards $0$ as $\beta\to+\infty$ and never has a stationary point. That is complete separation in miniature. Quasi-complete separation, a direction that sorts the labels with some points sitting on the boundary, produces the same infinite fit. Reported standard errors that explode are a symptom of that geometry.
""",
    "birth-death-balance": r"""
## Flow across one cut

A birth–death chain moves only to a neighbouring count: a birth raises the state by one, a death lowers it by one. The stationary question is whether probability can settle, and the useful balance is not the full generator equation but the flow across a single cut.

Label states $n=0,1,2,\ldots$. Let $\lambda_n\ge 0$ be the birth rate in $n$, and let $\mu_n\ge 0$ be the death rate in $n\ge 1$, with $\mu_0=0$. The only off-diagonal rates are $q_{n,n+1}=\lambda_n$ and $q_{n,n-1}=\mu_n$. In stationarity the upward flux across the cut between $n$ and $n+1$ equals the downward flux,

$$
\pi_n\lambda_n=\pi_{n+1}\mu_{n+1}.
$$

Provided every death rate is positive, iterating from $0$ gives $\pi_n$ as $\pi_0$ times a product of birth rates over the next death rates. On the irreducible chain these weights are a probability distribution precisely when their sum is finite, and that finiteness is positive recurrence. An infinite sum may be null recurrence or a drift to infinity; either way there is no stationary probability.

## Constant rates

Suppose $\lambda_n=\lambda$ and $\mu_n=\mu>0$ for every $n\ge 1$, and set $\rho=\lambda/\mu$. The product collapses to $\pi_n=\pi_0\rho^n$. The geometric series sums if and only if $\rho<1$, in which case $\pi_n=(1-\rho)\rho^n$. Take $\lambda=2$ and $\mu=4$, so $\rho=1/2$. Then $\pi_0=1/2$, $\pi_1=1/4$, $\pi_2=1/8$, and the mean count is $\rho/(1-\rho)=1$. If instead $\rho\ge 1$, the same formal weights sum to infinity and there is no stationary probability. This cut equation is [detailed balance](detailed-balance.qmd) on a path. It is the route into the [M/M/1 queue](m-m-1-queue.qmd) and the [local balance](local-balance.qmd) product.
""",
    "blocking-probability": r"""
## Arrivals that find the room full

A finite waiting room always has a stationary distribution, because the chain cannot run off to infinity. The price is that some arrivals are refused. The blocking probability is the long-run fraction of arrivals who find the room full and do not enter.

Let the state be the number of customers present, including anyone in service, and suppose the room holds at most $K$ customers. An arrival who finds state $K$ is lost. When arrivals are Poisson, an arrival sees the time-average distribution, so the fraction blocked equals the stationary probability $\pi_K$. For the single-server system with offered load $\rho=\lambda/\mu\neq 1$,

$$
\pi_n=\frac{(1-\rho)\rho^n}{1-\rho^{K+1}},\qquad 0\le n\le K,
$$

and the blocking probability is the case $n=K$. At $\rho=1$ every state is equally likely and $\pi_K=1/(K+1)$. The stationary law exists on both sides of $\rho=1$. What changes with $\rho$ is how much traffic is turned away.

## Three loads in a room of size two

Take $K=2$. At $\rho=1/2$ the unnormalised weights are $1$, $1/2$, $1/4$, which sum to $7/4$, so $\pi_2=(1/4)/(7/4)=1/7\approx 0.143$. At $\rho=1$, $\pi_2=1/3$. At $\rho=2$ the weights are $1$, $2$, $4$, which sum to $7$, so $\pi_2=4/7\approx 0.571$. Blocking rises with load. The accepted rate is not the offered rate $\lambda$: [throughput](throughput.qmd) equals $\lambda(1-\pi_K)$, and [Little's law](little-s-law.qmd) has to use that accepted rate. An infinite room with $\rho<1$ has $\pi_K=0$ in the limit of large $K$, which is why blocking disappears from the stable [M/M/1 queue](m-m-1-queue.qmd) and remains the central cost of a finite room.
""",
    "bootstrap-error-and-the-correction": r"""
## Leaving each case out of some of the refits

The apparent error scores a classifier on the cases that trained it and tends to be optimistic. A bootstrap replicate draws $n$ training cases with replacement. About $1-(1-1/n)^n$ of the original cases appear at least once, and that probability tends to $1-e^{-1}\approx 0.632$ (Efron, 1983). The complementary chance of being omitted tends to $0.368$. Let $C_{-i}$ be the replicates that omit case $i$, and let $\eta_b$ be the classifier trained on replicate $b$. The bootstrap error $\widehat{\mathrm{Err}}^{(\mathrm{BOOT})}$ averages the zero–one mismatch $Q$ of $y_i$ against $\eta_b(x_i)$ only over $b\in C_{-i}$, then averages those casewise rates over $i$. Each test case is scored by rules that did not train on it. Because those rules saw only about $0.632n$ distinct cases, they are weaker than the rule trained on all $n$ distinct cases, and the bootstrap error tends to sit above the error of the fully trained rule.

## Pulling the two biases together

The $.632$ estimator mixes the two biases with the limiting weights,

$$
\widehat{\mathrm{Err}}^{(.632)}=0.368\,\mathrm{err}+0.632\,\widehat{\mathrm{Err}}^{(\mathrm{BOOT})}.
$$

If the apparent error is $\mathrm{err}=0.10$ and the bootstrap error is $0.25$, the blend equals $0.368\times 0.10+0.632\times 0.25=0.1948$. The weights are limits, not exact finite-sample inclusion probabilities: at $n=10$ the inclusion probability is about $0.651$ rather than $0.632$. Strong overfitting can leave even the blend optimistic, because the apparent term can be near zero while the bootstrap rules are still unstable. The formula is a correction with those assumptions. It is not an identity for the unknown error of the deployed rule.
""",
    "borel-cantelli-lemmas": r"""
## Will the event keep happening?

Many arguments need to know whether an event that can occur at every trial occurs infinitely often, or only finitely often. The Borel–Cantelli lemmas turn a series of probabilities into that almost-sure statement.

Let $A_1,A_2,\ldots$ be events. The event that infinitely many of them occur is

$$
\{A_n\text{ infinitely often}\}=\bigcap_{m\ge 1}\bigcup_{n\ge m}A_n.
$$

If $\sum_n\mathbb{P}(A_n)<\infty$, the tail sums $\sum_{n\ge m}\mathbb{P}(A_n)$ tend to $0$. The union bound puts the tail union inside that sum, and continuity of probability from above forces $\mathbb{P}(A_n\text{ infinitely often})=0$. Independence is not used. This is the summable half (Cantelli, 1917).

If the events are independent and $\sum_n\mathbb{P}(A_n)=\infty$, the conclusion reverses: the probability is $1$ (Borel, 1909). Independence turns a long run of failures into a product, and $1-x\le e^{-x}$ makes that product collapse whenever the series of probabilities diverges.

## A harmonic series, and a repeated event

Suppose the $A_n$ are independent with $\mathbb{P}(A_n)=1/n^2$. The series converges, so almost every outcome lies in only finitely many of the $A_n$. If instead $\mathbb{P}(A_n)=1/n$ and the events stay independent, the harmonic series diverges and $A_n$ occurs infinitely often with probability $1$. Drop independence and the second conclusion can fail. Repeat one event $A$ of probability $1/2$ at every $n$. The probabilities sum to infinity, yet $\{A_n\text{ infinitely often}\}=A$ still has probability $1/2$. The lemmas are the bridge from summable tail bounds to the [strong law](strong-law.qmd), through [countable additivity](countable-additivity.qmd).
""",
    "box-muller-method": r"""
## Radius and angle

The standard normal distribution function has no elementary inverse, so the usual [inverse-transform method](inverse-transform-method.qmd) is unavailable. A pair of independent standard normals does have a simple description in polar coordinates. If $Z_1$ and $Z_2$ are independent and $\operatorname{N}(0,1)$, the squared radius $R^2=Z_1^2+Z_2^2$ has the chi-squared distribution on $2$ degrees of freedom, which is exponential with mean $2$, and the angle is independent of $R$ and uniform on $(0,2\pi)$. Inverting those two laws produces the Box–Muller map (Box and Muller, 1958).

Draw $U$ and $V$ independent and uniform on $(0,1)$. Set $R=\sqrt{-2\log U}$ and $\Theta=2\pi V$, and return

$$
Z_1=R\cos\Theta,\qquad Z_2=R\sin\Theta.
$$

Then $Z_1$ and $Z_2$ are independent and $\operatorname{N}(0,1)$. A general normal $\operatorname{N}(\mu,\sigma^2)$ draw is $\mu+\sigma Z_1$. The logarithm is natural. The construction uses each uniform once: discarding $Z_2$ wastes a draw, and feeding the same uniform in for both $U$ and $V$ destroys the independence.

## One numerical pair, and a trap at zero

Take $U=1/2$ and $V=1/4$. Then $R=\sqrt{2\log 2}\approx 1.177$ and $\Theta=\pi/2$, so $Z_1=0$ and $Z_2\approx 1.177$. The map needs $U\in(0,1]$. A [linear congruential generator](linear-congruential-generator.qmd) can return the state $0$, and $\log 0$ is undefined. That output has to be rejected or shifted before it is used. The exact normal law also assumes genuinely continuous independent uniforms. A coarse generator leaves $(Z_1,Z_2)$ on a lattice inherited from the uniforms.
""",
    "brier-score": r"""
## A score for the probabilities, not only the labels

Classification error counts a prediction as right or wrong after a threshold such as $1/2$. Two forecasts $0.51$ and $0.99$ can induce the same hard label and very different beliefs. The Brier score charges the squared distance from the forecast probability $\hat p_i$ to the binary outcome $y_i\in\{0,1\}$,

$$
\frac1n\sum_{i=1}^n(\hat p_i-y_i)^2.
$$

It is a proper scoring rule (Brier, 1950). If $Y$ is truly Bernoulli($p$) and the forecast is a constant $\hat p$, then $\mathbb{E}(\hat p-Y)^2=p(1-p)+(p-\hat p)^2$. The first term does not depend on the forecast. The second term is zero only at $\hat p=p$, so the expected score is minimised by reporting the true probability. A rule that is right just over half the time, but systematically overconfident, can lose to a calibrated rule with a similar error rate.

## Three forecasts and a constant baseline

For forecasts $0.9$, $0.2$ and $0.6$ on outcomes $1$, $0$ and $1$, the squared errors are $0.01$, $0.04$ and $0.16$. The Brier score is $0.21/3=0.07$. The constant forecast $1/2$ scores $(1/2-y)^2=1/4$ on every binary outcome. A hard classifier that emits $1$, $0$ and $1$ scores zero on these three outcomes and would look perfect, while hiding that the third case was only a probability $0.6$. The score applies to any source of probabilities, including a logistic fit. It does not by itself say which covariate caused an error, and with a rare class a small Brier score can coexist with weak discrimination if most probabilities sit near the base rate.
""",
    "cauchy-distribution": r"""
## A density with no mean

The standard Cauchy density is $f(x)=1/\{\pi(1+x^2)\}$ for every real $x$. Its distribution function is $F(x)=\tfrac12+\arctan(x)/\pi$, so the quantile function is $F^{-1}(u)=\tan\{\pi(u-\tfrac12)\}$ for $u\in(0,1)$. The tails are heavy enough that the mean does not exist: the integral of $\lvert x\rvert/\{\pi(1+x^2)\}$ over the real line diverges, because the integrand behaves like $1/(\pi\lvert x\rvert)$ at infinity. The [law of large numbers](law-of-large-numbers.qmd) therefore does not apply. Something sharper is true. The average of $n$ independent standard Cauchy variables is again standard Cauchy, for every $n$. Averaging does not concentrate the distribution at all.

The centre is still well defined as a median. $F(0)=1/2$, and $F(1)=3/4$ because $\arctan 1=\pi/4$, so the quartiles are $-1$ and $1$. The interquartile range is $2$, a finite scale, while the variance is not merely large: it is undefined. The same law is the [Student $t$ distribution](student-t-distribution.qmd) on $1$ degree of freedom, and it is the ratio of two independent standard normals.

## Drawing one value

The closed quantile makes simulation immediate. A uniform draw $U=0.9$ gives $\tan(0.4\pi)\approx 3.078$, a single Cauchy observation. The sample median is a consistent estimator of the centre. The sample mean is not, because it has the same distribution as one observation however large the sample. Moments of order $1$ and higher all fail to exist, so a moment generating function in a neighbourhood of $0$ is unavailable as well.
""",
    "characteristic-functions": r"""
## A transform that is always finite

Moment generating functions $\mathbb{E} e^{tX}$ are convenient when they exist, and useless for a Cauchy law, whose exponential moments are infinite. The characteristic function replaces the real exponential by a complex oscillation of modulus one, so the expectation exists for every real random variable and every real frequency $t$.

Define $\varphi_X(t)=\mathbb{E} e^{itX}=\mathbb{E}\cos(tX)+i\mathbb{E}\sin(tX)$. Because $|e^{itX}|=1$, there is no integrability restriction. The map $t\mapsto\varphi_X(t)$ determines the distribution of $X$: different laws have different characteristic functions. If $X$ and $Y$ are independent, the characteristic function of the sum multiplies, $\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t)$. The same formal convenience is what a [moment generating function](moment-generating-function.qmd) gives on the set where it is finite.

## A coin, a normal limit, and a law with no mean

A Bernoulli trial with $\mathbb{P}(X=1)=p$ has $\varphi_X(t)=1-p+pe^{it}$. A standard normal law has $\varphi(t)=e^{-t^2/2}$. For independent copies with mean $0$ and variance $1$, the characteristic function of the standardised sum tends to $e^{-t^2/2}$ at every $t$. [Lévy's continuity theorem](levy-s-continuity-theorem.qmd) promotes that pointwise limit to [convergence in distribution](modes-of-convergence.qmd), and the normal limit of the transform is the [central limit theorem](central-limit-theorem.qmd). A limit of transforms fixes the laws in the limit, and it leaves open whether the means converge. The standard Cauchy law has characteristic function $e^{-|t|}$ and no mean at all, so the transform can exist when moments do not.
""",
    "complementary-log-log-link": r"""
## A probability link that is not symmetric

A binary probability has to stay inside $(0,1)$, but the two tails do not have to approach their limits at the same speed. The complementary log-log link

$$
g(p)=\log\{-\log(1-p)\}
$$

sends $(0,1)$ onto the whole real line and inverts as $p=1-\exp\{-\exp(\eta)\}$, where $\eta$ is the linear predictor. At $\eta=0$ the probability is $1-e^{-1}\approx 0.632$, not $1/2$. The value that does give $p=1/2$ solves $\exp(\eta)=\log 2$, so $\eta=\log(\log 2)\approx -0.37$. Moving $\eta$ from $-1$ to $0$ raises $p$ from about $0.31$ to $0.63$; moving it from $0$ to $1$ raises $p$ from $0.63$ to about $0.93$. The two increments are about $0.32$ and then $0.30$, so the unit step on the right is not the steeper one. The asymmetry sits in the tails: at $\eta=2$ the probability is already about $0.999$, while at $\eta=-2$ it is still about $0.13$, so the approach to $1$ is much faster than the approach to $0$. A [logit link](logit-link.qmd) would have been symmetric about $1/2$, and its coefficient would have been a log odds ratio. The coefficient here is not.

## Any event, or none

The same formula is what a Poisson count becomes when only the occurrence is recorded. If $N$ has mean $\lambda$ and $Y=1$ when $N\ge 1$, then $p=1-e^{-\lambda}$ and $g(p)=\log\lambda$. A binary record of "at least one event", with $\log\lambda=\mathbf{x}^\top\boldsymbol{\beta}$, is a complementary log-log regression, and a unit increase in covariate $j$ multiplies the underlying Poisson mean by $e^{\beta_j}$. The asymmetry is appropriate when the scientific event is a threshold crossing, and it is a misspecification when the two tails really are mirror images. Fitted probabilities of exactly $0$ or $1$ still make $g(p)$ infinite, so a separated sample has the same diverging maximum likelihood that a logit model has.
""",
    "complete-data-likelihood": r"""
## The likelihood one would have if the labels were seen

A finite mixture draws each observation from one of $H$ components. The weight $\pi_h$ is the probability of component $h$, with $\pi_h\ge 0$ and $\sum_h\pi_h=1$, and $f_h(x;\theta_h)$ is that component's density. The parameter $\Psi$ collects every $\pi_h$ and every $\theta_h$. The label of observation $i$ can be written as indicators $z_{ih}\in\{0,1\}$ with exactly one of them equal to $1$. If those labels were observed, together with the sample $X_{\mathrm{all}}=(x_1,\ldots,x_n)$, the complete-data likelihood would multiply $\bigl(\pi_h f_h(x_i;\theta_h)\bigr)^{z_{ih}}$ over cases and components. The complete log-likelihood $\ell_C$ is therefore a sum of terms $z_{ih}\bigl(\log\pi_h+\log f_h(x_i;\theta_h)\bigr)$. With the $z_{ih}$ treated as known, the maximiser separates: the weights are the label frequencies, and each $\theta_h$ is estimated from the cases that carry component $h$.

## One case, written both ways

Take $H=2$, $\pi_1=0.3$, $\pi_2=0.7$, and one observation whose component densities are $f_1(x)=0.4$ and $f_2(x)=0.2$. If the latent label is component $1$, then $z=(1,0)$ and the complete likelihood equals $0.3\times 0.4=0.12$, so $\ell_C=\log 0.12\approx -2.120$. If the label is component $2$, the complete likelihood equals $0.7\times 0.2=0.14$. The observed likelihood does not see the label, so it adds the two routes: $0.12+0.14=0.26$. That sum of products is why the observed log-likelihood has a logarithm of a sum and is harder to maximise. The [E step](e-step.qmd) replaces each unobserved $z_{ih}$ by its conditional probability given $x_i$ and the current $\Psi$. The algebra above is exactly the weighted complete log-likelihood that replacement produces.
""",
    "complete-linkage": r"""
## Merging only when every cross-pair is close

[Hierarchical clustering](hierarchical-clustering.qmd) needs a dissimilarity $d_C(D_1,D_2)$ between two clusters. Complete linkage takes the maximum of $d(x,y)$ over $x\in D_1$ and $y\in D_2$. A proposed merge is therefore judged by its worst cross-pair. The height at which two clusters join is the diameter of the cluster that the merge would create, when diameter means the largest pairwise dissimilarity inside the union. Compact groups of similar diameter are favoured, and a chain of small steps does not qualify: one long link anywhere in the cross-pairs blocks the merge. The criterion uses only the dissimilarities. It does not need means, so it applies to non-Euclidean $d$, including sequence distances.

## Heights on a three-point line

Let the points be $0$, $1$ and $10$, with $d$ the absolute difference. The closest pair is $\{0,1\}$ at height $1$. Complete linkage from that pair to $10$ equals $\max(10,9)=10$. [Single linkage](single-linkage.qmd) would use $\min(10,9)=9$, and [average linkage](average-linkage.qmd) would use $(10+9)/2=9.5$. The complete-linkage dendrogram therefore waits until height $10$ to make the last merge, which is the diameter of $\{0,1,10\}$. An outlier creates the same effect inside a larger sample. One distant point joined early to an otherwise tight group raises every later complete-linkage comparison that group enters. The tendency is real, and it is not a theorem that the clusters must be spherical or of equal size. Those shapes are extra assumptions about the sample, not consequences of taking a maximum.
""",
    "complete-statistic": r"""
## No nonzero unbiased estimator of zero

Unbiasedness alone does not determine an estimator. Many functions of a sample can share one expectation. Completeness is the property that stops a statistic $T$ from carrying a nonzero unbiased estimator of zero. Let the law of $T$ be indexed by $\theta \in \Omega$. The family is complete when every real function $q$, not depending on $\theta$, that satisfies $\mathbb{E}_{\theta}[q(T)] = 0$ for all $\theta \in \Omega$ also satisfies $q(T) = 0$ almost surely for every $\theta$. A single mean-zero random variable at one parameter value is ordinary centring. Completeness says that no such function survives at every parameter value unless it vanishes almost surely.

## Full rank, and a shift model that is not complete

For a full-rank exponential family with an open natural-parameter set, the natural [sufficient statistic](sufficient-statistic.qmd) is complete. An iid Poisson sample is the usual example: the sum is complete and sufficient for the mean. Curved subfamilies need not inherit completeness, and neither do families whose support moves with $\theta$. If $X_1,\ldots,X_n$ are uniform on $(\theta, \theta+1)$, then $T = (X_{(1)}, X_{(n)})$ is minimal sufficient but not complete. The range $R = X_{(n)} - X_{(1)}$ has expectation $(n-1)/(n+1)$ for every $\theta$, because the order statistics of a uniform sample on $(0,1)$ have expectations $1/(n+1)$ and $n/(n+1)$ and a location shift does not change $R$. The function $q(T) = R - (n-1)/(n+1)$ has mean zero and is not almost surely zero. That range is also ancillary and is a function of $T$, which is why [Basu's theorem](basu-s-theorem.qmd) needs completeness before a sufficient statistic is independent of every [ancillary statistic](ancillary-statistic.qmd).
""",
    "conditional-distribution-of-a-multivariate-normal": r"""
## The conditional law stays normal

Split a multivariate normal vector into $X=(X_A,X_B)$ with $X_A$ of dimension $q$, mean blocks $\mu_A$ and $\mu_B$, and covariance blocks $\Sigma_{AA}$, $\Sigma_{AB}$ and $\Sigma_{BB}$. Assume $\Sigma_{BB}$ is nonsingular. The conditional distribution of $X_A$ given $X_B=x_B$ is normal. Its mean is the linear regression $\mu_A+\Sigma_{AB}\Sigma_{BB}^{-1}(x_B-\mu_B)$, and its covariance $\Sigma_{A\mid B}=\Sigma_{AA}-\Sigma_{AB}\Sigma_{BB}^{-1}\Sigma_{AB}^\top$ does not depend on the value $x_B$. The subtracted term is the variability in $X_A$ that is linearly explained by $X_B$. Conditioning therefore cannot increase variance in the positive semi-definite sense: $\Sigma_{AA}-\Sigma_{A\mid B}$ is positive semi-definite. If $\Sigma_{AB}=0$, the conditional mean stays at $\mu_A$ and the conditional covariance stays at $\Sigma_{AA}$, which is the independence case of a joint normal vector.

## A bivariate regression number

Let both means be $0$ and let $\Sigma=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}$, with $A=\{1\}$ and $B=\{2\}$. Then $\Sigma_{AB}\Sigma_{BB}^{-1}=1/2$ and $\Sigma_{A\mid B}=1-(1/2)^2=3/4$. Given $X_2=2$,

$$
X_1\mid X_2=2\sim\operatorname{N}(1,\,3/4).
$$

The conditional mean $1$ is the population regression of $X_1$ on $X_2$ evaluated at $2$, and the conditional variance $3/4$ is the residual variance. The same arithmetic with a singular $\Sigma_{BB}$ needs a generalised inverse and a consistency condition on $x_B$; the displayed formula assumes the inverse exists. Non-normal joints can have linear conditional means and still have conditional distributions that are not normal. The normality of the conditional law is a property of the joint normal family.
""",
    "confusion-matrix": r"""
## Counts arranged by the true class and the predicted class

For a classifier evaluated on a test set, the confusion count $n_{ij}$ is the number of cases whose true class is $i$ and whose predicted class is $j$. Rows are truths and columns are predictions, so the diagonal holds the correct calls. If $n$ is the test size, $\sum_{i\neq j}n_{ij}/n$ estimates the overall error $\mathrm{Err}$ under zero–one loss. Dividing row $g$ by its own total estimates the class-specific error $\mathrm{Err}_g$, the probability of a mistake given that the true class is $g$. Those row proportions are the complements of [sensitivity and specificity](sensitivity-and-specificity.qmd) once a class has been named as the event of interest. The reverse question, the probability that the true class is $g$ given that the classifier said $g$, divides the diagonal entry by the column total. That predictive value moves when the class prevalences move, even if every row proportion stays fixed.

## Fifty test cases, two classes

Suppose $30$ cases truly belong to class $1$ and $20$ to class $2$, and the count matrix is

$$
\begin{pmatrix}27&3\\5&15\end{pmatrix}.
$$

Eight cases lie off the diagonal, so the estimated error is $8/50=0.16$. The class-specific estimates are $3/30=0.10$ and $5/20=0.25$. Taking class $1$ as the event of interest, the sensitivity is $27/30=0.90$ and the specificity is $15/20=0.75$. Class $2$ was predicted $18$ times and was correct $15$ times, so the predictive value of a class-$2$ call on this test set is $15/18=5/6$.
""",
    "convolution": r"""
## The density of an independent sum

Adding random variables mixes every way of splitting the total. Let $X$ and $Y$ be independent, with densities $f_X$ and $f_Y$. Independence puts the product $f_X(x)f_Y(y)$ in the joint density. The event $\{X+Y\le z\}$ is a half-plane in that joint law, and differentiating the resulting distribution function produces

$$
f_{X+Y}(z)=\int_{-\infty}^{\infty} f_X(x)\,f_Y(z-x)\,\mathrm{d} x.
$$

The integrand is zero wherever the split is impossible for the supports of $X$ and $Y$. For non-negative variables the integral runs only from $0$ to $z$. If the variables are discrete, the same reasoning replaces the integral by a sum over the possible values of $X$. Dependence breaks the formula, because the joint density is then no longer the product of the marginals. Positive dependence usually makes the sum more variable than the independent convolution predicts.

The moment generating function turns the integral into multiplication. For independent $X$ and $Y$, $\mathbb{E} e^{s(X+Y)}=\mathbb{E} e^{sX}\,\mathbb{E} e^{sY}$ wherever both factors exist. Recognising a product of transforms is often easier than evaluating the integral.

## Two exponential waits

Let $X$ and $Y$ be independent, each exponential with rate $1$, so each density is $e^{-x}$ on $(0,\infty)$. For $z>0$,

$$
f_{X+Y}(z)=\int_0^z e^{-x}e^{-(z-x)}\,\mathrm{d} x=ze^{-z}.
$$

That is the [gamma density](gamma-distribution.qmd) with shape $2$ and rate $1$. The pattern continues: a sum of $k$ independent rate-$1$ exponentials is gamma with shape $k$ and rate $1$. Shared rate is essential. Different rates still give a convolution, but the integral is a sum of distinct exponentials rather than a single gamma density.
""",
    "correlation": r"""
## Covariance with the units removed

The covariance $\sigma_{jk}=\operatorname{Cov}(X_j,X_k)$ still carries the units of $X_j$ and of $X_k$. If those variables have positive finite variances $\sigma_j^2$ and $\sigma_k^2$, the Pearson correlation divides by both standard deviations,

$$
\rho_{jk}=\frac{\sigma_{jk}}{\sigma_j\sigma_k}\in[-1,1].
$$

The diagonal is $1$ because a variable agrees perfectly with itself. In matrix form, if $D=\operatorname{diag}(\sigma_1,\ldots,\sigma_p)$ and $\Sigma=(\sigma_{jk})$, then the correlation matrix is $P=D^{-1}\Sigma D^{-1}$, and $\Sigma=DPD$ puts the units back. Multiplying $X_j$ by a positive constant leaves every correlation unchanged and flips the sign of every off-diagonal correlation involving $X_j$ if the constant is negative, while the diagonal entry stays $1$. The bound $|\rho_{jk}|=1$ means that one variable is an affine function of the other, with a positive slope when $\rho_{jk}=1$.

## A covariance matrix and its correlation matrix

Suppose $\operatorname{Var}(X_1)=4$, $\operatorname{Var}(X_2)=9$ and $\operatorname{Cov}(X_1,X_2)=3$. Then $\rho_{12}=3/(2\times 3)=1/2$, and

$$
\Sigma=\begin{pmatrix}4&3\\3&9\end{pmatrix},
\qquad
P=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}.
$$

The number $1/2$ does not say that the relationship is causal, and it does not say that the conditional mean is linear except as a description of the best linear predictor. For a joint normal pair, $\rho_{12}=0$ is equivalent to independence. For other joints, uncorrelated coordinates can still be dependent: a standard construction with a finite third moment puts mass so that $X_2=X_1^2$ with $X_1$ symmetric about zero, forcing the covariance to vanish while $X_2$ remains a function of $X_1$. Sample correlations estimated from a few points can sit near $\pm 1$ by chance, which is a statement about variability of the estimator rather than about the population formula.
""",
    "countable-additivity": r"""
## Adding a countable list of disjoint events

Finite additivity says how to combine two disjoint events. Limits need a countable list. Continuity of probability along monotone sequences, the Borel–Cantelli lemmas, and the construction of infinite product measures all use that stronger axiom.

A probability $\mathbb{P}$ on a sigma-algebra $\mathcal{F}$ is countably additive when, for pairwise disjoint events $A_n\in\mathcal{F}$,

$$
\mathbb{P}\Bigl(\bigcup_{n=1}^{\infty} A_n\Bigr)=\sum_{n=1}^{\infty}\mathbb{P}(A_n).
$$

If $B_m\uparrow B$, the increments $B_1$, $B_2\setminus B_1$, $B_3\setminus B_2,\ldots$ are disjoint and their union is $B$, so $\mathbb{P}(B_m)\uparrow\mathbb{P}(B)$. If $C_m\downarrow C$, the complements increase and $\mathbb{P}(C_m)\downarrow\mathbb{P}(C)$. Kolmogorov took countable additivity as an axiom of probability (Kolmogorov, 1933).

## A tail that must shrink

Let $\Omega=\{1,2,\ldots\}$ and put mass $\mathbb{P}(\{n\})=2^{-n}$. The masses sum to $1$. The tail event $\{n,n+1,\ldots\}$ has probability $2^{-n+1}$, which decreases to $0$. That is continuity from above applied to a sequence of events falling to the empty set. Finite additivity does not force the same conclusion: a set function can vanish on every singleton and still give the whole of $\Omega$ mass $1$, provided it is not required to add up a countably infinite disjoint union. Such set functions are not probabilities in Kolmogorov's sense. Countable additivity is what makes the [Borel–Cantelli lemmas](borel-cantelli-lemmas.qmd) and the definition of a [probability measure](probability-measure.qmd) close under sequential limits.
""",
    "cover-hart-bound": r"""
## One neighbour samples the conditional label

For two classes, let $\tau(x)=\mathbb{P}(Y=1\mid X=x)$ and let $r(x)=\min\bigl(\tau(x),1-\tau(x)\bigr)$ be the conditional [Bayes risk](bayes-classifier.qmd) at $x$. The unconditional Bayes risk is $R^*=\mathbb{E}[r(X)]$. As the training sample grows, the nearest neighbour of a continuity point $x$ approaches $x$, so its label is almost a fresh draw from the same conditional distribution that produces a new label at $x$. The two labels disagree with probability $2\tau(1-\tau)$. The identity $\tau(1-\tau)=r(1-r)$ rewrites that probability as $2r(x)\bigl(1-r(x)\bigr)$. Averaging over $X$ gives the asymptotic one-nearest-neighbour error. Because $1-r(x)\le 1$, this error is at most $2R^*$. [Jensen's inequality](jensen-s-inequality.qmd), using the concavity of $u\mapsto u(1-u)$ on $[0,1]$, sharpens the constant: $\mathbb{E}[r(1-r)]\le R^*(1-R^*)$, and therefore the asymptotic error is at most $2R^*(1-R^*)$ (Cover and Hart, 1967).

## Equality when the conditional risk is constant

If $r(x)=0.2$ for almost every $x$, then $R^*=0.2$ and the nearest-neighbour conditional error is $2\times 0.2\times 0.8=0.32$ everywhere. The Cover–Hart upper bound is $2\times 0.2\times 0.8=0.32$, so the bound is tight for a constant conditional risk. The coarser bound $2R^*=0.4$ leaves a gap. If instead $R^*=0.1$ but $r(X)$ varies, Jensen still caps the asymptotic error by $2\times 0.1\times 0.9=0.18$, which is less than $2R^*=0.2$. The argument is asymptotic and uses two classes, a neighbour that converges to the query, and the zero–one loss. In high dimension, or in a small sample, the nearest training point need not be close, and the finite-sample error can exceed $2R^*(1-R^*)$. Growing $k$ can improve on the one-neighbour limit; the bound here is specifically about $k=1$.
""",
    "cubic-smoothing-spline": r"""
## A curve charged for bending

A scatter asks for a curve that follows the signal and not the jitter. One statement of that request is to maximise the log-likelihood of the responses and subtract a penalty $\lambda\int\{g''(x)\}^2\,\mathrm{d}x$. The integral is zero for every straight line, because a line has second derivative $0$, and it grows as the curve bends. The multiplier $\lambda\ge 0$ is the price of bending. For any fixed $\lambda>0$ the maximiser is a natural cubic [spline](spline.qmd), linear beyond the outermost knots with second derivative zero at those knots. Between consecutive distinct covariate values the fitted function is a cubic polynomial, and at each of those [knots](knot.qmd) the value, the first derivative and the second derivative agree from the left and the right. A jump is allowed only in the third derivative, which the plot does not show.

## The line at one extreme, the interpolant at the other

The points $(0,0)$, $(1,1)$ and $(2,0)$ have least-squares line equal to the constant $1/3$. Once the covariate is centred it is uncorrelated with the response, and the residual sum of squares about $1/3$ is $2/3$. That constant is the fitted curve as $\lambda\to\infty$. As $\lambda\to 0$, with the $x$ values distinct, the curve interpolates, so the fitted height at $x=1$ is $1$ rather than $1/3$. A moderate penalty places that height between the two. The number $\lambda$ itself travels badly: a different likelihood changes the units of the penalty, so two samples can share a $\lambda$ and not share a smoothness. The summary that does travel is the equivalent degrees of freedom of the fitted curve. The interpolating end fits noise as well as signal.
""",
    "cycle": r"""
## A repeated swing with no fixed clock

A series can rise and fall without repeating on a schedule that was known in advance. Business activity, epidemics and animal numbers often do this: a peak, a trough, and another peak several years later, with the gap changing from one swing to the next. That irregular swing is a cycle. It is not [seasonality](seasonality.qmd). Seasonality is a cycle whose period is fixed by the calendar, such as $12$ months or $7$ days, so the same lag is the right lag every time. A cycle of varying length has no such lag. A seasonal difference, or a seasonal autoregression at lag $12$, removes the calendar pattern and leaves the irregular cycle in the residuals. The forecast then keeps painting a year that was never the structure of the swing.

## Two cosines, and only one of them seasonal

Let $X_t=\cos(2\pi t/12)+\cos(2\pi t/8)$, read as a monthly index. The first term repeats every $12$ observations. The seasonal difference $\nabla_{12}X_t=X_t-X_{t-12}$ kills it, because $\cos(2\pi(t-12)/12)$ equals $\cos(2\pi t/12)$. The second term survives. A shift of $12$ months is $1.5$ cycles of length $8$, which multiplies that cosine by $-1$, and

$$
\cos(2\pi t/8)-\cos(2\pi(t-12)/8)=2\cos(2\pi t/8).
$$

The period-$8$ piece is still present, and the difference has doubled it. A purely seasonal model has no parameter for a rhythm whose length is free to change. The time plot, not the seasonal lag alone, is what shows the second swing.
""",
    "degrees-of-freedom": r"""
## How many free squares remain

Degrees of freedom count independent standard normal squares, and they count how many directions remain after a fit. If $Z_1,\ldots,Z_m$ are independent and $\operatorname{N}(0,1)$, then $V=Z_1^2+\cdots+Z_m^2$ has the [chi-squared distribution](chi-squared-distribution.qmd) with $m$ degrees of freedom. The mean is $m$ and the variance is $2m$. A [Student $t$](student-t-distribution.qmd) variable on $m$ degrees of freedom is an independent standard normal divided by $\sqrt{V/m}$. An $F$ variable on $(m_1,m_2)$ degrees of freedom is a ratio of two independent chi-squared variables, each divided by its own degrees of freedom.

Estimation spends some of those squares. For a normal sample of size $n$, the residuals $X_i-\overline X$ sum to zero. That one linear constraint removes one dimension, so $(n-1)s^2/\sigma^2$ is chi-squared on $n-1$ degrees of freedom rather than on $n$. A linear fit with $p$ coefficients, when the design has full rank, imposes $p$ independent constraints and leaves $n-p$ degrees of freedom in the residual sum of squares. In an $r\times c$ table the fitted independence model matches the row and column margins, and $(r-1)(c-1)$ free cells remain.

## Two normal observations

Take $n=2$. The residuals are $(X_1-X_2)/2$ and its negative, so only one number is free. The unbiased sample variance is $s^2=(X_1-X_2)^2/2$, and $(X_1-X_2)^2/(2\sigma^2)$ is chi-squared on $1$ degree of freedom when the two observations are independent and $\operatorname{N}(\mu,\sigma^2)$. Using $n$ instead of $n-1$ in the divisor biases $s^2$. Using the wrong degrees of freedom in a $t$ or $F$ critical value assigns the wrong coverage. Dependence does not always act the same way: with equal pairwise correlation $\rho$, the expected sum of squared deviations from the mean is $(n-1)\sigma^2(1-\rho)$, so $n-1$ overstates that expectation when the observations move together and understates it when they move in opposition.
""",
    "descent-of-lloyd-s-algorithm": r"""
## Each alternation is a minimisation of its own

Lloyd's algorithm minimises the within-cluster sum of squares

$$
\widetilde W(C,m_1,\ldots,m_K)=\sum_{i=1}^n\lVert x_i-m_{C(i)}\rVert^2
$$

over a labelling $C$ and centres $m_1,\ldots,m_K$. With the centres held fixed, assigning every point to a nearest centre cannot raise $\widetilde W$, because each summand is replaced by a value no larger. With the labels held fixed, replacing $m_k$ by the mean of the points labelled $k$ cannot raise $\widetilde W$ either: the squared Euclidean distance from a set of points to a centre is minimised at their mean, provided the cluster is nonempty. With a deterministic tie rule only finitely many labellings exist, so the descent stops at a fixed point of the two steps.

## A fixed point whose value is far from the best partition

Take the corners $(0,0)$, $(0,1)$, $(10,0)$ and $(10,1)$, and start with centres $(0,0)$ and $(0,1)$. The assignment puts the two bottom corners with $(0,0)$ and the two top corners with $(0,1)$, and $\widetilde W=200$. The means become $(5,0)$ and $(5,1)$, the assignment does not change, and $\widetilde W=100$. Each point is closer to its own centre than to the other, at distance $5$ against $\sqrt{26}\approx 5.10$, so Lloyd stops. The vertical partition, with centres $(0,1/2)$ and $(10,1/2)$, has $\widetilde W=1$. The stopped value $100$ is minimal for each step separately and far from the global minimum. Several random starts, keeping the smallest $\widetilde W$, are a practical response to that gap.
""",
    "detailed-balance": r"""
## Matching the flow on every edge

Global balance asks only that the total probability flowing into a state equal the probability sitting there. Detailed balance asks for something stronger, and often easier to check: across every ordered pair of states, the flow in one direction equals the flow back.

Let $\pi$ be a probability row vector and let $P=(p_{ij})$ be a transition matrix. Detailed balance holds when

$$
\pi_i p_{ij}=\pi_j p_{ji}\qquad\text{for all states }i,j.
$$

Summing over $i$ recovers $\pi_j=\sum_i\pi_i p_{ij}$, so detailed balance implies the stationary equation $\pi P=\pi$. If every $\pi_i$ is positive, the time-reversed transitions are $p_{ij}^{*}=\pi_j p_{ji}/\pi_i$, and detailed balance says $P^{*}=P$. A stationary path then has the same law read backwards as forwards. Stationarity alone does not give that symmetry.

## Two states, and a cycle with circulation

On two states, let $p_{01}=a$ and $p_{10}=b$ with $0<a,b\le 1$. Then $\pi_0=b/(a+b)$ and $\pi_1=a/(a+b)$, and both directed flows equal $ab/(a+b)$. Every two-state chain satisfies detailed balance. A deterministic cycle $1\to 2\to 3\to 1$ does not. The uniform vector $(1/3,1/3,1/3)$ is stationary, because the matrix is a permutation, but every reverse edge has probability $0$, so the pairwise products cannot match. Probability circulates. On a finite irreducible chain, an equivalent test that does not require $\pi$ in advance is Kolmogorov's cycle criterion (Kolmogorov, 1936): around every directed cycle the product of the transition probabilities equals the product around the reversed cycle. See [global balance](global-balance-and-detailed-balance.qmd).
""",
    "detailed-balance-implies-stationarity": r"""
## Pairwise flow implies the global equation

A transition is usable for simulation only if it leaves the target distribution unchanged. Let a [Markov chain](markov-chain.qmd) have transition density $q(y \mid x)$, the density of the next state when the current state is $x$; on a discrete space the same symbol is a transition probability and integrals below are sums. A probability density $\pi$ is a [stationary distribution](stationary-distribution.qmd) when one step preserves it. That requirement is global balance,

$$
\pi(y) = \int \pi(x)\, q(y \mid x) \,\mathrm{d}x.
$$

[Detailed balance](detailed-balance.qmd) is the stronger pairwise statement $\pi(x)\, q(y \mid x) = \pi(y)\, q(x \mid y)$ for every pair of states. The flow from $x$ to $y$ equals the flow from $y$ to $x$ when the chain is started from $\pi$. Integrate both sides in $x$. The left side becomes the integral in the global equation. The right side factors as $\pi(y)$ times $\int q(x \mid y) \,\mathrm{d}x$, and that integral equals one because $q(\cdot \mid y)$ is a transition density. Therefore any $\pi$ in detailed balance with $q$ satisfies global balance and is stationary.

## What the implication does not give

A chain can be stationary without detailed balance. Stationarity is also not convergence: if the state is already drawn from $\pi$, the next state is too, but an arbitrary start need not approach $\pi$. Irreducibility and aperiodicity, or a continuous-state substitute that makes the chain ergodic, are further conditions on the transition that was actually coded.
""",
    "deviance-residual": r"""
## Misfit on the likelihood's own scale

A raw residual $y_i-\hat\mu_i$ treats an error of $3$ as the same event at every mean. For a count, $3$ against a mean of $2$ is not $3$ against a mean of $50$. The deviance residual rescales each observation by its own contribution to the [deviance](deviance.qmd). If $d_i$ is that contribution,

$$
r_{D,i}=\operatorname{sign}(y_i-\hat\mu_i)\sqrt{d_i},
$$

and the sum of $r_{D,i}^2$ equals the deviance. The sign is the sign of $y_i-\hat\mu_i$, so a point above the fit is not collapsed with a point below it. For a Poisson observation, $d_i=2\{y_i\log(y_i/\hat\mu_i)-(y_i-\hat\mu_i)\}$, with the convention that $0\log 0=0$. The residual is large when the observation is unlikely under the fitted mean, which is the scale the likelihood itself uses.

## A zero is harsher here than in the Pearson residual

Take $y=8$ and $\hat\mu=5$. Then $d=2\{8\log(1.6)-3\}\approx 1.52$ and $r_D\approx 1.23$. The Pearson residual $(8-5)/\sqrt{5}\approx 1.34$ is close to it. Now take $y=0$ and $\hat\mu=2$. The deviance contribution is $2\hat\mu=4$, so $r_D=-2$, while the Pearson residual is $(0-2)/\sqrt{2}\approx -1.41$. A Poisson mean of $2$ dislikes a complete miss by more than the Pearson scaling suggests. A plot of $r_D$ against $\hat\mu$ still fans out when the variance function is wrong, and one huge residual is a point to inspect rather than an automatic deletion.
""",
    "discrete-time-markov-chain": r"""
## The next state depends only on the present

A chain is a model for a system that moves on a discrete clock and keeps no extra memory. The future may be dependent on the past, but only through the state occupied now.

Let $S$ be a finite or countable state space and let $X_0,X_1,\ldots$ be $S$-valued random variables. The process is a time-homogeneous discrete-time Markov chain when, for every $n$ and every choice of states,

$$
\mathbb{P}(X_{n+1}=j\mid X_n=i,X_{n-1},\ldots,X_0)=p_{ij}.
$$

The transition matrix $P=(p_{ij})$ has $p_{ij}\ge 0$ and $\sum_j p_{ij}=1$. The Markov property does not say that successive states are independent. They are dependent when different rows of $P$ differ and the current state puts positive probability on two such rows. If the initial law is a row vector $\mu$, the law of $X_n$ is $\mu P^n$. The Chapman–Kolmogorov equations say that $P^{m+n}=P^m P^n$: an $m$-step move followed by an $n$-step move is an $(m+n)$-step move.

## Two-step weather

Take states dry and wet, with $p_{\mathrm{dd}}=0.8$, $p_{\mathrm{dw}}=0.2$, $p_{\mathrm{wd}}=0.4$, and $p_{\mathrm{ww}}=0.6$. Starting from dry, the chance of being dry two days later is $0.8\times 0.8+0.2\times 0.4=0.72$. The same number is the dry-to-dry entry of $P^2$. A stationary distribution solves $\pi P=\pi$. For this weather chain, $\pi_{\mathrm{d}}=2/3$ and $\pi_{\mathrm{w}}=1/3$: the chain spends twice as much time dry as wet. The definition is the discrete-time case of the [Markov property](markov-property.qmd) on a [state space](state-space.qmd), recorded by a [transition matrix](transition-matrix.qmd).
""",
    "drift-and-scale-of-a-random-walk": r"""
## Linear trend, square-root scatter

A random walk adds a fresh increment at every step. The position after many steps has a mean that grows like the number of steps and a spread that grows only like the square root. Those two scales answer different questions, and neither is a statement about the first time a barrier is hit.

Let $Y_1,Y_2,\ldots$ be independent and identically distributed increments, and set $S_n=x+\sum_{i=1}^{n} Y_i$, with $S_0=x$. If $\mu=\mathbb{E} Y_1$ and $\sigma^2=\operatorname{Var}(Y_1)$ are finite, linearity gives $\mathbb{E} S_n=x+n\mu$ and $\operatorname{Var}(S_n)=n\sigma^2$. The [strong law](strong-law.qmd) adds a pathwise reading: $(S_n-x)/n\to\mu$ almost surely whenever the mean exists. When $0<\sigma^2<\infty$, the [central limit theorem](central-limit-theorem.qmd) scales the error by $\sqrt{n}$,

$$
\frac{S_n-x-n\mu}{\sigma\sqrt{n}}\;\xrightarrow{d}\;\operatorname{N}(0,1).
$$

Drift accumulates like $n$. Typical fluctuations are of order $\sqrt{n}$. A [first-passage time](first-passage-time.qmd) depends on the whole path up to the hitting time, not on the single variable $S_n$.

## A biased step of size one

Let $Y_i=+1$ with probability $0.6$ and $Y_i=-1$ with probability $0.4$. Then $\mu=0.2$ and $\mathbb{E} Y_1^2=1$, so $\sigma^2=1-0.04=0.96$. After $n=100$ steps the mean position is $x+20$ and the standard deviation is $\sqrt{96}\approx 9.8$. The walk is typically near $x+20$, about two standard deviations above the starting point. For the symmetric case $\mu=0$, $\sigma^2=1$, the same $100$ steps have mean $x$ and standard deviation $10$. Being above $x+20$ at step $100$ is then a normal tail beyond $2$, about $0.023$, while the chance of having touched $x+20$ at some earlier time is larger, because passage looks at the path.
""",
    "e-step": r"""
## Replacing the latent indicators by conditional probabilities

The complete log-likelihood of a mixture is linear in the unobserved indicators $Z_{ih}$, which equal $1$ when observation $i$ comes from component $h$. Given the observed sample and a current parameter $\Psi^{(k)}$, the conditional expectation of that complete log-likelihood is the function $Q(\Psi;\Psi^{(k)})$. Linearity lets the expectation pass inside the sum, and the expectation of a binary indicator is the probability that it equals one. By Bayes' rule that probability is the posterior membership $\tau_h(x_i;\Psi^{(k)})$, computed from the current weights $\pi_h^{(k)}$ and the current component densities $f_h(x_i;\theta_h^{(k)})$. The free parameter $\Psi=(\pi,\theta)$ remains only in $\log\pi_h+\log f_h(x_i;\theta_h)$. The current value $\Psi^{(k)}$ is held fixed inside $\tau_h$. Updating the memberships with the same $\Psi$ that is being varied would be a different algorithm.

## Responsibilities for a point at the origin

Let $H=2$, with equal weights $1/2$, component means $0$ and $3$, and unit variances. At $x=0$ the normal densities are about $\varphi(0)=0.399$ and $\varphi(3)=0.00443$, where $\varphi$ is the standard normal density. The memberships are

$$
\tau_1(0)\approx\frac{0.399}{0.399+0.00443}\approx 0.989,
\qquad
\tau_2(0)\approx 0.011.
$$

A hard label would discard the second component. The E step keeps a fractional count $0.011$, which still contributes to the expected complete log-likelihood. Those fractions are the input to the [M step](m-step.qmd). They are recomputed only after that step has produced a new $\Psi$. If a component density underflows to zero for every observation, its memberships vanish and the following weight update can hit the boundary $\pi_h=0$.
""",
    "effective-degrees-of-freedom": r"""
## Trace of the smoother matrix

In an unpenalised linear fit $\hat{\mathbf{y}}=X(X^\top X)^{-1}X^\top\mathbf{y}$, the hat matrix $H=X(X^\top X)^{-1}X^\top$ projects onto a $p$-dimensional subspace, so $\operatorname{tr}(H)=p$. A penalised spline or ridge smoother replaces $H$ by a linear smoother matrix $S_\lambda=B(B^\top B+\lambda\Omega)^{-1}B^\top$, where $B$ is the $n\times K$ basis matrix, $\Omega$ is a symmetric positive semi-definite roughness matrix, and $\lambda\ge 0$ is the smoothing parameter (Hastie and Tibshirani, 1990). The fitted vector is still linear in $\mathbf{y}$, $\hat{\mathbf{y}}=S_\lambda\mathbf{y}$, and the effective degrees of freedom of the fit are defined as

$$
\mathrm{edf}(\lambda)=\operatorname{tr}(S_\lambda).
$$

If $\Omega$ penalises the integrated squared second derivative of a cubic spline, two directions (constant and linear) lie in the null space of $\Omega$. When $B$ has full column rank so that $B^\top B$ is positive definite, write $d_1,\ldots,d_K\ge 0$ for the generalised eigenvalues of $\Omega$ relative to $B^\top B$. Then $\mathrm{edf}(\lambda)=\sum_{k=1}^K 1/(1+\lambda d_k)$, which decreases smoothly and strictly (once at least one $d_k>0$) from $K$ at $\lambda=0$ down to $2$ (intercept plus one slope, or $1$ for the centred smooth term alone) as $\lambda\to\infty$.

## Basis dimension versus fitted flexibility

Choosing $K=10$ basis functions sets only the ceiling on $\mathrm{edf}(\lambda)$, not the complexity of the fitted curve. Suppose $K=4$ with two unpenalised linear directions ($d_1=d_2=0$) and two curved directions with $d_3=1$ and $d_4=9$. At $\lambda=1$ the trace is $1+1+1/2+1/10=2.6$, so the centred smooth uses $1.6$ effective degrees of freedom rather than $3$. Unlike $\lambda$, whose numerical scale shifts whenever the predictor is rescaled or the likelihood dispersion changes, $\mathrm{edf}(\lambda)$ stays on a parameter-count scale that can be compared directly across terms and models.
""",
    "em-algorithm": r"""
## The observed likelihood, written as an expectation

The EM algorithm maximises an observed-data log-likelihood $\ell(\Psi)$ by repeatedly maximising an easier complete-data criterion. Latent variables $Z$, here the component labels of a mixture, are included so that the complete log-likelihood $\ell_C(\Psi)$ would be straightforward if $Z$ were known. At the current parameter $\Psi^{(k)}$ the E step computes

$$
Q(\Psi;\Psi^{(k)})=\mathbb{E}\bigl[\ell_C(\Psi)\mid X_{\mathrm{all}},\Psi^{(k)}\bigr],
$$

the expectation of $\ell_C$ under the conditional law of $Z$ given the observations. For a Gaussian mixture that conditional law is the list of responsibilities $\tau_h(\mathbf{x}_i;\Psi^{(k)})$. The M step maximises $Q$ in $\Psi$, with those responsibilities held fixed, and the maximiser becomes $\Psi^{(k+1)}$. An exact M step does not decrease $\ell$ (Dempster, Laird, and Rubin, 1977). Updating the responsibilities inside the M-step derivatives would differentiate a different function.

## A weighted M step on three points

Take responsibilities $0.9$, $0.2$ and $0.5$ for component $1$ on the points $0$, $1$ and $3$. The complementary responsibilities are $0.1$, $0.8$ and $0.5$. The effective counts are $n_1=1.6$ and $n_2=1.4$, so the M step sets $\hat\pi_1=1.6/3\approx 0.533$ and the weighted means $\hat\mu_1=1.0625$, $\hat\mu_2\approx 1.643$. A component variance is the matching weighted mean of squared deviations. The next E step inserts $(\hat\pi,\hat\mu)$ back into the responsibility formula. The path of $\ell$ is monotone when each M step is exact, and the limit can still be a local maximum or a component whose covariance has collapsed onto a few points. Several random starts, and a discard of any run whose component covariance becomes singular, are part of using the algorithm on a mixture.
""",
    "em-for-a-normal-mixture": r"""
## Alternating soft counts with weighted normal fits

A normal mixture has weights $\pi_h$, means $\mu_h$ and covariances $\Sigma_h$, collected in $\Psi$. The observed log-likelihood $\ell(\Psi;X_{\mathrm{all}})$ contains a logarithm of a sum over components, so a direct score equation couples every parameter. EM replaces that problem by two closed updates (Dempster, Laird and Rubin, 1977). The [E step](e-step.qmd) computes memberships $\tau_{ih}=\tau_h(x_i;\Psi^{(k)})$. The [M step](m-step.qmd) then maximises the expected complete log-likelihood with those memberships frozen. Writing $N_h=\sum_i\tau_{ih}$, the updates are $\pi_h=N_h/n$, the weighted mean $\mu_h=\sum_i\tau_{ih}x_i/N_h$, and the weighted covariance that divides $\sum_i\tau_{ih}(x_i-\mu_h)(x_i-\mu_h)^\top$ by $N_h$ rather than by $N_h-1$. An exact step cannot decrease $\ell$. The iteration stops when the rise in $\ell$ falls below a tolerance. A stationary point of a mixture likelihood need not be the global maximum.

## One update from a poor start

Take observations $0$ and $4$, with $\pi=(1/2,1/2)$, means $(1,2)$ and unit variances. The memberships are about $(0.818,0.182)$ at $0$ and $(0.076,0.924)$ at $4$. The effective sizes are $N_1\approx 0.893$ and $N_2\approx 1.107$, so the new weights are about $0.447$ and $0.553$. The new means are about $0.340$ and $3.341$, pulled from $(1,2)$ towards the observations that claim each component. The new variances, using the updated means in the numerator and $N_h$ in the denominator, are about $1.243$ and $2.203$. A component that collapses onto a single point sends a normal density to infinity, so a rising likelihood is not by itself evidence of a useful fit. Several starts, and a check that every $\Sigma_h$ stays well conditioned, belong with the reported parameter.
""",
    "error-and-residual": r"""
## The disturbance still contains the coefficients

A linear model separates the random mechanism from the numbers a fit produces. With a known predictor row $\boldsymbol{x}_i \in \mathbb{R}^{p}$ and an unknown coefficient vector $\boldsymbol{\beta}$, write $Y_i = \boldsymbol{x}_i^{\mathsf{T}}\boldsymbol{\beta} + \varepsilon_i$. If the errors are independent and $\varepsilon_i \sim \operatorname{N}(0, \sigma^2)$, the conditional mean of $Y_i$ is $\boldsymbol{x}_i^{\mathsf{T}}\boldsymbol{\beta}$ and the conditional variance is $\sigma^2$. The error $\varepsilon_i = Y_i - \boldsymbol{x}_i^{\mathsf{T}}\boldsymbol{\beta}$ still contains the unknown $\boldsymbol{\beta}$, so it is not a column in the observed table. For a free candidate $\boldsymbol{b}$, the sum of squares $\sum_i (y_i - \boldsymbol{x}_i^{\mathsf{T}}\boldsymbol{b})^2$ is a function of that candidate. It becomes a property of a fitted model only when $\boldsymbol{b}$ is set equal to a particular estimator.

## Fitting mixes the errors together

[Ordinary least squares](ordinary-least-squares.qmd), for an $n \times p$ design matrix $\boldsymbol{X}$ of rank $p$, uses $\widehat{\boldsymbol{\beta}} = (\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{-1}\boldsymbol{X}^{\mathsf{T}}\boldsymbol{y}$. The residual $e_i = y_i - \boldsymbol{x}_i^{\mathsf{T}}\widehat{\boldsymbol{\beta}}$ is then computable. In matrix form $\boldsymbol{e} = (\boldsymbol{I} - \boldsymbol{H})\boldsymbol{y}$ with $\boldsymbol{H} = \boldsymbol{X}(\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{-1}\boldsymbol{X}^{\mathsf{T}}$. Because $(\boldsymbol{I} - \boldsymbol{H})\boldsymbol{X} = \boldsymbol{0}$, one also has $\boldsymbol{e} = (\boldsymbol{I} - \boldsymbol{H})\boldsymbol{\varepsilon}$. Each residual is a linear mixture of every error. The residual covariance is $\sigma^2(\boldsymbol{I} - \boldsymbol{H})$, not $\sigma^2\boldsymbol{I}$: residuals are correlated, and the variance of $e_i$ is $\sigma^2(1 - h_{ii})$. If an intercept column is present, the residuals sum to zero. A reported sum of squared errors from a fitted regression is therefore a sum of squared residuals, and those residuals are not a fresh iid normal sample.
""",
    "exchangeable-correlation": r"""
## One correlation for every pair in the cluster

Repeated visits on one child, or successive counts from one factory, are not independent. The simplest working correlation gives every pair inside the cluster the same value $\rho$. For a cluster of size $K$ the matrix is $R(\rho)=(1-\rho)I_K+\rho\mathbf{1}\mathbf{1}^\top$, where $I_K$ is the identity and $\mathbf{1}$ is a column of ones. The diagonal is $1$ and every off-diagonal entry is $\rho$. This is the exchangeable [working correlation](working-correlation.qmd) in generalised estimating equations (Liang and Zeger, 1986). It is a working matrix. The estimating equations for the mean can remain consistent when $R$ is wrong, provided the mean is right and the clusters are independent, with a sandwich variance carrying the misspecification.

## A value four visits cannot have

The eigenvalues are $1-\rho$, repeated $K-1$ times, and $1+(K-1)\rho$ once. Both are non-negative only for $-1/(K-1)\le\rho\le 1$. For four visits the lower bound is $-1/3$. A proposed value $\rho=-1/2$ has eigenvalues $1-(-1/2)=1.5$ and $1+3(-1/2)=-0.5$. The negative eigenvalue means that no random vector has this correlation matrix: four measurements cannot all correlate at $-1/2$. At $\rho=-1/3$ the matrix is singular, and at $\rho=1$ it is singular again because the four visits are identical. Ages $8$, $10$, $12$ and $14$ show a scientific limit as well. Adjacent ages are usually more alike than ages six years apart, so one common $\rho$ is a convenient working value, not a claim that every pair decays in the same way.
""",
    "exploratory-data-analysis": r"""
## What the table is, before a model is chosen

A model commits you to a distribution, a mean and a list of covariates. Exploratory data analysis, as urged by Tukey (1977), is the inspection that comes first. It asks what one row represents, which values are missing or impossible, what the marginal distributions look like, and which associations remain after the rows are grouped. It does not produce a confidence interval, a $p$-value or a causal effect. A pattern found by looking is a reason to write a particular model, and that model is then assessed on its own terms. Treating the search itself as if it had been specified in advance overstates the evidence.

## The row is not always the person

Suppose a file has one row per clinic visit, four visits for some patients and one for others, and a complication recorded on each row. Treating the rows as independent patients makes the complication look precisely estimated, because the sample size has been counted in visits. The unit you can resample is the patient. The same pass catches values that cannot be real: an age of $999$, a serum creatinine of $0$, a date that falls after the visit it is supposed to precede. Those are codes or errors, not tails. After the file is reduced to one row per patient, an association that looked strong can shrink in the [scatterplot](scatterplot.qmd). That regrouping is still description. It is why the later likelihood is written for patients rather than for lines in a file.
""",
    "exponential-tails-and-the-gumbel-law": r"""
## Centring a light tail on the logarithm

When independent copies have an unbounded but light upper tail, the sample maximum drifts to infinity slowly, like a logarithm of the sample size. The Gumbel law is the limit that appears once that logarithmic drift is subtracted and the residual is left on the natural scale of the tail.

Let $X_1,\ldots,X_n$ be independent exponential random variables of rate $\lambda>0$, so $\mathbb{P}(X_i>x)=e^{-\lambda x}$ for $x>0$, and let $M_n=\max_i X_i$. Set $b_n=(\log n)/\lambda$ and $a_n=1/\lambda$. Whenever $x>-\log n$, the level $b_n+a_n x$ is positive and

$$
\mathbb{P}\Bigl(\frac{M_n-b_n}{a_n}\le x\Bigr)
=\Bigl(1-\frac{e^{-x}}{n}\Bigr)^n
\to\exp(-e^{-x}),
$$

where the limit holds for every fixed real $x$.

The limit distribution function is the Gumbel law, supported on the whole line. Choosing $\lambda b_n=\log n$ and $\lambda a_n=1$ makes the survival probability at the moving level $b_n+a_n x$ equal $e^{-x}/n$. A normal tail is lighter than a pure exponential, but it falls in the same extreme-value family, with a centring sequence of order $\sqrt{2\log n}$ rather than $\log n$.

## Where the median of the maximum sits

Take $\lambda=1$ and $n=100$, so $b_n=\log 100\approx 4.605$ and $a_n=1$. The median of the Gumbel limit solves $\exp(-e^{-x})=1/2$, hence $x=-\log\log 2\approx 0.367$. The median of $M_{100}$ is therefore near $4.97$. A single exponential observation has median $\log 2\approx 0.693$. The maximum has moved about four units to the right, and further increases in $n$ add only $\log n$ to that location. Compare a [Pareto maximum](power-law-tails-and-the-frechet-law.qmd), which grows like a power of $n$. This logarithmic case is one of the three shapes in the [extreme-value classification](extreme-value-classification.qmd).
""",
    "extinction-criterion": r"""
## Does the lineage die out?

A Galton–Watson process starts from one individual. Each individual, independently, produces a random number of offspring and is then replaced by them. The sharp question is whether the line eventually hits zero, not whether the expected population is growing.

Let $Z_0=1$ and $Z_{n+1}=\sum_{i=1}^{Z_n}\xi_{n,i}$, where the $\xi_{n,i}$ are independent copies of an offspring count $\xi$ on $\{0,1,2,\ldots\}$, with $\mathbb{P}(\xi=k)=p_k$ and mean $m=\mathbb{E}\xi$. The state $0$ is absorbing. The extinction probability $q=\mathbb{P}(Z_n=0\text{ for some }n)$ is the smallest root in $[0,1]$ of $s=f(s)$, where $f(s)=\mathbb{E}(s^{\xi})$ is the offspring probability generating function. For a non-degenerate law with $p_0>0$, one has $q=1$ when $m\le 1$, and $q<1$ when $m>1$. If $p_0=0$, then $q=0$. The deterministic law $\xi\equiv 1$ is the exception at the boundary: $m=1$ but $f(s)=s$, and $q=0$.

## A supercritical law with extinction probability one third

Take $p_0=1/4$ and $p_2=3/4$. The mean is $m=3/2>1$, so survival has positive probability. Here $f(s)=1/4+(3/4)s^2$, and $s=f(s)$ rearranges to $(3s-1)(s-1)=0$. The smallest root in $[0,1]$ is $q=1/3$. The lineage survives with probability $2/3$, while $\mathbb{E} Z_n=(3/2)^n$ still grows. Two supercritical laws with the same mean can have different extinction probabilities, because $q$ depends on the whole of $f$. In the subcritical direction, [Markov's inequality](markov-s-inequality.qmd) gives $\mathbb{P}(Z_n>0)\le m^n$, which tends to $0$ when $m<1$. At $m=1$ that bound is useless, and extinction comes from the shape of $f$. See the [Galton–Watson process](galton-watson-process.qmd).
""",
    "extreme-value-classification": r"""
## Only three shapes for a normalised maximum

Given a large sample of independent copies, the maximum has some distribution. After an affine change of location and scale, that distribution sometimes settles to a limit. The classification theorem says the possible non-degenerate limits are three, and no others.

Let $M_n$ be the maximum of $n$ independent copies of a random variable with distribution function $F$. Suppose there exist scales $a_n>0$ and centres $b_n$ such that $(M_n-b_n)/a_n$ converges in distribution to a non-degenerate law. Then the limit distribution function is, up to a further affine change, one of

$$
\begin{aligned}
\Lambda(x)&=\exp(-e^{-x}),\\
\Phi_{\alpha}(x)&=\exp(-x^{-\alpha})\quad(x>0),\\
\Psi_{\alpha}(x)&=\exp(-(-x)^{\alpha})\quad(x<0),
\end{aligned}
$$

with $\alpha>0$, and with $\Phi_{\alpha}(x)=0$ for $x\le 0$ and $\Psi_{\alpha}(x)=1$ for $x\ge 0$. These are the Gumbel, Fréchet, and Weibull extreme-value types. The first goes with tails of exponential type, such as the exponential and normal laws, as well as some distributions with a finite endpoint; the second goes with heavy tails whose survival is regularly varying of index $-\alpha$; and the third goes with a finite upper endpoint when the survival near that endpoint is regularly varying. Fisher and Tippett (1928) found the three forms, and Gnedenko (1943) characterised the distributions attracted to each.

## What the trichotomy does not decide

Not every distribution function admits such a limit, and the trichotomy is not a recipe for a tail index. Serial dependence, a drifting law, a hard measurement cap, or an awkward threshold can overwhelm the approximation in a finite sample. The three prototypes are exact limits for three laws: the [exponential tail](exponential-tails-and-the-gumbel-law.qmd) gives $\Lambda$, a [Pareto tail](pareto-distribution.qmd) gives $\Phi_{\alpha}$, and the [uniform endpoint](a-finite-endpoint-and-a-weibull-extreme-value-law.qmd) gives a Weibull limit. Those calculations illustrate the types. They are not a fitting procedure.
""",
    "f-test-for-equal-variances": r"""
## A variance ratio against an $F$ reference

A pooled comparison of two means assumes a common variance. The check uses the two bias-corrected sample variances. Let $X_{11},\ldots,X_{1n_1}$ and $X_{21},\ldots,X_{2n_2}$ be independent normal samples, with variances $\sigma_1^2$ and $\sigma_2^2$, and write

$$
s_j^2=\frac1{n_j-1}\sum_{i=1}^{n_j}(X_{ji}-\overline X_j)^2,\qquad j=1,2.
$$

Under $H_0:\sigma_1^2=\sigma_2^2$ the ratio $F=s_1^2/s_2^2$ has the $F$ distribution on $(n_1-1,n_2-1)$ [degrees of freedom](degrees-of-freedom.qmd). This is the [variance-ratio pivot](variance-ratio-f-pivot.qmd) with the two unknown variances cancelled. Large and small values of $F$ are both evidence against equality. At level $\alpha$, reject when $F$ exceeds $F_{n_1-1,n_2-1;\,1-\alpha/2}$ or falls below $1/F_{n_2-1,n_1-1;\,1-\alpha/2}$. The lower threshold is a reciprocal because $1/W\sim F_{b,a}$ whenever $W\sim F_{a,b}$.

## Two weight samples, and a fragile level

Suppose the samples have sizes $15$ and $10$ and sample standard deviations $15$ and $12$. Then $F=225/144=1.5625$ on $(14,9)$ degrees of freedom. The level-$0.05$ critical region is $[0,0.312]\cup[3.80,\infty)$, using $F_{14,9;\,0.975}=3.80$ and $F_{9,14;\,0.975}=3.21$, whose reciprocal is $0.312$. The observed ratio lies outside that region, so the data do not contradict a common variance at the $5\%$ level.

The null distribution is sensitive to non-normality (Box, 1953). Heavy tails make $s_j^2$ more variable than chi-squared theory allows, and a nominal $5\%$ test then rejects equal variances too often. A [two-sample $t$ test](two-sample-t-test.qmd) for the means is much less sensitive to the same tails. Using the $F$ test as a gate that decides whether a pooled $t$ test is permitted distorts the later error rate, because the gate is the fragile half of the procedure. Unequal variances are handled directly as a [Behrens–Fisher problem](behrens-fisher-problem.qmd), rather than by a preliminary screen.
""",
    "factor-analysis": r"""
## Shared factors plus a diagonal of unique noise

Factor analysis explains a covariance, not merely a list of high-variance directions. For a $p$-vector $X$ the model is $X=\mu+\Lambda f+\varepsilon$, where the latent factor $f$ is $k$-dimensional with mean $0$ and covariance $I_k$, the loading matrix $\Lambda$ is $p\times k$, and the noise $\varepsilon$ is independent of $f$ with mean $0$ and diagonal covariance $\Psi=\operatorname{diag}(\psi_1,\ldots,\psi_p)$. The implied covariance is $\Sigma=\Lambda\Lambda^\top+\Psi$. Off-diagonal entries of $\Sigma$ come only from the shared factors. The unique variance $\psi_j$ is the part of $\operatorname{Var}(X_j)$ that no factor explains. [Principal component directions](principal-component-directions.qmd) diagonalise $\Sigma$, or a sample version of it, without separating that diagonal noise from the shared part. Rotating the factors by an orthogonal matrix $R$ replaces $\Lambda$ by $\Lambda R$ and leaves $\Lambda\Lambda^\top$ unchanged, so the loadings are not identified until a rotation convention is imposed. A sign flip is the one-factor case of the same invariance.

## A just-identified triad

Let $k=1$, $p=3$, $\Lambda=(0.8,0.6,0.5)^\top$ and $\Psi=\operatorname{diag}(0.36,0.64,0.75)$. Then every variable has variance $1$, and

$$
\Sigma=\begin{pmatrix}1&0.48&0.40\\0.48&1&0.30\\0.40&0.30&1\end{pmatrix}.
$$

The products of loadings recover the correlations, and $\lambda_1^2=\sigma_{12}\sigma_{13}/\sigma_{23}=0.64$ recovers the first loading up to sign. A two-variable factor model does not have this identification: four parameters $(\lambda_1,\lambda_2,\psi_1,\psi_2)$ chase three covariance entries. Maximum likelihood can also drive a unique variance to the boundary $\psi_j=0$, a Heywood case, where a factor accounts for an entire observed variable. The fit is a model for second moments. It does not by itself name the scientific content of $f$.
""",
    "family-wise-control-implies-false-discovery-control": r"""
## Two rates built from the same rejection counts

Test $m$ hypotheses, of which $m_0$ are true nulls. Let $V$ be the number of true nulls that are rejected, and let $R$ be the number of rejections of either kind. The false-discovery proportion is $Q=V/R$ when $R>0$ and $Q=0$ when $R=0$, so a procedure that rejects nothing contributes no false discoveries. The false-discovery rate is $\mathrm{FDR}=\mathbb{E}(Q)$. The family-wise error rate is $\mathrm{FWER}=\mathbb{P}(V\ge 1)$, the probability of at least one false rejection, regardless of how many true signals were found beside it. These summaries answer different questions. One asks how polluted the rejected list is, in expectation. The other asks how often that list contains any pollution at all.

## Why the inequality holds, with a numerical extreme

If $V=0$, then $Q=0$. If $V\ge 1$, then $V\le R$, so $Q\le 1$. Hence $Q\le\mathbf{1}_{\{V\ge 1\}}$ on every outcome, and taking expectations yields $\mathrm{FDR}\le\mathrm{FWER}$. When every null is true, $m_0=m$, every rejection is false, and $V=R$. Then $Q$ equals $1$ on $\{R>0\}$ and equals $0$ otherwise, so $\mathrm{FDR}=\mathbb{P}(R>0)=\mathrm{FWER}$. The two rates can stand far apart when many alternatives are true. A procedure that always rejects $50$ hypotheses, exactly one of them null, has $Q=1/50=0.02$ on every outcome, hence $\mathrm{FDR}=0.02$, while $V=1$ always and $\mathrm{FWER}=1$. Any procedure that keeps $\mathrm{FWER}\le 0.05$ therefore also keeps $\mathrm{FDR}\le 0.05$. The family-wise guarantee is the stronger event, and it can reject fewer true signals in exchange for that strength.
""",
    "finite-irreducible-chains": r"""
## One occupancy law on a finite irreducible class

On a finite state space the chain cannot wander off forever. If every state can reach every other state, there is exactly one stationary distribution, and it charges every state. Convergence of the $n$-step probabilities needs one more assumption, aperiodicity.

Let $P$ be the transition matrix of a chain on a finite set $S$. Irreducibility means that for every pair $i,j$ there is some $n\ge 0$ with $p_{ij}^{(n)}>0$: the chain has a single communicating class. Then there is a unique probability row vector $\pi$ with $\pi P=\pi$, and $\pi_j>0$ for every $j$. The weight is the reciprocal mean return time. If $T_i^{+}=\inf\{n\ge 1:X_n=i\}$, then $\pi_i=1/\mathbb{E}_i T_i^{+}$. A state visited often has a short mean return. If the chain is also aperiodic, $p_{ij}^{(n)}\to\pi_j$ for every start $i$ and every destination $j$. Without aperiodicity, $\pi$ still exists and still equals the long-run fraction of time spent in each state. The one-time distributions may oscillate.

## A self-loop that removes the period

Deterministic alternation, $p_{01}=p_{10}=1$, is finite and irreducible, with $\pi=(1/2,1/2)$ and period $2$. The probabilities $p_{00}^{(n)}$ oscillate between $0$ and $1$. Now change the chain to $p_{00}=1/2$, $p_{01}=1/2$, $p_{10}=1$, and $p_{11}=0$. A return to $0$ is possible in one step, so the period is $1$. Solving $\pi P=\pi$ gives $\pi_0=2/3$ and $\pi_1=1/3$, and $p_{ij}^{(n)}$ converges to those values. The mean return to $0$ is $3/2$. Aperiodicity belongs to the limit, not to the existence of $\pi$. See [recurrence and period](recurrence-and-period.qmd).
""",
    "finite-mixture-model": r"""
## One density built from several sources

Some samples look multimodal because each draw comes from one of several populations that were not labelled. A finite mixture writes the marginal density as

$$
f(x)=\sum_{h=1}^{H}\pi_h f_h(x),
$$

with $H$ fixed, weights $\pi_h\ge 0$ summing to $1$, and component densities $f_h$. Equivalently, draw a component indicator with $\mathbb{P}(H_i=h)=\pi_h$ and then draw $x$ from $f_h$. The weight $\pi_h$ is a probability of origin, not a statement that the components have equal variance or equal scientific status. The marginal mean is the weighted average of the component means. The marginal variance adds the average within-component variance to the variance of the component means. Labels are not observed, so the likelihood of a sample is a product of sums, and swapping the names of two components leaves $f$ unchanged.

## Two normal sources

The mixture $0.3\,\varphi(x;0,1)+0.7\,\varphi(x;4,1)$, with $\varphi(\,\cdot\,;\mu,\sigma^2)$ a normal density, has mean $0.7\times 4=2.8$. Its variance equals $1+0.3(0-2.8)^2+0.7(4-2.8)^2=1+2.352+1.008=4.36$. The modes sit near $0$ and $4$ because the means are several standard deviations apart. Moving the means to $0$ and $1$ keeps a mixture formula and can leave a unimodal marginal, so several components do not guarantee several visible bumps. A normal component whose variance shrinks to $0$ at a single observation sends $f$ to infinity at that point, and the supremum of the likelihood need not be attained. Constraining the covariances, or comparing fits by a penalised criterion with that constraint stated, is part of using the model. The [EM algorithm](em-algorithm.qmd) is one way to search for a stationary point.
""",
    "fisher-s-direction": r"""
## Separation of the means relative to pooled scatter

For two labelled samples, let $\widehat\mu_1$ and $\widehat\mu_2$ be the class means, set $d=\widehat\mu_1-\widehat\mu_2$, and let $S$ be a pooled within-class covariance, assumed positive definite. A direction $a\neq 0$ projects the two means to the scalars $a^\top\widehat\mu_1$ and $a^\top\widehat\mu_2$. The two projected class means sit equally far from their midpoint, so the sum of their squared deviations is half the squared gap. Dividing that by the pooled variance $a^\top S a$ is how Fisher measures separation (Fisher, 1936). Rescaling $a$ multiplies the numerator and the denominator by the same positive factor, so only the direction matters. The ratio in the form $\bigl(a^\top d\bigr)^2\big/\bigl(2\,a^\top S a\bigr)$ is maximised at $a\propto S^{-1}d$, and the maximal value is $d^\top S^{-1}d\big/2$. The proof is Cauchy–Schwarz applied to $(S^{1/2}a)^\top(S^{-1/2}d)$: equality holds when $S^{1/2}a$ is parallel to $S^{-1/2}d$. If $d=0$ the numerator is identically zero and every direction is equally uninformative.

## A diagonal calculation

Let $S=\operatorname{diag}(2,1)$ and $d=(2,2)^\top$. Then $S^{-1}d=(1,2)^\top$ and $d^\top S^{-1}d=6$, so the maximal ratio is $3$. The naive direction $a=d$ has $a^\top d=8$ and $a^\top S a=12$, hence ratio $64/(2\times 12)=8/3\approx 2.667$, which is strictly smaller. The inverse covariance stretches the coordinate whose pooled variance is $1$, because a one-unit gap there is more impressive than a one-unit gap in the coordinate whose pooled variance is $2$. The direction matches the coefficient vector of linear discriminant analysis when the two classes share a normal covariance, but the derivation of $S^{-1}d$ used only means and $S$. It does not supply the intercept, and it does not by itself choose a threshold on the projected line.
""",
    "five-number-summary-and-boxplot": r"""
## The middle half, and then the extremes

The minimum and the maximum say nothing about the middle, and the mean says nothing about the tails. The five-number summary reports both ends and the middle: the minimum, the first quartile, the median, the third quartile and the maximum. A boxplot draws a box from the first quartile to the third, puts a line at the median, and runs whiskers out to the most extreme observations that are still within $1.5$ [interquartile ranges](interquartile-range.qmd) of the box. Points outside that fence are drawn individually. Tukey (1977) popularised the factor $1.5$. It is a convention for drawing, not a test that the flagged points are mistakes.

## Nine numbers, one of them past the fence

Take the ordered sample $2,3,3,4,5,6,7,8,20$. The median is $5$. With hinges that include the median in both halves, the first quartile is the third ordered value $3$ and the third quartile is $7$, so the interquartile range is $4$. The upper fence is $7+1.5\times 4=13$. The value $8$ lies inside the fence and ends the whisker; $20$ is drawn on its own. The five numbers are therefore $2,3,5,7,20$. The range is $18$, almost all of it from one point, while the box width is $4$. A long whisker, or a crowd of points beyond the fence, can be the tail of a skewed measurement. That is a finding about the shape. Deleting every flagged point would estimate a different population from the one that was sampled, and the plot itself does not authorise that deletion.
""",
    "fixed-rule-error": r"""
## The error of a rule that will not be refitted

Once a classifier $\eta$ has been trained and then locked, its future performance is a property of a fresh pair $(X,Y)$ drawn from the joint distribution $F$. Under zero–one loss, $Q(y,\eta(x))$ equals $1$ when $\eta(x)\neq y$ and equals $0$ otherwise. The fixed-rule error is the expectation $\mathrm{Err}=\mathbb{E}_F\bigl[Q(Y,\eta(X))\bigr]=\mathbb{P}\bigl(\eta(X)\neq Y\bigr)$. Class-specific rates condition on the true class. With prevalence $\pi_g=\mathbb{P}(Y=g)$ and indicator $I(Y,g)$,

$$
\mathrm{Err}_g=\mathbb{P}\bigl(\eta(X)\neq Y\mid Y=g\bigr)
=\frac{\mathbb{E}_F\bigl[Q(Y,\eta(X))\,I(Y,g)\bigr]}{\pi_g},
$$

and the law of total probability puts the pieces back together as $\mathrm{Err}=\sum_g\pi_g\mathrm{Err}_g$. The rule $\eta$ is not a function of the new pair. Replacing $\eta$ by a rule that was fitted on $(X,Y)$ itself would produce the apparent error, a different and usually smaller number.

## A rare class that contributes as much as the common class

Suppose two classes have prevalences $\pi_1=0.8$ and $\pi_2=0.2$, with class-specific errors $\mathrm{Err}_1=0.1$ and $\mathrm{Err}_2=0.4$. The overall error is $0.8\times 0.1+0.2\times 0.4=0.16$. Each class contributes $0.08$ to that total: the rare class is less common and more often misclassified, and those two facts cancel in the sum. An estimate of $\mathrm{Err}$ alone would hide the $0.4$. The same decomposition shows what a test set must contain. If class $2$ is scarce in the test sample, the average of $Q$ estimates $\mathrm{Err}$ with high variance in the rare-class term, even when the overall count of mistakes looks stable. The definition is also silent about costs. A loss that charges more for missing class $2$ would rank rules differently while leaving these zero–one rates unchanged.
""",
    "flat-prior": r"""
## Constant on one scale only

A flat prior gives the parameter a constant density on the scale at which it was written. On the whole real line that constant cannot be a probability: $\int_{-\infty}^{\infty} c \,\mathrm{d}\mu$ diverges for every $c > 0$, so the weight $p(\mu) \propto 1$ is an [improper prior](improper-prior.qmd). When the [likelihood function](likelihood-function.qmd) is integrable in $\mu$, the posterior is the normalised likelihood and a posterior mode is a [maximum likelihood](maximum-likelihood.qmd) estimate. Flatness does not survive a reparameterisation. If $\eta = e^{\mu}$ and the weight is constant in $\mu$, the [Jacobian](jacobian.qmd) contributes a factor $1/\eta$, so the weight in the $\eta$ coordinate is proportional to $1/\eta$. Calling a prior noninformative without naming the parameterisation omits the scale on which the constancy was assumed.

## A widening slab escapes every window

The proper uniform stand-in on a bounded interval is $p_C(\mu) = (1/(2C))\, \mathbf{1}_{\{-C \le \mu \le C\}}$. For any fixed window $|\mu| \le M$ with $0 < M < C$, this slab assigns probability $M/C$ to the window. As $C \to \infty$ that probability tends to $0$. The sequence of proper uniforms does not converge to a probability distribution that is uniform on the line; the mass escapes every fixed range. For iid normal observations with known variance the improper flat weight is still usable, because $n \ge 1$ observations produce a proper normal posterior centred at the sample mean, with variance $\sigma^2/n$. The finite slab shows what that limiting weight is spending its mass on, while remaining a genuine probability distribution.
""",
    "fold-cross-validation": r"""
## Every case is tested once, by a rule that did not see it

$K$-fold cross-validation splits the $n$ labelled cases into $K$ folds. For each $k$, the classifier $\eta_{(X^{(-k)},y^{(-k)})}$ is trained on the cases outside fold $k$, then scored on the $n_k$ cases inside the fold. The mismatch $Q$ is $1$ when the predicted label differs from $y_i^{(k)}$ and $0$ otherwise. The estimator $\widehat{\mathrm{Err}}_{\mathrm{KCV}}$ adds every case's mismatch and divides by $n$, not by $K$. Each observation therefore has equal weight, including when the fold sizes differ by one because $n$ is not divisible by $K$. The choice $K=n$ is leave-one-out cross-validation. Common compromises are $K=5$ and $K=10$: each training set is only a little smaller than the full sample, and only $K$ fits are required.

## Why the divisor is $n$ rather than a mean of fold rates

Suppose two folds have sizes $10$ and $30$, with $2$ and $3$ mistakes. The pooled estimator is $(2+3)/40=0.125$. The unweighted mean of the fold rates is $(0.20+0.10)/2=0.15$, which gives the small fold the same vote as the large one. The $1/n$ formula avoids that distortion. The estimator targets the error of a rule trained on about $n(1-1/K)$ cases. That target is close to the error of the full-sample rule when $K$ is large, and it is a more pessimistic target when $K$ is small. Choosing a tuning constant on these same scores reuses the test folds. Nesting a fresh split inside each training block estimates the whole selection procedure.
""",
    "fubini-s-theorem": r"""
## Expectation as an integral of tails

A double integral of a non-negative function may be evaluated in either order, and the common value may be infinite. If a signed function is absolutely integrable, the two orders again agree and the integral is finite. That swap is what turns a lifetime into an area under its survival curve. For a random variable $T\ge 0$,

$$
T=\int_0^T 1\,\mathrm{d} t=\int_0^{\infty}\mathbf{1}_{\{T>t\}}\,\mathrm{d} t.
$$

The integrand is non-negative, so expectation and integral may change places:

$$
\mathbb{E} T=\int_0^{\infty}\mathbb{P}(T>t)\,\mathrm{d} t,
$$

whenever the integral is allowed to take the value infinity. The integrand $\mathbb{P}(T>t)$ is the [survival function](survival-function.qmd). The same argument with sums, for a random variable $N$ taking values $0,1,2,\ldots$, gives $\mathbb{E} N=\sum_{k=1}^{\infty}\mathbb{P}(N\ge k)$.

The hypothesis matters. If $T$ can be negative, the integral from $0$ to infinity recovers only the expectation of the positive part. If the positive and negative parts both have infinite expectation, then $\mathbb{E} T$ does not exist, and swapping an integral that is not absolutely integrable can change the answer.

## A fair die, summed by tails

Let $T$ be uniform on $\{1,2,3,4,5,6\}$. Then $\mathbb{P}(T\ge k)=(7-k)/6$ for $k=1,\ldots,6$. The tail sum is

$$
1+\frac56+\frac46+\frac36+\frac26+\frac16=\frac{21}{6}=3.5,
$$

which matches $(1+2+3+4+5+6)/6$. An exponential lifetime with rate $\lambda$ has survival $e^{-\lambda t}$, and the integral of that survival is $1/\lambda$, the mean. Both checks are the same theorem, once in sums and once in integrals.
""",
    "generated-and-borel-sigma-algebras": r"""
## The smallest family closed under the operations we use

Probability is assigned to events, and the family of events has to be closed under complements and countable unions. Starting from a few sets one can actually name, the generated sigma-algebra is the smallest family that contains them and is closed in that way.

If $\mathcal{C}$ is a collection of subsets of $\Omega$, the generated sigma-algebra $\sigma(\mathcal{C})$ is the intersection of every sigma-algebra containing $\mathcal{C}$. For a single set $A$ it consists of $\emptyset$, $A$, $A^{c}$, and $\Omega$. For two sets $A$ and $B$, the four atoms

$$
A\cap B,\quad A\cap B^{c},\quad A^{c}\cap B,\quad A^{c}\cap B^{c}
$$

partition $\Omega$. Any event built from $A$ and $B$ is assembled from some of these atoms, which caps the sigma-algebra at $16$ sets, or fewer if an atom is empty.

## Borel sets, including the singletons

On the line, $\mathcal{B}(\mathbb{R})$ is the sigma-algebra generated by the open intervals. A closed interval is a complement of an open set, a half-open interval is a difference of opens, and a singleton is $\{x\}=\bigcap_{n\ge 1}(x-1/n,x+1/n)$. A countable set, being a union of singletons, is Borel as well. A Vitali set, one point from each rational translate class, is not Borel: not every subset of $\mathbb{R}$ is an event. Ordinary random variables are required only to pull Borel sets back into $\mathcal{F}$. That is the content of a [measurable random variable](measurable-random-variable.qmd).
""",
    "generator": r"""
## Rates rather than one-step probabilities

In continuous time there is no universal tick at which the chain must jump. The generator records the instantaneous rate of each possible jump. A rate has units of inverse time and is allowed to exceed $1$. The row of a generator sums to $0$, not to $1$.

On a finite state space the off-diagonal entries $q_{ij}\ge 0$ are jump rates, and the diagonal is set to $q_{ii}=-\sum_{j\neq i}q_{ij}$ so that each row sums to $0$. That matrix is $Q$, and $\nu_i=-q_{ii}$ is the rate of leaving $i$. Over a short interval of length $h$,

$$
\mathbb{P}\bigl(X(t+h)=j\mid X(t)=i\bigr)=q_{ij}h+o(h),\qquad j\neq i,
$$

while the probability of still being in $i$ is $1-\nu_i h+o(h)$. If $\nu_i>0$, the chain holds an exponential time of rate $\nu_i$ and then jumps to $j$ with probability $q_{ij}/\nu_i$. Those jump probabilities, not the rates, are the entries that sum to $1$. An absorbing state has $\nu_i=0$.

## Two states, and where the time is spent

Suppose the chain moves from $0$ to $1$ at rate $\alpha=2$ and from $1$ to $0$ at rate $\beta=4$. Then

$$
Q=\begin{pmatrix}-2&2\\ 4&-4\end{pmatrix}.
$$

The stationary equation $\pi Q=0$ gives $\pi_0=2/3$ and $\pi_1=1/3$. The chain leaves $0$ more slowly than it leaves $1$, so it spends twice as long in $0$. The mean hold in $0$ is $1/2$ and the mean hold in $1$ is $1/4$, and $(1/2)/(1/2+1/4)=2/3$ recovers $\pi_0$. The [holding time](holding-time.qmd) and the [jump chain](jump-chain.qmd) are the two pieces this rate matrix separates.
""",
    "gibbs-inequality": r"""
## A probability vector scores itself best

Let $p=(p_h)$ and $q=(q_h)$ be probability vectors on the same finite set, with $q_h>0$ whenever $p_h>0$. Gibbs' inequality says $\sum_h p_h\log p_h\ge\sum_h p_h\log q_h$, with equality if and only if $p=q$. The logarithm is natural. Rearranged, the difference is the Kullback–Leibler divergence $\sum_h p_h\log(p_h/q_h)$, so the inequality is the statement that this divergence is nonnegative. The short proof applies Jensen's inequality to the convex function $-\log$, or notes that $\log u\le u-1$ with $u=q_h/p_h$. For $p=(0.9,0.1)$ and $q=(0.5,0.5)$,

$$
\sum_h p_h\log p_h\approx -0.325,
\qquad
\sum_h p_h\log q_h=\log(1/2)\approx -0.693.
$$

The gap is about $0.368$ nats. Replacing $q$ by $p$ closes it. Any other $q$ leaves a strictly positive gap.

## Where the gap appears in one EM update

In a mixture, the observed log-likelihood and the expected complete log-likelihood differ by an entropy term in the latent labels. Write $\tau_h(x_i;\Psi)$ for the membership of component $h$ at parameter $\Psi$, and define $G(\Psi;\Psi^{(k)})=\sum_i\sum_h\tau_h(x_i;\Psi^{(k)})\log\tau_h(x_i;\Psi)$. Gibbs' inequality, applied at each $i$ with $p_h=\tau_h(x_i;\Psi^{(k)})$, gives $G(\Psi;\Psi^{(k)})\le G(\Psi^{(k)};\Psi^{(k)})$. The change in the observed log-likelihood from $\Psi^{(k)}$ to the next EM value splits into the rise in $Q$, which the M step makes nonnegative, and the drop in $G$, which Gibbs makes nonnegative. Both pieces are needed for the proof that the observed likelihood does not fall. Equality throughout holds when the new parameter induces the same memberships and the M step does not move $Q$.
""",
    "graphical-lasso": r"""
## A Gaussian likelihood with an $L^1$ charge on the precision

The graphical lasso estimates a positive definite precision matrix $K$ when the edge set is unknown (Friedman, Hastie and Tibshirani, 2008). Let $S$ be the sample covariance of $p$ variables. The objective maximises $\log|K|-\operatorname{tr}(SK)-\lambda\lVert K\rVert_1$, where $\lVert K\rVert_1$ sums the absolute values of all entries and $\lambda\ge 0$ is the penalty. The corners of the $L^1$ penalty allow exact zeros, and a zero off-diagonal entry is a missing edge. In the block algorithm, $W$ is a working estimate of the covariance, started at $W=S+\lambda I$ so that the start is positive definite even when $S$ is singular. For column $j$, the block $A$ is the remaining indices, $\beta$ is a vector of regression coefficients of variable $j$ on the others, and $z$ is a subgradient of the absolute value: $z_k=\operatorname{sign}(\beta_k)$ when $\beta_k\neq 0$, and $z_k\in[-1,1]$ when $\beta_k=0$. The update $w_{AB}=W_{AA}\widehat\beta$ refreshes that column of $W$. At convergence the precision column satisfies $\widehat\theta_{AB}=-\widehat\beta\,\widehat\theta_{BB}$, the usual block-inverse relation between regression coefficients and concentration, with $1/\widehat\theta_{BB}$ equal to the residual variance $w_{BB}-w_{AB}^\top\widehat\beta$.

## A diagonal sample covariance is already a fixed point

If $S=I_p$, the matrix $K=(1+\lambda)^{-1}I_p$ is optimal. The working covariance $W=K^{-1}=(1+\lambda)I_p$ equals the initial value $S+\lambda I$, every off-diagonal regression coefficient is zero, and the penalty does not invent edges. A large $\lambda$ pushes a nondiagonal $S$ towards this sparse pattern; $\lambda=0$ with $S$ nonsingular recovers $K=S^{-1}$. A fitted zero is a restriction at the chosen $\lambda$, under the Gaussian model that makes a precision entry a conditional-independence statement.
""",
    "hammersley-clifford": r"""
## Conditional independence drawn as a missing edge

An undirected graph $G$ has a vertex for each coordinate of a random vector $X$. The pairwise Markov property says that if $j$ and $k$ are not joined by an edge, then $X_j\perp X_k$ given all the remaining coordinates. A distribution factorises according to $G$ when its density, relative to a product measure, is a product of clique potentials $\psi_C$ divided by a normalising constant $Z$. Each potential depends only on the variables inside one clique, a complete subset of vertices. The Hammersley–Clifford theorem states that if the density is strictly positive on the product space, the pairwise Markov property and the factorisation are equivalent (Besag, 1974).

## A chain whose conditional odds ignore the far variable

On three binary coordinates, let the graph be the chain $1-2-3$, so the only maximal cliques are the edges $\{1,2\}$ and $\{2,3\}$. The unnormalised density $\exp(1.2\,x_1 x_2+0.8\,x_2 x_3)$ factorises into a potential of $(x_1,x_2)$ and a potential of $(x_2,x_3)$. Given $x_2=1$, the conditional odds of $x_1=1$ against $x_1=0$ equal $e^{1.2}$, whether $x_3$ is $0$ or $1$. Given $x_2=0$, those odds equal $1$ for both values of $x_3$. The missing edge means that the conditional distribution of $X_1$ given $(X_2,X_3)$ does not depend on $X_3$. If some of the eight binary atoms had probability zero, the same pairwise statements could fail to produce a clique factorisation.
""",
    "hard-margin-dual": r"""
## Multipliers for the margin constraints

The hard-margin primal looks for a weight $w$ and an intercept $b$ that separate labels $y_i\in\{-1,+1\}$ with functional margin at least $1$, while keeping $\tfrac12 w^\top w$ small. Each constraint $y_i(w^\top x_i+b)\ge 1$ receives a multiplier $\alpha_i\ge 0$. Stationarity with respect to $w$ produces $w=\sum_i\alpha_i y_i x_i$, and stationarity with respect to $b$ produces the linear constraint $\sum_i\alpha_i y_i=0$. Substituting these relations into the Lagrangian leaves a quadratic function of the multipliers alone,

$$
Q(\alpha)=\sum_{i=1}^n\alpha_i-\frac12\sum_{i=1}^n\sum_{j=1}^n\alpha_i\alpha_j y_i y_j x_i^\top x_j,
$$

which is maximised over $\alpha_i\ge 0$ subject to $\sum_i\alpha_i y_i=0$. Complementary slackness says that $\alpha_i>0$ only when case $i$ lies on the margin. Those cases are the support vectors. Every other training point has $\alpha_i=0$ and disappears from the expansion of $w$. The decision value at a new $x$ is $\sum_i\alpha_i y_i x_i^\top x+b$, an inner product between training points and the query.

## Two points on the line

Take $(x,y)=(-1,-1)$ and $(1,+1)$. The constraint $\sum\alpha_i y_i=0$ forces $\alpha_1=\alpha_2$. Then $Q=2\alpha_1-2\alpha_1^2$, whose maximum on $\alpha_1\ge 0$ is at $\alpha_1=\alpha_2=1/2$, with $Q=1/2$. Both multipliers are positive, so both points are support vectors, and $w=\alpha_1(-1)(-1)+\alpha_2(1)(1)=1$. The intercept recovered from either margin equation is $b=0$. The primal objective at this $w$ is also $1/2$, which is strong duality for a feasible problem with a positive gap. If the two labels cannot be separated by any hyperplane, the primal is infeasible and this dual, with $\alpha_i$ unbounded above, is unbounded as well. Slack variables are what put a finite upper bound on each $\alpha_i$.
""",
    "hard-margin-primal": r"""
## The widest gap, written as the shortest weight

Suppose two classes with labels $y_i\in\{-1,+1\}$ can be separated by a hyperplane. Among all separating hyperplanes, the hard-margin problem prefers the one whose slab between the classes is widest. A weight $w$ and intercept $b$ represent the same hyperplane as any positive multiple of $(w,b)$. The normalisation $y_i(w^\top x_i+b)\ge 1$ fixes that scale by putting the nearest points at functional margin $1$. The Euclidean distance from the origin-shifted plane $w^\top x+b=0$ to the plane $w^\top x+b=1$ equals $1/\lVert w\rVert$. The two classes therefore stand $2/\lVert w\rVert$ apart. Maximising the gap is the same geometry as minimising $\lVert w\rVert$, and minimising $\Phi(w)=\tfrac12 w^\top w$ has the same minimiser with a gradient equal to $w$. When the classes are linearly separable with a positive gap, strict convexity in $w$ makes the optimal weight unique. The intercept is unpenalised.

## The same two points in the primal

For the sample $(-1,-1)$ and $(1,+1)$, the constraints are $w-b\ge 1$ and $w+b\ge 1$. Adding them forces $w\ge 1$. The choice $w=1$, $b=0$ meets both constraints with equality, and $\Phi=1/2$. Any larger $|w|$ increases $\Phi$. The geometric margin on each side is $1/\lVert w\rVert=1$, and the gap between the two parallel lines $x=-1$ and $x=1$ is $2$. Doubling $(w,b)$ to $(2,0)$ raises $\Phi$ from $1/2$ to $2$. A third point at the origin stays separable under either label ($w=2,b=1$ for $+1$ or $w=2,b=-1$ for $-1$), whereas a third point at $x=2$ with label $-1$ makes the inequalities contradictory. The hard-margin primal is then infeasible, and a soft-margin slack is required before a finite optimum exists.
""",
    "hartigan-wong-algorithm": r"""
## Single-point transfers aimed at the same criterion

Lloyd's algorithm reassigns every point and then replaces every centre by a mean. A Lloyd fixed point is stable under that pair of moves, but the within-cluster sum of squares $\widetilde W=\sum_i\lVert x_i-m_{C(i)}\rVert^2$ can still fall if one point is moved and the two affected centres are recomputed. The Hartigan–Wong algorithm searches for such transfers (Hartigan and Wong, 1979). It keeps a live set of clusters that have recently changed, proposes moving one point into another cluster, and accepts the move when the resulting $\widetilde W$ decreases. Empty clusters are avoided by refusing a transfer that would leave a cluster with no points. The criterion is the same sum of squares that [Lloyd's algorithm](lloyd-s-k-means-algorithm.qmd) minimises. The path through partitions is different, so a start that traps Lloyd can remain available to a later one-point move.

## A transfer that leaves a Lloyd fixed point

On the corners $(0,0)$, $(0,1)$, $(10,0)$ and $(10,1)$, the horizontal partition has centres $(5,0)$ and $(5,1)$ and $\widetilde W=100$. Each point is nearer its own centre than the other, so Lloyd has stopped. Move $(10,0)$ into the upper cluster. The lower cluster is the single point $(0,0)$, with sum of squares $0$. The upper cluster $\{(0,1),(10,1),(10,0)\}$ has mean $(20/3,2/3)$ and sum of squares $606/9$, already below $100$, so the transfer is accepted. The point was nearer its old centre before the centres moved. Further transfers can reach the vertical partition, whose value is $1$. The terminal partition is optimal only relative to the moves under consideration.
""",
    "hazard-rate": r"""
## Failure among the survivors

A lifetime density says how much probability sits near time $t$. The hazard says how fast units that have already survived to $t$ are failing. Let $T\ge 0$ have density $f$ and [survival function](survival-function.qmd) $R(t)=\mathbb{P}(T>t)$. For every $t$ with $R(t)>0$,

$$
h(t)=\frac{f(t)}{R(t)}.
$$

For a small $\varepsilon>0$, the conditional probability of failure in $[t,t+\varepsilon)$, given survival to $t$, is about $\varepsilon\, h(t)$. Since $R'(t)=-f(t)$, the hazard is also $h(t)=-\frac{\mathrm{d}}{\mathrm{d} t}\log R(t)$. Integrating from $0$ and using $R(0)=1$ for a continuous lifetime with no mass at the origin gives $R(t)=\exp\bigl(-\int_0^t h(u)\,\mathrm{d} u\bigr)$. The integral of $h$ is the cumulative hazard. A constant hazard $h(t)=\lambda$ is the [exponential distribution](exponential-distribution.qmd) with rate $\lambda$, and it is the continuous lifetime with the [memoryless property](memoryless-property.qmd).

## A hazard that rises in proportion to age

Take $h(t)=2t$ for $t>0$. Then $\int_0^t h(u)\,\mathrm{d} u=t^2$, so $R(t)=e^{-t^2}$. This is the [Weibull law](weibull-distribution.qmd) with shape $2$ and rate $1$. The median solves $t^2=\log 2$, so $t=\sqrt{\log 2}\approx 0.833$, where $\log$ is the natural logarithm. The mean is $\Gamma(3/2)=\sqrt{\pi}/2\approx 0.886$. A single Weibull hazard is monotone. A bathtub hazard, high in early life, flat in middle life and high again with wear, is not this formula with one shape parameter. An atom at $0$, a unit dead on arrival, also sits outside the density formula and has to be handled as a point mass before the integral for $R$ begins.
""",
    "hinge-loss": r"""
## The slack that remains at the optimum

Soft-margin training allows the linear score $f(x)=w^\top x+b$ to miss the functional margin $1$. The slack $\xi_i\ge 0$ is constrained by $y_i f(x_i)\ge 1-\xi_i$, with $y_i\in\{-1,+1\}$, and the primal penalises $\sum_i\xi_i$ with a cost $C>0$ beside $\tfrac12\lVert w\rVert^2$. At the optimum there is no reason to make a slack larger than the constraint requires, so $\xi_i=\max\{0,\,1-y_i f(x_i)\}$. Substituting that value produces the hinge loss plus an $L^2$ penalty on $w$,

$$
\sum_{i=1}^n\max\{0,\,1-y_i f(x_i)\}+\frac{1}{2C}\lVert w\rVert^2.
$$

The hinge is zero whenever $y_i f(x_i)\ge 1$. A point that is correctly classified and at least a unit of functional margin away from the boundary exerts no pull. The factor $1/(2C)$ plays the role of a [regularisation](regularisation.qmd) weight: small $C$ charges the squared norm heavily and tolerates more margin violations; large $C$ spends more effort driving the slacks down. On separable data a large enough $C$ recovers a hard-margin solution.

## Four functional margins

The hinge at $y f=2$ equals $0$. At $y f=1$ it equals $0$. At $y f=0.2$ it equals $0.8$. At $y f=-1$ it equals $2$. Squared error does not share the flat region: a point with $y=1$ and $f=3$ has hinge $0$ but squared error $(1-3)^2=4$, so a squared-error fit keeps moving $w$ to reduce a residual that the hinge has already declared good enough. The binomial deviance likewise keeps a nonzero slope on correctly classified points, with negative derivative $-1/(e^{y f}+1)$ in the margin $y f$ so the loss keeps falling as the margin grows. The hinge is convex, and it is not differentiable at $y f=1$.
""",
    "holding-time": r"""
## The wait has to forget its age

Once a continuous-time chain has entered a state, the remaining time until it leaves must not depend on how long it has already stayed. If the elapsed time carried information, the present state would not be a sufficient summary of the past. That forces the holding time to be exponential.

From state $i$, the holding time $H_i$ is exponential with rate $\nu_i=-q_{ii}$, independent of the history before entry and independent of the state jumped to next. The survival function is $\mathbb{P}(H_i>t)=e^{-\nu_i t}$ for $t\ge 0$, and the mean hold is $1/\nu_i$ when $\nu_i>0$. Memorylessness is the identity $\mathbb{P}(H_i>t+s\mid H_i>t)=\mathbb{P}(H_i>s)$. If $\nu_i=0$, the state is absorbing and the hold is infinite.

## A race of clocks

The same hold can be built as a race. From $i$, start an independent exponential clock of rate $q_{ij}$ for each $j\neq i$. The minimum of independent exponential clocks is exponential with rate equal to the sum of the rates, which is $\nu_i$, and the probability that clock $j$ rings first is $q_{ij}/\nu_i$. That probability is exactly the jump probability of the embedded chain. Take $\nu_i=3$ per hour, with two exit routes of rates $1$ and $2$. The mean hold is $20$ minutes. The chance of still being in $i$ after $30$ minutes is $e^{-1.5}\approx 0.223$. The rate-$2$ route is chosen with probability $2/3$, and that chance does not depend on how long the hold lasted. See the [memoryless property](memoryless-property.qmd) of the [exponential distribution](exponential-distribution.qmd).
""",
    "homogeneous-poisson-process": r"""
## Counts at a steady rate, with independent increments

A homogeneous Poisson process is the counting model for events that arrive at a constant rate, with no lingering effect of the past and no extra clustering beyond what independence already produces. The increment over an interval depends on the length of the interval and on nothing else.

A process $N(t)$, $t\ge 0$, with $N(0)=0$, is a homogeneous Poisson process of rate $\lambda>0$ when it has stationary independent increments and

$$
N(t+h)-N(t)\sim\mathrm{Poisson}(\lambda h),\qquad t,h\ge 0.
$$

Thus $\mathbb{E} N(t)=\operatorname{Var}(N(t))=\lambda t$, and $\mathbb{P}(N(t)=k)=e^{-\lambda t}(\lambda t)^{k}/k!$. An equivalent construction uses the gaps. The interarrival times are independent exponential random variables of rate $\lambda$ and mean $1/\lambda$, and the arrival time of the $n$th event is their sum. That sum is finite for every $n$ and diverges as $n\to\infty$, so $N(t)$ is finite for each finite $t$ and tends to infinity as $t$ grows. There is no explosion in finite time.

## A half-hour window

Take $\lambda=2$ events per hour. Over a half hour the mean count is $1$. Then $\mathbb{P}(N(0.5)=0)=e^{-1}\approx 0.368$, and

$$
\mathbb{P}(N(0.5)\ge 2)=1-2e^{-1}\approx 0.264.
$$

The increment over any other half hour has the same Poisson law, and it is independent of the increment over a disjoint half hour. Superposing two independent Poisson processes adds their rates. Keeping each event independently with probability $r$ multiplies the rate by $r$. Both closures fail if a single shock creates several events at once, because that mark is shared rather than drawn independently for each event. See [stationary and independent increments](stationary-and-independent-increments.qmd).
""",
    "identity-link": r"""
## When the mean is already the linear predictor

Some responses are free to take any real value. A temperature anomaly, a difference of log measurements, or a gain score does not need to be forced into $(0,1)$ or kept positive. The identity link sets $g(\mu)=\mu$, so the mean equals the linear predictor, $\mu_i=\mathbf{x}_i^\top\boldsymbol{\beta}$. With independent normal responses of constant variance $\sigma^2$, this is the ordinary [normal linear model](normal-linear-model.qmd), and the identity is the canonical link for that [random component](random-component.qmd). The coefficient of a covariate is then the change in the mean for a one-unit change in that covariate, with the others held fixed. There is no factor to exponentiate and no odds to translate.

## A straight line can leave the legal range

The same link is a poor default when the mean is constrained. Give a count the predictor $2-0.5x$. At $x=2$ the fitted mean is $1$, at $x=4$ it is $0$, and at $x=6$ it is $-1$. A mean count cannot be negative, so the identity link has produced an impossible prediction as soon as $x$ leaves a short window. A temperature anomaly $\mu=-0.2+0.03x$ is allowed to be negative: at $x=10$ it equals $0.1$, and at $x=-10$ it equals $-0.5$, both legal. Constant variance is the other assumption packed into the normal identity model. If the scatter fans out as the mean rises, the link may still be right while $\sigma^2$ is not. Ordinary standard errors are then too small in the high-mean region and too large in the low-mean region.
""",
    "improper-prior": r"""
## Infinite mass is not a probability

Bayes' rule divides the product of likelihood and prior by its integral. The division is legitimate only when that integral is finite and strictly positive. A prior is proper when it is already a probability distribution, hence has total mass one. An improper prior is a nonnegative weight whose integral over the parameter space is infinite. It is not a distribution one could draw from, and posterior propriety is a separate fact: the product of the [likelihood function](likelihood-function.qmd) and the weight must have a finite positive integral. That integral has to be checked for the model and the sample at hand. Writing down a kernel does not guarantee it.

## One normal mean works; an empty binomial tail need not

For iid $\operatorname{N}(\mu, \sigma^2)$ observations with $\sigma^2$ known, the [flat](flat-prior.qmd) weight $p(\mu) \propto 1$ is improper, but $n \ge 1$ observations yield a proper posterior $\operatorname{N}(\overline{x}, \sigma^2/n)$. The likelihood supplies the decay the prior lacks. The Haldane weight $p(\theta) \propto \theta^{-1}(1-\theta)^{-1}$ on a binomial probability is also improper. Multiplied by a binomial likelihood with $x$ successes in $n$ trials it leaves the kernel of a $\operatorname{Beta}(x, n-x)$ density, which integrates if and only if $x \ge 1$ and $n-x \ge 1$. A sample of all successes leaves a non-integrable posterior. The same check applies to a flat weight on a variance and to a hierarchical hyperprior. A proper posterior at one sample size need not remain proper at a smaller one.
""",
    "intensity-function": r"""
## A rate allowed to change with the clock

Some streams of events speed up and slow down on a known schedule: a rush hour, a decaying hazard, a daily cycle. The counts over disjoint intervals can still be independent. What fails is stationarity, because a later interval of the same length need not have the same mean.

Let $\lambda(u)\ge 0$ be a locally integrable intensity. The cumulative intensity is $\Lambda(t)=\int_0^{t}\lambda(u)\,\mathrm{d}u$. A non-homogeneous Poisson process with this intensity has independent increments, and

$$
N(t)-N(s)\sim\mathrm{Poisson}\bigl(\Lambda(t)-\Lambda(s)\bigr),\qquad 0\le s\le t.
$$

The mean of an increment is the area under $\lambda$ over that interval. If $\lambda$ is the constant $\lambda$, then $\Lambda(t)=\lambda t$ and the process is homogeneous. A useful construction is the time change $N(t)=\widetilde{N}(\Lambda(t))$, where $\widetilde{N}$ is a homogeneous Poisson process of rate $1$. Randomness sits entirely in $\widetilde{N}$. The function $\Lambda$ only warps the clock.

## A rate that grows linearly

Take $\lambda(u)=2u$ for $u\ge 0$. Then $\Lambda(t)=t^{2}$. The count on $[0,2]$ is Poisson with mean $4$. The count on $[2,3]$ is Poisson with mean $9-4=5$, and the two counts are independent. Equal lengths do not give equal means: $[0,1]$ has mean $1$, while $[2,3]$ has mean $5$. The probability of no event on $[0,t]$ is $e^{-t^{2}}$, which decays much faster than the exponential survival $e^{-\lambda t}$ of a constant rate. An intensity is a deterministic function in this model. A random intensity would be a Cox process, a different dependence structure, because the increments would share the unobserved rate path.
""",
    "interarrival-time": r"""
## The gaps that build the arrival times

A counting process can be described forwards, by the number of events up to time $t$, or backwards, by the times at which the count increases. The interarrival time is the gap between successive events, and for a homogeneous Poisson process those gaps are the whole model.

Let $T_0=0$ and let $T_n$ be the time of the $n$th event. The interarrival times are $W_n=T_n-T_{n-1}$ for $n\ge 1$. If $N$ is homogeneous Poisson of rate $\lambda>0$, then $W_1,W_2,\ldots$ are independent exponential random variables with density $\lambda e^{-\lambda t}$ on $(0,\infty)$ and mean $1/\lambda$. Conversely, independent exponential gaps of rate $\lambda$ produce a Poisson process of rate $\lambda$. The arrival time $T_n=\sum_{i=1}^{n} W_i$ has the Erlang law, the gamma law with integer shape $n$ and rate $\lambda$, and mean $n/\lambda$. The count and the waiting time are linked by the identity

$$
\mathbb{P}(T_n\le t)=\mathbb{P}(N(t)\ge n).
$$

The $n$th event has occurred by time $t$ exactly when at least $n$ events lie in $[0,t]$.

## A third event inside the hour

Take $\lambda=4$ per hour, so a typical gap is $15$ minutes. Then $\mathbb{P}(W_1>1/2)=e^{-2}\approx 0.135$: only about one gap in seven exceeds half an hour, which is the memoryless survival of the exponential law. The third arrival has mean time $3/4$ of an hour, and

$$
\mathbb{P}(T_3>1)=\mathbb{P}(N(1)\le 2)=e^{-4}\bigl(1+4+8\bigr)=13e^{-4}\approx 0.238.
$$

For a non-homogeneous process the gaps are neither independent nor exponential. The first gap alone has survival $\mathbb{P}(T_1>t)=e^{-\Lambda(t)}$, which reduces to $e^{-\lambda t}$ only when the [intensity](intensity-function.qmd) is constant.
""",
    "interval-for-a-ratio-of-variances": r"""
## From an $F$ pivot to an interval

A pooled $t$ interval for a difference of means is valid when the two variances are equal. An interval for their ratio checks that claim without forcing it. Let the samples be independent and normal, of sizes $n_1$ and $n_2$, with variances $\sigma_1^2$ and $\sigma_2^2$, and let $s_1^2$ and $s_2^2$ be the bias-corrected sample variances, each using divisor $n_j-1$. The [variance-ratio pivot](variance-ratio-f-pivot.qmd)

$$
W=\frac{s_1^2/\sigma_1^2}{s_2^2/\sigma_2^2}
$$

has the $F_{n_1-1,n_2-1}$ distribution. Write $\rho=\sigma_1^2/\sigma_2^2$ and $r=s_1^2/s_2^2$, so $W=r/\rho$. Place $W$ between its quantiles of orders $\alpha/2$ and $1-\alpha/2$. The lower quantile equals $1/F_{n_2-1,n_1-1;\,1-\alpha/2}$, because a reciprocal $F$ variable swaps the degrees of freedom. Solving for $\rho$ gives the level $1-\alpha$ interval

$$
\left(\frac{r}{F_{n_1-1,n_2-1;\,1-\alpha/2}},\ r\,F_{n_2-1,n_1-1;\,1-\alpha/2}\right).
$$

The coverage is computed before the data are seen. The numerical interval is not assigned that probability after the samples have been drawn.

## A factor of four, and a very wide interval

Take $n_1=n_2=9$, $s_1^2=16$ and $s_2^2=4$, so $r=4$. The upper $0.975$ quantile of $F_{8,8}$ is $4.43$. The $95\%$ interval for $\rho$ is $(4/4.43,\ 4\times 4.43)=(0.903,\ 17.72)$. It contains $1$, so equal variances are compatible with the data, but $\sigma_1^2$ could still be nearly $18$ times $\sigma_2^2$. Containing $1$ is weak reassurance when the interval is this wide. Square roots of the endpoints, $0.95$ and $4.21$, give the corresponding interval for $\sigma_1/\sigma_2$, valid because the square root is increasing. Heavy tails inflate the variability of $s_j^2$ and the claimed coverage fails. A zero sample variance breaks the continuous $F$ pivot: if $s_1^2=0$ and $s_2^2>0$ the ratio degenerates to $0$, whereas if $s_2^2=0$ and $s_1^2>0$ the ratio is infinite and the interval blows up.
""",
    "intraclass-correlation": r"""
## How much of the scatter belongs to the block

Patients in one hospital share a theatre, a staff and a catchment. A random-intercept model writes the response of person $i$ in block $j$ as $Y_{ji}=\mu+\alpha_j+\varepsilon_{ji}$. The block effects $\alpha_j$ are uncorrelated, with mean $0$ and variance $\sigma_A^2$. The individual errors $\varepsilon_{ji}$ are uncorrelated, with mean $0$ and variance $\sigma^2$, and they are uncorrelated with the block effects. One response then has variance $\sigma_A^2+\sigma^2$. Two people in different blocks have covariance $0$. Two people in the same block share $\alpha_j$, so their covariance is $\sigma_A^2$. The intraclass correlation is

$$
\frac{\sigma_A^2}{\sigma_A^2+\sigma^2}.
$$

It is the fraction of the total variance that sits between blocks. It equals $0$ when $\sigma_A^2=0$ and $\sigma^2>0$, and it equals $1$ when $\sigma^2=0$ and $\sigma_A^2>0$.

## A numerical split, and a sign this model cannot give

If $\sigma_A^2=3$ and $\sigma^2=1$, the correlation is $3/4=0.75$. Three of the four units of variance are the hospital. A treatment contrast computed as if the patients were independent then overstates the precision, because the independent pieces of information are closer in number to the hospitals than to the patients. The correlation cannot be negative. The numerator $\sigma_A^2$ is a variance and the denominator is at least as large, so whenever the ratio is defined it lies in $[0,1]$. Shares that compete inside a block, such as proportions that sum to a fixed total, can be negatively associated, and a single random intercept cannot represent that. An [exchangeable correlation](exchangeable-correlation.qmd) used as a working matrix can sit a little below zero. The correlation implied by this [random-intercept model](random-intercept-model.qmd) cannot.
""",
    "inverse-link": r"""
## A mean that is a reciprocal

Clotting times and claim amounts are positive and continuous, and they often become more variable as they become larger. A gamma random component with variance $\phi\mu^2$ has that shape. Its canonical link, up to the sign of the natural parameter, is the inverse link $g(\mu)=1/\mu$, so

$$
\mu=\frac{1}{\mathbf{x}^\top\boldsymbol{\beta}},
$$

provided the linear predictor stays positive. A predictor of $0.25$ gives mean $4$. A predictor of $0.05$ gives mean $20$. Halving a small predictor doubles a large mean, so the map is far from a straight line in the mean. The coefficient is neither a difference in $\mu$ nor a multiplicative factor on $\mu$. It is a difference in the rate $1/\mu$.

## The reciprocal breaks when the predictor crosses zero

Nothing in the observations keeps $\mathbf{x}^\top\boldsymbol{\beta}$ positive. With intercept $0.5$ and slope $-0.1$, the predictor at $x=4$ is $0.1$ and the mean is $10$. At $x=6$ the predictor is $-0.1$ and the formal mean is $-10$. A clotting time cannot be negative, and just before the crossing the fitted mean has already exploded through large positive values. The [log link](log-link.qmd) $\mu=\exp(\mathbf{x}^\top\boldsymbol{\beta})$ stays positive for every real predictor, which is why it is the usual gamma link even though the inverse is the canonical one. Canonical structure simplifies the score. It does not guarantee a legal mean at the edge of the covariates. If an inverse fit stays positive only by a narrow margin inside the observed $x$, predictions a short step beyond the data are not usable.
""",
    "ising-model": r"""
## Neighbouring spins that prefer to agree

A binary lattice makes the normalising constant the whole difficulty. Put a spin $x_i \in \{-1,+1\}$ at each of $m$ sites, and write $i \sim j$ when $i$ and $j$ are neighbours. With coupling $\beta \in \mathbb{R}$, the Ising model (Ising, 1925) gives a configuration $\boldsymbol{x} = (x_1,\ldots,x_m)$ the unnormalised weight $\exp(\beta \sum_{i \sim j} x_i x_j)$. Each product $x_i x_j$ equals $+1$ when the neighbours agree and $-1$ when they differ. If $\beta > 0$ the weight favours local alignment; if $\beta < 0$ it favours alternation. The probability is the weight divided by the partition function $Z$, the sum of the weights over all $2^m$ configurations. For a $20 \times 20$ lattice, $m = 400$ and that sum cannot be evaluated term by term. Marginal probabilities and $Z$ itself have no useful closed form.

## Ratios that never build $Z$

A Metropolis update needs only ratios of probabilities. In a ratio of two configurations, $Z$ cancels, and flipping one spin changes the sum only on the edges that touch that site. The acceptance ratio is therefore a short function of the neighbouring spins. The original [Metropolis algorithm](metropolis-algorithm.qmd) was built for targets of this kind, using a symmetric proposal so that the proposal densities cancel as well (Metropolis et al., 1953). Hastings' later correction multiplies by the proposal ratio when the proposal is not symmetric. The lattice model is the statistical point in physical language: an intractable normaliser does not prevent simulation when the [Metropolis–Hastings](metropolis-hastings-algorithm.qmd) ratio is allowed to use the unnormalised weight.
""",
    "jackknife-bias-and-standard-error": r"""
## A comparison manufactured inside the sample

The bias of an estimator $\hat\theta$ is $\mathbb{E}(\hat\theta)-\theta$, and $\theta$ is unknown, so the bias cannot be computed by subtracting the truth. The jackknife builds a comparison from leave-one-out refits (Quenouille, 1956; Tukey, 1958). Let $\hat\theta_{(i)}$ be the estimate computed on the sample with observation $i$ removed, and let $\hat\theta_{(\cdot)}=n^{-1}\sum_i\hat\theta_{(i)}$ be their average. The jackknife bias is $(n-1)\bigl(\hat\theta_{(\cdot)}-\hat\theta\bigr)$, and the bias-corrected estimate is $n\hat\theta-(n-1)\hat\theta_{(\cdot)}$. The jackknife standard error is

$$
\widehat{\mathrm{se}}_{\mathrm{jack}}
=\Biggl(\frac{n-1}{n}\sum_{i=1}^n\bigl(\hat\theta_{(i)}-\hat\theta_{(\cdot)}\bigr)^2\Biggr)^{1/2}.
$$

The factor $n-1$ matches a bias expansion in powers of $1/n$. For the sample mean the population bias is zero, and the jackknife reproduces both that fact and the usual standard error $s/\sqrt{n}$, with $s^2$ the unbiased sample variance.

## Five numbers whose mean is already unbiased

The sample $2,4,6,8,10$ has mean $\hat\theta=6$. The leave-one-out means are $7$, $6.5$, $6$, $5.5$ and $5$, so $\hat\theta_{(\cdot)}=6$ and the jackknife bias is $(4)(6-6)=0$. The corrected estimate remains $6$. The squared deviations of the leave-one-out means from $6$ sum to $2.5$, and $\widehat{\mathrm{se}}_{\mathrm{jack}}=\sqrt{(4/5)\times 2.5}=\sqrt{2}\approx 1.414$. The unbiased sample variance is $10$, and $\sqrt{10}/\sqrt{5}=\sqrt{2}$, the same value. Smooth functions of means are the setting in which this match extends. The sample median is a warning: its jackknife variance estimator is inconsistent, because deleting one central observation often leaves the median unchanged and then moves it abruptly. A bootstrap variance is the more reliable companion for that nonsmooth statistic.
""",
    "jacobian": r"""
## Density has to undo a stretch

Probability in a small region is density times volume. A smooth change of variables stretches that volume, so the density on the new scale has to be multiplied by the stretch. Let $\mathbf{X}$ take values in an open subset of $\mathbb{R}^n$ with density $f_{\mathbf{X}}$, and let $\mathbf{Z}=g(\mathbf{X})$ where $g$ is a smooth bijection onto its image, with inverse $h$ whose derivative matrix $Dh(\mathbf{z})$ has non-zero determinant. The [transformation rule](transformation-rule.qmd) says

$$
f_{\mathbf{Z}}(\mathbf{z})=f_{\mathbf{X}}(h(\mathbf{z}))\,\lvert\det Dh(\mathbf{z})\rvert.
$$

The absolute value of the Jacobian determinant is the local factor by which $h$ changes volume. In one dimension, $Y=aX+b$ with $a\ne 0$ has inverse $x=(y-b)/a$ and Jacobian factor $1/\lvert a\rvert$, so $f_Y(y)=f_X((y-b)/a)/\lvert a\rvert$. For a linear map $\mathbf{Z}=A\mathbf{X}$ with $A$ invertible, the factor is $1/\lvert\det A\rvert$ and the density is evaluated at $A^{-1}\mathbf{z}$.

If a linear map $\mathbf{Z}=A\mathbf{X}$ has $\det A=0$, its image lies in a proper subspace and has no density on the whole of $\mathbb{R}^n$; by contrast, an isolated zero of a smooth bijection's derivative, such as $y=x^3$ at the origin, still pushes a density on $\mathbb{R}$ forward to a density on $\mathbb{R}$.

## Doubling a uniform

Let $X$ be uniform on $(0,1)$, with density $1$, and set $Y=2X$. The inverse is $x=y/2$ and $\lvert\mathrm{d} x/\mathrm{d} y\rvert=1/2$, so $f_Y(y)=1/2$ for $y\in(0,2)$. Then $\mathbb{P}(Y\le 1)=\mathbb{P}(X\le 1/2)=1/2$, and integrating the density $1/2$ over $(0,1)$ gives the same value. Omitting the Jacobian leaves the constant function $1$ on $(0,2)$, which integrates to $2$ and is not a density. The absolute value matters as well: a negative derivative reverses orientation, but probability uses volume, not signed volume.
""",
    "joint-distribution-and-density": r"""
## A multivariate law on orthants, and when a density exists

A random vector $\mathbf{X}=(X_1,\ldots,X_p)^\top$ always has a joint distribution function $F(\mathbf{x})=\mathbb{P}(X_1\le x_1,\ldots,X_p\le x_p)$ on $\mathbb{R}^p$. Sending all coordinates except $x_j$ to $+\infty$ recovers the marginal distribution function $F_{X_j}(x_j)$: the event $\{X_k\le\infty\}$ has probability $1$, so the intersection shrinks to $\{X_j\le x_j\}$. A rectangle probability is not a single difference $F(\mathbf{b})-F(\mathbf{a})$ once $p\ge 2$; in two dimensions $\mathbb{P}(a_1<X_1\le b_1,\,a_2<X_2\le b_2)=F(b_1,b_2)-F(a_1,b_2)-F(b_1,a_2)+F(a_1,a_2)$, and in $p$ dimensions the inclusion–exclusion sum over the $2^p$ corners must be non-negative on every box.

Absolute continuity asks for more than smooth margins. A joint density $f\ge 0$ exists on $\mathbb{R}^p$ only when probabilities of sets of $p$-dimensional volume zero vanish. If $X_1\sim\operatorname{N}(0,1)$ and $X_2=X_1$, each coordinate has a smooth normal density on $\mathbb{R}$, yet $(X_1,X_2)$ sits entirely on the diagonal line $\{x_1=x_2\}$, which has two-dimensional area zero. Then $F(x_1,x_2)=\Phi(\min(x_1,x_2))$ has a ridge along the diagonal, and no joint density $f(x_1,x_2)$ on $\mathbb{R}^2$ integrates to $F$.

## Differentiating on the unit square

Let $(X_1,X_2)$ have $F(x_1,x_2)=x_1 x_2(x_1+x_2)/2$ on $[0,1]^2$. Differentiating once in $x_1$ and once in $x_2$ gives

$$
f(x_1,x_2)=\frac{\partial^2 F}{\partial x_1\,\partial x_2}(x_1,x_2)=x_1+x_2,\qquad 0<x_1,x_2<1,
$$

which is non-negative and integrates to $\int_0^1\int_0^1(x_1+x_2)\,\mathrm{d}x_1\,\mathrm{d}x_2=1$. Integrating $x_2$ out gives the marginal density $f_{X_1}(x_1)=x_1+1/2$ on $(0,1)$, matching the derivative of $F(x_1,1)=(x_1^2+x_1)/2$. Compare [joint probability density](joint-probability-density.qmd) for integrating over general regions.
""",
    "jump-chain": r"""
## The sequence of states, with the clock removed

A continuous-time chain does two things in a state: it waits, and then it chooses a different state. The jump chain keeps only the sequence of states visited. It is a discrete-time chain, useful because many path questions do not depend on the holding times.

Let $q_{ij}$ be the rate from $i$ to $j\neq i$, and let $\nu_i=-q_{ii}=\sum_{j\neq i}q_{ij}$. If $\nu_i>0$, the embedded jump chain moves from $i$ to $j$ with probability $k_{ij}=q_{ij}/\nu_i$, and $k_{ii}=0$. If $\nu_i=0$, the state is absorbing and $k_{ii}=1$. The matrix $K=(k_{ij})$ is a transition matrix. The continuous-time path is recovered by attaching an independent exponential hold of rate $\nu$ at the current state between successive jumps of $K$. If the chain is irreducible and positive recurrent, $\pi Q=0$, and $0<\sum_k\pi_k\nu_k<\infty$, the jump chain has stationary distribution

$$
\hat\pi_i=\frac{\pi_i\nu_i}{\sum_k\pi_k\nu_k}.
$$

States that are left quickly are visited more often by the jump chain, for the same share of calendar time. An absorbing state has $\nu_i=0$, so a stationary distribution concentrated there makes the denominator zero and keeps the jump chain at that absorber.

## Alternation in jumps, convergence in time

Take rates $\alpha=2$ from $0$ to $1$ and $\beta=4$ from $1$ to $0$. Time-stationarity gives $\pi=(2/3,1/3)$. The exit rates are $2$ and $4$, and $\pi_0\nu_0=\pi_1\nu_1=4/3$, so $\hat\pi=(1/2,1/2)$. The jump chain alternates deterministically, so it is periodic and does not converge. Exponential [holding times](holding-time.qmd) destroy that parity, and the continuous-time probabilities still converge. The rates themselves sit in the [generator](generator.qmd).
""",
    "kernel": r"""
## An inner product that is never written in feature coordinates

In a support-vector classifier the training points enter the dual only through inner products $x_i^\top x_j$. A feature map $\phi$ replaces that inner product by $\phi(x_i)^\top\phi(x_j)$. A kernel is any function $K$ that equals such an inner product for some $\phi$, possibly into an infinite-dimensional space. The decision function becomes $\sum_i\alpha_i y_i K(x_i,x)+b$. The vector $\phi(x)$ is never required, which is the [kernel trick](kernel-trick.qmd). A necessary and sufficient condition is that every finite Gram matrix $K(x_i,x_j)$ be symmetric and positive semi-definite. Mercer's theorem adds continuity and domain conditions under which $K$ has an eigen-expansion; the Gram-matrix condition is the one used to keep the dual concave. The word kernel is also used for the bump function in density estimation. That bump integrates to one. The kernel on this page is a covariance of features, and it need not integrate to anything.

## A quadratic map, and a function that fails

For $x=(x_1,x_2)$ the polynomial kernel $K(u,v)=(u^\top v)^2$ matches the feature map $\phi(x)=(x_1^2,\sqrt{2}\,x_1 x_2,x_2^2)$. Indeed $\phi(u)^\top\phi(v)=(u^\top v)^2$. With $u=(1,1)$ and $v=(2,0)$, the original inner product is $2$ and $K(u,v)=4$. The same value is $\phi(u)^\top\phi(v)=(1,\sqrt{2},1)^\top(4,0,0)=4$. The classifier can use $4$ without storing $\phi$. The function $K(u,v)=-u^\top v$ is not a kernel: at any $u\neq 0$ the one-point Gram matrix equals $-\lVert u\rVert^2<0$. A proposed similarity has to pass the Gram test before it can replace an inner product in the dual.
""",
    "kernel-density-discriminant-analysis": r"""
## A class density estimated by bumps, then weighted by the prior

Linear and quadratic discriminant analysis replace each class density by a normal density. Kernel discriminant analysis makes the same Bayes comparison without that parametric shape. Let $\pi_g$ be the prior probability of class $g$, and let the $n_g$ training points with label $g$ estimate the class density by a [kernel density estimator](kernel-density-estimator.qmd)

$$
\widehat f_g(x)=\frac{1}{n_g}\sum_{i:y_i=g}K_{H_g}(x-x_i).
$$

Here $K$ is a symmetric probability density, $H_g$ is a symmetric positive definite bandwidth matrix, and $K_{H_g}(u)=|H_g|^{-1/2}K(H_g^{-1/2}u)$. The plug-in rule predicts $g^*=\arg\max_g\pi_g\widehat f_g(x)$. In one dimension, $H_g=h_g^2$ and a standard normal kernel reduces $K_H(u)$ to $h^{-1}\varphi(u/h)$. The bandwidths are chosen inside each training split, then frozen before the test points are scored. A bandwidth must be supported by nearby observations, which becomes difficult as the dimension grows.

## Two classes on the line, with unit bandwidth

Let class $1$ contain $\{0,1\}$, class $2$ contain $\{4,5\}$, both priors equal $1/2$, and let $h=1$, so each bump is a standard normal density. At $x=3$,

$$
\widehat f_1(3)=\frac{\varphi(3)+\varphi(2)}{2}\approx 0.029,
\qquad
\widehat f_2(3)=\frac{\varphi(1)+\varphi(2)}{2}\approx 0.148.
$$

The weighted densities $0.015$ and $0.074$ select class $2$. At the midpoint $x=2.5$ the two kernel estimates agree by symmetry, and equal priors leave a tie. A very large common bandwidth flattens both estimates until the prior alone decides every $x$. A very small bandwidth makes $\widehat f_g(x)$ tiny unless $x$ sits on a training point of class $g$.
""",
    "kernel-density-estimator": r"""
## Replacing each point mass by a bump of controlled width

The empirical distribution places mass $1/n$ at each sample point $x_i\in\mathbb{R}^p$ and has no ordinary density. A kernel density estimator spreads that mass. Let $K$ be a symmetric probability density and let $H$ be a symmetric positive definite bandwidth matrix. Then

$$
\widehat f(x;H)=\frac1n\sum_{i=1}^n K_H(x-x_i),
\qquad
K_H(u)=|H|^{-1/2}K(H^{-1/2}u),
$$

where $H^{-1/2}$ comes from a spectral square root. Because $K$ integrates to one, so does each $K_H$ and so does $\widehat f$. Nonnegativity of $K$ makes the estimate nonnegative. In one dimension the usual parameterisation is $H=h^2$, and a standard normal $K$ gives bumps of standard deviation $h$. Small $h$ keeps fine detail and sampling noise. Large $h$ damps both. The mean integrated squared error balances the resulting bias and variance. The training likelihood does not: as $h\to 0$ the density at each sample point diverges, so a held-out score or an estimate of the integrated error is what selects $h$.

## Three observations and a unit bandwidth

Take $\{-1,0,2\}$, a standard normal kernel and $h=1$. At the origin each bump contributes a standard normal ordinate,

$$
\widehat f(0)=\frac{\varphi(1)+\varphi(0)+\varphi(2)}{3}\approx\frac{0.242+0.399+0.054}{3}\approx 0.232.
$$

The same calculation at $x=2$ replaces the ordinates by $\varphi(3)$, $\varphi(2)$ and $\varphi(0)$, about $0.152$. Moving $h$ from $1$ to $0.2$ multiplies the central bump by $5$ and makes the estimate a sum of narrow spikes; moving $h$ to $3$ pulls $\widehat f(0)$ down towards the average of three wide bumps. An unconstrained $H$ has $p(p+1)/2$ free entries, already a difficult search at moderate $p$.
""",
    "knot": r"""
## Continuity across a join

A polynomial of high degree fitted globally across an interval oscillates wildly near the endpoints when a single region bends sharply. A spline avoids global oscillation by joining low-degree polynomials end to end at ordered points $\xi_1<\cdots<\xi_M$ called knots. For a cubic spline, the truncated power basis writes

$$
g(x)=\beta_0+\beta_1 x+\beta_2 x^2+\beta_3 x^3+\sum_{m=1}^M \gamma_m (x-\xi_m)_+^3,
$$

where $(u)_+=\max(u,0)$ (de Boor, 1978). Because $(x-\xi_m)_+^3$ and its first two derivatives vanish at $x=\xi_m$, adding $\gamma_m(x-\xi_m)_+^3$ leaves $g(\xi_m)$, $g'(\xi_m)$ and $g''(\xi_m)$ continuous while shifting the third derivative by $6\gamma_m$. Thus a cubic spline with these $M$ knots spans a linear space of dimension $M+4$; adding natural boundary constraints (linearity outside $[\xi_1,\xi_M]$) removes $4$ parameters and leaves $M$ free dimensions when $\xi_1$ and $\xi_M$ are the boundary knots (or $M+2$ free dimensions when $M$ counts strictly interior knots between two separate boundary knots).

## Placement and number of knots

With $M=1$ knot at $\xi_1=0$, $g(x)=x+(x)_+^3$ equals $x$ for $x\le 0$ and $x+x^3$ for $x>0$: value $0$, slope $1$, and curvature $0$ match at the join, while curvature grows smoothly as $6x$ to the right. In unpenalised regression splines, too many knots overfit and knot locations matter; in penalised regression splines, placing $10$–$30$ knots at sample quantiles gives ample local flexibility while the roughness penalty controls [effective degrees of freedom](effective-degrees-of-freedom.qmd).
""",
    "kolmogorov-extension-theorem": r"""
## A process specified only through finite collections of times

One often describes a process by saying what $(X_{t_1},\ldots,X_{t_k})$ should look like for every finite list of times, without ever naming the probability of a path property. Kolmogorov's extension theorem says that a consistent family of finite-dimensional distributions on $\mathbb{R}$ (or any Polish state space) is already enough to guarantee some process with exactly those margins (Kolmogorov, 1933).

Consistency has two parts. Permuting the times must permute the joint law in the same way. Dropping one time must leave the marginal law of the remaining times. Under those hypotheses there exists a probability space and a family $\{X_t:t\in T\}$ whose finite-dimensional distributions are the ones prescribed. The theorem is an existence result. It does not produce continuous paths, or a bound on the number of jumps.

## Gaussian margins are not yet a continuous Brownian motion

Suppose every finite collection $(X_{t_1},\ldots,X_{t_k})$ is multivariate normal with mean $0$ and $\operatorname{Cov}(X_s,X_t)=\min(s,t)$. These laws are consistent, because a margin of a Gaussian vector is Gaussian and the covariance of a subset is the corresponding submatrix. The extension theorem supplies a process with those margins. A version whose paths are continuous is a further theorem: the process delivered on the raw product space need not have continuous sample paths. Likewise, writing down consistent Poisson margins does not by itself hand over a counting path that increases by jumps of size $1$. The [Poisson process](homogeneous-poisson-process.qmd) is built from exponential clocks precisely to obtain that regularity. Consistency of the finite-dimensional laws is the weaker statement.
""",
    "kolmogorov-forward-and-backward-equations": r"""
## Two ways of differentiating the transition semigroup

The transition probabilities of a continuous-time chain form a semigroup: moving for time $s$ and then for time $t$ is the same as moving for time $s+t$. Differentiating that identity at the origin produces a linear equation driven by the generator. There are two places to put the generator, and on a finite state space they agree.

Let $p_{ij}(t)=\mathbb{P}(X(t)=j\mid X(0)=i)$ and let $P(t)$ be the matrix of these probabilities. The Chapman–Kolmogorov identity is $P(s+t)=P(s)P(t)$. With $P(0)=I$ and generator $Q$, the forward and backward equations are

$$
P'(t)=P(t)Q,
\qquad
P'(t)=QP(t).
$$

In the forward equation one looks at where the chain sits an instant before $t$ and applies $Q$ there. In the backward equation one looks at the first jump out of the starting state. With finitely many states and rates that do not change with time, that initial-value problem is solved by the series $P(t)=\sum_{n\ge 0}(tQ)^{n}/n!$, written $e^{tQ}$. Both products agree, since each term is a power of $Q$. On a countable state space, uniqueness can fail if the chain explodes.

## A scalar check with equal rates

Let the chain flip from $0$ to $1$ at rate $\alpha$ and from $1$ to $0$ at rate $\beta$. Set $u(t)=\mathbb{P}(X(t)=1\mid X(0)=0)$. Either equation reduces to $u'(t)=\alpha-(\alpha+\beta)u(t)$ with $u(0)=0$, so

$$
u(t)=\frac{\alpha}{\alpha+\beta}\bigl(1-e^{-(\alpha+\beta)t}\bigr).
$$

With $\alpha=\beta=1$, $u(1)=(1-e^{-2})/2\approx 0.432$, and $u(t)$ rises to the stationary value $1/2$. The derivative at $0$ equals $\alpha$, the instantaneous rate of leaving the start. See the [generator](generator.qmd) for the short-time rules that justify the differentiation (Kolmogorov, 1931).
""",
    "kullback-leibler-divergence": r"""
## Extra log-score from using the wrong density

Let $f$ and $g$ be densities on the same space, with $g$ positive wherever $f$ is positive. The Kullback–Leibler divergence (Kullback and Leibler, 1951) is

$$
D(f\,\Vert\,g)=\int f(x)\log\frac{f(x)}{g(x)}\,\mathrm{d}x
=\int f\log f-\mathbb{E}_f\bigl[\log g(X)\bigr],
$$

using the natural logarithm, and the integral form becomes a sum for a discrete distribution. The first term does not depend on $g$. Minimising $D(f\,\Vert\,g)$ over a family of candidates $g$ is therefore the same comparison as maximising the expected log-likelihood $\mathbb{E}_f[\log g(X)]$. Gibbs' inequality, or Jensen's inequality applied to $-\log$, gives $D(f\,\Vert\,g)\ge 0$, with equality when $f=g$ almost everywhere. The divergence is not a distance. It is not symmetric, and it does not satisfy the triangle inequality.

## Bernoulli numbers, read in both directions

Let $f$ be Bernoulli($0.9$) and $g$ Bernoulli($0.5$). Then

$$
D(f\,\Vert\,g)=0.9\log(1.8)+0.1\log(0.2)\approx 0.368
$$

nats, while $D(g\,\Vert\,f)=0.5\log(0.5/0.9)+0.5\log(0.5/0.1)\approx 0.511$ nats. Predicting the true biased coin with a fair-coin model is a different penalty from predicting a fair coin with the biased model. In model selection the unknown $f$ is held fixed and the fitted density plays the role of $g$, so only one direction is in view. The constant $\int f\log f$ cancels when two fitted densities are compared. AIC is built as an estimate of that expected log-score, corrected for having fitted the candidate on the same sample that is used to score it. The divergence itself remains a population comparison, not a test statistic with a critical value.
""",
    "learning-rate": r"""
## How far to walk along minus the gradient

Gradient descent replaces a weight $w$ by $w-\varepsilon\,\partial E/\partial w$, where $E$ is the training objective and the learning rate $\varepsilon>0$ is the step length. The same step length is often written $\eta$. Nothing in the update distinguishes a steep slope from a long step: the product $\varepsilon\,\partial E/\partial w$ is the change that is actually applied. On a quadratic bowl the right length is visible in closed form. For $E(w)=(w-3)^2$ the derivative is $2(w-3)$, and the error after one update is multiplied by $1-2\varepsilon$. The fixed point is $w=3$. The absolute value of the multiplier is smaller than $1$ precisely when $0<\varepsilon<1$, so those step lengths converge. At $\varepsilon=1$ the multiplier is $-1$ and the iterate oscillates. Beyond $1$ it diverges.

## Five steps, then an oscillation

Start at $w=0$ with $\varepsilon=0.1$. The multiplier is $0.8$, and the iterates are $0.60$, $1.08$, $1.46$, $1.77$ and $2.02$, approaching $3$ from below. With $\varepsilon=1$ the same start produces $6,0,6,0,\ldots$, a permanent oscillation about the minimiser. With $\varepsilon=1.1$ the multiplier is $-1.2$ and the distance to $3$ grows by $20\%$ at every step. A loss built from logistic units is only locally quadratic. A step that is stable on a shallow part of $E$ can be too long near a steep sigmoid. A fixed step tuned to a full-sample gradient can also be too long for a one-pattern update, whose noise a constant $\varepsilon$ does not remove.
""",
    "least-squares-decomposition": r"""
## An orthogonal split of a candidate residual

Fix a response $\boldsymbol{y} \in \mathbb{R}^{n}$ and an $n \times p$ design $\boldsymbol{X}$ of rank $p$. Every candidate coefficient $\boldsymbol{\beta}$ has residual vector $\boldsymbol{y} - \boldsymbol{X}\boldsymbol{\beta}$ and candidate sum of squares $\operatorname{SSE}(\boldsymbol{\beta}) = \lVert \boldsymbol{y} - \boldsymbol{X}\boldsymbol{\beta} \rVert_2^2$. [Ordinary least squares](ordinary-least-squares.qmd) chooses $\widehat{\boldsymbol{\beta}} = (\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{-1}\boldsymbol{X}^{\mathsf{T}}\boldsymbol{y}$, with fitted residual $\widehat{\boldsymbol{e}} = \boldsymbol{y} - \boldsymbol{X}\widehat{\boldsymbol{\beta}}$ and fitted sum of squares $\operatorname{SSE} = \lVert \widehat{\boldsymbol{e}} \rVert_2^2$. Decompose the candidate residual as $\boldsymbol{y} - \boldsymbol{X}\boldsymbol{\beta} = \widehat{\boldsymbol{e}} + \boldsymbol{X}(\widehat{\boldsymbol{\beta}} - \boldsymbol{\beta})$. The normal equations say $\boldsymbol{X}^{\mathsf{T}}\widehat{\boldsymbol{e}} = \boldsymbol{0}$, so $\widehat{\boldsymbol{e}}$ is orthogonal to the column space of $\boldsymbol{X}$, while $\boldsymbol{X}(\widehat{\boldsymbol{\beta}} - \boldsymbol{\beta})$ lies in that column space. Their inner product vanishes, and Pythagoras in $\mathbb{R}^{n}$ gives

$$
\operatorname{SSE}(\boldsymbol{\beta}) = \operatorname{SSE} + \lVert \boldsymbol{X}(\boldsymbol{\beta} - \widehat{\boldsymbol{\beta}}) \rVert_2^2.
$$

## The quadratic term is the posterior penalty

The second term equals $(\boldsymbol{\beta} - \widehat{\boldsymbol{\beta}})^{\mathsf{T}}\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X}(\boldsymbol{\beta} - \widehat{\boldsymbol{\beta}})$. Full column rank makes $\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X}$ [positive definite](positive-definite-matrix.qmd), so the quadratic term is zero only at $\widehat{\boldsymbol{\beta}}$ and is positive elsewhere. The identity is algebra: it does not require normal errors, and it shows both that the least-squares minimiser is unique and what the minimal value is. Under a Gaussian linear model with a flat prior on $\boldsymbol{\beta}$, the same quadratic is the kernel of the normal posterior of $\boldsymbol{\beta}$ given $\sigma^2$. The fitted $\operatorname{SSE}$ is what remains for the marginal posterior of $\sigma^2$. Moving $\boldsymbol{\beta}$ away from $\widehat{\boldsymbol{\beta}}$ spends residual sum of squares; it does not change the fitted sum of squares, which has already been minimised.
""",
    "least-squares-estimators-are-unbiased": r"""
## The slope is a fixed linear combination

Unbiasedness of a fitted straight line uses the means and nothing else. Suppose $\mathbb{E} Y_i=\beta_0+\beta_1 x_i$ for $i=1,\ldots,n$, with the $x_i$ fixed and not all equal. Write $S_{xx}=\sum_i(x_i-\overline x)^2>0$ and $S_{xY}=\sum_i(x_i-\overline x)(Y_i-\overline Y)$. The [least-squares](ordinary-least-squares.qmd) estimators are $\widehat\beta_1=S_{xY}/S_{xx}$ and $\widehat\beta_0=\overline Y-\widehat\beta_1\overline x$. Because $\sum_i(x_i-\overline x)=0$, the terms in $\overline Y$ drop out of $S_{xY}$, and

$$
\widehat\beta_1=\sum_{i=1}^n c_i Y_i,\qquad c_i=\frac{x_i-\overline x}{S_{xx}}.
$$

The weights $c_i$ are non-random. They sum to $0$, and $\sum_i c_i x_i=1$. Taking expectations, $\mathbb{E}\widehat\beta_1=\sum_i c_i(\beta_0+\beta_1 x_i)=\beta_1$. Also $\mathbb{E}\overline Y=\beta_0+\beta_1\overline x$, so $\mathbb{E}\widehat\beta_0=\beta_0$. No shape is assumed for the errors, and a finite error variance is not required. Each coefficient is an [unbiased estimator](unbiased-estimator.qmd) as soon as the means lie on a straight line.

A variance needs more. Uncorrelated errors with common variance $\sigma^2$ give $\operatorname{Var}(\widehat\beta_1)=\sigma^2/S_{xx}$. Normality is what produces the $t$ reference distribution. If the true mean is $\beta_0+\beta_1 x_i+\beta_2 x_i^2$, these weights estimate $\beta_1+\beta_2\sum_i c_i x_i^2$, which biases $\widehat\beta_1$ whenever $\sum_i c_i x_i^2\neq 0$ (though it vanishes on a design symmetric about zero). When $\sigma^2>0$ and $\mathbb{E}\exp(\widehat\beta_1)$ is finite, strict convexity and Jensen's inequality give $\mathbb{E}\exp(\widehat\beta_1)>\exp(\beta_1)$, so $e^{\widehat\beta_1}$ is biased high for $e^{\beta_1}$.

## Weights on $x=0,1,3$

Here $\overline x=4/3$ and $S_{xx}=14/3$. The weights are $-2/7$, $-1/14$ and $5/14$. They sum to $0$, and their weighted sum against $(0,1,3)$ equals $1$. On the line $\beta_0=1$, $\beta_1=2$ the means are $1,3,7$, and the weighted sum of those means equals $2$.
""",
    "leave-one-out-cross-validation": r"""
## The $K$-fold procedure with a fold for every case

Leave-one-out cross-validation is $K$-fold cross-validation at $K=n$. For each index $i$, fit the classifier $\eta_{(X_{-i},y_{-i})}$ on the other $n-1$ cases and score it on the held-out pair $(x_i,y_i)$. The mismatch $Q$ equals $1$ when the prediction differs from $y_i$ and equals $0$ otherwise. The estimator averages those $n$ mismatches. The class-specific version restricts the average to the cases with $y_i=g$, dividing by the number of such cases rather than by $n$. Every observation is used once as a test case. The $n$ scores are strongly dependent, so the estimator can have high variance, while the target stays close to the error of the full-sample rule.

## Four held-out outcomes, and the contrast with resubstitution

Suppose the four left-out predictions give mismatches $1,1,0,0$. The leave-one-out estimate is $1/2$. If two of the cases belong to class $g$ and exactly one of those two mismatches equals $1$, the class-specific estimate is also $1/2$. For one-nearest neighbours with no distance ties, the apparent error is $0$, because each training point is its own nearest neighbour. The leave-one-out calculation deletes that point before the search, so the neighbour is a different training case and the mismatch can equal $1$. The two numbers estimate different targets. For a nearest-neighbour rule the refit is free: removing case $i$ means ignoring it in the distance ranking. Any tuning has to be repeated inside each left-out fit.
""",
    "lebesgue-decomposition": r"""
## Three ways a probability can sit on the line

Not every law is either a list of point masses or a density. The Lebesgue decomposition splits an arbitrary probability on the real line into three canonical pieces, and the split is unique.

Let $\mu$ be a probability measure on the Borel sets of $\mathbb{R}$. There is a unique decomposition $\mu=\mu_{\mathrm{d}}+\mu_{\mathrm{ac}}+\mu_{\mathrm{s}}$ into non-negative measures summing to $\mu$, where $\mu_{\mathrm{d}}$ is discrete, $\mu_{\mathrm{ac}}$ is absolutely continuous, and $\mu_{\mathrm{s}}$ is singular continuous. The discrete part is a countable sum of atoms, $\mu_{\mathrm{d}}=\sum_k p_k\delta_{x_k}$. The absolutely continuous part has a density: $\mu_{\mathrm{ac}}(A)=\int_A f(x)\,\mathrm{d}x$ for some integrable $f\ge 0$. The singular continuous part has no atoms, yet it is concentrated on a Borel set of Lebesgue measure zero. The [distribution function](cumulative-distribution-function.qmd) shows the same split, as jumps, an integral of $f$, or a continuous increase on a set of length zero.

## A mixture one can compute, and a staircase one cannot

With probability $1/2$, draw a fair coin on $\{0,1\}$. With probability $1/2$, draw a uniform number on $(0,1)$. The discrete masses are $1/4$ at $0$ and $1/4$ at $1$. The density is $1/2$ on $(0,1)$. The singular continuous part is zero. A genuinely singular example is the Cantor distribution. Its distribution function, the devil's staircase, is constant on each interval removed in the middle-thirds construction, rises continuously from $0$ to $1$, and has derivative $0$ at almost every $x$. It is not the integral of its derivative, and it has no atoms. See [atoms](atom-of-a-distribution.qmd).
""",
    "lehmann-scheffe-theorem": r"""
## Only one unbiased function of a complete statistic

Several unbiased estimators of one target usually exist, and most of them use features of the sample that a sufficient statistic has discarded. Let $T$ be a [complete](complete-statistic.qmd) [sufficient statistic](sufficient-statistic.qmd), and suppose $\delta(T)$ is unbiased for a real target $g(\theta)$, so $\mathbb{E}_{\theta}[\delta(T)] = g(\theta)$ for every $\theta$. If $\delta^{\ast}(T)$ is any other unbiased estimator that is also a function of $T$, then $q(T) = \delta(T) - \delta^{\ast}(T)$ has mean zero at every $\theta$. Completeness forces $q(T) = 0$ almost surely. There is therefore at most one unbiased estimator based on $T$. That uniqueness is the first half of the Lehmann–Scheffé theorem (Lehmann and Scheffé, 1950).

## Rao–Blackwell supplies the minimum variance

The second half starts from an arbitrary [unbiased estimator](unbiased-estimator.qmd) $\delta_0(\boldsymbol{X})$ with finite variance $\operatorname{Var}_{\theta}(\delta_0)<\infty$, which may use the whole sample. The conditional expectation $\delta(T) = \mathbb{E}[\delta_0(\boldsymbol{X}) \mid T]$ is a function of $T$, remains unbiased, and satisfies $\operatorname{Var}_{\theta}(\delta_0) = \mathbb{E}_{\theta}[\operatorname{Var}(\delta_0 \mid T)] + \operatorname{Var}_{\theta}(\delta(T))$. The first term on the right is nonnegative, so $\delta(T)$ is at least as good as $\delta_0$ at every $\theta$ among unbiased estimators with finite variance. This is the [Rao–Blackwell theorem](rao-blackwell-theorem.qmd). Completeness says the improvement does not depend on which unbiased $\delta_0$ was chosen. Hence $\delta(T)$ is the unique [uniformly minimum-variance unbiased estimator](uniformly-minimum-variance-unbiased-estimator.qmd) of $g(\theta)$. For an iid Poisson sample the sample mean is that estimator of the mean. If completeness fails, two different functions of a minimal sufficient statistic can be unbiased for the same $g$, and this uniqueness is lost.
""",
    "levy-s-continuity-theorem": r"""
## When pointwise convergence of transforms is enough

Characteristic functions turn independent sums into products, so they are easy to compute along a sequence of approximations. Lévy's continuity theorem is the justification for passing from a pointwise limit of those transforms back to a limit of the distributions (Lévy, 1937).

Let $\varphi_{X_n}(t)=\mathbb{E} e^{itX_n}$. Suppose $\varphi_{X_n}(t)\to\varphi(t)$ for every real $t$, and suppose the limit $\varphi$ is continuous at $0$. Then $\varphi$ is the characteristic function of some probability law, and $X_n$ converges in distribution to that law: $F_{X_n}(x)\to F(x)$ at every continuity point of $F$. Continuity at $0$ stops mass from escaping to infinity. It is the tightness hidden in the transform. Without it, a pointwise limit need not be a characteristic function, and the distributions need not converge.

## A normal limit, and a sequence that escapes

If $Y_i$ are independent and identically distributed with mean $0$ and variance $1$, the characteristic function of $n^{-1/2}\sum_{i=1}^{n} Y_i$ tends to $e^{-t^2/2}$ at every $t$. The limit is continuous at $0$ and is the standard normal transform, so the [central limit theorem](central-limit-theorem.qmd) follows from this route. The hypothesis is not automatic. If $X_n$ is normal with mean $0$ and variance $n$, then $\varphi_{X_n}(t)=\exp(-nt^{2}/2)$ tends to $0$ for $t\neq 0$ and equals $1$ at $t=0$. The limit is discontinuous at $0$, and $X_n$ does not converge in distribution: the mass spreads without bound. Convergence of [characteristic functions](characteristic-functions.qmd) still does not give convergence of expectations. That needs [uniform integrability](uniform-integrability.qmd), a separate condition.
""",
    "likelihood-function": r"""
## The sample is fixed and the parameter moves

Once $x_1,\ldots,x_n$ have been observed, the joint density or mass function $f(x_1,\ldots,x_n;\theta)$ is no longer being used to spread probability over outcomes. As a function of $\theta$ it is the likelihood $L(\theta)$. For independent observations from a common density or mass function $f(x;\theta)$, this is a product, and the log-likelihood

$$
\ell(\theta)=\sum_{i=1}^n\log f(x_i;\theta)
$$

is a sum, up to any additive constant that does not depend on $\theta$. A multiplicative constant with no $\theta$ in it does not change ratios $L(\theta_1)/L(\theta_2)$ and does not move the maximiser. The binomial coefficient in a binomial likelihood is such a constant. The likelihood is not a probability distribution for $\theta$: nothing in the definition makes it integrate or sum to $1$ over the parameter space.

The ratio $L(\theta_1)/L(\theta_2)$ is the relative support for $\theta_1$ against $\theta_2$ on these data. [Maximum likelihood](maximum-likelihood.qmd) chooses a $\theta$ that maximises that support inside the family that was written down. If the family excludes the truth, the maximiser selects the best member of a family that is still wrong.

## Seven successes in ten trials

Suppose $X\sim\operatorname{Bin}(10,p)$ and the observation is $x=7$. Then $L(p)$ is proportional to $p^7(1-p)^3$ for $p\in(0,1)$. Comparing $p=0.7$ with $p=0.5$,

$$
\frac{L(0.7)}{L(0.5)}=\frac{0.7^{7}\times 0.3^{3}}{0.5^{10}}\approx 2.28.
$$

The observed count is a little more than twice as probable at $p=0.7$ as at $p=0.5$. The maximiser is $0.7$, the observed proportion. The numerical value of $L$ itself has no absolute scale; only the ratio does.
""",
    "linear-congruential-generator": r"""
## A deterministic loop of length at most $m$

A computer produces an apparently uniform stream from a short recursion. Choose a modulus $m$, a multiplier $a$ and an increment $c$, all positive integers, and a seed $X_0\in\{0,1,\ldots,m-1\}$. The states update by

$$
X_{i+1}=(aX_i+c)\bmod m,
$$

and the outputs are $U_i=X_i/m\in[0,1)$. The sequence is deterministic and periodic, and the period is at most $m$, because there are only $m$ possible states. With $c=0$ the generator is multiplicative, and the state $0$ is a fixed point, so a multiplicative generator must start from a nonzero seed.

A full period $m$, for every seed, holds if and only if three arithmetic conditions are met (Hull and Dobell, 1962): $c$ and $m$ are coprime, $a-1$ is divisible by every prime that divides $m$, and $a-1$ is divisible by $4$ whenever $m$ is divisible by $4$.

## Modulus eight, written out in full

Take $a=5$, $c=1$ and $m=8$. Then $\gcd(1,8)=1$ and $a-1=4$, so the criterion promises period $8$. From seed $1$ the states are $1,6,7,4,5,2,3,0$, and then $1$ again. The outputs are those integers over $8$. Successive pairs $(U_i,U_{i+1})$ lie on a handful of lines. A long period removes the obvious repetition and does not remove every lattice: a poor multiplier still drops consecutive blocks onto a coarse grid, which matters as soon as several outputs are used together. Anyone who knows $a$, $c$ and $m$ and sees a few states can continue the stream exactly. Recording the [seed](random-seed.qmd) makes the stream reproducible; it does not make it secret.
""",
    "linear-images-of-a-normal-vector": r"""
## Why full row rank keeps the output density nonsingular

Any linear combination of coordinates of a [multivariate normal](multivariate-normal-distribution.qmd) vector $\mathbf{X}\sim\operatorname{N}_p(\boldsymbol{\mu},\Sigma)$ stays normal, with mean $A\boldsymbol{\mu}$ and covariance $A\Sigma A^\top$ by linearity of expectation:

$$
\operatorname{Cov}(A\mathbf{X})=\mathbb{E}\bigl[A(\mathbf{X}-\boldsymbol{\mu})(\mathbf{X}-\boldsymbol{\mu})^\top A^\top\bigr]=A\Sigma A^\top.
$$

The rank condition separates a genuine $m$-dimensional density from a singular law. When $\Sigma$ is [positive definite](positive-definite-matrix.qmd) (rank $p$) and the $m\times p$ matrix $A$ has full row rank $m\le p$, for any non-zero $\mathbf{u}\in\mathbb{R}^m$ the transpose image $A^\top\mathbf{u}$ is non-zero in $\mathbb{R}^p$, so $\mathbf{u}^\top(A\Sigma A^\top)\mathbf{u}=(A^\top\mathbf{u})^\top\Sigma(A^\top\mathbf{u})>0$. Thus $A\Sigma A^\top$ is positive definite and $\mathbf{Y}=A\mathbf{X}$ has an ordinary $m$-variate normal density. Selecting a coordinate block with $A=(I_m\ \ 0)$ shows immediately that every marginal subvector of a multivariate normal is multivariate normal. Adding a shift $\mathbf{c}\in\mathbb{R}^m$ shifts the mean to $A\boldsymbol{\mu}+\mathbf{c}$ and leaves $A\Sigma A^\top$ unchanged; see [affine images of normal vectors](affine-images-of-normal-vectors.qmd).

## Sum and difference of two correlated normals, and a rank drop

Let $\mathbf{X}\sim\operatorname{N}_2\bigl((1,3)^\top,\bigl(\begin{smallmatrix}4&1\\1&2\end{smallmatrix}\bigr)\bigr)$ and take $A=\bigl(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr)$, which has rank $2$ and maps $(X_1,X_2)$ to $(X_1+X_2,\,X_1-X_2)$. Then $A\boldsymbol{\mu}=(4,-2)^\top$ and

$$
A\Sigma A^\top
=\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}4&1\\1&2\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
=\begin{pmatrix}8&2\\2&4\end{pmatrix},
$$

which has determinant $28>0$. If instead $m=3>p=2$, say by appending the row $(2,0)=(1,1)+(1,-1)$, then $\operatorname{rank}(A)=2<3$, the third coordinate equals the sum of the first two with probability $1$, and $A\Sigma A^\top$ is singular with no density on $\mathbb{R}^3$.
""",
    "linear-predictor": r"""
## Where the covariates actually enter

The random component says how the response scatters. The link says which means are legal. The linear predictor is the piece the explanatory variables build. With the covariates of unit $i$ stacked in a vector $\mathbf{x}_i$, including a $1$ for an intercept,

$$
\eta_i=\mathbf{x}_i^\top\boldsymbol{\beta}.
$$

Each entry of $\boldsymbol{\beta}$ multiplies a column you chose: a continuous measurement, an indicator for one level of a factor, or a product of two columns. The link then sets $g(\mu_i)=\eta_i$. Changing a covariate changes $\eta_i$ linearly even when the mean $\mu_i$ changes on a curve. That separation is the reason the same columns can sit under a log link, a logit link or an identity link. The meaning of a coefficient changes with the link. The construction of $\eta_i$ does not.

## A product column changes a slope

Take $\eta=1+0.2x-0.4z+0.1xz$. At $(x,z)=(2,1)$ the predictor equals $1.2$. The slope in $x$, holding $z$ fixed, is $0.2+0.1z$: it equals $0.2$ when $z=0$ and $0.3$ when $z=1$. Without the product column that slope cannot depend on $z$. The product is an [interaction](interaction.qmd), and it is still inside a linear predictor, because $\eta$ is linear in the parameters once the column $xz$ has been built. Factor coding is the same idea. An indicator that equals $1$ for treatment B and $0$ for treatment A makes its coefficient the contrast of B with A. Which level is coded $0$ is a constraint that keeps the columns from being collinear. It is not a number the responses estimate.
""",
    "link-function": r"""
## From an unrestricted predictor to a legal mean

A linear predictor $\eta=\mathbf{x}^\top\boldsymbol{\beta}$ can be any real number. The mean often cannot. A probability lies in $(0,1)$, and the mean of a count or of a positive continuous response has to stay positive. The link $g$ is the function you invert to enforce that constraint: $g(\mu)=\eta$, so $\mu=g^{-1}(\eta)$. It is chosen as part of the model. It is not a regression coefficient. Three ordinary choices are the identity $\mu=\eta$, the log $\mu=\exp(\eta)$, and the logit $\mu=\exp(\eta)/\{1+\exp(\eta)\}$. The same three numbers $\eta=-0.5$, $0$ and $1$ become three different means. The identity returns $-0.5$, $0$ and $1$, legal for an unrestricted mean and illegal for a probability. The log returns about $0.61$, $1$ and $2.72$, always positive. The logit returns about $0.38$, $0.50$ and $0.73$, always inside $(0,1)$.

## Canonical is convenient, not compulsory

In a one-parameter exponential family the canonical link makes the natural parameter equal to $\eta$. For the normal, Poisson and binomial families it is the identity, the log and the logit. A non-canonical link is still allowed. Gamma means are often given a log link rather than the canonical inverse, because the log cannot leave the positive half-line. Two links on the same responses are not nested models, so a likelihood-ratio comparison does not choose between them. [AIC](akaike-information-criterion.qmd) can, if the random component is held fixed and only $g$ changes. A link that fits a little better inside the sample can still give absurd predictions just outside it. The check is the fitted mean at the edge of the observed covariates.
""",
    "little-s-law": r"""
## Headcount equals arrival rate times time spent

In a stable queue one can relate three averages without solving the balance equations. If customers arrive steadily and each spends a typical time in the system, the typical number present is the product of those two quantities. Little's law is that accounting identity (Little, 1961).

In a stable system, $L=\lambda_{\mathrm{eff}} W$. Here $L$ is the mean number of customers in the system, the time average of the count. The number $W$ is the mean sojourn time of those customers, from arrival to departure. The rate $\lambda_{\mathrm{eff}}$ is the mean arrival rate of the customers who are actually counted in $L$. The identity does not require exponential service, a single server, or a Markov description. The three quantities have to describe one and the same population.

## Match the population, then check M/M/1

For the whole system, $W$ includes service and $\lambda_{\mathrm{eff}}$ is the rate of accepted arrivals. For the waiting line only, the companion identity is $L_q=\lambda_{\mathrm{eff}} W_q$, using the mean queue length and the mean wait before service. Mixing $L_q$ with the total sojourn pairs two different groups. In a blocking system the offered rate $\lambda$ counts people who never enter. [Throughput](throughput.qmd) $\lambda(1-\pi_K)$ is the rate Little's law wants.

Take an M/M/1 queue with $\lambda=3$ and $\mu=5$, so $\rho=0.6<1$. The mean number present is $L=\rho/(1-\rho)=1.5$. Then $W=L/\lambda=0.5$, which agrees with $1/(\mu-\lambda)=1/2$. Three arrivals an hour, each staying half an hour, produce an average headcount of $1.5$. The same arithmetic is the check on any [birth–death](birth-death-balance.qmd) formula for $L$.
""",
    "lloyd-s-k-means-algorithm": r"""
## Assign to the nearest centre, then replace centres by means

$K$-means seeks centres $m_1,\ldots,m_K$ in $\mathbb{R}^p$ and a labelling $C$ that make the within-cluster sum of squares $\sum_i\lVert x_i-m_{C(i)}\rVert^2$ small. Lloyd's iteration alternates two exact minimisations. Given the centres, set $C(i)$ to a minimiser of $\lVert x_i-m_k\rVert^2$ over $k$; ties may be given to the smallest index. Given the labels, replace $m_k$ by the mean of $\{x_i:C(i)=k\}$, which is the unique minimiser of that cluster's sum of squares when the cluster is nonempty. The loop stops when the labelling no longer changes. Each full pass holds $\widetilde W$ at the same value or lowers it, but the terminal labelling depends on the start and need not be a global minimiser.

## A one-dimensional run from centres $0$ and $3$

On the points $0,2,3,10$, the centres $0$ and $3$ produce the labelling $\{0\}$ against $\{2,3,10\}$, with $\widetilde W=50$. The means $0$ and $5$ produce $\{0,2\}$ against $\{3,10\}$, with $\widetilde W=33$. The means $1$ and $6.5$ produce $\{0,2,3\}$ against $\{10\}$, with $\widetilde W=18.25$. The means $5/3$ and $10$ leave that labelling unchanged and lower the criterion to $14/3\approx 4.667$. The same data with a different legal start can pass through other labellings, and in higher dimension two starts can stop at different values. Standardising the coordinates before the run matters because the Euclidean norm treats a unit gap in every coordinate as comparable. The integer $K$ is an input. The criterion falls as $K$ increases and hits zero at $K=n$, so it cannot by itself choose the number of centres.
""",
    "loadings": r"""
## Entries of a unit principal direction

A principal component direction is a unit-length eigenvector of the covariance or correlation matrix used in the analysis. The loadings of that component are the entries of this unit vector. If $a=(a_1,\ldots,a_p)^\top$ is the direction, the score of a centred, and possibly scaled, row $z$ is $a^\top z=\sum_j a_j z_j$. A large $|a_j|$ means that coordinate $j$ moves the score strongly. The sign of the whole vector is arbitrary: $a$ and $-a$ span the same line, carry the same variance, and reverse only the sign of every score. When the analysis is of the correlation matrix, the variables were standardised first, so a loading is a weight on a unit-variance coordinate. The correlation between standardised variable $j$ and the score is then $a_j\sqrt{\lambda}$, where $\lambda=a^\top R a$ is the component's variance. That correlation is sometimes also called a loading; the unit-vector entries are the coefficients meant here.

## Two standardised variables with correlation $0.6$

The correlation matrix $R=\begin{pmatrix}1&0.6\\0.6&1\end{pmatrix}$ has eigenvalues $1.6$ and $0.4$, because the characteristic equation is $\lambda^2-2\lambda+0.64=0$. The leading unit eigenvector may be taken as $(1/\sqrt{2},\,1/\sqrt{2})^\top\approx(0.707,0.707)^\top$. Both loadings are equal, and the first component accounts for $1.6/2=0.80$ of the total standardised variance. Each variable's correlation with the score is $\sqrt{0.8}\approx 0.894$. Flipping the vector to $(-0.707,-0.707)^\top$ leaves the variance unchanged after a sign flip of the scores. The second eigenvalue $0.4$ is the remainder of the trace.
""",
    "local-balance": r"""
## One neighbouring cut at a time

Global balance at a state equates every transition into that state with every transition out. On a birth–death chain the graph is a path, so the only way probability can move past $n$ is across the single edge to $n+1$. Local balance is that one-edge equation, and iterating it produces the stationary weights.

Let $\lambda_n$ be the birth rate in state $n$ and $\mu_{n+1}$ the death rate in state $n+1$. Local balance sets

$$
\pi_n\lambda_n=\pi_{n+1}\mu_{n+1},
$$

which rearranges to $\pi_{n+1}=\pi_n\lambda_n/\mu_{n+1}$. This is [detailed balance](detailed-balance.qmd) for a chain that steps by at most one. Starting from $\pi_0$ and unfolding the recurrence gives $\pi_n$ as $\pi_0$ times $\prod_{k=0}^{n-1}\lambda_k/\mu_{k+1}$. The weights form a probability when the sum over $n$ is finite. A formal solution with infinite total mass is an invariant measure, not a stationary distribution.

## Two machines and one repairer

Let $n$ be the number of failed machines among two. Operating machines fail at rate $1$ each, and one repairer works at rate $1$. Then $\lambda_0=2$, $\lambda_1=1$, $\lambda_2=0$, and $\mu_1=\mu_2=1$. The unnormalised weights are $1$, then $\lambda_0/\mu_1=2$, then $2\cdot\lambda_1/\mu_2=2$. They sum to $5$, so $\pi=(1/5,2/5,2/5)$. The first cut checks: $\pi_0\lambda_0=(1/5)\cdot 2=2/5$ and $\pi_1\mu_1=2/5$. The second cut checks the same way. Because the state space is finite the sum cannot diverge, and a stationary distribution exists at every positive failure and repair rate. On an infinite path the same arithmetic may produce weights that cannot be normalised, which is the instability condition for the [birth–death balance](birth-death-balance.qmd).
""",
    "local-minima-plateaus-and-symmetry": r"""
## Plateaus and local minima

Training a multilayer network means choosing weights that make a loss on the observed input–output pairs small. A nonlinear [activation](activation-function.qmd) makes that loss a nonconvex function of the weights. Gradient descent can enter a local minimum, creep across a plateau on which every partial derivative is nearly zero, or pass a saddle that curves upwards in some directions and downwards in others. The loss at the stopping point can be far above the loss reached from another initialisation. Several random starts, scored on held-out pairs, show when a run has settled in a poor basin.

## Copies of the same function

A [hidden layer](hidden-layer.qmd) of $\ell$ units with a shared activation can be relabelled without changing the represented function. Move each unit's incoming weights, bias and outgoing weights together. When all units differ there are $\ell!$ copies; coincident units produce fewer. For $\ell=3$ the count is $6$. Deterministic [gradient descent](gradient-descent.qmd) preserves equality. Two units that start with the same bias and the same incoming and outgoing weights receive the same gradient and remain clones, so one of them never specialises. Independent random initial weights break the tie.

The logistic [sigmoid](sigmoid-function.qmd) adds a sign symmetry, because $g(-u)=1-g(u)$. Flip the sign of one unit's incoming weights and bias, and its output $h$ becomes $1-h$. The next layer undoes that flip: replace the outgoing weight $w$ by $-w$ and add $w$ to the next bias. The function is unchanged, so distinct parameter vectors compute the same map and different initialisations can settle at different copies, though a single run of gradient descent stays in one basin rather than jumping between discrete sign flips.
""",
    "log-link": r"""
## Every coefficient multiplies the mean

Counts and positive continuous measurements need a positive mean for every covariate pattern, including patterns that were not observed. The log link $g(\mu)=\log\mu$ guarantees that: $\mu=\exp(\eta)$ is positive for every real linear predictor $\eta$. It is the canonical link for the Poisson and the usual link for a gamma mean. Add one unit to a covariate with coefficient $\beta_j$, hold the other covariates fixed, and the mean is multiplied by $e^{\beta_j}$. A coefficient of $\log 2\approx 0.693$ doubles the mean. A coefficient of $-0.693$ halves it. The arithmetic happens on the log scale. The sentence to report is the factor $e^{\beta_j}$, or the percentage change $100(e^{\beta_j}-1)$.

## Unequal exposure, and a small unit

Four events in $2$ years and four events in $8$ years are the same count and not the same rate: their observed rates are $2$ and $0.5$ per year. An offset puts the exposure in the predictor, $\log\mu_i=\mathbf{x}_i^\top\boldsymbol{\beta}+\log t_i$, which means $\mu_i=t_i\exp(\mathbf{x}_i^\top\boldsymbol{\beta})$. Two series that share $\mathbf{x}$ then share the model rate $\exp(\mathbf{x}_i^\top\boldsymbol{\beta})$, with expected counts proportional to their exposures. Dropping $\log t_i$ analyses the counts as if every unit had been watched for the same time. The intercept $\exp(\beta_0)$ is the mean at the baseline covariate and at exposure $1$. If that baseline is not a real situation, it is not a typical rate. A small coefficient can also be a large effect written per small unit. A slope of $0.01$ per kilometre is a slope of $1$ per hundred kilometres, and $e^{1}\approx 2.7$ rather than $e^{0.01}\approx 1.01$.
""",
    "log-partition-moment-identities": r"""
## Differentiating the normaliser

An [exponential family](exponential-family.qmd) density may be written

$$
p(x \mid \theta) = b(x)\exp\{c(\theta)^{\mathsf{T}} T(x)\} / a(\theta),
$$

where $c(\theta)$ is the [natural parameter](natural-parameter.qmd), $T(x)$ the natural statistic, $b(x)$ does not depend on $\theta$, and $a(\theta)$ normalises the density. In the continuous case $a(\theta) = \int b(x)\exp\{c^{\mathsf{T}} T(x)\} \,\mathrm{d}x$, and the integral is a sum if $x$ is discrete. Treat $c = c(\theta)$ as the coordinate, and assume differentiation under the integral is valid. Differentiating the identity $\int p(x \mid \theta) \,\mathrm{d}x = 1$ in $c$ produces $\nabla_c \log a(\theta) = \mathbb{E}_{\theta}[T(X)]$. One further derivative separates $\mathbb{E}[T T^{\mathsf{T}}]$ from the squared mean, so the Hessian equals $\operatorname{Cov}_{\theta}[T(X)]$. A covariance matrix is positive semi-definite, hence $\log a$ is convex in $c$, and strictly convex when that covariance is positive definite.

## The same Hessian is the information

The Hessian is the [Fisher information](fisher-information.qmd) for one observation in the natural parameter: the score is $T(X) - \mathbb{E}[T(X)]$, and the information is the covariance of the score. For $n$ iid observations the sufficient statistic is $S = \sum_{i=1}^{n} T(X_i)$. The log-likelihood is $c^{\mathsf{T}} S - n \log a(\theta)$ plus a term free of $\theta$, and the information is $n$ times the Hessian. Setting the score to zero matches the observed sufficient statistic to its expectation, $S(\boldsymbol{x}) = n\, \mathbb{E}_{\widehat{\theta}}[T(X)]$. The mean, the covariance, convexity, and the information are four readings of one function, $\log a$.
""",
    "logit-link": r"""
## Log odds, defined on the whole real line

A binary response has mean $p=\mathbb{P}(Y=1\mid\mathbf{x})$, and $p$ must lie in $(0,1)$. A straight line in the covariates will eventually leave that interval. The logit link maps the interval onto the whole line,

$$
g(p)=\log\frac{p}{1-p}=\mathbf{x}^\top\boldsymbol{\beta},
$$

and inverts as $p=\exp(\eta)/\{1+\exp(\eta)\}$ with $\eta=\mathbf{x}^\top\boldsymbol{\beta}$. The ratio $p/(1-p)$ is the odds. The link is canonical for the binomial, and it is symmetric about one half: $g(1-p)=-g(p)$, so $g(1/2)=0$. A coefficient $\beta_j$ is the change in the log odds for a one-unit change in that covariate. Equivalently, the odds are multiplied by $e^{\beta_j}$. That factor is an [odds ratio](odds-ratio.qmd), not a ratio of probabilities.

## Doubling the odds does not double the probability

Start at $p=0.2$. The odds are $0.25$ and the logit is $\log 0.25\approx -1.386$. Add $\log 2\approx 0.693$. The new logit is about $-0.693$, the new odds are $0.5$, and the new probability is $0.5/1.5=1/3$. The odds have doubled. The probability has moved from $0.20$ to about $0.33$. The same doubling near $p=0.5$ would move the probability by a different amount, so an odds ratio cannot be quoted in percentage points without a baseline. Complete separation breaks the fit in a particular way. If every success has a larger covariate than every failure, the maximised slope is infinite and the fitted probabilities are driven to $0$ and $1$. The data then determine a direction, not a finite coefficient.
""",
    "m-m-queue": r"""
## A server for every arrival

With infinitely many servers, nobody waits. Every customer begins service on arrival, and the departure rate grows in proportion to the number already present. The modelling question is the long-run number of busy servers, and there is no critical load at which that number runs away.

Arrivals are Poisson of rate $\lambda>0$. Service times are independent exponentials of rate $\mu>0$. In state $n$ there are $n$ services in progress, so the birth rate is $\lambda_n=\lambda$ and the death rate is $\mu_n=n\mu$. [Local balance](local-balance.qmd) gives

$$
\pi_n=\pi_0\frac{(\lambda/\mu)^n}{n!}.
$$

The exponential series sums to $e^{\lambda/\mu}$, hence $\pi_0=e^{-\lambda/\mu}$, and the stationary number in system is Poisson with mean $\lambda/\mu$. The mean service rate $n\mu$ grows without bound as $n$ grows, so the birth–death weights are summable for every $\lambda>0$ and $\mu>0$. There is no finite-server threshold analogous to $\lambda<\mu$ for one server.

## The mean sojourn is just the mean service

Take $\lambda=10$ customers per hour and $\mu=5$ per hour, so a typical service lasts $0.2$ hours. The stationary mean number present is $\lambda/\mu=2$. Then $\mathbb{P}(N=0)=e^{-2}\approx 0.135$. The Poisson$(2)$ probabilities up through $4$ sum to about $0.947$, so $\mathbb{P}(N\ge 5)\approx 0.053$. Five or more customers are present only about $5\%$ of the time. [Little's law](little-s-law.qmd) gives mean time in system $W=(2)/10=0.2$, which equals $1/\mu$. Nobody waits, so sojourn and service coincide. The same arrival and service rates with one server would have $\rho=2>1$ and no stationary distribution. Infinite capacity removes that threshold. Compare the [M/M/1 queue](m-m-1-queue.qmd).
""",
    "main-effect": r"""
## An average contrast, taken over the other factor

With two factors, the mean at level $i$ of the first and level $j$ of the second can be written $\mu_{ij}=\mu+\alpha_i+\beta_j+\gamma_{ij}$. The terms $\alpha_i$ and $\beta_j$ are the main effects. The term $\gamma_{ij}$ is the [interaction](interaction.qmd): the amount by which the contrast for one factor changes with the level of the other. A main effect averages a contrast over the levels of the other factor. If every interaction is zero, that average is also the contrast at each level, and the main-effect sentence is enough. If the interaction is not zero, the average can cancel a reversal.

## Equal averages and opposite winners

Suppose the yields are $8$ and $14$ for varieties A and B under low water, and $18$ and $12$ under high water. Both variety averages equal $13$, so a main-effect comparison says the varieties do not differ. Under low water, B beats A by $6$. Under high water, A beats B by $6$. The interaction is the result. Coding constraints add a second trap. Setting the first level of each factor to zero makes the reported coefficient of B equal to the contrast at the baseline level of water, not the average over water. With low water as that baseline the coefficient is $14-8=6$, even though the marginal contrast is $0$. Quoted as "the effect of variety", it silently conditions on the baseline. With the interaction kept in the model, each simple contrast has to name the level of the other factor.
""",
    "marginal-hyperposterior": r"""
## Integrate one beta–binomial study at a time

Let study $j = 1,\ldots,J$ report $y_j$ successes in $n_j$ trials, with $y_j \mid \theta_j \sim \operatorname{Binomial}(n_j, \theta_j)$ and with studies conditionally independent given the rates. Take $\theta_j \mid \alpha, \beta \sim \operatorname{Beta}(\alpha, \beta)$ independently, and let $(\alpha, \beta)$ have hyperprior density $p(\alpha, \beta)$ on $(0,\infty)^2$. The joint posterior is proportional to $p(\alpha, \beta)$ times $\prod_j p(y_j \mid \theta_j)\, p(\theta_j \mid \alpha, \beta)$. The binomial factor contributes $\theta_j^{y_j}(1-\theta_j)^{n_j-y_j}$, and the beta density contributes $\Gamma(\alpha+\beta)/(\Gamma(\alpha)\Gamma(\beta))$ times $\theta_j^{\alpha-1}(1-\theta_j)^{\beta-1}$. The product is a beta kernel in $\theta_j$. Integrating $\theta_j$ from $0$ to $1$ replaces that kernel by the beta function $B(y_j+\alpha, n_j-y_j+\beta)$, which is $\Gamma(y_j+\alpha)\Gamma(n_j-y_j+\beta)/\Gamma(n_j+\alpha+\beta)$.

## A pointwise kernel, not a named density

Repeating the integral for every study leaves

$$
p(\alpha,\beta \mid \boldsymbol{y}) \propto p(\alpha,\beta) \prod_{j=1}^{J} \frac{\Gamma(\alpha+\beta)\, \Gamma(y_j+\alpha)\, \Gamma(n_j-y_j+\beta)}{\Gamma(\alpha)\, \Gamma(\beta)\, \Gamma(n_j+\alpha+\beta)}.
$$

The binomial coefficient $\binom{n_j}{y_j}$ multiplies the marginal likelihood of study $j$, but it does not depend on $(\alpha, \beta)$, so it cancels once this [kernel](kernel-of-a-density.qmd) is normalised. Log-gamma functions evaluate the product at any particular $(\alpha, \beta)$. The product is not the kernel of a named distribution on the positive quadrant. Posterior means and probabilities for the [hyperparameters](hyperparameter.qmd) need a numerical normalising constant, such as a grid that includes the Jacobian of the coordinates in which the grid is drawn. Treating the displayed weight as if it were already a probability skips that constant.
""",
    "markov-random-field": r"""
## Conditional independence from a missing edge

Several measurements are taken on the same unit, and the question is which pairs still move together after the others are taken into account. An undirected [graph](undirected-graph.qmd) records the answer. Each vertex is a random variable. A missing edge between $j$ and $k$ means

$$
X_j \perp X_k \mid \{X_r: r\neq j,k\}.
$$

That pairwise statement is one Markov property of the joint law. A stronger, global property says that a [separating set](separating-set.qmd) of vertices blocks every path, and the variables on the two sides are conditionally independent given the separator. The [Hammersley–Clifford](hammersley-clifford.qmd) correspondence equates these independence statements with a factorisation into clique potentials when the density is positive. Zeros in the support can separate the two descriptions.

## A three-variable chain

Take vertices $\{1,2,3\}$ and edges $\{1,2\}$ and $\{2,3\}$ only. The missing edge says $X_1 \perp X_3 \mid X_2$. The pair $(X_1,X_3)$ can still be marginally dependent, because both track $X_2$. A Gaussian law makes the same graph visible in the [precision matrix](precision-matrix.qmd): the $(1,3)$ entry is zero, while the marginal correlation of $X_1$ and $X_3$ need not be. The field is a property of the joint distribution and the graph together. Drawing the graph does not by itself estimate the potentials.
""",
    "markov-s-inequality": r"""
## A tail bound that spends only the mean

With nothing but a mean, one can still cap the probability of a very large outcome. The bound is often loose, and it is the starting point for sharper inequalities that spend a variance or a higher moment.

Let $X$ be a non-negative random variable and let $a>0$. On the event $\{X\ge a\}$ one has $X\ge a$, and elsewhere the contribution can be dropped, so $X\ge a\,1_{\{X\ge a\}}$. Taking expectations yields $a\mathbb{P}(X\ge a)\le\mathbb{E} X$, hence

$$
\mathbb{P}(X\ge a)\le\frac{\mathbb{E} X}{a}.
$$

No variance, independence, or shape assumption enters. If $a\le\mathbb{E} X$ the right-hand side is at least $1$ and the bound says nothing. If $\mathbb{E} X=\infty$ the inequality is not available. Applied to $(X-\mathbb{E} X)^{2}$ at level $\varepsilon^{2}$, the same argument is [Chebyshev's inequality](chebyshev-s-inequality.qmd): $\mathbb{P}(|X-\mathbb{E} X|\ge\varepsilon)\le\operatorname{Var}(X)/\varepsilon^{2}$.

## Sharpness, and a job that might run long

The bound is sharp. If $X=a$ with probability $p$ and $X=0$ otherwise, then $\mathbb{E} X=ap$ and $\mathbb{P}(X\ge a)=p$, so equality holds. For a non-negative job time with mean $10$ minutes, $\mathbb{P}(X\ge 60)\le 10/60=1/6$. If one also knows $\operatorname{Var}(X)=25$, Chebyshev gives $\mathbb{P}(X\ge 60)\le 25/50^{2}=0.01$, which is much smaller, but it spends a second moment Markov never sees. A Pareto tail with index $\alpha$ satisfying $1<\alpha\le 2$ has a finite mean and an infinite variance: Markov still applies, and Chebyshev does not. The inequality is also the step from an $L^{p}$ bound to [convergence in probability](modes-of-convergence.qmd).
""",
    "maximum-likelihood-for-a-binomial-proportion": r"""
## The interior maximum is the sample proportion

A binomial count $X\sim\operatorname{Bin}(n,p)$ records the number of successes in $n$ independent trials, with $n$ known and $p\in[0,1]$ unknown. After observing $X=x$, the [likelihood](likelihood-function.qmd) is $L(p)=\binom{n}{x}p^x(1-p)^{n-x}$. For $p\in(0,1)$ and $0<x<n$ the log-likelihood, up to a constant, is $\ell(p)=x\log p+(n-x)\log(1-p)$. Its derivative, the score, is

$$
\ell'(p)=\frac{x}{p}-\frac{n-x}{1-p}.
$$

Setting the score equal to $0$ gives $x(1-p)=(n-x)p$, hence $\widehat p=x/n$. The second derivative $-x/p^2-(n-x)/(1-p)^2$ is negative on $(0,1)$, so this critical point is a maximum. The [estimator](estimator.qmd) $X/n$ is unbiased for $p$, because $\mathbb{E} X=np$, and its variance is $p(1-p)/n$.

## No successes, or no failures

The score equation needs $x$ and $n-x$ both positive. If $x=0$, then $\ell(p)=n\log(1-p)$ on $(0,1)$, whose derivative $-n/(1-p)$ is always negative. The likelihood increases as $p$ falls, and the maximum on the closed interval $[0,1]$ is at the endpoint $p=0$. Likewise $x=n$ forces $\widehat p=1$. In both boundary cases $\widehat p=X/n$ is still the right maximiser, but it is not an interior critical point.

The usual plug-in standard error $\sqrt{\widehat p(1-\widehat p)/n}$ is then $0$, which would claim that $p$ is known exactly. The likelihood says otherwise. For $n=10$ and $x=0$, $L(p)=(1-p)^{10}$, and $L(0.1)/L(0)=0.9^{10}\approx 0.35$. A success probability of $0.1$ remains plainly compatible with ten failures. Wald intervals that use the collapsed standard error are not usable at the boundary.
""",
    "maximum-likelihood-for-a-known-graph": r"""
## Matching the sample covariance on the edges

Suppose $n$ independent rows are drawn from $\operatorname{N}_p(\boldsymbol{\mu},\Sigma)$ and the zero pattern of the precision $\Theta=\Sigma^{-1}$ is known. The profile Gaussian log-likelihood equals $\tfrac n2\log|\Theta|-\tfrac n2\operatorname{tr}(S\Theta)$ plus a constant, with $S$ the $1/n$ sample covariance, so it has the same maximiser as $\log|\Theta|-\operatorname{tr}(S\Theta)$ over precision matrices that respect those zeros and stay [positive definite](positive-definite-matrix.qmd). On an edge, and on the diagonal, the fitted covariance $W$ is pinned to $S$. On a missing edge, $W$ is whatever value the conditional-independence constraints imply. The sweep in the definition is block regression: the free coefficients of variable $j$ are the regression of that variable on its graph neighbours, and the missing-edge covariances are then filled in from those coefficients.

## One sweep on a chain

Let $p=3$, with edges only between $1$ and $2$ and between $2$ and $3$, and

$$
S=\begin{pmatrix}1&0.4&0.3\\0.4&1&0.5\\0.3&0.5&1\end{pmatrix}.
$$

Start at $W=S$. Variable $1$ has neighbour $2$ only, so the free slope is $\hat\beta^{*}=s_{12}/w_{22}=0.4$. The update replaces the non-edge entry $w_{13}$ by $\hat\beta^{*} w_{23}=0.2$. The sample value $0.3$ is discarded because no direct edge is allowed to carry it. On this chain that fill-in is already the fixed point, with zero in position $(1,3)$ of $\hat\Theta$, whereas a non-decomposable graph can need repeated sweeps before the edge-matching and zero constraints hold together. The iteration above assumes $S\succ 0$. A singular $S$ can still admit a constrained maximiser on a sparse graph, but the same inverses of neighbour blocks need a feasible start. An unknown graph is a different problem, handled by a penalty such as the [graphical lasso](graphical-lasso.qmd).
""",
    "maximum-likelihood-for-a-normal-sample": r"""
## Differentiating in $\sigma$ or in $\sigma^2$

For independent $X_i\sim\operatorname{N}(\mu,\sigma^2)$ the log-likelihood is a function of the sample only through $\sum_i(x_i-\mu)^2$ and $n$. Differentiating in $\mu$ and setting the derivative to zero shows that the maximiser is $\widehat\mu=\overline x$, whatever value $\sigma^2$ takes. Substituting that maximiser leaves a one-parameter problem in the variance. Treating $\sigma^2$ as the unknown parameter produces $\widehat\sigma^2=\frac1n\sum_i(x_i-\overline x)^2$.

The same point is the maximiser if the unknown parameter is the standard deviation $\sigma>0$ instead. With $\widehat\mu$ substituted, the profile log-likelihood in $\sigma$ is $-\,n\log\sigma-\frac1{2\sigma^2}\sum_i(x_i-\overline x)^2$, up to a constant. Its derivative is

$$
-\frac{n}{\sigma}+\frac1{\sigma^3}\sum_{i=1}^n(x_i-\overline x)^2.
$$

Setting that equal to zero again gives $\widehat\sigma^2$ equal to the average squared residual. This is the invariance of maximum likelihood under the reparameterisation $\sigma\mapsto\sigma^2$: the two recipes name the same number. Both divide by $n$, not by $n-1$. The unbiased sample variance $s^2$ uses $n-1$, and $\mathbb{E}\widehat\sigma^2=((n-1)/n)\sigma^2$, so the maximum likelihood estimator of the variance is biased low. The two estimators are functions of the same sufficient summary, $(\overline X,\sum_i(X_i-\overline X)^2)$.

## Three numbers

The observations $1,2,6$ have mean $3$ and residual sum of squares $14$. The maximum likelihood estimate of $\sigma^2$ is $14/3$. The unbiased estimate is $14/2=7$. The factor $(n-1)/n=2/3$ converts $7$ into $14/3$. At this sample size the choice of divisor is a large part of the answer. If the data are not normal, $\overline x$ and $14/3$ are maximum likelihood only for a normal working model, and a single outlier moves both.
""",
    "mean-vector-and-covariance-matrix": r"""
## What the two summaries carry

A single draw $\mathbf{X}=(X_1,\ldots,X_p)^\top$ is a list of measurements on one unit. The mean vector $\boldsymbol{\mu}$ stacks $\mathbb{E}(X_j)$. The covariance matrix $\Sigma$ stacks $\sigma_{jk}=\operatorname{Cov}(X_j,X_k)$. The diagonal entries $\sigma_{jj}=\sigma_j^2$ are ordinary [variances](variance.qmd). Off the diagonal, $\sigma_{jk}=\sigma_{kj}$, so $\Sigma$ is symmetric. For every fixed vector $\mathbf{a}$,

$$
\operatorname{Var}(\mathbf{a}^\top\mathbf{X})=\mathbf{a}^\top\Sigma\mathbf{a}\ge 0,
$$

which is the statement that $\Sigma$ is positive semi-definite. A positive-definite $\Sigma$ gives every nonzero linear combination a positive variance. The correlation $\rho_{jk}=\sigma_{jk}/(\sigma_j\sigma_k)$ removes the units of measurement; $\Sigma$ itself keeps them.

## A two-coordinate calculation

Take $\boldsymbol{\mu}=(1,3)^\top$ and

$$
\Sigma=\begin{pmatrix}4&2\\2&9\end{pmatrix}.
$$

Then $\rho_{12}=2/\sqrt{4\cdot 9}=1/3$. The contrast $X_1-X_2$ has variance

$$
(1,-1)\Sigma(1,-1)^\top=4+9-2\cdot 2=9.
$$

The same number is $\operatorname{Var}(X_1)+\operatorname{Var}(X_2)-2\operatorname{Cov}(X_1,X_2)$. Adding a constant to $\mathbf{X}$ changes $\boldsymbol{\mu}$ and leaves $\Sigma$ as it was. Multiplying $X_1$ by $10$ multiplies $\sigma_{11}$ by $100$ and $\sigma_{12}$ by $10$. Sample versions replace $\boldsymbol{\mu}$ by the sample mean and $\Sigma$ by a matrix of corrected products. The trace of $\Sigma$ equals $\sum_j\sigma_j^2$, and it equals the sum of the eigenvalues of $\Sigma$. Adding two independent copies of $\mathbf{X}$ produces a vector with covariance $2\Sigma$.
""",
    "measurable-random-variable": r"""
## Which real functions can carry probability

Probability is defined on events in a sigma-algebra $\mathcal{F}$. A numerical measurement $X$ can be discussed only when the sets one reads off $X$, such as $\{X\le x\}$, are events. That pullback condition is measurability.

Let $(\Omega,\mathcal{F},\mathbb{P})$ be a probability space. A map $X:\Omega\to\mathbb{R}$ is a random variable when $\{\omega:X(\omega)\le x\}\in\mathcal{F}$ for every real $x$. Equivalently, $\{X\in B\}\in\mathcal{F}$ for every Borel set $B$. The distribution function $F_X(x)=\mathbb{P}(X\le x)$ is then defined. It is non-decreasing and right-continuous, with limit $0$ at $-\infty$ and limit $1$ at $+\infty$. If some $\{X\le x\}$ failed to lie in $\mathcal{F}$, the symbol $\mathbb{P}(X\le x)$ would not refer to an event, and the integral that defines $\mathbb{E} X$ would not be an integral on this space.

## Coordinates are measurable, and a Vitali selector is not

Take $\Omega=(0,1)$ with the Borel sigma-algebra and Lebesgue measure, and set $X(\omega)=\omega$. Then $\{X\le x\}$ is an interval, hence Borel, so $X$ is a random variable and $F_X$ is the uniform distribution function. A continuous function of a random variable is a random variable, and so is a pointwise limit of random variables. Sums and products preserve measurability. A Vitali set, which picks one point from each equivalence class of reals that differ by a rational, is not Lebesgue measurable, and its indicator is a standard non-measurable function: $\{X\le 1/2\}$ cannot be given a translation-invariant, countably additive probability extending Lebesgue measure. Ordinary modelling stays inside the [Borel sigma-algebra](generated-and-borel-sigma-algebras.qmd), where these constructions do not arise. The resulting $F_X$ is the [distribution function](cumulative-distribution-function.qmd) of $X$.
""",
    "metropolis-algorithm": r"""
## Symmetry removes the proposal ratio

From the current state $x$, a Metropolis–Hastings step draws a candidate $y$ from a proposal density $q(y \mid x)$ and accepts it with probability

$$
a(x,y) = \min\left\{1, \frac{\pi(y)\, q(x \mid y)}{\pi(x)\, q(y \mid x)}\right\}.
$$

If $q(y \mid x) = q(x \mid y)$, the proposal ratio equals one and the acceptance probability is $\min\{1, \pi(y)/\pi(x)\}$. That symmetric case is the Metropolis algorithm (Metropolis et al., 1953). A random-walk proposal $y = x + z$, with the increment $z$ symmetric about zero, is the usual example. A normal increment depends on $y-x$ only through $(y-x)^2$, so swapping the two arguments does not change the density. Every move that increases $\pi$ is accepted. A move to a point with two-thirds of the current density is accepted with probability $2/3$. On rejection the chain records $x$ again.

## The normaliser cancels; an asymmetric proposal does not

Symmetry is not the same as a proposal that ignores the current state. An independent proposal $q(y \mid x) = g(y)$ still needs the Hastings factor $g(x)/g(y)$ unless $g$ itself is constant (Hastings, 1970). What does cancel for every proposal is a normalising constant in the target. If $\pi = f/Z$ with $Z$ unknown, then $\pi(y)/\pi(x) = f(y)/f(x)$. The ratio can therefore target an [Ising model](ising-model.qmd), whose partition function sums $2^m$ spin configurations, or a posterior whose marginal likelihood is intractable. In the symmetric case the acceptance probability uses that unnormalised target and no proposal correction.
""",
    "metropolis-hastings-invariance": r"""
## Acceptance restores pairwise balance

Let $\pi$ be a target density and $q(y \mid x)$ a proposal density that can be simulated. Define

$$
r(x,y) = \frac{\pi(y)\, q(x \mid y)}{\pi(x)\, q(y \mid x)}, \qquad a(x,y) = \min\{1, r(x,y)\},
$$

with $a(x,y) = 0$ when the denominator vanishes (Hastings, 1970). For $y \ne x$ the transition density is $q_{\mathrm{MH}}(y \mid x) = q(y \mid x)\, a(x,y)$. A rejected candidate is replaced by a copy of the current state. This kernel is in [detailed balance](stationarity-and-detailed-balance.qmd) with $\pi$. The reverse ratio satisfies $r(y,x) = 1/r(x,y)$. If $r(x,y) \le 1$, the forward move is accepted with probability $r(x,y)$ and the reverse move with probability one, and both sides of $\pi(x)\, q_{\mathrm{MH}}(y \mid x)$ equal $\pi(y)\, q(x \mid y)$. If $r(x,y) > 1$, the two roles are exchanged. The diagonal case $x = y$ is immediate because both sides carry the same state. Detailed balance implies that $\pi$ is stationary for the chain.

## Keep the rejection, and keep the proposal ratio

An unknown normaliser in $\pi = f/Z$ cancels between $\pi(y)$ and $\pi(x)$, so an unnormalised posterior kernel is enough. The proposal densities cancel only when $q$ is symmetric. Redrawing candidates until one is accepted deletes the stay-put step and divides by $A(x) = \int q(z \mid x)\, a(x,z) \,\mathrm{d}z$. The altered chain is in detailed balance with a density proportional to $\pi(x)A(x)$, not with $\pi$, and therefore targets the wrong distribution. Invariance of the genuine kernel is a property of the transition. Convergence from an arbitrary start still requires an ergodicity condition, and the proposal still determines how fast the autocorrelation dies.
""",
    "minimal-sufficiency": r"""
## The coarsest reduction that stays sufficient

The entire sample is always a [sufficient statistic](sufficient-statistic.qmd), because conditioning on every observation leaves nothing random. Sufficiency alone is not compression. A statistic $T$ is minimal sufficient when it is a function of every other sufficient statistic: any sufficient reduction can be reduced further to $T$ without losing sufficiency. For a dominated family whose support does not depend on $\theta$, the likelihood ratio is a practical test. The ratio $p(\boldsymbol{x} \mid \theta)/p(\boldsymbol{y} \mid \theta)$ does not depend on $\theta$ if and only if $T(\boldsymbol{x}) = T(\boldsymbol{y})$. Samples that the likelihood cannot separate are assigned the same value of $T$.

## A normal mean, read from the ratio

For iid $\operatorname{N}(\mu, \sigma^2)$ observations with $\sigma^2$ known,

$$
\frac{p(\boldsymbol{x} \mid \mu)}{p(\boldsymbol{y} \mid \mu)} = \exp\left\{ -\frac{\sum_i x_i^2 - \sum_i y_i^2}{2\sigma^2} + \frac{\mu}{\sigma^2}\left(\sum_i x_i - \sum_i y_i\right) \right\}.
$$

The first term in the exponent does not involve $\mu$. The second term is free of $\mu$ for every $\mu$ precisely when $\sum_i x_i = \sum_i y_i$. The sum, or equivalently the sample mean, is minimal sufficient for $\mu$. Keeping the whole vector adds nothing about $\mu$ inside this model. A [complete](complete-statistic.qmd) sufficient statistic is automatically minimal sufficient, because a nontrivial further reduction would yield a nonzero function of the complete statistic with mean zero. The converse is false: minimal sufficiency does not imply completeness, as iid draws from the uniform shift model $\operatorname{Uniform}(\theta,\theta+1)$ show—$(X_{(1)},X_{(n)})$ is minimal sufficient, yet the range $X_{(n)}-X_{(1)}$ is ancillary.
""",
    "missing-data": r"""
## Observed pairs and a complete-data story

A mixture density for a point $\mathbf{x}$ is a sum $\sum_h \pi_h f_h(\mathbf{x})$. The observed-data log-likelihood is the sum of logarithms of those sums, and the logarithm of a sum is awkward to maximise. Introduce a component label $Z$ that was never written down, with $\mathbb{P}(Z=h)=\pi_h$ and with $\mathbf{x}$ drawn from $f_h$ once $Z=h$. If $Z$ had been recorded, the [complete-data likelihood](complete-data-likelihood.qmd) would be a product of ordinary component densities times the weights, and for Gaussian components the maximiser would be a weighted mean, covariance and relative frequency inside each component. The label is missing in that precise sense: it is part of the statistical model, and the sampler did not retain it.

## Replacing the label by its conditional probability

The [E step](e-step.qmd) of the [EM algorithm](em-algorithm.qmd) fills the gap with the conditional distribution of $Z$ given $\mathbf{x}$. Suppose two components have weights $1/2$ and, at a point $x$, densities $f_1(x)=0.4$ and $f_2(x)=0.1$. The conditional probabilities are

$$
\tau_1=\frac{0.5\cdot 0.4}{0.5\cdot 0.4+0.5\cdot 0.1}=0.8,
\qquad
\tau_2=0.2.
$$

The M step then treats the point as $0.8$ of an observation from component $1$ and $0.2$ of an observation from component $2$. A value that was intended to be measured and was not, such as a dropped coordinate, is a different missingness mechanism. The same EM idea applies when the complete-data problem would have been easy, but the conditional distribution of the missing piece must match the mechanism that deleted it. Inventing a latent label and ignoring a coordinate that failed to record are different models.
""",
    "modes-of-convergence": r"""
## Four different things a limit can mean

Saying that $X_n$ tends to $X$ is ambiguous until the mode is named. A path can settle, a deviation can become unlikely, a moment of the error can vanish, or only the distribution functions can line up. These are not interchangeable.

Work on a common probability space, except for distributional convergence, which uses only the laws. Almost-sure convergence means $\mathbb{P}(\{\omega:X_n(\omega)\to X(\omega)\})=1$. Convergence in probability means $\mathbb{P}(|X_n-X|>\varepsilon)\to 0$ for every $\varepsilon>0$. Convergence in $L^{p}$, for $p\ge 1$, means $\mathbb{E}|X_n-X|^{p}\to 0$. Convergence in distribution means $F_{X_n}(x)\to F_X(x)$ at every continuity point of $F_X$. The chain of implications runs from $L^{p}$ to in-probability, by [Markov's inequality](markov-s-inequality.qmd) applied to $|X_n-X|^{p}$, and from almost sure to in-probability, and from in-probability to in-distribution. If the distributional limit is a constant, in-distribution upgrades to in-probability.

## A spike, and an independent copy

Let $U$ be uniform on $(0,1)$ and set $X_n=n\,1_{\{U\le 1/n\}}$. For each fixed $u>0$, eventually $1/n<u$, so $X_n\to 0$ almost surely. But $\mathbb{E} X_n=1$ for every $n$, so the convergence is not in $L^{1}$. Separately, let $X_n$ and $X$ be independent standard normals. Then $X_n$ converges in distribution to $X$, because every margin is standard normal, yet $\mathbb{P}(|X_n-X|>1)$ does not tend to $0$. Distributional convergence does not say that $X_n-X$ is small on a shared space. Expectations follow from distributional or almost-sure convergence only under an extra condition such as [uniform integrability](uniform-integrability.qmd).
""",
    "moment-generating-function": r"""
## Moments by differentiating under the expectation

The moment generating function $M(s)=\mathbb{E} e^{sX}$ packages every moment that exists into one function of a real argument $s$. It is defined only for those $s$ at which the expectation is finite. If that set contains an open interval around $0$, then $M$ determines the distribution of $X$, and the moments are derivatives at the origin: $M^{(k)}(0)=\mathbb{E} X^k$. In particular $\mathbb{E} X=M'(0)$ and $\operatorname{Var}(X)=M''(0)-\{M'(0)\}^2$. Differentiation under the expectation is legitimate inside that open interval.

Independent sums become products. If $X$ and $Y$ are independent and both moment generating functions exist at $s$, then $M_{X+Y}(s)=M_X(s)M_Y(s)$. That identity is the transform form of [convolution](convolution.qmd). A [count variable](probability-generating-function.qmd) with probability generating function $G$ has $M(s)=G(e^s)$ wherever the rewrite is finite.

## A Poisson mean and variance

If $X\sim\operatorname{Poisson}(\lambda)$ with $\lambda>0$, then $M(s)=\exp\{\lambda(e^s-1)\}$ for every real $s$. Differentiating the exponential gives $M'(s)=\lambda e^s M(s)$, so $M'(0)=\lambda$. One more derivative gives $M''(s)=\lambda e^s M(s)+(\lambda e^s)^2 M(s)$, so $M''(0)=\lambda+\lambda^2$ and the variance is $\lambda$. For $\lambda=2$ the mean is $2$ and $\mathbb{E} X^2=6$.

The device needs exponential moments. A [Cauchy variable](cauchy-distribution.qmd) has no mean, so it has no moment generating function on any neighbourhood of $0$. The characteristic function $\mathbb{E} e^{\mathrm{i} tX}$ exists for every real random variable, because the integrand has absolute value $1$, and it is the replacement when $M$ does not exist.
""",
    "moments-of-the-sample-mean-and-variance": r"""
## Mean and variance of the two basic summaries

Let $X_1,\ldots,X_n$ be a [random sample](random-sample.qmd): independent copies of a random variable with mean $\mu$ and finite variance $\sigma^2$. The sample mean is $\overline X=n^{-1}\sum_i X_i$. Linearity gives $\mathbb{E}\overline X=\mu$ with no further assumption. Independence removes the covariance terms in the variance of the sum, so

$$
\operatorname{Var}(\overline X)=\frac1{n^2}\sum_{i=1}^n\operatorname{Var}(X_i)=\frac{\sigma^2}{n}.
$$

The usual sample variance uses the divisor $n-1$,

$$
s^2=\frac1{n-1}\sum_{i=1}^n(X_i-\overline X)^2.
$$

The algebraic identity $\sum_i(X_i-\overline X)^2=\sum_i(X_i-\mu)^2-n(\overline X-\mu)^2$ is the reason the divisor is $n-1$. Take expectations. The first sum on the right has expectation $n\sigma^2$, and the second term has expectation $n\cdot\sigma^2/n=\sigma^2$, so the residual sum of squares has expectation $(n-1)\sigma^2$. Dividing by $n-1$ produces $\mathbb{E} s^2=\sigma^2$. Dividing by $n$ instead produces a statistic whose expectation is $((n-1)/n)\sigma^2$. None of these steps uses normality. They do use a finite variance. If $\sigma^2$ is infinite, $\operatorname{Var}(\overline X)$ and $\mathbb{E} s^2$ are not finite numbers of this form.

## The identity when $n=2$

For two observations, $s^2=(X_1-X_2)^2/2$. Then $\mathbb{E} s^2=\operatorname{Var}(X_1-X_2)/2$. Independence and equal variances give $\operatorname{Var}(X_1-X_2)=2\sigma^2$, so $\mathbb{E} s^2=\sigma^2$ again. A distribution on $\{-1,0,1\}$ with probabilities $1/4$, $1/2$ and $1/4$ has $\mu=0$ and $\sigma^2=1/2$, and the same two-observation calculation returns $\mathbb{E} s^2=1/2$. The sample mean of two draws then has variance $1/4$.
""",
    "monotone-convergence-fatou-and-dominated-convergence": r"""
## When a limit may pass inside the expectation

Pointwise convergence of random variables does not by itself justify $\mathbb{E} X_n\to\mathbb{E} X$. Three classical theorems give sufficient conditions. One uses monotone increase, one gives an inequality for non-negative variables, and one uses an integrable dominant.

If $0\le X_n\uparrow X$ almost surely, the monotone convergence theorem says $\mathbb{E} X_n\uparrow\mathbb{E} X$, and the common limit may be infinite. No dominant is required, because the sequence is increasing. If $X_n\ge 0$, Fatou's lemma says

$$
\mathbb{E}(\liminf_{n\to\infty} X_n)\le\liminf_{n\to\infty}\mathbb{E} X_n
$$

(Fatou, 1906). Expectations may drop in the limit. They cannot drop below the expectation of the liminf. If $X_n\to X$ almost surely and $|X_n|\le Y$ for every $n$, with $\mathbb{E} Y<\infty$, the dominated convergence theorem gives $\mathbb{E} X_n\to\mathbb{E} X$, and in fact $\mathbb{E}|X_n-X|\to 0$.

## The spike makes Fatou's inequality strict

Let $U$ be uniform on $(0,1)$ and set $X_n=n\,1_{\{U\le 1/n\}}$. Then $X_n\to 0$ almost surely and $\mathbb{E} X_n=1$, so $\mathbb{E}(\lim X_n)=0<1=\lim\mathbb{E} X_n$. Fatou's inequality holds and is strict. No integrable $Y$ dominates every $X_n$, since the peaks have height $n$. The same spike shows why domination cannot be omitted. Monotone convergence is the tool for sums of non-negative terms: if $Y_k\ge 0$, then $\mathbb{E}\sum_{k=1}^{\infty} Y_k=\sum_{k=1}^{\infty}\mathbb{E} Y_k$, even when both sides are infinite. That identity is what lets the expected total progeny of a subcritical [branching process](galton-watson-process.qmd) be summed generation by generation. [Uniform integrability](uniform-integrability.qmd) is the corresponding condition when convergence is only in probability.
""",
    "monotonicity-of-em": r"""
## Why an exact step cannot decrease the likelihood

Let $\ell(\Psi)$ be the observed-data log-likelihood and let $\ell_C(\Psi)$ be the complete-data log-likelihood, including the latent component labels. Write $k(Z\mid X,\Psi)$ for the conditional density of those labels. Taking the expectation under the conditional law at the current value $\Psi^{(k)}$ gives the identity

$$
\ell(\Psi)=Q(\Psi;\Psi^{(k)})-H(\Psi;\Psi^{(k)}),
$$

where $Q$ is the expected complete log-likelihood and $H(\Psi;\Psi^{(k)})=\mathbb{E}[\log k(Z\mid X,\Psi)\mid X,\Psi^{(k)}]$. The Gibbs inequality says that $H(\Psi;\Psi^{(k)})$ is largest at $\Psi=\Psi^{(k)}$. Therefore any candidate whose $Q$ is at least $Q(\Psi^{(k)};\Psi^{(k)})$ has $\ell(\Psi)\ge\ell(\Psi^{(k)})$. An exact M step maximises $Q$, so the observed log-likelihood does not fall (Dempster, Laird, and Rubin, 1977).

## A numerical gap, and what the inequality does not say

For a single two-class label with conditional probabilities $0.8$ and $0.2$,

$$
0.8\log 0.8+0.2\log 0.2\approx -0.500.
$$

Under the same $0.8,0.2$ weights, $\log(1/2)\approx -0.693$. The entropy term is lower at the uniform conditional law by about $0.193$ nats. If a candidate also raises $Q$ by $0.1$, the observed log-likelihood rises by at least $0.1$, and the entropy gap can add more. The argument needs a step that does not decrease $Q$: an exact M step does that, and so does a partial step that raises $Q$ (a generalised EM step). A constrained variance floor that pushes $Q$ below its current value, or a Monte Carlo error in $Q$, can break monotonicity. Convergence of the likelihood values needs an upper bound. Convergence of $\Psi$ needs further regularity: under the conditions studied by Wu (1983) the limit points are stationary, and a stationary point of a [mixture](finite-mixture-model.qmd) likelihood can be a poor local maximum or a singular component.
""",
    "multinomial-central-limit-theorem": r"""
## Proportions tightening around a fixed probability vector

Suppose one trial falls into one of $K$ categories with probability vector $\boldsymbol{p}$, where $p_k > 0$ and $\sum_k p_k = 1$. In $n$ independent trials the count vector $\boldsymbol{x}$ follows the [multinomial distribution](multinomial-distribution.qmd) with parameters $n$ and $\boldsymbol{p}$. Then $\mathbb{E}[\boldsymbol{x}] = n\boldsymbol{p}$ and

$$
\operatorname{Cov}(\boldsymbol{x}) = n\boldsymbol{\Sigma}(\boldsymbol{p}), \qquad \boldsymbol{\Sigma}(\boldsymbol{p}) = \operatorname{diag}(\boldsymbol{p}) - \boldsymbol{p}\boldsymbol{p}^{\mathsf{T}}.
$$

The sample proportion is $\widehat{\boldsymbol{p}} = \boldsymbol{x}/n$. For fixed interior $\boldsymbol{p}$, apply the central limit theorem to the $n$ iid category-indicator vectors. Then $\sqrt{n}\,(\widehat{\boldsymbol{p}} - \boldsymbol{p})$ converges in distribution to $\operatorname{N}_{K}(\boldsymbol{0}, \boldsymbol{\Sigma}(\boldsymbol{p}))$. The cloud of proportions concentrates about $\boldsymbol{p}$ at rate $n^{-1/2}$ and is approximately normal near $\boldsymbol{p}$. The limit is a repeated-sampling statement with $\boldsymbol{p}$ held fixed. It is not a posterior distribution for $\boldsymbol{p}$.

## A zero eigenvalue from the simplex

Let $\boldsymbol{1}$ denote the $K$-vector of ones. Then $\boldsymbol{p}^{\mathsf{T}}\boldsymbol{1} = 1$ and $\operatorname{diag}(\boldsymbol{p})\boldsymbol{1} = \boldsymbol{p}$, so $\boldsymbol{\Sigma}(\boldsymbol{p})\boldsymbol{1} = \boldsymbol{0}$. The structural eigenvalue $0$ belongs to the all-ones direction. Equivalently, every realised difference $\widehat{\boldsymbol{p}} - \boldsymbol{p}$ sums to zero and lies in a subspace of dimension $K-1$. A quadratic form in that difference, such as the Pearson statistic at a known $\boldsymbol{p}$, is asymptotically chi-squared on $K-1$ degrees of freedom, not $K$. Calculations on the simplex use a generalised inverse of $\boldsymbol{\Sigma}(\boldsymbol{p})$, because the ordinary inverse does not exist.
""",
    "multivariate-central-limit-theorem": r"""
## A normal approximation for the sample mean

Each observation is a vector $\mathbf{X}_i$ in $\mathbb{R}^p$ with mean $\boldsymbol{\mu}$ and covariance $\Sigma$. The sample mean $\overline{\mathbf{X}}_n$ is unbiased for $\boldsymbol{\mu}$ and has covariance $\Sigma/n$, by independence, whether or not the vectors are Gaussian. The theorem adds a shape: after multiplication by $\sqrt{n}$, the centred mean settles to $\operatorname{N}_p(\mathbf{0},\Sigma)$. Equivalently, for every fixed contrast $\mathbf{a}\neq\mathbf{0}$,

$$
\sqrt{n}\,\mathbf{a}^\top(\overline{\mathbf{X}}_n-\boldsymbol{\mu})
$$

is approximately univariate normal with variance $\mathbf{a}^\top\Sigma\mathbf{a}$. If $\Sigma$ is invertible, the quadratic form

$$
n(\overline{\mathbf{X}}_n-\boldsymbol{\mu})^\top\Sigma^{-1}(\overline{\mathbf{X}}_n-\boldsymbol{\mu})
$$

is approximately [chi-squared](chi-squared-distribution.qmd) on $p$ degrees of freedom. That limit is what turns a Wald statistic into a chi-squared test once $\Sigma$ is replaced by a consistent estimator.

## A numerical check, and when the limit is a poor guide

Take $p=2$, $\Sigma=I_2$, $n=100$ and $\overline{\mathbf{X}}_n=(0.2,-0.1)^\top$, with $\boldsymbol{\mu}=\mathbf{0}$. The quadratic form equals $100(0.04+0.01)=5$. A chi-squared variable on $2$ degrees of freedom exceeds $5$ with probability $e^{-2.5}\approx 0.082$. The same arithmetic with a heavy-tailed or strongly skewed coordinate can be misleading at this $n$, because the theorem is a limit, not a sample-size certificate. Finite variances are enough for the independent identically distributed case. They do not supply a moment-generating function, and they say nothing about a design in which $p$ grows with $n$. Replacing $\Sigma$ by a singular sample covariance is a separate failure: the quadratic form above is then undefined.
""",
    "nearest-neighbours": r"""
## A local vote

A query $x$ arrives with no label. Fix a distance, sort the [training set](training-set.qmd) by increasing distance from $x$, and let the $k$ closest points vote. The predicted class is the majority label. The same $k$ points also supply a soft estimate of the class probability: if $k=3$ and the labels are $1,1,2$, the hard prediction is class $1$ and the soft weight on class $1$ is $2/3$. With two classes, an odd $k$ avoids a tied vote when exactly $k$ points are used. Distance ties, and software that keeps every point tied at the $k$th distance, can still produce an even count, so the tie rule is part of the method.

## Neighbourhood size

Small $k$ follows local labels, including their noise. Large $k$ averages over a wider region and is pulled towards the majority class. At $k=n$ every query has the same neighbourhood, the whole sample, and the rule always returns the majority label. The apparent error on the training points favours $k=1$, because each training point is its own nearest neighbour and is classified correctly. [Cross-validation](cross-validation.qmd) on held-out points is what can prefer a larger neighbourhood.

Under the conditions of the [Cover–Hart bound](cover-hart-bound.qmd), the asymptotic risk of one neighbour is at most twice the Bayes risk (Cover and Hart, 1967). The distance itself is a modelling choice: multiplying one coordinate by $10$ can change which point is nearest, and a standardisation fitted on the training sample has to be reused, unchanged, on each query.
""",
    "nettalk": r"""
## From a window of letters to a pronunciation code

The learning problem is a map from written context to a pronunciation code. A window of seven characters is centred on the letter being pronounced, and the target is a code for that central letter (Sejnowski and Rosenberg, 1986). Each character is a [one-hot](one-hot-encoding.qmd) pattern. With $29$ symbols the window supplies $7\times 29=203$ binary inputs. The published network then uses $80$ [hidden units](hidden-layer.qmd) and $26$ outputs. Counting one bias on every hidden and output unit gives

$$
(203+1)\cdot 80+(80+1)\cdot 26=18426
$$

free weights. The count is the point of the example: connections accumulate as the product of layer widths, long before anyone has assessed how many of those weights the sample can support.

## A smaller count, and a penalty that does not travel

The same arithmetic on a toy net, with $15$ inputs, $2$ hidden units and $3$ outputs, gives $(15+1)\cdot 2+(2+1)\cdot 3=41$ weights. Training error can be driven down by using those weights to fit idiosyncrasies of the sampled words. [Weight decay](regularisation-and-weight-decay.qmd) adds a penalty $\lambda$ times a squared-weight term and pulls the weights towards zero (Krogh and Hertz, 1992). A value of $\lambda$ that worked on one pronunciation sample is a property of that sample, that architecture and that split. Reusing it on a new corpus, or on the $18426$-weight net, is a new modelling choice and needs its own held-out check.
""",
    "neyman-pearson-approach": r"""
## Size first, then power

The Neyman–Pearson approach controls one error and then optimises the other (Neyman and Pearson, 1933). The [type I error](type-i-and-type-ii-errors.qmd) is rejecting $H_0$ when $H_0$ is true. The type II error is failing to reject $H_0$ when the alternative is true. Fix a [significance level](significance-level.qmd) $\alpha$. Among [critical regions](critical-region.qmd) with type I error at most $\alpha$, choose one that minimises the type II error at the alternative of interest. That choice maximises power.

For a simple null $\theta=\theta_0$ against a simple alternative $\theta=\theta_1$, the region rejects when the [likelihood](likelihood-function.qmd) ratio $L(\theta_0)/L(\theta_1)$ is small enough that the type I error equals $\alpha$. The sample is then at least as probable under $\theta_1$, relative to $\theta_0$, as the likelihood-ratio threshold requires (though for a nearby alternative that ratio need only be slightly below $1$). This is the [Neyman–Pearson lemma](neyman-pearson-lemma.qmd). On a discrete distribution the size $\alpha$ may be unattainable unless the test randomises on the boundary where the ratio equals its threshold.

## Known normal variance

Let $X_1,\ldots,X_n$ be independent and $\operatorname{N}(\mu,1)$, and test $\mu=0$ against $\mu>0$. Every alternative $\mu_1>0$ produces the same region: reject for large $\overline X$. The level-$0.05$ test rejects when $\overline X>1.645/\sqrt{n}$. With $n=25$ the threshold is $0.329$. At $\mu=0.4$ the standard error of $\overline X$ is $0.2$, and the power is about $0.64$. The region does not depend on which positive $\mu_1$ was used, so the one-sided $z$ test is [uniformly most powerful](uniformly-most-powerful-test.qmd) against $\mu>0$. Against a two-sided alternative, the best region for a positive shift and the best region for a negative shift reject on opposite sides. No single region is most powerful against both.
""",
    "node-impurity": r"""
## A split is useful when the children are purer

At a node $m$ of a classification tree, $\hat p_{mg}$ is the proportion of the training cases in that node whose class is $g$. Impurity is a number that is zero at a pure node and positive when several classes share the node. Cross-entropy, the [Gini index](gini-index.qmd) and the misclassification rate are three such numbers. A candidate split sends a proportion $p_L$ of the cases left and $p_R=1-p_L$ right, and the reduction is the parent's impurity minus the weighted average of the children's impurities. The split with the largest reduction is the one the tree keeps. Changing the base of the logarithm multiplies every cross-entropy, and every cross-entropy reduction, by the same positive constant, so the winning split is unchanged.

## Where the three scores disagree

Take a parent with proportions $0.8$ and $0.2$. Its Gini index is $1-(0.8^2+0.2^2)=0.32$, its natural-log cross-entropy is about $0.500$, and its misclassification rate is $0.20$. Suppose an even split produces children with proportions $(0.7,0.3)$ and $(0.9,0.1)$. Both children still have majority class $1$, so the average misclassification rate is $0.5\cdot(0.3+0.1)=0.20$ and the misclassification reduction is zero. The average Gini index falls to $0.30$, a reduction of $0.02$. The average cross-entropy falls to about $0.468$, a reduction of about $0.032$. Gini and entropy can therefore prefer a split that does not yet change the majority label. Using the misclassification rate as a splitting criterion can refuse that split and produce a different tree.
""",
    "non-negative-matrix-factorisation": r"""
## Parts that add

A data matrix $X$ with $n$ rows and $p$ columns has every entry nonnegative: pixel intensities, word counts, or concentrations. A rank-$r$ approximation $X\approx WH$ is asked for, with $W$ an $n\times r$ matrix and $H$ an $r\times p$ matrix, and with every entry of $W$ and of $H$ nonnegative. Each column of $X$ is then a nonnegative combination of $r$ columns of $W$. Those columns behave as parts. They can add, and they cannot cancel, because a negative loading is forbidden. A principal-component reconstruction of the same matrix is free to write a large entry as a sum of a still larger loading and a negative correction. That cancellation can reduce squared error, and the factors are harder to read as parts (Lee and Seung, 1999).

## Scale, residual, and local fits

The factorisation is unchanged by replacing $W$ with $WC$ and $H$ with $C^{-1}H$ for a positive diagonal $C$: one factor absorbs the scale and the other gives it back. An exact rank-1 example is

$$
\begin{pmatrix}3&1\\6&2\end{pmatrix}
=
\begin{pmatrix}1\\2\end{pmatrix}
\begin{pmatrix}3&1\end{pmatrix}.
$$

The second row is twice the first, so one part, scaled by $1$ and by $2$, rebuilds both rows. If the bottom-left entry is changed from $6$ to $5$, that same product leaves a residual of $1$ in that cell and Frobenius squared error $1$. Alternating updates that minimise the error under the sign constraints can stop at different $(W,H)$ from different starts, because the joint criterion is not convex in the pair $(W,H)$.
""",
    "normal-linear-model": r"""
## Independent normal coordinates with a linear mean

Let $\mathbf{Y}$ be an $n$-dimensional response, let $A$ be a known $n\times p$ matrix of full column rank $p$, let $\boldsymbol\beta\in\mathbb{R}^p$ be an unknown coefficient vector, and let $\sigma^2>0$. The normal linear model says

$$
\mathbf{Y}=A\boldsymbol\beta+\boldsymbol\varepsilon,\qquad\boldsymbol\varepsilon\sim\operatorname{N}(\mathbf{0},\sigma^2 I_n),
$$

where $I_n$ is the $n\times n$ identity. Equivalently, the coordinates of $\mathbf{Y}$ are independent, each has variance $\sigma^2$, and $\mathbb{E}\mathbf{Y}=A\boldsymbol\beta$. [Simple linear regression](simple-linear-regression.qmd) is the case $p=2$, with a column of ones and a column of the explanatory values.

Full rank makes $A^{\mathsf T}A$ invertible, so the least-squares estimator $\widehat{\boldsymbol\beta}=(A^{\mathsf T}A)^{-1}A^{\mathsf T}\mathbf{Y}$ is unique. It is unbiased for $\boldsymbol\beta$, and under this normal model it is also the maximum likelihood estimator. The squared length of $\mathbf{Y}-A\widehat{\boldsymbol\beta}$, divided by $\sigma^2$, is chi-squared on $n-p$ [degrees of freedom](degrees-of-freedom.qmd).

## A common mean, and a duplicated column

Three independent observations with one common mean have $n=3$ and $p=1$, and $A$ is a column of three ones. Then $\widehat\beta=\overline Y$, and the residual sum of squares has $3-1=2$ degrees of freedom. If a second column copies the first, the rank drops below $2$ and $A^{\mathsf T}A$ is singular. The two coefficients are not separately estimable, while the fitted mean vector can still be unique. Unbiasedness of least squares for a well specified mean $A\boldsymbol\beta$ does not need normality or equal variances. The covariance formula $\sigma^2(A^{\mathsf T}A)^{-1}$, and the $F$ tests built from it, do need $\operatorname{Var}(\boldsymbol\varepsilon)=\sigma^2 I_n$.
""",
    "normal-quantile-plot": r"""
## Sorted observations against normal scores

A histogram suggests skew only after a bin width has been chosen. A normal quantile plot asks the same question against a fixed reference. Sort the sample as $y_{(1)}\le\cdots\le y_{(n)}$ and plot $y_{(i)}$ against a standard [normal](normal-distribution.qmd) quantile. With plotting positions $(i-0.5)/n$, and with $\Phi$ the standard normal distribution function, the horizontal coordinate is $z_i=\Phi^{-1}((i-0.5)/n)$. If the sample is close to normal with mean $\mu$ and standard deviation $\sigma$, the points fall near the straight line $y=\mu+\sigma z$. The intercept estimates the mean and the slope estimates the standard deviation. A change of slope is only a change of scale. Curvature, not tilt, is the evidence against a normal shape.

## A right tail that leaves the line

For $n=5$ the positions $0.1,0.3,0.5,0.7,0.9$ have normal scores about $-1.28,-0.52,0,0.52,1.28$. A normal sample with mean $10$ and standard deviation $2$ should sit near $7.4,9.0,10,11.0,12.6$. The sample $7,9,10,11,18$ matches that line at the bottom and in the middle, and then the largest point is $18$ rather than about $12.6$. The plot bends upward: a long right tail. A long left tail bends the other way, and heavy tails at both ends make an S shape. With only five points a single unusual value moves the picture, so the plot is a diagnostic rather than a formal test. Curvature can also be a clue about the scale of a later model. A logarithm that straightens a positive right-skewed measurement is information about that scale, which a yes-or-no test on the original numbers does not supply.
""",
    "normal-sample-theorem": r"""
## Three facts that hold together

Let $X_1,\ldots,X_n$ be independent and $\operatorname{N}(\mu,\sigma^2)$, and write $\overline X$ for the sample mean and $s^2=\frac1{n-1}\sum_i(X_i-\overline X)^2$ for the unbiased sample variance. Then $\overline X$ is $\operatorname{N}(\mu,\sigma^2/n)$, the scaled variance $(n-1)s^2/\sigma^2$ is [chi-squared](chi-squared-distribution.qmd) on $n-1$ degrees of freedom, and $\overline X$ is independent of $s^2$. The first fact is ordinary addition of independent normals. The other two use the rotational symmetry of the standard normal vector.

Standardise $Z_i=(X_i-\mu)/\sigma$. There is an orthogonal transformation whose first new coordinate is $W_1=\sqrt{n}\,\overline Z$. Orthogonal images of independent standard normals are independent standard normals, and the sum of squares is preserved, so

$$
\sum_{i=2}^n W_i^2=\sum_{i=1}^n(Z_i-\overline Z)^2=\frac{(n-1)s^2}{\sigma^2}.
$$

The left side is chi-squared on $n-1$ degrees of freedom and is a function of $W_2,\ldots,W_n$ only. It is therefore independent of $W_1$, and hence of $\overline X$. The ratio $(\overline X-\mu)/(s/\sqrt{n})$ is the Student $t$ pivot on $n-1$ degrees of freedom (Student, 1908). The [moment formulae](moments-of-the-sample-mean-and-variance.qmd) $\mathbb{E}\overline X=\mu$, $\operatorname{Var}(\overline X)=\sigma^2/n$ and $\mathbb{E} s^2=\sigma^2$ do not need normality. The chi-squared law and the independence do.

## Two observations, without a rotation

For $n=2$, $\operatorname{Cov}(X_1+X_2,X_1-X_2)=\operatorname{Var}(X_1)-\operatorname{Var}(X_2)=0$. Joint normality turns that zero covariance into independence of $\overline X$ and $X_1-X_2$. And $(X_1-X_2)^2/(2\sigma^2)$ is chi-squared on $1$ degree of freedom, which is exactly $(n-1)s^2/\sigma^2$. Away from normality the independence fails. For a large non-normal sample the [central limit theorem](central-limit-theorem.qmd) still makes $\overline X$ approximately normal, which is why a $t$ interval remains a usable approximation.
""",
    "null-and-alternative-hypotheses": r"""
## Two disjoint claims, with different jobs

A test splits the parameter space into two disjoint pieces. The null hypothesis is $H_0:\theta\in\Theta_0$ and the alternative is $H_1:\theta\in\Theta_1$, with $\Theta_0\cap\Theta_1$ empty. The [type I error](type-i-and-type-ii-errors.qmd) is rejecting $H_0$ when $\theta$ really lies in $\Theta_0$. The significance level $\alpha$ is an upper bound on that probability. The type II error is failing to reject $H_0$ when $\theta$ lies in $\Theta_1$, and the power is the probability of rejection at such a $\theta$. The null is the claim whose false rejection is being controlled. The alternative is the departure the critical region is built to detect.

A simple hypothesis names one value of $\theta$. A composite hypothesis names a set of values. For a binomial count with known $n$, "$p=1/2$" is simple and "$p\neq 1/2$" is composite. Which claim is placed in $H_0$ is a design choice. In a trial of a new treatment, $H_0$ is often "no improvement", so that a significant result is a controlled false claim of benefit. A small sample can have low power, so failing to reject $H_0$ need not support $H_0$.

## Fifteen successes in twenty trials

Let $X\sim\operatorname{Bin}(20,p)$, and test $H_0:p=1/2$ against $H_1:p>1/2$. Large values of $X$ favour the alternative. The [one-sided $p$-value](p-value.qmd) at $x=15$ is $\mathbb{P}(X\ge 15)$ computed entirely under $\operatorname{Bin}(20,1/2)$,

$$
\frac{1}{2^{20}}\sum_{k=15}^{20}\binom{20}{k}=\frac{21700}{1048576}\approx 0.021.
$$

That number is not the probability that the coin is fair. It is the probability, if $p$ were $1/2$, of a count at least as large as the one observed.
""",
    "null-distribution-of-hotelling-s": r"""
## An exact level for a normal mean

The null hypothesis says that the mean of a $\operatorname{N}_p(\boldsymbol{\mu},\Sigma)$ population equals a nominated vector $\boldsymbol{\mu}_0$. Both $\boldsymbol{\mu}$ and the [positive definite](positive-definite-matrix.qmd) covariance $\Sigma$ are unknown, and $n>p$ independent vectors are observed. Hotelling's statistic is the squared [Mahalanobis](squared-mahalanobis-distance.qmd) distance of the sample mean from $\boldsymbol{\mu}_0$, using the unbiased covariance $S=A/(n-1)$ and multiplied by $n$. Under the null, and under normality, the scaled version

$$
F=\frac{n-p}{p(n-1)}\,T^2
$$

has an $F$ distribution on $(p,\, n-p)$ degrees of freedom. The factor $(n-p)/\bigl(p(n-1)\bigr)$ is the adjustment that turns $T^2$, built from a normal mean and an independent [Wishart](wishart-distribution.qmd) matrix, into exactly this $F$ law. Reject the null at level $\alpha$ when $F$ exceeds the upper $\alpha$ point of that law.

## A sample of size 20 in two dimensions

Take $n=20$, $p=2$ and an observed $T^2=10$. Then

$$
F=\frac{18}{2\cdot 19}\cdot 10=\frac{90}{19}\approx 4.74.
$$

The upper $5\%$ point of $F_{2,18}$ is $3.55$, and the tail probability beyond $4.74$ is about $0.022$. The test rejects at level $5\%$. The same $T^2$ is undefined when $S$ has no inverse, which is guaranteed if $p\ge n$ and can also happen, through collinearity, when $p<n$. Dropping normality keeps a large-sample chi-squared approximation for $T^2$ and removes the exact $F$ calibration. Using $A/n$ in place of $S$, without changing the critical value, changes the test.
""",
    "offspring-probability-generating-function": r"""
## One transform, composed once per generation

The next generation in a branching process is a random sum of independent offspring counts. A probability generating function turns that nesting into composition, so the law of generation $n$ is obtained by applying one function $n$ times.

Let $\xi$ be a random count on $\{0,1,2,\ldots\}$ with $\mathbb{P}(\xi=k)=p_k$. The offspring probability generating function is

$$
f(s)=\mathbb{E}(s^{\xi})=\sum_{k\ge 0}p_k s^{k},\qquad 0\le s\le 1.
$$

Always $f(1)=1$ and $f(0)=p_0$. If the mean is finite, $m=f'(1-)=\mathbb{E}\xi$. If $\mathbb{E}[\xi(\xi-1)]$ is finite, $f''(1-)$ equals that factorial moment, and $\operatorname{Var}(\xi)=f''(1-)+m-m^{2}$. Write $f_n(s)=\mathbb{E}(s^{Z_n})$ for the population $Z_n$ of a Galton–Watson process started at $Z_0=1$. Conditioning on the present generation gives $f_{n+1}(s)=f(f_n(s))$. A sum of a fixed number of independent copies would multiply transforms. Here the number of copies is itself random, so the transforms compose.

## Iterating a Poisson offspring law

If $\xi$ is Poisson with mean $\lambda$, then $f(s)=\exp(\lambda(s-1))$. For $\lambda=1.5$, extinction by generation $1$ has probability $f(0)=e^{-1.5}\approx 0.223$. The eventual [extinction probability](extinction-probability.qmd) is the smallest root of $q=f(q)$. Numerically that root is near $0.417$, strictly between $f(0)$ and $1$, in agreement with $m>1$. The mean $m=\lambda$ fixes only the slope of $f$ at $1$. The extinction probability uses the whole function. For a geometric law $\mathbb{P}(\xi=k)=(1-r)r^{k}$ on $k\ge 0$, one has the closed form $f(s)=(1-r)/(1-rs)$ and $m=r/(1-r)$, and the fixed-point equation can be solved by hand. Either way, $f$ is the object the [extinction criterion](extinction-criterion.qmd) analyses.
""",
    "one-hidden-layer-approximates-continuous-functions": r"""
## Existence of a shallow approximation

A continuous target $f$ is defined on the cube $[0,1]^p$. The modelling question is whether a network with one [hidden layer](hidden-layer.qmd) can track $f$ uniformly, to any prescribed tolerance $\varepsilon>0$. Cybenko's result says that a finite sum of ridge functions

$$
F(x)=\sum_{q=1}^{\ell} a_q\,\sigma(w_q^\top x+b_q)
$$

can do so, when $\sigma$ is a continuous sigmoidal [activation](activation-function.qmd) (Cybenko, 1989). Each term is constant on hyperplanes $w_q^\top x+b_q=\text{constant}$ and bends only along the normal $w_q$. The output weights $a_q$ are unrestricted, so $F$ can leave the range of $\sigma$. A bounded sigmoid on the output would be the wrong final map for a target that takes values outside $(0,1)$.

## What the existence result leaves open

A smooth step can be shifted and scaled, and a difference of two steps can approximate a localised bump. Sums of bumps, in turn, approximate a continuous function uniformly on a compact cube. The argument produces some finite width $\ell$ and some weights. It does not bound $\ell$, and it does not provide an algorithm that finds the weights from a sample. Approximation error, the distance from $f$ to the best network of a given size, is separate from optimisation error and from the statistical error of learning $f$ from $n$ noisy pairs. The result is also silent on discontinuous targets: continuous ridge sums are continuous, so they do not approximate every jump uniformly. A finite sample can still [overfit](overfitting.qmd) a wide one-hidden-layer net, because existence of a good $F$ is not a bound on estimation error.
""",
    "one-hot-encoding": r"""
## A code with a single one

A categorical response with $K$ levels has no numeric scale. One-hot coding replaces level $c$ by a vector $y\in\{0,1\}^K$ with $y_c=1$ and every other coordinate $0$. For $K=3$ and class $2$, the code is $(0,1,0)^\top$. A network with [softmax](output-coding-softmax-and-cross-entropy.qmd) outputs $s_1,\ldots,s_K$, positive and summing to $1$, is trained against this vector. The cross-entropy collapses to $-\log s_c$, the negative log probability of the true level. If the softmax probabilities are $(0.2,0.5,0.3)$ and the true class is $2$, the loss on that case is $-\log 0.5\approx 0.693$. Predicting a vector near $(0,1,0)$ makes the same loss near zero.

## Why a linear model usually drops a level

In a [linear model](gaussian-linear-model.qmd) with an intercept, the $K$ indicators sum to $1$, which is the intercept column. The design then has dependent columns, and the coefficient vector is not unique. The usual remedy is to omit one reference level and to read the remaining coefficients as contrasts with that level. Softmax does not need the omission. Adding the same constant to every class score leaves the probabilities unchanged, and the fit can set one score function to zero as a reference, which is the [baseline-category logit](baseline-category-logit-model.qmd) parameterisation. Using all $K$ scores, or using $K-1$ of them, represents the same probabilities. The coding of predictors is a separate choice from the coding of the target: a categorical predictor in a network is often left in full one-hot form, while the same predictor in an unpenalised linear predictor is reduced by one column.
""",
    "outlier": r"""
## A point sitting far from the bulk

An outlier is an observation far from the rest of the sample. On a [boxplot](five-number-summary-and-boxplot.qmd) the usual flag is a point more than $1.5$ interquartile ranges beyond the first or third quartile, the fence associated with Tukey (1977). In the ordered sample $2,3,3,4,5,6,7,8,20$, hinges that include the median in both halves are $3$ and $7$. The interquartile range is $4$ and the upper fence is $13$. The value $20$ lies past the fence and $8$ does not. The rule decides which points to draw one by one. It does not decide that $20$ was mistyped, and it is not permission to delete the row and refit as though that row had never been collected.

## A mistake, a tail, or the point that matters

Three different mechanisms produce the same flag. A transcription error, such as a shifted decimal or an age stored as $999$, should be corrected or marked missing, because it is not a measurement of the variable. A long-tailed distribution produces genuine extremes. The largest claim in an insurance file is an outlier relative to a normal model and an ordinary claim relative to a heavy-tailed one. Deleting it changes the population being estimated. The third case is influence rather than an extreme response. A covariate far from the other covariate values can swing a fitted slope even when the response looks ordinary. Refitting without the point shows which coefficients move. The science then decides whether the point is a mistake, a tail, or the observation the study was fortunate to include.
""",
    "overfitting": r"""
## Training error that keeps falling

A model family is fitted by driving a training loss down. With enough free parameters the fitted function can pass close to every training pair, including pairs whose response is mostly noise. The training error then falls, while the error on new draws from the same distribution rises. That gap is overfitting. A polynomial of degree $n-1$ through $n$ distinct covariate values interpolates the responses exactly, so its training squared error is zero whatever the responses were. The interpolant follows the noise as faithfully as it follows the signal. The [apparent error](apparent-error.qmd) on the training sample is then an optimistic report of the error on a fresh case.

## Guards that use data the fit did not see

Three standard controls change the fitting problem. [Regularisation](regularisation.qmd) adds a penalty on the size of the weights, so a wild interpolant has to pay for its large coefficients. [Early stopping](early-stopping.qmd) monitors a [held-out](a-held-out-test-set.qmd) loss during training and keeps the weights from the iteration at which that loss was smallest; later iterations may still be reducing the training loss. Restricting the architecture, for example by using fewer [hidden units](hidden-layer.qmd), limits the functions that can be represented. Each control has a tuning choice, and the tuning choice itself has to be scored on data that were not used to make it. A training error of $0.02$ beside a held-out error of $0.18$ is a description of one fit. It becomes evidence about a procedure only when the whole procedure, including the tuning, is applied to fresh pairs.
""",
    "paired-comparison": r"""
## A winner between two items, and no common score

Taste tests, matches and preference trials often record only which of two items won. There is no measurement of quality on a shared ruler, only the result of the pair that was actually run. A paired-comparison model gives item $i$ a strength $\lambda_i$ and sets the odds that $i$ beats $j$ equal to $\exp(\lambda_i-\lambda_j)$. The probability is

$$
\mathbb{P}(i\text{ beats }j)=\frac{\exp(\lambda_i)}{\exp(\lambda_i)+\exp(\lambda_j)}.
$$

This is the [Bradley–Terry model](bradley-terry-model.qmd) (Bradley and Terry, 1952). Swapping the two labels inverts the odds, so the match of $i$ against $j$ and the match of $j$ against $i$ are one comparison, not two unrelated probabilities. Each observed pair contributes a Bernoulli likelihood. Items that never meet can still be placed on one scale when the schedule connects them through other opponents.

## A shift of every strength leaves the odds alone

Only differences $\lambda_i-\lambda_j$ appear in the probabilities, so the strengths are not identified. Adding $5$ to every strength changes nothing that the matches can see. A constraint removes the free constant: one item is fixed at strength $0$, or the strengths are required to sum to $0$. With $\lambda_A=0$, $\lambda_B=0.8$ and $\lambda_C=1.4$, the probability that B beats A is $\exp(0.8)/\{1+\exp(0.8)\}\approx 0.69$, that C beats A is about $0.80$, and that C beats B is $\exp(0.6)/\{1+\exp(0.6)\}\approx 0.65$. The shifted strengths $5$, $5.8$ and $6.4$ reproduce those three probabilities exactly. A home advantage, if the design has one, is a further additive term on the log odds of the home item.
""",
    "pareto-distribution": r"""
## A tail heavy enough to dominate the sample

Some positive measurements, such as incomes or claim sizes, produce occasional values so large that one observation dominates the sum. The Pareto law is the standard power-law description of that tail, and its moments exist only for shapes above explicit thresholds.

Take $\mathbb{P}(X>x)=x^{-\alpha}$ for $x\ge 1$, with shape $\alpha>0$. This is a Pareto distribution with scale $1$. The density is $f(x)=\alpha x^{-\alpha-1}$ on $[1,\infty)$. Integrating the tail gives the moments. For $p>0$,

$$
\mathbb{E}[X^{p}]=\frac{\alpha}{\alpha-p}\qquad\text{when }\alpha>p,
$$

and the moment is infinite when $\alpha\le p$. In particular the mean is $\alpha/(\alpha-1)$ when $\alpha>1$, and infinite otherwise. The second moment is finite only when $\alpha>2$, so the variance is finite only in that range. A finite mean with an infinite variance, the case $1<\alpha\le 2$, is enough for the strong law and not enough for the classical central limit theorem.

## Shape $3/2$, mean $3$, and a large maximum

Take $\alpha=3/2$. The mean is $(3/2)/(1/2)=3$, and $\mathbb{E}[X^{2}]=\infty$. Also $\mathbb{P}(X>100)=100^{-3/2}=1/1000$. In a sample of $n=1000$ one therefore expects about one observation beyond $100$, and the scaling constant of the maximum is $n^{1/\alpha}=1000^{2/3}=100$. As $n\to\infty$, the normalised maximum $M_n/n^{1/\alpha}$ converges in distribution to the Fréchet law ($\mathbb{P}(M\le x)=\exp(-x^{-\alpha})$ for $x>0$, which equals $e^{-1}\approx 0.368$ at $x=1$), giving the approximation for $M_n/100$ at $n=1000$. A typical single draw is of order $1$, since the median solves $x^{-3/2}=1/2$ and is only $2^{2/3}\approx 1.6$. One large value can exceed the bulk of the sample by two orders of magnitude. That is the extreme-value content of a [power-law tail](power-law-tails-and-the-frechet-law.qmd).
""",
    "partial-autocorrelation": r"""
## Correlation left after the lags in between

The autocorrelation at lag $k$ mixes every route by which $X_t$ can depend on $X_{t-k}$, including the route through the times in between. The partial autocorrelation removes that route. At lag $k$ it is the correlation between two residuals: $X_t$ regressed linearly on $X_{t-1},\ldots,X_{t-k+1}$, and $X_{t-k}$ regressed on the same intermediates. Write $\phi_{kk}$ for that correlation. Equivalently, $\phi_{kk}$ is the coefficient of $X_{t-k}$ in the best linear autoregression of order $k$. For a weakly stationary series the two definitions agree. At lag $1$ there is no intermediate time, so $\phi_{11}$ is simply the lag-$1$ [autocorrelation](autocorrelation-function.qmd).

## A cutoff that names the autoregressive order

An autoregression of order $p$ has $\phi_{kk}=0$ for every $k>p$. Once the $p$ neighbouring lags are accounted for, nothing remains for an older lag to explain. The series $X_t=0.6X_{t-1}+\varepsilon_t$, with $\varepsilon_t$ white noise, has autocorrelations $0.6$, $0.36$ and $0.22$ at lags $1$, $2$ and $3$, but partial autocorrelations $0.6$, $0$ and $0$. The autocorrelation decays. The partial autocorrelation stops. A moving average of order $1$ does the opposite: its autocorrelation is zero after lag $1$, and its partial autocorrelation tails off. With coefficient $0.5$ on the lagged innovation, the lag-$1$ autocorrelation equals $0.5/(1+0.5^2)=0.4$ and every longer autocorrelation is $0$. A seasonal series need not obey either short-lag cutoff: a seasonal moving average keeps partial-autocorrelation spikes at multiples of the period, whereas a seasonal autoregression cuts the partial autocorrelation off after the seasonal lag while its autocorrelation tails off at those multiples—either pattern is a reason to model the season rather than fit an ordinary autoregression of huge order.
""",
    "partial-correlation": r"""
## Association after a linear adjustment

Two coordinates can move together because both track a third. The partial correlation removes that linear tracking. Partition $\mathbf{X}=(\mathbf{X}_A^\top,\mathbf{X}_B^\top)^\top$ and write $\Sigma_{A\mid B}$ for the covariance of the residual $\mathbf{X}_A-\Sigma_{AB}\Sigma_{BB}^{-1}\mathbf{X}_B$, after the population linear regression on $\mathbf{X}_B$ has been subtracted. The partial correlation of coordinates $j$ and $k$ inside $A$ is the ordinary correlation computed from that residual covariance. In a multivariate normal model the residual is independent of $\mathbf{X}_B$, so the partial correlation is also the conditional correlation given $\mathbf{X}_B$. Outside the Gaussian family the residual correlation remains defined whenever the regressions and second moments exist, and it need not equal the conditional correlation at every value of the conditioning variables.

## A chain in which the ends are marginally dependent

Take the precision matrix

$$
K=\begin{pmatrix}1&-1/2&0\\-1/2&1&-1/2\\0&-1/2&1\end{pmatrix},
\qquad
\Sigma=K^{-1}=\begin{pmatrix}1.5&1&0.5\\1&2&1\\0.5&1&1.5\end{pmatrix}.
$$

The marginal correlation of $X_1$ and $X_3$ is $0.5/\sqrt{1.5\cdot 1.5}=1/3$. The residual covariance of $(X_1,X_3)$ given $X_2$ is the identity, so the partial correlation $\rho_{13\mid 2}$ is $0$. The same zero is the $(1,3)$ entry of $K$, and in general

$$
\rho_{jk\mid\text{rest}}=-\frac{K_{jk}}{\sqrt{K_{jj}K_{kk}}}.
$$

Here $\rho_{12\mid 3}=1/2$. The partial correlation is a statement about linear association after adjustment. It is not, by itself, a claim that the conditioning variables cause the others.
""",
    "partially-linear-model": r"""
## A slope you can quote, and a curve you only adjust for

Some covariates are the comparison you came to estimate: a treatment, a dose, a price. Others are nuisances with a curved effect: age, ambient temperature, a baseline measurement. A partially linear model splits the two jobs. On the scale of the link,

$$
g(\mu)=\mathbf{x}^\top\boldsymbol{\beta}+f(z),
$$

$\boldsymbol{\beta}$ is an ordinary coefficient vector and $f$ is a smooth function, usually a penalised spline. The linear piece is what you quote per unit of $x$. The smooth piece keeps a curved nuisance from being forced into a straight line, and from being ignored. Putting every term into $\mathbf{x}^\top\boldsymbol{\beta}$ misstates the adjustment when the nuisance bends.

## Odds at a fixed age

On the logit scale let $\eta=\beta_0+\beta_1 T+f(\mathrm{age})$, where $T$ is $1$ under treatment and $0$ under control, and where $f$ is centred so that it does not swallow the intercept. A coefficient $\beta_1=0.4$ multiplies the odds by $\exp(0.4)\approx 1.49$ at any fixed age. The sentence is conditional on age through $f$. It is not an average that pretends age was absent. Two failures belong to this split. If treatment was given almost exactly when age crossed a threshold, then $T$ and $f(\mathrm{age})$ carry the same information. That concurvity makes $\beta_1$ unstable, in the way collinear columns make an ordinary slope unstable. An uncentred $f$ can also trade a constant with $\beta_0$, so the printed intercept is an arbitrary cut of that trade. [Cross-validation](cross-validation.qmd) can choose how smooth $f$ is. It cannot repair a design in which treatment and age never vary separately.
""",
    "pearson-dispersion-ratio": r"""
## Residual scatter against the variance the model allows

A generalised linear model states a variance function, not only a mean. For a Poisson fit that statement is $\operatorname{Var}(Y_i)=\mu_i$. The [Pearson statistic](pearson-statistic.qmd) adds the squared residuals on that scale, $\sum_i(y_i-\hat\mu_i)^2/\hat\mu_i$. The Pearson dispersion ratio divides the sum by the residual degrees of freedom $n-p$, where $p$ is the number of fitted mean parameters. A ratio near $1$ says the residuals are about as large as the variance function predicted. A ratio well above $1$ says they are larger, and a ratio well below $1$ says they are smaller. For a gamma mean with variance $\phi\mu^2$ the summand is $(y_i-\hat\mu_i)^2/\hat\mu_i^2$ instead. Using the Poisson summand on those data checks the wrong function.

## Four counts, and a ratio near three

The counts $1,2,8,9$ have mean $5$. An intercept-only Poisson fit sets every $\hat\mu_i=5$ and has $4-1=3$ residual degrees of freedom. The Pearson statistic is $(16+9+9+16)/5=10$, so the dispersion ratio is $10/3\approx 3.33$. Standard errors computed as if the ratio were $1$ are too small by about $\sqrt{3.33}\approx 1.8$. A $z$ statistic of $2.4$ would fall to about $1.3$. That is a reason to consider a [quasi-Poisson](quasi-poisson.qmd) variance $\phi\mu$, but only after the mean has been examined. A missing covariate, or a curve fitted by a straight line, inflates the same sum. The ratio cannot separate overdispersion from a wrong $\hat\mu$. It is a check on the variance function. It is not, by itself, a second sampling model.
""",
    "perceptron-learning-rule": r"""
## A correction only on a mistake

A threshold unit classifies a point $x$, augmented by a coordinate $x_0=1$, according to the sign of the score $w^\top x$. The weight vector includes the bias. There is no linear system whose solution is the weight, because the threshold is constant on each open half-space. The perceptron rule (Rosenblatt, 1958) builds a weight by correction. On a correctly classified pattern $y_i-o_i=0$ and the weight is left alone. On a mistake the pattern is added when the label was $1$ and the output was $0$, and subtracted when the label was $0$ and the output was $1$. The score on that pattern changes by $(y_i-o_i)\,\|x_i\|^2$.

## One step, and the stopping rule

Start at $w=\mathbf{0}$ and present the augmented point $x=(1,1,0)^\top$ with label $y=0$. The score is $0$. Under the convention that a nonnegative score outputs $1$, the point is misclassified. The update subtracts $x$, and the new weight is $(-1,-1,0)^\top$. The score changes by $-\|x\|^2=-2$, from $0$ to $-2$, and the output becomes $0$. Each later mistake moves the weight by one pattern and by no more.

If some hyperplane separates the training labels, repeated passes reach a separating weight after finitely many corrections. The rule then stops. Any separating hyperplane is a stopping place: the update has no further preference among them, and in particular it does not maximise the geometric [margin](linear-separators-and-the-margin.qmd). If no hyperplane separates the sample, as with the [XOR](xor-problem.qmd) corners, some pattern is always misclassified and the loop does not terminate.
""",
    "pitman-koopman-darmois-informal-form": r"""
## Which families keep a summary of fixed dimension?

For an iid sample the whole data vector is sufficient, and its dimension grows with $n$. The sharper question is whether some statistic of dimension independent of $n$ is sufficient for every sample size. [Exponential families](exponential-family.qmd) have exactly that reduction: if one observation contributes a natural statistic $T(x)$, then $S = \sum_{i=1}^{n} T(X_i)$ is sufficient for every $n$, and the dimension of $T$ does not grow. Conjugate updating adds those totals to a fixed collection of hyperparameters. The Pitman–Koopman–Darmois theorem says that, inside a regular class, a sufficient statistic of dimension bounded in $n$ essentially characterises the exponential families (Darmois, 1935; Pitman, 1936; Koopman, 1936). The support of each observation must not depend on $\theta$, and the densities must be smooth enough for the likelihood to force the exponential form.

## The uniform maximum uses a moving support

Remove the support restriction and the characterisation no longer holds. For iid observations from the [uniform distribution](uniform-distribution.qmd) on $(0, \theta)$, the maximum $X_{(n)}$ is sufficient for every $n$ and has dimension one. The density equals $\theta^{-1}$ on $(0, \theta)$ and equals zero outside that interval, so the set of possible observations changes with $\theta$. Sufficiency of the maximum uses the indicator of that moving support. It is not the regular form $b(x)\exp\{c(\theta) T(x)\}/a(\theta)$ with $b$ free of $\theta$ and with a common support. A one-dimensional sufficient statistic is therefore not, by itself, the regular exponential-family conjugate update that adds a sum of natural statistics: $\operatorname{Uniform}(0,\theta)$ still admits a conjugate two-parameter Pareto prior, updated by replacing its lower bound with $\max(x_m,X_{(n)})$ and adding $n$ to its shape.
""",
    "point-forecast": r"""
## The conditional mean at a stated horizon

A point forecast is one number offered for a future observation. Under squared error, the best number given the series up to time $T$ is the conditional mean $\mathbb{E}(X_{T+h}\mid X_T,X_{T-1},\ldots)$. Call it $\hat X_T(h)$. It is not a promise that the future observation will land on that number, and it is not a parameter of the process. The horizon $h$ belongs in the definition. For a stationary autoregression the forecast is pulled towards the unconditional mean as $h$ grows, and the variance of the forecast error rises towards the marginal variance of the series. A [prediction interval](prediction-interval.qmd) has to use that growing variance. A point on its own hides how fast the information in the latest observation expires.

## An autoregression walked three steps forward

Suppose $X_t=0.5X_{t-1}+\varepsilon_t$, where $\varepsilon_t$ has mean $0$ and variance $4$, and suppose $X_T=10$. The unconditional mean is $0$ and the marginal variance is $4/(1-0.5^2)=16/3\approx 5.33$. The point forecasts are $5$, $2.5$ and $1.25$ at horizons $1$, $2$ and $3$. The one-step error is $\varepsilon_{T+1}$, with variance $4$. The two-step error is $0.5\varepsilon_{T+1}+\varepsilon_{T+2}$, with variance $5$. The three-step error variance is $5.25$, already close to $5.33$. The forecast $1.25$ is only a little sharper than guessing the mean $0$. A random walk has no such ceiling. Its point forecast stays at the last observation for every horizon, and the error variance $h\sigma^2$ widens without bound. Using one style of interval for both series is a modelling error, not a choice of plot.
""",
    "poisson-limit-of-the-binomial": r"""
## Rare events among many trials

A binomial probability with a huge $n$ and a tiny $p$ is awkward to compute, and it depends on $n$ and $p$ almost only through the product $np$. Let $X_n\sim\operatorname{Bin}(n,p_n)$ with $np_n\to\lambda$ for some finite $\lambda>0$. Then for each fixed integer $k\ge 0$,

$$
\mathbb{P}(X_n=k)\to e^{-\lambda}\frac{\lambda^k}{k!}.
$$

The limit is the [Poisson distribution](poisson-distribution.qmd) with mean $\lambda$ (Poisson, 1837). For the leading case $p=\lambda/n$, write the binomial probability as

$$
\binom{n}{k}p^k(1-p)^{n-k}=\frac{\lambda^k}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k}\cdot\left(1-\frac{\lambda}{n}\right)^{n-k}.
$$

The fraction with $n(n-1)\cdots(n-k+1)$ tends to $1$. The last factor tends to $e^{-\lambda}$, because $(1-\lambda/n)^n\to e^{-\lambda}$ and $(1-\lambda/n)^{-k}\to 1$. The same limit holds when $p_n$ is only approximately $\lambda/n$. The approximation wants $n$ large and $p$ small, with $\lambda=np$ moderate. A binomial count with $p$ not small, such as $\operatorname{Bin}(20,0.4)$, is bounded by $n$ and is not in this rare-event regime, even though its mean is finite.

## Five hundred policies

Each of $500$ independent policies produces a claim with probability $0.01$, so $\lambda=5$. The exact probability of no claim is $0.99^{500}\approx 0.00657$, and $e^{-5}\approx 0.00674$. The exact probability of at most one claim is $0.0398$; the Poisson approximation $e^{-5}(1+5)$ equals $0.0404$. The two answers agree to about a thousandth. Only the product $np$ enters the approximation, which is why a rate can be estimated without separating $n$ from $p$.
""",
    "poisson-regression": r"""
## A positive mean for a non-negative count

Claims, collisions, organisms and failures are counts: non-negative integers. Their mean has to stay non-negative for every covariate pattern, including patterns outside the sample. Poisson regression is the generalised linear model with a Poisson random component and, usually, a log link $\log\mu_i=\mathbf{x}_i^\top\boldsymbol{\beta}$. Then $\mu_i=\exp(\mathbf{x}_i^\top\boldsymbol{\beta})$, and $e^{\beta_j}$ is the factor by which the mean count changes when covariate $j$ increases by one unit, the others held fixed. The Poisson statement $\operatorname{Var}(Y_i\mid\mathbf{x}_i)=\mu_i$ is part of the model. It matches a Poisson process with a fixed rate and independent increments. It fails when events arrive in clumps, or when units that share the same $\mathbf{x}$ still have different rates.

## Exposure, and variance that outgrows the mean

Equal counts are not equal rates. If unit $i$ is observed for an exposure $t_i$, the offset form $\log\mu_i=\mathbf{x}_i^\top\boldsymbol{\beta}+\log t_i$ makes $\exp(\mathbf{x}_i^\top\boldsymbol{\beta})$ a rate per unit of exposure. Three events in two years and six events in ten years are rates $1.5$ and $0.6$ per year. Omitting $\log t_i$ pretends that every unit was observed for the same time. [Overdispersion](overdispersion.qmd) is the separate failure $\operatorname{Var}(Y_i\mid\mathbf{x}_i)>\mu_i$. A dispersion ratio of $4$ leaves the log-link point estimates unchanged, because the dispersion factors out of the score, and it multiplies standard errors by $2$. A $z$ statistic of $2.4$ becomes $1.2$ and is no longer evidence against a zero coefficient. A ratio below $1$, underdispersion, occurs as well. A quasi-Poisson variance $\phi\mu$ repairs the standard errors. It does not by itself supply a distribution from which to simulate a new count.
""",
    "polynomial-kernel": r"""
## Monomials, written as one inner product

A linear separator in a higher-dimensional feature space can be fitted without storing the features, provided the algorithm uses the points only through inner products. The polynomial kernel

$$
K(x,x')=(1+x^\top x')^d
$$

is the inner product of a map $\phi$ whose coordinates are all monomials in the coordinates of $x$ of total degree at most $d$, with combinatorial coefficients such as $\sqrt{2}$ on the cross terms. The dimension of that map is $\binom{p+d}{d}$. For $p=2$ and $d=2$ the count is $6$. The Gram matrix with entries $K(x_i,x_j)$ is positive semi-definite because it is a matrix of inner products. Scaling a coordinate of $x$ changes every power, so a standardisation of the inputs is part of the kernel.

## A one-dimensional check, and the XOR corners

For scalars $x=2$ and $x'=1$, with $d=2$, $K=(1+2\cdot 1)^2=9$. The matching feature map is $\phi(t)=(1,\,\sqrt{2}\, t,\, t^2)^\top$, and

$$
\phi(2)=(1,\,2\sqrt{2},\,4)^\top,
\qquad
\phi(1)=(1,\,\sqrt{2},\,1)^\top
$$

have inner product $1+4+4=9$. In the plane, the four XOR corners $(\pm 1,\pm 1)$ are not linearly separable. The coordinate $x_1 x_2$ of a quadratic map equals $+1$ on the two corners where the signs agree and $-1$ where they differ, so a linear function of that coordinate separates them. The [kernel trick](kernel-trick.qmd) evaluates $K$ and never builds $\phi$. A large degree $d$ produces a rich class and can interpolate noise; the degree is a tuning choice, scored on held-out pairs, in the same way as the width of a [Gaussian kernel](gaussian-kernel.qmd).
""",
    "posterior-class-probability": r"""
## Turning class densities into a class probability

A classifier sees the measurement $\mathbf{x}$ and has to name a class $g\in\{1,\ldots,G\}$. The class-conditional density $f_g(\mathbf{x})$ describes the measurements inside class $g$. The prior $\pi_g=\mathbb{P}(Y=g)$ describes how common the class is before $\mathbf{x}$ is seen. Bayes' theorem converts the two into the posterior

$$
\tau_g(\mathbf{x})=\mathbb{P}(Y=g\mid X=\mathbf{x})=\frac{\pi_g f_g(\mathbf{x})}{\sum_{g'=1}^{G}\pi_{g'} f_{g'}(\mathbf{x})}.
$$

The denominator is the marginal density of $X$, the same for every class, so the class with the largest posterior is the class with the largest product $\pi_g f_g(\mathbf{x})$. When these are the true prior and the true densities, that choice minimises the zero–one risk at $\mathbf{x}$.

## A rare class with a higher density

Let $G=2$, $\pi_1=0.9$, $\pi_2=0.1$, $f_1(\mathbf{x})=1$ and $f_2(\mathbf{x})=4$. The un-normalised masses are $0.9$ and $0.4$, so

$$
\tau_1(\mathbf{x})=\frac{0.9}{1.3}\approx 0.692,
\qquad
\tau_2(\mathbf{x})=\frac{0.4}{1.3}\approx 0.308.
$$

Class $1$ remains more probable even though class $2$ is four times as dense at this $\mathbf{x}$. Equal priors $1/2$ would have reversed the comparison, because then only the densities matter. A plug-in rule replaces $\pi_g$ and $f_g$ by estimates. Training proportions estimate the priors when each case was drawn from the target population. A design that fixes the class counts, such as an equal number of cases and controls, does not: those proportions describe the sample, and the priors have to come from the population in which the rule will be used.
""",
    "posterior-median": r"""
## Absolute error and the posterior split

Absolute error treats an overestimate and an underestimate of the same size as equally bad. For a scalar parameter $\theta$, a decision $d$ is scored by $|\theta - d|$, and the Bayes action minimises the posterior expected absolute loss $\rho(d) = \mathbb{E}[|\theta - d| \mid x]$. When $\mathbb{E}[|\theta| \mid x]$ is finite and the posterior distribution function $F_{\theta\mid x}$ is continuous, split the integral at $d$. Differentiating under the integral sign, the Leibniz boundary terms cancel and

$$
\rho'(d) = 2F_{\theta\mid x}(d) - 1.
$$

The slope is negative while less than half the posterior mass lies at or below $d$, and positive while more than half lies there, so a minimiser satisfies $F_{\theta\mid x}(m) = \tfrac12$. With atoms, zero lies in the subgradient precisely when $\mathbb{P}(\theta \le m \mid x) \ge \tfrac12$ and $\mathbb{P}(\theta \ge m \mid x) \ge \tfrac12$. Mass on the left pulls the action down and mass on the right pulls it up. Under absolute-error loss, that minimiser is a posterior median.{{cite:lehmann_casella1998,gelman_bda2013}}

## Monotone reparameterisation, with a Beta comparison

Let $\phi$ be strictly monotone. If $\phi$ increases, then $\{\phi(\theta) \le \phi(m)\}$ coincides with $\{\theta \le m\}$, and likewise for the upper tail, so $\phi(m)$ is a posterior median of $\phi(\theta)$. If $\phi$ decreases, the tails exchange and both inequalities persist. The [posterior mean](posterior-mean.qmd) does not travel with $\phi$: $\mathbb{E}[\phi(\theta) \mid x]$ equals $\phi(\mathbb{E}[\theta \mid x])$ for every posterior when $\phi$ is affine, and can fail when $\phi$ is not. A [maximum a posteriori estimate](maximum-a-posteriori-estimate.qmd) fails as well, because the density of $\psi = \phi(\theta)$ is multiplied by the Jacobian $|\mathrm{d}\theta/\mathrm{d}\psi|$, which can move the mode.

For a skewed $\operatorname{Beta}(3, 9)$ posterior the mean is $3/12 = 0.25$, the mode is $(3-1)/(3+9-2) = 0.20$, and the median is approximately $0.236$. On the odds scale $\phi(\theta) = \theta/(1-\theta)$, the median transforms to $\phi(0.236) \approx 0.309$. By contrast, the posterior odds have an inverse-beta (Beta prime) density proportional to $\phi^{2}/(1+\phi)^{12}$: their mean is $3/(9-1) = 0.375 \neq \phi(0.25) = 1/3$, and their mode is $2/(9+1) = 0.20 \neq \phi(0.20) = 0.25$.
""",
    "posterior-membership": r"""
## A soft label for an unobserved component

In a [mixture](finite-mixture-model.qmd) the component label of a point $\mathbf{x}$ is not observed. The responsibility $\tau_h(\mathbf{x};\Psi)$ is the conditional probability of component $h$ given $\mathbf{x}$, computed at a parameter $\Psi=(\pi_h,\theta_h)_{h=1}^{H}$. The formula is Bayes' theorem with prior weight $\pi_h$ and component density $f_h(\cdot;\theta_h)$. The responsibilities are nonnegative and sum to $1$ over $h$. They are the soft labels used by the [E step](e-step.qmd). A hard assignment would replace each $\tau_h$ by $0$ or $1$. The EM update uses the fractional values, so a point between two components contributes to both.

## From responsibilities to a weighted mean

Suppose three scalar points $0$, $1$ and $3$ have responsibilities $0.9$, $0.2$ and $0.5$ for component $1$, and therefore $0.1$, $0.8$ and $0.5$ for component $2$. The component counts are $n_1=1.6$ and $n_2=1.4$, out of $n=3$. The M step sets

$$
\hat\pi_1=\frac{1.6}{3}\approx 0.533
$$

and the weighted means

$$
\hat\mu_1=\frac{0.9\cdot 0+0.2\cdot 1+0.5\cdot 3}{1.6}=1.0625,
\qquad
\hat\mu_2=\frac{0.1\cdot 0+0.8\cdot 1+0.5\cdot 3}{1.4}\approx 1.643.
$$

A point with $\tau_1=1/2$ is split evenly. The same weights, applied to squared deviations from $\hat\mu_h$, update a component variance. The calculation holds the responsibilities fixed. Recomputing them from $(\hat\pi,\hat\mu)$ is the next E step, not part of the derivative of $Q$. A component whose covariance collapses makes one density arbitrarily large at a single point and drives that point's responsibility to $1$, which is a numerical failure of an unconstrained Gaussian mixture, not a property the responsibilities were defined to have.
""",
    "power-law-tails-and-the-frechet-law": r"""
## The maximum grows like a power of the sample size

If a tail is regularly varying, enlarging the sample does not merely shift the maximum by a few units. It multiplies the scale of the maximum by a power of the sample size. The Fréchet law is the limit after that scaling, and it is supported on the positive half-line.

Suppose $\mathbb{P}(X>x)=x^{-\alpha}$ for $x\ge 1$ and some $\alpha>0$, and let $M_n$ be the maximum of $n$ independent copies. Set $a_n=n^{1/\alpha}$ and $b_n=0$. For every $x>0$ and $n$ large enough that $n^{1/\alpha}x\ge 1$,

$$
\mathbb{P}(M_n/a_n\le x)
=\Bigl(1-\frac{x^{-\alpha}}{n}\Bigr)^{n}
\to\exp(-x^{-\alpha}).
$$

The limit is the Fréchet distribution function $\Phi_{\alpha}$. Its own upper tail is of order $x^{-\alpha}$, so the limit has a finite mean only when $\alpha>1$, the same threshold as the parent [Pareto distribution](pareto-distribution.qmd). Multiplying the sample size by a constant $c$ multiplies the scale $a_n$ by $c^{1/\alpha}$. A larger $\alpha$ is a lighter tail, and the scale then grows more slowly.

## Against a typical observation, and against a logarithm

Take $\alpha=2$ and $n=10000$, so $a_n=100$. The median of $\Phi_{2}$ solves $x^{-2}=\log 2$, hence $x=(\log 2)^{-1/2}\approx 1.20$. The median of $M_n$ is near $120$. A single observation from this Pareto law has median $\sqrt{2}\approx 1.41$. The maximum is about two orders of magnitude larger than a typical draw. By contrast, the maximum of $10000$ unit exponential variables has median near $\log 10000-\log(\log 2)\approx 9.58$, a shift of logarithmic order rather than a multiplication by $100$. That contrast is why heavy tails and [exponential tails](exponential-tails-and-the-gumbel-law.qmd) belong to different families in the [extreme-value classification](extreme-value-classification.qmd) (Fréchet, 1927).
""",
    "precision-matrix": r"""
## The inverse covariance as a conditional parameter

For a random vector with covariance $\Sigma$ positive definite, the precision is $K=\Sigma^{-1}$. In a nonsingular multivariate normal model, $K$ carries the conditional structure. The conditional variance of coordinate $i$ given all the others is $1/K_{ii}$. The coefficient of $X_j$ in the linear regression of $X_i$ on the remaining coordinates is $-K_{ij}/K_{ii}$. In particular $K_{ij}=0$ if and only if $X_i$ and $X_j$ are conditionally independent given the rest, and the partial correlation is $-K_{ij}/\sqrt{K_{ii}K_{jj}}$ (Lauritzen, 1996). A zero in $K$ is a missing edge of the [Gaussian graphical model](gaussian-graphical-models.qmd). A zero in $\Sigma$ is a different statement: it says that the two coordinates are uncorrelated, with no conditioning.

## Reading a chain

For

$$
K=\begin{pmatrix}1&-1/2&0\\-1/2&1&-1/2\\0&-1/2&1\end{pmatrix}
$$

the conditional variance of each end, given the other two coordinates, is $1/K_{11}=1$. The partial correlation of the two ends, given the middle, is zero because $K_{13}=0$. The partial correlation of coordinate $1$ with the middle, given the far end, is $-K_{12}/\sqrt{K_{11}K_{22}}=1/2$. The inverse of this $K$ has a nonzero $(1,3)$ entry, so the ends are marginally correlated. Estimating $K$ by inverting a sample covariance is available when that sample covariance is positive definite. When $p\ge n$, the centred sample covariance is singular, the inverse does not exist, and a constrained or penalised precision is a different estimator.
""",
    "predictive-variance-decomposition": r"""
## Separate noise from doubt about the parameter

Predicting a new observation $\widetilde{X}$ is not the same task as estimating $\theta$. Assume $\widetilde{X}$ is conditionally independent of the sample $x$ given $\theta$, so $p(\widetilde{X} \mid \theta, x) = p(\widetilde{X} \mid \theta)$. Write $m(\theta) = \mathbb{E}[\widetilde{X} \mid \theta]$ and $v(\theta) = \operatorname{Var}(\widetilde{X} \mid \theta)$, with $\mathbb{E}[v(\theta) \mid x]$ and $\mathbb{E}[m(\theta)^2 \mid x]$ finite. The [tower property](tower-property.qmd) gives $\mathbb{E}[\widetilde{X} \mid x] = \mathbb{E}[m(\theta) \mid x]$. Split the centred new observation as

$$
\widetilde{X} - \mathbb{E}[\widetilde{X} \mid x] = \{\widetilde{X} - m(\theta)\} + \{m(\theta) - \mathbb{E}[m(\theta) \mid x]\}.
$$

Square both sides and take the expectation under the posterior predictive distribution. The cross term has conditional expectation zero given $\theta$, because $\widetilde{X} - m(\theta)$ has mean zero given $\theta$ and the second brace does not involve $\widetilde{X}$. What remains is

$$
\operatorname{Var}(\widetilde{X} \mid x) = \mathbb{E}[v(\theta) \mid x] + \operatorname{Var}\{m(\theta) \mid x\}.
$$

The first summand is observation noise. The second is posterior uncertainty in the conditional mean.

## A plug-in interval drops the second term

Replacing $\theta$ by a single estimate keeps a plug-in copy of $v(\theta)$ and discards $\operatorname{Var}\{m(\theta) \mid x\}$, so the interval is too narrow while that posterior variance is positive. For a normal measurement $\widetilde{X} \mid \mu \sim \operatorname{N}(\mu, \sigma^2)$ with $\sigma^2$ known and $\mu \mid x \sim \operatorname{N}(m_n, v_n)$, the predictive distribution is normal with mean $m_n$ and variance $\sigma^2 + v_n$. As the sample grows, $v_n$ typically tends to zero, but the predictive variance tends to $\sigma^2$ rather than to zero. A credible interval for $\mu$ and a [predictive interval](prior-and-posterior-predictive-distributions.qmd) for $\widetilde{X}$ answer different questions.
""",
    "principal-component-directions": r"""
## Orthogonal eigenvectors diagonalise the sample covariance

Because the sample covariance matrix $S$ is real and symmetric, its spectral decomposition $S=\Gamma\Lambda\Gamma^\top$ chooses an orthogonal matrix $\Gamma=(\boldsymbol{\gamma}_1,\ldots,\boldsymbol{\gamma}_p)$ whose columns satisfy $\Gamma^\top\Gamma=I_p$ and $S\boldsymbol{\gamma}_j=\lambda_j\boldsymbol{\gamma}_j$ with $\lambda_1\ge\cdots\ge\lambda_p\ge 0$. Rotating the centred vector $\mathbf{X}$ into the principal coordinates $\mathbf{Y}=\Gamma^\top\mathbf{X}$ gives sample covariance

$$
\operatorname{Cov}(\mathbf{Y})=\Gamma^\top S\Gamma=\Gamma^\top(\Gamma\Lambda\Gamma^\top)\Gamma=\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_p).
$$

Off-diagonal entries of $\Lambda$ are zero, so distinct principal components $Y_j$ and $Y_k$ ($j\ne k$) have sample covariance zero, while $\operatorname{Var}(Y_j)=\lambda_j$. Because cyclic permutation inside a trace gives $\operatorname{tr}(S)=\operatorname{tr}(\Gamma\Lambda\Gamma^\top)=\operatorname{tr}(\Lambda\Gamma^\top\Gamma)=\operatorname{tr}(\Lambda)$, rotating the axes redistributes variance across uncorrelated coordinates without creating or losing any of the total variance $\sum_{j=1}^p s_{jj}$.

## Two correlated measurements rotated to uncorrelated axes

Suppose $S=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$, which has total variance $\operatorname{tr}(S)=4$. Its eigenvalues solve $(2-\lambda)^2-1=0$, giving $\lambda_1=3$ and $\lambda_2=1$, with unit eigenvectors $\boldsymbol{\gamma}_1=(1,1)^\top/\sqrt{2}$ and $\boldsymbol{\gamma}_2=(1,-1)^\top/\sqrt{2}$. The first component $Y_1=(X_1+X_2)/\sqrt{2}$ has variance $3$ ($75\%$ of total variance), the second $Y_2=(X_1-X_2)/\sqrt{2}$ has variance $1$ ($25\%$), and $3+1=4=\operatorname{tr}(S)$. When two eigenvalues tie ($\lambda_j=\lambda_{j+1}$), any orthonormal basis of that two-dimensional eigenspace gives the same diagonal variances, so the subspace is unique even though individual directions inside it are not; see [principal component directions and scores](principal-component-directions-and-scores.qmd).
""",
    "principal-component-directions-and-scores": r"""
## Directions of greatest sample variance

After each observation has been centred, the sample covariance $S$ describes the shape of the cloud. The first principal-component direction is a unit vector $\mathbf{a}_1$ maximising $\mathbf{a}^\top S\mathbf{a}$, the sample variance of the projected points. The maximiser is a unit-length eigenvector for the largest eigenvalue $\lambda_1$ of $S$, and that maximal variance equals $\lambda_1$. The scores of the observations are the coordinates $\mathbf{a}_1^\top(\mathbf{x}_i-\bar{\mathbf{x}})$. The second direction $\mathbf{a}_2$ is a unit eigenvector for the next eigenvalue, orthogonal to $\mathbf{a}_1$, and the construction continues until $p$ orthogonal directions are in hand. The sign of each $\mathbf{a}_j$ is arbitrary: $-\mathbf{a}_j$ spans the same line and flips the sign of every score.

## A diagonal cloud, and a one-component reconstruction

If

$$
S=\begin{pmatrix}4&0\\0&1\end{pmatrix},
$$

then $\mathbf{a}_1=(1,0)^\top$, $\lambda_1=4$, $\mathbf{a}_2=(0,1)^\top$ and $\lambda_2=1$. The first score of a centred point $(x_1,x_2)$ is $x_1$, and the rank-1 reconstruction is $(x_1,0)$. The fraction of total sample variance on the first component is $4/(4+1)=0.8$. Leaving the data uncentred lets the leading axis fall along the line from the origin through the mean. Spread is what the centred matrix measures. The vectors $\mathbf{a}_j$ are the loadings of the covariance principal components. Changing the unit of one coordinate changes $S$ and can change the leading direction; standardising the columns is a separate choice of metric.
""",
    "prior-odds": r"""
## Model probabilities before the sample arrives

Prior odds compare two models before the data are used. For models $M_1$ and $M_2$, the prior odds of $M_1$ against $M_2$ are $\mathbb{P}(M_1)/\mathbb{P}(M_2)$. The ratio is a ratio of probabilities of models, not a ratio of parameter values inside one model, and it is not a likelihood ratio. Equal model probabilities are a special case rather than a requirement. Prior odds of $1/9$ mean that $M_2$ is nine times as plausible as $M_1$ before $x$ is seen. Those odds are part of the comparison. Setting them silently to one hides an assumption, especially when one model is a sharp simplification of the other and the analyst does not regard the two as equally credible.

## Multiply by the marginal-likelihood ratio

[Bayes' rule](bayes-rule.qmd) multiplies each prior model probability by its [marginal likelihood](marginal-likelihood-and-bayes-factor.qmd),

$$
p(x \mid M_j) = \int p(x \mid \theta_j, M_j)\, p(\theta_j \mid M_j) \,\mathrm{d}\theta_j.
$$

This average of the sampling density over the parameter prior is not the likelihood at a fitted point. The ratio of posterior model probabilities cancels the shared evidence $p(x)$ and leaves the Bayes factor $p(x \mid M_1)/p(x \mid M_2)$ times the prior odds. If the Bayes factor is $4$ and the prior odds are $1/2$, the [posterior odds](posterior-odds-factorisation.qmd) are $2$, so $M_1$ is favoured after the data even though it started behind. A large Bayes factor in favour of a model that was given tiny prior odds need not change which model the posterior prefers. Reporting the Bayes factor without the prior odds leaves that comparison unfinished.
""",
    "probability-generating-function": r"""
## A power series whose coefficients are the probabilities

Let $N$ take values in $\{0,1,2,\ldots\}$. The probability generating function is the power series

$$
G(z)=\mathbb{E} z^N=\sum_{n=0}^{\infty}\mathbb{P}(N=n)\,z^n,\qquad \lvert z\rvert\le 1.
$$

The series converges on the closed unit disc because the coefficients are non-negative and sum to at most $1$. Reading it is immediate: $G(0)=\mathbb{P}(N=0)$, and if the distribution is proper then $G(1)=1$. Differentiating term by term, $\mathbb{P}(N=k)=G^{(k)}(0)/k!$. The mean, when it is finite, is the derivative at the boundary, $G'(1)=\mathbb{E} N$. If the mean is infinite, that derivative tends to infinity as $z$ increases to $1$.

Independent sums multiply. If $N$ and $M$ are independent non-negative integer variables, then $G_{N+M}(z)=G_N(z)G_M(z)$ for $\lvert z\rvert\le 1$. That is [convolution](convolution.qmd) of the probability masses, written as algebra. Where the [moment generating function](moment-generating-function.qmd) exists it is the same object on an exponential scale, $M(s)=G(e^s)$. The probability generating function is special to counts. A continuous random variable has no probability masses to use as coefficients.

## Two Bernoulli trials

A single $\operatorname{Bern}(p)$ trial has $G(z)=1-p+pz$. Its derivative is $p$, so the mean is $p$, and $G(0)=1-p$ is the failure probability. Two independent copies have generating function $(1-p+pz)^2$, which expands to $(1-p)^2+2p(1-p)z+p^2 z^2$. Those coefficients are the $\operatorname{Bin}(2,p)$ probabilities. For $p=1/3$ the chance of two successes is $(1/3)^2=1/9$, the coefficient of $z^2$. The same product, with $n$ factors, is the probability generating function of $\operatorname{Bin}(n,p)$.
""",
    "probability-space": r"""
## Outcomes, events, and a countably additive weight

Before a random variable or a process can be defined, the experiment needs three pieces: a set of outcomes, a family of subsets closed under the operations probability uses, and a weight on that family that adds up over countable disjoint unions.

The triple $(\Omega,\mathcal{F},\mathbb{P})$ is a probability space. The sample space $\Omega$ is the set of outcomes. The sigma-algebra $\mathcal{F}$ contains $\Omega$, and it is closed under complements and under countable unions, hence also under countable intersections. A probability is a map $\mathbb{P}:\mathcal{F}\to[0,1]$ with $\mathbb{P}(\Omega)=1$ and, for pairwise disjoint events $A_n$,

$$
\mathbb{P}\Bigl(\bigcup_{n=1}^{\infty} A_n\Bigr)=\sum_{n=1}^{\infty}\mathbb{P}(A_n).
$$

The same set function is written $\mathbb{P}$ or $\mathrm{P}$. An event is a member of $\mathcal{F}$, not an arbitrary subset of $\Omega$.

## One toss, and a limit that needs the whole sequence

A single fair coin has $\Omega=\{H,T\}$, events $\emptyset$, $\{H\}$, $\{T\}$, and $\Omega$, with $\mathbb{P}(\{H\})=1/2$. Nothing about this space refers to an infinite sequence. For infinitely many independent fair tosses, $\Omega=\{0,1\}^{\mathbb{N}}$ and $\mathcal{F}$ is the sigma-algebra generated by the cylinder sets that fix finitely many coordinates. [Kolmogorov's extension](kolmogorov-extension-theorem.qmd) supplies the unique countably additive probability that gives each specified finite string its fair-coin probability. The event that the sample proportion of heads converges to $1/2$ depends on the entire sequence. It is a countable combination of cylinder events, so it lies in $\mathcal{F}$, and the [strong law](strong-law.qmd) says it has probability $1$. A finite algebra of cylinders would not contain that limit event.
""",
    "product-rule": r"""
## A joint event priced as a chain

The probability of a long intersection is often easiest as a sequence of conditional chances. Recall that $\mathbb{P}(B\mid A)=\mathbb{P}(A\cap B)/\mathbb{P}(A)$ whenever $\mathbb{P}(A)>0$. Rearranging gives $\mathbb{P}(A\cap B)=\mathbb{P}(A)\,\mathbb{P}(B\mid A)$. Apply that identity to $A_1$, then to $A_1\cap A_2$, and so on. If $\mathbb{P}(A_1\cap\cdots\cap A_{n-1})>0$, the intermediate intersections cancel and

$$
\mathbb{P}(A_1\cap\cdots\cap A_n)
=\mathbb{P}(A_1)\,\mathbb{P}(A_2\mid A_1)\cdots\mathbb{P}(A_n\mid A_1\cap\cdots\cap A_{n-1}).
$$

The hypothesis that the intersection of the first $n-1$ events has positive probability implies the same for every shorter intersection, so each conditional probability in the product is defined. If some earlier intersection already has probability $0$, the whole intersection has probability $0$, but the later conditional probabilities are undefined and the displayed product cannot be formed.

[Independence](independent-events.qmd) is the special case in which every conditional probability equals the corresponding unconditional probability. The joint probability is then the product of the marginals. Multiplying marginals when the events share a cause is the usual mistake: the formula is still true with the conditional probabilities, and it is false if those conditionals are replaced by marginals they do not equal.

## Three checks in series

A component passes a first inspection with probability $0.90$. Given that it passed, it passes a second inspection with probability $0.80$. Given both passes, it passes a third with probability $0.75$. The probability of passing all three is $0.90\times 0.80\times 0.75=0.54$. Treating the checks as independent with those same three numbers would be a different model. The numbers $0.80$ and $0.75$ are already conditional, and they must stay conditional in the product.
""",
    "proportional-hazards-model": r"""
## The same multiplier at every threshold

An ordered response often asks a cumulative question: the chance of landing at or above category $k$, not the chance of one particular bin. Write $\gamma_k=\mathbb{P}(Y\ge k\mid\mathbf{x})$. A proportional-hazards model puts the complementary log-log link on those probabilities and keeps a slope that does not depend on the cut,

$$
\log\{-\log(1-\gamma_k)\}=\theta_k+\mathbf{x}^\top\boldsymbol{\beta}.
$$

The intercept $\theta_k$ may change with the threshold. The coefficient vector $\boldsymbol{\beta}$ may not. Exponentiating a component of $\boldsymbol{\beta}$ produces a hazard ratio, the same factor at every cut. This is the grouped form of the continuous-time proportional-hazards model (Cox, 1972), read on cumulative probabilities. It is not a log [odds ratio](odds-ratio.qmd). A logit in place of the [complementary log-log](complementary-log-log-link.qmd) would make $\boldsymbol{\beta}$ a log odds ratio, which is a different parallel-lines model.

## Intercepts that have to respect the order

Take $\theta_2=-0.2$, $\theta_3=-1$, a single slope $\beta=0.5$ and a covariate $x=1$. The two linear predictors are $0.3$ and $-0.5$. The cumulative probabilities are about $0.74$ and $0.45$, so $\gamma_2>\gamma_3$, as a cumulative probability must. The hazard ratio is $\exp(0.5)\approx 1.65$ both for "at least category $2$" and for "at least category $3$". Swapping the intercepts would make the fitted probability increase as the threshold got harder, which is impossible rather than merely a poor fit. The common slope is the other restriction. It says the covariate shifts every threshold by the same amount on the complementary log-log scale. When a covariate matters for severe outcomes and not for mild ones, that single hazard ratio summarises a contrast the categories do not share.
""",
    "r-s-distribution-interface": r"""
## Four prefixes for four different questions

Once a posterior has been identified as a named distribution, further summaries are lookups in that distribution. The standard interface prefixes the family name by `d` for the density or mass function, `p` for the distribution function, `q` for a quantile, and `r` for a pseudo-random draw. For $\theta \mid x \sim \operatorname{Beta}(3, 9)$ the four prefixes answer different questions. The density is the input to a plot or to a mode calculation. The distribution function at $1/2$ equals $\mathbb{P}(\theta \le 1/2 \mid x)$, approximately $0.967$. The quantile function at $1/2$ is the posterior [median](median.qmd), approximately $0.236$. The quantiles at $0.025$ and $0.975$ form the [equal-tailed](credible-region-constructions.qmd) $95\%$ interval, approximately $(0.060, 0.518)$.

## Exact values, and the Monte Carlo copies

The `p` and `q` results are properties of the beta posterior. Draws produced by the `r` prefix estimate the same properties by averages and order statistics. The sample mean estimates the posterior mean $3/12 = 0.25$, the sample median estimates $0.236$, and the proportion of draws at most $1/2$ estimates $0.967$. That Monte Carlo error shrinks as the number of draws increases. A larger sample of draws does not repair a generator aimed at the wrong distribution, and it does not replace the algebra that showed the posterior is $\operatorname{Beta}(3, 9)$. If the posterior is available only through a Markov chain, these [Monte Carlo](monte-carlo-method.qmd) summaries are what remain, and dependence among the draws has to be taken into account. When the named functions exist, `p` and `q` are the exact versions of the same questions.
""",
    "random-component": r"""
## The distribution that fixes the noise

A generalised linear model has a random component, a linear predictor and a link (Nelder and Wedderburn, 1972). The random component is the distribution of the response given the covariates. The responses are independent, and each comes from the same [exponential family](exponential-family.qmd), such as the normal, Poisson, binomial or gamma. The family supplies a variance function $V$ and a dispersion $\phi$ with

$$
\operatorname{Var}(Y_i\mid\mathbf{x}_i)=\phi\, V(\mu_i).
$$

For the normal, $V(\mu)=1$ and $\phi=\sigma^2$. For the Poisson, $V(\mu)=\mu$ and $\phi=1$. For a binary response, $V(p)=p(1-p)$. For the gamma parameterisation used with positive continuous responses, $V(\mu)=\mu^2$ and $\phi$ is free. The link does not choose these functions. Two models can share a log link and still have different noise, and their standard errors will not agree.

## One mean, three different variances

At a fitted mean of $6$, a Poisson component has variance $6$. A gamma component with $\phi=1/2$ has variance $(1/2)\times 6^2=18$. A normal component with $\sigma^2=6$ matches the Poisson variance but can draw a negative number, which a count or a clotting time cannot be. The same mean is therefore not the same model. Quasi-likelihood keeps $V$ and $\phi$ and drops the rest of the density. The score for the regression coefficients can still be solved, but there is no distribution from which to simulate a new response. That is enough for point estimates and for dispersion-adjusted standard errors, and not enough for the probability of a future count. If the residuals fan out faster than $V(\hat\mu)$, the random component is the piece to reconsider.
""",
    "random-forest": r"""
## Two randomisations, then a vote

A single deep tree has low bias and high variance: a small change in the [training set](training-set.qmd) can change an early split and rearrange every later leaf. The forest grows $T$ such trees and averages them (Breiman, 2001). Tree $t$ is fit on a [bootstrap](bootstrap.qmd) sample of size $n$. At each node only $k$ of the $p$ predictors are offered, drawn at random, and the best split among those $k$ is kept. The bootstrap omits any given case with probability about $e^{-1}\approx 0.368$. The random subset of predictors stops every tree from cutting on the same strongest variable. For a new $x$, a regression forest returns the average of the $T$ predictions. A classification forest returns the majority vote. If $320$ of $T=500$ trees vote for class $1$, the hard prediction is class $1$ and the soft vote is $320/500=0.64$.

## The correlation floor

Suppose the tree predictions at a fixed $x$ have common variance $\sigma^2$ and common pairwise correlation $\rho$. The variance of their average is

$$
\rho\sigma^2+\frac{1-\rho}{T}\sigma^2.
$$

With $\sigma^2=0.2$, $\rho=0.3$ and $T=100$ this equals $0.0614$, already close to the floor $\rho\sigma^2=0.06$. Further trees shrink only the second term. Dropping $\rho$ to $0.05$, which is what a small $k$ is for, drops the floor to $0.01$. The usual defaults take $k=\sqrt{p}$ for classification and $k=p/3$ for regression, and they grow each tree until the leaves are small. Those defaults are part of the fitted procedure. A search over $k$ and the leaf size belongs inside cross-validation, off any final test set.
""",
    "random-seed": r"""
## The start that fixes every later draw

A [linear congruential generator](linear-congruential-generator.qmd) updates an integer state by $X_{i+1}=(aX_i+c)\bmod m$ and returns $U_i=X_i/m$. The seed is the starting state $X_0$. The update is a function, so the seed determines every later state and every output. Running the generator twice from the same seed, with the same multiplier, increment and modulus, reproduces the stream exactly. That is why a simulation records its seed: a surprising path can be replayed, and a bug can be separated from ordinary Monte Carlo noise.

The seed is not itself a source of randomness. If $a$, $c$ and $m$ are known, the entire future of the stream is a calculation. Choosing a seed and then forgetting it makes the stream unreproducible. It does not make the stream unpredictable to someone who sees a few outputs and knows the recursion.

## Two seeds, one cycle

Take $a=5$, $c=1$ and $m=8$, a generator of full period $8$. Seed $1$ produces the states $1,6,7,4,5,2,3,0$, and then returns to $1$. Seed $3$ produces $3,0,1,6,7,4,5,2$, and then returns to $3$. The second list is the first list, entered two steps earlier. On a full-period generator every seed in $\{0,1,\ldots,m-1\}$ is a different starting index on one loop. Two seeds give shifted copies of one sequence, not independent streams.
""",
    "random-variable": r"""
## A number attached to each outcome

Probabilities are defined on events. Most calculations are about numbers: a count, a lifetime, a sample mean. A random variable is the function that turns an outcome into the number. Let $\Omega$ be the [sample space](sample-space.qmd), the set of outcomes $\omega$. A random variable is a function $X$ from $\Omega$ to $\mathbb{R}$. For each real $x$ the set $\{\omega:X(\omega)\le x\}$ must be an [event](event.qmd), so that $\mathbb{P}(X\le x)$ is defined. That requirement is what lets a distribution function exist. The randomness sits in which outcome occurs. The function $X$ itself is fixed. Once $\omega$ is known, $X(\omega)$ is an ordinary number.

If $g$ is a measurable real function, $g(X)$ is again a random variable. Two random variables on the same $\Omega$ are functions of the same outcome, so they can move together.

## Heads in two tosses

Toss a fair coin twice, independently. Then $\Omega=\{\mathrm{HH},\mathrm{HT},\mathrm{TH},\mathrm{TT}\}$, and each outcome has probability $1/4$. Let $X$ be the number of heads: $X(\mathrm{HH})=2$, $X(\mathrm{HT})=X(\mathrm{TH})=1$ and $X(\mathrm{TT})=0$. The event $\{X=1\}$ equals $\{\mathrm{HT},\mathrm{TH}\}$ and has probability $1/2$. The event $\{X\le 1\}$ equals $\{\mathrm{HT},\mathrm{TH},\mathrm{TT}\}$ and has probability $3/4$. The expectation is $\mathbb{E} X=0\cdot\tfrac14+1\cdot\tfrac12+2\cdot\tfrac14=1$. The indicator $I$ of heads on the first toss equals $1$ on $\{\mathrm{HH},\mathrm{HT}\}$ and $0$ otherwise: it is dependent with $X$ because $\mathbb{P}(I=1,X=2)=1/4\neq\mathbb{P}(I=1)\mathbb{P}(X=2)=1/8$, whereas the indicator of the second toss is a function on the same $\Omega$ that remains independent of $I$.
""",
    "range": r"""
## A spread that uses only the two extremes

The range of a sample is the largest observation minus the smallest. For the values $4,8,9,11,13$ it equals $13-4=9$. It uses two numbers from the five-number summary and ignores the median and the two quartiles, so it says nothing about where the middle half of the sample sits. It is also the most fragile ordinary measure of spread. Replace the recorded $13$ by a mistyped $130$ and the range becomes $126$, while the median stays $9$. Taking the quartiles as the second and fourth ordered values, those quartiles stay $8$ and $11$, and the [interquartile range](interquartile-range.qmd) stays $3$. One keystroke has multiplied the range by fourteen and left the robust summary unchanged. For a skewed or dirty sample the interquartile range is the spread to lead with. The range describes the observed extremes. It is not a stable scale parameter.

## When the extremes are the question

The range is the right summary when the extremes themselves matter: the gap between the smallest and largest rainfall in a record, or the gap between the smallest and largest part in a batch. It is a poor stand-in for the standard deviation of a normal sample. One contaminated point moves it by an arbitrary amount, and it does not settle down with sample size in the way the sample standard deviation does. A range many times the interquartile range is a signal that the tails, not the centre, dominate the spread. The next step is to look at those two endpoints.
""",
    "rank-bound": r"""
## Centring spends one dimension

The sample covariance $S$ is built from $n$ centred rows in $\mathbb{R}^p$. Let $X_c$ be the $n\times p$ matrix with those rows. Then $A=X_c^\top X_c$ and $S=A/(n-1)$ have the same rank as $X_c$. The rows of $X_c$ sum to zero, because each column was centred, so those rows lie in the subspace of $\mathbb{R}^n$ orthogonal to the all-ones vector. That subspace has dimension $n-1$. The rows also lie in $\mathbb{R}^p$, so

$$
\operatorname{rank}(S)\le\min(n-1,p).
$$

Hence $S$ can be invertible only when $p\le n-1$ and the centred rows actually span $\mathbb{R}^p$. Collinear columns make the rank still smaller.

## What fails when the bound is tight

Three observations on five variables give $\operatorname{rank}(S)\le 2$. At least three eigenvalues of $S$ are zero, and $S^{-1}$ does not exist. A [squared Mahalanobis distance](squared-mahalanobis-distance.qmd), Hotelling's $T^2$, and an unregularised Gaussian discriminant rule all ask for that inverse. The Gaussian likelihood at a positive-definite population covariance is still defined. What fails is the unrestricted maximiser over positive-definite covariance matrices: the likelihood is unbounded above, so no maximiser exists. Centring $G$ nonempty groups, as in a [pooled covariance](pooled-covariance.qmd), spends one dimension per group and leaves rank at most $n-G$. For $n=100$ and $G=2$ the pooled matrix has rank at most $98$. In cross-validation the same bounds apply to each training fold, whose row count is smaller than $n$. A ridge penalty or a pseudoinverse changes the procedure; it does not restore an inverse that the rank forbids.
""",
    "rank-distance": r"""
## Order, with the spacing thrown away

Euclidean distance changes when one coordinate is rewritten in new units, and a single huge value can dominate it. The rank distance of Olshen (1977) and Devroye (1978) keeps the order on each coordinate and discards the spacing. Pool the $n$ training values of coordinate $j$ with the query's value, rank them from $1$ to $n+1$, and write $r_i^{(j)}$ and $r^{(j)}$ for the training point and the query. The distance is the worst coordinate disagreement,

$$
\rho(x,x_i)=\max_{1\le j\le p}\bigl|r_i^{(j)}-r^{(j)}\bigr|.
$$

Any strictly increasing transformation of a single coordinate leaves every rank, and therefore $\rho$, unchanged. The values are integers, so ties are common and are usually broken by a random order among the tied neighbours.

## Three training points and one query

Training points $(1,10)$, $(2,0)$ and $(4,5)$, and query $(3,7)$, give four numbers on each axis. On the first axis the ordered values are $1,2,3,4$, so the query has rank $3$ and the training ranks are $1,2,4$. Absolute gaps: $2,1,1$. On the second axis the ordered values are $0,5,7,10$, so the query has rank $3$ and the training ranks are $4,1,2$. Absolute gaps: $1,2,1$. The coordinate-wise maxima are $2$, $2$ and $1$. The nearest neighbour in $\rho$ is the third training point. The construction has bought invariance by ignoring spacing. If two units of the first coordinate are known to be equivalent to one unit of the second, the right-hand modification is to rescale the coordinates and then use an ordinary distance. Ranks answer a different question from that equivalence.
""",
    "reading-a-log-linear-coefficient": r"""
## Hold the other covariates fixed, then multiply

Under a log link the mean is $\mu=\exp(\beta_0+\beta_1 x_1+\beta_2 x_2)$. Increase $x_1$ by one unit and keep $x_2$ fixed. The mean is multiplied by $e^{\beta_1}$. The sentence uses the link, not a particular random component: Poisson, quasi-Poisson and gamma log-linear models share it. The intercept is a different kind of number. $\exp(\beta_0)$ is the mean when every covariate equals zero. If zero is not a situation in the design, the intercept recentres the fit and is not a rate to publish. A coefficient is compared with its [standard error](standard-error.qmd), not with the raw size of the number.

## The unit of $x$ is part of the coefficient

Take $\log\mu=0.1+0.02x_1-0.5x_2$, with $x_1$ a speed in kilometres per hour and $x_2$ equal to $1$ on a wet road. Then $e^{0.02}\approx 1.020$: about $2\%$ more expected events per extra kilometre per hour, at a fixed road condition. Ten kilometres per hour is not ten times that percentage. The step of $10$ has coefficient $0.20$ and factor $e^{0.2}\approx 1.22$, about $22\%$. The wet-road factor is $e^{-0.5}\approx 0.61$, so at the same speed a wet road has about $61\%$ of the dry-road mean. The intercept $e^{0.1}\approx 1.11$ is the mean at speed $0$ on a dry road. If every observed speed is near $40$ or above, that intercept lies outside the design. Comparing the raw numbers $0.02$ and $-0.5$ as if they were effects on a common scale confuses a per-kilometre slope with a wet-versus-dry contrast. Rescale each covariate to a step that the science cares about, then compare the factors.
""",
    "recurrence-and-period": r"""
## Coming back, and coming back on a lattice

From a state $i$, two separate questions matter. Does the chain return, and if it does, are the possible return times locked to a rigid step? Recurrence answers the first. The period answers the second. Communicating states share both.

Let $T_i^{+}=\inf\{n\ge 1:X_n=i\}$ be the first return time to $i$. The chain is recurrent at $i$ when it returns with probability $1$, that is $\mathbb{P}_i(T_i^{+}<\infty)=1$, and transient otherwise. A finite mean return, $\mathbb{E}_i T_i^{+}<\infty$, is positive recurrence. An infinite mean return, despite returning forever, is null recurrence. The period is $d(i)=\gcd\{n\ge 1:p_{ii}^{(n)}>0\}$, and $d(i)=1$ means aperiodic. In a finite closed class every state is positive recurrent. Null recurrence needs an infinite state space. The simple symmetric random walk on the integers returns to the origin with probability $1$, but the mean return time is infinite, so the origin is null recurrent.

## Mean return and stationary weight

On a positive recurrent state the stationary mass, when the chain is irreducible, is the reciprocal mean return, $\pi_i=1/\mathbb{E}_i T_i^{+}$. Deterministic alternation between two states has period $2$, mean return $2$, and $\pi_i=1/2$. Both states are positive recurrent, yet $p_{ii}^{(n)}$ oscillates and does not converge. A self-loop, or any pair of return lengths with gcd $1$, makes the class aperiodic and restores convergence of $p_{ij}^{(n)}$ on a finite irreducible chain. Period blocks that limit and leaves the occupation identity intact. See [transient and recurrent states](transient-and-recurrent-states.qmd) for the reading in terms of the number of visits.
""",
    "regression-slope": r"""
## Change in the mean per unit of $x$

In the straight line $\mathbb{E} Y=\beta_0+\beta_1 x$, the slope $\beta_1$ is the change in the mean response when the explanatory variable increases by one unit. The $x$ values are treated as fixed. The slope is a property of that conditional mean. It is not, by itself, the effect of intervening to change $x$.

With data $(x_i,Y_i)$ for $i=1,\ldots,n$, write $\overline x$ and $\overline Y$ for the two averages, $S_{xx}=\sum_i(x_i-\overline x)^2$ and $S_{xY}=\sum_i(x_i-\overline x)(Y_i-\overline Y)$. The [least-squares](ordinary-least-squares.qmd) slope and intercept are

$$
\widehat\beta_1=\frac{S_{xY}}{S_{xx}},\qquad\widehat\beta_0=\overline Y-\widehat\beta_1\overline x,
$$

provided $S_{xx}>0$. If every $x_i$ is equal, then $S_{xx}=0$ and the data contain no information about a change in $x$. The fitted slope is a slope on the scale that was actually used. A fit of $\log Y$ on $x$ estimates a change in the mean of the logarithm; exponentiating multiplies the conditional geometric mean of $Y$, and multiplies $\mathbb{E}[Y\mid x]$ only when the mean of the exponentiated error does not depend on $x$.

## Three points, and the regression the other way

For the points $(0,0)$, $(1,0)$ and $(2,1)$, one finds $\overline x=1$, $\overline y=1/3$, $S_{xx}=2$ and $S_{xY}=1$. Thus $\widehat\beta_1=1/2$ and $\widehat\beta_0=1/3-1/2=-1/6$. The sum of squared $y$-deviations is $S_{YY}=2/3$. The least-squares slope of $x$ on $y$ is $S_{xY}/S_{YY}=3/2$. The reciprocal of $1/2$ is $2$, and $3/2\neq 2$. The two slopes answer different questions. Each [regression](regression-effect.qmd) is pulled towards the mean of its own response. Under the normal linear model the pivot $(\widehat\beta_1-\beta_1)/(S/\sqrt{S_{xx}})$ has a $t$ distribution on $n-2$ degrees of freedom, where $S^2$ is the residual mean square on that same denominator.
""",
    "response-variable": r"""
## The variable being explained

A regression describes one variable given the others. The response is that variable: $Y$ before it is observed, and $y$ once a value is in hand. The [explanatory variables](explanatory-variable.qmd) are treated as given. Simple linear regression specifies the conditional mean $\mathbb{E}(Y_i\mid x_i)=\beta_0+\beta_1 x_i$. The slope of $Y$ on $x$, and the slope of $x$ on $Y$, are different functions of the scatter.

Galton took the son's height as the response and the parents' height as the explanatory variable (Galton, 1886). The fitted slope is smaller than the slope that would preserve deviations from the mean: unusually tall parents have children who are, on average, less unusually tall. He called the pattern regression towards mediocrity. Putting the parents' height on the response side asks for a different conditional mean. The [regression effect](regression-effect.qmd) follows whichever variable is the response.

## Axes swapped, and a change of scale

For the points $(0,0)$, $(1,0)$ and $(2,1)$, write $S_{xx}=\sum_i(x_i-\overline x)^2=2$, $S_{YY}=\sum_i(y_i-\overline y)^2=2/3$ and $S_{xY}=1$. The slope of $y$ on $x$ is $S_{xY}/S_{xx}=1/2$. The slope of $x$ on $y$ is $S_{xY}/S_{YY}=3/2$. The reciprocal of $1/2$ is $2$, so the two fitted lines are not inverses of each other.

Scale is part of the same choice. A fit of $\log y$ models the conditional mean of the logarithm, and the slope and the errors belong to that scale. A straight line on the raw response can miss that mean. The [logit](logit-link.qmd) of a probability is a response of the same kind: the linearity lives on the transformed scale.
""",
    "sample-size-for-a-confidence-interval": r"""
## A half-width chosen before the data arrive

For a normal mean with known standard deviation $\sigma$, the level $1-\alpha$ interval has half-width $z_{1-\alpha/2}\,\sigma/\sqrt{n}$, where $z_{1-\alpha/2}$ is the standard normal quantile of order $1-\alpha/2$. Call a target half-width $w>0$. The smallest $n$ that makes the half-width at most $w$ is

$$
n\ge\left(\frac{z_{1-\alpha/2}\,\sigma}{w}\right)^2,
$$

with $n$ the least integer satisfying the inequality. The bound scales with $1/w^2$. Halving the target multiplies the required $n$ by four. The population size does not appear. The calculation treats the observations as independent, which matches an infinite population or sampling with replacement. Sampling without replacement from a small population reduces the variance of the mean, so the same $w$ can be reached with a smaller $n$. If the $\sigma$ used in planning is smaller than the truth, the interval eventually computed is wider than the one that was ordered.

## Two units, then one unit, then a proportion

Take $\sigma=10$ and a $95\%$ interval, using $z_{0.975}=1.96$. For $w=2$, the bound is $(1.96\times 10/2)^2=96.04$, so $n\ge 97$. For $w=1$ the bound is $384.16$, so $n\ge 385$, four times the continuous bound and almost four times the integer sample size. For a proportion, $p(1-p)\le 1/4$, with equality at $p=1/2$. Replacing $\sigma$ by $1/2$ gives the conservative rule $n\ge z_{1-\alpha/2}^2/(4w^2)$. A margin of $0.05$ at $95\%$ confidence needs $n\ge 1.96^2/(4\times 0.05^2)=384.16$, hence $385$ people. If $p$ is known to lie near $0$ or $1$, the worst-case $n$ is larger than necessary. The [interval](confidence-interval.qmd) reported later still has random endpoints; choosing $n$ fixes the planned half-width, not the numerical error of one future sample.
""",
    "sampling-distribution-of-the-ols-estimator": r"""
## A fixed linear image of the error vector

Start from the Gaussian linear model $\boldsymbol{Y} = \boldsymbol{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$, with $\boldsymbol{\varepsilon} \mid \sigma^2 \sim \operatorname{N}_n(\boldsymbol{0}, \sigma^2 \boldsymbol{I}_n)$. The design $\boldsymbol{X}$ is $n \times p$ of rank $p$ and is treated as fixed, the coefficient vector $\boldsymbol{\beta}$ lies in $\mathbb{R}^{p}$, and the error variance satisfies $\sigma^2 > 0$. [Ordinary least squares](ordinary-least-squares.qmd) defines $\widehat{\boldsymbol{\beta}} = (\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{-1}\boldsymbol{X}^{\mathsf{T}}\boldsymbol{Y}$. Substitute the model equation. The design term cancels and

$$
\widehat{\boldsymbol{\beta}} = \boldsymbol{\beta} + (\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{-1}\boldsymbol{X}^{\mathsf{T}}\boldsymbol{\varepsilon}.
$$

A linear image of a centred normal vector is centred normal, so the conditional expectation of $\widehat{\boldsymbol{\beta}}$ is $\boldsymbol{\beta}$. With $A = (\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{-1}\boldsymbol{X}^{\mathsf{T}}$, the covariance is $\sigma^2 A A^{\mathsf{T}} = \sigma^2 (\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{-1}$. Thus $\widehat{\boldsymbol{\beta}}$, given $\boldsymbol{\beta}$, $\sigma^2$, and $\boldsymbol{X}$, is $\operatorname{N}_p$ with that mean and covariance. The randomness is the unobserved error. This is a sampling distribution, not a posterior distribution of $\boldsymbol{\beta}$.

## Residual length on $n-p$ degrees of freedom

Let $\boldsymbol{H} = \boldsymbol{X}(\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{-1}\boldsymbol{X}^{\mathsf{T}}$ and set $\widehat{\boldsymbol{e}} = (\boldsymbol{I}-\boldsymbol{H})\boldsymbol{\varepsilon}$, so that $\operatorname{SSE} = \lVert\widehat{\boldsymbol{e}}\rVert_2^2$. The matrix $\boldsymbol{I}-\boldsymbol{H}$ projects onto the complement of the column space of $\boldsymbol{X}$, a subspace of dimension $n-p$. The squared length of a standard normal vector in that subspace follows a [chi-squared distribution](chi-squared-distribution.qmd) on $n-p$ degrees of freedom, and therefore $\operatorname{SSE}/\sigma^2 \sim \chi^2_{n-p}$. Also $\boldsymbol{X}^{\mathsf{T}}(\boldsymbol{I}-\boldsymbol{H}) = \boldsymbol{0}$, so $\widehat{\boldsymbol{\beta}}$ and $\widehat{\boldsymbol{e}}$ are uncorrelated. Jointly normal uncorrelated vectors are independent, and $\widehat{\boldsymbol{\beta}}$ is independent of $\operatorname{SSE}$.
""",
    "sampling-distribution-of-the-regression-estimators": r"""
## Where the scatter of the fitted line comes from

Under [simple linear regression](simple-linear-regression.qmd), $Y_i=\beta_0+\beta_1 x_i+\varepsilon_i$ with the $\varepsilon_i$ independent and $\operatorname{N}(0,\sigma^2)$, and with fixed $x_i$ that are not all equal. Write $S_{xx}=\sum_i(x_i-\overline x)^2$, $S_{xY}=\sum_i(x_i-\overline x)(Y_i-\overline Y)$ and $\widehat\beta_1=S_{xY}/S_{xx}$, $\widehat\beta_0=\overline Y-\widehat\beta_1\overline x$. Then

$$
\widehat\beta_1\sim\operatorname{N}\!\left(\beta_1,\frac{\sigma^2}{S_{xx}}\right),\qquad
\widehat\beta_0\sim\operatorname{N}\!\left(\beta_0,\frac{\sigma^2\sum_i x_i^2}{nS_{xx}}\right).
$$

The residual mean square $S^2=\frac1{n-2}\sum_i(Y_i-\widehat\beta_0-\widehat\beta_1 x_i)^2$ satisfies $(n-2)S^2/\sigma^2\sim\chi^2_{n-2}$, independently of $(\widehat\beta_0,\widehat\beta_1)$. In particular $S^2$ is unbiased for $\sigma^2$. Also $\widehat\beta_1$ is independent of $\overline Y$. The slope variance falls as $S_{xx}$ grows: spread-out $x$ values pin the line down. [Unbiasedness](least-squares-estimators-are-unbiased.qmd) of $\widehat\beta_0$ and $\widehat\beta_1$ needs only the linear mean. The normal laws, the chi-squared residual, and the $t$ pivot $(\widehat\beta_1-\beta_1)/(S/\sqrt{S_{xx}})$ on $n-2$ [degrees of freedom](degrees-of-freedom.qmd) need normality and a constant variance.

If the $x_i$ are themselves random, the statement applies conditionally on the observed design. A tiny $S_{xx}$ leaves the slope almost unidentified. Non-normal errors can keep the coefficients unbiased while replacing the exact $t$ reference by an approximation.

## Five design points

For $x=1,2,3,4,5$, one has $\overline x=3$ and $S_{xx}=10$. With $\sigma=2$ the standard deviation of $\widehat\beta_1$ is $2/\sqrt{10}\approx 0.632$. Moving the same five points to $1,1,3,5,5$ raises $S_{xx}$ to $16$ and lowers that standard deviation to $2/4=0.5$. The sample size and the error variance are unchanged. Only the spread of $x$ has changed, and the conditional normal laws use those two values of $S_{xx}$.
""",
    "sampling-law-of-the-normal-mean-and-scatter": r"""
## Three facts that the normal sample supplies together

Draw $\mathbf{X}_1,\ldots,\mathbf{X}_n$ independently from $\operatorname{N}_p(\boldsymbol{\mu},\Sigma)$ with $\Sigma$ positive definite. The sample mean $\overline{\mathbf{X}}$ is exactly $\operatorname{N}_p(\boldsymbol{\mu},\Sigma/n)$, because it is a linear image of the stacked sample. The corrected cross-product matrix

$$
A=\sum_{i=1}^{n}(\mathbf{X}_i-\overline{\mathbf{X}})(\mathbf{X}_i-\overline{\mathbf{X}})^\top
$$

is exactly [Wishart](wishart-distribution.qmd), $A\sim W_p(\Sigma, n-1)$, and $\overline{\mathbf{X}}$ is independent of $A$. These are the multivariate forms of three univariate facts: the sample mean is normal, $(n-1)s^2/\sigma^2$ is chi-squared on $n-1$ degrees of freedom, and the mean is independent of the variance. The degrees of freedom are $n-1$ because the sample mean was subtracted. The expectation $\mathbb{E}(A)=(n-1)\Sigma$ follows from the Wishart construction, and it also follows from expanding the products without normality. The independence and the Wishart shape use normality.

## Where a later test spends the independence

Hotelling's $T^2$ is a quadratic form in $\overline{\mathbf{X}}-\boldsymbol{\mu}_0$, scaled by $S^{-1}$ with $S=A/(n-1)$. Independence of the normal mean and the Wishart matrix is what converts that ratio into an exact $F$ law under the null. For a numerical scale, $n=10$ and $p=2$ give $A\sim W_2(\Sigma, 9)$, so $\mathbb{E}(A)=9\Sigma$, while $\operatorname{Var}(\overline{\mathbf{X}})=\Sigma/10$. Drop normality and keep a finite $\Sigma$, and $\overline{\mathbf{X}}$ is still unbiased with covariance $\Sigma/n$. The [multivariate central limit theorem](multivariate-central-limit-theorem.qmd) then makes $\sqrt{n}(\overline{\mathbf{X}}-\boldsymbol{\mu})$ approximately normal. It does not make $A$ Wishart, and it does not make $A$ independent of $\overline{\mathbf{X}}$, so the exact $F$ calibration is withdrawn.
""",
    "scaling": r"""
## Units that rewrite the covariance

Covariance principal components maximise sample variance. Variance depends on the unit of measurement. A height recorded in metres with variance $0.01$ has variance $100$ if the same heights are written in centimetres, because each deviation is multiplied by $100$ and the square multiplies by $10^4$. A weight recorded in kilograms with variance $100$ then dominates the leading component when height is in metres, and it need not dominate when height is in centimetres. The physical cloud is the same. The matrix $S$ is not. Standardising each nonconstant column to sample variance $1$ produces correlation principal components. Each standardised coordinate is offered to the variance criterion on the same scale.

## The training location and scale travel with the rule

Suppose a column has training mean $4$ and training standard deviation $2$. The value $6$ becomes $(6-4)/2=1$. A new observation is transformed with those same numbers. Recomputing the mean and the standard deviation on a set that includes the new point, or on a held-out fold, changes the metric that the components were defined in. The choice to standardise is a modelling choice. Coordinates that are already in the same unit, and whose absolute differences are meaningful, can be left on the covariance scale. A pure-noise column, once standardised, has variance $1$ and can enter the leading components when many such columns are present. Record whether $S$ was the covariance or the correlation matrix, and store the training means and scales beside the loadings.
""",
    "scatterplot": r"""
## The shape of the cloud, before a single number

Two quantitative measurements on the same units are first a cloud of points, one point per unit. A scatterplot is that cloud. It shows whether the relation is straight, curved, fan-shaped or flat, whether it runs upward or downward, and whether a few points sit apart from the rest. The [sample correlation](sample-correlation-coefficient.qmd) then compresses the linear part of the picture into one number between $-1$ and $1$. The compression is the risk. Correlation misses a U-shape, it is pulled by a point far out in the covariate, and it says nothing about a strong relation that is not monotone.

## A perfect curve whose correlation is zero

Take $x=-2,-1,0,1,2$ and $y=4,1,0,1,4$. The points lie on the parabola $y=x^2$. The sample means are $\bar x=0$ and $\bar y=2$, and the products $(x_i-\bar x)(y_i-\bar y)$ sum to $-4+1+0-1+4=0$. The sample correlation is exactly $0$. A test of that correlation correctly reports no linear association, and it misses a deterministic curve. A different failure is an otherwise straight cloud plus one point far to the right. That single point can move a fitted slope from nearly flat to steep, and the correlation moves with it. Coarse recording creates a third, practical problem. When both variables are stored on a grid, many units share one coordinate and the plot understates the pile. A small jitter used only for drawing separates the pile visually. The jitter is not a new measurement, and it is not the series on which the correlation is computed.
""",
    "seasonality": r"""
## A period fixed by the clock

Seasonality is a repeating pattern whose period is known from the way the series was collected. Monthly accidents have period $12$. Weekday traffic has period $7$. Hourly load has period $24$. The period is a property of the calendar, not a lag discovered by searching every integer. In the [autocorrelation](autocorrelation-function.qmd) it shows up as a revival at the period and at its multiples: lags $12$ and $24$ for monthly data, after the short-lag correlation has already fallen. An ordinary first difference does not remove it. If every January is high and every July is low, $X_t-X_{t-1}$ is still high whenever the series enters January and low whenever it enters July.

## What a twelve-month difference actually erases

The seasonal difference $\nabla_{12}X_t=X_t-X_{t-12}$ subtracts each month from the same month a year earlier. A pure wave $\cos(2\pi t/12)$ is removed, because the wave one year earlier is the same number. A linear [trend](trend.qmd) is removed as a slope: $(a+bt)-(a+b(t-12))=12b$, a constant, so the differenced series has a new mean and no remaining straight-line drift. A rhythm whose length is not $12$ is not removed. A business swing of several years, or a cosine of period $8$ months, is still in $\nabla_{12}X_t$. Seasonal autoregressive and moving-average terms then describe whatever correlation is left at lag $12$ after that difference. Fitting them to a series whose repetition has no fixed period spends the parameters on a calendar the data do not possess, and the forecast keeps repeating a year that was not the structure.
""",
    "sensitivity-and-specificity": r"""
## Row rates from a confusion matrix

For a binary label, write $N_{11}$ for the number of true positives, $N_{10}$ for the false negatives, $N_{01}$ for the false positives and $N_{00}$ for the true negatives, in a [confusion matrix](confusion-matrix.qmd) on a stated set of cases. Sensitivity is the true-positive rate

$$
\frac{N_{11}}{N_{11}+N_{10}},
$$

the proportion of truly positive cases that the classifier labels positive. Specificity is the true-negative rate $N_{00}/(N_{00}+N_{01})$. On $50$ diseased cases of whom $40$ are detected, and $200$ healthy cases of whom $10$ are called diseased, the sensitivity is $40/50=0.80$ and the specificity is $190/200=0.95$. The accuracy is $(40+190)/250=0.92$. These two rates are row proportions. They do not contain the prevalence. The [positive predictive value](positive-predictive-value.qmd), the probability of disease given a positive call, does.

## The same rates at a new prevalence

Keep sensitivity $0.80$ and specificity $0.90$, and change the population to $10$ diseased cases and $190$ healthy cases. The expected counts are $8$ true positives and $19$ false positives, so the positive predictive value is $8/(8+19)=8/27\approx 0.296$. At prevalence $1/2$, with $100$ cases of each kind, the same rates give $80$ true positives and $10$ false positives, and the predictive value is $80/90\approx 0.889$. A threshold on a continuous score moves the two rates in opposite directions. With diseased scores $0.2,0.6,0.8$ and healthy scores $0.1,0.3,0.4$, calling scores at or above the cut positive gives sensitivity $2/3$ and specificity $1$ at threshold $0.5$, and sensitivity $1$ and specificity $1/3$ at threshold $0.2$.
""",
    "sequential-coherence": r"""
## The posterior after one batch is the next prior

Let a binomial probability $\theta$ have a $\operatorname{Beta}(\alpha, \beta)$ prior, with $\alpha > 0$ and $\beta > 0$, and let the batches be conditionally independent given $\theta$. Batch $i$ contributes $x_i$ successes in $n_i$ trials. The first likelihood multiplies the prior by $\theta^{x_1}(1-\theta)^{n_1-x_1}$, so

$$
\theta \mid x_1 \sim \operatorname{Beta}(\alpha+x_1,\, \beta+n_1-x_1).
$$

Coherence requires that this posterior be used as the prior for the next batch. The second binomial likelihood then adds $x_2$ to the first shape and $n_2-x_2$ to the second. The result is $\operatorname{Beta}(\alpha+x_1+x_2,\, \beta+n_1+n_2-x_1-x_2)$, which is also the posterior obtained by pooling the counts and updating once. A $\operatorname{Beta}(1,1)$ prior, followed by $3$ successes in $10$ trials and then by $2$ successes in $5$ trials, ends at $\operatorname{Beta}(6, 11)$. Five successes in fifteen trials, updated in one step from the same prior, end at the same distribution.

## Order does not matter; replacing the prior does

Given $\theta$, independent batches multiply, and addition of the success and failure counts does not depend on which batch is processed first. The further content of sequential coherence is that the analyst must not invent a fresh prior after seeing the first batch. Replacing $\operatorname{Beta}(\alpha+x_1, \beta+n_1-x_1)$ by some other distribution, because that batch was surprising, yields a final posterior that does not come from updating the prior declared before the data (even if it coincides with the pooled update of a different prior chosen after seeing batch $1$). The identity also fails when the batches are not conditionally independent given $\theta$, because the second factor is then not the ordinary binomial likelihood $p(x_2 \mid \theta)$.
""",
    "sigmoid-function": r"""
## A smooth step from the real line onto $(0,1)$

A threshold unit outputs $0$ or $1$ according to the sign of a linear score $z=w^\top x+b$. The jump has derivative zero on each open half-space, so a gradient method receives no signal from it. The logistic sigmoid

$$
g(z)=\frac{1}{1+e^{-z}}
$$

is a smooth stand-in, with $g(z)\in(0,1)$, $g(0)=1/2$ and $g(-z)=1-g(z)$. Its derivative is $g'(z)=g(z)\{1-g(z)\}$, largest at $z=0$, where it equals $1/4$. At $z=2$,

$$
g(2)=\frac{1}{1+e^{-2}}\approx 0.881,
\qquad
g'(2)\approx 0.881\times 0.119\approx 0.105.
$$

Once $|z|$ is large the output has nearly settled and the derivative is small, so a squared-error update that multiplies by $g'(z)$ moves the weights only a little. The unit is then called saturated.

## The one-layer case is logistic regression

With no hidden layer, a single sigmoid output $o=g(w^\top x+b)$ is the mean function of [binary logistic regression](binary-logistic-regression.qmd), and $w^\top x+b$ is the log-odds. Fitting by the Bernoulli negative log-likelihood uses the gradient $(o-y)x$, in which the factor $g'(z)$ has cancelled. Fitting by squared error keeps a factor $o(1-o)$. The two criteria share the sigmoid and differ in the loss. A hidden layer places further sigmoids between the input and this output, and the same derivative $g(1-g)$ is the local factor that backpropagation carries. Any other smooth step with the same qualitative shape can replace $g$ in a network; the logistic choice is the one whose derivative is $g(1-g)$ and whose one-layer likelihood is the logistic likelihood.
""",
    "sign-test": r"""
## A binomial count of directions

Paired measurements $(X_i,Y_i)$, $i=1,\ldots,n$, need not have normal differences. Let $D_i=Y_i-X_i$ and let $N$ be the number of pairs with $D_i>0$, after ties $D_i=0$ are discarded and $n$ is reduced to the number of untied pairs. The null hypothesis $\mathbb{P}(D_i>0)=1/2$, for continuous independent differences, says that the median of $D_i$ is $0$. It does not say that the mean of $D_i$ is $0$. A skewed continuous law can have median $0$ and a nonzero mean, and a law with no mean at all can still have median $0$. Under the null, $N\sim\operatorname{Bin}(n,1/2)$, so the test is a [binomial test](binomial-test.qmd) at $p=1/2$. Large $N$ is evidence that positive differences predominate. The statistic ignores the sizes of the differences. A [paired $t$ test](paired-samples.qmd) on the same differences assumes normal differences and uses the magnitudes to test the mean. When that assumption is right, the $t$ test is more powerful. One huge outlier moves the $t$ statistic sharply and moves the sign count by one pair. Coarse measurements produce many ties, and discarding them shrinks $n$.

## Ten increases out of twelve

Suppose $10$ of $12$ untied pairs have $Y_i>X_i$, and the alternative is $\mathbb{P}(D_i>0)>1/2$. Under the null,

$$
\mathbb{P}(N\ge 10)=\frac{\binom{12}{10}+\binom{12}{11}+\binom{12}{12}}{2^{12}}=\frac{66+12+1}{4096}=\frac{79}{4096}\approx 0.019.
$$

A one-sided level-$0.05$ test rejects. The same count in the other direction, $N\le 2$, would be just as extreme for a two-sided alternative, and the two-sided $p$-value would double. The [median](median.qmd) null is still the hypothesis being tested. A large positive mean produced by a few enormous jumps, with half the differences negative, need not make $N$ large.
""",
    "signed-distance": r"""
## From a functional score to a Euclidean distance

The hyperplane $w^\top x+b=0$, with $w\neq 0$, has normal vector $w$. Write a point as $x=x_\perp+r\, w/\|w\|$, where $x_\perp$ lies on the hyperplane and $r$ is the signed length along the unit normal. Substitute into the score:

$$
w^\top x+b=w^\top x_\perp+b+r\|w\|=r\|w\|,
$$

so $r=(w^\top x+b)/\|w\|$. The absolute value $|r|$ is the Euclidean distance from $x$ to the plane. The sign of $r$ says which side $x$ is on. The raw score $w^\top x+b$ equals that distance only when $\|w\|=1$.

## A plane $x_1=2$, and the unit-margin slab

Take $w=(3,0)^\top$ and $b=-6$. The plane is $3x_1-6=0$, that is $x_1=2$. The point $(5,4)$ has score $15-6=9$ and signed distance $9/3=3$, which matches the horizontal gap from $x_1=2$ to $x_1=5$. The parallel lines $w^\top x+b=-1$ and $w^\top x+b=1$ are $3x_1-6=\mp 1$, so $x_1=5/3$ and $x_1=7/3$. They are $2/3$ apart, and $2/\|w\|=2/3$. Rescaling $(w,b)$ by a positive constant leaves the plane $w^\top x+b=0$ unchanged and multiplies the numerator and the denominator of $r$ by the same constant. A maximum-margin method uses this geometry: the hard-margin constraints $y_i(w^\top x_i+b)\ge 1$ place every training point outside the slab, and the slab width is $2/\|w\|$. Maximising the width is the same problem as minimising $\|w\|$.
""",
    "single-complete-and-average-linkage": r"""
## Three ways to turn point distances into cluster distances

[Agglomerative clustering](hierarchical-clustering.qmd) starts with each point alone and repeatedly merges the two clusters with the smallest inter-cluster distance. The pointwise distance $d$ is already defined. A linkage extends it to a pair of clusters $D_1$ and $D_2$. Single linkage uses the closest cross-pair, so the clusters count as close as soon as they touch. Complete linkage uses the farthest cross-pair, so a merge is cheap only when every cross-pair is close. Group-average linkage uses the mean of all $|D_1|\,|D_2|$ cross-pairs. The mean of the distances is a different number from the distance between the two cluster means. Average linkage is the mean of the cross-pairs. Centroid linkage, the distance between means, can produce an inversion in which a later merge sits at a smaller height than an earlier one.

## Three points on a line

For the points $0$, $1$ and $10$ with absolute distance, every linkage first merges $0$ with $1$, at height $1$. Single linkage then joins $10$ at height $9$, the gap from $1$ to $10$. Complete linkage joins $10$ at height $10$, the gap from $0$ to $10$. Average linkage joins $10$ at height $(9+10)/2=9.5$. The single-linkage height follows a chain of neighbours. The complete-linkage height is the diameter of the merged set. One distant point raises that diameter and can postpone a merge that the other points would have accepted. Average linkage sits between those two readings of the same three distances. A linkage that uses only $d$ can run on an arbitrary dissimilarity.
""",
    "soft-margin-primal": r"""
## A priced shortfall from the margin

Hard-margin separation asks for $y_i(w^\top x_i+b)\ge 1$ for every training index $i$, with labels $y_i\in\{-1,+1\}$. Overlapping classes make that list of inequalities infeasible. A slack $\xi_i\ge 0$ records how far case $i$ falls short of functional margin $1$: the constraint becomes $y_i(w^\top x_i+b)\ge 1-\xi_i$. The primal cost is

$$
\Phi(w,\xi)=\frac12 w^\top w+C\sum_{i=1}^{n}\xi_i.
$$

The first term keeps the slab $2/\|w\|$ wide. The second charges $C$ per unit of total slack. At the optimum the slack is exactly the [hinge](hinge-loss.qmd), $\xi_i=\max\{0,\,1-y_i(w^\top x_i+b)\}$. A point with functional margin $1.5$ has $\xi_i=0$ and does not enter the sum. A point with functional margin $0.3$ has smallest feasible slack $0.7$.

## The cost $C$, and one feasible value

Take a candidate with $\|w\|^2=0.4$ and a single shortfall $\xi=0.7$, and set $C=2$. Then $\Phi=0.2+2\cdot 0.7=1.6$. Raising $C$ puts more weight on removing shortfalls. Lowering $C$ puts more weight on a small $\|w\|$. For separable data, a large enough $C$ recovers a hard-margin solution. For inseparable data, no finite $C$ creates a separating hyperplane that is not there. In the dual, the same $C$ appears as an upper bound $0\le\alpha_i\le C$ on the multiplier of case $i$. Cases with $\alpha_i=0$ lie outside the slab or on its boundary and do not shape $w$. Cases with $\alpha_i=C$ have functional margin at most $1$—on the boundary of the slab, inside it, or on the wrong side. The numerical value of $C$ is selected on validation data, together with any rescaling of the inputs.
""",
    "softmax-is-multinomial-logistic-regression": r"""
## Class probabilities from unrestricted scores

A network produces a score $z_k$ for each of $K$ classes. Softmax maps those scores to positive probabilities that sum to $1$,

$$
s_k=\frac{e^{z_k}}{\sum_{\ell=1}^{K} e^{z_\ell}}.
$$

Adding the same constant to every $z_k$ multiplies every exponential by the same factor and leaves $s$ unchanged, so one score may be set to zero as a reference. With no hidden layer, $z_k=\beta_k^\top x$, and the map is the [baseline-category logit](baseline-category-logit-model.qmd) model. Minimising the training [cross-entropy](cross-entropy.qmd) is then maximising the multinomial likelihood. A hidden layer replaces $x$ by a learned feature vector $h$, and the output layer is multinomial logistic regression on $h$.

## Three scores, and the two-class reduction

For scores $z=(1,0,-1)$ the exponentials are about $2.718$, $1$ and $0.368$, with sum about $4.086$. The probabilities are about $0.665$, $0.245$ and $0.090$. If the true class is the first, the cross-entropy is $-\log 0.665\approx 0.408$. Shifting the scores to $(6,5,4)$ leaves these probabilities where they were. For two classes,

$$
\frac{e^{z_1}}{e^{z_1}+e^{z_2}}=g(z_1-z_2),
$$

with $g$ the logistic sigmoid, so the second score is absorbed into a single log-odds. The probabilities are invariant to the shift. The individual coefficient vectors $\beta_k$ are not, until a reference class is fixed by $\beta_1=\mathbf{0}$. Reporting a coefficient without that convention, or without the matching feature scaling, does not identify a unique log-odds contrast.
""",
    "squared-error-is-not-the-logistic-likelihood": r"""
## Two losses on the same sigmoid

A single output $o=g(w^\top x)$ uses the logistic sigmoid $g$, and the label $y$ is $0$ or $1$. Squared error on one case is $(y-o)^2$. The Bernoulli negative log-likelihood is

$$
-\bigl(y\log o+(1-y)\log(1-o)\bigr).
$$

Both are functions of the same weights, and their gradients differ. Differentiating the square brings down $-2(y-o)$ and then the sigmoid derivative $o(1-o)$, so the weight gradient contains the product $(o-y)\,o(1-o)\,x$. Differentiating the negative log-likelihood, the factor $o(1-o)$ cancels with the derivative of $\log g$, and the gradient in the weight is $(o-y)x$. The score of the positive log-likelihood is the negative of that vector. The gradient is the direction; the descent update multiplies it by a step length and subtracts.

## Saturation

Take $y=1$, $o=0.9$ and a single input $x=1$. The negative-log-likelihood gradient in the weight is $0.9-1=-0.1$. The squared-error gradient, including the conventional factor $2$ from the square, is $-2(1-0.9)\cdot 0.9\cdot 0.1=-0.018$. Relative to the negative-log-likelihood gradient, the factor $2o(1-o)=0.18$ has shrunk the step. At $o=0.99$, $o(1-o)=0.0099$ (so $2o(1-o)\approx 0.0198$), and a saturated unit barely moves under squared error even though the probability of the observed label is still $0.99$. The negative-log-likelihood gradient at the same point is $0.99-1=-0.01$, small because the residual $o-y$ is small, and free of the second small factor. Through a [hidden layer](hidden-layer.qmd) the same distinction applies at the output: squared-error backpropagation carries $o(1-o)$ into every earlier weight, and the Bernoulli loss does not. The likelihood fit, with no hidden layer, is ordinary [logistic regression](binary-logistic-regression.qmd).
""",
    "squared-error-of-an-average": r"""
## The spread of the members is a credit

At a fixed input $x$, $T$ regression functions produce numbers $f_1(x),\ldots,f_T(x)$, and the ensemble predicts their average $f(x)$. Let $y$ be the response at this $x$. Expand the squared errors about $f(x)$. The cross term vanishes because the deviations $f_t(x)-f(x)$ sum to zero, and what remains is

$$
\bigl(f(x)-y\bigr)^2
=\frac1T\sum_{t=1}^{T}\bigl(f_t(x)-y\bigr)^2
-\frac1T\sum_{t=1}^{T}\bigl(f_t(x)-f(x)\bigr)^2.
$$

The first average on the right is the mean squared error of the members. The second is the sample variance of the members about their own average. The ensemble's squared error equals the members' average squared error, minus that variance. Diversity is an exact credit in squared error, at this $x$ and this $y$.

## Two members

Take $T=2$, $f_1(x)=3$, $f_2(x)=7$ and $y=4$. The average is $f(x)=5$, and $(5-4)^2=1$. The members' squared errors are $1$ and $9$, with mean $5$. Their squared deviations from $5$ are $4$ and $4$, with mean $4$. Then $5-4=1$, matching the ensemble. If both members predict $6$, the variance term is $0$ and the ensemble error equals the common member error, here $(6-4)^2=4$. Averaging identical functions does not reduce squared error. The identity is algebraic and holds for every $x$ and $y$. It does not say that a more variable member is a better member: a wild $f_t$ inflates the first term as well as the second. The useful members are accurate and they are accurate in different places, so that the variance term is large relative to the errors.
""",
    "squared-mahalanobis-distance": r"""
## Euclidean distance after whitening

The squared Euclidean distance $(X_1-\mu_1)^2+(X_2-\mu_2)^2$ treats one unit on each axis as equally large, and it ignores correlation. The squared Mahalanobis distance

$$
D^2=(\mathbf{X}-\boldsymbol{\mu})^\top\Sigma^{-1}(\mathbf{X}-\boldsymbol{\mu})
$$

rescales the axes by the covariance $\Sigma$. If $B$ is any matrix with $BB^\top=\Sigma$, such as a [Cholesky factor](cholesky-decomposition.qmd), then $D^2=\|B^{-1}(\mathbf{X}-\boldsymbol{\mu})\|^2$. In the whitened coordinate the law of a $\operatorname{N}_p(\boldsymbol{\mu},\Sigma)$ vector is standard normal, and $D^2$ is the squared distance from the origin in that coordinate. For a nonsingular normal, $D^2$ has a chi-squared distribution on $p$ degrees of freedom. Large $D^2$ is a point far from $\boldsymbol{\mu}$ in the metric that $\Sigma$ defines.

## Two points at the same Euclidean radius

Let $\boldsymbol{\mu}=\mathbf{0}$ and $\Sigma=\operatorname{diag}(4,1)$. The points $(2,0)$ and $(0,2)$ are both at Euclidean distance $2$ from the origin. Their squared Mahalanobis distances are

$$
\frac{2^2}{4}=1
\qquad\text{and}\qquad
\frac{2^2}{1}=4.
$$

The point on the short axis is the more unusual of the two. The inverse $\Sigma^{-1}$ is defined only when $\Sigma$ is positive definite. A sample covariance of rank less than $p$ has no inverse, and $D^2$ is then undefined until a reduced or penalised covariance is chosen. The covariance form already standardises each coordinate and keeps the correlations, since $\Sigma=DRD$ with $D=\operatorname{diag}(\sigma_1,\ldots,\sigma_p)$ makes $D^2$ equal to $\mathbf{z}^\top R^{-1}\mathbf{z}$ for $\mathbf{z}=D^{-1}(\mathbf{X}-\boldsymbol{\mu})$; substituting $R$ for $\Sigma$ without dividing by $D$ treats every raw coordinate as if its variance were already $1$. Both versions need a convention for the centre $\boldsymbol{\mu}$, and a sample plugin uses the sample mean and a chosen covariance estimator together.
""",
    "stationary-and-independent-increments": r"""
## Describing a process by how it changes

Many processes are easier to specify through their increments than through the height of the path. Two properties are often named together, and they are logically separate. One says the law of a change depends only on the length of the interval. The other says changes over disjoint intervals do not influence each other.

A process $\{X_t\}$ has stationary increments when, for each lag $h$, the difference $X_{t+h}-X_t$ has a distribution that does not depend on the time $t$. It has independent increments when, for every $t_0<t_1<\cdots<t_k$, the increments $X_{t_1}-X_{t_0},\ldots,X_{t_k}-X_{t_{k-1}}$ are independent. A [homogeneous Poisson process](homogeneous-poisson-process.qmd) has both: $N(t+h)-N(t)$ is Poisson with mean $\lambda h$, and increments over disjoint intervals are independent. A non-homogeneous Poisson process keeps independent increments, but $\mathbb{E}[N(t+h)-N(t)]=\Lambda(t+h)-\Lambda(t)$ depends on $t$ as soon as the intensity is not constant, so the increments are not stationary.

## Stationary increments are not a stationary process

A discrete-time random walk $S_n=\sum_{i=1}^{n} Y_i$ with independent and identically distributed steps has both properties on the integer clock. The block $S_{n+h}-S_n$ is a sum of $h$ steps, with a law free of $n$, and disjoint blocks use different steps. Stationary increments do not mean that the process itself is stationary. For a Poisson process, $\mathbb{E} N(t)=\lambda t$ grows with $t$, so the marginal law of $N(t)$ changes. What is stationary is the increment. Concretely, if $N$ has rate $3$, then $N(5)-N(2)$ is Poisson with mean $9$, the same law as $N(3)$, and it is independent of $N(2)$.
""",
    "stationary-distribution": r"""
## A starting law the chain never leaves

The stationary equation picks out those distributions that one step of the chain does not change. If the chain begins in such a distribution, every later time has the same distribution. On a finite irreducible chain that distribution is unique. It is the limiting distribution only when the chain is also aperiodic.

Let $P=(p_{ij})$ be a transition matrix. A probability row vector $\pi$ is stationary when $\pi P=\pi$, or, at each state $j$,

$$
\pi_j=\sum_i \pi_i p_{ij}.
$$

If $X_0$ has law $\pi$, then $X_n$ has law $\pi$ for every $n$. Existence does not give uniqueness. If states $0$ and $1$ are both absorbing, every mixture $a\delta_0+(1-a)\delta_1$ is stationary, and the long-run law depends on which absorber the path enters. A finite [irreducible](irreducible-markov-chain.qmd) chain has exactly one stationary distribution, with every entry positive, and $\pi_i=1/\mathbb{E}_i T_i^{+}$. [Detailed balance](detailed-balance.qmd) is a sufficient shortcut for solving $\pi P=\pi$. It is not necessary: a cycle can be stationary while probability circulates.

## A two-state balance

Take

$$
P=\begin{pmatrix} 0.7 & 0.3 \\ 0.6 & 0.4 \end{pmatrix}.
$$

The equation $\pi_0=0.7\pi_0+0.6\pi_1$ rearranges to $\pi_0=2\pi_1$. With $\pi_0+\pi_1=1$ one gets $\pi=(2/3,1/3)$. The second coordinate checks: $0.3\cdot(2/3)+0.4\cdot(1/3)=1/3$. This chain has a self-loop, so it is aperiodic, and $p_{ij}^{(n)}\to\pi_j$ from every start. For a periodic irreducible chain the same linear system still has a unique probability solution, and that solution is the long-run fraction of time in each state, but the one-step distributions may oscillate forever. See [finite irreducible chains](finite-irreducible-chains.qmd).
""",
    "statistic-and-estimator": r"""
## The expression may use the sample and nothing unknown

Write the random sample as $\boldsymbol{X} = (X_1,\ldots,X_n)$ and a realised sample as $\boldsymbol{x}$. A [statistic](statistic.qmd) is a function $T = T(\boldsymbol{X})$ of that vector alone. Known constants, such as the sample size or a fixed design, may appear in the formula. An unknown parameter may not. Thus $\sum_i (X_i - \mu)^2$ is not a statistic, because the unknown mean $\mu$ is inside the expression, whereas $\sum_i (X_i - \overline{X})^2$ is a statistic, because $\overline{X}$ is computed from $\boldsymbol{X}$. The sampling distribution of $T$ is still allowed to depend on the parameter. The function is free of $\theta$. The probabilities attached to its values need not be.

## Estimation is a job, not part of the definition

An [estimator](estimator.qmd) is a statistic that is used to estimate a parameter or a function of a parameter. Every estimator is a statistic, and many statistics are introduced for some other purpose. A residual vector may be a diagnostic. A test statistic may exist only to be compared with a null distribution. The sample mean can estimate a normal mean, and the sample maximum can estimate the upper endpoint of a uniform law. Sufficiency, ancillarity, and completeness are properties that a statistic may have. They are not extra clauses in the definition of an estimator. Before the data are drawn, $T(\boldsymbol{X})$ is random. Once $\boldsymbol{x}$ is observed, $T(\boldsymbol{x})$ is a number. Putting $\theta$ back into the formula, and still calling the result a statistic, confuses a computable summary of the sample with a parameter-dependent random variable such as $\sum_i(X_i-\mu)^2$: its sampling distribution is still defined, yet its numerical value cannot be evaluated from the observed sample alone.
""",
    "stochastic-process": r"""
## A random variable attached to every time

A single random variable records one measurement. A stochastic process records a measurement at every time, on one common outcome, so that questions about paths become questions about events.

Let $(\Omega,\mathcal{F},\mathbb{P})$ be a probability space, let $S$ be a state space, and let $T$ be an index set. A stochastic process is a family $\{X_t:t\in T\}$ of $S$-valued random variables on that space. If $T=\{0,1,2,\ldots\}$, time is discrete and the process is a sequence. If $T=[0,\infty)$, time is continuous. Two readings are used constantly. For fixed $t$, the map $\omega\mapsto X_t(\omega)$ is a random variable. For fixed $\omega$, the map $t\mapsto X_t(\omega)$ is a path, one realisation of the process. Events that depend on finitely many times are settled by the finite-dimensional distributions. Path properties, such as continuity or the number of jumps in a finite interval, require a version of the process and are not fixed by those margins alone. The [Kolmogorov extension theorem](kolmogorov-extension-theorem.qmd) produces a process from consistent margins. It does not produce a continuous version.

## Three processes, one definition

A [discrete-time Markov chain](discrete-time-markov-chain.qmd) is a process on a countable state space whose future depends on the past only through the present state. A [Poisson process](homogeneous-poisson-process.qmd) is a continuous-time counting process with stationary independent increments. A Galton–Watson process is a Markov chain on the non-negative integers whose step is a random sum of offspring. The path $t\mapsto X_t(\omega)$ is what a single run of the experiment produces.
""",
    "strong-law": r"""
## The average along one infinite sequence

The strong law answers a pathwise question. Given an endless sequence of repeated measurements, does the running average settle on the theoretical mean for almost every sequence, or only in the weaker sense that a large error becomes unlikely at each fixed $n$?

Let $Y_1,Y_2,\ldots$ be independent and identically distributed with finite absolute mean $\mathbb{E}|Y_1|<\infty$. Write $\mu=\mathbb{E} Y_1$ and

$$
\overline{Y}_n=\frac{1}{n}\sum_{i=1}^{n} Y_i.
$$

Kolmogorov's strong law says $\overline{Y}_n\to\mu$ almost surely (Kolmogorov, 1933). There is an event of probability $1$ on which the numerical sequence $\overline{Y}_n(\omega)$ converges to $\mu$. [Convergence in probability](modes-of-convergence.qmd) is weaker: $\mathbb{P}(|\overline{Y}_n-\mu|>\varepsilon)\to 0$ for every $\varepsilon>0$, and the bad set may change with $n$. If $\operatorname{Var}(Y_1)$ is finite, Chebyshev's inequality gives a bound of order $1/n$: the bound tends to zero, which proves the weak law, yet it is not summable and therefore does not, by itself, feed the [Borel–Cantelli lemmas](borel-cantelli-lemmas.qmd).

## Bernoulli sequences, and a Cauchy average that will not settle

Take $Y_i\in\{0,1\}$ with $\mathbb{P}(Y_i=1)=1/2$. Then $\mu=1/2$ and $\mathbb{E}|Y_1|=1/2<\infty$, so the proportion of ones tends to $1/2$ on almost every sequence. At $n=400$ a typical error is still about $0.025$, of the central-limit size $1/(2\sqrt{n})$. The strong law says that this error eventually becomes and remains small along the path. The finite-mean hypothesis is essential. A standard Cauchy law, density $1/(\pi(1+y^{2}))$, has $\mathbb{E}|Y_1|=\infty$. The average of independent copies is again standard Cauchy for every $n$, because $(e^{-|t|/n})^{n}=e^{-|t|}$. That average does not converge in probability to any constant. See the [law of large numbers](law-of-large-numbers.qmd).
""",
    "studentised-coefficient-pivot": r"""
## Take the unknown scale out of the denominator

In the Gaussian linear model $\boldsymbol{Y} = \boldsymbol{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$, let $\boldsymbol{\varepsilon} \sim \operatorname{N}_n(\boldsymbol{0}, \sigma^2\boldsymbol{I}_n)$ and let $\boldsymbol{X}$ be an $n \times p$ matrix of rank $p$ with $n>p$. The [least-squares estimator](ordinary-least-squares.qmd) is then normal with mean $\boldsymbol{\beta}$ and covariance $\sigma^2(\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{-1}$. Write $c_{jj}$ for the $j$th diagonal entry of $(\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{-1}$, so the sampling variance of $\widehat{\beta}_j$ is $\sigma^2 c_{jj}$. The ratio $(\widehat{\beta}_j - \beta_j)/(\sigma \sqrt{c_{jj}})$ is standard normal, but $\sigma$ is still in the denominator. Replace $\sigma^2$ by $s^2 = \operatorname{SSE}/(n-p)$, where $\operatorname{SSE} = \lVert \boldsymbol{Y} - \boldsymbol{X}\widehat{\boldsymbol{\beta}} \rVert_2^2$ is the fitted residual sum of squares. The studentised ratio is $(\widehat{\beta}_j - \beta_j)/(s \sqrt{c_{jj}})$.

## Normal numerator, independent chi-squared denominator

Under the model, $\operatorname{SSE}/\sigma^2$ follows a chi-squared distribution on $\nu = n-p$ degrees of freedom and is independent of $\widehat{\boldsymbol{\beta}}$. Divide the standard normal numerator by $\sqrt{(\operatorname{SSE}/\sigma^2)/\nu}$. The unknown $\sigma$ cancels, and the quotient is exactly the studentised ratio. A standard normal random variable divided by the square root of an independent chi-squared variable over its degrees of freedom follows a [Student $t$ distribution](student-t-distribution.qmd) on $n-p$ degrees of freedom. The ratio is a [pivot](pivot.qmd): its sampling distribution does not depend on $(\boldsymbol{\beta}, \sigma^2)$. The vector $\widehat{\boldsymbol{\beta}}$ has not become a $t$ random vector. Its sampling distribution, with $\sigma^2$ treated as known, remains normal. The $t$ distribution appears only after $\sigma$ is replaced by $s$ and the ratio is formed.
""",
    "study-rate-full-conditional": r"""
## Only one study rate is still free

Assign each study its own success probability. Let $y_j \mid \theta_j \sim \operatorname{Binomial}(n_j, \theta_j)$, independently across $j = 1,\ldots,J$ given the rates, and let $\theta_j \mid \alpha,\beta \sim \operatorname{Beta}(\alpha, \beta)$, independently across studies. The [hyperparameters](hyperparameter.qmd) $(\alpha, \beta)$ carry a hyperprior. Hold $(\alpha, \beta)$ and the whole data vector fixed, and consider the joint posterior as a function of the single coordinate $\theta_j$. The binomial factor for study $j$ is proportional to $\theta_j^{y_j}(1-\theta_j)^{n_j-y_j}$, and the beta factor is proportional to $\theta_j^{\alpha-1}(1-\theta_j)^{\beta-1}$. No other study contributes a power of $\theta_j$. Multiplying those powers produces $\theta_j^{y_j+\alpha-1}(1-\theta_j)^{n_j-y_j+\beta-1}$, which is the kernel of a $\operatorname{Beta}(y_j+\alpha,\, n_j-y_j+\beta)$ density.

## Independent conjugate updates

The beta function that normalises the kernel depends on $(y_j, n_j, \alpha, \beta)$ but not on any other rate. The [full conditional distribution](full-conditional-distribution.qmd) is therefore

$$
\theta_j \mid \alpha, \beta, \boldsymbol{y} \sim \operatorname{Beta}(y_j+\alpha,\, n_j-y_j+\beta),
$$

and, conditionally on the hyperparameters, the study rates are independent. Their joint full conditional is the product of these $J$ beta densities. A Gibbs update can draw every $\theta_j$ independently at the current value of $(\alpha, \beta)$. Each draw is an ordinary conjugate update, with the current hyperparameters playing the role of the beta prior. The draw does not integrate the hyperparameters out. Uncertainty about $(\alpha, \beta)$ appears only when those hyperparameters are updated themselves, or when several draws are pooled so that $(\alpha, \beta)$ varies. Reporting the beta laws at one plugged-in value of $(\alpha, \beta)$, as though they were marginal posteriors for the rates, omits that layer.
""",
    "superposition-and-thinning": r"""
## Merging independent streams, and splitting one at random

Two operations leave the Poisson process inside its own family. Independent streams can be laid on top of each other, and a single stream can be randomly labelled and separated. Both results are Poisson, with rates one can write down, and the split pieces are independent of each other.

Let $N_1$ and $N_2$ be independent homogeneous Poisson processes of rates $\lambda_1$ and $\lambda_2$. Their superposition $N_1+N_2$ is Poisson of rate $\lambda_1+\lambda_2$. On a common interval the merged count is Poisson with mean $(\lambda_1+\lambda_2)h$, and increments on disjoint intervals remain independent. For thinning, start with a Poisson process of rate $\lambda$ and keep each event independently with probability $r\in(0,1)$, discarding it otherwise. The kept process is Poisson of rate $r\lambda$, the discarded process is Poisson of rate $(1-r)\lambda$, and the two are independent. If the retention probability is a function $r(t)$, thinning the homogeneous process gives a non-homogeneous Poisson process with intensity $r(t)\lambda$ (or $r(t)\lambda(t)$ when the original process already has intensity $\lambda(t)$).

## A merged rate of eight, split again into three and five

Take independent call streams of rates $3$ and $5$ per hour. The merged process has rate $8$. Each merged call is of the first type with probability $3/8$, independently of the other calls, which is the thinning that recovers the original streams. In one hour the type counts are independent Poisson random variables of means $3$ and $5$, and $\mathbb{P}(N_1=0,N_2=0)=e^{-8}$. A shock that drops several events at one instant is a shared mark, not an independent toss on each event, and ordinary thinning does not describe that stream.
""",
    "surrogate-split": r"""
## A mimic of the primary left–right allocation

A primary split at a node sends each case left or right according to one variable, say $x_1<0$. A later case may arrive with $x_1$ missing. A surrogate is another question, using a variable that is observed, chosen so that its own left–right allocation agrees with the primary allocation on the cases where both are available. The surrogate is scored by agreement with the primary split. It is not scored by the impurity reduction that made the primary split win. Sending every incomplete case to the majority child is a fallback. That fallback does not look at a second variable, so it is not a surrogate.

## Agreement on twenty cases

Suppose the primary split and a candidate split on $x_2$, namely $x_2<1$, are both known for $20$ cases, and the two questions put $18$ of the $20$ cases on the same side. The agreement is $18/20=0.9$. If $x_1$ is missing and $x_2$ is present, the case follows $x_2<1$. A second variable that agrees on only $11$ of the $20$ cases is a weak mimic and would be ranked behind the first surrogate. The primary split can still be the better question for impurity. The surrogate exists to copy it, including on a variable whose own impurity reduction is modest. How many surrogates are kept changes the leaf reached by an incomplete case.
""",
    "the-beta-distribution-is-the-two-category-dirichlet": r"""
## Collapse the simplex onto the unit interval

A [Dirichlet distribution](dirichlet-distribution.qmd) is a distribution on a probability vector, not on a vector of counts. For $K$ categories, with every $\alpha_k > 0$ and with $\alpha_0 = \sum_{k=1}^{K} \alpha_k$, the density on the simplex $p_k \ge 0$, $\sum_k p_k = 1$, is

$$
\frac{\Gamma(\alpha_0)}{\prod_{k=1}^{K} \Gamma(\alpha_k)} \prod_{k=1}^{K} p_k^{\alpha_k-1},
$$

relative to Lebesgue measure on the free coordinates. Set $K = 2$, write $p_1 = p$ and $p_2 = 1-p$, and replace $\alpha_0$ by $\alpha_1+\alpha_2$. The simplex is then the unit interval, and the density becomes

$$
\frac{\Gamma(\alpha_1+\alpha_2)}{\Gamma(\alpha_1)\, \Gamma(\alpha_2)} \, p^{\alpha_1-1}(1-p)^{\alpha_2-1}, \qquad 0 < p < 1.
$$

That is the [beta density](beta-distribution.qmd) $\operatorname{Beta}(\alpha_1, \alpha_2)$, normalising constant included. The beta family is the two-category Dirichlet family.

## The mean and the update are the same arithmetic

Because the densities agree, so do the functionals computed from them. The mean of the first coordinate is $\alpha_1/\alpha_0$ in the Dirichlet law and $\alpha_1/(\alpha_1+\alpha_2)$ in the beta law. A Dirichlet$(1,1)$ prior is uniform on $(0,1)$. A binomial likelihood adds the success count to $\alpha_1$ and the failure count to $\alpha_2$, while a multinomial likelihood adds each category count to the matching Dirichlet parameter. At $K = 2$ those updates coincide. A multinomial distribution cannot serve as the prior for $\boldsymbol{p}$. Its support is a lattice of integer count vectors that sum to a fixed number of trials, whereas $\boldsymbol{p}$ varies continuously on the simplex. The data may be discrete while the parameter prior is continuous. The Dirichlet, through this beta case, is the prior attached to the probability vector.
""",
    "the-limit-of-hotelling-s-statistic": r"""
## The $F$ law becomes chi-squared as $n$ grows

Under normality, with $n>p$ and $\Sigma$ positive definite, Hotelling's $T^2$ satisfies

$$
F=\frac{n-p}{p(n-1)}\,T^2\sim F_{p,\, n-p}
$$

when the mean equals the null value $\boldsymbol{\mu}_0$. Multiply by the degrees of freedom: $pF=(n-p)/(n-1)\,T^2$. For fixed $p$, the fraction $(n-p)/(n-1)$ tends to $1$ as $n\to\infty$. A random variable with law $F_{p,\, n-p}$, multiplied by $p$, tends to chi-squared on $p$ degrees of freedom. Therefore $T^2$ itself is asymptotically $\chi^2_p$ under the null, once $S$ is consistent for $\Sigma$. The [multivariate central limit theorem](multivariate-central-limit-theorem.qmd) supplies the normal limit for $\sqrt{n}(\overline{\mathbf{X}}-\boldsymbol{\mu}_0)$ without requiring the observations to be Gaussian, and Slutsky's lemma replaces $\Sigma$ by $S$ inside the quadratic form. The chi-squared limit can outlive the exact $F$ law. The exact law does not survive non-normality.

## A moderate sample where the two tails differ

The upper $5\%$ point of $\chi^2_2$ is $5.991$. At that value of $T^2$, with $n=20$ and $p=2$,

$$
F=\frac{18}{38}\cdot 5.991\approx 2.84,
$$

and the tail probability of $F_{2,18}$ beyond $2.84$ is about $0.085$. A chi-squared comparison at level $5\%$ rejects; the exact normal-theory test does not. At $n=200$ and the same $T^2$, the $F$ tail is about $0.053$, close to the chi-squared tail. The approximation is a large-sample device. For small $n-p$ the exact $F$ critical value, when normality holds, is the one that keeps the nominal level.
""",
    "the-reweighted-error-is-one-half": r"""
## The weight update that neutralises the current learner

[AdaBoost](adaboost.qmd) fits a classifier $f_t$ to labels $y_i\in\{-1,+1\}$ under nonnegative weights that sum to $1$. Let $\varepsilon_t$ be the weight of the cases $f_t$ gets wrong, and assume $0<\varepsilon_t<1$. The vote of that learner is $\alpha_t=\frac12\log\bigl((1-\varepsilon_t)/\varepsilon_t\bigr)$. Correct cases are then multiplied by $e^{-\alpha_t}$ and incorrect cases by $e^{\alpha_t}$. The incorrect cases currently hold total weight $\varepsilon_t$, so their un-normalised new weight is $\varepsilon_t e^{\alpha_t}=\sqrt{\varepsilon_t(1-\varepsilon_t)}$. The correct cases hold $1-\varepsilon_t$, and their un-normalised new weight is the same square root. After dividing by the sum, each group carries weight $1/2$. The weighted error of this same $f_t$, under the new weights, is the weight of the incorrect group, which is exactly $1/2$.

## A round with error $0.2$

If $\varepsilon_t=0.2$, then $\alpha_t=\frac12\log 4\approx 0.693$ and $\sqrt{0.2\cdot 0.8}=0.4$. Both groups have un-normalised weight $0.4$, the normaliser is $0.8$, and each group has new weight $1/2$. The next learner is therefore trained on a problem for which the learner just fitted is no better than a fair coin. It has to use some other structure. The algebra uses this particular $\alpha_t$. A different reweighting can still build a useful ensemble and need not hit $1/2$.

The logarithm is finite only for $0<\varepsilon_t<1$. A perfect round, $\varepsilon_t=0$, makes $\alpha_t$ infinite: stop, or store that learner as a hard rule and leave the remaining weight update undefined. A usual positive vote also asks for $\varepsilon_t<1/2$. If $\varepsilon_t>1/2$, then $\alpha_t<0$, and the ensemble votes the opposite of $f_t$.
""",
    "three-easy-confusions": r"""
## The estimator stays normal; the pivot becomes Student

In the Gaussian linear model, $\widehat{\boldsymbol{\beta}}$ has an exact normal sampling distribution when the error variance $\sigma^2$ is known: its mean is $\boldsymbol{\beta}$ and its covariance is $\sigma^2(\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{-1}$. That sampling law is not a $t$ distribution. The $t$ distribution describes the studentised ratio $(\widehat{\beta}_j - \beta_j)/(s \sqrt{c_{jj}})$, where $s^2 = \operatorname{SSE}/(n-p)$ estimates $\sigma^2$ and $c_{jj}$ is a diagonal entry of $(\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{-1}$. The ratio follows a [Student $t$ distribution](student-t-distribution.qmd) on $n-p$ degrees of freedom. Quoting a $t$ sampling distribution for the coefficient vector itself skips the ratio that removed $\sigma$.

## Subtract $p/2$, and do not confuse the two samplers

Under the reference prior $p(\boldsymbol{\beta}, \sigma^2) \propto 1/\sigma^2$ with $n>p$, the marginal posterior of $\sigma^2$ is [inverse-gamma](inverse-gamma-distribution.qmd) with shape $(n-p)/2$ and rate $\operatorname{SSE}/2$. The kernel in the shape–rate parameterisation is $(\sigma^2)^{-a-1}\exp(-b/\sigma^2)$. Likelihood and prior together contribute the power $-(n/2+1)$. Integrating the $p$-dimensional normal density integrand in $\boldsymbol{\beta}$ multiplies by a factor $(\sigma^2)^{p/2}$, which subtracts $p/2$ from $n/2$. Adding $p/2$ instead leaves the wrong shape $(n+p)/2$. Equivalently, $\operatorname{SSE}/\sigma^2$ given $\boldsymbol{y}$ is chi-squared on $n-p$ degrees of freedom. Drawing $\sigma^2$ from this marginal posterior, then drawing $\boldsymbol{\beta}$ from its conditional normal distribution given $\sigma^2$ and $\boldsymbol{y}$, produces independent draws from the joint posterior. A [Gibbs sampler](gibbs-sampling.qmd) draws $\sigma^2$ from the full conditional given the current $\boldsymbol{\beta}$, which is inverse-gamma with shape $n/2$ and rate $\lVert \boldsymbol{y}-\boldsymbol{X}\boldsymbol{\beta}\rVert_2^2/2$. Successive pairs form a [Markov chain](markov-chain.qmd). The two algorithms can share a target. Only the marginal-then-conditional factorisation produces independent draws.
""",
    "throughput": r"""
## The rate of customers who actually enter

The offered arrival rate is the rate at which customers attempt to arrive. Throughput is the rate at which they are accepted, and, in equilibrium, the rate at which they depart. Once the system can refuse arrivals, those two rates differ, and formulas that assume they are equal become wrong.

Consider a room of capacity $K$. Arrivals are offered as a Poisson process of rate $\lambda$, and an arrival that finds $K$ customers present is lost. The long-run fraction lost is the [blocking probability](blocking-probability.qmd) $\pi_K$, so the throughput is $\lambda_{\mathrm{eff}}=\lambda(1-\pi_K)$. In equilibrium the long-run departure rate equals $\lambda_{\mathrm{eff}}$. It equals the offered rate $\lambda$ only when nothing is blocked. [Little's law](little-s-law.qmd) must be fed $\lambda_{\mathrm{eff}}$. Using $\lambda$ pairs the sojourn of accepted customers with a rate that includes people who never entered, and the resulting "mean time" is too small.

## A room of size two, offered well above service

Take an M/M/1/$2$ system with $\lambda=4$ and $\mu=2$, so $\rho=2$. The stationary weights are proportional to $1$, $2$, $4$, which sum to $7$. Thus $\pi_2=4/7$ and

$$
\lambda_{\mathrm{eff}}=4\bigl(1-4/7\bigr)=12/7\approx 1.71,
$$

below both the offered rate $4$ and the service rate $2$. The mean number present is $L=0\cdot(1/7)+1\cdot(2/7)+2\cdot(4/7)=10/7$. The mean sojourn of an accepted customer is $W=L/\lambda_{\mathrm{eff}}=(10/7)/(12/7)=5/6$. Dividing $L$ by the offered rate $4$ instead would give $10/28=5/14$, which is $3/7$ of the true sojourn $5/6$, because it pretends the blocked arrivals also passed through. Throughput, not the offered rate, is the arrival rate of the population counted by $L$.
""",
    "time-series": r"""
## One ordered stretch, not a bag of draws

A time series is a single run of one measurement in time order, $X_1,\ldots,X_T$. Neighbours share shocks, seasons or a slowly moving level, so the run is one realisation of a process, not $T$ independent draws from a common distribution. The usual sample-size arithmetic waits until something restores repetition. [Weak stationarity](weak-stationarity.qmd) is the usual restoration: a mean that does not depend on time, and a covariance that depends on two times only through the lag between them. Under that restriction the one stretch contains many overlapping pairs at each lag, and those pairs estimate one autocovariance. Without it, a separate mean at every time and a separate covariance for every pair is more structure than $T$ observations can carry.

## Why the sample mean is less precise than $T$ suggests

For the stationary autoregression $X_t-\mu=\phi(X_{t-1}-\mu)+\varepsilon_t$ with the absolute value of $\phi$ less than $1$, the variance of the sample mean is approximately $(\gamma_0/T)(1+\phi)/(1-\phi)$ once $T$ is large. Here $\gamma_0=\operatorname{Var}(X_t)$. Independent data with the same variance would have given $\gamma_0/T$. At $\phi=0.9$ the limiting factor $(1+\phi)/(1-\phi)$ equals $19$ ($\sqrt{19}\approx 4.4$). At length $T=100$ the exact finite-sample factor with end weights $(1-h/T)$ is about $17.2$, so the standard error is about $4.15$ times the independent-data formula and the series says about as much about $\mu$ as six independent observations. The usual aim is a forecast of the next value, not a description that stops at time $T$. A fit with a new parameter at every time can reproduce $X_1,\ldots,X_T$ and still say nothing about $X_{T+1}$. Models that forecast reuse a short list of coefficients across the whole stretch.
""",
    "trace-plot": r"""
## Reading the path against iteration

A trace plot graphs a scalar function of a Markov chain, often a single coordinate $\theta^{(t)}$, against the iteration index $t$. The picture records exploration and dependence. It is not a plot of the posterior density. Several chains, started at dispersed values, should occupy the same region after warm-up and should keep moving inside it. A path that drifts, that stays constant for a long stretch because proposals are rejected, or that settles in a different place from a second chain, shows that this particular run has not yet represented the target. A histogram of the stored draws estimates the distribution those draws occupied. The trace asks whether the draws were produced by a chain that was still travelling.

## A tidy trace is not an invariance proof

Detailed balance is a property of the transition kernel. The trace is one finite path, so a calm picture is not a proof of convergence. A chain can look locally stable while remaining inside one mode of a multimodal target, and a short run can look acceptable by chance. The [autocorrelation function](autocorrelation-function.qmd) supplies the matching numerical check. When correlation decays slowly, successive draws nearly repeat one another, and the [effective sample size](effective-sample-size.qmd) is much smaller than the number of iterations stored. Discarding a [warm-up](warm-up-is-not-a-convergence-proof.qmd) prefix is a practical convention. The deletion does not create stationarity, and it does not make the retained draws independent. The plot can justify a longer run, a different proposal, or a reparameterisation of the target. It cannot replace the argument that the transition kernel leaves the intended posterior invariant.
""",
    "training-data-and-classifier": r"""
## The object that is trained, and the object that is assessed

The training data are $n$ pairs $(\mathbf{x}_i,y_i)$ with $\mathbf{x}_i\in\mathbb{R}^p$ and $y_i\in\{1,\ldots,G\}$. A classifier is a rule that, from those pairs and from a new point $\mathbf{x}$, returns a class in $\{1,\ldots,G\}$. The notation $\eta^{(X_{\mathrm{all}},\mathbf{y}_{\mathrm{all}})}(\mathbf{x})$ records the dependence: change the training pairs and the function of $\mathbf{x}$ can change. Before the sample is drawn, the classifier is a random function. Its risk is an expectation over a fresh pair $(X,Y)$ and, if the training set is itself random, over that training set as well. The apparent error averages the zero–one loss only over the $n$ pairs that were used to build $\eta$. Those two averages answer different questions.

## A threshold rule on four points

Take $p=1$, $G=2$ and training inputs $-2,-1,1,2$ with labels $1,1,2,2$. The rule $\eta(x)=1$ when $x<0$ and $\eta(x)=2$ otherwise classifies all four training points correctly, so its apparent error is $0$. A constant rule that always returns class $1$ has apparent error $1/2$ on this sample. Neither number is the probability of a mistake on a new draw. If a fifth point arrives at $x=0.1$ from class $1$, the threshold rule errs and the constant rule does not. The definition of a classifier is wide enough to include both rules, and also any rule produced by linear discriminant analysis, a tree, or a neighbour vote. Comparing procedures means comparing the maps they build from a training set, under a stated loss and a stated distribution for the fresh pair.
""",
    "transient-and-recurrent-states": r"""
## Finitely many visits, or infinitely many

Recurrence can be read off the return time, or off the total number of visits. The two readings match. A transient state is seen only finitely often. A recurrent state is seen forever, and the mean return time then decides whether it can carry stationary mass.

Start the chain in $i$, and let $N_i=\sum_{n\ge 1}1_{\{X_n=i\}}$ be the number of later visits. Write $f_i=\mathbb{P}_i(T_i^{+}<\infty)$ for the probability of ever returning. The number of returns is geometric: $\mathbb{P}_i(N_i\ge k)=f_i^{k}$ for $k\ge 0$. Thus $\mathbb{E}_i N_i=f_i/(1-f_i)$ when $f_i<1$, and $\mathbb{E}_i N_i=\infty$ when $f_i=1$. The state is transient when $f_i<1$, equivalently when the expected number of visits is finite. It is recurrent when infinitely many visits occur almost surely. Among recurrent states, positive recurrence means $\mathbb{E}_i T_i^{+}<\infty$, while null recurrence means the chain returns forever but the expected return is infinite. Only positive recurrent states receive positive mass in a stationary distribution, with $\pi_i=1/\mathbb{E}_i T_i^{+}$.

## A state that is left for good

Let state $0$ be absorbing, $p_{00}=1$, and let $p_{10}=p_{11}=1/2$. State $0$ is positive recurrent: the return time is $1$ and $\pi$ may put mass $1$ there. State $1$ is transient. Each visit gives an independent chance $1/2$ of being absorbed, so the number of later visits is geometric with mean $1$, which is finite. In a finite chain there is no null recurrence. Every state of a closed communicating class is positive recurrent, and every state outside those classes is transient. See [recurrence and period](recurrence-and-period.qmd).
""",
    "translation-to-another-common-notation": r"""
## Match the symbols before differentiating

The same exponential-family density is commonly written in two ways. With a normalising function,

$$
p(x \mid \theta) = b(x)\exp\{c(\theta)^{\mathsf{T}} T(x)\} / a(\theta),
$$

the vector $c(\theta)$ is the natural parameter, $T(x)$ is the natural statistic, $b(x)$ does not depend on $\theta$, and $a(\theta)$ is the sum or integral that makes the density total one. The other writing is $p(x \mid \boldsymbol{\eta}) = h(x)\exp\{\boldsymbol{\eta}^{\mathsf{T}} T(x) - A(\boldsymbol{\eta})\}$. The dictionary is $\boldsymbol{\eta} = c(\theta)$, $h(x) = b(x)$, and $A(\boldsymbol{\eta}) = \log a(\theta)$. Dividing by the normaliser is the same operation as subtracting the cumulant function in the exponent. No probability is changed by the renaming. A prior derived in either notation is the same distribution once these symbols have been identified.

## Moments follow the logarithm either way

Where the natural parameter $\boldsymbol{\eta}$ lies in the interior of $\{\boldsymbol{\eta}:A(\boldsymbol{\eta})<\infty\}$, differentiating $A(\boldsymbol{\eta}) = \log a(\theta)$ gives $\nabla A(\boldsymbol{\eta})=\mathbb{E}[T(X)]$ and $\nabla^2 A(\boldsymbol{\eta})=\operatorname{Cov}[T(X)]$. Those are derivatives with respect to $\boldsymbol{\eta}$, not an arbitrary $\theta$: $A$ is convex in $\boldsymbol{\eta}$, whereas $\theta\mapsto\log a(\theta)$ need not be convex (for $\operatorname{N}(0,\sigma^2)$, $\log a(\sigma^2)=\tfrac12\log(2\pi\sigma^2)$ is concave in $\sigma^2$ while $A$ is convex in $\eta=-1/(2\sigma^2)$). A conjugate prior proportional to $\exp\{\boldsymbol{\eta}^{\mathsf{T}} \chi - \nu A(\boldsymbol{\eta})\}$ uses $\chi$ as a prior copy of the natural statistic and $\nu$ as a prior sample size. Adding $\sum_i T(x_i)$ to $\chi$, and adding the sample size $n$ to $\nu$, is the update obtained by collecting powers in the $a(\theta)$ form. When one calculation quotes $A$ and another quotes $a(\theta)$, the first step is this translation.
""",
    "treatment": r"""
## A condition the protocol assigns

A treatment is a condition assigned to a unit by the experimenter: a drug or a placebo, a fertiliser, a dose, a teaching method. The response is what is measured afterwards. In a [designed experiment](designed-experiment.qmd) that assignment is part of the protocol, and it stays the same if the response is measured again. An exposure that people choose for themselves is a different object. Comparing smokers with non-smokers uses the word treatment only loosely. Smoking was not assigned, so the groups can differ in age, prior health and whatever else leads a person to smoke. Those differences are [confounding](confounding-variable.qmd). A later regression removes only the confounders that were measured and entered in the mean.

## What a random assignment balances, and what it does not

Suppose $12$ plots are on hand and a fertiliser is to be compared with a control. A random assignment gives the fertiliser to $6$ plots, every subset of size $6$ equally likely. Soil quality may still differ between the groups, but it differs by the draw, not because the better soil was given the fertiliser. The randomisation distribution of a contrast, recomputed over the assignments that might have been used, is then a basis for inference that does not need a model for the soil. Choosing the six "treated" plots because they looked ready, or because a farmer volunteered them, puts soil quality back into the treatment column. No linear adjustment fixes that unless the soil was measured.
""",
    "trend": r"""
## A level that moves slowly

Trend is slow change in the level of a series. A deterministic trend is a fixed function of time. In $X_t=3+0.5t+\varepsilon_t$, with $\varepsilon_t$ [white noise](white-noise.qmd) of variance $\sigma^2$, the mean at time $t$ is $3+0.5t$ and the variance is $\sigma^2$ at every time. A stochastic trend has no fixed path. The random walk $X_t=X_{t-1}+\varepsilon_t$, started from a constant, has level equal to the sum of every shock so far, and its variance is $t\sigma^2$. Both series can look like a sloping line on a short window. They do not share a forecast, and the same operation does not make both of them stationary.

## Subtracting a line is not the same as differencing

The first difference of the straight-line example is $X_t-X_{t-1}=0.5+\varepsilon_t-\varepsilon_{t-1}$. The slope survives only as a constant mean of $0.5$, and the noise is a moving average of order $1$. That differenced series is stationary. Subtracting the known line $3+0.5t$ also works, and it returns $\varepsilon_t$. The random walk is not the same case. Its difference is $\varepsilon_t$, so differencing removes the trend. Subtracting a least-squares line does not. The residuals from a walk regressed on a fitted line stay strongly autocorrelated, because the level was free to wander. Forecasts split in the same way. The deterministic model extends the line and keeps a bounded error variance. The random walk extends the last observation, and the error variance at horizon $h$ is $h\sigma^2$. A plot that slopes is not evidence that the trend is a fixed function of time.
""",
    "two-pseudo-count-conventions": r"""
## Counts that reproduce the posterior mean

Suppose a binomial probability has a $\operatorname{Beta}(\alpha, \beta)$ prior, with $\alpha > 0$ and $\beta > 0$, and the sample contains $x$ successes in $n$ trials. The posterior is $\operatorname{Beta}(\alpha+x, \beta+n-x)$. Its mean $(x+\alpha)/(n+\alpha+\beta)$ is a weighted average of the sample proportion $x/n$ and the prior mean $\alpha/(\alpha+\beta)$, with weights $n$ and $\alpha+\beta$. In that average, $\alpha$ plays the role of a prior success count, $\beta$ the role of a prior failure count, and $\alpha+\beta$ the role of a prior sample size. Those are the pseudo-counts attached to the [posterior mean](posterior-mean.qmd). A $\operatorname{Beta}(1,1)$ prior contributes one success and one failure. A $\operatorname{Beta}(5,5)$ prior contributes five of each, hence a prior sample size of ten, rather than four successes in four trials.

## A smaller count reproduces an interior mode

The posterior mode is a different functional of the same beta distribution. When $\alpha+x > 1$ and $\beta+n-x > 1$, the mode equals $(x+\alpha-1)/(n+\alpha+\beta-2)$. The weighted-average arithmetic now uses prior counts $\alpha-1$ and $\beta-1$, so the prior sample size is $\alpha+\beta-2$. Relative to a $\operatorname{Beta}(1,1)$ prior, whose counts in this convention are zero, a $\operatorname{Beta}(5,5)$ prior contributes four additional successes and four additional failures. That is eight prior trials on the mode scale. The two conventions describe two summaries, not two conflicting priors. A sentence such as "the prior is worth eight observations" is incomplete until it names the summary being matched. If $\alpha < 1$, the mode-convention count $\alpha-1$ is negative: the prior density is unbounded at a boundary so the interior-mode formula does not apply to the prior, though enough data ($\alpha+x>1$ and $\beta+n-x>1$) still produce an interior posterior mode. It is not a negative number of trials one could have observed.
""",
    "two-sample-t-pivot": r"""
## A normal difference over a pooled scale

Two independent normal samples need a common variance before their mean difference has a $t$ pivot. Let $X_{11},\ldots,X_{1n_1}$ be $\operatorname{N}(\mu_1,\sigma^2)$ and $X_{21},\ldots,X_{2n_2}$ be $\operatorname{N}(\mu_2,\sigma^2)$, all $n_1+n_2$ variables independent, with the same $\sigma^2>0$. Write $\overline X_1$ and $\overline X_2$ for the sample means, and let

$$
s_j^2=\frac1{n_j-1}\sum_{i=1}^{n_j}(X_{ji}-\overline X_j)^2
$$

be the bias-corrected sample variances. The [pooled variance](pooled-variance.qmd) is

$$
s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}.
$$

Then $(n_1+n_2-2)s_p^2/\sigma^2$ is chi-squared on $n_1+n_2-2$ [degrees of freedom](degrees-of-freedom.qmd), because each $(n_j-1)s_j^2/\sigma^2$ is chi-squared and the samples are independent. The numerator $(\overline X_1-\overline X_2)-(\mu_1-\mu_2)$, divided by $\sigma\sqrt{1/n_1+1/n_2}$, is standard normal and independent of $s_p$. The ratio

$$
T=\frac{(\overline X_1-\overline X_2)-(\mu_1-\mu_2)}{s_p\sqrt{1/n_1+1/n_2}}
$$

therefore has the [Student $t$ distribution](student-t-distribution.qmd) on $n_1+n_2-2$ degrees of freedom. Replacing $s_p$ by a known $\sigma$ would make $T$ standard normal.

## Ten and ten, with equal sample variances

Take $n_1=n_2=10$, $\overline X_1=20$, $\overline X_2=17$ and $s_1^2=s_2^2=4$. Then $s_p^2=4$ and the denominator is $2\sqrt{1/5}\approx 0.894$. The pivot at a difference of $0$ equals $3/0.894\approx 3.35$, on $18$ degrees of freedom. The $0.975$ quantile of $t_{18}$ is $2.101$, so a $95\%$ interval for $\mu_1-\mu_2$ is $3\pm 1.88$, that is $(1.12, 4.88)$. If the two variances differ, $s_p$ estimates a compromise that is not the right standard error. That is the [Behrens–Fisher problem](behrens-fisher-problem.qmd). The level of this $t$ procedure is much less sensitive to heavy tails than the level of an $F$ test for $\sigma_1^2=\sigma_2^2$.
""",
    "underfitting": r"""
## A family that cannot follow the signal

Underfitting is a large approximation error. The best function inside the model family is still far from the regression mean, or from the Bayes classifier, so both the training loss and the loss on new data stay large. More data make the training loss a better estimate of that already-large error. They do not enlarge the family. Three common sources are a too-simple architecture, an optimisation run that was stopped while the training loss was still descending, and a penalty so heavy that the fitted function is forced towards a constant.

## A line fitted to a parabola

Let the noise-free responses at $x=-2,-1,0,1,2$ be $y=4,1,0,1,4$, the values of $x^2$. The least-squares line has slope $0$, because $\sum_i x_i y_i=0$, and intercept $2$, the mean of $y$. The residuals are $2,-1,-2,-1,2$, and the residual sum of squares is $14$. A quadratic term in $x$ fits these five points with residual sum of squares $0$. The line's error is visible on the training points themselves: the ends lie above the line and the middle lies below it. That pattern is the signature of underfitting. A degree-$4$ polynomial on the same five points, once a little noise is added to $y$, shows the opposite signature: a training error of zero and a large error on a new $x$. [Early stopping](early-stopping.qmd) and strong [regularisation](regularisation.qmd) can leave even a rich family in the underfitting regime, if they halt the fit while the training loss is still large.
""",
    "undirected-graph": r"""
## Vertices, undirected edges, and paths

An undirected graph $G=(V,E)$ is the combinatorial skeleton of a Markov random field. The vertex set $V=\{1,\ldots,p\}$ indexes the coordinates of a random vector. An edge is an unordered pair $\{j,k\}$ with $j\neq k$: there is no self-loop, and the pair is either present once or absent. A path from $a$ to $b$ is a sequence of distinct vertices, starting at $a$ and ending at $b$, with an edge between each consecutive pair. The neighbours of $j$ are the vertices joined to $j$ by an edge. The degree of $j$ is the number of neighbours. A set $C\subset V$ separates $A$ from $B$ when every path from a vertex in $A$ to a vertex in $B$ passes through $C$.

## A path on three vertices

Take $V=\{1,2,3\}$ and $E=\{\{1,2\},\{2,3\}\}$. Vertex $2$ has degree $2$, and vertices $1$ and $3$ have degree $1$. The unique path from $1$ to $3$ is $1-2-3$, so $\{2\}$ separates $\{1\}$ from $\{3\}$. The pair $\{1,3\}$ is a non-edge. In the [Markov random field](markov-random-field.qmd) on this graph, that non-edge is the pairwise statement $X_1\perp X_3\mid X_2$, and the separator $\{2\}$ is the same statement read globally. The graph itself does not contain the probability law. A complete graph on the same three vertices has all three edges, an empty separating statement, and no conditional-independence constraint of this kind. A [clique](clique.qmd) is a subset in which every pair is joined; here the cliques of the path are the two edges.
""",
    "uniform-integrability": r"""
## Tails that are small for every index at once

Almost-sure convergence does not let the limit pass inside the expectation. A rare spike can keep a fixed contribution to the mean while disappearing from almost every path. Uniform integrability is the extra control that rules that spike out: the contribution of the far tail must be small uniformly in $n$.

A family $\{X_n\}$ is uniformly integrable when

$$
\lim_{K\to\infty}\sup_n\mathbb{E}\bigl(|X_n|\,1_{\{|X_n|>K\}}\bigr)=0.
$$

If $X_n\to X$ in probability and $\{X_n\}$ is uniformly integrable, then $\mathbb{E}|X_n-X|\to 0$, so $\mathbb{E} X_n\to\mathbb{E} X$. An integrable dominant is a convenient sufficient condition. If $|X_n|\le Y$ for every $n$ and $\mathbb{E} Y<\infty$, the tail $\mathbb{E}(Y\,1_{\{Y>K\}})$ does not depend on $n$ and tends to $0$, which is uniform integrability. A bound on a higher moment also suffices: if $\sup_n\mathbb{E}|X_n|^{1+\delta}\le M$ for some $\delta>0$, Markov's inequality puts the tail expectation below $M/K^{\delta}$.

## The spike that keeps expectation one

Let $U$ be uniform on $(0,1)$ and set $X_n=n\,1_{\{U\le 1/n\}}$. Then $X_n\to 0$ almost surely, because each fixed $u>0$ eventually satisfies $1/n<u$, but $\mathbb{E} X_n=1$ for every $n$. For any threshold $K$, choose $n>K$. On $\{U\le 1/n\}$ one has $X_n=n>K$, and the tail expectation equals $1$. The supremum over $n$ never tends to $0$, so the family is not uniformly integrable, and the expectations do not converge to $\mathbb{E} 0=0$. By contrast, sample averages of independent copies with $\mathbb{E}|Y_1|<\infty$ are uniformly integrable, which is why the [strong law](strong-law.qmd) upgrades to $\mathbb{E}|\overline{Y}_n-\mu|\to 0$. Dominated convergence is the almost-sure case of the same bridge.
""",
    "uniformity-depends-on-a-domain": r"""
## A Jacobian states a local change of scale

Let $(\alpha, \beta)$ be positive hyperparameters of a beta population of rates. One convenient coordinate system is the mean weight $u = \alpha/(\alpha+\beta)$ and the scale $v = (\alpha+\beta)^{-1/2}$, so that $\alpha = u/v^2$ and $\beta = (1-u)/v^2$. Let $t = \alpha+\beta$. The absolute value of the [Jacobian](jacobian.qmd) determinant of $(u, v)$ with respect to $(\alpha, \beta)$ equals $\tfrac{1}{2}\, t^{-5/2}$. A density that is constant in the $(u, v)$ coordinates is therefore pushed forward to a weight $p(\alpha, \beta) \propto (\alpha+\beta)^{-5/2}$ on the positive quadrant. The determinant identity is local: it describes the transformation in the interior of the parameter space. It does not name the set over which a constant function of $(u, v)$ is to be integrated, and it does not make that constant into a probability.

## Infinite area is a modelling choice

If $u$ ranges over $(0,1)$ and $v$ ranges over $(0, \infty)$, the $(u, v)$ region has infinite area. No probability density is constant on a region of infinite area, so $(\alpha+\beta)^{-5/2}$ is an [improper prior](improper-prior.qmd). A posterior built from it may be used only after the normalising integral has been shown to be finite for the studies in hand. Restricting $v$ to a bounded interval $[\varepsilon, M]$ makes the prior proper, but the induced law of $(\alpha, \beta)$ depends on those cutoffs. If $\alpha$ and $\beta$ are instead independent exponential random variables with a common rate, the prior is proper, $u$ is uniform on $(0,1)$ and independent of $t$, and $t$ is gamma with shape $2$. The Jacobian does not choose the domain.
""",
    "unit-root": r"""
## A root at one, and a variance that grows like time

The autoregression $X_t=\phi X_{t-1}+\varepsilon_t$ is weakly stationary when the absolute value of $\phi$ is less than $1$. Its autoregressive polynomial is $1-\phi z$. A unit root means that this polynomial is zero at $z=1$, which forces $\phi=1$. The series is then the random walk $X_t=X_{t-1}+\varepsilon_t$. If $X_0$ is a fixed constant and $\operatorname{Var}(\varepsilon_t)=\sigma^2$, the walk is a sum of $t$ uncorrelated innovations, so

$$
\operatorname{Var}(X_t)=t\sigma^2.
$$

A weakly stationary series cannot have a variance that depends on $t$. One difference removes the root: $X_t-X_{t-1}=\varepsilon_t$. An [ARIMA model](arima-model.qmd) allows a stationary autoregressive moving-average series after $d$ such differences. The random walk is the case $d=1$ with no further terms.

## Two walks, and a slope that looks decisive

Regress one random walk on another independent random walk. The true slope is zero, because the walks share no innovation. The ordinary $t$ statistic of that slope does not settle as the series lengthens. Large values are typical, not rare. Granger and Newbold (1974) documented this spurious regression. The fitted residuals stay strongly autocorrelated, which is the warning hidden by a regression table that reports only the slope and its usual standard error. Differencing both series, or otherwise removing the unit roots, is what makes a slope interpretable as a relation between stationary variables. A unit-root test is a separate procedure, with a null of its own and a non-standard null distribution. Ignoring $t\sigma^2$ and treating the walk as a stationary autoregression is how the spurious slope acquires its false precision.
""",
    "vapnik-s-radius-margin-bound": r"""
## Capacity when every labelling must keep a margin

Ordinary affine half-spaces in $\mathbb{R}^p$ shatter some sets of size $p+1$, and no larger set, so their VC dimension is $p+1$. Vapnik's radius–margin bound asks a harder question. The points are confined to a ball of diameter $D$, and a set is counted only when every one of its $2^{h}$ binary labellings is realised by an affine separator whose geometric [margin](linear-separators-and-the-margin.qmd) is at least $\rho>0$. Let $h$ be the size of the largest such set. Then

$$
h\le\min\Bigl\{\Bigl\lceil\frac{D^2}{\rho^2}\Bigr\rceil,\, p\Bigr\}+1
$$

(Burges, 1998). The ratio $D^2/\rho^2$ is small when the slab is wide relative to the ball that holds the points. The ordinary VC dimension $p+1$ still caps the count, and it binds when $\rho$ is so small that the margin restriction has little force.

## A wide margin in a high-dimensional ball

Take $D=6$, $\rho=2$ and $p=20$. Then $D^2/\rho^2=9$, so $h\le\min\{9,\,20\}+1=10$. The class of all affine separators in $\mathbb{R}^{20}$ still has VC dimension $21$. What has shrunk is the largest set on which every labelling is achievable with margin at least $2$. One fitted separator that happens to have a large training margin does not lower the VC dimension of the whole class. The bound is a statement about a restricted shattering count. It is not a numerical upper bound on the test error of one training sample: that error also depends on the distribution of the pairs and on how the separator was chosen.
""",
    "variable-importance": r"""
## Impurity and permutation measures

A [random forest](random-forest.qmd) predicts by averaging many trees that were grown to disagree, so reading one tree does not describe the forest. Variable importance compresses the fit into a score for each predictor (Breiman, 2001). Two scores are in common use. The impurity score, often called mean decrease in impurity, adds up the drops in [node impurity](node-impurity.qmd) at every split that uses predictor $j$, then averages over the $T$ trees. For classification the impurity is usually the Gini index; for regression it is the residual sum of squares. The permutation score uses the [out-of-bag](out-of-bag-estimation-and-variable-importance.qmd) cases of each tree. Let $\mathrm{Err}_t$ be the error of tree $t$ on its out-of-bag sample, and let $\mathrm{Err}_t^{(j)}$ be the same error after the values of predictor $j$ in that sample have been randomly shuffled. The importance is the average rise

$$
\mathrm{VI}_j=\frac{1}{T}\sum_{t=1}^{T}\bigl(\mathrm{Err}_t^{(j)}-\mathrm{Err}_t\bigr).
$$

A large rise means the fitted trees were using $j$.

## Properties and correlated predictors

Suppose the out-of-bag error is $0.12$. Shuffling petal length raises it to $0.31$, so the permutation importance is $0.19$. Shuffling sepal width raises it to $0.13$, an importance of $0.01$. The same fit can report mean Gini decreases of $0.45$ and $0.05$. Both scores describe how this forest uses the variables. A causal effect would require an intervention, which the shuffle does not perform.

If petal length is duplicated, either copy can supply the splits. Permuting one copy leaves the other intact, and each $\mathrm{VI}_j$ can be small while the pair carries the signal. A continuous predictor offers more cutpoints than a binary one, so the impurity score can favour the continuous variable when the two are equally informative (Strobl, Boulesteix, Zeileis, and Hothorn, 2007). The forest, the impurity and the permutation scheme belong in the reported number.
""",
    "variance-ratio-f-pivot": r"""
## Scale each sample variance by its own $\sigma^2$

A ratio of sample variances still contains the unknown true variances. Cancel them and an $F$ law appears. Let two samples be independent and normal, of sizes $n_1$ and $n_2$, with variances $\sigma_1^2$ and $\sigma_2^2$. Let $s_1^2$ and $s_2^2$ be the bias-corrected sample variances, using divisors $n_1-1$ and $n_2-1$. By the normal sample theorem, $U=(n_1-1)s_1^2/\sigma_1^2$ is [chi-squared](chi-squared-distribution.qmd) on $n_1-1$ degrees of freedom, $V=(n_2-1)s_2^2/\sigma_2^2$ is chi-squared on $n_2-1$ degrees of freedom, and $U$ is independent of $V$. The [$F$ family](f-distribution.qmd) is defined by dividing each chi-squared variable by its degrees of freedom and taking the ratio:

$$
\frac{U/(n_1-1)}{V/(n_2-1)}=\frac{s_1^2/\sigma_1^2}{s_2^2/\sigma_2^2}\sim F_{n_1-1,n_2-1}.
$$

The means of the two samples do not appear. Under $\sigma_1^2=\sigma_2^2$ the pivot reduces to $s_1^2/s_2^2$, which is the statistic of the [equal-variance $F$ test](f-test-for-equal-variances.qmd). Solving the pivot for $\sigma_1^2/\sigma_2^2$ produces a confidence interval. When the two degrees of freedom are equal, $W\sim F_{m,m}$ implies $1/W\sim F_{m,m}$ as well, so the median of the pivot is exactly $1$.

## A raw ratio of four, and a pivot of one

Suppose $n_1=n_2=9$, $s_1^2=8$, $s_2^2=2$, $\sigma_1^2=4$ and $\sigma_2^2=1$. The raw ratio $s_1^2/s_2^2$ equals $4$. The pivot equals $(8/4)/(2/1)=1$, which is the median of $F_{8,8}$, not a surprise. The factor of four in the sample variances is the factor already present in the true variances. Heavy tails make $s_j^2$ more variable than the chi-squared laws allow, so the pivot is no longer $F$ and an interval built from $F$ quantiles has the wrong coverage.
""",
    "variogram": r"""
## How far the series moves, rather than where it sits

Often the useful question is how much a process changes between two times, not how far today's level sits from a historical mean. The variogram is that variance of a change, $\operatorname{Var}(X_s-X_t)$. When the process is [weakly stationary](weak-stationarity.qmd), with autocovariance $\gamma_h=\operatorname{Cov}(X_t,X_{t+h})$ and $\gamma_0=\operatorname{Var}(X_t)$, the variance of a difference expands to

$$
\operatorname{Var}(X_{t+h}-X_t)=2(\gamma_0-\gamma_h).
$$

The right-hand side depends on the two times only through the lag $h$. A variogram that rises and then levels off at $2\gamma_0$ belongs to a stationary series: at long lags the two values are uncorrelated, and the variance of their difference is twice the marginal variance. Some plots show half of this quantity, so the factor of $2$ has to be checked before two pictures are compared.

## A level variance that need not exist

Take a stationary autoregression with coefficient $0.5$ and $\gamma_0=4$. Then $\gamma_1=2$, and the lag-$1$ variogram is $2(4-2)=4$. At long lags the variogram levels off at $8$. A random walk has no such $\gamma_h$. Its level variance grows like $t\sigma^2$, so the covariance of the level is not a function of lag alone. The difference is still well behaved. $X_t-X_{t-h}$ is a sum of $h$ innovations and has variance $h\sigma^2$ when the innovations are uncorrelated and each has variance $\sigma^2$. At $\sigma^2=1$ the variogram at lags $1$, $2$ and $10$ equals $1$, $2$ and $10$, and it keeps climbing. That continued climb is the variogram's picture of a stochastic trend. Estimating it from one stretch still needs repetition: increments of a common lag should share a variance.
""",
    "vector-response-regression": r"""
## Several measurements that share one unit

One patient can contribute a systolic pressure and a heart rate. One site can contribute the presence or absence of several species. The independent unit is the patient or the site, and the response is a vector. Vector-response regression gives each component a mean model and then describes how the components are associated. Fitting each component by its own univariate regression estimates the margins and discards the association. That is not enough when the question is joint: both species present, both measurements high, both events observed. The joint probability is not determined by the marginal means alone.

## A joint cell the two margins do not fix

Suppose two binary components have $\mathbb{P}(Y_1=1)=0.3$ and $\mathbb{P}(Y_2=1)=0.4$. Independence would force $\mathbb{P}(Y_1=Y_2=1)=0.12$. An odds ratio of $2$, the odds of $Y_1=1$ when $Y_2=1$ divided by the odds of $Y_1=1$ when $Y_2=0$, raises the probability of the joint event to about $0.155$. The four cells, both present, only the first, only the second, and neither, are then about $0.155$, $0.145$, $0.245$ and $0.455$. The margins are unchanged and the joint event is more common than independence allows. A working model often stops at pairs. Marginal slopes can still be estimated, and a [sandwich estimator](sandwich-estimator.qmd) keeps the standard errors serviceable when that working association is wrong, provided the marginal means are right. The sandwich does not repair a margin that omitted a covariate the components actually depend on.
""",
    "ward-s-method": r"""
## The merge that least increases the sum of squares

Single linkage will chain along a path of near neighbours, and complete linkage will refuse a merge because one remote point inflates the diameter. Ward's method (Ward, 1963) uses a third question, the same one [k-means](k-means-criterion.qmd) asks of a finished partition: how large is the total within-cluster sum of squares? Start with each point as a cluster. At each step merge the two clusters $A$ and $B$ whose union increases that sum by the least. If $n_A$, $n_B$ and $\bar{\mathbf{x}}_A$, $\bar{\mathbf{x}}_B$ are the sizes and means, the increase is

$$
\Delta(A,B)=\frac{n_A n_B}{n_A+n_B}\,\|\bar{\mathbf{x}}_A-\bar{\mathbf{x}}_B\|^2.
$$

Cluster means make the formula a Euclidean construction. An arbitrary dissimilarity has no means, so the increase is then undefined.

## A four-point merge, and the two implementations

Take the sets $A=\{0,2\}$, $B=\{3\}$ and $C=\{10\}$ on the line. Then $\bar x_A=1$, and

$$
\Delta(A,B)=\frac{2\cdot 1}{3}\,(1-3)^2=\frac{8}{3},
\qquad
\Delta(B,C)=\frac{1}{2}\,(3-10)^2=24.5,
\qquad
\Delta(A,C)=\frac{2}{3}\,(1-10)^2=54.
$$

The first merge is $A$ with $B$. The within-cluster sum of squares of $\{0,2\}$ is $2$, and that of $\{0,2,3\}$ is $14/3$, an increase of $8/3$, matching $\Delta$. In the usual hierarchical routine, `ward.D2` applied to Euclidean distances implements this increase. The routine named `ward.D` scales the dissimilarities differently and does not minimise the sum of squares (Murtagh and Legendre, 2014).

The increase charges Euclidean radius, so compact clusters of similar spread are the clusters the criterion prefers. An elongated cloud can be split along its long direction. On one [iris](iris-data.qmd) sample, a three-group Ward cut agrees with the species labels more closely, by the [adjusted Rand index](adjusted-rand-index.qmd), than the three-group cuts from single, complete and average linkage. That index uses labels the clustering never saw. Using it to pick the linkage would spend those labels on model selection.
""",
    "weibull-distribution": r"""
## A hazard that is a power of time

Constant hazard means a lifetime that does not age. Many components either wear out or fail early and then settle. The Weibull family keeps a simple survival function and lets the hazard rise or fall (Weibull, 1951). A lifetime $T>0$ has shape $\beta>0$ and rate $\lambda>0$ when

$$
\mathbb{P}(T>t)=\exp\{-(\lambda t)^{\beta}\},\qquad t>0.
$$

The density is $f(t)=\lambda\beta(\lambda t)^{\beta-1}\exp\{-(\lambda t)^{\beta}\}$. Dividing $f$ by the survival function gives the [hazard](hazard-rate.qmd) $h(t)=\lambda\beta(\lambda t)^{\beta-1}$. Shape decides the ageing. If $\beta>1$ the hazard increases. If $\beta<1$ it decreases. If $\beta=1$ the hazard is the constant $\lambda$, and $T$ is [exponential](exponential-distribution.qmd) with rate $\lambda$, hence memoryless. The mean is $\mathbb{E} T=\Gamma(1+1/\beta)/\lambda$, where $\Gamma$ is the gamma function. In particular $\Gamma(1/2)=\sqrt{\pi}$ and $\Gamma(3/2)=\sqrt{\pi}/2\approx 0.886$.

Some writers use a scale $\theta=1/\lambda$ and write the survival as $\exp\{-(t/\theta)^{\beta}\}$. The mean is then $\theta\,\Gamma(1+1/\beta)$. Substituting a rate into a scale formula, or the reverse, multiplies the mean by a factor of $\lambda^2$ (for example turning $886$ hours at $\lambda=0.001$ into $0.000886$ hours).

## Eight hundred and eighty-six hours

Take $\beta=2$ and $\lambda=0.001$ per hour. The mean is about $0.886/0.001=886$ hours. The hazard is $h(t)=2\lambda^2 t=2\times 10^{-6}\,t$, linear in time. At $500$ hours it is $0.001$ per hour; at $1000$ hours it is $0.002$ per hour. Twice the age, twice the hazard. A uniform $U$ on $(0,1)$ produces a draw by inverting the survival function: $(\lambda T)^{\beta}=-\log U$, so $T=\lambda^{-1}(-\log U)^{1/\beta}$. A single shape cannot make a bathtub hazard that falls and later rises. That pattern needs a mixture, or separate pieces, rather than one Weibull term.
""",
    "white-noise": r"""
## Innovations with nothing left for a linear forecast

White noise is the innovation sequence inside a time-series model: uncorrelated variables $\varepsilon_t$ with mean $0$ and one common variance $\sigma^2$. The autocovariance equals $\sigma^2$ at lag $0$ and equals $0$ at every other lag, so the autocorrelation is a spike of height $1$ at the origin. The best linear forecast of a future innovation, given the past, is $0$ at every horizon, and the forecast-error variance stays $\sigma^2$. Residuals from a fitted autoregression are compared with this pattern. For a series of length $T=100$, a residual autocorrelation beyond about $1.96/\sqrt{T}=0.196$ in absolute value is larger than the usual null fluctuation of white noise. A value $0.05$ is compatible with the pattern. A value $0.45$ is not.

## Uncorrelated is weaker than independent

Gaussian white noise is independent, because the variables are jointly normal and uncorrelated, and uncorrelated jointly normal variables are independent (marginal normality alone is not enough). In general, uncorrelated does not mean independent. Let $z_t$ be independent standard normal variables and set $\varepsilon_t=z_t z_{t-1}$. Then $\mathbb{E}(\varepsilon_t)=0$ and $\operatorname{Var}(\varepsilon_t)=1$. For $s\neq t$ the product inside $\operatorname{Cov}(\varepsilon_s,\varepsilon_t)$ contains some $z$ to the first power and has mean $0$, so $\{\varepsilon_t\}$ is white noise. The squares are dependent: $\varepsilon_t^2=z_t^2 z_{t-1}^2$ and $\varepsilon_{t-1}^2=z_{t-1}^2 z_{t-2}^2$ share the factor $z_{t-1}^2$. A large squared innovation tends to be followed by another. No linear function of the past forecasts $\varepsilon_t$, but a function of past squares can forecast $\varepsilon_t^2$. A series can therefore pass an autocorrelation check and still have forecastable volatility, which is the opening that [ARCH and GARCH models](arch-and-garch-models.qmd) are built to use.
""",
    "why-the-raw-sum-of-squares-cannot-choose": r"""
## The criterion falls every time a cluster is split

The within-cluster sum of squares $W$ measures how tightly the points of each cluster sit around their cluster mean. Split one cluster into two nonempty pieces and recompute the two means. The sum of squared distances to the means cannot rise, because each point may move to a centre at least as close as the old common mean, and it falls whenever the two pieces have different means. At $k=n$ every cluster is a single point, every squared distance is $0$, and $W=0$. Minimising $W$ over the number of clusters therefore selects the largest $k$ on the list. The objective that justifies the partition, once $k$ is fixed, does not choose $k$.

## Three points, and the comparison the gap makes

For the points $0$, $1$ and $10$, the one-cluster mean is $11/3$ and

$$
W^{(1)}=\Bigl(0-\frac{11}{3}\Bigr)^2+\Bigl(1-\frac{11}{3}\Bigr)^2+\Bigl(10-\frac{11}{3}\Bigr)^2=\frac{546}{9}\approx 60.67.
$$

The two-cluster partition $\{0,1\}$ and $\{10\}$ has $W^{(2)}=0.5$. The three-cluster partition has $W^{(3)}=0$. The smallest value is at $k=3$, even when the large gap that a reader notices is the gap between $1$ and $10$. The [gap statistic](choosing-k-the-gap-statistic.qmd) compares $\log W_{\mathrm{data}}^{(k)}$ with the average of $\log W$ on reference samples that keep the coordinate-wise range and have no cluster structure (Tibshirani, Walther, and Hastie, 2001). Those reference curves also fall with $k$. A large gap means the data curve has fallen further than the featureless reference. The usual rule takes the smallest $k$ such that $\mathrm{Gap}(k)$ is at least $\mathrm{Gap}(k+1)$ minus a standard-error term from the reference draws.
""",
    "wilcoxon-rank-sum-test": r"""
## A shift scored only by order

Two independent samples can differ by a shift when neither is close to normal and both are too small for a $t$ interval to be comfortable. The Wilcoxon rank-sum test (Wilcoxon, 1945) discards the numerical spacing and keeps the order. Pool the samples, rank the combined observations from $1$ to $N$, and let $W$ be the sum of the ranks that fall in the first sample, of size $n_1$. If the two populations have the same continuous distribution, every subset of $n_1$ ranks out of $N$ is equally likely. The null mean of $W$ is $n_1(N+1)/2$. A very small or very large $W$ is evidence of a shift.

## A rank sum of eight, and the effect of a tie

Take the samples $1,4,6$ and $3,8,11$. The pooled order is $1,3,4,6,8,11$, so the first sample holds ranks $1,3,4$ and $W=8$. With $n_1=n_2=3$ and $N=6$, the null mean is $3\times 7/2=10.5$. The observed sum lies $2.5$ below that mean. There are $20$ equally likely ways to choose three ranks out of six, and four of those ways sum to $8$ or less, so a one-sided null probability is $4/20=0.2$. No normal assumption entered. Ties break the continuous-distribution step, because tied values have no unique order. Each tied observation is given the average of the ranks it shares: two values tied for ranks $2$ and $3$ each receive $2.5$. The null variance is then smaller than the no-tie formula $n_1 n_2(N+1)/12$, and a probability that ignores the tie correction is not the Wilcoxon probability.
""",
    "wishart-distribution": r"""
## A matrix of summed outer products

The Wishart law is the sampling distribution of a scatter matrix built from Gaussian vectors (Wishart, 1928). Let $\mathbf{U}_1,\ldots,\mathbf{U}_\nu$ be independent $\operatorname{N}_p(\mathbf{0},\Sigma)$ draws, with $\Sigma$ positive definite. Their outer-product sum $W=\sum_{m=1}^{\nu}\mathbf{U}_m\mathbf{U}_m^\top$ is written $W\sim W_p(\Sigma,\nu)$. Linearity gives $\mathbb{E}(W)=\nu\Sigma$ without using the density. When $\nu\ge p$ the matrix $W$ is positive definite with probability $1$ and has the density displayed in the definition, on the cone of positive-definite matrices. When $\nu<p$ the same outer-product sum is singular and does not have a density on that full cone. For $p=1$ and $\Sigma=\sigma^2$, $W/\sigma^2$ is chi-squared on $\nu$ degrees of freedom. Two standard normal scalars $1$ and $-1$ give $W=1^2+(-1)^2=2$, one draw from $W_1(1,2)$, whose expectation is $2$.

## The scatter of a normal sample

For an independent sample of size $n$ from $\operatorname{N}_p(\boldsymbol{\mu},\Sigma)$, the corrected cross-product matrix $A$ obeys $A\sim W_p(\Sigma, n-1)$. The degrees of freedom are $n-1$, not $n$, because the sample mean was removed: one linear constraint is spent on each coordinate. Thus $\mathbb{E}(A)=(n-1)\Sigma$. Dividing by $n-1$ produces an unbiased covariance; dividing by $n$ produces the maximum-likelihood covariance, whose expectation is $(n-1)/n\,\Sigma$. The density formula with $\nu=n-1$ has $|A|^{(n-p-2)/2}$ in the numerator, which is the general power $(\nu-p-1)/2$ at this $\nu$. Hotelling's exact $F$ calibration uses this Wishart law together with the independence of $A$ and the sample mean. A consistent covariance from non-Gaussian vectors can still have expectation proportional to $\Sigma$, and it is not Wishart, so probabilities read from the Wishart density are then the wrong probabilities.
""",
    "wold-decomposition": r"""
## Stationary dependence as noise, plus a predictable piece

Linear forecasting of a weakly stationary series is limited by a representation (Wold, 1938). If $\{X_t\}$ has mean $0$, a constant variance and a covariance that depends only on lag, then

$$
X_t=\sum_{j=0}^{\infty} a_j\varepsilon_{t-j}+\nu_t.
$$

The innovations $\varepsilon_t$ are uncorrelated, with mean $0$ and variance $\sigma^2$. The coefficients $a_j$ are constants, and the scale is usually chosen so that $a_0=1$, leaving $\sigma^2$ to carry the innovation variance. The term $\nu_t$ is determined by its own past: some linear function of $\{\nu_s:s<t\}$ predicts it exactly. The innovations are uncorrelated with $\nu_t$. If the series has mean $\mu$, add $\mu$ on the right-hand side. Every weakly stationary series is therefore an infinite moving average of uncorrelated noise, plus a piece that a linear forecast can call exactly. The moving-average piece is where [white noise](white-noise.qmd) enters the model.

## A short moving average, and a pure seasonal term

The series $X_t=\varepsilon_t+0.4\varepsilon_{t-1}$ is already in the form above: $a_0=1$, $a_1=0.4$, every later coefficient is $0$, and $\nu_t=0$. Once the latest innovation has been recovered, the one-step forecast is $0.4\varepsilon_T$, and every horizon past one step forecasts $0$. A random-phase seasonal harmonic $\nu_t=A\cos(2\pi t/12)+B\sin(2\pi t/12)$, with $A$ and $B$ uncorrelated, mean $0$ and equal finite variance, is the other piece: it is weakly stationary, two of its own lags determine its whole future via $\nu_t=2\cos(2\pi/12)\nu_{t-1}-\nu_{t-2}$, and it stays uncorrelated with the innovations when added beside a moving average (whereas a deterministic cosine with fixed amplitude has a time-varying mean and is not weakly stationary). The representation does not apply to a random walk. A walk is not weakly stationary, the variance $t\sigma^2$ is not constant, and there is no decomposition of this kind until the walk has been differenced.
""",
    "zero-one-loss-and-risk": r"""
## The conditional probability of a mistake

Zero–one loss charges $0$ for a correct label and $1$ for every wrong label. At a fixed measurement $\mathbf{x}$, the class $Y$ is random with $\mathbb{P}(Y=g\mid X=\mathbf{x})=\tau_g(\mathbf{x})$. If the classifier returns class $h$, the conditional expected loss is the posterior probability that $Y\neq h$,

$$
\mathbb{E}\bigl[l(Y,h)\mid X=\mathbf{x}\bigr]=1-\tau_h(\mathbf{x}).
$$

No normality is required: the identity uses only that the loss is $0$ on the predicted class and $1$ on the others, and that $\mathbb{E}(Y_g\mid\mathbf{x})=\tau_g(\mathbf{x})$ for the class indicators. The [Bayes rule](bayes-optimal-rule.qmd) chooses an $h$ with the largest $\tau_h(\mathbf{x})$, which makes this conditional risk as small as the posteriors allow. Integrating over $X$ gives the same ranking for the overall error rate.

## A three-class posterior, and a change of costs

Let $\tau(\mathbf{x})=(0.7,0.2,0.1)$. Predicting class $1$ has conditional zero–one risk $0.3$. Predicting class $2$ has risk $0.8$. Predicting class $3$ has risk $0.9$. The zero–one rule returns class $1$. Replace the loss by unequal costs $c_{gh}$, still with $c_{gg}=0$, and the conditional risk of predicting $h$ becomes $\sum_{g\neq h}\tau_g(\mathbf{x})\,c_{gh}$. Suppose a missed class $2$ costs $5$ and every other mistake costs $1$. Predicting class $1$ then costs $0.2\cdot 5+0.1\cdot 1=1.1$. Predicting class $2$ costs $0.7\cdot 1+0.1\cdot 1=0.8$. Predicting class $3$ costs $0.7\cdot 1+0.2\cdot 5=1.7$. The minimum is class $2$. The posteriors did not change. The loss did, and the optimal action moved with it. A fitted $\hat\tau$ plugged into the same comparison is a plug-in rule. Its training error can fall below the Bayes risk, because that error reuses the cases that built the rule.
""",
}
