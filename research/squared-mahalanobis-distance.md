# Squared Mahalanobis distance — rank 171

Type: concept. Baseline 457 words, zero figures. Preserve defining quadratic form, whitening/Cholesky interpretation, exact normal chi-square statement, diagonal $(2,0)$ versus $(0,2)$ example, sample-singularity warning and correlation-matrix qualification.

## Sources opened

- Strimmer (2025), full author-hosted licensed *Multivariate Statistics and Machine Learning*, Ch. 3 §3.1 Examples 3.7–3.9 for Mahalanobis transform, whitening and multivariate-normal density; Ch. 5 §5.3 for appearance in Gaussian discriminants.
- Dodge (2008), authorized printed pp. 324–326, “Mahalanobis Distance” and adjacent biographical entry: covariance/scale interpretation, $E(D^2)=p$, 1930 group-divergence paper and 1936 generalized-distance paper.
- Springer/Sankhya A official reprint DOI page inspected; it offers only a paywalled preview, so no mathematical claim newly cites the original text. A search result led to an unrelated official INSA PDF, which was rejected rather than used.

## Fact ledger

- **Checked:** For positive-definite covariance, $D^2=(x-\mu)^T\Sigma^{-1}(x-\mu)$ equals squared Euclidean norm after whitening and is invariant under invertible affine changes of units (Strimmer Ch. 3 §3.1; proof on page).
- **Checked:** $E(D^2)=p$ needs only finite covariance, not normality; if $X$ is nonsingular multivariate normal, $D^2\sim\chi^2_p$ (Dodge p. 325; Strimmer Ch. 3 §3.1; proof on page).
- **Checked:** Diagonal and correlated two-dimensional examples, correlation decomposition and normal contour $\chi^2$ link verified with NumPy/SciPy in focused check.
- **Checked:** Dodge pp. 324–326 distinguishes Mahalanobis's 1930 group-divergence paper from his 1936 generalized-distance paper.
- **Assumed:** The population covariance is positive definite and specified for the exact whitening/chi-square results; plugging in a sample estimate changes the reference distribution.
- **Disputed:** Existing source DOI `10.1007/s13171-019-00164-5` identifies a 2019 Sankhya A reprint, not the 1936 original's publication DOI. A generalized inverse in singular covariance measures only selected directions and is not the same full-space metric.
