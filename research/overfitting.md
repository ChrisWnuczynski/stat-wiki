# Overfitting research notes

Type: concept. Baseline: 456 words, no figures. The original generator supplies the interpolation intuition, training/held-out gap $0.02$ versus $0.18$, and three safeguards. These remain in the generated page. The depth text supplies a bias–variance proof, exact numeric illustration, leakage failure cases and test-set workflow.

## Sources opened

- James, Witten, Hastie and Tibshirani, *An Introduction to Statistical Learning* (2013), author-hosted full first-edition PDF, https://www.statlearning.com/s/ISLRSeventhPrinting.pdf. Read Ch. 2 §2.2.1 pp. 30–34 and §2.2.2 pp. 34–36, plus Ch. 5 §5.1. Checked training versus test MSE, the definition of overfitting relative to a less flexible alternative, the test-error curve, cross-validation, and the bias–variance decomposition in equation 2.7. The 2013 edition receives its own pending bibliography key; the existing 2021 key is not used for the 2013 text.
- Google for Developers, *Machine Learning Crash Course*, “Overfitting,” full online page, https://developers.google.com/machine-learning/crash-course/overfitting/overfitting. Checked training/validation loss divergence and the need for representative partitions.
- Google for Developers, *Machine Learning Crash Course*, “Overfitting: L2 regularization,” full online page, https://developers.google.com/machine-learning/crash-course/overfitting/regularization. Checked penalty and early-stopping description.
- Dodge index searched for “Overfitting”; no direct entry. No Dodge historical claim made.

## Fact ledger

- **Checked:** A smaller training MSE than test MSE is ordinary; overfitting specifically involves a procedure with inferior new-data performance to an appropriate less flexible alternative. ISLR Ch. 2 p. 33.
- **Checked:** For nested model classes under global empirical minimization, minimum training loss is nonincreasing; algebra in the collapsed proof.
- **Checked:** Expected squared prediction error separates into squared bias, fitted-prediction variance and independent test-noise variance; derived in the collapsed proof and matched to ISLR equation 2.7.
- **Checked:** Three-point interpolation and constant-predictor MSE values recomputed in `checks/overfitting.py`.
- **Assumed:** The illustrative underlying function is flat near zero and the held-out outcome happens to be zero. This is a counterexample, not a claim about an empirical dataset or expected risk.
- **Disputed:** A U-shaped test-error curve is a useful textbook pattern but not universal for every parameterization and sample. The page explicitly avoids claiming it as a universal finite-sample law.

## Bank selection

`ex-sl-09-6` asks why a selected minimum cross-validation score is optimistic; `ex-sl-09-7` tests the independent training/validation/test workflow; `ex-sl-16-7` tests early stopping and penalization for a network. All have worked answers and are distinct from the page's quadratic illustration.
