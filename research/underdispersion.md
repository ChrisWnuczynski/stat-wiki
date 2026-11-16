# Underdispersion

Rank 192. Type: Concept. Frozen baseline: 368 body words and zero figures. The existing bids-for-a-bankrupt-firm context, Poisson/quasi-Poisson/CMP relationships, citations and question link are retained.

## Checked

- **Checked in full source:** Dodge (2008), printed p. 341, “Measure of Dispersion”, explains why variability complements a measure of central tendency. The full extracted page `/workspace/statwiki-sources/dodge2008/pages/pdf-0341.txt` was read. It supports the motivation and background only, not GLM-specific formulas.
- **Checked in repository source chapters:** `sources/book/chapters/02-inference-and-counts.qmd` for the quasi-Poisson multiplier and `03-gamma-and-quasi.qmd`, lines 1–40, for the bids example and Conway–Maxwell–Poisson convention. The original fitted bids coefficients cannot be recomputed because the raw bid data and MATLAB fit are unavailable in this worktree.
- **Checked by derivation:** The binomial variance-to-mean ratio and Pearson estimate for an intercept-only Poisson fit are proved in the collapsed box. Python checks the worked ten-count data, Poisson(7) probability over 3–13, binomial practice and pooled-vs-conditional bank exercise.
- **Assumed:** The ten worked counts are independent comparable units with one common fitted mean. A Pearson dispersion ratio is interpreted descriptively rather than as a small-sample significance test.
- **Disputed:** The topic definition's claim that underdispersion is “rarer” than overdispersion is unsupported without a population of processes. Its phrase “for counts a variance below the mean” is Poisson-specific. Both require a focused `topics.py` shared correction (pending). The source chapter's description of firms with fitted mean 7 mostly producing 6–8 could not be reconstructed from data; the mathematical Poisson comparison was checked.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 341, “Measure of Dispersion”; existing `dodge2008` key.
- The original repository GLM book chapters were read and their existing supported citations retained. The new mathematical claims are derived on the page rather than ascribed to unread external papers.

## Changes

Added motivation, a conditional definition, diagnostic interpretation, a numerical example, hidden practice, three distinct answered bank questions (one existing), a collapsed proof, counterexamples, connections and context for dispersion's development. The lead and shared topic wording change are pending integration. No figure was added or removed.
