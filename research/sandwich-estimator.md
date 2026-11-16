# Sandwich estimator — rank 168

Type: concept. Baseline 388 words, zero figures. Preserve GEE, marginal-model and working-correlation links and the warning about few/imbalanced clusters. Clarify that the quoted asymptotic guarantee requires many independent clusters and that correct working covariance gives a model-based *limit*, not exact equality of finite-sample estimates.

## Sources opened

- Huber (1967), original paper from the University of California Berkeley library's authorized symposium archive, *The Behavior of Maximum Likelihood Estimates under Nonstandard Conditions*, pp. 221–233, especially §4 and corollary p. 231: general $A^{-1}C(A^T)^{-1}$ covariance under misspecification.
- Cameron and Miller (2015), full author-hosted *Journal of Human Resources* article *A Practitioner's Guide to Cluster-Robust Inference*, §§II.A, II.C pp. 3–8, §IV p. 16 and §VI: cluster score outer products, dependence assumptions, number of clusters, finite-sample corrections, history of White and Liang–Zeger extensions.
- Dodge (2008) index checked for sandwich/robust entries; no dedicated entry. No Dodge claim made.

## Fact ledger

- **Checked:** Sandwich covariance is sensitivity inverse, score covariance, sensitivity inverse-transpose; for symmetric bread it appears as $A^{-1}BA^{-1}$ (Huber p. 231; Cameron–Miller §II.C).
- **Checked:** For OLS with independent clusters, $A=X^TX$ and empirical meat is $\sum_g X_g^T\hat u_g\hat u_g^TX_g$; a numerical four-cluster example is verified by focused script (Cameron–Miller §II.C).
- **Checked:** Working covariance misspecification can be tolerated with correct mean/exogeneity and many independent clusters; cluster dependence or a wrong mean breaks that claim. Small number or extreme imbalance of clusters undermines usual asymptotics (Cameron–Miller §§II.C, IV, VI).
- **Checked:** Huber's 1967 general misspecified-likelihood result, White's 1980 heteroskedastic formula and Liang–Zeger's 1986 correlated-data extension are distinguished using Huber original and Cameron–Miller historical account.
- **Assumed:** Clusters independent with finite score second moments and nonsingular limiting sensitivity; for OLS, conditional zero-mean errors.
- **Disputed:** Existing claim that sandwich “collapses” to inverse information when the working variance is correct is true at the population asymptotic level, not generally as equality of observed empirical and model-based matrices. Existing claim that consistency requires both number and size of clusters to grow is too strong; fixed bounded cluster sizes are standard when the number of clusters grows.
