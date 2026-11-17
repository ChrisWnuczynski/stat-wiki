# Jackknife

Rank 476. Depth pass, batch AB.

## Scope and calculations

Read the generated article and all its source excerpts before extending the generator input. Baseline body contains 612 whitespace-delimited words and 0 figures. Preserve definitions, examples, code, mathematical results and figures while correcting the specifically identified errors in pending substitutions.

The independent numerical script `checks/jackknife.py` recomputes the new worked example, its practice answer, selected question answers and numerical claims in the source excerpt. Symbolic or direct algebra checks support derivatives, recurrences, variance identities or decision inequalities where applicable.

## Actually read proper sources

- `efron1979`: (§5, pp. 12–14); (§5, pp. 13–14); (§1, p. 1; §5, pp. 12–14). Full text: https://ledaliang.github.io/journalclub/_static/efron1979/Efron1979.pdf.
- `dodge2008`: (pp. 271–272); (pp. 271–272, grouped jackknife). Full text: private printed271–272, checked index.tsv and pdf-0273/pdf-0274 text.

## Shared proposals

Exact source/metadata/citation substitutions are in the ignored per-slug pending JSON; orchestrator reviews and applies them. These include 4 exact old/new substitutions.

## Validation

The final build passed: 718 articles, 626 question pages, 88 figures. All 15 AB numerical/generated-article checks passed, including this page's independent check. Offline verification passed for 665 bibliography entries. The full 72-test run passed 71 tests, including all 517 completed-page calculation scripts. Its sole failure was a custom heading in another batch's Wold decomposition page; a further audit identified the same alias issue in law of total probability. After both inputs were corrected, the failed citation/structure test passed in a focused rerun. All AB citation locators, hidden answers, self-check links, custom heading aliases and prose/figure preservation audits passed. Global `git diff --check` passed. The orchestrator will run the fresh full build and suite after merging the batches. Exact logs and page-level counts are in `/workspace/statwiki-run/report-ab.json`.
