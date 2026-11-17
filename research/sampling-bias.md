# Sampling bias

Rank 419. Depth pass, batch X.

## Material checked

Finite-population realised error is separated from estimator bias, using the exact Meng inclusion–outcome covariance identity. Weighted and unequal-inclusion examples avoid equating unequal inclusion with universal bias. Dodge Bias printed p. 41 and Sampling pp. 468–470 were read; Meng §§2.1–2.3 supplies the mathematical identity. A false source implication concerning independence/equal inclusion is staged for root.

Frozen article baseline: 201 words and 0 figures. Source examples, figures, code and results are preserved by extending generator inputs.

## Opened sources and verified locations

- `dodge2008`: (pp. 468–470, Sampling); (p. 41, Bias). [Full source](Private authorized copy: Encyclopedia of Statistics, printed pages recorded below.).
- `meng2018_big_data`: (§2, pp. 689–692); (§2.2, eqs. 2.2–2.4, pp. 690–691); (§2.2–2.3, pp. 690–694); (§2.3, weighting and data quality); (§2.1–2.2, pp. 688–691). [Full source](https://statistics.fas.harvard.edu/sites/g/files/omnuum10116/files/statistics-2/files/statistical_paradises_and_paradoxes.pdf).

## Checks and validation

The independent check is `checks/sampling-bias.py`. It recomputes the worked example, practice answer and numerical self-check answers, and inspects the generated article for the required results, citations and hidden exercises. Mathematical assumptions and calculation methods are stated above. Final build, offline citation verification, all 15 assigned numerical checks, full unit suite, generated-citation locator audit and diff checks are recorded in `/workspace/statwiki-run/report-x.json` after completion.

Final validation: full generator build passed (718 articles, 626 questions, 88 figures); all 15 batch calculation/article scripts passed; offline bibliography schema passed (648 entries); all 68 unit tests passed. The exact generated-citation locator audit found zero unlocated markers in the 15 pages, hidden answers contain no citations, both preservation baselines pass, and the global whitespace check is clean. Shared source/fixture/renderer changes were validated as uncommitted orchestrator inputs; the batch commit contains only assigned research content, logs and checks.
