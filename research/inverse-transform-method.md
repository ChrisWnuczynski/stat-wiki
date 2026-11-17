# Inverse transform method

Rank 415. Depth pass, batch X.

## Material checked

Generalised inverse handles continuous and discrete CDFs, endpoints and discontinuities. Durrett §1.2 Thm. 1.2.2 and Grinstead–Snell §§1.1 and 2.1 were read. The five closed-form inverse families are all preserved; the check verifies each quantile by substitution, with branch-restricted numerical verification for Weibull and Cauchy. Shared inverse-construction citations are staged.

Frozen article baseline: 630 words and 2 figures. Source examples, figures, code and results are preserved by extending generator inputs.

## Opened sources and verified locations

- `durrett2019`: (§1.2, Thm. 1.2.2, p. 11); (§1.2, Thm. 1.2.2, pp. 10–12); (§1.2, proof of Thm. 1.2.2, p. 11); (§1.2, inverse distribution construction). [Full source](https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf).
- `grinstead_snell1997`: (§1.1, simulation of discrete probabilities); (§2.1, simulation of continuous probabilities). [Full source](https://math.dartmouth.edu/~prob/prob/prob.pdf).

## Checks and validation

The independent check is `checks/inverse-transform-method.py`. It recomputes the worked example, practice answer and numerical self-check answers, and inspects the generated article for the required results, citations and hidden exercises. Mathematical assumptions and calculation methods are stated above. Final build, offline citation verification, all 15 assigned numerical checks, full unit suite, generated-citation locator audit and diff checks are recorded in `/workspace/statwiki-run/report-x.json` after completion.

Final validation: full generator build passed (718 articles, 626 questions, 88 figures); all 15 batch calculation/article scripts passed; offline bibliography schema passed (648 entries); all 68 unit tests passed. The exact generated-citation locator audit found zero unlocated markers in the 15 pages, hidden answers contain no citations, both preservation baselines pass, and the global whitespace check is clean. Shared source/fixture/renderer changes were validated as uncommitted orchestrator inputs; the batch commit contains only assigned research content, logs and checks.
