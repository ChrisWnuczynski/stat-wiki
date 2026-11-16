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
