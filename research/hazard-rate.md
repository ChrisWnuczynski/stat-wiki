# hazard-rate

Depth pass: batch W, ranks 398–412.

## Sources read

- `siegrist_weibull2022`: (§ “The Basic Weibull Distribution”, failure rate); (§ “The General Weibull Distribution”, distribution functions); (§ “The Basic Weibull Distribution”, quantiles and moments)
- `pishro_nik2014`: (§11.1.4)
- `siegrist_nhpp2022`: (§ “Arrival Times and Time Change”)

Siegrist full textbook Weibull sections (failure rate, scale transformation, quantiles, moments) and NHPP first-arrival section were read. Pishro-Nik §11.1.4 supplies the independent-increment first-arrival calculation.

Private Dodge extracts remain outside the repository at `/workspace/statwiki-sources/dodge2008/`.

## Mathematical checks

`checks/hazard-rate.py` independently recomputes the worked calculations and inspects the generated article. Final validation results are recorded in the batch report.

## Integration

Shared additions and corrections are staged in ignored `research/pending/hazard-rate.json`; that file is not committed.

## Validation

Build passed; all 68 unit tests and all 15 batch calculation scripts passed. The generated article has 7 located inline citations, two hidden-answer self-check questions, and no raw markers or citations in hidden answers. Offline verification passed for all 648 bibliography entries.
