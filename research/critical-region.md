# Critical region — rank 102

Type: concept. Frozen baseline 723 words, one figure. The source definition, caffeine and tuning-fork examples, blood-pressure question, figure, infobox and citations remain generated.

## Sources read

- **Checked:** NIST/SEMATECH, *e-Handbook of Statistical Methods*, §7.2.2 “Are the data consistent with the assumed process mean?”, §7.2.2.1 “Confidence interval approach” and §7.2.2.2 “Sample sizes required”, official public pages at https://www.itl.nist.gov/div898/handbook/prc/section2/prc22.htm and adjacent URLs. The one- and two-sided $t$ and $z$ critical-value formulas, null reference law, tail allocation and roles of alpha and beta are explicit.
- **Checked:** Dodge, *The Concise Encyclopedia of Statistics* (2008), printed pp. 1 and 452–454, “Acceptance Region” and “Rejection Region”. The scan's columns are scrambled by OCR on p. 453, so the left-tail display is checked against NIST rather than repeated verbatim.
- **Checked by code:** `checks/critical-region.py` evaluates binomial tail sizes for the new examples and serve question; normal and Student cutoffs and probabilities; inherited caffeine, fork and blood-pressure values.
- **Assumed:** The binomial worked and practice examples assume independent equal-probability trials. The standard-normal and Student rules require their stated sampling models.
- **Disputed:** Dodge's OCR left-tail text appears in the right-tail column; no claim depends on that line. Existing source citations to Neyman–Pearson, Lehmann–Romano and Casella–Berger are retained, but these books/paper were not newly verified in full and are not used for new citations.

## Proof and bank

One collapsed proof establishes monotonicity of rejection probability under nested regions and explains exact versus conservative size. Answered bank questions selected: `ex-inf-np-critical`, `ex-inf-serve-power`, `ex-inf-ump-two-sided`. They use settings distinct from the embedded blood-pressure, caffeine and fork examples.
