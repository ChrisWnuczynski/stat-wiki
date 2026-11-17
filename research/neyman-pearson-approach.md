# neyman-pearson-approach

Depth pass: batch W, ranks 398–412.

## Sources read

- `dodge2008`: (p. 250)
- `siegrist2022_testing`: (§9.1, Basic Theory)
- `siegrist2022_lrt`: (§9.5, The Neyman-Pearson Lemma); (§9.5, Composite Hypotheses); (§9.5, Normal Distribution)

Siegrist proper textbook Introduction to Hypothesis Testing §9.1 and Likelihood Ratio Tests §9.5 were read. Dodge printed250 was read for historical orientation. The likelihood-ratio optimality proof is supplied explicitly.

Private Dodge extracts remain outside the repository at `/workspace/statwiki-sources/dodge2008/`.

## Mathematical checks

`checks/neyman-pearson-approach.py` independently recomputes the worked calculations and inspects the generated article. Final validation results are recorded in the batch report.

## Integration

Shared additions and corrections are staged in ignored `research/pending/neyman-pearson-approach.json`; that file is not committed.

## Validation

Build passed; all 68 unit tests and all 15 batch calculation scripts passed. The generated article has 9 located inline citations, two hidden-answer self-check questions, and no raw markers or citations in hidden answers. Offline verification passed for all 648 bibliography entries.


## Source-scope correction

Dodge250 is confined to specifying a hypothesis test and its significance level. The fixed-significance greatest-power criterion uses actually read Siegrist §9.1 Basic Theory > Power; the existing Neyman–Pearson proof source remains §9.5. All mathematical and numerical content is unchanged.
