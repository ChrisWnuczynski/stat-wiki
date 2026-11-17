# hypergeometric-distribution

Depth pass: batch W, ranks 398–412.

## Sources read

- `dodge2008`: (p. 247); (pp. 247–248); (p. 248)
- `siegrist_hypergeometric2022`: (§ “Basic Theory, The Probability Density Function”); (§ “Basic Theory, Moments”); (§ “Convergence of the Hypergeometric Distribution to the Binomial”)

Dodge printed pp.247–248 and Siegrist full textbook section were read. The exact binomial-limit subsection is “Convergence of the Hypergeometric Distribution to the Binomial”. Agresti1992 full author-hosted paper §§1.3–2.1, printed pp.133–135, was read for the Fisher conditional hypergeometric calculation.

Siegrist Binomial Distribution §11.2, subsection “Sampling and the Hypergeometric Distribution”, was opened for the copied related-distribution limit: fixed sample size, marked fraction converging to p, and population size tending to infinity.

Private Dodge extracts remain outside the repository at `/workspace/statwiki-sources/dodge2008/`.

## Mathematical checks

`checks/hypergeometric-distribution.py` independently recomputes the worked calculations and inspects the generated article. Final validation results are recorded in the batch report.

## Integration

Shared additions and corrections are staged in ignored `research/pending/hypergeometric-distribution.json`; that file is not committed.

## Validation

Build passed; all 68 unit tests and all 15 batch calculation scripts passed. The generated article has 19 located inline citations, two hidden-answer self-check questions, and no raw markers or citations in hidden answers. Offline verification passed for all 648 bibliography entries.
