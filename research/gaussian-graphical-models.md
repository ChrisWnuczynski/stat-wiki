# gaussian-graphical-models

Depth pass: batch W, ranks 398–412.

## Sources read

- `bien_tibshirani2011_covariance`: (§1, pp. 807–808); (§1, p. 808)
- `friedman_glasso2008`: (§1, p. 432); (§§1–2, pp. 432–434)

Friedman et al. proper paper author full preprint §§1–2 and Bien–Tibshirani peer-reviewed Biometrika article §1 (PMC full text) were read; the course-note citation was replaced in shared-source pending changes.

Private Dodge extracts remain outside the repository at `/workspace/statwiki-sources/dodge2008/`.

## Mathematical checks

`checks/gaussian-graphical-models.py` independently recomputes the worked calculations and inspects the generated article. Final validation results are recorded in the batch report.

## Integration

Shared additions and corrections are staged in ignored `research/pending/gaussian-graphical-models.json`; that file is not committed.

## Validation

Build passed; all 68 unit tests and all 15 batch calculation scripts passed. The generated article has 6 located inline citations, two hidden-answer self-check questions, and no raw markers or citations in hidden answers. Offline verification passed for all 648 bibliography entries.
