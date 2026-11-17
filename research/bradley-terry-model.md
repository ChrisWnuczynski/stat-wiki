# bradley-terry-model

Depth pass: batch W, ranks 398–412.

## Sources read

- `caron_doucet2012_bt`: (§1, eq. 1); (§2, log-likelihood formulation); (§3, standard extensions); (§3, home advantage); (§3, models with ties)
- `turner_firth2012_bradley_terry`: (§1, eq. 1); (§1)

Published Turner–Firth JSS paper institutional full PDF §1 eq.1 pp.1–2 and Caron–Doucet full author preprint §§1–3 were read. Raw 2024 NRL fit coefficients lack a reproducible input dataset in this repository; the arithmetic transformations are independently recomputed, and dataset recovery remains a staged todo.

Private Dodge extracts remain outside the repository at `/workspace/statwiki-sources/dodge2008/`.

## Mathematical checks

`checks/bradley-terry-model.py` independently recomputes the worked calculations and inspects the generated article. Final validation results are recorded in the batch report.

## Integration

Shared additions and corrections are staged in ignored `research/pending/bradley-terry-model.json`; that file is not committed.

## Validation

Build passed; all 68 unit tests and all 15 batch calculation scripts passed. The generated article has 12 located inline citations, two hidden-answer self-check questions, and no raw markers or citations in hidden answers. Offline verification passed for all 648 bibliography entries.
