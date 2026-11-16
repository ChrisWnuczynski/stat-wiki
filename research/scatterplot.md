# Scatterplot — research record

## Sources opened

- NIST/SEMATECH e-Handbook of Statistical Methods, §1.3.3.26, full official webpage, `https://www.itl.nist.gov/div898/handbook/eda/section3/eda33q.htm`; opened and read its definition, questions, examples, causality warning, and display advice. Its linked §§1.3.3.26.5, 1.3.3.26.10, and 1.3.3.26.11 were also opened for nonlinear patterns, outliers, and scatterplot matrices.
- Dodge (2008), *The Concise Encyclopedia of Statistics*, printed p. 475, full entry "Scatterplot" in the authorized local source, PDF page 473.
- Existing generated article and course material, including the five-point parabola, discrete jitter, citations and question link, compared with `research/baseline.json` (477 words, zero figures).

## Claim ledger

- **Checked:** A scatterplot places corresponding quantitative pairs on horizontal and vertical axes, generally explanatory X and response Y (NIST §1.3.3.26; Dodge p. 475).
- **Checked:** It exposes straight and curved patterns, changing spread, and outliers; the NIST page expressly warns that a visible association cannot by itself prove causation (NIST §1.3.3.26).
- **Checked:** The NIST linked quadratic and outlier examples show why a straight-line summary can mislead (§§1.3.3.26.5 and .10). Dodge also recommends scatterplots before selecting a regression model and for residual analysis (p. 475).
- **Checked by algebra and code:** For x=(-2,-1,0,1,2), y=x², the centered cross-product sum is zero while the relationship is exact. The worked five-point and Your turn arithmetic is verified in `checks/scatterplot.py`.
- **Checked:** Coincident discrete pairs are hidden by overplotting; display-only jitter changes the drawn coordinates, not the measurements. This is a direct geometric consequence of point plotting; no external historical claim is attached.
- **Assumed:** The drawn weather, dose, or height examples are illustrative measurements, not claims about an actual sampled population.
- **Disputed/limited:** An extreme point is not automatically a bad record; NIST's example discusses exclusion for a point from another model, but that judgment cannot be transferred to an arbitrary dataset without checking provenance.

No new mathematical theorem is stated. The only algebraic relationship used for the zero-correlation example is derived in the article's single collapsed Proof box.
