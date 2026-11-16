# Knot

Rank 200. Type: Concept. Frozen baseline: 516 body words and zero figures. The original definition, smoothing-spline distinction, truncated-power representation, continuity statement, example, citations and linked questions remain represented. The shared spline basis, penalty-limit and natural-boundary claims were qualified in generator inputs.

## Checked

- **Checked in full repository source chapter:** `sources/book/chapters/06-smooth-means.qmd`, §§“A roughness penalty” and “Kyphosis and age”, and `article_extras.py` Knot entry around line 2001. The chapter introduces cubic smoothing splines, knots and penalty; the extra supplies the original truncated-power example.
- **Checked by proof:** One collapsed box proves continuity of a cubic truncated-power term through the second derivative, its third-derivative jump, linear independence of the unrestricted $M+4$ basis, and the slope jump of a linear truncated term.
- **Checked by code:** `checks/knot.py` evaluates the original and new worked functions, derivatives at joins, displayed values and hidden answer.
- **Assumed:** Distinct ordered knots and a function domain extending beyond the outer knots for the unrestricted dimension statement. The worked curves are illustrative, not fitted data.
- **Disputed:** The original claim of a universal ten-knot default, the suggestion that edf is a polynomial degree, and the unconditional generalized-model interpolation claim are too broad. The natural boundary dimension count in `article_extras.py` has a degenerate-case exception. These were corrected in `topics.py`, the *Smooth means* source chapter and `article_extras.py`; the one-knot natural-boundary case is now excluded from the dimension rule.

## Sources used

- Complete repository *Smooth means* chapter and original Knot extra were read to preserve baseline material; unread de Boor citations were removed from the Knot inputs. The page proves its basis and continuity claims directly; no new external citation was made to an unavailable full source.
- Dodge (2008) was searched in the authorized full text and index. Its “knot” occurrences describe dendrogram knots rather than spline knots, so no Dodge claim or citation was added to this article.

## Changes

Added spline-basis motivation, the distinction between available knots and penalised flexibility, a proof, checked cubic example and hidden practice answer, three answered bank links pending, misconceptions, failure cases and connections. No figures changed.
