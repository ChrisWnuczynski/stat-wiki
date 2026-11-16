# Residual deviance

Rank 202. Type: Concept/diagnostic. Frozen baseline: 354 body words and zero figures. The residual-deviance formula, Gaussian and Poisson cases, wafer example, R documentation citations, infobox and three linked questions remain represented.

## Checked

- **Checked in full authorized source:** Dodge (2008), printed pp. 309–310, “Likelihood Ratio Test”, `/workspace/statwiki-sources/dodge2008/pages/pdf-0310.txt` and `pdf-0311.txt`, describes likelihood comparisons and attributes the early hypothesis-testing approach to Neyman and Pearson (1928). Its apparently incorrect Wilks year is not repeated.
- **Checked in full repository source chapter:** `sources/book/chapters/05-comparisons-and-deviance.qmd`, §§“Deviance”, “Analysis of deviance” and “Residuals are not y−μ”, including the wafer comparison. The source supports the preserved examples and GLM context.
- **Checked by proof:** One collapsed box derives Poisson, Bernoulli, grouped-binomial and Gaussian deviance contributions, their nonnegativity where stated, and the nested-model likelihood-ratio identity.
- **Checked by code:** `checks/residual-deviance.py` recomputes the Poisson group-model and intercept-only numbers, binary practice contributions, and original rounded wafer arithmetic.
- **Assumed:** Independent observations under the stated likelihood, comparable response data for nested model subtraction, and full-rank design for the simple $n-p$ degree-of-freedom count. New counts are constructed examples.
- **Disputed:** The source's wafer values are rounded: $0.0255/4$ divided by $0.0084$ gives $F\approx0.759$ and p≈0.685, so the printed p=0.68 cannot be recovered exactly from these rounded values. It is retained as the reported source output. A blanket chi-squared residual-deviance goodness-of-fit rule for sparse binary outcomes is rejected.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), pp. 309–310, “Likelihood Ratio Test”, complete extracted pages read; existing `dodge2008` key.
- The complete relevant repository deviance chapter was read. Inherited R documentation and McCullagh citations stay with original source-derived statements; new formulas are derived rather than citing inaccessible external works.

## Changes

Added an explanatory lead request, motivation, family-specific deviance formulas, proof, interpretation of signed deviance residuals and fit calibration, checked Poisson worked example, hidden binary practice answer, three answered bank questions pending, distinct misconceptions, concrete failure cases, connections and cited history. No figures changed.
