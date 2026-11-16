# Eigenvalues and eigenvectors

Type: Concept/topic. Rank 40.

## Material checked

- Frozen baseline: 696 body words and no figures. The inherited page includes the matrix equation, the principal-component Lagrange multiplier passage, the normal-density ellipsoid derivation, the squared Mahalanobis distance block, and 15 distinct question links.
- Read the PCA derivation and reconstruction discussion in `sources/stat3006/chapters/sl-03-principal-components.qmd`, the normal ellipsoid and covariance material in `sources/stat3006/chapters/sl-01-multivariate-normal.qmd`, and the completed Positive definite matrix and Multivariate normal distribution research pages. The old prose treats eigendirections mainly as intermediate steps in those two applications; it lacks a general explanation and numerical practice.

## Sources opened and used

1. Korbinian Strimmer, [*Multivariate Statistics and Machine Learning*](https://strimmerlab.github.io/publications/lecture-notes/MATH38161/), University of Manchester author-hosted notes. Opened Chapter 1 §1.1, “Eigenvalue decomposition of the covariance matrix,” for spectral decomposition, covariance positivity, inverse and eigenvalues; Chapter 1 §1.3 for normal-density contours and ellipse axes; Chapter 3 §§3.1, 3.4–3.5 for orthogonal transformation, whitening, PCA scores, variance fractions, SVD and the Pearson/Hotelling history. Existing key `strimmer2025_mva`.
2. I. T. Jolliffe, [*Principal Component Analysis*](https://link.springer.com/book/10.1007/978-1-4757-1904-8), Springer, 1986. Opened the publisher synopsis, which describes Pearson's 1901 introduction and Hotelling's independent 1933 development, and confirms the eigenvalue problem at the heart of PCA. The research prose uses Strimmer's located §3.5 for these claims; no new bibliography entry or citation to Jolliffe was needed.

No new bibliography link points to an unauthorised copy.

## Changes and checks

- Added a motivating data-cloud example, the general eigenpair definition, spectral and variance properties, a complete collapsed proof, PCA and covariance uses, a numerical worked example, a hidden “Your turn” answer, misconceptions, limitations, connections, and a sourced history limited to the statistical use of eigenvalues in PCA.
- The proof derives covariance nonnegativity, trace, determinant, matrix inverse and square root, Rayleigh maximum, rotated-score covariance and normal contour axes from orthogonal diagonalisation. It explicitly distinguishes the symmetric-matrix argument from general square matrices.
- Replaced bibliography-only markers in the shared PCA stationary-point sentence and the multivariate-normal ellipsoid, Mahalanobis and chi-squared passages with citations to opened Strimmer sections and examples. Dependent pages are regenerated and checked for content retention.
- Preserved the inherited equation, PCA and Mahalanobis passages, all 15 question links and the zero-figure count. Added two answered bank questions in a collapsed “Check yourself” section. The page check asserts printed values against exact arithmetic, proof and link retention.

## Verification

The generator completed 718 articles and 557 questions. The generated page has 3,168 body words versus 696 before, no figures before or after, one collapsed proof, 15 distinct question links, and two embedded self-checks with hidden answers. The numerical page check, 67 Python tests, offline verification of 428 bibliography entries, and overview link check pass. The dependent Squared Mahalanobis distance page now has one inline citation to the opened source; its later depth pass is recorded in `citations-todo.md`. A full HTML render is unavailable because Quarto is not installed in this workspace; the generator uses the Pandoc shim for its conversion step.
