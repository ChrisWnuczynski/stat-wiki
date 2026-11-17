# label-switching

Depth pass: batch W, ranks 398–412.

## Sources read

- `stephens2000`: (§§1–2, pp. 795–797); (§§2–3, pp. 796–800); (§§3–4, pp. 798–803); (§2.2, pp. 796–798)
- `green2019_finite_mixtures`: (Ch. 1, §1.3.1, pp. 13–14)

Stephens2000 full published paper §§1–4 pp.795–803 and Green finite-mixtures chapter §1.3.1 pp.13–14 were read. Both address permutation nonidentifiability and meaningful posterior summaries.

The copied generic Fraley–Raftery mixture-fitting citation is staged for removal from the identification paragraph, where the directly read Green and Stephens works already supply the relevant support.

Private Dodge extracts remain outside the repository at `/workspace/statwiki-sources/dodge2008/`.

## Mathematical checks

`checks/label-switching.py` independently recomputes the worked calculations and inspects the generated article. Final validation results are recorded in the batch report.

## Integration

Shared additions and corrections are staged in ignored `research/pending/label-switching.json`; that file is not committed.

## Validation

Build passed; all 68 unit tests and all 15 batch calculation scripts passed. The generated article has 9 located inline citations, two hidden-answer self-check questions, and no raw markers or citations in hidden answers. Offline verification passed for all 648 bibliography entries.
