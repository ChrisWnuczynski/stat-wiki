# Bayesian result depth pass — batch 2

Baseline: generated pages at commit `d1b91cb`, before this batch. This batch covers 25 Bayesian theorem and proposition articles. Word counts use the substantive-word measure in the retention test.

## Per-article changes

All 25 pages gain a specific lead context, an intuition paragraph, a substantive statistical-use section, and reciprocal prose in Related concepts. Statement notes, worked examples, and cited history are listed where added. “Written” means a new reviewed collapsed proof; “Retained” means the page's existing collapsed proof remains.

| Article | Words before → after | Sections added or expanded | Proof |
|:--|--:|:--|:--|
| Bayes' rule | 834 → 1,076 | Lead, Intuition, Related concepts, Statistical use, History | Written |
| beta–binomial conjugacy | 1,187 → 1,539 | Lead, Statement, Intuition, Related concepts, Statistical use, History | Retained |
| beta–binomial posterior prediction | 768 → 1,141 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |
| Dirichlet–multinomial conjugacy | 2,287 → 2,514 | Lead, Statement, Intuition, Related concepts, Statistical use | Retained |
| Dirichlet moments | 1,060 → 1,379 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |
| interior Dirichlet mode | 1,036 → 1,437 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |
| beta distribution | 485 → 844 | Lead, Statement, Intuition, Related concepts, Statistical use, Examples | Written |
| exponential-family conjugate update | 1,687 → 2,175 | Lead, Statement, Intuition, Related concepts, Statistical use, History | Written |
| log-partition moment identities | 507 → 936 | Lead, Statement, Intuition, Related concepts, Statistical use, Examples | Written |
| normal–normal conjugacy | 1,132 → 1,386 | Lead, Statement, Intuition, Related concepts, Statistical use | Retained |
| normal–inverse-gamma conjugacy | 2,906 → 3,406 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |
| normal–inverse-gamma variance update | 1,837 → 2,172 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |
| full conditionals under independent priors | 1,894 → 2,264 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |
| conditional coefficient posterior | 1,573 → 1,927 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |
| marginal variance posterior | 1,591 → 2,028 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |
| marginal Student posterior | 2,482 → 2,919 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |
| marginal hyperposterior | 500 → 963 | Lead, Statement, Intuition, Related concepts, Statistical use, Examples | Written |
| normal hierarchical shrinkage | 1,693 → 2,079 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |
| predictive-variance decomposition | 895 → 1,141 | Lead, Statement, Intuition, Related concepts, Statistical use | Retained |
| posterior-odds factorisation | 1,202 → 1,698 | Lead, Statement, Intuition, Related concepts, Statistical use, History | Written |
| posterior prediction under the reference prior | 1,578 → 1,996 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |
| study-rate full conditional | 458 → 849 | Lead, Statement, Intuition, Related concepts, Statistical use, Examples | Written |
| sequential coherence | 479 → 876 | Lead, Statement, Intuition, Related concepts, Statistical use, Examples | Written |
| Bayes action for two hypotheses | 965 → 1,307 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |
| direct posterior simulation | 1,830 → 2,187 | Lead, Statement, Intuition, Related concepts, Statistical use | Written |

Total: **32,866 → 42,239 words**. Figure placements: **6 → 6**. Every prior citation key, infobox row, question link, and example heading is retained by the batch test.

## Proofs and pending work

**21 proofs written:** `bayes-rule`, `beta-binomial-posterior-prediction`, `dirichlet-moments`, `interior-dirichlet-mode`, `the-beta-distribution-is-the-two-category-dirichlet`, `generic-exponential-family-conjugate-update`, `log-partition-moment-identities`, `normal-inverse-gamma-conjugacy`, `normal-inverse-gamma-variance-update`, `full-conditionals-under-independent-priors`, `conditional-coefficient-posterior`, `marginal-variance-posterior`, `marginal-student-posterior`, `marginal-hyperposterior`, `normal-hierarchical-shrinkage`, `posterior-odds-factorisation`, `posterior-prediction-under-the-reference-prior`, `study-rate-full-conditional`, `sequential-coherence`, `bayes-action-for-two-hypotheses`, `direct-posterior-simulation`. **4 existing proofs retained:** `beta-binomial-conjugacy`, `dirichlet-multinomial-conjugacy`, `normal-normal-conjugacy`, `predictive-variance-decomposition`. Every article in this batch now has exactly one collapsed Proof box and none remains in `proofs-todo.json`.

The generated proof todo list now has **58** other result articles plus **37** copied distribution-property results from batch 1. The **21** results without verified original and modern historical accounts remain in `theorem-history-todo.json`: `beta-binomial-posterior-prediction`, `dirichlet-multinomial-conjugacy`, `dirichlet-moments`, `interior-dirichlet-mode`, `the-beta-distribution-is-the-two-category-dirichlet`, `log-partition-moment-identities`, `normal-normal-conjugacy`, `normal-inverse-gamma-conjugacy`, `normal-inverse-gamma-variance-update`, `full-conditionals-under-independent-priors`, `conditional-coefficient-posterior`, `marginal-variance-posterior`, `marginal-student-posterior`, `marginal-hyperposterior`, `normal-hierarchical-shrinkage`, `predictive-variance-decomposition`, `posterior-prediction-under-the-reference-prior`, `study-rate-full-conditional`, `sequential-coherence`, `bayes-action-for-two-hypotheses`, `direct-posterior-simulation`.

## Citations, maths, and preservation

Three citation keys newly appear across these 25 pages: `kass_raftery1995`, `robert_casella2004`, `wald1950`. They were already present in `bibliography.json`; no bibliography record was added. The new data contains **162** citation markers across context, statements, proofs, relationships, use, worked examples, and history.

The numerical worked examples newly added to five pages were checked against SciPy or independent arithmetic. Existing worked examples and practice answers remain on the other 20 pages. Relationship claims are generated in both directions from one data structure and use the target page's notation.

**Corrective wording:** The source statement for `interior-dirichlet-mode` called a coordinate of the *joint* Dirichlet mode the mode of a marginal component. The generator now labels the joint MAP coordinate correctly and explains the boundary case; its original question and answer remain. The existing Bayes history sentence was expanded to identify the repeated-trials problem addressed by the 1763 essay. No prior figure, citation, infobox value, definition, example, or practice question was removed.

## Verification

- Generator completed: 718 concept articles and 557 question pages.
- `python -m unittest discover -q`: 62 tests passed, including retention, proof/todo, lead, and generated-link checks. The existing site-wide warning still reports 17 articles with fewer than three inline citations.
- `python check_overview_links.py`: 115 internal targets valid.
- `python verify_citations.py --offline`: all 380 bibliography entries passed schema and provenance validation. Live verification remains unavailable because the network tunnel returns HTTP 403 for the external reference services.
- Five new numeric examples agree with SciPy or independent arithmetic.
- `git diff --check` passed.
