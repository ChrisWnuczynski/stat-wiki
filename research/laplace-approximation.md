# Laplace approximation

Rank 477. Depth pass, batch AB.

## Scope and calculations

Read the generated article and all its source excerpts before extending the generator input. Baseline body contains 527 whitespace-delimited words and 0 figures. Preserve definitions, examples, code, mathematical results and figures while correcting the specifically identified errors in pending substitutions.

The independent numerical script `checks/laplace-approximation.py` recomputes the new worked example, its practice answer, selected question answers and numerical claims in the source excerpt. Symbolic or direct algebra checks support derivatives, recurrences, variance identities or decision inequalities where applicable.

## Actually read proper sources

- `schwarz1978`: (§§2–3, pp. 462–464); (§3, pp. 463–464). Full text: https://sites.stat.washington.edu/courses/stat527/s14/readings/ann_stat1978.pdf.
- `tierney_kadane1986`: (§2, p. 83); (§2, p. 83, eq. 2.2); (§2, p. 83; Appendix, p. 86). Full text: https://www.math.mcgill.ca/dstephens/680/Handouts/OldPDFs/TierneyKadane-1986-JASA.pdf.

## Shared proposals

Exact source/metadata/citation substitutions are in the ignored per-slug pending JSON; orchestrator reviews and applies them. These include 1 exact old/new substitutions.

## Proof boundaries

- Full asymptotic Laplace approximation with tail control: The article evaluates the Gaussian surrogate exactly and checks an exact gamma-integral example; a general analytic proof controlling Taylor remainders and contributions outside the dominant peak is still required.

## Validation

The final build passed: 718 articles, 626 question pages, 88 figures. All 15 AB numerical/generated-article checks passed, including this page's independent check. Offline verification passed for 665 bibliography entries. The full 72-test run passed 71 tests, including all 517 completed-page calculation scripts. Its sole failure was a custom heading in another batch's Wold decomposition page; a further audit identified the same alias issue in law of total probability. After both inputs were corrected, the failed citation/structure test passed in a focused rerun. All AB citation locators, hidden answers, self-check links, custom heading aliases and prose/figure preservation audits passed. Global `git diff --check` passed. The orchestrator will run the fresh full build and suite after merging the batches. Exact logs and page-level counts are in `/workspace/statwiki-run/report-ab.json`.
