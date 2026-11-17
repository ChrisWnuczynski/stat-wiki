# Extinction criterion

Rank 414. Depth pass, batch X.

## Material checked

The probability-generating-function recursion, smallest fixed point, critical/supercritical distinction and multiple-ancestor law are derived. Degenerate one-child and no-zero-offspring cases are distinguished. Durrett printed pp. 230–234 and Grinstead–Snell §10.2 were read. Shared statement citation replacements and self-check mapping are staged for root.

Frozen article baseline: 436 words and 0 figures. Source examples, figures, code and results are preserved by extending generator inputs.

## Opened sources and verified locations

- `durrett2019`: (§4.3.4, Thm. 4.3.10–4.3.12, pp. 231–233); (§4.3.4, Thm. 4.3.12, pp. 232–233); (§4.3.4, Thm. 4.3.10–4.3.12 and Ex. 4.3.12, pp. 231–234); (§4.3.4, Thm. 4.3.12). [Full source](https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf).
- `grinstead_snell1997`: (§10.2, branching processes); (§10.2, fixed-point recursion); (§10.2, generating-function argument). [Full source](https://math.dartmouth.edu/~prob/prob/prob.pdf).

## Checks and validation

The independent check is `checks/extinction-criterion.py`. It recomputes the worked example, practice answer and numerical self-check answers, and inspects the generated article for the required results, citations and hidden exercises. Mathematical assumptions and calculation methods are stated above. Final build, offline citation verification, all 15 assigned numerical checks, full unit suite, generated-citation locator audit and diff checks are recorded in `/workspace/statwiki-run/report-x.json` after completion.

Final validation: full generator build passed (718 articles, 626 questions, 88 figures); all 15 batch calculation/article scripts passed; offline bibliography schema passed (648 entries); all 68 unit tests passed. The exact generated-citation locator audit found zero unlocated markers in the 15 pages, hidden answers contain no citations, both preservation baselines pass, and the global whitespace check is clean. Shared source/fixture/renderer changes were validated as uncommitted orchestrator inputs; the batch commit contains only assigned research content, logs and checks.
