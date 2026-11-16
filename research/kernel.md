# Kernel — rank 97

Type: concept. Baseline 488 words, no figures. Preserve the feature-map definition, quadratic example, invalid negative-dot-product example, infobox, citations and links. New content gives the complete finite-Gram/feature-space equivalence in one collapsed proof, a separate Gaussian numeric example, hidden Your turn, two bank checks and historical context.

## Sources opened

- **Checked:** Schölkopf and Smola (2003), full author-hosted chapter “A Short Introduction to Learning with Kernels,” §§4, 6–9, pp. 48–62. It derives kernelized SVM prediction, polynomial features, the Gram criterion and feature-space construction, Gaussian kernels and its integral-operator term history. Publication metadata verified against Springer/MPG records.
- **Checked:** Mercer (1909), full original Royal Society memoir in a University of Southern California faculty-hosted scan, pp. 415–446. The introduction (p. 415) states the positive/negative-type eigenfunction expansion proved in Part IV. This is the substantive paper for the named eigen-expansion, not the two-page Proceedings notice currently represented by `mercer1909`.
- **Checked:** Boser, Guyon and Vapnik (1992), original conference paper bibliography/abstract at ML Anthology; the full PDF link was inaccessible, so historical prose cites the fully read Schölkopf–Smola account rather than citing the original's abstract.
- **Checked:** authorized Dodge (2008) index; no entry on feature-space kernels, only unrelated kernel PLSR material. It was not cited.
- **Checked:** answered bank items `ex-sl-17-7` (overfit Gaussian SVM) and `ex-sl-17-10` (XOR feature map), both directly exercise this page's kernel meaning and differ from the embedded quadratic example.
- **Assumed:** the Gaussian worked example uses the standard positive-definite radial kernel from Schölkopf–Smola §8. The two-point Gram test itself cannot establish validity for every finite input set.
- **Disputed:** the inherited Interpretation calls a feature kernel “a covariance of features”; an arbitrary uncentered inner product need not equal their covariance. It also links the word “kernel” in its own definition to the KDE page because of term-linking ambiguity. Both shared-source corrections are recorded in pending. The bibliography key `mercer1909` currently identifies a two-page Proceedings notice, while the full substantive memoir read here is in *Philosophical Transactions* 209:415–446, DOI 10.1098/rsta.1909.0016. The named expansion now has a precise `mercer1909` locator, and the shared bibliography entry must be corrected before integration.

## Mathematical checks

For the Gaussian kernel at 0,1 with gamma=ln2, Gram matrix [[1,.5],[.5,1]], eigenvalues 1.5,.5 and determinant .75. For (1+xz)^2 at 0,1, Gram [[1,1],[1,4]], determinant3 and eigenvalues (5±sqrt13)/2≈4.302776,.697224. The explicit feature map (1,sqrt2 x,x²) verifies global positive semidefiniteness. For the linear kernel at -1,1, the off-diagonal value is -1 but eigenvalues are 0,2. The source quadratic map gives K((1,1),(2,0))=4. All checked with NumPy and SymPy in the focused check.
