# Sylvester s criterion

Rank 420. Depth pass, batch X.

## Material checked

The positive-definite leading-minor criterion is proved by a Schur-complement induction. The semidefinite analogue needs all principal minors rather than only leading ones; diag(0,-1) checks the failure. Treil §7.4.1 Thm. 7.4.2 and Boyd §§A.5.2, A.5.5 were read. The incorrect 2x2 semidefinite remark in the Treil text was not repeated.

Frozen article baseline: 195 words and 0 figures. Source examples, figures, code and results are preserved by extending generator inputs.

## Opened sources and verified locations

- `treil2026_linear_algebra`: (§7.4.1, Thm. 7.4.2); (§7.1.2 and §7.4.1); (§7.4.1, proof of Thm. 7.4.2). [Full source](https://www.math.brown.edu/streil/papers/LADW/HTML_2026_08-31/LADW_2026_08-31.html).
- `boyd_vandenberghe2004`: (§A.5.2, p. 647); (§A.5.5, pp. 650–651); (§A.5.2, definiteness and matrix inequalities). [Full source](https://www.seas.ucla.edu/~vandenbe/cvxbook/bv_cvxbook.pdf).

## Checks and validation

The independent check is `checks/sylvester-s-criterion.py`. It recomputes the worked example, practice answer and numerical self-check answers, and inspects the generated article for the required results, citations and hidden exercises. Mathematical assumptions and calculation methods are stated above. Final build, offline citation verification, all 15 assigned numerical checks, full unit suite, generated-citation locator audit and diff checks are recorded in `/workspace/statwiki-run/report-x.json` after completion.

Final validation: full generator build passed (718 articles, 626 questions, 88 figures); all 15 batch calculation/article scripts passed; offline bibliography schema passed (648 entries); all 68 unit tests passed. The exact generated-citation locator audit found zero unlocated markers in the 15 pages, hidden answers contain no citations, both preservation baselines pass, and the global whitespace check is clean. Shared source/fixture/renderer changes were validated as uncommitted orchestrator inputs; the batch commit contains only assigned research content, logs and checks.
