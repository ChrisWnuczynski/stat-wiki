# Interpretation and the decision boundary — rank 163

Type: concept. Baseline 772 words, zero figures. Preserve logistic odds interpretation, the two-class Gaussian LDA derivation, pure-prior-shift adjustment, ROC statement, all links and seven question backlinks.

## Sources opened

- James, Witten, Hastie and Tibshirani, *An Introduction to Statistical Learning*, first edition, seventh printing, complete author-publisher PDF at statlearning.com, Ch. 4 §§4.3.1–4.3.4 pp. 131–137, §§4.4.1–4.4.4 pp. 138–150, §4.5 pp. 151–152. Read log-odds/odds multiplier, logistic fitting, Bayes classification, LDA density and linear score, QDA unequal covariance, and comparison of methods.
- Msaouel et al. (2022), “Medicine before and after David Cox,” complete author manuscript hosted by PubMed Central, editorial paragraphs 2–3. Read the account of Berkson's 1944 bioassay use and Cox's 1958 binary-sequence development.
- Dodge (2008), printed p. 319, *Logistic Regression*, and p. 390, *Odds and Odds Ratio*. Read for historical context and orientation. Its p. 319 sentence describing a logistic coefficient as a “relative risk” conflicts with the exact odds-multiplier formula, and is not copied.

## Fact ledger

- **Checked:** `logit p(x)=beta0+beta'x`, and a unit increase in `x_j` at fixed other predictors multiplies odds by `exp(beta_j)` but changes probability by an amount depending on its starting point (ISLR §4.3.1 pp. 132–133; Dodge p. 319 for logit, not its risk reading).
- **Checked:** At equal misclassification costs and threshold one half, the boundary is zero linear predictor. A changed threshold gives `eta=logit(t)`; with unequal false-positive and false-negative costs and calibrated probabilities the optimal threshold is `C_FP/(C_FP+C_FN)` by direct conditional-risk comparison.
- **Checked:** Two multivariate normal classes with shared positive-definite covariance have affine posterior log odds; unequal class covariance can give quadratic boundaries (ISLR §§4.4.3–4.4.4 pp. 142–150 and §4.5 pp. 151–152). Derivation in Proof.
- **Checked:** Under pure prior shift, conditional feature densities remain stable and logit posterior changes by the difference in prior logits. ROC coordinates at a fixed score threshold are conditional tail probabilities and remain stable under that condition. Derived in Proof.
- **Checked:** All worked and Your-turn numbers recomputed in focused Python check.
- **Assumed:** The logistic scores used in decision examples are calibrated probabilities. Predictor contrasts keep the other coordinates fixed; a causal reading is not entailed.
- **Disputed:** Dodge p. 319 says the continuous-predictor coefficient reflects relative risk; this is false for the usual logistic coefficient, which is a log odds ratio. Inherited Cox and Berkson citations have no page locators on the generated page; shared source repair should add precise support when the full originals are read, while new prose cites the opened history article.
