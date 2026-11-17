# one-hot-encoding

Depth pass: batch W, ranks 398–412.

## Sources read

- `zhang_d2l2023`: (§4.1.1); (§4.1.2.2); (§§4.1.1.2–4.1.2.2)
- `goodfellow_bengio_courville2016`: (§6.2.2.3, pp. 180–183); (§6.2.2.3, pp. 182–183); (§§6.2.2.2–6.2.2.3, pp. 176–183)

The published D2L textbook chapter was read at https://d2l.ai/chapter_linear-classification/softmax-regression.html. Actual subsection numbers:4.1.1 one-hot coding,4.1.1.2 softmax,4.1.2.1 likelihood,4.1.2.2 gradient. Goodfellow et al. published book author HTML §§6.2.2.2–6.2.2.3 was also read.

Private Dodge extracts remain outside the repository at `/workspace/statwiki-sources/dodge2008/`.

## Mathematical checks

`checks/one-hot-encoding.py` independently recomputes the worked calculations and inspects the generated article. Final validation results are recorded in the batch report.

## Integration

Shared additions and corrections are staged in ignored `research/pending/one-hot-encoding.json`; that file is not committed.

## Validation

Build passed; all 68 unit tests and all 15 batch calculation scripts passed. The generated article has 8 located inline citations, two hidden-answer self-check questions, and no raw markers or citations in hidden answers. Offline verification passed for all 648 bibliography entries.
