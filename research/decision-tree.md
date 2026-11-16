# Decision tree

Rank 199. Type: Method. Frozen baseline: 359 body words, zero figures. The original binary-split definition, greedy local criterion, leaf proportions, majority prediction, rectangular geometry, conflicting-label caveat, citations and three linked questions remain represented.

## Checked

- **Checked in full authorized source:** Dodge (2008), printed pp. 82–83, “Classification” (`/workspace/statwiki-sources/dodge2008/pages/pdf-0088.txt` and `pdf-0089.txt`), describes partition, hierarchical and geometric classification and prediction as a use of classification. It does not develop supervised decision trees, so it is used only for this historical distinction.
- **Checked in full repository source chapter:** `sources/stat3006/chapters/sl-12-classification-trees.qmd`, §§“Building a tree”, “Node impurity”, “Choosing a split”, “Controlling the size” and worked five-point example. This supplies the fitting/validation context and preserves source material.
- **Checked by proof:** One collapsed box proves nonnegative weighted impurity reduction for concave impurity, zero majority-error improvement without majority flip, the leaf-majority optimality statement and axis-aligned geometry.
- **Checked by code:** `checks/decision-tree.py` recalculates all new printed counts, impurity values, improvements and practice values.
- **Assumed:** Finite training set, nonempty children and deterministic axis-aligned splits. The worked classification counts are constructed for illustration, not empirical clinic data.
- **Disputed:** The midpoint is merely a representative of a gap with a fixed training partition; it is not a population boundary. A pure leaf can still generalize poorly. No claim that the tree's leaf frequencies are calibrated probabilities is made.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), pp. 82–83, “Classification”, full page texts read; existing `dodge2008` key.
- The complete repository classification-tree chapter was read. Its inherited CART, ESL and ISLR citations remain attached to inherited claims; those external volumes were not available in full, so new mathematical claims are proved directly rather than citing them.

## Changes

Added a concrete motivation, split criterion, interpretive distinction between training impurity and predictive risk, proof, checked Gini example and hidden practice answer, three answered bank links pending, distinct misconceptions, limits, connections and cited historical context. No figures changed.
