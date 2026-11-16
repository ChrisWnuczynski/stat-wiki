# Leave-one-out cross-validation

Type: Concept. Rank 266. Tier: full.

## Material checked

- **Checked:** Baseline 597 words, 0 figures. ESL Ch. 7 §7.10.1, printed pp. 241–245, equations 7.48, 7.51 and 7.52: the K=n case, the linear-smoother identity, and GCV. §7.10.2, pp. 245–246, on selection before the split.
- **Checked by code:** The line through (1,1), (2,2), (3,6) is y = -2 + 2.5x, leverages 5/6, 1/3, 5/6, leave-one-out residuals 3, -1.5, 3, mean squared error 6.75 against ordinary mean squared residual 0.5. Refitting each pair matches the identity. `checks/leave-one-out-cross-validation.py`.
- **Assumed:** The identity requires a linear smoother whose operator does not depend on y, and S_ii ≠ 1.
- **Not opened:** Stone 1974. The copied chapter cites it. New sentences cite ESL.

## Sources opened

1. Hastie, Tibshirani and Friedman, ESL, Ch. 7 §7.10, pp. 241–246. Key `hastie_esl2009`.
