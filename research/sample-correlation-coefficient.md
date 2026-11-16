# Sample correlation coefficient — research record

## Sources opened

- NIST, *Dataplot Reference Manual: CORRELATION*, complete official page, `https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/correlat.htm`, Description and formula; read sample coefficient and zero-correlation test statistic.
- Strimmer, *Multivariate Statistics and Machine Learning* (2025), full University of Manchester author-hosted Chapters 1–2 at `https://strimmerlab.github.io/publications/lecture-notes/MATH38161/01-multivariate.html` and `/02-estimation.html`; read covariance/correlation matrix and sample covariance sections.
- Hannay, *Introduction to Statistics and Data Science* (2019), full author-hosted Ch. 11, especially §11.4, `https://faculty.nps.edu/rbassett/_book/introduction-to-linear-regression.html`; read correlation, regression slope and $R^2$.
- Dodge (2008), authorized local PDF pp. 115–118, using `index.tsv` mapping printed p. 115 to PDF p. 121; read definition, history, sample formula, $t$ test and limits. The entry omits the normal-model condition for its exact $t$ reference, so the article states it explicitly.
- Attempted publisher DOI pages for Pearson (1896), Student (1908) and Galton (1886); full originals were inaccessible. The three correct baseline citations remain, without new claims attributed to unread text.
- Baseline has 802 words and two figures. Preserve both figures, the 20-pair test, the slope-test derivation, the heart-failure example, original infobox values and four question links.

## Claim ledger

- **Checked:** $r=S_{xy}/\sqrt{S_{xx}S_{yy}}$ with paired observations and nonzero column variation; sample covariance divisors cancel (NIST Description; Dodge p. 117).
- **Checked:** Cauchy–Schwarz bounds $r$ in $[-1,1]$; equality means centred sample vectors are nonzero proportional, so observations lie exactly on a line. Affine rescaling changes only the sign when one scale factor is negative (direct algebra; NIST Description).
- **Checked:** In intercept-only simple regression, slope $S_{xy}/S_{xx}$, $R^2=r^2$, and the slope $t$ statistic equals $r\sqrt{n-2}/\sqrt{1-r^2}$ (Hannay §11.4; direct orthogonal-sum algebra).
- **Checked:** Under independent pairs from a bivariate normal law and $\rho=0$, the statistic has an exact $t_{n-2}$ distribution for $n>2$, $|r|<1$. Conditional-on-$X$ Gaussian regression projection proves the reference law; normality is needed for this exact distribution, not for calculating $r$ (NIST Description for statistic; Dodge p. 117 for reference law, with assumption supplied in proof).
- **Checked by code:** New four-pair example has centred sums $S_{xx}=S_{yy}=5$, $S_{xy}=4$, $r=0.8$; transformed response gives $-0.8$. The five-pair curved counterexample has zero cross-product sum. The outlier calculation and preserved 20-pair test numbers are checked in `checks/sample-correlation-coefficient.py`.
- **Checked/rounding note:** The printed $r=0.438$ gives $t=2.0671$ and a two-sided $p=0.0534$ if treated as exact. The source reports $2.06$ and $0.054$, consistent with separately rounded underlying values of $r$; both give the same decision against $2.101$. Do not silently replace the preserved example.
- **Checked:** Dodge p. 116 recounts Galton's late-1880s terminology and Pearson/Edgeworth's later development. Avoid assigning the modern sample formula solely to Galton.
- **Assumed:** The new small paired sample and outlier are illustrations; no population correlation or causal claim follows from them.
- **Disputed/limited:** A low $r$ does not exclude nonlinear dependence; the zero-correlation test's familiar $t$ calibration is not exact under arbitrary nonnormal laws or nonindependent pairs. The heart-failure sample association is observational.
