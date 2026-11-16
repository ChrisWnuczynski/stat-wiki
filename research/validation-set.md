# Validation set — rank 90

Type: method/concept. Baseline: 272 words, no figures; page already includes the train/validation/test division and the ten-tuning-value sketch, both preserved. Compared with rank 83 Precision, this eighth page needs a worked example, proof and enough explanatory depth to avoid thinning.

## Sources opened

- **Checked:** James, Witten, Hastie and Tibshirani (2013), author-hosted first edition *An Introduction to Statistical Learning*, §5.1.1, printed pp. 176–178. Read the holdout definition, 392 Auto cases split 196/196, split-to-split variation, and smaller-training-set drawback.
- **Checked:** Cawley and Talbot (2010), JMLR publisher full paper, §1, pp. 2079–2081 and §5.3, p. 2102. Model selection can overfit finite-sample assessment; a final evaluation must repeat the entire choice or use an independent test set.
- **Checked:** Stone (1974), existing bibliographic DOI record and Cawley–Talbot §1 p. 2080 and bibliography p. 2106; title/year only are used in the historical paragraph, supported by the fully read Cawley–Talbot source.
- **Checked:** Hyndman and Athanasopoulos (2021), author-published *Forecasting: Principles and Practice*, §5.10, chronological rolling-origin training and evaluation.
- **Checked:** the three bank answers `ex-sl-09-7`, `ex-sl-11-7`, `ex-sl-16-7` directly address tuning/evaluation separation, preprocessing, and early stopping.
- **Assumed:** the illustrative training, validation and test blocks are independently sampled from one target population. The numerical rates are examples, not a dataset result.
- **Disputed:** none. Dodge has no entry that resolves the origin of the validation-set method, so no origin claim is made.

## Mathematical checks

With 60 cases split 36/12/12, one versus three validation mistakes give 1/12=0.0833 and 3/12=0.25; four test mistakes give 4/12=0.3333. A fixed rule's validation mean is conditionally unbiased for its risk by independence. For several candidate rules, pointwise `min_j \hat R_j <= \hat R_k` for every k implies `E min_j \hat R_j <= min_j E\hat R_j`; this is a selection-optimism statement about the minimum noisy estimate, not a guarantee for a realized test comparison. Proved in collapsed box.
