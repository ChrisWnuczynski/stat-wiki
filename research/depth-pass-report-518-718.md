# Depth pass, ranks 518–718

All **201 pages** are complete in batches AE–AN. Progress is **Done 718, Left 0, Skipped 0**. The frozen ranking order and scores are unchanged. The pass adds located sources, motivating and worked examples, hidden Your turn answers, two bespoke self-checks per page, and 201 numerical scripts.

Target prose grew from **125,539 to 295,717 words**, using the existing preservation test’s counter. All **38 figures** remain, with every figure target preserved. Word floors for the 201 targets were raised to their final measured counts; no floor from main was lowered.

The integration was rebased onto `5546c8f`, preserving the separate term-page work and both sets of shared-file additions. That upstream work accounts for the site’s increase from the preflight 728 articles to 863. This pass creates no new term pages.

| Batch | Ranks | Pages | Located citations | Self-checks | Figures | Proof gaps |
|:--|:--|--:|--:|--:|--:|--:|
| AE | 518–537 | 20 | 265 | 40 | 5 | 2 |
| AF | 538–557 | 20 | 206 | 40 | 4 | 2 |
| AG | 558–577 | 20 | 220 | 40 | 1 | 3 |
| AH | 578–597 | 20 | 207 | 40 | 8 | 6 |
| AI | 598–617 | 20 | 199 | 40 | 2 | 3 |
| AJ | 618–637 | 20 | 220 | 40 | 10 | 2 |
| AK | 638–657 | 20 | 178 | 40 | 1 | 5 |
| AL | 658–677 | 20 | 205 | 40 | 3 | 2 |
| AM | 678–697 | 20 | 262 | 40 | 2 | 2 |
| AN | 698–718 | 21 | 210 | 42 | 2 | 9 |

## Validation

- Ordinary strict build: **863 articles, 626 question pages, 579 with answers**.
- Full Python suite: **85 tests passed** in 652.069s, including all **718 completed-page scripts** and the **863-script collection**. R was installed; the kyphosis check passes.
- Full **1,701-page Quarto render** passed with Quarto 1.6.40; the Ask widget production build also passed.
- Offline bibliography validation: **780 entries**; this pass adds **43** entries to the integration base.
- Fresh independent build: all **863 article QMD files and the proof ledger reproduced byte for byte**.
- Independent recomputation: **30 random pages**, three per batch, **138 passing claim checks**, including separate leaf-blotch and balanced-design sleep-study refits. Selection seed: `20261117`.
- All **14,443 mathematical expressions** across the targets parse with the site’s bundled KaTeX; zero syntax errors or control/replacement-character issues.
- Final HTML audit: **201 pages, 637 hidden answer boxes and 38 image occurrences**, with no hidden citations, missing images or collapse errors. All 39 target proof links resolve; the focused graph/source-override suite passed **58 tests**.
- Local calculations used R 4.2.2; CI keeps the repository’s R 4.5.0 configuration and pins the additional SVM/GEE dependencies.
- Offline overview-link validation and `git diff --check` passed. All pending bundles were applied and deleted; private Dodge PDFs and extracts remain outside the repository.

## Self-review gate

| Gate | Result |
|:--|:--|
| a — wording | 0 prohibited matches across all 201 article bodies. |
| b — hidden answers | 0 citations in 637 hidden answer boxes. |
| c — self-checks | 201 literal Check yourself headings; 402 bespoke, answered questions from the JSON bank. |
| d — sources | 142 cited work keys reviewed; 0 banned sources, including uncited reference lists. Software references support software behaviour or shipped-data descriptions. Biau–Devroye’s Lectures on the Nearest Neighbor Method is a Springer monograph. |
| e — depth | 2,172 located citations; 5–20 per page; at least 2 independent proper works each. Low-citation warnings: 39 → 0. |
| f — bibliography | 0 duplicate keys, normalized URLs, title/year entries or DOI identities. Editions and chapter aliases are grouped for independence. |
| g — structure | 76 distinct section combinations on the fresh build; largest combination 16/201. Worked-example titles on result pages appear as subheadings under Examples. |
| h — numbers | All 201 scripts pass; 30/30 random pages and 138/138 independent claims checked. Inputs and empirical provenance limitations are itemized below. |
| i — Dodge | All 257 citations map to 97 header-verified printed pages; no PDF index or unnumbered opener is used as a locator. |
| j — checks | Approved citation-contract and word-boundary repairs, plus eight new tests. Numerical, content, figure, question-link and snapshot assertions remain intact. Only target word floors increase. |
| k — protected inputs | The post-generation find-and-replace hook and the per-page reference override were removed. `sources/` and `theorem_depth.py` match main byte for byte, including the CRLF endings of `sources/book/chapters/09-marginal-models.qmd`. Chapter corrections that can only be made there are listed in `research/todo.md` and were not applied. `sources/book/figures/lidar.pdf` matches main. `ranking.json` is unchanged. |

## Approved exceptions

- The find-and-replace layer and the per-page reference override are gone. Legitimate wording lives in the generator inputs.
- The visible-label filter adds a word boundary so genuine STAT course codes fail while the published title SciKit-GStat 1.0 passes; a regression test covers both.
- `sources/book/figures/lidar.pdf` is the copy from main. The metres label is correct and is logged for a separate figure edit.
- The eight Bayesian research notes require a locator after every research citation, at least five citations and two sources, and they exclude the prohibited keys. `tokdar2018_dirichlet` stays in the preservation test, so it is not in that prohibited set. A bare citation that lives only in a frozen chapter or in main's `theorem_depth.py` stays on the built page and is logged in `research/todo.md`.

## Open items

**36 anchored proof gaps across 35 pages** are explicit in [the overrides](proofs-todo-overrides.json). They concern general existence, convergence, asymptotic calibration and extension results beyond the supplied derivations. The generated ledger has 36 added anchors and 26 resolved or replaced generic result entries; previous overrides are unchanged. Three general page flags refer to the same results identified by anchored entries.

**23 provenance or source-access items** remain in [todo.md](todo.md). These include unavailable student-survey observations and prediction-interval reconstruction, exact gene-selection preprocessing/folds and full discovery lists, the burn fit and figure provenance, some empirical table/sample origins, TG5 posterior refitting, and the experimental cluster/order interpretation of warpbreaks. Supplied inputs are distinguished from reproduced empirical results; the full gene-discovery counts and exact historical fits are not independently reconstructed.

Notable corrections include finite-endpoint/extreme-value assumptions, Dirichlet joint versus marginal modes, Student scale versus variance, fitted-parameter count-test calibration, REML precision, lidar physical units, and the wool-versus-factory distinction. Repeated citation locators were removed while preserving the researched scope.

The [machine audit](depth-pass-518-718-audit.json), [before/after metrics](depth-baseline-518-718.json), and [independent mathematics checks](depth-pass-518-718-maths.json) record the evidence. No pages were skipped. No main push, main merge or deployment was performed.
