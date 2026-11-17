# bagging

Depth pass: batch W, ranks 398–412.

## Sources read

- `breiman1996_bagging`: (§1); (§4)
- `dietterich2000_ensembles`: (§2.2, Bagging); (§1, pp. 1–3)
- `breiman2001_rf`: (§3.1, p. 11)

Breiman author bagging manuscript was read in §§1 and4 and the named subsection “Bagging Class Probability Estimates”; journal page numbers were not inferred from that manuscript. Random Forests published paper was read at https://www.ams.jhu.edu/~priebe/COURSES/FALL2003/550.730/RF/breiman-rf.pdf, §§1.1,3.1,4 (pp.5–6,11), correcting preprint numbering. Dietterich published conference paper was read at the author-hosted full PDF, §§1–2.3.

Freund–Schapire1997 full published paper was read at https://www.cs.cmu.edu/~bhiksha/courses/mlsp.fall2010/class7/freund.boosting.pdf, §4.1 pp.125–126, including adaptive reweighting and Fig.2. The copied boosting lead locator is supported.

Private Dodge extracts remain outside the repository at `/workspace/statwiki-sources/dodge2008/`.

## Mathematical checks

`checks/bagging.py` independently recomputes the worked calculations and inspects the generated article. Final validation results are recorded in the batch report.

## Integration

Shared additions and corrections are staged in ignored `research/pending/bagging.json`; that file is not committed.

## Validation

Build passed; all 68 unit tests and all 15 batch calculation scripts passed. The generated article has 15 located inline citations, two hidden-answer self-check questions, and no raw markers or citations in hidden answers. Offline verification passed for all 648 bibliography entries.
