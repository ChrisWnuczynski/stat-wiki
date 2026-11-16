# Pooled variance

Type: Concept/definition. Rank 248. Tier: full.

## Material checked

- **Checked:** Frozen baseline 602 body words and no figures. The definition, the two-sample $t$ pivot, and the safety-programme interval remain in the generated page because they are copied from the inference chapter.
- **Checked:** Dodge, pp. 427–428, gives the degrees-of-freedom formula and the computer-brand calculation with sums of squares 95000 and 70000. Siegrist §6.08 states the pooled estimator, the chi-squared sum, independence of means and variances, and the $t_{m+n-2}$ ratio, and requires a common standard deviation. NIST §1.3.5.2 was read for the general $t$ interval that uses a single scale estimate.
- **Checked by code:** `checks/pooled-variance.py` recomputes every new printed value, including 13750, 63.328, 19.214, 9.250, 201.65, and the $F$ interval endpoints 0.5518 and 1.7131.
- **Assumed:** Exact chi-squared and $t$ laws need independent normal samples. Unbiasedness of $s_p^2$ for one $\sigma^2$ needs that common variance.
- **Disputed:** Nothing in the new numerical example. The chapter's safety interval prints a margin 5.64; that figure was left as chapter text and was not recomputed into the new prose.

## Sources opened and used

1. Yadolah Dodge, *The Concise Encyclopedia of Statistics*, Springer, 2008, pp. 427–428, local extract `pdf-0425.txt` and `pdf-0426.txt`. Key `dodge2008`.
2. Kyle Siegrist, *Special Properties of Normal Samples*, §6.08, LibreTexts, opened at the two-sample section. Key `siegrist2022_normals`.
3. NIST/SEMATECH e-Handbook, §1.3.5.2, opened in full. Key `nist_mean_limits2002`.

## Changes and checks

Research prose is about 2000 words. One collapsed proof covers the chi-squared sum, unbiasedness, and the two-sample $t$ ratio. Practice has one hidden “Your turn” and two bank-linked checks. No figure was added. Fisher 1925 and Casella–Berger are cited in the copied chapter text; those books were not reopened for the new paragraphs, so the new paragraphs do not cite them.
