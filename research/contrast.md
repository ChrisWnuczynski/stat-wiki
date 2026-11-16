# Contrast — research record

## Sources opened

- NIST/SEMATECH e-Handbook, official full §7.4.3.6 on factor-level means, contrast definition, unbiased estimate, variance, t interval and numerical example. Also opened official §7.4.7.2 on simultaneous Scheffé intervals.
- Dodge (2008), *Concise Encyclopedia of Statistics*, full local entry "Contrast", printed p. 113 (PDF page 119), including history and unequal-group weighting when treatment totals rather than means are parameterized.
- Generated article and course examples, including two five-variety corn comparisons and both linked questions, compared to baseline (552 words, no figures).

## Claim ledger

- **Checked:** For coefficients of treatment *means*, the contrast condition is sum of coefficients zero; it removes a common additive shift (NIST §7.4.3.6). Dodge p. 113 writes a weighted condition for coefficients of *treatment totals*, which is consistent after changing parameterization.
- **Checked:** Independent group means with common within-group variance give unbiased contrast estimate and variance $\sigma^2\sum c_j^2/n_j$ (NIST §7.4.3.6). Normal independent errors and pooled MSE give a t or squared F calibration.
- **Checked:** An unadjusted single-contrast interval is distinct from a simultaneous interval over all possible contrasts; NIST §7.4.7.2 describes Scheffé's method.
- **Checked by code:** Existing corn contrast numbers and new worked example are recomputed in `checks/contrast.py`. The displayed corn p-values are checked numerically with SciPy.
- **Checked:** Orthogonality for unequal sample sizes uses $\sum c_jd_j/n_j=0$ because this is proportional to the covariance of the two estimated contrasts; simple coefficient dot product suffices for equal group sizes.
- **Assumed:** The fresh worked three-group means are illustrative, with independent equal-variance normal errors and an MSE supplied for arithmetic.
- **Disputed:** Dodge p. 113 attributes first simultaneous estimation of all contrasts to Tukey; NIST distinguishes Scheffé's all-contrast method from Tukey's pairwise method. The article describes the development without repeating the disputed priority attribution.
- **Correction requested:** Stock Definition prose says a contrast "has to" be chosen before seeing data and that data-selected contrasts "do not keep" the null distribution. A fixed contrast retains its stated fixed-comparison null law; the *selection procedure* changes the calibration when the same data chose it. Root should revise the stock/source-chapter wording accordingly, retaining the corn arithmetic and examples.
