# Decision stump

Rank 473. Depth pass, batch AB.

## Scope and calculations

Read the generated article and all its source excerpts before extending the generator input. Baseline body contains 508 whitespace-delimited words and 0 figures. Preserve definitions, examples, code, mathematical results and figures while correcting the specifically identified errors in pending substitutions.

The independent numerical script `checks/decision-stump.py` recomputes the new worked example, its practice answer, selected question answers and numerical claims in the source excerpt. Symbolic or direct algebra checks support derivatives, recurrences, variance identities or decision inequalities where applicable.

## Actually read proper sources

- `lindholm2022_ml`: (Ch. 7, p. 175); (§2.3; Ch. 7, p. 175); (§2.3, decision-tree construction). Full text: https://smlbook.org/book/sml-book-draft-latest.pdf.
- `schapire2013_explaining_adaboost`: (§2, p. 3); (§1, Fig. 1, pp. 1–2); (§1, weight update); (§1, Fig. 1). Full text: https://rob.schapire.net/papers/explaining-adaboost.pdf.

The author landing page recommends the published 2022 Cambridge citation. Its linked first-edition manuscript is updated 4 March 2026; locators are the printed pages in that actually read manuscript, not an inferred new publication year. No claim about an unpublished second edition is used.

## Shared proposals

Exact source/metadata/citation substitutions are in the ignored per-slug pending JSON; orchestrator reviews and applies them. These include 2 exact old/new substitutions.

## Validation

The final build passed: 718 articles, 626 question pages, 88 figures. All 15 AB numerical/generated-article checks passed, including this page's independent check. Offline verification passed for 665 bibliography entries. The full 72-test run passed 71 tests, including all 517 completed-page calculation scripts. Its sole failure was a custom heading in another batch's Wold decomposition page; a further audit identified the same alias issue in law of total probability. After both inputs were corrected, the failed citation/structure test passed in a focused rerun. All AB citation locators, hidden answers, self-check links, custom heading aliases and prose/figure preservation audits passed. Global `git diff --check` passed. The orchestrator will run the fresh full build and suite after merging the batches. Exact logs and page-level counts are in `/workspace/statwiki-run/report-ab.json`.
