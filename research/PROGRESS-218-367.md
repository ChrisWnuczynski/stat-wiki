# Depth pass ranks 218–367

Integration branch: `research/depth-pass-ranks-218-367`.

Shared bibliography works are added only when the key is absent and the offline citation schema accepts the entry. Proof gaps on concept pages are recorded in `research/todo.md`. `proofs-todo.json` stays limited to unproved result pages, which is what the unit test checks. `research/PROGRESS.md` is left unchanged.

## Batch K — ranks 218–232

Ranks: 218 memoryless-property, 219 simple-linear-regression, 220 time-series, 221 baseline-category-logit-model, 222 communicating-classes, 223 fisher-scoring, 224 multicollinearity, 225 pareto-distribution, 226 white-noise, 227 least-squares-line, 228 poisson-regression, 229 undirected-graph, 230 posterior-membership, 231 sums-of-smooth-functions, 232 hotelling-s-t2-test.

Pages fixed:

- memoryless-property: the converse now uses the words “Conversely” and “only continuous memoryless”, matching the proved statement.
- hotelling-s-t2-test: the opening sentence no longer places mathematics on the generated lead line.
- baseline-category-logit-model: the softmax link now points at `softmax-is-multinomial-logistic-regression`, because there is no `softmax-function` page.

Conflicts: none. The batch fast-forwarded from `origin/main`.

Tests: `build_wiki.py` wrote 718 articles and 557 question pages. `python3 -m unittest discover` passed 67 tests. `verify_citations.py --offline` passed 469 works. `git diff --check` passed. All 15 page checks passed.

Unverified:

- New bibliography keys (`r_nnet_multinom2026`, `siegrist2022_markov_recurrence`, `siegrist2022_markov_period`, `scipy_f2026`, `scipy_pareto2026`, `nist_linear_model2002`, `nist_ls_straight2002`, `r_mgcv_gam2026`) passed the offline schema only. Live URL checks were not run.
- Fisher scoring: the 1972 Nelder–Wedderburn paper was not opened.
- Simple linear regression: the \(t_{n-2}\) slope pivot was not re-derived.
- Baseline-category logit: a textbook page beyond the nnet manual was not opened.
- Hotelling's Wishart null distribution and the general Hammersley–Clifford equivalence for undirected graphs remain unproved. They are logged in `research/todo.md` rather than `proofs-todo.json`.

## Batch L — ranks 233–247

Ranks: 233 probability-space, 234 roughness-penalty, 235 strong-law, 236 wishart-distribution, 237 geometric-distribution, 238 kullback-leibler-divergence, 239 learning-rate, 240 markov-s-inequality, 241 minimal-sufficiency, 242 single-complete-and-average-linkage, 243 bonferroni-correction, 244 generator, 245 hierarchical-clustering, 246 limit-theorems, 247 output-coding-softmax-and-cross-entropy.

Pages fixed:

- bonferroni-correction: the opening sentence no longer uses mathematics, and the loose-bound sentence states the fact directly.
- geometric-distribution and wishart-distribution: the statistical-inference heading keeps the canonical title the distribution test requires. The specific labels stay as the first sentence of each section.

Conflicts: none.

Tests: `build_wiki.py` wrote 718 articles and 557 question pages. Unit tests passed (67). Offline citation check passed (469 works). `git diff --check` passed. All 15 page checks passed. The strong-law page and the geometric memoryless property left `proofs-todo.json` because those proofs are now on the pages.

Unverified:

- No new bibliography keys.
- Markov's inequality todo records a comparison note only; no further source was opened for that line.
- Spot-check of probability-space and output-coding-softmax-and-cross-entropy found complete proofs and worked numbers. No further prose change.

## Batch M — ranks 248–262

Ranks: 248 pooled-variance, 249 designed-experiment, 250 marginal-and-conditional-effects, 251 significance-level, 252 posterior-hypothesis-probability, 253 cauchy-schwarz-inequality, 254 galton-watson-process, 255 gaussian-linear-model, 256 interquartile-range, 257 inverse-gaussian-distribution, 258 detailed-balance, 259 effective-sample-size, 260 global-balance-and-detailed-balance, 261 pearson-residual, 262 stationary-and-independent-increments.

Pages fixed:

- gaussian-linear-model: the design-matrix sentence now states that the entries may have been measured and that their uncertainty is outside the model.
- effective-sample-size: the shared lead now finishes the sentence from the research prose.
- detailed-balance: the opening sentence no longer places mathematics on the generated lead line.

Conflicts: none.

Tests: `build_wiki.py` wrote 718 articles and 557 question pages. Unit tests passed (67). Offline citation check passed (470 works). `git diff --check` passed. All 15 page checks passed.

Unverified:

- `nist_doe_intro2002` passed the offline schema. The designed-experiment article still cites Dodge only; §5.1.1 was not inserted into the prose.
- Copied citations listed in the research todo still have no new page locators: Cauchy–Schwarz, detailed balance, Galton–Watson, marginal effects, Pearson residual, pooled variance, posterior hypothesis probability, significance level, and stationary increments.
- Inverse Gaussian: Tweedie (1957) was not opened. The distribution template has no Check yourself slot, so that research heading is not a generated section.
- Spot-check of pooled-variance and stationary-and-independent-increments found numerical examples and sourced definitions. No further prose change.

## Batch N — ranks 263–277

Ranks: 263 complete-linkage, 264 count-models-beyond-the-poisson, 265 single-linkage, 266 leave-one-out-cross-validation, 267 nested-cross-validation, 268 trace-plot, 269 partial-correlation, 270 random-slopes, 271 cauchy-distribution, 272 clique, 273 conway-maxwell-poisson-distribution, 274 multinomial-distribution, 275 student-t-distribution, 276 average-linkage, 277 cubic-smoothing-spline.

Pages fixed: none. Spot-check of complete-linkage and cubic-smoothing-spline found sourced definitions, proofs, and worked numbers. “Retained draws” on the trace plot is the Monte Carlo term.

Conflicts: none.

Tests: `build_wiki.py` wrote 718 articles and 557 question pages. Unit tests passed (67). Offline citation check passed (470 works). `git diff --check` passed. All 15 page checks passed.

Unverified:

- No new bibliography keys.
- Cauchy sample averages, the natural-cubic minimiser, and the Gaussian precision-block identity remain unproved and are logged in `research/todo.md`.

## Batch O — ranks 278–292

Ranks: 278 gram-matrix, 279 soft-margin-primal, 280 tukey-intervals, 281 uniformly-minimum-variance-unbiased-estimator, 282 cramer-rao-lower-bound, 283 fisher-neyman-factorisation, 284 logit-probit-and-complementary-log-log-links, 285 principal-component-directions-and-scores, 286 benjamini-hochberg, 287 sample-variance-and-standard-deviation, 288 link-function, 289 wald-test, 290 ancillary-statistic, 291 chapman-kolmogorov-equations, 292 count-responses.

Pages fixed:

- ancillary-statistic, cramer-rao-lower-bound, and fisher-neyman-factorisation: shared leads now use the pending field, capitalisation, and proper-name flag.
- fisher-neyman-factorisation: the statement heading stays `Statement`, which the result-page test requires. The specific label remains the first sentence.

Conflicts: none.

Tests: `build_wiki.py` wrote 718 articles and 557 question pages. Unit tests passed (67). Offline citation check passed (470 works). `git diff --check` passed. All 15 page checks passed. Fisher–Neyman left `proofs-todo.json` because the discrete direction is proved on the page.

Unverified:

- No new bibliography keys.
- Ten partial proofs are logged in `research/todo.md`: Basu independence, the false-discovery-rate bound, convergence of transition powers, the multiparameter Cramér–Rao bound, the dominated-family converse, successive principal-component directions, the soft-margin KKT characterisation, the studentised-range density, Lehmann–Scheffé uniqueness, and the Wald asymptotic null.
- Spot-check of gram-matrix and count-responses found sourced definitions and proofs. No further prose change.

## Batch P — ranks 293–307

Ranks: 293 first-passage-time, 294 five-number-summary-and-boxplot, 295 identity-link, 296 newton-raphson-method, 297 normal-sample-theorem, 298 sigma-algebra, 299 complete-separation, 300 dummy-variable-coding, 301 lloyd-s-k-means-algorithm, 302 m-m-1-queue, 303 markov-properties-and-factorisation, 304 maximum-likelihood-in-a-glm, 305 proportional-odds-model, 306 restricted-maximum-likelihood, 307 sparsity.

Pages fixed: none. Spot-check of first-passage-time and sparsity found sourced definitions and worked calculations.

Conflicts: none.

Tests: `build_wiki.py` wrote 718 articles and 557 question pages. Unit tests passed (67). Offline citation check passed (470 works). `git diff --check` passed. All 15 page checks passed. The normal-sample-theorem entry in `proofs-todo.json` now records why the orthogonal-transformation argument is not in a proof box.

Unverified:

- No new bibliography keys.
- Complete separation's general existence theorem, the Hammersley–Clifford converse, and general REML remain unproved and are logged in `research/todo.md`.

## Batch Q — ranks 308–322

Ranks: 308 stochastic-gradient-descent, 309 stochastic-process, 310 tower-property, 311 wald-interval, 312 weight-initialisation, 313 early-stopping, 314 epoch, 315 random-forest, 316 gini-index, 317 out-of-bag-estimation-and-variable-importance, 318 adjusted-rand-index, 319 bids-for-a-bankrupt-firm, 320 chi-squared-test-of-independence, 321 complete-data-likelihood, 322 countable-additivity.

Pages fixed:

- adjusted-rand-index: the shared lead now ends with identical partitions scoring one and chance agreement scoring about zero.
- tower-property: the statement heading stays `Statement`. The specific label remains the first sentence.

Conflicts: none.

Tests: `build_wiki.py` wrote 718 articles and 557 question pages. Unit tests passed (67). Offline citation check passed (470 works). `git diff --check` passed. All 15 page checks passed.

Unverified:

- No new bibliography keys.
- The bankrupt-firm log-mean multiplier still needs a page-located source. Dodge's name for a stochastic process is the infinite-index case; the page also allows a finite index.
- Chi-squared convergence under estimated margins, the early-stopping weight-decay identification, stochastic-approximation convergence, and plug-in Wald coverage remain unproved and are logged in `research/todo.md`.
- Spot-check of stochastic-gradient-descent and countable-additivity found sourced definitions. No further prose change.

## Batch R — ranks 323–337

Ranks: 323 discrete-time-markov-chain, 324 f-distribution, 325 hammersley-clifford, 326 hinge-loss, 327 holding-time, 328 loadings, 329 missing-data, 330 multivariate-central-limit-theorem, 331 normal-quantile-plot, 332 positive-continuous-responses, 333 regression-slope, 334 weibull-distribution, 335 adaboost, 336 arima-model, 337 bias-of-an-estimator.

Pages fixed:

- f-distribution and weibull-distribution: the definition heading stays `Definition`.
- hammersley-clifford and multivariate-central-limit-theorem: the statement heading stays `Statement`.

Conflicts: none.

Tests: `build_wiki.py` wrote 718 articles and 557 question pages. Unit tests passed (67). Offline citation check passed (474 works). `git diff --check` passed. All 15 page checks passed. The F reciprocal proof cleared the catalogue variance-ratio and ANOVA entries from `proofs-todo.json`. Those two gaps are in `research/todo.md`. Hammersley–Clifford and the multivariate central limit theorem remain in `proofs-todo.json` with the longer reasons from the pending files.

Unverified:

- New bibliography keys passed the offline schema only: `schapire2013_explaining_adaboost`, `nist_f_distribution`, `nist_qq_plot`, `nist_least_squares`. Live URL checks were not run.
- The variance-ratio F pivot and the ANOVA F law are not proved on the F page.
- Spot-check of discrete-time-markov-chain and bias-of-an-estimator found sourced definitions. No further prose change.

## Batch S — ranks 338–352

Ranks: 338 boosting, 339 borel-cantelli-lemmas, 340 confounding-variable, 341 dirichlet-multinomial-conjugacy, 342 false-discovery-rate, 343 little-s-law, 344 local-balance, 345 nominal-responses, 346 precision-weighting, 347 product-rule, 348 dendrogram, 349 extinction-probability, 350 null-deviance, 351 ordinal-responses, 352 partial-autocorrelation.

Pages fixed:

- little-s-law: the shared lead now uses the name “Little's law”.
- partial-autocorrelation: the opening sentence no longer places mathematics on the generated lead line.
- dirichlet-multinomial-conjugacy and product-rule: statement, intuition, and related-concept headings that the result tests read stay canonical. The specific labels remain in the sections.
- borel-cantelli-lemmas: removed from `proofs-todo.json` because the page now proves the logged lemmas. No other proof-todo slug was removed.

Conflicts: none.

Tests: `build_wiki.py` wrote 718 articles and 557 question pages. Unit tests passed (67). Offline citation check passed (474 works). `git diff --check` passed. All 15 page checks passed.

Unverified:

- No new bibliography keys.
- Durrett's pairwise second lemma (Theorem 2.3.9) is not proved on the Borel–Cantelli page.
- The critical Galton–Watson case is cited and not rewritten. The sample-path argument for Little's law was not opened.
- The Benjamini–Hochberg bound stays on the existing theorem-page entry in `proofs-todo.json`.
- Spot-check of boosting and partial-autocorrelation found sourced definitions. No further prose change.

## Batch T — ranks 353–367

Ranks: 353 positive-predictive-value, 354 prediction-interval, 355 quadratic-discriminant-analysis, 356 randomised-block-design, 357 voronoi-tessellation, 358 hastings-correction, 359 structure-function, 360 convolution, 361 extreme-value-classification, 362 independent-random-variables, 363 jump-chain, 364 markov-random-field, 365 mini-batch, 366 multiple-testing, 367 polynomial-kernel.

Pages fixed: none. Spot-check of positive-predictive-value and polynomial-kernel found sourced definitions and worked numbers.

Conflicts: none.

Tests: `build_wiki.py` wrote 718 articles and 557 question pages. Unit tests passed (67). Offline citation check passed (479 works). `git diff --check` passed. All 15 page checks passed. The same full checks were run again after this last batch.

Unverified:

- New bibliography keys passed the offline schema only: `pishro_nik2014`, `nist_extreme_value`, `lecun_efficient_backprop1998`, `nist_prediction_interval`, `nist_randomized_block`. Live URL checks were not run. The same Pishro-Nik work is cited from several pages and was added once.
- The general extreme-value classification, the Hastings stationarity argument, the positive-density Hammersley–Clifford equivalence, the Benjamini–Hochberg independence proof, and the randomised-block chi-squared laws remain unproved and are logged in `research/todo.md`.

## After rank 367

The next unstarted rank is **368**.
