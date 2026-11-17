# Blocking probability

Rank 426. Depth pass, batch X.

## Material checked

The stationary long-run probability statement explicitly assumes ergodicity; stationarity alone permits random limiting time fractions. The original Wolff article was opened, including its nonanticipation condition and pre-arrival convention on printed pp. 224–227. Durrett §5.5 supplies stationary detailed balance. Finite birth–death weights are derived directly through uniformisation and checked by matrix multiplication; PASTA is identified as the additional arrival-sampling theorem. Its general proof is staged as a proof-todo anchor.

Frozen article baseline: 471 words and 0 figures. Source examples, figures, code and results are preserved by extending generator inputs.

## Opened sources and verified locations

- `wolff1982_pasta`: (§1, pp. 224–225); (§1, Thm. 1, pp. 224–225); (§1); (§§1–2, pp. 224–227). [Full source](https://www.math.purdue.edu/~peterson/Teaching/532/PASTA.pdf).
- `durrett2019`: (§5.5, detailed balance and stationary measures); (§5.5, detailed balance); (§5.5, stationary balance equations). [Full source](https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf).

## Checks and validation

The independent check is `checks/blocking-probability.py`. It recomputes the worked example, practice answer and numerical self-check answers, and inspects the generated article for the required results, citations and hidden exercises. Mathematical assumptions and calculation methods are stated above. Final build, offline citation verification, all 15 assigned numerical checks, full unit suite, generated-citation locator audit and diff checks are recorded in `/workspace/statwiki-run/report-x.json` after completion.

Final validation: full generator build passed (718 articles, 626 questions, 88 figures); all 15 batch calculation/article scripts passed; offline bibliography schema passed (648 entries); all 68 unit tests passed. The exact generated-citation locator audit found zero unlocated markers in the 15 pages, hidden answers contain no citations, both preservation baselines pass, and the global whitespace check is clean. Shared source/fixture/renderer changes were validated as uncommitted orchestrator inputs; the batch commit contains only assigned research content, logs and checks.
