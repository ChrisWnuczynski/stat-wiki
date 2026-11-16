# Within-cluster scatter

Rank 198. Type: Concept/criterion. Frozen baseline: 746 body words and zero figures. The full original pairwise identity, unequal cluster-size weighting, distinction from Lloyd's objective, Stirling counts, citations and two question links are preserved.

## Checked

- **Checked in full source:** Dodge (2008), printed p. 83, “Cluster Analysis”, describes grouping by measured similarity and cites Tryon's 1939 *Cluster Analysis*. The complete extracted page `/workspace/statwiki-sources/dodge2008/pages/pdf-0089.txt` was read. It supports historical context only, not the weighted scatter identity.
- **Checked in original repository source chapter:** `sources/stat3006/chapters/sl-04-kmeans.qmd`, §§“Within-cluster scatter” and “Lloyd's algorithm”, lines 23–125. The chapter distinguishes the pairwise $W$ from ordinary unweighted K-means $\widetilde W$. Its later partition-enumeration paragraph should repeat that distinction (pending shared fix).
- **Checked by proof:** One collapsed box proves centering/mean optimality, the pairwise identity, monotonicity under cluster refinement and the Stirling inclusion–exclusion formula. The numerical counterexample verifies that Lloyd-style reassignment can lower ordinary scatter while raising weighted pairwise scatter.
- **Checked by code:** `checks/within-cluster-scatter.py` recalculates the original Stirling values and all new cluster-centre, pairwise, Lloyd counterexample, scale and practice numbers.
- **Assumed:** Nonempty finite clusters, ordinary squared Euclidean distance, and given assignments when computing either scatter. Comparing scores requires the same feature scaling and objective definition.
- **Disputed:** The existing generic lead describes only distances to centres, which omits the cluster-size weighting of the page's defined $W$. The pending lead names pairwise within-group separation. Lloyd's algorithm is not an optimizer of this $W$ in general; the source chapter's enumeration transition needs clarification.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 83, “Cluster Analysis”; existing `dodge2008` key for historical context.
- The repository's complete K-means source section was read to preserve the mathematical baseline. Existing HTF, MacQueen and Lloyd citations remain in their source-derived paragraphs; the new identities are proved rather than attributed to unopened papers.

## Changes

Added motivation, explicit distinction between pairwise and software objectives, a proof of the original formula, two checked numerical examples including a counterexample to weighted descent, hidden Your turn answer, misconceptions, concrete limits, connections and cited history. Two existing answered questions are pending as self-checks. No figures changed.
