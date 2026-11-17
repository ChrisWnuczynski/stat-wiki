# Distance to a hyperplane

Rank 413. Depth pass, batch X.

## Material checked

Projection, uniqueness by Pythagoras, signed-distance orientation, scale invariance and support-vector margin are derived. Treil §§5.1.1 and 5.3 were read in the current author-hosted edition, including its proof; Boyd §2.2.1 fixes the affine hyperplane convention; Cortes–Vapnik §2.1 supplies the margin formulation.

Frozen article baseline: 484 words and 0 figures. Source examples, figures, code and results are preserved by extending generator inputs.

## Opened sources and verified locations

- `treil2026_linear_algebra`: (§5.3, Thm. 5.3.2); (§5.3, Def. 5.3.1 and Props. 5.3.3); (§5.1.1, norm and inner product). [Full source](https://www.math.brown.edu/streil/papers/LADW/HTML_2026_08-31/LADW_2026_08-31.html).
- `boyd_vandenberghe2004`: (§2.2.1, pp. 27–28). [Full source](https://www.seas.ucla.edu/~vandenbe/cvxbook/bv_cvxbook.pdf).
- `cortes_vapnik1995`: (§2.1, pp. 277–279). [Full source](https://homepages.math.uic.edu/~lreyzin/papers/cortes95.pdf).

## Checks and validation

The independent check is `checks/distance-to-a-hyperplane.py`. It recomputes the worked example, practice answer and numerical self-check answers, and inspects the generated article for the required results, citations and hidden exercises. Mathematical assumptions and calculation methods are stated above. Final build, offline citation verification, all 15 assigned numerical checks, full unit suite, generated-citation locator audit and diff checks are recorded in `/workspace/statwiki-run/report-x.json` after completion.

Final validation: full generator build passed (718 articles, 626 questions, 88 figures); all 15 batch calculation/article scripts passed; offline bibliography schema passed (648 entries); all 68 unit tests passed. The exact generated-citation locator audit found zero unlocated markers in the 15 pages, hidden answers contain no citations, both preservation baselines pass, and the global whitespace check is clean. Shared source/fixture/renderer changes were validated as uncommitted orchestrator inputs; the batch commit contains only assigned research content, logs and checks.
