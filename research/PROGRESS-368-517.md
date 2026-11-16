# Depth pass ranks 368–517

Integration branch: `research/depth-pass-ranks-368-517`. Brief: [depth-brief-368-517.md](depth-brief-368-517.md). Ranks 68–217 and 218–367 are handled on other branches and are not touched here.

## Setup

- The Dodge (2008) source was not available in this session (`research/check_sources.py` failed on both standard paths). On the owner's instruction the pass continues without it: no new prose cites `dodge2008`.
- Open textbooks were downloaded and split into per-page text outside the repository at `/workspace/statwiki-sources/open/`: Gelman et al. (BDA3), Bishop, Durrett, Grinstead–Snell, Levin–Peres, MacKay, Shalizi and two Owen chapters. Elements of Statistical Learning, ISL, CASI and Boyd–Vandenberghe were not reachable from this machine (moved files or a bot check), so they are not cited for new claims.
- Four shared works were registered before the batches started so that batches do not create clashing keys: `levin_peres2017`, `mackay2003`, `shalizi_ada2026`, `owen2013_mc`.
- Theorem and distribution pages now accept a researched `Check yourself` section, placed where the existing section-order tests expect it. Every page type in this range carries one.
- `research/check_depth_pass.py` applies the research-page rules to these ranks, including a stricter ban on editor wording (inherited, retained, existing, original, kept, opened). `research/apply_pending.py` overlays and applies the shared-file proposals in `research/pending/`.
- `scripts/oai.py` calls the OpenAI API through the session proxy (the credential is injected by the proxy; `OPENAI_API_KEY` is unset in the shell). Drafts use `gpt-5.4-mini`; reviews use `gpt-5.5`. Responses are cached in the git-ignored `research/.oai-cache/`.
- The build regenerates `proofs-todo.json` with generic reasons; integration keeps the specific reasons committed at HEAD and those proposed in pending files.

## Batches

### Batch U — ranks 368–382

Ranks: 368 proportional-hazards-model, 369 recurrence-and-period, 370 response-variable, 371 seasonality, 372 thinning-a-markov-chain, 373 trend, 374 welch-interval, 375 wold-decomposition, 376 birth-death-balance, 377 consistent-estimator, 378 cover-hart-bound, 379 grid-monte-carlo-approximation, 380 law-of-total-probability, 381 nettalk, 382 offspring-probability-generating-function.

Status: not started.

### Batch V — ranks 383–397

Ranks: 383 proper-prior-and-proper-posterior, 384 strict-stationarity, 385 confusion-matrix, 386 doubly-stochastic-matrix, 387 graphical-lasso, 388 hitting-probabilities, 389 joint-probability-mass-function, 390 margin-of-error, 391 poisson-limit-of-the-binomial, 392 behrens-fisher-problem, 393 binomial-test, 394 box-muller-method, 395 confidence-region-for-a-normal-mean-vector, 396 deviance-residual, 397 dual-problem.

Status: not started.

### Batch W — ranks 398–412

Ranks: 398 gaussian-graphical-models, 399 generalised-likelihood-ratio-test, 400 hazard-rate, 401 hypergeometric-distribution, 402 invariance-of-maximum-likelihood, 403 label-switching, 404 neyman-pearson-approach, 405 nonhomogeneous-poisson-process, 406 one-hot-encoding, 407 perceptron, 408 regression-effect, 409 throughput, 410 uniform-integrability, 411 bagging, 412 bradley-terry-model.

Status: not started.

### Batch X — ranks 413–427

Ranks: 413 distance-to-a-hyperplane, 414 extinction-criterion, 415 inverse-transform-method, 416 neyman-pearson-lemma, 417 uniformly-most-powerful-test, 418 limiting-distribution, 419 sampling-bias, 420 sylvester-s-criterion, 421 addiction-data, 422 agglomerative-and-divisive-clustering, 423 alon-colon-cancer-data, 424 atom-of-a-distribution, 425 basu-s-theorem, 426 blocking-probability, 427 characteristic-functions.

Status: not started.

### Batch Y — ranks 428–442

Ranks: 428 clotting-time-data, 429 cross-validation-of-the-likelihood, 430 cycle, 431 exponential-loss, 432 exponential-tails-and-the-gumbel-law, 433 finite-irreducible-chains, 434 fisher-s-exact-test, 435 gaussian-process, 436 gibbs-inequality, 437 intensity-function, 438 interarrival-time, 439 intraclass-correlation, 440 ising-model, 441 iteratively-reweighted-least-squares, 442 kernel-trick.

Status: not started.

### Batch Z — ranks 443–457

Ranks: 443 kolmogorov-extension-theorem, 444 kolmogorov-forward-and-backward-equations, 445 kyphosis-data, 446 lehmann-scheffe-theorem, 447 linear-congruential-generator, 448 marginal-variance-posterior, 449 measurement-error, 450 metropolis-algorithm, 451 moments-of-the-sample-mean-and-variance, 452 monotone-convergence-fatou-and-dominated-convergence, 453 natural-exponential-family, 454 paired-comparison, 455 partially-linear-model, 456 power-law-tails-and-the-frechet-law, 457 probability-generating-function.

Status: not started.

### Batch AA — ranks 458–472

Ranks: 458 rao-blackwell-theorem, 459 separating-set, 460 sequential-coherence, 461 signed-distance, 462 soft-margin-slack-variables, 463 soft-thresholding-for-orthonormal-predictors, 464 subset-selection-and-shrinkage, 465 superposition-and-thinning, 466 two-sample-hotelling-test, 467 variance-ratio-f-pivot, 468 arch-and-garch-models, 469 asymptotic-relative-efficiency, 470 cholesky-decomposition, 471 choosing-k-the-gap-statistic, 472 cost-complexity-pruning.

Status: not started.

### Batch AB — ranks 473–487

Ranks: 473 decision-stump, 474 fisher-s-linear-discriminant-analysis, 475 gamma-regression, 476 jackknife, 477 laplace-approximation, 478 m-m-queue, 479 negative-predictive-value, 480 perceptron-learning-rule, 481 randomised-controlled-trial, 482 scaled-deviance, 483 expected-duration-of-a-random-walk, 484 generalised-linear-mixed-model, 485 a-finite-stationary-point-is-a-global-maximiser, 486 a-hypothesis-region-is-not-a-separate-model, 487 a-single-threshold-unit-cannot-compute-xor.

Status: not started.

### Batch AC — ranks 488–502

Ranks: 488 a-zero-precision-entry-is-conditional-independence, 489 affine-images-of-normal-vectors, 490 anova-f-distribution, 491 backpropagation-batch-form, 492 basic-gradient-descent-learning, 493 bayes-action-for-two-hypotheses, 494 bayes-optimal-rule, 495 beta-binomial-posterior-prediction, 496 blocks-in-analysis-of-variance, 497 bootstrap-error-and-the-correction, 498 brier-score, 499 coefficient-of-determination, 500 conditional-coefficient-posterior, 501 delta-rule, 502 direct-posterior-simulation.

Status: not started.

### Batch AD — ranks 503–517

Ranks: 503 dirichlet-moments, 504 distribution-of-a-function-or-a-sum, 505 em-for-a-normal-mixture, 506 empirical-bayes, 507 epanechnikov-kernel, 508 equally-likely-outcomes, 509 exchangeable-correlation, 510 f-test-for-equal-variances, 511 factor-analysis, 512 family-wise-control-implies-false-discovery-control, 513 fisher-s-direction, 514 fold-cross-validation, 515 full-conditionals-under-independent-priors, 516 gradient-boosting, 517 hard-margin-dual.

Status: not started.

## OpenAI usage

Token counts per batch from `python scripts/oai.py --usage`.

| Batch | Calls | Prompt tokens | Completion tokens | Used for |
|:--|--:|--:|--:|:--|
| Setup | 2 | 35 | 27 | Connectivity check |
