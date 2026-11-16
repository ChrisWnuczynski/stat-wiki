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
