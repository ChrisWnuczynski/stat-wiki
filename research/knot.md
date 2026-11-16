# Knot

Rank 200. Type: Concept. Frozen baseline: 516 body words and zero figures. The original definition, smoothing-spline distinction, truncated-power representation, continuity statement, example, citations and linked questions remain represented. Several broad shared claims need qualification through pending changes.

## Checked

- **Checked in full repository source chapter:** `sources/book/chapters/06-smooth-means.qmd`, §§“A roughness penalty” and “Kyphosis and age”, and `article_extras.py` Knot entry around line 2001. The chapter introduces cubic smoothing splines, knots and penalty; the extra supplies the original truncated-power example.
- **Checked by proof:** One collapsed box proves continuity of a cubic truncated-power term through the second derivative, its third-derivative jump, linear independence of the unrestricted $M+4$ basis, and the slope jump of a linear truncated term.
- **Checked by code:** `checks/knot.py` evaluates the original and new worked functions, derivatives at joins, displayed values and hidden answer.
- **Assumed:** Distinct ordered knots and a function domain extending beyond the outer knots for the unrestricted dimension statement. The worked curves are illustrative, not fitted data.
- **Disputed:** The original claim of a universal ten-knot default, the suggestion that edf is a polynomial degree, and the unconditional generalized-model interpolation claim are too broad. The natural boundary dimension count in `article_extras.py` has a degenerate-case exception. These are recorded as precise pending shared changes.

## Sources used

- Complete repository *Smooth means* chapter and original Knot extra were read to preserve baseline material; inherited Wood, de Boor, Wahba, Green–Silverman and Reinsch citations stay with original source-derived claims. No new citation is made to an external volume that was unavailable in full.
- Dodge (2008) was searched in the authorized full text and index. Its “knot” occurrences describe dendrogram knots rather than spline knots, so no Dodge claim or citation was added to this article.

## Changes

Added spline-basis motivation, the distinction between available knots and penalised flexibility, a proof, checked cubic example and hidden practice answer, three answered bank links pending, misconceptions, failure cases and connections. No figures changed.
