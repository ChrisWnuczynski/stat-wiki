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
