# nonhomogeneous-poisson-process

Depth pass: batch W, ranks 398–412.

## Sources read

- `pishro_nik2014`: (§11.1.4); (§11.1.4, definition)
- `siegrist_nhpp2022`: (§ “Definition and Basic Properties”); (§ “Arrival Times and Time Change”)

Pishro-Nik published textbook §11.1.4 and Siegrist full textbook “Definition and Basic Properties” plus “Arrival Times and Time Change” were read. Time-change conditions are stated explicitly.

Full generated-page audit found that the copied Durrett§3.7.2p179 citations point to thinning rather than the general integrated-intensity definition. Exact replacements with the read Siegrist and Pishro-Nik definitions are staged for root integration.

Private Dodge extracts remain outside the repository at `/workspace/statwiki-sources/dodge2008/`.

## Mathematical checks

`checks/nonhomogeneous-poisson-process.py` independently recomputes the worked calculations and inspects the generated article. Final validation results are recorded in the batch report.

## Integration

Shared additions and corrections are staged in ignored `research/pending/nonhomogeneous-poisson-process.json`; that file is not committed.

## Validation

Build passed; all 68 unit tests and all 15 batch calculation scripts passed. The generated article has 11 located inline citations, two hidden-answer self-check questions, and no raw markers or citations in hidden answers. Offline verification passed for all 648 bibliography entries.
