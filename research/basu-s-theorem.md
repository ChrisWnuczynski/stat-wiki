# Basu s theorem

Rank 425. Depth pass, batch X.

## Material checked

DasGupta 2007 pp. 945–947 and full Siegrist §7.6 were read. The bounded-completeness conditional-event proof is explicit. DasGupta textbook §18.4 pp. 511–512 Thm. 18.8–18.9 supplies full exponential-family completeness and Basu application; the later general-Basu statement omits completeness and is not used. A gamma-total/uniform-ratio Jacobian calculation independently proves the worked example.

Frozen article baseline: 398 words and 0 figures. Source examples, figures, code and results are preserved by extending generator inputs.

## Opened sources and verified locations

- `dasgupta2007_basu`: (§1, pp. 945–946); (§1, p. 945); (§2, pp. 946–947, conditional-distribution formulation). [Full source](https://www.stat.purdue.edu/~dasgupta/basuinfdiv.pdf).
- `siegrist2022_sufficient_complete`: (§7.6, Ancillary Statistics and Basu's theorem); (§7.6, Complete Statistics); (§7.6, proof of Basu's theorem); (§7.6, sufficiency, completeness and ancillary statistics). [Full source](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/07:_Point_Estimation/7.06:_Sufficient_Complete_and_Ancillary_Statistics).
- `dasgupta2011_exponential_family`: (§18.4, Thm. 18.8–18.9, pp. 511–512). [Full source](https://www.stat.purdue.edu/~dasgupta/expfamily.pdf).

## Checks and validation

The independent check is `checks/basu-s-theorem.py`. It recomputes the worked example, practice answer and numerical self-check answers, and inspects the generated article for the required results, citations and hidden exercises. Mathematical assumptions and calculation methods are stated above. Final build, offline citation verification, all 15 assigned numerical checks, full unit suite, generated-citation locator audit and diff checks are recorded in `/workspace/statwiki-run/report-x.json` after completion.

Final validation: full generator build passed (718 articles, 626 questions, 88 figures); all 15 batch calculation/article scripts passed; offline bibliography schema passed (648 entries); all 68 unit tests passed. The exact generated-citation locator audit found zero unlocated markers in the 15 pages, hidden answers contain no citations, both preservation baselines pass, and the global whitespace check is clean. Shared source/fixture/renderer changes were validated as uncommitted orchestrator inputs; the batch commit contains only assigned research content, logs and checks.
