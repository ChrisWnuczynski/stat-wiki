# Nested cross-validation

Type: Concept. Rank 267. Tier: full.

## Material checked

- **Checked:** Baseline 651 words, 0 figures. Cawley and Talbot, JMLR 11 (2010), pp. 2079–2080 (§1): selection bias from optimising a cross-validation score, and nested cross-validation as the remedy. ESL §7.10.2, pp. 245–246, on screening before cross-validation; §7.10.1, pp. 242–243, on learning-curve bias of smaller training sets.
- **Checked by code:** Constants 0, 1 and 4 on responses 0, 1, 0, 8 have mean squared errors 16.25, 12.75 and 14.25. The outer scores are 64, 16, 16 and 9, averaging 26.25. `checks/nested-cross-validation.py`.
- **Assumed:** The expectation inequality uses only that a minimum is smaller than each candidate. It does not estimate the error of the full-sample deployed fit.
- **Not recomputed:** ESL’s reported simulation with cross-validated error near zero and true error one half. That simulation is cited only as their reported design, and the precise 3% figure is not reprinted.

## Sources opened

1. Gavin C. Cawley and Nicola L. C. Talbot, “On over-fitting in model selection and subsequent selection bias in performance evaluation”, *JMLR* 11 (2010), pp. 2079–2080. Key `cawley_talbot2010`. JMLR PDF.
2. Hastie, Tibshirani and Friedman, ESL, Ch. 7 §7.10, pp. 241–246. Key `hastie_esl2009`.
