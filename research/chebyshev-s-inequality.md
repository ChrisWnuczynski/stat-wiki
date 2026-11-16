# Chebyshev's inequality

Rank 194. Type: Theorem/topic. Frozen baseline: 427 body words and zero figures. The original bound, Markov connection, weak-law relation, citations and question links remain.

## Checked

- **Checked in full source:** Dodge (2008), printed p. 68, “Chebyshev, Pafnutii Lvovich”, identifies the Bienaymé–Chebyshev name, the earlier Bienaymé article and Chebyshev's 1867 French publication. The complete extracted page `/workspace/statwiki-sources/dodge2008/pages/pdf-0074.txt` was read. The original 1867 paper was not accessible, so the added historical statement cites Dodge rather than the unread paper.
- **Checked in the repository source chapter:** `sources/stat2003/chapters/prob-05-transforms-and-limits.qmd`, lines 196–220, states the variance bound and its weak-law application. The generated page's original formulas were preserved.
- **Checked by proof:** The single collapsed box derives Chebyshev from Markov, verifies a three-point equality case, and derives the finite-variance independent-sample weak law. No unproved new theorem remains.
- **Checked by code:** `checks/chebyshev-s-inequality.py` verifies bottle, three-point, sample-average, normal-tail and pending bank calculations.
- **Assumed:** Finite mean and variance for the bound; independent identically distributed finite-variance observations only for the $1/n$ average-variance formula, not for Chebyshev itself.
- **Disputed:** Treating a bound as an actual tail probability is incorrect. Normal 95% folklore cannot replace the distribution-free 75% bound at two standard deviations. The exact historical priority between Bienaymé and Chebyshev was not reconstructed from their original papers; Dodge's secondary account is cited narrowly.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 68, Chebyshev biographical entry; existing `dodge2008` key.
- The repository probability chapter was read for the pre-existing mathematical baseline. The original paper and standard textbook citations in that baseline are retained; the new proof and historical paragraph do not cite unread full texts.

## Changes

Added motivation, exact threshold interpretation, sharpness construction, a proof including the weak-law application, numerical worked and hidden examples, distinct misconceptions, concrete failures and sourced history. One existing answered bank problem plus one new sample-size question are pending for self-checks. No figures changed.
