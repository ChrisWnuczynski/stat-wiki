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
