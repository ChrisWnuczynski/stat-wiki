# cost-complexity-pruning

Rank 472; batch AA.

## Sources read

- `loh2014_trees` (§2.1, p. 331): https://pages.stat.wisc.edu/~loh/treeprogs/guide/LohISI14.pdf
- `quan_etal2023_hybrid_trees` (§2.1, eq. 4): https://www.cambridge.org/core/journals/probability-in-the-engineering-and-informational-sciences/article/on-hybrid-treebased-methods-for-shortterm-insurance-claims/6578C721FEB7D7470C0C159234650C23
- `quan_etal2023_hybrid_trees` (§2.1, cost-complexity criterion): https://www.cambridge.org/core/journals/probability-in-the-engineering-and-informational-sciences/article/on-hybrid-treebased-methods-for-shortterm-insurance-claims/6578C721FEB7D7470C0C159234650C23
- `cawley_talbot2010` (§2, pp. 2081–2084): https://www.jmlr.org/papers/volume11/cawley10a/cawley10a.pdf
- `cawley_talbot2010` (§2, model-selection criterion overfitting): https://www.jmlr.org/papers/volume11/cawley10a/cawley10a.pdf

## Calculations

`checks/cost-complexity-pruning.py` passed its independent numerical calculations and generated-article inspection. Final build5 passed (718 articles, 626 questions, 579 answers); all 15 AA checks, 45 exact custom-heading assertions, generated citation/hidden-answer/wording audits, offline verification of 665 bibliography entries and whitespace checks passed.

The full 72-test suite ran in 211.891 seconds with 71 passing, including all 517 completed-page numerical scripts. Its one failure was a root-owned Wold heading alias. Root corrected that and the analogous total-probability alias; the focused citation/structure method then passed in 1.136 seconds. The orchestrator will rerun the full suite after integrating the branches.

## Shared proposals

Exact source-input substitutions, bibliography additions where needed, and proof debts are staged in ignored `research/pending/cost-complexity-pruning.json`. Root integrates shared inputs; only this page’s prose, log and check are committed by this batch.

The branch breakpoint and monotonic leaf-count comparison are proved locally. The general nested optimal-pruning path remains an anchored proof debt.
