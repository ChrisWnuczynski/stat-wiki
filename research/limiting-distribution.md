# Limiting distribution

Rank 418. Depth pass, batch X.

## Material checked

Finite convergence uses an explicit common-mass contraction proof and Cesaro existence argument. Periodic distributions are separated from time averages; positive recurrence is distinguished from null recurrence. Durrett §§5.5–5.6 and Grinstead–Snell §11.4 were read. A source equal-drift error and periodic-start qualification are staged for root.

Frozen article baseline: 1170 words and 4 figures. Source examples, figures, code and results are preserved by extending generator inputs.

## Opened sources and verified locations

- `grinstead_snell1997`: (§11.4, fundamental limit theorem); (§11.4, regular transition matrices); (§11.4, finite-chain convergence proof). [Full source](https://math.dartmouth.edu/~prob/prob/prob.pdf).
- `durrett2019`: (§5.6, Thm. 5.6.6, pp. 313–314); (§5.6, Ex. 5.6.2, p. 311); (§5.6, Ex. 5.6.3–5.6.4); (§5.6, Thm. 5.6.1, pp. 310–311); (§5.5, stationary measures and positive recurrence). [Full source](https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf).

## Checks and validation

The independent check is `checks/limiting-distribution.py`. It recomputes the worked example, practice answer and numerical self-check answers, and inspects the generated article for the required results, citations and hidden exercises. Mathematical assumptions and calculation methods are stated above. Final build, offline citation verification, all 15 assigned numerical checks, full unit suite, generated-citation locator audit and diff checks are recorded in `/workspace/statwiki-run/report-x.json` after completion.

Final validation: full generator build passed (718 articles, 626 questions, 88 figures); all 15 batch calculation/article scripts passed; offline bibliography schema passed (648 entries); all 68 unit tests passed. The exact generated-citation locator audit found zero unlocated markers in the 15 pages, hidden answers contain no citations, both preservation baselines pass, and the global whitespace check is clean. Shared source/fixture/renderer changes were validated as uncommitted orchestrator inputs; the batch commit contains only assigned research content, logs and checks.
