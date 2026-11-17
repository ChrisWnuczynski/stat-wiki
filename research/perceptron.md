# perceptron

Depth pass: batch W, ranks 398–412.

## Sources read

- `rosenblatt1958`: (pp. 386–389); (pp. 387–389)
- `goodfellow_bengio_courville2016`: (§6.1, pp. 166–170); (§§6.1–6.2, pp. 166–183)
- `shalev_bendavid2014`: (§9.1.2, pp. 92–93); (§9.1.2, Thm. 9.1, pp. 92–93)

The modern algorithm and complete finite-mistake proof were read in Shalev-Shwartz and Ben-David, published CUP book, §9.1.2 pp.92–93, institutional copy https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf. Rosenblatt historical discussion and Goodfellow XOR section were read separately.

Private Dodge extracts remain outside the repository at `/workspace/statwiki-sources/dodge2008/`.

## Mathematical checks

`checks/perceptron.py` independently recomputes the worked calculations and inspects the generated article. Final validation results are recorded in the batch report.

## Integration

Shared additions and corrections are staged in ignored `research/pending/perceptron.json`; that file is not committed.

## Validation

Build passed; all 68 unit tests and all 15 batch calculation scripts passed. The generated article has 10 located inline citations, two hidden-answer self-check questions, and no raw markers or citations in hidden answers. Offline verification passed for all 648 bibliography entries.
