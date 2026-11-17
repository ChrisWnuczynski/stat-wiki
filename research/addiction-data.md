# Addiction data

Rank 421. Depth pass, batch X.

## Material checked

CRAN catdata help verifies dataset dimensions and category coding only. D2L §4.1 and Boyd §3.1.5 supply multinomial softmax likelihood, normalization and odds interpretation. Public catdata addiction.rda was obtained from the CRAN GitHub mirror outside the repo and fit independently by SciPy BFGS on all 682 complete cases. The check embeds only 211 public aggregate-frequency rows, independently recomputes the eight coefficients, observed-information standard errors and z ratios, and verifies probabilities/odds. No private reference text is embedded.

Frozen article baseline: 695 words and 0 figures. Source examples, figures, code and results are preserved by extending generator inputs.

## Opened sources and verified locations

- `zhang_d2l2023`: (§4.1.1, classification and one-hot responses); (§4.1.1.1–4.1.1.2, eqs. 4.1.2–4.1.3); (§4.1.1.2, softmax probabilities); (§4.1.2.1, log likelihood); (§4.1.1.2, normalisation). [Full source](https://d2l.ai/chapter_linear-classification/softmax-regression.html).
- `r_catdata_addiction2026`: (Description and Format). [Full source](https://search.r-project.org/CRAN/refmans/catdata/html/addiction.html).
- `boyd_vandenberghe2004`: (§3.1.5, pp. 72–74, log-sum-exp). [Full source](https://www.seas.ucla.edu/~vandenbe/cvxbook/bv_cvxbook.pdf).

## Checks and validation

The independent check is `checks/addiction-data.py`. It recomputes the worked example, practice answer and numerical self-check answers, and inspects the generated article for the required results, citations and hidden exercises. Mathematical assumptions and calculation methods are stated above. Final build, offline citation verification, all 15 assigned numerical checks, full unit suite, generated-citation locator audit and diff checks are recorded in `/workspace/statwiki-run/report-x.json` after completion.

Metadata verification: [catdata DESCRIPTION](https://raw.githubusercontent.com/cran/catdata/master/DESCRIPTION) gives version1.2.5 and Date/Publication2025-12-04, with authors GuntherSchauberger and GerhardTutz. The stable pending key remains `r_catdata_addiction2026`, while its publication-year value is corrected to2025.

Final validation: full generator build passed (718 articles, 626 questions, 88 figures); all 15 batch calculation/article scripts passed; offline bibliography schema passed (648 entries); all 68 unit tests passed. The exact generated-citation locator audit found zero unlocated markers in the 15 pages, hidden answers contain no citations, both preservation baselines pass, and the global whitespace check is clean. Shared source/fixture/renderer changes were validated as uncommitted orchestrator inputs; the batch commit contains only assigned research content, logs and checks.
