# regression-effect

Depth pass: batch W, ranks 398–412.

## Sources read

- `galton1886`: (pp. 246–247); (pp. 247–250)
- `dodge2008`: (p. 451); (pp. 491–492)

Dodge printed451 (history) and491–492 (least-squares regression) were read. Galton1886 original public-domain paper pp.246–250 was read. The modern standardized linear-prediction result is proved by minimizing the quadratic risk.

NIST/SEMATECH Handbook151 §4.1.2 was opened for the response/predictor terminology in the introduction; it is statistical textbook content, separate from software documentation.

Private Dodge extracts remain outside the repository at `/workspace/statwiki-sources/dodge2008/`.

## Mathematical checks

`checks/regression-effect.py` independently recomputes the worked calculations and inspects the generated article. Final validation results are recorded in the batch report.

## Integration

Shared additions and corrections are staged in ignored `research/pending/regression-effect.json`; that file is not committed.

## Validation

Build passed; all 68 unit tests and all 15 batch calculation scripts passed. The generated article has 10 located inline citations, two hidden-answer self-check questions, and no raw markers or citations in hidden answers. Offline verification passed for all 648 bibliography entries.


## Source-scope correction

The population covariance/correlation calculation and normal conditional mean use actually read Grinstead–Snell (1997), §6.3 Exercises17–21 pp.281–282 and Exercise24 p.283, https://math.dartmouth.edu/~prob/prob/prob.pdf. The selection/repeated-measure motivation additionally uses actually read Barnett, van der Pols and Dobson (2005), pp.215–216, doi:10.1093/ije/dyh299; full six-page published paper read through its institutional copy. Dodge451 and Galton retain historical scope. All mathematics, proof steps, figures, worked numbers and numerical checks are unchanged.
