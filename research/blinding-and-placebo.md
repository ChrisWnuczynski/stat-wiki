# Blinding and placebo

Rank 193. Type: Concept/design method. Frozen baseline: 504 body words, zero figures. The Alice caffeine experiment, its twenty heart-rate changes, both group means and all original links are retained.

## Checked

- **Checked in full source:** Dodge (2008), printed p. 102, “Completely Randomized Design”, defines random assignment of experimental units to treatments. The full extracted page `/workspace/statwiki-sources/dodge2008/pages/pdf-0108.txt` was read. It supports the allocation distinction but does not itself describe blinding or placebos.
- **Checked in the original source chapter:** `sources/stat1301/chapters/da-01-studies-and-data.qmd`, lines 35–75 and the Alice caffeine example. Its blinding/placebo definition and all Alice observations were read. The chapter's stronger claims about exact covariate balance and causal inference require the focused corrections in pending shared changes.
- **Checked mathematically:** The collapsed proof shows unbiasedness of the treated-minus-control mean under complete randomization for finite-population potential outcomes. `checks/blinding-and-placebo.py` recomputes the original Alice group means and every number in the added trial examples and pending bank exercise.
- **Assumed:** Well-defined assignment-level potential outcomes and complete random assignment for the proof; the numerical trial examples are hypothetical and use simple observed proportions, not confidence intervals or claims of statistical significance.
- **Disputed:** A placebo-arm improvement rate is not solely an expectancy effect; natural history and shared care also contribute. “Double blind” is underspecified without naming masked roles. Allocation concealment and post-assignment blinding are distinct. The original source chapter's categorical randomization and placebo claims need qualification.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 102, “Completely Randomized Design”; existing `dodge2008` key.
- The repository's original *Studies, data, and evidence* chapter was read to preserve its example and definitions. Its existing Fisher and MRC bibliography entries are retained, but no new statement is cited to those unread works.

## Changes

Added motivation, roles and timing of masking, a conditional assignment-effect proof, numerical masked-trial example with hidden answer, interpretation of placebo improvement, distinct misconceptions, concrete failures and design history. Three substantive answered bank questions, including the existing devil-tumours design question, are pending. Shared source corrections await integration. No figure was present.
